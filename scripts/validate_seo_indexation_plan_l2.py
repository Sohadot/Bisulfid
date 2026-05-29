#!/usr/bin/env python3
"""L2 SEO and indexation plan validator — read-only, stdlib only (Sprint 5O-A)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEO_MODEL_PATH = ROOT / "main/data/CORPUS_PRODUCTION_SEO_INDEXATION_MODEL.md"
ROUTES_PATH = ROOT / "main/data/routes.json"
SITEMAP_PATH = ROOT / "main/data/sitemap_policy.json"
THRESHOLD_PATH = ROOT / "main/data/CORPUS_LAUNCH_THRESHOLD.md"

REQUIRED_TOPICS = (
    "seo metadata",
    "title",
    "description",
    "canonical",
    "sitemap lock",
    "indexation lock",
    "noindex",
    "anti-thin",
    "structured data",
    "500",
)

FORBIDDEN = (
    re.compile(r"indexable\s*:\s*true\s+before\s+publication", re.I),
    re.compile(r"random\s+seo\s+expansion\s+allowed", re.I),
    re.compile(r"route\s+count\s+(equals|is)\s+seo\s+quality", re.I),
    re.compile(r"thin\s+seo\s+pages?\s+allowed", re.I),
)


def run_validation() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SEO_MODEL_PATH.exists():
        errors.append("Missing CORPUS_PRODUCTION_SEO_INDEXATION_MODEL.md")
        return errors, warnings

    text = SEO_MODEL_PATH.read_text(encoding="utf-8")
    lower = text.lower()

    for topic in REQUIRED_TOPICS:
        if topic not in lower:
            errors.append(f"SEO/indexation model missing topic: {topic}")

    for pat in FORBIDDEN:
        if pat.search(text):
            errors.append(f"Forbidden SEO plan pattern: {pat.pattern}")

    if ROUTES_PATH.exists():
        routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
        for route in routes:
            rid = route["route_id"]
            if route.get("indexable") is True:
                errors.append(f"{rid}: indexable true before publication gates")
            if route.get("in_sitemap") is True:
                errors.append(f"{rid}: in_sitemap true before publication gates")

    if SITEMAP_PATH.exists():
        sm = json.loads(SITEMAP_PATH.read_text(encoding="utf-8"))
        if sm.get("urls"):
            errors.append("sitemap_policy.json contains active urls before launch gates")
        if sm.get("status") not in ("inactive", "planned", None):
            warnings.append(f"sitemap_policy status is {sm.get('status')!r}")

    if THRESHOLD_PATH.exists():
        th = THRESHOLD_PATH.read_text(encoding="utf-8")
        if "500" not in th:
            errors.append("Launch threshold doc missing 500-page sitemap/indexation gate")
    else:
        errors.append("CORPUS_LAUNCH_THRESHOLD.md missing")

    if "metadata" not in lower or "before publication" not in lower.replace("pre-publication", "before publication"):
        warnings.append("SEO model should require metadata before publication")

    return errors, warnings


def main() -> int:
    errors, warnings = run_validation()
    print("=== SEO Indexation Plan L2 Validation ===")
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
