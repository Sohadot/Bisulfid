#!/usr/bin/env python3
"""L1 claim registry lock validator — read-only, stdlib only (Sprint 5K, 5N-U)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
CLAIMS_DIR = ROOT / "main/data/claims"
SOURCE_REGISTRY = ROOT / "main/data/sources/source_registry.json"

REQUIRED_PROHIBITED_FOR_APPROVED = frozenset({
    "chemical safety",
    "medical claims",
    "market data",
    "route publication",
    "removal of [SOURCE REQUIRED] markers",
    "source-locking by itself",
})


def claims_locking_complete(text: str) -> bool:
    lower = text.lower()
    for m in re.finditer(r"source-locking is complete", lower):
        before = lower[max(0, m.start() - 35) : m.start()]
        if "not" in before or "does not claim" in before:
            continue
        return True
    return False


def approval_ready_claim_map(data: dict) -> dict[str, dict]:
    calr = data.get("claim_approval_lock_resolution")
    if not isinstance(calr, dict):
        return {}
    ready = calr.get("approval_ready_claims", [])
    if not isinstance(ready, list):
        return {}
    out: dict[str, dict] = {}
    for item in ready:
        if isinstance(item, dict):
            cid = item.get("claim_id")
            if isinstance(cid, str) and cid:
                out[cid] = item
    return out


def approval_limited_posture(data: dict) -> bool:
    calr = data.get("claim_approval_lock_resolution")
    if not isinstance(calr, dict):
        return False
    return calr.get("resolved_posture") == "approval_limited"


def load_source_postures() -> dict[str, dict]:
    if not SOURCE_REGISTRY.exists():
        return {}
    data = json.loads(SOURCE_REGISTRY.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for src in data.get("sources", []):
        if isinstance(src, dict):
            sid = src.get("source_id")
            if sid:
                out[sid] = src
    return out


def validate_approved_claim_boundary(
    claim_file: str,
    claim: dict,
    ready_map: dict[str, dict],
    limited: bool,
    source_postures: dict[str, dict],
) -> list[str]:
    errors: list[str] = []
    cid = claim.get("claim_id", "?")
    if claim.get("status") != "approved":
        return errors

    if not limited:
        errors.append(
            f"{claim_file}: {cid}: narrow claim approval requires "
            "claim_approval_lock_resolution.resolved_posture 'approval_limited'"
        )
        return errors

    ready = ready_map.get(cid)
    if not ready:
        errors.append(
            f"{claim_file}: {cid}: narrow claim status 'approved' not permitted — "
            "claim_id not listed in approval_ready_claims"
        )
        return errors

    if claim.get("claim_type") != "terminology":
        errors.append(f"{claim_file}: {cid}: approved claim must remain terminology-scoped")

    expected_sources = ready.get("source_ids", [])
    if not isinstance(expected_sources, list):
        expected_sources = []
    claim_sources = claim.get("source_ids", [])
    if claim_sources != expected_sources:
        errors.append(
            f"{claim_file}: {cid}: approved claim source_ids must match approval_ready_claims"
        )

    for sid in claim_sources:
        src = source_postures.get(sid)
        if not src:
            errors.append(f"{claim_file}: {cid}: linked source {sid!r} not found in source_registry")
            continue
        if src.get("status") != "verified":
            errors.append(
                f"{claim_file}: {cid}: narrow claim approval requires verified source {sid!r}"
            )
        if src.get("source_lock_status") != "candidate":
            errors.append(
                f"{claim_file}: {cid}: narrow claim approval requires source_lock_status 'candidate' "
                f"on {sid!r}; approved is not content source-locking"
            )

    if cid == "CLM-TERM-MOS2-DE-001":
        if claim.get("related_routes") != ["de_core_mos2"]:
            errors.append(f"{claim_file}: {cid}: approved boundary limited to de_core_mos2")
        if claim.get("allowed_pages") != ["de_core_mos2"]:
            errors.append(f"{claim_file}: {cid}: approved allowed_pages limited to de_core_mos2")

    prohibited = set(claim.get("prohibited_uses", []))
    missing = REQUIRED_PROHIBITED_FOR_APPROVED - prohibited
    if missing:
        errors.append(
            f"{claim_file}: {cid}: approved claim missing required prohibited_uses: {sorted(missing)}"
        )

    return errors


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {
        "claim_files": 0,
        "approved_claims": 0,
        "narrow_approved_claims": 0,
        "pending_review": 0,
    }

    if not CLAIMS_DIR.is_dir():
        return ["claims directory missing"], [], stats

    source_postures = load_source_postures()

    for claim_file in sorted(CLAIMS_DIR.glob("*.json")):
        stats["claim_files"] += 1
        data = json.loads(claim_file.read_text(encoding="utf-8"))
        fname = claim_file.name
        if data.get("status") != "inactive":
            errors.append(f"{fname}: registry status must be inactive")
        claims = data.get("claims", [])
        if not isinstance(claims, list):
            continue

        limited = approval_limited_posture(data)
        ready_map = approval_ready_claim_map(data)

        for claim in claims:
            if not isinstance(claim, dict):
                continue
            st = claim.get("status", "")
            if st == "approved":
                stats["approved_claims"] += 1
                boundary_errors = validate_approved_claim_boundary(
                    fname, claim, ready_map, limited, source_postures
                )
                if boundary_errors:
                    errors.extend(boundary_errors)
                else:
                    stats["narrow_approved_claims"] += 1
                    warnings.append(
                        f"{claim.get('claim_id')}: narrow claim approval only — not publication readiness"
                    )
            if st == "pending_review":
                stats["pending_review"] += 1

    if SOURCE_REGISTRY.exists():
        src = json.loads(SOURCE_REGISTRY.read_text(encoding="utf-8"))
        verified = [
            s for s in src.get("sources", [])
            if isinstance(s, dict) and s.get("status") in ("verified", "locked")
        ]
        stats["verified_sources"] = len(verified)
        if verified:
            warnings.append(
                f"source_registry has {len(verified)} verified/locked sources; "
                "content must not claim full source-locking complete"
            )

    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    for route in routes:
        cf = ROOT / route["content_file"]
        if not cf.exists():
            continue
        text = cf.read_text(encoding="utf-8").lower()
        rid = route["route_id"]
        if claims_locking_complete(text):
            errors.append(f"{rid}: claims source-locking complete")
        if "all claims approved" in text or "claims are approved" in text:
            errors.append(f"{rid}: implies claims approved")
        if "claim is approved" in text:
            if "no claim is approved" not in text and "kein claim ist freigegeben" not in text:
                errors.append(f"{rid}: implies individual claim approval")
        if "[source required]" in text:
            if "satisfied" in text and "not satisfied" not in text:
                warnings.append(f"{rid}: may treat [SOURCE REQUIRED] as satisfied")

    if stats["narrow_approved_claims"] > 0:
        warnings.append(
            "narrow approved claim(s) present; claim registry file remains inactive — "
            "not route publication or production readiness"
        )

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Corpus Claims L1 Validation ===")
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
