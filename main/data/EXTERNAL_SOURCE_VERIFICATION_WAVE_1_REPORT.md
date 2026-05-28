# External Source Verification Wave 1 — Report

**Sprint:** 5N-E  
**Date:** 2026-05-28  
**Branch:** `claude/sprint-5n-e-external-source-verification-wave-1`

---

## Why this sprint exists

Sprint **5N-D** completed human candidate source review for **5** drafts and recommended **external source verification** for the two highest-priority cases: `de_core_mos2` and `sulfur_element_term_record`. Sprint **5N-E** documents external verification posture — evidence families, authority classes, acceptance/rejection boundaries, and blockers — without registering sources, approving claims, or modifying content.

---

## Why external source verification comes after human candidate review

Human review (5N-D) classified candidate **families**, suitability, and future registry actions. External verification closes the **naming and evidence-class gap**: what specific authority tier a human must confirm outside the repository, what evidence would be acceptable or rejected, and whether either draft may proceed later to a source registry **proposal** sprint — still without registry rows.

---

## Why verification still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Verification ≠ registration | Naming evidence class is not a verified registry entry |
| Guardrail gate | Sprint **5N-B** runtime must **PASS** |
| No fabricated bibliographic lines | Humans must verify named candidates externally |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited linkage |

---

## Relationship to Sprint 5N-D

This sprint verifies exactly the **2** priority drafts from `HUMAN_CANDIDATE_SOURCE_REVIEW_MATRIX_WAVE_1.md`, inheriting human review status, discovery source family, and future registry action flags.

---

## Relationship to Sprint 5N-C

Sprint **5N-C** identified candidate source families and search targets. Sprint **5N-E** evaluates whether those families can support future registry proposals after human external verification — not whether they are verified now.

---

## Relationship to Sprint 5N-B guardrail automation

Pre-flight and post-sprint: guardrail + corpus L1 **PASS**. Verification documents must not introduce approval language, raw URLs (unless SOURCE_POLICY allows — it does not for these docs), or registry-edit implications.

---

## Relationship to Sprint 5M source mapping

Sprint **5M** mapped source gaps across the corpus. External verification confirms which gaps on the **2** priority drafts remain blocked by missing human-verified naming, insufficient evidence class, or authority-tier mismatch.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Current route count (`routes.json`) | **126** |
| External verification drafts | **2** |
| Registry entries added | **0** |
| Publication-ready | **0** |

External verification advances **governance readiness** without publication eligibility or governed-page count increment.

---

## Files reviewed

- Sprint **5N-D** human review documents (6 files)
- Sprint **5N-C** discovery documents (6 files)
- Sprint **5N-A** proposal and evidence matrices
- Sprint **5N-B** guardrail reports
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- **2** selected draft content files (read-only)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-D | **Yes** |
| Guardrail runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Selected drafts exist | **2/2** |
| Match `routes.json` | **2/2** |
| draft / non_public / non-indexable | **2/2** |
| Registry unchanged pre-sprint | **Yes** |
| Claims unchanged pre-sprint | **Yes** |

---

## Selected draft count

**2** drafts.

---

## Selected route_id list

```
de_core_mos2
sulfur_element_term_record
```

---

## Current route count from routes.json

**126** routes (all `planned`; read from `routes.json` `routes` array length, 2026-05-28).

---

## Selected draft status

| route_id | content_file | route status | draft posture |
| --- | --- | --- | --- |
| `de_core_mos2` | `main/content/de/pages/terminology/molybdenum-disulfide.md` | `planned` | draft / non_public / indexable false / in_sitemap false |
| `sulfur_element_term_record` | `main/content/en/pages/terminology/sulfur-element.md` | `planned` | draft / non_public / indexable false / in_sitemap false |

---

## Verification methodology

1. Inherit human review status and discovery family from Sprint **5N-D** / **5N-C** matrices.
2. Read draft content for marker scope and page role (read-only).
3. Map required authority class against `SOURCE_POLICY.md` approved categories.
4. Classify external verification status and evidence posture using governed enums.
5. Document acceptable and unacceptable evidence classes without inventing bibliographic details.
6. Record blockers for registry entry, claim approval, and publication.
7. Run guardrail + corpus L1 runtimes before and after documentation.

**Limitation:** Exact external verification of named publisher/database/lexicon instances cannot be performed safely in this environment without raw URLs or invented citation lines. This sprint documents **evidence family + human external verification required** instead.

---

## External source authority principles

- **Primary authority tier must match page role** — element identity requires scientific database authority; compound naming requires dictionary or nomenclature authority as scoped.
- **Teaching sources are supporting context only** — never sole formal authority for element identity or systematic names.
- **Dictionary authority is class-bound** — mineral/compound naming support does not extend to market, safety, or procurement claims.
- **Formal nomenclature is separate** — database element records do not substitute for IUPAC or nomenclature-standard lines where asserted.
- **German lexical authority applies to DE surface forms** — EN element record authority does not automatically govern DE compound pages.

---

## Evidence acceptance principles

Acceptable evidence **classes** (after human external verification names a specific candidate):

