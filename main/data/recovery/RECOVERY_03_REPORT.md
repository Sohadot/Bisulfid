# Recovery-03 — Reference Authority Activation & Controlled SEO Recovery

**Date:** 2026-10-30 · **Branch:** `claude/corpus-distinctiveness-audit-4wsa9f` · **Baseline:** Recovery-02 `fb940e6429`
**Live surface:** `site/public` unchanged since `b1757cb532`. This sprint changed no live HTML, robots file, sitemap, route, release-ledger record or deployment, and approved no decision.

## Verdict

**Substantive progress, no release.**
- The bisulfid/bisulfide reference went from 0 renderable modules to a full, evidence-only preview: 15 admitted records, 11 reviewed claims, Gate 12 PASS with 13/13 IG units.
  - It corrects the existing draft, which claimed that the two spellings name "the same underlying compound". The evidence does not support that.
- The homepage has EN and DE equivalents, reciprocal hreflang and an honest statement of editorial responsibility.
- MoS₂ was re-verified live with zero drift.
- The generated-identity surface has a measured plan.
  - The first wave is 15 URLs (0.12%), proposed only.
  - No canonical change is safe today.
- **Release eligibility now: none.** Every governed object derives Contract C `(not_public, noindex)`. The one action the owner can take immediately, with low risk, is approving the staged `/acquire/` `noindex, follow` change. It unblocks the deploy gate.

---

## A. Safety review of the cumulative branch

| Check | Result |
|---|---|
| `site/public`, robots, sitemaps, routes, release ledger changed vs `main` | **No** (diff contains none of them) |
| Deploy trigger | `workflow_dispatch` only, so merging deploys nothing |
| Deploy gate on the live surface | 14,040 LEGACY_STATUS_QUO, 1 BLOCK (`/acquire/`). Pre-existing, identical at `fb940e6429`. |
| Gate 12 / Gate 12-I / Contract C | Effective: Gate 12 is a veto in the authority, Gate 12-I governs institutional pages, and every KO derives Contract C. Property and IG suites pass. |
| Legacy hold | Intact; the shrink-only ratchet against `origin/main` passes |

Historical indexability is treated as **migration debt**: the RL debt (14,032 indexed legacy pages that fail Gate 12) is printed on every gate run. Nothing in this branch converts it into authorization.

**`/acquire/` correction, staged and not applied.**
- `URL-DEC-R03-ACQUIRE-001` is recorded with status `proposed`, so the resolver ignores it.
- The staged page `main/data/recovery/staged/acquire/index.html` and its patch change exactly one line: `index, follow` → `noindex, follow`.
- Body, canonical, outgoing links and the `mailto:` contact are unchanged; the page stays reachable.
- The release ledger was **not** edited. The page is brought into line with the ledger, not the reverse.
- Simulated on a copy of the surface: the gate reports 14,041 LEGACY_STATUS_QUO and PASS, and the Gate 12 surface counts are unchanged.
- Factual-claim review (`ACQUIRE_FACTUAL_CLAIM_REVIEW.json`) covers 7 statements:
  - 2 unsupported: "German-form spelling of a compound class", repeated.
  - 1 partly supported: the -id/-ide boundary.
  - 2 contradicted by site data:
    - "seven-language architecture": only EN and DE exist;
    - "no claim reaches a public page without a verified source": 12,289 generated unverified pages.
  - Rewordings are proposed. The lift condition: back to `index` only after a ledger release **and** correction of AQ-1..AQ-5.

## B. Terminology: Bisulfid, bisulfide and neighbours

**Sources.**
- 15 sources were fetched openly; for each, HTTP status, sha256 and verbatim passages were recorded (43/43 passages found). Capture file: `captures/R03_TERMINOLOGY_CAPTURES.json`.
- The IUPAC Gold Book (HTTP 403) and the Uni Rostock handout (HTTP 404) were recorded as unreachable. They were not bypassed and are not cited.

**Governed objects.**
- 14 sources verified (lock stays `candidate`).
- 13 narrow qualifications.
- 13 lexemes, plus a new concept `hydrogen_sulfite`.
- 16 `EVD-TERM-*` records, each with a capture locator.

**Claims.**

