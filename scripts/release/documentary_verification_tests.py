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

# 1b D7 covers every author-controlled field (each inserted into a copy of the real spec; full evaluate())
SPEC = dv._spec_for(TERM)


def with_spec(mutate):
    sp = copy.deepcopy(SPEC)
    mutate(sp)
    return dv.evaluate(TERM, {"spec": sp})


def risky(r):
    return r["risk_class"] == "higher_risk" and r["verification_level"] == "not_verified"


ok("10_risk_in_summary_cannot_bypass_d7",
   risky(with_spec(lambda sp: sp.update(summary=sp["summary"] + " Handle with care: the occupational exposure limit is 1 ppm."))))
ok("11_risk_in_comparison_table_cannot_bypass_d7",
   risky(with_spec(lambda sp: sp["modules"][0].update(table={"columns": ["Term", "Note"], "evidence_ids": ["EVD-TERM-MW-BISULFIDE"],
                                                            "rows": [["bisulfide", "Wear protective equipment when handling it"]]}))))
ok("12_risk_in_concluding_sections_cannot_bypass_d7",
   risky(with_spec(lambda sp: sp["synthesis"]["groups"][0]["items"].append(
       {"text": "A dose of 5 mg is tolerated.", "evidence_ids": ["EVD-TERM-MW-BISULFIDE"]})))
   and risky(with_spec(lambda sp: sp["not_established"].update(
       text=sp["not_established"]["text"] + " Store below 25 °C and avoid exposure; toxicity is outside this reference."))))
ok("13_risk_only_in_seo_or_structured_data_cannot_bypass_d7",
   risky(with_spec(lambda sp: sp["seo"].update(description="Bisulfide toxicity, safe exposure limits and dosage explained by IUPAC sources.")))
   and risky(with_spec(lambda sp: sp["seo"]["json_ld"]["hasDefinedTerm"][0].update(description="Lethal above the exposure limit.")))
   and risky(with_spec(lambda sp: sp["seo"].update(title="Bisulfid vs Bisulfide: Handling, Toxicity and Exposure"))))
ok("14_ordinary_terminology_stays_eligible",
   with_spec(lambda sp: sp["synthesis"]["groups"][0]["items"].append(
       {"text": "Sulfide and Sulfid both name salts of hydrogen sulfide in the sources cited.",
        "evidence_ids": ["EVD-TERM-MW-SULFIDE", "EVD-TERM-DWDS-SULFID"]}))["verification_level"] == "documentary_verified")
r15 = with_spec(lambda sp: sp["not_established"].update(
    text=sp["not_established"]["text"] + " Toxicity, exposure limits and handling are outside this reference."))
ok("15_exclusion_statements_are_not_treated_as_advice",
   r15["risk_class"] == "low_risk_informational" and r15["verification_level"] == "documentary_verified")
r16a = with_spec(lambda sp: sp.update(summary=""))
r16b = with_spec(lambda sp: sp["not_established"].update(text=""))
r16c = with_spec(lambda sp: sp["seo"].update(description=""))
ok("16_missing_content_is_never_approved_as_low_risk",
   all(r["risk_class"] == "undetermined" and r["verification_level"] == "not_verified" for r in (r16a, r16b, r16c)))
ok("17_evidence_validation_unchanged",
   all(BASE["checks"][k] == "pass" for k in ("D1_claims", "D2_evidence", "D3_scope", "D4_reproducible", "D5_conflicts", "D6_quality"))
   and BASE["sources_assessed"] == 11 and BASE["claims_assessed"] == 11 and BASE["ig_valid_units"] >= 3)

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

# 7 Owner adoption enables documentary evidence acceptance, not release authority.
import publication_authority as pa  # noqa: E402
now = pa.Authority()
p_now, _ = rc.honoured_postures(TERM, claimed)
ok("07a_adoption_enables_only_documentary_acceptance",
   dv.policy_adopted() is True
   and p_now["validation_posture"] == "validated"
   and p_now["evidence_posture"] == "evidence_locked"
   and p_now["claim_posture"] == "claim_pending"
   and p_now["release_authorization"] == "not_authorized"
   and p_now["information_gain_posture"] == "ig_reviewed_no_new_route")
# Simulate the previous, unadopted policy without changing the actual owner decision.
dv.policy = lambda: dict(ORIG_POLICY(), status="proposed_for_owner_adoption", adopted_by=None, adopted_on=None)
try:
    prior = pa.Authority()
    p_prior, _ = rc.honoured_postures(TERM, claimed)
finally:
    dv.policy = ORIG_POLICY
ok("07b_without_adoption_the_documentary_path_remains_closed",
   p_prior["validation_posture"] == "not_validated"
   and p_prior["evidence_posture"] == "evidence_sufficient")
ok("07c_adoption_does_not_publish_any_reference",
   all(prior.contract_c(x)[0] == now.contract_c(x)[0] == ("not_public", "noindex")
       for x in ("/molybdenum-disulfide/", "/bisulfid-vs-bisulfide/")))
# Internal diagnostic notes legitimately differ between an adopted and a simulated
# unadopted documentary policy. The outward route, robots, canonical, sitemap
# and redirect must remain identical for every sealed legacy URL.
PUBLIC_DIRECTIVE_FIELDS = ("render", "robots", "canonical", "sitemap", "redirect_to")
ok("08_every_legacy_url_has_identical_public_directives",
   all(all(now.resolve(x)[k] == prior.resolve(x)[k] for k in PUBLIC_DIRECTIVE_FIELDS)
       for x in now.baseline))

# 9 Accepted documentary evidence must be represented consistently without authorizing release.
actual_pc = dv._pc_for(TERM)
actual_postures, _ = rc.honoured_postures(TERM, actual_pc["postures"])
manifest = json.load(open(os.path.join(ROOT, "main", "data", "release", "staged",
                                      "bisulfid-vs-bisulfide", "release.json"), encoding="utf-8"))
ok("18_candidate_and_manifest_use_accepted_documentary_postures",
   actual_postures["validation_posture"] == "validated"
   and actual_postures["evidence_posture"] == "evidence_locked"
   and manifest["postures_honoured"] == actual_postures
   and manifest["contract_c_honoured"] == ["not_public", "noindex"]
   and actual_postures["claim_posture"] == "claim_pending"
   and actual_postures["release_authorization"] == "not_authorized")
ok("19_source_lock_reporting_does_not_imitate_human_signatures",
   "11 of 11 sources accepted documentarily via L1–L5 (0 independently signed source locks)" in page
   and not rc.validation_ok(TERM)[0])

print("=" * 56)
print("RESULT: " + ("PASS — documentary pathway is proportionate and fail-closed" if not FAILS else f"FAIL — {FAILS}"))
sys.exit(1 if FAILS else 0)
