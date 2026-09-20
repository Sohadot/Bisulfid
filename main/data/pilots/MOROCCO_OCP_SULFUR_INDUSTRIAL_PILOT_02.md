# Pilot 02 — Morocco OCP Sulfur Industrial Chain

**Date:** 2026-09-19 (opened) · 2026-09-20 (evidence completion) · **Baselines:** `4a685bc2a9` (completion) on `c2c390b670`.
**Scope:** "OCP Group × sulfur × Morocco industrial context × FY2024". Max three principal claims. Issuer-primary OCP official disclosures only.
**Constraints honored:** no public page, no route authorization, no sitemap/robots, no indexation, no 14K migration, no GCC/China/Germany expansion, no Arabic/French lexeme expansion, no Pilot 03, no PR. No third-party databases/press/market sites. No figure/sentence taken from prompt text or search snippets — everything below is extracted verbatim from the **original uploaded PDF**.

## Source availability

- **OCP Consolidated Financial Statements at 31 December 2024 (IFRS)** — original PDF **uploaded**. Identity **verified** (C1–C8; independent auditors' report present). `SRC-OCP-AFR-2024` → status **verified**, lock **candidate**.
- **OCP Sustainability Integrated Report 2024** — direct **page-excerpt uploaded** (original report page 20; pages 305–306 for assurance bounding). Identity **verified** (C1–C8 for the excerpt scope). `SRC-OCP-SUSTAINABILITY-2024` → status **verified**, lock **candidate**.

## Proven (issuer-primary, admitted evidence)

- **Claim A — sulfur purchase accounting fact** (`CLM-OCP-SULFUR-PURCHASE-FY2024`, evidence `EVD-OCP-SULFUR-PURCHASE-FY2024`). From the **audited FY2024 consolidated financial statements**, Note 4.2.2 "Analysis of purchases consumed and external charges" → "Purchases consumed", "In millions of dirhams", page 21:
  - **Sulfur — FY2024 source literal `(8,344)` → signed `-8344` MDH**; FY2023 `(8,088)` → `-8088` MDH (`NUM-ACCOUNTING-PAREN-NEG`). Derived magnitude 8,344 MDH is prose-only, not stored as competing truth.
  - Means only: *OCP's own consolidated statements report Sulfur under raw-material purchases/purchases consumed at the source-presented amount of (8,344) million dirhams.* NOT import value, NOT physical tonnage, NOT Morocco demand, NOT market size.
- **Claim B — sulfur consumption observation** (`CLM-OCP-SULFUR-CONSUMPTION-OBS-FY2024`, evidence `EVD-OCP-SULFUR-CONSUMPTION-FY2024`). Verbatim MD&A sentence (page 21): *"sulfur consumption volumes increased in correlation with the rise in sulfuric acid production."* Supported as an **issuer-reported operational observation**, FY2024-scoped. No tonnage, percentage, causal elasticity, or national consumption inferred.
- **Claim C — industrial process context** (`CLM-OCP-PHOSPHATE-SULFURIC-ACID-PROCESS`, evidence `EVD-OCP-PHOSPHATE-PROCESS-2024`). Verbatim page-20 statement: OCP's phosphate processing at **Jorf Lasfar and Safi** combines phosphate rock with sulphuric acid to create phosphoric acid; these sites are equipped with sulphuric-acid and phosphoric-acid production lines. Supported as **issuer-primary, organization-scoped, site-scoped process CONTEXT**. Does not by itself prove sulfur feedstock quantities or national demand. `sulphuric acid`/`phosphoric acid` kept as qualitative text; **no `sulfuric_acid` concept fabricated**.

## Blocked

- None. Claims A, B, C are all supported at their reviewed scope (A & B from the audited financial statements; C from the sustainability page-excerpt). Broader inferences (tonnage, national demand, market size, an upgraded relationship) remain out of scope by policy, not by acquisition.

## Source inconsistency (quarantined, excluded from admitted claims)

The same page-21 paragraph states sulfur purchases "decreased by 256 million dirhams due to the **drop in price per ton** ($127/T CFR in 2024 compared to $113/T CFR in 2023)". This is **internally inconsistent**: the quoted figures rise (127 > 113), not drop; and the Note 4.2.2 magnitude rises from 8,088 to 8,344 (a +256 change in magnitude), not a decrease. This statement is recorded in `EVD-OCP-SULFUR-CONSUMPTION-FY2024.quarantined_not_admitted` with `excluded_from_claims: true`, `resolution: none`. It was **not** silently fixed, years not reversed, no external knowledge used, and it is **not** used to explain the Claim-A accounting movement. Promotion to admitted evidence would require an explicit, separate resolution step that this sprint does not perform.

## Not inferred

- No sulfur import value; no physical sulfur tonnage from an accounting value; no Morocco-wide or national sulfur demand; no sulfur market size; no percentage/causal-elasticity from the consumption sentence; no assumption that all sulfur purchased was consumed in the period.
- **OCP is an organization, not Morocco.** No `GEO-MA → REL-INDUSTRIAL-USER → sulfur` was created from OCP evidence.
- 'Sulfuric acid' (FY2024 `(2,364)`) is a **distinct** raw-material line and is **not merged** into the sulfur claim.

## Relationship

`REL-INST-OCP-SULFUR-FY2024`: **ORG-OCP-GROUP → REL-INDUSTRIAL-USER → sulfur**, FY2024-bounded, `qualification_state = evidence_collecting`, evidence_ids = [purchase, consumption, phosphate-process]. **Not upgraded** to `evidence_qualified`: REL-INDUSTRIAL-USER requires primary production/statistical/scientific categories plus **independent** corroboration; OCP is a single issuer and all three records are not independent. Policy not weakened.

## Independence

The financial report and the sustainability report share the issuer (OCP Group). They are **not** independent corroboration. The financial statements being independently audited, and the sustainability report carrying (metric-scoped) third-party assurance, does not make OCP's reports independent publishers of each other. The independence evaluator returns **not independent** for the OCP units; the relationship correctly stays `evidence_collecting`.

## Evidence postures (via the real admission bridge)

| Record | Source verified | Qualification | admissible() | Review posture | Sufficiency pattern | Derived posture |
|---|---|---|---|---|---|---|
| `EVD-OCP-SULFUR-PURCHASE-FY2024` | yes | `QUAL-OCP-AFR-001` qualified_narrow | **True** | evidence_verified | single_authoritative_sufficient | **evidence_sufficient** (not locked — lock candidate) |
| `EVD-OCP-SULFUR-CONSUMPTION-FY2024` | yes | `QUAL-OCP-AFR-001` qualified_narrow | **True** | evidence_verified | primary_plus_corroborating | **evidence_collecting** (single issuer) |
| `EVD-OCP-PHOSPHATE-PROCESS-2024` | yes | `QUAL-OCP-SUS-001` qualified_narrow | **True** | evidence_verified | primary_plus_corroborating | **evidence_collecting** (single issuer) |
| Relationship `REL-INST-OCP-SULFUR-FY2024` | — | — | — | — | primary_plus_corroborating | **evidence_collecting** |

## Third-party assurance bounding (Claim C source)

The sustainability report's third-party assurance (pages 305–306: ISO 14064-1/-3, "reasonable assurance", GUTcert, Berlin 29 Jul 2025) covers **environmental metrics only** — GHG emissions (Scope 1: 3,365,208 tCO₂e; Scope 2: 767,239; Scope 3: 16,255,947; Total 20,388,394), clean-electricity use ratio (80.00%), waste-management ratios (99.06% / 15.03%), non-conventional-waters use ratio (66.89%). It does **not** assure the page-20 industrial-process statement (Claim C), which is issuer-reported but **unassured**. These assured environmental metrics are **out of Pilot-02 scope** and are **not** admitted as Pilot-02 claims.

Because source locks remain **candidate**, no branch is `evidence_locked`.

## Contract-C state

`(not_public, noindex)` for every Pilot-02 object. Nothing in this sprint authorizes publication, routes, sitemap, robots, or indexation.

## Policy findings

- Accounting sign law works end-to-end: `(8,344)` stored verbatim + normalized to `-8344`; magnitude is derived/labelled; a parenthesised literal stored positive is rejected.
- SD-CORPORATE-FINANCIALS single-authoritative works for a narrow issuer accounting line; SD-INDUSTRIAL keeps `primary_plus_corroborating`, so the corporate self-report supports Claim B as an observation but does not qualify the broader relationship.
- Same-issuer non-independence and organization≠geography both hold structurally.

## Next possible expansion (not started)

- Independent corroboration (official production/statistical/scientific) would be required to move `REL-INST-OCP-SULFUR-FY2024` beyond `evidence_collecting`.
- A governed `sulfuric_acid` concept only if concept-governance independently authorizes it. No Pilot 03.
