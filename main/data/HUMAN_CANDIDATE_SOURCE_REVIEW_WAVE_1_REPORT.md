# Human Candidate Source Review Wave 1 — Report

**Sprint:** 5N-D  
**Date:** 2026-05-28  
**Branch:** `claude/sprint-5n-d-human-candidate-source-review-wave-1`

---

## Why this sprint exists

Sprint **5N-C** named candidate source **families** and search targets for **5** drafts. Sprint **5N-D** applies **human-governed** acceptance, rejection, and future-registry logic to those candidates — without registering sources, approving claims, or removing markers.

---

## Why human candidate review comes after candidate source discovery

Discovery answers **where to look** (family + search target type). Human review answers **whether a named candidate class is acceptable**, **what verification is still missing**, and **whether registry proposal may proceed later** — still without registry rows.

---

## Why human review still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Candidate ≠ approved | Review targets are **not** verified entries |
| Guardrail gate | Sprint **5N-B** runtime must PASS |
| Verification gap | No named external source has been human-verified in this sprint |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited linkage |

---

## Relationship to Sprint 5N-C

This sprint reviews exactly the **5** discovery matrix rows from `CANDIDATE_SOURCE_DISCOVERY_MATRIX_WAVE_1.md`, inheriting discovery status, source family, and authority requirements.

---

## Relationship to Sprint 5N-B guardrail automation

Pre-flight and post-sprint: guardrail + corpus L1 **PASS**. Review documents must not introduce approval language, URLs, or registry-edit implications.

---

## Relationship to Sprint 5N-A source registration proposals

Proposals defined evidence tiers and posture flags. Human review evaluates whether discovery targets could **eventually** satisfy those tiers after external verification — not now.

---

## Relationship to Sprint 5M source mapping

Sprint **5M** mapped source gaps. Human review confirms which gaps remain blocked by missing verification, policy extension, or formal authority.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Human-reviewed drafts | **5** |
| Registry entries added | **0** |
| Publication-ready | **0** |

Human review advances **governance readiness** without publication eligibility.

---

## Files reviewed

- Sprint **5N-C** discovery documents (6 files)
- Sprint **5N-A** proposal and evidence matrices
- Sprint **5N-B** guardrail reports
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- **5** selected draft content files (read-only)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-C | **Yes** |
| Guardrail runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Selected drafts exist | **5/5** |
| Match `routes.json` | **5/5** |
| draft / non_public / non-indexable | **5/5** |
| Registry unchanged pre-sprint | **Yes** |

---

## Selected draft count

**5** drafts.

---

## Selected route_id list

```
sulfur_element_term_record
de_core_biogenic_lang
copper_sulfides_language
de_core_fes
de_core_mos2
```

---

## Language split

| Language | Count |
| --- | ---: |
| English (`en`) | **2** |
| German (`de`) | **3** |

---

## Human review methodology

1. Read Sprint **5N-C** discovery row per draft.
2. Read Sprint **5N-A** evidence and proposal rows.
3. Read draft markers and section structure (read-only).
4. Review SOURCE_POLICY categories and seeded registry **patterns** (no new rows).
5. Apply acceptance criteria and rejection rules.
6. Assign human review status, suitability, and future registry action.
7. Confirm **no** URLs, bibliographic fabrication, registry edits, or marker removal.
8. Re-run guardrail + corpus L1 after document creation.

---

## Source acceptance principles

- Named publisher/database/dictionary **class** must be verifiable by humans before registry proposal
- Category must fit SOURCE_POLICY
- Scope must map to draft markers line-by-line
- Teaching tier = supporting only; dictionary = naming/usage; database = identity tier where applicable
- Formal nomenclature required where evidence matrix flags **yes**

---

## Source rejection principles

- Reject weak, AI, uncited, market, safety, medical, procurement-primary candidates
- Reject teaching-as-formal-authority and dictionary-as-chemical-authority drift
- Reject partial marker satisfaction implying full source-lock
- See `HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md`

---

## Authority hierarchy principles

