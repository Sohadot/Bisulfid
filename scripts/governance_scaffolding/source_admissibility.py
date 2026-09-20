"""
Deterministic source admissibility + evidence-posture derivation
(source-qualification-evidence-admission -> admission-enforcement-closure).

Pure, read-only, unwired from deploy/CI. Enforces every input the API advertises:
allowed_uses (allowlist), prohibited_uses (veto), allowed_categories, evidence_role,
geography_limitation, jurisdiction_limitation, temporal_boundary, source revision,
plus domain rules. Category ALONE never admits. Admissibility never implies claim
approval, activation, publication, or indexation.

Also derives evidence_posture (evidence_collecting|evidence_sufficient|evidence_locked)
and evaluates sufficiency patterns, so Contract C's evidence input is governed, not
manually asserted.
"""

import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")

GOVERNED_EVIDENCE_ROLES = {
    "primary_authoritative", "official_record", "primary_scientific",
    "secondary_scholarly", "corroborating", "contextual", "historical",
    # authoritative_database: a curated authoritative DATABASE record faithfully
    # representing an originating scientific work's structured data (e.g. a
    # crystallographic-database CIF). Distinct from primary_scientific (the primary
    # study itself). Scientific INDEPENDENCE is judged by originating_work lineage.
    "authoritative_database",
}
ADMITTING_QUAL_STATES = {"qualified", "qualified_narrow"}


def _load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as fh:
        return json.load(fh)


def load_all():
    reg = _load("sources", "source_registry.json")
    qual = _load("source_use_qualification_registry.json")
    pol = _load("source_admissibility_policy.json")
    # Originating-work lineage (retrieval artifact != originating scientific work).
    work_reg_path = os.path.join(DATA, "originating_work_registry.json")
    related = {}
    if os.path.exists(work_reg_path):
        wr = _load("originating_work_registry.json")
        for w in wr.get("works", []):
            related[w["work_id"]] = set(w.get("related_work_ids", []) or [])
    return {
        "source_by_id": {s["source_id"]: s for s in reg["sources"]},
        "category_by_source": {s["source_id"]: s.get("category") for s in reg["sources"]},
        "revision_by_source": {s["source_id"]: s.get("identity_revision") for s in reg["sources"]},
        "work_by_source": {s["source_id"]: s.get("originating_work_id") for s in reg["sources"]},
        "related_works": related,
        # Governed corporate ISSUER lineage and statistical/trade DATASET lineage
        # (explicit fields only — never inferred from names/URLs).
        "issuer_by_source": {s["source_id"]: s.get("issuer_id") for s in reg["sources"]},
        "dataset_by_source": {s["source_id"]: (s.get("dataset_id") or s.get("underlying_study_id")) for s in reg["sources"]},
        "qual_by_id": {q["qualification_id"]: q for q in qual["qualifications"]},
        "category_roles": pol["category_default_roles"],
        "domains": pol["domain_admissibility"],
        "policy": pol,
    }


# Governed mapping of subject_domain -> independence domain. Used for admission-unit
# metadata; the actual independence test is key-based (see _independent), so only the
# lineage keys that a domain populates ever match.
_SCIENCE_DOMAINS = {"SD-CHEMISTRY", "SD-INORGANIC-CHEMISTRY", "SD-MATERIALS-SCIENCE",
                    "SD-PHYSICS", "SD-BIOLOGY", "SD-BIOMEDICAL", "SD-NOMENCLATURE"}
_CORPORATE_DOMAINS = {"SD-CORPORATE-FINANCIALS", "SD-INDUSTRIAL"}
_TRADE_DOMAINS = {"SD-TRADE", "SD-ECONOMICS", "SD-CUSTOMS-CLASSIFICATION"}


def _independence_domain(subject_domain):
    if subject_domain in _SCIENCE_DOMAINS:
        return "science"
    if subject_domain in _CORPORATE_DOMAINS:
        return "corporate"
    if subject_domain in _TRADE_DOMAINS:
        return "trade_statistical"
    return "other"


def _domain_rule(domains_policy, subject_domain):
    for rule in domains_policy.values():
        if subject_domain in rule.get("applies_to_domains", []):
            return rule
    return None


