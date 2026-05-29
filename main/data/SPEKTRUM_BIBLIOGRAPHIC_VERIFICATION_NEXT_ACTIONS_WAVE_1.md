# Spektrum Bibliographic Verification Next Actions — Wave 1

**Sprint:** 5N-K  
**Date:** 2026-05-29  
**Status:** Bibliographic field verification complete — registry execution **not allowed**

---

## Recommended next sprint

**Sprint 5N-L prep — direct source access bibliographic capture for Spektrum** — human with direct access to Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid supplies confirmed `author_or_organization`, `publisher`, `publication_date`, `edition`, `page_or_entry_citation`, and `url_or_doi` (if applicable) as verified capture artifacts. After capture clears, charter **separate registry execution sprint**.

**Parallel:** Draft Wave 1 backlog (**58** missing drafts); `sulfur_element_term_record` database track — **not advanced**.

---

## Whether next step should be source registry execution

**No — not yet.** Spektrum is **`execution_blocked_pending_direct_source_access`**. Required bibliographic fields remain **unverified**. Execution requires:

1. Direct source access bibliographic capture (**5N-L** recommended).
2. Readiness upgrade to **`execution_ready_after_field_verification`**.
3. Separate execution sprint charter + human sign-off.
4. Guardrail + L1 **PASS** on registry diff.

**`execution allowed now: no`**

---

## Whether additional direct source access is required

**Yes — required.** Primary blocker after 5N-K. Governance chain verified identity and scope; bibliographic values require human inspection of the Spektrum lexicon entry.

---

## Whether claim-boundary registration/reporting should happen next

**Yes — recommended in parallel** with 5N-L capture. Document MoS2 lexical/document-form claim boundaries in claim registries (reporting only — registries remain **inactive**). Claim **approval** remains blocked.

---

## Whether content source-lock planning should happen next

**Yes — recommended after execution**, not before. Source-lock planning charters audited line-to-source mapping — **after** registry execution and **before** marker removal.

---

## Whether legacy draft hardening should happen before draft wave 2

**Yes — recommended.** **58** routes lack drafts. Harden Wave 1 backlog before Draft Wave 2.

---

## Whether draft wave 2 should still wait

**Yes.** Draft Wave 2 **not approved** (Sprint 5O-B). Explicit charter required.

---

## Whether Route Registration Wave 2 should still wait

**Yes.** Route Registration Wave 2 execution **not approved**. **83** dry-run candidates; **0** added in 5N-K. `production_can_safely_proceed: no`.

---

## Criteria for moving from field verification to source_registry.json edit

All must be true:

1. Bibliographic field verification complete (**5N-K**).
2. Direct source access capture complete — all required bibliographic fields verified, none invented (**5N-L**).
3. Readiness classification upgraded to **`execution_ready_after_field_verification`**.
4. Execution readiness reviewed (**5N-J**).
5. Proposal draft reviewed (**5N-I**).
6. Execution sprint charter issued — distinct from verification and capture.
7. Guardrail + corpus L1 **PASS** on proposed registry diff.
8. Human sign-off on inactive → verified transition.
9. `[SOURCE REQUIRED]` markers **remain** until content audit sprint.
10. Claim boundaries documented — claim approval still separate.

---

## Criteria for stopping execution

Stop or defer registry execution when any apply:

| Criterion | Action |
| --- | --- |
| Direct source access unavailable | **Defer** until access confirmed |
| Bibliographic capture fails verification | **Stop** — do not insert row |
| Entry scope insufficient for MoS2 DE naming | **Defer** or reject primary row |
| Supporting row elevated to primary | **Reject** elevation |
| Guardrail runtime fails on diff | **Stop** — fix before merge |
| Claim boundaries undefined for asserted lines | **Defer** claim linkage |
| Invented bibliography detected | **Stop** — remove invented values |

---

## How GitHub Actions governance must be used before merge

1. Open PR targeting `main` from Sprint 5N-K branch.
2. **Corpus governance validation** runs on PR.
3. All validators exit **0** — required under branch protection.
4. Human review confirms documentation-only scope.
5. CI **PASS** does **not** authorize registry execution or source approval.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Mechanism |
| --- | --- |
| Source track advance | `de_core_mos2` progresses readiness → verification → capture → execution |
| Field discipline | Unverified bibliographic fields documented blank — no invention |
| Merge gates | Corpus Governance CI on every PR |
| Launch threshold | **500-page** minimum preserved |
| Parallel backlog | **58** missing drafts governed under locks |

Verification clears **one gate** — it does not authorize registry edit today.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Merge Sprint 5N-K verification docs | **Yes** (after review + CI PASS) |
| Direct source access bibliographic capture (5N-L) | **Yes** (next) |
| Source registry execution | **No** |
| Source approval | **No** |
| Claim approval | **No** |
| Content source-locking / marker removal | **No** |
| Route Registration Wave 2 execution | **No** |
| Draft Wave 2 | **No** |
| `sulfur_element_term_record` database track | **Parallel** — not advanced |

---

## Related documents

- `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_EXECUTION_NEXT_ACTIONS_WAVE_1.md`
