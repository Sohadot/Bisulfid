# Named Source Candidate Next Actions — Wave 1

**Sprint:** 5N-G  
**Date:** 2026-05-29  
**Status:** Intake complete — **named candidate absent** — registry execution **not allowed**

---

## Recommended next sprint

**Owner / human action — name specific DE specialist lexicon candidate for `de_core_mos2`**, then re-run named candidate intake or proceed to external verification sprint with the human-provided name documented in governance artifacts.

**Do not proceed to:** source registry proposal drafting (5N-H), source registry editing, claim approval, content source-locking, Route Registration Wave 2 execution, or Draft Wave 2 until named candidate intake clears for MoS2.

---

## Whether next step should be human naming of a specific German specialist lexicon candidate

**Yes — required.** Sprint 5N-G confirmed **`named_candidate_absent`**. A corpus owner or designated human must name a **specific** German specialist chemistry lexicon work suitable for MoS2 compound naming under `NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`.

This is **human governance action**, not an automation sprint substitute.

---

## Whether next step should be source registry proposal drafting

**No — not yet.** Proposal drafting (planned 5N-H) requires intake status ≥ `named_candidate_provided_by_human` and cleared external verification path. Current posture: **`do_not_prepare_registry_proposal_yet`**.

---

## Whether next step should be source registry editing

**No.** Registry execution requires separate sprint charter, guardrail **PASS**, human-verified proposal, and inactive → verified transition policy. **0** registry rows may be added now.

---

## Whether sulfur_element_term_record should remain in database candidate naming track

**Yes.** Remains **`needs_scientific_database_candidate_first`** — parallel track, not advanced in 5N-G. Scientific database candidate naming is independent of MoS2 lexicon intake.

---

## Whether claim-boundary registration/reporting should happen before registry execution

**Yes — recommended in parallel with source track**, but claim-boundary work does **not** substitute for named source intake. Strict-registry MoS2 lines require claim gates before publication-ready status — claim approval remains blocked with inactive registries.

---

## Whether legacy draft hardening should happen before draft wave 2

**Yes — recommended.** **58** routes lack drafts from Wave 1. Hardening existing drafts and reducing backlog should precede Draft Wave 2 or mass draft production.

---

## Whether draft wave 2 should still wait

**Yes.** Draft Wave 2 is **not approved** (Sprint 5O-B). Draft Wave 2 should wait until:

1. Wave 1 draft backlog materially addressed,
2. Named source progress for priority drafts (`de_core_mos2`),
3. Explicit Draft Wave 2 charter with capacity.

---

## Criteria for moving from named candidate intake to proposal draft

All must be true:

1. Human names specific DE specialist lexicon candidate — intake re-classified from `named_candidate_absent`.
2. Candidate passes acceptance rules; not rejected under rejection rules.
3. External human verification completed or in progress with documented posture.
4. Guardrail + corpus L1 (+ L2 if production context) runtimes **PASS**.
5. Separate **5N-H** proposal drafting sprint chartered — maximum **1** draft: `de_core_mos2`.
6. Proposal contains human-verified bibliographic details only.
7. `[SOURCE REQUIRED]` markers **remain** until source-locking sprint.

---

## Criteria for rejecting named candidates

Apply `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`:

- Vague, family-only, or AI-invented identities
- General web, commercial, or market-drift sources
- EN-only dictionary without DE verification for DE page
- Dictionary scope exceeded (formal nomenclature, market, safety, medical)
- Cannot be human-verified

Rejected candidates → **`named_candidate_rejected`**; registry proposal drafting **blocked**.

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
| Sequencing clarity | Named intake prevents registry inflation without verified sources |
| `de_core_mos2` path | Lowest-gap DE terminology draft — priority source track when human names candidate |
| Blocked false progress | Absent candidate documented — no fake source-locking or publication readiness |
| Parallel tracks | Database naming for `sulfur_element_term_record` separated from lexicon track |
| Production discipline | L2 dry-run (5O-B) + source intake (5N-G) advance planning without route/draft mass generation |
| Launch threshold | **500** governed pages require source-locked, editorially signed pages — not registry or intake rows |

Authority preserved by: **no approval without verification**, **no registry without execution sprint**, **no marker removal without audit**, **no publication without locks cleared**.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Human naming of DE specialist lexicon for MoS2 | **Yes — required** |
| Re-intake / external verification after naming | **Yes — after human provides name** |
| Source registry proposal drafting (5N-H) | **No — wait** |
| Source registry editing | **No** |
| Claim approval | **No** |
| Content source-locking | **No** |
| `sulfur_element_term_record` database naming track | **Parallel — unchanged** |
| Draft Wave 2 | **No — wait** |
| Route Registration Wave 2 execution | **No** |

---

## Related documents

- `NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `PRODUCTION_DRY_RUN_NEXT_ACTIONS.md`
