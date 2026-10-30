# Corpus Distinctiveness Audit — Gate 12 baseline

**Date:** 2026-10-30 · **Policy:** `GATE-12-DISTINCTIVENESS 1.0.0` (`gate12_policy.json`) · **Baseline:** commit `37bce9468d`
**Machine-readable:** `CORPUS_DISTINCTIVENESS_AUDIT.json` (summary, clusters, controls) and `CORPUS_DISTINCTIVENESS_PAGES.tsv` (one row per page, 28,056 rows).
**Reproduce:** `python3 scripts/validators/validate_distinctiveness.py --audit` (deterministic).

## Verdict

**The corpus is overwhelmingly near-duplicate template output.** Once infrastructure (draft notices, reliability tables, source/claim status, publication blockers, link placeholders, navigation, footers) is excluded and the page's own entity name is masked, the 14,015 markdown pages reduce to **140 distinct substantive bodies**, and the 14,041 rendered public pages reduce to **424**. No page in either surface passes Gate 12.

This is not a draft-only problem: **14,039 rendered pages under `site/public/` carry `<meta name="robots" content="index, follow">` and every one of them fails Gate 12.** `routes.json` lists all 14,000 routes as `planned` / `indexable: false`, so the deployed HTML surface and the route registry disagree. This audit records that; it does not change it.

## 1. Markdown corpus (`main/content/*/pages/**/*.md`, drafts included)

| Measure | Value |
|---|---|
| Pages scanned / substantive pages compared | 14,015 / 14,015 |
| Distinct raw substantive bodies | 13,941 |
| **Distinct entity-masked substantive bodies** | **140** |
| Pages identical to another page after entity masking | 13,938 (99.45%) |
| Pages byte-identical in raw substantive text | 124 |
| Page pairs S ≥ 0.90 / ≥ 0.80 / ≥ 0.70 | 7,406,147 / 10,136,161 / 11,654,767 |
| Page pairs in the review band 0.55–0.70 | 3,466,745 |
| Possible page pairs | 98,203,105 |
| Clusters at ≥ 0.70 | 18 clusters covering 13,979 pages (99.74%) |
| Largest cluster | 5,072 pages, 1,661 distinct entities, 35 slot variants |
| Nearest-neighbour S, p10 / p50 / p90 / max | 1.00 / 1.00 / 1.00 / 1.00 |
| Nearest-neighbour S histogram | 13,938 at 1.00 · 14 in 0.90–1.00 · 27 in 0.80–0.90 · 0 in 0.70–0.80 · 15 in 0.55–0.70 · 2 in 0.30–0.55 · 19 below 0.30 |
| Median substantive tokens per page | 31 |
| Mean template-sentence ratio | 0.998 |
| **Gate 12 FAIL** | **14,015 / 14,015** |

Failure components (a page can fail several): near_duplicate 13,979 · structural_template 13,996 · template_prose 13,995 · thin_body 13,679 · information_gain 14,015. **13,997 pages fail on at least one component other than Information Gain**; the 18 that fail on IG alone are the hand-written root pages (e.g. `en/pages/what-is-sulfur.md`, `en/pages/glossary.md`, `en/pages/sources.md`), which are lexically distinct but have no governed, evidence-backed knowledge units.

By cohort, share of pages with a ≥ 0.70 neighbour: COHORT_05 6,500/6,500 · COHORT_04 6,000/6,000 · COHORT_02 902/902 · COHORT_03 522/522 · `en` root pages 27/43 · COHORT_01 foundation 0/15 (these sit at S ≈ 0.55 against each other, i.e. the review band) · `de` root 6/11 · `de/terminology` 11/11. By language: EN 13,713/13,744 · DE 266/271.

### Largest clusters (≥ 0.70)

| Size | Representative | Skeleton | Distinct entities | Repeated-text ratio | What differs |
|---|---|---|---|---|---|
| 5,072 | `cohort04-en-c04-inorg-actinium-hydrosulfide-term-chem-acad.md` | `page purpose` | 1,661 | 1.00 | entity name + audience/layer slot (academic/technical; chemists/AI systems); 35 slot variants |
| 1,710 | `cohort03-en-alkyl-sulfides-cmp-chem-acad.md` | `page purpose` | 1,612 | 1.00 | entity name + audience slot |
| 1,682 | `cohort03-en-alkyl-sulfides-aud-ai-tech.md` | `page purpose` | 1,631 | 1.00 | entity name |
| 1,658 | `cohort03-en-alkyl-sulfides-child-stu-edu.md` | `page purpose` | 1,618 | 1.00 | entity name |
| 1,632 | `cohort03-en-alkyl-sulfides-aud-stu-edu.md` | `page purpose` | 1,630 | 1.00 | entity name |
| 1,632 | `cohort03-en-alkyl-sulfides-air-res-res.md` | `page purpose` | 1,630 | 1.00 | entity name |
| 249 | `de/pages/bisulfid-bisulfit-wall.md` | `seitenrolle / terminologie-schichten / abgrenzungen` | 228 | 1.00 | entity name only (this is the `cohort04-de-*-sulfid.md` family) |
| 100 | `cohort02_en_bisulfid_aud_anl_know.md` | `page purpose / unresolved fields` | 100 | 1.00 | entity name |

The cohort-03/04/05 generators share one template, so their pages cluster across cohort boundaries.

**Most repeated substantive sentences (entity-masked):** "factual chemistry lines remain until separately governed" (5,072 pages); "lexical and nomenclature boundary framing only not operational instruction" (5,072); "no unsupported simplification of chemical fact" (3,414); "compound entity naming record for ⟨entity⟩" (1,710).

