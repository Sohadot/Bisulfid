#!/usr/bin/env python3
"""build.py — Sovereign build engine for bisulfid.com (Sprint 6M-A).

Governed, fail-closed static build orchestrator. Reads route governance from
main/data/routes.json and build config from main/config/build.json.

Default invocation performs no file writes. Use explicit flags for output.

Modes:
  --dry-run       Inspect routes, templates, and output plan (default action)
  --sample N      Plan a controlled sample of N routes (no HTML in locked posture)
  --strict        Fail closed on validation errors
  --write-build-status  Write site/build-status.json audit artifact only

Does not generate public HTML unless publication gates explicitly allow it.
Does not modify routes, content, sources, claims, or registries.
Python standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "main/config/build.json"
ROUTES_PATH = ROOT / "main/data/routes.json"
SITEMAP_PATH = ROOT / "main/data/sitemap_policy.json"
NAV_PATHS = (ROOT / "main/data/navigation.json", ROOT / "main/config/navigation.json")
DEFAULT_SITE_DIR = ROOT / "site"
AUDIT_REPORT_DIR = ROOT / "main/data"

REQUIRED_ROUTE_FIELDS = (
    "route_id",
    "path",
    "language",
    "title",
    "template",
    "content_file",
    "status",
    "indexable",
    "in_sitemap",
    "in_navigation",
)

TEMPLATE_GOVERNANCE_MARKERS = (
    "SKELETON TEMPLATE",
    "Do not generate",
    "Do not render",
    "Quality Gate",
)

BASE_REQUIRED_SLOTS = (
    "{{head}}",
    "{{nav}}",
    "{{content}}",
    "{{footer}}",
    "{{language}}",
    "{{text_direction}}",
)

PARTIAL_HEAD_MARKERS = ("{{robots_directive}}", "charset", "viewport")
PARTIAL_FOOTER_PATH = ROOT / "main/templates/partials/footer.html"
PARTIAL_SOURCE_BAR_PATH = ROOT / "main/templates/partials/source_bar.html"
PARTIAL_INTERNAL_LINKS_PATH = ROOT / "main/templates/partials/internal_links.html"

PLACEHOLDER_SIZE_THRESHOLD = 800  # bytes; skeleton templates are intentionally small


@dataclass
class TemplateCheck:
    path: str
    exists: bool
    size_bytes: int = 0
    placeholder_like: bool = False
    missing_blocks: list[str] = field(default_factory=list)
    governance_present: bool = False
    issues: list[str] = field(default_factory=list)


@dataclass
class RouteAssessment:
    route_id: str
    path: str
    eligibility_class: str
    block_reasons: list[str] = field(default_factory=list)
    output_path: str = ""
    robots_directive: str = "noindex, nofollow"
    would_sitemap: bool = False
    would_navigation: bool = False
    would_index: bool = False
    selected_for_sample: bool = False


@dataclass
class BuildAudit:
    mode: str
    timestamp_utc: str
    route_count: int = 0
    draft_backed_count: int = 0
    missing_draft_count: int = 0
    eligible_render_count: int = 0
    blocked_count: int = 0
    non_public_count: int = 0
    non_indexable_count: int = 0
    out_of_sitemap_count: int = 0
    out_of_navigation_count: int = 0
    sample_planned_count: int = 0
    publication_lock: str = "LOCKED"
    indexation_lock: str = "LOCKED"
    sitemap_lock: str = "LOCKED"
    navigation_lock: str = "LOCKED"
    production_can_safely_proceed: str = "no"
    public_html_generated: int = 0
    sitemap_generated: bool = False
    navigation_generated: bool = False
    strict_errors: list[str] = field(default_factory=list)
    content_alignment_warnings: list[str] = field(default_factory=list)
    content_alignment_checked: int = 0
    template_checks: list[TemplateCheck] = field(default_factory=list)
    route_assessments: list[RouteAssessment] = field(default_factory=list)
    output_plan_notes: list[str] = field(default_factory=list)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def route_output_path(route: dict[str, Any], output_dir: Path) -> str:
    raw = route.get("path", "/").strip("/")
    if not raw:
        rel = "index.html"
    else:
        rel = f"{raw}/index.html"
    return str(output_dir / rel).replace("\\", "/")


def global_sitemap_allowed() -> tuple[bool, str]:
    if not SITEMAP_PATH.exists():
        return False, "sitemap_policy.json missing"
    policy = load_json(SITEMAP_PATH)
    status = policy.get("status", "inactive")
    urls = policy.get("urls") or []
    if status not in ("active", "published"):
        return False, f"sitemap_policy status={status!r}"
    if not urls:
        return False, "sitemap_policy.urls empty"
    return True, "sitemap gate open"


def global_navigation_allowed() -> tuple[bool, str]:
    for nav_path in NAV_PATHS:
        if nav_path.exists():
            nav = load_json(nav_path)
            status = nav.get("status", "inactive")
            items = nav.get("items") or []
            if status in ("active", "published") and items:
                return True, f"{nav_path.name} active with items"
            return False, f"{nav_path.name} status={status!r}, items={len(items)}"
    return False, "navigation config missing"


def assess_template(templates_root: Path, template_name: str) -> TemplateCheck:
    rel = template_name.replace("\\", "/")
    path = templates_root / rel
    check = TemplateCheck(path=str(path.relative_to(ROOT)), exists=path.is_file())
    if not check.exists:
        check.issues.append("template file missing")
        return check

    text = path.read_text(encoding="utf-8")
    check.size_bytes = len(text.encode("utf-8"))
    check.placeholder_like = check.size_bytes < PLACEHOLDER_SIZE_THRESHOLD
    check.governance_present = any(m in text for m in TEMPLATE_GOVERNANCE_MARKERS)

    if rel == "base.html":
        for slot in BASE_REQUIRED_SLOTS:
            if slot not in text:
                check.missing_blocks.append(slot)
    elif rel.startswith("partials/"):
        pass  # partials are fragments; content-body slot not required
    elif rel.endswith(".html"):
        if "{{content}}" not in text and "SLOT:" not in text and "{{source_bar}}" not in text:
            check.missing_blocks.append("content body slot")
        if "{{source_bar}}" not in text and "source_bar" not in text:
            if route_layer_needs_source_bar(rel):
                has_governance = "{{acquisition_disclaimer}}" in text or "disclaimer" in text.lower()
                if not has_governance:
                    check.missing_blocks.append("source/governance partial slot")

    if check.placeholder_like:
        check.issues.append("template appears placeholder-like (below size threshold)")
    if check.missing_blocks:
        check.issues.append(f"missing blocks: {', '.join(check.missing_blocks)}")
    if not check.governance_present and rel != "partials/nav.html":
        check.issues.append("missing governance/skeleton markers")

    return check


def route_layer_needs_source_bar(template_name: str) -> bool:
    return template_name in (
        "term_page.html",
        "reference_page.html",
        "glossary.html",
    )


def validate_required_metadata(route: dict[str, Any]) -> list[str]:
    missing = [f for f in REQUIRED_ROUTE_FIELDS if f not in route or route[f] in (None, "")]
    if missing:
        return [f"missing required metadata: {', '.join(missing)}"]
    return []


def unsafe_flag_errors(route: dict[str, Any], build_config: dict[str, Any]) -> list[str]:
    rid = route["route_id"]
    status = route.get("status")
    errors: list[str] = []

    if route.get("indexable") is True and status != "published":
        errors.append(f"{rid}: indexable=true while status={status!r}")
    if route.get("in_sitemap") is True and status != "published":
        errors.append(f"{rid}: in_sitemap=true while status={status!r}")
    if route.get("in_sitemap") is True and route.get("indexable") is not True:
        errors.append(f"{rid}: in_sitemap=true while indexable=false")
    if route.get("in_navigation") is True and status != "published":
        errors.append(f"{rid}: in_navigation=true while status={status!r}")

    generate_only_published = build_config.get("generate_only_published_routes", True)
    publish_planned = build_config.get("publish_planned_routes", False)
    if status == "planned" and not publish_planned and generate_only_published:
        pass  # expected locked posture
    elif status not in ("published", "planned"):
        errors.append(f"{rid}: unexpected status={status!r}")

    return errors


def assess_route(
    route: dict[str, Any],
    build_config: dict[str, Any],
    templates_root: Path,
    output_dir: Path,
    sitemap_gate: bool,
    nav_gate: bool,
) -> RouteAssessment:
    rid = route["route_id"]
    status = route.get("status", "planned")
    content_path = ROOT / route.get("content_file", "")
    template_name = route.get("template", "")
    template_path = templates_root / template_name

    block_reasons: list[str] = []
    eligibility = "blocked_planned"

    block_reasons.extend(unsafe_flag_errors(route, build_config))
    block_reasons.extend(validate_required_metadata(route))

    content_exists = content_path.is_file()
    template_exists = template_path.is_file()

    if not content_exists:
        block_reasons.append("missing content_file")
    if not template_exists:
        block_reasons.append("missing template")

    generate_only_published = build_config.get("generate_only_published_routes", True)
    publish_planned = build_config.get("publish_planned_routes", False)

    may_render = False
    if status == "published":
        eligibility = "eligible_published"
        may_render = True
    elif status == "planned" and publish_planned and not generate_only_published:
        eligibility = "eligible_planned_override"
        may_render = True
    else:
        block_reasons.append("route not published; publication gate closed")

    if not content_exists or not template_exists:
        eligibility = "blocked_missing_assets"
        may_render = False

    if block_reasons and eligibility.startswith("eligible"):
        eligibility = "blocked_unsafe_flags"
        may_render = False

    would_index = (
        route.get("indexable") is True
        and status == "published"
        and generate_only_published
    )
    would_sitemap = (
        route.get("in_sitemap") is True
        and route.get("indexable") is True
        and status == "published"
        and sitemap_gate
    )
    would_navigation = (
        route.get("in_navigation") is True
        and status == "published"
        and nav_gate
    )

    robots = "index, follow" if would_index else "noindex, nofollow"

    if status != "published":
        eligibility = "non_public"

    return RouteAssessment(
        route_id=rid,
        path=route.get("path", ""),
        eligibility_class=eligibility,
        block_reasons=sorted(set(block_reasons)),
        output_path=route_output_path(route, output_dir),
        robots_directive=robots,
        would_sitemap=would_sitemap,
        would_navigation=would_navigation,
        would_index=would_index,
    )


def check_duplicate_output_paths(assessments: list[RouteAssessment]) -> list[str]:
    paths: Counter[str] = Counter(a.output_path for a in assessments)
    return [f"duplicate output path: {p} ({c} routes)" for p, c in paths.items() if c > 1]


def parse_content_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fm[key.strip()] = value.strip()
    return fm


def is_truthy_flag(value: str) -> bool:
    return value.strip().lower() in ("true", "1", "yes", "on")


def format_route_content_mismatch(
    route: dict[str, Any],
    *,
    field: str,
    expected: str,
    actual: str,
) -> str:
    return (
        f"route/content mismatch: route_id={route['route_id']} "
        f"route_path={route.get('path', '')} "
        f"content_file={route.get('content_file', '')} "
        f"field={field} expected={expected!r} actual={actual!r}"
    )


def check_duplicate_content_file_assignments(routes: list[dict[str, Any]]) -> list[str]:
    by_file: dict[str, list[str]] = {}
    for route in routes:
        content_file = route.get("content_file", "")
        if content_file:
            by_file.setdefault(content_file, []).append(route["route_id"])
    errors: list[str] = []
    for content_file, route_ids in by_file.items():
        if len(route_ids) <= 1:
            continue
        for route_id in route_ids:
            errors.append(
                format_route_content_mismatch(
                    {
                        "route_id": route_id,
                        "path": next(
                            (r.get("path", "") for r in routes if r["route_id"] == route_id),
                            "",
                        ),
                        "content_file": content_file,
                    },
                    field="content_file",
                    expected="unique registry assignment",
                    actual=f"shared with {', '.join(route_ids)}",
                )
            )
    return errors


def validate_route_content_alignment(
    route: dict[str, Any],
) -> tuple[list[str], list[str]]:
    """Validate registry route identity against its registered content file."""
    errors: list[str] = []
    warnings: list[str] = []
    content_rel = route.get("content_file", "")
    if not content_rel:
        return errors, warnings

    content_path = ROOT / content_rel
    if not content_path.is_file():
        return errors, warnings

    resolved = content_path.resolve()
    expected_resolved = (ROOT / content_rel).resolve()
    if resolved != expected_resolved:
        errors.append(
            format_route_content_mismatch(
                route,
                field="content_file_path",
                expected=str(expected_resolved),
                actual=str(resolved),
            )
        )

    text = content_path.read_text(encoding="utf-8")
    fm = parse_content_frontmatter(text)

    if fm.get("route_id") and fm["route_id"] != route["route_id"]:
        errors.append(
            format_route_content_mismatch(
                route,
                field="route_id",
                expected=route["route_id"],
                actual=fm["route_id"],
            )
        )

    for lang_field in ("language", "locale", "source_language"):
        if lang_field in fm and fm[lang_field] != route.get(lang_field):
            errors.append(
                format_route_content_mismatch(
                    route,
                    field=lang_field,
                    expected=str(route.get(lang_field)),
                    actual=fm[lang_field],
                )
            )

    route_status = route.get("status", "planned")
    if fm.get("status"):
        content_status = fm["status"].lower()
        if content_status == "published" and route_status != "published":
            errors.append(
                format_route_content_mismatch(
                    route,
                    field="status",
                    expected=f"not published (route status={route_status!r})",
                    actual=fm["status"],
                )
            )

    if fm.get("publication_status"):
        pub_status = fm["publication_status"].lower()
        contradictory = {
            "public",
            "published",
            "live",
            "launch_ready",
            "publication_ready",
            "indexable",
        }
        if pub_status in contradictory and route_status != "published":
            errors.append(
                format_route_content_mismatch(
                    route,
                    field="publication_status",
                    expected="non_public or absent (route not published)",
                    actual=fm["publication_status"],
                )
            )

    for flag in ("indexable", "in_sitemap", "in_navigation"):
        if flag in fm and is_truthy_flag(fm[flag]) and route.get(flag) is not True:
            errors.append(
                format_route_content_mismatch(
                    route,
                    field=flag,
                    expected="false (route registry lock)",
                    actual=fm[flag],
                )
            )

    if fm.get("content_file") and fm["content_file"] != content_rel:
        errors.append(
            format_route_content_mismatch(
                route,
                field="content_file",
                expected=content_rel,
                actual=fm["content_file"],
            )
        )

    return errors, warnings


def check_partials(templates_root: Path) -> list[TemplateCheck]:
    partial_checks = []
    for partial in (
        "partials/head.html",
        "partials/nav.html",
        "partials/footer.html",
        "partials/source_bar.html",
        "partials/internal_links.html",
        "partials/hreflang.html",
        "partials/safety_notice.html",
    ):
        partial_checks.append(assess_template(templates_root, partial))
    head = next(c for c in partial_checks if c.path.endswith("head.html"))
    if head.exists:
        text = (templates_root / "partials/head.html").read_text(encoding="utf-8")
        for marker in PARTIAL_HEAD_MARKERS:
            if marker not in text:
                head.missing_blocks.append(marker)
                head.issues.append(f"head partial missing {marker}")
    return partial_checks


def select_sample_routes(
    assessments: list[RouteAssessment],
    routes: list[dict[str, Any]],
    sample_size: int,
) -> list[str]:
    """Select deterministic sample by route_id sort — planning only in locked posture."""
    ordered = sorted(routes, key=lambda r: r["route_id"])
    chosen_ids = [r["route_id"] for r in ordered[:sample_size]]
    for assessment in assessments:
        if assessment.route_id in chosen_ids:
            assessment.selected_for_sample = True
    return chosen_ids


def compute_locks(routes: list[dict[str, Any]]) -> tuple[str, str, str, str]:
    published = sum(1 for r in routes if r.get("status") == "published")
    indexable = sum(1 for r in routes if r.get("indexable") is True)
    in_sitemap = sum(1 for r in routes if r.get("in_sitemap") is True)
    in_navigation = sum(1 for r in routes if r.get("in_navigation") is True)

    pub = "LOCKED" if published == 0 else f"OPEN ({published} published)"
    idx = "LOCKED" if indexable == 0 else f"FAIL ({indexable} indexable)"
    sm = "LOCKED" if in_sitemap == 0 else f"FAIL ({in_sitemap} in_sitemap)"
    nav = "LOCKED" if in_navigation == 0 else f"FAIL ({in_navigation} in_navigation)"
    return pub, idx, sm, nav


def production_can_proceed(
    routes: list[dict[str, Any]],
    build_config: dict[str, Any],
    eligible: int,
) -> str:
    pub, idx, sm, nav = compute_locks(routes)
    if "FAIL" in pub or "FAIL" in idx or "FAIL" in sm or "FAIL" in nav:
        return "no"
    if eligible == 0:
        return "no"
    if build_config.get("generate_only_published_routes", True):
        published = sum(1 for r in routes if r.get("status") == "published")
        if published == 0:
            return "no"
    sm_allowed, _ = global_sitemap_allowed()
    nav_allowed, _ = global_navigation_allowed()
    if sm_allowed or nav_allowed:
        return "no"  # global gates still closed in current posture
    return "no"  # fail-closed default until explicit launch authorization


def run_build_engine(
    *,
    dry_run: bool = True,
    strict: bool = False,
    sample_size: int | None = None,
    write_build_status: bool = False,
    write_audit_report: Path | None = None,
) -> BuildAudit:
    mode = "dry-run"
    if sample_size is not None:
        mode = f"sample-plan-{sample_size}"
    if write_build_status:
        mode += "+write-build-status"

    audit = BuildAudit(
        mode=mode,
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
    )

    if not CONFIG_PATH.is_file():
        audit.strict_errors.append(f"build config missing: {CONFIG_PATH.relative_to(ROOT)}")
        if strict:
            return audit
    if not ROUTES_PATH.is_file():
        audit.strict_errors.append(f"routes missing: {ROUTES_PATH.relative_to(ROOT)}")
        return audit

    build_config = load_json(CONFIG_PATH)
    routes_data = load_json(ROUTES_PATH)
    routes: list[dict[str, Any]] = routes_data.get("routes", [])

    templates_root = ROOT / build_config.get("templates_root", "main/templates")
    output_dir = ROOT / build_config.get("output_dir", "site")

    audit.route_count = len(routes)
    backed = 0
    missing = 0
    for route in routes:
        cf = ROOT / route.get("content_file", "")
        if cf.is_file():
            backed += 1
        elif route.get("content_file"):
            missing += 1
    audit.draft_backed_count = backed
    audit.missing_draft_count = missing

    sitemap_gate, sitemap_note = global_sitemap_allowed()
    nav_gate, nav_note = global_navigation_allowed()

    template_names = sorted({r.get("template", "") for r in routes if r.get("template")})
    audit.template_checks.extend(check_partials(templates_root))
    for name in template_names:
        audit.template_checks.append(assess_template(templates_root, name))

    assessments: list[RouteAssessment] = []
    for route in routes:
        assessments.append(
            assess_route(route, build_config, templates_root, output_dir, sitemap_gate, nav_gate)
        )
    audit.route_assessments = assessments

    if sample_size is not None:
        select_sample_routes(assessments, routes, sample_size)
        audit.sample_planned_count = min(sample_size, len(routes))

    audit.eligible_render_count = sum(
        1 for a in assessments if a.eligibility_class.startswith("eligible")
    )
    audit.blocked_count = audit.route_count - audit.eligible_render_count
    audit.non_public_count = sum(1 for a in assessments if a.eligibility_class == "non_public")
    audit.non_indexable_count = sum(1 for a in assessments if not a.would_index)
    audit.out_of_sitemap_count = sum(1 for a in assessments if not a.would_sitemap)
    audit.out_of_navigation_count = sum(1 for a in assessments if not a.would_navigation)

    pub, idx, sm, nav = compute_locks(routes)
    audit.publication_lock = pub
    audit.indexation_lock = idx
    audit.sitemap_lock = sm
    audit.navigation_lock = nav
    audit.production_can_safely_proceed = production_can_proceed(
        routes, build_config, audit.eligible_render_count
    )

    audit.output_plan_notes.extend([
        f"output_dir: {output_dir.relative_to(ROOT)}",
        f"sitemap gate: {'OPEN' if sitemap_gate else 'CLOSED'} ({sitemap_note})",
        f"navigation gate: {'OPEN' if nav_gate else 'CLOSED'} ({nav_note})",
        "public HTML generation: DISABLED (no published routes / locked posture)",
        "sitemap generation: DISABLED",
        "navigation generation: DISABLED",
        "sample output labeling: dry-run/sample/non-public (when sample render authorized)",
    ])

    audit.strict_errors.extend(check_duplicate_output_paths(assessments))

    if strict:
        audit.strict_errors.extend(check_duplicate_content_file_assignments(routes))

        selected_route_ids: set[str] | None = None
        if sample_size is not None:
            selected_route_ids = {
                a.route_id for a in assessments if a.selected_for_sample
            }

        for route in routes:
            audit.strict_errors.extend(unsafe_flag_errors(route, build_config))
            if route.get("status") == "planned":
                cf = ROOT / route.get("content_file", "")
                tp = templates_root / route.get("template", "")
                if sample_size and route["route_id"] in {
                    a.route_id for a in assessments if a.selected_for_sample
                }:
                    if not cf.is_file():
                        audit.strict_errors.append(
                            f"{route['route_id']}: missing content_file for sample candidate"
                        )
                    if not tp.is_file():
                        audit.strict_errors.append(
                            f"{route['route_id']}: missing template for sample candidate"
                        )
            audit.strict_errors.extend(validate_required_metadata(route))

            content_path = ROOT / route.get("content_file", "")
            if not content_path.is_file():
                continue
            if selected_route_ids is not None and route["route_id"] not in selected_route_ids:
                continue

            audit.content_alignment_checked += 1
            align_errors, align_warnings = validate_route_content_alignment(route)
            audit.strict_errors.extend(align_errors)
            audit.content_alignment_warnings.extend(align_warnings)

        for check in audit.template_checks:
            if not check.exists:
                audit.strict_errors.append(f"missing template: {check.path}")
            if check.missing_blocks:
                audit.strict_errors.append(
                    f"template {check.path} missing blocks: {', '.join(check.missing_blocks)}"
                )

    # Never generate public HTML in current locked posture
    audit.public_html_generated = 0
    audit.sitemap_generated = False
    audit.navigation_generated = False

    if write_build_status and not dry_run:
        pass  # guarded below — status write allowed explicitly

    if write_build_status:
        output_dir.mkdir(parents=True, exist_ok=True)
        status_path = output_dir / "build-status.json"
        status_payload = {
            "build_engine": "sovereign-hardened",
            "build_mode": audit.mode,
            "build_status": build_config.get("build_status", "skeleton"),
            "public_pages_generated": audit.public_html_generated,
            "reason": "Publication gates closed. No public HTML generated.",
            "route_count": audit.route_count,
            "eligible_render_count": audit.eligible_render_count,
            "draft_backed_route_count": audit.draft_backed_count,
            "missing_draft_count": audit.missing_draft_count,
            "production_can_safely_proceed": audit.production_can_safely_proceed,
            "publication_lock": audit.publication_lock,
            "indexation_lock": audit.indexation_lock,
            "sitemap_lock": audit.sitemap_lock,
            "navigation_lock": audit.navigation_lock,
            "timestamp_utc": audit.timestamp_utc,
        }
        with status_path.open("w", encoding="utf-8") as f:
            json.dump(status_payload, f, indent=2)
        audit.output_plan_notes.append(f"wrote build-status.json: {status_path.relative_to(ROOT)}")

    if write_audit_report:
        write_audit_report.parent.mkdir(parents=True, exist_ok=True)
        report_payload = audit_to_dict(audit)
        with write_audit_report.open("w", encoding="utf-8") as f:
            json.dump(report_payload, f, indent=2)

    return audit


def audit_to_dict(audit: BuildAudit) -> dict[str, Any]:
    return {
        "mode": audit.mode,
        "timestamp_utc": audit.timestamp_utc,
        "route_count": audit.route_count,
        "draft_backed_count": audit.draft_backed_count,
        "missing_draft_count": audit.missing_draft_count,
        "eligible_render_count": audit.eligible_render_count,
        "blocked_count": audit.blocked_count,
        "non_public_count": audit.non_public_count,
        "non_indexable_count": audit.non_indexable_count,
        "out_of_sitemap_count": audit.out_of_sitemap_count,
        "out_of_navigation_count": audit.out_of_navigation_count,
        "sample_planned_count": audit.sample_planned_count,
        "publication_lock": audit.publication_lock,
        "indexation_lock": audit.indexation_lock,
        "sitemap_lock": audit.sitemap_lock,
        "navigation_lock": audit.navigation_lock,
        "production_can_safely_proceed": audit.production_can_safely_proceed,
        "public_html_generated": audit.public_html_generated,
        "strict_errors": audit.strict_errors,
        "template_checks": [
            {
                "path": t.path,
                "exists": t.exists,
                "size_bytes": t.size_bytes,
                "placeholder_like": t.placeholder_like,
                "missing_blocks": t.missing_blocks,
                "issues": t.issues,
            }
            for t in audit.template_checks
        ],
        "output_plan_notes": audit.output_plan_notes,
    }


def print_summary(audit: BuildAudit, strict: bool) -> None:
    print("bisulfid.com — Sovereign Build Engine")
    print("=" * 60)
    print(f"  Mode:                         {audit.mode}")
    print(f"  Timestamp (UTC):              {audit.timestamp_utc}")
    print(f"  Routes loaded:                {audit.route_count}")
    print(f"  Draft-backed routes:          {audit.draft_backed_count}")
    print(f"  Missing drafts:               {audit.missing_draft_count}")
    print(f"  Eligible for render:          {audit.eligible_render_count}")
    print(f"  Blocked routes:               {audit.blocked_count}")
    print(f"  Non-public routes:            {audit.non_public_count}")
    print(f"  Non-indexable (planned):      {audit.non_indexable_count}")
    print(f"  Out of sitemap:               {audit.out_of_sitemap_count}")
    print(f"  Out of navigation:            {audit.out_of_navigation_count}")
    if audit.sample_planned_count:
        print(f"  Sample planned (IDs):         {audit.sample_planned_count}")
    print()
    print("  Governance locks:")
    print(f"    Publication:                {audit.publication_lock}")
    print(f"    Indexation:                 {audit.indexation_lock}")
    print(f"    Sitemap:                    {audit.sitemap_lock}")
    print(f"    Navigation:                 {audit.navigation_lock}")
    print(f"    production_can_safely_proceed: {audit.production_can_safely_proceed}")
    print()
    print(f"  Public HTML generated:        {audit.public_html_generated}")
    print(f"  Sitemap generated:            {audit.sitemap_generated}")
    print(f"  Navigation generated:         {audit.navigation_generated}")

    placeholder_templates = [t.path for t in audit.template_checks if t.placeholder_like]
    missing_templates = [t.path for t in audit.template_checks if not t.exists]
    if missing_templates:
        print()
        print(f"  Missing templates:            {len(missing_templates)}")
        for p in missing_templates[:10]:
            print(f"    - {p}")
    if placeholder_templates:
        print()
        print(f"  Placeholder-like templates:   {len(placeholder_templates)}")
        for p in placeholder_templates[:10]:
            print(f"    - {p}")

    if audit.content_alignment_checked:
        print()
        print(f"  Route/content alignment checked: {audit.content_alignment_checked}")
    if audit.content_alignment_warnings:
        print(f"  Content alignment warnings:   {len(audit.content_alignment_warnings)}")
        for warn in audit.content_alignment_warnings[:10]:
            print(f"    - {warn}")

    if audit.strict_errors:
        print()
        print(f"  Strict validation issues:     {len(audit.strict_errors)}")
        for err in audit.strict_errors[:20]:
            print(f"    - {err}")
        if len(audit.strict_errors) > 20:
            print(f"    ... and {len(audit.strict_errors) - 20} more")

    print()
    for note in audit.output_plan_notes:
        print(f"  {note}")

    print("=" * 60)
    if strict and audit.strict_errors:
        print("STRICT MODE: FAIL — validation errors detected.")
    elif audit.mode.startswith("dry-run") or audit.mode.startswith("sample"):
        print("Dry-run complete. No public HTML generated. No registries modified.")
    else:
        print("Build engine run complete. No public HTML generated.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sovereign build engine for bisulfid.com (fail-closed, governance-aware).",
        epilog=(
            "Default: show help. Use --dry-run for inspection. "
            "Public HTML is never generated while publication locks are active."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Inspect routes, templates, and output plan without writing public HTML.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail closed on missing templates, unsafe flags, duplicates, and metadata gaps.",
    )
    parser.add_argument(
        "--sample",
        type=int,
        metavar="N",
        help="Plan a controlled sample of N routes (planning only; no HTML in locked posture).",
    )
    parser.add_argument(
        "--write-build-status",
        action="store_true",
        help="Write site/build-status.json audit artifact (not public HTML).",
    )
    parser.add_argument(
        "--write-audit-report",
        metavar="PATH",
        help="Write JSON audit report to PATH (relative to repo root).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not any((args.dry_run, args.sample is not None, args.write_build_status)):
        parser.print_help()
        print()
        print("No action selected. Default is read-only help (no file writes).")
        print("Safe inspection: python scripts/build.py --dry-run")
        return 0

    audit_report_path = None
    if args.write_audit_report:
        audit_report_path = ROOT / args.write_audit_report

    audit = run_build_engine(
        dry_run=True,
        strict=args.strict,
        sample_size=args.sample,
        write_build_status=args.write_build_status,
        write_audit_report=audit_report_path,
    )

    print_summary(audit, strict=args.strict)

    if args.strict and audit.strict_errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
