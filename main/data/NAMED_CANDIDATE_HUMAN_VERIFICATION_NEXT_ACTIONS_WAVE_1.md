# Named Candidate Human Verification Next Actions — Wave 1

**Sprint:** 5N-H  
**Date:** 2026-05-27  
**Status:** Human verification complete — registry execution **not allowed**

---

## Recommended next sprint

**Sprint 5N-I prep — source registry proposal drafting for `de_core_mos2`** — author proposal document with human-verified Spektrum bibliographic lines; document PubChem/NIST/Chemie.de in supporting-only roles; still **no** `source_registry.json` modification.

**Parallel:** Enable or confirm branch protection requiring **Corpus Governance CI** on `main` (repository admin — should already be active post-5P-A).

---

## Whether next step should be source registry proposal drafting

**Yes — conditional.** Spektrum is **`primary_candidate_verified_for_later_proposal`**. Proposal drafting may be chartered when human supplies **directly verified** bibliographic details from Spektrum with direct source access. Proposal drafting is **not** registry execution.

---

## Whether next step should be source registry editing

**No.** Registry execution requires separate sprint charter after proposal review, guardrail **PASS**, and human sign-off. **`source registry entry allowed now: no`**.

---

## Whether next step should be claim-boundary registration/reporting

**Yes — recommended in parallel** with proposal drafting preparation. Claim-boundary documentation for MoS2 lexical and document-form lines should precede claim approval. Claim **approval** remains blocked with inactive registries.

---

## Whether legacy draft hardening should happen before draft wave 2

**Yes — recommended.** **58** routes lack drafts from Wave 1. Hardening existing drafts and reducing backlog should precede Draft Wave 2 or mass draft production.

---

## Whether draft wave 2 should still wait

**Yes.** Draft Wave 2 is **not approved** (Sprint 5O-B). Draft Wave 2 should wait until:

1. Wave 1 draft backlog materially addressed,
2. Source registry proposal drafting progresses for `de_core_mos2`,
3. Explicit Draft Wave 2 charter with capacity.

---

## Whether Route Registration Wave 2 should still wait

**Yes.** Route Registration Wave 2 execution is **not approved** (Sprint 5O-B dry-run). **83** dry-run candidates documented; **0** added to `routes.json`. `production_can_safely_proceed: no`. Source/claim gates not cleared for bulk registration.

---

## Criteria for moving Spektrum into a future source registry proposal draft

All must be true:

1. Human verification complete — **`primary_candidate_verified_for_later_proposal`** (Sprint 5N-H).
2. Human supplies **directly verified** Spektrum bibliographic details — no AI invention.
3. Entry scope confirmed to cover MoS2 German naming lines on `de_core_mos2`.
4. PubChem/NIST/Chemie.de documented as supporting-only in proposal.
5. Guardrail + corpus L1 runtimes **PASS**.
6. Claim boundaries for MoS2 lines scoped in proposal — not approved.
7. `[SOURCE REQUIRED]` markers **remain** until audited linkage sprint.
8. Separate proposal drafting sprint charter — not bundled with registry execution.

---

## Criteria for keeping PubChem/NIST as supporting-only

| Criterion | Requirement |
| --- | --- |
| Authority class | Database/technical — not DE lexicon |
| Primary rejection | **`rejected_as_primary_german_authority`** must remain in proposal |
| Scope | Identity (PubChem) and technical data (NIST) only |
| Claim scope | No terminology claims approved from database rows alone |
| Drift block | No lubricant market or operational extension |

---

## Criteria for rejecting or limiting Chemie.de

| Criterion | Action |
| --- | --- |
| Primary elevation attempt | **Reject** — Spektrum remains primary |
| Web lexicon as sole DE authority | **Reject** for strict-registry page |
| Contradiction with Spektrum | **Defer** — human resolves before proposal |
| Inclusion in proposal | **Optional** secondary row only — not required for proposal validity |

---

## How GitHub Actions governance must be used before merge

1. Open PR targeting `main` from Sprint 5N-H branch.
2. **Corpus Governance CI** runs automatically — L1, guardrail, L2, L0 validators.
3. All scripts must exit **0** — nonzero blocks merge when branch protection enabled.
4. Human review confirms sprint scope: documentation only — no registry/content/workflow changes.
5. CI **PASS** does **not** authorize source approval, registry editing, or publication.

Manual `workflow_dispatch` may re-run governance validation on demand — same read-only steps.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Mechanism |
| --- | --- |
| Source track advance | `de_core_mos2` lowest-gap draft progresses verification → proposal → execution sequence |
| Authority discipline | Primary/supporting boundaries prevent thin-authority pages at scale |
| Merge gates | Corpus Governance CI enforces locks on every PR to `main` |
| Launch threshold | **500-page** minimum preserved — verification does not bypass |
| Parallel backlog | **58** missing drafts and **126** existing routes remain governed under locks |
| Blocked tracks | `sulfur_element_term_record` database naming — separate parallel track |

Human verification clears **one gate** in the source sequence — it does not increment launch-eligible page count or weaken the **500-page** sovereign launch threshold.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Merge Sprint 5N-H verification docs | **Yes** (after review + CI PASS) |
| Source registry proposal drafting (5N-I) | **Yes** (conditional — next sprint) |
| Source registry editing | **No** |
| Claim approval | **No** |
| Content source-locking / marker removal | **No** |
| Route Registration Wave 2 execution | **No** |
| Draft Wave 2 | **No** |
| `sulfur_element_term_record` database track | **Parallel** — not advanced here |

---

## Related documents

- `NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`
- `NAMED_CANDIDATE_HUMAN_VERIFICATION_MATRIX_WAVE_1.md`
- `SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md`
- `SUPPORTING_CANDIDATE_BOUNDARY_REVIEW_WAVE_1.md`
- `NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md`
- `GITHUB_ACTIONS_GOVERNANCE_NEXT_ACTIONS.md`
