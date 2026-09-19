"""
Source admissibility & evidence admission tests (13 required proofs).
Pure; reads governance data, changes nothing, unwired from CI.
Exit 0 = pass, 1 = fail.
"""

import json
import os
import sys

from source_admissibility import admissible, load_all

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
    print("=== Source admissibility & evidence admission tests ===")
    d = load_all()
    qual = load("source_use_qualification_registry.json")
    pol = load("source_admissibility_policy.json")
    evp = load("evidence_admission_policy.json")
    clp = load("claim_activation_policy.json")

    # base MoS2 admissible context (matches the one real qualification)
    base = {
        "source_id": "SRC-SPEKTRUM-MOS2-DE", "qualification_id": "QUAL-SPEKTRUM-MOS2-DE-001",
        "subject_domain": "SD-TERMINOLOGY", "evidence_kind": "terminological", "claim_level": "lexeme",
    }
    adm, _ = admissible(base, d)
    ok("00_baseline_mos2_admissible", adm)

    # 1: source category alone cannot grant admissibility (no qualification)
    a, r = admissible(dict(base, qualification_id=None), d)
    ok("1_category_alone_insufficient", (a is False) and "category alone" in r)

    # 2: prohibited use always vetoes
    a, r = admissible(dict(base, intended_use="route_publication"), d)
    ok("2_prohibited_use_vetoes", a is False and "prohibited" in r)

    # 3: qualification cannot silently broaden scope (domain outside scope)
    a, _ = admissible(dict(base, subject_domain="SD-CHEMISTRY"), d)
    ok("3_no_scope_broadening", a is False)

    # 4: lexeme/terminological qualification cannot satisfy a concept/scientific/economic claim
    a, _ = admissible(dict(base, claim_level="concept"), d)
    ok("4_lexeme_cannot_do_concept", a is False)

    # 5: contextual market/industry sources cannot alone establish importer/exporter.
    #    (policy-level proof: trade domain lists them contextual_only and requires official records.)
    trade = pol["domain_admissibility"]["trade_economics"]
    ok("5_contextual_cannot_establish_trade",
       set(trade["contextual_only_categories"]) == {"market_report", "industry_publication"}
       and "official_customs_data" in trade["allowed_categories"])

    # 6: current-law claims require an official instrument
    reg = pol["domain_admissibility"]["regulation_government"]
    ok("6_current_law_requires_instrument", reg["current_law_requires_category"] == ["regulatory_instrument"])

    # 7: evidence_verified does not imply claim approval
    ev = evp["evidence_review_lifecycle"]["evidence_verified"]
    ok("7_verified_not_claim_approval", "claim_approval" in ev["must_not_imply"])

    # 8: claim approval does not imply publication
    ok("8_approval_not_publication",
       any("claim_approval does NOT imply" in s for s in clp["independence_invariants"])
       and any("does NOT imply route_publication" in s for s in clp["independence_invariants"]))

    # 9: qualification regression never raises downstream privilege
    suspended = dict(base)
    # simulate by pointing at a copy whose state is suspended
    d2 = load_all()
    d2["qual_by_id"] = dict(d2["qual_by_id"])
    q = dict(d2["qual_by_id"]["QUAL-SPEKTRUM-MOS2-DE-001"]); q["qualification_state"] = "suspended"
    d2["qual_by_id"]["QUAL-SPEKTRUM-MOS2-DE-001"] = q
    a, _ = admissible(suspended, d2)
    ok("9_regression_lowers_privilege", a is False and evp["regression_rules"]["monotonic_direction"] == "regression_never_raises_privilege")

    # 10: conflicting evidence can remain unresolved
    ok("10_conflict_unresolved_supported",
       "unresolved_claim" in evp["conflicting_evidence"]["supported_representations"]
       and "contested_status" in evp["conflicting_evidence"]["supported_representations"])

    # 11: qualification references exactly one source
    ok("11_qualification_one_source",
       all(isinstance(q["source_id"], str) and q["source_id"] for q in qual["qualifications"]))

    # 12: qualification duplicates no bibliographic metadata
    forbidden = set(qual["qualification_record_schema"]["forbidden_fields"])
    leaked = [q["qualification_id"] for q in qual["qualifications"] if forbidden.intersection(q.keys())]
    ok("12_no_bibliographic_duplication", not leaked, f"leaked in {leaked}")

    # 13: MoS2 still derives not_public/noindex
    sys.path.insert(0, os.path.dirname(__file__))
    from contract_c_derive import derive
    ok("13_mos2_not_public",
       derive(governance="planned", evidence="evidence_sufficient", claim="claim_pending",
              validation="not_validated", ig="ig_not_reviewed", release="not_authorized") == ("not_public", "noindex"))

    print("=" * 56)
    if FAIL:
        print(f"RESULT: FAIL ({len(FAIL)})")
        return 1
    print("RESULT: PASS — all 13 admission proofs hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
