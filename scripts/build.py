#!/usr/bin/env python3
"""build.py — Sovereign build engine for bisulfid.com (Sprint 6M-A).

Governed, fail-closed static build orchestrator. Reads route governance from
main/data/routes.json and build config from main/config/build.json.

Default invocation performs no file writes. Use explicit flags for output.

Modes:
  --dry-run       Inspect routes, templates, and output plan (default action)
  --sample N      Plan a controlled sample of N routes (no HTML in locked posture)
  --render-quarantined-sample  Render deterministic 8-page QA HTML to site/_sample/ only
  --render-quarantined-rc-batch --limit N  Render non-public RC batch to site/_sample/ only
  --render-public-launch-foundation --limit N  Render controlled public launch foundation to site/public/ only
  --render-public-design-system-refresh --limit N  Re-render public foundation with design system (Sprint 6N-C)
  --render-visual-proof-sample  Render 6N-D visual proof (7 routes) before full 14,000 refresh
  --render-integration-sample  Render design-system integration pilot to site/public/_integration_sample/
  --strict        Fail closed on validation errors
  --write-build-status  Write site/build-status.json audit artifact only

Does not generate public HTML unless publication gates explicitly allow it.
Does not modify routes, content, sources, claims, or registries.
Python standard library only.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
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

# Legacy registry template names -> hardened publication frame (Sprint 6M-C bridge)
TEMPLATE_FRAME_BRIDGE: dict[str, str] = {
    "reference_page.html": "reference.html",
    "term_page.html": "term.html",
    "home.html": "home.html",
    "glossary.html": "reference.html",
    "newsletter.html": "page.html",
    "acquire.html": "page.html",
}

BRIDGE_TEMPLATE_MARKERS = (
    "Registry bridge",
    "Bridge target:",
    "reference-frame",
    "term-frame",
)

# Deterministic quarantined QA sample — fixed route_ids, no registry mutation
QUARANTINED_SAMPLE_ROUTE_IDS: tuple[str, ...] = (
    "home",
    "what_is_bisulfid",
    "de_core_mos2",
    "en_index_disambiguation_map",
    "sources",
    "corpus_methodology_overview",
    "de_bisulfide_hydrosulfide_sulfide",
    "bisulfide_hydrosulfide_sulfide",
)

QUARANTINED_SAMPLE_DIR = DEFAULT_SITE_DIR / "_sample"

RC_BATCH_DEFAULT_LIMIT = 250
RC_BATCH_MAX_LIMIT = 14000
RC_BATCH_MIN_TARGET = 100
RC_BATCH_1500_TARGET = 1500
RC_BATCH_7500_TARGET = 7500
RC_BATCH_14000_TARGET = 14000
RC_BATCH_MANIFEST_NAME = "rc_batch_manifest.json"

PUBLIC_LAUNCH_FOUNDATION_DIR = DEFAULT_SITE_DIR / "public"
PUBLIC_LAUNCH_MANIFEST_NAME = "public_launch_manifest.json"
PUBLIC_LAUNCH_FOUNDATION_TARGET = 14000
PUBLIC_LAUNCH_MAX_LIMIT = 14000

# Design-system integration pilot — deterministic 7-route sample (Sprint 6N-B)
INTEGRATION_SAMPLE_ROUTE_IDS: tuple[str, ...] = (
    "home",
    "what_is_bisulfid",
    "de_core_mos2",
    "en_index_disambiguation_map",
    "bisulfide_hydrosulfide_sulfide",
    "sources",
    "corpus_methodology_overview",
)
INTEGRATION_SAMPLE_DIR = PUBLIC_LAUNCH_FOUNDATION_DIR / "_integration_sample"
INTEGRATION_SAMPLE_MANIFEST_NAME = "integration_sample_manifest.json"

# Visual proof gate — deterministic 7-route sample before full 14,000 refresh (Sprint 6N-D)
VISUAL_PROOF_SAMPLE_ROUTE_IDS: tuple[str, ...] = INTEGRATION_SAMPLE_ROUTE_IDS
VISUAL_PROOF_SAMPLE_DIR = PUBLIC_LAUNCH_FOUNDATION_DIR / "_visual_proof_sample"
VISUAL_PROOF_MANIFEST_NAME = "visual_proof_manifest.json"
VISUAL_PROOF_REVIEW_APPROVED = "approved"
DESIGN_SYSTEM_SRC = ROOT / "bisulfid-design-system"
DESIGN_SYSTEM_PUBLIC_ASSETS = PUBLIC_LAUNCH_FOUNDATION_DIR / "assets" / "bisulfid-design-system"
DESIGN_SYSTEM_REFRESH_SPRINT = "6N-D"
DESIGN_SYSTEM_VISUAL_RECONSTRUCTION_SPRINT = "6N-D"
DESIGN_SYSTEM_REFRESH_EXACT = 14000

PUBLIC_FOUNDATION_CSP = (
    "default-src 'none'; "
    "base-uri 'none'; "
    "form-action 'none'; "
    "frame-ancestors 'none'; "
    "style-src 'self'; "
    "img-src 'self' data:; "
    "font-src 'self'; "
    "connect-src 'none'; "
    "object-src 'none'; "
    "media-src 'none'; "
    "script-src 'none'"
)

QA_HTML_PREAMBLE = """<!--
  QUARANTINED NON-PUBLIC QA RENDER — NOT A LAUNCH
  Sprint 6M-C publication-frame proof. Not indexable. Outside sitemap. Outside navigation.
  Source/claim approval not implied. 14,000-page minimum launch objective unchanged.
  production_can_safely_proceed: no
-->
"""

RC_HTML_PREAMBLE = """<!--
  QUARANTINED NON-PUBLIC RELEASE CANDIDATE — NOT A LAUNCH
  Sprint 6M-D RC Batch 01 inside the 14,000-page publication pipeline.
  Not indexable. Not publication-ready. Outside sitemap. Outside navigation.
  Source/claim approval not implied. Not a reduced launch target.
  production_can_safely_proceed: no
-->
"""

PUBLIC_LAUNCH_HTML_PREAMBLE = """<!--
  PUBLIC LAUNCH FOUNDATION — 14,000-PAGE CONTROLLED VISIBILITY (Sprint 6M-G)
  Indexation gate: CLOSED (noindex,nofollow). Sitemap gate: CLOSED. Navigation gate: CLOSED.
  Source approval not implied. Claim approval not implied. [SOURCE REQUIRED] preserved.
  Public visibility does not mean final publication-ready status.
-->
"""

INTEGRATION_HTML_PREAMBLE = """<!--
  DESIGN SYSTEM INTEGRATION SAMPLE — Sprint 6N-B controlled pilot
  Output: site/public/_integration_sample/ only. Does not replace 14,000-page foundation.
  Indexation gate: CLOSED (noindex,nofollow). Sitemap gate: CLOSED. Navigation gate: CLOSED.
  Source approval not implied. Claim approval not implied. [SOURCE REQUIRED] preserved.
  Bisulfid proprietary design system — local assets only. No external dependencies.
