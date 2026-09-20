"""
Pilot 03 (MoS2 scientific reference chain) — required proofs (§19).

Concept-level scientific evidence for molybdenum_disulfide, established independently
from the German lexical chain. Claim A (formula) + B (2H structure) + C (2H lattice
parameter a) are supported from authoritative databases / primary crystallographic
literature. Proves lexical<->scientific separation, polytype/form scope, numeric
normalization, coexisting values, use-scoped qualification, and that nothing publishes.

Pure; reads governance data + the real evidence records; uses the real admission
bridge; unwired from CI. Exit 0 pass / 1 fail.
"""

import os
import json
import sys

from source_admissibility import load_all, admissible, build_admission_unit, derive_evidence_posture_governed
from numeric_normalization import normalize, validate_evidence_numbers, iter_measures
from contract_c_derive import derive

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
FAIL = []


def load(*p):
    with open(os.path.join(DATA, *p), encoding="utf-8") as fh:
        return json.load(fh)


def ev(name):
    return load("evidence", name + ".json")


def ok(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAIL.append(name)


def main():
    print("=== Pilot 03 (MoS2 scientific reference) tests ===")
    d = load_all()
    srcs = {s["source_id"]: s for s in load("sources", "source_registry.json")["sources"]}
    quals = {q["qualification_id"]: q for q in load("source_use_qualification_registry.json")["qualifications"]}
    roles = load("ontology_node_roles.json")
    elig = {n["term_id"] for n in roles["node_roles"] if n["role"] == "concept_eligible"}
    p3 = load("pilots", "PILOT_03_claims.json")
    claims = {c["claim_id"]: c for c in p3["claims"]}
    pubchem = ev("EVD-MOS2-FORMULA-PUBCHEM"); nist = ev("EVD-MOS2-FORMULA-NIST")
    struct1 = ev("EVD-MOS2-STRUCTURE-DICKINSON"); struct2 = ev("EVD-MOS2-STRUCTURE-ACTACRYST")
    latt1 = ev("EVD-MOS2-LATTICE-A-DICKINSON"); latt2 = ev("EVD-MOS2-LATTICE-A-ACTACRYST")
    all_ev = [pubchem, nist, struct1, struct2, latt1, latt2]

    # 1 Spektrum LEXICAL evidence cannot support scientific Claim A/B/C
    def spektrum_ctx(sd, use):
        return {"source_id": "SRC-SPEKTRUM-MOS2-DE", "qualification_id": "QUAL-SPEKTRUM-MOS2-DE-001",
                "subject_domain": sd, "evidence_kind": "scientific", "claim_level": "concept",
                "evidence_role": "primary_authoritative", "intended_use": use}
    ok("1a_spektrum_not_formula", admissible(spektrum_ctx("SD-INORGANIC-CHEMISTRY", "chemical_formula_identity"), d)[0] is False)
    ok("1b_spektrum_not_structure", admissible(spektrum_ctx("SD-MATERIALS-SCIENCE", "crystal_structure_identity_2h"), d)[0] is False)
    ok("1c_spektrum_not_lattice", admissible(spektrum_ctx("SD-MATERIALS-SCIENCE", "lattice_parameter_2h"), d)[0] is False)

    # 2 scientific evidence cannot silently establish a German lexeme
    sci_as_lexeme = {"source_id": "SRC-PUBCHEM-MOS2", "qualification_id": "QUAL-PUBCHEM-MOS2-001",
                     "subject_domain": "SD-TERMINOLOGY", "evidence_kind": "terminological", "claim_level": "lexeme",
                     "evidence_role": "primary_authoritative", "intended_use": "german_lexeme_or_terminology"}
    ok("2_scientific_not_lexeme", admissible(sci_as_lexeme, d)[0] is False)

    # 3 formula claim resolves to the molybdenum_disulfide concept (concept-eligible)
    ok("3_formula_concept", claims["CLM-MOS2-FORMULA"]["claim_level"] == "concept"
       and pubchem["concept_ids"] == ["molybdenum_disulfide"] and "molybdenum_disulfide" in elig
       and all(e["claim_level"] == "concept" and e["evidence_kind"] == "scientific" for e in all_ev))

    # 4 polytype/form scope retained (2H) and 3R/monolayer distinguished
    ok("4_polytype_scope", struct1["scientific_scope"]["polytype"] == "2H"
       and struct2["scientific_scope"]["polytype"] == "2H"
       and "polytype_3r_or_1t_or_monolayer" in struct1["prohibited_uses"]
       and "3R" in struct1["scientific_scope"]["polytype_boundary"])

    # 5 a monolayer/other-form value cannot become the 2H/bulk (or global) value
    base_cod = {"source_id": "SRC-COD-MOS2-DICKINSON-1923", "qualification_id": "QUAL-COD-MOS2-DICKINSON-001",
                "subject_domain": "SD-MATERIALS-SCIENCE", "evidence_kind": "scientific", "claim_level": "concept",
                "evidence_role": "primary_scientific"}
    ok("5a_form_veto", admissible({**base_cod, "intended_use": "polytype_3r_or_1t_or_monolayer"}, d)[0] is False)
    ok("5b_form_scope_recorded", latt1["scientific_scope"]["material_form"].startswith("2H")
       and "must NOT be attached to monolayer" in latt1["scientific_scope"]["form_scope_rule"])

    # 6 numeric property carries unit + conditions, and normalizes correctly
    m1 = latt1["quantitative"]["primary_measure"]
    ok("6a_unit_and_conditions", m1["unit"] == "angstrom"
       and latt1["quantitative"]["numeric_convention_id"] == "NUM-EN-DOT-DECIMAL"
       and "method" in latt1["scientific_scope"] and "conditions" in latt1["scientific_scope"])
    ok("6b_normalization", normalize("3.15", "NUM-EN-DOT-DECIMAL") == (3.15, None)
       and validate_evidence_numbers(latt1) == [] and validate_evidence_numbers(latt2) == []
       and m1["series"]["value"]["source_literal"] == "3.15" and m1["series"]["value"]["normalized_value"] == 3.15
       and m1["uncertainty"] == 0.02)

    # 7 conflicting/independent values coexist without a forced single value
    v1 = latt1["quantitative"]["primary_measure"]["series"]["value"]["normalized_value"]
    v2 = latt2["quantitative"]["primary_measure"]["series"]["value"]["normalized_value"]
    ok("7_values_coexist", v1 == 3.15 and v2 == 3.161 and v1 != v2
       and claims["CLM-MOS2-LATTICE-A-2H"]["supporting_evidence_ids"] == ["EVD-MOS2-LATTICE-A-DICKINSON", "EVD-MOS2-LATTICE-A-ACTACRYST"])

    # 8 source category alone does not admit (no qualification)
    ok("8_category_alone", admissible({"source_id": "SRC-PUBCHEM-MOS2", "qualification_id": None,
        "subject_domain": "SD-INORGANIC-CHEMISTRY", "evidence_kind": "scientific", "claim_level": "concept",
        "evidence_role": "primary_authoritative", "intended_use": "chemical_formula_identity"}, d)[0] is False)

    # 9 qualification is use-scoped: a structure/lattice source cannot support band gap
    ok("9_use_scoped", admissible({**base_cod, "intended_use": "band_gap"}, d)[0] is False
       and "band_gap" in quals["QUAL-COD-MOS2-DICKINSON-001"]["prohibited_uses"]
       and "band_gap" not in quals["QUAL-COD-MOS2-DICKINSON-001"]["allowed_uses"])

    # 10 source verification does not imply lock
    new_ids = ["SRC-PUBCHEM-MOS2", "SRC-NIST-MOS2", "SRC-COD-MOS2-DICKINSON-1923", "SRC-COD-MOS2-ACTACRYST-1983"]
    ok("10a_verified_not_locked", all(srcs[i]["status"] == "verified" and srcs[i]["source_lock_status"] == "candidate" for i in new_ids))
    ok("10b_no_source_locked", all(s.get("source_lock_status") == "candidate" for s in srcs.values()))

    # 11 evidence admission / claims do not imply activation
    ok("11a_non_operational", p3.get("operational") is False)
    ok("11b_nothing_activated", load("claim_activation_policy.json")["this_sprint"].startswith("No registry activated"))

    # 12/13 claims/evidence create no routes; no public page
    url_fields = {"path", "route", "url_route", "route_id", "in_sitemap", "indexable"}
    leaked = set()
    for e in all_ev:
        leaked |= (url_fields & set(e.keys()))
    ok("12_no_routes", not leaked)
    ok("13_no_public_page", load("sources", "source_registry.json")["status"] == "inactive")

    # 14 Contract C remains not_public/noindex for every claim's derived posture
    postures = {}
    for cid, binds in {
        "A": [(pubchem, "QUAL-PUBCHEM-MOS2-001", "chemical_formula_identity"),
              (nist, "QUAL-NIST-MOS2-001", "chemical_formula_identity")],
        "B": [(struct1, "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h"),
              (struct2, "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h")],
        "C": [(latt1, "QUAL-COD-MOS2-DICKINSON-001", "lattice_parameter_2h"),
              (latt2, "QUAL-COD-MOS2-ACTACRYST-001", "lattice_parameter_2h")],
    }.items():
        postures[cid] = derive_evidence_posture_governed(binds, "primary_plus_corroborating", d)
    ok("14a_postures_sufficient", postures == {"A": "evidence_sufficient", "B": "evidence_sufficient", "C": "evidence_sufficient"}, str(postures))
    ok("14b_contract_c", all(derive(governance="planned", evidence=p, claim="claim_pending",
        validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex") for p in postures.values()))

    # 15 (regression) Spektrum stays lexical-only and untouched
    sq = quals["QUAL-SPEKTRUM-MOS2-DE-001"]
    ok("15_spektrum_lexical_only", sq["permitted_evidence_kinds"] == ["terminological"]
       and set(sq["applicable_subject_domains"]) == {"SD-TERMINOLOGY", "SD-LINGUISTICS"}
       and srcs["SRC-SPEKTRUM-MOS2-DE"]["category"] == "authoritative_dictionary")

    # 16 admission bridge computes admitted (forged admitted=true ignored)
    forged = dict(pubchem); forged["admitted"] = True
    u, _ = build_admission_unit(forged, "QUAL-PUBCHEM-MOS2-001", "chemical_formula_identity", d)
    ok("16_bridge_recomputes", u["admitted"] is True and u["review_posture"] == "evidence_verified")

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all Pilot 03 proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
