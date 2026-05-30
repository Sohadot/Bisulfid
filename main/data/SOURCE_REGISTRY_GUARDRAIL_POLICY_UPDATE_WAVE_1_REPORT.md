# Source Registry Guardrail Policy Update — Wave 1 Report

**Sprint:** 5N-S  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-5n-s-source-registry-guardrail-policy-update`  
**Scope:** Guardrail policy update for `verification_limited` bibliographic verification

---

## Why this sprint exists

Sprint **5N-R** documented **`verification_limited`** posture and listed **`SRC-SPEKTRUM-MOS2-DE`** in **`verification_ready_sources`**, but Sprint **5N-B** guardrail **`validate_source_registry_lock_l1.py`** rejected any row with `status: verified` while the registry file remained **`inactive`**. Sprint **5N-S** updates the guardrail to distinguish **bibliographic verification** from **registry/publication activation** — then performs one controlled verified transition.

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-R | **Yes** |
| All L1/L2 runtimes (pre) | **PASS** |
| `production_can_safely_proceed: no` | **Yes** |
| All corpus locks **LOCKED** | **Yes** |
| `verification_lock_resolution` present | **Yes** |
| `resolved_posture` | **`verification_limited`** |
| `verification_ready_sources` includes Spektrum | **Yes** |
| Spektrum pre-sprint `status` | **seeded** |
| Spektrum `source_lock_status` | **candidate** |
| `CLM-TERM-MOS2-DE-001` | **pending_review** |

---

## Guardrail policy change

**File:** `scripts/validate_source_registry_lock_l1.py`

| Rule | Before (5N-B) | After (5N-S) |
| --- | --- | --- |
| Registry file `status` | Must be **`inactive`** | Unchanged — publication lock preserved |
| `status: verified` | Always **error** | **Permitted** only under `verification_limited` + `verification_ready_sources` + `source_lock_status: candidate` |
| `status: approved/locked/final` | **Error** | Unchanged — publication approval blocked |
| `source_lock_status: locked` | **Error** | Unchanged — source-locking blocked |
| Verified not in ready list | N/A | **Error** |
| Verified with `source_lock_status` ≠ candidate | N/A | **Error** |

---

## Distinction enforced by validator messages

- **Bibliographic verification:** `status: verified` under `verification_limited` — evidence posture only.
- **Registry/publication approval:** `status: approved/locked/final` or registry file activation — **blocked**.
- **Source-locking:** `source_lock_status: locked` — **blocked**.
- **Non-effects:** verified status does not imply claim approval, route publication, sitemap, navigation, or `production_can_safely_proceed: yes`.

---

## Related documents

- `SPEKTRUM_VERIFIED_TRANSITION_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_VERIFICATION_LIMITED_NO_PUBLICATION_WAVE_1.md`
- `SOURCE_REGISTRY_GUARDRAIL_POLICY_UPDATE_VALIDATION_REPORT.md`
- `SOURCE_REGISTRY_VERIFICATION_LOCK_RESOLUTION_WAVE_1_REPORT.md` (5N-R)

---

## Recommended next sprint

Claim approval sprint; content source-lock audit; marker resolution — separate charters. Verified bibliographic status does not authorize any of the above.
