# BISULFID — Doctrine-to-Corpus Reconciliation

**Type:** Read-only analysis. No production data modified.
**Date:** 2026-09-19 · **First pass:** v1 · **Correction pass:** v2 (2026-09-19)
**Scope:** `sohadot/bisulfid` @ `main` (last production commit 2026-07-29, PR #105)
**Mandate:** Reconcile the deployed 14K public dossier surface with the original BISULFID doctrine. Prove exactly where conceptual richness was lost between doctrine and production. Propose the smallest set of amendments. Do **not** execute changes.

> **⚠ READ THIS FIRST — v2 correction pass supersedes parts of v1.**
> Sections A–L below are the **first-pass (v1)** analysis. A **[Correction Pass — Architectural and Evidentiary Reconciliation](#correction-pass--architectural-and-evidentiary-reconciliation)** at the end of this document corrects several v1 errors and is **authoritative where the two disagree.** Specific v1 statements that v2 corrects are tagged inline with **⚠v2 §N**. Do not act on a v1 statement that carries such a tag without reading the referenced Correction Pass item. No implementation sprint (including F1) is approved.

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
| **9 reference layers (presentation/evidence-standard roles — NOT subject domains ⚠v2 §1)** | codified | `reference_layer_registry.json`: academic, knowledge, research, educational, economic, institutional, technical, linguistic, logistical — each with own source/claim posture and `indexation_default: noindex_default` |
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
| **Geography / jurisdiction** | Germany, Morocco, Gulf, China all named in `ASSET_THESIS`, `MULTILINGUAL_POLICY`, README | **0 / 14,000** (full scan ⚠v2 §13) | **LOST / collapsed into `language`.** `de` is treated as Germany, `ar` as "Gulf+Morocco." The prompt's conceptual correction is correct and the repo proves it: geography is not a dimension. |
| **Subject domain (chemistry/physics/biology/economics/trade/regulation…) ⚠v2 §1** | *no true subject-domain registry exists*; nearest signals are per-term `chemical_field`/`industrial_signal`/`safety_context` in `ontology/sulfur_terms.json` (14 terms, free-text, chemistry-only) | **0 / 14,000** (full scan) | **MISSING as a governed concept.** *v1 wrongly treated `reference_layer` as "domain." It is not* (⚠v2 §1). Subject domain is registered only as free-text per-term chemistry tags, never as a governed enum or route field. |
| **Reference layer (presentation/evidence-standard role)** | 9 layers in `reference_layer_registry.json` | **0 / 14,000** (`reference_layer` is not a route field) | **REGISTERED BUT NOT WIRED.** Exists as a standalone registry, absent from route identity and route records; the route_key formula omits it too. |
| **Supply-chain role** | Gulf supply / Morocco phosphate demand (`MULTILINGUAL_POLICY`); `REF_LOGISTICAL` layer | **0 / 14,000** (full scan) | **LOST.** Only survives as prose in doctrine. |
| **Temporal validity** | implied by "market reports with date," regulatory currency | **0 / 14,000** (full scan; no `valid_from`/`valid_to`/`period`) | **ABSENT ENTIRELY.** No page can express "as of year X" or "effective date." |
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
Deployed `site/public`: **14,039 of 14,041 distinct deploy pages are `index, follow`** (2 `noindex`; 0 missing/conflicting robots meta — ⚠v2 §7), `robots.txt: Allow: /`, **9 sitemaps = 13,998 URLs**. Google Search Console (24/07/2026): **3 pages indexed**; ~3,369 "Discovered – currently not indexed" + 132 "Crawled – currently not indexed". **⚠v2 §6:** those GSC statuses are *consistent with* the repository's independently measured thin/near-duplicate problem (sibling similarity ~0.84, `source_pack_id: null`), but they are **not, by themselves, a formal Google doorway-content verdict or penalty.** The site's **own Sprint 98 classification** had already flagged **13,956 routes as `blocked_source_required`** and only **26 as eligible** — one day before Sprint 99 released 13,998 of them anyway. The contradiction is internal and dated.

**Net:** doctrine intact → registry intact → **ledger + generators + deploy diverged**. The fix targets E1–E4, not the doctrine or `routes.json`.

---

## F. Proposed minimal architecture amendments (extension, not rewrite)

Ordered smallest-first. None deletes routes or content.

1. **⚠v2 §2 — CORRECTED. Do *not* pre-decide that `routes.json` becomes "the single publication authority."** That is itself a governance change (Sprint 99 deliberately named the *release ledger* the public-route source of truth), not a neutral repair. v2 replaces this with: **reconcile the four distinct states — governance registry / release-authorization ledger / deployed state / sitemap-indexation state — and choose among 2–3 authority contracts** (see [Correction Pass §2](#2-publication-authority-not-yet-decided--three-contracts)). Any consistency validator ships **audit/report-only first**, never as a CI hard-fail against a historically authorized mismatch.
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

- **⚠v2 §1 — CORRECTED. `subject_domain` ≠ `reference_layer`.** *v1 wrongly proposed reusing `reference_layer` as "domain."* `reference_layer` is a presentation/evidence-standard role (academic/technical/economic…); `subject_domain` is the field of knowledge (chemistry, physics, materials, biology, medicine, agriculture, environment, mining, industry, energy, economics, trade, logistics, regulation, safety, linguistics, …). They are orthogonal — the same chemistry fact can appear in an academic *or* a technical reference layer. See [Correction Pass §1](#1-subject_domain-vs-reference_layer-vs-audience-vs-page_type-vs-geography-vs-jurisdiction) for whether a new `subject_domain_registry` is warranted (provisional answer: **yes**, seeded from the ontology's existing `chemical_field`/`industrial_signal`/`safety_context` and grown from evidence — **not invented as a fixed taxonomy now**).
- **Geography = a new nullable enum**, distinct from `language`, expressing **entity ↔ geography ↔ relationship ↔ evidence** (importer/producer/exporter/regulatory-jurisdiction/… — relationship types *discovered and governed, not assumed*; ⚠v2 §10). Correct the `de = Germany` conflation: a German-language *terminology* page (`geography: null`) differs from a Germany-*jurisdiction* standards page (`language: de`, `geography: DE`, `jurisdiction: …`). A country never earns a page for existing; a country×domain becomes a knowledge object only when evidence proves a meaningful relationship.
- **Eligibility rule (the anti-explosion guard):** a `(entity × domain × geography × language × audience)` intersection is **route-eligible only if ≥1 verified evidence record exists** for that intersection. No evidence → the intersection stays `EVIDENCE_COLLECTING`, produces **no page**. This turns geography/domain from page-multipliers into **evidence-gated positions**, satisfying the prompt's "combination is eligible only when a meaningful relationship exists and sufficient evidence supports it."

Result: geography/domain add *expressive precision* to the few evidence-backed routes, not 7× more permutations.

---

## I. Information Gain Gate — machine-testable + human-reviewable

Build on the existing `anti_duplication_rule`. A candidate route passes only if **both** stages pass:

**Machine stage (automatable, blocks CI):**
1. **Evidence-set delta:** the route's evidence-set (Section G) is not a subset of any sibling's evidence-set. *(Evidence overlap, per the prompt, matters more than prose.)*
2. **Dimension delta:** it differs from every sibling on ≥1 of {domain, geography, jurisdiction, temporal, source-set, page_type, comparison-pair}.
3. **Textual similarity as a diagnostic signal only ⚠v2 §4** — *v1 hard-coded a `< 0.60` ceiling; that number was uncalibrated and is withdrawn.* Similarity is one input among many, never a standalone blocking threshold, and never a target to optimize toward. Any numeric threshold is ratified only after the calibration procedure in [Correction Pass §4](#4-information-gain-gate-multi-signal-no-uncalibrated-threshold) (labelled pairs across true-duplicate / near-duplicate / valid-sibling / valid-localization / valid-domain-reference). Reference datum: current thin siblings measure **0.841**.
4. **Minimum structured yield:** satisfies its reference layer's `minimum_quality_requirements` (already defined per layer).

**Human stage (review checklist, for `REFERENCE_INDEXABLE` promotion):** the 10 questions from the prompt (what question does it answer; what is lost if removed; what evidence; jurisdiction; period; uncertainty; sibling difference; ontology links; reference role; externally auditable provenance). Stored as a signed checklist on the route record.

**Rule:** stylistic rewrite ≠ information gain; different wording ≠ uniqueness. A route failing the machine stage never reaches human review.

---

## J. Pilot — a deliberately diverse set (evidence-availability-driven, not assumption-driven)

Per the prompt, the pilot must test the architecture across combinations, and selection must follow **evidence availability**. Given today's source registry (**15 sources: 7 dictionaries, 2 nomenclature standards, 3 gov scientific DBs, 1 industry, 2 academic-teaching; only 1 verified**), the honest split is:

**⚠v2 §3 — this v1 table is CORRECTED. "Present" ≠ "verified" ≠ "locked" ≠ "claim-approved." Under actual governance almost none of these are buildable today.** See the [corrected eligibility matrix in the Correction Pass (§3)](#3-pilot-re-audited-against-actual-verification-eligibility). Summary of the correction: 14 of 15 sources are `seeded`; the 1 `verified` source is `source_lock_status: candidate` and narrowly scoped to German MoS₂; only 1 claim is `approved` (`CLM-TERM-MOS2-DE-001`) and it sits in an **inactive** registry. The honest count of routes that current governance permits to publish today is effectively **zero**; the single nearest-ready object is German MoS₂ terminology, still blocked on source-lock + claim-registry activation.

*v1 table (retained for the audit trail; each row's "present" basis is corrected in §3):*
| # | Entity | Domain | Language | Audience | v1 claimed basis | v2 verdict |
|---|---|---|---|---|---|---|
| 1 | Bisulfid ("missing-E") | linguistic | de | translator/researcher | dictionaries + nomenclature | **not eligible** — MW/Duden/IUPAC all `seeded`, lock=candidate |
| 2 | HS⁻ / hydrosulfide vs sulfide vs bisulfide | chemistry (disambiguation) | en | chemist | nomenclature + gov sci DB | **not eligible** — IUPAC/PubChem `seeded`, no approved claim |
| 3 | Sulfid vs Sulfide (DE/EN suffix) | linguistic | de↔en | terminology professional | dictionaries | **not eligible** — Duden `seeded` |
| 4 | Pyrite (FeS₂) canonical | chemistry/materials | en | student | gov scientific DB | **not eligible** — no pyrite source in registry at all |
| 5 | AI-readable record for #2 | technical | en | ai_system | derivative of #2 | **not eligible** — inherits #2 |

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

1. **Freeze the fork (no content change):** decide the authority contract first (⚠v2 §2), then add the ledger↔routes consistency validator **in audit/report-only mode** (not a CI hard-fail). Stop new ledger-authorized indexation.
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
| **Indexability-review candidates ⚠v2 §5** *(renamed from v1 "currently-safe indexable references" — historical publication status grants nothing; each must pass the citation-grade audit in §5 before any `index,follow`)* | ~52 Wave-1 + 12 hubs (**unaudited**; Tier-1 pilot removed — not evidence-eligible, ⚠v2 §3) | `INDEXABILITY_REVIEW_CANDIDATE` → only then `REFERENCE_INDEXABLE` | **audit first**; none indexed until it passes |
| **Public-but-noindex support** | the ~10,908 terminology + 2,416 industrial permutations, reachable but thin (⚠v2 §12: *not necessarily permanent* — some become modules, consolidations, redirects, or retirements) | `PUBLIC_NOINDEX` (= formula `noindex_governance`) | `noindex,follow`; drop from sitemap; keep live pending disposition |
| **Evidence-building routes** | geography/economic/regulatory positions named in doctrine (Morocco/Gulf/China/economic) — **hypotheses, not pages** | `EVIDENCE_COLLECTING` (maps to `routes.json status: planned` + `source_required_unresolved`) | **no page** until verified evidence qualifies the relationship |
| **Consolidation candidates** | audience/sub sibling families (~84% similar) | `CONSOLIDATION_CANDIDATE` (new sub-state of `PUBLIC_NOINDEX`) | merge into one richer knowledge object; redirect |
| **Blocked routes** | release-eligibility axis: **16 `blocked_high_risk_or_source_review` + 2 `blocked_acquisition_or_utility`** (⚠v2 §8; the "18" in v1 was the *production-lane M* count, a different axis) | keep blocked | remain blocked; specialist review only |

**Proposed lifecycle mapped to existing states (no casual renames):**
`PLANNED`→`routes.json status: planned` · `RELATIONSHIP_QUALIFIED`→new flag on route · `EVIDENCE_COLLECTING`→`source_required_unresolved` · `EVIDENCE_SUFFICIENT`→`source_verified` · `REFERENCE_DRAFT`→`status: draft` · `VALIDATED`→Quality Gate pass · `PUBLIC_NOINDEX`→`indexation_posture: noindex_governance` · `REFERENCE_INDEXABLE`→`indexation_posture: indexable_approved`.

**This section is a map, not an instruction to deploy.**

---

## Honesty statement (prompt §21)

- **The prompt's file list is accurate.** Every named constitutional file exists and was read.
- **The doctrine already says what the prompt asks for** (depth over volume, SEO subordinate, publication ≠ indexation, 500-page floor). This is reconciliation, not redirection.
- **Contradiction found and reported:** the deployed site contradicts `routes.json`, `sitemap_policy.json`, the route formula's `non_indexable` default, and Quality Gate 05 — via the Sprint 99 release ledger. Named, dated, evidenced above.
- **Geography claims lack evidence today.** Morocco, Gulf, China, biology/medicine, and economic/investment layers have **zero verified sources** in `source_registry.json` (only 1 of 15 sources is verified, none are trade/economic/regulatory). They are **strategically meaningful but must remain `EVIDENCE_COLLECTING`.** I did not fabricate rationale to preserve them.
- **Audience gap — CORRECTED ⚠v2 §9.** *v1 wrongly implied journalist/translator/law-enforcement should simply be "added" as route audiences.* v2 position: a broad *target-user universe* is not a mandate for more route dimensions — that is how the permutation problem started. Distinguish **user type** vs **information task** vs **reference layer** vs **independent knowledge surface**: a journalist typically uses the research/analyst layer; a regulatory/law-enforcement researcher the institutional/legal layer; a translator the linguistic layer. Create a *new first-class audience only if it changes evidence requirements, knowledge structure, claim boundary, or user task* enough to justify independent treatment. See [Correction Pass §9](#9-audiences--personas-are-not-automatically-dimensions).
- **No production data was modified** producing this report. CI (Corpus Governance L0/L1/L2) re-run 2026-09-19: PASS.

---

## Appendix — ground-truth evidence (measured 2026-09-19)

| Measurement | Value | Source |
|---|---|---|
| Deployed pages (deploy-gate metric) | 14,041 distinct `index.html` (excl. samples) | `find site/public …` |
| Deployed robots meta — **distinct pages, corrected ⚠v2 §7** | **Deploy population (14,041):** 14,039 `index,follow`; 2 `noindex` (1 `noindex,follow` + 1 `noindex,nofollow`); 0 missing; 0 conflicting/duplicate. **Full population (14,055 incl. 14 sample pages):** 14,039 index; 16 noindex; 0 missing; 0 conflicting. *(v1 mixed populations and summed meta occurrences.)* | per-file scan |
| Sitemap URLs | 13,998 across 9 shards | `grep -c '<loc>' sitemap-*.xml` |
| `robots.txt` | `Allow: /` + sitemap.xml | `site/public/robots.txt` |
| `routes.json` | 14,000 routes; all `status:planned, indexable:false, in_sitemap:false, in_navigation:false` | field distribution scan |
| `routes.json` lost dims | geography/jurisdiction/subject_domain/reference_layer/supply_chain/temporal/evidence/audience/source_posture/claim_posture/indexation_posture/internal_link_role = **0 / 14,000** (full scan ⚠v2 §13) | key-presence scan |
| `release_ledger.json` (Sprint 99, 2026-06-05) | total 14,000; **released 13,998; indexable true 13,998 / false 2**; `source_pack_id:null`; `claim_set_id:"cautious_framing"`; `validation_status:"pending"` | ledger scan |
| `14K_CORPUS_CLASSIFICATION` (Sprint 98) — **release_eligibility axis** (sums to 14,000) | eligible_atlas_hub_wave **26**; blocked_source_required **13,956**; blocked_high_risk_or_source_review **16**; blocked_acquisition_or_utility **2** | `release_eligibility_distribution` |
| `14K_CORPUS_CLASSIFICATION` — **production-lane axis** (separate ⚠v2 §8) | Lane M (blocked/high-risk requiring review) = **18**; Lane A terminology = 10,908; Lane F industrial = 2,416; HUB = 159; … | `lane_distribution` |
| Source registry | 15 entries — **14 `seeded` + 1 `verified`; ALL 15 `source_lock_status: candidate` (0 locked)**; 0 trade/economic/regulatory | `source_registry.json` |
| Verified source scope | `SRC-SPEKTRUM-MOS2-DE` — German Spektrum lexicon MoS₂; `do_not_use_for` includes "claim approval by itself", "route publication by itself", "EN-only authority" | `source_registry.json` |
| Claims | all claim registries `inactive`; exactly **1 `approved` claim** `CLM-TERM-MOS2-DE-001` (in the inactive `terminology_claims.json`) | `claims/*.json` |
| Registered route languages | **EN 13,730 + DE 270 only** (0 AR/ZH/JA/FR/ES routes despite AR = market-chain priority) | `routes.json` language scan |
| Claim library | `status: inactive` | `claims/claim_library.json` |
| Source packs | 8 packs, `architecture_active`; pages released with `source_pack_id:null` | `source_pack_registry.json` |
| Thin sample page | ~392 words, `index,follow` | `…/hydrosulfide/aud/res/res/` |
| Sibling similarity | **0.841** (`…/res/res/` vs `…/stu/edu/`) | difflib SequenceMatcher |
| Internal-link integrity | 0 dead directory links / 3,000-page sample (PR #105 fix holds) | breadcrumb scan |
| Corpus Governance CI | L0/L1/L2 all PASS | re-run 2026-09-19 |
| GSC (24/07/2026, from `SEO_INDEXATION_STRATEGY.md`) | 3 indexed; 3,369 discovered-not-indexed; 132 crawled-not-indexed | prior diagnosis |

---

*Read-only reconciliation. No routes, content, sources, claims, sitemaps, indexation flags, or the route formula were modified. Await explicit approval of the next implementation sprint before any change in Sections F–L is executed.*

---
---

# Correction Pass — Architectural and Evidentiary Reconciliation

**v2 · 2026-09-19 · READ-ONLY.** No production data, routes, release ledger, source states, claims, sitemap, HTML, robots, generators, or CI behavior were modified. This pass is **authoritative** wherever it disagrees with v1 (Sections A–L). It responds point-by-point to the correction mandate.

## 1. `subject_domain` vs `reference_layer` vs `audience` vs `page_type` vs `geography` vs `jurisdiction`

**v1 error:** equated "domain" with `reference_layer`. Corrected.

These are six orthogonal concepts. Evidence from the registries:

| Concept | What it answers | Where it lives today | Governed? |
|---|---|---|---|
| **subject_domain** | *What field of knowledge is this?* (chemistry, physics, materials, biology, medicine, agriculture, environment, mining, industry, energy, economics, trade, logistics, regulation, safety, linguistics…) | **Nowhere as a governed concept.** Only per-term free-text `chemical_field` / `industrial_signal` / `safety_context` in `ontology/sulfur_terms.json` (14 terms, chemistry-centric) | **No** |
| **reference_layer** | *To what evidentiary/presentation standard is it written?* (academic, knowledge, research, educational, economic, institutional, technical, linguistic, logistical) | `reference_layer_registry.json` (9, each with source/claim posture, `noindex_default`) | Yes (registry), not wired to routes |
| **audience** | *Who is the reader, and what claims are allowed for them?* (chemist, researcher, analyst, government, investor, company, student, ai_system, child_edu) | `audience_layer_registry.json` (9) | Yes (registry), not a route field |
| **page_type** | *What is the structural form?* (canonical term, comparison, glossary, AI-readable, hub, …) | `page_type_registry.json` (19) | Yes; reflected coarsely as `layer` on routes |
| **geography** | *Which place/region does the relationship involve?* | **Nowhere** (0/14,000) | **No** |
| **jurisdiction** | *Which legal authority/instrument governs?* | **Nowhere** (0/14,000) | **No** |

**Overlap vs difference:** `reference_layer` and `audience` correlate (a researcher tends toward the research layer) but are not identical — one audience can be served across layers, and one layer serves several audiences. `subject_domain` is independent of all of them: a single chemistry fact can appear in an academic *or* technical *or* educational layer, for a chemist *or* a student. Conflating domain with layer (v1) would re-flatten the model exactly as production already did.

**Do we need a new `subject_domain_registry`?** **Provisionally yes, but not invented now.** Recommended discipline:
1. Do **not** author a final taxonomy up front (that risks a fresh flattening).
2. **Seed** `subject_domain` candidates from evidence actually present — starting from the ontology's `chemical_field`/`industrial_signal`/`safety_context` (today: chemistry, nomenclature, inorganic chemistry, industrial-signal, safety-context).
3. **Grow** the enum only as verified evidence introduces a genuinely new domain (physics, materials, trade, regulation…). A domain exists in the registry only once ≥1 verified evidence record uses it.
4. Extending the ontology's per-entity domain tag into a small governed enum is preferable to a brand-new sprawling registry — least semantic distortion, reuses an existing field.

## 2. Publication authority — not yet decided; three contracts

**v1 error:** proposed "re-assert `routes.json` as the sole publication authority." That is a **governance decision**, not a technical repair — Sprint 99 deliberately declared the **release ledger** the public-route source of truth (`DECISION_LOG.md` ~L4416/4551). Reversing it silently would itself repeat the "one file quietly overrides another" failure.

**First, separate the four states that v1 blurred:**
| State | File(s) | Current value |
|---|---|---|
| **Governance/route registry** | `routes.json` | 14,000 × `planned / indexable:false / in_sitemap:false` |
| **Release-authorization ledger** | `release_ledger.json` | 13,998 `released` + `indexable:true`, `source_pack_id:null`, `validation_status:pending` |
| **Deployed state** | `site/public/**/index.html` | 14,039/14,041 `index,follow` |
| **Sitemap/indexation state** | `sitemap*.xml`, `robots.txt` | 13,998 URLs in 9 shards; `Allow: /` |

**Three candidate authority contracts (trade-offs; decision deferred to governance):**

- **Contract A — Registry-canonical.** `routes.json` is truth; the ledger records *decisions* and must reconcile to it; deploy derives from routes.json. *Pro:* matches the route formula's own indexation rules and the doctrine. *Con:* reverses an explicit Sprint 99 decision; needs a DECISION_LOG supersession entry.
- **Contract B — Ledger-canonical (status quo formalized).** The ledger stays the publication authority; `routes.json` is demoted to a *planning* registry and its `indexable:false` flags are re-interpreted as "planning defaults, not live truth." *Pro:* honors Sprint 99; least churn. *Con:* leaves the doctrine/formula indexation rules unenforced; keeps two schemas.
- **Contract C — Derived canonical state (preferred long-term).** Neither file is "the boss." A single **derived publication state** is computed from an explicit precedence function over {registry posture, ledger authorization, validation status, gate result}. `routes.json` and the ledger each own the fields they are authoritative for (registry owns governance posture; ledger owns release authorization + validation), and the derived state is what deploy/sitemap read. *Pro:* removes the fork by construction; auditable. *Con:* requires design + a DECISION_LOG entry; most upfront work.

**Do not build a CI hard-fail now.** Any `validate_ledger_route_consistency` must ship **audit/report-only** until the state migration completes; failing CI today would red-line the repo over a *historically authorized* mismatch. The choice among A/B/C is a **governance decision**, not something to auto-select.

## 3. Pilot re-audited against actual verification eligibility

**v1 error:** called five pilot pages "buildable immediately" because sources were *present*. `present`/`seeded`/`candidate` ≠ `verified` ≠ `source-locked` ≠ `claim-approved`. Corrected with the required matrix (measured 2026-09-19):

| Route concept | Claim(s) required | source_id(s) | source status | source_lock | claim status | allowed use | Publication eligibility **today** |
|---|---|---|---|---|---|---|---|
| Bisulfid "missing-E" (DE/EN suffix) | suffix/orthography claim | SRC-MW-*, SRC-DUDEN-*, SRC-IUPAC-* | **seeded** (14/15) | **candidate** | none approved | — | **NOT eligible** |
| hydrosulfide/sulfide/bisulfide disambiguation | terminology + identity | SRC-IUPAC-HYDROSULFIDES, SRC-PUBCHEM-HYDROSULFIDE, SRC-NIST-* | **seeded** | **candidate** | none approved | — | **NOT eligible** |
| Sulfid vs Sulfide | comparative orthography | SRC-DUDEN-SULFID | **seeded** | **candidate** | none approved | — | **NOT eligible** |
| Pyrite (FeS₂) | compound identity | *(none in registry)* | — | — | none | — | **NOT eligible** (no source at all) |
| AI-readable derivative of #2 | structured terminology | inherits #2 | seeded | candidate | none | — | **NOT eligible** |
| **German MoS₂ terminology** (`de_core_mos2`) | German lexical terminology, narrow | **SRC-SPEKTRUM-MOS2-DE** | **verified** | **candidate** (not locked) | **CLM-TERM-MOS2-DE-001 = approved** *(but in an inactive registry)* | German lexicon terminology, cautious lexical support only | **NEAREST-READY, still blocked** on: source-lock + claim-registry activation |

**Honest conclusion:** under current governance the number of routes that may publish today is **effectively zero**. Exactly **one** end-to-end evidence→claim chain exists (Spektrum → MoS₂), and even it is `source_lock: candidate`, its source's `do_not_use_for` forbids "route publication by itself," and its approved claim lives in an **inactive** registry. A genuine pilot is therefore **one narrow object (German MoS₂)**, and only after source-lock + claim activation — not five. The broader multi-domain/multi-geography pilot the prompt envisions is an **evidence-acquisition target**, not a build target.

## 4. Information Gain Gate — multi-signal, no uncalibrated threshold

**v1 error:** hard-coded a `< 0.60` textual-similarity blocking threshold. Withdrawn — it was uncalibrated, and optimizing prose to beat a number is exactly the wrong incentive.

**Corrected gate — nine signals, similarity is only one and only diagnostic:**
1. evidence-set overlap (primary), 2. claim-set overlap, 3. module/section overlap, 4. entity-relationship difference, 5. geography/jurisdiction difference, 6. temporal difference, 7. source-set difference, 8. user-task difference, 9. textual similarity (diagnostic warning only).

**Calibration procedure before any numeric threshold is ratified:**
1. Hand-label a corpus of route pairs into five classes: **true duplicate / near-duplicate / valid sibling / valid localization / valid domain-specific reference.**
2. Measure each of the nine signals across the labelled set.
3. Choose thresholds/weights that separate "true/near duplicate" from the three valid classes with agreed precision/recall — **localization and domain-specific references must not be flagged as duplicates.**
4. Ratify thresholds via DECISION_LOG; re-calibrate when the corpus composition changes. Similarity thresholds are never a content-optimization target.

## 5. The 52 Wave-1 pages / 12 hubs are NOT assumed citation-grade

**v1 error:** placed "~52 Wave-1 + 12 hubs + Tier-1 pilot" into "currently-safe indexable references." Corrected: the category is renamed **`INDEXABILITY_REVIEW_CANDIDATE`** and nothing is indexable until it passes an audit. Historical publication status confers nothing.

**Per-candidate audit checklist (before any `REFERENCE_INDEXABLE` promotion):** information gain (§4 gate) · evidence provenance (real `source_id`, not `null`) · source eligibility (verified + locked) · claim eligibility (approved, active registry) · factual depth · sibling duplication · freshness/update state where relevant · reference role · citation quality. The Tier-1 pilot pages are removed from this bucket (they are not evidence-eligible, §3). Even the Wave-1 pages must be re-checked against `source_pack_id`/claim backing before indexation — many Wave-1 pages were authored as "cautious framing" without per-page evidence records.

## 6. GSC wording corrected

The GSC "Discovered – currently not indexed" and "Crawled – currently not indexed" statuses are **not, by themselves, an official Google doorway-content verdict or penalty.** Correct framing (now used in §E4): *the GSC pattern is consistent with the repository's independently measured thin/near-duplicate content problem (sibling similarity ~0.841; `source_pack_id: null`; single "cautious_framing" claim set), but does not itself constitute a formal Google doorway classification.* The quality/duplication diagnosis rests on the repository's own measurements, not on inferring intent from Google's status labels.

## 7. Page-count measurements reconciled (distinct pages)

**v1 error:** summed raw robots-meta occurrences across mixed populations (14,039 + 15 + 1 exceeded 14,041). Re-measured per **distinct HTML file**:

| Population | Distinct pages | index,follow | any noindex | missing robots | conflicting/duplicate |
|---|---|---|---|---|---|
| **Deploy** (excludes `_integration_sample`,`_visual_proof_sample`) | **14,041** | 14,039 | 2 (1 `noindex,follow` + 1 `noindex,nofollow`) | 0 | 0 |
| **Full** (incl. 14 sample pages) | **14,055** | 14,039 | 16 | 0 | 0 |

The v1 "15 noindex,nofollow + 1 noindex,follow" conflated the 14 sample pages (all noindex) with the 2 deploy-population noindex pages. Corrected figures now used in §E4 and the appendix.

## 8. Blocked-route count reconciled (two different axes)

The "18" and "16" were **different measurement axes** in `14K_CORPUS_CLASSIFICATION.json`, not a contradiction:
- **`release_eligibility_distribution`** (sums to 14,000): eligible_atlas_hub_wave **26** · blocked_source_required **13,956** · blocked_high_risk_or_source_review **16** · blocked_acquisition_or_utility **2**.
- **`lane_distribution`** (production lanes): Lane M "blocked/high-risk requiring review" = **18** (a lane label, not the eligibility bucket).

**Canonical for eligibility:** use the release-eligibility axis (**16** + **2** blocked). Report lane M (**18**) only as a production-lane figure. Both v1 locations are corrected accordingly.

## 9. Audiences / personas are not automatically dimensions

**v1 error:** implied journalist/translator/law-enforcement should be "added" as route audiences. Corrected. Distinguish four things before creating any dimension:
- **user type** (journalist, translator, regulator) — who they are;
- **information task** (verify a source, translate a term, find the governing instrument) — what they need to do;
- **reference layer** (research, linguistic, institutional) — the standard the content is written to;
- **independent knowledge surface** — whether it deserves its own URL.

A persona earns a **first-class audience** only if it changes **evidence requirements, knowledge structure, claim boundary, or user task** enough to warrant independent treatment. Otherwise it is served by an existing layer (journalist → research/analyst; law-enforcement/regulatory researcher → institutional/legal; translator → linguistic). Adding personas as dimensions "because they are target users" is a direct cause of the original permutation explosion and is rejected.

## 10. Geography = governed relationships, not country permutations

Geography is modelled as **entity ↔ geography ↔ relationship ↔ evidence**, where relationship types (importer, producer, exporter, industrial user, regulatory jurisdiction, research center, terminology origin, supply-chain node, transformation/manufacturing center) are **discovered from evidence and governed**, not assumed. A country never receives a page for existing; a country×domain intersection becomes a knowledge object only when verified evidence proves a meaningful relationship. **Morocco, Gulf states, China, Germany and all other geographies remain hypotheses / `EVIDENCE_COLLECTING` positions** until evidence qualifies the relationship. (Today: zero trade/economic/regulatory sources exist — so all of these remain unqualified.)

## 11. Knowledge objects are separate from URLs

A governed knowledge position does **not** automatically require a public page. The model must support evidence-backed objects that live as: modules inside a larger reference page, data records, machine-readable relationships, tables, timeline entries, jurisdiction records, or source/evidence objects. An object is promoted to an **independent URL only when the Information Gain Gate (§4) demonstrates independent reference value.** This is the primary guard preventing the richer evidence/geography/domain model from producing a *larger* Cartesian explosion than the one it replaces.

## 12. The 14K is preserved for analysis/migration — not frozen as permanent public-noindex

The 14K inventory is retained as a governed **map of potential knowledge positions**, not assumed to remain permanently public-but-noindex. Per-route disposition (after audit) may be: deep reference, module, consolidated page, redirect, machine-readable object, or **retired route**. Knowledge is preserved where valuable; **the URL count is not sacred.** v1 Section L is corrected to mark `PUBLIC_NOINDEX` as a *holding* state pending disposition, not an endpoint.

## 13. Full 14,000-record field scan (replaces the 3,000 sample)

Full scan of all 14,000 `routes.json` records (not extrapolated):

| Dimension | Present in routes.json |
|---|---|
| geography | **0 / 14,000** |
| jurisdiction | **0 / 14,000** |
| subject_domain (and `domain`) | **0 / 14,000** |
| reference_layer | **0 / 14,000** |
| supply_chain / supply_chain_role | **0 / 14,000** |
| temporal / valid_from / valid_to | **0 / 14,000** |
| evidence / evidence_ids | **0 / 14,000** |
| audience / audience_layer | **0 / 14,000** |
| source_posture | **0 / 14,000** (only coarse `source_required` bool: True 13,971 / False 29) |
| claim_posture | **0 / 14,000** (only `required_claim_groups`) |
| indexation_posture | **0 / 14,000** (only boolean `indexable`: False 14,000) |
| internal_link_role | **0 / 14,000** (only `required_internal_links`) |
| `status` | 14,000 (all `planned`) · `in_sitemap` 14,000 (all false) · `in_navigation` 14,000 (all false) |
| `layer` | 14,000 (terminology_system 13,810; methodology_reference 62; gateway 52; foundation_reference 44; industrial_intelligence 7; public_gateway 7; utility 11; future_materials 3; safety_governance 3; acquisition 1) |
| `language` | EN 13,730 · DE 270 · **(AR/ZH/JA/FR/ES = 0)** |
| `risk_level` | low 111 · medium 13,885 · high 4 |

**Confirmed:** even five of the eight route-formula dimensions (`audience_layer`, `source_posture`, `claim_posture`, `indexation_posture`, `internal_link_role`) are absent as explicit route fields — `routes.json` implements only a coarse subset. Geography, jurisdiction, subject_domain, temporal, and evidence are absent entirely. The full scan corroborates the v1 sample.

## 14. Revised migration ordering (still requires approval)

**v1 error:** implied the next step is automatically "F1." Corrected. The smallest safe *conceptual* order, verified against the repository, is:

1. **Reconcile the constitutional authority model** (choose Contract A/B/C, §2) + DECISION_LOG entry. *No code.*
2. **Define the missing semantic dimensions** (subject_domain seeded from ontology; geography/jurisdiction/temporal as nullable) — schema design only, no backfill.
3. **Define evidence eligibility** (atomic evidence schema, §G) + the source-lock/claim-activation path (the MoS₂ chain is the first test case).
4. **Calibrate the Information Gain Gate** (§4) on labelled pairs.
5. **Audit the `INDEXABILITY_REVIEW_CANDIDATE` set** (Wave-1 + hubs, §5) against evidence + gate.
6. **Only then** add the ledger↔routes consistency check in **audit/report-only** mode.
7. **Only then** change any live indexation or sitemap posture.

This order is repository-verified: steps 1–5 are prerequisites that touch no live indexation; the consistency check (6) is meaningful only after the authority contract exists; live posture (7) is last. **None of this is approved to execute.**

---

# Final Summary

**1. What v1 findings remain valid?**
- The central finding: doctrine and `routes.json` are coherent and already forbid thin volume; the failure is a **fork between two publication authorities** (`routes.json` planned/non-indexable vs `release_ledger.json` released/indexable), with the deployed site obeying the ledger. Dated and evidence-backed.
- The Sprint 98→99 contradiction (13,956 `blocked_source_required` classified one day before 13,998 were released).
- **Lost/absent dimensions** — geography, jurisdiction, subject_domain, temporal validity, atomic evidence provenance are not first-class (now confirmed by a **full 14,000-record scan**, not a sample).
- Existing safeguards (anti-thin, anti-duplication, anti-free-form-LLM, source/claim discipline, publication≠indexation, 500-page floor) already exist and should be reused.
- The internal link graph is intact (breadcrumb-404 fix holds).

**2. What was corrected?**
- **§1** `subject_domain` ≠ `reference_layer` (the most important fix); domain is essentially ungoverned today.
- **§2** "Re-assert routes.json" withdrawn — publication authority is an undecided governance choice (three contracts offered); any consistency validator is audit-only first.
- **§3** Pilot re-audited: "present" ≠ eligible; realistically **zero** publishable routes today, one nearest-ready object (German MoS₂), still blocked.
- **§4** The `0.60` similarity threshold withdrawn → multi-signal gate + calibration.
- **§5** Wave-1/hubs reclassified `INDEXABILITY_REVIEW_CANDIDATE`; not assumed citation-grade.
- **§6** GSC wording corrected (no formal doorway "verdict").
- **§7** Page counts re-measured per distinct file (deploy 14,041 = 14,039 index + 2 noindex; full 14,055).
- **§8** Blocked count reconciled (release-eligibility 16+2 vs production-lane M 18 — different axes).
- **§9** Personas are not automatically route dimensions.
- **§10–12** Geography = governed relationships; knowledge objects ≠ URLs; the 14K is not frozen as permanent noindex.
- **§13** 3,000 sample replaced with a full 14,000 scan.
- **§14** "next step = F1" withdrawn → a 7-step order, authority reconciliation first.

**3. What remains unresolved and requires a governance decision?**
- **Which publication-authority contract (A/B/C)** governs — reversing or formalizing the Sprint 99 ledger decision is the owner's call, with a DECISION_LOG supersession entry.
- **Whether to create a `subject_domain_registry`** and its seeding/growth rule.
- **Source-lock + claim-registry activation** policy (nothing publishes until this is decided; currently all sources are `candidate`, all claim registries `inactive`).
- **Disposition policy for the 14K** (module / consolidate / redirect / retire) and whether URL retirement is permitted.
- **Information Gain thresholds** — cannot be ratified until calibration on labelled pairs.
- **Which new audiences (if any)** clear the "changes evidence/structure/claim/task" bar.

**4. Smallest safe implementation sprint after — and only after — this corrected report is reviewed (NOT started):**
A **read-only / design-only "Authority & Dimension Reconciliation" sprint** that produces: (a) a DECISION_LOG entry choosing an authority contract; (b) schema *proposals* for `subject_domain`, `geography`, `jurisdiction`, `temporal`, and the atomic evidence record (no backfill, no route edits); (c) the source-lock + claim-activation path exercised on the single MoS₂ chain as a proof-of-discipline; (d) the Information-Gain calibration dataset design. **It writes no HTML, changes no indexation, adds no CI hard-fail, and publishes nothing.** Live-posture work (the consistency check, then de-indexation) is deferred to a later, separately-approved sprint per §14.

---

*v2 correction pass — READ-ONLY. No production files modified. No implementation sprint authorized or begun.*
