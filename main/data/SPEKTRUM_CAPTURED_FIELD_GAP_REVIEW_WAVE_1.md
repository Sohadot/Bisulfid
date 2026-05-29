# Spektrum Captured Field Gap Review — Wave 1

**Sprint:** 5N-L  
**Scope:** Captured field gap assessment for proposed Spektrum row on `de_core_mos2`  
**Date:** 2026-05-29

---

## Captured field gap summary

| Category | Available now | Unavailable now | Safe to omit at capture |
| --- | ---: | ---: | ---: |
| Governance fields (5N-K carry-forward) | **7** | **0** | **0** |
| Bibliographic fields captured (5N-L) | **0** | **6** | **0** |
| Capture metadata | **1** (access method documented) | **1** (verification incomplete) | **0** |

**Gap conclusion:** Governance fields sufficient for **future proposal carry-forward**. Bibliographic capture **insufficient** for registry execution.

---

## Fields available now

### Governance (verified Sprint 5N-K — unchanged)

| Field | Value | Status |
| --- | --- | --- |
| `proposed_source_id` | `SRC-SPEKTRUM-MOS2-DE` | **Verified** |
| `source_label` | Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid | **Verified** |
| `source_family` | German specialist chemistry reference lexicon | **Verified** |
| `authority_class` | `authoritative_dictionary` | **Verified** |
| `language` | `de` | **Verified** |
| `route_relationship` | `de_core_mos2` | **Verified** |
| `claim_boundary_scope` | Documented forbidden uses | **Verified** |

### Bibliographic (Sprint 5N-L capture)

**None captured.**

---

## Fields unavailable now

| Field | Gap | Blocker |
| --- | --- | --- |
| `author_or_organization` | Not captured | Direct access + artifact required |
| `publisher` | Not captured | Direct access + artifact required |
| `publication_date` | Not captured | Direct access + artifact required |
| `url_or_doi` | Not captured | Direct access + artifact required |
| `edition` | Not captured | Direct access + artifact required |
| `page_or_entry_citation` | Not captured | Direct access + artifact required |

All six are **`field_rejected_if_unverified`** for registry execution.

---

## Fields that can be omitted safely

At **capture documentation** stage (not execution):

| Field | Reason |
| --- | --- |
| `last_reviewed` | Set only at execution with human review date |
| `source_lock_status` | Assigned at execution if schema used |
| `risk_notes` | Optional at execution |

At **execution** stage, all required bibliographic fields **cannot** be omitted.

---

## Fields that cannot be omitted safely

At registry execution, all of the following must be populated with **verified captured** values:

- `author_or_organization`
- `publisher`
- `publication_date`
- `url` or `doi` (where applicable)
- Edition and entry citation strongly recommended for lexicon audit

**Current capture count: 0** — execution blocked.

---

## Fields that require additional access

| Field | Access requirement |
| --- | --- |
| All six bibliographic fields | Human direct inspection of Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid entry |
| Capture artifact | Governed deposit of confirmed values with human sign-off (**5N-M** recommended) |

Repository review alone is **insufficient** — direct access with artifact deposit required.

---

## Blockers before execution

| Blocker | Status |
| --- | --- |
| Direct source access capture documentation (5N-L) | **Complete** |
| Verified bibliographic capture artifact | **Pending** |
| Required `SOURCE_POLICY` fields populated from capture | **No** — 0 of 6 |
| Readiness upgrade to `execution_ready_after_field_verification` | **No** |
| Execution sprint charter | **Not issued** |
| Claim boundary registration | **Incomplete** |
| Guardrail **PASS** on registry diff | **N/A** — no diff |
| Human sign-off on inactive → verified | **Not performed** |

---

## Proposed decision: execution-ready / execution-still-blocked

**Decision: execution-still-blocked**

Spektrum retains:

- **`direct_access_not_available`** (in repository)
- **`execution_still_blocked`**
- **`execution_not_allowed_now`**
- **`source_approval_not_allowed_now`**

Upgrade to **`execution_candidate_after_capture`** requires Sprint **5N-M** verified bibliographic artifact with human sign-off covering all six bibliographic fields.

---

## Why capture review does not modify source_registry.json

| Capture review (5N-L) | Registry execution (future) |
| --- | --- |
| Inventories captured vs unavailable fields | Inserts row with verified values |
| Documents execution-still-blocked decision | May transition registry to active row |
| Leaves uncaptured fields blank | Closes gaps with captured data |
| No approval | Requires sign-off |

Capture review is **readiness documentation** — not registry mutation.

---

## Related documents

- `SPEKTRUM_DIRECT_SOURCE_ACCESS_FIELD_MATRIX_WAVE_1.md`
- `SPEKTRUM_DIRECT_SOURCE_ACCESS_EVIDENCE_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`
- `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`
