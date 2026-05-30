# Source Registry Verification Lock Resolution — Wave 1 Report

**Sprint:** 5N-R  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-5n-r-source-registry-verification-lock-resolution`  
**Scope:** Resolve source registry verification lock for `SRC-SPEKTRUM-MOS2-DE`

---

## Why this sprint exists

Sprint **5N-Q** concluded that human-reviewed bibliographic evidence is **sufficient** for a narrow **`authoritative_dictionary`** verification posture, but **`validate_source_registry_lock_l1.py`** blocks `status: verified` while the registry file remains **`inactive`**. Sprint **5N-R** resolves the **architectural lock** separating registry publication posture from individual source verification — without claim approval, source-locking, marker resolution, or route publication.

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-Q | **Yes** |
| L2 / L1 / guardrail runtimes (pre) | **PASS** |
| `production_can_safely_proceed: no` | **Yes** |
| All corpus locks **LOCKED** | **Yes** |
| `SRC-SPEKTRUM-MOS2-DE` exists | **Yes** |
| Source `status` pre-sprint | **seeded** |
| `CLM-TERM-MOS2-DE-001` | **pending_review** |
| `[SOURCE REQUIRED]` markers | **Present** |

---

## Task 1 — Why registry-level inactive status blocks individual source verification

Sprint **5N-B** guardrail `validate_source_registry_lock_l1.py` enforces a **dual lock**:

| Lock layer | Validator rule | Effect |
| --- | --- | --- |
| Registry file | `status` must be **`inactive`** | Any non-inactive registry status **errors** |
| Source row | `status` in `verified` / `approved` / `locked` / `final` **errors** | No individual source may be verified |

The dual lock conflated **publication registry posture** (file inactive) with **source bibliographic verification** (row verified). Sprint **5N-Q** could not assign `verified` without failing guardrails. Changing registry file status alone also fails — the validator requires **`inactive`**.

---

## Task 2 — SOURCE_POLICY allowance for verification-limited posture

| SOURCE_POLICY principle | 5N-R interpretation |
| --- | --- |
| Verified entries required for **published** claims | Publication remains **LOCKED** — routes, claims, content unchanged |
| Authoritative dictionary category approved | **Spektrum** qualifies for narrow dictionary boundary |
| Human-reviewed bibliographic evidence | **Sufficient** (5N-Q conclusion) |
| Registry format fields | Present or policy-satisfied (access date in notes) |

**Policy conclusion:** SOURCE_POLICY **allows** individual source **`verified`** status for bibliographic governance **without** implying route publication, claim approval, or content source-locking. Publication locks remain enforced by separate validators (`validate_corpus_publication_lock_l1.py`, `validate_claim_registry_lock_l1.py`).

---

## Task 3 — Minimal registry-level state change

Added **`verification_lock_resolution`** object at registry root in `source_registry.json`:

| Field | Value |
| --- | --- |
| `resolved_posture` | **`verification_limited`** |
| `publication_lock` | **LOCKED** |
| `claim_registry_lock` | **LOCKED** |
| `route_publication_lock` | **LOCKED** |
| `allows_individual_source_verified_status` | **true** (policy) |
| `guardrail_transition_pending` | **true** |
| `verification_ready_sources` | **`SRC-SPEKTRUM-MOS2-DE`** |

Registry file **`status`** remains **`inactive`** — required by current guardrail. Updated **`rule`** clarifies dual-layer lock model.

---

## Task 4 — Verified status transition outcome

| Field | Before | After |
| --- | --- | --- |
| Registry file `status` | inactive | **inactive** (guardrail required) |
| `SRC-SPEKTRUM-MOS2-DE` `status` | seeded | **seeded** (guardrail blocks verified) |
| `source_lock_status` | candidate | **candidate** |
| Verification-ready documented | No | **Yes** |

**Decision:** Policy and schema **support** `verified` transition for **`SRC-SPEKTRUM-MOS2-DE`**. Current guardrails **do not allow** data-only `verified` assignment without validator policy update. **`verification_lock_resolution`** documents resolved posture and pending guardrail charter.

---

## Validator modification assessment

| Question | Answer |
| --- | --- |
| Is validator modification required for `verified` row? | **Yes** |
| Modified in 5N-R? | **No** — per sprint charter: stop and report instead of editing scripts |
| Recommended next charter | Validator policy update to permit **`verification_limited`** posture with individual **`verified`** rows while publication locks remain **LOCKED** |

---

## What this sprint does not do

- **No** claim approval.
- **No** `source_lock_status` → locked.
- **No** content edits or marker removal.
- **No** route publication.
- **No** new source registration.
- **No** validator weakening or bypass.

---

## Related documents

- `SPEKTRUM_VERIFIED_STATUS_TRANSITION_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_LOCK_NO_PUBLICATION_NO_SOURCE_LOCK_WAVE_1.md`
- `SOURCE_REGISTRY_VERIFICATION_LOCK_VALIDATION_REPORT.md`
- `SPEKTRUM_SOURCE_VERIFICATION_REVIEW_WAVE_1_REPORT.md` (5N-Q)

---

## Recommended next sprint

**Validator policy update charter** — update `validate_source_registry_lock_l1.py` to distinguish **`verification_limited`** registry posture from full publication activation; then assign **`SRC-SPEKTRUM-MOS2-DE`** `status: verified` with guardrail **PASS**.
