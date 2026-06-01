#!/usr/bin/env python3
"""L1 14,000-page public launch foundation validator — read-only, stdlib only (Sprint 6M-G).

Validates controlled public launch foundation HTML under site/public/ only.
Does not modify files.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
PUBLIC_DIR = SITE_DIR / "public"
MANIFEST_PATH = PUBLIC_DIR / "public_launch_manifest.json"
ROUTES_PATH = ROOT / "main/data/routes.json"

PUBLIC_LAUNCH_EXACT = 14000
INTEGRATION_SAMPLE_DIR = PUBLIC_DIR / "_integration_sample"
VISUAL_PROOF_SAMPLE_DIR = PUBLIC_DIR / "_visual_proof_sample"


def is_foundation_public_page(path: Path) -> bool:
    try:
        rel = path.relative_to(PUBLIC_DIR)
    except ValueError:
        return False
    if not rel.parts:
        return True
    return rel.parts[0] not in ("_integration_sample", "_visual_proof_sample")


def foundation_public_html_files() -> list[Path]:
    if not PUBLIC_DIR.is_dir():
        return []
    return sorted(p for p in PUBLIC_DIR.rglob("index.html") if is_foundation_public_page(p))

REQUIRED_MARKERS = (
    "noindex",
    "nofollow",
    "public launch foundation",
    "14,000",
    "public_visible_foundation",
    "planned",
    "closed",
    "no_claims_approved",
    "source approval not implied",
    "claim approval not implied",
)

FORBIDDEN = (
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"(?<!not )(?<!non-)(ready for (public )?launch|go live now)", re.I),
    re.compile(r"<script\s+src=", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
    re.compile(r"sitemap\.xml", re.I),
)

FORBIDDEN_CONTENT = (
    re.compile(r"\bCAGR\b", re.I),
    re.compile(r"\bacquisition\b", re.I),
    re.compile(r"\bprocurement\b", re.I),
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
        if not rel.parts:
            disallowed.append(path)
            continue
        if rel.parts[0] not in ("_sample", "public"):
            disallowed.append(path)
    return disallowed


def validate_public_file(path: Path, manifest_page: dict | None) -> tuple[list[str], list[str]]:
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

    for pattern in FORBIDDEN_CONTENT:
        if pattern.search(strip_html_tags(text)):
            warnings.append(f"{path.name}: flagged content pattern {pattern.pattern}")

    if implies_claim_approval(text):
        errors.append(f"{path.name}: implies claim approval")
    if implies_source_approval(text):
        errors.append(f"{path.name}: implies source approval")

    if "production_can_safely_proceed: yes" in lower.replace(" ", ""):
        errors.append(f"{path.name}: claims production_can_safely_proceed yes")

    if manifest_page and manifest_page.get("source_required_visible") == "yes":
        if "[source required]" not in lower and "source-required-marker" not in lower:
            errors.append(f"{path.name}: source-required page missing [SOURCE REQUIRED] visibility")

    if 'data-qa-artifact="true"' in lower:
        errors.append(f"{path.name}: marked as QA artifact in public foundation")

    return errors, warnings


def main() -> int:
    print("=" * 60)
    print("Bisulfid 14,000-Page Public Launch Foundation Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Public dir: {PUBLIC_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []
    all_warnings: list[str] = []

    routes_data = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))
    routes = routes_data.get("routes", [])
    route_count = len(routes)
    backed = sum(
        1 for r in routes
        if (ROOT / r.get("content_file", "")).is_file()
    )

    disallowed = find_disallowed_html()
    if disallowed:
        all_errors.append(
            f"HTML outside site/public/ or site/_sample/: {len(disallowed)} file(s)"
        )

    if not MANIFEST_PATH.is_file():
        all_errors.append("public_launch_manifest.json missing under site/public/")
        manifest = None
    else:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    public_files = foundation_public_html_files()
    output_paths = [str(p.relative_to(ROOT)).replace("\\", "/") for p in public_files]

    if len(output_paths) != len(set(output_paths)):
        all_errors.append("duplicate public output paths")

    if len(public_files) != PUBLIC_LAUNCH_EXACT:
        all_errors.append(
            f"expected {PUBLIC_LAUNCH_EXACT} public pages, found {len(public_files)}"
        )

    manifest_by_output: dict[str, dict] = {}
    if manifest:
        for page in manifest.get("pages", []):
            manifest_by_output[page.get("output_path", "")] = page
        if manifest.get("indexation_gate") != "closed":
            all_errors.append("manifest indexation_gate not closed")
        if manifest.get("sitemap_gate") != "closed":
            all_errors.append("manifest sitemap_gate not closed")
        if manifest.get("navigation_gate") != "closed":
            all_errors.append("manifest navigation_gate not closed")

    for artifact in ("sitemap.xml", "navigation.html"):
        if (PUBLIC_DIR / artifact).is_file():
            all_errors.append(f"uncontrolled {artifact} under site/public/")

    language_split: Counter[str] = Counter()
    family_split: Counter[str] = Counter()
    source_required_count = 0

    sample_size = min(200, len(public_files))
    for i, path in enumerate(public_files):
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        mp = manifest_by_output.get(rel)
        if mp:
            language_split[mp.get("language", "unknown")] += 1
            family_split[mp.get("page_type", "unknown")] += 1
            if mp.get("source_required_visible") == "yes":
                source_required_count += 1
        if i < sample_size:
            errs, warns = validate_public_file(path, mp)
            all_errors.extend(errs)
            all_warnings.extend(warns)

    print(f"Routes: {route_count}")
    print(f"Draft-backed: {backed}")
    print(f"Missing drafts: {route_count - backed}")
    print(f"Public output pages: {len(public_files)}")
    print(f"Manifest pages: {len(manifest.get('pages', [])) if manifest else 0}")
    print(f"Skipped (manifest): {manifest.get('skipped_count', '?') if manifest else '?'}")
    print(f"Disallowed HTML paths: {len(disallowed)}")
    print(f"Sample deep-checked: {sample_size}")
    if language_split:
        print(f"Language split (manifest): {dict(language_split)}")
    if family_split:
        print(f"Family split (manifest): {dict(family_split)}")
    print()

    if all_warnings:
        print("--- Warnings ---")
        for w in all_warnings[:10]:
            print(f"  WARN: {w}")
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
