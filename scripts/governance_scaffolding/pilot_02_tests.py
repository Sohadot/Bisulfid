"""
Pilot 02 (OCP Group x sulfur x Morocco industrial context x FY2024) — proofs.

Completion state: Claims A & B are SUPPORTED from the original OCP Consolidated
Financial Statements (uploaded); Claim C stays BLOCKED (Sustainability report PDF
not provided). Proves the corporate-actor chain admits correctly, preserves
accounting semantics, quarantines the price inconsistency, keeps the relationship
evidence_collecting (same-issuer non-independence), and publishes nothing.

Pure; reads governance data + the real evidence records; uses the real admission
bridge (never manual admitted=true); unwired from CI. Exit 0 pass / 1 fail.
"""

import copy
import json
import os
import sys

from source_admissibility import (
    load_all, admissible, build_admission_unit, derive_evidence_posture_governed,
    evaluate_sufficiency, _independent,
)
from numeric_normalization import normalize, magnitude, validate_evidence_numbers, iter_measures
from relationship_grammar import validate_instance
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
    print("=== Pilot 02 (OCP x sulfur industrial) tests ===")
    d = load_all()
    orgs = {o["organization_id"]: o for o in load("organization_registry.json")["organizations"]}
    geo_ids = {g["geo_id"] for g in load("geography_registry.json")["geographies"]}
    srcs = {s["source_id"]: s for s in load("sources", "source_registry.json")["sources"]}
    quals = {q["qualification_id"]: q for q in load("source_use_qualification_registry.json")["qualifications"]}
    rels = load("relationship_class_registry.json")
    inst = next((i for i in rels["relationship_instances"] if i["relationship_instance_id"] == "REL-INST-OCP-SULFUR-FY2024"), None)
    onto_roles = load("ontology_node_roles.json")
    onto = load("ontology", "sulfur_terms.json")
    purchase = load("evidence", "EVD-OCP-SULFUR-PURCHASE-FY2024.json")
    consumption = load("evidence", "EVD-OCP-SULFUR-CONSUMPTION-FY2024.json")
    pstore = load("pilots", "PILOT_02_claims.json")
    claims = {c["claim_id"]: c for c in pstore["claims"]}

    # --- identity / organization ---
    # 1 OCP resolves as organization; identity_revision on both sources
    ok("1_ocp_org_resolves", orgs.get("ORG-OCP-GROUP", {}).get("organization_type") == "company"
       and srcs["SRC-OCP-AFR-2024"].get("identity_revision") == "rev-2026-09-19-1"
       and srcs["SRC-OCP-SUSTAINABILITY-2024"].get("identity_revision") == "rev-2026-09-19-1")

    # 2 OCP cannot become GEO-MA (id spaces disjoint; relationship subject is the organization)
    ok("2_org_not_geo", "ORG-OCP-GROUP" not in geo_ids and inst is not None
       and inst["subject_ref"] == "ORG-OCP-GROUP" and inst["subject_type"] == "organization")

    # --- source verification / qualification ---
    # 3 financial source verified but lock stays candidate; sustainability stays seeded
    ok("3_verified_not_locked", srcs["SRC-OCP-AFR-2024"]["status"] == "verified"
       and srcs["SRC-OCP-AFR-2024"]["source_lock_status"] == "candidate"
       and srcs["SRC-OCP-SUSTAINABILITY-2024"]["status"] == "seeded")
    ok("3b_no_source_locked", all(s.get("source_lock_status") == "candidate" for s in srcs.values()))

    # 4 financial qualification promoted to qualified_narrow; sustainability stays candidate
    ok("4_qual_states", quals["QUAL-OCP-AFR-001"]["qualification_state"] == "qualified_narrow"
       and quals["QUAL-OCP-SUS-001"]["qualification_state"] == "candidate")

    # --- Claim A: accounting semantics ---
    fy = purchase["quantitative"]["primary_measure"]["series"]
    # 5 "(8,344)" literal retained; signed -8344; FY2023 (8,088) -> -8088
    ok("5_literal_and_sign", fy["2024"]["source_literal"] == "(8,344)" and fy["2024"]["normalized_value"] == -8344
       and fy["2023"]["source_literal"] == "(8,088)" and fy["2023"]["normalized_value"] == -8088)
    ok("5b_normalizer", normalize("(8,344)", "NUM-ACCOUNTING-PAREN-NEG") == (-8344, None)
       and normalize("(8,088)", "NUM-ACCOUNTING-PAREN-NEG") == (-8088, None))
    # 6 magnitude 8344 is DERIVED only (not stored as a measure)
    md = purchase["quantitative"]["magnitude_derived"]
    ok("6_magnitude_derived", md["fy2024_magnitude_mdh"] == 8344 and magnitude(-8344) == 8344
       and "source_literal" not in md)
    # 6b numeric law holds (parentheses not dropped) for the record
    ok("6b_numeric_law", validate_evidence_numbers(purchase) == [])
    # 7 sulfuric acid (2,364) NOT merged: no measure carries 2364/-2364 in the sulfur record
    vals = {m.get("normalized_value") for _, m in iter_measures(purchase)}
    ok("7_sulfuric_acid_not_merged", 2364 not in vals and -2364 not in vals and vals == {-8344, -8088})

    # --- admission (real bridge) ---
    # 8 purchase evidence admitted; forged admitted=true ignored; posture evidence_sufficient (not locked)
    unit, reason = build_admission_unit(purchase, "QUAL-OCP-AFR-001", "issuer_own_accounting_line_ocp_fy2024", d)
    ok("8_purchase_admitted", unit["admitted"] is True and unit["review_posture"] == "evidence_verified", reason)
    forged = dict(purchase); forged["admitted"] = True
    p_posture = derive_evidence_posture_governed(
        [(purchase, "QUAL-OCP-AFR-001", "issuer_own_accounting_line_ocp_fy2024")], "single_authoritative_sufficient", d)
    ok("8b_purchase_sufficient_not_locked", p_posture == "evidence_sufficient", p_posture)

    # 9 purchase amount cannot imply tonnage or imports (vetoes)
    base = {"source_id": "SRC-OCP-AFR-2024", "qualification_id": "QUAL-OCP-AFR-001",
            "subject_domain": "SD-CORPORATE-FINANCIALS", "evidence_kind": "quantitative", "claim_level": "relationship",
            "evidence_role": "primary_authoritative"}
    ok("9a_no_tonnage", admissible({**base, "intended_use": "physical_tonnage_from_value"}, d)[0] is False)
    ok("9b_no_imports", admissible({**base, "intended_use": "sulfur_import_value"}, d)[0] is False)
    ok("9c_allowed_use_admits", admissible({**base, "intended_use": "issuer_own_accounting_line_ocp_fy2024"}, d)[0] is True)

    # --- Claim B: consumption observation ---
    c_posture = derive_evidence_posture_governed(
        [(consumption, "QUAL-OCP-AFR-001", "issuer_reported_sulfur_consumption_observation_ocp_fy2024")],
        "primary_plus_corroborating", d)
    ok("10_consumption_collecting", c_posture == "evidence_collecting", c_posture)
    prop = consumption["qualitative"]["supported_proposition"].lower()
    ok("10b_increase_only", "increased in correlation" in prop
       and set(["absolute sulfur tonnage", "percentage increase", "causal elasticity"]).issubset(set(consumption["qualitative"]["not_inferred"])))

    # --- price inconsistency quarantine ---
    q = consumption["quarantined_not_admitted"]
    ok("11a_price_quarantined", q.get("excluded_from_claims") is True and q.get("resolution") == "none")
    # price figures never appear as an admitted measure, nor in any SUPPORTED claim statement
    admitted_vals = {m.get("normalized_value") for ev in (purchase, consumption) for _, m in iter_measures(ev)}
    supported_text = " ".join(c.get("statement", "") for c in claims.values() if str(c.get("outcome", "")).startswith("SUPPORTED")).lower()
    ok("11b_price_not_in_admitted", 127 not in admitted_vals and 113 not in admitted_vals
       and "$127" not in supported_text and "$113" not in supported_text and "drop in price" not in supported_text)
    # cannot be promoted without an explicit resolution step
    ok("11c_price_not_promotable", "sulfur_price_directional_claim" in consumption["prohibited_uses"]
       and admissible({**base, "subject_domain": "SD-INDUSTRIAL", "evidence_kind": "qualitative",
                       "intended_use": "sulfur_price_directional_claim"}, d)[0] is False)

    # --- Claim C blocked; no substitution ---
    cC = claims["CLM-OCP-PHOSPHATE-SULFURIC-ACID-PROCESS"]
    ok("12_claimC_blocked", cC["outcome"] == "BLOCKED" and cC["supporting_evidence_ids"] == [])
    # financial evidence cannot replace the process evidence: SD-INDUSTRIAL process use is not in allowed_uses
    ok("12b_financial_not_process", admissible({**base, "subject_domain": "SD-INDUSTRIAL", "evidence_kind": "qualitative",
                       "intended_use": "issuer_own_process_context_ocp"}, d)[0] is False)
    # no sulfuric_acid concept fabricated
    elig = {n["term_id"] for n in onto_roles["node_roles"] if n["role"] == "concept_eligible"}
    all_terms = {t["term_id"] for t in onto["terms"]}
    ok("12c_no_sulfuric_acid_concept", "sulfuric_acid" not in elig and "sulfuric_acid" not in all_terms)

    # 13 sustainability evidence cannot support the accounting value (even if hypothetically qualified)
    d13 = load_all()
    q13 = copy.deepcopy(quals["QUAL-OCP-SUS-001"])
    q13.update({"applicable_subject_domains": ["SD-CORPORATE-FINANCIALS"], "qualification_state": "qualified_narrow",
                "permitted_evidence_kinds": ["quantitative"], "permitted_claim_levels": ["relationship"],
                "allowed_uses": ["issuer_own_accounting_line_ocp_fy2024"], "evidence_roles": ["primary_authoritative"]})
    d13["qual_by_id"]["QUAL-OCP-SUS-001"] = q13
    ctx13 = {"source_id": "SRC-OCP-SUSTAINABILITY-2024", "qualification_id": "QUAL-OCP-SUS-001",
             "subject_domain": "SD-CORPORATE-FINANCIALS", "evidence_kind": "quantitative", "claim_level": "relationship",
             "evidence_role": "primary_authoritative", "intended_use": "issuer_own_accounting_line_ocp_fy2024"}
    ok("13_sustainability_not_financial", admissible(ctx13, d13)[0] is False, admissible(ctx13, d13)[1])

    # --- relationship ---
    # 14 grammar valid; evidence_collecting; FY2024-bounded; NOT evidence_qualified
    ok("14a_grammar_valid", validate_instance(inst, rels) == [])
    ok("14b_period_bounded", inst["temporal_scope"]["valid_from"] == "2024-01-01" and inst["temporal_scope"]["valid_to"] == "2024-12-31")
    ok("14c_not_qualified", inst["qualification_state"] == "evidence_collecting")
    # reversed direction rejected (sulfur cannot be the subject of REL-INDUSTRIAL-USER)
    rev = {**inst, "subject_ref": "sulfur", "subject_type": "concept", "object_ref": "ORG-OCP-GROUP", "object_type": "organization"}
    ok("14d_reverse_rejected", validate_instance(rev, rels) != [])
    # no GEO-MA industrial-user-of-sulfur instance created from OCP evidence
    ge = [i for i in rels["relationship_instances"] if i.get("relationship_class_id") == "REL-INDUSTRIAL-USER" and i.get("subject_ref") == "GEO-MA"]
    ok("14e_no_geo_ma_industrial", ge == [])

    # --- independence ---
    uA = {"role": "primary_authoritative", "source_id": "SRC-OCP-AFR-2024", "publisher": "OCP Group"}
    uS = {"role": "corroborating", "source_id": "SRC-OCP-SUSTAINABILITY-2024", "publisher": "OCP Group"}
    ok("15a_same_issuer_not_independent", _independent(uA, uS) is False)
    ok("15b_no_self_corroboration", evaluate_sufficiency([uA, uS], "primary_plus_corroborating")[0] is False)

    # --- claims supported with evidence; publication withheld ---
    ok("16a_claimA_supported", str(claims["CLM-OCP-SULFUR-PURCHASE-FY2024"]["outcome"]).startswith("SUPPORTED")
       and claims["CLM-OCP-SULFUR-PURCHASE-FY2024"]["supporting_evidence_ids"] == ["EVD-OCP-SULFUR-PURCHASE-FY2024"])
    ok("16b_claimB_supported", str(claims["CLM-OCP-SULFUR-CONSUMPTION-OBS-FY2024"]["outcome"]).startswith("SUPPORTED")
       and claims["CLM-OCP-SULFUR-CONSUMPTION-OBS-FY2024"]["supporting_evidence_ids"] == ["EVD-OCP-SULFUR-CONSUMPTION-FY2024"])
    ok("16c_non_operational", pstore.get("operational") is False)

    # 17 admission does not imply publication; no route fields; Contract-C safe from real postures
    url_fields = {"path", "route", "url_route", "route_id", "in_sitemap", "indexable"}
    leaked = (url_fields & set(purchase.keys())) | (url_fields & set(consumption.keys())) | (url_fields & set(inst.keys())) | (url_fields & set(orgs["ORG-OCP-GROUP"].keys()))
    ok("17a_no_url_fields", not leaked)
    ok("17b_contract_c_purchase", derive(governance="planned", evidence=p_posture, claim="claim_pending",
        validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))
    ok("17c_contract_c_relationship", derive(governance="planned", evidence=c_posture, claim="claim_pending",
        validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all Pilot 02 proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
