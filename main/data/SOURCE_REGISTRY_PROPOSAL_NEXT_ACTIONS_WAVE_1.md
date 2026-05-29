# Source Registry Proposal Next Actions — Wave 1

**Sprint:** 5N-I  
**Date:** 2026-05-29  
**Status:** Proposal draft complete — registry execution **not allowed**

---

## Recommended next sprint

**Sprint 5N-J prep — source registry execution review for `de_core_mos2`** — human review of proposal draft; human supplies directly verified Spektrum bibliographic fields; guardrail **PASS**; separate execution charter before any `source_registry.json` modification.

**Parallel:** Draft Wave 1 backlog reduction (**58** missing drafts); `sulfur_element_term_record` database candidate naming track — **not advanced**.

---

## Whether next step should be source registry execution

**No — not yet.** Proposal draft is complete and **`proposal_draft_allowed_for_review`**. Execution requires:

1. Human review and acceptance of proposal documents.
2. Human-verified bibliographic fields for all proposed rows.
3. Separate execution sprint charter.
4. Guardrail + L1 **PASS** on registry diff.

**`source registry execution allowed now: no`**

---

## Whether next step should be claim-boundary registration/reporting

**Yes — recommended in parallel** with execution review preparation. Document MoS2 lexical and document-form claim boundaries in governance artifacts before claim approval. Claim **approval** remains blocked with inactive registries.

---

## Whether next step should be content source-lock planning

**Yes — recommended after execution review**, not before. Source-lock planning sprint may charter audited line-to-source mapping — **after** registry execution and **before** marker removal. Content must not be edited in execution sprint without separate audit charter.

---

## Whether legacy draft hardening should happen before draft wave 2

**Yes — recommended.** **58** routes lack drafts from Wave 1. Hardening existing drafts should precede Draft Wave 2.

---

## Whether draft wave 2 should still wait

**Yes.** Draft Wave 2 is **not approved** (Sprint 5O-B). Wait until Wave 1 backlog addressed, source track progresses, and explicit Draft Wave 2 charter.

---

## Whether Route Registration Wave 2 should still wait

**Yes.** Route Registration Wave 2 execution is **not approved**. **83** dry-run candidates; **0** added to `routes.json`. `production_can_safely_proceed: no`.

---

## Criteria for moving from proposal draft to execution

All must be true:

1. Proposal draft reviewed and accepted by corpus owner or designated reviewer.
2. Human supplies **directly verified** Spektrum bibliographic fields — no AI invention.
3. Entry scope confirmed against live Spektrum entry for MoS2 German naming lines.
4. Supporting rows (if any) bounded and bibliographically verified separately.
5. Guardrail + corpus L1 runtimes **PASS**.
6. Separate execution sprint charter — not bundled with claim approval or content edit.
7. `[SOURCE REQUIRED]` markers **remain** until content audit sprint after execution.
8. Claim boundaries documented — claim approval still separate.

---

## Criteria for rejecting or limiting Spektrum

| Criterion | Action |
| --- | --- |
| Bibliographic verification fails | **Reject execution** — return to human verification or re-intake |
| Entry scope insufficient for MoS2 DE naming | **Reject or defer** primary row |
| Lubricant/market drift detected | **Reject** per rejection rules |
| Human cannot access verifiable edition | **Defer execution** until access confirmed |

---

## Criteria for keeping PubChem/NIST supporting-only

| Criterion | Requirement |
| --- | --- |
| Not registry primary | Must not be primary row for `de_core_mos2` |
| Scope | Identity (PubChem) and technical data (NIST) only |
| Bibliographic verification | Separate human verification if row added |
| Claim scope | No terminology claims from database rows alone |

---

## Criteria for keeping Chemie.de secondary-only

| Criterion | Action |
| --- | --- |
| Primary elevation attempt | **Reject** — Spektrum remains primary |
| Optional inclusion | Tertiary row only — not required for execution validity |
| Contradiction with Spektrum | Human resolves before any row added |

---

## How GitHub Actions governance must be used before merge

1. Open PR targeting `main` from Sprint 5N-I branch.
2. **Corpus Governance CI** runs automatically — L1, guardrail, L2, L0 validators.
3. All scripts must exit **0** — nonzero blocks merge under branch protection.
4. Human review confirms sprint scope: proposal documentation only — no registry/content/workflow changes.
5. CI **PASS** does **not** authorize registry execution, source approval, or publication.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Mechanism |
| --- | --- |
| Source track advance | `de_core_mos2` progresses verification → proposal → execution sequence |
| Authority discipline | Primary/supporting boundaries documented before registry mutation |
| Merge gates | Corpus Governance CI enforces locks on every PR |
| Launch threshold | **500-page** minimum preserved — proposal does not bypass |
| Parallel backlog | **58** missing drafts remain governed under locks |

Proposal drafting clears **one gate** — it does not increment launch-eligible pages or weaken authority discipline.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Merge Sprint 5N-I proposal docs | **Yes** (after review + CI PASS) |
| Human review of proposal draft | **Yes** (next) |
| Source registry execution | **No** |
| Claim approval | **No** |
| Content source-locking / marker removal | **No** |
| Route Registration Wave 2 execution | **No** |
| Draft Wave 2 | **No** |
| `sulfur_element_term_record` database track | **Parallel** — not advanced |

---

## Related documents

- `SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_PROPOSAL_DRAFT_MATRIX_WAVE_1.md`
- `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`
- `SUPPORTING_SOURCE_BOUNDARY_PROPOSAL_DRAFT_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`
- `NAMED_CANDIDATE_HUMAN_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
