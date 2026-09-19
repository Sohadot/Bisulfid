"""
Pilot 01 (Morocco x Sulfur Trade) chain tests — 16 required proofs.
Pure; reads governance data + the real pilot evidence record; changes nothing; unwired from CI.
Exit 0 = pass, 1 = fail.
"""

import copy
import json
import os
import sys

from source_admissibility import (
    load_all, admissible, build_admission_unit,
    derive_evidence_posture_governed, trade_quant_classification_ok,
)
from relationship_grammar import load_registry, validate_instance
from contract_c_derive import derive

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
    print("=== Pilot 01 (Morocco x Sulfur Trade) tests ===")
    d = load_all()
    reg = load("sources", "source_registry.json")
    src = next(s for s in reg["sources"] if s["source_id"] == "SRC-OC-MA-TRADE")
    qreg = load("source_use_qualification_registry.json")
    qual = next(q for q in qreg["qualifications"] if q["qualification_id"] == "QUAL-OC-MA-TRADE-001")
    ev = load("evidence", "EVD-MA-SULFUR-IMPORT-2024.json")
    rels = load("relationship_class_registry.json")
    inst = next(i for i in rels["relationship_instances"] if i["relationship_instance_id"] == "REL-INST-MA-SULFUR-IMPORT-2024")
    pilot_claims = load("pilots", "PILOT_01_claims.json")

    # 1 new source identity has identity_revision
    ok("1_source_identity_revision", src.get("identity_revision") == "rev-2026-09-19-1")

    # 2 qualification references exactly that revision
    ok("2_qual_revision_match", qual.get("qualified_against_source_revision") == src.get("identity_revision"))

    # 3 source category is trade-admissible
    trade = d["domains"]["trade_economics"]
    ok("3_category_trade_admissible", src["category"] in trade["allowed_categories"])

    # Synthetic copy where the OC qualification is bumped to qualified_narrow, to test discrimination
    d2 = load_all()
    d2["qual_by_id"]["QUAL-OC-MA-TRADE-001"] = copy.deepcopy(d2["qual_by_id"]["QUAL-OC-MA-TRADE-001"])
    d2["qual_by_id"]["QUAL-OC-MA-TRADE-001"]["qualification_state"] = "qualified_narrow"
    base = {"source_id": "SRC-OC-MA-TRADE", "qualification_id": "QUAL-OC-MA-TRADE-001",
            "subject_domain": "SD-TRADE", "evidence_kind": "quantitative", "claim_level": "relationship",
            "evidence_role": "official_record", "intended_use": "official_import_value_measure_ma",
            "geography": "GEO-MA"}
    ok("3b_admits_when_qualified", admissible(base, d2)[0] is True, admissible(base, d2)[1])

    # 4 intended use explicitly allowlisted
    ok("4a_allowlisted_use_ok", admissible(base, d2)[0] is True)
    ok("4b_unlisted_use_denied", admissible({**base, "intended_use": "random_use"}, d2)[0] is False)

    # 5 trade/classification evidence cannot support unrelated industrial/economic claims
    ok("5a_industrial_use_denied", admissible({**base, "intended_use": "sulfur_industrial_demand"}, d2)[0] is False)
    ok("5b_chemistry_domain_denied", admissible({**base, "subject_domain": "SD-CHEMISTRY"}, d2)[0] is False)

    # 6 Morocco geography explicitly qualified, not inferred
    ok("6a_geo_ma_qualified", qual.get("geography_limitation") == ["GEO-MA"])
    ok("6b_other_geo_denied", admissible({**base, "geography": "GEO-CN"}, d2)[0] is False)

    # 7 period mandatory for the import relationship (not timeless)
    ts = inst.get("temporal_scope", {})
    ok("7_period_mandatory", ts.get("valid_from") == "2024-01-01" and ts.get("valid_to") == "2024-12-31")

    # 8 commodity classification/version mandatory for quantitative trade evidence (absent here -> not ok)
    ok("8_classification_mandatory_absent", trade_quant_classification_ok(ev) is False
       and ev["locator"]["classification_code"] is None)

    # 9 admission bridge computes admitted via admissible(), ignoring forged admitted=true
    forged = dict(ev); forged["admitted"] = True
    # inadmissible because the REAL qualification is 'reviewed'
    unit, reason = build_admission_unit(forged, "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma", d)
    ok("9_bridge_recomputes_admitted", unit["admitted"] is False, reason)

    # 10 forged admitted=true not accepted by production evaluation
    posture_forged = derive_evidence_posture_governed(
        [(forged, "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma")], "primary_plus_corroborating", d)
    ok("10_forged_admitted_ignored", posture_forged == "evidence_collecting")

    # 11 evidence posture is DERIVED (real committed state: qualification 'reviewed' -> not admitted)
    posture_real = derive_evidence_posture_governed(
        [(ev, "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma")], "primary_plus_corroborating", d)
    ok("11_posture_derived_collecting", posture_real == "evidence_collecting")
    ok("11b_real_qual_is_reviewed", qual["qualification_state"] == "reviewed")

    # 12 relationship direction GEO-MA -> imports -> sulfur (and reverse fails)
    ok("12a_direction_valid", validate_instance(inst, rels) == [])
    reversed_inst = {**inst, "subject_ref": "sulfur", "subject_type": "concept", "object_ref": "GEO-MA", "object_type": "geography"}
    ok("12b_reverse_rejected", validate_instance(reversed_inst, rels) != [])

    # 13 evidence cannot create a URL (no route/url/path fields on evidence or instance)
    url_fields = {"path", "route", "url", "route_id", "in_sitemap", "indexable"}
    ok("13_no_url_fields", not (url_fields & set(ev.keys())) and not (url_fields & set(inst.keys())))

    # 14 claims do not imply activation
    ok("14_claims_non_operational", pilot_claims.get("operational") is False)

    # 15 relationship does not imply publication (even if posture were higher, governance=planned blocks)
    ok("15_relationship_not_publication",
       derive(governance="planned", evidence="evidence_locked", claim="claim_pending",
              validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))

    # 16 Contract C final state computed from REAL pilot postures
    final = derive(governance="planned", evidence=posture_real, claim="claim_pending",
                   validation="not_validated", ig="ig_not_reviewed", release="not_authorized")
    ok("16_contract_c_final", final == ("not_public", "noindex"), f"{final}")

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all 16 Pilot 01 proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
