# Claim Approval Limited — No Source Lock, No Publication — Wave 1

**Sprint:** 5N-U  
**Date:** 2026-05-27  
**Posture:** `approval_limited` with one narrow approved claim

---

## Locked gates (unchanged)

| Gate | Status |
| --- | --- |
| Claim registry file `status` | **inactive** |
| `production_can_safely_proceed` | **no** |
| Route publication lock | **LOCKED** |
| Sitemap activation | **LOCKED** |
| Navigation activation | **LOCKED** |
| Public HTML generation | **not performed** |
| Content source-locking | **not performed** |
| `[SOURCE REQUIRED]` markers | **retained** |

---

## Source posture (unchanged)

| Source | Field | Value |
| --- | --- | --- |
| SRC-SPEKTRUM-MOS2-DE | `status` | verified |
| SRC-SPEKTRUM-MOS2-DE | `source_lock_status` | **candidate** |
| source_registry.json | file `status` | inactive |

---

## Content posture (unchanged)

| Route | Publication | Indexable | Markers |
| --- | --- | --- | --- |
| de_core_mos2 | draft / non_public | false | `[SOURCE REQUIRED]` present |

No content pages were modified in this sprint.

---

## Claim posture (changed — narrow only)

| Claim | Status | Scope |
| --- | --- | --- |
| CLM-TERM-MOS2-DE-001 | **approved** | German Lexikon der Chemie dictionary-entry terminology for de_core_mos2 only |
| All other claims | pending_review | Unchanged |

**Approved claim count:** 1  
**Approved does not mean:** source-locked, publication-ready, marker-resolved, or production-safe.

---

## Validator enforcement

Guardrails now **permit** `status: approved` only when all of the following hold:

1. Claim registry file remains **`inactive`**
2. `claim_approval_lock_resolution.resolved_posture` is **`approval_limited`**
3. Claim is listed in **`approval_ready_claims`**
4. Linked source is **`verified`** with **`source_lock_status: candidate`**
5. Claim boundary remains narrow (terminology, bounded routes/pages, required prohibited_uses)

Guardrails **fail** if approved status implies source-locking, route publication, sitemap, navigation, or public HTML generation.

---

## Explicit non-claims

This sprint does **not** claim:

- Claim registry / publication activation is complete
- Content source-locking is complete
- `[SOURCE REQUIRED]` markers are satisfied
- Routes are publication-ready
- Corpus is ready for production deployment
