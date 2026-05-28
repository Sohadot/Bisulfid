#!/usr/bin/env python3
"""L1 claim registry lock guardrail validator — read-only, stdlib only (Sprint 5N-B)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLAIMS_DIR = ROOT / "main/data/claims"
ROUTES_PATH = ROOT / "main/data/routes.json"

PROPOSAL_DOCS = (
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md",
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md",
    ROOT / "main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md",
    ROOT / "main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md",
)

NEGATION_WINDOW = 40


def claims_locking_complete(text: str) -> bool:
    lower = text.lower()
    for m in re.finditer(r"source-locking is complete", lower):
        before = lower[max(0, m.start() - 35) : m.start()]
        if "not" in before or "does not claim" in before:
            continue
        return True
    return False


def has_unnegated(text: str, phrase: str) -> bool:
    lower = text.lower()
    phrase_l = phrase.lower()
    start = 0
    while True:
        idx = lower.find(phrase_l, start)
        if idx == -1:
            return False
        before = lower[max(0, idx - NEGATION_WINDOW) : idx]
        if any(n in before for n in ("not ", "no ", "never ", "without ", "0 ", "inactive")):
            start = idx + len(phrase_l)
            continue
        return True
    return False


def run_validation() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {"claim_files": 0, "approved_claims": 0, "pending_review": 0}

    if not CLAIMS_DIR.is_dir():
        return ["claims directory missing"], [], stats

    for claim_file in sorted(CLAIMS_DIR.glob("*.json")):
        stats["claim_files"] += 1
        data = json.loads(claim_file.read_text(encoding="utf-8"))
        if data.get("status") != "inactive":
            errors.append(f"{claim_file.name}: registry status must be inactive")
        for claim in data.get("claims", []):
            if not isinstance(claim, dict):
                continue
            if claim.get("status") == "approved":
                stats["approved_claims"] += 1
                errors.append(f"{claim_file.name}: approved claim {claim.get('claim_id')}")
            if claim.get("status") == "pending_review":
                stats["pending_review"] += 1

    for path in PROPOSAL_DOCS:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if has_unnegated(text, "claim approval allowed now: yes"):
            errors.append(f"{rel}: allows claim approval now")
        if has_unnegated(text, "claims approved"):
            errors.append(f"{rel}: implies claims approved")
        if has_unnegated(text, "claim is approved"):
            if "no claim is approved" not in text.lower():
                errors.append(f"{rel}: implies claim approval")

    if ROUTES_PATH.exists():
        routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
        for route in routes:
            cf = ROOT / route["content_file"]
            if not cf.exists():
                continue
            body = cf.read_text(encoding="utf-8")
            rid = route["route_id"]
            if "[SOURCE REQUIRED]" not in body:
                warnings.append(f"{rid}: missing [SOURCE REQUIRED] marker (conceptual unresolved posture)")
            lower = body.lower()
            if claims_locking_complete(body):
                errors.append(f"{rid}: claims source-locking complete")
            if "publication-ready" in lower and "not publication-ready" not in lower:
                if "no" not in lower[:500]:
                    warnings.append(f"{rid}: check publication-ready negation in draft notice")

    return errors, warnings, stats


def main() -> int:
    errors, warnings, stats = run_validation()
    print("=== Claim Registry Lock L1 Validation ===")
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
