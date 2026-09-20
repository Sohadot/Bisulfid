"""
Information-Gain Governance Ratification — required proofs.

Proves the ratified IG authority is machine-discoverable, deterministic, non-numeric,
fail-closed, and strictly separated from every other governance gate; that only a positive
independent-reference classification can pass; and that ratifying IG publishes nothing.

Pure; reads governance data + the real engines; unwired from CI. Exit 0 pass / 1 fail.
"""

import os
import json
import sys

from information_gain_gate import evaluate, load_policy, _posture_for, POSITIVE_CLASSIFICATIONS
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


def keys_rec(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from keys_rec(v)
    elif isinstance(o, list):
        for v in o:
            yield from keys_rec(v)


def main():
    print("=== IG Governance Ratification tests ===")
    policy = load_policy()
    cp = load("information_gain", "calibration_pairs.json")
    koreg = load("knowledge_objects", "knowledge_object_registry.json")
    ko = koreg["knowledge_objects"][0]
    pc = load("publication_candidates", "PC-MOS2-SCIENTIFIC-001.json")
    _routes_obj = load("routes.json")
    routes = _routes_obj if isinstance(_routes_obj, list) else _routes_obj.get("routes", [])
    route_ids = {r.get("route_id") for r in routes}
    ko_ids = {k["knowledge_object_id"] for k in koreg["knowledge_objects"]}
    pairs = {p["pair_id"]: p for p in cp["pairs"]}
    class_by_id = {c["classification"]: c for c in policy["classifications"]}
    post_by_id = {p["posture"]: p for p in policy["postures"]}

    # 1 policy is machine-discoverable & ratified with a version
    ok("1_policy_ratified", policy.get("policy_id") == "IG-GOVERNANCE"
       and policy.get("status") == "ratified" and bool(policy.get("version")))

    # 2 exactly the four governed classifications
    ok("2_four_classifications", set(policy["classification_ids"]) ==
       {"valid_domain_specific_reference", "near_duplicate", "module_relationship", "unresolved"}
       and set(class_by_id) == set(policy["classification_ids"]))

    # 3 only positive classifications are route-eligible
    ok("3_route_eligibility",
       class_by_id["valid_domain_specific_reference"]["route_eligible"] is True
       and class_by_id["near_duplicate"]["route_eligible"] is False
       and class_by_id["module_relationship"]["route_eligible"] is False
       and class_by_id["unresolved"]["route_eligible"] is False)

    # 4 the three governed postures exist; only ig_reviewed_pass is route-eligible
    ok("4_postures", set(policy["posture_ids"]) == {"ig_reviewed_pass", "ig_reviewed_no_new_route", "ig_review_required"}
       and post_by_id["ig_reviewed_pass"]["route_eligible"] is True
       and post_by_id["ig_reviewed_no_new_route"]["route_eligible"] is False
       and post_by_id["ig_review_required"]["route_eligible"] is False)

    # 5 numeric authority machine-discoverably prohibited; textual similarity diagnostic only
    nap = policy["numeric_authority_prohibited"]
    bad_keys = [k for k in list(keys_rec(policy)) + list(keys_rec(cp))
                if any(s in k.lower() for s in ("threshold", "weight", "cutoff", "score"))]
    ok("5_no_numeric_authority", nap.get("prohibited") is True
       and nap.get("textual_similarity_role") == "diagnostic_only"
       and not bad_keys, f"forbidden numeric key(s): {bad_keys}")

    # 6 gate is deterministic
    p1 = pairs["PAIR-KO-MOS2-SCI-vs-DE-LEXICAL"]
    ok("6_deterministic", evaluate(p1, policy) == evaluate(p1, policy))

    # 7 fail-closed on missing required signals -> unresolved / ig_review_required / no route
    r_missing = evaluate({"object_a": "KO-X", "route_b": "r", "signals": {"textual_similarity": "diagnostic_only"}}, policy)
    ok("7_fail_closed_missing", r_missing["classification"] == "unresolved"
       and r_missing["posture"] == "ig_review_required" and r_missing["route_eligible"] is False
       and r_missing["unresolved_signals"])

    # 8 fail-closed on self-comparison
    r_self = evaluate({"object_a": "KO-MOS2-SCIENTIFIC-001", "object_b": "KO-MOS2-SCIENTIFIC-001", "signals": {}}, policy)
    ok("8_fail_closed_self", r_self["classification"] == "unresolved" and r_self["route_eligible"] is False)

    # 9 textual similarity cannot decide: same-task stays near_duplicate even when text is dissimilar;
    #    "not a duplicate" alone is not independent value
    r_text = evaluate({"object_a": "KO-X", "route_b": "leg", "signals": {
        "evidence_set_overlap": "disjoint", "claim_set_overlap": "disjoint", "source_set_overlap": "disjoint",
        "relationship_difference": "low", "module_section_overlap": "high", "user_task_difference": "low",
        "textual_similarity": "low (very different wording)"}}, policy)
    ok("9_textual_not_decisive", r_text["classification"] == "near_duplicate" and r_text["route_eligible"] is False
       and "textual_similarity" not in r_text["signals_considered"])

    # 10 Pair 1 -> valid_domain_specific_reference / ig_reviewed_pass / route-eligible
    r1 = evaluate(p1, policy)
    ok("10_pair1_pass_capable", r1["classification"] == "valid_domain_specific_reference"
       and r1["posture"] == "ig_reviewed_pass" and r1["route_eligible"] is True and not r1["unresolved_signals"])

    # 11 Pair 2 -> near_duplicate / ig_reviewed_no_new_route / not route-eligible
    r2 = evaluate(pairs["PAIR-KO-MOS2-SCI-vs-LEGACY-SCI-ROUTE"], policy)
    ok("11_pair2_near_duplicate", r2["classification"] == "near_duplicate"
       and r2["posture"] == "ig_reviewed_no_new_route" and r2["route_eligible"] is False)

    # 12 Pair 3 -> module_relationship / not route-eligible
    r3 = evaluate(pairs["PAIR-KO-MOS2-FORMULA-vs-STRUCTURE-MODULE"], policy)
    ok("12_pair3_module", r3["classification"] == "module_relationship" and r3["route_eligible"] is False)

    # 13 gate NEVER returns a pass posture without a positive classification (over all pairs + edge)
    all_results = [evaluate(p, policy) for p in cp["pairs"]] + [r_missing, r_self, r_text]
    ok("13_pass_requires_positive", all(
        (res["route_eligible"] is False) or (res["classification"] in POSITIVE_CLASSIFICATIONS)
        for res in all_results))

    # 14 gate NEVER returns route_eligible with any unresolved signals
    ok("14_no_pass_with_unresolved", all(not (res["route_eligible"] and res["unresolved_signals"]) for res in all_results))

    # 15 near_duplicate / module_relationship are NOT eligible for a sibling-route pass
    ok("15_no_sibling_pass", _posture_for("near_duplicate", policy) == ("ig_reviewed_no_new_route", False)
       and _posture_for("module_relationship", policy) == ("ig_reviewed_no_new_route", False))

    # 16 IG cannot authorize publication: even the MoS2 KO's ratified posture yields not_public;
    #    and a hypothetical passed-IG object still needs every other gate (reference_draft => not_public)
    kp = ko["postures"]
    ig_public = derive(governance="reference_draft", evidence="evidence_locked", claim="claim_approved",
                       validation="validated", ig="ig_reviewed_pass", release="authorized")
    ok("16_ig_never_publishes",
       derive(governance=kp["governance_posture"], evidence=kp["evidence_posture"], claim=kp["claim_posture"],
              validation=kp["validation_posture"], ig=kp["information_gain_posture"],
              release=kp["release_authorization"])[0] == "not_public"
       and ig_public[0] == "not_public")

    # 17 gate separation: the gate output touches none of the other governance dimensions,
    #    and this sprint mutated no evidence/claim/source-lock state
    r_keys = set(r1.keys())
    forbidden_out = {"evidence_posture", "claim_posture", "source_lock_status", "validation_posture",
                     "release_authorization", "publication_state", "indexation_state", "evidence_ids", "claim_ids"}
    srcs = load("sources", "source_registry.json")["sources"]
    ok("17_gate_separation", not (r_keys & forbidden_out)
       and kp["evidence_posture"] == "evidence_sufficient" and kp["claim_posture"] == "claim_pending"
       and all(s.get("source_lock_status") == "candidate" for s in srcs))

    # 18 Contract-C for the KO is DERIVED and equals recorded == (not_public, noindex); a manual
    #    mismatch would be caught (recompute with a passing posture would differ from recorded)
    recomputed = derive(governance=kp["governance_posture"], evidence=kp["evidence_posture"], claim=kp["claim_posture"],
                        validation=kp["validation_posture"], ig=kp["information_gain_posture"], release=kp["release_authorization"])
    dc = ko["derived_contract_c"]
    ok("18_contract_c_derived", recomputed == ("not_public", "noindex")
       and (dc["publication_state"], dc["indexation_state"]) == recomputed
       and (pc["derived_contract_c"]["publication_state"], pc["derived_contract_c"]["indexation_state"]) == recomputed)

    # 19 One-Fact-One-Owner: the IG layer carries NO scientific values
    blob = json.dumps(policy) + json.dumps(cp) + json.dumps([evaluate(p, policy) for p in cp["pairs"]])
    ok("19_one_owner", "normalized_value" not in blob and "source_literal" not in blob
       and "3.15" not in blob and "P6_3" not in blob and "3.161" not in blob)

    # 20 KO separates object informational validity from new-route distinctness
    igr = ko.get("ig_resolution", {})
    ok("20_validity_vs_distinctness", igr.get("object_informational_validity") == "object_valid_governed"
       and igr.get("new_route_distinctness") == "no_new_route_warranted"
       and igr.get("new_route_classification") == "near_duplicate"
       and pc.get("ig_resolution", {}).get("object_informational_validity") == "object_valid_governed")

    # 21 governed fixtures: the gate reproduces every normative pair's expected outcome
    norm_ok = True
    for p in cp["pairs"]:
        if p.get("fixture_kind") != "normative":
            continue
        res = evaluate(p, policy)
        if not (res["classification"] == p["expected_classification"]
                and res["posture"] == p["expected_posture"]
                and res["route_eligible"] == p["expected_route_eligible"]):
            norm_ok = False
    ok("21_fixtures_reproduced", norm_ok and any(p.get("fixture_kind") == "normative" for p in cp["pairs"]))

    # 22 fixtures are well-formed: unique ids, no self-comparison, endpoints resolve, no contradiction
    ids = [p["pair_id"] for p in cp["pairs"]]
    def ep(p, s):
        return p.get(f"object_{s}") or p.get(f"route_{s}")
    def resolves(v):
        base = str(v).split("#")[0]
        return base in ko_ids or base in route_ids
    seen_endpoints = {}
    contradiction = False
    for p in cp["pairs"]:
        key = frozenset([str(ep(p, "a")), str(ep(p, "b"))])
        if key in seen_endpoints and seen_endpoints[key] != p["expected_classification"]:
            contradiction = True
        seen_endpoints[key] = p["expected_classification"]
    ok("22_fixtures_wellformed", len(ids) == len(set(ids))
       and all(ep(p, "a") != ep(p, "b") for p in cp["pairs"])
       and all(resolves(ep(p, "a")) and resolves(ep(p, "b")) for p in cp["pairs"])
       and not contradiction)

    # 23 unknown classification fails closed (no accidental pass)
    ok("23_unknown_classification", _posture_for("totally_unknown_class", policy) == ("ig_review_required", False))

    # 24 policy version referenced consistently across policy / calibration / KO / PC
    v = policy["version"]
    ok("24_version_consistency", cp.get("policy_version") == v
       and igr.get("policy_version") == v
       and pc.get("ig_resolution", {}).get("policy_version") == v
       and all(p.get("policy_version") == v for p in cp["pairs"] if p.get("fixture_kind") == "normative"))

    # 25 contradictory/ambiguous governed signals fail closed (not a silent pass)
    r_amb = evaluate({"object_a": "KO-X", "route_b": "r", "signals": {
        "evidence_set_overlap": "disjoint", "claim_set_overlap": "high", "source_set_overlap": "partial",
        "relationship_difference": "partial", "module_section_overlap": "partial", "user_task_difference": "partial",
        "textual_similarity": "diagnostic_only"}}, policy)
    ok("25_ambiguous_fail_closed", r_amb["classification"] == "unresolved" and r_amb["route_eligible"] is False)

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all IG governance ratification proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
