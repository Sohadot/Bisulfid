#!/usr/bin/env python3
"""L1 public output validator — read-only, stdlib only (Sprint 6M-G).

Validates controlled public HTML under site/public/ only.
Ensures no unsafe leakage, no uncontrolled sitemap/navigation/indexation exposure,
and no false source/claim approval implication.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
PUBLIC_DIR = SITE_DIR / "public"
SAMPLE_DIR = SITE_DIR / "_sample"
ROUTES_PATH = ROOT / "main/data/routes.json"

ALLOWED_PUBLIC_ROOTS = frozenset({"public", "_sample"})

FORBIDDEN = (
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"<script\s+src=", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
)

GOVERNANCE_MARKERS = (
    "noindex",
    "nofollow",
    "data-route-id",
    "data-publication-posture",
)


def strip_html_tags(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))


def implies_claim_approval(text: str) -> bool:
    lower = strip_html_tags(text).lower()
    for phrase in (
        "no claim is approved",
        "any claim is approved",
        "not imply any claim is approved",
        "not imply claim approval",
        "no_claims_approved",
        "no claims_approved",
        "claim approval not implied",
    ):
        lower = lower.replace(phrase, "")
    return "claim is approved" in lower


def implies_source_approval(text: str) -> bool:
    lower = text.lower()
    if "source approval not implied" in lower or "no source approval" in lower:
        return False
    if "sources and claims remain unapproved" in lower:
        return False
    return bool(re.search(r"source(?:s)?\s+(?:is|are)\s+approved", lower))


def find_unsafe_html_outside_allowed() -> list[str]:
    if not SITE_DIR.is_dir():
        return []
    errors: list[str] = []
    for path in SITE_DIR.rglob("*.html"):
        try:
            rel = path.relative_to(SITE_DIR)
        except ValueError:
            errors.append(str(path))
            continue
        if not rel.parts:
            errors.append(str(rel))
            continue
        if rel.parts[0] not in ALLOWED_PUBLIC_ROOTS:
            errors.append(str(rel))
    return errors


def find_uncontrolled_artifacts() -> list[str]:
    errors: list[str] = []
    for name in ("sitemap.xml", "sitemap_index.xml", "navigation.html"):
        for path in SITE_DIR.rglob(name):
            try:
                rel = path.relative_to(SITE_DIR)
            except ValueError:
                errors.append(str(path))
                continue
            if rel.parts and rel.parts[0] == "public":
                errors.append(f"uncontrolled artifact under public: {rel}")
            elif rel.parts and rel.parts[0] not in ALLOWED_PUBLIC_ROOTS:
                errors.append(f"uncontrolled artifact: {rel}")
    return errors


def validate_public_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    for marker in GOVERNANCE_MARKERS:
        if marker.lower() not in lower and marker not in text:
            errors.append(f"{path}: missing governance marker {marker!r}")

    for pattern in FORBIDDEN:
        if pattern.search(text):
            errors.append(f"{path}: forbidden pattern {pattern.pattern}")

    if implies_claim_approval(text):
        errors.append(f"{path}: implies claim approval")
    if implies_source_approval(text):
        errors.append(f"{path}: implies source approval")

    if "in_sitemap_flag" in text and 'content="true"' in lower:
        if 'name="in_sitemap_flag"' in lower or "in_sitemap_flag" in lower:
            if re.search(r"in_sitemap_flag[^>]*content\s*=\s*[\"']true[\"']", text, re.I):
                errors.append(f"{path}: in_sitemap_flag true in public output")

    if re.search(r"robots[^>]*content\s*=\s*[\"']index,\s*follow[\"']", text, re.I):
        errors.append(f"{path}: index,follow robots directive")

    return errors


def main() -> int:
    print("=" * 60)
    print("Bisulfid Public Output Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Public dir: {PUBLIC_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []

    unsafe = find_unsafe_html_outside_allowed()
    if unsafe:
        all_errors.append(f"HTML outside allowed areas ({len(unsafe)}): {unsafe[:5]}")

    uncontrolled = find_uncontrolled_artifacts()
    if uncontrolled:
        all_errors.extend(uncontrolled)

    if not PUBLIC_DIR.is_dir():
        all_errors.append("site/public/ missing")
        print("VALIDATION SUMMARY: FAIL")
        for e in all_errors:
            print(f"  ERROR: {e}")
        return 1

    public_files = sorted(PUBLIC_DIR.rglob("index.html"))
    rel_paths = [str(p.relative_to(ROOT)).replace("\\", "/") for p in public_files]
    if len(rel_paths) != len(set(rel_paths)):
        all_errors.append("duplicate public output paths detected")

    sample_checked = min(50, len(public_files))
    for path in public_files[:sample_checked]:
        all_errors.extend(validate_public_file(path))

    print(f"Public output pages: {len(public_files)}")
    print(f"Sample validated: {sample_checked}")
    print(f"Unsafe leakage paths: {len(unsafe)}")
    print(f"Uncontrolled artifacts: {len(uncontrolled)}")
    print()

    if all_errors:
        print("--- Errors ---")
        for e in all_errors[:30]:
            print(f"  ERROR: {e}")
        if len(all_errors) > 30:
            print(f"  ... and {len(all_errors) - 30} more")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print("VALIDATION SUMMARY: PASS")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
