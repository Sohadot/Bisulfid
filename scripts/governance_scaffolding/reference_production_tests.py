"""
Reference Production 01 (MoS2 scientific Knowledge Object) — required proofs (§20).

Exercises Evidence -> Claim Set -> Knowledge Object -> IG review -> Publication Candidate,
proving the KO aggregates governed claims/evidence without re-owning facts, IG is semantic
multi-signal (no threshold), and nothing publishes.

Pure; reads governance data; recomputes Contract-C via the real engine; unwired from CI.
Exit 0 pass / 1 fail.
"""

import os
import json
import sys

from source_admissibility import load_all, derive_evidence_posture_governed
from contract_c_derive import derive

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
FAIL = []


def load(*p):
    with open(os.path.join(DATA, *p), encoding="utf-8") as fh:
        return json.load(fh)


def raw(*p):
    with open(os.path.join(DATA, *p), encoding="utf-8") as fh:
        return fh.read()


def ok(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAIL.append(name)


def main():
    print("=== Reference Production 01 (MoS2 KO) tests ===")
    d = load_all()
    koreg = load("knowledge_objects", "knowledge_object_registry.json")
    ko = koreg["knowledge_objects"][0]
    pc = load("publication_candidates", "PC-MOS2-SCIENTIFIC-001.json")
    cp = load("information_gain", "calibration_pairs.json")
    p3 = {c["claim_id"]: c for c in load("pilots", "PILOT_03_claims.json")["claims"]}
    onto_roles = load("ontology_node_roles.json")
    elig = {n["term_id"] for n in onto_roles["node_roles"] if n["role"] == "concept_eligible"}
    ev_dir = os.path.join(DATA, "evidence")
    ev_ids = {load("evidence", n).get("evidence_id") for n in os.listdir(ev_dir) if n.startswith("EVD-") and n.endswith(".json")}
    _routes_obj = load("routes.json")
    routes = _routes_obj if isinstance(_routes_obj, list) else _routes_obj.get("routes", [])
    route_ids = {r.get("route_id") for r in routes}
    ko_raw = raw("knowledge_objects", "knowledge_object_registry.json")

    # 1 KO resolves to molybdenum_disulfide
    ok("1_ko_entity", ko["knowledge_object_id"] == "KO-MOS2-SCIENTIFIC-001"
       and ko["entity_ids"] == ["molybdenum_disulfide"] and "molybdenum_disulfide" in elig)

    # 2 references existing claims rather than inventing facts
    ok("2_references_claims", set(ko["claim_ids"]) == {"CLM-MOS2-FORMULA", "CLM-MOS2-STRUCTURE-2H", "CLM-MOS2-LATTICE-A-2H"}
       and all(cid in p3 for cid in ko["claim_ids"]))

    # 3 every bound evidence_id resolves
    ok("3_evidence_resolves", all(e in ev_ids for e in ko["evidence_ids"] + ko.get("boundary_evidence_ids", [])))

    # 4 evidence values remain owned by evidence records (KO OBJECT stores no raw values)
    ko_obj = json.dumps(ko)
    ok("4_one_owner", "normalized_value" not in ko_obj and "source_literal" not in ko_obj and "3.15" not in ko_obj
       and load("evidence", "EVD-MOS2-LATTICE-A-DICKINSON.json")["quantitative"]["primary_measure"]["series"]["value"]["normalized_value"] == 3.15)

    # 5 Claim A/B/C unchanged from Pilot 03
    ok("5_claims_unchanged", p3["CLM-MOS2-FORMULA"]["statement"] == "The formula of molybdenum disulfide is MoS2."
       and "layered" in p3["CLM-MOS2-STRUCTURE-2H"]["statement"]
       and p3["CLM-MOS2-LATTICE-A-2H"]["outcome"].startswith("SUPPORTED_CONDITIONAL"))

    # 6 German lexical evidence not merged into the scientific object
    ok("6_no_lexical_merge", "EVD-MOS2-DE-001" not in ko["evidence_ids"]
       and ko["distinct_from"]["german_lexical_object"]["claim_id"] == "CLM-TERM-MOS2-DE-001")

    # 7 3R remains boundary/context, not 2H claim support
    bound = {e for cb in ko["claim_bindings"] for e in cb["evidence_ids"]}
    ok("7_3r_boundary_only", "EVD-MOS2-3R-BOUNDARY-RSC" in ko.get("boundary_evidence_ids", [])
       and "EVD-MOS2-3R-BOUNDARY-RSC" not in bound)

    # 8 band gap absent
    ok("8_no_band_gap", "band_gap" in ko["excluded_claim_classes"]
       and "band" not in " ".join(ko["claim_ids"]).lower()
       and all("band" not in c.lower() for c in ko["entity_ids"]))

    # 9 source locks remain candidate
    srcs = load("sources", "source_registry.json")["sources"]
    ok("9_locks_candidate", all(s.get("source_lock_status") == "candidate" for s in srcs))

    # 10 no claim registry activated
    ok("10_no_activation", ko["claim_source"] == "pilot_non_operational"
       and load("pilots", "PILOT_03_claims.json").get("operational") is False
       and load("claim_activation_policy.json")["this_sprint"].startswith("No registry activated"))

    # 11 no route created (routes.json unchanged count; KO/PC carry no route/url fields)
    url_fields = {"route", "path", "url", "url_route", "in_sitemap", "indexable", "html"}
    ok("11_no_route", len(routes) == 14000 and "KO-MOS2-SCIENTIFIC-001" not in route_ids
       and not (url_fields & set(ko.keys())) and not (url_fields & set(pc.keys())))

    # 12 no HTML generated (KO/PC carry no html FIELD; html is a forbidden field)
    ok("12_no_html", "html" in set(koreg["record_schema"]["forbidden_fields"])
       and "html" not in ko.keys() and "html" not in pc.keys())

    # 13 no sitemap/robots change (KO/PC declare no sitemap entry)
    ok("13_no_sitemap", "in_sitemap" not in ko and "in_sitemap" not in pc)

    # 14 IG uses the existing multi-signal model
    ok("14_multi_signal", set(cp["signals"]) == {
        "evidence_set_overlap", "claim_set_overlap", "source_set_overlap", "relationship_difference",
        "geography_jurisdiction_difference", "temporal_difference", "module_section_overlap",
        "user_task_difference", "textual_similarity"})

    # 15 textual similarity cannot independently decide
    ok("15_textual_diagnostic", all("diagnostic" in str(p["signals"].get("textual_similarity", "")).lower()
                                    and len(set(p["signals"].keys()) - {"textual_similarity"}) >= 3
                                    for p in cp["pairs"]))

    # 16 calibration pairs reference real objects/routes
    ko_ids = {k["knowledge_object_id"] for k in koreg["knowledge_objects"]}
    def endpoint_ok(v):
        base = str(v).split("#")[0]
        return base in ko_ids or base in route_ids
    ok("16_pairs_real", len(cp["pairs"]) >= 3 and all(
        endpoint_ok(p.get("object_a") or p.get("route_a")) and endpoint_ok(p.get("object_b") or p.get("route_b"))
        for p in cp["pairs"]))

    # 17 no arbitrary IG threshold
    def keys_rec(o):
        if isinstance(o, dict):
            for k, v in o.items():
                yield k
                yield from keys_rec(v)
        elif isinstance(o, list):
            for v in o:
                yield from keys_rec(v)
    ok("17_no_threshold", not [k for k in keys_rec(cp) if "threshold" in k.lower() or "weight" in k.lower()])

    # 18 Contract C is computed, not manually written (recompute == recorded == not_public/noindex)
    p = ko["postures"]
    recomputed = derive(governance=p["governance_posture"], evidence=p["evidence_posture"], claim=p["claim_posture"],
                        validation=p["validation_posture"], ig=p["information_gain_posture"], release=p["release_authorization"])
    dc = ko["derived_contract_c"]
    ok("18_contract_c_computed", recomputed == ("not_public", "noindex")
       and (dc["publication_state"], dc["indexation_state"]) == recomputed
       and (pc["derived_contract_c"]["publication_state"], pc["derived_contract_c"]["indexation_state"]) == recomputed)

    # 18b evidence posture is really derived (aggregate of A/B/C)
    agg = min(
        [derive_evidence_posture_governed([(load("evidence", "EVD-MOS2-FORMULA-PUBCHEM.json"), "QUAL-PUBCHEM-MOS2-001", "chemical_formula_identity"),
                                           (load("evidence", "EVD-MOS2-FORMULA-NIST.json"), "QUAL-NIST-MOS2-001", "chemical_formula_identity")], "primary_plus_corroborating", d),
         derive_evidence_posture_governed([(load("evidence", "EVD-MOS2-STRUCTURE-DICKINSON.json"), "QUAL-COD-MOS2-DICKINSON-001", "crystal_structure_identity_2h"),
                                           (load("evidence", "EVD-MOS2-STRUCTURE-ACTACRYST.json"), "QUAL-COD-MOS2-ACTACRYST-001", "crystal_structure_identity_2h")], "primary_plus_corroborating", d),
         derive_evidence_posture_governed([(load("evidence", "EVD-MOS2-LATTICE-A-DICKINSON.json"), "QUAL-COD-MOS2-DICKINSON-001", "lattice_parameter_2h"),
                                           (load("evidence", "EVD-MOS2-LATTICE-A-ACTACRYST.json"), "QUAL-COD-MOS2-ACTACRYST-001", "lattice_parameter_2h")], "primary_plus_corroborating", d)],
        key=lambda x: {"evidence_collecting": 0, "evidence_sufficient": 1, "evidence_locked": 2}[x])
    ok("18b_evidence_posture_derived", agg == "evidence_sufficient" and p["evidence_posture"] == "evidence_sufficient")

    # 19 a new reference_draft cannot become public (even with otherwise-strong postures)
    ok("19_reference_draft_not_public",
       derive(governance="reference_draft", evidence="evidence_locked", claim="claim_approved",
              validation="validated", ig="ig_passed", release="authorized")[0] == "not_public")

    # 20 ig_not_reviewed cannot become public
    ok("20_ig_not_reviewed_not_public",
       derive(governance="governed", evidence="evidence_locked", claim="claim_approved",
              validation="validated", ig="ig_not_reviewed", release="authorized")[0] == "not_public")

    # 21 legacy public holding is not used for this new object
    ok("21_no_legacy_holding", "legacy_public_holding" not in json.dumps(ko) and "legacy_public_holding" not in json.dumps(pc))

    # 22 publication-candidate is an internal candidate, never published/indexable
    ok("22_candidate_not_published", pc["status"] == "internal_candidate"
       and pc["proposed_disposition"] == "independent_reference_candidate"
       and "published" in pc["not_disposition"] and "indexable" in pc["not_disposition"]
       and pc["postures"]["information_gain_posture"] == "ig_not_reviewed")

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all Reference Production 01 proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