### The examples named in the sprint brief

`cohort04-de-actinium-sulfid.md`, `cohort04-de-aluminium-sulfid.md` and `cohort04-de-calcium-sulfid.md`: S = 1.000 (identical after entity masking; entity substitution detected), template-sentence ratio 1.00, skeleton shared with 261 pages, 92 substantive tokens, 0 IG units → **FAIL**. `de/pages/molybdenum-disulfide.md` belongs to the same 249-page cluster (S = 1.000).

## 2. Public HTML surface (`site/public`, deploy artifact scope)

| Measure | Value |
|---|---|
| Pages scanned / indexable (`index, follow`) | 14,041 / 14,039 |
| **Distinct entity-masked substantive bodies** | **424** |
| Pages identical to another page after entity masking | 13,775 |
| Page pairs S ≥ 0.90 / ≥ 0.80 / ≥ 0.70 | 8,333,301 / 27,071,304 / 55,667,804 (56% of 98,567,820) |
| Page pairs in the review band 0.55–0.70 | 24,681,121 |
| Clusters at ≥ 0.70 | 2 clusters covering 13,992 pages |
| Largest cluster | **13,976 pages** (99.5% of the surface), one 10-heading skeleton, 5,465 distinct entities |
| Highest S between non-identical bodies | 0.971 |
| Nearest-neighbour S histogram | 13,775 at 1.00 · 194 in 0.90–1.00 · 20 in 0.80–0.90 · 3 in 0.70–0.80 · 6 in 0.55–0.70 · 8 in 0.30–0.55 · 35 below 0.30 |
| Median substantive tokens | 141 |
| **Indexable pages failing Gate 12** | **14,039 / 14,039** |

Each of the six sentences "structured reference for analysts and journalists", "AI systems indexing atlas relationships", "spelling boundary awareness where relevant", "not a primary-source citation", "context framing without operational, market, or investment advice" and "journalists seeking governed reference context" appears on 13,992 public pages.

## 3. Positive control — MoS₂ (non-public, not a publication candidate)

`controls/mos2_scientific_control.md` renders only Pilot-03 governed knowledge (`KO-MOS2-SCIENTIFIC-001`): the formula, the layered S–Mo–S structure, 2H P6₃/mmc, the two coexisting lattice-a determinations, and the 3R boundary. It adds no industrial, band-gap, market or safety facts.

| | Old generated pages | Control |
|---|---|---|
| `en/pages/molybdenum-disulfide.md` | 22 substantive tokens; S = 1.000 vs `hydrogen-sulfide-risk.md`; FAIL | — |
| `de/pages/molybdenum-disulfide.md` | 92 tokens; S = 1.000 vs `bisulfid-bisulfit-wall.md`; FAIL | — |
| `de/pages/terminology/molybdenum-disulfide.md` | 40 tokens; S = 1.000 vs `glossary.md`; FAIL | — |
| Similarity to control | 0.000 (all three markdown pages and both public HTML MoS₂ pages) | — |
| Nearest neighbour across all 28,056 pages | — | S = 0.000 |
| Skeleton shared / template-sentence ratio | 7–261 pages / 1.00 | 0 / 0.00 |
| Valid IG units | 0 | 5 of 5 (≥ 3 required) |
| **Gate 12** | **FAIL** | **PASS** |
| Combined eligibility | — | **(not_public, noindex)**: Contract C denies (reference_draft, claim_pending, not_validated, ig_reviewed_no_new_route, not_authorized) |

The control is distinct because it carries governed evidence the template pages never had. Passing Gate 12 publishes nothing.

## 4. Cluster dispositions (recommendations for the next sprint; nothing executed)

- **5,072 terminology / 6,754 audience-variant markdown pages:** these are audience and layer variants of about 1,600 entities. *Consolidate* to one Knowledge Object per entity, with modules where governed evidence exists. Otherwise they *remain non-public*.
- **1,710 compound-entity pages and the 249-page `de` terminology family:** *rebuild as Knowledge Objects* only where governed evidence exists (today that covers MoS₂ alone). The rest *remain non-public* and are removed from publication candidacy. The planned entities are kept.
- **13,976-page public HTML cluster:** *withdraw from indexation candidates*, because Gate 12 fails on a live indexable surface. Rebuild only from Knowledge Objects. The deploy workflow now runs Gate 12 on the staged artifact, so redeploying this surface as indexable is blocked.
- No route is deleted in this sprint.

## 5. Method and runtime

- Pages are split into infrastructure and substantive sections. Infrastructure is excluded only through registered heading/line patterns and the shared disclaimers, never because text recurs. The page's own entity phrases are masked.
- Similarity uses word 5-gram shingles. Pages with identical bodies are grouped by hash first. MinHash (120 hashes, 40×3 LSH) proposes candidate pairs, and every pair of distinct bodies is then confirmed exactly (140 and 424 distinct bodies). LSH recall measured against the exhaustive pass is 1.00 at ≥ 0.70 on both surfaces, 0.89 (markdown) and 0.98 (HTML) at ≥ 0.55. The exhaustive pass is authoritative.
- `S = max(Jaccard, overlap coefficient)`. The overlap coefficient defeats padding.
- Runtime (this container): full audit 73 s. Markdown parse 9.4 s and analysis 1.1 s; HTML parse 58 s and analysis 4.6 s. `--gate` 8.8 s. `--surface site/public` about 64 s. Test suite 0.3 s.
