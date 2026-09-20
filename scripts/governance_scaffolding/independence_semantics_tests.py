"""
Pre-production independence-semantics hardening — required proofs (§5).

Independence is DOMAIN-SEMANTIC, not URL/publisher-semantic:
  science  -> originating-work / data lineage
  corporate-> issuer lineage
  trade    -> dataset/release lineage
  same source -> never independent
Journal/publisher equality is NOT a universal independence key.

Pure; reads governance data; uses the real admission bridge; unwired from CI.
Exit 0 pass / 1 fail.
"""

import os
import json
import sys

from source_admissibility import (
    load_all, build_admission_unit, derive_evidence_posture_governed, _independent,
)
from contract_c_derive import derive

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
FAIL = []


def ev(name):
    with open(os.path.join(DATA, "evidence", name + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def ok(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAIL.append(name)


def contract_safe(posture):
    return derive(governance="planned", evidence=posture, claim="claim_pending",
                  validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex")


def main():
    print("=== Independence semantics hardening tests ===")
    d = load_all()

    def unit(evname, qid, use):
        return build_admission_unit(ev(evname), qid, use, d)[0]

    # real units
    codD = unit("EVD-MOS2-STRUCTURE-DICKINSON", "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h")
    codA = unit("EVD-MOS2-STRUCTURE-ACTACRYST", "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h")
    jacs = unit("EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT", "QUAL-JACS-MOLYBDENITE-1923-EXCERPT-001", "molybdenite_mos2_hexagonal_identity")
    huang = unit("EVD-MOS2-LAYERED-HUANG1981", "QUAL-HUANG-THESIS-1981-001", "layered_structure_mos2")
    ocpA = unit("EVD-OCP-SULFUR-PURCHASE-FY2024", "QUAL-OCP-AFR-001", "issuer_own_accounting_line_ocp_fy2024")
    ocpS = unit("EVD-OCP-PHOSPHATE-PROCESS-2024", "QUAL-OCP-SUS-001", "issuer_own_process_context_ocp")

    # 1 same source_id => not independent
    ok("1_same_source_not_independent", _independent({"source_id": "S1"}, {"source_id": "S1"}) is False
       and _independent(codD, dict(codD)) is False)

    # 2 same originating_work_id through two artifacts => not independent (COD copy + article excerpt)
    ok("2_same_work_not_independent", codD["originating_work_id"] == jacs["originating_work_id"]
       and _independent(codD, jacs) is False)

    # 3 related scientific works => conservatively not independent (Huang 1981 <-> Schonfeld 1983)
    ok("3_related_works_not_independent", _independent(codA, huang) is False)

    # 4 two DISTINCT scientific works from the SAME journal/publisher CAN be independent
    x = {"source_id": "SX", "originating_work_id": "WORK-A", "publisher": "Journal Z"}
    y = {"source_id": "SY", "originating_work_id": "WORK-B", "publisher": "Journal Z"}
    ok("4_same_journal_distinct_works_independent", _independent(x, y) is True
       and _independent(codD, codA) is True)  # 1923 vs 1983 = distinct works

    # 5 two OCP reports, different source_ids, issuer_id=ORG-OCP-GROUP => NOT independent
    ok("5_same_issuer_not_independent", ocpA["source_id"] != ocpS["source_id"]
       and ocpA["issuer_id"] == "ORG-OCP-GROUP" and ocpS["issuer_id"] == "ORG-OCP-GROUP"
       and _independent(ocpA, ocpS) is False)

    # 6 two UNRELATED corporate issuers are not collapsed merely by matching category
    a = {"source_id": "S1", "issuer_id": "ORG-A", "category": "corporate_financial_report"}
    b = {"source_id": "S2", "issuer_id": "ORG-B", "category": "corporate_financial_report"}
    ok("6_distinct_issuers_independent", _independent(a, b) is True)

    # 7 same governed dataset_id => not independent
    ok("7_same_dataset_not_independent",
       _independent({"source_id": "S1", "dataset_id": "DS-1"}, {"source_id": "S2", "dataset_id": "DS-1"}) is False)

    # 8 different URLs alone never establish independence (url is not a key)
    ok("8_url_not_a_key",
       _independent({"source_id": "S1", "issuer_id": "ORG-A", "url": "http://a"},
                    {"source_id": "S2", "issuer_id": "ORG-A", "url": "http://b"}) is False
       and _independent({"source_id": "S1", "originating_work_id": "W", "url": "http://a"},
                        {"source_id": "S2", "originating_work_id": "W", "url": "http://b"}) is False)

    # 9 Pilot 02 relationship remains evidence_collecting
    p2 = derive_evidence_posture_governed(
        [(ev("EVD-OCP-SULFUR-PURCHASE-FY2024"), "QUAL-OCP-AFR-001", "issuer_own_accounting_line_ocp_fy2024"),
         (ev("EVD-OCP-SULFUR-CONSUMPTION-FY2024"), "QUAL-OCP-AFR-001", "issuer_reported_sulfur_consumption_observation_ocp_fy2024")],
        "primary_plus_corroborating", d)
    ok("9_pilot02_collecting", p2 == "evidence_collecting", p2)

    # 10 Pilot 03 A/B/C postures unchanged
    A = derive_evidence_posture_governed(
        [(ev("EVD-MOS2-FORMULA-PUBCHEM"), "QUAL-PUBCHEM-MOS2-001", "chemical_formula_identity"),
         (ev("EVD-MOS2-FORMULA-NIST"), "QUAL-NIST-MOS2-001", "chemical_formula_identity")], "primary_plus_corroborating", d)
    B = derive_evidence_posture_governed(
        [(ev("EVD-MOS2-STRUCTURE-DICKINSON"), "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h"),
         (ev("EVD-MOS2-STRUCTURE-ACTACRYST"), "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h")], "primary_plus_corroborating", d)
    C = derive_evidence_posture_governed(
        [(ev("EVD-MOS2-LATTICE-A-DICKINSON"), "QUAL-COD-MOS2-DICKINSON-001", "lattice_parameter_2h"),
         (ev("EVD-MOS2-LATTICE-A-ACTACRYST"), "QUAL-COD-MOS2-ACTACRYST-001", "lattice_parameter_2h")], "primary_plus_corroborating", d)
    ok("10_pilot03_unchanged", A == "evidence_sufficient" and B == "evidence_sufficient" and C == "evidence_sufficient",
       f"A={A} B={B} C={C}")

    # 11 Pilot 01 unchanged (trade qualification still 'reviewed' -> not admitted -> collecting)
    p1 = derive_evidence_posture_governed(
        [(ev("EVD-MA-SULFUR-IMPORT-2024"), "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma")],
        "primary_plus_corroborating", d)
    ok("11_pilot01_unchanged", p1 == "evidence_collecting", p1)

    # 12 Contract C safe everywhere
    ok("12_contract_c_safe", all(contract_safe(p) for p in (p2, A, B, C, p1)))

    # 13 admission-unit carries governed independence metadata (not publisher)
    ok("13_unit_metadata", set(["independence_domain", "originating_work_id", "issuer_id", "dataset_id", "related_work_ids"]).issubset(codD.keys())
       and codD["independence_domain"] == "science" and ocpA["independence_domain"] == "corporate"
       and "publisher" not in codD)

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all independence-semantics proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
