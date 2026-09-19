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
