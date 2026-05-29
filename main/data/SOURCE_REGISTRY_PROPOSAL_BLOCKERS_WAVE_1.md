# Source Registry Proposal Blockers — Wave 1

**Sprint:** 5N-F  
**Date:** 2026-05-29

---

## Blockers for de_core_mos2

| Blocker | Status | Effect |
| --- | --- | --- |
| No named DE specialist lexicon candidate | **Active** | Blocks proposal drafting and registry execution |
| Human external verification incomplete | **Active** | Blocks transition from readiness to proposal draft |
| `[SOURCE REQUIRED]` markers unresolved | **Active** | Blocks source-locking and publication |
| Claim registries inactive | **Active** | Blocks claim approval |
| No registry row | **Active** | Blocks verified source linkage |
| Route publication lock | **Active** | Route `planned`; draft non-public |

**Conditional path:** Proposal readiness **conditional** — blockers allow documentation and future proposal drafting after named candidate intake; they **prevent** registry execution now.

---

## Blockers for sulfur_element_term_record

| Blocker | Status | Effect |
| --- | --- | --- |
| No named scientific database candidate | **Active** | Blocks proposal readiness and drafting |
| Database verification incomplete | **Active** | `needs_database_source_verification` |
| 5N-E proposal allowed next = **no** | **Active** | `do_not_prepare_proposal_yet` |
| Human external verification incomplete | **Active** | No verified element-record tier |
| `[SOURCE REQUIRED]` markers unresolved | **Active** | Blocks source-locking and publication |
| Claim registries inactive | **Active** | Blocks claim approval |
| No registry row | **Active** | Blocks verified source linkage |

**Status:** **Blocked from proposal now** until database candidate named and verified.

---

## Blockers caused by missing named source candidates

- **0** human-verified named candidates in repository for either draft
- Evidence family identified (5N-E) is **not** a named candidate
- Proposal drafting requires named intake sprint before bibliographic proposal lines
- Registry execution requires named candidate + full verified bibliographic details

---

## Blockers caused by missing database candidate

Applies to `sulfur_element_term_record` only:

- Element identity requires `scientific_database_authority`
- No government/scientific element-record database candidate named
- Readiness status: `needs_scientific_database_candidate_first`
- Cannot prepare proposal draft until database naming track completes

---

## Blockers caused by source policy uncertainty

| Draft | Policy uncertainty |
| --- | --- |
| `de_core_mos2` | **None** — `authoritative_dictionary` category exists |
| `sulfur_element_term_record` | **None** — `government_scientific_database` category exists |

Policy extension blockers apply to other drafts (e.g., `de_core_biogenic_lang`) — **not** these two targets in 5N-F.

---

## Blockers caused by claim registry inactivity

- **6** claim registries **inactive**
- **0** approved claims
- No claim may be approved without verified source linkage
- Proposal readiness does not activate registries

---

## Blockers caused by publication locks

- All **126** routes `planned`
- No route `indexable: true`, `in_sitemap: true`, or `in_navigation: true`
- Drafts `non_public`
- Quality Gate not satisfied

---

## Blockers caused by unresolved [SOURCE REQUIRED] markers

Both drafts retain markers on factual lines:

- Lexical / document form lines
- Source-locking incomplete per draft frontmatter
- Marker removal requires audited registry linkage — not proposal readiness alone

---

## Blockers caused by lack of human verification

| Verification gap | Drafts affected |
| --- | --- |
| Named lexicon candidate | `de_core_mos2` |
| Named database candidate | `sulfur_element_term_record` |
| Scope boundary confirmation | Both |
| Marker mapping | Both |
| Rejection-rule clearance | Both |

---

## Why blockers do not prevent documentation but do prevent registry execution

| Activity | Blockers prevent? |
| --- | --- |
| Readiness documentation (5N-F) | **No** — this sprint |
| Proposal drafting (future) | **Yes** — until named candidate for MoS2; always for sulfur until database named |
| Registry row writes | **Yes** — all drafts |
| Claim approval | **Yes** — all drafts |
| Route publication | **Yes** — all drafts |
| Marker removal | **Yes** — all drafts |

Documentation records **gates** without bypassing them. Registry execution remains a **separate chartered sprint** after blockers clear for a given draft.

---

*Sprint 5N-F — Source Registry Proposal Blockers Wave 1*
