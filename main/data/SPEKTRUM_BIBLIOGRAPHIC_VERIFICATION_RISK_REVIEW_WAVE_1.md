# Spektrum Bibliographic Verification Risk Review — Wave 1

**Sprint:** 5N-K  
**Date:** 2026-05-29

---

## Risk of inventing bibliographic fields

Inserting guessed publisher, author, edition, date, or citation values into readiness or registry docs creates **false verification posture**. Guardrails and human audit would treat invented metadata as governance failure. Sprint **5N-K** leaves all unverified bibliographic fields **blank**.

---

## Risk of using an unverified URL/DOI

An unconfirmed locator implies retrievability and edition identity not established in repository. Broken, wrong-edition, or paywalled links weaken strict-registry discipline. **Mitigation:** no raw URLs in 5N-K docs; `url_or_doi` remains blank until direct source access confirms.

---

## Risk of using publisher/author/date guesses

Lexicon editions change imprints, editorial boards, and pagination. Guessed metadata could misidentify the authority backing draft lines. **Mitigation:** `author_or_organization`, `publisher`, `publication_date` remain **unverified** and blank.

---

## Risk of approving source before field verification

Treating governance-verified fields as full source approval bypasses `SOURCE_POLICY` required bibliographic gates. **Mitigation:** Spektrum **`source_approval_not_allowed_now`**; verification ≠ approval.

---

## Risk of editing source_registry.json too early

Inserting a row with blank or invented bibliographic fields activates false registry authority. Claim and content pipelines could treat the row as verified. **Mitigation:** registry **unchanged**; execution **blocked**.

---

## Risk of source-locking before field verification

Source-locking draft lines to an unverified registry row would imply factual resolution without bibliographic audit. **Mitigation:** no source-locking; `[SOURCE REQUIRED]` markers remain.

---

## Risk of removing [SOURCE REQUIRED] markers too early

Marker removal before audited line-to-source mapping publishes unresolved assertions. **Mitigation:** markers unchanged on `de_core_mos2`.

---

## Risk of claim approval before claim boundary registration

Bibliographic verification does not register MoS2 lexical/document-form claim boundaries in claim registries. Approving claims without boundaries risks over-broad authority attribution. **Mitigation:** claim registries **inactive**; claim approval **not allowed now**.

---

## Risk of publication before source and claim gates clear

Publishing `de_core_mos2` with unresolved markers and no verified registry row violates launch discipline. **Mitigation:** route remains `planned`; draft / non_public / non-indexable.

---

## Risk of treating CI pass as source approval

Corpus Governance CI validates repository integrity — not source bibliographic truth. **Mitigation:** CI **PASS** required for merge; CI **PASS** does **not** authorize source approval, registry execution, or publication readiness.

---

## Why bibliographic verification does not approve execution

| Verification outcome | Execution authorization |
| --- | --- |
| 7 governance fields verified | **Not sufficient** |
| 6 bibliographic fields unverified | **Execution blocked** |
| Direct source access pending | **No charter** |
| Registry diff | **None** |

Bibliographic verification **documents** field posture — it does **not** authorize `source_registry.json` edit, source approval, claim approval, source-locking, or publication.

---

## Related documents

- `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_EXECUTION_RISK_REVIEW_WAVE_1.md`
