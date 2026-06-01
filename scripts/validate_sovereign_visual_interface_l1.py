#!/usr/bin/env python3
"""L1 sovereign visual interface validator — read-only, stdlib only (Sprint 6N-D).

Validates 6N-D visual reconstruction: material palette, control-room hero,
spatial depth, governance chips, source crystal, missing-E motif.
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
SAMPLE_DIR = ROOT / "site/_sample"
MANIFEST_PATH = PUBLIC_DIR / "public_launch_manifest.json"
HOME_PATH = PUBLIC_DIR / "index.html"
PROOF_MANIFEST_PATH = PUBLIC_DIR / "_visual_proof_sample" / "visual_proof_manifest.json"
PROOF_HOME_PATH = PUBLIC_DIR / "_visual_proof_sample" / "index.html"
DS_ASSETS = PUBLIC_DIR / "assets/bisulfid-design-system"

FOUNDATION_EXACT = 14000
RAW_MD = re.compile(r"\*\*[^*]+\*\*")
QA_PLACEHOLDER = "Slot reserved — not populated in QA render"

EXTERNAL_PATTERNS = (
    re.compile(r"//cdn\.", re.I),
    re.compile(r"fonts\.googleapis\.com", re.I),
    re.compile(r"npmjs\.com|unpkg\.com|jsdelivr", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
)

# Template/UI boolean leakage — not governance prose inside content body
GOVERNANCE_UI_FALSE = re.compile(
    r"(?:<li>\s*Indexable:\s*<strong>false</strong>|"
    r"Indexation:\s*false\s*·|"
    r"Sitemap:\s*false\s*·|"
    r"Navigation:\s*false\s*·|"
    r"(?<![\w:/-])>\s*false\s*<(?!/meta))",
    re.I,
)
GOVERNANCE_UI_TRUE = re.compile(
    r"(?<![\w:/-])>\s*true\s*<(?!/meta)|"
    r"(?<![\w-])\strue\s*(?:</p>|</li>|</span>)",
    re.I,
)


def is_foundation_page(path: Path) -> bool:
    try:
        rel = path.relative_to(PUBLIC_DIR)
    except ValueError:
        return False
    return not rel.parts or rel.parts[0] not in ("_integration_sample", "_visual_proof_sample")


def foundation_pages() -> list[Path]:
    return sorted(p for p in PUBLIC_DIR.rglob("index.html") if is_foundation_page(p))


def strip_meta_and_comments(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<meta[^>]+>", " ", text, flags=re.I)
    text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r'\s[\w:-]+="[^"]*"', " ", text)
    text = re.sub(r"\s[\w:-]+='[^']*'", " ", text)
    return text


def implies_claim_approval(text: str) -> bool:
    lower = re.sub(r"<[^>]+>", " ", text).lower()
    for phrase in (
        "no claim is approved",
        "not imply any claim is approved",
        "not imply claim approval",
        "no_claims_approved",
        "claim approval not implied",
        "no claims_approved",
        "none approved",
    ):
        lower = lower.replace(phrase, "")
    return "claim is approved" in lower or "claims approved" in lower


def implies_source_approval(text: str) -> bool:
    lower = text.lower()
    if "source approval not implied" in lower or "no source approval" in lower:
        return False
    if "sources and claims remain unapproved" in lower:
        return False
    return bool(re.search(r"source(?:s)?\s+(?:is|are)\s+approved", lower))


def validate_homepage_at(path: Path, label: str = "homepage") -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        errors.append(f"{label} missing: {path.relative_to(ROOT)}")
        return errors, warnings

    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    if "bs-control-room-hero" not in text:
        errors.append(f"{label} missing bs-control-room-hero")
    if "chemical-space.svg" not in text:
        errors.append(f"{label} missing chemical-space visual")
    if "missing-e-boundary.svg" not in text:
        errors.append(f"{label} missing missing-E boundary visual")
    if "bs-gov-chip" not in text:
        errors.append(f"{label} missing governance chips")
    if "bs-relation-lattice" not in text:
        errors.append(f"{label} missing relation lattice")
    if "bs-term-node" not in text:
        errors.append(f"{label} missing term nodes")
    if "bisulfid-design-system" not in text:
        errors.append(f"{label} missing design-system links")

    visible = strip_meta_and_comments(text)
    if GOVERNANCE_UI_TRUE.search(visible):
        errors.append(f"{label} raw true leakage in governance UI")
    if GOVERNANCE_UI_FALSE.search(visible):
        errors.append(f"{label} raw false leakage in governance UI")

    if "noindex" not in lower or "nofollow" not in lower:
        errors.append(f"{label} missing noindex,nofollow")
    if "[source required]" not in lower:
        errors.append(f"{label} missing [SOURCE REQUIRED]")

    for pattern in EXTERNAL_PATTERNS:
        if pattern.search(text):
            errors.append(f"{label} external dependency: {pattern.pattern}")

    return errors, warnings


def validate_homepage() -> tuple[list[str], list[str]]:
    return validate_homepage_at(HOME_PATH, "foundation homepage")


def validate_page(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    if "bisulfid-design-system" not in text:
        errors.append(f"{path.name}: missing design-system links")
    if "bs-control-room" not in text:
        errors.append(f"{path.name}: missing bs-control-room")
    if "bs-gov-chip" not in text and "bs-governance-banner" not in text:
        errors.append(f"{path.name}: missing governance UI")
    if RAW_MD.search(text):
        errors.append(f"{path.name}: raw markdown markers")
    if QA_PLACEHOLDER in text:
        errors.append(f"{path.name}: QA placeholder text")
    if "noindex" not in lower or "nofollow" not in lower:
        errors.append(f"{path.name}: missing noindex,nofollow")
    if implies_claim_approval(text):
        errors.append(f"{path.name}: implies claim approval")
    if implies_source_approval(text):
        errors.append(f"{path.name}: implies source approval")

    visible = strip_meta_and_comments(text)
    if GOVERNANCE_UI_TRUE.search(visible):
        errors.append(f"{path.name}: visible raw 'true' leakage in governance UI")
    if GOVERNANCE_UI_FALSE.search(visible):
        errors.append(f"{path.name}: visible raw 'false' leakage in governance UI")

    for pattern in EXTERNAL_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path.name}: external dependency")

    return errors


def validate_manifest(*, full_refresh_applied: bool) -> list[str]:
    errors: list[str] = []
    if not MANIFEST_PATH.is_file():
        errors.append("public_launch_manifest.json missing")
        return errors
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("rendered_count") != FOUNDATION_EXACT:
        errors.append("manifest rendered_count != 14000")
    if full_refresh_applied:
        if manifest.get("visual_reconstruction") is not True:
            errors.append("manifest visual_reconstruction not true")
        if manifest.get("visual_reconstruction_sprint") != "6N-D":
            errors.append("manifest visual_reconstruction_sprint != 6N-D")
    for gate in ("indexation_gate", "sitemap_gate", "navigation_gate"):
        if manifest.get(gate) != "closed":
            errors.append(f"manifest {gate} not closed")
    return errors


def full_visual_refresh_applied() -> bool:
    if not MANIFEST_PATH.is_file():
        return False
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return manifest.get("visual_reconstruction") is True


def main() -> int:
    print("=" * 60)
    print("Bisulfid Sovereign Visual Interface Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Public dir: {PUBLIC_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []
    all_warnings: list[str] = []

    pages = foundation_pages()
    print(f"Foundation pages: {len(pages)}")
    if len(pages) != FOUNDATION_EXACT:
        all_errors.append(f"expected {FOUNDATION_EXACT} foundation pages, found {len(pages)}")

    if not (DS_ASSETS / "bisulfid-frame.css").is_file():
        all_errors.append("bisulfid-frame.css missing in public assets")
    else:
        css = (DS_ASSETS / "bisulfid-frame.css").read_text(encoding="utf-8")
        if "bs-control-room-hero" not in css:
            all_errors.append("bisulfid-frame.css missing control-room hero styles")
        colors = DS_ASSETS / "tokens/colors.css"
        if colors.is_file():
            ct = colors.read_text(encoding="utf-8")
            for token in ("--bs-carbon-950", "--bs-sulfur-500", "--bs-molybdenum-500"):
                if token not in ct:
                    all_errors.append(f"colors.css missing {token}")

    full_refresh = full_visual_refresh_applied()
    print(f"Full 6N-D refresh applied: {full_refresh}")

    all_errors.extend(validate_manifest(full_refresh_applied=full_refresh))
    if full_refresh:
        home_errors, home_warnings = validate_homepage()
    else:
        home_errors, home_warnings = validate_homepage_at(
            PROOF_HOME_PATH, "visual proof homepage"
        )
        if not PROOF_MANIFEST_PATH.is_file():
            all_errors.append("visual proof manifest missing — run --render-visual-proof-sample")
    all_errors.extend(home_errors)
    all_warnings.extend(home_warnings)

    for artifact in ("sitemap.xml", "navigation.html", "robots.txt"):
        if (PUBLIC_DIR / artifact).is_file():
            all_errors.append(f"forbidden artifact: {artifact}")

    sample_count = len(list(SAMPLE_DIR.rglob("*.html"))) if SAMPLE_DIR.is_dir() else 0
    print(f"Quarantine sample pages (unchanged check deferred to git): {sample_count}")

    if full_refresh:
        sample_checked = min(100, len(pages))
        for path in pages[:sample_checked]:
            all_errors.extend(validate_page(path))
        print(f"Foundation pages sampled: {sample_checked}")
    else:
        print("Foundation page visual sampling deferred until full 14,000 refresh")

    if all_warnings:
        print()
        print("--- Warnings ---")
        for w in all_warnings[:10]:
            print(f"  WARN: {w}")

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
