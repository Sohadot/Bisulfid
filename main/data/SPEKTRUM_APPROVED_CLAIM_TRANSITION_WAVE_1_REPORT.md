# Spektrum Approved Claim Transition — Wave 1 Report

**Sprint:** 5N-U  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5n-u-claim-guardrail-policy-update`  
**Scope:** Controlled transition of `CLM-TERM-MOS2-DE-001` to `approved`

---

## Transition summary

| Field | Before (5N-T) | After (5N-U) |
| --- | --- | --- |
| `claim_id` | CLM-TERM-MOS2-DE-001 | Unchanged |
| `status` | **pending_review** | **approved** |
| `claim_type` | terminology | Unchanged |
| `source_ids` | SRC-SPEKTRUM-MOS2-DE | Unchanged |
| `related_routes` | de_core_mos2 | Unchanged |
| `allowed_pages` | de_core_mos2 | Unchanged |
| Linked source `status` | verified | Unchanged |
| Linked source `source_lock_status` | candidate | Unchanged |
| Claim registry file `status` | inactive | Unchanged |

---

## Narrow boundary preserved

The approved claim remains limited strictly to:

> German Lexikon der Chemie dictionary-entry terminology for de_core_mos2 only

**Statement (approved):** Molybdän(IV)-sulfid has a German Lexikon der Chemie dictionary entry on Spektrum.de that supports cautious terminology framing for the de_core_mos2 route within the registered narrow dictionary-entry boundary.

**Excluded claim classes (prohibited_uses unchanged in scope):**

- Chemical safety
- Medical claims
- Market data, pricing, trade, CAGR
- Production, procurement, industrial performance
- Acquisition targets
- Route publication
- Removal of `[SOURCE REQUIRED]` markers
- Source-locking by itself

---

## Evidence chain

| Sprint | Outcome |
| --- | --- |
| 5N-O | SRC-SPEKTRUM-MOS2-DE registered (seeded, candidate) |
| 5N-P | CLM-TERM-MOS2-DE-001 registered (pending_review) |
| 5N-S | SRC-SPEKTRUM-MOS2-DE → verified (verification_limited) |
| 5N-T | Approval evidence sufficient; guardrail blocked approved |
| 5N-U | Guardrail updated; claim → approved (approval_limited) |

---

## What this transition does not do

- Does not source-lock `de_core_mos2`
- Does not change SRC-SPEKTRUM-MOS2-DE `source_lock_status` from candidate
- Does not remove `[SOURCE REQUIRED]` markers
- Does not modify content pages
- Does not publish routes
- Does not activate sitemap or navigation
- Does not generate public HTML
- Does not set `production_can_safely_proceed: yes`

---

## Related documents

- `CLAIM_GUARDRAIL_POLICY_UPDATE_WAVE_1_REPORT.md`
- `CLAIM_APPROVAL_LIMITED_NO_SOURCE_LOCK_NO_PUBLICATION_WAVE_1.md`
- `SPEKTRUM_CLAIM_APPROVAL_REVIEW_WAVE_1_REPORT.md` (5N-T)
