# Source Identity Verification Checklist

**Sprint:** pilot-01-evidence-admission-closure · **Date:** 2026-09-19
**Governed by:** `doctrine/SOURCE_POLICY.md`, `main/data/SOURCE_QUALIFICATION_PROTOCOL.md`, `DECISION_LOG.md`

## What this is (and is not)

**Source IDENTITY verification** answers one narrow question: *is the source in the registry the real, stable, correctly-described artifact it claims to be?* It is deliberately separated from three other, later, independent acts:

1. **source-USE qualification** (`source_use_qualification_registry.json`) — *may this source support this kind of evidence, scoped?*
2. **evidence admission** (`admissible()`) — *may this specific evidence assertion be admitted?*
3. **publication / indexation** (Contract C) — *may a route be published/indexed?*

Passing this checklist transitions a source's **bibliographic `status` from `seeded` → `verified`** under the `verification_limited` posture. It **never**: locks the source (`source_lock_status` stays `candidate`), approves a claim, activates a registry, publishes a route, or indexes anything. The registry file `status` stays `inactive`.

## The checklist (all items must pass)

For each source:

- **C1 — Artifact reachable.** The declared `url`/`doi` resolves to a live artifact (no fabricated/placeholder URL).
- **C2 — Artifact type matches.** The retrieved artifact's media type matches the described artifact (e.g. a PDF report is `application/pdf`; a reference file is the declared JSON).
- **C3 — Publisher / authority matches.** The declared `publisher` / `author_or_organization` is the true issuer of the artifact.
- **C4 — Title / edition matches.** The declared `title` and any version/edition (e.g. "HS 2022 (H6)") match what the artifact states.
- **C5 — Quoted content matches verbatim.** Any code/label/figure the registry or its downstream classification objects quote is present verbatim in the artifact (no memory, no paraphrase).
- **C6 — No credentials / no gate bypass.** Verification used only openly-fetchable artifacts; no authentication, login, or access-control bypass was performed. Gated endpoints stay recorded as gated.
- **C7 — identity_revision present & immutable.** The source carries a governed `identity_revision`; any change to bibliographic identity requires a new revision (which forces dependent qualifications to review-required).
- **C8 — Posture guardrails.** `source_lock_status` remains `candidate`; source is listed in `verification_lock_resolution.verification_ready_sources`; posture is `verification_limited`.

## Results — 2026-09-19

Scope: applied ONLY to the two Pilot-01 sources (no other source touched; no new source acquired — the two artifacts were re-fetched for verification only).

### SRC-UN-COMTRADE-HS2022 — **PASS → status `verified`**

| Item | Result |
|---|---|
| C1 reachable | PASS — `comtradeapi.un.org/files/v1/app/reference/H6.json` re-fetched (HTTP 200). |
| C2 type | PASS — JSON reference file, 6940 nomenclature rows. |
| C3 publisher | PASS — UN Statistics Division / UN Comtrade, official reproduction of WCO HS 2022; WCO is the underlying authority. |
| C4 title/edition | PASS — HS 2022 (H6) reference. |
| C5 verbatim | PASS — `250300` = "Sulphur of all kinds; other than sublimed, precipitated and colloidal sulphur"; `280200` = "Sulphur; sublimed or precipitated, colloidal sulphur" — verbatim match to `CLS-HS2022-2503-00` and its `excluded_forms_go_to`. |
| C6 no bypass | PASS — public reference JSON, no credentials. WCO's own HS Online / wcotradetools.org remain interactive/gated and were NOT bypassed. |
| C7 identity_revision | PASS — `rev-2026-09-19-1`. |
| C8 guardrails | PASS — `source_lock_status` candidate; listed in verification_ready_sources; posture verification_limited. |

Effect: use-qualification `QUAL-UN-HS2022-001` promoted `reviewed → qualified_narrow` (its criteria — verified identity + reviewed narrow scope — are now met).

### SRC-OC-MA-TRADE — **PASS → status `verified`**

| Item | Result |
|---|---|
| C1 reachable | PASS — annual-report PDF URL re-fetched (HTTP 200). |
| C2 type | PASS — `application/pdf`, 2,495,085 bytes, `%PDF-` header. |
| C3 publisher | PASS — Office des Changes (Royaume du Maroc), the official foreign-trade statistics authority. |
| C4 title | PASS — "Commerce extérieur du Maroc — Rapport annuel 2024". |
| C5 verbatim | PASS — product label "Soufres bruts et non raffinés" and the 2024 value/price figures were extracted verbatim in Pilot 01 (see evidence `EVD-MA-SULFUR-IMPORT-2024`, locators). |
| C6 no bypass | PASS — static official PDF only; the authenticated interactive database (`services.oc.gov.ma/.../login`) was NOT used. |
| C7 identity_revision | PASS — `rev-2026-09-19-1`. |
| C8 guardrails | PASS — `source_lock_status` candidate; listed in verification_ready_sources; posture verification_limited. |

Effect: use-qualification `QUAL-OC-MA-TRADE-001` is **NOT** promoted — it stays `reviewed`. Verifying the source's *identity* is a separate act from ratifying a *use-qualification*; the trade path's admission and sufficiency (`primary_plus_corroborating`, one non-independent source → `evidence_collecting`) are deliberately left unchanged.

## Non-effects (explicit)

Verifying these two identities changes **no** claim status, activates **no** registry, publishes **no** route, indexes **nothing**, and locks **no** source. Contract-C derived state for every Pilot-01 object remains `(not_public, noindex)`.

## Results — 2026-09-20 (Pilot 02 completion)

Scope: the two OCP sources, verified against the **original uploaded PDFs** provided by the user (no network fetch; the earlier Cloudflare block is moot when the original artifact is supplied directly).

