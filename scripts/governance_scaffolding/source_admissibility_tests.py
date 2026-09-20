"""
Admission enforcement closure tests (21 required proofs).
Pure; reads governance data, changes nothing, unwired from CI.
Exit 0 = pass, 1 = fail.
"""

import json
import os
import sys

from source_admissibility import admissible, load_all, evaluate_sufficiency, derive_evidence_posture

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
FAIL = []


def load(*p):
    with open(os.path.join(DATA, *p), encoding="utf-8") as fh:
        return json.load(fh)


def ok(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAIL.append(name)


def main():
    print("=== Admission enforcement closure tests ===")
    d = load_all()

    # Fully-specified admissible MoS2 context (matches QUAL-SPEKTRUM-MOS2-DE-001).
    base = {
        "source_id": "SRC-SPEKTRUM-MOS2-DE", "qualification_id": "QUAL-SPEKTRUM-MOS2-DE-001",
        "subject_domain": "SD-TERMINOLOGY", "evidence_kind": "terminological", "claim_level": "lexeme",
        "evidence_role": "primary_authoritative",
        "intended_use": "cautious_terminology_framing_de_dictionary_entry",
    }
    ok("00_baseline_admissible", admissible(base, d)[0] is True, admissible(base, d)[1])

    # 1 unspecified intended use cannot pass a narrow qualification
    ok("1_unspecified_use_denied", admissible({**base, "intended_use": None}, d)[0] is False)

    # 2 use not in allowed_uses denied even if not in prohibited_uses
    ok("2_unlisted_use_denied", admissible({**base, "intended_use": "some_other_lexical_use"}, d)[0] is False)

    # 3 prohibited use vetoes
    ok("3_prohibited_vetoes", admissible({**base, "intended_use": "route_publication"}, d)[0] is False)

    # 4 category not in domain allowed_categories denied even with compatible generic role.
    #    Simulate: a source whose category is official_customs_data qualified for terminology.
    d2 = load_all()
    d2["category_by_source"]["SRC-SPEKTRUM-MOS2-DE"] = "official_customs_data"
    d2["category_roles"]["official_customs_data"] = ["primary_authoritative", "official_record"]
    ok("4_category_not_in_allowed_denied", admissible(base, d2)[0] is False)

    # 5 evidence role must be declared and permitted
    ok("5a_role_required", admissible({**base, "evidence_role": None}, d)[0] is False)
    ok("5b_role_must_be_permitted", admissible({**base, "evidence_role": "official_record"}, d)[0] is False)

    # 6 geography limitation enforced (qualification grants no geography)
    ok("6_geography_enforced", admissible({**base, "geography": "GEO-DE"}, d)[0] is False)

    # 7 language never creates geography qualification (de lexeme != Germany)
    q = d["qual_by_id"]["QUAL-SPEKTRUM-MOS2-DE-001"]
    ok("7_language_not_geography", q.get("geography_limitation") in (None, [],) and admissible({**base, "geography": "GEO-DE"}, d)[0] is False)

    # 8 jurisdiction limitation enforced
    ok("8_jurisdiction_enforced", admissible({**base, "jurisdiction": "JUR-DE"}, d)[0] is False)

    # 9 temporal boundary enforced (simulate a bounded qualification)
    d3 = load_all()
    q3 = dict(d3["qual_by_id"]["QUAL-SPEKTRUM-MOS2-DE-001"]); q3["temporal_boundary"] = {"valid_from": "2020-01-01", "valid_to": "2021-12-31"}
    d3["qual_by_id"]["QUAL-SPEKTRUM-MOS2-DE-001"] = q3
    ok("9a_temporal_out_of_range", admissible({**base, "temporal_scope": {"as_of": "2026-01-01"}}, d3)[0] is False)
    ok("9b_temporal_current_needs_historical", admissible({**base, "claims_current": True}, d3)[0] is False)

    # 10 source-version mismatch forces review/denial
    d4 = load_all()
    d4["revision_by_source"]["SRC-SPEKTRUM-MOS2-DE"] = "rev-DIFFERENT"
    ok("10_revision_mismatch_denied", admissible(base, d4)[0] is False)

    # 11 category alone insufficient
    ok("11_category_alone_insufficient", admissible({**base, "qualification_id": None}, d)[0] is False)

    # 12 qualification suspension regresses evidence posture (cannot be locked)
    susp_units = [{"admitted": True, "review_posture": "evidence_verified", "qualification_state": "suspended",
                   "source_locked": True, "role": "primary_authoritative", "source_id": "SRC-SPEKTRUM-MOS2-DE"}]
    ok("12_suspension_regresses", derive_evidence_posture(susp_units, "single_authoritative_sufficient") == "evidence_collecting")

    # 13 evidence_verified alone (source not locked) does not create evidence_locked
    v_unlocked = [{"admitted": True, "review_posture": "evidence_verified", "qualification_state": "qualified_narrow",
                   "source_locked": False, "role": "primary_authoritative", "source_id": "S1"}]
    ok("13_verified_not_locked_without_lock", derive_evidence_posture(v_unlocked, "single_authoritative_sufficient") == "evidence_sufficient")

    # 14 source locked without valid qualification does not create evidence_locked
    locked_noqual = [{"admitted": False, "review_posture": "evidence_verified", "qualification_state": "candidate",
                      "source_locked": True, "role": "primary_authoritative", "source_id": "S1"}]
    ok("14_locked_without_qual_not_locked", derive_evidence_posture(locked_noqual, "single_authoritative_sufficient") == "evidence_collecting")

    # 15 valid qualification without verification does not create evidence_locked
    qual_unverified = [{"admitted": True, "review_posture": "scope_reviewed", "qualification_state": "qualified_narrow",
                        "source_locked": True, "role": "primary_authoritative", "source_id": "S1"}]
    ok("15_qual_without_verify_not_locked", derive_evidence_posture(qual_unverified, "single_authoritative_sufficient") == "evidence_sufficient")

    # 16 single_authoritative_sufficient works
    ok("16_single_authoritative", evaluate_sufficiency([{"role": "primary_authoritative", "source_id": "S1"}], "single_authoritative_sufficient")[0] is True)

    # 17 primary_plus_corroborating requires genuinely separate support
    two_diff = [{"role": "official_record", "source_id": "A"}, {"role": "corroborating", "source_id": "B"}]
    ok("17_primary_plus_corroborating", evaluate_sufficiency(two_diff, "primary_plus_corroborating")[0] is True)

    # 18 same source cannot corroborate itself
    two_same = [{"role": "official_record", "source_id": "A"}, {"role": "corroborating", "source_id": "A"}]
    ok("18_no_self_corroboration", evaluate_sufficiency(two_same, "primary_plus_corroborating")[0] is False)

    # 19 original-instrument pattern requires instrument evidence
    ok("19a_instrument_required_absent", evaluate_sufficiency([{"role": "official_record", "source_id": "A", "category": "regulatory_body"}], "original_instrument_required")[0] is False)
    ok("19b_instrument_present", evaluate_sufficiency([{"role": "official_record", "source_id": "A", "category": "regulatory_instrument"}], "original_instrument_required")[0] is True)

    # 20 unresolved multi-source threshold cannot silently pass
    r20 = evaluate_sufficiency([{"role": "primary_scientific", "source_id": "A"}, {"role": "primary_scientific", "source_id": "B"}], "multi_source_synthesis")
    ok("20_multi_source_blocked", r20[0] is False and "governance_threshold_required" in r20[1])

    # 21 MoS2 remains not_public/noindex, with GOVERNED evidence posture feeding Contract C
    sys.path.insert(0, os.path.dirname(__file__))
    from contract_c_derive import derive
    mos2_units = [{"admitted": True, "review_posture": "scope_reviewed", "qualification_state": "qualified_narrow",
                   "source_locked": False, "role": "primary_authoritative", "source_id": "SRC-SPEKTRUM-MOS2-DE"}]
    ep = derive_evidence_posture(mos2_units, "single_authoritative_sufficient")
    state = derive(governance="planned", evidence=ep, claim="claim_pending",
                   validation="not_validated", ig="ig_not_reviewed", release="not_authorized")
    ok("21_mos2_not_public", ep == "evidence_sufficient" and state == ("not_public", "noindex"), f"ep={ep} state={state}")

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all 21 enforcement proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
