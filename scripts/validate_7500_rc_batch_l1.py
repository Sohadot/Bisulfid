#!/usr/bin/env python3
"""L1 7,500-page RC batch validator — read-only, stdlib only (Sprint 6M-F).

Validates quarantined non-public 7,500-page RC HTML under site/_sample/ only.
Does not modify files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
SAMPLE_DIR = SITE_DIR / "_sample"
MANIFEST_PATH = SAMPLE_DIR / "rc_batch_manifest.json"
ROUTES_PATH = ROOT / "main/data/routes.json"

RC_7500_EXACT = 7500

REQUIRED_MARKERS = (
    "noindex",
    "nofollow",
    "NOT A LAUNCH",
    "14,000",
    "non_public",
    "non-public",
    "release candidate",
    "planned",
    "outside sitemap",
    "outside navigation",
    "not publication-ready",
    "no_claims_approved",
)

FORBIDDEN = (
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"(?<!not )(?<!non-)(ready for (public )?launch|go live now)", re.I),
    re.compile(r"<script\s+src=", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
    re.compile(r"sitemap\.xml", re.I),
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


def implies_source_approval(text: str) -> bool:
    lower = text.lower()
    if "source approval not implied" in lower or "no source approval" in lower:
        return False
    if "sources and claims remain unapproved" in lower:
        return False
    return bool(re.search(r"source(?:s)?\s+(?:is|are)\s+approved", lower))


def find_disallowed_html() -> list[Path]:
    if not SITE_DIR.is_dir():
        return []
    disallowed: list[Path] = []
    for path in SITE_DIR.rglob("*.html"):
        try:
            rel = path.relative_to(SITE_DIR)
        except ValueError:
            disallowed.append(path)
            continue
        if not (len(rel.parts) >= 1 and rel.parts[0] == "_sample"):
            disallowed.append(path)
    return disallowed


def validate_rc_file(path: Path, manifest_page: dict | None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    for marker in REQUIRED_MARKERS:
        if marker.lower() not in lower and marker not in text:
            errors.append(f"{path.name}: missing marker {marker!r}")

    for pattern in FORBIDDEN:
        if pattern.search(text):
            errors.append(f"{path.name}: forbidden pattern {pattern.pattern}")

    if implies_claim_approval(text):
        errors.append(f"{path.name}: implies claim approval")
    if implies_source_locking_complete(text):
        errors.append(f"{path.name}: implies source-locking complete")
    if implies_source_approval(text):
        errors.append(f"{path.name}: implies source approval")

    if "production_can_safely_proceed: yes" in lower.replace(" ", ""):
        errors.append(f"{path.name}: claims production_can_safely_proceed yes")

    if manifest_page and manifest_page.get("source_required_visible") == "yes":
        if "[source required]" not in lower and "source-required-marker" not in lower:
            errors.append(f"{path.name}: source-required page missing [SOURCE REQUIRED] visibility")

    return errors, warnings


def main() -> int:
    print("=" * 60)
    print("Bisulfid 7,500-Page RC Batch Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Sample dir: {SAMPLE_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []

    if not MANIFEST_PATH.is_file():
        all_errors.append("rc_batch_manifest.json missing under site/_sample/")
        manifest = None
    else:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    manifest_by_output: dict[str, dict] = {}
    if manifest:
        for page in manifest.get("pages", []):
            manifest_by_output[page.get("output_path", "").split("/")[-1]] = page
        rendered = manifest.get("rendered_count", 0)
        print(f"--- Manifest: {manifest.get('batch_id', '?')} ---")
        print(f"  Target limit: {manifest.get('target_limit', '?')}")
        print(f"  Rendered count: {rendered}")
        print(f"  Skipped count: {manifest.get('skipped_count', 0)}")
        if rendered != RC_7500_EXACT:
            all_errors.append(f"rendered count {rendered} != required {RC_7500_EXACT}")
        if manifest.get("batch_id") not in ("rc_7500", "rc_batch_7500"):
            all_errors.append(f"unexpected batch_id {manifest.get('batch_id')!r}")
    print()

    disallowed = find_disallowed_html()
    print("--- site/ HTML scan (outside _sample) ---")
    if disallowed:
        for path in disallowed:
            all_errors.append(f"HTML outside quarantine: {path.relative_to(ROOT)}")
    else:
        print("  No HTML outside site/_sample/")
    print()

    sample_html = sorted(SAMPLE_DIR.glob("*.html")) if SAMPLE_DIR.is_dir() else []
    print(f"--- site/_sample/ RC HTML ({len(sample_html)} files) ---")
    if manifest and len(sample_html) != manifest.get("rendered_count", -1):
        all_errors.append(
            f"HTML file count {len(sample_html)} != manifest rendered_count "
            f"{manifest.get('rendered_count')}"
        )
    if len(sample_html) != RC_7500_EXACT:
        all_errors.append(f"HTML file count {len(sample_html)} != {RC_7500_EXACT}")

    checked = 0
    for path in sample_html:
        checked += 1
        if checked <= 3 or checked > len(sample_html) - 2:
            print(f"  Checked: {path.relative_to(ROOT)}")
        elif checked == 4:
            print(f"  ... ({len(sample_html) - 5} more files) ...")
        errs, _ = validate_rc_file(path, manifest_by_output.get(path.name))
        all_errors.extend(errs)
    print()

    if ROUTES_PATH.is_file():
        routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
        published = sum(1 for r in routes if r.get("status") == "published")
        indexable = sum(1 for r in routes if r.get("indexable") is True)
        in_sitemap = sum(1 for r in routes if r.get("in_sitemap") is True)
        in_nav = sum(1 for r in routes if r.get("in_navigation") is True)
        if published or indexable or in_sitemap or in_nav:
            all_errors.append("routes.json publication posture changed")
        print("--- Route registry posture ---")
        print(f"  Routes: {len(routes)} | Published: {published} | Indexable: {indexable}")
    print()

    if all_errors:
        print("--- Errors ---")
        for e in all_errors[:30]:
            print(f"  ERROR: {e}")
        if len(all_errors) > 30:
            print(f"  ... and {len(all_errors) - 30} more errors")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print(f"VALIDATION SUMMARY: PASS ({len(sample_html)} RC file(s))")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
