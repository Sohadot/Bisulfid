"""
Validator for the governance-scaffolding artifacts created in
sprint authority-dimension-impl-1.

Scope: validates ONLY the NEW architecture artifacts this sprint introduced.
It does NOT read or validate the legacy 14K corpus, routes.json, release_ledger,
sources, claims, ontology, sitemaps, robots, or site/public. It is NOT wired into
the CI workflow and produces no hard-fail against pre-existing production files.

Checks (per BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md IP-5/IP-6/IP-11/IP-16):
  - registries parse; IDs unique; enum values valid;
  - subject_domain: no domain marked evidence_active this sprint;
  - geography: records carry NO relationship/evidence-status field;
  - relationship_class: no relationship instances this sprint;
  - jurisdiction: no active instruments this sprint;
  - evidence schema forbids source_type / editable used_by / confidence;
  - production evidence IDs start EVD-; fixtures start TEST-EVD- and are non-governed;
  - no real (governed) evidence record exists;
  - information_gain calibration is empty and defines the five labels; no threshold.

Exit code 0 = all pass, 1 = any failure.
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


def validate_subject_domain():
    d = load(os.path.join(DATA, "subject_domain_registry.json"))
    ids = [x["subject_domain_id"] for x in d["subject_domains"]]
    check(len(ids) == len(set(ids)), "subject_domain: duplicate IDs")
    for x in d["subject_domains"]:
        check(x["state"] in d["domain_states"], f"subject_domain: bad state {x.get('subject_domain_id')}")
        check(x["state"] != "evidence_active", f"subject_domain: {x['subject_domain_id']} must not be evidence_active this sprint")
        check(x["subject_domain_id"].startswith("SD-"), f"subject_domain: bad id prefix {x['subject_domain_id']}")


def validate_geography():
    d = load(os.path.join(DATA, "geography_registry.json"))
    ids = [x["geo_id"] for x in d["geographies"]]
    check(len(ids) == len(set(ids)), "geography: duplicate IDs")
    forbidden = set(d.get("forbidden_geography_fields", []))
    for x in d["geographies"]:
        check(x["geo_id"].startswith("GEO-"), f"geography: bad id prefix {x['geo_id']}")
        leaked = forbidden.intersection(x.keys())
        check(not leaked, f"geography: {x['geo_id']} carries forbidden relationship/evidence field(s): {sorted(leaked)}")
    # GCC/Gulf naming must be unambiguous (concept-lexeme-resolution correction).
    check("GEO-GCC" in ids, "geography: GEO-GCC (GCC member states) must exist")
    check("GEO-GULF" not in ids, "geography: ambiguous GEO-GULF must be renamed to GEO-GCC")


def validate_jurisdiction():
    d = load(os.path.join(DATA, "jurisdiction_registry.json"))
    check(d.get("jurisdictions") == [], "jurisdiction: no jurisdictions may be seeded this sprint")
    check(d.get("authorities") == [], "jurisdiction: no authorities may be seeded this sprint")
    check(d.get("instruments") == [], "jurisdiction: no active instruments this sprint")
    # Roles must not overlap: jurisdiction record must NOT carry 'authority'.
    jreq = set(d.get("jurisdiction_record_schema", {}).get("required_fields", []))
    check("authority" not in jreq, "jurisdiction: jurisdiction record must not include 'authority' (role overlap)")
    check("authority_record_schema" in d, "jurisdiction: authority_record_schema missing")
    check("instrument_record_schema" in d, "jurisdiction: instrument_record_schema missing")
    ireq = set(d.get("instrument_record_schema", {}).get("required_fields", []))
    check({"jurisdiction_id", "authority_id"}.issubset(ireq),
          "jurisdiction: instrument must reference both jurisdiction_id and authority_id")


def validate_relationship_classes():
    d = load(os.path.join(DATA, "relationship_class_registry.json"))
    ids = [x["relationship_class_id"] for x in d["relationship_classes"]]
    check(len(ids) == len(set(ids)), "relationship_class: duplicate IDs")
    # Relationship instances are permitted from Pilot 01 onward; each must obey the typed
    # subject->predicate->object grammar and carry evidence references.
    import importlib
    rg = importlib.import_module("relationship_grammar")
    class_ids = {x["relationship_class_id"] for x in d["relationship_classes"]}
    valid_qstates = set(d["instance_qualification_states"])
    for inst in d.get("relationship_instances", []):
        rid = inst.get("relationship_instance_id", "?")
        errs = rg.validate_instance(inst, d)
        check(not errs, f"relationship instance {rid}: grammar errors {errs}")
        check(inst.get("relationship_class_id") in class_ids, f"relationship instance {rid}: unknown class")
        check(inst.get("qualification_state") in valid_qstates, f"relationship instance {rid}: bad qualification_state")
        check(bool(inst.get("evidence_ids")), f"relationship instance {rid}: must carry evidence_ids")
        check(isinstance(inst.get("temporal_scope"), dict), f"relationship instance {rid}: temporal_scope required (not timeless)")
        # evidence_qualified requires non-empty evidence (grammar checks this too)
        if inst.get("qualification_state") == "evidence_qualified":
            check(bool(inst.get("evidence_ids")), f"relationship instance {rid}: evidence_qualified needs evidence")
    for x in d["relationship_classes"]:
        check(x["relationship_class_id"].startswith("REL-"), f"relationship_class: bad id prefix {x['relationship_class_id']}")
        check(x["state"] == "registered", f"relationship_class: {x['relationship_class_id']} must be 'registered'")
    # Trade/economic classes must require PRIMARY authoritative evidence, not market/industry pubs alone.
    check("proposed_source_categories" in d, "relationship_class: proposed_source_categories (source-taxonomy gap) missing")
    by_id = {x["relationship_class_id"]: x for x in d["relationship_classes"]}
    for rid in ("REL-IMPORTER", "REL-EXPORTER", "REL-PRODUCER", "REL-INDUSTRIAL-USER"):
        rc = by_id.get(rid, {})
        prim = set(rc.get("primary_evidence_required", []))
        check(prim and not prim.issubset({"market_report", "industry_publication"}),
              f"relationship_class: {rid} must require a primary authoritative source category")
    # Typed subject/predicate/object grammar: endpoint contracts must be well-formed.
    endpoint_types = set(d.get("endpoint_types", []))
    check(endpoint_types, "relationship_class: endpoint_types vocabulary missing")
    for x in d["relationship_classes"]:
        rid = x["relationship_class_id"]
        st = set(x.get("subject_types", []))
        ot = set(x.get("object_types", []))
        check(st and st.issubset(endpoint_types), f"relationship_class: {rid} subject_types must be non-empty and drawn from endpoint_types")
        check(ot and ot.issubset(endpoint_types), f"relationship_class: {rid} object_types must be non-empty and drawn from endpoint_types")
    ischema = set(d.get("relationship_instance_schema", {}).get("required_fields", []))
    check({"subject_ref", "subject_type", "object_ref", "object_type"}.issubset(ischema),
          "relationship_class: instance schema must use typed subject/object endpoints")


def validate_evidence():
    schema = load(os.path.join(DATA, "evidence", "evidence_schema.json"))
    forbidden = set(schema["forbidden_fields"].keys())
    check(forbidden == {"source_type", "used_by", "confidence", "entities", "risk_class"},
          f"evidence: forbidden_fields must be source_type/used_by/confidence/entities/risk_class, got {sorted(forbidden)}")
    # required fields use concept_ids (not generic 'entities') and carry no risk_class.
    req = set(schema["fields"]["required_all_kinds"])
    check("concept_ids" in req and "claim_level" in req, "evidence: schema must require concept_ids and claim_level")
    check("entities" not in req and "risk_class" not in req, "evidence: schema must NOT require entities or risk_class")

    ev_dir = os.path.join(DATA, "evidence")
    # Governed evidence records (EVD-*.json) are now permitted; structural + forbidden-field checks here,
    # cross-registry resolution + claim-level rules in validate_concept_lexeme.py.
    for name in os.listdir(ev_dir):
        if name.endswith(".json") and name.startswith("EVD-"):
            rec = load(os.path.join(ev_dir, name))
            check(rec.get("governed") is True, f"evidence {name}: governed record must set governed=true")
            leaked = forbidden.intersection(rec.keys())
            check(not leaked, f"evidence {name}: contains forbidden field(s) {sorted(leaked)}")
            for f in req:
                check(f in rec, f"evidence {name}: missing required field '{f}'")
            # Numeric-normalization law: source_literal vs normalized_value must be consistent
            # (catches locale thousands-separators used as naive floats).
            import importlib
            nn = importlib.import_module("numeric_normalization")
            nerrs = nn.validate_evidence_numbers(rec)
            check(not nerrs, f"evidence {name}: numeric normalization errors {nerrs}")
    # Fixtures: must be test-only, synthetic, non-governed, and carry no forbidden fields.
    fx_dir = os.path.join(ev_dir, "fixtures")
    if os.path.isdir(fx_dir):
        for name in os.listdir(fx_dir):
            if not name.endswith(".json"):
                continue
            rec = load(os.path.join(fx_dir, name))
            check(rec.get("evidence_id", "").startswith("TEST-EVD-"),
                  f"evidence fixture {name}: id must start TEST-EVD-")
            check(rec.get("governed") is False, f"evidence fixture {name}: governed must be false")
            check(rec.get("test_fixture") is True, f"evidence fixture {name}: test_fixture must be true")
            check(rec.get("source_id", "").startswith("TEST-"),
                  f"evidence fixture {name}: must reference a synthetic TEST- source_id")
            leaked = forbidden.intersection(rec.keys())
            check(not leaked, f"evidence fixture {name}: contains forbidden field(s) {sorted(leaked)}")


def _keys_recursive(obj):
    """Yield every mapping key anywhere in a nested JSON structure."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k
            yield from _keys_recursive(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _keys_recursive(v)


def validate_information_gain():
    d = load(os.path.join(DATA, "information_gain", "calibration_pairs.json"))
    check(d.get("pairs") == [], "information_gain: pairs must be empty this sprint")
    check(set(d.get("labels", [])) == {
        "true_duplicate", "near_duplicate", "valid_sibling",
        "valid_localization", "valid_domain_specific_reference"
    }, "information_gain: five canonical labels required")
    # No threshold may be *defined* (as a key/field). The word may appear in prose rules
    # (which explicitly state none is defined), so inspect KEYS, not serialized text.
    bad_keys = [k for k in _keys_recursive(d) if "threshold" in k.lower() or "weight" in k.lower()]
    check(not bad_keys, f"information_gain: no threshold/weight field may be defined this sprint (found keys {bad_keys})")


def validate_source_qualification():
    reg = load(os.path.join(DATA, "sources", "source_registry.json"))
    source_ids = {s["source_id"] for s in reg["sources"]}
    revision_of = {s["source_id"]: s.get("identity_revision") for s in reg["sources"]}
    registry_categories = set(reg["source_categories"])
    q = load(os.path.join(DATA, "source_use_qualification_registry.json"))
    valid_states = set(q["qualification_states"].keys())
    forbidden = set(q["qualification_record_schema"]["forbidden_fields"])
    seen = set()
    for x in q["qualifications"]:
        qid = x["qualification_id"]
        check(qid.startswith("QUAL-"), f"qualification {qid}: bad id prefix")
        check(qid not in seen, f"qualification {qid}: duplicate id")
        seen.add(qid)
        # references exactly one registered source
        check(isinstance(x.get("source_id"), str) and x["source_id"] in source_ids,
              f"qualification {qid}: source_id must reference exactly one registered source")
        # no bibliographic duplication (incl. source_edition)
        leaked = forbidden.intersection(x.keys())
        check(not leaked, f"qualification {qid}: duplicates bibliographic field(s) {sorted(leaked)}")
        # source revision ownership: qualification references the source's identity_revision, not bibliographic strings
        qrev = x.get("qualified_against_source_revision")
        check(qrev is not None, f"qualification {qid}: missing qualified_against_source_revision")
        check(qrev == revision_of.get(x.get("source_id")),
              f"qualification {qid}: revision '{qrev}' != source identity_revision '{revision_of.get(x.get('source_id'))}'")
        # valid state; none implies publication
        check(x.get("qualification_state") in valid_states, f"qualification {qid}: bad state")
        check("route_publication" in x.get("prohibited_uses", []) or x.get("qualification_state") in ("candidate", "reviewed"),
              f"qualification {qid}: admissible qualification must explicitly prohibit route_publication")

    pol = load(os.path.join(DATA, "source_admissibility_policy.json"))
    check("source_category_alone_never_admissible" in pol["hard_rules"], "policy: missing category-alone hard rule")
    check("prohibited_use_always_vetoes" in pol["hard_rules"], "policy: missing prohibited-use veto rule")
    # every ratified category has default roles
    newly = {c["category"] for c in pol["ratified_source_categories"]["newly_ratified"]}
    ratified = set(pol["ratified_source_categories"]["existing_confirmed"]) | newly
    for c in ratified:
        check(c in pol["category_default_roles"], f"policy: category '{c}' missing default roles")
    # NO DRIFT: policy-ratified categories must all exist in the source-registry vocabulary, and vice versa.
    check(ratified == registry_categories,
          f"policy/source-registry category drift: policy_only={sorted(ratified - registry_categories)} registry_only={sorted(registry_categories - ratified)}")

    ep = load(os.path.join(DATA, "evidence_admission_policy.json"))
    ev = ep["evidence_review_lifecycle"]["evidence_verified"]
    check(ev.get("admits") is True, "evidence policy: evidence_verified must admit")
    check("route_publication" in ev.get("must_not_imply", []), "evidence policy: verified must not imply publication")
    check(ep["regression_rules"]["monotonic_direction"] == "regression_never_raises_privilege",
          "evidence policy: regression must never raise privilege")

    cl = load(os.path.join(DATA, "claim_activation_policy.json"))
    check(cl["this_sprint"].startswith("No registry activated"), "claim policy: nothing may be activated this sprint")


def validate_classification():
    path = os.path.join(DATA, "classification_registry.json")
    if not os.path.exists(path):
        return
    reg = load(os.path.join(DATA, "sources", "source_registry.json"))
    source_ids = {s["source_id"] for s in reg["sources"]}
    # Classification evidence records: one-fact-one-owner means the SOURCE binding lives here,
    # and a classification object references it via supporting_evidence_ids (never source_id).
    ev_dir = os.path.join(DATA, "evidence")
    class_evidence = {}
    for name in os.listdir(ev_dir):
        if name.endswith(".json") and name.startswith("EVD-"):
            rec = load(os.path.join(ev_dir, name))
            class_evidence[rec.get("evidence_id", name)] = rec
    d = load(path)
    req = set(d["record_schema"]["required_fields"])
    forbidden = set(d["record_schema"]["forbidden_fields"])
    seen = set()
    for c in d["classifications"]:
        cid = c["classification_id"]
        check(cid.startswith("CLS-"), f"classification {cid}: bad id prefix")
        check(cid not in seen, f"classification {cid}: duplicate id")
        seen.add(cid)
        for f in req:
            check(f in c, f"classification {cid}: missing required field '{f}'")
        leaked = forbidden.intersection(c.keys())
        check(not leaked, f"classification {cid}: forbidden field(s) present {sorted(leaked)}")
        # one-fact-one-owner: no direct source_id on a classification object
        check("source_id" not in c, f"classification {cid}: must not carry source_id (use supporting_evidence_ids -> evidence)")
        # supporting_evidence_ids must be a list; each entry resolves to a classification-kind evidence
        # record whose own source_id resolves. An EMPTY list is allowed (identity unproven/blocked).
        sev = c.get("supporting_evidence_ids", [])
        check(isinstance(sev, list), f"classification {cid}: supporting_evidence_ids must be a list")
        for eid in sev if isinstance(sev, list) else []:
            ev = class_evidence.get(eid)
            check(ev is not None, f"classification {cid}: supporting evidence '{eid}' not found")
            if ev is not None:
                check(ev.get("evidence_kind") == "classification",
                      f"classification {cid}: supporting evidence '{eid}' must be classification-kind")
                check(ev.get("source_id") in source_ids,
                      f"classification {cid}: supporting evidence '{eid}' source_id does not resolve")
                check(cid in (ev.get("classification_ids") or []),
                      f"classification {cid}: supporting evidence '{eid}' must reference this classification back in classification_ids")
        # HS6 and national code must be distinct fields, never conflated
        if "hs6" in c and "national_code" in c:
            check("hs6" in c and "national_code" in c, f"classification {cid}: hs6/national_code must be separate")
        # A statistical product grouping must not silently carry an HS code as its own code
        if c.get("object_type") == "statistical_product_grouping":
            check(c.get("code") is None, f"classification {cid}: statistical grouping must not assert a single HS code as its own")


def main():
    print("=== Governance scaffolding validator (new artifacts only) ===")
    validate_subject_domain()
    validate_geography()
    validate_jurisdiction()
    validate_relationship_classes()
    validate_evidence()
    validate_information_gain()
    validate_source_qualification()
    validate_classification()
    print(f"    (ran {CHECKS} checks)")
    print("=" * 56)
    if ERRORS:
        print(f"RESULT: FAIL ({len(ERRORS)} error(s))")
        for e in ERRORS:
            print(f"  - {e}")
        return 1
    print("RESULT: PASS — all scaffolding artifacts valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
