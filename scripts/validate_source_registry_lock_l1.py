#!/usr/bin/env python3
"""L1 source registry lock guardrail validator — read-only, stdlib only (Sprint 5N-B, 5N-S)."""
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

PUBLICATION_APPROVAL_STATUSES = frozenset({"approved", "locked", "final"})


def verification_ready_source_ids(data: dict) -> set[str]:
    vlr = data.get("verification_lock_resolution")
    if not isinstance(vlr, dict):
        return set()
    ready = vlr.get("verification_ready_sources", [])
    if not isinstance(ready, list):
        return set()
    ids: set[str] = set()
    for item in ready:
        if isinstance(item, str):
            ids.add(item)
        elif isinstance(item, dict):
            sid = item.get("source_id")
            if isinstance(sid, str) and sid:
                ids.add(sid)
    return ids


def verification_limited_posture(data: dict) -> bool:
    vlr = data.get("verification_lock_resolution")
    if not isinstance(vlr, dict):
        return False
    return vlr.get("resolved_posture") == "verification_limited"


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {
        "source_count": 0,
        "verified_sources": 0,
        "bibliographic_verified_sources": 0,
        "approved_sources": 0,
    }

    registry_path = SOURCE_REGISTRY if SOURCE_REGISTRY.exists() else LEGACY_REGISTRY
    if not registry_path.exists():
        return ["source_registry.json not found"], [], stats

    data = json.loads(registry_path.read_text(encoding="utf-8"))
    registry_status = data.get("status")
    if registry_status != "inactive":
        errors.append(
            f"source registry file status must remain inactive for publication lock "
            f"(got {registry_status!r}); inactive does not block bibliographic verification under verification_limited"
        )

    sources = data.get("sources", [])
    if not isinstance(sources, list):
        errors.append("source registry sources must be a list")
        return errors, warnings, stats

    limited = verification_limited_posture(data)
    ready_ids = verification_ready_source_ids(data)

    stats["source_count"] = len(sources)
    verified_ids: list[str] = []

    for src in sources:
        if not isinstance(src, dict):
            continue
        sid = src.get("source_id", "?")
        status = src.get("status", "")
        lock = src.get("source_lock_status", "")

        if lock in ("locked", "final", "verified"):
            stats["approved_sources"] += 1
            errors.append(
                f"{sid}: source_lock_status {lock!r} implies content source-lock complete; "
                "not permitted under verification_limited posture"
            )

        if status == "verified":
            stats["verified_sources"] += 1
            verified_ids.append(sid)
            if lock != "candidate":
                errors.append(
                    f"{sid}: bibliographic status 'verified' requires source_lock_status 'candidate' "
                    f"(got {lock!r}); verified is bibliographic evidence only, not source-locking"
                )
            elif not limited:
                errors.append(
                    f"{sid}: bibliographic status 'verified' requires "
                    "verification_lock_resolution.resolved_posture 'verification_limited' "
                    "(not registry/publication activation)"
                )
            elif sid not in ready_ids:
                errors.append(
                    f"{sid}: bibliographic status 'verified' not permitted — "
                    "source_id not listed in verification_ready_sources"
                )
            else:
                stats["bibliographic_verified_sources"] += 1
                warnings.append(
                    f"{sid}: bibliographic verification only — not claim approval, source-locking, "
                    "route publication, sitemap, navigation, or production readiness"
                )
        elif status in PUBLICATION_APPROVAL_STATUSES:
            stats["approved_sources"] += 1
            errors.append(
                f"{sid}: source status {status!r} implies registry/publication approval "
                "(distinct from bibliographic verification under verification_limited)"
            )

    for sid in verified_ids:
        if sid not in ready_ids:
            continue  # already reported above

    for sid in ready_ids:
        if sid not in verified_ids:
            warnings.append(
                f"{sid}: listed in verification_ready_sources but status is not yet 'verified'"
            )

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

    if stats["bibliographic_verified_sources"] > 0 and registry_status == "inactive":
        warnings.append(
            "registry file status inactive with bibliographic verified row(s): "
            "publication/claim/route locks remain enforced by separate validators"
        )

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
