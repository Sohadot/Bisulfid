#!/usr/bin/env python3
"""Sprint 98 — Validate atlas public release quality."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "main/data/release_ledger.json"
PUBLIC_DIR = ROOT / "site/public"
ROUTES_PATH = ROOT / "main/data/routes.json"

FORBIDDEN = [
    re.compile(r"\[SOURCE REQUIRED\]", re.I),
    re.compile(r"noindex", re.I),
    re.compile(r"planned route;\s*non-public", re.I),
    re.compile(r"not publication-ready", re.I),
    re.compile(r"\bCAGR\b"),
    re.compile(r"\bprocurement\b", re.I),
]


def main() -> int:
    print("=" * 60)
    print("Sprint 98 — Atlas Public Release Validator")
    print("=" * 60)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    routes_by_id = {r["route_id"]: r for r in json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]}
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    errors = []
    for rec in released:
        rid = rec["route_id"]
        route = routes_by_id[rid]
        raw_path = route.get("path", "/").strip("/")
        html_path = PUBLIC_DIR / ("index.html" if not raw_path else f"{raw_path}/index.html")
        if not html_path.is_file():
            errors.append(f"{rid}: missing HTML at {html_path}")
            continue
        text = html_path.read_text(encoding="utf-8")
        lower = text.lower()
        if "<title>" not in lower:
            errors.append(f"{rid}: missing title")
        if 'name="description"' not in lower:
            errors.append(f"{rid}: missing meta description")
        if 'rel="canonical"' not in lower:
            errors.append(f"{rid}: missing canonical")
        if "noindex" in lower:
            errors.append(f"{rid}: contains noindex")
        for pat in FORBIDDEN:
            if pat.search(text):
                errors.append(f"{rid}: forbidden pattern {pat.pattern}")
        link_count = text.lower().count("<a href=")
        if link_count < 6:
            errors.append(f"{rid}: fewer than 6 internal links ({link_count})")
    sitemap = PUBLIC_DIR / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("sitemap.xml missing")
    robots = PUBLIC_DIR / "robots.txt"
    if not robots.is_file() or "sitemap" not in robots.read_text(encoding="utf-8").lower():
        errors.append("robots.txt missing or no sitemap reference")
    print(f"Released routes checked: {len(released)}")
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        print("VALIDATION SUMMARY: FAIL")
        return 1
    print("VALIDATION SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
