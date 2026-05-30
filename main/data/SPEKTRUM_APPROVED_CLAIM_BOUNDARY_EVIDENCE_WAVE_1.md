# Spektrum Approved Claim Boundary Evidence — Wave 1

**Sprint:** 5N-T  
**Scope:** Evidence for `CLM-TERM-MOS2-DE-001` approval readiness  
**Date:** 2026-05-30

---

## Claim under review

| Field | Value |
| --- | --- |
| `claim_id` | **`CLM-TERM-MOS2-DE-001`** |
| `claim_type` | terminology |
| `status` (5N-T) | **pending_review** (approval deferred) |
| `source_ids` | **`SRC-SPEKTRUM-MOS2-DE`** |
| `related_routes` | **`de_core_mos2`** |

---

## Allowed approved boundary (narrow)

If guardrails permit **`approved`** transition, the claim may approve **only**:

1. **Molybdän(IV)-sulfid** is a German **Lexikon der Chemie** dictionary entry associated with the **`de_core_mos2`** route.
2. **Spektrum Lexikon der Chemie** provides **authoritative dictionary / terminology support** for that German entry boundary.

---

## Explicit exclusions (unchanged)

| Excluded | Documented in |
| --- | --- |
| Chemical safety | `prohibited_uses` |
| Medical claims | `prohibited_uses` |
| Market / CAGR / pricing | `prohibited_uses` |
| Production / procurement / trade | `prohibited_uses` |
| Industrial performance | `prohibited_uses` |
| Acquisition claims | `prohibited_uses` |
| Non-terminology claims | claim scope + notes |

---

## Evidence chain

| Stage | Sprint | Outcome |
| --- | --- | --- |
| Claim boundary registration | 5N-P | **`CLM-TERM-MOS2-DE-001`** registered |
| Source verification review | 5N-Q | Policy evidence sufficient |
| Lock resolution | 5N-R | **`verification_limited`** posture |
| Source verified | 5N-S | **`SRC-SPEKTRUM-MOS2-DE`** **`verified`** |
| **Claim approval review** | **5N-T** | Approval evidence **sufficient**; status transition **deferred** |

---

## Source linkage evidence

| Source field | Value | Sufficient for claim |
| --- | --- | --- |
| `source_id` | `SRC-SPEKTRUM-MOS2-DE` | **Yes** |
| `status` | **verified** | **Yes** |
| `source_lock_status` | **candidate** | **Yes** — not source-locking |
| `category` | authoritative_dictionary | **Yes** |
| Route scope | `de_core_mos2` | **Yes** |

---

## Guardrail blocker (5N-T)

Tested: `status: approved` on **`CLM-TERM-MOS2-DE-001`** → **`validate_claim_registry_lock_l1.py`** and **`validate_corpus_claims_l1.py`** **FAIL**.

---

## Conclusion

**Approval-ready by policy; `approved` assignment deferred by guardrail.**
