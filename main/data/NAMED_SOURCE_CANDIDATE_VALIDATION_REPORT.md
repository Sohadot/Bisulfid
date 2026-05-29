# Named Source Candidate Validation Report — Wave 1

**Sprint:** 5N-G  
**Validation date:** 2026-05-29 (post-patch)  
**Branch:** `claude/sprint-5n-g-named-source-candidate-intake-wave-1`

---

## Scripts run

| Script | Exit | Result |
| --- | ---: | --- |
| `scripts/corpus_production_runtime_l2.py` | 0 | **PASS** (pre-sprint, post-sprint, post-patch) |
| `scripts/corpus_validation_runtime_l1.py` | 0 | **PASS** (pre-sprint, post-sprint, post-patch) |
| `scripts/source_claim_guardrail_runtime_l1.py` | 0 | **PASS** (pre-sprint, post-sprint, post-patch) |
| `scripts/corpus_production_planner_l2.py` | 0 | **PASS** (dry-run report, post-patch) |

---

## Files checked

### Named candidate intake documents (Sprint 5N-G — patched)

- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md`

### Reference documents (read-only)

- Sprint **5N-F** proposal readiness documents
- Sprint **5N-E** external verification documents
- Sprint **5N-D** human review matrix
- Sprint **5N-C** discovery matrix
- Sprint **5N-B** guardrail reports
- Sprint **5O-A** / **5O-B** production documents
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json`
- `main/data/claims/terminology_claims.json`
- `main/data/routes.json`
- `main/content/de/pages/terminology/molybdenum-disulfide.md`

---

## Selected draft checked

| route_id | Exists | routes.json match | draft posture | Intake result (post-patch) |
| --- | --- | --- | --- | --- |
| `de_core_mos2` | Yes | Yes | draft / non_public / non-indexable | **`named_candidate_requires_external_verification`** |

---

## Named candidate targets documented

**PASS** — four candidate targets documented as **candidates only** (not approved):

| Role | Candidate target |
| --- | --- |
| Primary German specialist lexicon | Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid |
| Supporting database | PubChem — Molybdenum disulfide / CID 14823 |
| Supporting technical data | NIST Chemistry WebBook — molybdenum disulphide |
| Secondary German support | Chemie.de Lexikon — Molybdän(IV)-sulfid |

Original repository-internal finding **`named_candidate_absent`** superseded for intake posture after external human review. All candidates remain **unapproved**.

---

## Named candidate docs checked

| Document | Scope | Posture |
| --- | --- | --- |
| Intake matrix | **1** row | named present = **yes**; proposal/entry/claim/pub = **no** |
| Acceptance rules | DE lexicon + verification role boundaries | Intake ≠ approval |
| Rejection rules | Full rejection set | No registry on reject |
| Next actions | Human verification required next | No registry drafting until verification |
| Report | Route count **126**; candidate role table | Documented from `routes.json` |

---

## Corpus metrics (planner output)

| Metric | Value |
| --- | ---: |
| Route count | **126** |
| Draft-backed route count | **68** |
| Missing draft count | **58** |

---

## Lock posture (planner output)

| Lock | Result |
| --- | --- |
| Publication lock | **LOCKED** (all `planned`) |
| Indexation lock | **LOCKED** (none indexable) |
| Sitemap lock | **LOCKED** (none in sitemap) |
| Navigation lock | **LOCKED** (none in navigation) |

---

## Source registry unchanged result

**PASS** — `source_registry.json` not modified; status **inactive**; **14** entries; **0** verified; **0** new entries.

---

## Claim registry unchanged result

**PASS** — **6** registries **inactive**; **0** approved claims; `terminology_claims.json` not modified.

---

## routes.json unchanged result

**PASS** — **126** routes; all `planned`; not modified in Sprint 5N-G or patch.

---

## Content unchanged result

**PASS** — `de_core_mos2` draft read-only; no content pages created or modified; `[SOURCE REQUIRED]` markers remain.

---

## Raw URL result

**PASS** — no `http://` or `https://` URLs in Sprint **5N-G** intake documents (including patch). Candidate targets documented by work name and identifier (e.g. CID 14823) only.

---

## Invented bibliography result

**PASS** — no invented DOI, ISBN, edition, author, publisher, date, citation, or page numbers in Sprint **5N-G** documents.

---

## Source approval false-positive result

**PASS** — all four named targets explicitly **candidates only — not approved**; matrix and report state verification required before proposal drafting.

---

## Source-locking false-positive result

**PASS** — no language implying `de_core_mos2` is source-locked; draft retains `[SOURCE REQUIRED]` markers (read-only verification).

---

## Publication-ready false-positive result

**PASS** — intake matrix: **publication-ready: no**; all routes `planned`, non-indexable.

---

## Runtime results

| Runtime | Result |
| --- | --- |
| Production L2 runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Source/claim guardrail runtime | **PASS** |
| L2 planner | **PASS** — `production_can_safely_proceed: no` |

---

## Unresolved warnings

| Warning | Notes |
| --- | --- |
| Human external verification incomplete | Expected — next gate before proposal drafting |
| `production_can_safely_proceed: no` | Expected — not an error |
| **58** missing drafts | Wave 1 backlog — parallel track |
| `sulfur_element_term_record` blocked | Database candidate track — not advanced in 5N-G |

No validator failures. No registry drift detected.

---

## Final validation conclusion

**PASS** — Sprint **5N-G** named source candidate intake documentation updated for **`de_core_mos2`**. Post-patch classification: **`named_candidate_requires_external_verification`**; **`candidate_requires_human_verification`**; **`can_prepare_registry_proposal_after_human_verification`**. Four named candidate targets documented (Spektrum primary; PubChem/NIST supporting; Chemie.de secondary only). All **unapproved**. Registry proposal drafting **blocked until human verification**; registry execution **blocked** (separate sprint). **`sulfur_element_term_record`** not advanced. No registry edits, no content edits, no raw URLs, no invented bibliographic details, no approval false-positives. All runtimes **PASS**.

---

## Recommended follow-up validation (after human verification)

1. Re-run guardrail + corpus L1 (+ L2 if applicable) runtimes.
2. Confirm verification outcome per candidate role.
3. Charter 5N-H proposal drafting only if verification clears all gates.
