#!/usr/bin/env python3
"""L1 quarantined sample output validator — read-only, stdlib only (Sprint 6M-B).

Validates site/_sample/ QA artifacts are non-public engineering proofs only.
Does not modify files.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DIR = ROOT / "site/_sample"

REQUIRED_MARKERS = (
    "noindex",
    "nofollow",
    "NOT A LAUNCH",
    "14,000",
    "non_public",
    "non-public",
    "QA",
)

FORBIDDEN = (
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"(?<!not )(?<!non-)(ready for (public )?launch|go live now)", re.I),
)


def validate_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    for marker in REQUIRED_MARKERS:
        if marker.lower() not in lower and marker not in text:
            errors.append(f"{path.name}: missing marker {marker!r}")

    for pattern in FORBIDDEN:
        if pattern.search(text):
            errors.append(f"{path.name}: forbidden pattern in sample output")

    if "production_can_safely_proceed: yes" in lower.replace(" ", ""):
        errors.append(f"{path.name}: claims production_can_safely_proceed yes")

    return errors, warnings


def main() -> int:
    print("=" * 60)
    print("Bisulfid Sample Output Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Sample dir: {SAMPLE_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    if not SAMPLE_DIR.is_dir():
        print("No sample directory — skip (optional QA artifacts)")
        print("VALIDATION SUMMARY: PASS (no samples)")
        return 0

    html_files = list(SAMPLE_DIR.glob("*.html"))
    if not html_files:
        print("No HTML in _sample — skip")
        print("VALIDATION SUMMARY: PASS (no samples)")
        return 0

    all_errors: list[str] = []
    all_warnings: list[str] = []
    for path in html_files:
        errs, warns = validate_file(path)
        all_errors.extend(errs)
        all_warnings.extend(warns)
        print(f"Checked: {path.relative_to(ROOT)}")

    print()
    if all_warnings:
        for w in all_warnings:
            print(f"  WARN: {w}")
    if all_errors:
        for e in all_errors:
            print(f"  ERROR: {e}")
        print("VALIDATION SUMMARY: FAIL")
        return 1

    print(f"VALIDATION SUMMARY: PASS ({len(html_files)} quarantined QA file(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
