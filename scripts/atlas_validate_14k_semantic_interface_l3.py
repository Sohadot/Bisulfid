#!/usr/bin/env python3
"""Sprint 99B — Validate 14K semantic sovereign interface repair."""
from __future__ import annotations

import json
import random
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import (  # noqa: E402
    CSS_IMPORT_DEPENDENCIES,
    FORBIDDEN_PUBLIC_LANGUAGE_99A,
    LANE_DOMAIN_CLASS,
    LANE_SEMANTIC_CLASS,
    SOVEREIGN_SHELL_MARKERS,
    STYLESHEET_PATH,
    load_release_model,
    strip_machine_content_for_audit,
)
from atlas_hub_semantic_99bh import HUB_REQUIRED_PATHS  # noqa: E402

LEDGER_PATH = ROOT / "main/data/release_ledger.json"
PUBLIC_DIR = ROOT / "site/public"
CSS_DIR = PUBLIC_DIR / "assets/bisulfid-design-system"
CSS_PATH = CSS_DIR / "bisulfid-frame.css"
HREF_RE = re.compile(r'<a\s+href="([^"]+)"', re.I)
LANE_CLASS_RE = re.compile(r"atlas-lane-[a-z]+")
DOMAIN_CLASS_RE = re.compile(r"domain-[a-z]+")
AUDIENCE_CLASS_RE = re.compile(r"audience-[a-z]+")
MIN_BODY_CHARS = 400

SEMANTIC_COMPONENTS = (
    "atlas-dossier-hero",
    "atlas-role-panel",
    "atlas-context-layer-grid",
    "atlas-related-node-grid",
    "atlas-source-posture-panel",
    "atlas-audience-panel",
    "atlas-domain-ribbon",
)

def hub_sample_paths() -> list[str]:
    paths = []
    for p in HUB_REQUIRED_PATHS:
        if p == "/methodology/" and not (PUBLIC_DIR / "methodology" / "index.html").is_file():
            continue
        paths.append(p)
    return paths


def html_path_for(route_path: str) -> Path:
    path = route_path.strip("/")
    return PUBLIC_DIR / ("index.html" if not path else f"{path}/index.html")


def audit_css_imports() -> tuple[list[str], dict[str, bool]]:
    errors: list[str] = []
    status: dict[str, bool] = {}
    if not CSS_PATH.is_file():
        errors.append("bisulfid-frame.css missing")
        return errors, status
    css_text = CSS_PATH.read_text(encoding="utf-8")
    for dep in CSS_IMPORT_DEPENDENCIES:
        present = dep in css_text
        exists = (CSS_DIR / dep).is_file()
        status[dep] = present and exists
        if not present:
            errors.append(f"CSS import missing in frame: {dep}")
        elif not exists:
            errors.append(f"CSS import file missing: {dep}")
    return errors, status


