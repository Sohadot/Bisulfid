#!/usr/bin/env python3
"""L1 template layer validator — read-only, stdlib only (Sprint 6M-B).

Validates sovereign publication frame templates for the 14,000-page launch corpus
pipeline. Does not modify files or render public output.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "main/templates"

FRAME_TEMPLATES = (
    "base.html",
    "home.html",
    "page.html",
    "reference.html",
    "term.html",
)

REQUIRED_PARTIALS = (
    "partials/head.html",
    "partials/governance_banner.html",
    "partials/breadcrumbs.html",
    "partials/nav.html",
    "partials/footer.html",
    "partials/source_bar.html",
    "partials/internal_links.html",
    "partials/hreflang.html",
    "partials/safety_notice.html",
)

BASE_REQUIRED = (
    "{{head}}",
    "{{nav}}",
    "{{footer}}",
    "{{content}}",
    "{{governance_banner}}",
    "{{breadcrumbs}}",
    "{{language}}",
    "{{text_direction}}",
    "{{route_id}}",
    "{{route_status}}",
    "{{publication_posture}}",
)

HEAD_REQUIRED = (
    "{{page_title}}",
    "{{meta_description}}",
    "{{robots_directive}}",
    "{{canonical_url}}",
    "{{canonical_mode}}",
    "{{source_required_flag}}",
    "{{claim_approval_state}}",
    "noindex, nofollow",
)

GOVERNANCE_REQUIRED = (
    "14,000",
    "{{route_status}}",
    "{{publication_posture}}",
    "{{robots_directive}}",
    "Not a launch",
)

FOOTER_REQUIRED = (
    "14,000",
    "{{claim_approval_state}}",
    "{{publication_posture}}",
)

FORBIDDEN_PATTERNS = (
    re.compile(r"(?<!not )(?<!non-)(ready for (public )?launch|go live now|publish now)", re.I),
    re.compile(r"index,\s*follow", re.I),
    re.compile(r"claim is approved", re.I),
    re.compile(r"source-locking is complete", re.I),
    re.compile(r"500-page launch target", re.I),
    re.compile(r"pilot site|small website|blog launch", re.I),
)

MULTILINGUAL_MARKERS = (
    "{{language}}",
    "{{text_direction}}",
)


def read_template(rel: str) -> str:
    path = TEMPLATES / rel
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def check_markers(text: str, markers: tuple[str, ...]) -> list[str]:
    return [m for m in markers if m not in text]


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {
        "frame_templates_checked": 0,
        "partials_checked": 0,
        "fourteen_thousand_frame": True,
    }

    for rel in FRAME_TEMPLATES:
        path = TEMPLATES / rel
        if not path.is_file():
            errors.append(f"missing frame template: {rel}")
            continue
        stats["frame_templates_checked"] += 1
        text = path.read_text(encoding="utf-8")
        if "14,000" not in text and rel != "base.html":
            warnings.append(f"{rel}: may not reference 14,000-page frame context")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel}: forbidden pattern {pattern.pattern}")

    for rel in REQUIRED_PARTIALS:
        path = TEMPLATES / rel
        if not path.is_file():
            errors.append(f"missing partial: {rel}")
            continue
        stats["partials_checked"] += 1
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel}: forbidden pattern {pattern.pattern}")

    base = read_template("base.html")
    if base:
        missing = check_markers(base, BASE_REQUIRED)
        if missing:
            errors.append(f"base.html missing slots: {', '.join(missing)}")
        for m in MULTILINGUAL_MARKERS:
            if m not in base:
                errors.append(f"base.html missing multilingual marker {m}")

    head = read_template("partials/head.html")
    if head:
        missing = check_markers(head, HEAD_REQUIRED)
        if missing:
            errors.append(f"partials/head.html missing: {', '.join(missing)}")

    gov = read_template("partials/governance_banner.html")
    if gov:
        missing = check_markers(gov, GOVERNANCE_REQUIRED)
        if missing:
            errors.append(f"partials/governance_banner.html missing: {', '.join(missing)}")

    footer = read_template("partials/footer.html")
    if footer:
        missing = check_markers(footer, FOOTER_REQUIRED)
        if missing:
            errors.append(f"partials/footer.html missing: {', '.join(missing)}")

    for rel in ("page.html", "reference.html", "term.html"):
        text = read_template(rel)
        if not text:
            continue
        for slot in ("{{source_bar}}", "{{internal_links}}"):
            if slot not in text:
                errors.append(f"{rel} missing slot {slot}")
        if "{{page_h1}}" not in text:
            errors.append(f"{rel} missing {{page_h1}}")

    home = read_template("home.html")
    if home and "{{internal_links}}" not in home:
        errors.append("home.html missing {{internal_links}}")

    # Legacy registry templates remain skeleton — informational only
    legacy = ("reference_page.html", "term_page.html", "glossary.html")
    for rel in legacy:
        if (TEMPLATES / rel).is_file():
            text = read_template(rel)
            if "SKELETON TEMPLATE" in text:
                warnings.append(
                    f"{rel}: legacy skeleton remains; migrate to publication frame in future sprint"
                )

    return errors, warnings, stats


def main() -> int:
    print("=" * 60)
    print("Bisulfid Template Layer Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only")
    print("Frame target: 14,000-page governed launch corpus")
    print("=" * 60)
    print()

    errors, warnings, stats = run_validation()

    print("--- Stats ---")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print()

    if warnings:
        print("--- Warnings ---")
        for w in warnings:
            print(f"  WARN: {w}")
        print()

    if errors:
        print("--- Errors ---")
        for e in errors:
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
