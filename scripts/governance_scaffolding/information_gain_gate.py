"""
Information-Gain gate — deterministic, non-numeric, multi-signal route-distinctness authority.

Sprint: ig-governance-ratification.
Policy:  main/data/information_gain/ig_governance_policy.json (machine-discoverable, versioned).

WHAT THIS DOES
--------------
Given a pair of endpoints (routes and/or governed objects) and their qualitative,
multi-signal evidence, it classifies whether a candidate knowledge surface adds
distinct governed knowledge or a distinct reference task that warrants an INDEPENDENT
URL. It answers route-distinctness only; it never rewrites facts, claims, evidence,
independence, source locks, validation, Contract-C, release, or indexation.

LAWS (enforced here and by the validator)
-----------------------------------------
* NON-NUMERIC: signal values are categorical (disjoint/low/partial/high, na). There is
  NO numeric threshold, score, ratio, or weight. None is defined or permitted.
* TEXTUAL SIMILARITY IS DIAGNOSTIC ONLY: it is never a decision signal and can never
  upgrade a same-task surface to a pass. "Not a textual duplicate" is not independent value.
* FAIL-CLOSED: missing/unknown required signals, self-comparison, or ambiguous/contradictory
  evidence => 'unresolved' (posture ig_review_required, route_eligible False). Never a pass.
* POSITIVE VALUE REQUIRED FOR PASS: only valid_domain_specific_reference / valid_sibling /
  valid_localization yield ig_reviewed_pass. near_duplicate / module_relationship / unresolved
  are NEVER eligible for a sibling-route pass.

Pure; reads the ratified policy; unwired from CI. Exit 0 self-test pass / 1 fail.
"""

import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
POLICY_PATH = os.path.join(ROOT, "main", "data", "information_gain", "ig_governance_policy.json")

# Signals that may participate in a decision (textual_similarity is deliberately excluded).
DECISION_SIGNALS = (
    "evidence_set_overlap", "claim_set_overlap", "source_set_overlap",
    "relationship_difference", "geography_jurisdiction_difference",
    "temporal_difference", "module_section_overlap", "user_task_difference",
)
# Signals that MUST be present and recognized for the gate to resolve at all.
REQUIRED_SIGNALS = (
    "evidence_set_overlap", "claim_set_overlap", "source_set_overlap",
    "relationship_difference", "module_section_overlap", "user_task_difference",
)
DIAGNOSTIC_ONLY = ("textual_similarity",)

POSITIVE_CLASSIFICATIONS = ("valid_domain_specific_reference", "valid_sibling", "valid_localization")

_OVERLAP_TOKENS = ("disjoint", "partial", "high", "low")   # order: check 'disjoint' etc; 'high'/'low' last
_DIFF_TOKENS = ("high", "partial", "low", "na")


def load_policy(path=POLICY_PATH):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _endpoint(pair, side):
    """Return endpoint A or B ('a'/'b'), preferring an object ref over a route ref."""
    return pair.get(f"object_{side}") or pair.get(f"route_{side}")


def _base(ref):
    """Base object id of a possibly module-suffixed ref ('KO-X#formula' -> 'KO-X')."""
    return str(ref).split("#", 1)[0]


def _is_module_ref(ref):
    return "#" in str(ref)


def _same_object_modules(a, b):
    """True when both endpoints are distinct modules of ONE base object."""
    return _is_module_ref(a) and _is_module_ref(b) and _base(a) == _base(b) and a != b


def _bucket_overlap(raw):
    """Categorical overlap bucket from a (possibly verbose) signal string; None if unknown."""
    s = str(raw).strip().lower()
    if s.startswith("disjoint"):
        return "disjoint"
    if s.startswith("partial"):
        return "partial"
    # 'high'/'low' may be prefixes or leading tokens ('high (...)').
    if s.startswith("high"):
        return "high"
    if s.startswith("low"):
        return "low"
    return None


def _bucket_diff(raw):
    """Categorical difference bucket; treats any n/a-like value as 'na'; None if unknown."""
    s = str(raw).strip().lower()
    if s.startswith("n/a") or s.startswith("na") or s.startswith("none"):
        return "na"
    if s.startswith("high"):
        return "high"
    if s.startswith("partial"):
        return "partial"
    if s.startswith("low"):
        return "low"
    return None


def _posture_for(classification, policy):
    for c in policy["classifications"]:
        if c["classification"] == classification:
            return c["yields_posture"], bool(c["route_eligible"])
    # Unknown classification -> fail closed.
    return "ig_review_required", False


