# Spektrum Source Artifact Deposit Protocol — Wave 1

**Sprint:** 5N-M  
**Scope:** Governed deposit of verified bibliographic artifacts for Spektrum / `de_core_mos2`  
**Date:** 2026-05-29

---

## Purpose

Define **where** verified bibliographic artifacts and source receipts may be placed, **what** must be deposited, and **what must not** be deposited in the public Bisulfid repository.

Artifact deposit is a **governance gate** — not registry execution, not source approval, not publication.

---

## What must be deposited (verified artifact bundle)

A complete bundle requires all items below before intake can upgrade to execution-ready:

| Artifact component | Content |
| --- | --- |
| Bibliographic capture record | All ten intake fields from `SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_FIELD_MATRIX_WAVE_1.md` — values confirmed from direct source inspection |
| Citation locator evidence | Edition and page/section/entry reference as seen in source |
| Access record | Access date; method of access (physical copy, licensed digital, institutional) |
| Rights posture statement | What use is permitted for registry row vs public page; license or restriction summary |
| Verification note | Human attestation that values match source; no invention |
| Sign-off record | Completed `SPEKTRUM_BIBLIOGRAPHIC_HUMAN_SIGNOFF_CHECKLIST_WAVE_1.md` |

**Partial bundles are rejected.** Missing required fields remain **blank** — do not infer.

---

## Where verified artifacts should be placed

| Deposit tier | Location | Use |
| --- | --- | --- |
| **Governed intake documentation** | `main/data/` sprint-governed markdown under explicit artifact-intake charter | Structured bibliographic values, verification notes, sign-off records — **no copyrighted full-text reproduction** |
| **Private verification store** | Out-of-repo secure store (maintainer-controlled; not public GitHub) | Source receipts, scans, licensed PDF excerpts, institutional access logs |
| **Registry row (future execution only)** | `main/data/sources/source_registry.json` | **Not in intake sprint** — execution sprint only after bundle + sign-off + guardrail **PASS** |

**Current repository state:** No intake artifact bundle deposited in governed documentation layer.

---

## What must NOT be deposited in the public repository

| Prohibited deposit | Reason |
| --- | --- |
| Full lexicon entry text reproduction | Copyright / licensing risk |
| Unverified bibliographic guesses | Violates `SOURCE_POLICY`; false verification posture |
| Raw unsourced URLs in public docs | Implies retrievability and verification not established |
| Paywalled or session-specific URLs without stable identifier | Breaks audit trail |
| Scanned pages without rights clearance | Copyright risk |
| Market, safety, medical, or procurement content | Out of scope; permanently blocked uses |
| Content page edits or marker removals | Intake sprint only — content audit is separate |
| `source_registry.json` rows | Execution sprint only |

---

## Deposit workflow (human)

1. Human obtains direct access to Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid entry.
2. Human records bibliographic values in governed intake template — **no invention**.
3. Human completes rights/license posture assessment.
4. Human stores sensitive receipts in **private verification store** (not public repo).
5. Human deposits structured intake record in governed documentation layer (future deposit sprint or maintainer action).
6. Human completes sign-off checklist — explicitly **not** approving registry execution in intake step.
7. Separate execution sprint chartered only if bundle complete and guardrails **PASS**.

---

## Deposit rejection criteria

Reject or defer deposit when any apply:

- Any required field invented or inferred
- Citation locator not confirmed from source
- Rights posture unknown or prohibitive for intended registry use
- Sign-off missing or incomplete
- Full-text reproduction attempted in public repo
- Deposit treated as source approval or execution authorization

---

## Relationship to source_registry.json

| Deposit protocol (5N-M) | Registry execution (future) |
| --- | --- |
| Defines where artifacts go | Inserts verified row |
| Requires sign-off | Requires execution charter |
| Leaves registry unchanged | Modifies `source_registry.json` |

---

## Related documents

- `SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_WAVE_1_REPORT.md`
- `SPEKTRUM_BIBLIOGRAPHIC_HUMAN_SIGNOFF_CHECKLIST_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
