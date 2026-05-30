#!/usr/bin/env python3
"""L1 claim registry lock guardrail validator — read-only, stdlib only (Sprint 5N-B, 5N-U)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLAIMS_DIR = ROOT / "main/data/claims"
ROUTES_PATH = ROOT / "main/data/routes.json"
SOURCE_REGISTRY = ROOT / "main/data/sources/source_registry.json"

PROPOSAL_DOCS = (
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md",
    ROOT / "main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md",
    ROOT / "main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md",
    ROOT / "main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md",
)

NEGATION_WINDOW = 40

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
            "claim_approval_lock_resolution.resolved_posture 'approval_limited' "
            "(not claim registry / publication activation)"
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
            f"{claim_file}: {cid}: approved claim source_ids must match approval_ready_claims "
            f"(expected {expected_sources!r}, got {claim_sources!r})"
        )

    for sid in claim_sources:
        src = source_postures.get(sid)
        if not src:
            errors.append(f"{claim_file}: {cid}: linked source {sid!r} not found in source_registry")
            continue
        if src.get("status") != "verified":
            errors.append(
                f"{claim_file}: {cid}: narrow claim approval requires verified source {sid!r} "
                f"(got {src.get('status')!r})"
            )
        if src.get("source_lock_status") != "candidate":
            errors.append(
                f"{claim_file}: {cid}: narrow claim approval requires source_lock_status 'candidate' "
                f"on {sid!r}; approved is not content source-locking"
            )

    related_routes = claim.get("related_routes", [])
    if cid == "CLM-TERM-MOS2-DE-001":
        if related_routes != ["de_core_mos2"]:
            errors.append(
                f"{claim_file}: {cid}: approved boundary limited to de_core_mos2 route scope"
            )
        allowed_pages = claim.get("allowed_pages", [])
        if allowed_pages != ["de_core_mos2"]:
            errors.append(
                f"{claim_file}: {cid}: approved boundary limited to de_core_mos2 allowed_pages"
            )

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
        registry_status = data.get("status")
        if registry_status != "inactive":
            errors.append(
                f"{fname}: claim registry file status must remain inactive for publication lock "
                f"(got {registry_status!r}); inactive does not block narrow claim approval under approval_limited"
            )

        limited = approval_limited_posture(data)
        ready_map = approval_ready_claim_map(data)

        for claim in data.get("claims", []):
            if not isinstance(claim, dict):
                continue
            st = claim.get("status", "")
            cid = claim.get("claim_id", "?")

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
                        f"{cid}: narrow claim approval only — not content source-locking, "
                        "route publication, sitemap, navigation, or production readiness"
                    )
            elif st == "pending_review":
                stats["pending_review"] += 1

        for cid in ready_map:
            if not any(
                isinstance(c, dict) and c.get("claim_id") == cid and c.get("status") == "approved"
                for c in data.get("claims", [])
            ):
                warnings.append(
                    f"{fname}: {cid} listed in approval_ready_claims but status is not yet 'approved'"
                )

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

    if stats["narrow_approved_claims"] > 0:
        warnings.append(
            "claim registry file status inactive with narrow approved claim(s): "
            "publication/route/content locks remain enforced by separate validators"
        )

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