def admissible(context, data=None):
    """Return (bool, reason). Deny-by-default; every advertised input is enforced."""
    d = data or load_all()
    sid = context.get("source_id")
    qid = context.get("qualification_id")

    if sid not in d["category_by_source"]:
        return (False, f"unknown source_id '{sid}'")
    category = d["category_by_source"][sid]

    # (11) category alone never admits: a covering qualification is mandatory.
    if not qid:
        return (False, "source category alone is not admissible: no source-use qualification supplied")
    q = d["qual_by_id"].get(qid)
    if q is None:
        return (False, f"unknown qualification '{qid}'")
    if q["source_id"] != sid:
        return (False, f"qualification '{qid}' does not reference source '{sid}'")
    if q["qualification_state"] not in ADMITTING_QUAL_STATES:
        return (False, f"qualification state '{q['qualification_state']}' is not admissible")

    # (10) source revision must match what was qualified (else review-required).
    q_rev = q.get("qualified_against_source_revision")
    s_rev = d["revision_by_source"].get(sid)
    if q_rev is not None:
        if s_rev is None:
            return (False, f"source '{sid}' has no identity_revision but qualification expects '{q_rev}' (review-required)")
        if s_rev != q_rev:
            return (False, f"source revision mismatch: source '{s_rev}' != qualified '{q_rev}' (review-required)")

    # (1/2) intended_use: allowlist first, then veto.
    intended = context.get("intended_use")
    if not intended:
        return (False, "intended_use must be explicit for a scoped qualification (deny by default)")
    if intended in q.get("prohibited_uses", []):
        return (False, f"intended_use '{intended}' is in qualification prohibited_uses (veto)")
    if intended not in q.get("allowed_uses", []):
        return (False, f"intended_use '{intended}' not in qualification allowed_uses (deny by default)")

    # scope cannot broaden
    sd = context.get("subject_domain")
    if sd not in q.get("applicable_subject_domains", []):
        return (False, f"subject_domain '{sd}' outside qualification scope {q.get('applicable_subject_domains')}")
    if context.get("evidence_kind") not in q.get("permitted_evidence_kinds", []):
        return (False, f"evidence_kind '{context.get('evidence_kind')}' not permitted by qualification")
    cl = context.get("claim_level")
    if cl not in q.get("permitted_claim_levels", []):
        return (False, f"claim_level '{cl}' not permitted by qualification")

    # (3) evidence_role: declared, governed, permitted by qualification, offered by category.
    role = context.get("evidence_role")
    if not role:
        return (False, "evidence_role must be declared by the evidence assertion")
    if role not in GOVERNED_EVIDENCE_ROLES:
        return (False, f"evidence_role '{role}' not in governed vocabulary")
    if role not in q.get("evidence_roles", []):
        return (False, f"evidence_role '{role}' not permitted by qualification {qid}")
    cat_roles = set(d["category_roles"].get(category, []))
    if role not in cat_roles:
        return (False, f"evidence_role '{role}' incompatible with source category '{category}' roles {sorted(cat_roles)}")

    # domain rule
    rule = _domain_rule(d["domains"], sd)
    if rule is None:
        return (False, f"no domain admissibility rule for subject_domain '{sd}'")
    if cl not in rule.get("claim_levels", []):
        return (False, f"claim_level '{cl}' not admissible for domain '{sd}'")

    # (13) current-law legal context: only a governing instrument establishes current law.
    legal_ctx = context.get("legal_context")
    req_cat = rule.get("current_law_requires_category")
    if req_cat:
        if legal_ctx == "current_law" and category not in req_cat:
            return (False, f"current-law claim requires official instrument category {req_cat}, not '{category}'")

    # (2) allowed_categories allowlist for the domain (role compatibility is additional, not a substitute).
    allowed_cats = rule.get("allowed_categories")
    if allowed_cats is not None and category not in allowed_cats:
        return (False, f"category '{category}' not in domain '{sd}' allowed_categories {allowed_cats}")
    if category in rule.get("forbidden_alone_categories", []):
        return (False, f"category '{category}' cannot alone establish a {sd} {cl}-level claim")
    if category in rule.get("contextual_only_categories", []):
        return (False, f"category '{category}' is contextual-only for {sd}; cannot alone establish the relationship")

    # role must satisfy domain required role
    required_roles = set(rule.get("required_any_role", []))
    if required_roles and role not in required_roles:
        return (False, f"evidence_role '{role}' does not satisfy domain '{sd}' required roles {sorted(required_roles)}")

    # (4) geography enforcement
    geo = context.get("geography")
    if geo:
        gl = q.get("geography_limitation")
        if not gl:
            return (False, f"context asserts geography '{geo}' but qualification grants no geography (language != geography)")
        allowed_geo = gl if isinstance(gl, list) else [gl]
        if geo not in allowed_geo:
            return (False, f"geography '{geo}' outside qualification geography_limitation {allowed_geo}")

    # (5) jurisdiction enforcement
    jur = context.get("jurisdiction")
    if jur:
        jl = q.get("jurisdiction_limitation")
        if not jl:
            return (False, f"context asserts jurisdiction '{jur}' but qualification grants no jurisdiction")
        allowed_jur = jl if isinstance(jl, list) else [jl]
        if jur not in allowed_jur:
            return (False, f"jurisdiction '{jur}' outside qualification jurisdiction_limitation {allowed_jur}")

    # (6) temporal boundary enforcement
    tb = q.get("temporal_boundary")
    if tb:
        as_of = (context.get("temporal_scope") or {}).get("as_of")
        claims_current = context.get("claims_current", False)
        historical = context.get("historical_evidence", False)
        if claims_current and not historical:
            return (False, "qualification is time-bounded; a current-state claim from a bounded source needs historical_evidence=True")
        vf, vt = tb.get("valid_from"), tb.get("valid_to")
        if as_of is not None and vf is not None and as_of < vf:
            return (False, f"temporal: as_of {as_of} before qualification valid_from {vf}")
        if as_of is not None and vt is not None and as_of > vt:
            return (False, f"temporal: as_of {as_of} after qualification valid_to {vt}")

    return (True, f"admissible: '{sid}' via '{qid}' role={role} for {sd}/{cl}/{context.get('evidence_kind')} "
                  f"(does NOT imply claim approval, activation, or publication)")


