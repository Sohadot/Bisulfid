#!/usr/bin/env python3
"""L1 visual proof sample validator — read-only, stdlib only (Sprint 6N-D).

Validates the 7-route visual proof render before full 14,000-page refresh.
Does not modify files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF_DIR = ROOT / "site/public/_visual_proof_sample"
MANIFEST_PATH = PROOF_DIR / "visual_proof_manifest.json"
HOME_PATH = PROOF_DIR / "index.html"
DS_ASSETS = ROOT / "site/public/assets/bisulfid-design-system"

PROOF_ROUTE_COUNT = 7
PROOF_ROUTES = (
    "home",
    "what_is_bisulfid",
    "de_core_mos2",
    "en_index_disambiguation_map",
    "bisulfide_hydrosulfide_sulfide",
    "sources",
    "corpus_methodology_overview",
)

EXTERNAL_PATTERNS = (
    re.compile(r"//cdn\.", re.I),
    re.compile(r"fonts\.googleapis\.com", re.I),
    re.compile(r"npmjs\.com|unpkg\.com|jsdelivr", re.I),
)

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


def strip_html(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<meta[^>]+>", " ", text, flags=re.I)
    text = re.sub(r'\s[\w:-]+="[^"]*"', " ", text)
    return text


def validate_manifest() -> list[str]:
    errors: list[str] = []
    if not MANIFEST_PATH.is_file():
        errors.append("visual_proof_manifest.json missing")
        return errors
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if data.get("route_count") != PROOF_ROUTE_COUNT:
        errors.append(f"manifest route_count != {PROOF_ROUTE_COUNT}")
    if data.get("visual_review_status") not in ("pending_review", "approved"):
        errors.append("manifest visual_review_status invalid")
    if data.get("visual_palette") != "carbon-sulfur-molybdenum":
        errors.append("manifest visual_palette not carbon-sulfur-molybdenum")
    if data.get("full_refresh_allowed") is True and data.get("visual_review_status") != "approved":
        errors.append("full_refresh_allowed true without approved review")
    return errors


def validate_home() -> list[str]:
    errors: list[str] = []
    if not HOME_PATH.is_file():
        errors.append("visual proof homepage missing")
        return errors
    text = HOME_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    checks = (
        ("bs-control-room-hero", "control-room hero"),
        ("chemical-space.svg", "chemical-space layer"),
        ("missing-e-boundary.svg", "missing-E motif"),
        ("bs-gov-chip", "governance chips"),
        ("bs-relation-lattice", "relation lattice"),
        ("bs-term-node", "term nodes"),
        ("bisulfid-design-system", "design-system CSS"),
        ("bs-source-crystal", "source crystal"),
        ("source-crystal.svg", "source crystal asset"),
        ("bs-missing-e-boundary-system", "missing-E boundary system"),
        ("bs-missing-e-boundary-system__name", "canonical BISULFID name"),
    )
    for marker, label in checks:
        if marker not in text:
            errors.append(f"homepage missing {label}")
    csp_match = re.search(
        r'Content-Security-Policy"\s+content="([^"]+)"',
        text,
        re.I,
    )
    if not csp_match:
        errors.append("homepage missing CSP meta")
    else:
        csp = csp_match.group(1).lower()
        for required in (
            "default-src 'none'",
            "style-src 'self'",
            "img-src 'self' data:",
            "script-src 'none'",
        ):
            if required not in csp:
                errors.append(f"homepage CSP missing {required}")
        if "unsafe-inline" in csp or "unsafe-eval" in csp:
            errors.append("homepage CSP allows unsafe directives")
    if "noindex" not in lower or "nofollow" not in lower:
        errors.append("homepage missing noindex,nofollow")
    if "[source required]" not in lower:
        errors.append("homepage missing [SOURCE REQUIRED]")
    visible = strip_html(text)
    if GOVERNANCE_UI_TRUE.search(visible):
        errors.append("homepage raw true leakage in governance UI")
    if GOVERNANCE_UI_FALSE.search(visible):
        errors.append("homepage raw false leakage in governance UI")
    for pattern in EXTERNAL_PATTERNS:
        if pattern.search(text):
            errors.append(f"homepage external dependency: {pattern.pattern}")

    if re.search(r">Bisulfi<", text, re.I):
        errors.append("homepage wrong missing-E split (isolated Bisulfi fragment)")
    if "bisulfi-de" in lower.replace(" ", ""):
        errors.append("homepage wrong BISULFI-DE split motif")
    if "BISULFID" not in text:
        errors.append("homepage missing canonical BISULFID identity")

    svg_path = DS_ASSETS / "assets/missing-e-boundary.svg"
    if svg_path.is_file():
        svg_text = svg_path.read_text(encoding="utf-8")
        if "BISULFID" not in svg_text:
            errors.append("missing-e-boundary.svg missing BISULFID")
        if re.search(r">Bisulfi<", svg_text, re.I):
            errors.append("missing-e-boundary.svg uses wrong Bisulfi split")
        if re.search(r">de<", svg_text, re.I) and "BISULFIDE" not in svg_text:
            errors.append("missing-e-boundary.svg implies wrong de split")

    return errors


def main() -> int:
    print("=" * 60)
    print("Bisulfid Visual Proof Sample Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Proof dir: {PROOF_DIR}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    errors: list[str] = []
    if not PROOF_DIR.is_dir():
        errors.append("_visual_proof_sample/ missing — run --render-visual-proof-sample")
    else:
        pages = sorted(PROOF_DIR.rglob("index.html"))
        print(f"Proof pages: {len(pages)}")
        errors.extend(validate_manifest())
        errors.extend(validate_home())
        if len(pages) != PROOF_ROUTE_COUNT:
            errors.append(f"expected {PROOF_ROUTE_COUNT} proof pages, found {len(pages)}")

    if not (DS_ASSETS / "bisulfid-frame.css").is_file():
        errors.append("design-system assets missing under site/public/assets/")

    status = None
    if MANIFEST_PATH.is_file():
        status = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")).get("visual_review_status")
    print(f"Visual review status: {status or 'missing'}")

    print()
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        print()
        print("VALIDATION SUMMARY: FAIL")
        print("=" * 60)
        return 1

    print("VALIDATION SUMMARY: PASS")
    if status == "pending_review":
        print("NOTE: Visual proof structurally valid — human eye review still required.")
        print("      Set visual_review_status to 'approved' before full 14,000 refresh.")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
