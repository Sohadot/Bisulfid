# Source and Claim Automation Validation Report

**Sprint:** 5N-B  
**Validation date:** 2026-05-28  
**Runtime:** `python scripts/source_claim_guardrail_runtime_l1.py`

---

## Scripts run

| Script | Exit | Result |
| --- | ---: | --- |
| `validate_source_registration_proposals_l1.py` | 0 | **PASS** |
| `validate_source_evidence_requirements_l1.py` | 0 | **PASS** |
| `validate_claim_boundary_preparation_l1.py` | 0 | **PASS** |
| `validate_source_registry_lock_l1.py` | 0 | **PASS** |
| `validate_claim_registry_lock_l1.py` | 0 | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | 0 | **PASS** |

**Corpus L1 (informational):** `corpus_validation_runtime_l1.py` — **PASS**

---

## Files checked

### Proposal and evidence documents

- `main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`
- `main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md`

### Claim-boundary preparation

- `main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`

### Registries (read-only)

- `main/data/sources/source_registry.json`
- `main/data/claims/*.json` (6 registries)

### Draft content (read-only scan)

- All draft-backed routes referenced in `routes.json`

---

## Validation results

| Check area | Result | Notes |
| --- | --- | --- |
| Source proposal validation | **PASS** | 5 files; 5 matrix rows; all posture flags `no` |
| Evidence requirement validation | **PASS** | 5 evidence rows; authority boundaries intact |
| Claim boundary prep validation | **PASS** | 20 medium-risk rows; all deferral flags `no` |
| Source registry lock | **PASS** | inactive; 14 sources; 0 verified/approved |
| Claim registry lock | **PASS** | 6 inactive registries; 0 approved claims |

---

## Raw URL / invented bibliography result

**PASS** — no raw URLs or ISBN/DOI patterns in Sprint 5N-A proposal documents.

---

## Source-locking false-positive result

**PASS** — negation-aware scan matches corpus claims L1 behavior. Legacy drafts with “does **not** claim source-locking is complete” are not flagged.

---

## Publication-ready false-positive result

**PASS** — proposal matrix `publication-ready` column is `no` for all **5** rows. No document states any page is publication-ready.

---

## Unresolved warnings (non-blocking)

| Source | Warning |
| --- | --- |
| Evidence validator | `de_core_biogenic_lang`, `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`: dictionary/teaching tier scoping reminders (notes already bound in matrix) |
| Claim registry lock | `acquire`: missing `[SOURCE REQUIRED]` marker (landing page; pre-existing) |

Warnings do **not** fail guardrail runtime.

---

## Final validation conclusion

**GUARDRAIL RUNTIME: PASS** — all five source/claim guardrail validators passed on 2026-05-28.

Sprint **5N-B** automation is ready to protect future source discovery and registry execution sprints. Human review remains mandatory before any registry edit or claim activation.

---

*Sprint 5N-B — Source and Claim Automation Validation Report*
