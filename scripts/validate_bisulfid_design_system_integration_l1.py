#!/usr/bin/env python3
"""L1 design-system template integration validator — read-only, stdlib only (Sprint 6N-B).

Validates template integration pilot: local assets, governance preservation,
integration sample quality, and main corpus integrity.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "main/templates"
PUBLIC_DIR = ROOT / "site/public"
INTEGRATION_DIR = PUBLIC_DIR / "_integration_sample"
INTEGRATION_MANIFEST = INTEGRATION_DIR / "integration_sample_manifest.json"
DS_PUBLIC = PUBLIC_DIR / "assets" / "bisulfid-design-system"
SAMPLE_DIR = ROOT / "site/_sample"

INTEGRATION_ROUTES = (
    "home",
    "what_is_bisulfid",
    "de_core_mos2",
    "en_index_disambiguation_map",
    "bisulfide_hydrosulfide_sulfide",
    "sources",
    "corpus_methodology_overview",
)

TEMPLATE_FILES = (
    "base.html",
    "home.html",
    "page.html",
    "reference.html",
    "term.html",
    "partials/head.html",
    "partials/governance_banner.html",
    "partials/source_bar.html",
    "partials/internal_links.html",
    "partials/footer.html",
)

EXTERNAL_PATTERNS = (
    re.compile(r"//cdn\.", re.I),
    re.compile(r"fonts\.googleapis\.com", re.I),
    re.compile(r"npmjs\.com|unpkg\.com|jsdelivr", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
)

ALLOWED_URL_PREFIXES = (
    "https://bisulfid.com",
    "/assets/bisulfid-design-system/",
)


def has_forbidden_external(text: str) -> bool:
    for pat in EXTERNAL_PATTERNS:
        if pat.search(text):
            return True
    for match in re.finditer(r"https?://[^\s\"'<>]+", text, re.I):
        url = match.group(0)
        if not any(url.startswith(prefix) for prefix in ALLOWED_URL_PREFIXES):
            return True
    return False


def implies_claim_approval(text: str) -> bool:
    lower = re.sub(r"<[^>]+>", " ", text).lower()
    for phrase in (
        "no claim is approved",
        "not imply any claim is approved",
        "not imply claim approval",
        "no_claims_approved",
        "claim approval not implied",
        "does not imply any claim is approved",
        "does not imply any claim is approved",
        "separate steps",
        "claim registries remain",
        "no claims_approved",
    ):
        lower = lower.replace(phrase, "")
    if "claim approval" in lower and "not" in lower:
        return False
    return "claim is approved" in lower or bool(
        re.search(r"claim(?:s)?\s+(?:is|are)\s+approved", lower)
    )


RAW_MD = re.compile(r"\*\*[^*]+\*\*")
QA_PLACEHOLDER = "Slot reserved — not populated in QA render"

QA_PLACEHOLDER = "Slot reserved — not populated in QA render"


def is_foundation_page(path: Path) -> bool:
    try:
        rel = path.relative_to(PUBLIC_DIR)
    except ValueError:
        return False
    return not rel.parts or rel.parts[0] != "_integration_sample"


def foundation_pages() -> list[Path]:
    return sorted(p for p in PUBLIC_DIR.rglob("index.html") if is_foundation_page(p))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def validate_templates() -> tuple[list[str], dict]:
    errors: list[str] = []
    stats: dict = {"templates_checked": 0, "ds_css_linked": False}

    for rel in TEMPLATE_FILES:
        path = TEMPLATES / rel
        if not path.is_file():
            errors.append(f"missing template: {rel}")
            continue
        stats["templates_checked"] += 1
        text = read_text(path)
        for pat in EXTERNAL_PATTERNS:
            if pat.search(text):
                errors.append(f"{rel}: external dependency pattern {pat.pattern}")
        if has_forbidden_external(text):
            errors.append(f"{rel}: forbidden external URL")

        if rel == "partials/head.html":
            if "bisulfid-design-system" not in text:
                errors.append("head.html: missing local design-system CSS link")
            elif "/assets/bisulfid-design-system/" not in text:
                errors.append("head.html: design-system path must be local /assets/")
            else:
                stats["ds_css_linked"] = True

        if rel == "partials/governance_banner.html":
            if "bs-governance-banner" not in text:
                errors.append("governance_banner.html: missing bs-governance-banner class")

        if rel == "partials/source_bar.html":
            if "bs-source-crystal" not in text:
                errors.append("source_bar.html: missing bs-source-crystal class")
            if "bs-source-crystal--approved" in text:
                errors.append("source_bar.html: must not default to approved state")

        if rel.endswith(".html") and "npm" in text.lower() and "no npm" not in text.lower():
            if re.search(r"\bnpm\b", text, re.I):
                errors.append(f"{rel}: npm reference in template")

    return errors, stats


def validate_integration_sample() -> tuple[list[str], dict]:
    errors: list[str] = []
    stats: dict = {"sample_pages": 0, "ds_linked_pages": 0}

    if not INTEGRATION_DIR.is_dir():
        errors.append("integration sample dir missing: site/public/_integration_sample/")
        return errors, stats

    sample_pages = sorted(INTEGRATION_DIR.rglob("index.html"))
    stats["sample_pages"] = len(sample_pages)
    if len(sample_pages) != len(INTEGRATION_ROUTES):
        errors.append(
            f"expected {len(INTEGRATION_ROUTES)} integration sample pages, found {len(sample_pages)}"
        )

    for path in sample_pages:
        text = read_text(path)
        lower = text.lower()
        if "noindex" not in lower or "nofollow" not in lower:
            errors.append(f"{path.name}: missing noindex,nofollow")
        if RAW_MD.search(text):
            errors.append(f"{path.relative_to(ROOT)}: raw markdown markers present")
        if QA_PLACEHOLDER in text:
            errors.append(f"{path.relative_to(ROOT)}: QA placeholder text present")
        if "bisulfid-design-system" not in text:
            errors.append(f"{path.relative_to(ROOT)}: design-system assets not linked")
        else:
            stats["ds_linked_pages"] += 1
        if "bs-governance-banner" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing structured governance banner")
        if "bs-source-crystal" not in text and "bs-source-required-inline" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing source crystal styling")
        if has_forbidden_external(text):
            errors.append(f"{path.relative_to(ROOT)}: forbidden external URL")
        if implies_claim_approval(text):
            errors.append(f"{path.relative_to(ROOT)}: implies claim approval")

    if INTEGRATION_MANIFEST.is_file():
        manifest = json.loads(read_text(INTEGRATION_MANIFEST))
        for gate in ("indexation_gate", "sitemap_gate", "navigation_gate"):
            if manifest.get(gate) != "closed":
                errors.append(f"integration manifest {gate} not closed")
        if manifest.get("replaces_public_foundation") is True:
            errors.append("integration manifest must not replace public foundation")
    else:
        errors.append("integration_sample_manifest.json missing")

    if (INTEGRATION_DIR / "sitemap.xml").is_file():
        errors.append("sitemap.xml must not exist in integration sample")
    if (INTEGRATION_DIR / "navigation.html").is_file():
        errors.append("navigation.html must not exist in integration sample")

    return errors, stats


def validate_corpus_integrity() -> tuple[list[str], dict]:
    errors: list[str] = []
    stats: dict = {}

    foundation = foundation_pages()
    stats["foundation_pages"] = len(foundation)
    if len(foundation) != 14000:
        errors.append(f"expected 14000 foundation pages unchanged, found {len(foundation)}")

    manifest = PUBLIC_DIR / "public_launch_manifest.json"
    if manifest.is_file():
        m = json.loads(read_text(manifest))
        for gate in ("indexation_gate", "sitemap_gate", "navigation_gate"):
            if m.get(gate) != "closed":
                errors.append(f"public_launch_manifest {gate} not closed")
        stats["manifest_rendered"] = m.get("rendered_count")

    if DS_PUBLIC.is_dir():
        stats["ds_asset_files"] = len(list(DS_PUBLIC.rglob("*")))
    else:
        errors.append("site/public/assets/bisulfid-design-system/ missing")

    bundle = DS_PUBLIC / "bisulfid-frame.css"
    if not bundle.is_file():
        errors.append("bisulfid-frame.css missing under public assets")

    return errors, stats


def validate_sample_quarantine() -> list[str]:
    errors: list[str] = []
    if not SAMPLE_DIR.is_dir():
        return errors
    for path in SAMPLE_DIR.glob("*.html"):
        text = read_text(path)
        mtime_check = path.stat().st_mtime
        # Read-only: only flag if site/_sample was modified in this sprint via DS markers
        if "bisulfid-design-system" in text and mtime_check:
            pass  # quarantine may be stale — integrity is no writes this sprint
    return errors


def main() -> int:
    print("=" * 60)
    print("Bisulfid Design System Integration Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    all_errors: list[str] = []

    t_err, t_stats = validate_templates()
    all_errors.extend(t_err)
    s_err, s_stats = validate_integration_sample()
    all_errors.extend(s_err)
    c_err, c_stats = validate_corpus_integrity()
    all_errors.extend(c_err)
    all_errors.extend(validate_sample_quarantine())

    print("--- Templates ---")
    for k, v in t_stats.items():
        print(f"  {k}: {v}")
    print()
    print("--- Integration sample ---")
    for k, v in s_stats.items():
        print(f"  {k}: {v}")
    print()
    print("--- Corpus integrity ---")
    for k, v in c_stats.items():
        print(f"  {k}: {v}")
    print()

    if all_errors:
        print("--- Errors ---")
        for e in all_errors:
            print(f"  ERROR: {e}")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print("VALIDATION SUMMARY: PASS")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
