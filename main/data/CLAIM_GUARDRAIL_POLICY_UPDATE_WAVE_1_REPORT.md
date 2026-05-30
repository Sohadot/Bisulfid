# Claim Guardrail Policy Update — Wave 1 Report

**Sprint:** 5N-U  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5n-u-claim-guardrail-policy-update`  
**Scope:** Guardrail policy update for `approval_limited` narrow claim approval

---

## Why this sprint exists

Sprint **5N-T** documented **`approval_limited`** posture and listed **`CLM-TERM-MOS2-DE-001`** in **`approval_ready_claims`**, but Sprint **5N-B** guardrails in **`validate_claim_registry_lock_l1.py`** and **`validate_corpus_claims_l1.py`** rejected any claim row with `status: approved` while the claim registry file remained **`inactive`**. Sprint **5N-U** updates those guardrails to distinguish **narrow individual claim approval** from **claim registry / publication activation** — then performs one controlled approved transition.

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-T | **Yes** |
| All L1/L2 runtimes (pre) | **PASS** |
| `production_can_safely_proceed: no` | **Yes** |
| All corpus locks **LOCKED** | **Yes** |
| `claim_approval_lock_resolution` present | **Yes** |
| `resolved_posture` | **`approval_limited`** |
| `approval_ready_claims` includes CLM-TERM-MOS2-DE-001 | **Yes** |
| CLM-TERM-MOS2-DE-001 pre-sprint `status` | **pending_review** |
| SRC-SPEKTRUM-MOS2-DE `status` | **verified** |
| SRC-SPEKTRUM-MOS2-DE `source_lock_status` | **candidate** |
| Claim registry file `status` | **inactive** |

---

## Guardrail policy change

**Files:**

- `scripts/validate_claim_registry_lock_l1.py`
- `scripts/validate_corpus_claims_l1.py`

| Rule | Before (5N-B) | After (5N-U) |
| --- | --- | --- |
| Claim registry file `status` | Must be **`inactive`** | Unchanged — publication lock preserved |
| Claim row `status: approved` | Always **error** | **Permitted** only under `approval_limited` + `approval_ready_claims` + verified linked source + `source_lock_status: candidate` |
| Approved not in ready list | N/A | **Error** |
| Approved with linked source not verified | N/A | **Error** |
| Approved with `source_lock_status: locked` | N/A | **Error** |
| Approved boundary expansion | N/A | **Error** (route scope, source_ids, prohibited_uses) |
| Registry file activation / publication | **Blocked** | Unchanged — **blocked** |

---

## Distinction enforced by validator messages

- **Narrow claim approval:** `status: approved` under `approval_limited` — terminology evidence posture only.
- **Claim registry / publication activation:** registry file `status` change or bulk claim publication — **blocked**.
- **Source-locking:** approved claim does not require or imply `source_lock_status: locked` — **blocked**.
- **Non-effects:** approved claim does not imply route publication, sitemap inclusion, navigation inclusion, public HTML generation, marker removal, or `production_can_safely_proceed: yes`.

---

## Related documents

- `SPEKTRUM_APPROVED_CLAIM_TRANSITION_WAVE_1_REPORT.md`
- `CLAIM_APPROVAL_LIMITED_NO_SOURCE_LOCK_NO_PUBLICATION_WAVE_1.md`
- `CLAIM_GUARDRAIL_POLICY_UPDATE_VALIDATION_REPORT.md`
- `SPEKTRUM_CLAIM_APPROVAL_REVIEW_WAVE_1_REPORT.md` (5N-T)

---

## Recommended next sprint

Content source-lock audit; marker resolution; route publication — separate charters. Narrow claim approval does not authorize any of the above.