| Class | Accept when |
| --- | --- |
| Government/scientific database | Stable element record tier; no safety/market fields; category fits SOURCE_POLICY |
| Authoritative chemistry dictionary | Compound/mineral naming scope only; named publisher; no application-market framing |
| Academic teaching reference | Supporting terminology context only; paired with stronger tier for formal lines |
| Formal nomenclature standard | Systematic names only; supporting tier where dictionary covers lexical variants |

---

## Evidence rejection principles

Reject evidence when it matches `HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md` or:

- Unsourced web content, AI summaries, commercial pages without authority
- Safety/medical/procurement/market content
- Teaching used as sole formal authority
- Dictionary used as chemical identity authority beyond its class
- Lubricant/application market framing for MoS2
- Element database treated as authority for all sulfur terminology pages

---

## What external source verification means in this sprint

- Classifies **external verification status** and **evidence posture** per draft
- Identifies **authority class** required and **candidate evidence type** (family, not fabricated citation)
- States what a **human must verify next** outside the repository
- Determines whether either draft may **later** enter a source registry **proposal** sprint
- Documents risks and blockers

---

## What external source verification does not mean in this sprint

- Does **not** register sources or modify `source_registry.json`
- Does **not** approve sources, claims, or markers
- Does **not** source-lock any page
- Does **not** make any page publication-ready
- Does **not** add raw URLs or invented DOI/ISBN/edition/author/publisher/date details
- Does **not** treat verification documentation as verified evidence

---

## Verification findings by draft

### `de_core_mos2`

| Field | Finding |
| --- | --- |
| Human review status (5N-D) | `review_candidate_ready` |
| Discovery family (5N-C) | `chemistry_dictionary_reference` |
| External verification status | `human_external_verification_required` |
| Source evidence posture | `evidence_family_identified` |
| Authority class | `chemistry_dictionary_authority` |
| Future action | `prepare_source_registry_proposal_later` (after human names DE specialist lexicon) |
| Registry proposal allowed next | **Yes** — conditional on human naming acceptable DE lexicon candidate |
| Blockers | No named verified lexicon yet; formal authority lines still need human confirmation; markers remain |

**Summary:** Lowest-gap draft. DE specialist chemistry lexicon class is **potentially suitable** for future registry proposal after human externally verifies a named candidate. Block lubricant/application market drift.

### `sulfur_element_term_record`

| Field | Finding |
| --- | --- |
| Human review status (5N-D) | `needs_scientific_database_review` |
| Discovery family (5N-C) | `scientific_database_reference` |
| External verification status | `needs_database_source_verification` |
| Source evidence posture | `evidence_family_identified` |
| Authority class | `scientific_database_authority` (primary); `academic_support_only` (secondary) |
| Future action | `run_human_external_verification_first` |
| Registry proposal allowed next | **No** — human must name and verify element-record database tier first |
| Blockers | No named database authority; teaching cannot substitute; markers remain |

**Summary:** Element-record database tier is the correct primary family. Human must name government/scientific database candidate and confirm element-record scope before registry proposal.

---

## Source families that may proceed later

| route_id | Family | Condition |
| --- | --- | --- |
| `de_core_mos2` | Authoritative dictionary / DE specialist chemistry lexicon | Human names candidate; compound naming scope only; no lubricant market framing |
| `sulfur_element_term_record` | Government/scientific database | Human names element-record database; teaching as supporting context only |

---

## Source families needing stronger verification

| route_id | Gap |
| --- | --- |
| `de_core_mos2` | Named DE lexicon instance; formal nomenclature boundary for systematic names if asserted |
| `sulfur_element_term_record` | Named database instance; marker-to-record mapping; confirmation database tier is not misused for non-element claims |

---

## Blocked or insufficient evidence classes

| Class | Applies to | Reason |
| --- | --- | --- |
| Academic teaching alone | Both | Insufficient as sole authority |
| Unsourced web / AI summaries | Both | Rejected by policy |
| Industrial lubricant market sources | `de_core_mos2` | Out of scope; market drift risk |
| Safety SDS / medical / procurement | Both | Permanently blocked content classes |
| Generic “chemistry website” without authority | Both | No named publisher/database |

---

## Why no source entries were added

External verification documents **evidence posture** only. No candidate has been human-verified with named bibliographic details suitable for a registry row.

---

## Why source_registry.json was not modified

Registry remains **inactive** with **14** seeded candidates and **0** new verified entries. Verification sprint charter excludes registry execution.

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

Markers indicate open factual lines needing registry work. Verification documentation does not satisfy marker removal criteria.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, and out of sitemap/navigation.

---

## Publication blocker summary

| Blocker | Status |
| --- | --- |
| Verified source entries | **0** for both drafts |
| Approved claims | **0** |
| Source-locking complete | **No** |
| Human external verification | **Required** for both |
| Registry proposal (sulfur) | **Not ready** |
| Registry proposal (MoS2) | **Conditional** after human naming |
| Quality Gate / editorial signoff | **Not satisfied** |
| Publication-ready pages | **0** |

---

## Recommended next sprint

**Sprint 5N-F — Source registry proposal drafting wave 1** (maximum **1–3** drafts) **only after** humans externally verify and name acceptable candidates — prioritize `de_core_mos2` if DE specialist lexicon candidate is confirmed. Still **no** `source_registry.json` edits unless execution sprint chartered separately.

Run guardrail + corpus L1 before and after.

---

*Sprint 5N-E — External Source Verification Wave 1 Report*
