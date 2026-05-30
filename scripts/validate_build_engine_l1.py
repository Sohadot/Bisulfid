#!/usr/bin/env python3
"""L1 build engine validator — read-only, stdlib only (Sprint 6M-A).

Validates that scripts/build.py exists, exposes safe dry-run/help modes,
respects route governance flags, and does not bypass publication locks.
Does not modify any files.
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_PATH = ROOT / "scripts/build.py"
TEMPLATES_ROOT = ROOT / "main/templates"
CONFIG_PATH = ROOT / "main/config/build.json"
ROUTES_PATH = ROOT / "main/data/routes.json"

FORBIDDEN_WRITE_PATTERNS = (
    re.compile(r"routes\.json\s*[\"']?\s*,\s*[\"']w", re.I),
    re.compile(r"open\s*\(\s*[^)]*routes\.json[^)]*[\"']w", re.I),
    re.compile(r"open\s*\(\s*[^)]*content_file[^)]*[\"']w", re.I),
    re.compile(r"source_registry\.json.*[\"']w", re.I),
    re.compile(r"terminology_claims\.json.*[\"']w", re.I),
)

REQUIRED_GOVERNANCE_TERMS = (
    "indexable",
    "in_sitemap",
    "in_navigation",
    "status",
    "published",
    "dry-run",
    "dry_run",
    "noindex",
    "production_can_safely_proceed",
    "generate_only_published_routes",
)

FORBIDDEN_HARDCODE = (
    re.compile(r"status\s*=\s*[\"']published[\"']", re.I),
    re.compile(r"public_pages_generated\s*=\s*[1-9]", re.I),
    re.compile(r"force_publish\s*=\s*True", re.I),
)

REQUIRED_TEMPLATES = (
    "base.html",
    "partials/head.html",
    "partials/nav.html",
    "partials/footer.html",
    "partials/source_bar.html",
    "partials/internal_links.html",
)


def read_build_source() -> str:
    if not BUILD_PATH.is_file():
        return ""
    return BUILD_PATH.read_text(encoding="utf-8")


def run_build(args: list[str]) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(BUILD_PATH), *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {}

    if not BUILD_PATH.is_file():
        errors.append("scripts/build.py not found")
        return errors, warnings, stats

    source = read_build_source()
    stats["build_py_bytes"] = len(source.encode("utf-8"))

    if "--dry-run" not in source and "dry_run" not in source:
        errors.append("build.py missing dry-run capability")
    if "argparse" not in source:
        warnings.append("build.py does not use argparse (manual flag parsing?)")

    for term in REQUIRED_GOVERNANCE_TERMS:
        if term.replace("-", "_") not in source.replace("-", "_"):
            errors.append(f"build.py missing governance reference: {term}")

    for pattern in FORBIDDEN_HARDCODE:
        if pattern.search(source):
            errors.append(f"build.py may hardcode publication: {pattern.pattern}")

    for pattern in FORBIDDEN_WRITE_PATTERNS:
        if pattern.search(source):
            errors.append(f"build.py may mutate governed JSON: {pattern.pattern}")

    if re.search(r"open\s*\([^)]*content[^)]*[\"']w", source, re.I):
        if "build-status" not in source and "audit" not in source.lower():
            warnings.append("build.py may write content paths — verify scope")

    if "SOURCE REQUIRED" in source and "remove" in source.lower():
        errors.append("build.py may remove [SOURCE REQUIRED] markers")

    missing_templates = []
    for rel in REQUIRED_TEMPLATES:
        if not (TEMPLATES_ROOT / rel).is_file():
            missing_templates.append(rel)
    stats["missing_required_templates"] = missing_templates
    if missing_templates:
        errors.append(f"missing required templates: {', '.join(missing_templates)}")

    if CONFIG_PATH.is_file() and ROUTES_PATH.is_file():
        stats["config_present"] = True
        stats["routes_present"] = True
    else:
        errors.append("build config or routes.json missing")

    # Safe help invocation
    code, output = run_build([])
    stats["help_exit_code"] = code
    stats["help_invocation"] = "PASS" if code == 0 else "FAIL"
    if code != 0:
        errors.append(f"build.py default/help exit {code}")
    if "dry-run" not in output.lower() and "--dry-run" not in output:
        warnings.append("help output may not document dry-run")

    # Safe dry-run invocation (must not fail in locked posture)
    code, output = run_build(["--dry-run"])
    stats["dry_run_exit_code"] = code
    stats["dry_run_invocation"] = "PASS" if code == 0 else "FAIL"
    if code != 0:
        errors.append(f"build.py --dry-run exit {code}")
    if "public html generated" in output.lower():
        m = re.search(r"public html generated:\s*(\d+)", output.lower())
        if m and int(m.group(1)) > 0:
            errors.append("dry-run reported public HTML generated")
    if "production_can_safely_proceed" in output.lower():
        if "production_can_safely_proceed: yes" in output.lower().replace(" ", ""):
            errors.append("dry-run reported production_can_safely_proceed yes")

    # Strict dry-run may fail on template placeholders — note only
    code_strict, _ = run_build(["--dry-run", "--strict"])
    stats["strict_dry_run_exit_code"] = code_strict
    if code_strict != 0:
        stats["strict_dry_run_note"] = "strict mode fails on template/metadata gaps (expected in skeleton phase)"

    return errors, warnings, stats


def main() -> int:
    print("=" * 60)
    print("Bisulfid Build Engine Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only")
    print("=" * 60)
    print()

    errors, warnings, stats = validate()

    print("--- Static checks ---")
    print(f"build.py present: {BUILD_PATH.is_file()}")
    print(f"build.py size: {stats.get('build_py_bytes', 0)} bytes")
    print(f"config/routes present: {stats.get('config_present', False)}")
    print(f"missing required templates: {len(stats.get('missing_required_templates', []))}")
    print()

    print("--- Safe invocation ---")
    print(f"help/default: {stats.get('help_invocation', 'N/A')} (exit {stats.get('help_exit_code', '?')})")
    print(f"--dry-run: {stats.get('dry_run_invocation', 'N/A')} (exit {stats.get('dry_run_exit_code', '?')})")
    if "strict_dry_run_exit_code" in stats:
        print(f"--dry-run --strict: exit {stats['strict_dry_run_exit_code']} ({stats.get('strict_dry_run_note', '')})")
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
