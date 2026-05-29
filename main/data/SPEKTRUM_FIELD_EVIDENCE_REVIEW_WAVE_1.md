# Spektrum Field Evidence Review — Wave 1

**Sprint:** 5N-K  
**Scope:** Evidence basis for Spektrum bibliographic field verification on `de_core_mos2`  
**Date:** 2026-05-29  
**Status:** Field evidence review only — **not executed**, **not approved**

---

## Field-by-field evidence notes

### proposed_source_id

| Aspect | Detail |
| --- | --- |
| Proposed value | `SRC-SPEKTRUM-MOS2-DE` |
| Evidence | Sprint **5N-I** proposal draft; consistent with registry `source_id` naming patterns |
| Classification | **verified** (governance label) |
| Registry presence | **0** — label not inserted |

### source_label

| Aspect | Detail |
| --- | --- |
| Proposed value | Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid |
| Evidence | Named candidate intake (**5N-G**); human verification **`primary_candidate_verified_for_later_proposal`** (**5N-H**) |
| Classification | **verified** (label identity) |

### source_family

| Aspect | Detail |
| --- | --- |
| Proposed value | German specialist chemistry reference lexicon |
| Evidence | 5N-H role classification; 5N-I proposal draft family statement |
| Classification | **verified** |

### authority_class

| Aspect | Detail |
| --- | --- |
| Proposed value | `authoritative_dictionary` / `chemistry_dictionary_authority` (DE) |
| Evidence | `doctrine/SOURCE_POLICY.md` approved category; 5N-H authority fit review |
| Classification | **verified** |

### language

| Aspect | Detail |
| --- | --- |
| Proposed value | `de` |
| Evidence | `de_core_mos2` route locale; DE draft page language |
| Classification | **verified** |

### route_relationship

| Aspect | Detail |
| --- | --- |
| Proposed value | Primary route `de_core_mos2` |
| Evidence | `routes.json` route_id match; content file path confirmed |
| Classification | **verified** |

### claim_boundary_scope

| Aspect | Detail |
| --- | --- |
| Proposed scope | DE MoS2 compound naming; lexical/document-language within lexicon entry |
| Forbidden scope | Market, safety prescriptive, medical, procurement, EN-only authority, universal suffix rules |
| Evidence | 5N-I proposal draft; 5N-J execution readiness review |
| Classification | **verified** (governance scope — not claim approval) |

### author_or_organization

| Aspect | Detail |
| --- | --- |
| Proposed value | *(blank)* |
| Evidence | **None** in repository — no human-confirmed author/editor organization artifact |
| Classification | **unverified**; **must_remain_blank**; **requires_direct_source_access** |

### publisher

| Aspect | Detail |
| --- | --- |
| Proposed value | *(blank)* |
| Evidence | **None** in repository — no confirmed publisher imprint |
| Classification | **unverified**; **must_remain_blank**; **requires_direct_source_access** |

### publication_date

| Aspect | Detail |
| --- | --- |
| Proposed value | *(blank)* |
| Evidence | **None** in repository — no confirmed publication or access date |
| Classification | **unverified**; **must_remain_blank**; **requires_direct_source_access** |

### url_or_doi

| Aspect | Detail |
| --- | --- |
| Proposed value | *(blank)* |
| Evidence | **None** in repository — no verified locator; no raw URLs added in 5N-K documentation |
| Classification | **unverified**; **must_remain_blank**; **requires_direct_source_access** |

### edition

| Aspect | Detail |
| --- | --- |
| Proposed value | *(blank)* |
| Evidence | **None** in repository — no confirmed edition/volume identity |
| Classification | **unverified**; **must_remain_blank**; **requires_direct_source_access** |

### page_or_entry_citation

| Aspect | Detail |
| --- | --- |
| Proposed value | *(blank)* |
| Evidence | **None** in repository — no confirmed lexicon entry locator |
| Classification | **unverified**; **must_remain_blank**; **requires_direct_source_access** |

### access_method

| Aspect | Detail |
| --- | --- |
| Required method | Direct human access to Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid entry |
| Current status | **Not performed** in repository artifacts |
| Classification | **requires_direct_source_access** |

### verification_status

| Aspect | Detail |
| --- | --- |
| Overall posture | Field verification **incomplete** — execution **blocked** |
| Verified field count | **7** governance fields |
| Unverified field count | **6** bibliographic fields |
| Classification | **unverified**; **rejected_if_unverified** for registry execution |

---

## Verified governance fields

Governance-known without bibliographic invention:

- `SRC-SPEKTRUM-MOS2-DE` (label)
- Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid (source label)
- German specialist chemistry reference lexicon (source family)
- `authoritative_dictionary` (authority class)
- `de` (language)
- `de_core_mos2` (route relationship)
- Claim boundary scope and forbidden uses

---

## Verified label fields

| Label field | Status |
| --- | --- |
| Entry subject | Molybdän(IV)-sulfid — **verified** (intake identity) |
| Lexicon series name | Spektrum Lexikon der Chemie — **verified** (named candidate) |
| Compound context | MoS2 specialist DE terminology page — **verified** (route scope) |

---

## Unverified bibliographic fields

All six bibliographic fields required for safe registry execution remain **unverified**:

- `author_or_organization`
- `publisher`
- `publication_date`
- `url_or_doi`
- `edition`
- `page_or_entry_citation`

---

## Fields requiring direct source access

Bibliographic verification **cannot** complete from governance documentation alone. A human with direct access to the Spektrum lexicon entry must confirm publisher, edition, date, entry citation, and access locator (if applicable).

Recommended: Sprint **5N-L** direct source access bibliographic capture.

---

## Fields that must remain blank

Until direct source access verification supplies confirmed values, all unverified bibliographic fields **must remain blank**. No placeholder strings, inferred imprints, or approximate dates.

---

## Fields that must not be invented

- DOI, ISBN, ISSN, or fabricated URLs
- Edition, volume, or page numbers
- Author, editor, or organization names not confirmed
- Publisher details not confirmed from source
- Citation strings implying verification not performed

---

## Why field evidence review does not approve the source

| Gate | Status |
| --- | --- |
| Bibliographic bundle | **Incomplete** |
| Registry row | **0** inserted |
| `verified` status | **Not assigned** |
| Human sign-off on bibliographic values | **Not performed** |

Evidence review documents verification posture — **not** approval.

---

## Why field evidence review does not execute the registry entry

| Evidence review (5N-K) | Execution (future) |
| --- | --- |
| Documents verified vs unverified fields | Writes `source_registry.json` |
| Leaves bibliographic fields blank | Populates verified bibliographic values |
| No registry mutation | Inserts registry row |
| No approval | May assign `verified` status with sign-off |

---

## Why [SOURCE REQUIRED] markers remain

Draft factual lines on `de_core_mos2` require audited source linkage after registry execution. Field evidence review confirms metadata gaps — does not resolve draft assertions or remove markers.

---

## Related documents

- `SPEKTRUM_BIBLIOGRAPHIC_FIELD_MATRIX_WAVE_1.md`
- `SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_ENTRY_FIELD_REVIEW_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
