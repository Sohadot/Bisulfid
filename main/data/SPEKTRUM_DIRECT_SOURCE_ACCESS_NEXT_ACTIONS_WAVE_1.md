# Spektrum Direct Source Access Next Actions — Wave 1

**Sprint:** 5N-L  
**Date:** 2026-05-29  
**Status:** Direct source access capture documentation complete — registry execution **not allowed**

---

## Recommended next sprint

**Sprint 5N-M prep — verified bibliographic artifact capture with human sign-off for Spektrum** — human with direct access to Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid deposits confirmed bibliographic values as a governed capture artifact with explicit human verification sign-off. After artifact clears, charter **separate registry execution sprint**.

**Parallel:** Draft Wave 1 backlog (**58** missing drafts); `sulfur_element_term_record` database track — **not advanced**.

---

## Whether next step should be source registry execution

**No — not yet.** Spektrum is **`execution_still_blocked`**. **0** bibliographic fields captured. Execution requires:

1. Verified bibliographic artifact capture with human sign-off (**5N-M** recommended).
2. Readiness upgrade to **`execution_ready_after_field_verification`**.
3. Separate execution sprint charter + human sign-off.
4. Guardrail + L1 **PASS** on registry diff.

**`execution allowed now: no`**

---

## Whether additional direct source access is still required

**Yes — required.** Primary blocker after 5N-L. Capture documentation complete; verified artifact deposit from direct inspection **not yet performed**.

---

## Whether claim-boundary registration/reporting should happen next

**Yes — recommended in parallel** with 5N-M artifact capture. Document MoS2 lexical/document-form claim boundaries (reporting only — registries remain **inactive**). Claim **approval** remains blocked.

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

**Yes.** Route Registration Wave 2 execution **not approved**. **83** dry-run candidates; **0** added in 5N-L. `production_can_safely_proceed: no`.

---

## Criteria for moving from direct source capture to source_registry.json edit

All must be true:

1. Direct source access capture documentation complete (**5N-L**).
2. Verified bibliographic artifact capture complete — all six required fields captured, none invented (**5N-M**).
3. Readiness classification upgraded to **`execution_ready_after_field_verification`**.
4. Bibliographic field verification reviewed (**5N-K**).
5. Execution readiness reviewed (**5N-J**).
6. Execution sprint charter issued — distinct from capture and verification.
7. Guardrail + corpus L1 **PASS** on proposed registry diff.
8. Human sign-off on inactive → verified transition.
9. `[SOURCE REQUIRED]` markers **remain** until content audit sprint.
10. Claim boundaries documented — claim approval still separate.

---

## Criteria for stopping execution

Stop or defer registry execution when any apply:

| Criterion | Action |
| --- | --- |
| Bibliographic artifact capture incomplete | **Stop** — do not insert row |
| Any required field invented or inferred | **Stop** — remove invented values |
| Entry scope insufficient for MoS2 DE naming | **Defer** or reject primary row |
| Human cannot access verifiable edition | **Defer** until access confirmed |
| Supporting row elevated to primary | **Reject** elevation |
| Guardrail runtime fails on diff | **Stop** — fix before merge |
| Claim boundaries undefined for asserted lines | **Defer** claim linkage |

---

## How GitHub Actions governance must be used before merge

1. Open PR targeting `main` from Sprint 5N-L branch.
2. **Corpus governance validation** runs on PR.
3. All validators exit **0** — required under branch protection.
4. Human review confirms documentation-only scope.
5. CI **PASS** does **not** authorize registry execution or source approval.

---

## How this moves the corpus toward 500 governed pages without weakening authority

| Contribution | Mechanism |
| --- | --- |
| Source track advance | `de_core_mos2` progresses verification → capture → artifact → execution |
| Field discipline | Uncaptured fields documented blank — no bibliographic invention |
| Merge gates | Corpus Governance CI on every PR |
| Launch threshold | **500-page** minimum preserved |
| Parallel backlog | **58** missing drafts governed under locks |

Capture clears **one gate** — it does not authorize registry edit today.

---

## Summary action table

| Action | Proceed? |
| --- | ---: |
| Merge Sprint 5N-L capture docs | **Yes** (after review + CI PASS) |
| Verified bibliographic artifact capture (5N-M) | **Yes** (next) |
| Source registry execution | **No** |
| Source approval | **No** |
| Claim approval | **No** |
| Content source-locking / marker removal | **No** |
| Route Registration Wave 2 execution | **No** |
| Draft Wave 2 | **No** |
| `sulfur_element_term_record` database track | **Parallel** — not advanced |

---

## Related documents

- `SPEKTRUM_DIRECT_SOURCE_ACCESS_CAPTURE_WAVE_1_REPORT.md`
- `SPEKTRUM_BIBLIOGRAPHIC_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `SPEKTRUM_CAPTURED_FIELD_GAP_REVIEW_WAVE_1.md`