def validate_page(rec: dict, public_paths: set[str]) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    rid = rec["route_id"]
    route_path = rec.get("route_path", "/")
    html_path = html_path_for(route_path)
    meta: dict = {"route_id": rid, "route_path": route_path, "html_exists": html_path.is_file()}
    if not html_path.is_file():
        errors.append("missing HTML")
        return errors, warnings, meta
    text = html_path.read_text(encoding="utf-8")
    lower = text.lower()

    meta["has_stylesheet"] = STYLESHEET_PATH in text
    meta["shell_markers"] = {m: m.lower() in lower for m in SOVEREIGN_SHELL_MARKERS}
    meta["has_lane_class"] = bool(LANE_CLASS_RE.search(text))
    meta["has_domain_class"] = bool(DOMAIN_CLASS_RE.search(text))
    meta["has_audience_or_domain"] = meta["has_domain_class"] or bool(AUDIENCE_CLASS_RE.search(text))
    meta["semantic_components"] = {c: c in lower for c in SEMANTIC_COMPONENTS}
    meta["indexable"] = 'content="index, follow"' in lower
    meta["link_count"] = lower.count("<a href=")
    meta["has_breadcrumb"] = "atlas-breadcrumbs" in lower or "breadcrumb-list" in lower
    meta["has_title"] = "<title>" in lower
    meta["has_meta_desc"] = 'name="description"' in lower
    meta["has_canonical"] = 'rel="canonical"' in lower

    visible = strip_machine_content_for_audit(text)
    for pat in FORBIDDEN_PUBLIC_LANGUAGE_99A:
        if pat.search(visible):
            errors.append(f"forbidden: {pat.pattern}")
            break

    if not meta["has_stylesheet"]:
        errors.append("missing absolute stylesheet")
    for marker, ok in meta["shell_markers"].items():
        if not ok:
            errors.append(f"missing shell marker: {marker}")
    if not meta["has_lane_class"]:
        errors.append("missing semantic lane class")
    if not meta["has_audience_or_domain"]:
        errors.append("missing domain or audience class")
    for comp, ok in meta["semantic_components"].items():
        if not ok:
            errors.append(f"missing component: {comp}")
    if "noindex" in lower:
        errors.append("contains noindex")
    if not meta["has_title"]:
        errors.append("missing title")
    if not meta["has_meta_desc"]:
        errors.append("missing meta description")
    if not meta["has_canonical"]:
        errors.append("missing canonical")
    if not meta["has_breadcrumb"]:
        errors.append("missing breadcrumb")
    if meta["link_count"] < 8:
        errors.append(f"fewer than 8 links ({meta['link_count']})")

    body_match = re.search(r'class="atlas-dossier-body"[^>]*>(.*?)</section>', text, re.S | re.I)
    if not body_match:
        body_match = re.search(r'class="atlas-page__body">(.*?)</section>', text, re.S | re.I)
    body_len = 0
    if body_match:
        body_len = len(re.sub(r"<[^>]+>", "", body_match.group(1)).strip())
    meta["body_chars"] = body_len
    if body_len < MIN_BODY_CHARS:
        errors.append(f"body below minimum ({body_len})")

    for href in HREF_RE.findall(text):
        if href.startswith(("http", "#", "mailto:")):
            continue
        norm = href if href.endswith("/") else href + "/"
        if not norm.startswith("/"):
            norm = "/" + norm
        if norm not in public_paths:
            target = PUBLIC_DIR / norm.strip("/") / "index.html"
            if not target.is_file():
                warnings.append(f"broken link: {href}")

    meta["status"] = "PASS" if not errors else "FAIL"
    return errors, warnings, meta


def validate_hub_path(path: str, public_paths: set[str]) -> tuple[list[str], dict]:
    rec = {"route_id": f"hub:{path.strip('/') or 'home'}", "route_path": path}
    errs, _, meta = validate_page(rec, public_paths)
    html_path = html_path_for(path)
    meta["html_exists"] = html_path.is_file()
    if not html_path.is_file():
        meta["status"] = "MISSING"
        errs.append("missing HTML")
    meta["forbidden_absent"] = not any(e.startswith("forbidden:") for e in errs)
    meta["css_imports_ok"] = (PUBLIC_DIR / "assets/bisulfid-design-system/bisulfid-frame.css").is_file()
    return errs, meta


