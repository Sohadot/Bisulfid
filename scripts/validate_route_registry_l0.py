#!/usr/bin/env python3
"""Read-only L0 validator for main/data/routes.json (Sprint 5I-B).

Uses Python standard library only. Does not modify any files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main" / "data" / "routes.json"

REQUIRED_FIELDS = (
    "route_id",
    "path",
    "language",
    "locale",
    "source_language",
    "title",
    "description",
    "h1",
    "layer",
    "template",
    "content_file",
    "status",
    "indexable",
    "in_sitemap",
    "in_navigation",
    "hreflang_group",
    "required_internal_links",
    "required_claim_groups",
    "source_required",
    "risk_level",
)

FORBIDDEN_KEYWORDS = (
    "cagr",
    "market_share",
    "market-share",
    "procurement",
    "handling instruction",
    "dosage",
    "acquisition-target",
    "newsletter",
    "acquire",
)

WAVE1_MARKER = "Sprint 5I-B wave 1"


def load_routes() -> tuple[list[dict], list[str]]:
    errors: list[str] = []
    try:
        raw = ROUTES_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        return [], [f"Cannot read routes.json: {exc}"]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return [], [f"routes.json is not valid JSON: {exc}"]

    routes = data.get("routes")
    if not isinstance(routes, list):
        return [], ["routes.json must contain a 'routes' array"]
    return routes, errors


def validate_content_file_pattern(route: dict) -> str | None:
    lang = route.get("language")
    content_file = route.get("content_file", "")
    if lang == "en" and not content_file.startswith("main/content/en/pages/"):
        return f"{route['route_id']}: EN content_file must start with main/content/en/pages/"
    if lang == "de" and not content_file.startswith("main/content/de/pages/"):
        return f"{route['route_id']}: DE content_file must start with main/content/de/pages/"
    if lang in {"ar", "zh", "ja"}:
        prefix = f"main/content/{lang}/pages/"
        if not content_file.startswith(prefix):
            return f"{route['route_id']}: {lang} content_file must start with {prefix}"
    if not content_file.endswith(".md"):
        return f"{route['route_id']}: content_file must end with .md"
    return None


def scan_forbidden(route: dict) -> list[str]:
    hits: list[str] = []
    fields = (
        route.get("route_id", ""),
        route.get("path", ""),
        route.get("title", ""),
        route.get("description", ""),
        route.get("h1", ""),
    )
    blob = " ".join(str(f) for f in fields).lower()
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in blob:
            hits.append(f"{route['route_id']}: forbidden keyword '{keyword}'")
    return hits


def main() -> int:
    routes, fatal = load_routes()
    warnings: list[str] = []
    errors = list(fatal)

    if not errors:
        ids = [r.get("route_id") for r in routes]
        paths = [r.get("path") for r in routes]

        for rid in ids:
            if ids.count(rid) > 1:
                errors.append(f"Duplicate route_id: {rid}")
        for path in paths:
            if paths.count(path) > 1:
                errors.append(f"Duplicate path: {path}")

        for route in routes:
            rid = route.get("route_id", "<unknown>")
            for field in REQUIRED_FIELDS:
                if field not in route:
                    errors.append(f"{rid}: missing required field '{field}'")

            if route.get("status") != "planned":
                errors.append(f"{rid}: status must be 'planned', got {route.get('status')!r}")
            if route.get("indexable") is True:
                errors.append(f"{rid}: indexable must be false")
            if route.get("in_sitemap") is True:
                errors.append(f"{rid}: in_sitemap must be false")
            if route.get("in_navigation") is True:
                errors.append(f"{rid}: in_navigation must be false")

            pattern_err = validate_content_file_pattern(route)
            if pattern_err:
                errors.append(pattern_err)

            for hit in scan_forbidden(route):
                if WAVE1_MARKER in route.get("notes", ""):
                    errors.append(hit)
                else:
                    warnings.append(hit + " (pre-existing route; review separately)")

        wave1_routes = [r for r in routes if WAVE1_MARKER in r.get("notes", "")]
        for route in wave1_routes:
            cf = route.get("content_file", "")
            cf_path = ROOT / cf
            if cf_path.exists():
                warnings.append(
                    f"{route['route_id']}: content_file already exists on disk: {cf}"
                )

    wave1_count = sum(1 for r in routes if WAVE1_MARKER in r.get("notes", ""))
    total = len(routes)

    print("=== Route Registry L0 Validation ===")
    print(f"File: {ROUTES_PATH.relative_to(ROOT)}")
    print(f"Date: {date.today().isoformat()}")
    print(f"Routes total: {total}")
    print(f"Wave 1 routes (marker in notes): {wave1_count}")
    print()

    if errors:
        print("FAIL — errors:")
        for err in errors:
            print(f"  - {err}")
    else:
        print("PASS — no blocking errors")

    if warnings:
        print()
        print("Warnings:")
        for warn in warnings:
            print(f"  - {warn}")

    print()
    print(f"Summary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
