#!/usr/bin/env python3
"""L1 route registry validator — read-only, stdlib only (Sprint 5K)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"

REQUIRED_FIELDS = (
    "route_id", "path", "language", "locale", "source_language", "title", "description",
    "h1", "layer", "template", "content_file", "status", "indexable", "in_sitemap",
    "in_navigation", "hreflang_group", "required_internal_links", "required_claim_groups",
    "source_required", "risk_level",
)

FORBIDDEN_KEYWORDS = (
    "cagr", "market_share", "market-share", "procurement advice", "handling instruction",
    "dosage", "acquisition-target", "medical advice", "market report",
)

PUBLIC_LAUNCH_LANG = (
    "ready for public launch", "public launch now", "launch now", "go live",
    "published and indexable", "now indexable",
)

PRE_EXISTING_FORGIVEN = frozenset({
    "industrial_sulfur_systems", "sulfur_safety_context", "hydrogen_sulfide_risk",
    "newsletter", "acquire", "sodium_bisulfide", "sds_and_sulfur_terms",
})


COHORT02_CONTENT_PREFIX = "main/content/en/pages/cohort-02-terminology/"


def validate_content_file_pattern(route: dict) -> str | None:
    lang = route.get("language")
    cf = route.get("content_file", "")
    if lang == "en" and not cf.startswith("main/content/en/pages/"):
        return f"{route['route_id']}: EN content_file prefix invalid"
    if lang == "de" and not cf.startswith("main/content/de/pages/"):
        return f"{route['route_id']}: DE content_file prefix invalid"
    if lang in {"ar", "zh", "ja"} and not cf.startswith(f"main/content/{lang}/pages/"):
        return f"{route['route_id']}: {lang} content_file prefix invalid"
    if not cf.endswith(".md"):
        return f"{route['route_id']}: content_file must end with .md"
    slug = cf.split("/")[-1].replace(".md", "")
    if cf.startswith(COHORT02_CONTENT_PREFIX):
        if not re.match(r"^[a-z0-9][a-z0-9_\-]*$", slug):
            return f"{route['route_id']}: content_file slug discipline ({slug})"
    elif not re.match(r"^[a-z0-9][a-z0-9\-]*$", slug) and slug not in ("de",):
        return f"{route['route_id']}: content_file slug discipline ({slug})"
    return None


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {}

    try:
        data = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"routes.json: {exc}"], [], {}

    routes = data.get("routes")
    if not isinstance(routes, list):
        return ["routes.json missing routes array"], [], {}

    stats["route_count"] = len(routes)
    stats["draft_backed_count"] = sum(
        1 for r in routes if (ROOT / r.get("content_file", "")).exists()
    )
    stats["missing_drafts"] = stats["route_count"] - stats["draft_backed_count"]

    ids = [r.get("route_id") for r in routes]
    paths = [r.get("path") for r in routes]
    cfs = [r.get("content_file") for r in routes]

    for rid in set(ids):
        if ids.count(rid) > 1:
            errors.append(f"Duplicate route_id: {rid}")
    for path in set(paths):
        if paths.count(path) > 1:
            errors.append(f"Duplicate path: {path}")
    for cf in set(cfs):
        if cfs.count(cf) > 1:
            errors.append(f"Duplicate content_file: {cf}")

    for route in routes:
        rid = route.get("route_id", "<unknown>")
        for field in REQUIRED_FIELDS:
            if field not in route:
                errors.append(f"{rid}: missing field '{field}'")

        if route.get("status") != "planned":
            errors.append(f"{rid}: status must be planned")
        for flag in ("indexable", "in_sitemap", "in_navigation"):
            if route.get(flag) is True:
                errors.append(f"{rid}: {flag} must be false")

        err = validate_content_file_pattern(route)
        if err:
            errors.append(err)

        blob = " ".join(
            str(route.get(k, "")) for k in ("route_id", "path", "title", "description", "h1", "notes")
        ).lower()
        for phrase in PUBLIC_LAUNCH_LANG:
            if phrase in blob and "not " not in blob[max(0, blob.find(phrase) - 20): blob.find(phrase)]:
                errors.append(f"{rid}: forbidden public-launch language '{phrase}'")

        for kw in FORBIDDEN_KEYWORDS:
            if kw in blob:
                if rid in PRE_EXISTING_FORGIVEN or "Sprint 5I-B wave 1" not in route.get("notes", ""):
                    warnings.append(f"{rid}: forbidden keyword '{kw}' (pre-existing or review)")
                else:
                    errors.append(f"{rid}: forbidden keyword '{kw}'")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Corpus Routes L1 Validation ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print()
    if errors:
        print("FAIL — errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("PASS — no blocking errors")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    print(f"\nSummary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
