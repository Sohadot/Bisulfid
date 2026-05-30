# Corpus Production Rules

**Sprint:** 6A  
**Version:** 1.0.0  
**Site:** bisulfid.com  
**Status:** Codified operational rulebook  
**Governed by:** `doctrine/SOURCE_POLICY.md`, `main/data/corpus_route_formula.json`, `main/data/page_type_registry.json`, `main/data/audience_layer_registry.json`

---

## 1. Purpose

This rulebook defines what the sovereign 14,000-page corpus **may** generate, **must not** generate, and **how** batch-governed automation must constrain every page. It is executable doctrine—not brainstorming.

---

## 2. Strategic scale rule

- **Minimum target:** 14,000 real governed reference pages.
- **Derivation:** dimensional intersection (language × term/entity × page family × audience × source posture × claim posture × indexation × internal-link role)—**not** volume inflation.
- **Multilingual floor:** 7 languages × 2,000 governed pages per language = 14,000 pages.
- **English** is the primary global/institutional layer; **Arabic, German, French, Spanish, Japanese, Chinese** are governed expansion layers.

---

## 3. What may be generated

A page may enter generation only when **all** of the following hold:

1. **Route inventory row exists** with unique `route_id` and valid dimensional intersection per `corpus_route_formula.json`.
2. **Page type** is registered in `page_type_registry.json` with `generation_eligibility` satisfied.
3. **Audience** is allowed for the page type per `audience_layer_registry.json`.
4. **Required data fields** for the page type are present in ontology, route, source, and claim registries.
5. **Source posture** meets page type `source_requirements`.
6. **Claim posture** meets page type `claim_requirements`.
7. **Draft or planned status** only unless explicit launch charter authorizes publication.
8. **Generator reads registries**—no free-form LLM generation as production method.
9. **Validators pass** for the cohort before merge.

---

## 4. What must not be generated

| Forbidden output | Rule |
| --- | --- |
| Fake pages | No route without dimensional justification and required fields |
| Thin pages | Fewer than page type `required_data_fields`; stub-only content |
| Placeholder public pages | No `published` or `indexable: true` without launch gate |
| Random SEO pages | Every page must map to page_type and audience |
| Unsupported safety/medical/market claims | SOURCE_POLICY and audience restrictions |
| Hallucinated facts | Generator must not invent bibliographic or chemical facts |
| Free LLM pages | LLM may assist drafting under registry constraints; not autonomous production |
| Broken-link targets | Every internal link `route_id` must exist in inventory |
| Marker removal without charter | `[SOURCE REQUIRED]` preserved until dedicated sprint |
| Public HTML before gates | No generated public output until S8 pre-publication pass |

---

## 5. Thin and fake page definitions

A page is **thin** if:

- Body lacks page type `required_data_fields` content.
- Word count below minimum for page type (terminology reference: substantive sections; comparison: both sides addressed).
- Only boilerplate with no entity-specific governed content.
- Duplicate intent of another route without dimensional distinction (e.g. same term + language + audience + page type twice).

A page is **fake** if:

- Route exists only to inflate count without registry backing.
- Factual lines lack source/claim registry linkage.
- Content contradicts registered claim boundaries.
- Generated without reading ontology, sources, and claims.

**Action:** Reject at generation; do not register route or do not merge draft.

---

## 6. Route existence vs publication

| State | Meaning |
| --- | --- |
| `planned` + no draft | Route inventory only; no content file |
| `planned` + draft | Draft-backed; **non_public**; may exist indefinitely |
| `published` | Owner-authorized only; all gates passed |

A route **may exist but remain non-public** when source or claim gates are incomplete. Existence does not imply indexation or visibility.

---

## 7. Draft-backed eligibility

Draft creation requires:

- Row in route inventory (`routes.json` or future master inventory).
- `status: planned` or charter-authorized draft wave.
- Frontmatter: `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`.
- Draft notice, boundaries, `[SOURCE REQUIRED]` on unresolved factual lines.
- Page type and audience compatibility verified.

---

## 8. Indexation eligibility

A page may become **indexable** only when:

1. `production_can_safely_proceed: yes` or launch cohort authorized.
2. Source posture: verified/locked for all factual claims.
3. Claim posture: approved for all registered claim classes on page.
4. `[SOURCE REQUIRED]` markers resolved under charter.
5. Internal-link graph valid (no broken edges).
6. SEO metadata validated (title, description, hreflang, canonical).
7. Technical/security validation pass.
8. Explicit owner decision recorded in DECISION_LOG.

**Default for all new routes:** `indexable: false`, `in_sitemap: false`, `in_navigation: false`.

---

## 9. Source and claim constraints on content

- **No source entry = no published factual claim** (SOURCE_POLICY).
- Generator must inject only claims present in claim registries with `status: approved` or `approval_limited` narrow approval.
- Generator must cite only sources with `status: verified` or `source_lock_status: locked` for published lines.
- Draft pages may retain `[SOURCE REQUIRED]` and `source_posture: source_required_unresolved`.
- Page type `forbidden_content_classes` and audience `forbidden_claim_classes` are hard rejects.

---

## 10. Batch generation anti-hallucination rules

1. Generator input = route row + ontology term + page type + audience + source rows + claim rows.
2. Generator output template = page type schema; no unconstrained prose generation.
3. Every factual sentence must map to a claim_id or remain `[SOURCE REQUIRED]`.
4. No new sources or claims created by generator.
5. Human or validator sample audit on every cohort (minimum 10% or 3 pages).
6. Failed validation blocks merge.

---

## 11. Automation and validator connection

| Stage | Validator layer |
| --- | --- |
| Route inventory | L0 route registry; future 6B inventory validators |
| Draft production | L0 content drafts; L1 corpus drafts |
| Source/claim | L1 source/claim guardrail runtime |
| Publication lock | L1 publication lock |
| Internal links | L2 internal link graph plan |
| SEO/metadata | L2 SEO indexation plan |
| Multilingual | L2 multilingual wave plan |
| Pre-publication | L2 production planner; S8 readiness |

Automation **reports**; automation does **not** auto-publish, auto-approve claims, or auto-index.

---

## 12. Batch production benchmarks

| Phase | Benchmark |
| --- | --- |
| Initial automation | 100 governed pages/day minimum once generator stable |
| Target throughput | 500 pages/day with stable validators and inventory |
| Method | Route cohort waves—not one-source-one-page month cycles |

---

## 13. Difference/comparison pages (core SEO class)

`PT_DIFFERENCE_COMPARISON` is a **core page family**, not secondary articles. High-intent reference for chemists, researchers, students, analysts, and AI systems. Every comparison route requires registered `comparison_pair_id` and sources/claims for both sides where distinction is stated.

---

## 14. Phased execution reference

| Sprint | Focus |
| --- | --- |
| **6A** | Codify architecture (this sprint) |
| **6B** | 14,000-route master inventory model |
| **6C** | Schemas, templates, generator design |
| **6D** | First large governed draft cohort |
| **6E** | Internal-link graph and validation expansion |
| **6F** | Controlled public visibility plan |

---

## 15. Current corpus baseline (Sprint 6A)

| Metric | Value |
| --- | ---: |
| Registered routes | 126 |
| Draft-backed routes | 68 |
| Missing drafts | 58 |
| Publication lock | LOCKED |
| `production_can_safely_proceed` | no |

No pages generated in Sprint 6A. Architecture codification only.