-->
"""

RTL_LANGUAGES = frozenset({"ar", "he", "fa", "ur"})


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
class RCBatchResult:
    rendered_count: int
    skipped_count: int
    written_paths: list[str]
    errors: list[str]
    skipped_by_category: dict[str, int]
    manifest_path: str
    selected_route_ids: list[str]
    page_records: list[dict[str, Any]]


@dataclass
class PublicLaunchResult:
    rendered_count: int
    skipped_count: int
    written_paths: list[str]
    errors: list[str]
    skipped_by_category: dict[str, int]
    manifest_path: str
    selected_route_ids: list[str]
    page_records: list[dict[str, Any]]


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
    rc_batch_result: RCBatchResult | None = None
    public_launch_result: PublicLaunchResult | None = None
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


def resolve_frame_template(template_name: str) -> str:
    """Map legacy registry template name to hardened publication frame."""
    return TEMPLATE_FRAME_BRIDGE.get(template_name, template_name)


def is_bridged_template(text: str) -> bool:
    return any(marker in text for marker in BRIDGE_TEMPLATE_MARKERS)


def assess_template(templates_root: Path, template_name: str) -> TemplateCheck:
    rel = template_name.replace("\\", "/")
    path = templates_root / rel
    check = TemplateCheck(path=str(path.relative_to(ROOT)), exists=path.is_file())
    if not check.exists:
        check.issues.append("template file missing")
        return check

    text = path.read_text(encoding="utf-8")
    check.size_bytes = len(text.encode("utf-8"))
    bridged = is_bridged_template(text) or template_name in TEMPLATE_FRAME_BRIDGE
    frame_target = resolve_frame_template(template_name)
    frame_exists = (templates_root / frame_target).is_file()
    check.placeholder_like = (
        check.size_bytes < PLACEHOLDER_SIZE_THRESHOLD
        and "SKELETON TEMPLATE" in text
        and not bridged
    )
    if bridged and frame_exists and "SKELETON TEMPLATE" not in text:
        check.placeholder_like = False
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
    if template_name in TEMPLATE_FRAME_BRIDGE:
        if not frame_exists:
            check.issues.append(f"bridge target missing: {frame_target}")
        elif "SKELETON TEMPLATE" in text:
            check.issues.append("legacy template remains unresolved skeleton")
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


def assert_quarantine_output_dir(sample_dir: Path) -> None:
    """Fail closed if output target is outside site/_sample/."""
    resolved = sample_dir.resolve()
    expected_root = QUARANTINED_SAMPLE_DIR.resolve()
    if resolved != expected_root and expected_root not in resolved.parents:
        raise ValueError(
            f"quarantine output dir must be under site/_sample/: got {resolved}"
        )


def assert_public_launch_output_path(out_path: Path) -> None:
    """Fail closed if public launch output is outside site/public/."""
    resolved = out_path.resolve()
    public_root = PUBLIC_LAUNCH_FOUNDATION_DIR.resolve()
    sample_root = QUARANTINED_SAMPLE_DIR.resolve()
    if sample_root in resolved.parents or resolved == sample_root:
        raise ValueError(f"public launch must not write to quarantine: {resolved}")
    try:
        resolved.relative_to(public_root)
    except ValueError as exc:
        raise ValueError(f"public launch output must be under site/public/: {resolved}") from exc


def route_is_public_launch_eligible(route: dict[str, Any], templates_root: Path) -> tuple[bool, str]:
    content_path = ROOT / route.get("content_file", "")
    if not content_path.is_file():
        return False, "missing_content"
    template_name = route.get("template", "")
    if template_name not in TEMPLATE_FRAME_BRIDGE and not (templates_root / template_name).is_file():
        return False, "unmapped_template"
    if route.get("status") != "planned":
        return False, "non_planned_status"
    if route.get("indexable") is True:
        return False, "indexable_not_allowed"
    if route.get("in_sitemap") is True:
        return False, "in_sitemap_not_allowed"
    if route.get("in_navigation") is True:
        return False, "in_navigation_not_allowed"
    return True, ""


def select_public_launch_routes(
    routes: list[dict[str, Any]],
    templates_root: Path,
    limit: int,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Deterministic stratified public launch foundation selection."""
    route_by_id = {r["route_id"]: r for r in routes}
    selected_ids: list[str] = []
    seen: set[str] = set()
    skipped_by_category: Counter[str] = Counter()

    def add_route(route: dict[str, Any]) -> bool:
        if len(selected_ids) >= limit:
            return False
        rid = route["route_id"]
        if rid in seen:
            return True
        ok, reason = route_is_public_launch_eligible(route, templates_root)
        if not ok:
            skipped_by_category[reason] += 1
            return True
        selected_ids.append(rid)
        seen.add(rid)
        return True

    eligible = [r for r in routes if r["route_id"] not in seen]
    buckets: dict[str, list[dict[str, Any]]] = {
        "gateway": [],
        "de_terminology": [],
        "en_terminology": [],
        "disambiguation": [],
        "reference_governance": [],
        "reference": [],
        "acquisition": [],
    }
    for route in eligible:
        ok, reason = route_is_public_launch_eligible(route, templates_root)
        if not ok:
            continue
        page_type = classify_route_page_type(route)
        bucket = page_type if page_type in buckets else "reference"
        buckets[bucket].append(route)

    for key in buckets:
        buckets[key].sort(key=lambda r: r["route_id"])

    bucket_order = (
        "gateway",
        "de_terminology",
        "disambiguation",
        "reference_governance",
        "en_terminology",
        "acquisition",
        "reference",
    )
    indices = {k: 0 for k in bucket_order}
    while len(selected_ids) < limit:
        progressed = False
        for bucket_name in bucket_order:
            if len(selected_ids) >= limit:
                break
            idx = indices[bucket_name]
            bucket = buckets[bucket_name]
            if idx >= len(bucket):
                continue
            route = bucket[idx]
            indices[bucket_name] += 1
            if route["route_id"] in seen:
                continue
            add_route(route)
            progressed = True
        if not progressed:
            break

    if len(selected_ids) < limit:
        for route in sorted(eligible, key=lambda r: r["route_id"]):
            if len(selected_ids) >= limit:
                break
            if route["route_id"] in seen:
                continue
            ok, reason = route_is_public_launch_eligible(route, templates_root)
            if not ok:
                skipped_by_category[reason] += 1
                continue
            selected_ids.append(route["route_id"])
            seen.add(route["route_id"])

    selected_routes = [route_by_id[rid] for rid in selected_ids if rid in route_by_id]
    return selected_routes, dict(skipped_by_category)


def classify_route_page_type(route: dict[str, Any]) -> str:
    layer = route.get("layer", "")
    lang = route.get("language", "en")
    notes = route.get("notes", "").lower()
    template = route.get("template", "")
    rid = route.get("route_id", "")

    if layer in ("gateway", "public_gateway") or template == "home.html" or rid == "home":
        return "gateway"
    if "disambiguation" in notes or "disambiguation" in rid:
        return "disambiguation"
    if layer in ("methodology_reference", "utility", "foundation_reference", "safety_governance"):
        return "reference_governance"
    if template == "term_page.html" or layer == "terminology_system":
        return "de_terminology" if lang == "de" else "en_terminology"
    if layer == "acquisition" or template == "acquire.html":
        return "acquisition"
    return "reference"


def route_is_render_eligible(route: dict[str, Any], templates_root: Path) -> tuple[bool, str]:
    content_path = ROOT / route.get("content_file", "")
    if not content_path.is_file():
        return False, "missing_content"
    template_name = route.get("template", "")
    if template_name not in TEMPLATE_FRAME_BRIDGE and not (templates_root / template_name).is_file():
        return False, "unmapped_template"
    if route.get("status") != "planned":
        return False, "non_planned_status"
    return True, ""