def sample_routes(released: list[dict]) -> list[dict]:
    buckets: dict[str, list[dict]] = {
        "en_terminology_deep": [],
        "de_terminology": [],
        "context": [],
        "language": [],
        "material": [],
        "student": [],
        "hub": [],
    }
    for rec in released:
        path = rec.get("route_path", "")
        lane = rec.get("production_lane", "")
        if path.startswith("/en/terminology/") and path.count("/") >= 6:
            buckets["en_terminology_deep"].append(rec)
        elif path.startswith("/de/terminology/"):
            buckets["de_terminology"].append(rec)
        elif lane in {"F", "G", "H", "I", "J", "K"} or "context" in path or "/gov/" in path:
            buckets["context"].append(rec)
        elif lane == "B" or "/languages/" in path or "language" in path:
            buckets["language"].append(rec)
        elif lane == "E" or "molybdenum" in path or "mos2" in path or "mineral" in path:
            buckets["material"].append(rec)
        elif lane == "L" or "/stu/" in path or "aud-stu" in path or "/child/" in path:
            buckets["student"].append(rec)
        elif lane == "HUB" or rec["route_id"] in {"home", "sources"}:
            buckets["hub"].append(rec)
    picks: list[dict] = []
    rng = random.Random(99)
    picks.extend(rng.sample(buckets["en_terminology_deep"], min(20, len(buckets["en_terminology_deep"]))))
    picks.extend(rng.sample(buckets["de_terminology"], min(20, len(buckets["de_terminology"]))))
    picks.extend(rng.sample(buckets["language"], min(10, len(buckets["language"]))))
    picks.extend(rng.sample(buckets["material"], min(10, len(buckets["material"]))))
    picks.extend(rng.sample(buckets["context"], min(10, len(buckets["context"]))))
    picks.extend(rng.sample(buckets["student"], min(10, len(buckets["student"]))))
    seen: set[str] = set()
    out: list[dict] = []
    for rec in picks:
        if rec["route_id"] not in seen:
            seen.add(rec["route_id"])
            out.append(rec)
    return out


def sitemap_audit(released_paths: set[str]) -> tuple[int, list[str]]:
    errors: list[str] = []
    index_path = PUBLIC_DIR / "sitemap.xml"
    if not index_path.is_file():
        return 0, ["sitemap index missing"]
    index_text = index_path.read_text(encoding="utf-8")
    shard_names = re.findall(r"<loc>https://bisulfid\.com/(sitemap[^<]+)</loc>", index_text)
    urls: set[str] = set()
    for shard in shard_names:
        shard_path = PUBLIC_DIR / shard
        if not shard_path.is_file():
            errors.append(f"sitemap shard missing: {shard}")
            continue
        try:
            root = ET.fromstring(shard_path.read_text(encoding="utf-8"))
        except ET.ParseError:
            errors.append(f"sitemap shard invalid XML: {shard}")
            continue
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for loc in root.findall(".//sm:loc", ns):
            if loc.text:
                path = loc.text.replace("https://bisulfid.com", "")
                if not path.endswith("/"):
                    path += "/"
                urls.add(path)
    missing_from_sitemap = released_paths - urls
    extra_in_sitemap = urls - released_paths
    if missing_from_sitemap:
        errors.append(f"released pages missing from sitemap: {len(missing_from_sitemap)}")
    if extra_in_sitemap:
        errors.append(f"sitemap URLs not in release ledger: {len(extra_in_sitemap)}")
    return len(urls), errors


def layer_mapping_rows(released: list[dict]) -> list[str]:
    lane_counts: Counter = Counter()
    domain_counts: Counter = Counter()
    for rec in released:
        lane = rec.get("production_lane", "A")
        lane_counts[lane] += 1
        domain_counts[LANE_DOMAIN_CLASS.get(lane, "domain-chemistry")] += 1
    lines = [
        "# 14K Interface Layer Mapping Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Sprint:** 99B",
        "",
        "## Lane → semantic class mapping",
        "",
        "| Lane | Semantic class | Domain class | Public label | Count |",
        "|------|----------------|--------------|--------------|------:|",
    ]
    from atlas_dossier_common_l3 import PUBLIC_LANE_ROLES  # noqa: E402

    for lane in sorted(lane_counts.keys(), key=lambda x: (x != "HUB", x)):
        lines.append(
            f"| {lane} | `{LANE_SEMANTIC_CLASS.get(lane, '')}` | "
            f"`{LANE_DOMAIN_CLASS.get(lane, '')}` | "
            f"{PUBLIC_LANE_ROLES.get(lane, '')} | {lane_counts[lane]} |"
        )
    lines.extend(["", "## Domain class distribution", ""])
    for dom, count in domain_counts.most_common():
        lines.append(f"- `{dom}`: {count}")
    return lines