```
government_scientific_database / chemical_nomenclature_standard (formal, scoped)
        ↓ supporting only
authoritative_dictionary / German_lexical_dictionary (naming, usage)
        ↓ supporting only
academic_teaching_reference (terminology context, not formal lock)
        ↓ never alone for external factual authority
internal doctrine (framing only; not marker satisfaction)
```

---

## What human candidate source review means in this sprint

- Evaluates discovery targets under human governance logic
- Records accept/defer/reject/**blocked** posture per draft
- Defines criteria for **future** registry proposal drafting
- Documents verification gaps explicitly

---

## What human candidate source review does not mean

| Not implied | Reason |
| --- | --- |
| Source approved | Candidates remain unverified |
| Source-lock complete | Markers remain |
| Registry row authorized | No execution sprint |
| Claim approved | Registries inactive |
| Publication-ready | All posture flags **no** |
| Bibliographic certainty | Human verification required where naming unavailable |

---

## Candidate review findings by draft

| route_id | Review outcome summary |
| --- | --- |
| `sulfur_element_term_record` | Scientific database tier **potentially acceptable** after human names element-record authority; teaching **supporting only** |
| `de_core_biogenic_lang` | DE lexical family **potentially acceptable** but **blocked** until SOURCE_POLICY biogenic tier extension and human verification |
| `copper_sulfides_language` | Dictionary + formal nomenclature **potentially acceptable** as split tiers; formal authority verification required before registry |
| `de_core_fes` | DE mineral naming **potentially acceptable** with pyrite/procurement guard; formal authority for systematic names |
| `de_core_mos2` | **Lowest-gap** — DE specialist lexicon **review_candidate_ready**; human must name candidate before registry proposal |

---

## Candidates that may move toward future registry proposal

- `de_core_mos2` — after human names DE specialist lexicon candidate
- `sulfur_element_term_record` — after human names element-record database tier
- `copper_sulfides_language` — after dictionary + nomenclature candidates verified and mapped
- `de_core_fes` — after DE mineral lexicon candidate verified

---

## Candidates needing stronger verification

- All **5** drafts: **human verification required** for named external authority (no bibliographic details invented in this sprint)
- `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`: formal nomenclature verification where systematic names apply
- `sulfur_element_term_record`: element-record database verification

---

## Candidates rejected or blocked for now

| route_id | Status |
| --- | --- |
| `de_core_biogenic_lang` | **Blocked** until SOURCE_POLICY extension for biogenic/environmental tier |
| All drafts | **Rejected for source_registry_now** — no named verified candidate exists yet |
| Weak/AI/market/safety candidates | **Rejected** per rejection decisions (hypothetical classes) |

No draft is **approved**; none may enter registry in this sprint.

---

## Why no source entries were added

Sprint charter: **human-review documentation only**. Registry execution requires verified named candidates and separate charter.

---

## Why source_registry.json was not modified

Explicit sprint rule. Registry remains **inactive** with **14** seeded **candidate** rows.

---

## Why no claims were approved

Claim registries **inactive**. Human review does not activate claims.

---

## Why terminology_claims.json was not modified

Review sprint only. Claim boundary work remains separate.

---

## Why no content pages were modified

Review is governance documentation. `[SOURCE REQUIRED]` markers remain.

---

## Why `[SOURCE REQUIRED]` markers remain

Human review identifies acceptable **classes**; it does not satisfy authority lines or audit marker removal.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap/navigation.

---

## Publication blocker summary

| Blocker | All 5 drafts |
| --- | --- |
| Unresolved markers | **Yes** |
| No verified registry rows | **Yes** |
| Human verification incomplete | **Yes** |
| Registry inactive | **Yes** |
| Publication-ready | **No** |

---

## Recommended next sprint

**Sprint 5N-E — Source registry proposal drafting wave 1** (optional, 1–3 drafts maximum) **only after** external source verification sprint names concrete candidates for `de_core_mos2` and/or `sulfur_element_term_record`. Still **no** registry edits unless execution sprint chartered. Run guardrail + corpus L1 before and after.

See `HUMAN_SOURCE_REVIEW_NEXT_ACTIONS_WAVE_1.md`.

---

*Sprint 5N-D — Human Candidate Source Review Wave 1 Report*