# ---------------------------------------------------------------------------
# Sufficiency evaluator + evidence-posture derivation (governed, pure).
# ---------------------------------------------------------------------------

def _independent(u1, u2):
    """Domain-SEMANTIC independence (not URL/publisher-semantic). Two evidence units are
    NOT independent when they share a governed lineage key:
      - same registered source_id (always);
      - SCIENCE: same or conservatively-related originating_work_id (retrieval artifact !=
        originating work; a database copy and the article of the same work are ONE lineage);
      - CORPORATE: same issuer_id (e.g. two OCP reports -> ORG-OCP-GROUP);
      - STATISTICAL/TRADE: same governed dataset_id / underlying_study_id (release lineage).
    Journal/publisher equality is DELIBERATELY NOT an independence key: two distinct
    scientific works from the same journal can be independent. Lineage is never inferred
    from organization names or URL strings — only explicit governed ids are compared."""
    # same registered source is never independent
    if u1.get("source_id") is not None and u1.get("source_id") == u2.get("source_id"):
        return False
    # SCIENCE: originating-work lineage (+ conservative related works)
    w1, w2 = u1.get("originating_work_id"), u2.get("originating_work_id")
    if w1 is not None and w2 is not None:
        if w1 == w2:
            return False
        if w2 in set(u1.get("related_work_ids") or []) or w1 in set(u2.get("related_work_ids") or []):
            return False
    # CORPORATE: issuer lineage
    i1, i2 = u1.get("issuer_id"), u2.get("issuer_id")
    if i1 is not None and i2 is not None and i1 == i2:
        return False
    # STATISTICAL/TRADE: governed dataset / study lineage
    for key in ("dataset_id", "underlying_study_id"):
        a, b = u1.get(key), u2.get(key)
        if a is not None and a == b:
            return False
    return True


def _has_independent_pair(primary_units, corroborating_units):
    for p in primary_units:
        for c in corroborating_units:
            if _independent(p, c):
                return True
    return False


def evaluate_sufficiency(units, pattern):
    """units: list of admitted evidence units {role, source_id, category, dataset?, excluded?, binding?}.
    Returns (bool, reason). Excluded units never count. CONTEXT-bound units
    (binding == 'context') never fill a sufficiency slot: only DIRECT evidence can
    satisfy a relationship's evidence pattern."""
    u = [x for x in units if not x.get("excluded") and x.get("binding") != "context"]
    if pattern == "single_authoritative_sufficient":
        ok = any(x.get("role") == "primary_authoritative" for x in u)
        return (ok, "primary_authoritative present" if ok else "no primary_authoritative record")
    if pattern == "primary_plus_corroborating":
        # 'primary' = a primary-grade record (primary study, official record, or an
        # authoritative-database record faithfully representing a primary determination).
        # 'corrob' additionally allows secondary_scholarly (e.g. a review) — as corroboration,
        # never alone. Independence is judged by originating-work lineage (see _independent).
        primary_roles = ("primary_authoritative", "official_record", "primary_scientific", "authoritative_database")
        corrob_roles = primary_roles + ("corroborating", "secondary_scholarly")
        primary = [x for x in u if x.get("role") in primary_roles]
        corrob = [x for x in u if x.get("role") in corrob_roles]
        ok = bool(primary) and _has_independent_pair(primary, corrob)
        return (ok, "primary + independent corroboration" if ok else "needs a primary and a genuinely independent corroborating record (distinct originating work)")
    if pattern == "original_instrument_required":
        ok = any(x.get("category") == "regulatory_instrument" or x.get("is_instrument") for x in u)
        return (ok, "governing instrument present" if ok else "governing instrument required")
    if pattern == "multi_source_synthesis":
        return (False, "governance_threshold_required: multi_source_synthesis threshold not yet ratified")
    if pattern == "explicit_source_exclusion":
        return (False, "explicit_source_exclusion is a constraint, not a standalone sufficiency pattern")
    return (False, f"unknown sufficiency pattern '{pattern}'")