def evaluate(pair, policy=None):
    """Classify a single endpoint pair. Returns a governed, deterministic decision record.

    Result keys: classification, posture, route_eligible, reasons, signals_considered,
    unresolved_signals, endpoints, policy_version.
    """
    if policy is None:
        policy = load_policy()
    version = policy["version"]
    a, b = _endpoint(pair, "a"), _endpoint(pair, "b")
    sig = pair.get("signals") or {}
    reasons = []

    def result(classification, unresolved_signals, extra_reasons):
        posture, route_eligible = _posture_for(classification, policy)
        rs = list(reasons) + list(extra_reasons)
        # Belt-and-braces invariants (the classification logic already respects them):
        if route_eligible and classification not in POSITIVE_CLASSIFICATIONS:
            classification, posture, route_eligible = "unresolved", "ig_review_required", False
            rs.append("fail-closed: a route-eligible posture requires a positive independent-reference classification")
        if route_eligible and unresolved_signals:
            classification, posture, route_eligible = "unresolved", "ig_review_required", False
            rs.append("fail-closed: cannot pass with unresolved signals")
        return {
            "classification": classification,
            "posture": posture,
            "route_eligible": route_eligible,
            "reasons": rs,
            "signals_considered": [s for s in DECISION_SIGNALS if s in sig],
            "diagnostic_signals_ignored": [s for s in DIAGNOSTIC_ONLY if s in sig],
            "unresolved_signals": unresolved_signals,
            "endpoints": {"a": a, "b": b},
            "policy_version": version,
        }

    # (1) Self-comparison is never information gain — fail closed.
    if a is None or b is None:
        return result("unresolved", [s for s in REQUIRED_SIGNALS if s not in sig],
                      ["fail-closed: pair is missing an endpoint"])
    if a == b:
        return result("unresolved", [], ["fail-closed: self-comparison (endpoint A == endpoint B)"])

    # (2) Two modules of one object are a module_relationship regardless of prose.
    if _same_object_modules(a, b):
        return result("module_relationship", [],
                      [f"both endpoints are modules of one object ({_base(a)}); they are sections, not sibling URLs"])

    # (3) Resolve the required decision signals; missing/unknown => fail closed.
    unresolved = []
    buckets = {}
    for s in REQUIRED_SIGNALS:
        if s not in sig:
            unresolved.append(s)
            continue
        bucketed = _bucket_diff(sig[s]) if s.endswith("_difference") else _bucket_overlap(sig[s])
        if bucketed is None:
            unresolved.append(s)
        else:
            buckets[s] = bucketed
    if unresolved:
        return result("unresolved", unresolved,
                      ["fail-closed: required decision signals missing or unrecognized"])

    ev = buckets["evidence_set_overlap"]
    cl = buckets["claim_set_overlap"]
    sr = buckets["source_set_overlap"]
    rel = buckets["relationship_difference"]
    mod = buckets["module_section_overlap"]
    task = buckets["user_task_difference"]

    # (4) Positive independent reference value: disjoint governed sets AND a distinct task.
    distinct_task = (task == "high" and rel == "high"
                     and ev == "disjoint" and cl == "disjoint" and sr == "disjoint")
    # Same reference task as the compared surface: no new URL warranted.
    same_task = (task == "low" and mod == "high")

    if distinct_task:
        return result("valid_domain_specific_reference", [],
                      ["disjoint evidence/claim/source sets and a distinct reference task "
                       "(user_task_difference=high, relationship_difference=high): positive independent reference value"])
    if same_task:
        return result("near_duplicate", [],
                      ["same reference task (user_task_difference=low, module_section_overlap=high): "
                       "no new independent URL warranted"])

    # (5) Anything else is ambiguous on governed evidence — fail closed (textual similarity,
    #     which is diagnostic-only, is never consulted to break the tie).
    return result("unresolved", [],
                  ["fail-closed: governed decision signals are ambiguous; textual similarity is diagnostic-only "
                   "and cannot decide (not-a-duplicate alone is not independent value)"])


def _selftest():
    policy = load_policy()
    ok = True

    def expect(name, cond):
        nonlocal ok
        print(f"[{'PASS' if cond else 'FAIL'}] {name}")
        ok = ok and cond

    # Deterministic
    p = {"object_a": "KO-X", "route_b": "r", "signals": {
        "evidence_set_overlap": "disjoint", "claim_set_overlap": "disjoint", "source_set_overlap": "disjoint",
        "relationship_difference": "high", "module_section_overlap": "low", "user_task_difference": "high",
        "textual_similarity": "diagnostic_only"}}
    r1, r2 = evaluate(p, policy), evaluate(p, policy)
    expect("deterministic", r1 == r2)
    expect("positive->pass", r1["classification"] == "valid_domain_specific_reference"
           and r1["posture"] == "ig_reviewed_pass" and r1["route_eligible"] is True)

    # near_duplicate
    p2 = {"object_a": "KO-X", "route_b": "legacy", "signals": {
        "evidence_set_overlap": "disjoint", "claim_set_overlap": "disjoint", "source_set_overlap": "disjoint",
        "relationship_difference": "low", "module_section_overlap": "high", "user_task_difference": "low",
        "textual_similarity": "diagnostic_only"}}
    expect("near_duplicate->no route", evaluate(p2, policy)["route_eligible"] is False
           and evaluate(p2, policy)["classification"] == "near_duplicate")

    # module_relationship
    p3 = {"object_a": "KO-X#formula", "object_b": "KO-X#structure", "signals": {}}
    expect("module_relationship", evaluate(p3, policy)["classification"] == "module_relationship")

    # self-comparison fail-closed
    expect("self-comparison", evaluate({"object_a": "KO-X", "object_b": "KO-X", "signals": {}}, policy)["classification"] == "unresolved")

    # missing signals fail-closed
    expect("missing-signals", evaluate({"object_a": "KO-X", "route_b": "r", "signals": {"textual_similarity": "x"}}, policy)["classification"] == "unresolved")

    print("=" * 40)
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(_selftest())
