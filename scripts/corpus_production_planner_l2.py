#!/usr/bin/env python3
"""L2 corpus production planner — dry-run status summary only (Sprint 5O-A).

Read-only. Python standard library only. Does not modify files or generate pages.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
SOURCE_REGISTRY_PATH = ROOT / "main/data/sources/source_registry.json"
CLAIMS_DIR = ROOT / "main/data/claims"
THRESHOLD_PATH = ROOT / "main/data/CORPUS_LAUNCH_THRESHOLD.md"
WAVE_CONTROL_PATH = ROOT / "main/data/CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def count_draft_backed(routes: list[dict]) -> tuple[int, int]:
    backed = 0
    missing = 0
    for route in routes:
        cf = ROOT / route.get("content_file", "")
        if cf.exists():
            backed += 1
        elif route.get("content_file"):
            missing += 1
    return backed, missing


def registry_lock_status() -> str:
    if not SOURCE_REGISTRY_PATH.exists():
        return "missing"
    reg = load_json(SOURCE_REGISTRY_PATH)
    status = reg.get("status", "unknown")
    sources = reg.get("sources", [])
    verified = sum(1 for s in sources if s.get("verified") is True)
    return f"{status} ({len(sources)} entries, {verified} verified)"


def claim_lock_status() -> str:
    if not CLAIMS_DIR.is_dir():
        return "missing"
    inactive = 0
    active = 0
    approved = 0
    for path in CLAIMS_DIR.glob("*_claims.json"):
        data = load_json(path)
        st = data.get("status", "unknown")
        if st == "inactive":
            inactive += 1
        else:
            active += 1
        for claim in data.get("claims", []):
            if claim.get("status") == "approved":
                approved += 1
    return f"{inactive} inactive registries, {active} active, {approved} approved claims"


def publication_lock_status(routes: list[dict]) -> str:
    published = sum(1 for r in routes if r.get("status") == "published")
    non_planned = sum(1 for r in routes if r.get("status") != "planned")
    if published or non_planned:
        return f"FAIL ({published} published, {non_planned} non-planned)"
    return "LOCKED (all planned)"


def indexation_lock_status(routes: list[dict]) -> str:
    indexable = sum(1 for r in routes if r.get("indexable") is True)
    if indexable:
        return f"FAIL ({indexable} indexable)"
    return "LOCKED (none indexable)"


def sitemap_lock_status(routes: list[dict]) -> str:
    in_sitemap = sum(1 for r in routes if r.get("in_sitemap") is True)
    if in_sitemap:
        return f"FAIL ({in_sitemap} in_sitemap)"
    return "LOCKED (none in_sitemap)"


def next_eligible_wave_type(route_count: int, draft_backed: int) -> str:
    if route_count < 500:
        if WAVE_CONTROL_PATH.exists():
            return "route_registration_wave_2_planning (L2 dry-run; source/claim gates mandatory first)"
        return "route_registration_wave_planning"
    return "publication_readiness_wave_planning (only after 500 governed pages pass all gates)"


def main() -> int:
    print("=" * 60)
    print("Bisulfid Corpus Production Planner — Layer 2 (dry-run)")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only / dry-run — no files modified")
    print("=" * 60)
    print()

    if not ROUTES_PATH.exists():
        print("ERROR: routes.json not found")
        return 1

    routes = load_json(ROUTES_PATH)["routes"]
    route_count = len(routes)
    draft_backed, missing_drafts = count_draft_backed(routes)

    threshold_active = THRESHOLD_PATH.exists() and "500" in THRESHOLD_PATH.read_text(encoding="utf-8")

    print("--- Production status summary ---")
    print(f"current_route_count: {route_count}")
    print(f"draft_backed_route_count: {draft_backed}")
    print(f"missing_draft_count: {missing_drafts}")
    print(f"route_publication_lock: {publication_lock_status(routes)}")
    print(f"indexation_lock: {indexation_lock_status(routes)}")
    print(f"sitemap_lock: {sitemap_lock_status(routes)}")
    print(f"source_registry_lock: {registry_lock_status()}")
    print(f"claim_registry_lock: {claim_lock_status()}")
    print(f"500_page_threshold_active: {threshold_active}")
    print(f"production_can_safely_proceed: no")
    print(f"next_eligible_planning_wave_type: {next_eligible_wave_type(route_count, draft_backed)}")
    print()
    print("--- Governance note ---")
    print("L2 planner reports status only. No routes, content, sources, or claims are modified.")
    print("Mass production requires L2 gate validation + L1 corpus runtime + source/claim guardrails.")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
