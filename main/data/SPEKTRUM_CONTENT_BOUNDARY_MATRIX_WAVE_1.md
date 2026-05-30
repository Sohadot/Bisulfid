# Spektrum Content Boundary Matrix — Wave 1

**Sprint:** 5N-V  
**Date:** 2026-05-30  
**Route:** `de_core_mos2`  
**Content file:** `main/content/de/pages/terminology/molybdenum-disulfide.md`

---

## Source and claim reference

| ID | Role | Status | Lock posture |
| --- | --- | --- | --- |
| `SRC-SPEKTRUM-MOS2-DE` | German Lexikon der Chemie dictionary | **verified** | `source_lock_status: candidate` |
| `CLM-TERM-MOS2-DE-001` | Narrow terminology claim | **approved** | Registry file **inactive** |

**Approved boundary:** German Lexikon der Chemie dictionary-entry terminology for `de_core_mos2` only.

---

## Section-by-section matrix

| # | Content section | Line / marker | Supported by source + claim? | Boundary class | Source-lock eligible? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Entwurfsstatus notice | Body L13 | Governance only | Non-claim | N/A | Non-public posture; not terminology content |
| 2 | Seitenrolle | Body L15–16 | **Yes** | Terminology framing | **Partial** | Route-scoped terminology entry role aligns with claim scope |
| 3 | Lexikalische Form | Body L19 | **No** (placeholder) | Terminology | **No** | `[SOURCE REQUIRED]` — no lexical form stated |
| 4 | Chemische / Dokumentform | Body L20 | **No** (placeholder) | Terminology | **No** | `[SOURCE REQUIRED]` — no document form stated |
| 5 | Claim-Status (layer) | Body L21 | **Contradicts registry** | Governance | **No** | States "keine freigegebenen Claims"; registry has 1 approved claim |
| 6 | Abgrenzungen | Body L23–24 | **Yes** (exclusions) | Boundary guard | **Partial** | Negative framing aligns with prohibited_uses; `[SOURCE REQUIRED]` on binding line |
| 7 | Quellen- und Claim-Status | Body L26–29 | **Partially stale** | Governance | **No** | Says inactive registries / no approved claims / source-locking incomplete |
| 8 | Veröffentlichungsblocker | Body L31–33 | **Yes** | Governance | N/A | Accurate publication lock language |
| 9 | Interne Referenzrolle | Body L35–36 | **Yes** | Structural | N/A | Internal reference only; no factual claim |

---

## Marker inventory

| Occurrence | Location | Content context | Resolvable under narrow boundary? |
| --- | --- | --- | --- |
| 1 | L19 | Lexikalische Form layer | **Future** — requires Spektrum dictionary-entry terminology text |
| 2 | L20 | Chemische / Dokumentform layer | **Future** — requires document-language terminology from lexicon scope |
| 3 | L24 | Abgrenzungen — stronger source binding | **Future** — binding statement, not exclusion |
| 4 | L29 | Source-locking status line | **Future** — marker on open factual lines reference |

**Markers removed this sprint:** **0**

---

## Excluded claim class scan

| Excluded class | Present in draft? | Result |
| --- | --- | --- |
| Chemical safety | No | **PASS** |
| Medical claims | No | **PASS** |
| Market / pricing / trade / CAGR | No | **PASS** |
| Production / procurement | No | **PASS** |
| Industrial performance | No | **PASS** |
| Acquisition claims | No | **PASS** |
| Non-terminology factual claims | No | **PASS** |

---

## Supported vs unsupported summary

| Category | Count | Source-lock posture |
| --- | ---: | --- |
| Supported (governance / structural / exclusions) | 5 sections | Documented; no metadata applied |
| Partially supported (role framing) | 2 sections | Awaiting factual terminology |
| Unsupported / placeholder | 3 terminology layers | `[SOURCE REQUIRED]` — deferred |
| Stale vs registry | 2 sections | Deferred until marker-resolution charter |

---

## Matrix conclusion

**0** content lines are source-lock eligible in the current draft state. Registry-layer source and claim approval exist, but **content-layer source-locking is deferred** until schema support, factual terminology population, and marker-resolution charter allow safe non-public lock annotation without body rewrite or marker removal.
