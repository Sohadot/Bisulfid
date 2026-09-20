"""
Pilot 01 Data Semantics Correction — 11 required proofs.
Pure; reads governance data; changes nothing; unwired from CI. Exit 0 pass / 1 fail.
"""

import json
import os
import sys

from numeric_normalization import normalize_fr_grouped, validate_evidence_numbers
from source_admissibility import derive_evidence_posture_governed, load_all
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
    print("=== Pilot 01 Data Semantics Correction tests ===")
    ev = load("evidence", "EVD-MA-SULFUR-IMPORT-2024.json")
    q = ev["quantitative"]
    prim = q["primary_measure"]
    anc = {a["scope"]: a for a in q["ancillary_scoped"]}

    # 1 total-import 2024 normalized = 9108
    ok("1_total_2024_9108", prim["series"]["2024"]["normalized_value"] == 9108 and prim["series"]["2024"]["source_literal"] == "9.108")
    # 2 total-import 2023 = 8007
    ok("2_total_2023_8007", prim["series"]["2023"]["normalized_value"] == 8007)
    # 3 ATPA 9102 cannot be treated as total (different scope, explicitly labelled)
    atpa = anc.get("customs_regime=ATPA_with_payment")
    ok("3_atpa_scoped_not_total", atpa is not None and atpa["series"]["2024"]["normalized_value"] == 9102
       and atpa["series"]["2024"]["normalized_value"] != prim["series"]["2024"]["normalized_value"])
    # 4 Asia 8737 cannot be treated as world-total
    asia = anc.get("origin=Asia")
    ok("4_asia_scoped_subset", asia is not None and asia["series"]["2024"]["normalized_value"] == 8737
       and asia["series"]["2024"]["normalized_value"] != prim["series"]["2024"]["normalized_value"])
    # 5 normalized 2024 avg price = 1099
    ok("5_price_2024_1099", q["average_unit_price"]["series"]["2024"]["normalized_value"] == 1099)
    # 6 source literal and normalized value remain distinct + consistent across the record
    nerrs = validate_evidence_numbers(ev)
    ok("6_literal_vs_normalized_consistent", nerrs == [], f"{nerrs}")
    # extra: normalization helper correctness
    ok("6b_helper", normalize_fr_grouped("9.108") == 9108 and normalize_fr_grouped("1.099") == 1099 and normalize_fr_grouped("18.768") == 18768)
    # 7 percentage +27.4 is NOT absolute tonnage
    ok("7_pct_not_tonnage", q["quantity"]["quantity_change_pct"] == 27.4)
    # 8 no absolute tonnage created
    ok("8_no_tonnage", q["quantity"]["absolute_quantity_tonnes"] is None)
    # 9 classification: Moroccan mapping remains blocked (HS side later proven in the classification sprint -> PARTIAL)
    pc = load("pilots", "PILOT_01_claims.json")
    a = next(c for c in pc["claims"] if c["claim_id"] == "CLM-MA-SULFUR-HS-CLASS")
    ok("9_moroccan_classification_blocked", a["outcome"] in ("BLOCKED", "PARTIAL") and ev["locator"]["classification_code"] is None)
    # 10 generic sulfur relationship remains evidence_collecting
    rels = load("relationship_class_registry.json")
    inst = next(i for i in rels["relationship_instances"] if i["relationship_instance_id"] == "REL-INST-MA-SULFUR-IMPORT-2024")
    ok("10a_relationship_collecting", inst["qualification_state"] == "evidence_collecting")
    d = load_all()
    posture = derive_evidence_posture_governed(
        [(ev, "QUAL-OC-MA-TRADE-001", "official_import_value_measure_ma")], "primary_plus_corroborating", d)
    ok("10b_derived_collecting", posture == "evidence_collecting")
    # 11 Contract C remains (not_public, noindex)
    final = derive(governance="planned", evidence=posture, claim="claim_pending",
                   validation="not_validated", ig="ig_not_reviewed", release="not_authorized")
    ok("11_contract_c_not_public", final == ("not_public", "noindex"), f"{final}")

    # guard: no "variant"/"within-source variance" framing left in pilot artifacts
    text = ""
    for f in ["pilots/MOROCCO_SULFUR_TRADE_PILOT_01.md", "pilots/PILOT_01_source_acquisition_dossier.md", "pilots/PILOT_01_claims.json"]:
        text += open(os.path.join(DATA, f), encoding="utf-8").read().lower()
    ok("12_no_variant_framing", "within-source variance" not in text and "variant 9.108" not in text and "variant of" not in text.replace("not a variant of", ""))

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all correction proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
