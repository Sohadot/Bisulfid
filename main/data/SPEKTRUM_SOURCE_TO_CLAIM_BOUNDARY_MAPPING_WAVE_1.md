# Spektrum Source-to-Claim Boundary Mapping — Wave 1

**Sprint:** 5N-P  
**Date:** 2026-05-30  
**Scope:** Mapping `SRC-SPEKTRUM-MOS2-DE` → `CLM-TERM-MOS2-DE-001` for `de_core_mos2`

---

## Source record

| Field | Value |
| --- | --- |
| `source_id` | **`SRC-SPEKTRUM-MOS2-DE`** |
| `title` | Molybdän(IV)-sulfid - Lexikon der Chemie |
| `category` | authoritative_dictionary |
| `language` | de |
| `status` | **seeded** (not verified) |
| `source_lock_status` | **candidate** |
| Route scope | **`de_core_mos2`** |

---

## Claim record

| Field | Value |
| --- | --- |
| `claim_id` | **`CLM-TERM-MOS2-DE-001`** |
| `claim_type` | terminology |
| `status` | **pending_review** (not approved) |
| `related_routes` | **`de_core_mos2`** |
| `allowed_pages` | **`de_core_mos2`** |
| `related_terms` | molybdän(iv)-sulfid, mos2, molybdän disulfid |

---

## Source → claim boundary matrix

| Boundary dimension | `SRC-SPEKTRUM-MOS2-DE` may support | Must not support |
| --- | --- | --- |
| German lexicon entry | Molybdän(IV)-sulfid as Lexikon der Chemie entry on Spektrum.de for `de_core_mos2` | Universal suffix rules; formal IUPAC authority |
| Dictionary authority | Authoritative dictionary / terminology framing within lexicon-entry scope | EN-only authority; regulatory authority |
| Terminology framing | Cautious lexical and document-language support where directly stated in entry | Safety, medical, market, production, procurement, trade, CAGR, pricing, acquisition |
| Route association | Entry associated with **`de_core_mos2`** route scope | Route publication; indexation; navigation |
| Governance posture | Candidate boundary registration for future review | Claim approval; source-locking; marker removal |

---

## Route mapping

| `route_id` | Draft posture | Claim linked | Source linked | Source-locked |
| --- | --- | --- | --- | --- |
| **`de_core_mos2`** | draft / non_public / non-indexable | **`CLM-TERM-MOS2-DE-001`** (pending_review) | **`SRC-SPEKTRUM-MOS2-DE`** (seeded / candidate) | **No** |

---

## Content file mapping (read-only; not modified)

| Content file | `[SOURCE REQUIRED]` markers | Claim boundary applies to |
| --- | --- | --- |
| `main/content/de/pages/terminology/molybdenum-disulfide.md` | **Present** (4 occurrences) | Future terminology framing only — markers **not** resolved by 5N-P |

---

## Cross-reference note

`source_registry.json` was **not modified** in 5N-P. The `linked_claims` field is not populated on the registry row — consistent with existing registry entries and with **0** approved claims. Future source verification or claim approval sprints may add cross-references under separate charter.

---

## Supporting candidates (not registered in 5N-P)

The following remain **unregistered** and **outside** this sprint scope:

- PubChem — Molybdenum disulfide / CID 14823
- NIST Chemistry WebBook — molybdenum disulphide
- Chemie.de Lexikon — Molybdän(IV)-sulfid
- `sulfur_element_term_record` track

---

## Mapping conclusion

One narrow **pending_review** claim boundary links **`SRC-SPEKTRUM-MOS2-DE`** to **`de_core_mos2`** for German dictionary-entry terminology support only. No approval, no source-lock, no publication readiness implied.