def select_rc_batch_routes(
    routes: list[dict[str, Any]],
    templates_root: Path,
    limit: int,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Deterministic stratified RC batch selection from draft-backed routes."""
    route_by_id = {r["route_id"]: r for r in routes}
    selected_ids: list[str] = []
    seen: set[str] = set()
    skipped_by_category: Counter[str] = Counter()

    def add_route(route: dict[str, Any]) -> bool:
        if len(selected_ids) >= limit:
            return False
        rid = route["route_id"]
        if rid in seen:
            return True
        ok, reason = route_is_render_eligible(route, templates_root)
        if not ok:
            skipped_by_category[reason] += 1
            return True
        selected_ids.append(rid)
        seen.add(rid)
        return True

    # Tier 0: Sprint 6M-C QA proof routes (always first)
    for rid in QUARANTINED_SAMPLE_ROUTE_IDS:
        route = route_by_id.get(rid)
        if route:
            add_route(route)

    eligible = [r for r in routes if r["route_id"] not in seen]
    buckets: dict[str, list[dict[str, Any]]] = {
        "gateway": [],
        "de_terminology": [],
        "en_terminology": [],
        "disambiguation": [],
        "reference_governance": [],
        "reference": [],
        "acquisition": [],
    }
    for route in eligible:
        ok, reason = route_is_render_eligible(route, templates_root)
        if not ok:
            continue
        page_type = classify_route_page_type(route)
        bucket = page_type if page_type in buckets else "reference"
        buckets[bucket].append(route)

    for key in buckets:
        buckets[key].sort(key=lambda r: r["route_id"])

    bucket_order = (
        "gateway",
        "de_terminology",
        "disambiguation",
        "reference_governance",
        "en_terminology",
        "acquisition",
        "reference",
    )
    indices = {k: 0 for k in bucket_order}
    while len(selected_ids) < limit:
        progressed = False
        for bucket_name in bucket_order:
            if len(selected_ids) >= limit:
                break
            idx = indices[bucket_name]
            bucket = buckets[bucket_name]
            if idx >= len(bucket):
                continue
            route = bucket[idx]
            indices[bucket_name] += 1
            if route["route_id"] in seen:
                continue
            selected_ids.append(route["route_id"])
            seen.add(route["route_id"])
            progressed = True
        if not progressed:
            break

    if len(selected_ids) < limit:
        for route in sorted(eligible, key=lambda r: r["route_id"]):
            if len(selected_ids) >= limit:
                break
            if route["route_id"] in seen:
                continue
            ok, reason = route_is_render_eligible(route, templates_root)
            if not ok:
                skipped_by_category[reason] += 1
                continue
            selected_ids.append(route["route_id"])
            seen.add(route["route_id"])

    selected_routes = [route_by_id[rid] for rid in selected_ids if rid in route_by_id]
    return selected_routes, dict(skipped_by_category)


def strip_content_body(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text.strip()


def highlight_source_required(text: str) -> str:
    return text.replace(
        "[SOURCE REQUIRED]",
        '<mark class="source-required-marker">[SOURCE REQUIRED]</mark>',
    )


def restore_inline_html_tags(text: str) -> str:
    return (
        text.replace("&lt;strong&gt;", "<strong>")
        .replace("&lt;/strong&gt;", "</strong>")
        .replace("&lt;code&gt;", "<code>")
        .replace("&lt;/code&gt;", "</code>")
        .replace("&lt;mark class=&quot;source-required-marker&quot;&gt;", '<mark class="source-required-marker">')
        .replace("&lt;/mark&gt;", "</mark>")
    )


def markdown_inline_to_html(text: str) -> str:
    """Convert inline markdown (bold, code) for gateway intros and short fields."""
    converted = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    converted = re.sub(r"`([^`]+)`", r"<code>\1</code>", converted)
    converted = highlight_source_required(html.escape(converted))
    return restore_inline_html_tags(converted)


def empty_slot_markup(render_mode: str) -> str:
    """QA placeholder only in quarantined engineering renders — not public/integration."""
    if render_mode in ("integration_sample", "public_launch_foundation"):
        return '<div class="bs-slot-empty" aria-hidden="true"></div>'
    return (
        '<p class="slot-empty" data-empty="true">'
        "Slot reserved — not populated in QA render.</p>"
    )


def markdown_body_to_html(markdown: str) -> str:
    """Minimal markdown-to-HTML for quarantined QA renders (stdlib only)."""
    lines = markdown.splitlines()
    out: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False
    table_rows: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not in_table:
            return
        out.append("<table>")
        for i, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            rendered_cells = []
            for c in cells:
                cell = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", c)
                cell = highlight_source_required(html.escape(cell))
                cell = restore_inline_html_tags(cell)
                rendered_cells.append(cell)
            out.append("<tr>" + "".join(f"<{tag}>{cell}</{tag}>" for cell in rendered_cells) + "</tr>")
        out.append("</table>")
        in_table = False
        table_rows = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("|") and "|" in line[1:]:
            close_lists()
            if not in_table:
                in_table = True
                table_rows = []
            if re.match(r"^\|[\s\-:|]+\|$", line):
                continue
            table_rows.append(line)
            continue
        flush_table()

        if not line.strip():
            close_lists()
            continue
        if line.strip() == "---":
            close_lists()
            out.append("<hr>")
            continue
        if line.startswith("#"):
            close_lists()
            level = len(line) - len(line.lstrip("#"))
            level = min(max(level, 1), 6)
            title = line[level:].strip()
            title = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", title)
            title = highlight_source_required(html.escape(title))
            title = restore_inline_html_tags(title)
            out.append(f"<h{level}>{title}</h{level}>")
            continue
        if line.lstrip().startswith("- "):
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            item = line.lstrip()[2:].strip()
            item = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", item)
            item = highlight_source_required(html.escape(item))
            item = restore_inline_html_tags(item)
            out.append(f"<li>{item}</li>")
            continue
        if re.match(r"^\d+\.\s", line.lstrip()):
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            item = re.sub(r"^\d+\.\s", "", line.lstrip())
            item = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", item)
            item = highlight_source_required(html.escape(item))
            item = restore_inline_html_tags(item)
            out.append(f"<li>{item}</li>")
            continue

        close_lists()
        para = line.strip()
        para = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", para)
        para = re.sub(r"`([^`]+)`", r"<code>\1</code>", para)
        para = highlight_source_required(html.escape(para))
        para = restore_inline_html_tags(para)
        out.append(f"<p>{para}</p>")

    close_lists()
    flush_table()
    return "\n".join(out)


def substitute_slots(template: str, context: dict[str, str]) -> str:
    result = template
    for key, value in context.items():
        result = result.replace(f"{{{{{key}}}}}", value)
    return result


def read_template_file(templates_root: Path, rel: str) -> str:
    path = templates_root / rel
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def build_render_context(
    route: dict[str, Any],
    body_html: str,
    *,
    render_mode: str = "qa_sample",
) -> dict[str, str]:
    language = route.get("language", "en")
    text_direction = "rtl" if language in RTL_LANGUAGES else "ltr"
    status = route.get("status", "planned")
    indexable = route.get("indexable", False)
    in_sitemap = route.get("in_sitemap", False)
    in_navigation = route.get("in_navigation", False)
    source_required = route.get("source_required", False)
    has_source_markers = "[SOURCE REQUIRED]" in body_html or source_required

    frame = resolve_frame_template(route.get("template", ""))
    layer = route.get("layer", "reference")

    empty_slot = empty_slot_markup(render_mode)
    safety_body = ""
    if layer == "safety_governance":
        safety_body = (
            "Safety-layer route — governance notice required before publication. "
            "No handling instructions implied."
        )

    context: dict[str, str] = {
        "language": language,
        "text_direction": text_direction,
        "route_id": route["route_id"],
        "route_status": status,
        "route_path": route.get("path", ""),
        "route_layer": layer,
        "publication_posture": (
            "integration_sample"
            if render_mode == "integration_sample"
            else (
                "public_visible_foundation"
                if render_mode == "public_launch_foundation"
                else "non_public"
            )
        ),
        "language_depth_label": language.upper(),
        "source_crystal_class": (
            "bs-source-crystal--required" if has_source_markers else "bs-source-crystal--candidate"
        ),
        "term_card_modifier": (
            "bs-term-card--source-required" if has_source_markers else ""
        ),
        "page_title": route.get("title", route["route_id"]),
        "meta_description": route.get("description", ""),
        "robots_directive": (
            "noindex, nofollow"
            if render_mode == "public_launch_foundation" or not indexable
            else "noindex, nofollow"
        ),
        "canonical_url": f"https://bisulfid.com{route.get('path', '/')}",
        "canonical_mode": (
            "public_foundation_noindex" if render_mode == "public_launch_foundation"
            else "non_public_withheld"
        ),
        "indexable_flag": "false",
        "in_sitemap_flag": "false",
        "in_navigation_flag": "false",
        "indexable_label": "Closed",
        "in_sitemap_label": "Closed",
        "in_navigation_label": "Closed",
        "gate_indexation_label": "CLOSED",
        "gate_sitemap_label": "CLOSED",
        "gate_navigation_label": "CLOSED",
        "route_status_label": route.get("status", "planned"),
        "publication_posture_label": (
            "Public foundation"
            if render_mode == "public_launch_foundation"
            else route.get("status", "planned")
        ),
        "source_required_flag": "true" if has_source_markers else "false",
        "source_required_chip": (
            "[SOURCE REQUIRED]" if has_source_markers else "Not flagged"
        ),
        "claim_approval_state": "no_claims_approved",
        "claim_approval_label": "None approved",
        "source_registry_posture": "inactive",
        "csp_policy_placeholder": PUBLIC_FOUNDATION_CSP,
        "site_name": "bisulfid.com",
        "copyright_year": str(datetime.now(timezone.utc).year),
        "page_h1": route.get("h1", route.get("title", route["route_id"])),
        "qa_artifact_flag": (
            "false"
            if render_mode in ("public_launch_foundation", "integration_sample")
            else "true"
        ),
        "governance_banner_title": (
            "Design system integration sample — controlled pilot"
            if render_mode == "integration_sample"
            else (
                "Public launch foundation — controlled visibility"
                if render_mode == "public_launch_foundation"
                else (
                    "Non-public release candidate — NOT A LAUNCH"
                    if render_mode == "rc_batch"
                    else "Non-public QA render — NOT A LAUNCH"
                )
            )
        ),
        "governance_banner_body": (
            "Bisulfid design-system template integration pilot (Sprint 6N-B). "
            "Indexation CLOSED (noindex). Sitemap CLOSED. Navigation CLOSED. "
            "Source approval not implied. Claim approval not implied. "
            "[SOURCE REQUIRED] preserved where unresolved."
            if render_mode == "integration_sample"
            else (
                "14,000-page public launch foundation. Indexation CLOSED (noindex). "
                "Sitemap CLOSED. Navigation CLOSED. Source approval not implied. "
                "Claim approval not implied. [SOURCE REQUIRED] preserved where unresolved."
                if render_mode == "public_launch_foundation"
                else (
                    "RC Batch 01 under site/_sample/ inside the 14,000-page publication pipeline. "
                    "Not indexable. Not publication-ready. Outside sitemap. Outside navigation. "
                    "Not a reduced launch target."
                    if render_mode == "rc_batch"
                    else (
                        "Quarantined engineering sample under site/_sample/. "
                        "Not indexable. Outside sitemap. Outside navigation. "
                        "14,000-page governed launch corpus frame proof only."
                    )
                )
            )
        ),
        "navigation_status": "inactive",
        "navigation_items": "",
        "hreflang_status": "inactive",
        "hreflang_link_tags": "<!-- hreflang withheld — publication locks active -->",
        "breadcrumb_items": (
            f'<li><span>Design system integration sample</span></li>'
            f'<li><span>{html.escape(route["route_id"])}</span></li>'
            if render_mode == "integration_sample"
            else (
                f'<li><span>Public launch foundation</span></li>'
                f'<li><span>{html.escape(route["route_id"])}</span></li>'
                if render_mode == "public_launch_foundation"
                else (
                    f'<li><span>RC Batch 01</span></li><li><span>{html.escape(route["route_id"])}</span></li>'
                    if render_mode == "rc_batch"
                    else (
                        f'<li><span>QA sample</span></li>'
                        f'<li><span>{html.escape(route["route_id"])}</span></li>'
                    )
                )
            )
        ),
        "breadcrumb_context_hidden": "false",
        "source_posture_message": (
            "Sources and claims remain unapproved. [SOURCE REQUIRED] markers are binding."
            if has_source_markers
            else "No source approval implied by public visibility."
        ),
        "source_list": "",
        "source_required_visible": "true" if has_source_markers else "false",
        "internal_link_items": "",
        "internal_links_empty": "true",
        "safety_notice_body": safety_body,
        "gateway_intro": empty_slot,
        "interactive_term_map": empty_slot,
        "language_entry_points": empty_slot,
        "related_terms": empty_slot,
        "disambiguation_notice": empty_slot,
        "reference_body": body_html,
        "term_definition": body_html,
        "page_body": body_html,
    }

    if frame == "home.html":
        intro_lines = []
        for line in strip_content_body(
            (ROOT / route.get("content_file", "")).read_text(encoding="utf-8")
            if route.get("content_file") and (ROOT / route["content_file"]).is_file()
            else ""
        ).splitlines():
            if line.strip() and not line.startswith("#"):
                intro_lines.append(line.strip())
                if len(intro_lines) >= 2:
                    break
        context["gateway_intro"] = (
            markdown_inline_to_html(" ".join(intro_lines)) if intro_lines else empty_slot
        )

    return context


def render_route_quarantined(
    route: dict[str, Any],
    templates_root: Path,
    *,
    render_mode: str = "qa_sample",
) -> str:
    content_path = ROOT / route.get("content_file", "")
    if not content_path.is_file():
        raise FileNotFoundError(f"missing content: {content_path}")

    body_md = strip_content_body(content_path.read_text(encoding="utf-8"))
    body_html = markdown_body_to_html(body_md)
    context = build_render_context(route, body_html, render_mode=render_mode)

    registry_template = route.get("template", "")
    frame_template = resolve_frame_template(registry_template)
    bridge_text = read_template_file(templates_root, registry_template)
    frame_text = read_template_file(templates_root, frame_template)
    inner_template = bridge_text if bridge_text and "SKELETON TEMPLATE" not in bridge_text else frame_text
    if not inner_template:
        inner_template = frame_text

    if frame_template == "home.html":
        inner_template = read_template_file(templates_root, "home.html")

    inner_html = substitute_slots(inner_template, context)

    partials = {
        "head": read_template_file(templates_root, "partials/head.html"),
        "nav": read_template_file(templates_root, "partials/nav.html"),
        "footer": read_template_file(templates_root, "partials/footer.html"),
        "governance_banner": read_template_file(templates_root, "partials/governance_banner.html"),
        "breadcrumbs": read_template_file(templates_root, "partials/breadcrumbs.html"),
        "hreflang": read_template_file(templates_root, "partials/hreflang.html"),
        "source_bar": read_template_file(templates_root, "partials/source_bar.html"),
        "internal_links": read_template_file(templates_root, "partials/internal_links.html"),
        "safety_notice": read_template_file(templates_root, "partials/safety_notice.html"),
    }
    for key in partials:
        partials[key] = substitute_slots(partials[key], context)

    if layer := route.get("layer"):
        if layer != "safety_governance":
            partials["safety_notice"] = ""

    context["head"] = partials["head"]
    context["nav"] = partials["nav"]
    context["footer"] = partials["footer"]
    context["governance_banner"] = partials["governance_banner"]
    context["breadcrumbs"] = partials["breadcrumbs"]
    context["hreflang"] = partials["hreflang"]
    context["content"] = inner_html
    context["source_bar"] = partials["source_bar"]
    context["internal_links"] = partials["internal_links"]
    context["safety_notice"] = partials["safety_notice"]

    inner_html = substitute_slots(inner_html, {
        "source_bar": partials["source_bar"],
        "internal_links": partials["internal_links"],
        "safety_notice": partials["safety_notice"],
    })
    context["content"] = inner_html

    base = read_template_file(templates_root, "base.html")
    page = substitute_slots(base, context)

    if render_mode == "rc_batch":
        qa_notice = (
            '<div class="qa-render-notice rc-batch-notice" role="status" '
            'data-qa-artifact="true" data-rc-batch="01" '
            'data-publication-posture="non_public">'
            "<p><strong>Quarantined non-public release candidate batch</strong> — "
            "not a public launch. Not publication-ready. Not indexable. "
            "Outside sitemap. Outside navigation. "
            "Source and claim approval not implied. "
            f"Route status: <strong>{html.escape(route.get('status', 'planned'))}</strong>. "
            "14,000-page minimum launch objective unchanged. "
            "Not a reduced publication target.</p></div>"
        )
        preamble = RC_HTML_PREAMBLE
    elif render_mode == "public_launch_foundation":
        qa_notice = (
            '<div class="public-launch-foundation-notice bs-governance-banner__sr-summary" '
            'role="status" data-public-launch-foundation="14000" '
            'data-publication-posture="public_visible_foundation" aria-hidden="true">'
            "Public launch foundation — controlled visibility. "
            "Indexation CLOSED. Sitemap CLOSED. Navigation CLOSED."
            "</div>"
        )
        preamble = PUBLIC_LAUNCH_HTML_PREAMBLE
    elif render_mode == "integration_sample":
        qa_notice = (
            '<div class="integration-sample-notice bs-governance-banner" role="status" '
            'data-integration-sample="6N-B" '
            'data-publication-posture="integration_sample">'
            "<p><strong>Design system integration sample</strong> — controlled pilot only. "
            "Indexation gate: <strong>CLOSED</strong> (noindex,nofollow). "
            "Sitemap gate: <strong>CLOSED</strong>. Navigation gate: <strong>CLOSED</strong>. "
            "Source approval not implied. Claim approval not implied. "
            "Does not replace the 14,000-page public foundation corpus.</p></div>"
        )
        preamble = INTEGRATION_HTML_PREAMBLE
    else:
        qa_notice = (
            '<div class="qa-render-notice" role="status" data-qa-artifact="true" '
            'data-publication-posture="non_public">'
            "<p><strong>Quarantined non-public QA render</strong> — not a public launch. "
            "Not indexable. Outside sitemap. Outside navigation. "
            "Source and claim approval not implied. "
            "Route status: <strong>planned</strong>. "
            "14,000-page minimum launch objective unchanged.</p></div>"
        )
        preamble = QA_HTML_PREAMBLE
    page = page.replace("<main id=\"main-content\"", qa_notice + "\n  <main id=\"main-content\"", 1)
    return preamble + page


def write_quarantined_sample_html(
    routes: list[dict[str, Any]],
    templates_root: Path,
    sample_dir: Path,
) -> tuple[int, list[str], list[str]]:
    """Render deterministic QA sample to site/_sample/ only."""
    errors: list[str] = []
    written: list[str] = []
    route_by_id = {r["route_id"]: r for r in routes}

    sample_dir.mkdir(parents=True, exist_ok=True)
    for existing in sample_dir.glob("*.html"):
        existing.unlink()

    for route_id in QUARANTINED_SAMPLE_ROUTE_IDS:
        route = route_by_id.get(route_id)
        if not route:
            errors.append(f"quarantined sample route missing: {route_id}")
            continue
        content_path = ROOT / route.get("content_file", "")
        if not content_path.is_file():
            errors.append(f"{route_id}: missing content_file for QA render")
            continue
        template_name = route.get("template", "")
        if template_name not in TEMPLATE_FRAME_BRIDGE and not (
            templates_root / template_name
        ).is_file():
            errors.append(f"{route_id}: unmapped template {template_name}")
            continue
        try:
            html_out = render_route_quarantined(route, templates_root)
        except OSError as exc:
            errors.append(f"{route_id}: render failed: {exc}")
            continue

        out_path = sample_dir / f"{route_id}.html"
        out_path.write_text(html_out, encoding="utf-8")
        written.append(str(out_path.relative_to(ROOT)).replace("\\", "/"))

    return len(written), written, errors


def sync_design_system_public_assets() -> list[str]:
    """Copy local design-system assets to site/public/assets/ (stdlib only)."""
    written: list[str] = []
    if not DESIGN_SYSTEM_SRC.is_dir():
        raise FileNotFoundError(f"design system source missing: {DESIGN_SYSTEM_SRC}")

    DESIGN_SYSTEM_PUBLIC_ASSETS.mkdir(parents=True, exist_ok=True)
    for sub in ("tokens", "components", "assets", "engine"):
        src_dir = DESIGN_SYSTEM_SRC / sub
        dst_dir = DESIGN_SYSTEM_PUBLIC_ASSETS / sub
        if not src_dir.is_dir():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        for src_file in src_dir.iterdir():
            if src_file.is_file():
                dst_file = dst_dir / src_file.name
                shutil.copy2(src_file, dst_file)
                written.append(str(dst_file.relative_to(ROOT)).replace("\\", "/"))

    bundle_src = DESIGN_SYSTEM_SRC / "bisulfid-frame.css"
    bundle_path = DESIGN_SYSTEM_PUBLIC_ASSETS / "bisulfid-frame.css"
    if bundle_src.is_file():
        shutil.copy2(bundle_src, bundle_path)
        written.append(str(bundle_path.relative_to(ROOT)).replace("\\", "/"))
    elif not bundle_path.is_file():
        bundle_path.write_text(
            '@import url("tokens/colors.css");\n'
            '@import url("tokens/typography.css");\n'
            '@import url("tokens/spacing.css");\n'
            '@import url("tokens/motion.css");\n'
            '@import url("tokens/depth.css");\n'
            '@import url("tokens/governance.css");\n'
            '@import url("components/governance-banner.css");\n'
            '@import url("components/source-crystal.css");\n'
            '@import url("components/term-card.css");\n'
            '@import url("components/term-node.css");\n'
            '@import url("components/language-depth.css");\n'
            '@import url("components/relation-lattice.css");\n',
            encoding="utf-8",
        )
        written.append(str(bundle_path.relative_to(ROOT)).replace("\\", "/"))

    return written


def write_integration_sample_html(
    routes: list[dict[str, Any]],
    templates_root: Path,
    sample_dir: Path,
) -> tuple[int, list[str], list[str]]:
    """Render design-system integration pilot to site/public/_integration_sample/ only."""
    if sample_dir.resolve().parent != PUBLIC_LAUNCH_FOUNDATION_DIR.resolve():
        raise ValueError(f"integration sample must be under site/public/: {sample_dir}")
    if "_integration_sample" not in sample_dir.parts:
        raise ValueError(f"integration sample dir must be _integration_sample: {sample_dir}")

    errors: list[str] = []
    written: list[str] = []
    page_records: list[dict[str, Any]] = []
    route_by_id = {r["route_id"]: r for r in routes}

    sync_design_system_public_assets()

    if sample_dir.exists():
        for existing in sample_dir.rglob("*.html"):
            existing.unlink()
    sample_dir.mkdir(parents=True, exist_ok=True)

    for route_id in INTEGRATION_SAMPLE_ROUTE_IDS:
        route = route_by_id.get(route_id)
        if not route:
            errors.append(f"integration sample route missing: {route_id}")
            continue
        ok, reason = route_is_render_eligible(route, templates_root)
        if not ok:
            errors.append(f"{route_id}: not render eligible ({reason})")
            continue
        try:
            html_out = render_route_quarantined(
                route, templates_root, render_mode="integration_sample"
            )
        except OSError as exc:
            errors.append(f"{route_id}: render failed: {exc}")
            continue

        raw_path = route.get("path", "/").strip("/")
        out_path = sample_dir / ("index.html" if not raw_path else f"{raw_path}/index.html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_out, encoding="utf-8")
        rel_path = str(out_path.relative_to(ROOT)).replace("\\", "/")
        written.append(rel_path)

        source_vis = "[SOURCE REQUIRED]" in html_out or "source-required-marker" in html_out
        page_records.append({
            "route_id": route_id,
            "route_path": route.get("path", ""),
            "language": route.get("language", ""),
            "output_path": rel_path,
            "source_required_visible": "yes" if source_vis else "no",
            "design_system_linked": "yes" if "bisulfid-design-system" in html_out else "no",
        })

    manifest = {
        "sample_id": "design_system_integration_pilot_6N-B",
        "sprint": "6N-B",
        "route_count": len(written),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(sample_dir.relative_to(ROOT)).replace("\\", "/"),
        "indexation_gate": "closed",
        "sitemap_gate": "closed",
        "navigation_gate": "closed",
        "replaces_public_foundation": False,
        "pages": page_records,
    }
    manifest_path = sample_dir / INTEGRATION_SAMPLE_MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return len(written), written, errors


def visual_proof_review_status() -> str | None:
    """Return visual_review_status from proof manifest, or None if absent."""
    manifest_path = VISUAL_PROOF_SAMPLE_DIR / VISUAL_PROOF_MANIFEST_NAME
    if not manifest_path.is_file():
        return None
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    status = data.get("visual_review_status")
    return str(status) if status is not None else None


def visual_proof_gate_allows_full_refresh() -> tuple[bool, str]:
    """Full 14,000 refresh requires approved visual proof manifest (Sprint 6N-D gate)."""
    manifest_path = VISUAL_PROOF_SAMPLE_DIR / VISUAL_PROOF_MANIFEST_NAME
    if not manifest_path.is_file():
        return False, (
            "visual proof manifest missing — run "
            "'python scripts/build.py --render-visual-proof-sample' and complete visual review first"
        )
    status = visual_proof_review_status()
    if status != VISUAL_PROOF_REVIEW_APPROVED:
        return False, (
            f"visual proof not approved (status={status!r}) — review "
            f"{manifest_path.relative_to(ROOT)} routes visually, set "
            f"visual_review_status to {VISUAL_PROOF_REVIEW_APPROVED!r}, then re-run full refresh"
        )
    return True, "visual proof approved"


def write_visual_proof_sample_html(
    routes: list[dict[str, Any]],
    templates_root: Path,
    sample_dir: Path,
) -> tuple[int, list[str], list[str]]:
    """Render 6N-D visual proof sample — 7 routes with public_launch_foundation templates."""
    if sample_dir.resolve().parent != PUBLIC_LAUNCH_FOUNDATION_DIR.resolve():
        raise ValueError(f"visual proof sample must be under site/public/: {sample_dir}")
    if "_visual_proof_sample" not in sample_dir.parts:
        raise ValueError(f"visual proof dir must be _visual_proof_sample: {sample_dir}")

    errors: list[str] = []
    written: list[str] = []
    page_records: list[dict[str, Any]] = []
    route_by_id = {r["route_id"]: r for r in routes}

    sync_design_system_public_assets()

    if sample_dir.exists():
        for existing in sample_dir.rglob("*.html"):
            existing.unlink()
    sample_dir.mkdir(parents=True, exist_ok=True)

    for route_id in VISUAL_PROOF_SAMPLE_ROUTE_IDS:
        route = route_by_id.get(route_id)
        if not route:
            errors.append(f"visual proof route missing: {route_id}")
            continue
        ok, reason = route_is_public_launch_eligible(route, templates_root)
        if not ok:
            errors.append(f"{route_id}: not public launch eligible ({reason})")
            continue
        try:
            html_out = render_route_quarantined(
                route, templates_root, render_mode="public_launch_foundation"
            )
        except OSError as exc:
            errors.append(f"{route_id}: render failed: {exc}")
            continue

        if "bs-control-room-hero" not in html_out and route_id == "home":
            errors.append(f"{route_id}: missing bs-control-room-hero in visual proof output")
        if route_id == "home" and "bs-source-crystal" not in html_out:
            errors.append(f"{route_id}: missing source crystal on gateway home")
        if "bisulfid-design-system" not in html_out:
            errors.append(f"{route_id}: missing design-system links in visual proof output")

        raw_path = route.get("path", "/").strip("/")
        out_path = sample_dir / ("index.html" if not raw_path else f"{raw_path}/index.html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_out, encoding="utf-8")
        rel_path = str(out_path.relative_to(ROOT)).replace("\\", "/")
        written.append(rel_path)

        source_vis = "[SOURCE REQUIRED]" in html_out or "source-required-marker" in html_out
        page_records.append({
            "route_id": route_id,
            "route_path": route.get("path", ""),
            "language": route.get("language", ""),
            "output_path": rel_path,
            "source_required_visible": "yes" if source_vis else "no",
            "design_system_linked": "yes" if "bisulfid-design-system" in html_out else "no",
            "bs_control_room_hero": "yes" if "bs-control-room-hero" in html_out else "no",
            "bs_gov_chip": "yes" if "bs-gov-chip" in html_out else "no",
        })

    manifest = {
        "sample_id": "sovereign_visual_proof_6N-D",
        "sprint": DESIGN_SYSTEM_VISUAL_RECONSTRUCTION_SPRINT,
        "route_count": len(written),
        "expected_route_count": len(VISUAL_PROOF_SAMPLE_ROUTE_IDS),
        "visual_proof_iteration": 3,
        "visual_review_status": "pending_review",
        "visual_review_note": (
            "Human visual review required before full 14,000-page refresh. "
            "Set visual_review_status to 'approved' after proof passes eye review."
        ),
        "visual_palette": "carbon-sulfur-molybdenum",
        "proof_routes": list(VISUAL_PROOF_SAMPLE_ROUTE_IDS),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(sample_dir.relative_to(ROOT)).replace("\\", "/"),
        "indexation_gate": "closed",
        "sitemap_gate": "closed",
        "navigation_gate": "closed",
        "replaces_public_foundation": False,
        "full_refresh_allowed": False,
        "pages": page_records,
    }
    manifest_path = sample_dir / VISUAL_PROOF_MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return len(written), written, errors


def content_has_source_required(route: dict[str, Any]) -> bool:
    if route.get("source_required"):
        return True
    content_path = ROOT / route.get("content_file", "")
    if not content_path.is_file():
        return False
    return "[SOURCE REQUIRED]" in content_path.read_text(encoding="utf-8")


def write_quarantined_rc_batch_html(
    routes: list[dict[str, Any]],
    templates_root: Path,
    sample_dir: Path,
    limit: int,
) -> RCBatchResult:
    """Render deterministic non-public RC batch to site/_sample/ only."""
    assert_quarantine_output_dir(sample_dir)
    errors: list[str] = []
    written: list[str] = []
    page_records: list[dict[str, Any]] = []
    skipped_by_category: Counter[str] = Counter()

    selected_routes, selection_skipped = select_rc_batch_routes(routes, templates_root, limit)
    skipped_by_category.update(selection_skipped)

    sample_dir.mkdir(parents=True, exist_ok=True)
    for existing in sample_dir.glob("*.html"):
        existing.unlink()

    for route in selected_routes:
        rid = route["route_id"]
        ok, reason = route_is_render_eligible(route, templates_root)
        if not ok:
            skipped_by_category[reason] += 1
            errors.append(f"{rid}: skipped ({reason})")
            continue
        try:
            html_out = render_route_quarantined(route, templates_root, render_mode="rc_batch")
        except OSError as exc:
            skipped_by_category["render_failed"] += 1
            errors.append(f"{rid}: render failed: {exc}")
            continue

        out_path = sample_dir / f"{rid}.html"
        if sample_dir.resolve() != QUARANTINED_SAMPLE_DIR.resolve():
            raise ValueError(f"refusing to write outside quarantine: {out_path}")
        out_path.write_text(html_out, encoding="utf-8")
        rel_path = str(out_path.relative_to(ROOT)).replace("\\", "/")
        written.append(rel_path)

        source_vis = (
            "[SOURCE REQUIRED]" in html_out or "source-required-marker" in html_out
        )
        page_records.append({
            "route_id": rid,
            "route_path": route.get("path", ""),
            "language": route.get("language", ""),
            "page_type": classify_route_page_type(route),
            "template_used": route.get("template", ""),
            "output_path": rel_path,
            "source_required_visible": "yes" if source_vis else "no",
            "route_status": route.get("status", "planned"),
        })

    total_skipped = sum(skipped_by_category.values())
    if limit >= RC_BATCH_14000_TARGET:
        batch_id = "rc_14000"
        sprint_tag = "6M-G"
    elif limit >= RC_BATCH_7500_TARGET:
        batch_id = "rc_7500"
        sprint_tag = "6M-F"
    elif limit >= RC_BATCH_1500_TARGET:
        batch_id = "rc_1500"
        sprint_tag = "6M-E"
    else:
        batch_id = "rc_batch_01"
        sprint_tag = "6M-D"
    manifest = {
        "batch_id": batch_id,
        "sprint": sprint_tag,
        "target_limit": limit,
        "rendered_count": len(written),
        "skipped_count": total_skipped,
        "skipped_by_category": dict(skipped_by_category),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(sample_dir.relative_to(ROOT)).replace("\\", "/"),
        "pages": page_records,
    }
    manifest_path = sample_dir / RC_BATCH_MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return RCBatchResult(
        rendered_count=len(written),
        skipped_count=total_skipped,
        written_paths=written,
        errors=errors,
        skipped_by_category=dict(skipped_by_category),
        manifest_path=str(manifest_path.relative_to(ROOT)).replace("\\", "/"),
        selected_route_ids=[r["route_id"] for r in selected_routes],
        page_records=page_records,
    )


def is_foundation_public_html_path(path: Path, public_dir: Path) -> bool:
    """True for 14,000-page foundation HTML (excludes pilot/proof sample dirs)."""
    try:
        rel = path.relative_to(public_dir)
    except ValueError:
        return False
    if not rel.parts:
        return True
    return rel.parts[0] not in ("_integration_sample", "_visual_proof_sample")


def clear_foundation_public_html(public_dir: Path) -> int:
    """Clear foundation index.html only; preserve _integration_sample and assets."""
    cleared = 0
    for existing in public_dir.rglob("index.html"):
        if is_foundation_public_html_path(existing, public_dir):
            existing.unlink()
            cleared += 1
    return cleared


def write_public_launch_foundation_html(
    routes: list[dict[str, Any]],
    templates_root: Path,
    public_dir: Path,
    limit: int,
) -> PublicLaunchResult:
    """Render controlled public launch foundation to site/public/ only."""
    public_root = PUBLIC_LAUNCH_FOUNDATION_DIR.resolve()
    if public_dir.resolve() != public_root:
        raise ValueError(f"public launch dir must be site/public/: got {public_dir.resolve()}")

    errors: list[str] = []
    written: list[str] = []
    page_records: list[dict[str, Any]] = []
    skipped_by_category: Counter[str] = Counter()
    language_split: Counter[str] = Counter()
    family_split: Counter[str] = Counter()

    selected_routes, selection_skipped = select_public_launch_routes(routes, templates_root, limit)
    skipped_by_category.update(selection_skipped)

    public_dir.mkdir(parents=True, exist_ok=True)
    for existing in public_dir.rglob("*.html"):
        if is_foundation_public_html_path(existing, public_dir):
            existing.unlink()

    for route in selected_routes:
        rid = route["route_id"]
        ok, reason = route_is_public_launch_eligible(route, templates_root)
        if not ok:
            skipped_by_category[reason] += 1
            errors.append(f"{rid}: skipped ({reason})")
            continue
        try:
            html_out = render_route_quarantined(
                route, templates_root, render_mode="public_launch_foundation"
            )
        except OSError as exc:
            skipped_by_category["render_failed"] += 1
            errors.append(f"{rid}: render failed: {exc}")
            continue

        rel_out = route_output_path(route, public_dir)
        out_path = ROOT / rel_out
        assert_public_launch_output_path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_out, encoding="utf-8")
        rel_path = str(out_path.relative_to(ROOT)).replace("\\", "/")
        written.append(rel_path)

        page_type = classify_route_page_type(route)
        language_split[route.get("language", "unknown")] += 1
        family_split[page_type] += 1

        source_vis = (
            "[SOURCE REQUIRED]" in html_out or "source-required-marker" in html_out
        )
        page_records.append({
            "route_id": rid,
            "route_path": route.get("path", ""),
            "language": route.get("language", ""),
            "page_type": page_type,
            "template_used": route.get("template", ""),
            "output_path": rel_path,
            "source_required_visible": "yes" if source_vis else "no",
            "route_status": route.get("status", "planned"),
            "public_visibility_enabled": "yes",
            "indexation_enabled": "no",
            "sitemap_enabled": "no",
            "navigation_enabled": "no",
        })

    total_skipped = sum(skipped_by_category.values())
    manifest = {
        "foundation_id": "public_launch_14000",
        "sprint": "6M-G",
        "target_limit": limit,
        "rendered_count": len(written),
        "skipped_count": total_skipped,
        "skipped_by_category": dict(skipped_by_category),
        "language_split": dict(language_split),
        "family_split": dict(family_split),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(public_dir.relative_to(ROOT)).replace("\\", "/"),
        "indexation_gate": "closed",
        "sitemap_gate": "closed",
        "navigation_gate": "closed",
        "pages": page_records,
    }
    manifest_path = public_dir / PUBLIC_LAUNCH_MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return PublicLaunchResult(
        rendered_count=len(written),
        skipped_count=total_skipped,
        written_paths=written,
        errors=errors,
        skipped_by_category=dict(skipped_by_category),
        manifest_path=str(manifest_path.relative_to(ROOT)).replace("\\", "/"),
        selected_route_ids=[r["route_id"] for r in selected_routes],
        page_records=page_records,
    )


def write_public_design_system_refresh_html(
    routes: list[dict[str, Any]],
    templates_root: Path,
    public_dir: Path,
    limit: int,
) -> PublicLaunchResult:
    """Re-render 14,000-page public foundation with integrated design system (Sprint 6N-C)."""
    public_root = PUBLIC_LAUNCH_FOUNDATION_DIR.resolve()
    if public_dir.resolve() != public_root:
        raise ValueError(f"design system refresh dir must be site/public/: got {public_dir.resolve()}")
    if limit != DESIGN_SYSTEM_REFRESH_EXACT:
        raise ValueError(
            f"design system refresh requires limit {DESIGN_SYSTEM_REFRESH_EXACT}, got {limit}"
        )

    gate_ok, gate_msg = visual_proof_gate_allows_full_refresh()
    if not gate_ok:
        raise ValueError(f"visual proof gate CLOSED: {gate_msg}")

    sync_design_system_public_assets()

    errors: list[str] = []
    written: list[str] = []
    page_records: list[dict[str, Any]] = []
    skipped_by_category: Counter[str] = Counter()
    language_split: Counter[str] = Counter()
    family_split: Counter[str] = Counter()

    selected_routes, selection_skipped = select_public_launch_routes(routes, templates_root, limit)
    skipped_by_category.update(selection_skipped)

    public_dir.mkdir(parents=True, exist_ok=True)
    clear_foundation_public_html(public_dir)

    for route in selected_routes:
        rid = route["route_id"]
        ok, reason = route_is_public_launch_eligible(route, templates_root)
        if not ok:
            skipped_by_category[reason] += 1
            errors.append(f"{rid}: skipped ({reason})")
            continue
        try:
            html_out = render_route_quarantined(
                route, templates_root, render_mode="public_launch_foundation"
            )
        except OSError as exc:
            skipped_by_category["render_failed"] += 1
            errors.append(f"{rid}: render failed: {exc}")
            continue

        if "bisulfid-design-system" not in html_out:
            errors.append(f"{rid}: missing design-system asset links in output")
        if "bs-control-room" not in html_out:
            errors.append(f"{rid}: missing bs-control-room in output")

        rel_out = route_output_path(route, public_dir)
        out_path = ROOT / rel_out
        assert_public_launch_output_path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_out, encoding="utf-8")
        rel_path = str(out_path.relative_to(ROOT)).replace("\\", "/")
        written.append(rel_path)

        page_type = classify_route_page_type(route)
        language_split[route.get("language", "unknown")] += 1
        family_split[page_type] += 1

        source_vis = (
            "[SOURCE REQUIRED]" in html_out or "source-required-marker" in html_out
        )
        page_records.append({
            "route_id": rid,
            "route_path": route.get("path", ""),
            "language": route.get("language", ""),
            "page_type": page_type,
            "template_used": route.get("template", ""),
            "output_path": rel_path,
            "source_required_visible": "yes" if source_vis else "no",
            "route_status": route.get("status", "planned"),
            "public_visibility_enabled": "yes",
            "indexation_enabled": "no",
            "sitemap_enabled": "no",
            "navigation_enabled": "no",
            "design_system_linked": "yes",
        })

    total_skipped = sum(skipped_by_category.values())
    refresh_ts = datetime.now(timezone.utc).isoformat()
    manifest = {
        "foundation_id": "public_launch_14000",
        "sprint": DESIGN_SYSTEM_REFRESH_SPRINT,
        "previous_sprint": "6N-C",
        "design_system_refresh": True,
        "design_system_refresh_sprint": "6N-C",
        "visual_reconstruction": True,
        "visual_reconstruction_sprint": DESIGN_SYSTEM_VISUAL_RECONSTRUCTION_SPRINT,
        "visual_palette": "carbon-sulfur-molybdenum",
        "design_system_bundle": "/assets/bisulfid-design-system/bisulfid-frame.css",
        "target_limit": limit,
        "rendered_count": len(written),
        "skipped_count": total_skipped,
        "skipped_by_category": dict(skipped_by_category),
        "language_split": dict(language_split),
        "family_split": dict(family_split),
        "timestamp_utc": refresh_ts,
        "design_system_refresh_timestamp_utc": refresh_ts,
        "output_dir": str(public_dir.relative_to(ROOT)).replace("\\", "/"),
        "indexation_gate": "closed",
        "sitemap_gate": "closed",
        "navigation_gate": "closed",
        "pages": page_records,
    }
    manifest_path = public_dir / PUBLIC_LAUNCH_MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return PublicLaunchResult(
        rendered_count=len(written),
        skipped_count=total_skipped,
        written_paths=written,
        errors=errors,
        skipped_by_category=dict(skipped_by_category),
        manifest_path=str(manifest_path.relative_to(ROOT)).replace("\\", "/"),
        selected_route_ids=[r["route_id"] for r in selected_routes],
        page_records=page_records,
    )


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
    render_quarantined_sample: bool = False,
    render_quarantined_rc_batch: bool = False,
    render_public_launch_foundation: bool = False,
    render_public_design_system_refresh: bool = False,
    render_integration_sample: bool = False,
    render_visual_proof_sample: bool = False,
    rc_batch_limit: int = RC_BATCH_DEFAULT_LIMIT,
    public_launch_limit: int = PUBLIC_LAUNCH_FOUNDATION_TARGET,
    write_build_status: bool = False,
    write_audit_report: Path | None = None,
) -> BuildAudit:
    mode = "dry-run"
    if render_public_launch_foundation:
        mode = f"render-public-launch-foundation-{public_launch_limit}"
    elif render_public_design_system_refresh:
        mode = f"render-public-design-system-refresh-{public_launch_limit}"
    elif render_integration_sample:
        mode = "render-integration-sample"
    elif render_visual_proof_sample:
        mode = "render-visual-proof-sample"
    elif render_quarantined_rc_batch:
        mode = f"render-quarantined-rc-batch-{rc_batch_limit}"
    elif render_quarantined_sample:
        mode = "render-quarantined-sample"
    elif sample_size is not None:
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

    # Default: no public HTML unless explicit public launch foundation render
    audit.public_html_generated = 0
    audit.sitemap_generated = False
    audit.navigation_generated = False

    render_modes = sum((
        render_quarantined_rc_batch,
        render_quarantined_sample,
        render_public_launch_foundation,
        render_public_design_system_refresh,
        render_integration_sample,
        render_visual_proof_sample,
    ))
    if render_modes > 1:
        audit.strict_errors.append("cannot combine multiple render modes")

    if render_visual_proof_sample:
        count, paths, render_errors = write_visual_proof_sample_html(
            routes, templates_root, VISUAL_PROOF_SAMPLE_DIR
        )
        audit.strict_errors.extend(render_errors)
        audit.public_html_generated = count
        audit.output_plan_notes.append(
            f"Visual proof sample: rendered {count} page(s) under "
            f"{VISUAL_PROOF_SAMPLE_DIR.relative_to(ROOT)}"
        )
        audit.output_plan_notes.append(
            "Visual proof gate: full 14,000 refresh BLOCKED until "
            f"visual_review_status is {VISUAL_PROOF_REVIEW_APPROVED!r} in "
            f"{VISUAL_PROOF_MANIFEST_NAME}"
        )
        for p in paths:
            audit.output_plan_notes.append(f"  - {p}")
        if strict and render_errors:
            pass
        elif strict and count != len(VISUAL_PROOF_SAMPLE_ROUTE_IDS):
            audit.strict_errors.append(
                f"visual proof sample rendered {count} pages "
                f"(expected {len(VISUAL_PROOF_SAMPLE_ROUTE_IDS)})"
            )

    elif render_integration_sample:
        count, paths, render_errors = write_integration_sample_html(
            routes, templates_root, INTEGRATION_SAMPLE_DIR
        )
        audit.strict_errors.extend(render_errors)
        audit.public_html_generated = count
        audit.output_plan_notes.append(
            f"Design system integration sample: rendered {count} page(s) under "
            f"{INTEGRATION_SAMPLE_DIR.relative_to(ROOT)}"
        )
        for p in paths:
            audit.output_plan_notes.append(f"  - {p}")
        if strict and render_errors:
            pass
        elif strict and count != len(INTEGRATION_SAMPLE_ROUTE_IDS):
            audit.strict_errors.append(
                f"integration sample rendered {count} pages "
                f"(expected {len(INTEGRATION_SAMPLE_ROUTE_IDS)})"
            )

    elif render_public_design_system_refresh:
        pl_result = write_public_design_system_refresh_html(
            routes, templates_root, PUBLIC_LAUNCH_FOUNDATION_DIR, public_launch_limit
        )
        audit.public_launch_result = pl_result
        audit.public_html_generated = pl_result.rendered_count
        audit.strict_errors.extend(pl_result.errors)
        audit.output_plan_notes.append(
            f"Design system public refresh: rendered {pl_result.rendered_count} page(s), "
            f"skipped {pl_result.skipped_count}"
        )
        audit.output_plan_notes.append(f"manifest: {pl_result.manifest_path}")
        audit.output_plan_notes.append(
            f"output scope: {PUBLIC_LAUNCH_FOUNDATION_DIR.relative_to(ROOT)} "
            f"(foundation only; _integration_sample preserved)"
        )
        for category, count in sorted(pl_result.skipped_by_category.items()):
            audit.output_plan_notes.append(f"  skipped ({category}): {count}")
        if strict and pl_result.rendered_count < DESIGN_SYSTEM_REFRESH_EXACT:
            audit.strict_errors.append(
                f"design system refresh rendered {pl_result.rendered_count} pages "
                f"(required {DESIGN_SYSTEM_REFRESH_EXACT})"
            )

    elif render_public_launch_foundation:
        pl_result = write_public_launch_foundation_html(
            routes, templates_root, PUBLIC_LAUNCH_FOUNDATION_DIR, public_launch_limit
        )
        audit.public_launch_result = pl_result
        audit.public_html_generated = pl_result.rendered_count
        audit.strict_errors.extend(pl_result.errors)
        audit.output_plan_notes.append(
            f"Public launch foundation: rendered {pl_result.rendered_count} page(s), "
            f"skipped {pl_result.skipped_count}"
        )
        audit.output_plan_notes.append(f"manifest: {pl_result.manifest_path}")
        audit.output_plan_notes.append(
            f"output scope: {PUBLIC_LAUNCH_FOUNDATION_DIR.relative_to(ROOT)}"
        )
        for category, count in sorted(pl_result.skipped_by_category.items()):
            audit.output_plan_notes.append(f"  skipped ({category}): {count}")
        if strict and pl_result.rendered_count < PUBLIC_LAUNCH_FOUNDATION_TARGET:
            audit.strict_errors.append(
                f"public launch rendered {pl_result.rendered_count} pages "
                f"(required {PUBLIC_LAUNCH_FOUNDATION_TARGET})"
            )

    elif render_quarantined_rc_batch:
        if render_quarantined_sample:
            audit.strict_errors.append("cannot combine --render-quarantined-sample with RC batch")
        else:
            rc_result = write_quarantined_rc_batch_html(
                routes, templates_root, QUARANTINED_SAMPLE_DIR, rc_batch_limit
            )
            audit.rc_batch_result = rc_result
            audit.strict_errors.extend(rc_result.errors)
            audit.output_plan_notes.append(
                f"RC Batch 01: rendered {rc_result.rendered_count} page(s), "
                f"skipped {rc_result.skipped_count}"
            )
            audit.output_plan_notes.append(f"manifest: {rc_result.manifest_path}")
            for category, count in sorted(rc_result.skipped_by_category.items()):
                audit.output_plan_notes.append(f"  skipped ({category}): {count}")
            if strict and rc_result.rendered_count < RC_BATCH_MIN_TARGET:
                audit.strict_errors.append(
                    f"RC batch rendered {rc_result.rendered_count} pages "
                    f"(minimum target {RC_BATCH_MIN_TARGET})"
                )
            if strict and rc_batch_limit >= RC_BATCH_14000_TARGET and rc_result.rendered_count < RC_BATCH_14000_TARGET:
                audit.strict_errors.append(
                    f"RC 14000 batch rendered {rc_result.rendered_count} pages "
                    f"(required {RC_BATCH_14000_TARGET})"
                )
            elif strict and rc_batch_limit >= RC_BATCH_7500_TARGET and rc_result.rendered_count < RC_BATCH_7500_TARGET:
                audit.strict_errors.append(
                    f"RC 7500 batch rendered {rc_result.rendered_count} pages "
                    f"(required {RC_BATCH_7500_TARGET})"
                )
            elif strict and rc_batch_limit >= RC_BATCH_1500_TARGET and rc_result.rendered_count < RC_BATCH_1500_TARGET:
                audit.strict_errors.append(
                    f"RC 1500 batch rendered {rc_result.rendered_count} pages "
                    f"(required {RC_BATCH_1500_TARGET})"
                )

    elif render_quarantined_sample:
        count, paths, render_errors = write_quarantined_sample_html(
            routes, templates_root, QUARANTINED_SAMPLE_DIR
        )
        audit.strict_errors.extend(render_errors)
        if paths:
            audit.output_plan_notes.append(
                f"quarantined QA HTML written: {count} file(s) under site/_sample/"
            )
            for p in paths:
                audit.output_plan_notes.append(f"  - {p}")
        if strict and render_errors:
            pass  # strict exit handled by caller
        if count == 0 and not render_errors:
            audit.strict_errors.append("quarantined sample render produced zero files")

    if write_build_status and not render_quarantined_sample and not render_quarantined_rc_batch and not render_public_launch_foundation and not render_public_design_system_refresh and not render_visual_proof_sample:
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
    elif audit.mode.startswith("render-visual-proof-sample"):
        print("Visual proof sample render complete.")
        print(f"  Output under {VISUAL_PROOF_SAMPLE_DIR.relative_to(ROOT)}/ only.")
        print("  14,000-page public foundation corpus unchanged.")
        print(
            f"  Review routes visually, then set visual_review_status to "
            f"{VISUAL_PROOF_REVIEW_APPROVED!r} in {VISUAL_PROOF_MANIFEST_NAME} "
            "before full refresh."
        )
    elif audit.mode.startswith("render-integration-sample"):
        print("Design system integration sample render complete.")
        print(f"  Output under {INTEGRATION_SAMPLE_DIR.relative_to(ROOT)}/ only.")
        print("  14,000-page public foundation corpus unchanged.")
    elif audit.mode.startswith("render-public-design-system-refresh"):
        print("Design system public refresh complete. Output under site/public/ foundation.")
        if audit.public_launch_result:
            print(
                f"  Rendered: {audit.public_launch_result.rendered_count} | "
                f"Skipped: {audit.public_launch_result.skipped_count}"
            )
        print("  _integration_sample/ and assets/ preserved.")
        print(f"  Visual proof gate: approved status required in {VISUAL_PROOF_MANIFEST_NAME}")
    elif audit.mode.startswith("render-public-launch-foundation"):
        print("Public launch foundation render complete. Output under site/public/ only.")
        if audit.public_launch_result:
            print(
                f"  Rendered: {audit.public_launch_result.rendered_count} | "
                f"Skipped: {audit.public_launch_result.skipped_count}"
            )
        print("Indexation/sitemap/navigation gates remain CLOSED. No registries modified.")
    elif audit.mode.startswith("render-quarantined-rc-batch"):
        print("RC Batch 01 render complete. Output under site/_sample/ only.")
        if audit.rc_batch_result:
            print(
                f"  Rendered: {audit.rc_batch_result.rendered_count} | "
                f"Skipped: {audit.rc_batch_result.skipped_count}"
            )
        print("No public HTML outside quarantine. No registries modified.")
    elif audit.mode.startswith("render-quarantined-sample"):
        print("Quarantined QA render complete. Output under site/_sample/ only.")
        print("No public HTML outside quarantine. No registries modified.")
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
        "--render-public-launch-foundation",
        action="store_true",
        help="Render controlled public launch foundation HTML to site/public/ only (noindex).",
    )
    parser.add_argument(
        "--render-quarantined-rc-batch",
        action="store_true",
        help="Render non-public RC batch HTML to site/_sample/ only (noindex, not a launch).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=RC_BATCH_DEFAULT_LIMIT,
        metavar="N",
        help=(
            f"Max routes for RC batch or public launch foundation "
            f"(default {RC_BATCH_DEFAULT_LIMIT}, up to {RC_BATCH_MAX_LIMIT})."
        ),
    )
    parser.add_argument(
        "--render-public-design-system-refresh",
        action="store_true",
        help="Re-render 14,000 public foundation pages with design system (noindex; gates closed).",
    )
    parser.add_argument(
        "--render-visual-proof-sample",
        action="store_true",
        help=(
            "Render 6N-D visual proof (7 routes) to site/public/_visual_proof_sample/ "
            "before full 14,000 refresh."
        ),
    )
    parser.add_argument(
        "--render-integration-sample",
        action="store_true",
        help="Render design-system integration pilot to site/public/_integration_sample/ only.",
    )
    parser.add_argument(
        "--render-quarantined-sample",
        action="store_true",
        help="Render deterministic QA HTML to site/_sample/ only (non-public, noindex).",
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

    if not any((
        args.dry_run,
        args.sample is not None,
        args.render_quarantined_sample,
        args.render_quarantined_rc_batch,
        args.render_public_launch_foundation,
        args.render_public_design_system_refresh,
        args.render_integration_sample,
        args.render_visual_proof_sample,
        args.write_build_status,
    )):
        parser.print_help()
        print()
        print("No action selected. Default is read-only help (no file writes).")
        print("Safe inspection: python scripts/build.py --dry-run")
        print("Quarantined QA render: python scripts/build.py --render-quarantined-sample")
        print("RC Batch 01 render: python scripts/build.py --render-quarantined-rc-batch --limit 250")
        print("RC 1500 render: python scripts/build.py --render-quarantined-rc-batch --limit 1500")
        print("RC 7500 render: python scripts/build.py --render-quarantined-rc-batch --limit 7500")
        print("Public launch foundation: python scripts/build.py --render-public-launch-foundation --limit 14000")
        print("Design system refresh: python scripts/build.py --render-public-design-system-refresh --limit 14000")
        print("  (requires visual_review_status=approved in _visual_proof_sample/visual_proof_manifest.json)")
        print("Visual proof sample: python scripts/build.py --render-visual-proof-sample")
        print("Integration sample: python scripts/build.py --render-integration-sample")
        return 0

    audit_report_path = None
    if args.write_audit_report:
        audit_report_path = ROOT / args.write_audit_report

    render_any = (
        args.render_quarantined_sample
        or args.render_quarantined_rc_batch
        or args.render_public_launch_foundation
        or args.render_public_design_system_refresh
        or args.render_integration_sample
        or args.render_visual_proof_sample
    )
    public_limit = (
        args.limit
        if (args.render_public_launch_foundation or args.render_public_design_system_refresh)
        else PUBLIC_LAUNCH_FOUNDATION_TARGET
    )

    audit = run_build_engine(
        dry_run=not render_any,
        strict=args.strict,
        sample_size=args.sample,
        render_quarantined_sample=args.render_quarantined_sample,
        render_quarantined_rc_batch=args.render_quarantined_rc_batch,
        render_public_launch_foundation=args.render_public_launch_foundation,
        render_public_design_system_refresh=args.render_public_design_system_refresh,
        render_integration_sample=args.render_integration_sample,
        render_visual_proof_sample=args.render_visual_proof_sample,
        rc_batch_limit=args.limit,
        public_launch_limit=public_limit,
        write_build_status=args.write_build_status,
        write_audit_report=audit_report_path,
    )

    print_summary(audit, strict=args.strict)

    if args.strict and audit.strict_errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
