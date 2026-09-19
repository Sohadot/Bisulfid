"""
Concept <-> Lexeme semantic validator (sprint concept-lexeme-resolution).

Validates ONLY the new semantic architecture: the lexeme registry and governed
atomic evidence records against the ontology (concepts), languages.json, sources,
and claims. It does NOT read or gate the legacy 14K corpus, routes, release ledger,
sitemaps, robots, or site/public. Not wired into CI.

Rules enforced:
  - every lexeme resolves to exactly one governed concept (ontology term_id);
  - lexeme language is valid in languages.json;
  - concept IDs carry no language semantics (concept_id is a bare ontology term_id);
  - lexeme_id unique, prefixed LEX-; no concept_id == lexeme_id (no cycle/confusion);
  - lexical_relationship_type in the governed vocabulary;
  - a lexeme record carries no route/URL field (lexeme never generates a URL);
  - governed evidence: concept_ids resolve to ontology; lexeme_ids resolve to the
    lexeme registry (free-text forbidden); source_id/claim_id resolve;
  - claim-level rules: concept-level claim cannot be satisfied by terminological
    (lexical) evidence; lexeme-level requires terminological kind + lexeme_ids;
    relationship-level requires a relationship reference;
  - test fixtures are isolated (TEST- ids, not resolved against registries).

Exit 0 = pass, 1 = fail.
"""

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")

