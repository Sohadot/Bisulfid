#!/usr/bin/env python3
"""release_checks_tests.py — the human gates of a reference release cannot be self-granted (Release-01)."""

import copy
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "publication"))
import release_checks as rc  # noqa: E402

FAILS = []
KO = "KO-MOS2-SCIENTIFIC-001"
CLAIMS = rc._ko(KO)["claim_ids"]


def ok(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


GOOD = {"knowledge_object_id": KO, "preparer": "claude-code-agent", "reviews": [{
    "status": "signed", "reviewer": "Dr. Fixture Reviewer", "reviewer_kind": "human", "independence_declared": True,
    "signed_on": "2026-11-01", "claim_verdicts": [{"claim_id": c, "verdict": "confirmed"} for c in CLAIMS], "findings": []}]}


def with_review(**chg):
    r = copy.deepcopy(GOOD)
    r["reviews"][0].update(chg)
    return r


ok("01_complete_independent_human_review_validates", rc.validation_ok(KO, GOOD) == (True, []))
ok("02_no_record_does_not_validate", rc.validation_ok(KO, {"reviews": []})[0] is False)
ok("03_preparer_cannot_review", rc.validation_ok(KO, with_review(reviewer="claude-code-agent"))[0] is False)
ok("04_agent_cannot_review", rc.validation_ok(KO, with_review(reviewer="Claude (automated)", reviewer_kind="agent"))[0] is False)
ok("05_unsigned_review_does_not_count", rc.validation_ok(KO, with_review(status="draft"))[0] is False)
ok("06_partial_claim_coverage_refused",
   rc.validation_ok(KO, with_review(claim_verdicts=[{"claim_id": CLAIMS[0], "verdict": "confirmed"}]))[0] is False)
ok("07_rejected_claim_refused", rc.validation_ok(KO, with_review(claim_verdicts=[{"claim_id": c, "verdict": "rejected"} for c in CLAIMS]))[0] is False)
ok("08_open_finding_refused", rc.validation_ok(KO, with_review(findings=[{"id": "F1", "status": "open"}]))[0] is False)
ok("09_independence_must_be_declared", rc.validation_ok(KO, with_review(independence_declared=False))[0] is False)

srcs = {"S1": {"source_id": "S1", "source_lock_status": "locked"}, "S2": {"source_id": "S2", "source_lock_status": "candidate"}}
signed = {"S1": {"source_id": "S1", "status": "signed", "signed_by": "Registry Owner", "preparer": "claude-code-agent",
                 "checklist": {k: "pass" for k in rc.policy()["source_lock_checklist"]}}}
ok("10_signed_complete_lock_is_honoured", rc.source_lock_ok("S1", signed, srcs) == (True, []))
ok("11_candidate_status_is_not_locked", rc.source_lock_ok("S2", signed, srcs)[0] is False)
ok("12_agent_signed_lock_refused", rc.source_lock_ok("S1", {"S1": dict(signed["S1"], signed_by="claude-code-agent")}, srcs)[0] is False)
ok("13_incomplete_checklist_refused",
   rc.source_lock_ok("S1", {"S1": dict(signed["S1"], checklist=dict(signed["S1"]["checklist"], L6="pending"))}, srcs)[0] is False)

ok("14_no_owner_activation_today", rc.claims_active_ok(KO)[0] is False and rc.release_authorized_ok(KO)[0] is False)
act = [{"knowledge_object_id": KO, "status": "signed", "signed_by": "Site Owner", "signed_on": "2026-11-02", "claim_ids": CLAIMS}]
ok("15_signed_owner_activation_accepted", rc.claims_active_ok(KO, act) == (True, []))
ok("16_activation_must_cover_exact_claims", rc.claims_active_ok(KO, [dict(act[0], claim_ids=CLAIMS[:1])])[0] is False)
ok("17_agent_cannot_activate", rc.claims_active_ok(KO, [dict(act[0], signed_by="claude-code-agent")])[0] is False)

claimed = {"governance_posture": "governed", "evidence_posture": "evidence_locked", "claim_posture": "claim_approved_narrow",
           "validation_posture": "validated", "information_gain_posture": "ig_reviewed_route_realization",
           "release_authorization": "authorized"}
p, notes = rc.honoured_postures(KO, claimed)
ok("18_self_declared_green_postures_are_all_downgraded_today",
   (p["validation_posture"], p["evidence_posture"], p["claim_posture"], p["release_authorization"])
   == ("not_validated", "evidence_sufficient", "claim_pending", "not_authorized") and p["governance_posture"] == "reference_draft"
   and p["information_gain_posture"] == "ig_reviewed_no_new_route" and len(notes) == 6)

print("=" * 56)
print("RESULT: " + ("PASS — release gates cannot be self-granted" if not FAILS else f"FAIL — {FAILS}"))
sys.exit(1 if FAILS else 0)
