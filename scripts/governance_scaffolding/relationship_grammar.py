"""
Relationship grammar — typed subject -> predicate -> object validation.

Sprint: semantic-integrity-hardening. Pure; validates the DIRECTION and endpoint
types of a relationship instance against the class endpoint contracts in
main/data/relationship_class_registry.json. No instances are stored this sprint;
this is the grammar future facts must obey. Not wired to CI.
"""

import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")


def load_registry():
    with open(os.path.join(DATA, "relationship_class_registry.json"), encoding="utf-8") as fh:
        return json.load(fh)


def build_contracts(registry):
    """class_id -> {subject_types:set, object_types:set}."""
    return {
        c["relationship_class_id"]: {
            "subject_types": set(c["subject_types"]),
            "object_types": set(c["object_types"]),
        }
        for c in registry["relationship_classes"]
    }


def validate_instance(inst, registry):
    """Return a list of errors for a relationship instance dict. Empty list = valid.

    Enforces: known class; subject_type in class.subject_types; object_type in
    class.object_types; endpoint types drawn from the controlled endpoint_types;
    evidence_ids non-empty when evidence_qualified. Directionality is enforced
    structurally: a reversed instance (e.g. concept as subject of REL-IMPORTER)
    fails because 'concept' is not an allowed subject_type for that class.
    """
    errors = []
    contracts = build_contracts(registry)
    endpoint_types = set(registry["endpoint_types"])
    cid = inst.get("relationship_class_id")
    if cid not in contracts:
        return [f"unknown relationship_class_id '{cid}'"]
    c = contracts[cid]
    st, ot = inst.get("subject_type"), inst.get("object_type")
    if st not in endpoint_types:
        errors.append(f"{cid}: subject_type '{st}' not a controlled endpoint type")
    if ot not in endpoint_types:
        errors.append(f"{cid}: object_type '{ot}' not a controlled endpoint type")
    if st not in c["subject_types"]:
        errors.append(f"{cid}: subject_type '{st}' not allowed (expected {sorted(c['subject_types'])}) — check proposition direction")
    if ot not in c["object_types"]:
        errors.append(f"{cid}: object_type '{ot}' not allowed (expected {sorted(c['object_types'])}) — check proposition direction")
    if inst.get("qualification_state") == "evidence_qualified" and not inst.get("evidence_ids"):
        errors.append(f"{cid}: evidence_qualified requires non-empty evidence_ids")
    return errors
