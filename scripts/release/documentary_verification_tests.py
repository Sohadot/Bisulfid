#!/usr/bin/env python3
"""documentary_verification_tests.py — the low-risk documentary pathway: positive and adversarial proofs."""

import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "publication"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "governance_scaffolding"))
import contract_c_derive as cc  # noqa: E402
import documentary_verification as dv  # noqa: E402
import release_checks as rc  # noqa: E402

FAILS = []
TERM, MOS2 = "KO-BISULFID-TERMINOLOGY-001", "KO-MOS2-SCIENTIFIC-001"
ORIG_POLICY = dv.policy


def ok(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


def adopted(by="Site Owner (fixture)", on="2026-11-01"):
    return lambda: dict(ORIG_POLICY(), status="adopted", adopted_by=by, adopted_on=on)


BASE = dv.evaluate(TERM)

# 1 a documented low-risk reference passes without any fabricated signature
reviews = json.load(open(os.path.join(ROOT, "main", "data", "release", "reviews", TERM + ".json")))
locks = json.load(open(os.path.join(ROOT, "main", "data", "sources", "source_lock_records.json")))
ok("01_low_risk_reference_documentary_verified_without_signatures",
   BASE["verification_level"] == "documentary_verified" and BASE["risk_class"] == "low_risk_informational"
   and reviews["reviews"] == [] and locks["records"] == [] and all(o["outcome"] == "documentary_verified" for o in BASE["claim_outcomes"])
   and len(BASE["claim_outcomes"]) == 11)

# 2 an unsupported claim cannot pass
claims = dv._claims()
c2 = copy.deepcopy(claims)
c2["CLM-TERM-GERMAN-ID-RULE-001"]["supporting_evidence_ids"] = []
r2 = dv.evaluate(TERM, {"claims": c2})
c3 = copy.deepcopy(claims)
c3["CLM-TERM-IUPAC-HS-NAMES-001"]["status"] = "pending_review"
r3 = dv.evaluate(TERM, {"claims": c3})
ko = rc._ko(TERM)
ko_bad = copy.deepcopy(ko)
ko_bad["claim_ids"] = ko_bad["claim_ids"] + ["CLM-TERM-BISULFID-001"]
ko_bad["claim_bindings"] = ko_bad["claim_bindings"] + [{"claim_id": "CLM-TERM-BISULFID-001", "evidence_ids": ["EVD-TERM-BADGER-BISULFID-USAGE"]}]
r4 = dv.evaluate(TERM, {"ko": ko_bad})
ok("02_unsupported_or_pending_claim_cannot_pass",
   r2["verification_level"] == "not_verified" and r3["verification_level"] == "not_verified"
   and r4["verification_level"] == "not_verified")

# 3 high-risk content never gets the exemption automatically
spec = copy.deepcopy(dv._spec_for(TERM))
spec["modules"][0]["paragraphs"][1]["text"] += " Avoid exposure above the occupational exposure limit."
r5 = dv.evaluate(TERM, {"spec": spec})
pc = dv._pc_for(TERM)
r6 = dv.evaluate(TERM, {"pc": dict(pc, risk_classification={"class": "higher_risk", "rationale": "x"})})
r7 = dv.evaluate(TERM, {"pc": {k: v for k, v in pc.items() if k != "risk_classification"}})
ok("03_high_risk_or_undeclared_fails_closed",
   r5["risk_class"] == "higher_risk" and r5["verification_level"] == "not_verified"
   and r6["risk_class"] == "undetermined" and r7["risk_class"] == "undetermined"
   and dv.evaluate(MOS2)["risk_class"] in ("undetermined", "higher_risk"))

# 4 missing or contradictory evidence blocks acceptance
def l3_missing(sid, evs):
    r = rc.lock_checklist(sid, evs)
    r["checklist"]["L3"] = "pending (needs a re-fetch on a later date)"
    return r
r8 = dv.evaluate(TERM, {"lock_checklist": l3_missing})
c4 = copy.deepcopy(claims)
c4["CLM-TERM-SULFIDE-EN-SENSE-001"]["contradiction_status"] = "unresolved"
r9 = dv.evaluate(TERM, {"claims": c4})
ok("04_missing_or_contradictory_evidence_blocks",
   r8["verification_level"] == "not_verified" and r9["verification_level"] == "not_verified"
   and dv.evaluate(MOS2)["verification_level"] == "not_verified")

# 5 nothing claims independent human review
page = open(os.path.join(ROOT, "main", "data", "release", "staged", "bisulfid-vs-bisulfide", "index.html"), encoding="utf-8").read()
ok("05_no_claim_of_independent_review",
   BASE["independently_human_reviewed"] is False and "not independent peer review" in BASE["label"]
   and "independently reviewed by" not in page and "not independent peer review" in page
   and "independent review not yet performed" in page)

# 6 owner authorization stays separate from evidence verification
claimed = {"governance_posture": "governed", "evidence_posture": "evidence_locked", "claim_posture": "claim_approved_narrow",
           "validation_posture": "validated", "information_gain_posture": "ig_reviewed_route_realization",
           "release_authorization": "authorized"}
dv.policy = adopted()
try:
    p, _ = rc.honoured_postures(TERM, claimed)
    derived = cc.derive(governance=p["governance_posture"], evidence=p["evidence_posture"], claim=p["claim_posture"],
                        validation=p["validation_posture"], ig=p["information_gain_posture"], release=p["release_authorization"])
    ok("06_documentary_path_never_grants_owner_acts",
       p["validation_posture"] == "validated" and p["evidence_posture"] == "evidence_locked"
       and (p["claim_posture"], p["release_authorization"], p["governance_posture"], p["information_gain_posture"])
       == ("claim_pending", "not_authorized", "reference_draft", "ig_reviewed_no_new_route")
       and derived == ("not_public", "noindex"))
    pm, _ = rc.honoured_postures(MOS2, claimed)
    ok("06b_documentary_path_refused_for_a_failing_ko",
       pm["validation_posture"] == "not_validated" and pm["evidence_posture"] == "evidence_sufficient")
finally:
    dv.policy = ORIG_POLICY

dv.policy = adopted(by="claude-code-agent")
try:
    ok("06c_an_agent_cannot_adopt_the_policy", dv.policy_adopted() is False and dv.documentary_ok(TERM)[0] is False)
finally:
    dv.policy = ORIG_POLICY

# 7 nothing previously blocked becomes publishable; 8 legacy URLs and directives unchanged
import publication_authority as pa  # noqa: E402
now = pa.Authority()
p_now, _ = rc.honoured_postures(TERM, claimed)
ok("07a_unadopted_policy_changes_nothing",
   dv.policy_adopted() is False and p_now["validation_posture"] == "not_validated"
   and p_now["evidence_posture"] == "evidence_sufficient")
dv.policy = adopted()
try:
    later = pa.Authority()
finally:
    dv.policy = ORIG_POLICY
ok("07b_no_reference_becomes_publishable_even_if_adopted",
   all(later.contract_c(x)[0] == now.contract_c(x)[0] == ("not_public", "noindex")
       for x in ("/molybdenum-disulfide/", "/bisulfid-vs-bisulfide/")))
ok("08_every_url_resolves_identically",
   all(now.resolve(x) == later.resolve(x) for x in now.baseline))

print("=" * 56)
print("RESULT: " + ("PASS — documentary pathway is proportionate and fail-closed" if not FAILS else f"FAIL — {FAILS}"))
sys.exit(1 if FAILS else 0)
