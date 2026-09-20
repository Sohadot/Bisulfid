# Pilot 01 — Source Acquisition Dossier (Morocco × Sulfur Trade)

**Date:** 2026-09-19 · **Retrieval date:** 2026-09-19 · **Corrected:** 2026-09-19 (data-semantics correction).

## Source acquired
- **Authority:** Office des Changes — Royaume du Maroc (Morocco's official foreign-trade statistics authority).
- **Artifact used (primary official):** *Commerce extérieur du Maroc — Rapport annuel 2024* (official PDF).
- **URL:** https://www.oc.gov.ma/sites/default/files/2025-07/Rapport%20Commerce%20Ext%C3%A9rieur%202024%20VF.pdf
- **Interactive database (NOT used):** https://services.oc.gov.ma/DataBase/CommerceExterieur/login — authentication-gated; not fetchable; no credentials in git.
- **Canonical source id:** `SRC-OC-MA-TRADE` · **identity_revision:** `rev-2026-09-19-1` · **category:** `official_trade_statistics` · **status:** seeded · **lock:** candidate.

## Numeric convention (CRITICAL)
In this French report's tables/graphs the **dot is a THOUSANDS separator** and the **comma is the decimal** (percentages). So `9.108` = **9108**, `1.099` = **1099**. Every figure below is stored as `source_literal` (as printed) + `normalized_value` (machine int). Normalization is source-specific.

## Figures by SOURCE SCOPE (do not mix scopes)
| Scope | Table | Product | 2022 | 2023 | 2024 | Δ2024/23 | unit |
|---|---|---|---|---|---|---|---|
| **TOTAL imports** | **T1-10** | Soufres bruts et non raffinés | 18.768→18768 | 8.007→8007 | **9.108→9108** | +1.101→+1101 / +13,8% | MDH |
| ATPA-with-payment (ancillary) | T3-4 | Soufres bruts et non raffinés | 18.758→18758 | 7.994→7994 | 9.102→9102 | +1.108→+1108 / +13,9% | MDH |
| Asia origin (ancillary subset) | T4-9 | Soufres bruts et non raffinés | 17.019→17019 | 7.197→7197 | 8.737→8737 | +1.540→+1540 / +21,4% | MDH |
| Avg unit price | G1-5 | soufre brut | — | 1.231→1231 | 1.099→1099 | — | DH/T |

- **Quantity:** narrative states imported **quantities rose +27,4%**; **no absolute tonnage is printed**. Tonnage NOT derived.
- **`9.102` is NOT a variant of `9.108`.** It is the ATPA-with-payment customs regime (T3-4), a different scope. `8.737` is the Asia-origin subset (T4-9). Neither substitutes for the T1-10 total.

## Retrieval method (reconstructable)
1. WebSearch → located the official annual-report URL (snippets used only to locate the URL; snippet numbers inadmissible).
2. WebFetch of the PDF (2.4 MB) — fetch tool could not parse compressed streams; binary saved; text extracted locally with pdfminer.six over the unencrypted PDF (a minimal `cryptography` stub was used because the environment's native crypto binding is broken; the PDF is not encrypted).
3. Searched extracted text for `soufre`; scope identities (T1-10 / T3-4 / T4-9, ATPA) confirmed by the source owner's independent re-check (ATPA appears 51× in the extract; T1-10/T3-4/T4-9 all present).

## Discipline notes
- Dot-thousands normalization applied; source literals preserved.
- No HS code asserted (none in source; memory-based "HS 2503" is inadmissible AI summary).
- No tonnage derived from value ÷ price. Scopes not mixed or reconciled.
