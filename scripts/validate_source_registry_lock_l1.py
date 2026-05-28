#!/usr/bin/env python3
"""L1 source registry lock guardrail validator — read-only, stdlib only (Sprint 5N-B)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOURCE_REGISTRY = ROOT / "main/data/sources/source_registry.json"
LEGACY_REGISTRY = ROOT / "main/data/source_registry.json"

PROPOSAL_DOCS = (
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md",
    ROOT / "main/data/SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md",
    ROOT / "main/data/SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md",
)


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"source_count": 0, "verified_sources": 0, "approved_sources": 0}

    registry_path = SOURCE_REGISTRY if SOURCE_REGISTRY.exists() else LEGACY_REGISTRY
    if not registry_path.exists():
        return ["source_registry.json not found"], [], stats

    data = json.loads(registry_path.read_text(encoding="utf-8"))
    if data.get("status") != "inactive":
        errors.append(f"source registry status must be inactive (got {data.get('status')!r})")

    sources = data.get("sources", [])
    if not isinstance(sources, list):
        errors.append("source registry sources must be a list")
        return errors, warnings, stats

    stats["source_count"] = len(sources)
    for src in sources:
        if not isinstance(src, dict):
            continue
        sid = src.get("source_id", "?")
        status = src.get("status", "")
        lock = src.get("source_lock_status", "")
        if status in ("verified", "approved", "locked", "final"):
            stats["verified_sources"] += 1
            errors.append(f"{sid}: source status {status!r} implies approved registry entry")
        if lock in ("locked", "final", "verified"):
            stats["approved_sources"] += 1
            errors.append(f"{sid}: source_lock_status {lock!r} implies source-lock complete")
        if status == "approved":
            stats["approved_sources"] += 1

    governed_by = data.get("governed_by", "")
    if governed_by and "SOURCE_POLICY" not in governed_by:
        warnings.append(f"registry governed_by unexpected: {governed_by!r}")

    for path in PROPOSAL_DOCS:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8").lower()
        rel = path.relative_to(ROOT)
        if re.search(r"source_registry\.json was modified(?!.*not modified)", text):
            errors.append(f"{rel}: contradicts unchanged registry posture")
        if "new source entries were added" in text and "no source entries" not in text:
            if "0" not in text and "not added" not in text:
                errors.append(f"{rel}: implies new source entries were added")
        if "registry entry added" in text and "no entries" not in text and "0" not in text:
            warnings.append(f"{rel}: verify registry entry language is negated")

    if stats["source_count"] == 0:
        warnings.append("source registry has zero source rows (expected seeded candidates)")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Source Registry Lock L1 Validation ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print()
    if errors:
        print("FAIL — errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("PASS — no blocking errors")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    print(f"\nSummary: {'FAIL' if errors else 'PASS'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
