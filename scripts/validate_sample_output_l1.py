#!/usr/bin/env python3
"""L1 quarantined sample output validator — read-only, stdlib only (Sprint 6M-B).

Validates:
  1. No HTML exists under site/ outside the quarantined site/_sample/ path.
  2. Quarantined sample HTML under site/_sample/ meets non-public QA markers.

Does not modify files.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
SAMPLE_DIR = SITE_DIR / "_sample"

ALLOWED_NON_HTML = (
    SITE_DIR / ".gitkeep",
    SAMPLE_DIR / ".gitkeep",
)

REQUIRED_MARKERS = (
    "noindex",
    "nofollow",
    "NOT A LAUNCH",
    "14,000",
    "non_public",
    "non-public",
    "planned",
    "outside sitemap",
    "outside navigation",
    "no_claims_approved",
)

# QA sample (6M-C) or RC batch (6M-D) posture marker — at least one required
POSTURE_MARKERS = ("QA", "release candidate")

SOURCE_CLAIM_MARKERS = (
    "[SOURCE REQUIRED]",
    "source approval not implied",
    "no source approval",
    "unapproved",
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
        "no claims_approved",
        "no_claims_approved",
        "no approved claim is implied",
        "no science claim is approved",
        "no science or industry claim is approved",
        "no industry claim is approved",
        "none approved today",
        "not approved claim is implied",
    ):
        lower = lower.replace(phrase, "")
    return "claim is approved" in lower


def implies_source_locking_complete(text: str) -> bool:
    lower = strip_html_tags(text).lower()
    if not re.search(r"source-locking is complete", lower):
        return False
    if re.search(r"(?:does|do)\s+not\s+claim\s+source-locking is complete", lower):
        return False
    if re.search(r"not\s+claim\s+source-locking is complete", lower):
        return False
    return True


FORBIDDEN = (
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"(?<!not )(?<!non-)(ready for (public )?launch|go live now)", re.I),
)


def is_allowed_html(path: Path) -> bool:
    """HTML is allowed only under site/_sample/."""
    try:
        rel = path.relative_to(SITE_DIR)
    except ValueError:
        return False
    parts = rel.parts
    return len(parts) >= 2 and parts[0] == "_sample" and path.suffix.lower() == ".html"


def find_disallowed_html() -> list[Path]:
    if not SITE_DIR.is_dir():
        return []
    disallowed: list[Path] = []
    for path in SITE_DIR.rglob("*.html"):
        if not is_allowed_html(path):
            disallowed.append(path)
    return disallowed


def validate_sample_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    for marker in REQUIRED_MARKERS:
        if marker.lower() not in lower and marker not in text:
            errors.append(f"{path.name}: missing marker {marker!r}")

    if not any(m.lower() in lower or m in text for m in POSTURE_MARKERS):
        errors.append(f"{path.name}: missing QA or release candidate posture marker")

    if "release candidate" in lower or "rc-batch" in lower:
        if "not publication-ready" not in lower:
            errors.append(f"{path.name}: RC batch missing not publication-ready marker")

    for pattern in FORBIDDEN:
        if pattern.search(text):
            errors.append(f"{path.name}: forbidden pattern in sample output")

    if implies_claim_approval(text):
        errors.append(f"{path.name}: implies claim approval")

    if implies_source_locking_complete(text):
        errors.append(f"{path.name}: implies source-locking complete")

    if "production_can_safely_proceed: yes" in lower.replace(" ", ""):
        errors.append(f"{path.name}: claims production_can_safely_proceed yes")

    if "route_status" not in lower and "route status" not in lower:
        errors.append(f"{path.name}: missing route status visibility")

    has_source_marker = any(m.lower() in lower for m in SOURCE_CLAIM_MARKERS)
    if "[source required]" in lower and not has_source_marker:
        errors.append(f"{path.name}: [SOURCE REQUIRED] not visibly preserved")

    if "claim approval not implied" not in lower and "no_claims_approved" not in lower:
        warnings.append(f"{path.name}: claim non-approval posture could be clearer")

    return errors, warnings


def main() -> int:
    print("=" * 60)
    print("Bisulfid Sample Output Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Site dir: {SITE_DIR}")
    print(f"Sample dir: {SAMPLE_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []
    all_warnings: list[str] = []

    disallowed = find_disallowed_html()
    print("--- site/ HTML scan (outside _sample) ---")
    if disallowed:
        for path in disallowed:
            rel = path.relative_to(ROOT)
            all_errors.append(f"public HTML outside quarantine: {rel}")
            print(f"  DISALLOWED: {rel}")
    else:
        print("  No HTML outside site/_sample/")
    print()

    sample_html = list(SAMPLE_DIR.glob("*.html")) if SAMPLE_DIR.is_dir() else []
    print("--- site/_sample/ quarantined HTML ---")
    if not sample_html:
        print("  No quarantined sample HTML (allowed: .gitkeep only)")
    else:
        for path in sample_html:
            print(f"  Checked: {path.relative_to(ROOT)}")
            errs, warns = validate_sample_file(path)
            all_errors.extend(errs)
            all_warnings.extend(warns)
    print()

    allowed_present = [p for p in ALLOWED_NON_HTML if p.is_file()]
    print(f"--- Allowed placeholders: {len(allowed_present)} ---")
    for p in allowed_present:
        print(f"  {p.relative_to(ROOT)}")
    print()

    if all_warnings:
        print("--- Warnings ---")
        for w in all_warnings:
            print(f"  WARN: {w}")
        print()

    if all_errors:
        print("--- Errors ---")
        for e in all_errors:
            print(f"  ERROR: {e}")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    if sample_html:
        print(f"VALIDATION SUMMARY: PASS ({len(sample_html)} quarantined QA file(s))")
    else:
        print("VALIDATION SUMMARY: PASS (no HTML; quarantine placeholders only)")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