ERRORS = []
CHECKS = 0


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        ERRORS.append(msg)


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    print("=== Concept <-> Lexeme semantic validator ===")

    ontology = load(os.path.join(DATA, "ontology", "sulfur_terms.json"))
    all_term_ids = {t["term_id"] for t in ontology["terms"]}

    # Concept eligibility is governed by the sidecar, NOT by mere existence in the ontology.
    roles = load(os.path.join(DATA, "ontology_node_roles.json"))
    valid_roles = set(roles["roles"])
    role_of = {}
    for nr in roles["node_roles"]:
        check(nr["role"] in valid_roles, f"ontology_node_roles: bad role '{nr['role']}' for {nr['term_id']}")
        check(nr["term_id"] in all_term_ids, f"ontology_node_roles: {nr['term_id']} not in ontology")
        role_of[nr["term_id"]] = nr["role"]
    # completeness: every ontology node classified exactly once
    check(set(role_of) == all_term_ids,
          f"ontology_node_roles: must classify every ontology node exactly once (missing {sorted(all_term_ids - set(role_of))})")
    concept_eligible = {tid for tid, r in role_of.items() if r == "concept_eligible"}
    check(len(concept_eligible) == roles.get("concept_eligible_count"),
          "ontology_node_roles: concept_eligible_count mismatch")

    languages = load(os.path.join(DATA, "languages.json"))
    lang_codes = {l["code"] for l in languages["languages"]}

    lexreg = load(os.path.join(DATA, "lexeme_registry.json"))
    valid_rel_types = set(lexreg["lexical_relationship_types"])
    valid_reg_states = set(lexreg["registration_states"])
    forbidden_lex_fields = set(lexreg["lexeme_record_schema"]["forbidden_fields"])

    lex_ids = set()
    for lx in lexreg["lexemes"]:
        lid = lx["lexeme_id"]
        check(lid.startswith("LEX-"), f"lexeme {lid}: id must start LEX-")
        check(lid not in lex_ids, f"lexeme {lid}: duplicate id")
        lex_ids.add(lid)
        # resolves to exactly one CONCEPT-ELIGIBLE node (existence alone is not enough)
        check(lx["concept_id"] in concept_eligible,
              f"lexeme {lid}: concept_id '{lx['concept_id']}' is not concept-eligible (role='{role_of.get(lx['concept_id'], 'UNKNOWN')}')")
        # language valid
        check(lx["language"] in lang_codes, f"lexeme {lid}: language '{lx['language']}' not in languages.json")
        # relationship type governed
        check(lx["lexical_relationship_type"] in valid_rel_types,
              f"lexeme {lid}: bad lexical_relationship_type '{lx['lexical_relationship_type']}'")
        # registration state governed (separate from derived evidence support)
        check(lx.get("registration_state") in valid_reg_states,
              f"lexeme {lid}: bad/missing registration_state")
        # no cycle/confusion
        check(lx["concept_id"] != lid, f"lexeme {lid}: concept_id must differ from lexeme_id")
        # one-fact-one-owner + language!=geography + no URL: lexeme must carry no forbidden field
        # (source_ids/evidence_ids backlinks, geography, route/url fields, legacy 'status').
        leaked = forbidden_lex_fields.intersection(lx.keys())
        check(not leaked, f"lexeme {lid}: carries forbidden field(s) {sorted(leaked)} (backlinks/geography/url/status)")

    # Governed evidence records
    sources = load(os.path.join(DATA, "sources", "source_registry.json"))
    source_ids = {s["source_id"] for s in sources["sources"]}
    # Classification registry ids (for classification-level evidence resolution)
    classification_ids = set()
    cls_path = os.path.join(DATA, "classification_registry.json")
    if os.path.exists(cls_path):
        classification_ids = {c["classification_id"] for c in load(cls_path)["classifications"]}
    claim_ids = set()
    claims_dir = os.path.join(DATA, "claims")
    for name in os.listdir(claims_dir):
        if name.endswith(".json"):
            cj = load(os.path.join(claims_dir, name))
            for c in cj.get("claims", []):
                if isinstance(c, dict) and c.get("claim_id"):
                    claim_ids.add(c["claim_id"])
    # Pilot-scoped (non-operational) claim records live under main/data/pilots/*claims*.json.
    pilots_dir = os.path.join(DATA, "pilots")
    if os.path.isdir(pilots_dir):
        for name in os.listdir(pilots_dir):
            if name.endswith(".json") and "claims" in name.lower():
                cj = load(os.path.join(pilots_dir, name))
                for c in cj.get("claims", []):
                    if isinstance(c, dict) and c.get("claim_id"):
                        claim_ids.add(c["claim_id"])

    ev_dir = os.path.join(DATA, "evidence")
    governed_records = 0
    for name in os.listdir(ev_dir):
        if not (name.endswith(".json") and name.startswith("EVD-")):
            continue
        governed_records += 1
        rec = load(os.path.join(ev_dir, name))
        eid = rec.get("evidence_id", name)
        # concept_ids must resolve to a CONCEPT-ELIGIBLE node (not merely any ontology term)
        for cid in rec.get("concept_ids", []):
            check(cid in concept_eligible,
                  f"evidence {eid}: concept_id '{cid}' is not concept-eligible (role='{role_of.get(cid, 'UNKNOWN')}')")
        # lexeme_ids resolve to registry (free-text forbidden)
        for lxid in rec.get("lexeme_ids", []) or []:
            check(lxid in lex_ids, f"evidence {eid}: lexeme_id '{lxid}' not a governed lexeme (free-text forbidden)")
        # source_id / claim_id resolve
        check(rec.get("source_id") in source_ids, f"evidence {eid}: source_id does not resolve")
        if rec.get("claim_id"):
            check(rec["claim_id"] in claim_ids, f"evidence {eid}: claim_id does not resolve")
        # claim-level rules
        level = rec.get("claim_level")
        kind = rec.get("evidence_kind")
        if level == "concept":
            check(kind in ("scientific", "quantitative", "legal_regulatory"),
                  f"evidence {eid}: concept-level claim cannot be satisfied by '{kind}' (lexical) evidence")
        elif level == "lexeme":
            check(kind == "terminological", f"evidence {eid}: lexeme-level requires terminological evidence_kind")
            check(bool(rec.get("lexeme_ids")), f"evidence {eid}: lexeme-level requires non-empty lexeme_ids")
        elif level == "relationship":
            check(rec.get("relationship"), f"evidence {eid}: relationship-level requires a relationship reference")
        elif level == "classification":
            check(kind == "classification", f"evidence {eid}: classification-level requires classification evidence_kind")
            check(bool(rec.get("classification_ids")), f"evidence {eid}: classification-level requires non-empty classification_ids")
            for clsid in rec.get("classification_ids", []) or []:
                check(clsid in classification_ids,
                      f"evidence {eid}: classification_id '{clsid}' does not resolve to classification_registry")
        else:
            check(False, f"evidence {eid}: invalid claim_level '{level}'")

    # Test-fixture isolation: fixtures must not leak into governed space.
    fx_dir = os.path.join(ev_dir, "fixtures")
    if os.path.isdir(fx_dir):
        for name in os.listdir(fx_dir):
            if name.endswith(".json"):
                rec = load(os.path.join(fx_dir, name))
                check(rec.get("evidence_id", "").startswith("TEST-EVD-"), f"fixture {name}: must be TEST-EVD-")
                check(rec.get("governed") is False, f"fixture {name}: must be non-governed")
                for lxid in rec.get("lexeme_ids", []) or []:
                    check(lxid.startswith("TEST-LEX-"), f"fixture {name}: fixture lexeme id must be synthetic TEST-LEX-")

    print(f"    (ran {CHECKS} checks; {len(lex_ids)} lexeme(s), {governed_records} governed evidence record(s))")
    print("=" * 56)
    if ERRORS:
        print(f"RESULT: FAIL ({len(ERRORS)} error(s))")
        for e in ERRORS:
            print(f"  - {e}")
        return 1
    print("RESULT: PASS — concept/lexeme semantic architecture valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
