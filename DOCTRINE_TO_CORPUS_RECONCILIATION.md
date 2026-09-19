# BISULFID — Doctrine-to-Corpus Reconciliation

**Type:** Read-only analysis. No production data modified.
**Date:** 2026-09-19
**Scope:** `sohadot/bisulfid` @ `main` (last production commit 2026-07-29, PR #105)
**Mandate:** Reconcile the deployed 14K public dossier surface with the original BISULFID doctrine. Prove exactly where conceptual richness was lost between doctrine and production. Propose the smallest set of amendments. Do **not** execute changes.

> **Governing finding.** The doctrine and the machine-readable governance model (`routes.json`, `corpus_route_formula.json`, `sitemap_policy.json`, the reference/audience registries) are internally coherent and already forbid thin-page volume. The failure is **not** in the doctrine and **not** in the route registry. It is a **fork between two publication authorities**: `routes.json` (governance truth) says all 14,000 routes are `planned / indexable:false / in_sitemap:false`, while `release_ledger.json` (Sprint 99) independently marked **13,998 routes `released` + `indexable:true`** with `source_pack_id: null` and `validation_status: pending`. The deployed site obeys the ledger, not the registry. Everything below follows from that fork.

---

## A. Original thesis — what the repository intended BISULFID to become

From `doctrine/ASSET_THESIS.md`, `PROJECT_DOCTRINE.md`, `GLOBAL_REFERENCE_STANDARD.md`, and `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`:

- **A sovereign reference layer for sulfur *terminology intelligence*** — explicitly "not a chemistry website," "not a generic sulfur content site," "not a content farm" (`ASSET_THESIS.md`, `PROJECT_DOCTRINE.md §Identity Rules`).
- **Depth over volume, as a hard rule:** *"A single authoritative page is worth more than ten thin pages… No thin pages published to fill route coverage"* (`GLOBAL_REFERENCE_STANDARD.md`). *"No language layer exists only for SEO volume."*
- **Source-governed and claim-governed:** *"No source entry = no published claim"* (`SOURCE_POLICY.md`). Every claim traces to `source_registry.json`; claims live in `main/data/claims/`.
- **A large corpus — but only under gates.** `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` sets **500 governed pages as the *minimum* public-launch floor (Sprint 5H)**, scaling to 1,000+ then 3,000+ *"while strict quality gates remain in force."* It names the exact failure mode we are now in: *"500 weak pages = same as failure."*
- **Publication ≠ indexation ≠ full authority.** The architecture separates these three concepts explicitly and stages them: Blueprint → Route registration → Draft → Source-lock → Claim approval → Quality Gate.
- **SEO is subordinate to reference quality** (`SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md §Launch strategy`: *"Launch is authority-first; SEO tactics subordinate to doctrine."*).

**The prompt's non-negotiable objective is already the repository's stated objective.** This is a return-to-doctrine task, not a new direction.

---

## B. Existing architecture — what already exists and is sound

The governed data model is richer than the deployed site suggests. Present and coherent today:

| Asset | State | Evidence |
|---|---|---|
| **8-dimension route identity formula** | codified | `corpus_route_formula.json`: `{language}:{term_entity}:{page_type}:{audience}:{source_posture}:{claim_posture}:{indexation_posture}:{internal_link_role}` |
| **Anti-Cartesian / anti-thin rules in the formula itself** | codified | `"dimensional_intersection_not_volume_inflation"`; rules *"Reject thin pages"*, *"Reject free-form LLM generation; generator must read registries"*, *"Not every Cartesian product is valid"* |
| **9 reference layers (domain-ish)** | codified | `reference_layer_registry.json`: academic, knowledge, research, educational, economic, institutional, technical, linguistic, logistical — each with own source/claim posture and `indexation_default: noindex_default` |
| **Explicit anti-duplication rule** | codified | `reference_layer_registry.json`: *"A route may exist only if reference_layer changes structure, purpose, evidence standard, vocabulary level, internal links, or claim boundary…"* — an **embryonic Information Gain Gate** |
| **9 audience layers** | codified | `audience_layer_registry.json`: chemist, researcher, analyst, government, investor, company, student, ai_system, child_edu — each with allowed/forbidden claim classes |
| **19 page-type families** | codified | `page_type_registry.json` (PT_TERM_CANONICAL, PT_DIFFERENCE_COMPARISON, PT_AI_READABLE, PT_INVESTOR_ECONOMIC, PT_GOVERNMENT_POLICY, …) |
| **Route registry** | governed, LOCKED | `routes.json`: 14,000 routes, **all `status: planned`, `indexable: false`, `in_sitemap: false`, `in_navigation: false`** |
| **Sitemap policy** | doctrine-faithful | `sitemap_policy.json`: `status: inactive`, `urls: []`, excludes planned/draft/non-indexable/non-QG routes |
| **Source & claim registries** | present, mostly inactive | `source_registry.json` (15 entries); `claims/claim_library.json` `status: inactive`; 8 source packs (`architecture_active`) |
| **7-language model** | codified | `languages.json`: EN/DE/AR/ZH/JA/FR/ES, all `status: planned`, identity=de, market-chain=ar |
| **11-gate Quality Gate + CI** | passing | `QUALITY_GATE.md`; Corpus Governance CI L0/L1/L2 all PASS (re-run 2026-09-19) |

**Conclusion for B:** The "sovereign reference architecture" the prompt asks for is ~70% already designed. The evidence model, geography, and temporal dimensions are the notable gaps (Section C).

---

## C. Lost dimensions — concepts in doctrine that were reduced or flattened in production

Method: audited the union of keys across `routes.json` (14,000 records) and the release ledger, and checked whether each doctrine concept is a **first-class, machine-readable route dimension**.

`routes.json` record schema (actual):
`route_id, path, language, locale, source_language, title, description, h1, layer, template, content_file, status, indexable, in_sitemap, in_navigation, translation_status, hreflang_group, alternate_routes, required_internal_links, required_claim_groups, source_required, risk_level, notes`

| Doctrine concept | Doctrine home | First-class in `routes.json`? | Verdict |
|---|---|---|---|
| **Geography / jurisdiction** | Germany, Morocco, Gulf, China all named in `ASSET_THESIS`, `MULTILINGUAL_POLICY`, README | **0 / 3,000 sampled** | **LOST / collapsed into `language`.** `de` is treated as Germany, `ar` as "Gulf+Morocco." The prompt's conceptual correction is correct and the repo proves it: geography is not a dimension. |
| **Domain (chemistry/physics/economic/regulatory/linguistic…)** | 9 reference layers in `reference_layer_registry.json` | **0 / 3,000** (`reference_layer` is not a route field) | **REGISTERED BUT NOT WIRED.** The domain taxonomy exists as a standalone registry but is not part of route identity or route records. The route_key formula omits it too. |
| **Supply-chain role** | Gulf supply / Morocco phosphate demand (`MULTILINGUAL_POLICY`); `REF_LOGISTICAL` layer | **0 / 3,000** | **LOST.** Only survives as prose in doctrine. |
| **Temporal validity** | implied by "market reports with date," regulatory currency | **0 / 3,000** (no `valid_from`/`valid_to`/`period`) | **ABSENT ENTIRELY.** No page can express "as of year X" or "effective date." |
| **Evidence provenance (atomic)** | `SOURCE_POLICY` (source_id, date, doi, linked_claims) | Only `source_required` (bool) + `required_claim_groups` on the route | **FLATTENED.** Provenance is a coarse boolean/state, not an auditable evidence record with geography/period/methodology/retrieval date. |
| **Audience / source-posture / claim-posture / indexation-posture / internal-link-role** | 5 of the 8 formula dimensions | **Not explicit route fields** (`routes.json` has only `layer`, `source_required`, `required_claim_groups`, `risk_level`) | **PARTIALLY IMPLEMENTED.** The rich 8-dimension formula was only coarsely reflected in the actual route registry. |

**Where the domain richness actually went:** the post-hoc `14K_CORPUS_CLASSIFICATION` (Sprint 98) shows the 14,000 routes collapsed into production lanes dominated by **10,908 "low-risk terminology" + 2,416 "industrial-context"**, with **academic = 0, economic/investment = 1, journalistic = 0, biotechnology = 0, student = 0**. The multi-domain, multi-audience intersection the doctrine promised did not materialize; it became one giant terminology-permutation lane.

---

## D. Existing safeguards — rules already present (do not reinvent)

These are already codified and should be **reused**, not rebuilt:

- **Anti-thin:** `GLOBAL_REFERENCE_STANDARD.md` ("no thin pages… depth over volume"); `corpus_route_formula.json` ("Reject thin pages: fewer than required_data_fields satisfied"); Quality Gate **Gate 05** ("No thin pages in the sitemap").
- **Anti-duplication:** `reference_layer_registry.json §anti_duplication_rule` — a route may exist only if its reference layer changes structure/purpose/evidence/vocabulary/links/claim boundary. This is the seed of the Information Gain Gate.
- **Anti-free-form-LLM:** `corpus_route_formula.json` — "Reject free-form LLM generation; generator must read registries"; `SOURCE_POLICY.md` — "AI-generated text is not a source."
- **Source discipline:** `SOURCE_POLICY.md` — "No source entry = no published claim"; permanently blocked content list (market stats w/o source, bisulfite-as-bisulfide, safety thresholds, medical, handling, procurement, acquisition targeting).
- **Claim discipline:** claim registries per class; `claim_library.json status: inactive`; publication requires `claim_approved`/`claim_approved_narrow`.
- **Audience discipline:** per-audience allowed/forbidden claim classes (`audience_layer_registry.json`).
- **Multilingual discipline:** `MULTILINGUAL_POLICY.md` — no partial language, no MT-only page, hreflang must resolve, unpublished languages excluded from sitemap.
- **Publication ≠ indexation:** `corpus_route_formula.json indexation_posture default_for_new_routes: non_indexable`; `sitemap_policy.json` exclusion rules; architecture's staged model.
- **500-page governed floor:** `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`.

**The prompt's requested Information Gain Gate, evidence model, and lifecycle are extensions of rules that already exist — not new inventions.**

---

## E. Implementation divergence — exactly where production forked from the rules

Four distinct causes, separated as the prompt requires:

**E1 — Deliberate historical decision: the "cautious reference framing" dossier release (Sprint 99, 2026-06-05).**
`DECISION_LOG.md` (line ~4527): *"Public dossier release at 14K scale is authorized only when pages use cautious reference framing, pass validation, appear in the release ledger and sitemap, and do not convert source-required terminology into unsupported scientific claims."* This was a conscious choice to publish 13,998 pages that make **no source-required factual claims** (hence `claim_set_id: "cautious_framing"`, `source_pack_id: null`). Intent: ship a large surface without violating `SOURCE_POLICY`. It technically avoids unsourced *claims* — but it collides head-on with the **depth-over-volume** and **anti-thin** rules, because "no real claim" also means "no real information gain."

**E2 — Architecture limitation: the release ledger became a *parallel publication authority* that bypasses `routes.json`.**
`DECISION_LOG.md` (line ~4416, ~4551): *"The release ledger is the source of truth for which routes are public."* But `routes.json` still says all 14,000 are `planned / indexable:false / in_sitemap:false`. Two sources of truth now disagree:

| Field | `routes.json` (governance) | `release_ledger.json` (deployed) |
|---|---|---|
| status / release_status | `planned` (14,000) | `released` (13,998) |
| indexable | `false` (14,000) | `true` (13,998) |
| in_sitemap | `false` (14,000) | assigned to 9 shards (13,998 URLs) |
| source backing | `source_required` per route | `source_pack_id: null` |
| validation | Quality Gate pending | `validation_status: pending` |

The route formula's own rule — *"Reject public indexation unless indexation_posture is indexable_approved and all publication locks cleared"* — was never enforced against the ledger path.

**E3 — Implementation shortcut: Route → Template → Generated Text (the exact anti-pattern the prompt names).**
The generators (`generate_14000_corpus_expansion_v1.py`, `generate_7500_…`, `generate_1500_…`) fill templates across `{compound} × {facet: cmp|aud|air|term} × {audience: ai|res|stu|chem…} × {sub: tech|res|know|edu…}`. Measured on deployed output:
- Sample thin page `.../hydrosulfide/aud/res/res/` ≈ **392 visible words**, `robots: index, follow`, `source_pack_id`-less.
- Two siblings (`…/aud/res/res/` vs `…/aud/stu/edu/`) are **~84% textually identical** (SequenceMatcher 0.841) — audience label swap, same facts.
This is `Route → Template → Text`, precisely inverted from the doctrine's `Evidence → Knowledge Object → Reference Surface`.

**E4 — Current SEO/indexation problem (the visible symptom).**
Deployed `site/public`: **14,039 pages `index, follow`**, `robots.txt: Allow: /`, **9 sitemaps = 13,998 URLs**. Google Search Console (24/07/2026): **3 pages indexed**; ~3,369 "Discovered – not indexed" + 132 "Crawled – not indexed" — the thin/doorway verdict. The site's **own Sprint 98 classification** had already flagged **13,956 routes as `blocked_source_required`** and only **26 as eligible** — one day before Sprint 99 released 13,998 of them anyway. The contradiction is internal and dated.

**Net:** doctrine intact → registry intact → **ledger + generators + deploy diverged**. The fix targets E1–E4, not the doctrine or `routes.json`.

---

## F. Proposed minimal architecture amendments (extension, not rewrite)

Ordered smallest-first. None deletes routes or content.

1. **Re-assert `routes.json` as the single publication authority; demote the release ledger to a *record* of ledger decisions, reconciled against `routes.json`.** Add a validator (`validate_ledger_route_consistency`) that fails CI when `release_ledger.indexable` disagrees with `routes.json.indexable`. This closes the E2 fork without touching content.
2. **Wire the three existing-but-orphaned dimensions into the route record:** add `reference_layer` (from `reference_layer_registry.json`), `audience_layer`, and `indexation_posture` as explicit `routes.json` fields. These registries already exist; this only connects them.
3. **Add three genuinely missing dimensions as *optional, nullable* route fields:** `geography` (ISO-3166 / region enum), `domain` (maps to reference_layer), `temporal_validity` (`valid_from`/`valid_to`/`as_of`). Nullable = no forced backfill; a route without evidence simply leaves them empty (honesty requirement).
4. **Introduce an atomic evidence store** (`main/data/evidence/`) keyed by `evidence_id`, linking `source_id → claim_id → route_id` (Section G). This is additive to the existing source/claim registries.
5. **Codify the Information Gain Gate** as a validator (`validate_information_gain`) built on the existing `anti_duplication_rule` (Section I).
6. **Map the deployed 14K into lifecycle states** (Section L) inside `release_ledger` records — a classification pass, not a content change.

**Explicitly out of scope of these amendments:** deleting routes, rewriting pages, changing the route_key formula, activating claims, changing source states, altering live indexation. (Those await an approved implementation sprint.)

---

## G. Evidence model — minimal atomic schema

Smallest robust record that supports serious reference work, connecting to today's `source_registry.json` and `claims/`:

```jsonc
// main/data/evidence/<evidence_id>.json  (proposed, additive)
{
  "evidence_id": "EVD-…",              // stable, unique
  "entities": ["term_entity_id", …],   // -> ontology/sulfur_terms.json
  "domain": "chemistry|linguistic|economic|institutional|…", // -> reference_layer_registry
  "geography": "DE|MA|SA|CN|GLOBAL|null",                     // ISO-3166 or region; null allowed
  "jurisdiction": "authority/instrument id | null",           // for regulatory evidence only
  "claim_scope": "exact scope of what this supports",
  "claim_id": "CLM-…",                 // -> claims/*.json
  "source_id": "SRC-…",                // -> sources/source_registry.json (REQUIRED)
  "source_type": "authoritative_dictionary|chemical_nomenclature_standard|government_scientific_database|…",
  "language_of_evidence": "en|de|ar|…",
  "publication_date": "YYYY-MM-DD",
  "effective_date": "YYYY-MM-DD | null",   // regulatory/temporal facts
  "retrieval_date": "YYYY-MM-DD",
  "applicable_period": {"from": "…", "to": "… | open"},
  "quantitative": {                        // only for numeric evidence
    "metric": "…", "unit": "…", "value": "…",
    "methodology": "…", "revision_state": "final|provisional|revised"
  },
  "verification_state": "seeded|verified|locked",   // reuses source_registry vocabulary
  "confidence": "high|medium|low",
  "risk_class": "low|medium|high",
  "allowed_uses": ["terminology","comparison",…],
  "prohibited_uses": ["market_forecast","safety_prescription",…],
  "pages_using": ["route_id", …]           // back-reference for auditability
}
```

**Connection to current registries:** `source_id` is mandatory and must resolve to an existing `source_registry.json` entry (preserves "No source entry = no published claim"). `claim_id` resolves to `claims/*.json`. Quantitative and jurisdiction/temporal blocks are **optional by source class** (the prompt's "do not assume every field is needed"). Nothing here activates claims or changes source states — it is a new, initially-empty store.

---

## H. Geographic / domain model — first-class without Cartesian explosion

**Principle:** geography and domain become **attributes of evidence and (optionally) of a route**, gated by an eligibility rule — never free multipliers of the route grid.

- **Domain = existing `reference_layer`** (9 layers already defined). Promote it to a route field; no new taxonomy needed.
- **Geography = a new nullable enum**, distinct from `language`. Correct the `de = Germany` conflation: a German-language *terminology* page (`geography: null`, `domain: linguistic`) is a different object from a Germany-*jurisdiction* standards page (`language: de`, `geography: DE`, `domain: institutional`).
- **Eligibility rule (the anti-explosion guard):** a `(entity × domain × geography × language × audience)` intersection is **route-eligible only if ≥1 verified evidence record exists** for that intersection. No evidence → the intersection stays `EVIDENCE_COLLECTING`, produces **no page**. This turns geography/domain from page-multipliers into **evidence-gated positions**, satisfying the prompt's "combination is eligible only when a meaningful relationship exists and sufficient evidence supports it."

Result: geography/domain add *expressive precision* to the few evidence-backed routes, not 7× more permutations.

---

## I. Information Gain Gate — machine-testable + human-reviewable

Build on the existing `anti_duplication_rule`. A candidate route passes only if **both** stages pass:

**Machine stage (automatable, blocks CI):**
1. **Evidence-set delta:** the route's evidence-set (Section G) is not a subset of any sibling's evidence-set. *(Evidence overlap, per the prompt, matters more than prose.)*
2. **Dimension delta:** it differs from every sibling on ≥1 of {domain, geography, jurisdiction, temporal, source-set, page_type, comparison-pair}.
3. **Textual similarity ceiling:** body similarity to nearest sibling **< 0.60** (current thin siblings measure **0.84** — they would fail). Similarity is a *warning gate*, not the primary test.
4. **Minimum structured yield:** satisfies its reference layer's `minimum_quality_requirements` (already defined per layer).

**Human stage (review checklist, for `REFERENCE_INDEXABLE` promotion):** the 10 questions from the prompt (what question does it answer; what is lost if removed; what evidence; jurisdiction; period; uncertainty; sibling difference; ontology links; reference role; externally auditable provenance). Stored as a signed checklist on the route record.

**Rule:** stylistic rewrite ≠ information gain; different wording ≠ uniqueness. A route failing the machine stage never reaches human review.

---

## J. Pilot — a deliberately diverse set (evidence-availability-driven, not assumption-driven)

Per the prompt, the pilot must test the architecture across combinations, and selection must follow **evidence availability**. Given today's source registry (**15 sources: 7 dictionaries, 2 nomenclature standards, 3 gov scientific DBs, 1 industry, 2 academic-teaching; only 1 verified**), the honest split is:

**Tier 1 — evidence exists now (terminology/chemistry/linguistic domains):** buildable immediately.
| # | Entity | Domain | Language | Audience | Evidence basis today |
|---|---|---|---|---|---|
| 1 | Bisulfid ("missing-E") | linguistic | de | translator/researcher | dictionaries + nomenclature standards (present) |
| 2 | HS⁻ / hydrosulfide vs sulfide vs bisulfide | chemistry (disambiguation) | en | chemist | nomenclature + gov sci DB (present) |
| 3 | Sulfid vs Sulfide (DE/EN suffix) | linguistic | de↔en | terminology professional | dictionaries (present) |
| 4 | Pyrite (FeS₂) canonical | chemistry/materials | en | student | gov scientific DB (present) |
| 5 | AI-readable record for #2 | technical | en | ai_system | structured re-expression of #2 evidence |

**Tier 2 — strategically named in doctrine but NO verified evidence today → must remain `EVIDENCE_COLLECTING`, publish nothing yet:**
| Hypothesis (from doctrine) | Evidence needed | Status now |
|---|---|---|
| Morocco phosphate-linked sulfur demand | official customs/trade data (HS codes), OCP/institutional sources | **none in registry** → EVIDENCE_COLLECTING |
| Gulf sulfur supply/recovery | production/export statistics, refining sources | **none** → EVIDENCE_COLLECTING |
| China sulfur production/manufacturing | national statistical + standards sources | **none** → EVIDENCE_COLLECTING |
| Biology/medicine (disulfide bonds in proteins) | peer-reviewed literature + high claim restriction | **none verified** → EVIDENCE_COLLECTING |
| Economic/investment context | market reports w/ methodology (blocked without) | **none** → EVIDENCE_COLLECTING |

The pilot **proves the architecture end-to-end on Tier 1** (5 pages spanning linguistic/chemistry/materials/technical domains and translator/chemist/student/ai audiences) and **proves the discipline on Tier 2** (the geography/economic layers are wired but correctly produce zero pages until evidence arrives).

---

## K. Migration path — from dossier atlas to citation-grade infrastructure (no needless URL breakage)

1. **Freeze the fork (no content change):** add the ledger↔routes consistency validator (F1). Stop new ledger-authorized indexation.
2. **Classify, don't delete (F6 / Section L):** run a lifecycle-classification pass over the 14K, assigning each route a state. URLs stay live.
3. **De-index the thin surface *in place*:** the ~13,900 thin permutation routes move to `PUBLIC_NOINDEX` — HTML `robots: noindex, follow`, removed from sitemaps, **kept reachable** for humans/agents. No URL dies; only the indexation posture changes. (This is the previously-recommended SEO Phase 2, now framed as a lifecycle transition, not an SEO tactic.)
4. **Promote the evidence-backed pillars:** the ~52 Wave-1 + hub pages + Tier-1 pilot pass the Information Gain Gate → `REFERENCE_INDEXABLE`, and are the *only* URLs in the sitemap.
5. **Grow toward the 500-page governed floor** by consolidating permutation families into single richer knowledge objects (audience as *sections*, not URLs) and attaching real evidence records — each addition gated by Sections G–I.
6. **Consolidation, not retirement, first.** Retire a route only after its knowledge is absorbed elsewhere and it fails the Information Gain Gate with no evidence path. Redirects preserve any external links.

**URL safety:** steps 3–4 change *indexation posture and sitemap membership*, not paths. The breadcrumb-404 fix (PR #105) already holds (0 dead directory links in a 3,000-page sample, re-verified 2026-09-19), so the internal graph is safe to keep live while de-indexed.

---

## L. Indexation strategy — five buckets (classification only; do NOT execute)

Mapping the deployed 14K to states. Reuses existing vocabulary; proposes new states only where none exist, and maps (not renames) the prompt's lifecycle onto them.

| Bucket | Approx. count (from `14K_CORPUS_CLASSIFICATION` + deployed audit) | Proposed state | Action when approved |
|---|---|---|---|
| **Currently-safe indexable references** | ~52 Wave-1 + 12 hubs + Tier-1 pilot (~70) | `REFERENCE_INDEXABLE` (= formula `indexable_approved`) | keep `index,follow`; sole sitemap members |
| **Public-but-noindex support** | the ~10,908 terminology + 2,416 industrial permutations that are reachable/useful but thin | `PUBLIC_NOINDEX` (= formula `noindex_governance`) | `noindex,follow`; drop from sitemap; keep live |
| **Evidence-building routes** | geography/economic/regulatory positions named in doctrine (Morocco/Gulf/China/economic) | `EVIDENCE_COLLECTING` (maps to `routes.json status: planned` + `source_required_unresolved`) | **no page** until verified evidence exists |
| **Consolidation candidates** | audience/sub sibling families (~84% similar) | `CONSOLIDATION_CANDIDATE` (new sub-state of `PUBLIC_NOINDEX`) | merge into one richer knowledge object; redirect |
| **Blocked routes** | 18 high-risk + 2 acquisition/utility (`14K_CORPUS_CLASSIFICATION`) | keep `blocked_high_risk` / `blocked_acquisition` | remain blocked; specialist review only |

**Proposed lifecycle mapped to existing states (no casual renames):**
`PLANNED`→`routes.json status: planned` · `RELATIONSHIP_QUALIFIED`→new flag on route · `EVIDENCE_COLLECTING`→`source_required_unresolved` · `EVIDENCE_SUFFICIENT`→`source_verified` · `REFERENCE_DRAFT`→`status: draft` · `VALIDATED`→Quality Gate pass · `PUBLIC_NOINDEX`→`indexation_posture: noindex_governance` · `REFERENCE_INDEXABLE`→`indexation_posture: indexable_approved`.

**This section is a map, not an instruction to deploy.**

---

## Honesty statement (prompt §21)

- **The prompt's file list is accurate.** Every named constitutional file exists and was read.
- **The doctrine already says what the prompt asks for** (depth over volume, SEO subordinate, publication ≠ indexation, 500-page floor). This is reconciliation, not redirection.
- **Contradiction found and reported:** the deployed site contradicts `routes.json`, `sitemap_policy.json`, the route formula's `non_indexable` default, and Quality Gate 05 — via the Sprint 99 release ledger. Named, dated, evidenced above.
- **Geography claims lack evidence today.** Morocco, Gulf, China, biology/medicine, and economic/investment layers have **zero verified sources** in `source_registry.json` (only 1 of 15 sources is verified, none are trade/economic/regulatory). They are **strategically meaningful but must remain `EVIDENCE_COLLECTING`.** I did not fabricate rationale to preserve them.
- **Audience gap noted honestly:** the prompt's target audiences include *journalists, translators/terminology professionals, and regulatory/law-enforcement researchers*; the current `audience_layer_registry.json` does **not** model journalist, translator, or law-enforcement as first-class audiences (nearest: analyst, researcher, government). Adding them is a small registry extension, flagged for the implementation sprint.
- **No production data was modified** producing this report. CI (Corpus Governance L0/L1/L2) re-run 2026-09-19: PASS.

---

## Appendix — ground-truth evidence (measured 2026-09-19)

| Measurement | Value | Source |
|---|---|---|
| Deployed pages (deploy-gate metric) | 14,041 `index.html` | `find site/public …` |
| Deployed robots meta | 14,039 `index,follow`; 15 `noindex,nofollow`; 1 `noindex,follow` | grep over `site/public` |
| Sitemap URLs | 13,998 across 9 shards | `grep -c '<loc>' sitemap-*.xml` |
| `robots.txt` | `Allow: /` + sitemap.xml | `site/public/robots.txt` |
| `routes.json` | 14,000 routes; all `status:planned, indexable:false, in_sitemap:false, in_navigation:false` | field distribution scan |
| `routes.json` lost dims | geography/jurisdiction/domain/reference_layer/supply_chain/temporal/evidence/period = **0 / 3,000** | key-presence scan |
| `release_ledger.json` (Sprint 99, 2026-06-05) | total 14,000; **released 13,998; indexable true 13,998 / false 2**; `source_pack_id:null`; `claim_set_id:"cautious_framing"`; `validation_status:"pending"` | ledger scan |
| `14K_CORPUS_CLASSIFICATION` (Sprint 98) | **blocked_source_required 13,956**; eligible_atlas_hub_wave 26; blocked_high_risk 16; blocked_acquisition 2 | classification report |
| Source registry | 15 entries — 14 `seeded`, **1 `verified`**; 0 trade/economic/regulatory | `source_registry.json` |
| Claim library | `status: inactive` | `claims/claim_library.json` |
| Source packs | 8 packs, `architecture_active`; pages released with `source_pack_id:null` | `source_pack_registry.json` |
| Thin sample page | ~392 words, `index,follow` | `…/hydrosulfide/aud/res/res/` |
| Sibling similarity | **0.841** (`…/res/res/` vs `…/stu/edu/`) | difflib SequenceMatcher |
| Internal-link integrity | 0 dead directory links / 3,000-page sample (PR #105 fix holds) | breadcrumb scan |
| Corpus Governance CI | L0/L1/L2 all PASS | re-run 2026-09-19 |
| GSC (24/07/2026, from `SEO_INDEXATION_STRATEGY.md`) | 3 indexed; 3,369 discovered-not-indexed; 132 crawled-not-indexed | prior diagnosis |

---

*Read-only reconciliation. No routes, content, sources, claims, sitemaps, indexation flags, or the route formula were modified. Await explicit approval of the next implementation sprint before any change in Sections F–L is executed.*
