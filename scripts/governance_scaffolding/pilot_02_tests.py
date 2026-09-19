"""
Pilot 02 (OCP Group x sulfur x Morocco industrial context x FY2024) — required proofs.

Proves the governance layer can REPRESENT a corporate actor and its sulfur relationship
without turning issuer disclosures into national statistics or market claims, and that it
correctly WITHHOLDS: the three principal claims are BLOCKED (OCP primary documents could not
be opened here). No figure/sentence was taken from prompt text or search snippets.

Pure; reads governance data; changes nothing; unwired from CI. Exit 0 pass / 1 fail.
"""

import copy
import json
import os
import sys

from source_admissibility import load_all, admissible, evaluate_sufficiency, derive_evidence_posture, _independent
from numeric_normalization import normalize, magnitude, validate_evidence_numbers
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
    onto_roles = load("ontology_node_roles.json")
    onto = load("ontology", "sulfur_terms.json")
    claims = {c["claim_id"]: c for c in load("pilots", "PILOT_02_claims.json")["claims"]}
    pilot_store = load("pilots", "PILOT_02_claims.json")

    # 1 OCP identity resolves as an organization
    ok("1_ocp_org_resolves", "ORG-OCP-GROUP" in orgs and orgs["ORG-OCP-GROUP"]["organization_type"] == "company")

    # 2 OCP cannot be silently substituted for GEO-MA (id spaces disjoint; org is not a geography)
    ok("2_org_not_geo", "ORG-OCP-GROUP" not in geo_ids and "GEO-MA" in geo_ids
       and orgs["ORG-OCP-GROUP"]["home_geography_context"] == "GEO-MA"  # disambiguation hint only
       and "GEO-MA" != "ORG-OCP-GROUP")

    # 3 both OCP source identities carry identity_revision
    ok("3_identity_revision", srcs["SRC-OCP-AFR-2024"].get("identity_revision") == "rev-2026-09-19-1"
       and srcs["SRC-OCP-SUSTAINABILITY-2024"].get("identity_revision") == "rev-2026-09-19-1")

    # 4 accounting "(8,344)" retains exact literal + correct SIGNED normalization; parentheses never dropped
    ok("4a_signed_normalization", normalize("(8,344)", "NUM-ACCOUNTING-PAREN-NEG") == (-8344, None)
       and normalize("8,344", "NUM-ACCOUNTING-PAREN-NEG") == (8344, None))
    paren_drop = {"quantitative": {"numeric_convention_id": "NUM-ACCOUNTING-PAREN-NEG",
                                   "m": {"source_literal": "(8,344)", "normalized_value": 8344}}}
    paren_ok = {"quantitative": {"numeric_convention_id": "NUM-ACCOUNTING-PAREN-NEG",
                                 "m": {"source_literal": "(8,344)", "normalized_value": -8344}}}
    ok("4b_parentheses_not_dropped", validate_evidence_numbers(paren_drop) != [] and validate_evidence_numbers(paren_ok) == [])

    # 5 accounting magnitude cannot be confused with a Morocco trade value
    #   (signed value is negative; magnitude is a DERIVED positive, and the accounting convention
    #    is NOT the FR trade convention)
    signed, _ = normalize("(8,344)", "NUM-ACCOUNTING-PAREN-NEG")
    ok("5_magnitude_labelled", signed == -8344 and magnitude(signed) == 8344
       and normalize("(8,344)", "NUM-FR-DOT-THOUSANDS")[0] is None)

    # 6 corporate financial evidence cannot satisfy sovereign trade claims (SD-TRADE)
    d6 = load_all()
    q6 = copy.deepcopy(quals["QUAL-OCP-AFR-001"])
    q6.update({"applicable_subject_domains": ["SD-TRADE"], "qualification_state": "qualified_narrow",
               "allowed_uses": ["morocco_trade_totals"], "evidence_roles": ["official_record"]})
    d6["qual_by_id"]["QUAL-OCP-AFR-001"] = q6
    ctx6 = {"source_id": "SRC-OCP-AFR-2024", "qualification_id": "QUAL-OCP-AFR-001",
            "subject_domain": "SD-TRADE", "evidence_kind": "quantitative", "claim_level": "relationship",
            "evidence_role": "official_record", "intended_use": "morocco_trade_totals", "geography": "GEO-MA"}
    ok("6_corporate_not_trade", admissible(ctx6, d6)[0] is False, admissible(ctx6, d6)[1])

    # 7 sustainability evidence cannot establish a financial amount
    d7 = load_all()
    q7 = copy.deepcopy(quals["QUAL-OCP-SUS-001"])
    q7.update({"applicable_subject_domains": ["SD-CORPORATE-FINANCIALS"], "qualification_state": "qualified_narrow",
               "permitted_evidence_kinds": ["quantitative"], "permitted_claim_levels": ["relationship"],
               "allowed_uses": ["issuer_own_accounting_line_ocp_fy2024"], "evidence_roles": ["primary_authoritative"]})
    d7["qual_by_id"]["QUAL-OCP-SUS-001"] = q7
    ctx7 = {"source_id": "SRC-OCP-SUSTAINABILITY-2024", "qualification_id": "QUAL-OCP-SUS-001",
            "subject_domain": "SD-CORPORATE-FINANCIALS", "evidence_kind": "quantitative", "claim_level": "relationship",
            "evidence_role": "primary_authoritative", "intended_use": "issuer_own_accounting_line_ocp_fy2024"}
    ok("7_sustainability_not_financial", admissible(ctx7, d7)[0] is False, admissible(ctx7, d7)[1])

    # 8 sulfur purchase evidence cannot establish tonnage (veto), while the allowed use WOULD admit if ratified
    d8 = load_all()
    q8 = copy.deepcopy(quals["QUAL-OCP-AFR-001"]); q8["qualification_state"] = "qualified_narrow"
    d8["qual_by_id"]["QUAL-OCP-AFR-001"] = q8
    base8 = {"source_id": "SRC-OCP-AFR-2024", "qualification_id": "QUAL-OCP-AFR-001",
             "subject_domain": "SD-CORPORATE-FINANCIALS", "evidence_kind": "quantitative", "claim_level": "relationship",
             "evidence_role": "primary_authoritative"}
    ok("8a_tonnage_vetoed", admissible({**base8, "intended_use": "physical_tonnage_from_value"}, d8)[0] is False)
    ok("8b_allowed_use_would_admit", admissible({**base8, "intended_use": "issuer_own_accounting_line_ocp_fy2024"}, d8)[0] is True,
       admissible({**base8, "intended_use": "issuer_own_accounting_line_ocp_fy2024"}, d8)[1])

    # 8c deny-by-default: the REAL qualification is 'candidate' -> not admissible
    ok("8c_real_qual_candidate_denied", quals["QUAL-OCP-AFR-001"]["qualification_state"] == "candidate"
       and admissible({**base8, "intended_use": "issuer_own_accounting_line_ocp_fy2024"}, d)[0] is False)

    # 9 price-per-ton narrative is ABSENT (not ingested); no $/T CFR figure anywhere in pilot artifacts
    text = ""
    for f in ["pilots/PILOT_02_claims.json", "pilots/MOROCCO_OCP_SULFUR_INDUSTRIAL_PILOT_02.md"]:
        p = os.path.join(DATA, f)
        if os.path.exists(p):
            text += open(p, encoding="utf-8").read().lower()
    ok("9_no_price_narrative", "$/t" not in text and "cfr" not in text and "per ton" not in text and "per tonne" not in text)

    # 10 the industrial relationship is period-bounded (FY2024) and NOT created as an instance
    ok("10a_period_bounded", quals["QUAL-OCP-AFR-001"]["temporal_boundary"] == {"valid_from": "2024-01-01", "valid_to": "2024-12-31"})
    rels = load("relationship_class_registry.json")
    ocp_inst = [i for i in rels.get("relationship_instances", []) if i.get("subject_ref") == "ORG-OCP-GROUP"]
    ok("10b_no_unbounded_instance", ocp_inst == [], f"unexpected OCP relationship instance(s): {[i.get('relationship_instance_id') for i in ocp_inst]}")

    # 11 same-issuer reports do NOT automatically count as independent corroboration
    uAFR = {"role": "primary_authoritative", "source_id": "SRC-OCP-AFR-2024", "publisher": "OCP Group"}
    uSUS = {"role": "corroborating", "source_id": "SRC-OCP-SUSTAINABILITY-2024", "publisher": "OCP Group"}
    ok("11a_same_issuer_not_independent", _independent(uAFR, uSUS) is False)
    ok("11b_no_self_corroboration_across_reports",
       evaluate_sufficiency([uAFR, uSUS], "primary_plus_corroborating")[0] is False)

    # 12 no sulfuric-acid concept fabricated
    elig = {n["term_id"] for n in onto_roles["node_roles"] if n["role"] == "concept_eligible"}
    all_terms = {t["term_id"] for t in onto["terms"]}
    ok("12_no_sulfuric_acid_concept", "sulfuric_acid" not in elig and "sulfuric_acid" not in all_terms)

    # 13 source verification does not imply lock — OCP sources are seeded (unverified) AND lock candidate;
    #    no source anywhere is locked
    ok("13a_ocp_seeded_candidate", srcs["SRC-OCP-AFR-2024"]["status"] == "seeded"
       and srcs["SRC-OCP-AFR-2024"]["source_lock_status"] == "candidate"
       and srcs["SRC-OCP-SUSTAINABILITY-2024"]["status"] == "seeded"
       and srcs["SRC-OCP-SUSTAINABILITY-2024"]["source_lock_status"] == "candidate")
    ok("13b_no_source_locked", all(s.get("source_lock_status") == "candidate" for s in srcs.values()))

    # 14 evidence admission / claims do not imply activation
    ok("14a_claims_non_operational", pilot_store.get("operational") is False)
    ca = load("claim_activation_policy.json")
    ok("14b_nothing_activated", ca["this_sprint"].startswith("No registry activated"))
    ok("14c_all_blocked", all(c["outcome"] == "BLOCKED" and c["supporting_evidence_ids"] == [] for c in claims.values()))

    # 15 relationship does not imply route creation (even a hypothetical locked posture stays not_public/noindex)
    ok("15a_relationship_not_route",
       derive(governance="planned", evidence="evidence_locked", claim="claim_pending",
              validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))
    url_fields = {"path", "route", "url_route", "route_id", "in_sitemap", "indexable"}
    ok("15b_no_url_fields", not (url_fields & set(orgs["ORG-OCP-GROUP"].keys())))

    # 16 Contract C derived from ACTUAL Pilot-02 postures: nothing admitted -> evidence_collecting -> not_public
    real_units = []  # no admitted evidence exists (all claims blocked)
    posture = derive_evidence_posture(real_units, "single_authoritative_sufficient")
    final = derive(governance="planned", evidence=posture, claim="claim_pending",
                   validation="not_validated", ig="ig_not_reviewed", release="not_authorized")
    ok("16_contract_c", posture == "evidence_collecting" and final == ("not_public", "noindex"), f"{posture} {final}")

    # 17 organization identity carries no financials/relationship/route fields
    forbidden = {"financials", "revenue", "market_position", "ownership", "acquisition", "relationship", "supporting_evidence_ids", "route", "status"}
    ok("17_org_identity_only", not (forbidden & set(orgs["ORG-OCP-GROUP"].keys())))

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all Pilot 02 proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
