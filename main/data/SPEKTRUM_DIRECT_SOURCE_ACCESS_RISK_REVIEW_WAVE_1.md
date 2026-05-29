# Spektrum Direct Source Access Risk Review — Wave 1

**Sprint:** 5N-L  
**Date:** 2026-05-29

---

## Risk of treating direct access as source approval

Completing capture documentation without verified bibliographic values could be misread as source approval. **Mitigation:** **`source_approval_not_allowed_now`**; capture ≠ approval; **0** fields captured.

---

## Risk of using visible fields beyond their evidence class

Governance-verified fields from 5N-K (label, category, route scope) must not be treated as bibliographic verification. **Mitigation:** matrix separates governance carry-forward from uncaptured bibliographic rows.

---

## Risk of inventing missing bibliographic fields

Pressure to unblock execution may encourage guessed publisher, edition, or citation values. **Mitigation:** all six bibliographic fields remain **blank**; invented bibliography forbidden.

---

## Risk of using inaccessible citation data

Citing edition or page numbers not confirmed by direct inspection weakens strict-registry audit. **Mitigation:** `page_or_entry_citation` and `edition` remain blank; **`field_not_visible`**.

---

## Risk of editing source_registry.json too early

Inserting a row with blank bibliographic fields activates false registry authority. **Mitigation:** registry **unchanged**; **`execution_still_blocked`**.

---

## Risk of source-locking before field and claim alignment

Source-locking draft lines without full bibliographic capture and claim boundary registration over-asserts factual resolution. **Mitigation:** no source-locking; `[SOURCE REQUIRED]` markers remain.

---

## Risk of removing [SOURCE REQUIRED] markers too early

Marker removal before audited line-to-source mapping publishes unresolved assertions. **Mitigation:** markers unchanged on `de_core_mos2`.

---

## Risk of claim approval before claim boundary registration

Bibliographic capture does not register MoS2 claim boundaries. **Mitigation:** claim registries **inactive**; claim approval **not allowed now**.

---

## Risk of publication before source and claim gates clear

Publishing with incomplete capture and unresolved markers violates launch discipline. **Mitigation:** route remains `planned`; draft / non_public / non-indexable.

---

## Risk of treating CI pass as source approval

Corpus Governance CI validates repository integrity — not bibliographic truth from direct source inspection. **Mitigation:** CI **PASS** required for merge; CI **PASS** does **not** authorize source approval or registry execution.

---

## Why direct source access capture does not approve execution

| Capture outcome | Execution authorization |
| --- | --- |
| Direct access not available in repository | **Not sufficient** |
| 0 bibliographic fields captured | **Execution blocked** |
| 7 governance fields carry forward | **Not sufficient alone** |
| Registry diff | **None** |

Direct access capture **documents** capture posture — it does **not** authorize `source_registry.json` edit, source approval, claim approval, source-locking, or publication.

---

## Related documents

- `SPEKTRUM_DIRECT_SOURCE_ACCESS_CAPTURE_WAVE_1_REPORT.md`
- `SPEKTRUM_CAPTURED_FIELD_GAP_REVIEW_WAVE_1.md`
- `SPEKTRUM_BIBLIOGRAPHIC_VERIFICATION_RISK_REVIEW_WAVE_1.md`
