"""
Relationship grammar tests (semantic-integrity-hardening).

Uses SYNTHETIC, in-memory instances only (nothing stored). Verifies that the
typed subject->predicate->object grammar accepts correctly-directed propositions
and rejects reversed / wrong-endpoint ones. Not wired to CI.

Exit 0 = pass, 1 = fail.
"""

import sys

from relationship_grammar import load_registry, validate_instance

FAILURES = []


def expect(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAILURES.append(name)


def main():
    print("=== Relationship grammar tests (synthetic; no stored instances) ===")
    reg = load_registry()

    # Correct direction: 'Morocco imports [substance]'  GEO --imports--> concept
    good_import = {
        "relationship_class_id": "REL-IMPORTER",
        "subject_ref": "GEO-MA", "subject_type": "geography",
        "object_ref": "molybdenum_disulfide", "object_type": "concept",
        "qualification_state": "unqualified", "evidence_ids": [], "temporal_scope": {},
    }
    expect("importer_correct_direction", validate_instance(good_import, reg) == [])

    # Reversed direction: 'substance imports Morocco' — concept as subject must FAIL.
    bad_import = dict(good_import, subject_ref="molybdenum_disulfide", subject_type="concept",
                      object_ref="GEO-MA", object_type="geography")
    expect("importer_reversed_rejected", validate_instance(bad_import, reg) != [])

    # terminology-origin: lexeme --context--> geography is allowed; reversed is not.
    good_term = {
        "relationship_class_id": "REL-TERMINOLOGY-ORIGIN",
        "subject_ref": "LEX-DE-MOS2-001", "subject_type": "lexeme",
        "object_ref": "GEO-DE", "object_type": "geography",
        "qualification_state": "unqualified", "evidence_ids": [], "temporal_scope": {},
    }
    expect("terminology_origin_correct", validate_instance(good_term, reg) == [])
    bad_term = dict(good_term, subject_type="geography", object_type="lexeme")
    expect("terminology_origin_reversed_rejected", validate_instance(bad_term, reg) != [])

    # regulatory jurisdiction: jurisdiction --regulates--> concept; concept-subject fails.
    good_reg = {
        "relationship_class_id": "REL-REGULATORY-JURISDICTION",
        "subject_ref": "JUR-EXAMPLE", "subject_type": "jurisdiction",
        "object_ref": "hydrogen_sulfide", "object_type": "concept",
        "qualification_state": "unqualified", "evidence_ids": [], "temporal_scope": {},
    }
    expect("regulatory_correct", validate_instance(good_reg, reg) == [])
    bad_reg = dict(good_reg, subject_type="concept", object_type="jurisdiction")
    expect("regulatory_reversed_rejected", validate_instance(bad_reg, reg) != [])

    # evidence_qualified requires evidence_ids.
    unq = dict(good_import, qualification_state="evidence_qualified", evidence_ids=[])
    expect("evidence_qualified_requires_evidence", validate_instance(unq, reg) != [])

    # unknown class rejected.
    expect("unknown_class_rejected",
           validate_instance({"relationship_class_id": "REL-NOPE", "subject_type": "geography",
                              "object_type": "concept"}, reg) != [])

    print("=" * 56)
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)})")
        return 1
    print("RESULT: PASS — relationship directionality/endpoint grammar holds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
