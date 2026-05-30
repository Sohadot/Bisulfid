# Spektrum Claim Boundary Registration — Wave 1 Report

**Sprint:** 5N-P  
**Date:** 2026-05-30  
**Scope:** Non-approved claim boundary registration for `de_core_mos2` tied to `SRC-SPEKTRUM-MOS2-DE`

---

## Why this sprint exists

Sprint **5N-O** registered **`SRC-SPEKTRUM-MOS2-DE`** in `source_registry.json` with `status: seeded` and `source_lock_status: candidate`. The registry row does not approve claims, does not source-lock content, and does not resolve `[SOURCE REQUIRED]` markers.

Sprint **5N-P** registers the **narrow claim boundary** that the Spektrum source may support for `de_core_mos2` — without claim approval, without source verification, without content modification, and without route publication.

---

## Pre-flight posture (confirmed)

| Check | Result |
| --- | --- |
| Branch based on latest main after 5N-O | **Yes** |
| All L1/L2 runtimes | **PASS** (pre-sprint) |
| `production_can_safely_proceed` | **no** |
| Corpus locks | **LOCKED** |
| `SRC-SPEKTRUM-MOS2-DE` in registry | **Yes** (15 entries) |
| Source `status` | **seeded** / not verified |
| Source `source_lock_status` | **candidate** |
| Registry file `status` | **inactive** |
| `de_core_mos2` draft posture | draft / non_public / non-indexable |
| `[SOURCE REQUIRED]` markers | **Present** (unchanged) |
| `terminology_claims.json` before sprint | **Unchanged** (11 claims) |

---

## Claim boundary registered

| Field | Value |
| --- | --- |
| `claim_id` | **`CLM-TERM-MOS2-DE-001`** |
| `claim_type` | terminology |
| `status` | **`pending_review`** (not approved) |
| `source_ids` | **`SRC-SPEKTRUM-MOS2-DE`** |
| `related_routes` | **`de_core_mos2`** |
| `allowed_pages` | **`de_core_mos2`** |
| `risk_level` | medium |

---

## Allowed boundary (narrow)

`SRC-SPEKTRUM-MOS2-DE` may support only:

1. That **Molybdän(IV)-sulfid** is a German **Lexikon der Chemie** entry associated with the **`de_core_mos2`** route.
2. That **Spektrum Lexikon der Chemie** provides **authoritative dictionary / terminology support** for the German entry boundary within lexicon-entry scope.
3. **Terminology framing only** — cautious lexical and document-language support where directly supported by the Spektrum entry.

---

## Explicit exclusions

The registered boundary does **not** permit:

- Chemical safety or handling instructions
- Medical claims
- Market data, market-share data, or CAGR claims
- Pricing, production, procurement, or trade claims
- Industrial performance claims
- Acquisition-target claims
- EN-only authority, formal IUPAC standard authority, or universal suffix rules
- Claim approval, source-locking, marker removal, or route publication by itself

---

## What this sprint does not do

| Action | Status |
| --- | --- |
| Claim approval | **Not performed** |
| Source verification (`verified`) | **Not performed** |
| `source_lock_status` → locked | **Not performed** |
| Content page edits | **Not performed** |
| `[SOURCE REQUIRED]` marker removal | **Not performed** |
| Route publication | **Not performed** |
| `source_registry.json` modification | **Not performed** |
| Public HTML generation | **Not performed** |

---

## Registry posture after registration

| Metric | Value |
| --- | ---: |
| Terminology claims (total) | **12** |
| Approved claims | **0** |
| Claims linked to `SRC-SPEKTRUM-MOS2-DE` | **1** (`CLM-TERM-MOS2-DE-001`, pending_review) |
| Claim registry `status` | **`inactive`** |
| Verified sources | **0** |

---

## Related documents

- `SPEKTRUM_SOURCE_TO_CLAIM_BOUNDARY_MAPPING_WAVE_1.md`
- `SPEKTRUM_CLAIM_BOUNDARY_NO_APPROVAL_NO_SOURCE_LOCK_WAVE_1.md`
- `SPEKTRUM_CLAIM_BOUNDARY_REGISTRATION_VALIDATION_REPORT.md`
- `doctrine/SOURCE_POLICY.md`
- `SPEKTRUM_SOURCE_REGISTRY_EXECUTION_WAVE_1_REPORT.md` (5N-O)

---

## Recommended next sprint

Separate charters required for: source verification, claim approval, content source-lock audit, marker resolution — none authorized by 5N-P.