### SRC-OCP-AFR-2024 — **PASS → status `verified`**

| Item | Result |
|---|---|
| C1 reachable | PASS — original PDF supplied locally (`Plaquette_OCP_IFRS_31Déc24_…vUK`). |
| C2 type | PASS — valid PDF, ~62 pages. |
| C3 publisher | PASS — OCP Group (OCP S.A.), the reporting entity. |
| C4 title/edition | PASS — Consolidated Financial Statements at 31 December 2024 (IFRS). Note: the uploaded file's edition datestamp (20 Mar 2025) differs from the URL-located re-issue (27 Mar 2025) of the same FY2024 work — a publication-revision nuance; FY2024 figures unchanged. `identity_revision rev-2026-09-19-1` (the bibliographic work) is unchanged. |
| C5 verbatim | PASS — Note 4.2.2 'Purchases consumed' ('In millions of dirhams'): **Sulfur (8,344) FY2024, (8,088) FY2023**; **Sulfuric acid (2,364)** is a DISTINCT line. MD&A sentence 'sulfur consumption volumes increased in correlation with the rise in sulfuric acid production' confirmed verbatim. |
| C5 auditors | PASS — an **independent auditors' report** on the FY2024 consolidated financial statements is present. |
| C6 no bypass | PASS — original local artifact; no credentials/login/TLS bypass. |
| C7 identity_revision | PASS — `rev-2026-09-19-1`. |
| C8 guardrails | PASS — lock candidate; listed in verification_ready_sources; posture verification_limited. |

Effect: `QUAL-OCP-AFR-001` promoted `candidate → qualified_narrow` for two explicitly-reviewed issuer-primary uses (FY2024 accounting sulfur line; FY2024 sulfur-consumption operational observation). Verification does **not** imply source-lock (stays candidate), claim approval, or publication.

### SRC-OCP-SUSTAINABILITY-2024 — **FAIL at C1 (2026-09-20 first pass) → later PASS**

First completion pass: the Sustainability Integrated Report 2024 PDF was not among the uploads → C1 failed → status stayed `seeded`, `QUAL-OCP-SUS-001` stayed `candidate`, Claim C BLOCKED.

### SRC-OCP-SUSTAINABILITY-2024 — **PASS (2026-09-20, page-excerpt supplied) → status `verified`**

A direct page-excerpt of the original report was then supplied (original report **page 20** = industrial-process statement; **pages 305–306** = third-party assurance).

| Item | Result |
|---|---|
| C1 reachable | PASS — original page-excerpt PDF supplied locally. |
| C2 type | PASS — valid PDF (5 extractable pages). |
| C3 publisher | PASS — OCP Group (OCP S.A.). |
| C4 title/edition | PASS — Sustainability Integrated Report 2024 (page-excerpt; page 305 folio and 'Sustainability Report 2024' present). |
| C5 verbatim | PASS — page 20: "…two platforms located in Jorf Lasfar and Safi. During processing, phosphate rock is combined with sulphuric acid to create phosphoric acid…These processing sites are equipped with sulphuric acid and phosphoric acid production lines…". |
| C6 no bypass | PASS — original local excerpt; no credentials/login/TLS bypass. |
| C7 identity_revision | PASS — `rev-2026-09-19-1`. |
| C8 guardrails | PASS — lock candidate; listed in verification_ready_sources; posture verification_limited. |

**Assurance bounding (pages 305–306):** third-party assurance (ISO 14064-1/-3, "reasonable assurance", GUTcert, Berlin 29 Jul 2025) covers **environmental metrics only** — GHG emissions (Scope 1/2/3 CO₂e), clean-electricity use ratio (80.00%), waste-management ratios, non-conventional-waters use ratio. It does **not** assure the page-20 industrial-process statement, which is issuer-reported but unassured. Those assured metrics are out of Pilot-02 scope and are not admitted as Pilot-02 claims.

Effect: `QUAL-OCP-SUS-001` promoted `candidate → qualified_narrow` for the site-scoped issuer-own process-context use. Verification does **not** imply source-lock (stays candidate), claim approval, or publication.

## Results — 2026-09-20 (Pilot 03 scientific provenance closure)

Verified against the uploaded artifacts (RSC 2015 full PDF; Huang 1981 thesis PDF; Acta 1983 page-404 excerpt image; Dickinson & Pauling 1923 first-page excerpt image; COD 1010993 CIF). All → status `verified`, lock **candidate**; no locking.

| Source | C-checks | Note |
|---|---|---|
| `SRC-RSC-MOS2-REVIEW-2015` | C1–C8 PASS | Full peer-reviewed review PDF; doi 10.1039/C4RA11852A; role secondary_scholarly. |
| `SRC-ACTACRYST-MOS2-1983-EXCERPT` | PASS (excerpt scope) | Page-404 image only; role primary_scientific; same originating work as COD 9007660. |
| `SRC-JACS-MOLYBDENITE-1923-EXCERPT` | PASS (excerpt scope) | First-page image only; no modern "2H"; same originating work as COD 1010993. |
| `SRC-HUANG-THESIS-1981` | PASS | M.S. thesis PDF; category academic_thesis; supporting only; related to the 1983 work. |
| `SRC-COD-MOS2-DICKINSON-1923` / `SRC-COD-MOS2-ACTACRYST-1983` | re-verified vs CIF | Provenance corrected: category `crystallographic_database`, role authoritative_database, originating_work_id + originating DOI retained; identity_revision → rev-2026-09-20-2. |

Retrieval repository ≠ originating scientific work; scientific independence judged on originating-work lineage. No lock, no claim approval, no publication.