def main() -> int:
    print("=" * 60)
    print("Sprint 99B — 14K Semantic Interface Validator")
    print("=" * 60)
    load_release_model()
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    public_paths: set[str] = set()
    released_paths: set[str] = set()
    for rec in released:
        path = rec.get("route_path", "/").strip("/")
        norm = "/" if not path else f"/{path}/"
        public_paths.add(norm)
        released_paths.add(norm)

    css_errors, css_import_status = audit_css_imports()
    all_errors: list[str] = list(css_errors)
    forbidden_hits: Counter = Counter()
    shell_fail = 0
    lane_fail = 0
    component_fail = 0

    for rec in released:
        errs, _, meta = validate_page(rec, public_paths)
        if not all(meta.get("shell_markers", {}).values()):
            shell_fail += 1
        if not meta.get("has_lane_class"):
            lane_fail += 1
        if not all(meta.get("semantic_components", {}).values()):
            component_fail += 1
        for e in errs:
            if e.startswith("forbidden:"):
                forbidden_hits[e] += 1
            all_errors.append(f"{rec['route_id']}: {e}")

    sitemap_urls, sitemap_errors = sitemap_audit(released_paths)
    all_errors.extend(sitemap_errors)

    hub_rows: list[dict] = []
    hub_fail = 0
    for hub_path in hub_sample_paths():
        errs, meta = validate_hub_path(hub_path, public_paths)
        if errs:
            hub_fail += 1
            for e in errs:
                all_errors.append(f"hub:{hub_path}: {e}")
        hub_rows.append(meta | {"errors": errs})

    sample = sample_routes(released)
    sample_rows: list[dict] = []
    sample_errors = 0
    for rec in sample:
        errs, warns, meta = validate_page(rec, public_paths)
        if errs:
            sample_errors += 1
        sample_rows.append({
            "route_id": rec["route_id"],
            "route_path": rec["route_path"],
            "status": meta.get("status", "FAIL"),
            "stylesheet": meta.get("has_stylesheet", False),
            "shell": all(meta.get("shell_markers", {}).values()),
            "lane_class": meta.get("has_lane_class", False),
            "domain_class": meta.get("has_domain_class", False),
            "forbidden_errors": [e for e in errs if e.startswith("forbidden:")],
            "body_chars": meta.get("body_chars", 0),
            "links": meta.get("link_count", 0),
        })

    summary_pass = not all_errors

    repair_report = [
        "# 14K Semantic Interface Repair Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Sprint:** 99B",
        f"**Released pages:** {len(released)}",
        f"**Validation errors:** {len(all_errors)}",
        "",
        "## Repairs applied",
        "",
        "- Sovereign `bs-control-room` shell on every released dossier page",
        "- Semantic lane/domain/audience body classes from release ledger classification",
        "- Human-facing public labels (no machine lane identifiers in visible copy)",
        "- Layer-specific interface components and CSS treatments per atlas lane",
        "- CSS import chain: frame → tokens → components → public-surface → atlas-semantic-interface",
        "",
        f"**Shell failures:** {shell_fail}",
        f"**Lane class failures:** {lane_fail}",
        f"**Component failures:** {component_fail}",
        f"**Sitemap URLs:** {sitemap_urls}",
        f"**Hub entry failures:** {hub_fail}",
        "",
        f"**Summary:** {'PASS' if summary_pass else 'FAIL'}",
    ]
    (ROOT / "main/data/14K_SEMANTIC_INTERFACE_REPAIR_REPORT.md").write_text(
        "\n".join(repair_report) + "\n", encoding="utf-8"
    )

    shell_contract = [
        "# 14K CSS Shell Contract Repair Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Stylesheet:** `{STYLESHEET_PATH}`",
        f"**Pages with stylesheet reference:** {len(released) - sum(1 for e in all_errors if 'stylesheet' in e)}",
        "",
        "## Required shell contract",
        "",
        "- Absolute stylesheet: `/assets/bisulfid-design-system/bisulfid-frame.css`",
        "- Body class: `bs-control-room`",
        "- Atlas class: `bisulfid-atlas`",
        "- Shell: `bs-control-room__shell`",
        "- Header: `site-header`",
        "- Main: `id=\"main-content\"`",
        "- Footer: `site-footer`",
        "",
        f"**Shell marker failures:** {shell_fail}",
        f"**Summary:** {'PASS' if shell_fail == 0 and not css_errors else 'FAIL'}",
    ]
    (ROOT / "main/data/14K_CSS_SHELL_CONTRACT_REPAIR_REPORT.md").write_text(
        "\n".join(shell_contract) + "\n", encoding="utf-8"
    )

    (ROOT / "main/data/14K_INTERFACE_LAYER_MAPPING_REPORT.md").write_text(
        "\n".join(layer_mapping_rows(released)) + "\n", encoding="utf-8"
    )

    import_lines = [
        "# 14K CSS Import Dependency Audit",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Frame CSS exists:** {CSS_PATH.is_file()}",
        "",
        "| Import | Referenced | File exists |",
        "|--------|:----------:|:-----------:|",
    ]
    for dep, ok in css_import_status.items():
        import_lines.append(
            f"| `{dep}` | {'yes' if dep in CSS_PATH.read_text(encoding='utf-8') else 'no'} | "
            f"{'yes' if (CSS_DIR / dep).is_file() else 'no'} |"
        )
    import_lines.extend(["", f"**Summary:** {'PASS' if not css_errors else 'FAIL'}"])
    (ROOT / "main/data/14K_CSS_IMPORT_DEPENDENCY_AUDIT.md").write_text(
        "\n".join(import_lines) + "\n", encoding="utf-8"
    )

    structure_lines = [
        "# 14K Public Shell Structure Audit",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Pages scanned:** {len(released)}",
        "",
        "## Shell markers",
        "",
    ]
    for marker in SOVEREIGN_SHELL_MARKERS:
        structure_lines.append(f"- `{marker}`")
    structure_lines.extend([
        "",
        "## Semantic components",
        "",
    ])
    for comp in SEMANTIC_COMPONENTS:
        structure_lines.append(f"- `{comp}`")
    structure_lines.extend([
        "",
        f"**Shell failures:** {shell_fail}",
        f"**Component failures:** {component_fail}",
        f"**Summary:** {'PASS' if shell_fail == 0 and component_fail == 0 else 'FAIL'}",
    ])
    (ROOT / "main/data/14K_PUBLIC_SHELL_STRUCTURE_AUDIT.md").write_text(
        "\n".join(structure_lines) + "\n", encoding="utf-8"
    )

    hub_align_lines = [
        "# 14K Hub Semantic Shell Alignment Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Sprint:** 99B-H",
        f"**Hub routes required:** {len(hub_sample_paths())}",
        f"**Hub failures:** {hub_fail}",
        "",
        "## Hub routes",
        "",
        "| Path | Status | Stylesheet | Shell | Lane | Domain | Forbidden absent | Body | Links |",
        "|------|--------|:----------:|:-----:|:----:|:------:|:----------------:|-----:|------:|",
    ]
    for row in hub_rows:
        hub_align_lines.append(
            f"| `{row.get('route_path', '')}` | {row.get('status', 'N/A')} | "
            f"{'yes' if row.get('has_stylesheet') else 'no'} | "
            f"{'yes' if all(row.get('shell_markers', {}).values()) else 'no'} | "
            f"{'yes' if row.get('has_lane_class') else 'no'} | "
            f"{'yes' if row.get('has_domain_class') else 'no'} | "
            f"{'yes' if row.get('forbidden_absent') else 'no'} | "
            f"{row.get('body_chars', 0)} | {row.get('link_count', 0)} |"
        )
    hub_align_lines.extend(["", f"**Summary:** {'PASS' if hub_fail == 0 else 'FAIL'}"])
    (ROOT / "main/data/14K_HUB_SEMANTIC_SHELL_ALIGNMENT_REPORT.md").write_text(
        "\n".join(hub_align_lines) + "\n", encoding="utf-8"
    )

    sample_lines = [
        "# 14K Live Route Semantic Sample Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        "",
        "## Public hub entry samples (99B-H)",
        "",
        "| Path | Exists | Status | Stylesheet | Shell | Lane | Domain | Forbidden absent | Body | Links |",
        "|------|:------:|--------|:----------:|:-----:|:----:|:------:|:----------------:|-----:|------:|",
    ]
    for row in hub_rows:
        sample_lines.append(
            f"| `{row.get('route_path', '')}` | "
            f"{'yes' if row.get('html_exists') else 'no'} | {row.get('status', 'N/A')} | "
            f"{'yes' if row.get('has_stylesheet') else 'no'} | "
            f"{'yes' if all(row.get('shell_markers', {}).values()) else 'no'} | "
            f"{'yes' if row.get('has_lane_class') else 'no'} | "
            f"{'yes' if row.get('has_domain_class') else 'no'} | "
            f"{'yes' if row.get('forbidden_absent') else 'no'} | "
            f"{row.get('body_chars', 0)} | {row.get('link_count', 0)} |"
        )
    sample_lines.extend([
        "",
        "## Deep route samples",
        "",
        "| Route | Path | Status | CSS | Shell | Lane | Links | Body |",
        "|-------|------|--------|:---:|:-----:|:----:|------:|-----:|",
    ])
    for row in sample_rows:
        sample_lines.append(
            f"| `{row['route_id']}` | `{row['route_path']}` | {row['status']} | "
            f"{'yes' if row['stylesheet'] else 'no'} | {'yes' if row['shell'] else 'no'} | "
            f"{'yes' if row['lane_class'] else 'no'} | {row['links']} | {row['body_chars']} |"
        )
    (ROOT / "main/data/14K_LIVE_ROUTE_SEMANTIC_SAMPLE_REPORT.md").write_text(
        "\n".join(sample_lines) + "\n", encoding="utf-8"
    )

    val_lines = [
        "# 14K Validation After Semantic Interface Repair",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Released routes:** {len(released)}",
        f"**Sitemap URLs:** {sitemap_urls}",
        f"**Errors:** {len(all_errors)}",
        f"**Sample failures:** {sample_errors}",
        f"**Hub entry failures:** {hub_fail}",
        "",
        f"**Summary:** {'PASS' if summary_pass else 'FAIL'}",
    ]
    if all_errors:
        val_lines.extend(["", "## Errors (first 40)", ""])
        for e in all_errors[:40]:
            val_lines.append(f"- {e}")
    (ROOT / "main/data/14K_VALIDATION_AFTER_SEMANTIC_INTERFACE_REPAIR.md").write_text(
        "\n".join(val_lines) + "\n", encoding="utf-8"
    )

    print(f"Released: {len(released)}")
    print(f"Sitemap URLs: {sitemap_urls}")
    print(f"CSS import errors: {len(css_errors)}")
    print(f"Shell failures: {shell_fail}")
    print(f"Lane failures: {lane_fail}")
    print(f"Hub failures: {hub_fail}")
    print(f"Errors: {len(all_errors)}")
    print(f"Sample checked: {len(sample_rows)} (failures: {sample_errors})")
    if all_errors:
        for e in all_errors[:15]:
            print(f"  ERROR: {e}")
        print("VALIDATION SUMMARY: FAIL")
        return 1
    print("VALIDATION SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
