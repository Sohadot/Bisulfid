# Pilot 01 — Source Acquisition Dossier (Morocco × Sulfur Trade)

**Date:** 2026-09-19 · **Retrieval date:** 2026-09-19 · **Acquirer:** governed pilot ingestion.

## Source acquired
- **Authority:** Office des Changes — Royaume du Maroc (Morocco's official foreign-trade statistics authority).
- **Artifact used (primary official):** *Commerce extérieur du Maroc — Rapport annuel 2024* (official PDF).
- **URL:** https://www.oc.gov.ma/sites/default/files/2025-07/Rapport%20Commerce%20Ext%C3%A9rieur%202024%20VF.pdf
- **Interactive database (NOT used):** https://services.oc.gov.ma/DataBase/CommerceExterieur/login — authentication-gated; not fetchable; no credentials placed in git.
- **Canonical source id:** `SRC-OC-MA-TRADE` · **identity_revision:** `rev-2026-09-19-1` · **category:** `official_trade_statistics` · **status:** seeded · **lock:** candidate.

## Retrieval method (reconstructable)
1. WebSearch → located the official Office des Changes annual-report URL (search snippets used ONLY to locate the official URL; snippet numbers treated as inadmissible).
2. WebFetch of the PDF (2.4 MB) — the fetch tool could not parse the compressed streams, so the binary was saved and text extracted locally with pdfminer.six over an unencrypted PDF.
3. Searched the extracted text for `soufre`.

## Verbatim figures extracted (French, as printed) with locators
- **Product label:** `Soufres bruts et non raffinés` (crude and unrefined sulfurs). No HS/nomenclature code printed.
- **Top imported products table** (part of total imports **5,5%**): `Soufres bruts et non raffinés  18.758  7.994  9.102  5,5  +1.108  +13,9` → columns 2022, 2023, **2024 = 9.102 MDH**, part %, variation MDH, variation %.
- **Produits bruts breakdown table** (part **59,5%**): `Soufres bruts et non raffinés 18.768 8.007 9.108 59,5 +1.101 +13,8` → **2024 = 9.108 MDH**, +13,8% vs 2023.
- **Imports from Asia (Total Asie table):** `Soufres bruts et non raffinés 17.019 7.197 8.737 4,4 +1.540 +21,4` → **2024 (from Asia) = 8.737 MDH**.
- **Average unit price** (narrative + chart G1-5 "Evolution du prix moyen du soufre brut"): `1.231 DH/T en 2023 et 1.099 DH/T en 2024` → **2024 = 1.099 DH/T**.
- **Quantity:** narrative states imported **quantities rose +27,4%**; **no absolute tonnage is printed**.
- **Supplier table present:** `T1-11 Pays fournisseurs du soufre brut` (supplier-country detail — OUT OF SCOPE for Pilot 01, not ingested).

## Units / scope
- MDH = millions de dirhams (MAD millions). DH/T = dirhams per tonne. Reporter = Maroc. Flow = importations. Partner = Monde (total) for 9.102/9.108; Asie for 8.737. Period = calendar year 2024.
- **Within-source variation:** 9.102 MDH vs 9.108 MDH across two official tables (different aggregation scope) — recorded, not reconciled.
- **Provisional/final:** wording not located in the extracted tables; not asserted as final.

## Discipline notes
- Search-engine/AI summary numbers (e.g., a "1,099 DH/T" figure appearing in a search summary) were **not** used as evidence; the same figure was independently confirmed **from the official PDF itself** before recording.
- No HS code asserted (none in the source; memory-based "HS 2503" is an inadmissible AI summary).
- No tonnage derived from value ÷ price.
