# Spektrum Direct Source Access Evidence Review — Wave 1

**Sprint:** 5N-L  
**Scope:** Direct access evidence for Spektrum bibliographic capture on `de_core_mos2`  
**Date:** 2026-05-29  
**Status:** Direct access evidence review only — **not executed**, **not approved**

---

## Direct access evidence notes

Sprint **5N-L** reviewed the repository for human-confirmed direct-access capture artifacts tied to Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid. **No such artifact exists** in governed repository files at capture review time.

| Evidence type searched | Found |
| --- | --- |
| Signed bibliographic capture record | **No** |
| Human-verified edition/page confirmation | **No** |
| Publisher imprint confirmation from direct inspection | **No** |
| Author/editor organization confirmation | **No** |
| Verified access locator (if applicable) | **No** |

**Direct access classification:** **`direct_access_not_available`** in repository.

---

## Fields captured from direct source access

**None.** No field met **`field_verified_from_source`** threshold.

| Field | Capture result |
| --- | --- |
| `author_or_organization` | Not captured — blank |
| `publisher` | Not captured — blank |
| `publication_date` | Not captured — blank |
| `url_or_doi` | Not captured — blank |
| `edition` | Not captured — blank |
| `page_or_entry_citation` | Not captured — blank |

---

## Fields not visible from direct source access

All six bibliographic target fields are **`field_not_visible`** in repository because direct access capture was not performed with a depositable artifact:

- `author_or_organization`
- `publisher`
- `publication_date`
- `url_or_doi`
- `edition`
- `page_or_entry_citation`

---

## Fields requiring additional access

| Field | Additional access required |
| --- | --- |
| All six bibliographic fields | Human with physical or licensed digital access to Spektrum entry must inspect and confirm values |
| `access_method` | Direct inspection of Molybdän(IV)-sulfid lexicon entry — **not completed** in repository |

Recommended: Sprint **5N-M** verified bibliographic artifact capture with human sign-off.

---

## Fields that must remain blank

Until verified capture artifact supplies confirmed values, all six bibliographic fields **must remain blank**. Partial capture without full required-field confirmation does not permit registry execution.

---

## Fields that must not be invented

- DOI, ISBN, ISSN, or fabricated URLs
- Edition, volume, or page numbers
- Author, editor, or organization names
- Publisher details not confirmed from direct inspection
- Publication or access dates
- Citation strings implying verification not performed

Sprint **5N-L** added **0** invented values.

---

## Why direct access capture does not approve the source

| Gate | Status |
| --- | --- |
| Bibliographic capture | **Incomplete** — 0 fields captured |
| Registry row | **0** inserted |
| `verified` status | **Not assigned** |
| Human sign-off on captured values | **Not performed** |

Capture documents access posture — **not** approval.

---

## Why direct access capture does not execute the registry entry

| Direct access capture (5N-L) | Execution (future) |
| --- | --- |
| Documents capture availability and field visibility | Writes `source_registry.json` |
| Leaves bibliographic fields blank when not captured | Populates verified bibliographic values |
| No registry mutation | Inserts registry row |
| No approval | May assign `verified` status with sign-off |

---

## Why [SOURCE REQUIRED] markers remain

Draft factual lines on `de_core_mos2` require audited source linkage after registry execution. Incomplete capture confirms metadata gaps — does not resolve draft assertions or remove markers.

---

## Related documents

- `SPEKTRUM_DIRECT_SOURCE_ACCESS_FIELD_MATRIX_WAVE_1.md`
- `SPEKTRUM_CAPTURED_FIELD_GAP_REVIEW_WAVE_1.md`
- `SPEKTRUM_BIBLIOGRAPHIC_FIELD_MATRIX_WAVE_1.md`
- `doctrine/SOURCE_POLICY.md`
