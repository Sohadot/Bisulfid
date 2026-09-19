"""
Deterministic source admissibility (source-qualification-evidence-admission sprint).

admissible(context) -> (bool, reason). Reads:
  - main/data/sources/source_registry.json      (source -> category; identity)
  - main/data/source_use_qualification_registry.json  (use-scoped qualification)
  - main/data/source_admissibility_policy.json  (roles, category roles, domain matrix, hard rules)

Pure w.r.t. governance state: reads only, changes nothing, wired to nothing.
Source category ALONE never returns admissible. Admissibility never implies claim
approval, claim-registry activation, route publication, or indexation.
"""

import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")


def _load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as fh:
        return json.load(fh)


def load_all():
    reg = _load("sources", "source_registry.json")
    qual = _load("source_use_qualification_registry.json")
    pol = _load("source_admissibility_policy.json")
    return {
        "category_by_source": {s["source_id"]: s.get("category") for s in reg["sources"]},
        "qual_by_id": {q["qualification_id"]: q for q in qual["qualifications"]},
        "category_roles": pol["category_default_roles"],
        "domains": pol["domain_admissibility"],
        "policy": pol,
    }


def _domain_rule(domains_policy, subject_domain):
    for rule in domains_policy.values():
        if subject_domain in rule.get("applies_to_domains", []):
            return rule
    return None


def admissible(context, data=None):
    """context: {source_id, qualification_id, subject_domain, evidence_kind,
    claim_level, intended_use?, geography?, jurisdiction?, temporal_scope?}.
    Returns (bool, reason)."""
    d = data or load_all()
    sid = context.get("source_id")
    qid = context.get("qualification_id")

    if sid not in d["category_by_source"]:
        return (False, f"unknown source_id '{sid}'")
    category = d["category_by_source"][sid]

    # HARD RULE: category alone is never enough — a covering qualification is required.
    if not qid:
        return (False, "source category alone is not admissible: no source-use qualification supplied")
    q = d["qual_by_id"].get(qid)
    if q is None:
        return (False, f"unknown qualification '{qid}'")
    # qualification must reference exactly this source
    if q["source_id"] != sid:
        return (False, f"qualification '{qid}' does not reference source '{sid}'")

    # qualification state must currently admit
    if q["qualification_state"] not in ("qualified", "qualified_narrow"):
        return (False, f"qualification state '{q['qualification_state']}' is not admissible")

    # prohibited use always vetoes
    intended = context.get("intended_use")
    if intended and intended in q.get("prohibited_uses", []):
        return (False, f"intended_use '{intended}' is in qualification prohibited_uses (veto)")

    # scope cannot be silently broadened: domain / evidence_kind / claim_level must be permitted
    sd = context.get("subject_domain")
    if sd not in q.get("applicable_subject_domains", []):
        return (False, f"subject_domain '{sd}' outside qualification scope {q.get('applicable_subject_domains')}")
    if context.get("evidence_kind") not in q.get("permitted_evidence_kinds", []):
        return (False, f"evidence_kind '{context.get('evidence_kind')}' not permitted by qualification")
    cl = context.get("claim_level")
    if cl not in q.get("permitted_claim_levels", []):
        return (False, f"claim_level '{cl}' not permitted by qualification")

    # domain admissibility: category must be able to play a required role and not be excluded
    rule = _domain_rule(d["domains"], sd)
    if rule is None:
        return (False, f"no domain admissibility rule for subject_domain '{sd}'")
    if cl not in rule.get("claim_levels", []):
        return (False, f"claim_level '{cl}' not admissible for domain '{sd}' (allowed {rule.get('claim_levels')})")
    cat_roles = set(d["category_roles"].get(category, []))
    # explicit exclusions
    if category in rule.get("forbidden_alone_categories", []):
        return (False, f"category '{category}' cannot alone establish a {sd} {cl}-level claim")
    if category in rule.get("contextual_only_categories", []):
        return (False, f"category '{category}' is contextual-only for {sd}; cannot alone establish the relationship")
    # current-law special rule
    req_cat = rule.get("current_law_requires_category")
    if req_cat and category not in req_cat:
        return (False, f"current-law/regulation claim requires an official instrument category {req_cat}, not '{category}'")
    # required role
    required_roles = set(rule.get("required_any_role", []))
    if required_roles and not (cat_roles & required_roles):
        return (False, f"category '{category}' (roles {sorted(cat_roles)}) lacks a required role {sorted(required_roles)} for {sd}/{cl}")

    return (True, f"admissible: source '{sid}' via qualification '{qid}' for {sd}/{cl}/{context.get('evidence_kind')} "
                  f"(does NOT imply claim approval, activation, or publication)")
