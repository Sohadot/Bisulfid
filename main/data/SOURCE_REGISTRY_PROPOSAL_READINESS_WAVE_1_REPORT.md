# Source Registry Proposal Readiness Wave 1 — Report

**Sprint:** 5N-F  
**Date:** 2026-05-29  
**Branch:** `claude/sprint-5n-f-source-registry-proposal-readiness-wave-1`

---

## Why this sprint exists

Sprint **5N-E** completed external source verification for `de_core_mos2` and `sulfur_element_term_record`, identifying evidence families and human verification gaps. Sprint **5N-F** documents **source registry proposal readiness** — whether either draft may later enter a tightly scoped **proposal drafting** sprint — without registering sources, approving claims, or modifying content.

---

## Why proposal readiness comes after external source verification

External verification (5N-E) classified authority classes and evidence posture. Proposal readiness answers a narrower question: **given verification findings, is proposal drafting permitted next, and under what conditions?** Readiness documentation still precedes any registry row or proposal draft with bibliographic details.

---

## Why proposal readiness still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Readiness ≠ execution | Documentation of gates is not registry entry |
| No named candidates | **0** human-verified named source candidates in repository |
| Guardrail gate | Sprint **5N-B** runtime must **PASS** |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited linkage |

---

## Relationship to Sprint 5N-E

This sprint inherits external verification status, authority class, and `source registry proposal allowed next` flags from `EXTERNAL_SOURCE_VERIFICATION_MATRIX_WAVE_1.md` for both target drafts.

---

## Relationship to Sprint 5N-D

Human review (5N-D) established acceptance/rejection criteria and future registry actions. Proposal readiness applies those criteria to the post-verification posture without treating human review as approval.

---

## Relationship to Sprint 5N-B guardrail automation

Pre-flight and post-sprint: guardrail + corpus L1 **PASS**. Readiness documents must not introduce approval language, raw URLs, or registry-execution implications.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Current route count (`routes.json`) | **126** |
| Proposal-readiness drafts | **2** (1 conditional, 1 blocked) |
| Registry entries added | **0** |
| Publication-ready | **0** |

Proposal readiness advances **governance sequencing** without publication eligibility.

---

## Files reviewed

- Sprint **5N-E** external verification documents (6 files)
- Sprint **5N-D** human review documents (acceptance/rejection criteria, matrix)
- Sprint **5N-C** discovery matrix
- Sprint **5N-A** proposal and evidence matrices
- Sprint **5N-B** guardrail reports
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- **2** target draft content files (read-only)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-E | **Yes** |
| Guardrail runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Target drafts exist | **2/2** |
| Match `routes.json` | **2/2** |
| draft / non_public / non-indexable | **2/2** |
| Registry unchanged pre-sprint | **Yes** |
| Claims unchanged pre-sprint | **Yes** |

---

## Selected draft count

**2** drafts (1 primary conditional, 1 secondary blocked).

---

## Selected route_id list

```
de_core_mos2
sulfur_element_term_record
```

---

## Current route count from routes.json

**126** routes (all `planned`; read from `routes.json` `routes` array length, 2026-05-29).

---

## Selected draft status

| route_id | content_file | route status | draft posture |
| --- | --- | --- | --- |
| `de_core_mos2` | `main/content/de/pages/terminology/molybdenum-disulfide.md` | `planned` | draft / non_public / indexable false / in_sitemap false |
| `sulfur_element_term_record` | `main/content/en/pages/terminology/sulfur-element.md` | `planned` | draft / non_public / indexable false / in_sitemap false |

---

## Proposal-readiness methodology

1. Inherit 5N-E external verification status, authority class, and proposal-allowed-next flags.
2. Read draft content for marker scope (read-only).
3. Classify proposal readiness status, proposal posture, and registry execution status using governed enums.
4. Distinguish proposal readiness, registry execution, source approval, source-locking, claim approval, and publication readiness.
5. Document blockers and drafting criteria without inventing bibliographic details.
6. Run guardrail + corpus L1 runtimes before and after documentation.

---

## Registry proposal principles

- **One draft, one scoped proposal** — proposals map to specific marker lines and authority tier only.
- **Named candidate required** — proposal drafting requires human-verified named source class; not evidence family alone.
- **Proposal ≠ execution** — drafting sprint produces proposal documents; execution sprint writes registry rows.
- **Proposal ≠ approval** — proposal readiness does not mark sources approved or verified.
- **Authority class alignment** — DE chemistry dictionary for MoS2; scientific database for element record — not interchangeable.

---

## Registry execution boundary

| Stage | Allowed in 5N-F |
| --- | --- |
| Proposal readiness documentation | **Yes** |
| Proposal draft authoring (future sprint) | **Conditional** — `de_core_mos2` only after named DE lexicon |
| Registry row writes | **No** |
| Claim activation | **No** |
| Marker removal | **No** |
| Route publication | **No** |

Registry execution requires a **separate chartered sprint** after proposal draft, human charter, and guardrail **PASS**.

