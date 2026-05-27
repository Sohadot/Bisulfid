#!/usr/bin/env python3
"""L1 claim registry lock validator — read-only, stdlib only (Sprint 5K)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
CLAIMS_DIR = ROOT / "main/data/claims"
SOURCE_REGISTRY = ROOT / "main/data/sources/source_registry.json"


def claims_locking_complete(text: str) -> bool:
    lower = text.lower()
    for m in re.finditer(r"source-locking is complete", lower):
        before = lower[max(0, m.start() - 35) : m.start()]
        if "not" in before or "does not claim" in before:
            continue
        return True
    return False


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"claim_files": 0, "approved_claims": 0, "pending_review": 0}

    if not CLAIMS_DIR.is_dir():
        return ["claims directory missing"], [], {}

    for claim_file in sorted(CLAIMS_DIR.glob("*.json")):
        stats["claim_files"] += 1
        data = json.loads(claim_file.read_text(encoding="utf-8"))
        if data.get("status") != "inactive":
            errors.append(f"{claim_file.name}: registry status must be inactive")
        claims = data.get("claims", [])
        if not isinstance(claims, list):
            continue
        for claim in claims:
            if not isinstance(claim, dict):
                continue
            st = claim.get("status", "")
            if st == "approved":
                stats["approved_claims"] += 1
                errors.append(f"{claim_file.name}: approved claim {claim.get('claim_id')}")
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
