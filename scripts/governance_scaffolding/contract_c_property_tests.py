"""
Contract C — property tests (specification-level, unwired).

Sprint: authority-dimension-impl-1.
Runs the seven canonical property tests over the EXHAUSTIVE Cartesian product of
canonical input postures. Pure; touches no repository state; not wired to CI hard-fail.

Canonical property set (reconciles the earlier "four vs six" doc inconsistency —
see BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md IP-1, reconciled to SEVEN):
  1. Totality
  2. Determinism
  3. Monotonic veto
  4. All-green indexability
  5. Hold isolation
  6. New-object law
  7. Legacy isolation

Exit code 0 = all pass, 1 = any failure.
"""

import sys

from contract_c_derive import (
    derive,
    all_input_combinations,
    privilege_rank,
    legacy_holding_allowed,
    PUBLICATION_STATES,
    INDEXATION_STATES,
)

FAILURES = []


def record(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append((name, detail))


def test_totality_and_determinism():
    """1 Totality: every combo returns exactly one valid pair.
       2 Determinism: identical inputs always yield identical outputs."""
    total = 0
    totality_ok = True
    determinism_ok = True
    for inp in all_input_combinations():
        total += 1
        out1 = derive(**inp)
        out2 = derive(**inp)
        if not (isinstance(out1, tuple) and len(out1) == 2):
            totality_ok = False
        pub, idx = out1
        if pub not in PUBLICATION_STATES or idx not in INDEXATION_STATES:
            totality_ok = False
        if out1 != out2:
            determinism_ok = False
    record("1_totality", totality_ok, "some combo returned an invalid/absent pair")
    record("2_determinism", determinism_ok, "same inputs produced differing outputs")
    print(f"    (evaluated {total} input combinations)")
    return total


def test_monotonic_veto():
    """3 Moving any single upstream posture to a maximally-blocking value never
       raises output privilege."""
    blocks = {
        "release": "withdrawn",
        "governance": "planned",
        "validation": "not_validated",
        "claim": "claim_forbidden",
        "evidence": "evidence_collecting",
        "ig": "ig_failed",
    }
    ok = True
    for inp in all_input_combinations():
        base_rank = privilege_rank(*derive(**inp))
        for field, blocking_value in blocks.items():
            mutated = dict(inp)
            mutated[field] = blocking_value
            if privilege_rank(*derive(**mutated)) > base_rank:
                ok = False
                break
        if not ok:
            break
    record("3_monotonic_veto", ok, "a blocking posture raised privilege")


def test_all_green_indexability():
    """4 index_approved occurs only through the permitted factual or certified
       non-factual paths, with every gate green and no hold."""
    ok = True
    for inp in all_input_combinations():
        pub, idx = derive(**inp)
        if idx == "index_approved":
            factual = (
                inp["evidence"] == "evidence_locked"
                and inp["claim"] in ("claim_approved", "claim_approved_narrow")
            )
            non_factual = (
                inp["evidence"] == "evidence_not_required"
                and inp["claim"] == "claim_not_required"
                and inp["non_factual_class_certified"] is True
            )
            all_green = (
                inp["legacy"] == "none"
                and inp["governance"] == "governed"
                and inp["validation"] == "validated"
                and inp["release"] == "authorized"
                and inp["ig"] in ("ig_passed", "ig_not_required")
                and inp["hold"] == "none"
                and pub == "public_indexable"
            )
            if not (all_green and (factual or non_factual)):
                ok = False
                break
    record("4_all_green_indexability", ok, "index_approved reached without all-green permitted path")


def test_hold_isolation():
    """5 indexation_hold changes only indexation_state, never publication_state,
       and forces noindex when held."""
    ok = True
    for inp in all_input_combinations():
        if inp["hold"] != "none":
            continue
        none_pub, none_idx = derive(**inp)
        held = dict(inp)
        held["hold"] = "held"
        held_pub, held_idx = derive(**held)
        if held_pub != none_pub:
            ok = False
            break
        if held_idx != "noindex":
            ok = False
            break
    record("5_hold_isolation", ok, "hold changed publication_state or failed to force noindex")


def test_new_object_law():
    """6 For new objects (legacy=none), reference_draft / ig_not_reviewed / ig_failed
       can never produce a public URL."""
    ok = True
    for inp in all_input_combinations():
        if inp["legacy"] != "none":
            continue
        if inp["governance"] == "reference_draft" or inp["ig"] in ("ig_not_reviewed", "ig_failed"):
            pub, idx = derive(**inp)
            if pub != "not_public" or idx != "noindex":
                ok = False
                break
    record("6_new_object_law", ok, "a new draft/unreviewed/failed-IG object became public")


def test_legacy_isolation():
    """7 legacy_public_holding yields exactly (public_noindex, noindex) unless withdrawn,
       never index_approved, and can never be assigned to a newly created route."""
    ok = True
    for inp in all_input_combinations():
        if inp["legacy"] != "legacy_public_holding":
            continue
        pub, idx = derive(**inp)
        if inp["release"] == "withdrawn":
            expected = ("not_public", "noindex")
        else:
            expected = ("public_noindex", "noindex")
        if (pub, idx) != expected:
            ok = False
            break
        if idx == "index_approved":
            ok = False
            break
    # Assignment precondition: legacy holding must be rejected for a newly created route.
    assign_ok = (
        legacy_holding_allowed(is_new_route=True, pre_ratification_public=True) is False
        and legacy_holding_allowed(is_new_route=True, pre_ratification_public=False) is False
        and legacy_holding_allowed(is_new_route=False, pre_ratification_public=True) is True
        and legacy_holding_allowed(is_new_route=False, pre_ratification_public=False) is False
    )
    record("7_legacy_isolation", ok and assign_ok,
           "legacy holding produced a wrong state or was assignable to a new route")


def main():
    print("=== Contract C — property tests (unwired specification) ===")
    test_totality_and_determinism()
    test_monotonic_veto()
    test_all_green_indexability()
    test_hold_isolation()
    test_new_object_law()
    test_legacy_isolation()
    print("=" * 56)
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)} property test(s) failed)")
        return 1
    print("RESULT: PASS — all 7 canonical property tests hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
