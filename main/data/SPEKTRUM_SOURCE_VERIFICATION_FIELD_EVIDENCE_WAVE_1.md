# Spektrum Source Verification Field Evidence — Wave 1

**Sprint:** 5N-Q  
**Scope:** Field-level evidence for `SRC-SPEKTRUM-MOS2-DE` verification review  
**Date:** 2026-05-30

---

## Field evidence matrix

| field_name | registry_value | evidence_basis | verification_class | sufficient_for_verified | must_remain_blank | notes |
| --- | --- | --- | --- | --- | --- | --- |
| `source_id` | `SRC-SPEKTRUM-MOS2-DE` | 5N-K governance + 5N-O execution | verified_governance | yes | no | Stable identifier |
| `category` | `authoritative_dictionary` | SOURCE_POLICY + 5N-K | verified_governance | yes | no | Approved category |
| `title` | Molybdän(IV)-sulfid - Lexikon der Chemie | 5N-N human artifact | verified_from_human_artifact | yes | no | Matches live entry |
| `author_or_organization` | Lexikon editorial/authorial team (summarized) | 5N-N human artifact | verified_from_human_artifact | yes | no | Collective lexicon authorship |
| `publisher` | Spektrum Akademischer Verlag, Heidelberg | 5N-N human artifact | verified_from_human_artifact | yes | no | From copyright line |
| `url` | https://www.spektrum.de/lexikon/chemie/molybdaen-iv-sulfid/5985 | 5N-N human artifact | verified_from_human_artifact | yes | no | Stable lexicon URL |
| `language` | de | 5N-K governance | verified_governance | yes | no | DE route scope |
| `publication_date` | *(omitted)* | 5N-N not visible | not_visible_from_source | conditional | yes | Copyright 1998 **not** used |
| `access_date` | 2026-05-30 (in notes) | 5N-N human artifact | verified_from_human_artifact | yes | no | Satisfies SOURCE_POLICY access-date allowance |
| `edition_or_version` | *(omitted)* | 5N-N not visible | not_visible_from_source | no | yes | Not inferred |
| `page_or_entry_citation` | entry: Molybdän(IV)-sulfid, in Lexikon der Chemie | 5N-N human artifact | verified_from_human_artifact | yes | no | In notes |
| `status` | seeded | 5N-O execution + 5N-Q review | verification_review_deferred | pending | no | Guardrail blocks verified while registry inactive |
| `source_lock_status` | candidate | 5N-O execution | verified_governance | n/a | no | Unchanged — not source-locking |
| `use_for` | DE lexicon / terminology scope | 5N-K + 5N-P boundary | verified_governance | yes | no | Narrow dictionary boundary |
| `do_not_use_for` | safety, market, medical, etc. | SOURCE_POLICY + 5N-P | verified_governance | yes | no | Explicit exclusions |
| `linked_claims` | *(not populated)* | schema pattern | empty_by_design | yes | no | No approved claims |

*Rows: 16*

---

## Evidence chain

| Stage | Sprint | Outcome |
| --- | --- | --- |
| Bibliographic field verification | 5N-K | 7 governance fields verified; 6 bibliographic blank |
| Direct source access capture | 5N-L | `direct_access_not_available` in repo artifacts |
| Artifact intake layer | 5N-M | Requirements defined; no bundle in repo |
| Human artifact review | 5N-N | **8** fields verified from human receipt; **2** blank |
| Registry execution | 5N-O | Row inserted with human-reviewed values only |
| Claim boundary registration | 5N-P | **`CLM-TERM-MOS2-DE-001`** pending_review |
| **Verification review** | **5N-Q** | Policy evidence **sufficient**; status transition **deferred** |

---

## Verified vs blank field summary

| Classification | Count |
| --- | ---: |
| verified_from_human_artifact | **8** |
| verified_governance | **6** |
| not_visible / must remain blank | **2** (`publication_date`, `edition_or_version`) |
| verification_review_deferred | **1** (`status` field transition) |

---

## SOURCE_POLICY required-field conclusion

Per `doctrine/SOURCE_POLICY.md` registry format:

- All required bibliographic identity fields are **present or policy-satisfied** (access date substitutes for omitted `publication_date` on online lexicon entry).
- Blank fields are **intentionally omitted** — not invented.
- Evidence is **sufficient** for **`verified`** posture on the **narrow dictionary-entry boundary**.

---

## Guardrail field conclusion

`validate_source_registry_lock_l1.py` treats `status: verified` as blocking error while registry file `status: inactive`. Therefore:

- Field evidence supports verification **in principle**.
- Registry `status` field **remains `seeded`** in 5N-Q.
- Verification review recorded in `notes` and `risk_notes`.

---

## Claim linkage evidence (read-only)

| claim_id | status | source_ids | modified in 5N-Q |
| --- | --- | --- | --- |
| `CLM-TERM-MOS2-DE-001` | pending_review | `SRC-SPEKTRUM-MOS2-DE` | **No** |

Claim boundary exists; claim approval is **not** part of source verification review.
