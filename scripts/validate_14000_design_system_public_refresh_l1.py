#!/usr/bin/env python3
"""L1 14,000-page design-system public refresh validator — read-only, stdlib only (Sprint 6N-C).

Validates full public foundation refresh with integrated Bisulfid design system.
Does not modify files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "site/public"
MANIFEST_PATH = PUBLIC_DIR / "public_launch_manifest.json"
DS_ASSETS = PUBLIC_DIR / "assets/bisulfid-design-system"
SAMPLE_DIR = ROOT / "site/_sample"

FOUNDATION_EXACT = 14000
RAW_MD = re.compile(r"\*\*[^*]+\*\*")
QA_PLACEHOLDER = "Slot reserved — not populated in QA render"

EXTERNAL_PATTERNS = (
    re.compile(r"//cdn\.", re.I),
    re.compile(r"fonts\.googleapis\.com", re.I),
    re.compile(r"npmjs\.com|unpkg\.com|jsdelivr", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
)

FORBIDDEN_CONTENT = (
    re.compile(r"\bCAGR\b", re.I),
    re.compile(r"\bacquisition\b", re.I),
    re.compile(r"\bprocurement\b", re.I),
)


def is_foundation_page(path: Path) -> bool:
    try:
        rel = path.relative_to(PUBLIC_DIR)
    except ValueError:
        return False
    return not rel.parts or rel.parts[0] not in ("_integration_sample", "_visual_proof_sample")


def foundation_pages() -> list[Path]:
    return sorted(p for p in PUBLIC_DIR.rglob("index.html") if is_foundation_page(p))


def strip_html_tags(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))


def implies_claim_approval(text: str) -> bool:
    lower = strip_html_tags(text).lower()
    for phrase in (
        "no claim is approved",
        "not imply any claim is approved",
        "not imply claim approval",
        "no_claims_approved",
        "claim approval not implied",
        "no claims_approved",
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


def validate_manifest() -> tuple[list[str], dict]:
    errors: list[str] = []
    stats: dict = {}
    if not MANIFEST_PATH.is_file():
        errors.append("public_launch_manifest.json missing")
        return errors, stats
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    stats["manifest_rendered"] = manifest.get("rendered_count")
    stats["design_system_refresh"] = manifest.get("design_system_refresh")
    if manifest.get("rendered_count") != FOUNDATION_EXACT:
        errors.append(f"manifest rendered_count != {FOUNDATION_EXACT}")
    if manifest.get("design_system_refresh") is not True:
        errors.append("manifest design_system_refresh not true")
    if manifest.get("sprint") not in ("6N-C", "6N-D"):
        errors.append(f"manifest sprint expected 6N-C or 6N-D, got {manifest.get('sprint')!r}")
    if manifest.get("sprint") == "6N-D" and manifest.get("visual_reconstruction") is not True:
        errors.append("manifest visual_reconstruction required for sprint 6N-D")
    for gate in ("indexation_gate", "sitemap_gate", "navigation_gate"):
        if manifest.get(gate) != "closed":
            errors.append(f"manifest {gate} not closed")
    return errors, stats


def validate_page(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    if "noindex" not in lower or "nofollow" not in lower:
        errors.append(f"{path.name}: missing noindex,nofollow")
    if "bisulfid-design-system" not in text:
        errors.append(f"{path.name}: missing design-system links")
    if "bs-control-room" not in text:
        errors.append(f"{path.name}: missing bs-control-room")
    if "bs-governance-banner" not in text:
        errors.append(f"{path.name}: missing bs-governance-banner")
    if RAW_MD.search(text):
        errors.append(f"{path.name}: raw markdown markers")
    if QA_PLACEHOLDER in text:
        errors.append(f"{path.name}: QA placeholder text")
    if implies_claim_approval(text):
        errors.append(f"{path.name}: implies claim approval")
    if implies_source_approval(text):
        errors.append(f"{path.name}: implies source approval")
    for pat in EXTERNAL_PATTERNS:
        if pat.search(text):
            errors.append(f"{path.name}: external pattern {pat.pattern}")
    for pat in FORBIDDEN_CONTENT:
        if pat.search(strip_html_tags(text)):
            warnings.append(f"{path.name}: flagged content pattern {pat.pattern}")

    return errors, warnings


def main() -> int:
    print("=" * 60)
    print("Bisulfid 14,000 Design-System Public Refresh Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Public dir: {PUBLIC_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []
    all_warnings: list[str] = []
    stats: dict = {}

    pages = foundation_pages()
    stats["foundation_pages"] = len(pages)
    if len(pages) != FOUNDATION_EXACT:
        all_errors.append(f"expected {FOUNDATION_EXACT} foundation pages, found {len(pages)}")

    if not DS_ASSETS.is_dir():
        all_errors.append("site/public/assets/bisulfid-design-system/ missing")
    else:
        stats["ds_asset_files"] = len(list(DS_ASSETS.rglob("*")))
        if not (DS_ASSETS / "bisulfid-frame.css").is_file():
            all_errors.append("bisulfid-frame.css missing")

    m_err, m_stats = validate_manifest()
    all_errors.extend(m_err)
    stats.update(m_stats)

    for artifact in ("sitemap.xml", "navigation.html", "robots.txt"):
        if (PUBLIC_DIR / artifact).is_file():
            all_errors.append(f"forbidden artifact: site/public/{artifact}")

    sample_size = min(100, len(pages))
    md_count = 0
    slot_count = 0
    ds_count = 0
    for path in pages:
        text = path.read_text(encoding="utf-8")
        if RAW_MD.search(text):
            md_count += 1
        if QA_PLACEHOLDER in text:
            slot_count += 1
        if "bisulfid-design-system" in text:
            ds_count += 1

    stats["raw_markdown_files"] = md_count
    stats["qa_placeholder_files"] = slot_count
    stats["design_system_linked_files"] = ds_count

    for path in pages[:sample_size]:
        p_err, p_warn = validate_page(path)
        all_errors.extend(p_err)
        all_warnings.extend(p_warn)

    print(f"Foundation pages: {stats.get('foundation_pages', '?')}")
    print(f"Design-system linked: {ds_count}/{len(pages) if pages else 0}")
    print(f"Raw markdown files: {md_count}")
    print(f"QA placeholder files: {slot_count}")
    print(f"Sample validated: {sample_size}")
    if all_warnings:
        print(f"Content pattern warnings: {len(all_warnings)}")
    print()

    if all_errors:
        print("--- Errors ---")
        for e in all_errors[:40]:
            print(f"  ERROR: {e}")
        if len(all_errors) > 40:
            print(f"  ... and {len(all_errors) - 40} more")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print("VALIDATION SUMMARY: PASS")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
