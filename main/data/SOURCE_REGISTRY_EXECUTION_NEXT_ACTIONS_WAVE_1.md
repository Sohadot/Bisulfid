# Source Registry Execution Next Actions — Wave 1

**Sprint:** 5N-J  
**Date:** 2026-05-29  
**Status:** Execution readiness complete — registry execution **not allowed**

---

## Recommended next sprint

**Sprint 5N-K prep — human bibliographic field verification for Spektrum** — human supplies directly verified `author_or_organization`, `publisher`, `publication_date`, and `url`/`doi` (if applicable) from Spektrum entry with direct source access. After verification clears, charter **separate registry execution sprint**.

**Parallel:** Draft Wave 1 backlog (**58** missing drafts); `sulfur_element_term_record` database track — **not advanced**.

---

## Whether next step should be source registry execution

**No — not yet.** Spektrum is **`execution_blocked_pending_field_verification`**. Required bibliographic fields are **unverified**. Execution requires:

1. Human bibliographic verification sprint (**5N-K** recommended).
2. Readiness upgrade to **`execution_ready_after_field_verification`**.
3. Separate execution sprint charter + human sign-off.
4. Guardrail + L1 **PASS** on registry diff.

**`execution allowed now: no`**

---

## Whether next step should be additional field verification

**Yes — required.** Primary blocker for Spektrum execution. Human must verify all `SOURCE_POLICY` required fields before any `source_registry.json` edit.

---

## Whether next step should be claim-boundary registration/reporting

**Yes — recommended in parallel** with bibliographic verification prep. Document MoS2 lexical/document-form claim boundaries before claim approval. Claim **approval** remains blocked.

---

## Whether next step should be content source-lock planning

**Yes — recommended after execution**, not before. Source-lock planning charters audited line-to-source mapping — **after** registry execution and **before** marker removal.

---

## Whether legacy draft hardening should happen before draft wave 2

**Yes — recommended.** **58** routes lack drafts. Harden Wave 1 backlog before Draft Wave 2.

---

## Whether draft wave 2 should still wait

**Yes.** Draft Wave 2 **not approved** (Sprint 5O-B). Explicit charter required.

---

## Whether Route Registration Wave 2 should still wait

**Yes.** Route Registration Wave 2 execution **not approved**. **83** dry-run candidates; **0** in `routes.json`. `production_can_safely_proceed: no`.

---

## Criteria for moving from execution readiness to source_registry.json edit

All must be true:

1. Readiness review complete (**5N-J**).
2. Human bibliographic verification complete — all required fields verified, none invented.
3. Readiness classification upgraded to **`execution_ready_after_field_verification`**.
4. Proposal draft reviewed and accepted (**5N-I**).
5. Execution sprint charter issued — distinct from verification and readiness.
6. Guardrail + corpus L1 **PASS** on proposed registry diff.
7. Human sign-off on inactive → verified transition.
8. `[SOURCE REQUIRED]` markers **remain** until content audit sprint.
9. Claim boundaries documented — claim approval still separate.

---

## Criteria for stopping execution

Stop or defer registry execution when any apply:

| Criterion | Action |
| --- | --- |
| Bibliographic verification fails | **Stop** — do not insert row |
| Entry scope insufficient for MoS2 DE naming | **Defer** or reject primary row |
| Human cannot access verifiable edition | **Defer** until access confirmed |
| Supporting row elevated to primary | **Reject** elevation |
| Guardrail runtime fails on diff | **Stop** — fix before merge |
| Claim boundaries undefined for asserted lines | **Defer** claim linkage |

---

## How GitHub Actions governance must be used before merge

1. Open PR targeting `main` from Sprint 5N-J branch.
2. **Corpus governance validation** runs on PR.
3. All validators exit **0** — required under branch protection.
4. Human review confirms documentation-only scope.
5. CI **PASS** does **not** authorize registry execution or source approval.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Mechanism |
| --- | --- |
| Source track advance | `de_core_mos2` progresses proposal → readiness → verification → execution |
| Field discipline | Unverified fields documented blank — no bibliographic invention |
| Merge gates | Corpus Governance CI on every PR |
| Launch threshold | **500-page** minimum preserved |
| Parallel backlog | **58** missing drafts governed under locks |

Readiness clears **one gate** — it does not authorize registry edit today.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Merge Sprint 5N-J readiness docs | **Yes** (after review + CI PASS) |
| Human bibliographic verification (5N-K) | **Yes** (next) |
| Source registry execution | **No** |
| Claim approval | **No** |
| Content source-locking / marker removal | **No** |
| Route Registration Wave 2 execution | **No** |
| Draft Wave 2 | **No** |
| `sulfur_element_term_record` database track | **Parallel** — not advanced |

---

## Related documents

- `SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
