# Named Source Candidate Next Actions — Wave 1

**Sprint:** 5N-G  
**Date:** 2026-05-29 (patched after external human review)  
**Status:** Intake complete — **named candidates documented, verification required** — registry execution **not allowed**

---

## Recommended next sprint

**Human external verification sprint for `de_core_mos2` named candidates** — verify primary Spektrum lexicon fit, PubChem/NIST supporting scope, and Chemie.de secondary-only role. After verification clears, charter **5N-H** source registry **proposal drafting** (still no registry execution).

**Do not proceed to:** source registry editing, claim approval, content source-locking, Route Registration Wave 2 execution, or Draft Wave 2 until human verification completes and proposal drafting gates clear.

---

## Whether next step should be human naming of a specific German specialist lexicon candidate

**Partially complete.** External human review identified named targets including **Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid** as **primary** German specialist lexicon candidate. **Next step is human external verification** of documented targets — not additional naming unless verification rejects primary candidate.

---

## Whether next step should be source registry proposal drafting

**No — not yet.** Proposal drafting (planned 5N-H) requires completed human external verification confirming authority fit and `SOURCE_POLICY` fit. Current posture: **`can_prepare_registry_proposal_after_human_verification`** — verification **not yet complete**. **`source registry proposal allowed next: no`**.

---

## Whether next step should be source registry editing

**No.** Registry execution requires separate sprint charter, guardrail **PASS**, human-verified proposal, and inactive → verified transition policy. **0** registry rows may be added now.

---

## Whether sulfur_element_term_record should remain in database candidate naming track

**Yes.** Remains **`needs_scientific_database_candidate_first`** — parallel track, **not advanced** in 5N-G. MoS2 supporting candidates (PubChem, NIST) documented for **`de_core_mos2` only** and do **not** advance `sulfur_element_term_record`.

---

## Whether claim-boundary registration/reporting should happen before registry execution

**Yes — recommended in parallel with source track**, but claim-boundary work does **not** substitute for human verification of named candidates. Claim approval remains blocked with inactive registries.

---

## Whether legacy draft hardening should happen before draft wave 2

**Yes — recommended.** **58** routes lack drafts from Wave 1. Hardening existing drafts and reducing backlog should precede Draft Wave 2 or mass draft production.

---

## Whether draft wave 2 should still wait

**Yes.** Draft Wave 2 is **not approved** (Sprint 5O-B). Draft Wave 2 should wait until:

1. Wave 1 draft backlog materially addressed,
2. Human verification progress for `de_core_mos2`,
3. Explicit Draft Wave 2 charter with capacity.

---

## Criteria for moving from named candidate intake to proposal draft

All must be true:

1. Named candidate targets documented — **complete** (Sprint 5N-G patch).
2. **Human external verification completed** for Spektrum (primary), PubChem/NIST (supporting), Chemie.de (secondary only).
3. Candidates pass acceptance rules; none rejected under rejection rules.
4. Guardrail + corpus L1 (+ L2 if production context) runtimes **PASS**.
5. Separate **5N-H** proposal drafting sprint chartered — maximum **1** draft: `de_core_mos2`.
6. Proposal contains **human-verified** bibliographic details only.
7. `[SOURCE REQUIRED]` markers **remain** until source-locking sprint.

---

## Criteria for rejecting named candidates

Apply `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`:

- Vague, family-only, or AI-invented identities
- PubChem or NIST elevated to **primary DE lexical authority** without verification
- Chemie.de elevated to primary without verification
- General web, commercial, or market-drift sources
- Dictionary/database scope exceeded (formal nomenclature, market, safety, medical)
- Cannot be human-verified

Rejected candidates → **`named_candidate_rejected`** or reversion to blocked posture; registry proposal drafting **blocked**.

---

## How guardrail runtime must be used before and after future source sprints

| When | Requirement |
| --- | --- |
| Pre-sprint | `source_claim_guardrail_runtime_l1.py` **PASS** |
| Pre-sprint | `corpus_validation_runtime_l1.py` **PASS** |
| Pre-sprint (production context) | `corpus_production_runtime_l2.py` **PASS** |
| Post-sprint | Re-run all applicable runtimes before merge |
| Registry-touching sprint | Guardrail **mandatory**; no registry edits on failure |
| Content-touching sprint | L1 corpus + guardrail; markers discipline enforced |

Guardrail failure **blocks** registry execution regardless of intake or readiness documentation.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Mechanism |
| --- | --- |
| Named targets documented | Spektrum + supporting candidates give verification-ready intake — still **unapproved** |
| Role boundaries | Primary DE lexicon vs database/technical support prevents authority substitution |
| Verification gate | No proposal drafting until human confirms fit — no fake source-locking |
| Parallel tracks | `sulfur_element_term_record` database track unchanged |
| Production discipline | L2 dry-run (5O-B) + source intake (5N-G) advance planning without route/draft mass generation |
| Launch threshold | **500** governed pages require source-locked, editorially signed pages — not intake documentation |

Authority preserved by: **no approval without verification**, **no registry without execution sprint**, **no marker removal without audit**, **no publication without locks cleared**.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Human external verification of documented MoS2 candidates | **Yes — required next** |
| Source registry proposal drafting (5N-H) | **No — wait for verification** |
| Source registry editing | **No** |
| Claim approval | **No** |
| Content source-locking | **No** |
| `sulfur_element_term_record` database naming track | **Parallel — unchanged, not advanced** |
| Draft Wave 2 | **No — wait** |
| Route Registration Wave 2 execution | **No** |

---

## Related documents

- `NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `PRODUCTION_DRY_RUN_NEXT_ACTIONS.md`
