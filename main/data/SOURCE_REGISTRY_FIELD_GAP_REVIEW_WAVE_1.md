# Source Registry Field Gap Review — Wave 1

**Sprint:** 5N-K  
**Scope:** Field gap assessment for proposed Spektrum row on `de_core_mos2`  
**Date:** 2026-05-29

---

## Source registry field gap summary

| Category | Available now | Unavailable now | Safe to omit |
| --- | ---: | ---: | ---: |
| Governance / identity fields | **7** | **0** | **0** |
| Required bibliographic fields (`SOURCE_POLICY`) | **0** | **4** | **0** |
| Recommended bibliographic fields | **0** | **2** | **0** |
| Execution metadata | **0** | **1** | **0** |

**Gap conclusion:** Governance fields sufficient for **future proposal carry-forward**. Bibliographic bundle **insufficient** for registry execution.

---

## Required fields available now

Per `doctrine/SOURCE_POLICY.md` and registry schema:

| Field | Available value | Verification |
| --- | --- | --- |
| `source_id` (proposed) | `SRC-SPEKTRUM-MOS2-DE` | **verified** — governance label |
| `title` (entry subject) | Molybdän(IV)-sulfid | **verified** — intake identity |
| `category` | `authoritative_dictionary` | **verified** — policy-aligned |
| `language` | `de` | **verified** |
| `linked_claims` | `[]` | **verified empty** — no approved claims |

**Count:** **5** required-schema fields have verified governance values. **4** required bibliographic fields have **no** verified values.

---

## Required fields unavailable now

| Field | Gap | Blocker |
| --- | --- | --- |
| `author_or_organization` | No confirmed value | Direct source access required |
| `publisher` | No confirmed imprint | Direct source access required |
| `publication_date` | No confirmed date | Direct source access required |
| `url` or `doi` | No verified locator | Direct source access required |

These fields are **rejected_if_unverified** for registry execution.

---

## Optional fields unavailable now

| Field | Gap | Impact if omitted at execution |
| --- | --- | --- |
| `edition` | No confirmed edition | **High** — lexicon authority audit weakened |
| `page_or_entry_citation` | No confirmed entry locator | **High** — line-to-source audit blocked |

Recommended for strict-registry discipline — should not be omitted at execution if verifiable, but must remain blank until verified.

---

## Fields that can be omitted safely

At **verification** stage (not execution):

| Field | Reason |
| --- | --- |
| `last_reviewed` | Set only at execution with human review date |
| `source_lock_status` | Assigned at execution if schema used |
| `risk_notes` | Optional at execution |

At **execution** stage, bibliographic required fields **cannot** be omitted.

---

## Fields that cannot be omitted safely

At registry execution, all of the following must be populated with **verified** values:

- `author_or_organization`
- `publisher`
- `publication_date`
- `url` or `doi` (where applicable)
- Entry scope confirmation covering proposed draft lines (edition + citation strongly recommended)

Omitting verified bibliographic values while inserting a row would violate `SOURCE_POLICY`.

---

## Fields that require direct source access

| Field | Access requirement |
| --- | --- |
| `author_or_organization` | Inspect Spektrum entry front matter / editorial credit |
| `publisher` | Confirm imprint from physical or licensed digital edition |
| `publication_date` | Confirm from edition metadata |
| `url_or_doi` | Confirm only if policy-applicable and verifiable — no invention |
| `edition` | Confirm edition/volume from source |
| `page_or_entry_citation` | Confirm lexicon entry locator for MoS2 subject |

**Access method:** Direct human access to Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid entry. Governance chain alone is **insufficient**.

---

## Blockers before execution

| Blocker | Status |
| --- | --- |
| Bibliographic field verification (governance layer) | **Complete** (5N-K) |
| Direct source access bibliographic capture | **Pending** |
| Required `SOURCE_POLICY` fields populated | **No** |
| Readiness upgrade to `execution_ready_after_field_verification` | **No** |
| Execution sprint charter | **Not issued** |
| Claim boundary registration | **Incomplete** |
| Guardrail **PASS** on registry diff | **N/A** — no diff |
| Human sign-off on inactive → verified | **Not performed** |

---

## Proposed decision: execution-ready / execution-blocked

**Decision: execution-blocked**

Spektrum retains:

- **`field_verification_governance_complete`**
- **`execution_blocked_pending_direct_source_access`**
- **`execution_not_allowed_now`**
- **`source_approval_not_allowed_now`**

Upgrade to **`execution_ready_after_field_verification`** requires Sprint **5N-L** direct source access bibliographic capture with confirmed values for all required bibliographic fields.

---

## Why gap review does not modify source_registry.json

| Gap review (5N-K) | Registry execution (future) |
| --- | --- |
| Inventories available vs unavailable fields | Inserts row with verified values |
| Documents execution-blocked decision | May transition registry to active row |
| Leaves bibliographic gaps explicit | Closes gaps with human-verified data |
| No approval | Requires sign-off |

Gap review is **readiness documentation** — not registry mutation.

---

## Related documents

- `SPEKTRUM_BIBLIOGRAPHIC_FIELD_MATRIX_WAVE_1.md`
- `SPEKTRUM_FIELD_EVIDENCE_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_ENTRY_FIELD_REVIEW_WAVE_1.md`
- `SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`
