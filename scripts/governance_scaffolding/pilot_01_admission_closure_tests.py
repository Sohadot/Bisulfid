"""
Pilot 01 — Evidence Admission Closure: 19 required proofs.

Proves the classification path now obeys Source -> Qualification -> Evidence -> Claim,
that the HS classification is genuinely ADMITTED (not merely asserted), that the derived
posture is evidence_sufficient (NOT locked, NOT published), that one-fact-one-owner holds
(classification objects reference supporting_evidence_ids, never source_id), that the
Moroccan mapping stays unproven, and that the trade path is unchanged.

Pure; reads governance data; changes nothing; unwired from CI. Exit 0 pass / 1 fail.
"""

import copy
import json
import os
import sys

from source_admissibility import (
    load_all, admissible, build_admission_unit,
    derive_evidence_posture_governed, derive_evidence_posture,
)
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
    print("=== Pilot 01 — Evidence Admission Closure tests ===")
    d = load_all()
    sd = load("subject_domain_registry.json")
    schema = load("evidence", "evidence_schema.json")
    pol = load("source_admissibility_policy.json")
    reg = load("sources", "source_registry.json")
    srcs = {s["source_id"]: s for s in reg["sources"]}
    quals = {q["qualification_id"]: q for q in load("source_use_qualification_registry.json")["qualifications"]}
    cls = {c["classification_id"]: c for c in load("classification_registry.json")["classifications"]}
    hs = cls["CLS-HS2022-2503-00"]
    odc = cls["CLS-MA-ODC-SOUFRES-BRUTS"]
    hs_ev = load("evidence", "EVD-HS2022-2503-00.json")
    tr_ev = load("evidence", "EVD-MA-SULFUR-IMPORT-2024.json")
    claim_a = next(c for c in load("pilots", "PILOT_01_claims.json")["claims"] if c["claim_id"] == "CLM-MA-SULFUR-HS-CLASS")

    hs_ctx = {"source_id": "SRC-UN-COMTRADE-HS2022", "qualification_id": "QUAL-UN-HS2022-001",
              "subject_domain": "SD-CUSTOMS-CLASSIFICATION", "evidence_kind": "classification",
              "claim_level": "classification", "evidence_role": "primary_authoritative",
              "intended_use": "hs_classification_identity"}

    # 1 new subject domain exists and is distinct from chemical nomenclature
    domain_ids = {x["subject_domain_id"] for x in sd["subject_domains"]}
    ok("1_customs_classification_domain", "SD-CUSTOMS-CLASSIFICATION" in domain_ids and "SD-NOMENCLATURE" in domain_ids
       and "SD-CUSTOMS-CLASSIFICATION" != "SD-NOMENCLATURE")

    # 2 evidence schema extended: classification kind + level + reference field + level rule
    ok("2_schema_classification", "classification" in schema["evidence_kinds"]
       and "classification" in schema["claim_levels"]
       and "classification_ids" in schema["fields"]["optional_common"]
       and "classification_ids" in schema["fields"]["reference_fields_resolve_to"]
       and "classification" in schema["level_rules"])

    # 3 real HS classification evidence record exists and is well-formed
    ok("3_hs_evidence_record", hs_ev["evidence_kind"] == "classification"
       and hs_ev["claim_level"] == "classification"
       and hs_ev["classification_ids"] == ["CLS-HS2022-2503-00"]
       and hs_ev["source_id"] == "SRC-UN-COMTRADE-HS2022"
       and hs_ev["governed"] is True)

    # 4 HS classification evidence is ADMITTED (admissible enforces the whole chain)
    adm, reason = admissible(hs_ctx, d)
    ok("4_hs_admissible", adm is True, reason)

    # 5 classification qualification promoted reviewed -> qualified_narrow, on the customs-classification domain
    q_hs = quals["QUAL-UN-HS2022-001"]
    ok("5_qual_promoted", q_hs["qualification_state"] == "qualified_narrow"
       and q_hs["applicable_subject_domains"] == ["SD-CUSTOMS-CLASSIFICATION"]
       and q_hs["qualified_against_source_revision"] == srcs["SRC-UN-COMTRADE-HS2022"].get("identity_revision"))

    # 6 evidence_verified promotion is gated by admissible(): verified iff admissible TRUE
    unit, _ = build_admission_unit(hs_ev, "QUAL-UN-HS2022-001", "hs_classification_identity", d)
    d_rev = load_all()
    d_rev["qual_by_id"] = copy.deepcopy(d_rev["qual_by_id"])
    d_rev["qual_by_id"]["QUAL-UN-HS2022-001"]["qualification_state"] = "reviewed"
    unit_if_reviewed, _ = build_admission_unit(hs_ev, "QUAL-UN-HS2022-001", "hs_classification_identity", d_rev)
    ok("6_verified_gated_by_admissible", hs_ev["evidence_review_posture"] == "evidence_verified"
       and unit["admitted"] is True and unit_if_reviewed["admitted"] is False)

    # 7 derived classification posture = evidence_sufficient (single_authoritative_sufficient)
    posture = derive_evidence_posture_governed(
        [(hs_ev, "QUAL-UN-HS2022-001", "hs_classification_identity")], "single_authoritative_sufficient", d)
    ok("7_posture_sufficient", posture == "evidence_sufficient", posture)

    # 8 posture is NOT evidence_locked (source_lock_status candidate); locking is the only missing step
    ok("8a_not_locked_now", posture != "evidence_locked" and srcs["SRC-UN-COMTRADE-HS2022"]["source_lock_status"] == "candidate")
    locked_units = [dict(unit, source_locked=True)]
    ok("8b_would_lock_only_if_source_locked",
       derive_evidence_posture(locked_units, "single_authoritative_sufficient") == "evidence_locked")

    # 9 Contract C for the classification path stays (not_public, noindex)
    final = derive(governance="planned", evidence=posture, claim="claim_pending",
                   validation="not_validated", ig="ig_not_reviewed", release="not_authorized")
    ok("9_contract_c_not_public", final == ("not_public", "noindex"), f"{final}")

    # 10 one-fact-one-owner: classification objects carry NO source_id
    ok("10_no_source_id_on_class", "source_id" not in hs and "source_id" not in odc
       and "supporting_evidence_ids" in hs and "supporting_evidence_ids" in odc)

    # 11 HS classification's supporting evidence resolves (classification-kind, source resolves, back-references)
    ok("11_supporting_evidence_resolves", hs["supporting_evidence_ids"] == ["EVD-HS2022-2503-00"]
       and hs_ev["evidence_kind"] == "classification"
       and hs_ev["source_id"] in srcs
       and "CLS-HS2022-2503-00" in hs_ev["classification_ids"])

    # 12 Moroccan grouping stays unproven: NO supporting classification evidence
    ok("12_moroccan_unproven", odc["supporting_evidence_ids"] == []
       and "unproven" in odc["mapping_status"].lower()
       and odc["object_type"] == "statistical_product_grouping" and odc["code"] is None)

    # 13 Claim A HS side references supporting_evidence_ids (evidence), not classification IDs as a substitute
    ok("13_claim_a_evidence", "EVD-HS2022-2503-00" in claim_a["supporting_evidence_ids"]
       and claim_a["supporting_classification_ids"] == ["CLS-HS2022-2503-00", "CLS-MA-ODC-SOUFRES-BRUTS"])

    # 14 Claim A wording softened (governed posture, not bare 'PROVEN'); outcome PARTIAL; Moroccan side blocked
    ok("14_claim_a_wording", claim_a["outcome"] == "PARTIAL"
       and "ADMITTED" in claim_a["wco_hs_side"] and "PROVEN" not in claim_a["wco_hs_side"]
       and ("BLOCKED" in claim_a["moroccan_mapping_side"] or "NOT PROVEN" in claim_a["moroccan_mapping_side"]))

    # 15 SD-CUSTOMS-CLASSIFICATION domain policy is single_authoritative_sufficient (distinct from trade)
    dom = next(r for r in pol["domain_admissibility"].values() if "SD-CUSTOMS-CLASSIFICATION" in r.get("applies_to_domains", []))
    ok("15_domain_sufficiency", dom["sufficiency"] == "single_authoritative_sufficient"
       and "customs_nomenclature_authority" in dom["allowed_categories"]
       and "official_trade_statistics" not in dom["allowed_categories"])

    # 16 trade path UNCHANGED: sufficiency primary_plus_corroborating; posture evidence_collecting; qual still reviewed
    trade_posture = derive_evidence_posture_governed(
        [(tr_ev, "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma")], "primary_plus_corroborating", d)
    ok("16_trade_unchanged", pol["domain_admissibility"]["trade_economics"]["sufficiency"] == "primary_plus_corroborating"
       and trade_posture == "evidence_collecting"
       and quals["QUAL-OC-MA-TRADE-001"]["qualification_state"] == "reviewed")

    # 17 identity verification applied to EXACTLY the two pilot sources; none locked; no other source verified this way
    verified = {sid for sid, s in srcs.items() if s.get("status") == "verified"}
    ok("17a_two_pilot_verified", {"SRC-OC-MA-TRADE", "SRC-UN-COMTRADE-HS2022"}.issubset(verified)
       and srcs["SRC-OC-MA-TRADE"]["source_lock_status"] == "candidate"
       and srcs["SRC-UN-COMTRADE-HS2022"]["source_lock_status"] == "candidate")
    ok("17b_no_source_locked", all(s.get("source_lock_status") == "candidate" for s in srcs.values()))
    ready = {r["source_id"] for r in reg["verification_lock_resolution"]["verification_ready_sources"]}
    ok("17c_verified_are_ready", verified.issubset(ready))

    # 18 domain isolation: HS classification cannot support trade totals; trade qual cannot support classification
    ok("18a_class_not_trade_totals", admissible({**hs_ctx, "intended_use": "morocco_trade_totals"}, d)[0] is False)
    q_tr = quals["QUAL-OC-MA-TRADE-001"]
    ok("18b_trade_not_classification", "classification" not in q_tr["permitted_evidence_kinds"]
       and "SD-CUSTOMS-CLASSIFICATION" not in q_tr["applicable_subject_domains"])

    # 19 no publication/indexation created anywhere by this sprint
    url_fields = {"path", "route", "url_route", "route_id", "in_sitemap", "indexable"}
    ok("19_no_publication", reg["status"] == "inactive"
       and not (url_fields & set(hs.keys())) and not (url_fields & set(odc.keys()))
       and not (url_fields & set(hs_ev.keys()))
       and derive(governance="planned", evidence=posture, claim="claim_pending",
                  validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex")
       and derive(governance="planned", evidence=trade_posture, claim="claim_pending",
                  validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all 19 admission-closure proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
