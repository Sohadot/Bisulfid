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

from source_admissibility import load_all, admissible, build_admission_unit, derive_evidence_posture_governed, _independent
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

    # ===================== Scientific Provenance Closure (§26 / §27) =====================
    works = {w["work_id"]: w for w in load("originating_work_registry.json")["works"]}
    layered_rsc = ev("EVD-MOS2-LAYERED-RSC"); poly_rsc = ev("EVD-MOS2-POLYTYPES-RSC")
    ref2h_rsc = ev("EVD-MOS2-2H-REF-RSC"); r3_rsc = ev("EVD-MOS2-3R-BOUNDARY-RSC")
    acta_x = ev("EVD-MOS2-LAYERED-ACTA1983-EXCERPT"); jacs_x = ev("EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT")
    huang = ev("EVD-MOS2-LAYERED-HUANG1981")
    claimB = claims["CLM-MOS2-STRUCTURE-2H"]

    def adm(evrec, qid, use):
        return build_admission_unit(evrec, qid, use, d)[0]["admitted"]

    # §26.1 layered has admitted evidence
    ok("26_1_layered_admitted", adm(layered_rsc, "QUAL-RSC-MOS2-REVIEW-001", "layered_structure_mos2") is True
       and adm(acta_x, "QUAL-ACTACRYST-MOS2-1983-EXCERPT-001", "layered_dichalcogenide_context") is True
       and "EVD-MOS2-LAYERED-RSC" in claimB["components"]["layered"]["supporting_evidence_ids"])
    # §26.2 2H label has admitted evidence
    ok("26_2_2h_admitted", adm(ref2h_rsc, "QUAL-RSC-MOS2-REVIEW-001", "crystal_structure_identity_2h") is True
       and adm(acta_x, "QUAL-ACTACRYST-MOS2-1983-EXCERPT-001", "mos2_2h_3r_terminology") is True)
    # §26.3 space group P63/mmc has admitted evidence (two independent COD works -> sufficient)
    sg = derive_evidence_posture_governed([
        (ev("EVD-MOS2-STRUCTURE-DICKINSON"), "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h"),
        (ev("EVD-MOS2-STRUCTURE-ACTACRYST"), "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h")],
        "primary_plus_corroborating", d)
    ok("26_3_spacegroup_admitted", sg == "evidence_sufficient")
    # §26.4 Dickinson 1923 excerpt not represented as saying '2H'
    ok("26_4_no_false_2h", jacs_x["scientific_scope"].get("modern_2h_label_present") is False
       and "modern_2h_label" in jacs_x["prohibited_uses"]
       and adm(jacs_x, "QUAL-JACS-MOLYBDENITE-1923-EXCERPT-001", "modern_2h_label") is False)
    # §26.5 RSC review explicitly distinguishes 1T/2H/3R
    ok("26_5_rsc_polytypes", set(poly_rsc["scientific_scope"]["polytypes"]) == {"1T", "2H", "3R"}
       and "1T" in poly_rsc["locator"]["verbatim"] and "3R" in poly_rsc["locator"]["verbatim"])
    # §26.6 3R-specific details cannot contaminate the 2H claim (record scope + claim wiring)
    comp_ids = {e for c in claimB["components"].values() for e in c["supporting_evidence_ids"]}
    ok("26_6_3r_not_2h", r3_rsc.get("claim_id") is None
       and "EVD-MOS2-3R-BOUNDARY-RSC" not in claimB["supporting_evidence_ids"]
       and "EVD-MOS2-3R-BOUNDARY-RSC" not in comp_ids
       and r3_rsc["allowed_uses"] == ["polytype_3r_reference"]
       and "attach_to_2h_claim" in r3_rsc["prohibited_uses"]
       and "crystal_structure_identity_2h" in r3_rsc["prohibited_uses"])
    # §26.7 a review cannot masquerade as a primary experiment (secondary alone insufficient)
    rsc_alone = derive_evidence_posture_governed([
        (ref2h_rsc, "QUAL-RSC-MOS2-REVIEW-001", "crystal_structure_identity_2h")], "primary_plus_corroborating", d)
    ok("26_7_review_not_primary", ref2h_rsc["evidence_role"] == "secondary_scholarly"
       and works["WORK-SONG-PARK-CHOI-2015"]["work_type"] == "secondary_review"
       and rsc_alone == "evidence_collecting")

    codD = srcs["SRC-COD-MOS2-DICKINSON-1923"]; codA = srcs["SRC-COD-MOS2-ACTACRYST-1983"]
    # §27.1 COD not a peer-reviewed journal artifact
    ok("27_1_cod_not_journal", codD["category"] == "crystallographic_database" and codA["category"] == "crystallographic_database")
    # §27.2 COD retains originating DOI
    ok("27_2_cod_doi", codD["originating_doi"] == "10.1021/ja01659a020" and codA["originating_doi"] == "10.1107/S0108768183002645")
    # §27.3 COD retains originating_work_id
    ok("27_3_cod_work", codD["originating_work_id"] == "WORK-DICKINSON-PAULING-1923" and codA["originating_work_id"] == "WORK-SCHONFELD-HUANG-MOSS-1983")
    # §27.4 retrieval_repository != originating_work
    ok("27_4_retrieval_vs_work", codD.get("retrieval_repository", "").startswith("Crystallography Open Database")
       and codD["originating_work_id"] != codD.get("retrieval_repository"))
    # §27.5 / §27.8 same originating_work_id cannot count twice (excerpt + COD copy = one lineage)
    uCOD, _ = build_admission_unit(ev("EVD-MOS2-STRUCTURE-DICKINSON"), "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h", d)
    uJAC, _ = build_admission_unit(jacs_x, "QUAL-JACS-MOLYBDENITE-1923-EXCERPT-001", "molybdenite_mos2_hexagonal_identity", d)
    ok("27_5_same_work_one_lineage", _independent(uCOD, uJAC) is False)
    # §27.6 different COD IDs are not automatically independent — same work => not independent
    fake = dict(uJAC); fake["originating_work_id"] = "WORK-DICKINSON-PAULING-1923"; fake["source_id"] = "SRC-OTHER"
    ok("27_6_diff_id_not_auto_indep", _independent(uCOD, fake) is False)
    # §27.7 Dickinson 1923 vs Schonfeld/Huang/Moss 1983 = distinct lineages (independent)
    uCODA, _ = build_admission_unit(ev("EVD-MOS2-STRUCTURE-ACTACRYST"), "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h", d)
    ok("27_7_distinct_lineages_independent", _independent(uCOD, uCODA) is True)
    # §27.9 Huang thesis not a peer-reviewed journal; and not independent of the 1983 work
    uHUANG, _ = build_admission_unit(huang, "QUAL-HUANG-THESIS-1981-001", "layered_structure_mos2", d)
    ok("27_9_thesis_not_journal", srcs["SRC-HUANG-THESIS-1981"]["category"] == "academic_thesis"
       and _independent(uCODA, uHUANG) is False)
    # §27.10 RSC review is not a primary experimental study
    ok("27_10_review_not_primary_study", srcs["SRC-RSC-MOS2-REVIEW-2015"]["category"] == "peer_reviewed_journal"
       and works["WORK-SONG-PARK-CHOI-2015"]["work_type"] == "secondary_review")

    # closure: new sources verified but lock candidate; overall Claim B posture sufficient; Contract-C safe
    new2 = ["SRC-RSC-MOS2-REVIEW-2015", "SRC-ACTACRYST-MOS2-1983-EXCERPT", "SRC-JACS-MOLYBDENITE-1923-EXCERPT", "SRC-HUANG-THESIS-1981"]
    ok("28_new_sources_candidate", all(srcs[i]["status"] == "verified" and srcs[i]["source_lock_status"] == "candidate" for i in new2))
    B_all = derive_evidence_posture_governed([
        (ev("EVD-MOS2-STRUCTURE-DICKINSON"), "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h"),
        (ev("EVD-MOS2-STRUCTURE-ACTACRYST"), "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h"),
        (layered_rsc, "QUAL-RSC-MOS2-REVIEW-001", "layered_structure_mos2"),
        (acta_x, "QUAL-ACTACRYST-MOS2-1983-EXCERPT-001", "layered_dichalcogenide_context")],
        "primary_plus_corroborating", d)
    ok("28_claimB_sufficient", B_all == "evidence_sufficient"
       and derive(governance="planned", evidence=B_all, claim="claim_pending", validation="not_validated",
                  ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))
    # Claim A wording corrected; layered retained in Claim B statement
    ok("28_wording", claims["CLM-MOS2-FORMULA"]["statement"] == "The formula of molybdenum disulfide is MoS2."
       and "layered" in claimB["statement"])

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all Pilot 03 proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
