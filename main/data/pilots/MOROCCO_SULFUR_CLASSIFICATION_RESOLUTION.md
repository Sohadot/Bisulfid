# Pilot 01 — Morocco Sulfur Classification Resolution

**Date:** 2026-09-19 · **Baseline:** commit `da896cf0b7` · **Scope:** resolve the classification identity behind the Office des Changes label "Soufres bruts et non raffinés". No route/publication/indexation/14K/Pilot-02.

## Proven (official sources)
- **HS 2022 international identity — PROVEN.** From the official **UN Comtrade HS 2022 (H6) reference** (`comtradeapi.un.org/files/v1/app/reference/H6.json`, retrieved 2026-09-19; official intergovernmental reproduction of WCO HS 2022; WCO is the underlying authority):
  - **2503 / 2503.00** = *"Sulphur of all kinds; other than sublimed, precipitated and colloidal sulphur"* (verbatim).
  - **Chapter 25** = *"Salt; sulphur; earths, stone; plastering materials, lime and cement"*.
  - Classification object: `CLS-HS2022-2503-00` (system=WCO HS, version=HS 2022 (H6), object_type=hs_subheading).

## Exclusions (boundary preserved, machine-readable)
- **2802 / 2802.00** = *"Sulphur; sublimed or precipitated, colloidal sulphur"* (verbatim). So **sublimed, precipitated, colloidal** sulphur are **outside** 2503 and outside the traded product's scope. The BISULFID generic `sulfur` concept is broader than 2503; 2503 is a scoped subset.

## Mapping (WCO HS ↔ Moroccan nomenclature ↔ Office des Changes label)
| Layer | Object | Status |
|---|---|---|
| International HS heading/subheading | `25.03` / `2503.00` (HS 2022) | **PROVEN** (UN Comtrade H6) |
| Moroccan national SH code | (unknown digits) | **BLOCKED** — douane.gov.ma tariff endpoints WAF/access-restricted; no login workaround (§P) |
| Office des Changes label | "Soufres bruts et non raffinés" (produit remarquable) | **statistical grouping**; no SH code printed in the annual report |
| OdC label → HS 2503 | correspondence | **HYPOTHESIS only** — label text ("bruts et non raffinés" = crude and unrefined) is consistent with 2503 scope, but no official mapping artifact was acquired |

## Not proven
- The exact **Moroccan national tariff/statistical code** for the product.
- The **official OdC-produit-remarquable → HS** mapping (could be a one-code commodity or an aggregation of several HS lines). Treated as `statistical_product_grouping` (`CLS-MA-ODC-SOUFRES-BRUTS`), **not** forced to a one-to-one HS code.

## Effect on Pilot 01
- **Claim A:** BLOCKED → **PARTIAL** (WCO/HS side proven; Moroccan mapping blocked).
- **Claim B / C:** unchanged — Claim B (import observation) PROVEN; Claim C (total value 9108 MDH, unit price 1099 DH/T) supported; tonnage still BLOCKED.

## Effect on the relationship
- `GEO-MA → REL-IMPORTER → sulfur` stays **evidence_collecting** (Outcome 2): because the OdC-product → HS-concept mapping is unproven, the generic `sulfur` object is **not** upgraded. `object_ref = sulfur` is retained only with an explicit commodity-scope qualifier ("crude/unrefined subset; Moroccan mapping unproven"). Trade sufficiency policy (`primary_plus_corroborating`) is **unchanged**.

## Sources
- UN Comtrade HS 2022 (H6) reference — https://comtradeapi.un.org/files/v1/app/reference/H6.json
- WCO HS 2022 edition (authority; artifact interactive/not directly fetched) — https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2022-edition.aspx
- Moroccan customs tariff Chapter 25 (access-restricted this sprint) — https://www.douane.gov.ma
