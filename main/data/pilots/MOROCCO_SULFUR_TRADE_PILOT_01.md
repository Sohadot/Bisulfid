# Pilot 01 — Morocco × Sulfur Trade — Evidence Acquisition Report

**Date:** 2026-09-19 · **Baseline:** commit `bc20510d4c` · **Scope:** `GEO-MA × sulfur × SD-TRADE`, relationship `GEO-MA → REL-IMPORTER → sulfur`.
**Outcome headline:** the architecture ingested one real official source, captured true figures with a reconstructable locator, and **correctly withheld** admission/qualification/publication. Derived Contract-C state = **`(not_public, noindex)`**. This is a successful pilot.

---

## PROVEN (supported by the official source)
- **Product label identity (source-internal):** Morocco's official trade statistics record a product line labelled **"Soufres bruts et non raffinés"** (crude & unrefined sulfurs).
- **Claim B — import observation:** Morocco **recorded imports** of "Soufres bruts et non raffinés" in **calendar year 2024** (Office des Changes annual report; multiple tables + a supplier-country table).
- **Claim C — quantitative measure (value + unit price):** 2024 **TOTAL import value = 9108 MDH** (T1-10; source literal "9.108", dot = thousands separator); **average unit price = 1099 DH/T** (G1-5; literal "1.099"). Different scopes, kept separate: **ATPA-with-payment = 9102 MDH** (T3-4), **Asia-origin = 8737 MDH** (T4-9) — neither is the total. Absolute tonnage BLOCKED (only +27,4% change printed).

## NOT PROVEN (intentionally not inferred)
- Morocco "depends on" / is a "major importer of" sulfur — analytical, out of scope.
- Any link to phosphate/fertilizer/OCP/sulfuric-acid demand — out of scope (Pilot 02).
- Absolute **import tonnage** — the source prints only a +27,4% quantity change and a unit price; tonnage was **not derived** from value ÷ price.

## BLOCKED (governance/architecture correctly prevented)
- **Claim A — HS classification identity:** the source states **no HS code**; no authoritative classification source (WCO/ADII) was fetched; and "crude & unrefined" is a **subset** of the general `sulfur` concept. Recorded as BLOCKED; not fabricated from memory.
- **Admission of the trade evidence:** `QUAL-OC-MA-TRADE-001` is state **`reviewed`** (the source is brand-new, `seeded`/`candidate`, not identity-verified), so `admissible()` **withholds**. Independently, `SD-TRADE` requires **primary_plus_corroborating** and only one **non-independent** official source exists → **evidence_collecting**. Two independent gates hold the line.
- **Quantitative measure as a qualified figure:** trade quantitative evidence requires a commodity **classification code/version**, which is absent → the measure cannot be promoted to a qualified figure.

## POLICY FINDINGS (report only — no policy changed mid-pilot, per brief §13)
1. **Corroboration vs. sovereign primary source.** For a narrowly-scoped "recorded import exists" observation, the **national official trade authority is itself the primary record**; genuinely independent corroboration effectively does not exist (UN Comtrade / ITC / WITS derive from the same national reporting chain → **non-independent**). Requiring `primary_plus_corroborating` here may be **too strict**. Proposed (separately): a `single_official_record_sufficient` pattern for narrowly-scoped recorded-observation claims from a qualified national statistics authority, distinct from analytical/market claims. **Not applied.**
2. **New-source admission floor.** A brand-new official source cannot admit evidence until it clears identity verification (state must reach `qualified`/`qualified_narrow`). This is correct, but the pilot shows we need a defined **verification path for a new official source** (who verifies, against what) before Pilot 02.
3. **Classification dependency.** Trade quantitative evidence needs an HS/nomenclature identity the national summary report does not carry. A **classification-acquisition step** (WCO/ADII) must precede quantitative trade admission.
4. **Locale numeric normalization + scope discipline.** The report's dots are thousands separators (9.108 = 9108 MDH; 1.099 = 1099 DH/T). Evidence now stores `source_literal` + `normalized_value` + `unit`, validated by a source-specific normalization law. The earlier "9.102 vs 9.108 variance/conflict" reading was WRONG: 9108 = total imports (T1-10), 9102 = ATPA-with-payment regime (T3-4), 8737 = Asia origin (T4-9) — three different scopes, never variants and never reconciled.

## Derived states
- **Evidence posture (governed derivation):** `evidence_collecting`.
- **Relationship `REL-INST-MA-SULFUR-IMPORT-2024`:** `GEO-MA → imports → sulfur`, period 2024, `qualification_state = evidence_collecting`.
- **Contract-C:** `(not_public, noindex)`.

## Artifacts created
- Source `SRC-OC-MA-TRADE` (seeded/candidate, identity_revision); qualification `QUAL-OC-MA-TRADE-001` (reviewed); evidence `EVD-MA-SULFUR-IMPORT-2024`; relationship instance `REL-INST-MA-SULFUR-IMPORT-2024`; non-operational pilot claims; acquisition dossier; 16-proof test suite.

## Next possible expansion (only after review — NOT started)
- Acquire the HS/nomenclature classification from an authoritative source (WCO/ADII) to resolve Claim A and the classification dependency.
- Decide the corroboration-policy amendment (finding 1) and the new-source verification path (finding 2).
- Add a second, genuinely-independent official period/source, or ratify single-official-record sufficiency, before promoting the relationship beyond `evidence_collecting`.
- **Pilot 02 (Morocco Industrial Chain / OCP)** — deferred.
