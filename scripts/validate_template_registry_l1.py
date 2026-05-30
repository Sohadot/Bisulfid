#!/usr/bin/env python3
"""L1 template registry validator — read-only, stdlib only (Sprint 6M-C).

Validates legacy registry template references bridge to hardened publication frames.
Does not modify files.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
TEMPLATES = ROOT / "main/templates"
BUILD_PATH = ROOT / "scripts/build.py"
MIGRATION_REPORT = ROOT / "main/data/TEMPLATE_REGISTRY_MIGRATION_REPORT.md"

HARDENED_FRAMES = (
    "base.html",
    "home.html",
    "page.html",
    "reference.html",
    "term.html",
)

LEGACY_BRIDGE_TEMPLATES = (
    "reference_page.html",
    "term_page.html",
)

SKELETON_MARKER = "SKELETON TEMPLATE"

BRIDGE_MARKERS = (
    "Registry bridge",
    "Bridge target:",
    "reference-frame",
    "term-frame",
)

BUILD_BRIDGE_PATTERN = re.compile(
    r"TEMPLATE_FRAME_BRIDGE\s*:\s*dict\[str,\s*str\]\s*=\s*\{([^}]+)\}",
    re.S,
)


def load_routes() -> list[dict]:
    return json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]


def active_templates(routes: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for route in routes:
        name = route.get("template", "")
        if name:
            counts[name] = counts.get(name, 0) + 1
    return counts


def is_unresolved_skeleton(path: Path) -> bool:
    if not path.is_file():
        return True
    text = path.read_text(encoding="utf-8")
    if SKELETON_MARKER in text:
        return True
    if path.name in LEGACY_BRIDGE_TEMPLATES:
        return not any(marker in text for marker in BRIDGE_MARKERS)
    if path.stat().st_size < 800 and "SLOT:" in text:
        return True
    return False


def parse_build_bridge_map() -> dict[str, str]:
    if not BUILD_PATH.is_file():
        return {}
    source = BUILD_PATH.read_text(encoding="utf-8")
    match = BUILD_BRIDGE_PATTERN.search(source)
    if not match:
        return {}
    block = match.group(1)
    mapping: dict[str, str] = {}
    for line in block.splitlines():
        m = re.search(r'["\']([^"\']+\.html)["\']\s*:\s*["\']([^"\']+\.html)["\']', line)
        if m:
            mapping[m.group(1)] = m.group(2)
    return mapping


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {
        "active_template_names": 0,
        "hardened_frames_present": 0,
        "legacy_bridges_ok": 0,
        "build_bridge_entries": 0,
    }

    routes = load_routes()
    templates_used = active_templates(routes)
    stats["active_template_names"] = len(templates_used)

    for frame in HARDENED_FRAMES:
        if (TEMPLATES / frame).is_file():
            stats["hardened_frames_present"] += 1
        else:
            errors.append(f"missing hardened frame template: {frame}")

    for legacy in LEGACY_BRIDGE_TEMPLATES:
        path = TEMPLATES / legacy
        if not path.is_file():
            errors.append(f"missing legacy bridge template file: {legacy}")
            continue
        if is_unresolved_skeleton(path):
            errors.append(f"{legacy} is an unresolved skeleton placeholder")
        else:
            stats["legacy_bridges_ok"] += 1

    bridge_map = parse_build_bridge_map()
    stats["build_bridge_entries"] = len(bridge_map)
    if not bridge_map:
        errors.append("build.py TEMPLATE_FRAME_BRIDGE mapping not found")
    else:
        for legacy in LEGACY_BRIDGE_TEMPLATES:
            target = bridge_map.get(legacy)
            if not target:
                errors.append(f"build.py bridge missing for {legacy}")
            elif not (TEMPLATES / target).is_file():
                errors.append(f"bridge target missing for {legacy}: {target}")

    for template_name, count in sorted(templates_used.items()):
        path = TEMPLATES / template_name
        if not path.is_file():
            errors.append(f"active route template missing: {template_name} ({count} routes)")
            continue
        if template_name in LEGACY_BRIDGE_TEMPLATES:
            continue
        if is_unresolved_skeleton(path):
            if template_name in bridge_map:
                target = bridge_map[template_name]
                if not (TEMPLATES / target).is_file():
                    errors.append(
                        f"{template_name} is skeleton-only; bridge target {target} missing"
                    )
                else:
                    warnings.append(
                        f"{template_name}: skeleton file remains but build.py bridges to {target}"
                    )
            else:
                errors.append(
                    f"{template_name} is placeholder-only ({count} routes) with no build bridge"
                )

    if not MIGRATION_REPORT.is_file():
        errors.append("TEMPLATE_REGISTRY_MIGRATION_REPORT.md not found")
    else:
        report = MIGRATION_REPORT.read_text(encoding="utf-8")
        for section in (
            "legacy template references",
            "hardened template targets",
            "migration",
            "routes.json was not modified",
            "14,000",
        ):
            if section.lower() not in report.lower():
                warnings.append(f"migration report may omit section: {section}")

    if ROUTES_PATH.exists():
        warnings.append(
            "routes.json not modified in this sprint — template bridge via wrappers and build.py map"
        )

    return errors, warnings, stats


def main() -> int:
    print("=" * 60)
    print("Bisulfid Template Registry Validator — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only")
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