def trade_quant_classification_ok(evidence_record):
    """Rule: quantitative trade evidence MUST carry a commodity classification code/version.
    Returns True only if the evidence locator provides classification_code AND classification_system."""
    loc = evidence_record.get("locator") or {}
    return bool(loc.get("classification_code")) and bool(loc.get("classification_system"))


def build_admission_unit(evidence_record, qualification_id, intended_use, data=None):
    """Production bridge: build an evidence unit whose `admitted` flag is COMPUTED by
    admissible(), never taken from the input. A caller cannot forge admitted=true.
    Returns (unit, reason)."""
    d = data or load_all()
    sid = evidence_record["source_id"]
    q = d["qual_by_id"].get(qualification_id, {})
    ctx = {
        "source_id": sid,
        "qualification_id": qualification_id,
        "subject_domain": (evidence_record.get("subject_domain") or [None])[0],
        "evidence_kind": evidence_record.get("evidence_kind"),
        "claim_level": evidence_record.get("claim_level"),
        "evidence_role": evidence_record.get("evidence_role"),
        "intended_use": intended_use,
        "geography": (evidence_record.get("geography") or [None])[0],
        "jurisdiction": evidence_record.get("jurisdiction"),
        "temporal_scope": evidence_record.get("temporal_scope"),
    }
    admitted, reason = admissible(ctx, d)
    unit = {
        "admitted": admitted,                                   # COMPUTED, not trusted from input
        "review_posture": evidence_record.get("evidence_review_posture"),
        "qualification_state": q.get("qualification_state"),
        "source_locked": d["source_by_id"].get(sid, {}).get("source_lock_status") == "locked",
        "role": evidence_record.get("evidence_role"),
        "source_id": sid,
        "category": d["category_by_source"].get(sid),
        # DIRECT vs CONTEXT binding, read from the evidence record (default direct). A context
        # unit is admissible on its own terms but never fills a relationship sufficiency slot.
        "binding": evidence_record.get("evidence_binding", "direct"),
        # Governed independence metadata (explicit fields only; never free-text publisher).
        # independence_domain is derived from the evidence subject_domain; the lineage keys
        # (originating_work_id / issuer_id / dataset_id) are propagated from the source.
        "independence_domain": _independence_domain((evidence_record.get("subject_domain") or [None])[0]),
        "originating_work_id": d.get("work_by_source", {}).get(sid),
        "related_work_ids": sorted(d.get("related_works", {}).get(d.get("work_by_source", {}).get(sid), set())),
        "issuer_id": d.get("issuer_by_source", {}).get(sid),
        "dataset_id": d.get("dataset_by_source", {}).get(sid),
    }
    return unit, reason


def derive_evidence_posture_governed(evidence_bindings, pattern, data=None):
    """Production evidence-posture derivation. evidence_bindings: list of
    (evidence_record, qualification_id, intended_use). Units are built via the
    admission bridge (admitted is recomputed), so a forged admitted=true is ignored."""
    d = data or load_all()
    units = [build_admission_unit(ev, qid, use, d)[0] for (ev, qid, use) in evidence_bindings]
    return derive_evidence_posture(units, pattern)


def derive_evidence_posture(units, pattern, lock_required_for_locked=True):
    """Governed derivation of Contract C's evidence input. units carry:
    {admitted, review_posture, qualification_state, source_locked, role, source_id, category, dataset?, excluded?}.
    Returns 'evidence_collecting' | 'evidence_sufficient' | 'evidence_locked'."""
    admitted = [u for u in units
                if u.get("admitted") and u.get("qualification_state") in ADMITTING_QUAL_STATES
                and not u.get("excluded") and u.get("binding") != "context"]
    suff_admitted, _ = evaluate_sufficiency(admitted, pattern)
    if not suff_admitted:
        return "evidence_collecting"
    verified = [u for u in admitted if u.get("review_posture") == "evidence_verified"]
    suff_verified, _ = evaluate_sufficiency(verified, pattern)
    if suff_verified and (not lock_required_for_locked or all(u.get("source_locked") for u in verified)):
        return "evidence_locked"
    return "evidence_sufficient"
