# Source Registry Execution Risk Review — Wave 1

**Sprint:** 5N-J  
**Scope:** Execution readiness risks for `de_core_mos2`  
**Date:** 2026-05-29

---

## Risk of editing source_registry.json too early

| Risk | Consequence | Mitigation in 5N-J |
| --- | --- | --- |
| Registry row before field verification | False verified signal | **0** rows added |
| Skipping readiness review | Unverified bibliographic data in registry | Readiness documents gaps |
| Bypassing execution charter | Audit failure | Execution **not allowed now** |

---

## Risk of approving a source before field verification

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| `verified` status without bibliographic proof | Publication path opened prematurely | **source_approval_not_allowed_now** |
| Readiness misread as approval | Contributors treat Spektrum as source-locked | Documents state not approved |
| Inactive registry bypass | Guardrail discipline broken | Registry **unchanged** |

---

## Risk of inventing bibliographic fields

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| AI-generated publisher/edition | Registry integrity failure | All bibliographic fields **blank/unverified** in docs |
| Fabricated DOI/URL | Policy violation | No URLs invented |
| False merge confidence | Bad execution sprint | **`execution_blocked_pending_field_verification`** |

---

## Risk of using supporting candidates as primary authority

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| PubChem/NIST as DE lexicon | Authority class violation | **`not_primary_registry_source_now`** |
| Chemie.de elevation | Thin authority | **`supporting_boundary_retained`** |
| Database row replaces Spektrum | Proposal integrity loss | Primary row reserved for Spektrum only |

---

## Risk of claim approval before claim boundary registration

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Terminology claims activated early | Unverified MoS2 statements governed | **0** approved claims |
| Registry execution conflated with claims | Lexical lines treated as claim-backed | **`not_claim_approval_source_now`** |
| `linked_claims` pre-populated | False claim linkage | **Empty** in field review |

---

## Risk of removing [SOURCE REQUIRED] markers too early

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Readiness treated as linkage | Unresolved lines appear resolved | Markers **remain** |
| Execution bundled with content edit | Draft drift | Content **not modified** |
| No audit trail | Governance failure | Separate content audit sprint required |

---

## Risk of source-locking before content/source alignment

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Page marked source-locked without registry row | False confidence | **not source-locked** |
| Partial linkage | Inconsistent draft | No content edits in 5N-J |
| Marker removal without audit | Publication risk | Markers **remain** |

---

## Risk of publishing before source and claim gates clear

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Route publication | Public thin-authority page | All routes **`planned`** |
| Launch threshold bypass | **126** treated as ready | **500-page** threshold documented |
| `production_can_safely_proceed` ignored | Production wave risk | Planner reports **no** |

---

## Risk of using CI passing as source approval

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Corpus Governance CI PASS misread | Merge allowed ≠ sources approved | Documents state CI validates discipline only |
| Readiness sprint merged → execution assumed | Registry edit without charter | **`execution_not_allowed_now`** explicit |

---

## Why execution readiness does not approve execution

| Readiness completes | Execution still requires |
| --- | --- |
| Field gap documentation | Human bibliographic verification |
| Role-fit confirmation | Execution sprint charter |
| Risk documentation | Human sign-off on registry diff |
| Runtime PASS | Verified field population |

Sprint **5N-J** output is **readiness documentation** — not execution authorization.

---

## Related documents

- `SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_EXECUTION_NEXT_ACTIONS_WAVE_1.md`
- `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`