---

## What source registry proposal readiness means in this sprint

- Classifies whether each draft may **later** enter proposal **drafting**
- Documents conditions, blockers, and criteria for that transition
- Identifies `de_core_mos2` as the **only conditional** readiness candidate
- Keeps `sulfur_element_term_record` **blocked** until database candidate named

---

## What source registry proposal readiness does not mean in this sprint

- Does **not** register sources or modify `source_registry.json`
- Does **not** approve sources, claims, or markers
- Does **not** source-lock any page
- Does **not** make any page publication-ready
- Does **not** add raw URLs or invented bibliographic details
- Does **not** treat readiness as verified evidence

---

## Readiness findings by draft

### `de_core_mos2` (primary — conditional)

| Field | Finding |
| --- | --- |
| External verification status (5N-E) | `human_external_verification_required` |
| Authority class (5N-E) | `chemistry_dictionary_authority` |
| Proposal allowed next (5N-E) | **Yes** — conditional |
| Proposal readiness status | `proposal_readiness_conditional` |
| Proposal posture | `can_prepare_proposal_draft_after_named_source` |
| Registry execution status | `registry_execution_requires_separate_sprint` |
| Named source candidate present | **No** |

**Summary:** Only draft with conditional proposal-readiness path. Human must name and verify DE specialist lexicon candidate before proposal drafting sprint. Registry execution remains blocked.

### `sulfur_element_term_record` (secondary — blocked)

| Field | Finding |
| --- | --- |
| External verification status (5N-E) | `needs_database_source_verification` |
| Authority class (5N-E) | `scientific_database_authority` |
| Proposal allowed next (5N-E) | **No** |
| Proposal readiness status | `needs_scientific_database_candidate_first` |
| Proposal posture | `do_not_prepare_proposal_yet` |
| Registry execution status | `registry_execution_not_allowed` |
| Named source candidate present | **No** |

**Summary:** Blocked from proposal readiness until human names and verifies scientific database candidate for element-record tier.

---

## Why de_core_mos2 is the only conditional proposal-readiness candidate

| Factor | `de_core_mos2` | `sulfur_element_term_record` |
| --- | --- | --- |
| 5N-D human review | `review_candidate_ready` | `needs_scientific_database_review` |
| 5N-E proposal allowed next | **Yes** (conditional) | **No** |
| Evidence family gap | Named DE lexicon only | Named database authority |
| Authority path | Chemistry dictionary — scoped | Scientific database — primary required |
| Policy extension | **No** | N/A |

`de_core_mos2` has the lowest governance gap: evidence family identified, authority class clear, no policy extension required — but **still requires named human-verified candidate** before proposal drafting.

---

## Why sulfur_element_term_record remains blocked until a database candidate is named

Element-level identity requires **scientific database authority**. Sprint **5N-E** found evidence family identified but **no** named database candidate and **no** human external verification complete. Proposal drafting cannot begin until:

1. Human names government/scientific element-record database candidate
2. Human verifies category under `SOURCE_POLICY.md`
3. Acceptance/rejection criteria clearance
4. Guardrail **PASS**

Until then: `do_not_prepare_proposal_yet`.

---

## Why no source entries were added

Proposal readiness documents **gates and sequencing** only. No candidate has human-verified bibliographic details suitable for registry rows.

---

## Why source_registry.json was not modified

Registry remains **inactive** with **14** seeded candidates and **0** new verified entries.

---

## Why no claims were approved

No verified source linkage exists. Claim registries remain **inactive** with **0** approved claims.

---

## Why terminology_claims.json was not modified

Claim approval requires verified sources. This sprint produces governance documentation only.

---

## Why no content pages were modified

Content edits are out of scope. Draft posture and `[SOURCE REQUIRED]` markers are preserved.

---

## Why [SOURCE REQUIRED] markers remain

Markers indicate open factual lines needing registry work. Proposal readiness does not satisfy marker removal criteria.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, and out of sitemap/navigation.

---

## Publication blocker summary

| Blocker | `de_core_mos2` | `sulfur_element_term_record` |
| --- | --- | --- |
| Named verified candidate | **Missing** | **Missing** |
| Proposal draft complete | **No** | **N/A — blocked** |
| Registry row | **0** | **0** |
| Approved claims | **0** | **0** |
| Source-locking complete | **No** | **No** |
| Publication-ready | **No** | **No** |

---

## Recommended next sprint

**Sprint 5N-G — Named source candidate intake wave 1** for `de_core_mos2` (human names and documents DE specialist lexicon candidate class externally) **or** parallel **source registry proposal drafting** sprint **only after** named candidate intake completes. `sulfur_element_term_record`: **database candidate naming track** — remain blocked from proposal drafting until complete.

Still **no** `source_registry.json` row writes unless separate execution sprint chartered.

Run guardrail + corpus L1 before and after.

---

*Sprint 5N-F — Source Registry Proposal Readiness Wave 1 Report*