| Claim | Decision | Basis |
|---|---|---|
| EN *bisulfide* dictionary sense = **disulfide** | approved (narrow) | Merriam-Webster: ": disulfide", first use 1831 |
| EN *sulfide*, *disulfide*, *bisulfite* senses | approved (narrow) | Merriam-Webster entries (verbatim) |
| IUPAC names: HS⁻ = sulfanide / hydridosulfate(1−); S₂²⁻ = disulfide(2−) / disulfanediide; HSO₃⁻ = hydrogensulfite | approved (narrow) | Red Book 2005, IR-5.3.3.4 / IR-5.3.3 (PDF p. 86), IR-8.5 (p. 149) |
| DE *Sulfid* = salt of hydrogen sulfide | approved (narrow) | Duden and DWDS (eWDG 1976) |
| DE *Bisulfid*, *Hydrogensulfid* absent from DWDS contemporary sources | approved (narrow) | DWDS lookup statements (verbatim) |
| DE *Hydrogensulfide* = salts MᴵHS (technical usage) | approved (narrow) | Spektrum Lexikon der Chemie |
| DE -id ending rule | approved (narrow) | FH Münster teaching text |
| DE *Bisulfid* used for HS⁻ | **pending, boundary recorded** | Only source is industry (Badger Meter); `industry_publication` is not admissible for SD-TERMINOLOGY |
| "Bisulfid is the German spelling of bisulfide" | **not established** | Similar spelling ≠ equivalence. The English word itself has two attested referents. |
| CLM-TERM-001..005, GERMAN-ID-ACADEMIC-001 | superseded | Replaced by the narrower claims above |

**Distinctions kept on the page.**
- Attested dictionary sense (disulfide) vs database synonym (PubChem lists "bisulfide" under HS⁻, CID 5047209).
- Systematic names (IUPAC) vs historical/trivial forms (the bi- form).
- The brand name **BISULFID** is a site name, not a chemical claim.
- Competitor note: Wikipedia and its mirrors present bisulfide as HS⁻ and warn against confusing it with disulfide. The page shows that Merriam-Webster gives disulfide, and presents both with sources, without resolving the disagreement by assertion.

**Object and preview.**
- `KO-BISULFID-TERMINOLOGY-001` (4 concepts) with `PC-BISULFID-TERMINOLOGY-001`.
- IG pair: near_duplicate with the existing route, so no new URL.
- The renderer and Gate 12 IG now accept multi-concept objects; each IG unit stays specific to one concept.
- Preview at `previews/bisulfid-vs-bisulfide/`; it replaces the draft in place.
- The plan is now RENDERABLE: 6/7 modules. `de_usage` stays blocked.

## C. MoS₂ toward release

- **Accuracy:** 13/13 displayed fields equal the live COD CIFs 1010993/9007660, PubChem CID 14823 and NIST (`captures/R03_MOS2_RECAPTURE.json`). 3.161 Å lies inside 3.15(2) Å.
- **Admissibility:** 11/11 records admitted. **Gate 12:** PASS, 7/7 units.
- **Blockers,** with their order computed by `contract_c_derive` (`MOS2_RELEASE_READINESS.json`):

| # | Blocker | Owner |
|---|---|---|
| 1 | Claims are pilot, non-operational; no science approval posture exists in the claim registries | owner, claim policy |
| 2 | **Structural IG defect:** `ig_reviewed_no_new_route` normalizes to `ig_failed`, so R7 denies even the reconstruction of the object's own existing route | owner ratifies `AMD-IG-R03-001` (proposed) |
| 3 | `not_validated` | independent reviewer |
| 4 | Sources lock `candidate`, so evidence is not locked | source registry owner |
| 5 | `not_authorized`; governance still `reference_draft` | owner |

Resolving all of them, in order, gives `public_noindex` once IG passes and `public_indexable` once evidence is locked.
- **Competitors:** wider coverage (band gap, uses), but mixed experimental and DFT values. No section was expanded, because no governed evidence exists for those topics.

## D. Homepage and institutional foundation

- **`INST-HOME-EN` v1.1:**
  - Links both governed references.
  - Every number comes from the registries (`{{GOV:*}}`).
  - "Who is responsible" section: the publisher is the domain owner; no affiliation; **no named reviewer or credential is claimed**; validation is shown only after a review exists.
- **`INST-HOME-DE`:** the German equivalent of the same institutional function, written for German readers rather than translated word for word. Reciprocal `hreflang` en/de plus `x-default` is emitted only when both specs declare the same set; one-sided pairs are refused (tested).
- **R11:** `R11-HOME-EN-001` / `R11-HOME-DE-001` are `proposed`. They list the owner actions still needed: confirm the wording, decide on an editorial contact (the only verified address is commercial), and approve the live replacement.
- **Legacy renderer:** `atlas_render_dossier_l3.py` wrapped all 45 released institutional routes, including `/` and `/de/`, in compound-dossier boilerplate. It now skips them; this is tested.

## E. Generated-identity pages (12,289): risk-based plan

