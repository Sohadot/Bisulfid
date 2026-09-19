# Pilot 02 — Morocco OCP Sulfur Industrial Chain

**Date:** 2026-09-19 · **Baseline:** commit `c2c390b670` · **Scope:** "OCP Group × sulfur × Morocco industrial context × FY2024". Max three principal claims. Issuer-primary OCP official disclosures only.
**Constraints honored:** no public page, no route authorization, no indexation, no 14K migration, no GCC/China/Germany expansion, no Arabic/French lexeme expansion, no Pilot 03. No third-party databases/press/market sites. No credentials, no login, no TLS-verification bypass. No figure/sentence taken from prompt text or search snippets.

## Headline outcome

Pilot 02 is a **governance success by withholding**. BISULFID can now *represent* a corporate actor (organization identity, issuer-primary source categories, a corporate-financials domain, accounting numeric semantics) **and** it correctly refuses to assert anything, because the OCP primary documents **could not be opened in this environment**. All three principal claims are **BLOCKED**; the intended relationship is **not** created; Contract-C state is `(not_public, noindex)`.

## Official sources (located, registered, NOT verified)

| Source ID | Artifact | Category | Status / lock |
|---|---|---|---|
| `SRC-OCP-AFR-2024` | OCP Group — Consolidated Financial Statements at 31 December 2024 (IFRS), `www.ocpgroup.ma/.../Plaquette OCP IFRS_31Déc24_...vUK-2.pdf` | `corporate_financial_report` (new) | seeded / candidate |
| `SRC-OCP-SUSTAINABILITY-2024` | OCP Group — Sustainability Integrated Report 2024, `www.ocpgroup.ma/.../OCP_Sustainbility_Report-2024.pdf` | `corporate_sustainability_report` (new) | seeded / candidate |

Both were located on OCP's **official domain**. Each is registered with an immutable `identity_revision` (`rev-2026-09-19-1`) from first canonical registration.

## Proven

- **Nothing factual about sulfur or OCP.** No accounting value, no consumption sentence, no process statement is asserted. This is deliberate.
- **The governance architecture works and withholds** (see tests): organization identity resolves and is not a geography; issuer-primary evidence cannot satisfy sovereign trade claims; a sustainability report cannot establish a financial amount; a purchase line cannot establish physical tonnage; same-issuer reports are not independent corroboration.

## Not proven / not attempted

- Independence of the two reports: they share the issuer (OCP Group), so they are recorded as **non-independent** (common publisher/organization lineage). Where a pattern requires independent corroboration, the correct result is `evidence_collecting`.
- The intended relationship `ORG-OCP-GROUP → REL-INDUSTRIAL-USER → sulfur` (FY2024-scoped) is **not created**: no admitted evidence exists, and `REL-INDUSTRIAL-USER` requires primary categories (official production/statistical/scientific), which a single corporate self-report does not satisfy. Building it now would weaken `primary_plus_corroborating`; declined.

## Blocked

- **Acquisition of both OCP PDFs is blocked.** `www.ocpgroup.ma` serves a Cloudflare JS bot-challenge (HTTP 403 "Just a moment…") to `curl` and to WebFetch. The pre-installed Chromium can execute the challenge, but it cannot be made to trust the session's egress-proxy CA without a TLS-trust change that is disallowed in this environment (the attempt was denied). No credentials, login, or TLS-verification bypass were used — consistent with policy (this parallels the douane.gov.ma block in Pilot 01).
- **Claim A — sulfur purchase accounting fact** (`CLM-OCP-SULFUR-PURCHASE-FY2024`): BLOCKED. The exact accounting literal (an accounting-parenthesised amount in millions of dirhams) was **not** extracted. The accounting convention `NUM-ACCOUNTING-PAREN-NEG` is in place so that, once the PDF is obtained, a parenthesised literal will be stored verbatim and normalized to its correct **signed** value (negative), never silently to a positive magnitude.
- **Claim B — sulfur consumption operational observation** (`CLM-OCP-SULFUR-CONSUMPTION-OBS-FY2024`): BLOCKED. The sprint requires re-opening the original PDF for the exact sentence + locator; acquisition blocked, so nothing captured. No tonnage/causality/efficiency/national-demand inferred.
- **Claim C — phosphate + sulphuric-acid → phosphoric-acid process context** (`CLM-OCP-PHOSPHATE-SULFURIC-ACID-PROCESS`): BLOCKED. Not extracted. Kept as a *future* governed qualitative knowledge assertion; **no `sulfuric_acid` ontology concept was fabricated** (concept-governance not extended here).
- **The sulfur price statement is OUT OF SCOPE** and was not ingested. The sprint flagged an apparent directional inconsistency between the prose and the quoted figures; resolving it requires a visual/textual recheck of the original page, which acquisition blocks. No price figure is stored anywhere, and it is not used to explain any accounting movement.

## Policy findings

1. **Taxonomy:** an issuer's own audited/consolidated statements are not market/industry press. Added minimal governed categories `corporate_financial_report` and `corporate_sustainability_report`, each with authority **strictly limited to the issuer's own disclosed facts**. Category alone still never admits.
2. **New domain `SD-CORPORATE-FINANCIALS`** (distinct from `SD-TRADE`): a narrow accounting line from the issuer's own statements may use `single_authoritative_sufficient` **for that exact fact type only**. This does not alter trade/economics sufficiency, which stays `primary_plus_corroborating`.
3. **SD-INDUSTRIAL** now distinguishes issuer-primary observation (OCP's own operations, narrowly scoped) from analytical/economy-wide claims; broader industrial relationships still require `primary_plus_corroborating` (not weakened).
4. **Organization ≠ geography:** the organization registry forbids ID collision with geographies and stores identity only (no financials/relationship/route). Creating `ORG-OCP-GROUP` implies no relationship.
5. **Accounting sign law:** parentheses mean negative and are never silently dropped; a positive magnitude for prose is derived and must be labelled, never stored as competing truth. A validator rejects a parenthesised literal stored as positive.
6. **Independence lineage:** two artifacts from one issuer are not independent; recorded explicitly.

## Next possible expansion (not started)

- Obtain the two OCP PDFs by a permitted route (e.g. a browser-CA permission so Chromium can clear the Cloudflare challenge, or the user supplying the files), then run C1–C8 identity verification, extract the exact accounting literal / consumption sentence / process statement, create separate atomic evidence records, and re-derive postures.
- Only if evidence genuinely supports it: qualify a FY2024-scoped `ORG-OCP-GROUP → REL-INDUSTRIAL-USER → sulfur` relationship (issuer-specific, never `GEO-MA → … → sulfur`).
- A governed `sulfuric_acid` concept, only if concept-governance is ready (not forced into the generic sulfur concept).
- No Pilot 03.

## Tests

`pilot_02_tests.py` (organization resolves; org ≠ geography; identity_revision present; accounting `(8,344)` literal + signed normalization + parentheses-drop guard; magnitude not confused with trade value; corporate evidence cannot satisfy sovereign trade; sustainability cannot establish a financial amount; purchase cannot establish tonnage; deny-by-default candidate; price statement absent; relationship period-bounded and not created; same-issuer not independent; no sulfuric-acid concept; verification ≠ lock; admission ≠ activation; relationship ≠ route; Contract-C derived). Plus every prior governance + Pilot-01 regression suite.
