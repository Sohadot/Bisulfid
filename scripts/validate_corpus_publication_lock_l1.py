#!/usr/bin/env python3
"""L1 publication lock validator — read-only, stdlib only (Sprint 5K)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
SITEMAP_PATH = ROOT / "main/data/sitemap_policy.json"
NAV_PATHS = (ROOT / "main/data/navigation.json", ROOT / "main/config/navigation.json")
THRESHOLD_PATH = ROOT / "main/data/CORPUS_LAUNCH_THRESHOLD.md"

LAUNCH_NOW = re.compile(
    r"(?<!not )(?<!non-)(ready for public launch|public launch now|launch now|go live now|publish now)",
    re.I,
)
HTML_OUTPUT_DIRS = ("site", "public", "dist", "output", "build")


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"route_count": 0, "published_routes": 0}

    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    stats["route_count"] = len(routes)

    for route in routes:
        rid = route["route_id"]
        if route.get("status") == "published":
            stats["published_routes"] += 1
            errors.append(f"{rid}: route status is published")
        if route.get("status") != "planned":
            errors.append(f"{rid}: route status must be planned (got {route.get('status')!r})")
        for flag in ("indexable", "in_sitemap", "in_navigation"):
            if route.get(flag) is True:
                errors.append(f"{rid}: {flag} is true")

    if SITEMAP_PATH.exists():
        sm = json.loads(SITEMAP_PATH.read_text(encoding="utf-8"))
        if sm.get("status") not in ("inactive", "planned"):
            warnings.append(f"sitemap_policy status is {sm.get('status')!r}")
        if sm.get("urls"):
            errors.append("sitemap_policy.json contains active urls")
    else:
        warnings.append("sitemap_policy.json not found")

    nav_found = False
    for nav_path in NAV_PATHS:
        if nav_path.exists():
            nav_found = True
            nav = json.loads(nav_path.read_text(encoding="utf-8"))
            if nav.get("status") not in ("inactive", "planned"):
                warnings.append(f"{nav_path.name} status is {nav.get('status')!r}")
            if nav.get("items"):
                errors.append(f"{nav_path.name} contains navigation items")
    if not nav_found:
        warnings.append("navigation.json not found at expected paths")

    for dirname in HTML_OUTPUT_DIRS:
        d = ROOT / dirname
        if not d.is_dir():
            continue
        html_files: list[Path] = []
        for path in d.rglob("*.html"):
            if dirname == "site":
                try:
                    rel = path.relative_to(d)
                except ValueError:
                    html_files.append(path)
                    continue
                if len(rel.parts) >= 1 and rel.parts[0] in ("_sample", "public"):
                    continue
            html_files.append(path)
        if html_files:
            errors.append(
                f"Generated HTML found in {dirname}/ outside quarantine "
                f"({len(html_files)} files)"
            )

    if THRESHOLD_PATH.exists():
        th = THRESHOLD_PATH.read_text(encoding="utf-8").lower()
        if "500" not in th:
            warnings.append("CORPUS_LAUNCH_THRESHOLD.md may not reference 500-page threshold")
    else:
        warnings.append("CORPUS_LAUNCH_THRESHOLD.md not found")

    backed = 0
    for route in routes:
        cf = ROOT / route["content_file"]
        if not cf.exists():
            continue
        backed += 1
        text = cf.read_text(encoding="utf-8")
        if LAUNCH_NOW.search(text):
            errors.append(f"{route['route_id']}: content claims public launch readiness")
        lower = text.lower()
        if "publication-ready" in lower.replace("not publication-ready", ""):
            if "not publication-ready" not in lower and "nicht veröffentlichungsreif" not in lower:
                errors.append(f"{route['route_id']}: content claims publication-ready")

    stats["draft_backed"] = backed
    stats["threshold_enforced"] = stats["route_count"] < 500

    if stats["route_count"] >= 500 and stats["published_routes"] == 0:
        pass  # pre-launch OK
    elif stats["route_count"] < 500:
        stats["below_500_threshold"] = True

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Corpus Publication Lock L1 Validation ===")
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