`R03_INDEXATION_REDUCTION_PLAN.json`. Search Console data is **not available** in the repository, so no traffic or indexation figure is asserted.

| Family | Pages | Disposition |
|---|---:|---|
| EN synthetic inorg / organo / ind variants | 2,504 / 2,448 / 2,416 | later temporary noindex (no canonical destination exists) |
| EN synthetic mineral / metal variants | 2,400 / 2,144 | rebuild a governed destination, then consolidate |
| EN synthetic boundary topics | 224 | preserve and rebuild (real terminology tasks) |
| DE element-Sulfid, PubChem name resolved | 78 | status quo, then rebuild |
| DE element-Sulfid, not resolved, Z < 104 | 21 | status quo (the screen is inconclusive: common compounds also miss) |
| **DE element-Sulfid, not resolved, Z ≥ 104** | **15** | **wave 1: temporary `noindex, follow` (proposed)** |
| DE named substances/terms | 25 | preserve and rebuild |
| pipeline/reference other | 14 | eventual retirement, with evidence only |

- **Canonicals:**
  - R-CANON-1 v1.1.0: similarity ≥ 0.80 only nominates. Identity, destination quality (Gate 12 PASS or a KO route) and Search Console concordance decide.
  - Of 453 nominated pairs, **0 are eligible**: all 106 destinations fail Gate 12.
- **Wave 1:**
  - 15 decisions `URL-DEC-R03-W1-*` (proposed).
  - Preconditions: owner approval, a Search Console export with no clicks or external links, and `/acquire/` fixed first.
  - Checks: diff covers robots and sitemap only; gate PASS; "Excluded by noindex" rises by ≤ 15; non-wave pages are unchanged.
  - Rollback: revert one commit.
- **Governance gap found:** the deploy gate accepts robots downgrades with no approved decision (verified by simulation). Approval is enforced only by review. A follow-up is proposed: require an approved decision for every legacy downgrade.

## F. Reference role and SEO comparison (preview vs live; automated measures, no ranking claims)

| Page | Live substantive tokens / Gate 12 | Preview tokens / Gate 12 | Search intent served | Structured data | Internal navigation |
|---|---|---|---|---|---|
| `/bisulfid-vs-bisulfide/` | 117 / FAIL (thin template) | 923 / PASS, 13 IG units | direct comparison, definition, bisulfide vs sulfide/disulfide/bisulfite, German term lookup | `DefinedTermSet` (values from evidence, no `sameAs`) | breadcrumb; links to MoS₂ and Methodology; linked from both homepages |
| `/` | 115 / FAIL | 362 / Gate 12-I PASS | brand and routing | `WebSite`, `inLanguage` | links to both references, Methodology, Sources, DE |
| `/de/` | 112 / FAIL | 295 / Gate 12-I PASS | brand (DE), routing | `WebSite` (de) | reciprocal hreflang with `/` |
| `/molybdenum-disulfide/` | 143 / FAIL | 591 / PASS, 7 IG units | entity, structure, polytype, lattice | `ChemicalSubstance` with `sameAs` PubChem/NIST | breadcrumb; DE terminology record; Methodology |

All four previews pass the SEO checks (title, description, single canonical, one h1, no skipped heading levels, links resolve, intents served, no placeholder leak) in `SEO_PREVIEW_ASSESSMENT.json`.

**Reliability and reference role:**
- Every value on the reference pages is a placeholder resolved from an admitted evidence record.
- Unsupported areas are stated in "What this reference does not establish".

### Safe PR sequence

1. **PR-1:** this branch (governance, previews, proposals). It deploys nothing.
2. **PR-2:** apply the `/acquire/` patch, after owner approval of `URL-DEC-R03-ACQUIRE-001`. The deploy gate turns green.
3. **PR-3:** owner ratification of `AMD-IG-R03-001` and of a science-claim approval posture (policy only).
4. **PR-4:** wave 1 (15 URLs), only with the Search Console export. Measure for 4–8 weeks.
5. **PR-5:** live replacement of `/` and `/de/` bodies, after R11 certification.
6. **PR-6:** live replacement of `/bisulfid-vs-bisulfide/` and `/molybdenum-disulfide/` bodies, after independent validation and source locking. Indexing follows only from Contract C.

### Actual release eligibility today

| Object | Contract C | Eligible |
|---|---|---|
| KO-MOS2-SCIENTIFIC-001 | (not_public, noindex) | no |
| KO-BISULFID-TERMINOLOGY-001 | (not_public, noindex) | no |
| Homepage EN/DE | no binding (R11 proposed) | no |
| `/acquire/` noindex,follow | staged | ready for owner approval |
