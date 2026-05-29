# Source Registry Entry Field Review — Wave 1

**Sprint:** 5N-J  
**Scope:** Proposed Spektrum row for `de_core_mos2`  
**Date:** 2026-05-29

---

## Proposed source entry fields

Future execution **may** populate a Spektrum row matching existing registry schema patterns (see seeded rows in `source_registry.json`). Proposed field set for **`SRC-SPEKTRUM-MOS2-DE`**:

| Field | Proposed value (readiness) | Verification |
| --- | --- | --- |
| `source_id` | `SRC-SPEKTRUM-MOS2-DE` | **Known** — governance label |
| `category` | `authoritative_dictionary` | **Known** — policy-aligned |
| `title` | Molybdän(IV)-sulfid (lexicon entry subject) | **Known** — intake/verification identity |
| `language` | `de` | **Known** |
| `author_or_organization` | *(blank — unverified)* | **Unverified** |
| `publisher` | *(blank — unverified)* | **Unverified** |
| `publication_date` | *(blank — unverified)* | **Unverified** |
| `url` or `doi` | *(blank — unverified)* | **Unverified** |
| `status` | `verified` (future only) | **Not assigned now** |
| `source_lock_status` | `candidate` (future) | **Not assigned now** |
| `use_for` | DE MoS2 compound naming; lexical/document-language on `de_core_mos2` | **Known** — governance scope |
| `do_not_use_for` | market; safety prescriptive; medical; procurement; EN-only authority | **Known** — policy |
| `linked_claims` | `[]` | **Empty** — no approved claims |
| `last_reviewed` | *(at execution only)* | **Unverified** |
| `notes` | Execution-readiness row — bibliographic fields pending human verification | **Known** — governance |

---

## Required fields for source_registry.json

Per `doctrine/SOURCE_POLICY.md`:

| Required field | Readiness status |
| --- | --- |
| `source_id` | **Known** (proposed label) |
| `title` | **Known** (entry subject identity) |
| `author_or_organization` | **Unverified — must remain blank** |
| `publisher` | **Unverified — must remain blank** |
| `publication_date` | **Unverified — must remain blank** |
| `url` or `doi` | **Unverified — must remain blank** |
| `category` | **Known** |
| `linked_claims` | **Known empty** |

**Conclusion:** Required bibliographic fields are **incomplete** — execution **blocked**.

---

## Optional fields

| Field | Notes |
| --- | --- |
| `source_lock_status` | Set at execution if schema used |
| `use_for` / `do_not_use_for` | Recommended for strict-registry discipline |
| `risk_notes` | Optional at execution |
| `last_reviewed` | Set at execution with human review date |

---

## Known fields

Governance-known without bibliographic invention:

- Proposed `source_id`, `category`, `language`, `title` (entry subject)
- Route relationship: `de_core_mos2`
- Authority class: `authoritative_dictionary` / DE lexicon
- Claim boundary scope and forbidden uses
- Supporting candidate rejection posture

---

## Unknown fields

Must be supplied by human with direct source access at verification/execution:

- Publisher imprint and edition identity
- Publication or access date
- Author/editor organization as required by policy
- Verifiable `url` or `doi` if applicable
- Confirmation that live entry covers proposed draft lines

---

## Fields that must remain blank if not verified

| Field | Rule |
| --- | --- |
| `author_or_organization` | Blank until human-verified |
| `publisher` | Blank until human-verified |
| `publication_date` | Blank until human-verified |
| `url` / `doi` | Blank until human-verified |
| Edition / page | Omit — do not invent |

Placeholder or fabricated values are **forbidden**.

---

## Fields that must not be invented

- DOI, ISBN, ISSN
- Edition number, volume, page range
- Author, editor, translator names
- Publisher address or imprint details not confirmed
- Access dates not confirmed
- Citation strings implying verification not performed

---

## Proposed route relationship

| Field | Value |
| --- | --- |
| Primary route | `de_core_mos2` |
| Content file | `main/content/de/pages/terminology/molybdenum-disulfide.md` |
| Marker lines (future audit) | Lexikalische Form; Chemische / Dokumentform — subject to entry scope confirmation |

---

## Proposed authority class

`authoritative_dictionary` (DE) — `chemistry_dictionary_authority` tier.

---

## Proposed source family

German specialist chemistry reference lexicon — Spektrum Lexikon der Chemie.

---

## Future execution requirements

1. All required `SOURCE_POLICY` fields populated with **human-verified** values.
2. Readiness upgraded from **`execution_blocked_pending_field_verification`** to **`execution_ready_after_field_verification`**.
3. Execution sprint charter + human sign-off.
4. Guardrail + L1 **PASS** on registry diff.
5. No `[SOURCE REQUIRED]` removal in execution sprint.
6. Claim boundaries registered before claim approval — separate track.

---

## Why field review is not source execution

| Field review (5N-J) | Execution (future) |
| --- | --- |
| Documents verification gaps | Writes `source_registry.json` |
| Leaves bibliographic fields blank | Populates verified fields |
| No registry mutation | Inserts registry row |
| No approval | May assign `verified` status with sign-off |

Sprint **5N-J** completes **field readiness assessment** — not registry insertion.

---

## Related documents

- `SPEKTRUM_EXECUTION_READINESS_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_EXECUTION_READINESS_MATRIX_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
