#!/usr/bin/env python3
"""L1 Bisulfid design system validator — read-only, stdlib only (Sprint 6N-A).

Validates proprietary design-system foundation without external dependencies.
Does not modify any files.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_ROOT = ROOT / "bisulfid-design-system"

REQUIRED_FILES = (
    "README.md",
    "DESIGN_SYSTEM_DOCTRINE.md",
    "tokens/colors.css",
    "tokens/typography.css",
    "tokens/spacing.css",
    "tokens/motion.css",
    "tokens/depth.css",
    "tokens/governance.css",
    "components/term-node.css",
    "components/term-card.css",
    "components/source-crystal.css",
    "components/governance-banner.css",
    "components/language-depth.css",
    "components/relation-lattice.css",
    "assets/README.md",
    "assets/term-node.svg",
    "assets/missing-e-boundary.svg",
    "assets/source-crystal.svg",
    "assets/chemical-space.svg",
    "engine/README.md",
    "engine/motion-governor.js",
)

FORBIDDEN_PATTERNS = (
    re.compile(r"https?://", re.I),
    re.compile(r"cdn\.|unpkg\.|jsdelivr|googleapis|bootstrap|tailwind", re.I),
    re.compile(r"\bnpm\b|\byarn\b|\bpnpm\b|package\.json", re.I),
    re.compile(r"import\s+.*from\s+['\"]", re.I),
    re.compile(r"require\s*\(", re.I),
    re.compile(r"three\.js|react|vue|angular", re.I),
)

NETWORK_PATTERNS = (
    re.compile(r"\bfetch\s*\(", re.I),
    re.compile(r"XMLHttpRequest", re.I),
    re.compile(r"navigator\.sendBeacon", re.I),
    re.compile(r"google-analytics|gtag\(", re.I),
)


def collect_ds_files() -> list[Path]:
    files: list[Path] = []
    if not DS_ROOT.is_dir():
        return files
    for path in DS_ROOT.rglob("*"):
        if path.is_file():
            files.append(path)
    return files


def validate() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (DS_ROOT / rel).is_file():
            errors.append(f"missing required file: bisulfid-design-system/{rel}")

    css_files = list((DS_ROOT / "tokens").glob("*.css")) + list(
        (DS_ROOT / "components").glob("*.css")
    )
    if css_files:
        has_custom_props = any("--bs-" in f.read_text(encoding="utf-8") for f in css_files)
        if not has_custom_props:
            errors.append("CSS files missing --bs- custom properties")
    else:
        errors.append("no CSS token/component files found")

    motion_css = DS_ROOT / "tokens/motion.css"
    if motion_css.is_file():
        text = motion_css.read_text(encoding="utf-8")
        if "prefers-reduced-motion" not in text:
            errors.append("motion.css missing prefers-reduced-motion")

    gov_css = DS_ROOT / "tokens/governance.css"
    if gov_css.is_file():
        gtext = gov_css.read_text(encoding="utf-8")
        if "source-required" not in gtext.lower() and "SOURCE REQUIRED" not in gtext:
            errors.append("governance.css missing source-required tokens")
        if "source-approved" not in gtext.lower() or "claim-approved" not in gtext.lower():
            errors.append("governance.css missing approval boundary tokens")

    for css in css_files:
        ct = css.read_text(encoding="utf-8").lower()
        if "source-required" not in ct and css.name in (
            "term-node.css",
            "source-crystal.css",
            "governance-banner.css",
        ):
            errors.append(f"{css.name} missing source-required representation")

    motion_js = DS_ROOT / "engine/motion-governor.js"
    if motion_js.is_file():
        jtext = motion_js.read_text(encoding="utf-8")
        if "prefers-reduced-motion" not in jtext:
            errors.append("motion-governor.js missing prefers-reduced-motion")
        for pattern in NETWORK_PATTERNS:
            if pattern.search(jtext):
                errors.append(f"motion-governor.js forbidden network pattern: {pattern.pattern}")

    for path in collect_ds_files():
        text = path.read_text(encoding="utf-8")
        suffix = path.suffix.lower()
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                if suffix == ".svg" and "xmlns=" in text:
                    continue
                if suffix == ".md":
                    continue
                rel = path.relative_to(ROOT)
                errors.append(f"{rel}: forbidden pattern {pattern.pattern}")

    svg_dir = DS_ROOT / "assets"
    for name in ("term-node.svg", "missing-e-boundary.svg", "source-crystal.svg", "chemical-space.svg"):
        svg = svg_dir / name
        if svg.is_file():
            st = svg.read_text(encoding="utf-8")
            if "<svg" not in st:
                errors.append(f"{name} is not valid SVG")

    engine_readme = DS_ROOT / "engine/README.md"
    if engine_readme.is_file():
        if "WebGL" not in engine_readme.read_text(encoding="utf-8"):
            warnings.append("engine/README.md should document WebGL boundary")

    # Public output must not be modified in this sprint — check git if available
    import subprocess

    r = subprocess.run(
        ["git", "diff", "--name-only", "HEAD", "--", "site/public", "site/_sample"],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    if r.stdout.strip():
        errors.append(f"public/quarantine output modified: {r.stdout.strip()}")

    pages_wf = ROOT / ".github/workflows/pages-public-deploy.yml"
    if pages_wf.is_file():
        r2 = subprocess.run(
            ["git", "diff", "--name-only", "HEAD", "--", str(pages_wf)],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        if r2.stdout.strip():
            errors.append("pages-public-deploy.yml modified in this sprint")

    return errors, warnings


def main() -> int:
    print("=" * 60)
    print("Bisulfid Design System Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {DS_ROOT}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    errors, warnings = validate()
    print(f"Required files: {len(REQUIRED_FILES)}")
    print(f"Design-system files on disk: {len(collect_ds_files())}")
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
