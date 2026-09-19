"""
Pilot 01 Classification Resolution + source-specific normalization — 17 proofs.
Pure; reads governance data; changes nothing; unwired from CI. Exit 0 pass / 1 fail.
"""

import json
import os
import sys

from numeric_normalization import normalize, validate_evidence_numbers
from contract_c_derive import derive
from source_admissibility import derive_evidence_posture_governed, load_all

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
    print("=== Pilot 01 Classification Resolution tests ===")
    reg = load("sources", "source_registry.json")
    srcs = {s["source_id"]: s for s in reg["sources"]}
    quals = {q["qualification_id"]: q for q in load("source_use_qualification_registry.json")["qualifications"]}
    cls = {c["classification_id"]: c for c in load("classification_registry.json")["classifications"]}
    hs = cls["CLS-HS2022-2503-00"]
    odc = cls["CLS-MA-ODC-SOUFRES-BRUTS"]
    ev = load("evidence", "EVD-MA-SULFUR-IMPORT-2024.json")
    hs_ev = load("evidence", "EVD-HS2022-2503-00.json")
    rels = load("relationship_class_registry.json")
    inst = next(i for i in rels["relationship_instances"] if i["relationship_instance_id"] == "REL-INST-MA-SULFUR-IMPORT-2024")
    pol = load("source_admissibility_policy.json")
    pc = {c["claim_id"]: c for c in load("pilots", "PILOT_01_claims.json")["claims"]}

    # 1 normalizer uses declared source-specific convention
    ok("1_convention_specific", normalize("9.108", "NUM-FR-DOT-THOUSANDS") == (9108, None)
       and normalize("1.099", "NUM-EN-DOT-DECIMAL") == (1.099, None))
    # 2 evidence without a required numeric convention fails
    ok("2_missing_convention_fails",
       validate_evidence_numbers({"quantitative": {"m": {"source_literal": "9.108", "normalized_value": 9108}}}) != [])
    # 3 English decimal-dot fixture NOT normalized with Morocco convention
    en_ok = {"quantitative": {"numeric_convention_id": "NUM-EN-DOT-DECIMAL", "m": {"source_literal": "1.099", "normalized_value": 1.099}}}
    en_bad = {"quantitative": {"numeric_convention_id": "NUM-EN-DOT-DECIMAL", "m": {"source_literal": "1.099", "normalized_value": 1099}}}
    ok("3_en_not_fr", validate_evidence_numbers(en_ok) == [] and validate_evidence_numbers(en_bad) != [])
    # 4 WCO/classification source has identity_revision
    ok("4_class_source_revision", srcs["SRC-UN-COMTRADE-HS2022"].get("identity_revision") == "rev-2026-09-19-1")
    # 5 WCO evidence states classification version
    ok("5_version_stated", hs["classification_version"] == "HS 2022 (H6)")
    # 6 heading/subheading/code level explicit
    ok("6_levels_explicit", hs["heading"] == "25.03" and hs["code"] == "2503.00" and hs["hs6"] == "2503.00")
    # 7 exclusions preserved
    ok("7_exclusions", set(hs["exclusions"]) == {"sublimed sulphur", "precipitated sulphur", "colloidal sulphur"}
       and hs["excluded_forms_go_to"]["code"] == "2802.00")
    # 8 WCO classification qualification cannot support Morocco trade-value claims
    q_hs = quals["QUAL-UN-HS2022-001"]
    ok("8_wco_not_trade", "morocco_trade_totals" in q_hs["prohibited_uses"] and "trade_flow_value" in q_hs["prohibited_uses"]
       and "SD-TRADE" not in q_hs["applicable_subject_domains"])
    # 9 Moroccan trade source cannot independently establish WCO classification;
    #   HS classification source binding lives on the evidence record (one-fact-one-owner)
    q_tr = quals["QUAL-OC-MA-TRADE-001"]
    ok("9_trade_not_classification", "hs_classification_identity" not in q_tr["allowed_uses"]
       and "classification" not in q_tr["permitted_evidence_kinds"]
       and "source_id" not in hs
       and hs["supporting_evidence_ids"] == ["EVD-HS2022-2503-00"]
       and hs_ev["source_id"] == "SRC-UN-COMTRADE-HS2022")
    # 10 national code and HS6 never silently conflated
    ok("10_no_code_conflation", hs["hs6"] == "2503.00" and hs["national_code"] is None and odc["hs6"] is None and odc["national_code"] is None)
    # 11 statistical product grouping vs HS commodity distinguishable
    ok("11_grouping_vs_commodity", odc["object_type"] == "statistical_product_grouping" and odc["code"] is None
       and hs["object_type"] == "hs_subheading")
    # 12 Claim A promoted only to level established via the governed admission path (PARTIAL);
    #    HS side wording softened from bare 'PROVEN' to the governed posture (ADMITTED)
    ok("12_claim_a_partial", pc["CLM-MA-SULFUR-HS-CLASS"]["outcome"] == "PARTIAL"
       and "ADMITTED" in pc["CLM-MA-SULFUR-HS-CLASS"]["wco_hs_side"]
       and "EVD-HS2022-2503-00" in pc["CLM-MA-SULFUR-HS-CLASS"]["supporting_evidence_ids"]
       and ("BLOCKED" in pc["CLM-MA-SULFUR-HS-CLASS"]["moroccan_mapping_side"] or "NOT PROVEN" in pc["CLM-MA-SULFUR-HS-CLASS"]["moroccan_mapping_side"]))
    # 13 relationship remains period-bounded
    ts = inst["temporal_scope"]
    ok("13_period_bounded", ts.get("valid_from") == "2024-01-01" and ts.get("valid_to") == "2024-12-31")
    # 14 generic sulfur relationship not upgraded (mapping unproven)
    ok("14_relationship_not_upgraded", inst["qualification_state"] == "evidence_collecting"
       and "unproven" in odc["mapping_status"].lower())
    # 15 trade sufficiency policy unchanged
    ok("15_sufficiency_unchanged", pol["domain_admissibility"]["trade_economics"]["sufficiency"] == "primary_plus_corroborating")
    # 16 no public URL created (no route/url fields in new artifacts)
    url_fields = {"path", "route", "route_id", "in_sitemap", "indexable"}
    ok("16_no_url", not (url_fields & set(hs.keys())) and not (url_fields & set(odc.keys())) and not (url_fields & set(ev.keys())))
    # 17 Contract C computed from real postures
    d = load_all()
    posture = derive_evidence_posture_governed(
        [(ev, "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma")], "primary_plus_corroborating", d)
    final = derive(governance="planned", evidence=posture, claim="claim_pending",
                   validation="not_validated", ig="ig_not_reviewed", release="not_authorized")
    ok("17_contract_c", posture == "evidence_collecting" and final == ("not_public", "noindex"), f"{posture} {final}")

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all 17 classification-resolution proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
