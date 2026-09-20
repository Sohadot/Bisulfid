# DECISION LOG

This document records decisions that affect the architecture, doctrine, data, or direction of bisulfid.com.

All structural decisions require an entry here. Changes to doctrine require an entry here.

---

## Log Format

Each entry includes:

- **Date**
- **Sprint / Phase**
- **Decision**
- **Rationale**
- **Doctrine reference** (if applicable)
- **Files affected**

---

## Entries

### 2026-05-15 — Sprint 0A: Doctrine Foundation

**Decision:** Establish the minimum sovereign doctrine foundation for bisulfid.com.

**Rationale:** The README defines bisulfid.com as a Global Sovereign Sulfur Intelligence Gateway with a governed doctrine folder. Before any content, code, or deployment decisions are made, the governing documents that define what this asset is, how it operates, and what conditions must be met before launch must exist in the repository. These documents serve as the single source of truth for all future decisions.

**Doctrine reference:** `ASSET_THESIS.md` — all documents flow from it.

**Files created:**

- `doctrine/ASSET_THESIS.md` — top doctrine document; defines what this asset is.
- `doctrine/PROJECT_DOCTRINE.md` — governs all operations.
- `doctrine/MULTILINGUAL_POLICY.md` — governs language architecture and hreflang integrity.
- `doctrine/GLOBAL_REFERENCE_STANDARD.md` — governs global reference quality.
- `doctrine/SOURCE_POLICY.md` — governs claims and sources.
- `doctrine/QUALITY_GATE.md` — defines the 11 launch conditions.
- `doctrine/SECURITY_POLICY.md` — governs security posture.
- `DECISION_LOG.md` — this document.
- `main/data/languages.json` — machine-readable language registry.

**Not created in this sprint:** frontend UI, HTML, CSS, JS, images, GitHub Actions, scripts, package.json, CURSOR_RULES.md, generated site output, placeholder content pages.

---

### 2026-05-15 — Sprint 0B: Data Skeleton and Route Governance Established

**Decision:** Create planned route, ontology, source, claim, sitemap, hreflang, translation, and internal-link registries.

**Rationale:** Before content or UI work can begin, the data governance skeleton must exist. Routes, ontology terms, and claim categories must be registered in a planned or inactive state so that content creation has a governed framework to operate within. No routes were published. No sitemap entries were activated. No claims were approved. No sources were fabricated.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`

**Files created:**

- `main/data/routes.json` — planned EN v1 route registry (21 routes, all planned, none published).
- `main/data/hreflang_groups.json` — empty hreflang group registry, inactive.
- `main/data/translation_registry.json` — empty translation registry, inactive.
- `main/data/internal_links.json` — planned internal link graph (route_id references only, not raw URLs).
- `main/data/sitemap_policy.json` — sitemap governance policy, inactive, no active URLs.
- `main/data/ontology/sulfur_terms.json` — governed ontology skeleton with 14 terms, all planned.
- `main/data/ontology/spatial_nodes.json` — Interactive Term Map node registry, 11 nodes, all planned.
- `main/data/ontology/term_edges.json` — semantic edge registry, 12 edges, all planned, no sources locked.
- `main/data/sources/source_registry.json` — source registry structure established, no sources added.
- `main/data/claims/terminology_claims.json` — empty claim registry, inactive.
- `main/data/claims/science_claims.json` — empty claim registry, inactive.
- `main/data/claims/industry_claims.json` — empty claim registry, inactive.
- `main/data/claims/safety_claims.json` — empty claim registry, inactive, blocked patterns defined.
- `main/data/claims/market_claims.json` — empty claim registry, inactive, blocked patterns defined.
- `main/data/claims/acquisition_claims.json` — empty claim registry, inactive.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0B entry appended.

**Not created in this sprint:** HTML pages, markdown content pages, templates, CSS, JS, scripts, GitHub Actions, package.json, dependencies, site/ output, placeholder content.

---

### 2026-05-15 — Sprint 0C: Multilingual Content Skeleton Established

**Decision:** Create the governed multilingual content directory structure for EN, DE, AR, ZH, JA, FR, and ES, plus shared disclaimer, source-note, and canonical-claim folders.

**Rationale:** Before any content work begins, the directory structure must exist in a governed state. Content directories make clear where files belong, what layer each language occupies, and that file presence is not the same as publication. The shared disclaimer folder establishes a controlled location for site-wide governance fragments that must be attached to pages before any route may pass the Quality Gate.

**Doctrine reference:** `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`

**Files created:**

- `main/content/README.md` — content directory governance document.
- `main/content/en/pages/.gitkeep`
- `main/content/en/term-records/.gitkeep`
- `main/content/en/fragments/.gitkeep`
- `main/content/de/pages/.gitkeep`
- `main/content/de/term-records/.gitkeep`
- `main/content/de/fragments/.gitkeep`
- `main/content/ar/pages/.gitkeep`
- `main/content/ar/term-records/.gitkeep`
- `main/content/ar/fragments/.gitkeep`
- `main/content/zh/pages/.gitkeep`
- `main/content/zh/term-records/.gitkeep`
- `main/content/zh/fragments/.gitkeep`
- `main/content/ja/pages/.gitkeep`
- `main/content/ja/term-records/.gitkeep`
- `main/content/ja/fragments/.gitkeep`
- `main/content/fr/pages/.gitkeep`
- `main/content/fr/term-records/.gitkeep`
- `main/content/fr/fragments/.gitkeep`
- `main/content/es/pages/.gitkeep`
- `main/content/es/term-records/.gitkeep`
- `main/content/es/fragments/.gitkeep`
- `main/content/shared/canonical-claims/.gitkeep`
- `main/content/shared/source-notes/.gitkeep`
- `main/content/shared/disclaimers/editorial-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/safety-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/translation-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/sponsorship-disclaimer.md` — draft, not attached to any route.
- `main/content/shared/disclaimers/acquisition-disclaimer.md` — draft, not attached to any route.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0C entry appended.

**Not created in this sprint:** public content pages, index.md, route content files, templates, CSS, JS, scripts, GitHub Actions, package.json, dependencies, site/ output. No routes were published. No sitemap or navigation state was changed. No claims or sources were added.

---

### 2026-05-15 — Sprint 0D: Validator Skeleton Established

**Decision:** Create safe placeholder validator files aligned with the 11 Quality Gates and route/source/claim/multilingual governance requirements.

**Rationale:** Before a build system exists, the validator surface area must be reserved in code. Validators need to exist as named, documented files so that future build-system integration has stable entry points. Each validator documents what it will enforce without claiming to enforce it yet. Placeholder behavior (print warning, exit 0) prevents false failures in CI stubs while making the non-enforcement status explicit and undeniable.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/SECURITY_POLICY.md`

**Sprint 0D constraints (all observed):**
- Validators are intentionally non-enforcing at this stage.
- No build system was created.
- No GitHub Actions workflows were created.
- No dependencies were added.
- No package.json was created.
- No public pages were created.
- No routes were modified.
- No claim files were modified.
- No source registry was modified.
- No content directories were modified.
- README.md was not modified.
- Placeholder validators must not be treated as proof of launch readiness.

**Files created:**

- `scripts/validators/README.md` — validator directory governance document.
- `scripts/validators/validate_all.py` — orchestrator; runs all validators in Quality Gate order.
- `scripts/validators/validate_links.py` — future Gate 01 + Gate 08 (links and orphans).
- `scripts/validators/validate_content.py` — future Gate 02 + Gate 09 (content quality).
- `scripts/validators/validate_indexation.py` — future Gate 03 (sitemap and indexation).
- `scripts/validators/validate_sources.py` — future Gate 04 (source registry).
- `scripts/validators/validate_claims.py` — future Gate 04 + blocked-claim patterns.
- `scripts/validators/validate_seo.py` — future Gate 05 (SEO compliance).
- `scripts/validators/validate_security.py` — future Gate 06 (security posture).
- `scripts/validators/validate_accessibility.py` — future Gate 07 (accessibility).
- `scripts/validators/validate_routes.py` — future route registry governance.
- `scripts/validators/validate_schema.py` — future structured data (JSON-LD) checks.
- `scripts/validators/validate_hreflang.py` — future Gate 11 (hreflang correctness).
- `scripts/validators/validate_translations.py` — future Gate 11 (translation integrity).
- `scripts/validators/validate_language_routes.py` — future Gate 11 (language routes).
- `scripts/validators/validate_supply_chain.py` — future supply chain security checks.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0D entry appended.

**Not created in this sprint:** build system, GitHub Actions, package.json, dependencies, templates, CSS, JS, HTML pages, site/ output, frontend UI.

---

### 2026-05-15 — Sprint 1: Static Build Skeleton Established

**Decision:** Create a minimal Python-stdlib-only static build skeleton: config layer, template skeletons, build scripts, and sitemap/robots generators. Zero public pages are generated. All routes remain in `planned` state.

**Rationale:** A governed build system must exist before any content can be placed into production. The build skeleton establishes the machinery — config, templates, scripts — without activating any route, publishing any page, or enabling any indexation. The prelaunch posture (full robots.txt disallow, zero-URL sitemap, `noindex` SEO config) is enforced at the script level, not merely declared. This sprint creates the assembly line, not the product.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/SECURITY_POLICY.md`

**Sprint 1 constraints (all observed):**
- Python standard library only. No external dependencies.
- No package.json created.
- No GitHub Actions workflows created.
- No deployment config created.
- No Cloudflare config created.
- No routes marked published.
- No routes marked indexable.
- No routes marked in_sitemap.
- No routes.json modified.
- No claim files modified.
- No source registry modified.
- No content directories modified.
- No real content pages created.
- No inline JS in any template.
- No external scripts referenced.
- No tracking of any kind.
- No visual UI, advanced CSS, or animations.
- All templates carry skeleton disclaimer comment.
- Placeholder validators must not be treated as proof of launch readiness.

**Files created:**

- `main/config/build.json` — build orchestrator config; `publish_planned_routes: false`, `generate_only_published_routes: true`.
- `main/config/seo.json` — SEO governance config; `default_robots: "noindex, nofollow"`.
- `main/config/security.json` — security policy config; inline JS and external scripts disallowed.
- `main/config/navigation.json` — navigation config; status inactive, items empty.
- `main/config/site.json` — site identity config; status prelaunch.
- `main/templates/base.html` — base layout skeleton; no inline JS, no external scripts.
- `main/templates/home.html` — home page skeleton.
- `main/templates/term.html` — term record page skeleton.
- `main/templates/category.html` — category page skeleton.
- `main/templates/language_index.html` — language index page skeleton.
- `main/templates/404.html` — 404 error page skeleton.
- `main/templates/robots.txt` — robots.txt template (prelaunch: full disallow).
- `main/templates/partials/header.html` — header partial skeleton.
- `main/templates/partials/footer.html` — footer partial skeleton.
- `main/templates/partials/nav.html` — navigation partial skeleton (inactive).
- `main/templates/partials/breadcrumb.html` — breadcrumb partial skeleton.
- `main/templates/partials/hreflang_block.html` — hreflang link block partial.
- `main/templates/partials/structured_data.html` — JSON-LD structured data partial skeleton.
- `main/templates/partials/disclaimer_block.html` — disclaimer block partial skeleton.
- `main/templates/partials/interactive_term_map.html` — Interactive Term Map partial; documents data sources and JS-disabled fallback.
- `scripts/build.py` — build orchestrator; loads config and routes; generates `site/build-status.json` only; 0 public pages.
- `scripts/generate_robots.py` — generates `site/robots.txt`; prelaunch full-disallow policy.
- `scripts/generate_sitemap.py` — generates `site/sitemap.xml`; filters published+indexable+in_sitemap; 0 URLs pass.
- `scripts/generate_placeholders.py` — generates placeholder HTML skeletons for planned routes (dev/review use only; no public output).
- `scripts/README.md` — scripts directory governance document.
- `site/.gitkeep` — reserves site/ output directory.

**Files updated:**

- `DECISION_LOG.md` — Sprint 1 entry appended.

**Not created in this sprint:** public content pages, real index.html, published routes, sitemap URLs, GitHub Actions, package.json, external dependencies, deployment config, Cloudflare config, visual UI, animations, inline JS, external scripts, tracking.

---

### 2026-05-15 — Sprint 2: English Source Drafts Established

**Decision:** Create the first non-public English source-layer draft pages for the homepage, Bisulfid definition, spelling boundary, German-English sulfur terminology, source discipline, and strategic acquisition surface.

**Rationale:** Before any route can be considered for publication, draft content must exist in a governed state. Draft pages establish what each route will say, identify which claims require source-locking, and provide reviewable material for the source registry population sprint. Draft presence is not publication — no route was published, no claim was approved, no source was added.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 2 constraints (all observed):**
- No route was published.
- No sitemap or navigation state was changed.
- No claims were approved.
- No sources were added.
- No fake source citations were included.
- No external links were included as verified.
- No numerical market claims were stated as verified.
- No specific companies were named as acquisition targets.
- No chemical handling instructions were included.
- No medical or therapeutic advice was included.
- No safety thresholds were included.
- Bisulfid and bisulfite were not conflated.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- source_registry.json was not modified.
- Claim files were not modified.
- README.md was not modified.
- No HTML output was created.
- No dependencies were added.
- No GitHub Actions were created.
- All draft pages carry `status: draft` and `publication_status: non_public`.
- All draft pages carry `indexable: false` and `in_sitemap: false`.
- Claims requiring source-locking are marked `[SOURCE REQUIRED]` inline.

**Files created:**

- `main/content/en/README.md` — English source layer governance document.
- `main/content/en/pages/index.md` — homepage draft; Global Sovereign Sulfur Intelligence Gateway positioning; six strategic layers; language architecture; Interactive Term Map as planned future interface; link intent by route_id.
- `main/content/en/pages/what-is-bisulfid.md` — defines Bisulfid as the central term; domain thesis vs chemical definition; center-node position; disambiguation from bisulfite; German-form spelling boundary.
- `main/content/en/pages/bisulfid-vs-bisulfide.md` — The Missing Letter; bisulfide→bisulfid; English vs German spelling boundary; E is not missing; asset architecture.
- `main/content/en/pages/sulfid-vs-sulfide.md` — broader -id/-ide suffix pattern; Oxide/Oxid and Chloride/Chlorid examples (all [SOURCE REQUIRED]); supports German identity layer.
- `main/content/en/pages/sources.md` — source discipline; no source entry = no published claim; blocked source types; registry not yet populated; draft content is not public evidence.
- `main/content/en/pages/acquire.md` — strategic acquisition surface; what a buyer acquires; no price; no urgency; no named targets; contact agent@sohadot.com.

**Files updated:**

- `DECISION_LOG.md` — Sprint 2 entry appended.

**Not created in this sprint:** HTML output, published pages, sitemap entries, navigation items, source entries, approved claims, GitHub Actions, dependencies, package.json, route modifications.

---

### 2026-05-15 — Sprint 2B: English Draft Alignment Review Completed

**Decision:** Review and align all six English source-layer draft pages against route governance, internal link planning, ontology, source discipline, and acquisition discipline. Make minimal corrections only.

**Rationale:** The Sprint 2 drafts contained a systematic route ID format error: all six pages used `en-*` prefixed, hyphen-separated route IDs (e.g., `en-home`, `en-what-is-bisulfid`) rather than the IDs defined in `routes.json` (e.g., `home`, `what_is_bisulfid`). This would prevent the build system from matching content files to their routes. Additional issues included incomplete planned link sections and a reference to a nonexistent route. All corrections were minimal and did not alter content, remove [SOURCE REQUIRED] markers, or change any governance state.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 2B constraints (all observed):**
- No new pages created.
- No route was published.
- No sitemap or navigation state was changed.
- No claims were approved.
- No sources were added.
- No [SOURCE REQUIRED] markers removed.
- All pages remain `status: draft` and `publication_status: non_public`.
- All pages remain `indexable: false` and `in_sitemap: false`.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- source_registry.json was not modified.
- Claim files were not modified.
- root README.md was not modified.
- No HTML output was created.
- No dependencies were added.
- No GitHub Actions were created.

**Issues corrected:**

- All six pages: `route_id` corrected from `en-*` format to `routes.json` format (e.g., `en-home` → `home`, `en-what-is-bisulfid` → `what_is_bisulfid`).
- All inline route references: corrected to use `routes.json` format throughout.
- `index.md`: removed reference to `en-term-bisulfid` (no corresponding route in routes.json); added `what_is_sulfur` and `industrial_sulfur_systems` to planned link section.
- `what-is-bisulfid.md`: added `bisulfide_hydrosulfide_sulfide` and `german_english_chemical_terms` to planned link section.
- `bisulfid-vs-bisulfide.md`: added `german_english_chemical_terms` and `bisulfide_hydrosulfide_sulfide` to planned link section.
- `sulfid-vs-sulfide.md`: added `what_is_bisulfid`, `glossary`, and `sources` to planned link section.
- `sources.md`: added planned link section (`what_is_bisulfid`, `glossary`, `home`).
- `acquire.md`: added planned link section (`home`, `what_is_bisulfid`, `industrial_sulfur_systems`).

**Infrastructure note recorded:**

`routes.json` `content_file` fields point to `main/content/en/*.md` while actual files are in `main/content/en/pages/*.md`. This path discrepancy requires resolution in a future sprint.

**Files created:**

- `main/content/en/DRAFT_ALIGNMENT_REPORT.md` — full alignment review report.

**Files updated:**

- `main/content/en/pages/index.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/what-is-bisulfid.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/bisulfid-vs-bisulfide.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/sulfid-vs-sulfide.md` — route_id corrected; link intent aligned.
- `main/content/en/pages/sources.md` — route_id corrected; planned link section added.
- `main/content/en/pages/acquire.md` — route_id corrected; planned link section added.
- `DECISION_LOG.md` — Sprint 2B entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, source_registry.json, claim files, root README.md, templates, scripts, doctrine files, ontology files, data registries.

---

### 2026-05-15 — Sprint 2C: Route Content Paths Aligned

**Decision:** Update all 21 `content_file` paths in `routes.json` to point to the governed `main/content/en/pages/` directory structure. Correct the `home` route to point to `index.md` rather than the non-existent `home.md`.

**Rationale:** Sprint 0B created `routes.json` with `content_file` paths pointing to `main/content/en/*.md`. Sprint 0C established `main/content/en/pages/` as the governed directory for English page drafts. Sprint 2 created draft files in `pages/`. This path mismatch was identified in Sprint 2B and recorded as an infrastructure issue. Sprint 2C resolves it. No route status, indexation, sitemap, navigation, or governance state was changed — only the `content_file` field values.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`

**Sprint 2C constraints (all observed):**
- No route was published.
- No route `status` value was changed.
- No route `indexable` value was changed.
- No route `in_sitemap` value was changed.
- No route `in_navigation` value was changed.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- source_registry.json was not modified.
- Claim files were not modified.
- No new content pages were created.
- No generated HTML route pages were created.
- Templates were not modified.
- Root README.md was not modified.

**Path corrections (all 21 routes):**

- `home`: `main/content/en/home.md` → `main/content/en/pages/index.md`
- `what_is_sulfur`: `main/content/en/what-is-sulfur.md` → `main/content/en/pages/what-is-sulfur.md`
- `sulfur_compounds`: `main/content/en/sulfur-compounds.md` → `main/content/en/pages/sulfur-compounds.md`
- `sulfur_uses`: `main/content/en/sulfur-uses.md` → `main/content/en/pages/sulfur-uses.md`
- `what_is_bisulfid`: `main/content/en/what-is-bisulfid.md` → `main/content/en/pages/what-is-bisulfid.md`
- `bisulfid_vs_bisulfide`: `main/content/en/bisulfid-vs-bisulfide.md` → `main/content/en/pages/bisulfid-vs-bisulfide.md`
- `sulfid_vs_sulfide`: `main/content/en/sulfid-vs-sulfide.md` → `main/content/en/pages/sulfid-vs-sulfide.md`
- `bisulfide_hydrosulfide_sulfide`: `main/content/en/bisulfide-hydrosulfide-sulfide.md` → `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md`
- `sodium_bisulfide`: `main/content/en/sodium-bisulfide.md` → `main/content/en/pages/sodium-bisulfide.md`
- `disulfide_bonds`: `main/content/en/disulfide-bonds.md` → `main/content/en/pages/disulfide-bonds.md`
- `industrial_sulfur_systems`: `main/content/en/industrial-sulfur-systems.md` → `main/content/en/pages/industrial-sulfur-systems.md`
- `sulfur_safety_context`: `main/content/en/sulfur-safety-context.md` → `main/content/en/pages/sulfur-safety-context.md`
- `hydrogen_sulfide_risk`: `main/content/en/hydrogen-sulfide-risk.md` → `main/content/en/pages/hydrogen-sulfide-risk.md`
- `sds_and_sulfur_terms`: `main/content/en/sds-and-sulfur-terms.md` → `main/content/en/pages/sds-and-sulfur-terms.md`
- `protein_disulfide_structure`: `main/content/en/protein-disulfide-structure.md` → `main/content/en/pages/protein-disulfide-structure.md`
- `molybdenum_disulfide`: `main/content/en/molybdenum-disulfide.md` → `main/content/en/pages/molybdenum-disulfide.md`
- `german_english_chemical_terms`: `main/content/en/german-english-chemical-terms.md` → `main/content/en/pages/german-english-chemical-terms.md`
- `glossary`: `main/content/en/glossary.md` → `main/content/en/pages/glossary.md`
- `sources`: `main/content/en/sources.md` → `main/content/en/pages/sources.md`
- `newsletter`: `main/content/en/newsletter.md` → `main/content/en/pages/newsletter.md`
- `acquire`: `main/content/en/acquire.md` → `main/content/en/pages/acquire.md`

**Files created:**

- `main/data/ROUTE_CONTENT_PATH_ALIGNMENT_REPORT.md` — alignment report documenting issue, corrections, and governance state.

**Files updated:**

- `main/data/routes.json` — all 21 `content_file` paths corrected.
- `DECISION_LOG.md` — Sprint 2C entry appended.

**Not modified in this sprint:** route status values, indexation state, sitemap state, navigation state, sitemap_policy.json, navigation.json, source_registry.json, claim files, content draft pages, templates, scripts, doctrine files, ontology files, root README.md.

---

### 2026-05-15 — Sprint 3: Source Registry Seeded

**Decision:** Seed the first real source entries into `source_registry.json`, assign candidate `source_ids` to eight ontology terms in `sulfur_terms.json`, and register five terminology claims and three science claims in the claim registries. All claims remain `pending_review`. No claim is approved.

**Rationale:** The source registry must be populated before any claim can progress toward publication. Sprint 3 seeds authoritative dictionary, chemical nomenclature standard, and government scientific database sources that correspond to the terminology and chemical identity claims most central to the bisulfid.com domain thesis. All sources are `seeded` and `candidate` — none are final or permanently approved. No [SOURCE REQUIRED] markers were removed from draft content pages. No route was published. This sprint establishes the first layer of the three-layer source discipline: source_registry.json → claim registries → content pages.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 3 constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved. All claims remain pending_review.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- All source entries carry status: seeded and source_lock_status: candidate.
- All ontology term statuses remain planned.
- No term was marked verified or published.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- industry_claims.json was not modified.
- acquisition_claims.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- routes.json was not modified.
- root README.md was not modified.
- templates were not modified.
- scripts were not modified.
- No market statistics were added.
- No Gulf, Morocco, or China production or trade data was added.
- No acquisition-target company claims were added.
- No dependencies were added.
- No GitHub Actions were created.
- No HTML output was created.
- This sprint does not constitute publication readiness.

**Sources seeded (8):**

- `SRC-MW-BISULFIDE` — authoritative_dictionary — Merriam-Webster — bisulfide
- `SRC-MW-SULFIDE` — authoritative_dictionary — Merriam-Webster — sulfide
- `SRC-MW-BISULFITE` — authoritative_dictionary — Merriam-Webster — bisulfite
- `SRC-DUDEN-SULFID` — authoritative_dictionary — Duden — Sulfid
- `SRC-IUPAC-HYDROSULFIDES` — chemical_nomenclature_standard — IUPAC Gold Book — hydrosulfides
- `SRC-PUBCHEM-HYDROSULFIDE` — government_scientific_database — PubChem / NIH — Hydrosulfide
- `SRC-PUBCHEM-SODIUM-HYDROSULFIDE` — government_scientific_database — PubChem / NIH — Sodium hydrosulfide
- `SRC-NIST-HYDROGEN-SULFIDE` — government_scientific_database — NIST Chemistry WebBook — Hydrogen sulfide

**Terminology claims registered (5):** CLM-TERM-001 through CLM-TERM-005, all pending_review.

**Science claims registered (3):** CLM-SCI-001 through CLM-SCI-003, all pending_review.

**Ontology terms receiving candidate source_ids (8):** bisulfide, sulfide, sulfid, bisulfite_disambiguation, hydrosulfide, sodium_hydrosulfide, sodium_bisulfide, hydrogen_sulfide.

**Terms with no source_ids this sprint (6):** bisulfid (center node — highest priority for next source sprint), disulfide, disulfid, molybdenum_disulfide, molybdenum_disulfide_mos2, sulfur.

**Files created:**

- `main/data/SOURCE_REGISTRY_SEED_REPORT.md` — seed report documenting sources, claims, term mappings, gaps, and publication state.

**Files updated:**

- `main/data/sources/source_registry.json` — 8 sources added.
- `main/data/claims/terminology_claims.json` — 5 pending_review claims added.
- `main/data/claims/science_claims.json` — 3 pending_review claims added.
- `main/data/ontology/sulfur_terms.json` — candidate source_ids added to 8 terms.
- `DECISION_LOG.md` — Sprint 3 entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, market_claims.json, safety_claims.json, industry_claims.json, acquisition_claims.json, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 3 Patch: Source Governance Fields Completed

**Decision:** Add structured `use_for`, `do_not_use_for`, and `risk_notes` fields to all eight seeded source entries in `source_registry.json`.

**Summary:** Sprint 3 patch added structured use_for, do_not_use_for, and risk_notes fields to all seeded source entries, preserving candidate status and non-public claim state.

**Rationale:** Pre-merge review identified that the source schema required three structured governance fields per entry. The original Sprint 3 commit used a single freeform `notes` field. This patch adds the three required fields as arrays of strings to all 8 entries. The `notes` field was retained alongside the new structured fields. No source status, claim status, ontology term status, routes, content pages, or publication state was changed.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`

**Patch constraints (all observed):**
- Only `main/data/sources/source_registry.json` and `DECISION_LOG.md` were modified.
- No claim files were modified.
- No ontology files were modified.
- No routes were modified.
- No content pages were modified.
- All source entries retain `status: seeded`.
- All source entries retain `source_lock_status: candidate`.
- No new sources were added.
- No sources were removed.
- No claim was approved.
- No public route or sitemap state was changed.
- No dependencies, workflows, generated output, or README modifications.

**Files updated:**

- `main/data/sources/source_registry.json` — `use_for`, `do_not_use_for`, and `risk_notes` arrays added to all 8 source entries.
- `DECISION_LOG.md` — Sprint 3 patch entry appended.

---

### 2026-05-16 — Sprint 3B: Bisulfid Center Node Candidate Source Added

**Decision:** Add candidate source support for the `bisulfid` center node in `source_registry.json`, assign that source to `bisulfid.source_ids` in `sulfur_terms.json`, register a corresponding pending_review terminology claim, and document the sprint in `BISULFID_CENTER_SOURCE_REPORT.md`.

**Summary:** Sprint 3B addressed the highest-priority Sprint 3 source gap by adding candidate source support for the bisulfid center node. The source support is limited to German technical usage and does not make the center node verified. No routes were published. No claims were approved. No sitemap, navigation, content, market, safety, or acquisition state was changed. The center node still requires stronger source-locking before publication.

**Rationale:** The `bisulfid` center node is the conceptual and linguistic anchor of bisulfid.com. Sprint 3 explicitly flagged it as the highest-priority remaining source gap. No authoritative dictionary, nomenclature standard, or government scientific database entry directly under the term 'Bisulfid' was identified for seeding in this sprint. The Badger Meter German-language technical page was identified as the strongest currently available candidate source: it directly uses 'Bisulfid und Schwefelwasserstoff' in a German water-quality monitoring context. It was added as an `industry_publication` source with strict use limitations. The center node remains `planned` and requires a stronger tier-1 source before any publication pathway opens.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 3B constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved. All claims remain pending_review.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- New source entry carries status: seeded and source_lock_status: candidate.
- bisulfid term status remains planned.
- bisulfid was not marked verified.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- science_claims.json was not modified.
- industry_claims.json was not modified.
- acquisition_claims.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- routes.json was not modified.
- root README.md was not modified.
- templates were not modified.
- scripts were not modified.
- No market data was added.
- No Gulf, Morocco, or China production or trade data was added.
- No acquisition-target company claims were added.
- No dependencies were added.
- No GitHub Actions were created.
- No HTML output was created.
- No Wikipedia or AI summary sources were used.
- This sprint does not constitute publication readiness.

**Source added (1):**

- `SRC-BADGER-BISULFID-H2S` — industry_publication — Badger Meter — Messung von Bisulfid und Schwefelwasserstoff im Wasser

**Ontology update:** `bisulfid.source_ids` updated from `[]` to `["SRC-BADGER-BISULFID-H2S"]`. Status remains `planned`.

**Terminology claim added (1):** CLM-TERM-BISULFID-001, pending_review, candidate usage only.

**Remaining gap:** Bisulfid center node still requires a tier-1 source (Duden 'Bisulfid' entry, IUPAC direct entry, German regulatory database, or peer-reviewed academic reference) before the center node can be considered for source-locking.

**Files created:**

- `main/data/BISULFID_CENTER_SOURCE_REPORT.md` — source evaluation report for the bisulfid center node.

**Files updated:**

- `main/data/sources/source_registry.json` — SRC-BADGER-BISULFID-H2S added.
- `main/data/ontology/sulfur_terms.json` — bisulfid.source_ids updated; notes updated.
- `main/data/claims/terminology_claims.json` — CLM-TERM-BISULFID-001 added, pending_review.
- `DECISION_LOG.md` — Sprint 3B entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 3C: Source-to-Claim Governance Alignment Completed

**Decision:** Review the seeded source registry, pending terminology claims, pending science claims, ontology source mappings, and English draft pages. Produce a source-to-claim alignment report. Correct structural inconsistencies in claim entries.

**Summary:** Sprint 3C reviewed the seeded source registry, pending terminology claims, pending science claims, ontology source mappings, and English draft pages. The sprint produced a source-to-claim alignment report. No claims were approved. No routes were published. No sitemap or navigation state was changed. No content pages were modified. No market, safety, acquisition, or industrial data was added.

**Structural corrections made:**
- `main/data/claims/terminology_claims.json`: CLM-TERM-001 through CLM-TERM-005 were missing three governance fields (`allowed_pages`, `prohibited_uses`, `risk_level`) present in CLM-TERM-BISULFID-001. These fields were added to all five claims. No claim status was changed.
- `main/data/claims/science_claims.json`: CLM-SCI-001 through CLM-SCI-003 were missing the same three governance fields. These fields were added to all three claims. No claim status was changed.

**Key findings:**
- All 9 source entries confirmed complete with required fields and appropriate scope.
- 6 terminology claims and 3 science claims all remain pending_review.
- No claim uses out-of-scope source material (no market data, safety advice, medical claims, or bisulfite data used as bisulfide data).
- No ontology term is marked verified.
- bisulfid center node remains planned with candidate source support only.
- sources.md contains a stale statement (“The source registry is not populated yet”) — correction deferred to a future content update sprint.
- sulfid_vs_sulfide is the most heavily blocked page: three distinct source gaps with no registered claims covering Oxide/Oxid or Chloride/Chlorid examples or a formal suffix-pattern nomenclature standard.

**Rationale:** A governance alignment review was required before any claim approval sprint can proceed. Claims missing `allowed_pages`, `prohibited_uses`, and `risk_level` cannot be safely approved or scoped to pages. Correcting the structural inconsistency in this sprint ensures the claim registries are in a state where future approval decisions can be made against a complete schema.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 3C constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved. All claims remain pending_review.
- Claim registries remain inactive.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- source_registry.json was not modified.
- ontology/sulfur_terms.json was not modified.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- industry_claims.json was not modified.
- acquisition_claims.json was not modified.
- root README.md was not modified.
- No dependencies, workflows, or generated output were created.
- No Wikipedia or AI summary sources were used.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/SOURCE_CLAIM_ALIGNMENT_REPORT.md` — source-to-claim alignment report.

**Files updated:**

- `main/data/claims/terminology_claims.json` — `allowed_pages`, `prohibited_uses`, `risk_level` added to CLM-TERM-001 through CLM-TERM-005.
- `main/data/claims/science_claims.json` — `allowed_pages`, `prohibited_uses`, `risk_level` added to CLM-SCI-001 through CLM-SCI-003.
- `DECISION_LOG.md` — Sprint 3C entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, source_registry.json, ontology/sulfur_terms.json, market_claims.json, safety_claims.json, industry_claims.json, acquisition_claims.json, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 3D: Sources Page Draft Statement Corrected

**Decision:** Correct a stale statement in `main/content/en/pages/sources.md` that said “The source registry is not populated yet.” after Sprint 3 and Sprint 3B had populated the registry with seeded candidate sources.

**Summary:** Sprint 3D corrected a stale non-public draft statement in sources.md after the source registry gained seeded candidate sources. The page now distinguishes candidate source entries from approved publication claims. No route was published. No claim was approved. No sitemap, navigation, source registry, or claim registry state changed.

**Rationale:** Sprint 3C’s `SOURCE_CLAIM_ALIGNMENT_REPORT.md` explicitly flagged the statement as inaccurate following the source seeding work of Sprint 3 and Sprint 3B. Leaving a factually incorrect description of the source registry in a governed draft page creates an internal inconsistency that must be resolved before any publication sprint proceeds.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`

**Sprint 3D constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- No claim was approved.
- No [SOURCE REQUIRED] marker was removed.
- No other content pages were modified.
- source_registry.json was not modified.
- ontology/sulfur_terms.json was not modified.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- market_claims.json was not modified.
- safety_claims.json was not modified.
- industry_claims.json was not modified.
- science_claims.json was not modified.
- terminology_claims.json was not modified.
- acquisition_claims.json was not modified.
- root README.md was not modified.
- No dependencies, workflows, or generated output were created.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/SOURCES_PAGE_DRAFT_CORRECTION_REPORT.md` — correction report.

**Files updated:**

- `main/content/en/pages/sources.md` — “Current Registry Status” section rewritten; stale statement removed; new wording distinguishes candidate sources from approved claims.
- `DECISION_LOG.md` — Sprint 3D entry appended.

**Not modified in this sprint:** source_registry.json, routes.json, sitemap_policy.json, navigation.json, claim registries, ontology files, templates, scripts, doctrine files, root README.md. No other content pages were modified.

---

### 2026-05-16 — Sprint 4A: German Suffix Pattern Candidate Sources Added

**Decision:** Add candidate lexical source support for German `Oxid` and `Chlorid`, align those sources with existing `Sulfid` support as a cautious German `-id` lexical comparison set, and add English IUPAC nomenclature context as candidate support only.

**Summary:** Sprint 4A added candidate lexical source support for German Oxid and Chlorid and aligned these with existing Sulfid support as a cautious German -id lexical comparison set. No formal German suffix rule was claimed. No claims were approved. No routes were published. No content pages were modified. The sulfid-vs-sulfide draft remains blocked until stronger nomenclature source-locking is completed.

**Rationale:** Sprint 3C identified `sulfid_vs_sulfide` as the most blocked draft page because its Oxide/Oxid and Chloride/Chlorid examples lacked registered source and claim support. Duden dictionary entries can support individual German lexical forms, but not a formal chemical nomenclature rule. The IUPAC 1971 source can provide English `-ide` nomenclature context only and cannot prove a German suffix-compression rule.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4A constraints (all observed):**
- No route was published.
- No route status, indexable, in_sitemap, or in_navigation value was changed.
- routes.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- No claim was approved. All new claims remain pending_review.
- Claim registries remain inactive.
- No [SOURCE REQUIRED] marker was removed from any content page.
- No content pages were created or modified.
- No ontology term was marked verified.
- No market_claims, safety_claims, science_claims, industry_claims, or acquisition_claims files were modified.
- No market data was added.
- No Gulf, Morocco, China, production, trade, CAGR, or market-share data was added.
- No acquisition-target company claims were added.
- Root README.md was not modified.
- Templates were not modified.
- No generated HTML route pages were created.
- No dependencies were added.
- No GitHub Actions workflows were created.
- No Wikipedia or AI summary sources were used.
- No formal German suffix rule source was found.
- This sprint does not constitute publication readiness.

**Sources added (3):**

- `SRC-DUDEN-OXID` — authoritative_dictionary — Duden — Oxid.
- `SRC-DUDEN-CHLORID` — authoritative_dictionary — Duden — Chlorid.
- `SRC-IUPAC-INORGANIC-NOMENCLATURE-1971` — chemical_nomenclature_standard — IUPAC / Pure and Applied Chemistry — Nomenclature of Inorganic Chemistry.

**Terminology claims added (4):**

- `CLM-TERM-OXID-001` — pending_review lexical claim for Oxid.
- `CLM-TERM-CHLORID-001` — pending_review lexical claim for Chlorid.
- `CLM-TERM-GERMAN-ID-PATTERN-001` — pending_review cautious lexical comparison-set claim for Sulfid, Oxid, and Chlorid.
- `CLM-TERM-ENGLISH-IDE-CONTEXT-001` — pending_review English -ide nomenclature context claim.

**Files created:**

- `main/data/SULFID_SUFFIX_SOURCE_REPORT.md` — Sprint 4A source report and publication readiness conclusion.

**Files updated:**

- `main/data/sources/source_registry.json` — Duden Oxid, Duden Chlorid, and IUPAC 1971 candidate sources added.
- `main/data/claims/terminology_claims.json` — four pending_review terminology claims added.
- `DECISION_LOG.md` — Sprint 4A entry appended.

**Not modified in this sprint:** routes.json, sitemap_policy.json, navigation.json, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json, ontology files, content draft pages, templates, scripts, doctrine files, root README.md.

---

### 2026-05-16 — Sprint 4B: Formal German Nomenclature Source Search Completed

**Decision:** Evaluate stronger German nomenclature sources for the `-id` pattern behind the `sulfid_vs_sulfide` draft and document the source-category gap for academic teaching and textbook/book-chapter materials.

**Summary:** Sprint 4B evaluated stronger German nomenclature sources for the -id pattern behind the sulfid-vs-sulfide draft. No sources were added because the evaluated German academic teaching and book/chapter sources do not fit an existing governed source category without inventing or stretching the registry taxonomy. No formal German suffix rule was claimed. No claims were approved. No routes were published. No content pages were modified. The sulfid-vs-sulfide draft remains non-public until source-locking and claim approval are completed.

**Rationale:** Sprint 4A established lexical candidate support for `Sulfid`, `Oxid`, and `Chlorid`, but did not close the formal German nomenclature gap. Sprint 4B searched for stronger German support and found potentially useful academic or teaching sources, but the current source registry categories do not include academic teaching PDFs, textbook chapters, or book chapters as governed source types unless they qualify as formal chemical nomenclature standards or peer-reviewed journals. No new category was created.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4B constraints (all observed):**
- source_registry.json was not modified.
- No unsupported source category was invented.
- No source was added, so no source was marked final, locked, approved, verified, or public-ready.
- terminology_claims.json was not modified.
- No claim was approved.
- Claim registries remain inactive.
- No market_claims, safety_claims, science_claims, industry_claims, or acquisition_claims files were modified.
- sulfur_terms.json was not modified.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No Wikipedia or AI summary sources were used as sources.
- No market data, Gulf data, Morocco data, China data, production data, trade data, CAGR data, or market-share data was added.
- No acquisition-target company claims were added.
- This sprint does not constitute publication readiness.

**Sources evaluated but not added:**

- `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR` — academic/teaching PDF; category not currently governed.
- `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN` — university teaching PDF; category not currently governed.
- `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID` — book/chapter or textbook material; category not currently governed.
- `SRC-IUPAC-BRIEF-GUIDE-INORGANIC-2005` — English IUPAC nomenclature context only; not distinct German suffix-rule authority beyond the Sprint 4A IUPAC context source.

**Claims added:** None.

**Files created:**

- `main/data/GERMAN_NOMENCLATURE_SOURCE_SEARCH_REPORT.md` — Sprint 4B source-search report documenting evaluated sources, category gap, formal-source status, and publication readiness.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4B entry appended.

**Not modified in this sprint:** source_registry.json, terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, doctrine files, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4C: Source Category Governance Expansion Reviewed

**Decision:** Review whether Bisulfid should later expand its source governance system to include academic teaching references, textbook references, or technical educational references.

**Summary:** Sprint 4C reviewed whether Bisulfid should expand its source governance system to include academic teaching references, textbook references, or technical educational references. No source category was added. No source was added. No claim was added or approved. No route was published. No content page was modified. The sprint produced a governance review report to guide a future implementation decision.

**Rationale:** Sprint 4B identified useful German academic/teaching/book sources for the `-id` nomenclature pattern, but those sources were not added because current source categories do not govern those source types. Sprint 4C evaluates whether a future controlled category could preserve useful instructional evidence without weakening source discipline or treating teaching material as formal nomenclature authority.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4C constraints (all observed):**
- `SOURCE_CATEGORY_GOVERNANCE_REVIEW.md` was created.
- SOURCE_POLICY.md was not modified.
- source_registry.json was not modified.
- No source category was added.
- No source entries were added.
- terminology_claims.json was not modified.
- No claim entries were added.
- No claim was approved.
- Claim registries remain inactive.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market data or acquisition-target company claims were added.
- This sprint does not constitute publication readiness.

**Recommendation:** Add no category in Sprint 4C. Consider a future narrow `academic_teaching_reference` category, with a separate `textbook_reference` category or sub-scope only if explicit safeguards are implemented first. Any such category should remain candidate-only by default and should not approve claims alone or prove formal nomenclature authority.

**Files created:**

- `main/data/SOURCE_CATEGORY_GOVERNANCE_REVIEW.md` — governance review report for possible future source category expansion.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4C entry appended.

**Not modified in this sprint:** SOURCE_POLICY.md, source_registry.json, terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, doctrine files, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4D: Controlled Academic Teaching Source Category Implemented

**Decision:** Implement a narrow governed source category named `academic_teaching_reference`.

**Summary:** Sprint 4D implemented a narrow governed source category named academic_teaching_reference. The category is candidate-only and may support source-search review or cautious educational terminology context, but it cannot serve as formal nomenclature authority, cannot approve claims alone, cannot publish routes, and cannot remove [SOURCE REQUIRED] markers by itself. No source entries were added. No claims were added or approved. No routes were published. No content pages were modified.

**Rationale:** Sprint 4B identified useful German academic/teaching/book sources that did not fit existing source categories, and Sprint 4C recommended a narrow controlled category rather than a broad educational catch-all. Sprint 4D implements the category-level governance needed before any future sprint evaluates specific academic teaching sources.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4D constraints (all observed):**
- SOURCE_POLICY.md was modified only to add the governed `academic_teaching_reference` category and its constraints.
- source_registry.json remains valid JSON.
- `academic_teaching_reference` was added to the governed source categories.
- No source entries were added.
- No existing source entry status was changed.
- No source was marked final, locked, approved, verified, or public-ready.
- terminology_claims.json was not modified.
- No claim entries were added.
- No claim was approved.
- Claim registries remain inactive.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market data or acquisition-target company claims were added.
- No actual FH Münster, Rostock, Springer/Jander, or other source entries were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/ACADEMIC_SOURCE_CATEGORY_IMPLEMENTATION_REPORT.md` — implementation report for the controlled academic teaching source category.

**Files updated:**

- `doctrine/SOURCE_POLICY.md` — `academic_teaching_reference` added as a governed candidate-only category with constraints.
- `main/data/sources/source_registry.json` — `academic_teaching_reference` added to `source_categories`; no source entries added.
- `DECISION_LOG.md` — Sprint 4D entry appended.

**Not modified in this sprint:** terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4E: Academic Teaching Candidate Sources Registered

**Decision:** Register selected German academic teaching references under the governed `academic_teaching_reference` category.

**Summary:** Sprint 4E registered candidate academic teaching references under the newly governed academic_teaching_reference category where permitted by SOURCE_POLICY.md. The sources may support draft/source-search review and cautious educational terminology context only. They do not establish formal nomenclature authority, do not approve claims alone, do not publish routes, and do not remove [SOURCE REQUIRED] markers by themselves. No claims were approved. No routes were published. No content pages were modified.

**Rationale:** Sprint 4D created a narrow candidate-only category for university and academic instructional chemistry sources. Sprint 4E applies that category to FH Münster and Universität Rostock teaching references while leaving Springer/Jander unregistered because publisher-hosted textbook/book-chapter material is not clearly governed by the current category.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4E constraints (all observed):**
- source_registry.json remains valid JSON.
- All newly added source entries use `category: academic_teaching_reference`.
- Every new source has `status: seeded` and `source_lock_status: candidate`.
- Every new source has `use_for`, `do_not_use_for`, and `risk_notes` arrays.
- No new source is marked final, locked, approved, verified, or public-ready.
- No source outside the governed category boundary was added.
- Springer/Jander was not added because SOURCE_POLICY.md does not clearly govern textbook/book-chapter sources under `academic_teaching_reference`.
- terminology_claims.json remains valid JSON.
- New claims are status: pending_review only.
- No claim was approved.
- Claim registry remains inactive.
- market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, and acquisition_claims.json were not modified.
- SOURCE_POLICY.md was not modified.
- sulfur_terms.json was not modified.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, Gulf, Morocco, China, production, trade, CAGR, market-share, or acquisition-target claims were added.
- This sprint does not constitute publication readiness.

**Sources added (2):**

- `SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR` — academic_teaching_reference — FH Münster — Anorganische Nomenklatur.
- `SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN` — academic_teaching_reference — Universität Rostock — Materialdesign / Nomenklatur.

**Sources evaluated but not added:**

- `SRC-SPRINGER-JANDER-ANORGANISCHE-NOMENKLATUR-ID` — not registered because textbook/book-chapter material is not clearly governed by the current `academic_teaching_reference` category.

**Claims added (1):**

- `CLM-TERM-GERMAN-ID-ACADEMIC-001` — pending_review candidate academic teaching support only.

**Files created:**

- `main/data/ACADEMIC_TEACHING_SOURCE_REGISTRATION_REPORT.md` — Sprint 4E source registration report.

**Files updated:**

- `main/data/sources/source_registry.json` — two academic teaching candidate source entries added.
- `main/data/claims/terminology_claims.json` — one pending_review terminology claim added.
- `DECISION_LOG.md` — Sprint 4E entry appended.

**Not modified in this sprint:** SOURCE_POLICY.md, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4F: Academic Source Claim Boundaries Reviewed

**Decision:** Review and document the claim boundaries of the registered `academic_teaching_reference` sources before any claim approval, source-locking, content edit, or publication decision.

**Summary:** Sprint 4F reviewed the claim boundaries of the newly registered academic_teaching_reference sources. The sprint documented what FH Münster and Universität Rostock may support as candidate academic teaching context, and what they cannot support without stronger formal authority. No claims were approved. No source entries were modified. No routes were published. No content pages were modified. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Sprint 4E added candidate academic teaching references and a pending-review claim. Before any future source-locking or content sprint, the project needs an explicit boundary record stating that these sources can support cautious educational context only, not formal DIN, official German IUPAC, GDCh, route publication, ontology verification, or marker removal.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4F constraints (all observed):**
- `ACADEMIC_SOURCE_CLAIM_BOUNDARY_REPORT.md` was created.
- SOURCE_POLICY.md was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- No source entries were added.
- No source entries were modified.
- No claim entries were added.
- No claim was approved.
- Claim registries remain inactive.
- routes.json was not modified.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, or acquisition claims were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/data/ACADEMIC_SOURCE_CLAIM_BOUNDARY_REPORT.md` — boundary report for academic teaching sources and `CLM-TERM-GERMAN-ID-ACADEMIC-001`.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4F entry appended.

**Not modified in this sprint:** SOURCE_POLICY.md, source_registry.json, terminology_claims.json, routes.json, sitemap_policy.json, navigation.json, ontology files, content draft pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Sprint 4G: German-English Chemical Terms Draft Path Reviewed

**Decision:** Review the missing German-English chemical terms draft path and route/content alignment state without creating content or changing route governance.

**Summary:** Sprint 4G reviewed the missing German-English chemical terms draft path identified in Sprint 4F. The sprint diagnosed the route/content alignment state without creating the missing page, modifying routes, publishing any route, approving claims, or removing [SOURCE REQUIRED] markers. The result will guide a future content-alignment sprint.

**Rationale:** `routes.json` contains a planned `german_english_chemical_terms` route pointing to `main/content/en/pages/german-english-chemical-terms.md`, but the content file does not exist. Internal links reference the route by `route_id`, and the route remains planned and non-public. The review also found that this is part of a broader planned-route/content inventory gap, not a unique missing page.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4G constraints (all observed):**
- `GERMAN_ENGLISH_TERMS_DRAFT_PATH_REVIEW.md` was created.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were created.
- No content pages were modified.
- `main/content/en/pages/german-english-chemical-terms.md` was not created.
- No [SOURCE REQUIRED] markers were removed.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- This sprint does not constitute publication readiness.

**Finding:** `german_english_chemical_terms` is a planned route with a valid expected content path, but the draft file is missing. It is one of multiple planned English routes without content drafts.

**Files created:**

- `main/data/GERMAN_ENGLISH_TERMS_DRAFT_PATH_REVIEW.md` — diagnostic route/content path review for `german_english_chemical_terms`.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4G entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, content pages, templates, scripts, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — German-English Chemical Terms Non-Public Draft Created

**Decision:** Create the missing English draft page for `german_english_chemical_terms` as a terminology-control file aligned with Sprint 4G route/content path findings, without changing route metadata, link registries, or claim state.

**Summary:** Sprint 4H created the missing non-public English draft for `german_english_chemical_terms` at `main/content/en/pages/german-english-chemical-terms.md`. The route remains planned, indexable remains false, sitemap inclusion remains false, and the draft is not publication-ready. No claims were approved. No source entries were modified. No routes or internal links were changed. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Sprint 4G diagnosed a missing `content_file` at the governed path while `routes.json` already pointed to it. Adding the draft file closes that gap for future source-locking and Quality Gate work. The page is explicitly non-public, cautious, and marked with [SOURCE REQUIRED] where factual support is not yet approved; academic teaching sources are not conflated with DIN or official German IUPAC authority, and no universal English-to-German suffix rule is asserted as fact.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4H constraints (all observed):**
- `main/content/en/pages/german-english-chemical-terms.md` was created with required frontmatter.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No [SOURCE REQUIRED] markers were removed from any page.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, or acquisition claims were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/content/en/pages/german-english-chemical-terms.md` — non-public terminology-control draft for `german_english_chemical_terms`.
- `main/data/GERMAN_ENGLISH_TERMS_DRAFT_CREATION_REPORT.md` — sprint record and remaining blockers.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4H entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, templates, scripts, other content draft pages (except the new file listed above), root README.md, package files, workflows, generated output, ontology files, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — English Draft Inventory Reviewed

**Decision:** Map all planned English routes to draft file presence, content-directory inventory, and internal link dependencies without creating or editing drafts or changing route metadata.

**Summary:** Sprint 4I reviewed the English planned route inventory and mapped routes to existing draft content files. The sprint identified which planned English routes already have drafts, which routes remain missing drafts, and which routes should be prioritized in future draft-creation sprints. No content pages were created or modified. No routes were published. No claims were approved. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Sprint 4G framed a broader route/content inventory gap beyond `german_english_chemical_terms`. Sprint 4H created that one missing draft; remaining English routes still lack `content_file` bodies. A consolidated table and link-demand view reduces ad hoc planning risk and keeps prioritization explicit while routes stay `planned` and non-indexable.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4I constraints (all observed):**
- `ENGLISH_DRAFT_INVENTORY_REVIEW.md` was created.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were created.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, handling, or acquisition claims were added.
- This sprint does not constitute publication readiness.

**Finding (English):** 21 `language: en` routes; 7 draft-backed; 14 missing `content_file`. Highest planned link demand among missing routes targets `glossary` (18 referring link groups), then `sodium_bisulfide` (7), `industrial_sulfur_systems` (6), and `sulfur_safety_context` (5). `newsletter` has no incoming planned internal link targets.

**Files created:**

- `main/data/ENGLISH_DRAFT_INVENTORY_REVIEW.md` — English planned-route draft inventory and prioritization notes.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4I entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, content pages, templates, scripts, root README.md, package files, workflows, generated output, ontology files, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Terminology Reference Spine Batch 1 Established

**Decision:** Create the first batch of non-public English drafts for the terminology reference spine (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`) as internal reference infrastructure without changing route metadata, link registries, or claim state.

**Summary:** Sprint 4J added governed draft bodies at the exact `content_file` paths declared in `routes.json` for `glossary`, `sulfur_compounds`, and `bisulfide_hydrosulfide_sulfide`. The drafts function as a terminology chamber scaffold, a sulfur-compound scope map, and a bisulfide/hydrosulfide/sulfide disambiguation authority file. All remain non-public, non-indexable, not sitemap-listed, and not publication-ready. No routes were published. No claims were approved. No registries were modified. [SOURCE REQUIRED] markers remain on all relevant drafts and were not removed from other pages.

**Rationale:** Sprint 4I showed heavy planned internal-link demand on `glossary` and related terminology routes. Establishing these three drafts closes the highest-priority missing-body gap for the terminology spine while keeping strict separation from safety handling, market data, and publication workflows.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4J constraints (all observed):**
- Three target `content_file` drafts created with required frontmatter; paths verified against `routes.json`; no pre-existing files overwritten.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No [SOURCE REQUIRED] markers were removed from any page.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety-handling, medical, procurement, or acquisition-target content was added.
- No raw URLs or publication-assuming links were added.
- This sprint does not constitute publication readiness.

**Files created:**

- `main/content/en/pages/glossary.md` — controlled terminology chamber draft.
- `main/content/en/pages/sulfur-compounds.md` — sulfur terminology scope map draft.
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` — disambiguation authority draft.
- `main/data/TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md` — sprint record.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4J entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, templates, scripts, other existing content draft pages (except the three new files listed above), root README.md, package files, workflows, generated output, ontology files, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Terminology Reference Spine Batch 1 Completion Patch

**Decision:** Close Sprint 4J pre-merge acceptance gaps by expanding terminology spine draft coverage and report inventory accounting without publishing routes, changing registries, or removing [SOURCE REQUIRED] markers.

**Summary:** This patch completed the Sprint 4J reference-spine acceptance gaps by expanding the glossary term coverage, strengthening the sulfur compound scope map, preserving the bisulfite disambiguation boundary in the bisulfide/hydrosulfide/sulfide draft, and completing the Sprint 4J report with the remaining missing draft count. No routes were published. No claims were approved. No registries or route records were modified. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Initial batch 4J drafts met governance scope but lacked full controlled-term tables, explicit scope-map sections, dedicated non-claim and registry-status sections on the disambiguation page, bisulfite separation language, and explicit 14/3/11 missing-draft accounting in the sprint report.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Patch constraints (all observed):**
- Only the three spine drafts, `TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md`, and `DECISION_LOG.md` were edited for this patch.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified.
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No [SOURCE REQUIRED] markers were removed from any page.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety-handling, medical, procurement, production, trade, CAGR, market-share, or acquisition-target content was added.
- No raw URLs or publication-assuming links were added.
- This patch does not constitute publication readiness.

**Files updated:**

- `main/content/en/pages/glossary.md` — expanded controlled term table and distinction rules.
- `main/content/en/pages/sulfur-compounds.md` — expanded terminology groups and teaching vs authority section.
- `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md` — bisulfite boundary; what this page does not claim; source and claim status.
- `main/data/TERMINOLOGY_REFERENCE_SPINE_BATCH_1_REPORT.md` — spine vs generic framing; 11 remaining missing drafts; blockers; no publication recommendation.
- `DECISION_LOG.md` — this patch entry appended.

**Not modified in this patch:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, source_registry.json, terminology_claims.json, sulfur_terms.json, templates, other content draft pages outside the three spine files above, root README.md, package files, workflows, generated output, ontology files, claim data JSON beyond those listed, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Terminology Reference Spine Boundaries Reviewed

**Decision:** Read-only boundary review of the first terminology reference spine (`glossary`, `sulfur_compounds`, `bisulfide_hydrosulfide_sulfide`) after Sprint 4J, without creating or modifying content pages or changing route or registry state.

**Summary:** Sprint 4K reviewed the first non-public terminology reference spine created in Sprint 4J. The review confirmed the glossary, sulfur_compounds, and bisulfide_hydrosulfide_sulfide drafts remain non-public reference infrastructure and not publication-ready content. The sprint documented claim boundaries, source boundaries, bisulfite disambiguation boundaries, and future internal reference roles. No content pages were created or modified. No claims were approved. No routes were published. [SOURCE REQUIRED] markers remain in place.

**Rationale:** Before expanding the English draft inventory (11 routes still missing `content_file` bodies), the project needs a recorded check that spine copy stays within terminology governance, does not imply approved claims, and does not drift into generic chemistry, safety, or market content.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4K constraints (all observed):**
- `TERMINOLOGY_REFERENCE_SPINE_BOUNDARY_REVIEW.md` was created.
- routes.json was not modified.
- internal_links.json was not modified.
- sitemap_policy.json was not modified.
- navigation.json was not modified.
- hreflang_groups.json was not modified.
- translation_registry.json was not modified.
- source_registry.json was not modified (path: `main/data/sources/source_registry.json` on disk).
- terminology_claims.json was not modified.
- sulfur_terms.json was not modified.
- No content pages were created.
- No content pages were modified.
- No [SOURCE REQUIRED] markers were removed.
- No claim was approved.
- Claim registries remain inactive.
- All routes remain planned.
- No route has indexable: true or in_sitemap: true.
- No generated HTML pages were created.
- No dependencies or workflows were created.
- Root README.md was not modified.
- No market, safety, medical, procurement, acquisition, production, or trade content was added.
- No raw URLs or publication-assuming links were added by this sprint.
- This sprint does not constitute publication readiness.

**Finding:** Spine drafts align with terminology-first infrastructure roles; bisulfite boundary and teaching-vs-authority separation are preserved in copy; registries remain unchanged and inactive for approval work.

**Files created:**

- `main/data/TERMINOLOGY_REFERENCE_SPINE_BOUNDARY_REVIEW.md` — boundary review record for the first terminology reference spine.

**Files updated:**

- `DECISION_LOG.md` — Sprint 4K entry appended.

**Not modified in this sprint:** routes.json, internal_links.json, sitemap_policy.json, navigation.json, hreflang_groups.json, translation_registry.json, `main/data/sources/source_registry.json`, terminology_claims.json, sulfur_terms.json, all English and other content draft pages, templates, root README.md, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-16 — Core Term Drafts Batch 2 Sprint Record (Route Targets Absent)

**Decision:** Execute Sprint 4L pre-flight against `main/data/routes.json` before drafting core term pages; do not create orphan `content_file` bodies when `route_id` records are missing.

**Summary:** Sprint 4L targeted non-public English core term drafts for `bisulfid`, `sulfid`, and `hydrosulfide`, but pre-flight review found **none** of those `route_id` values in `routes.json`. Per project rules, no `bisulfid.md`, `sulfid.md`, or `hydrosulfide.md` files were added. The sprint created `CORE_TERM_DRAFTS_BATCH_2_REPORT.md` documenting the blocker, nearest existing related routes (`what_is_bisulfid`, `sulfid_vs_sulfide`, `bisulfide_hydrosulfide_sulfide`), and recommended follow-up. **Remaining missing English draft count stays 11** (unchanged from post–Sprint 4J). No routes were published. No claims were approved. No source entries, route records, internal links, sitemap policy, navigation, hreflang, translation registry, ontology, or claim registries were modified. `[SOURCE REQUIRED]` markers on existing pages remain unchanged.

**Rationale:** Core term drafts must map 1:1 to authoritative `content_file` paths in `routes.json`. Inventing routes or orphan markdown files would break inventory integrity and violate Sprint 4L constraints.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`

**Sprint 4L validation (observed where applicable):**

- Target `route_id` values `bisulfid`, `sulfid`, and `hydrosulfide` **do not** exist in `routes.json` — **blocker recorded**; no page files created for those names.
- All **existing** routes remain `status: planned`, `language: en` where declared, `indexable: false`, `in_sitemap: false` — verified on read of `routes.json`; **no edits** made.
- **No** new content pages created; **no** existing content pages modified.
- **No** `[SOURCE REQUIRED]` markers removed from any file.
- **No** raw URLs or publication-assuming links added by this sprint.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- No claim has `status: approved`; claim registries remain **inactive**.
- No generated HTML pages, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `main/data/CORE_TERM_DRAFTS_BATCH_2_REPORT.md` exists; states remaining missing draft count **11** after this sprint; **8** is the modeled count only if all three target routes had existed and all three drafts had been created.
- `DECISION_LOG.md` updated with this entry.
- This sprint does **not** recommend publication.

**Files created:**

- `main/data/CORE_TERM_DRAFTS_BATCH_2_REPORT.md` — Sprint 4L record; pre-flight route absence; next steps.

**Files updated:**

- `DECISION_LOG.md` — this entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all existing content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-18 — Sovereign Reference Corpus Architecture Established

**Decision:** Record Bisulfid.com as a **large, sovereign-grade, multilingual chemical-language reference corpus** with **300 governed pages** as the **minimum public launch threshold**, not the final ambition, and scale horizons toward **500 / 1,000 / 3,000+** pages only under strict quality gates.

**Summary:** Sprint **5A** established long-term corpus architecture and launch-cohort blueprint documentation. The sprint defined the difference between **minimum public launch cohort**, **long-term reference corpus**, and **full authority system**; specified multilingual layers (English spine, German identity, Arabic, Chinese, Japanese technical references); documented expansion rules, anti-thin and anti-generic discipline, and launch thresholds. **CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md** lists **307** proposed page concepts (blueprint only—**not** added to `routes.json`). **No** routes were published. **No** content pages were created or modified. **No** claims were approved. **No** registry files (`routes.json`, `internal_links.json`, sitemap/navigation, source or claim registries, ontology) were modified. **No** public HTML or dependencies were added.

**Rationale:** The owner rejects weak visibility and generic chemistry sites; reference trust requires doctrine-first scaling and a planned path to a **large** corpus—not a stop at 300 pages.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/MULTILINGUAL_POLICY.md`

**Sprint 5A validation (observed where applicable):**

- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` created; states **300 pages** = **minimum launch cohort**, **not** the final goal.
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` created; **≥ 300** proposed concepts (**307** rows).
- `main/data/CORPUS_EXPANSION_MODEL.md` created; defines expansion beyond 300 pages with strict gates.
- `main/data/CORPUS_LAUNCH_THRESHOLD.md` created; minimum threshold and no-publication conditions.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified** (this sprint).
- **No** content under `main/content/` created or modified.
- **No** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML pages, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Files created:**

- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` — corpus thesis, layers, categories, multilingual model, authority standard, risks, next sprint.
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` — launch cohort blueprint table (**307** concepts).
- `main/data/CORPUS_EXPANSION_MODEL.md` — expansion horizons and governance rules.
- `main/data/CORPUS_LAUNCH_THRESHOLD.md` — launch and no-go gates.

**Files updated:**

- `DECISION_LOG.md` — Sprint 5A entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-19 — Launch Cohort Blueprint Quality Reviewed

**Decision:** Record a **blueprint-only quality review** of the **307** proposed launch-cohort concepts from Sprint **5A**; **do not** treat the raw blueprint as **launch-cohort-ready** without refinement.

**Summary:** Sprint **5B** evaluated `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` against sovereign-grade doctrine: thesis fit, anti-thin / anti-generic posture, source and claim risk, multilingual discipline (controlled terminology vs translation spam), duplicate/merge needs, and utility pages vs reference pages. Findings are recorded in **`LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`** and **`LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`**. **No** routes were created. **No** content pages were created or modified. **No** claims were approved. **No** registries (`routes.json`, `internal_links.json`, sitemap/navigation, source/claim/ontology JSON) were modified. **No** public HTML, dependencies, or workflows were added.

**Rationale:** A 307-row scaffold is necessary but **not sufficient** for a sovereign first launch; **EN+DE** must lead, **ar/zh/ja** bulk mirrors should **defer**, **H₂S** and **MoS₂/WS₂** concepts should **merge**, and **newsletter/acquire** must be **excluded from the 300 reference-page** cohort accounting.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`; corpus docs from Sprint 5A.

**Sprint 5B validation (observed where applicable):**

- `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md` created.
- `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md` created.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- **No** `main/content/**` changes.
- **No** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` changes.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication** (review/reporting sprint only).

**Files created:**

- `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md` — methodology, classification, strengths/risks, multilingual and source/claim assessment, launch-cohort-ready verdict (**no**), refinement prerequisites.
- `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md` — keep/revise/merge/defer/reject lists, first implementation batch size (**40–55** routes recommended), Sprint **5C** options.

**Files updated:**

- `DECISION_LOG.md` — Sprint 5B entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`, `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `main/data/CORPUS_EXPANSION_MODEL.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, all content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-18 — Launch Cohort Implementation Batch 1 Planned

**Decision:** Record Sprint **5C** as a **planning and implementation-readiness** sprint that defines **Batch 1** (**55** proposed `route_id` concepts: **44** English, **11** German) for later controlled routing and drafting—**without** registering new routes, **without** creating or modifying content pages, and **without** publication.

**Summary:** Sprint **5C** converted the Sprint **5A**/ **5B** launch-cohort architecture and quality review into a disciplined first implementation batch. The sprint did **not** create routes, did **not** create content pages, did **not** publish any route, and did **not** approve any claim. The selected batch prioritizes source-governed terminology, German–English chemical language, disambiguation authority, corpus methodology, source/nomenclature governance, and controlled reference infrastructure while deferring weak, mirrored, utility, or insufficiently governed concepts (`newsletter` / `acquire`, `ar` / `zh` / `ja` mirrors, high-risk safety substance pages in this batch, and broad DE term grids). Deliverables: `LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`, `ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`, `SPRINT_5C_ROUTE_SELECTION_RATIONALE.md`.

**Rationale:** A 307-row blueprint is necessary but insufficient; a **55-route** governed slice proves editorial depth, citation discipline, and linking density before scaling toward the **300-page** minimum launch cohort—without lowering the threshold or recommending public launch.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/MULTILINGUAL_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`; Sprint **5A**/**5B** corpus documentation.

**Sprint 5C validation (observed where applicable):**

- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` exists; **55** proposed concepts (within **40–55** batch intent stated in 5B as a range; Batch 1 lands at **55** as the upper disciplined bound).
- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` exists; all **55** rows classified.
- `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md` exists.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified** (this sprint).
- **No** `main/content/**` pages created or modified.
- **No** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All existing routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` changes from this sprint (no `routes.json` edits).
- **No** generated HTML pages, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication** (strategy/planning sprint only).

**Files created:**

- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` — Batch 1 roster, governance logic, and full per-concept specifications.
- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` — readiness classification and next actions for each concept.
- `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md` — selection thesis and exclusions.

**Files updated:**

- `DECISION_LOG.md` — Sprint 5C entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`, `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `main/data/CORPUS_EXPANSION_MODEL.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, `main/data/LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md`, `main/data/LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`, all content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-20 — Ready Route Planning Batch 1A Added

**Decision:** Register the Sprint **5C** **`ready_for_route_planning`** slice (**7** concepts) in `routes.json` as **`planned`**, non-indexable, non-sitemap routes—**without** duplicating pre-existing `route_id`s and **without** creating `content_file` bodies.

**Summary:** Sprint **5D** added **five** new route records (`corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, `de_method_translator_playbook`). **`home`** and **`sources`** were **already** in `routes.json`; no duplicate rows were inserted (documented in `ROUTE_PLANNING_BATCH_1A_REPORT.md`). The sprint did **not** create or modify content pages, did **not** modify `internal_links.json`, did **not** publish routes, did **not** approve claims, and did **not** alter source, claim, sitemap, navigation, or ontology registries. The remaining Sprint **5C** concepts remain outside `routes.json` until source mapping, claim-boundary review, merge/scope refinement, or later-phase governance is completed.

**Rationale:** Execute Batch **1A** as a **route-planning-only** increment that matches the readiness matrix’s lowest-friction cohort while keeping the **300-page** launch threshold and Quality Gate doctrine unchanged.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`; Sprint **5C** planning documents.

**Sprint 5D validation (observed where applicable):**

- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` lists exactly **7** `ready_for_route_planning` concepts; **no** concepts from other buckets were added.
- `main/data/routes.json` parses as valid JSON; **26** route records total (**21** prior + **5** new).
- Every **new** route: `status: planned`, `indexable: false`, `in_sitemap: false`.
- `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- **No** `main/content/**` files created or modified.
- No claim has `status: approved`; claim registries remain **inactive** (no edits this sprint).
- **No** generated HTML, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `main/data/ROUTE_PLANNING_BATCH_1A_REPORT.md` created.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not public launch**; all routes remain **planned** and non-sitemap.

**Files created:**

- `main/data/ROUTE_PLANNING_BATCH_1A_REPORT.md` — Batch 1A scope, sources, adds vs skips, confirmations, deferred cohort counts.

**Files updated:**

- `main/data/routes.json` — **five** new planned route records.
- `DECISION_LOG.md` — Sprint 5D entry appended.

**Not modified in this sprint:** `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`, `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md`, `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md`, `main/data/CORPUS_LAUNCH_THRESHOLD.md`, all existing content draft pages, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json.

---

### 2026-05-21 — Batch 1A Non-Public Drafts Created

**Decision:** Create **non-public** Markdown drafts for the **five** Sprint **5D** Batch **1A** `route_id` records—matching **`routes.json`** `content_file` paths—without changing route publication state, registries, or the internal link graph.

**Summary:** Sprint **5E** added draft bodies for `corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, and `de_method_translator_playbook`. Drafts support sovereign corpus **methodology**, **internal linking discipline**, **Quality Gate** explanation, and **German** methodology layers. **No** routes were published. **No** `routes.json` fields were edited. **No** `internal_links.json` changes. **No** claims were approved. **No** source, sitemap, navigation, or ontology registries were modified. **`[SOURCE REQUIRED]`** markers remain where claims are not yet registry-backed.

**Rationale:** Route shells from Sprint **5D** require reviewable text while keeping all assets **planned**, **non-indexable**, and **non-sitemap** until Quality Gate and source/claim work catch up.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`.

**Sprint 5E validation (observed where applicable):**

- Five target `content_file` paths exist with YAML frontmatter: `route_id`, `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`, language fields aligned with `routes.json`.
- Draft bodies state **non-public** / **not publication-ready** posture; include **`[SOURCE REQUIRED]`** where appropriate; do **not** claim source-locking complete; do **not** approve claims; use **route_id** plain references only (**no** raw URLs; **no** markdown links assuming publication).
- German drafts (`de_method_corpus_map`, `de_method_translator_playbook`) are written in **German**; do **not** assert DIN or official German IUPAC authority.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` introduced.
- **No** generated HTML, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `main/data/BATCH_1A_NON_PUBLIC_DRAFT_CREATION_REPORT.md` created.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not public launch**; drafts are **inventory for review** only.

**Files created:**

- `main/content/en/pages/corpus-methodology.md`
- `main/content/en/pages/internal-linking-discipline.md`
- `main/content/en/pages/quality-gate.md`
- `main/content/de/pages/corpus-map.md`
- `main/content/de/pages/translator-playbook.md`
- `main/data/BATCH_1A_NON_PUBLIC_DRAFT_CREATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5E entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, templates, root `README.md`, package files, workflows, generated output, market_claims.json, safety_claims.json, science_claims.json, industry_claims.json, acquisition_claims.json. **Pre-existing** content draft pages (every file other than the five new Batch 1A targets above) — **not modified**.

---

### 2026-05-22 — Batch 1A Source and Claim Boundaries Reviewed

**Decision:** Record a **report-only** governance review of the five Batch **1A** non-public methodology drafts against source policy, claim boundaries, German authority constraints, internal-link readiness, and publication blockers—**without** mutating content, routes, or registries.

**Summary:** Sprint **5F** reviewed `corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, and `de_method_translator_playbook` for source requirements, claim boundaries, German terminology authority boundaries, internal-link readiness, and publication blockers. **No** content pages were modified. **No** routes were published. **No** claims were approved. **No** registries were modified. **`[SOURCE REQUIRED]`** markers remain in place.

**Rationale:** Batch **1A** drafts are review inventory; explicit boundary mapping prevents premature publication, marker stripping, or linking batches that assume public eligibility.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`.

**Sprint 5F validation (observed where applicable):**

- `main/data/BATCH_1A_SOURCE_CLAIM_BOUNDARY_REVIEW.md` exists and documents reviewed files, per-page assessments, German boundary review, blocker matrix, and **not ready for publication** conclusion.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- **No** `main/content/**` files modified; **no** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true` introduced.
- **No** generated HTML, dependencies, workflows, package files, deployment configs, or Cloudflare configs created.
- Root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication**; **not** public launch.

**Files created:**

- `main/data/BATCH_1A_SOURCE_CLAIM_BOUNDARY_REVIEW.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5F entry appended.

**Not modified in this sprint:** All content pages, `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, templates, root `README.md`, package files, workflows, generated output.

---

### 2026-05-27 — Batch 1B Existing Planned Route Drafts Created

**Decision:** Create the next controlled batch of **non-public draft pages** from **existing planned routes** in `routes.json`—increasing real corpus inventory without publishing routes, modifying route state, or mutating governance registries.

**Summary:** Sprint **5G** created non-public drafts for `what_is_sulfur`, `disulfide_bonds`, and `protein_disulfide_structure`—the full set of **safe eligible** planned routes whose `content_file` paths did not yet exist. **Eight** other missing routes were skipped (safety, industrial/procurement, substance operations, utility). **No** routes were published. **No** claims were approved. **No** registries were modified. **`[SOURCE REQUIRED]`** markers remain in all created and pre-existing drafts.

**Rationale:** Move Bisulfid.com from planning into **controlled corpus production** while preserving sovereign-grade discipline. Only **3** of **11** missing registered routes met low-risk eligibility; target range 8–12 could not be met without adding new routes (out of scope) or drafting high-risk pages (forbidden).

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `doctrine/QUALITY_GATE.md`, `doctrine/PROJECT_DOCTRINE.md`.

**Sprint 5G validation (observed where applicable):**

- All selected `route_id` values pre-existed in `routes.json`; **no** new route records added.
- Every created `content_file` matches the exact path in `routes.json`; **no** existing file overwritten.
- Every created draft has matching frontmatter: `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`.
- Every created draft states non-public / not publication-ready posture; includes **`[SOURCE REQUIRED]`** where factual support is pending.
- **No** draft claims source-locking complete; **no** draft approves or implies claim approval; **no** raw URLs or markdown links assuming publication.
- **No** market, safety handling, medical, procurement, production, trade, CAGR, market-share, or acquisition-target content in created drafts.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML, dependencies, workflows, or root `README.md` changes.
- `main/data/BATCH_1B_EXISTING_ROUTE_DRAFT_CREATION_REPORT.md` created; `DECISION_LOG.md` updated.

**Publication readiness:** **Not ready for publication**; **not** public launch.

**Draft-backed route count:** **18** of **26** registered routes now have draft bodies (**3** created this sprint).

**Files created:**

- `main/content/en/pages/what-is-sulfur.md`
- `main/content/en/pages/disulfide-bonds.md`
- `main/content/en/pages/protein-disulfide-structure.md`
- `main/data/BATCH_1B_EXISTING_ROUTE_DRAFT_CREATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5G entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, templates, root `README.md`, package files, workflows, generated output, **pre-existing** content draft pages (every file other than the three Batch 1B targets above).

---

### 2026-05-27 — Five Hundred Page Sovereign Launch Program Established

**Decision:** Upgrade Bisulfid.com’s **minimum public launch threshold** from **300** to **500 governed reference pages** and establish the strategic production program, expansion model, blueprint expansion, and wave-based production architecture required to reach that threshold—**without** publishing routes, creating content, or modifying registries.

**Summary:** Sprint **5H** revised `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_EXPANSION_MODEL.md`, and `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` to reflect the **500-page minimum** first public launch cohort (300 is no longer the launch threshold). Created `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md` and `CORPUS_PRODUCTION_WAVE_MODEL.md`. Blueprint expansion adds **193** concepts to the original **307** for **500** total proposed reference pages. **No** routes were published. **No** content pages were created or modified. **No** claims were approved. **No** registries were modified.

**Rationale:** The owner judged **300 pages insufficient** for a sovereign-grade first public surface. **500** is the new **floor** (not the ceiling); long-term ambition remains **1,000+** and **3,000+** pages under strict governance. Small batch sprints proved discipline; **wave-based production** is now required to reach launch scale without thin pages, translation spam, or fake readiness.

**Doctrine reference:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`.

**Sprint 5H validation (observed where applicable):**

- `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md` and `CORPUS_PRODUCTION_WAVE_MODEL.md` exist with layer allocation, audience map, wave sizes, production sequence, and rejected shortcuts.
- `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md` states **500 pages** as minimum public launch threshold; **300** superseded.
- `CORPUS_LAUNCH_THRESHOLD.md` defines **500** governed pages as minimum cohort with full launch gates (metadata, links, SEO, technical/security, no markers, no thin pages).
- `CORPUS_EXPANSION_MODEL.md` defines horizons: **500** launch, **1,000+** authority, **3,000+** multilingual, optional **5,000+**.
- `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` acknowledges **307 insufficient**; expansion register totals **500** proposed concepts.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- **No** content pages created or modified; **no** `[SOURCE REQUIRED]` markers removed.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML, dependencies, workflows, or root `README.md` changes.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication**; **not** public launch. **No publication before 500-page threshold.**

**Files created:**

- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `main/data/CORPUS_PRODUCTION_WAVE_MODEL.md`

**Files updated:**

- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/CORPUS_EXPANSION_MODEL.md`
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`
- `DECISION_LOG.md` — Sprint 5H entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, templates, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Corpus Automation Control Layer Established

**Decision:** Establish the **governed automation control layer** for Bisulfid.com’s **500-page sovereign reference corpus program**—defining how future automation may support wave production without publishing routes, approving claims, generating weak pages, or bypassing human governance.

**Summary:** Sprint **5I-A** created `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_MANIFEST.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, and `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`. The layer defines automation boundaries for route registration, draft production, source mapping, claim boundary review, internal-link wiring, SEO/metadata validation, and technical/pre-publication validation. **No** scripts, workflows, dependencies, routes, content pages, or registries were created or modified.

**Rationale:** Sprint **5H** established **500-page** wave production; scaling to 80–120 route waves and 40–60 draft waves requires **repeatable validation and manifest discipline** before tooling is implemented. Automation follows doctrine; human review remains mandatory at merge, sample audit, source/claim signoff, and launch authorization (S9).

**Doctrine reference:** `CORPUS_PRODUCTION_WAVE_MODEL.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `doctrine/QUALITY_GATE.md`, `doctrine/SOURCE_POLICY.md`.

**Sprint 5I-A validation (observed where applicable):**

- `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_MANIFEST.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, and `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md` exist with stage definitions, wave protocol, validation check IDs, and publication lock rules.
- **No** scripts created; **no** GitHub workflows created; **no** dependencies added.
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/ontology/sulfur_terms.json` — **not modified**.
- **No** content pages created or modified.
- No claim has `status: approved`; claim registries remain **inactive**.
- All routes remain `status: planned`; **no** `indexable: true` or `in_sitemap: true`.
- **No** generated HTML; root `README.md` **not modified**.
- `DECISION_LOG.md` updated with this entry.

**Publication readiness:** **Not ready for publication**; **not** public launch. **No publication before 500-page threshold.**

**Files created:**

- `main/data/CORPUS_AUTOMATION_CONTROL_LAYER.md`
- `main/data/CORPUS_AUTOMATION_MANIFEST.md`
- `main/data/CORPUS_AUTOMATION_WAVE_PROTOCOL.md`
- `main/data/CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5I-A entry appended.

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, templates, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output, scripts directories.

---

### 2026-05-27 — Route Registration Wave 1 Added

**Decision:** Register the **first large wave** of low-risk **planned** routes toward the **500-page sovereign launch threshold** and introduce a read-only **L0 route registry validator**.

**Summary:** Sprint **5I-B** added **100** new route records to `routes.json` (26 → **126** total). Created `scripts/validate_route_registry_l0.py`, `ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`, `ROUTE_REGISTRATION_WAVE_1_REPORT.md`, and `ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`. **No** content pages were created. **No** routes were published. All new routes remain `planned`, `indexable: false`, `in_sitemap: false`, `in_navigation: false`. **No** claims were approved. **No** internal links, source registries, claim registries, sitemap, navigation, generated HTML, dependencies, workflows, or root README files were modified.

**Rationale:** Sprint **5H** set the 500-page launch threshold; Sprint **5I-A** defined automation control and wave protocol. Route-scale production must begin with governed **registry-only** waves (80–120 routes) before draft production, preserving publication and claim locks.

**Doctrine reference:** `CORPUS_PRODUCTION_WAVE_MODEL.md`, `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `doctrine/QUALITY_GATE.md`.

**Sprint 5I-B validation:**

- `routes.json` remains valid JSON; **100** new route records added (target 80–120 met).
- Every new `route_id` was absent before this sprint; no duplicate `route_id` or `path`.
- Every new route: `status: planned`, `indexable: false`, `in_sitemap: false`, `in_navigation: false`.
- **No** content files created or modified; **no** generated HTML.
- `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- No claim `status: approved`; claim registries remain **inactive**.
- `scripts/validate_route_registry_l0.py` exists; L0 validation **PASS**.
- Manifest, report, and validation report artifacts exist.

**Publication readiness:** **Not ready for publication**. Registry expansion only. **374** routes remain to be registered toward the 500-page threshold.

**Recommended next sprint:** Draft production wave 1 (40–60 governed drafts for highest-priority newly registered routes) and/or route registration wave 2.

**Files created:**

- `scripts/validate_route_registry_l0.py`
- `main/data/ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`
- `main/data/ROUTE_REGISTRATION_WAVE_1_REPORT.md`
- `main/data/ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/routes.json` — 100 planned routes added (126 total).
- `DECISION_LOG.md` — Sprint 5I-B entry appended.

**Not modified in this sprint:** `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, templates, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Route Registration Wave 1 Report Corrected

**Decision:** Correct the Sprint **5I-B** route registration report so audit documentation explicitly records the `routes.json` modification and the intentional **30 English / 70 German** wave split.

**Summary:** This patch corrected `ROUTE_REGISTRATION_WAVE_1_REPORT.md` by explicitly stating that **`main/data/routes.json` was modified** in Sprint 5I-B to add **100** planned route records (26 → **126** total) and by documenting why the wave is **German-heavy**. Bisulfid.com’s strategic identity depends on **German lexical and terminology boundaries** while **English remains the global base layer** through EN terminology, disambiguation, governance, and index infrastructure routes. Arabic, Chinese, and Japanese routes remain deferred until EN/DE spine and hreflang/translation governance are stronger. **No** routes were changed. **No** content pages were created. **No** routes were published. **No** claims were approved. **No** registries, validator, generated output, dependencies, workflows, or root README files were modified.

**Rationale:** Post-merge verification (Sprint 5I-B) passed registry and governance checks but identified two documentation gaps: the report did not explicitly name `routes.json` as a modified artifact, and it did not explain the German-heavy language split. This patch closes those gaps without altering registry state.

**Sprint 5I-B report-correction validation:**

- Only `ROUTE_REGISTRATION_WAVE_1_REPORT.md` and `DECISION_LOG.md` changed.
- Report explicitly states `routes.json` was modified; **100** new planned records; count **26 → 126**.
- Report explains **30 EN / 70 DE** split and German-heavy strategic rationale; preserves EN as global base layer.
- Report does not imply `routes.json` was unmodified.
- `routes.json`, validator, manifest, validation report, content, registries — **not modified**.

**Files updated:**

- `main/data/ROUTE_REGISTRATION_WAVE_1_REPORT.md` — registry modification statement and German-heavy rationale added.
- `DECISION_LOG.md` — corrective entry appended.

**Not modified in this patch:** `main/data/routes.json`, `scripts/validate_route_registry_l0.py`, `main/data/ROUTE_REGISTRATION_WAVE_1_MANIFEST.md`, `main/data/ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all `main/content/**` pages, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Draft Production Wave 1 Created

**Decision:** Create the **first large wave** of **non-public draft pages** for selected low-risk planned routes under the **500-page sovereign launch program** and automation control doctrine.

**Summary:** Sprint **5J** created **50** non-public Markdown drafts at exact `routes.json` `content_file` paths (draft-backed routes: **18 → 68**). Created `scripts/validate_content_drafts_l0.py`, `DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`, `DRAFT_PRODUCTION_WAVE_1_REPORT.md`, and `CONTENT_DRAFTS_L0_VALIDATION_REPORT.md`. **No** routes were published. **`routes.json` was not modified.** All created drafts remain `non_public`, non-indexable, out of sitemap, and not publication-ready. **No** claims were approved. **No** internal links, source registries, claim registries, sitemap, navigation, generated HTML, dependencies, workflows, or root README files were modified.

**Rationale:** Sprint **5I-B** registered 100 new routes; Sprint **5I-A** defines draft production as stage S2 (40–60 drafts per wave). Controlled draft bodies must precede publication, source-locking, and claim approval.

**Doctrine reference:** `CORPUS_PRODUCTION_WAVE_MODEL.md`, `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`.

**Sprint 5J validation:**

- **50** non-public drafts created (target 40–60 met).
- Every draft matches an existing `route_id` and exact `content_file` path; **no overwrites**.
- Required frontmatter, non-public notices, and `[SOURCE REQUIRED]` markers present.
- No raw URLs or markdown links to unpublished routes.
- `routes.json`, registries, and pre-existing draft pages (except new wave targets) governance posture unchanged.
- L0 content validation **PASS**.
- All routes remain `planned`; no claim approved; registries inactive.

**Publication readiness:** **Not ready for publication**. Draft review and source/claim work required.

**Recommended next sprint:** Draft production wave 2 (next 40–60 drafts) or route registration wave 2.

**Files created:**

- **50** draft Markdown files under `main/content/en/pages/` and `main/content/de/pages/`
- `scripts/validate_content_drafts_l0.py`
- `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`
- `main/data/DRAFT_PRODUCTION_WAVE_1_REPORT.md`
- `main/data/CONTENT_DRAFTS_L0_VALIDATION_REPORT.md`

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Corpus Automation Runtime Layer 1 Established

**Decision:** Establish the first **executable read-only automation runtime layer** (L1) for Bisulfid.com’s sovereign reference corpus validation.

**Summary:** Sprint **5K** added L1 validators for route registry integrity, draft content discipline, publication locks, claim locks, and internal reference discipline, plus a local orchestration runtime (`corpus_validation_runtime_l1.py`). Created automation documentation and validation reports. **No** routes, content pages, registries, workflows, dependencies, or public HTML were added or modified. **No** routes were published. **No** claims were approved. All routes remain `planned`; all claim registries remain **inactive**.

**Rationale:** After Sprint **5I-B** (126 routes) and Sprint **5J** (68 draft-backed pages), isolated L0 wave validators are insufficient for corpus-scale governance. L1 provides repeatable, stdlib-only, read-only validation toward the **500-page** launch threshold and later **1,000+** / **3,000+** expansion without lowering quality, trust, SEO, security, or governance control.

**Doctrine reference:** `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_MANIFEST.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`.

**Sprint 5K validation:**

- All new L1 scripts exist under `scripts/`; Python standard library only; read-only.
- `python scripts/corpus_validation_runtime_l1.py` — **PASS** (all L1 validators; L0 informational PASS).
- `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json` — **not modified**.
- **No** content pages created or modified; **no** generated HTML; root `README.md` **not modified**.
- **No** GitHub workflows created; **no** dependencies added.
- All **126** routes remain `status: planned`; **no** `indexable: true`, `in_sitemap: true`, or `in_navigation: true`.
- Claim registries remain **inactive**; **0** approved claims; **14** pending_review.
- L1 warnings documented for **18** legacy pre-5J drafts and **4** pre-existing safety-context route metadata keywords — **not auto-fixed**.
- `CORPUS_AUTOMATION_SCRIPT_REGISTRY.md`, `CORPUS_AUTOMATION_RUNTIME_LAYER_1_REPORT.md`, `CORPUS_L1_VALIDATION_REPORT.md`, and `CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md` exist.

**Publication readiness:** **Not ready for publication**. Validation infrastructure only. **374** routes remain to be registered toward the 500-page threshold; **58** routes lack drafts.

**Recommended next sprint:** Source and claim boundary review for Sprint 5J drafts (Sprint 5L), then draft production wave 2.

**Files created:**

- `scripts/corpus_validation_runtime_l1.py`
- `scripts/validate_corpus_routes_l1.py`
- `scripts/validate_corpus_drafts_l1.py`
- `scripts/validate_corpus_publication_lock_l1.py`
- `scripts/validate_corpus_claims_l1.py`
- `scripts/validate_corpus_references_l1.py`
- `main/data/CORPUS_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/CORPUS_AUTOMATION_RUNTIME_LAYER_1_REPORT.md`
- `main/data/CORPUS_L1_VALIDATION_REPORT.md`
- `main/data/CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5K entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, `scripts/validate_route_registry_l0.py`, `scripts/validate_content_drafts_l0.py`, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Draft Wave 1 Source and Claim Boundaries Reviewed

**Decision:** Review and classify source and claim boundaries for all **50** Sprint **5J** non-public drafts before the next large draft-production wave.

**Summary:** Sprint **5L** classified wave-1 drafts by source requirement level, claim-risk level, publication blockers, and readiness for future source-mapping and claim-boundary work. Created boundary review report and four supporting matrices/action documents. **No** content pages were modified. **No** routes were published. **No** claims were approved. **No** source entries, claim registries, route records, internal links, sitemap, navigation, generated HTML, dependencies, workflows, or root README files were modified. `[SOURCE REQUIRED]` markers remain in place.

**Rationale:** Sprint **5K** established L1 automation and recommended source/claim boundary review (5L) before draft wave 2. With **68** draft-backed routes and **50** new standardized drafts, unclassified source/claim debt would compound toward the **500-page** launch threshold.

**Doctrine reference:** `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_PRODUCTION_WAVE_MODEL.md`, `DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`, `CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md`.

**Sprint 5L validation:**

- **50/50** Sprint 5J drafts exist, match `routes.json`, remain `draft` / `non_public` / non-indexable.
- L1 runtime **PASS** (pre-flight).
- **0** drafts publication-ready; **12** ready for source-mapping cohort A; **3** blocked pending reframe.
- Matrices contain **50** rows each.
- `routes.json`, registries, content pages — **not modified**.
- No claim `status: approved`; registries remain **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Classification sprint only.

**Recommended next sprint:** Source mapping wave 1 (cohort A, 10–15 drafts) plus claim boundary registration report for medium-risk drafts.

**Files created:**

- `main/data/DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`
- `main/data/DRAFT_WAVE_1_SOURCE_REQUIREMENT_MATRIX.md`
- `main/data/DRAFT_WAVE_1_CLAIM_RISK_MATRIX.md`
- `main/data/DRAFT_WAVE_1_PUBLICATION_BLOCKER_MATRIX.md`
- `main/data/DRAFT_WAVE_1_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5L entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, L1/L0 validator scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Draft Wave 1 Source Mapping Wave 1 Completed

**Decision:** Complete the first **source-mapping wave** for the **12** lowest-risk Sprint **5J** drafts identified by Sprint **5L**, and prepare claim-boundary notes for **20** medium-risk drafts.

**Summary:** Sprint **5M** mapped source requirements, source category gaps, and claim posture for cohort-A drafts and produced medium-risk claim-boundary preparation for **20** drafts. **No** source entries were added. **No** claim registries, content pages, or route records were modified. **No** claims were approved. **No** routes were published. `[SOURCE REQUIRED]` markers remain in place.

**Rationale:** Sprint **5L** classified wave-1 drafts and recommended source mapping before draft wave 2. Mapping defines audit-grade plans for future source registration without falsely claiming source-lock completion.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`, `DRAFT_WAVE_1_NEXT_ACTIONS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`.

**Sprint 5M validation:**

- **12/12** cohort-A drafts mapped; **20/20** medium-risk drafts covered in claim-boundary prep.
- L1 runtime **PASS** (pre-flight).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed.
- **0** publication-ready drafts; **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Mapping and preparation sprint only.

**Recommended next sprint:** Source registration proposal wave 1 (4–6 drafts, report-only) and claim boundary registration report (20 medium-risk drafts).

**Files created:**

- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_WAVE_1_REPORT.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`
- `main/data/DRAFT_WAVE_1_SOURCE_CATEGORY_GAP_ANALYSIS.md`
- `main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5M entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Source Registration Proposal Wave 1 Completed

**Decision:** Prepare the first **source registration proposal wave** for **5** selected low-risk drafts from the Sprint **5M** source-mapped cohort.

**Summary:** Sprint **5N-A** prepared source registration proposals for **5** lowest-gap cohort-A drafts (`sulfur_element_term_record`, `de_core_biogenic_lang`, `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`). The sprint identified future source authority needs, source evidence requirements, source policy gaps, and registration risks without adding source entries, modifying `source_registry.json`, editing content pages, approving claims, modifying claim registries, publishing routes, or removing `[SOURCE REQUIRED]` markers. The output prepares a future source discovery or source registration sprint while preserving strict human governance.

**Rationale:** Sprint **5M** mapped **12** cohort-A drafts but forbade registry edits. Proposals define what future registration would require—evidence types, authority tiers, policy gaps, and rejection criteria—before any candidate source is treated as verified or any page advances toward publication.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `DRAFT_WAVE_1_SOURCE_MAPPING_WAVE_1_REPORT.md`, `DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`, `DRAFT_WAVE_1_SOURCE_MAPPING_NEXT_ACTIONS.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`.

**Sprint 5N-A validation:**

- **5/5** selected drafts from Sprint **5M** cohort-A; **7** cohort-A drafts deferred with documented rationale.
- **5/5** selected drafts exist, match `routes.json`, remain `draft` / `non_public` / non-indexable.
- L1 runtime **PASS** (pre-flight).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** generated HTML.
- **0** publication-ready drafts; **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Proposal sprint only.

**Recommended next sprint:** Sprint **5N-B** (claim boundary registration report, 20 medium-risk drafts) in parallel with Sprint **5N-C** (candidate source discovery for 5 proposed drafts).

**Files created:**

- `main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`
- `main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — Source and Claim Automation Guardrails Established

**Decision:** Establish specialized read-only automation guardrails for Bisulfid.com's source and claim governance layer before candidate source discovery or registry edits.

**Summary:** Sprint **5N-B** established specialized read-only automation guardrails for Bisulfid.com's source and claim governance layer. The sprint added validators for source registration proposals, source evidence requirements, claim-boundary preparation, source registry locks, and claim registry locks without adding sources, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, generating public output, adding dependencies, creating workflows, or removing `[SOURCE REQUIRED]` markers. The guardrail layer protects the future source registration process before the corpus advances toward public launch readiness.

**Rationale:** Sprint **5N-A** produced source registration proposals; Sprint **5M** mapped sources and prepared medium-risk claim boundaries. Before 5N-C candidate discovery or registry execution, automation must verify proposals and registries remain controlled, non-approved, and non-misleading. Sources are the trust root of the sovereign reference corpus.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`, `DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`, `CORPUS_AUTOMATION_SCRIPT_REGISTRY.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-B validation:**

- **6** guardrail scripts created; stdlib-only; read-only.
- Guardrail runtime **PASS** (2026-05-28).
- Corpus L1 runtime **PASS** (informational).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Automation sprint only.

**Recommended next sprint:** Sprint **5N-C** (candidate source discovery for 5 proposed drafts) with guardrail runtime as pre/post gate.

**Files created:**

- `scripts/source_claim_guardrail_runtime_l1.py`
- `scripts/validate_source_registration_proposals_l1.py`
- `scripts/validate_source_evidence_requirements_l1.py`
- `scripts/validate_claim_boundary_preparation_l1.py`
- `scripts/validate_source_registry_lock_l1.py`
- `scripts/validate_claim_registry_lock_l1.py`
- `main/data/SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-B entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, existing L0/L1 corpus validator scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — Candidate Source Discovery Wave 1 Completed

**Decision:** Create the first candidate source discovery layer for the **5** selected source-registration proposal drafts from Sprint **5N-A**.

**Summary:** Sprint **5N-C** created the first candidate source discovery layer for the five selected source-registration proposal drafts. The sprint classified candidate source families, authority requirements, rejection rules, and next actions without adding source entries, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, adding raw URLs, or inventing bibliographic details. Candidate sources remain discovery targets only and are not approved, source-locked, or publication-ready.

**Rationale:** Sprint **5N-A** proposals and Sprint **5N-B** guardrails established prerequisites. Discovery names **families and search targets** for human review before any registry execution — preserving the trust root without false source-lock progress.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`, `SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`, `SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-C validation:**

- **5/5** selected drafts covered in discovery matrices.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Discovery-planning sprint only.

**Recommended next sprint:** Sprint **5N-D** — human candidate source review wave 1 (name and evaluate candidates; still no registry edits unless execution sprint chartered).

**Files created:**

- `main/data/CANDIDATE_SOURCE_DISCOVERY_WAVE_1_REPORT.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_MATRIX_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_AUTHORITY_REQUIREMENTS_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_REJECTION_RULES_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_NEXT_ACTIONS_WAVE_1.md`
- `main/data/CANDIDATE_SOURCE_DISCOVERY_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-C entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — Human Candidate Source Review Wave 1 Completed

**Decision:** Complete human candidate source review documentation for the **5** candidate-source-discovery drafts from Sprint **5N-C**.

**Summary:** Sprint **5N-D** completed human candidate source review documentation for the five candidate-source-discovery drafts from Sprint **5N-C**. The sprint evaluated candidate source families, authority requirements, acceptance criteria, rejection decisions, and future registry actions without adding source entries, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, adding raw URLs, or inventing bibliographic details. Candidate sources remain unapproved and no page is source-locked or publication-ready.

**Rationale:** Sprint **5N-C** identified discovery families and search targets. Human review applies governance acceptance/rejection logic and documents verification gaps before any registry proposal or execution — preserving the trust root without false progress.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `CANDIDATE_SOURCE_DISCOVERY_WAVE_1_REPORT.md`, `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-D validation:**

- **5/5** selected drafts covered in human review matrix.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Human-review documentation sprint only.

**Recommended next sprint:** Sprint **5N-E** — external source verification wave 1 (`de_core_mos2`, `sulfur_element_term_record` priority).

**Files created:**

- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_WAVE_1_REPORT.md`
- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_MATRIX_WAVE_1.md`
- `main/data/HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`
- `main/data/HUMAN_SOURCE_REJECTION_DECISIONS_WAVE_1.md`
- `main/data/HUMAN_SOURCE_REVIEW_NEXT_ACTIONS_WAVE_1.md`
- `main/data/HUMAN_CANDIDATE_SOURCE_REVIEW_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-D entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-28 — External Source Verification Wave 1 Completed

**Decision:** Complete external source verification documentation for the **2** highest-priority human-reviewed candidate-source drafts from Sprint **5N-D**.

**Summary:** Sprint **5N-E** completed external source verification documentation for the two highest-priority human-reviewed candidate-source drafts, `de_core_mos2` and `sulfur_element_term_record`. The sprint classified external verification status, authority class, evidence posture, risks, and next actions without adding source entries, modifying `source_registry.json`, approving claims, modifying claim registries, editing content pages, publishing routes, adding raw URLs where not allowed, or inventing bibliographic details. Source verification remains non-approval, non-source-locking, and non-publication-ready.

**Rationale:** Sprint **5N-D** identified human review status and future registry actions but required external verification to close the naming gap. This sprint documents evidence families, authority requirements, and human verification needs before any source registry proposal or execution — preserving the trust root without fabrication.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `HUMAN_CANDIDATE_SOURCE_REVIEW_WAVE_1_REPORT.md`, `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-E validation:**

- **2/2** priority drafts covered in verification matrix.
- Route count **126** read from `routes.json` and documented.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. External verification documentation sprint only.

**Recommended next sprint:** Sprint **5N-F** — source registry proposal drafting wave 1 (maximum **1–3** drafts; prioritize `de_core_mos2` after human names DE lexicon candidate).

**Files created:**

- `main/data/EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_AUTHORITY_REVIEW_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/EXTERNAL_SOURCE_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-E entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Source Registry Proposal Readiness Wave 1 Completed

**Decision:** Complete source registry proposal readiness documentation for `de_core_mos2` and `sulfur_element_term_record` after external source verification.

**Summary:** Sprint **5N-F** completed source registry proposal readiness documentation for `de_core_mos2` and `sulfur_element_term_record` after external source verification. The sprint identified `de_core_mos2` as the only conditional proposal-readiness candidate and kept `sulfur_element_term_record` blocked until a scientific database candidate is named. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, `[SOURCE REQUIRED]` markers remain unresolved, and no page is source-locked or publication-ready.

**Rationale:** Sprint **5N-E** found conditional proposal path for `de_core_mos2` but **0** named verified candidates. Proposal readiness documents gates, criteria, and blockers before any proposal drafting or registry execution — preserving separation between readiness, drafting, execution, approval, and publication.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`, `HUMAN_SOURCE_ACCEPTANCE_CRITERIA_WAVE_1.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`.

**Sprint 5N-F validation:**

- **2/2** target drafts covered in readiness matrix.
- `de_core_mos2` — **only conditional** proposal-readiness candidate (`proposal_readiness_conditional`).
- `sulfur_element_term_record` — **blocked** (`needs_scientific_database_candidate_first`).
- Route count **126** read from `routes.json` and documented.
- Guardrail runtime **PASS** (pre- and post-sprint).
- Corpus L1 runtime **PASS** (pre- and post-sprint).
- `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `routes.json` — **not modified**.
- **No** content pages created or modified; **no** markers removed; **no** raw URLs; **no** invented bibliographic details.
- **0** approved claims; registries **inactive**.
- All **126** routes remain `planned`; no `indexable: true` or `in_sitemap: true`.

**Publication readiness:** **Not ready for publication**. Proposal-readiness documentation sprint only.

**Recommended next sprint:** Sprint **5N-G** — named source candidate intake wave 1 (`de_core_mos2`); parallel database candidate naming for `sulfur_element_term_record`.

**Files created:**

- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_BLOCKERS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-F entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Corpus Production Automation Layer 2 Established

**Decision:** Establish read-only Corpus Production Automation Layer 2 for sovereign-scale corpus growth planning and validation.

**Summary:** Sprint **5O-A** established a read-only Corpus Production Automation Layer 2 for sovereign-scale Bisulfid.com corpus growth. The sprint added dry-run production planning and validation scripts for production waves, internal link graph planning, SEO/indexation planning, multilingual expansion planning, and L2 runtime orchestration. It also documented wave controls, production gates, link graph discipline, SEO/indexation discipline, and multilingual production rules. No routes were added, no content pages were created, no sources were added, no claims were approved, no registries were modified, no routes were published, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Scaling toward **500** governed launch pages and beyond requires repeatable wave planning, gate enforcement, and merge-blocking validation — not ad hoc page generation. L2 complements L1 corpus automation and 5N-B source/claim guardrails without weakening authority.

**Doctrine reference:** `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_PRODUCTION_WAVE_MODEL.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`.

**Sprint 5O-A validation:**

- **6** L2 scripts created — stdlib-only, read-only/dry-run.
- L2 production runtime **PASS**; L1 corpus runtime **PASS**; guardrail runtime **PASS**.
- Route count **126**; draft-backed **68**; production can safely proceed: **no**.
- `routes.json`, registries, content pages — **not modified**.
- **0** approved claims; registries **inactive**; all routes `planned`, non-indexable.

**Publication readiness:** **Not ready for publication**. Automation architecture sprint only.

**Recommended next sprint:** Sprint **5O-B** — production dry-run wave planning; parallel **5N-G** named source candidate intake.

**Files created:**

- `scripts/corpus_production_planner_l2.py`
- `scripts/validate_production_wave_plan_l2.py`
- `scripts/validate_internal_link_graph_plan_l2.py`
- `scripts/validate_seo_indexation_plan_l2.py`
- `scripts/validate_multilingual_wave_plan_l2.py`
- `scripts/corpus_production_runtime_l2.py`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_LAYER_2_REPORT.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md`
- `main/data/CORPUS_PRODUCTION_GATE_MODEL.md`
- `main/data/CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md`
- `main/data/CORPUS_PRODUCTION_SEO_INDEXATION_MODEL.md`
- `main/data/CORPUS_PRODUCTION_MULTILINGUAL_MODEL.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5O-A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages (except no edits), root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output. Existing L1 automation scripts unchanged except additive L2 siblings.

---

### 2026-05-27 — Production Dry-Run Wave Planning Completed

**Decision:** Complete production dry-run wave planning for a future Route Registration Wave 2 without modifying `routes.json` or creating pages.

**Summary:** Sprint **5O-B** completed a dry-run production planning wave for a future Route Registration Wave 2 without modifying `routes.json` or creating pages. The sprint used the Corpus Production Automation Layer 2 to plan and evaluate a candidate route-registration wave under the 500-page sovereign launch threshold, source/claim gates, internal link graph discipline, SEO/indexation locks, multilingual governance, and anti-thin-content standards. **83** dry-run candidates were identified from the launch cohort blueprint (80–120 band; below preferred 100 because safely eligible EN/DE-first inventory is exhausted under current gates). No routes were added, no content pages were created, no sources were added, no claims were approved, no registries were modified, no routes were published, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5O-A** established L2 read-only production automation. Before Route Registration Wave 2 execution, L2 must be tested against a real planning cohort with manifest, matrix, risk review, and execution blockers — without registry side effects. Wave 1 left **58** missing drafts; registering 83 additional routes now would inflate content debt without source/claim clearance.

**Doctrine reference:** `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`, `CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md`, `CORPUS_PRODUCTION_GATE_MODEL.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `ROUTE_REGISTRATION_WAVE_1_REPORT.md`.

**Sprint 5O-B validation:**

- Dry-run candidates: **83** (all absent from `routes.json`).
- Language split: **72** `en`, **11** `de`; ar/zh/ja excluded.
- Candidate status: **74** `dry_run_candidate`, **9** `dry_run_candidate_needs_review`.
- Route count **126**; draft-backed **68**; missing drafts **58**.
- L2 production runtime **PASS**; L1 corpus runtime **PASS**; guardrail runtime **PASS**.
- Planner: publication/indexation/sitemap/navigation locks **LOCKED**; `production_can_safely_proceed: no`.
- `routes.json`, registries, content pages — **not modified**.
- **0** approved claims; registries **inactive**; all routes `planned`, non-indexable.

**Publication readiness:** **Not ready for publication**. Dry-run planning sprint only — Route Registration Wave 2 execution **not approved**.

**Recommended next sprint:** Sprint **5N-G** — named source candidate intake (`de_core_mos2`); parallel Draft Wave 1 backlog reduction. **Do not** execute Route Registration Wave 2 or Draft Wave 2 in the next sprint without explicit execution charter and cleared blockers.

**Files created:**

- `main/data/PRODUCTION_DRY_RUN_WAVE_PLANNING_REPORT.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_DRY_RUN_MANIFEST.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_CANDIDATE_MATRIX.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_RISK_REVIEW.md`
- `main/data/ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md`
- `main/data/PRODUCTION_DRY_RUN_VALIDATION_REPORT.md`
- `main/data/PRODUCTION_DRY_RUN_NEXT_ACTIONS.md`

**Files updated:**

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Named Source Candidate Intake Wave 1 Completed

**Decision:** Complete named source candidate intake documentation for `de_core_mos2` without registry or content modification.

**Summary:** Sprint **5N-G** completed named source candidate intake documentation for `de_core_mos2` while keeping `sulfur_element_term_record` on a separate database-candidate naming track. The sprint preserved the distinction between candidate intake, source approval, registry execution, claim approval, source-locking, and publication readiness. Initial repository-internal finding: **`named_candidate_absent`**. After external human review (patch): intake re-classified to **`named_candidate_requires_external_verification`** with four documented candidate targets — **Spektrum Lexikon der Chemie — Molybdän(IV)-sulfid** (primary DE lexicon), **PubChem — Molybdenum disulfide / CID 14823** (supporting database), **NIST Chemistry WebBook — molybdenum disulphide** (supporting technical data), **Chemie.de Lexikon — Molybdän(IV)-sulfid** (secondary DE support only). All candidates **unapproved**. Registry proposal drafting **blocked until human verification**; registry execution **blocked** (separate sprint). No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-F** made `de_core_mos2` the only conditional proposal-readiness candidate but recorded **named source candidate present: no**. Intake must confirm naming before proposal drafting — without inventing bibliographic details or treating evidence families as named candidates.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`, `EXTERNAL_SOURCE_VERIFICATION_WAVE_1_REPORT.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`.

**Sprint 5N-G validation:**

- Intake target: **`de_core_mos2`** — **`named_candidate_requires_external_verification`** (post-patch; originally **`named_candidate_absent`** repository-internal).
- Named candidate targets documented: **4** (Spektrum primary; PubChem/NIST supporting; Chemie.de secondary) — all **unapproved**.
- `sulfur_element_term_record` — **not advanced**; database-candidate track unchanged.
- Route count **126**; draft-backed **68**; missing drafts **58**.
- L2 production runtime **PASS**; L1 corpus runtime **PASS**; guardrail runtime **PASS**.
- Planner: all locks **LOCKED**; `production_can_safely_proceed: no`.
- `source_registry.json`, `terminology_claims.json`, content — **not modified**.
- **0** approved claims; registries **inactive**; all routes `planned`, non-indexable.

**Publication readiness:** **Not ready for publication**. Named-source-intake documentation sprint only — registry execution **not allowed**.

**Recommended next sprint:** **Human external verification** of documented MoS2 named candidates (`de_core_mos2`). **Do not** proceed to source registry proposal drafting (5N-H) until verification completes; registry editing remains blocked. Parallel: `sulfur_element_term_record` database candidate naming; Draft Wave 1 backlog reduction.

**Files created:**

- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_WAVE_1_REPORT.md`
- `main/data/NAMED_SOURCE_CANDIDATE_INTAKE_MATRIX_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_NEXT_ACTIONS_WAVE_1.md`
- `main/data/NAMED_SOURCE_CANDIDATE_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-G entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, root `README.md`, package files, workflows, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — GitHub Actions Governance Workflow Layer Established

**Decision:** Establish read-only GitHub Actions governance CI for merge-time corpus validation.

**Summary:** Sprint **5P-A** established the first GitHub Actions governance workflow layer for Bisulfid.com. The sprint added a read-only Corpus Governance CI workflow that runs existing L1, source/claim guardrail, and L2 production validation scripts on pull requests and manual dispatch. The workflow is governance-only, not deployment automation. It does not publish routes, generate HTML, approve claims, register sources, modify registries, create content pages, use secrets, deploy to GitHub Pages, or integrate Cloudflare. No routes were added, no content pages were created, no sources were added, no claims were approved, no public output was generated, and all publication/indexation locks remain active.

**Rationale:** Scaling toward **500** governed pages requires merge-blocking validation beyond local runs. L1 (**5K**), guardrails (**5N-B**), and L2 (**5O-A**) runtimes must enforce the same discipline on every PR to `main` before deployment or generation automation is considered.

**Doctrine reference:** `CORPUS_PRODUCTION_AUTOMATION_LAYER_2_REPORT.md`, `SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`, `CORPUS_LAUNCH_THRESHOLD.md`, `GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md`.

**Sprint 5P-A validation:**

- Workflow: `.github/workflows/corpus-governance-ci.yml` — **Corpus Governance CI**.
- Triggers: `pull_request` → `main`, `workflow_dispatch` only.
- Permissions: `contents: read`; no secrets; no deploy; no artifacts; no package install.
- Scripts: L1 runtime, guardrail runtime, L2 runtime, L2 planner, L0 route registry, L0 content drafts.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README — **not modified**.

**Publication readiness:** **Not ready for publication**. Governance CI sprint only — no deployment.

**Recommended next sprint:** **5N-H prep** — human external verification for `de_core_mos2` named candidates; enable branch protection for Corpus Governance CI.

**Files created:**

- `.github/workflows/corpus-governance-ci.yml`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_SECURITY_MODEL.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_VALIDATION_REPORT.md`
- `main/data/GITHUB_ACTIONS_GOVERNANCE_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5P-A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, existing automation scripts, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Named Candidate Human Verification Wave 1 Completed

**Decision:** Complete human verification documentation for `de_core_mos2` named candidate sources without registry, claim, or content execution.

**Summary:** Sprint **5N-H** completed human verification documentation for `de_core_mos2` named candidate sources. Spektrum was reviewed as the primary German specialist lexicon candidate (`primary_candidate_verified_for_later_proposal`), while PubChem and NIST were kept as supporting database/technical candidates and Chemie.de was kept as secondary German-language support only. The sprint preserved the distinction between human verification, source approval, source registry execution, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-G** documented named candidate targets requiring external human verification. Controlled human verification must confirm authority role fit before source registry proposal drafting — without treating verification as approval or registry execution.

**Doctrine reference:** `NAMED_SOURCE_CANDIDATE_ACCEPTANCE_RULES_WAVE_1.md`, `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`, `doctrine/SOURCE_POLICY.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-H validation:**

- Target: `de_core_mos2` — **1** draft verified.
- Spektrum: **`primary_candidate_verified_for_later_proposal`** — not approved.
- PubChem / NIST: supporting-only; **`rejected_as_primary_german_authority`**.
- Chemie.de: **`secondary_german_support_only`**; **`not_primary_authority`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Human verification sprint only — no source-locking.

**Recommended next sprint:** **5N-I prep** — source registry proposal drafting for `de_core_mos2` with human-verified Spektrum bibliographic lines; still no registry execution.

**Files created:**

- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md`
- `main/data/SUPPORTING_CANDIDATE_BOUNDARY_REVIEW_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/NAMED_CANDIDATE_HUMAN_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-H entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Source Registry Proposal Draft Wave 1 Completed

**Decision:** Complete source registry proposal drafting documentation for `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-I** completed source registry proposal drafting documentation for `de_core_mos2`. Spektrum was drafted as the primary German specialist lexicon proposal candidate for later source registry review, while PubChem and NIST remain supporting database/technical candidates and Chemie.de remains secondary German-language support only. The sprint preserved the distinction between proposal drafting, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-H** verified Spektrum as **`primary_candidate_verified_for_later_proposal`**. Structured proposal drafting must precede registry execution so human reviewers can assess intended registry role, claim boundaries, and supporting-only discipline before any `source_registry.json` modification.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_PROPOSAL_DRAFTING_CRITERIA_WAVE_1.md`, `NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-I validation:**

- Target: `de_core_mos2` — **1** draft proposal.
- Spektrum: **`proposal_draft_primary_candidate`** — not approved; execution **not allowed now**.
- PubChem / NIST: supporting-only proposal boundaries.
- Chemie.de: secondary-only proposal boundary.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Proposal drafting sprint only — no source-locking.

**Recommended next sprint:** **5N-J prep** — source registry execution review with human-verified Spektrum bibliographic fields; still requires separate execution charter.

**Files created:**

- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFT_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`
- `main/data/SUPPORTING_SOURCE_BOUNDARY_PROPOSAL_DRAFT_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_DRAFT_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-I entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Source Registry Execution Readiness Wave 1 Completed

**Decision:** Complete source registry execution readiness documentation for `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-J** completed source registry execution readiness documentation for `de_core_mos2`. Spektrum was reviewed as the primary German specialist lexicon source execution candidate for a future `source_registry.json` entry, while PubChem, NIST, and Chemie.de remain bounded supporting candidates. The sprint preserved the distinction between execution readiness, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-I** drafted Spektrum as **`proposal_draft_primary_candidate`**. Execution readiness must confirm verified vs unverified registry fields before any `source_registry.json` modification — without treating readiness as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`, `SOURCE_REGISTRY_PROPOSAL_EXECUTION_BLOCKERS_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-J validation:**

- Target: `de_core_mos2` — **1** draft readiness review.
- Spektrum: **`execution_readiness_candidate`**, **`execution_blocked_pending_field_verification`**, **`execution_not_allowed_now`** — not approved.
- PubChem / NIST / Chemie.de: **`supporting_boundary_retained`**, **`not_primary_registry_source_now`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Execution readiness sprint only — no source-locking.

**Recommended next sprint:** **5N-K prep** — human bibliographic field verification for Spektrum; then separate execution sprint if readiness clears.

**Files created:**

- `main/data/SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_READINESS_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_EXECUTION_READINESS_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_ENTRY_FIELD_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_RISK_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_EXECUTION_READINESS_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-J entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Spektrum Bibliographic Field Verification Wave 1 Completed

**Decision:** Complete bibliographic field verification documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-K** completed bibliographic field verification documentation for the Spektrum candidate associated with `de_core_mos2`. The sprint identified which governance/source fields are verified for a future registry proposal and which bibliographic fields remain unverified, must stay blank, or require direct source access. The sprint preserved the distinction between bibliographic verification, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-J** classified Spektrum as **`execution_blocked_pending_field_verification`**. Bibliographic field verification must confirm verified vs unverified registry fields at bibliographic granularity before any `source_registry.json` modification — without treating verification as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_EXECUTION_READINESS_WAVE_1_REPORT.md`, `SPEKTRUM_EXECUTION_READINESS_REVIEW_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-K validation:**

- Target: `de_core_mos2` — **1** draft field verification.
- Spektrum: **7** governance fields **verified**; **6** bibliographic fields **unverified** — **`execution_blocked_pending_direct_source_access`**, **`execution_not_allowed_now`** — not approved.
- PubChem / NIST / Chemie.de: **`supporting_boundary_retained`**, **`not_primary_registry_source_now`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Bibliographic verification sprint only — no source-locking.

**Recommended next sprint:** **5N-L prep** — direct source access bibliographic capture for Spektrum; then separate execution sprint if readiness clears.

**Files created:**

- `main/data/SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_FIELD_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_FIELD_EVIDENCE_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_VERIFICATION_RISK_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_VERIFICATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-K entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Spektrum Direct Source Access Bibliographic Capture Wave 1 Completed

**Decision:** Complete direct source access bibliographic capture documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-L** completed direct source access bibliographic capture documentation for the Spektrum candidate associated with `de_core_mos2`. The sprint documented which bibliographic fields were captured through direct source access, which fields remain unavailable or require additional access, and which fields must stay blank rather than be invented. Direct access was **`direct_access_not_available`** in repository artifacts — **0** bibliographic fields captured; **6** remain blank. The sprint preserved the distinction between direct source capture, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-K** classified Spektrum as **`execution_blocked_pending_direct_source_access`**. Direct source access capture must document verified bibliographic values from direct inspection before any `source_registry.json` modification — without treating capture as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`, `SOURCE_REGISTRY_FIELD_GAP_REVIEW_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-L validation:**

- Target: `de_core_mos2` — **1** draft direct access capture review.
- Spektrum: **`direct_access_not_available`** in repository; **0** bibliographic fields captured; **6** remain blank — **`execution_still_blocked`**, **`execution_not_allowed_now`** — not approved.
- **7** governance fields carry forward verified from 5N-K.
- PubChem / NIST / Chemie.de: **`supporting_boundary_retained`**, **`not_primary_registry_source_now`**.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Direct source access capture sprint only — no source-locking.

**Recommended next sprint:** **5N-M prep** — verified bibliographic artifact capture with human sign-off for Spektrum; then separate execution sprint if readiness clears.

**Files created:**

- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_CAPTURE_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_FIELD_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_EVIDENCE_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_CAPTURED_FIELD_GAP_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_RISK_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SPEKTRUM_DIRECT_SOURCE_ACCESS_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-L entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-29 — Spektrum Verified Bibliographic Artifact Intake Wave 1 Completed

**Decision:** Establish governed bibliographic artifact intake documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-M** completed verified bibliographic artifact intake documentation for the Spektrum candidate associated with `de_core_mos2`. The sprint defined required human-provided evidence, intake field matrix, source artifact deposit protocol, and human sign-off checklist. No verified artifact bundle is present in repository — **0** intake fields deposited; **10** required fields missing or awaiting human confirmation. The sprint preserved the distinction between artifact intake, source registry execution, source approval, claim approval, source-locking, and publication readiness. No source entries were added, `source_registry.json` was not modified, no claims were approved, claim registries were not modified, content pages were not edited, routes were not published, no routes were added, no generated HTML was created, no dependencies or workflows were added, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-L** documented **`direct_access_not_available`** with **0** bibliographic fields captured. A governed intake layer must define exact evidence requirements before any `source_registry.json` modification — without treating intake as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_DIRECT_SOURCE_ACCESS_CAPTURE_WAVE_1_REPORT.md`, `SPEKTRUM_BIBLIOGRAPHIC_FIELD_VERIFICATION_WAVE_1_REPORT.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-M validation:**

- Target: `de_core_mos2` — **1** artifact intake layer.
- Spektrum: artifact bundle **absent**; **0** intake fields present — **`execution_still_blocked`**, **`execution_not_allowed_now`**, **`source_approval_not_allowed_now`** — not approved.
- **7** governance fields carry forward verified from 5N-K.
- Local runtimes **PASS**; route count **126**; draft-backed **68**; missing drafts **58**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Artifact intake sprint only — no source-locking.

**Recommended next step:** Human artifact deposit + sign-off per deposit protocol; then separate registry execution sprint if readiness clears.

**Files created:**

- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_FIELD_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_ARTIFACT_DEPOSIT_PROTOCOL_WAVE_1.md`
- `main/data/SPEKTRUM_BIBLIOGRAPHIC_HUMAN_SIGNOFF_CHECKLIST_WAVE_1.md`
- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_RISK_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-M entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Human Bibliographic Artifact Review Wave 1 Completed

**Decision:** Complete human bibliographic artifact review documentation for the Spektrum candidate associated with `de_core_mos2` without registry execution, source approval, or content modification.

**Summary:** Sprint **5N-N** completed human bibliographic artifact review for the Spektrum candidate associated with `de_core_mos2`. The repository owner supplied a direct-access bibliographic receipt from the live Spektrum Lexikon der Chemie page. The sprint classified **8** fields as **`verified_from_human_artifact`**, **2** fields as **`not_visible_from_source`** (`publication_date`, `edition_or_version` — remain blank), and copyright 1998 as **`visible_but_policy_sensitive`** rights evidence only — **not** `publication_date`. Posture upgraded to **`execution_candidate_after_artifact_review`**. Preserved: **`source_registry_execution_not_allowed_now`**, **`source_approval_not_allowed_now`**, **`claim_approval_not_allowed_now`**, **`production_can_safely_proceed: no`**. No source entries added, `source_registry.json` was not modified, no claims were approved, content pages were not edited, routes were not published, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-M** defined artifact intake requirements but recorded no human bundle. Human artifact review must evaluate the repository-owner receipt before chartering a separate execution sprint — without treating review as execution or approval.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_VERIFIED_BIBLIOGRAPHIC_ARTIFACT_INTAKE_WAVE_1_REPORT.md`, `SPEKTRUM_SOURCE_ARTIFACT_DEPOSIT_PROTOCOL_WAVE_1.md`, `GITHUB_ACTIONS_GOVERNANCE_WORKFLOW_REPORT.md`.

**Sprint 5N-N validation:**

- Target: `de_core_mos2` — **1** human artifact review.
- Human receipt: **8** verified; **2** blank; copyright 1998 rights-only.
- Posture: **`execution_candidate_after_artifact_review`** — execution charter **may proceed**; execution **not allowed now**.
- Local runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Registries, content, packages, README, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Human artifact review sprint only — no source-locking.

**Recommended next sprint:** **5N-O prep** — source registry execution charter for `SRC-SPEKTRUM-MOS2-DE` using human-reviewed receipt; blank `publication_date`; documented `access_date` 2026-05-30.

**Files created:**

- `main/data/SPEKTRUM_HUMAN_ARTIFACT_REVIEW_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_HUMAN_ARTIFACT_FIELD_CLASSIFICATION_WAVE_1.md`
- `main/data/SPEKTRUM_HUMAN_ARTIFACT_EXECUTION_CHARTER_REVIEW_WAVE_1.md`
- `main/data/SPEKTRUM_HUMAN_ARTIFACT_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-N entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `main/data/sources/source_registry.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Source Registry Execution Candidate Wave 1 Completed

**Decision:** Execute controlled source registry entry for `SRC-SPEKTRUM-MOS2-DE` associated with `de_core_mos2` without source approval, claim approval, or content modification.

**Summary:** Sprint **5N-O** completed controlled source registry execution for Spektrum on `de_core_mos2`. One schema-compliant row **`SRC-SPEKTRUM-MOS2-DE`** was added to `source_registry.json` using verified governance fields (5N-K) and human-reviewed bibliographic fields (5N-N). Entry posture: `status: seeded`, `source_lock_status: candidate`; registry file remains **`inactive`**. `publication_date` and `edition_or_version` omitted — not invented. Copyright 1998 documented as rights evidence only. The sprint preserved the distinction between registry execution, source approval, claim approval, source-locking, and publication readiness. `terminology_claims.json` was not modified, no claims were approved, content pages were not edited, routes were not published, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-N** concluded **`execution_candidate_after_artifact_review`**. Controlled registry execution inserts the governed row without granting `verified` status or approving claims.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_HUMAN_ARTIFACT_REVIEW_WAVE_1_REPORT.md`, `SPEKTRUM_HUMAN_ARTIFACT_FIELD_CLASSIFICATION_WAVE_1.md`.

**Sprint 5N-O validation:**

- Target: `de_core_mos2` — **1** registry execution.
- Added: **`SRC-SPEKTRUM-MOS2-DE`** — **15** total entries; **0** verified.
- Local runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Claims, content, routes, packages, README, workflows — **not modified** (except `source_registry.json`).

**Publication readiness:** **Not ready for publication**. Registry execution only — no source-locking.

**Recommended next step:** Claim boundary registration sprint; content source-lock audit sprint — separate charters.

**Files created:**

- `main/data/SPEKTRUM_SOURCE_REGISTRY_EXECUTION_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_SOURCE_REGISTRY_FIELD_MAPPING_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_REGISTRY_NO_CLAIM_APPROVAL_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_REGISTRY_EXECUTION_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/sources/source_registry.json` — **`SRC-SPEKTRUM-MOS2-DE`** row added.
- `DECISION_LOG.md` — Sprint 5N-O entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/claims/*.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Claim Boundary Registration Wave 1 Completed

**Decision:** Register narrow non-approved claim boundary for `de_core_mos2` tied to `SRC-SPEKTRUM-MOS2-DE` without claim approval, source verification, or content modification.

**Summary:** Sprint **5N-P** completed claim-boundary registration for Spektrum on `de_core_mos2`. One schema-compliant **`pending_review`** claim **`CLM-TERM-MOS2-DE-001`** was added to `terminology_claims.json`, linking **`SRC-SPEKTRUM-MOS2-DE`** to the German Lexikon der Chemie dictionary-entry terminology boundary only. Explicit exclusions: chemical safety, medical, market, production, procurement, pricing, trade, CAGR, industrial performance, and acquisition claims. The sprint preserved the distinction between claim-boundary registration, claim approval, source verification, source-locking, and publication readiness. `source_registry.json` was not modified; **`SRC-SPEKTRUM-MOS2-DE`** remains `status: seeded`, `source_lock_status: candidate`; registry file remains **`inactive`**. No claims were approved, content pages were not edited, routes were not published, and `[SOURCE REQUIRED]` markers remain unresolved.

**Rationale:** Sprint **5N-O** registered the Spektrum source row without claim linkage. Claim-boundary registration defines what the source may support in future review — without granting approval or resolving draft markers.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_SOURCE_REGISTRY_EXECUTION_WAVE_1_REPORT.md`, `SPEKTRUM_SOURCE_REGISTRY_NO_CLAIM_APPROVAL_WAVE_1.md`.

**Sprint 5N-P validation:**

- Target: `de_core_mos2` — **1** claim boundary registration.
- Added: **`CLM-TERM-MOS2-DE-001`** — **12** terminology claims; **0** approved.
- Local runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Source registry, content, routes, packages, README, workflows — **not modified** (except `terminology_claims.json`).

**Publication readiness:** **Not ready for publication**. Claim-boundary registration only — no source-locking.

**Recommended next step:** Source verification sprint; claim approval sprint; content source-lock audit sprint — separate charters.

**Files created:**

- `main/data/SPEKTRUM_CLAIM_BOUNDARY_REGISTRATION_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_SOURCE_TO_CLAIM_BOUNDARY_MAPPING_WAVE_1.md`
- `main/data/SPEKTRUM_CLAIM_BOUNDARY_NO_APPROVAL_NO_SOURCE_LOCK_WAVE_1.md`
- `main/data/SPEKTRUM_CLAIM_BOUNDARY_REGISTRATION_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/claims/terminology_claims.json` — **`CLM-TERM-MOS2-DE-001`** added.
- `DECISION_LOG.md` — Sprint 5N-P entry appended.

**Not modified in this sprint:** `main/data/sources/source_registry.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Source Verification Review Wave 1 Completed

**Decision:** Complete source verification review for `SRC-SPEKTRUM-MOS2-DE` on `de_core_mos2` without claim approval, source-locking, or content modification.

**Summary:** Sprint **5N-Q** reviewed whether human-reviewed bibliographic evidence (5N-N), registry execution (5N-O), and claim-boundary registration (5N-P) are sufficient to transition **`SRC-SPEKTRUM-MOS2-DE`** from **`seeded`** to **`verified`** per `doctrine/SOURCE_POLICY.md`. Policy assessment: evidence **sufficient** for narrow **`authoritative_dictionary`** / terminology boundary; access date **2026-05-30** satisfies publication/access date requirement; blank `publication_date` and `edition_or_version` remain omitted. Guardrail assessment: `validate_source_registry_lock_l1.py` **blocks** `status: verified` while registry file remains **`inactive`** — verified transition **deferred**. Registry row `notes` and `risk_notes` updated to document verification review; **`status` remains `seeded`**; **`source_lock_status` remains `candidate`**. No claims approved; `CLM-TERM-MOS2-DE-001` unchanged; `[SOURCE REQUIRED]` markers remain.

**Rationale:** Source verification review evaluates evidence and guardrail gates separately from claim approval and source-locking. Policy-sufficient evidence does not override inactive registry lock without a separate activation charter.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_HUMAN_ARTIFACT_FIELD_CLASSIFICATION_WAVE_1.md`, `SPEKTRUM_SOURCE_REGISTRY_EXECUTION_WAVE_1_REPORT.md`, `SPEKTRUM_CLAIM_BOUNDARY_REGISTRATION_WAVE_1_REPORT.md`.

**Sprint 5N-Q validation:**

- Target: `de_core_mos2` — **1** source verification review.
- Registry: **`SRC-SPEKTRUM-MOS2-DE`** — verification review documented; **0** verified sources.
- Local runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Claims, content, routes, packages, README, workflows — **not modified** (except registry row notes/risk_notes).

**Publication readiness:** **Not ready for publication**. Verification review only — no source-locking.

**Recommended next step:** Registry verified-status transition charter (guardrail policy review); claim approval sprint; content source-lock audit — separate charters.

**Files created:**

- `main/data/SPEKTRUM_SOURCE_VERIFICATION_REVIEW_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_SOURCE_VERIFICATION_FIELD_EVIDENCE_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_VERIFICATION_NO_CLAIM_APPROVAL_NO_SOURCE_LOCK_WAVE_1.md`
- `main/data/SPEKTRUM_SOURCE_VERIFICATION_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/sources/source_registry.json` — **`SRC-SPEKTRUM-MOS2-DE`** verification review documented in `notes` / `risk_notes`.
- `DECISION_LOG.md` — Sprint 5N-Q entry appended.

**Not modified in this sprint:** `main/data/claims/terminology_claims.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Source Registry Verification Lock Resolution Wave 1 Completed

**Decision:** Resolve source registry verification lock architecture for `SRC-SPEKTRUM-MOS2-DE` without claim approval, source-locking, or content modification.

**Summary:** Sprint **5N-R** resolved the Sprint **5N-B** dual lock that blocked individual source verification while the registry file remains **`inactive`**. Added **`verification_lock_resolution`** to `source_registry.json` documenting **`verification_limited`** posture: publication, claim, and route locks remain **LOCKED**; SOURCE_POLICY evidence for **`SRC-SPEKTRUM-MOS2-DE`** is **sufficient** (5N-Q); source listed in **`verification_ready_sources`**. Guardrail assessment: `validate_source_registry_lock_l1.py` **blocks** data-only `status: verified` transition — validator policy update deferred to separate charter per sprint constraints. **`SRC-SPEKTRUM-MOS2-DE`** **`status` remains `seeded`**; **`source_lock_status` remains `candidate`**; **0** verified sources. No claims approved; `CLM-TERM-MOS2-DE-001` unchanged; `[SOURCE REQUIRED]` markers remain.

**Rationale:** Lock resolution separates registry publication posture from individual source bibliographic verification. Policy-sufficient evidence and guardrail enforcement require distinct governance layers — resolved in data without weakening validators.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_SOURCE_VERIFICATION_REVIEW_WAVE_1_REPORT.md`, `scripts/validate_source_registry_lock_l1.py` (read-only review).

**Sprint 5N-R validation:**

- Target: registry verification lock — **1** resolution.
- Registry: **`verification_lock_resolution`** added; **1** verification-ready source documented; **0** verified rows.
- Validators: **not modified**; all runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Claims, content, routes, packages, README, workflows — **not modified** (except registry lock resolution metadata).

**Publication readiness:** **Not ready for publication**. Lock resolution only — no source-locking.

**Recommended next step:** Validator policy update charter to permit **`verified`** rows under **`verification_limited`** posture; then Spektrum verified status transition with guardrail **PASS**.

**Files created:**

- `main/data/SOURCE_REGISTRY_VERIFICATION_LOCK_RESOLUTION_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_VERIFIED_STATUS_TRANSITION_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_LOCK_NO_PUBLICATION_NO_SOURCE_LOCK_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_VERIFICATION_LOCK_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/sources/source_registry.json` — **`verification_lock_resolution`** added; Spektrum notes updated.
- `DECISION_LOG.md` — Sprint 5N-R entry appended.

**Not modified in this sprint:** `main/data/claims/terminology_claims.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Source Registry Guardrail Policy Update and Spektrum Verified Transition Wave 1 Completed

**Decision:** Update source registry guardrail for `verification_limited` bibliographic verification and transition `SRC-SPEKTRUM-MOS2-DE` to `verified` without claim approval, source-locking, or content modification.

**Summary:** Sprint **5N-S** updated **`validate_source_registry_lock_l1.py`** to distinguish bibliographic **`verified`** status from registry/publication activation while preserving **`inactive`** registry file posture and all publication locks. Guardrail permits **`verified`** only when `verification_lock_resolution.resolved_posture` is **`verification_limited`**, source is listed in **`verification_ready_sources`**, and **`source_lock_status`** remains **`candidate`**. **`SRC-SPEKTRUM-MOS2-DE`** transitioned from **`seeded`** to **`verified`**. Registry file remains **`inactive`**; **`source_lock_status`** remains **`candidate`**; **`CLM-TERM-MOS2-DE-001`** unchanged (**`pending_review`**); **0** approved claims; `[SOURCE REQUIRED]` markers remain.

**Rationale:** Sprint **5N-R** resolved lock architecture in data; Sprint **5N-S** implements guardrail policy to allow controlled bibliographic verification without weakening publication, claim, route, or source-lock gates.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SOURCE_REGISTRY_VERIFICATION_LOCK_RESOLUTION_WAVE_1_REPORT.md`, `SPEKTRUM_SOURCE_VERIFICATION_REVIEW_WAVE_1_REPORT.md`.

**Sprint 5N-S validation:**

- Target: guardrail policy + **1** verified transition.
- Bibliographic verified sources: **1**; registry file **`inactive`**; approved claims **0**.
- All runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Content, routes, claims, workflows, packages, README — **not modified** (except guardrail script and registry row).

**Publication readiness:** **Not ready for publication**. Bibliographic verification only — no source-locking.

**Recommended next step:** Claim approval sprint; content source-lock audit; marker resolution — separate charters.

**Files created:**

- `main/data/SOURCE_REGISTRY_GUARDRAIL_POLICY_UPDATE_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_VERIFIED_TRANSITION_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRY_VERIFICATION_LIMITED_NO_PUBLICATION_WAVE_1.md`
- `main/data/SOURCE_REGISTRY_GUARDRAIL_POLICY_UPDATE_VALIDATION_REPORT.md`

**Files updated:**

- `scripts/validate_source_registry_lock_l1.py` — `verification_limited` bibliographic verification policy.
- `main/data/sources/source_registry.json` — **`SRC-SPEKTRUM-MOS2-DE`** `status: verified`; lock resolution updated.
- `DECISION_LOG.md` — Sprint 5N-S entry appended.

**Not modified in this sprint:** `main/data/claims/terminology_claims.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Claim Approval Review Wave 1 Completed

**Decision:** Complete claim approval review for `CLM-TERM-MOS2-DE-001` on `de_core_mos2` without content source-locking, marker resolution, or route publication.

**Summary:** Sprint **5N-T** reviewed whether **`CLM-TERM-MOS2-DE-001`** may transition from **`pending_review`** to **`approved`** given bibliographic **`verified`** source **`SRC-SPEKTRUM-MOS2-DE`** (5N-S) and registered narrow terminology boundary (5N-P). Policy assessment: evidence **sufficient** for narrow German Lexikon der Chemie dictionary-entry approval only. Guardrail assessment: **`validate_claim_registry_lock_l1.py`** and **`validate_corpus_claims_l1.py`** **block** `status: approved` while claim registry file remains **`inactive`** — approved transition **deferred**. Added **`claim_approval_lock_resolution`** to `terminology_claims.json`; claim listed in **`approval_ready_claims`**. **`CLM-TERM-MOS2-DE-001`** remains **`pending_review`**; **0** approved claims; `[SOURCE REQUIRED]` markers remain.

**Rationale:** Claim approval review evaluates policy evidence and guardrail gates separately from content source-locking and publication. Policy-sufficient evidence does not override inactive claim registry lock without separate guardrail charter.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_CLAIM_BOUNDARY_REGISTRATION_WAVE_1_REPORT.md`, `SPEKTRUM_VERIFIED_TRANSITION_WAVE_1_REPORT.md`.

**Sprint 5N-T validation:**

- Target: `de_core_mos2` — **1** claim approval review.
- Claim: **`CLM-TERM-MOS2-DE-001`** — approval review documented; **0** approved claims.
- All runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Source registry, content, routes, workflows, packages, README — **not modified** (except `terminology_claims.json`).

**Publication readiness:** **Not ready for publication**. Claim approval review only — no source-locking.

**Recommended next step:** Claim guardrail policy update charter; then controlled **`approved`** transition with guardrail **PASS**.

**Files created:**

- `main/data/SPEKTRUM_CLAIM_APPROVAL_REVIEW_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_APPROVED_CLAIM_BOUNDARY_EVIDENCE_WAVE_1.md`
- `main/data/SPEKTRUM_CLAIM_APPROVAL_NO_SOURCE_LOCK_NO_PUBLICATION_WAVE_1.md`
- `main/data/SPEKTRUM_CLAIM_APPROVAL_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/claims/terminology_claims.json` — **`claim_approval_lock_resolution`** added; claim notes updated.
- `DECISION_LOG.md` — Sprint 5N-T entry appended.

**Not modified in this sprint:** `main/data/sources/source_registry.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-27 — Claim Guardrail Policy Update and Spektrum Approved Claim Transition Wave 1 Completed

**Decision:** Update claim guardrails for `approval_limited` narrow claim approval and transition `CLM-TERM-MOS2-DE-001` to `approved` without source-locking, marker resolution, or route publication.

**Summary:** Sprint **5N-U** updated **`validate_claim_registry_lock_l1.py`** and **`validate_corpus_claims_l1.py`** to distinguish **narrow individual claim approval** from **claim registry/publication activation** while preserving **`inactive`** claim registry file posture and all publication locks. Guardrail permits **`approved`** only when `claim_approval_lock_resolution.resolved_posture` is **`approval_limited`**, claim is listed in **`approval_ready_claims`**, linked source is **`verified`**, and **`source_lock_status`** remains **`candidate`**. **`CLM-TERM-MOS2-DE-001`** transitioned from **`pending_review`** to **`approved`**. Claim registry file remains **`inactive`**; **`SRC-SPEKTRUM-MOS2-DE`** remains **`verified`** with **`source_lock_status: candidate`**; **1** narrow approved claim; `[SOURCE REQUIRED]` markers remain.

**Rationale:** Sprint **5N-T** resolved approval evidence in data; Sprint **5N-U** implements guardrail policy to allow controlled narrow claim approval without weakening publication, route, source-lock, or production gates.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_CLAIM_APPROVAL_REVIEW_WAVE_1_REPORT.md`, `CLAIM_GUARDRAIL_POLICY_UPDATE_WAVE_1_REPORT.md`.

**Sprint 5N-U validation:**

- Target: guardrail policy + **1** approved claim transition.
- Narrow approved claims: **1**; claim registry file **`inactive`**; source **`candidate`** lock unchanged.
- All runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Content, routes, source registry, workflows, packages, README — **not modified** (except guardrail scripts and claim row).

**Publication readiness:** **Not ready for publication**. Narrow claim approval only — no source-locking.

**Recommended next step:** Content source-lock audit; marker resolution; route publication — separate charters.

**Files created:**

- `main/data/CLAIM_GUARDRAIL_POLICY_UPDATE_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_APPROVED_CLAIM_TRANSITION_WAVE_1_REPORT.md`
- `main/data/CLAIM_APPROVAL_LIMITED_NO_SOURCE_LOCK_NO_PUBLICATION_WAVE_1.md`
- `main/data/CLAIM_GUARDRAIL_POLICY_UPDATE_VALIDATION_REPORT.md`

**Files updated:**

- `scripts/validate_claim_registry_lock_l1.py` — `approval_limited` narrow claim approval policy.
- `scripts/validate_corpus_claims_l1.py` — `approval_limited` narrow claim approval policy.
- `main/data/claims/terminology_claims.json` — **`CLM-TERM-MOS2-DE-001`** `status: approved`; lock resolution updated.
- `DECISION_LOG.md` — Sprint 5N-U entry appended.

**Not modified in this sprint:** `main/data/sources/source_registry.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Spektrum Content Source-Lock Audit for de_core_mos2 Wave 1 Completed

**Decision:** Audit `de_core_mos2` draft content against `SRC-SPEKTRUM-MOS2-DE` and `CLM-TERM-MOS2-DE-001`; defer content source-locking with documented blockers.

**Summary:** Sprint **5N-V** read-only audited `main/content/de/pages/terminology/molybdenum-disulfide.md` against bibliographic **`verified`** source **`SRC-SPEKTRUM-MOS2-DE`** and narrow **`approved`** claim **`CLM-TERM-MOS2-DE-001`**. Structural page role and boundary exclusions align with the approved German Lexikon der Chemie dictionary-entry terminology boundary. Factual terminology lines remain **`[SOURCE REQUIRED]`** placeholders only; no MoS2 dictionary-entry content is present to lock. Content schema lacks governed partial source-lock metadata for DE Wave 1 drafts; body source/claim status section is stale relative to registry (states zero approved claims). **Content source-locking deferred** — not applied. **`[SOURCE REQUIRED]`** markers (**4**) remain; no content body rewrite; no route publication.

**Rationale:** Registry-layer verification and claim approval (5N-S, 5N-U) do not automatically authorize content-layer source-locking. Audit must distinguish supported governance framing from unsupported factual placeholders and schema/guardrail blockers before any lock annotation.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `SPEKTRUM_APPROVED_CLAIM_TRANSITION_WAVE_1_REPORT.md`, `SPEKTRUM_CONTENT_SOURCE_LOCK_AUDIT_WAVE_1_REPORT.md`.

**Sprint 5N-V validation:**

- Target: **`de_core_mos2`** — **1** content source-lock audit.
- Content source-lock applied: **No** — deferred.
- All runtimes **PASS**; route count **126**; all locks **LOCKED**; `production_can_safely_proceed: no`.
- Source registry, claims, routes, content, workflows, packages, README — **not modified** (audit documentation only).

**Publication readiness:** **Not ready for publication**. Content source-lock audit only — no source-locking, no marker resolution.

**Recommended next step:** Content schema partial-lock charter (if desired); marker-resolution sprint for narrow dictionary-entry terminology; registry source-lock sprint only after content alignment.

**Files created:**

- `main/data/SPEKTRUM_CONTENT_SOURCE_LOCK_AUDIT_WAVE_1_REPORT.md`
- `main/data/SPEKTRUM_CONTENT_BOUNDARY_MATRIX_WAVE_1.md`
- `main/data/SPEKTRUM_CONTENT_SOURCE_LOCK_NO_MARKER_REMOVAL_NO_PUBLICATION_WAVE_1.md`
- `main/data/SPEKTRUM_CONTENT_SOURCE_LOCK_AUDIT_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 5N-V entry appended.

**Not modified in this sprint:** `main/data/sources/source_registry.json`, `main/data/claims/terminology_claims.json`, `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `main/data/ontology/sulfur_terms.json`, all `main/content/**` pages, automation scripts, workflows, root `README.md`, package files, deployment configs, Cloudflare configs, generated output.

---

### 2026-05-30 — Sovereign 14,000-Page Corpus Production Architecture Codification Completed

**Decision:** Codify agreed strategic direction for sovereign-grade 14,000-page corpus production into operational repository files and machine-readable registries.

**Summary:** Sprint **6A** codified bisulfid.com as a visible, global, multilingual, sovereign-grade reference asset—not a thin glossary or hidden internal corpus. Created **`corpus_route_formula.json`** (8-dimensional route derivation), **`page_type_registry.json`** (19 page families including **`PT_DIFFERENCE_COMPARISON`** as core SEO class), **`audience_layer_registry.json`** (9 audiences), and **`corpus_production_rules.md`** (batch production rulebook). Target scale: **7 languages × 2,000 pages = 14,000** governed pages via dimensional intersection. Documented SEO/internal-link/security model, batch production transition (100–500 pages/day benchmarks), and phased execution **6B–6F**. **No routes published. No pages generated. No HTML created.** Validators unchanged.

**Rationale:** Sprints 5A–5N proved governance at small scale; batch-governed production requires codified execution primitives before inventory and generator sprints. Strategic direction was agreed—6A operationalizes it in repository doctrine.

**Doctrine reference:** `doctrine/SOURCE_POLICY.md`, `CORPUS_AUTOMATION_CONTROL_LAYER.md`, `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`, `corpus_production_rules.md`.

**Sprint 6A validation:**

- Target: architecture codification only.
- Registered routes: **126** (unchanged); publication **LOCKED**; `production_can_safely_proceed: no`.
- All L1/L2 runtimes **PASS**; no validator weakening.
- Routes, content, sources, claims, workflows, packages — **not modified**.

**Publication readiness:** **Not ready for publication**. Architecture codification only.

**Recommended next step:** Sprint **6B** — 14,000-route master inventory model (execution, not discussion).

**Files created:**

- `main/data/SOVEREIGN_CORPUS_ARCHITECTURE_CODIFICATION_REPORT.md`
- `main/data/SOVEREIGN_PAGE_FAMILY_TAXONOMY_WAVE_1.md`
- `main/data/SOVEREIGN_MULTILINGUAL_ROUTE_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_AUDIENCE_LAYER_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_SEO_INTERNAL_LINKING_SECURITY_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_BATCH_PRODUCTION_TRANSITION_PLAN_WAVE_1.md`
- `main/data/SOVEREIGN_CORPUS_ARCHITECTURE_CODIFICATION_VALIDATION_REPORT.md`
- `main/data/corpus_route_formula.json`
- `main/data/page_type_registry.json`
- `main/data/audience_layer_registry.json`
- `main/data/corpus_production_rules.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6A entry appended.

**Not modified in this sprint:** `main/data/routes.json`, all `main/content/**` pages, `main/data/sources/source_registry.json`, `main/data/claims/`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, automation scripts, workflows, root `README.md`, package files, deployment configs, generated output.

---

### 2026-05-30 — Sovereign 14,000-Route Master Inventory Model Completed

**Decision:** Create master route inventory model for 14,000+ governed multilingual routes with reference_layer dimension — without modifying production routes or generating content.

**Summary:** Sprint **6B** transformed 6A architecture into executable inventory model artifacts: **`SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json`** (row schema, route/indexation states, anti-fake rules), **`SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json`** (language × page_type × audience × reference_layer matrix), **`reference_layer_registry.json`** (9 reference layers — scope amendment), plus cohort, path pattern, and guardrail documentation. Extended route formula with **`reference_layer`** as ninth dimension. Defined 7 batch cohorts, 10 route states, 4 indexation states, 9 internal-link roles. Target scale **7 × 2,000 = 14,000** routes via dimensional intersection — not repetition. **`routes.json` unchanged** (126 routes); **`production_route_registry: false`** for all model rows; no inventory rows emitted to production.

**Rationale:** Batch-governed corpus production requires machine-readable inventory schema before generator (6C) and draft cohorts (6D). reference_layer prevents shallow duplication — each page exists for distinct field, evidence, and vocabulary posture.

**Doctrine reference:** `corpus_route_formula.json`, `page_type_registry.json`, `audience_layer_registry.json`, `corpus_production_rules.md`, `SOVEREIGN_14000_ROUTE_MASTER_INVENTORY_MODEL.md`.

**Sprint 6B validation:**

- Target: inventory model only — **0** production route changes.
- Registered routes: **126** (unchanged); `production_can_safely_proceed: no`.
- All L1/L2 runtimes **PASS**; validators not weakened.
- Routes, content, sources, claims, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Inventory modeling only.

**Recommended next step:** Sprint **6C** — schemas, templates, generator design.

**Files created:**

- `main/data/SOVEREIGN_14000_ROUTE_MASTER_INVENTORY_MODEL.md`
- `main/data/SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json`
- `main/data/SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json`
- `main/data/reference_layer_registry.json`
- `main/data/SOVEREIGN_ROUTE_COHORT_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_ROUTE_PATH_PATTERN_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_ROUTE_INVENTORY_NO_PUBLICATION_GUARDRAIL_WAVE_1.md`
- `main/data/SOVEREIGN_ROUTE_INVENTORY_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6B entry appended.

**Not modified in this sprint:** `main/data/routes.json`, all `main/content/**` pages, `main/data/sources/source_registry.json`, `main/data/claims/`, `corpus_route_formula.json`, `page_type_registry.json`, `audience_layer_registry.json`, `corpus_production_rules.md`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, automation scripts, workflows, root `README.md`, package files, deployment configs, generated output.

---

### 2026-05-30 — Sovereign Corpus Generator Schema and Template Requirements Completed

**Decision:** Design generator schema, template contracts, validation gates, and knowledge reliability layer for batch-governed corpus production — without generating pages or modifying production routes.

**Summary:** Sprint **6C** designed **`SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json`** (registry-constrained generator; no free-form LLM), **`SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json`** (6 template contracts with full SEO/reliability fields), validation gate model (G0–G8), batch automation design (100–500 pages/day), and reference-layer duplication guard. Scope amendment added **knowledge reliability layer**: **`SOVEREIGN_KNOWLEDGE_RELIABILITY_MODEL_WAVE_1.md`**, **`SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json`** (8 evidence grades), **`SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json`** (10 ranked source types), **`SOVEREIGN_KNOWLEDGE_RELIABILITY_VALIDATION_REQUIREMENTS_WAVE_1.md`** (KR-01–KR-15). Every future page requires knowledge_reliability_profile — not optional. **No pages generated. routes.json unchanged (126).**

**Rationale:** 6A/6B codified architecture and inventory model; 6C defines how automation produces validation-controlled drafts with maximum epistemic credibility — exposing evidence, claim boundaries, and unresolved areas.

**Doctrine reference:** `corpus_production_rules.md`, `SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json`, `reference_layer_registry.json`, `SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json`.

**Sprint 6C validation:**

- Target: generator schema design only — **0** pages, **0** content files.
- All L1/L2 runtimes **PASS**; validators not weakened.
- routes, content, sources, claims, workflows — **not modified**.

**Publication readiness:** **Not ready for publication**. Generator design only.

**Recommended next step:** Sprint **6D** — first large governed draft cohort under 6C schema.

**Files created:**

- `main/data/SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json`
- `main/data/SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json`
- `main/data/SOVEREIGN_GENERATOR_VALIDATION_GATE_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_BATCH_GENERATION_AUTOMATION_DESIGN_WAVE_1.md`
- `main/data/SOVEREIGN_GENERATOR_REFERENCE_LAYER_DUPLICATION_GUARD_WAVE_1.md`
- `main/data/SOVEREIGN_GENERATOR_NO_PUBLICATION_GUARDRAIL_WAVE_1.md`
- `main/data/SOVEREIGN_GENERATOR_SCHEMA_VALIDATION_REPORT.md`
- `main/data/SOVEREIGN_KNOWLEDGE_RELIABILITY_MODEL_WAVE_1.md`
- `main/data/SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json`
- `main/data/SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json`
- `main/data/SOVEREIGN_KNOWLEDGE_RELIABILITY_VALIDATION_REQUIREMENTS_WAVE_1.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6C entry appended.

**Not modified in this sprint:** `main/data/routes.json`, all `main/content/**` pages, `main/data/sources/source_registry.json`, `main/data/claims/`, 6A/6B registry files, automation scripts, workflows, root `README.md`, package files, deployment configs, generated output.

---

## Sprint 6D — Sovereign Content Automation Engine v1

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6d-sovereign-content-automation-engine-v1`  
**Base:** main @ Sprint 6C merge  
**Status:** Complete — engine v1, COHORT_01 drafts, dry-run manifest; no publication

**Summary:** Sprint **6D** implemented **Content Automation Engine v1** (`scripts/generate_sovereign_foundation_cohort_v1.py`) — registry-constrained, deterministic, stdlib-only draft generation with no LLM. Engine reads 6A–6C governed inputs and produces **COHORT_01_FOUNDATION_GOV** (15 English foundation units): dry-run manifest, draft blueprints, and non-public pre-route markdown under `main/content/en/pages/foundation/`. Each unit receives full metadata assignments (page_type, reference_layer, reliability profile, evidence grade, source/claim posture, indexation state, validation gates). **routes.json unchanged (126). No public routes. No public HTML. production_can_safely_proceed remains no.**

**Rationale:** Corpus architecture (6A), inventory model (6B), and generator schema (6C) enable controlled automation instead of manual page-by-page work. Engine v1 proves the pipeline on a small foundation cohort without publication activation.

**Doctrine reference:** `corpus_production_rules.md`, `SOVEREIGN_CORPUS_GENERATOR_SCHEMA_WAVE_1.json`, `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json`, `TPL_FOUNDATION_GOV_V1`, `SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json`.

**Sprint 6D validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- Engine: 15/15 units validated; `llm_used: false`; `routes_json_modified: false`
- Validators not weakened; sources/claims not modified

**Publication readiness:** **Not ready for publication**. Pre-route foundation drafts only.

**Recommended next step:** Review COHORT_01 drafts; separate charter for route registration merge if authorized.

**Files created:**

- `scripts/generate_sovereign_foundation_cohort_v1.py`
- `main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_REPORT.md`
- `main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRY_RUN_MANIFEST.json`
- `main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRAFT_BLUEPRINTS.json`
- `main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_VALIDATION_REPORT.md`
- `main/data/SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_NO_PUBLICATION_GUARDRAIL.md`
- `main/content/en/pages/foundation/*.md` (15 non-public draft files)

**Files updated:**

- `DECISION_LOG.md` — Sprint 6D entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `main/data/sources/source_registry.json`, `main/data/claims/`, 6A/6B/6C registry files, workflows, root `README.md`, package files, dependencies, deployment configs.

---

## Sprint 6E — Foundation Cohort Validation and Internal Link Graph

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6e-foundation-cohort-validation-link-graph`  
**Base:** main @ Sprint 6D merge (PR #67)  
**Status:** Complete — COHORT_01 validated; internal-link graph modeled; no publication

**Summary:** Sprint **6E** audited all **15** non-public COHORT_01 foundation drafts under `main/content/en/pages/foundation/`, confirmed zero fake-page/thin-page/forbidden-claim risk, verified reliability profile and noindex posture on every unit, and built the governed **internal-link graph** (hubs, spokes, required/optional/prohibited edges, orphan prevention, breadcrumbs). Documented **future route mapping** and **multilingual expansion readiness** without modifying `routes.json`. **No draft content changes required. No public routes. No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6D produced registry-constrained foundation drafts via Content Automation Engine v1; 6E validates quality and defines link topology before any route registration merge charter.

**Doctrine reference:** `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRY_RUN_MANIFEST.json`, `SOVEREIGN_CONTENT_AUTOMATION_ENGINE_V1_DRAFT_BLUEPRINTS.json`, `CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md`, `SOVEREIGN_SEO_INTERNAL_LINKING_SECURITY_MODEL_WAVE_1.md`.

**Sprint 6E validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- COHORT_01 audit: 15/15 pass; 0 draft modifications
- Internal-link graph: 0 orphans; no live links added
- Validators not weakened; sources/claims not modified

**Publication readiness:** **Not ready for publication**. Validation and graph modeling only.

**Recommended next step:** Sprint **6F** or route registration merge charter review if authorized.

**Files created:**

- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_QUALITY_MATRIX.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_INTERNAL_LINK_GRAPH.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_ROUTE_MAPPING_READINESS.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_MULTILINGUAL_EXPANSION_READINESS.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6E entry appended.

**Not modified in this sprint:** `main/data/routes.json`, COHORT_01 draft files, `main/data/sources/source_registry.json`, `main/data/claims/`, automation scripts, workflows, root `README.md`, package files, dependencies.

---

## Sprint 6F — COHORT_01 Foundation Route Registration Candidate

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6f-cohort-01-foundation-route-registration`  
**Base:** main @ Sprint 6E merge  
**Status:** Complete — 15 COHORT_01 routes registered; no publication

**Summary:** Sprint **6F** registered all **15** COHORT_01 foundation drafts in `routes.json` as **planned**, **draft-backed**, **non-public** routes (126 → **141**). Each route retains `indexable: false`, `in_sitemap: false`, `in_navigation: false`, and `source_required: false`. `required_internal_links` populated from Sprint 6E graph. **No routes published. No public HTML. No sitemap/navigation/indexation activation. production_can_safely_proceed remains no.**

**Rationale:** 6D generated drafts; 6E validated quality and link graph; 6F binds drafts to the governed route registry without publication activation.

**Doctrine reference:** `SOVEREIGN_FOUNDATION_COHORT_01_INTERNAL_LINK_GRAPH.md`, `SOVEREIGN_FOUNDATION_COHORT_01_ROUTE_MAPPING_READINESS.md`, `validate_corpus_routes_l1.py` schema.

**Sprint 6F validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- `validate_corpus_routes_l1.py`: 141 routes, 0 errors
- `validate_corpus_drafts_l1.py`: 83 draft-backed, 0 errors
- No draft content modifications required

**Publication readiness:** **Not ready for publication**. Route registration only.

**Recommended next step:** Sprint **6G** or internal link wiring / multilingual foundation expansion if authorized.

**Files created:**

- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_ROUTE_REGISTRATION_REPORT.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_ROUTE_TO_DRAFT_MAPPING.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_ROUTE_REGISTRATION_NO_PUBLICATION_GUARDRAIL.md`
- `main/data/SOVEREIGN_FOUNDATION_COHORT_01_ROUTE_REGISTRATION_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/routes.json` — 15 COHORT_01 foundation routes added
- `DECISION_LOG.md` — Sprint 6F entry appended.

**Not modified in this sprint:** COHORT_01 draft content files, `main/data/sources/source_registry.json`, `main/data/claims/`, automation scripts, workflows, root `README.md`, package files, dependencies.

---

## Sprint 6G — Initial 14,000-Page Launch Corpus Execution Charter

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6g-initial-14000-page-launch-corpus-charter`  
**Base:** main @ Sprint 6F merge  
**Status:** Complete — launch charter; composition model; no generation

**Summary:** Sprint **6G** established the **initial 14,000-page launch corpus** as the **minimum launch target** (7 languages × 2,000 pages), not a distant future goal. Created execution charter, launch composition model (JSON), cohort sequencing (COHORT_01 complete → COHORT_02 next in 6H), quality thresholds, internal-link requirements, controlled indexation strategy, and scale model to **100,000+** / **300,000+** pages. **No pages generated. routes.json unchanged (141). No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6A–6F built architecture, engine, foundation cohort, validation, and route registration. 6G defines how the corpus moves from 141 registered routes toward 14,000 governed launch pages as scalable sovereign infrastructure.

**Doctrine reference:** `corpus_route_formula.json`, `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json`, `SOVEREIGN_BATCH_GENERATION_AUTOMATION_DESIGN_WAVE_1.md`, COHORT_01 artifacts (6D–6F).

**Sprint 6G validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- routes.json, sources, claims — **not modified**
- Validators not weakened

**Publication readiness:** **Not ready for publication**. Charter and planning only.

**Recommended next step:** Sprint **6H** — route inventory generation for COHORT_02 (core EN terminology spine, 500–1,000 inventory rows).

**Files created:**

- `main/data/INITIAL_14000_PAGE_LAUNCH_CORPUS_CHARTER.md`
- `main/data/INITIAL_14000_PAGE_LAUNCH_COMPOSITION_MODEL.json`
- `main/data/INITIAL_14000_PAGE_LAUNCH_COHORT_SEQUENCE.md`
- `main/data/INITIAL_14000_PAGE_LAUNCH_QUALITY_THRESHOLDS.md`
- `main/data/INITIAL_14000_PAGE_LAUNCH_INTERNAL_LINK_REQUIREMENTS.md`
- `main/data/INITIAL_14000_PAGE_LAUNCH_INDEXATION_STRATEGY.md`
- `main/data/SOVEREIGN_CORPUS_SCALE_TO_100K_PLUS_MODEL.md`
- `main/data/INITIAL_14000_PAGE_LAUNCH_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6G entry appended.

**Not modified in this sprint:** `main/data/routes.json`, all content drafts, source/claim registries, automation scripts, workflows, root `README.md`, package files, dependencies.

---

## Sprint 6H — COHORT_02 English Terminology Route Inventory Generation

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6h-cohort-02-english-terminology-route-inventory`  
**Base:** main @ Sprint 6G merge  
**Status:** Complete — 902 inventory rows; no content; no routes.json merge

**Summary:** Sprint **6H** generated **902** governed COHORT_02 English terminology spine inventory rows in `COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json` (500–1,000 target). Coverage: 50 entities, 6 page types (canonical, audience explainer, compound, AI-readable, child-safe, comparison), 7 reference layers, 7 audiences. All rows: `inventory_planned`, `noindex_default`, `publication_eligibility: false`, `generation_eligibility: conditional`. **routes.json unchanged (141). No content. No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6G chartered the 14k launch path with COHORT_02 as first major terminology spine. 6H emits executable inventory without content generation or route publication.

**Doctrine reference:** `SOVEREIGN_ROUTE_INVENTORY_SCHEMA_WAVE_1.json`, `SOVEREIGN_ROUTE_GENERATION_MATRIX_WAVE_1.json`, `ontology/sulfur_terms.json`, `INITIAL_14000_PAGE_LAUNCH_COHORT_SEQUENCE.md`.

**Sprint 6H validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- Inventory: 902 rows; unique route_ids; all safety postures verified
- routes.json not modified; sources/claims not modified

**Publication readiness:** **Not ready for publication**. Inventory only.

**Recommended next step:** Sprint **6I** — COHORT_02 draft generation charter or selective inventory merge review.

**Files created:**

- `main/data/COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json`
- `main/data/COHORT_02_EN_TERMINOLOGY_ROUTE_GENERATION_REPORT.md`
- `main/data/COHORT_02_EN_TERMINOLOGY_SPINE_MODEL.md`
- `main/data/COHORT_02_EN_COMPARISON_ROUTE_SUBSET_MODEL.md`
- `main/data/COHORT_02_NO_PUBLICATION_NO_CONTENT_GENERATION_GUARDRAIL.md`
- `main/data/COHORT_02_ROUTE_INVENTORY_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6H entry appended.

**Not modified in this sprint:** `main/data/routes.json`, all content drafts, source/claim registries, automation scripts, workflows, root `README.md`, package files.

---

## Sprint 6I — COHORT_02 Full Non-Public Draft Generation Wave

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6i-cohort-02-full-draft-generation-wave`  
**Base:** main @ Sprint 6H merge  
**Status:** Complete — 902/902 non-public drafts generated; no route registration

**Summary:** Sprint **6I** executed the first large non-public draft generation wave toward the 14,000-page launch corpus. Deterministic engine `generate_cohort_02_full_draft_wave_v1.py` processed all **902** COHORT_02 English terminology inventory rows with **0 rejections**. Drafts written to `main/content/en/pages/cohort-02-terminology/`. All drafts: `non_public`, `indexable: false`, `source_required_unresolved`, `claim_pending_review`, `[SOURCE REQUIRED]` markers. **routes.json unchanged (141). No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6H produced executable inventory; 6I converts inventory into governed draft artifacts without publication, route merge, or indexation activation — the required pipeline step before controlled route registration.

**Doctrine reference:** `COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json`, `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json`, `corpus_production_rules.md`, `INITIAL_14000_PAGE_LAUNCH_COHORT_SEQUENCE.md`.

**Sprint 6I validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- Engine: 902 generated, 0 rejected; min word count 311
- routes.json not modified; sources/claims not modified
- Initial blocker (registry key `audiences` vs `audience_layers`) resolved in-engine

**Publication readiness:** **Not ready for publication**. Non-public drafts only.

**Recommended next step:** Sprint **6J** — COHORT_02 draft validation charter, internal-link graph planning, controlled route-registration wave planning (still gated by source/claim locks).

**Files created:**

- `scripts/generate_cohort_02_full_draft_wave_v1.py`
- `main/data/COHORT_02_FULL_DRAFT_MANIFEST.json`
- `main/data/COHORT_02_FULL_DRAFT_BLUEPRINTS.json`
- `main/data/COHORT_02_FULL_DRAFT_GENERATION_REPORT.md`
- `main/data/COHORT_02_FULL_DRAFT_QUALITY_ANTI_THIN_VALIDATION_REPORT.md`
- `main/data/COHORT_02_FULL_DRAFT_NO_PUBLICATION_NO_ROUTE_REGISTRATION_GUARDRAIL.md`
- `main/data/COHORT_02_FULL_DRAFT_GENERATION_VALIDATION_REPORT.md`
- `main/content/en/pages/cohort-02-terminology/*.md` (902 files)

**Files updated:**

- `DECISION_LOG.md` — Sprint 6I entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `source_registry.json`, `terminology_claims.json`, workflows, root `README.md`, package files, dependencies.

---

## Sprint 6I — COHORT_02 Full Non-Public Draft Generation Wave

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6i-cohort-02-full-draft-generation-wave`  
**Base:** main @ Sprint 6H merge  
**Status:** Complete — 902/902 non-public drafts generated; no route registration

**Summary:** Sprint **6I** executed the first large non-public draft generation wave toward the 14,000-page launch corpus. Deterministic engine `generate_cohort_02_full_draft_wave_v1.py` processed all **902** COHORT_02 English terminology inventory rows with **0 rejections**. Drafts written to `main/content/en/pages/cohort-02-terminology/`. All drafts: `non_public`, `indexable: false`, `source_required_unresolved`, `claim_pending_review`, `[SOURCE REQUIRED]` markers. **routes.json unchanged (141). No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6H produced executable inventory; 6I converts inventory into governed draft artifacts without publication, route merge, or indexation activation — the required pipeline step before controlled route registration.

**Doctrine reference:** `COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json`, `SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json`, `corpus_production_rules.md`, `INITIAL_14000_PAGE_LAUNCH_COHORT_SEQUENCE.md`.

**Sprint 6I validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- Engine: 902 generated, 0 rejected; min word count 311
- routes.json not modified; sources/claims not modified
- Initial blocker (registry key `audiences` vs `audience_layers`) resolved in-engine

**Publication readiness:** **Not ready for publication**. Non-public drafts only.

**Recommended next step:** Sprint **6J** — COHORT_02 draft validation charter, internal-link graph planning, controlled route-registration wave planning (still gated by source/claim locks).

**Files created:**

- `scripts/generate_cohort_02_full_draft_wave_v1.py`
- `main/data/COHORT_02_FULL_DRAFT_MANIFEST.json`
- `main/data/COHORT_02_FULL_DRAFT_BLUEPRINTS.json`
- `main/data/COHORT_02_FULL_DRAFT_GENERATION_REPORT.md`
- `main/data/COHORT_02_FULL_DRAFT_QUALITY_ANTI_THIN_VALIDATION_REPORT.md`
- `main/data/COHORT_02_FULL_DRAFT_NO_PUBLICATION_NO_ROUTE_REGISTRATION_GUARDRAIL.md`
- `main/data/COHORT_02_FULL_DRAFT_GENERATION_VALIDATION_REPORT.md`
- `main/content/en/pages/cohort-02-terminology/*.md` (902 files)

**Files updated:**

- `DECISION_LOG.md` — Sprint 6I entry appended.

**Not modified in this sprint:** `main/data/routes.json`, `source_registry.json`, `terminology_claims.json`, workflows, root `README.md`, package files, dependencies.



---

## Sprint 6J — COHORT_02 Full Draft Quality Gate and Internal Link Graph

**Date:** 2026-05-30  
**Branch:** claude/sprint-6j-cohort-02-full-draft-quality-gate-link-graph  
**Base:** main @ Sprint 6I merge  
**Status:** Complete — 902/902 audited; internal-link graph defined; no route registration

**Summary:** Sprint **6J** audited all **902** COHORT_02 non-public terminology drafts and produced quality gate documentation plus a governed internal-link graph using 
oute_id references only. Quality gate: **PASS** (anti-fake, anti-thin, anti-blog, forbidden-claim, reliability coverage). Link graph: 50 entity hubs, 5 cluster types, 0 broken route_id references. **0 draft files modified.** **routes.json unchanged (141). No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6I generated the first large terminology draft wave; 6J validates draft quality and defines the link graph required before any controlled COHORT_02 route registration charter.

**Doctrine reference:** COHORT_02_FULL_DRAFT_MANIFEST.json, COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json, INITIAL_14000_PAGE_LAUNCH_INTERNAL_LINK_REQUIREMENTS.md, Sprint 6E foundation link graph discipline.

**Sprint 6J validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- Quality audit: 902/902 pass; 253–298 words; 0 broken internal-link refs
- Structural duplication: 902 unique signatures (6 shared templates — expected)
- Generator refinement: **not required**
- routes.json not modified; sources/claims not modified; no draft rewrites

**Publication readiness:** **Not ready for publication**. Audit and planning graph only.

**Recommended next step:** Sprint **6K** — COHORT_02 controlled route registration wave charter (staged; still gated by source/claim locks and merge approval).

**Files created:**

- main/data/COHORT_02_FULL_DRAFT_QUALITY_MATRIX.md
- main/data/COHORT_02_FULL_DRAFT_ANTI_THIN_ANTI_FAKE_REPORT.md
- main/data/COHORT_02_FULL_DRAFT_FORBIDDEN_CLAIM_VALIDATION_REPORT.md
- main/data/COHORT_02_FULL_DRAFT_KNOWLEDGE_RELIABILITY_COVERAGE_REPORT.md
- main/data/COHORT_02_INTERNAL_LINK_GRAPH.md
- main/data/COHORT_02_ROUTE_REGISTRATION_READINESS_REPORT.md
- main/data/COHORT_02_FULL_DRAFT_NO_PUBLICATION_NO_ROUTE_REGISTRATION_GUARDRAIL.md
- main/data/COHORT_02_FULL_DRAFT_QUALITY_GATE_VALIDATION_REPORT.md

**Files updated:**

- DECISION_LOG.md — Sprint 6J entry appended.

**Not modified in this sprint:** main/data/routes.json, all 902 COHORT_02 draft files, source_registry.json, terminology_claims.json, workflows, root README.md, package files, dependencies.

---

## Sprint 6K — COHORT_02 Controlled Route Registration

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6k-cohort-02-controlled-route-registration`  
**Base:** main @ Sprint 6J merge  
**Status:** Complete — 902/902 routes registered; no publication

**Summary:** Sprint **6K** registered all **902** COHORT_02 English terminology draft routes in `routes.json` as **planned**, **draft-backed**, **non-public** routes (**141 → 1,043**). Each route: `indexable: false`, `in_sitemap: false`, `in_navigation: false`, `source_required: true`. `required_internal_links` from Sprint 6J graph. **48** comparison routes received disambiguated paths. **No content created. No public HTML. production_can_safely_proceed remains no.**

**Rationale:** 6J validated drafts and link graph; 6K binds the first large terminology cohort to the governed route registry — material progress toward the 14,000-page launch corpus without publication activation.

**Doctrine reference:** `COHORT_02_INTERNAL_LINK_GRAPH.md`, `COHORT_02_ROUTE_REGISTRATION_READINESS_REPORT.md`, `COHORT_02_FULL_DRAFT_MANIFEST.json`.

**Sprint 6K validation:**

- Pre-flight and post-run: all L1/L2 runtimes **PASS**
- `validate_corpus_routes_l1.py`: 1,043 routes, 0 errors
- `validate_corpus_drafts_l1.py`: 985 draft-backed, 0 errors
- L1 slug alignment for `cohort-02-terminology/` route_id filenames
- No draft content modifications

**Publication readiness:** **Not ready for publication**. Route registration only.

**Recommended next step:** Sprint **6L** — next cohort inventory/draft wave or source/claim boundary work toward publication gates (still gated by `production_can_safely_proceed: no`).

**Files created:**

- `main/data/COHORT_02_CONTROLLED_ROUTE_REGISTRATION_REPORT.md`
- `main/data/COHORT_02_ROUTE_TO_DRAFT_MAPPING_WAVE_1.md`
- `main/data/COHORT_02_ROUTE_REGISTRATION_NO_PUBLICATION_GUARDRAIL.md`
- `main/data/COHORT_02_ROUTE_REGISTRATION_VALIDATION_REPORT.md`

**Files updated:**

- `main/data/routes.json` — 902 COHORT_02 routes added
- `scripts/validate_corpus_routes_l1.py` — cohort-02-terminology slug alignment (L1 schema; not publication lock change)
- `DECISION_LOG.md` — Sprint 6K entry appended

**Not modified in this sprint:** all 902 COHORT_02 draft content files, source_registry.json, terminology_claims.json, workflows, root README.md, package files, dependencies.

---

## Sprint 6L — Route Registry Integrity Gate After COHORT_02 Registration

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6l-route-registry-integrity-gate`  
**Base:** main @ Sprint 6K merge  
**Status:** Complete — 1,043/1,043 audited; registry stable; no corrections required

**Summary:** Sprint **6L** audited the full route registry after the **141 → 1,043** COHORT_02 registration jump. **902/902** COHORT_02 route-to-draft mappings confirmed. **Zero** duplicate route_ids, paths, or content_files. **Zero** publication/indexation/sitemap/navigation leakage. **Zero** broken COHORT_02 draft paths. **58** pre-existing missing drafts (pre-COHORT Wave 1) documented — not introduced by 6K. **`routes.json` unchanged.** `production_can_safely_proceed remains no.**

**Rationale:** After registering 902 routes in one wave, the registry must be proven stable before the next large-scale generation wave toward 14,000 pages.

**Doctrine reference:** `COHORT_02_ROUTE_TO_DRAFT_MAPPING_WAVE_1.md`, `COHORT_02_CONTROLLED_ROUTE_REGISTRATION_REPORT.md`, `validate_corpus_routes_l1.py`.

**Sprint 6L validation:**

- Pre-audit and post-run: all L1/L2 runtimes **PASS**
- Integrity gate: 1,043 routes; 0 collisions; 0 leakage
- Sprint 6K slug validator scope confirmed narrow (cohort-02-terminology only)
- No registry or content modifications

**Publication readiness:** **Not ready for publication**. Integrity audit only.

**Recommended next step:** Resume large-scale corpus production — likely **multilingual / reference-layer wave** toward 14,000-page launch target (subject to source/claim gates).

**Files created:**

- `main/data/ROUTE_REGISTRY_INTEGRITY_GATE_WAVE_1_REPORT.md`
- `main/data/COHORT_02_ROUTE_TO_DRAFT_INTEGRITY_MATRIX.md`
- `main/data/ROUTE_REGISTRY_DUPLICATE_AND_PATH_COLLISION_AUDIT.md`
- `main/data/ROUTE_REGISTRY_PUBLICATION_INDEXATION_LEAKAGE_AUDIT.md`
- `main/data/ROUTE_REGISTRY_INTEGRITY_GATE_VALIDATION_REPORT.md`

**Files updated:**

- `DECISION_LOG.md` — Sprint 6L entry appended.

**Not modified in this sprint:** `main/data/routes.json`, all content drafts, `scripts/validate_corpus_routes_l1.py`, source/claim registries, workflows, root README.md, package files, dependencies.

---

## Sprint 6M-A — Sovereign Build Engine Hardening Layer Established

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-a-sovereign-build-engine-hardening-layer`  
**Base:** main @ Sprint 6L merge  
**Status:** Complete — build engine hardened; no public output; all locks intact

**Summary:** Sprint **6M-A** hardened the Bisulfid build engine before any public output generation. The sprint strengthened `scripts/build.py` as a governed, fail-closed, dry-run-capable build engine designed to respect route status, indexation locks, sitemap locks, navigation locks, source/claim boundaries, and publication controls. The sprint did not publish routes, did not generate a public launch, did not approve sources or claims, did not modify registries, did not edit content pages, did not remove `[SOURCE REQUIRED]` markers, and did not authorize sitemap, navigation, or indexation exposure. The purpose was to prepare the build layer for future governed sample rendering and later large-scale controlled output.

**Rationale:** With **1,043** governed routes and zero publication activation, the highest-risk next step would be uncontrolled HTML generation. Hardening the build layer first ensures future render sprints cannot accidentally expose draft-backed routes.

**Doctrine reference:** `BUILD_ENGINE_POLICY.md`, `BUILD_ENGINE_DRY_RUN_MODEL.md`, `BUILD_ENGINE_OUTPUT_LOCK_MODEL.md`, `main/config/build.json`.

**Sprint 6M-A validation:**

- Pre-run and post-run: all L1/L2 runtimes **PASS**
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run`: 1,043 routes inspected; 0 eligible; 0 public HTML
- `build.py --dry-run --strict`: **PASS**
- `production_can_safely_proceed`: **no** (confirmed)
- No registry, content, or route status modifications

**Publication readiness:** **Not ready for publication**. Build engine hardening only.

**Recommended next step:** Sprint **6M-B** — template hardening, then first governed non-public sample render under quarantined output path.

**Files created:**

- `scripts/validate_build_engine_l1.py`
- `main/data/BUILD_ENGINE_HARDENING_REPORT.md`
- `main/data/BUILD_ENGINE_POLICY.md`
- `main/data/BUILD_ENGINE_DRY_RUN_MODEL.md`
- `main/data/BUILD_ENGINE_OUTPUT_LOCK_MODEL.md`
- `main/data/BUILD_ENGINE_VALIDATION_REPORT.md`
- `main/data/BUILD_ENGINE_NEXT_ACTIONS.md`

**Files updated:**

- `scripts/build.py` — sovereign build engine (dry-run, strict, sample, explicit write modes)
- `scripts/serve.py` — safe local preview documentation
- `DECISION_LOG.md` — Sprint 6M-A entry appended

**Not modified in this sprint:** `main/data/routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, all content pages, workflows, root README.md, package files, dependencies, generated public HTML.

---

## Sprint 6M-B — Sovereign Template Layer Hardened for 14,000-Page Publication Frame

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-b-fourteen-thousand-publication-frame-template-layer`  
**Base:** main @ Sprint 6M-A merge  
**Status:** Complete — publication frame hardened; all locks intact

**Summary:** Sprint **6M-B** hardened the template layer as the **publication frame** for the fixed **14,000-page minimum launch corpus**. The sprint created governed frame templates (`page.html`, `reference.html`, `term.html`), hardened `base.html`, `home.html`, and nine partials with institutional shell, metadata, robots/noindex defaults, canonical non-public behavior, multilingual/RTL readiness, governance visibility, and source/claim honesty. The sprint did **not** publish routes, did **not** authorize indexation/sitemap/navigation, did **not** approve sources or claims, did **not** modify registries or content, and did **not** create a public launch. Sample rendering remains an engineering QA step inside the 14k pipeline only — not a launch strategy.

**Rationale:** The build engine (6M-A) requires a scalable publication frame before governed rendering at 14,000-page scale. Template hardening precedes render wiring and local quarantined QA.

**Doctrine reference:** `FOURTEEN_THOUSAND_PUBLICATION_FRAME_MODEL.md`, `TEMPLATE_CONTRACT_MODEL.md`, `BUILD_ENGINE_POLICY.md`.

**Sprint 6M-B validation:**

- `validate_template_layer_l1.py`: **PASS**
- `build.py --dry-run` / `--dry-run --strict`: **PASS**
- All L1/L2 corpus runtimes: **PASS**
- `production_can_safely_proceed`: **no**
- `site/_sample/` quarantine path reserved; no public HTML committed

**Publication readiness:** **Not ready for publication**. Template frame only.

**Recommended next step:** Sprint **6M-C** — governed render wiring + local quarantined QA sample under `site/_sample/`.

**Files created:**

- `main/templates/page.html`, `reference.html`, `term.html`
- `main/templates/partials/governance_banner.html`, `breadcrumbs.html`
- `scripts/validate_template_layer_l1.py`
- `scripts/validate_sample_output_l1.py`
- `main/data/TEMPLATE_HARDENING_REPORT.md`
- `main/data/TEMPLATE_CONTRACT_MODEL.md`
- `main/data/TEMPLATE_GOVERNANCE_STATUS_MODEL.md`
- `main/data/TEMPLATE_MULTILINGUAL_RENDERING_MODEL.md`
- `main/data/FOURTEEN_THOUSAND_PUBLICATION_FRAME_MODEL.md`
- `main/data/TEMPLATE_VALIDATION_REPORT.md`
- `main/data/TEMPLATE_NEXT_ACTIONS.md`
- `site/_sample/.gitkeep`

**Files updated:**

- `main/templates/base.html`, `home.html`, `partials/*.html` (hardened)
- `DECISION_LOG.md`

**Not modified in this sprint:** `routes.json`, `internal_links.json`, sitemap/navigation policies, source/claim registries, all content pages, `build.py`, workflows, root README.md, package files, dependencies.

---

## Template Registry Migration and Quarantined QA Render Completed

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-c-template-registry-migration-and-quarantined-qa-render`  
**Base:** main @ Sprint 6M-B merge  
**Status:** Complete — template bridges wired; quarantined QA render under `site/_sample/`; all locks intact

**Summary:** Sprint **6M-C** migrated or bridged legacy template references into the hardened sovereign template layer and produced the first quarantined non-public QA render under `site/_sample/`. The sprint proved that the publication frame can generate visible HTML without weakening publication, indexation, sitemap, navigation, source, or claim locks. The QA output remained isolated, noindex, outside sitemap, outside navigation, and clearly marked as non-public. No routes were published, no routes were made indexable, no routes were added to sitemap or navigation, no sources or claims were approved, no registries were modified, no content pages were edited, and `[SOURCE REQUIRED]` markers remained unresolved. The fixed **14,000-page minimum launch objective** remains unchanged.

**Rationale:** Sprint 6M-B hardened publication frames but deferred registry template name migration. 6M-C connects legacy `reference_page.html` / `term_page.html` registry references to hardened frames via wrapper bridges and `build.py` `TEMPLATE_FRAME_BRIDGE` without mutating `routes.json`.

**Sprint 6M-C validation:**

- `validate_template_registry_l1.py`: **PASS**
- `validate_template_layer_l1.py`: **PASS**
- `validate_sample_output_l1.py`: **PASS** (8 quarantined QA files)
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--dry-run --strict`: **PASS**
- `build.py --render-quarantined-sample`: **PASS** (8 files)
- All L1/L2 corpus runtimes + source/claim guardrails: **PASS**
- `production_can_safely_proceed`: **no**
- Corpus Governance CI: **required on PR**

**Publication readiness:** **Not ready for publication**. QA engineering proof only.

**Recommended next step:** Sprint **6M-D** — expanded non-public release candidate (100–250 pages) or authorized registry template name migration.

**Files created:**

- `scripts/validate_template_registry_l1.py`
- `main/data/TEMPLATE_REGISTRY_MIGRATION_REPORT.md`
- `main/data/QUARANTINED_QA_RENDER_REPORT.md`
- `main/data/QUARANTINED_QA_RENDER_VALIDATION_REPORT.md`
- `main/data/PUBLICATION_FRAME_QA_NEXT_ACTIONS.md`
- `site/_sample/*.html` (8 quarantined QA pages)

**Files updated:**

- `scripts/build.py` — template bridge map, quarantined sample render mode
- `main/templates/reference_page.html`, `term_page.html` — hardened frame bridges
- `scripts/validate_sample_output_l1.py` — expanded QA marker checks
- `scripts/validate_corpus_publication_lock_l1.py` — quarantine exception for `site/_sample/`
- `DECISION_LOG.md`

**Not modified in this sprint:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, all `main/content/**` pages, workflows, root README.md, package files, dependencies, public HTML outside `site/_sample/`.

---

## 14K Pipeline Non-Public Release Candidate Batch 01 Completed

**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-d-14k-pipeline-non-public-release-candidate-batch-01`  
**Base:** main @ Sprint 6M-C merge  
**Status:** Complete — 250-page RC batch rendered under quarantine; all locks intact

**Summary:** Sprint **6M-D** produced the first larger non-public release candidate batch inside the fixed **14,000-page** Bisulfid publication pipeline. The sprint expanded quarantined rendering beyond the initial 8-page QA proof to **250 deterministic pages** while keeping all output isolated under `site/_sample/`, noindex, outside sitemap, outside navigation, and clearly marked as non-public release candidate output. The sprint did not publish routes, did not make routes indexable, did not add routes to sitemap or navigation, did not approve sources or claims, did not modify registries, did not edit content pages, and did not remove `[SOURCE REQUIRED]` markers. The batch is an engineering release candidate for the 14,000-page launch pipeline, not a reduced launch target.

**Rationale:** Sprint 6M-C proved the publication frame at 8 pages. 6M-D validates batch selection, render throughput, multilingual and source-required coverage at RC scale before 500 / 1,000 / 14,000 execution stages.

**Sprint 6M-D validation:**

- `validate_release_candidate_batch_l1.py`: **PASS** (250 files)
- `validate_template_registry_l1.py`: **PASS**
- `validate_template_layer_l1.py`: **PASS**
- `validate_sample_output_l1.py`: **PASS** (250 files)
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--dry-run --strict`: **PASS**
- `build.py --render-quarantined-rc-batch --limit 250`: **PASS**
- All L1/L2 corpus runtimes + source/claim guardrails: **PASS**
- `production_can_safely_proceed`: **no**
- Corpus Governance CI: **required on PR**

**Publication readiness:** **Not ready for publication**. RC engineering batch only.

**Recommended next step:** Sprint **6M-E** — 500-page non-public RC Batch 02 or markdown rendering improvements.

**Files created:**

- `scripts/validate_release_candidate_batch_l1.py`
- `main/data/NON_PUBLIC_RELEASE_CANDIDATE_BATCH_01_REPORT.md`
- `main/data/NON_PUBLIC_RELEASE_CANDIDATE_BATCH_01_MATRIX.md`
- `main/data/NON_PUBLIC_RELEASE_CANDIDATE_BATCH_01_VALIDATION_REPORT.md`
- `main/data/FOURTEEN_THOUSAND_PIPELINE_NEXT_ACTIONS.md`
- `site/_sample/rc_batch_manifest.json`
- `site/_sample/*.html` (250 RC batch pages)

**Files updated:**

- `scripts/build.py` — RC batch render mode, stratified selection, manifest
- `scripts/validate_sample_output_l1.py` — RC marker support, negation-aware governance scans
- `DECISION_LOG.md`

**Not modified in this sprint:** `routes.json`, `internal_links.json`, sitemap/navigation policies, source/claim registries, `sulfur_terms.json`, all `main/content/**` pages, workflows, root README.md, package files, dependencies, public HTML outside `site/_sample/`.

---

## 14K Pipeline 1,500-Page Non-Public RC Completed

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-e-1500-page-14k-pipeline-non-public-rc`  
**Base:** main @ Sprint 6M-D merge (`f2752a1`)  
**Status:** Complete — 1,500-page RC rendered under quarantine; all locks intact

**Summary:** Sprint **6M-E** advanced the Bisulfid **14,000-page** publication pipeline by producing a **1,500-page** non-public release candidate under `site/_sample/`. The sprint deliberately skipped the smaller **500-page** and **1,000-page** RC stages to accelerate toward the fixed **14,000-page** launch corpus while preserving all governance controls. The **1,500-page** batch is an engineering release candidate, **not a public launch** and **not a reduced target**. Corpus expanded from **1,043** to **1,500** planned routes (**985 → 1,500** draft-backed). No routes were published, no routes were made indexable, no routes were added to sitemap or navigation, no sources or claims were approved, protected registries were not modified for approval, and `[SOURCE REQUIRED]` markers remained unresolved.

**Rationale:** Sprint 6M-D proved 250-page RC scale. 6M-E validates governed corpus expansion, render throughput, and validator coverage at **1,500 pages** on the direct path to **7,500** and **14,000** non-public RC stages.

**Sprint 6M-E validation:**

- `validate_1500_rc_batch_l1.py`: **PASS** (1,500 files)
- `validate_release_candidate_batch_l1.py`: **PASS** (1,500 files)
- `validate_template_registry_l1.py`: **PASS**
- `validate_template_layer_l1.py`: **PASS**
- `validate_sample_output_l1.py`: **PASS** (1,500 files)
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--strict`: **PASS**
- `build.py --render-quarantined-rc-batch --limit 1500`: **PASS** (1,500 rendered, 0 skipped)
- `corpus_production_runtime_l2.py`: **PASS**
- `corpus_validation_runtime_l1.py`: **PASS**
- `source_claim_guardrail_runtime_l1.py`: **PASS**
- `corpus_production_planner_l2.py`: **PASS**

**Files created:**

- `scripts/generate_1500_corpus_expansion_v1.py`
- `scripts/validate_1500_rc_batch_l1.py`
- `main/data/NON_PUBLIC_RC_1500_REPORT.md`
- `main/data/NON_PUBLIC_RC_1500_MATRIX.md` (1,500 rows)
- `main/data/NON_PUBLIC_RC_1500_VALIDATION_REPORT.md`
- `main/data/SEVEN_THOUSAND_FIVE_HUNDRED_PIPELINE_NEXT_ACTIONS.md`
- `site/_sample/rc_batch_manifest.json`
- `site/_sample/*.html` (1,500 RC pages)

**Files updated:**

- `scripts/build.py` — RC 1,500 limit, dynamic manifest batch_id
- `scripts/validate_release_candidate_batch_l1.py` — RC max 1,500, negation-aware scans
- `scripts/validate_sample_output_l1.py` — negation-aware claim scan expansion
- `main/data/routes.json` — +457 governed planned routes (COHORT_03 expansion)
- `main/data/internal_links.json` — cohort03 spine planning link group
- `main/content/**` — governed draft expansion + missing-draft backfill only
- `DECISION_LOG.md`

**Not modified:** `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, workflows, root README.md, package files, dependencies, public HTML outside `site/_sample/`.

---

## 14K Pipeline 7,500-Page Non-Public RC Completed

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-f-7500-page-14k-pipeline-non-public-rc`  
**Base:** main @ Sprint 6M-E merge (`9c0d434`)  
**Status:** Complete — 7,500-page RC rendered under quarantine; all locks intact

**Summary:** Sprint **6M-F** advanced the Bisulfid **14,000-page** publication pipeline by expanding the governed non-public corpus to **7,500** draft-backed routes and producing a **7,500-page** non-public release candidate under `site/_sample/`. The sprint moved directly from the **1,500-page** RC stage to the **7,500-page** RC stage to accelerate toward the fixed **14,000-page** launch corpus while preserving all governance controls. The **7,500-page** batch is an engineering release candidate, **not a public launch** and **not a reduced target**. No routes were published, no routes were made indexable, no routes were added to sitemap or navigation, no sources or claims were approved, no protected registries were modified for approval, and `[SOURCE REQUIRED]` markers remained unresolved.

**Rationale:** Sprint 6M-E proved 1,500-page RC scale. 6M-F validates governed corpus expansion (+6,000 COHORT_04 routes), render throughput, and validator coverage at **7,500 pages** on the direct path to **14,000** non-public launch-corpus candidate.

**Sprint 6M-F validation:**

- `validate_7500_rc_batch_l1.py`: **PASS** (7,500 files)
- `validate_release_candidate_batch_l1.py`: **PASS** (7,500 files)
- `validate_template_registry_l1.py`: **PASS**
- `validate_template_layer_l1.py`: **PASS**
- `validate_sample_output_l1.py`: **PASS** (7,500 files)
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--strict`: **PASS**
- `build.py --render-quarantined-rc-batch --limit 7500`: **PASS** (7,500 rendered, 0 skipped)
- `corpus_production_runtime_l2.py`: **PASS**
- `corpus_validation_runtime_l1.py`: **PASS**
- `source_claim_guardrail_runtime_l1.py`: **PASS**
- `corpus_production_planner_l2.py`: **PASS**

**Files created:**

- `scripts/generate_7500_corpus_expansion_v1.py`
- `scripts/validate_7500_rc_batch_l1.py`
- `main/data/NON_PUBLIC_RC_7500_REPORT.md`
- `main/data/NON_PUBLIC_RC_7500_MATRIX.md` (7,500 rows)
- `main/data/NON_PUBLIC_RC_7500_VALIDATION_REPORT.md`
- `main/data/FOURTEEN_THOUSAND_LAUNCH_CORPUS_NEXT_ACTIONS.md`
- `main/data/COHORT_04_7500_EXPANSION_INVENTORY.json`
- `main/data/COHORT_04_7500_EXPANSION_MANIFEST.json`
- `site/_sample/rc_batch_manifest.json`
- `site/_sample/*.html` (7,500 RC pages)

**Files updated:**

- `scripts/build.py` — RC 7,500 limit, `batch_id: rc_7500`, sprint 6M-F tag
- `scripts/validate_release_candidate_batch_l1.py` — RC max 7,500, rc_7500 batch check
- `main/data/routes.json` — +6,000 governed planned routes (COHORT_04 expansion)
- `main/data/internal_links.json` — cohort04 spine planning link group
- `main/content/**` — governed draft expansion only
- `DECISION_LOG.md`

**Not modified:** `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, workflows, root README.md, package files, dependencies, public HTML outside `site/_sample/`.

---

## 14,000-Page Controlled Public Launch Foundation Completed

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-g-14000-page-controlled-public-launch-foundation`  
**Base:** main @ Sprint 6M-F merge  
**Status:** Complete — 14,000-page controlled public launch foundation

**Summary:** Sprint **6M-G** moved Bisulfid from non-public release-candidate testing into the first controlled public launch foundation. The sprint expanded the governed corpus to **14,000** draft-backed routes and generated **14,000** controlled public output pages under `site/public/` while preserving source/claim truth and gate separation. The sprint established public visibility as the primary track after the successful 7,500-page non-public RC test. It did not approve sources or claims, did not remove unresolved source markers, did not create uncontrolled sitemap/navigation/indexation exposure, and did not weaken the quality system. The 14,000-page launch foundation is the first visible public beginning of a much larger reference asset intended to scale to 100,000+ and eventually hundreds of thousands of governed pages.

**Corpus expansion:**

- Before: 7,500 routes, 7,500 draft-backed, 0 missing drafts
- Added: +6,500 COHORT_05 routes via `generate_14000_corpus_expansion_v1.py`
- After: 14,000 routes, 14,000 draft-backed, 0 missing drafts

**Public output:**

- Command: `python scripts/build.py --render-public-launch-foundation --limit 14000`
- Rendered: 14,000 pages, 0 skipped
- Location: `site/public/` (not `site/_sample/`)
- Indexation: CLOSED (`noindex,nofollow`)
- Sitemap: CLOSED
- Navigation: CLOSED

**Sprint 6M-G validation:**

- `validate_14000_public_launch_foundation_l1.py`: **PASS**
- `validate_public_output_l1.py`: **PASS**
- `validate_release_candidate_batch_l1.py`: **PASS**
- `validate_template_registry_l1.py`: **PASS**
- `validate_template_layer_l1.py`: **PASS**
- `validate_sample_output_l1.py`: **PASS**
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--strict`: **PASS**
- `corpus_production_runtime_l2.py`: **PASS**
- `corpus_validation_runtime_l1.py`: **PASS**
- `source_claim_guardrail_runtime_l1.py`: **PASS**
- `corpus_production_planner_l2.py`: **PASS**

**Files created:**

- `scripts/generate_14000_corpus_expansion_v1.py`
- `scripts/validate_14000_public_launch_foundation_l1.py`
- `scripts/validate_public_output_l1.py`
- `main/data/LAUNCH_FOUNDATION_14000_REPORT.md`
- `main/data/LAUNCH_FOUNDATION_14000_MATRIX.md` (14,000 rows)
- `main/data/LAUNCH_FOUNDATION_14000_VALIDATION_REPORT.md`
- `main/data/PUBLICATION_GATE_MODEL_14000.md`
- `main/data/PUBLIC_LAUNCH_NEXT_ACTIONS.md`
- `main/data/COHORT_05_14000_EXPANSION_INVENTORY.json`
- `main/data/COHORT_05_14000_EXPANSION_MANIFEST.json`
- `site/public/public_launch_manifest.json`
- `site/public/**/index.html` (14,000 public foundation pages)

**Files updated:**

- `scripts/build.py` — `--render-public-launch-foundation`, RC 14,000 batch_id, public launch render pipeline
- `scripts/validate_release_candidate_batch_l1.py` — allow `site/public/`, RC max 14,000
- `scripts/validate_sample_output_l1.py` — allow `site/public/` in HTML scan
- `main/data/routes.json` — +6,500 governed planned routes (COHORT_05)
- `main/data/internal_links.json` — cohort05 spine planning link group
- `main/content/**` — governed draft expansion only
- `DECISION_LOG.md`

**Not modified:** `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, workflows, root README.md, package files, dependencies.

---

## GitHub Pages Public Deployment Gate Established

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-h-github-pages-public-deployment-gate`  
**Base:** main @ Sprint 6M-G merge (`5cfd22f34`)  
**Status:** Complete — governed GitHub Pages deployment gate configured

**Summary:** Sprint **6M-H** established the governed GitHub Pages deployment gate for the 14,000-page Bisulfid public launch foundation. The sprint configured deployment to serve `site/public/` as the public website artifact while preserving branch protection, source/claim truth, and gate separation. It did not deploy repository root, did not deploy `site/_sample/`, did not open indexation, did not publish sitemap or navigation artifacts, did not approve sources or claims, and did not modify content pages or protected registries. CNAME handling was moved into repository-controlled files rather than direct GitHub UI commits, preserving the protected-main workflow.

**Deployment model:**

- Workflow: `.github/workflows/pages-public-deploy.yml`
- Trigger: `workflow_dispatch` (explicit manual run)
- Artifact root: `site/public/` only (14,000 pages + manifest + CNAME + `.nojekyll`)
- Permissions: `contents: read`, `pages: write`, `id-token: write`
- No secrets, no Cloudflare API, no dependency install, no corpus regeneration

**Sprint 6M-H validation:**

- `validate_pages_deployment_gate_l1.py`: **PASS**
- `validate_14000_public_launch_foundation_l1.py`: **PASS**
- `validate_public_output_l1.py`: **PASS**
- `validate_release_candidate_batch_l1.py`: **PASS**
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--strict`: **PASS**
- `corpus_production_runtime_l2.py`: **PASS**
- `corpus_validation_runtime_l1.py`: **PASS**
- `source_claim_guardrail_runtime_l1.py`: **PASS**
- `corpus_production_planner_l2.py`: **PASS**

**Files created:**

- `.github/workflows/pages-public-deploy.yml`
- `scripts/validate_pages_deployment_gate_l1.py`
- `site/public/CNAME`
- `site/public/.nojekyll`
- `main/data/GITHUB_PAGES_PUBLIC_DEPLOYMENT_GATE_REPORT.md`
- `main/data/GITHUB_PAGES_PUBLIC_DEPLOYMENT_SECURITY_MODEL.md`
- `main/data/GITHUB_PAGES_PUBLIC_DEPLOYMENT_VALIDATION_REPORT.md`
- `main/data/GITHUB_PAGES_PUBLIC_DEPLOYMENT_NEXT_ACTIONS.md`
- `DECISION_LOG.md`

**Not modified:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, `main/content/**`, `site/public/*.html`, `site/_sample/**`, root README.md, package files, dependencies, `corpus-governance-ci.yml`.

---

## Bisulfid Proprietary Design System Foundation Established

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6n-a-bisulfid-design-system-foundation`  
**Base:** main @ Sprint 6M-H merge (`249ad0b28`)  
**Status:** Complete — dependency-free design-system foundation

**Summary:** Sprint **6N-A** established the dependency-free Bisulfid design-system foundation as a proprietary visual and interaction language for the 14,000-page public launch foundation and future 100,000+ page expansion. The sprint created internal tokens, component primitives, SVG identity assets, and a vanilla motion governance layer without external UI libraries, npm dependencies, CDN assets, tracking scripts, or third-party visual frameworks. The design system preserves source-required visibility, source/claim truth, governance states, accessibility, and future multilingual readiness. It does not modify public output, open indexation, publish sitemap/navigation, or approve sources or claims.

**Sprint 6N-A validation:**

- `validate_bisulfid_design_system_l1.py`: **PASS**
- `validate_pages_deployment_gate_l1.py`: **PASS**
- `validate_14000_public_launch_foundation_l1.py`: **PASS**
- `validate_public_output_l1.py`: **PASS**
- `corpus_validation_runtime_l1.py`: **PASS**
- `source_claim_guardrail_runtime_l1.py`: **PASS**
- All prior public foundation validators: **PASS**

**Files created:**

- `bisulfid-design-system/**` — tokens, components, assets, engine
- `scripts/validate_bisulfid_design_system_l1.py`
- `main/data/BISULFID_DESIGN_SYSTEM_FOUNDATION_REPORT.md`
- `main/data/BISULFID_DESIGN_SYSTEM_TOKEN_MODEL.md`
- `main/data/BISULFID_DESIGN_SYSTEM_COMPONENT_MODEL.md`
- `main/data/BISULFID_DESIGN_SYSTEM_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md`

**Not modified:** `routes.json`, registries, `main/content/**`, `site/public/**`, `site/_sample/**`, `.github/workflows/pages-public-deploy.yml`, root README.md, package files, dependencies.

---

## Live Site Visibility Verified and Rendering Defects Registered

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-i-live-site-verification-and-render-defect-register`  
**Base:** main @ Sprint 6N-A merge (`6ae6ca0c4`)  
**Status:** Complete — live visibility verified; rendering defects registered; all gates preserved

**Summary:** Sprint **6M-I** verified that bisulfid.com is serving the controlled `site/public/` launch foundation and that public visibility is operational. The sprint also registered the first live-rendering defects exposed by public visibility: default browser styling, raw Markdown markers, QA placeholder text, and unintegrated governance presentation. The sprint preserved all gates: indexation, sitemap, navigation, source approval, and claim approval remain closed. The result confirms that deployment succeeded while making **6N-B** design-system template integration the immediate next priority before search exposure.

**Live verification findings:**

- `https://bisulfid.com/` → **200**, public launch foundation HTML (not README)
- Forbidden paths `/scripts/`, `/main/`, `/_sample/`, `/README.md` → **404**
- `noindex,nofollow` present on live and local artifact
- `sitemap.xml` and `robots.txt` → **404** on live; absent under `site/public/`
- Navigation inactive; source/claim approval not implied; `[SOURCE REQUIRED]` visible where unresolved

**Rendering defects registered:**

| ID | Defect | Local count |
|----|--------|-------------|
| DEF-01 | Default browser styling | 14,000 pages |
| DEF-02 | Raw Markdown `**` markers | 4 pages |
| DEF-03 | QA placeholder leakage | 228 pages |
| DEF-04 | Governance overload (raw text) | All pages |
| DEF-05 | Design system not integrated | 14,000 pages |

**Sprint 6M-I validation:**

- `validate_live_site_visibility_l1.py`: **PASS**
- `validate_pages_deployment_gate_l1.py`: **PASS**
- `validate_14000_public_launch_foundation_l1.py`: **PASS**
- `validate_public_output_l1.py`: **PASS**
- `validate_bisulfid_design_system_l1.py`: **PASS**
- `validate_release_candidate_batch_l1.py`: **PASS**
- `validate_template_registry_l1.py`: **PASS**
- `validate_template_layer_l1.py`: **PASS**
- `validate_sample_output_l1.py`: **PASS**
- `validate_build_engine_l1.py`: **PASS**
- `build.py --dry-run` / `--strict`: **PASS**
- `corpus_production_runtime_l2.py`: **PASS**
- `corpus_validation_runtime_l1.py`: **PASS**
- `source_claim_guardrail_runtime_l1.py`: **PASS**
- `corpus_production_planner_l2.py`: **PASS**

**Files created:**

- `scripts/validate_live_site_visibility_l1.py`
- `main/data/LIVE_SITE_VERIFICATION_REPORT.md`
- `main/data/PUBLIC_RENDERING_DEFECT_REGISTER.md`
- `main/data/LIVE_SITE_VISIBILITY_GATE_VALIDATION_REPORT.md`
- `main/data/DESIGN_SYSTEM_INTEGRATION_URGENCY_REPORT.md`
- `main/data/LIVE_SITE_NEXT_ACTIONS.md`

**Files updated:**

- `DECISION_LOG.md`

**Not modified:** `routes.json`, `source_registry.json`, `terminology_claims.json`, `main/content/**`, `site/public/*.html`, `site/_sample/**`, GitHub Pages workflow, package files, dependencies, root README.md.

**Next sprint:** **6N-B — Design System Template Integration Pilot** (see `main/data/LIVE_SITE_NEXT_ACTIONS.md`).

---

## Bisulfid Design System Template Integration Pilot Completed

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6n-b-design-system-template-integration-pilot`  
**Base:** main @ Sprint 6M-I merge (`8e7b80d24`)  
**Status:** Complete — design-system template integration pilot

**Summary:** Sprint **6N-B** integrated the first layer of the proprietary Bisulfid design system into the publication template layer through a controlled pilot. The sprint began moving the live public foundation away from browser-default rendering toward a sovereign chemical-language control room interface while preserving source-required visibility, source/claim boundaries, noindex posture, and closed sitemap/navigation gates. The sprint addressed raw Markdown and public QA placeholder defects in the controlled integration sample and established the next path toward staged 14,000-page design-system re-rendering. No external dependencies, CDNs, npm packages, tracking scripts, source approvals, claim approvals, sitemap artifacts, or navigation artifacts were introduced.

**Integration pilot:**

- Templates wired to local `/assets/bisulfid-design-system/bisulfid-frame.css`
- Components: governance banner, source crystal, term card, language depth
- Build engine: `--render-integration-sample` → `site/public/_integration_sample/` (7 routes)
- Markdown rendering fixed (inline, headings, table cells)
- QA placeholder suppressed in integration/public render modes
- 14,000-page foundation corpus unchanged

**Sprint 6N-B validation:**

- `validate_bisulfid_design_system_integration_l1.py`: **PASS**
- `validate_live_site_visibility_l1.py`: **PASS**
- `validate_bisulfid_design_system_l1.py`: **PASS**
- All prior L1/L2 validators: **PASS**

**Files created/updated:**

- `main/templates/**` — design-system class integration
- `scripts/build.py` — integration sample render + markdown fixes
- `scripts/validate_bisulfid_design_system_integration_l1.py`
- `site/public/assets/bisulfid-design-system/**`
- `site/public/_integration_sample/**`
- Sprint reports under `main/data/`
- `DECISION_LOG.md`

**Not modified:** `routes.json`, registries, `main/content/**`, 14,000 foundation `site/public/**` pages (excluding `_integration_sample/`), `site/_sample/**`, GitHub Pages workflow, package files, dependencies, root README.md.

**Next sprint:** **6N-C — Controlled design-system re-render** (see `main/data/DESIGN_SYSTEM_TEMPLATE_INTEGRATION_NEXT_ACTIONS.md`).

---

## 14,000-Page Design-System Public Refresh Completed

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-c-controlled-14000-design-system-public-refresh`  
**Base:** main @ Sprint 6N-B merge (`79fe30532`)  
**Status:** Complete — full public foundation refreshed with design system

**Summary:** Sprint **6N-C** performed the controlled 14,000-page public refresh using the proprietary Bisulfid design system. The sprint moved the public foundation away from browser-default rendering toward a sovereign chemical-language control room interface across the full public output while preserving noindex posture, source-required visibility, source/claim truth, and closed sitemap/navigation/indexation gates. The sprint addressed the raw Markdown and QA placeholder defects identified in live-site verification and prepared the refreshed output for a governed GitHub Pages redeploy and live re-check. No external dependencies, CDNs, npm packages, tracking scripts, source approvals, claim approvals, sitemap artifacts, or navigation artifacts were introduced.

**Refresh command:** `python scripts/build.py --render-public-design-system-refresh --limit 14000`

**Results:**

- **14,000** foundation pages re-rendered with design-system templates
- **14,000/14,000** pages link local design-system CSS
- **0** raw Markdown marker files (DEF-02 closed)
- **0** QA placeholder files (DEF-03 closed)
- `site/public/_integration_sample/` preserved (7 routes)
- `public_launch_manifest.json`: `design_system_refresh: true`, sprint **6N-C**

**Sprint 6N-C validation:**

- `validate_14000_design_system_public_refresh_l1.py`: **PASS**
- `validate_bisulfid_design_system_integration_l1.py`: **PASS**
- All prior L1/L2 validators: **PASS**

**Files created/updated:**

- `scripts/build.py` — `--render-public-design-system-refresh`
- `scripts/validate_14000_design_system_public_refresh_l1.py`
- `site/public/**/*.html` (14,000 foundation pages)
- `site/public/public_launch_manifest.json`
- Sprint reports under `main/data/`
- `DECISION_LOG.md`

**Not modified:** `routes.json`, registries, `main/content/**`, `site/_sample/**`, GitHub Pages workflow, package files, dependencies, root README.md.

**Next steps:** GitHub Pages redeploy → **Sprint 6M-J — Post-Refresh Live Site Verification** (indexation remains **CLOSED**).

---

## Pages Artifact Sample Exclusion Patch Completed

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-c-p1-pages-artifact-sample-exclusion-patch`  
**Base:** main @ Sprint 6N-C merge (`5e7202fea`)  
**Status:** Complete — deployment artifact boundary corrected

**Summary:** Sprint **6N-C-P1** corrected the GitHub Pages deployment artifact boundary after the post-6N-C deploy attempt detected 14,007 HTML pages instead of the expected 14,000. The patch preserves `site/public/` as the repository public-output source while excluding `site/public/_integration_sample/` from the deployed Pages artifact. The sprint does not modify corpus routes, content, registries, design-system output pages, source/claim data, sitemap, navigation, or indexation posture. The deployment gate now protects the live site from serving integration sample pages while preserving the 14,000-page design-system public foundation.

**Root cause:** Pre-patch workflow uploaded entire `site/public/` including 7 integration sample pages from Sprint 6N-B.

**Fix:** Stage temporary artifact via `rsync --exclude='_integration_sample/'`; verify exactly 14,000 pages; upload staged directory only.

**Files updated:**

- `.github/workflows/pages-public-deploy.yml` — staged artifact with sample exclusion
- `scripts/validate_pages_deployment_gate_l1.py` — validates staging and exclusion
- Sprint reports under `main/data/`
- `DECISION_LOG.md`

**Not modified:** `routes.json`, registries, `main/content/**`, `site/public/**/*.html`, `site/public/assets/**`, `site/public/_integration_sample/**`, `site/_sample/**`, package files, dependencies, root README.md.

**Next steps:** Merge → **Pages public deploy** → **Sprint 6M-J — Post-Refresh Live Site Verification** (indexation remains **CLOSED**).

---

## Sovereign Visual Interface Reconstruction Completed

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-d-sovereign-visual-interface-reconstruction`  
**Base:** main @ Sprint 6N-C-P1 merge  
**Status:** In progress — design-system + templates complete; **visual proof gate active**; full 14,000 refresh **pending human proof approval**

**Visual Proof Gate:** 6N-C validators passed while live UI failed eye review. 6N-D requires `--render-visual-proof-sample` (7 routes) and `visual_review_status: approved` before `--render-public-design-system-refresh --limit 14000`.

**Summary:** Sprint **6N-D** reconstructs the visible Bisulfid public interface using the fixed **carbon-gray, warm sulfur-yellow, and molybdenum-silver** material palette. Design-system tokens, components, SVG assets, templates, and validators are in place. The **14,000-page foundation remains on 6N-C output** until visual proof passes human review and full refresh is explicitly authorized.

**Proof command:** `python scripts/build.py --render-visual-proof-sample`

**Full refresh command (gated):** `python scripts/build.py --render-public-design-system-refresh --limit 14000`

**Results (current):**

- Visual proof sample: **7 routes** under `site/public/_visual_proof_sample/`
- Public foundation: **14,000 pages** (6N-C design until proof-approved full refresh)
- Material palette: carbon / sulfur / molybdenum
- Full refresh: **BLOCKED** until `visual_review_status: approved`

**Files updated:**

- `bisulfid-design-system/**` — tokens, components, SVG assets, bisulfid-frame.css
- `main/templates/**` — hero, governance chips, footer labels
- `scripts/build.py` — display labels, manifest metadata, asset sync
- `scripts/validate_sovereign_visual_interface_l1.py`
- `site/public/**` (14,000 foundation + assets)
- Sprint reports under `main/data/`
- `DECISION_LOG.md`

**Not modified:** `routes.json`, registries, `main/content/**`, `site/_sample/**`, GitHub Pages workflow, package files, dependencies, root README.md.

**Next steps:** GitHub Pages redeploy → **Sprint 6M-J — Post-Refresh Live Site Verification** (indexation remains **CLOSED**).


---

## Decision: Public Surface Integrity Repair After Governance Leakage

**Date:** 2026-06-05
**Asset:** Bisulfid.com
**Decision status:** Accepted
**Related PR:** #92
**Scope:** `site/public/` public-facing surface only

### Context

After the initial homepage repair, the live public surface of bisulfid.com exposed several unacceptable public-facing defects:

- `/en/` returned a GitHub Pages 404.
- `/de/` exposed draft/governance language publicly.
- `/what-is-bisulfid/` exposed internal publication warnings and source-required markers.
- The homepage contained broken or unstable public interface elements.
- Public navigation linked to routes that were not yet clean public pages.
- The mobile interface showed default/raw HTML behavior inconsistent with the sovereign asset standard.

These defects did not indicate a failure of the corpus governance system. They indicated a failure to separate the public display layer from internal draft/corpus governance outputs.

### Decision

Bisulfid.com will maintain a strict separation between:

1. **Internal governed corpus layers** — draft, source-locked, validation-controlled, not automatically public.
2. **Public surface pages** — clean, intentional, visitor-safe, free from internal governance warnings, broken assets, source placeholders, and non-public route leakage.

The emergency repair was therefore limited to `site/public/` files and did not weaken corpus governance, route locks, source validation, or publication gates.

### Implemented Public Surface Repair

PR #92 repaired the visible public surface by introducing clean public pages for the currently exposed routes:

- `/`
- `/en/`
- `/de/`
- `/what-is-bisulfid/`
- `/bisulfid-vs-bisulfide/`
- `/glossary/`
- `/sources/`
- `/acquire/`

The repair removed public exposure of:

- GitHub Pages 404 from `/en/`
- Draft/governance language from `/de/`
- `[SOURCE REQUIRED]` public markers
- "not public", "not indexable", "publication blocker", and similar internal state language
- Broken image references
- Raw/default navigation behavior
- Public links to unrepaired/non-public routes

### Governance Principle Confirmed

No public-facing page may expose internal governance language unless the page itself is explicitly designed as a public governance explainer.

Internal phrases such as:

- `SOURCE REQUIRED`
- `draft`
- `not public`
- `not indexable`
- `publication blocker`
- `not in sitemap`
- `claim approval not implied`

must remain inside the governance/corpus layer and must not leak into public-facing pages.

Public source discipline may be explained conceptually, but not by exposing internal validation markers.

### Public Linking Rule

The homepage and public navigation must link only to routes that meet all of the following conditions:

- The route exists.
- The route does not return 404.
- The route has no broken images.
- The route does not expose draft/governance warnings.
- The route uses the public visual shell.
- The route is suitable for a public visitor.

Routes that do not meet these conditions must remain unlinked from the public surface until repaired.

### Strategic Interpretation

This repair is not the final Bisulfid interface. It is a public-surface stabilization layer.

Its purpose is to prevent trust damage while preserving the deeper governed corpus strategy. The site can now remain publicly visible without exposing broken routes or internal validation language, while the larger 14,000-page governed corpus remains under strict source and publication control.

### Next Required Phase

*(Superseded — executed as Sprint 93 through Sprint 98; see decision entries below.)*

### Permanent Decision

Bisulfid.com must never again expose internal corpus governance output directly to the public surface unless explicitly approved as a public governance document.

The public surface must remain small, clean, controlled, source-disciplined, and visitor-safe until the full governed corpus is ready for controlled publication.

---

## Decision: Public Surface Integrity Repair — Governance Decision Recorded

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PRs:** #92, #95  
**Scope:** Decision-log governance continuity; public-surface repair doctrine

### Context

PR #92 implemented the emergency public-surface repair documented above. PR #95 recorded the same governance principle in the decision log so the separation rule between internal corpus layers and public visitor pages would not be lost across later sprints.

### Decision

The public surface integrity repair doctrine is a permanent governance rule, not a one-time patch. Internal draft, source-lock, validation, and publication-blocker language must never leak into public visitor pages unless a route is explicitly published as public governance documentation.

### Outcome

The repair rule is preserved in this decision log. Later public atlas waves (Sprint 97A, Sprint 98) inherit the same constraint: public pages must be clean, intentional, and free from governance leakage.

---

## Decision: Sprint 93 — Public Interface Refinement and Mobile Authority Pass

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #96  
**Scope:** Public shell refinement — mobile navigation, typography, active states, homepage thesis

### Context

After PR #92 stabilized the visible public surface, the site remained functionally clean but not yet sovereign-grade on mobile or in navigational authority. Ordinary website behavior, weak typographic hierarchy, and incomplete mobile treatment remained visible on the small public layer.

### Decision

The public shell may be refined for mobile authority, active route states, glossary card treatment, stronger homepage thesis, footer architecture, and German/English spelling-boundary interface language — without publishing the 14,000-route corpus and without weakening source or claim locks.

### Outcome

Sprint 93 improved the repaired public surface toward a more deliberate sovereign interface. This refinement applied only to the small visible public layer, not to the governed 14K scaffold.

---

## Decision: Deploy Gate Alignment for Public Surface Expansion

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #93  
**Scope:** GitHub Pages public deploy workflow; page-count deployment gate

### Context

Public-surface repairs and additions changed the number of generated public HTML files served by GitHub Pages. The deployment gate expected a fixed page count that no longer matched verified public output after `/en/index.html` and related public-surface changes.

### Decision

Deployment count gates may be updated to match verified generated public output, but must never be used to bypass source discipline, claim approval, corpus publication locks, or release-ledger governance.

### Outcome

The deploy gate was aligned so the repaired public surface could deploy successfully. Gate updates are operational alignment only — not publication authorization.

---

## Decision: Public Atlas Compliance Patch

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #96  
**Scope:** Existing public pages, `/languages/`, sitemap, robots, public CSS

### Context

The repaired public surface was clean but not yet atlas-compliant. Public pages lacked several minimum atlas-page requirements: breadcrumbs, source-posture sections, sufficient internal links, active navigation state, and a truthful sitemap/robots layer.

### Decision

Public pages must meet atlas-page minimums before being linked or indexed. Minimums include title, meta description, canonical, breadcrumbs, source posture, meaningful internal links, and footer atlas navigation where applicable.

PR #96 improved the visible public layer by:

- adding `/languages/`
- adding breadcrumbs
- adding source-posture sections
- adding internal links
- improving active navigation state
- adding glossary mobile card treatment
- creating `robots.txt`
- creating a truthful public `sitemap.xml`

### Outcome

The visible public layer became cleaner and more indexable, but still represented only a small public surface — not the full 14,000-route atlas.

---

## Decision: 14K Public Release Blocker Truth

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Scope:** 14,000-route corpus scaffold; publication doctrine

### Context

A blocker analysis established the true state of the 14K corpus:

- 14,000 routes existed in `routes.json`
- 14,002 generated HTML files existed under `site/public/`
- source markdown files existed
- all 14,000 routes remained `planned`
- zero corpus routes were published as real reference pages
- 13,971 routes required verified sources
- almost all corpus bodies still contained `[SOURCE REQUIRED]`
- real written reference body content did not exist at atlas scale

The scaffold was governance output and structural HTML — not a completed sovereign reference atlas.

### Decision

The 14,000-route scaffold must not be published as if it were a completed reference atlas. Publishing boilerplate, thin, or source-required pages would violate Bisulfid's sovereign reference doctrine.

Fake publication to hit page-count targets is prohibited.

### Outcome

The project shifted from attempting direct 14K publication toward building a source-pack, claim-library, and release-ledger-driven production system.

---

## Decision: Public Atlas Wave 1

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #97  
**Scope:** First real public indexable atlas wave (Sprint 97A)

### Context

After public-surface repair and compliance patching, Bisulfid needed its first wave of real public atlas pages — not scaffold overwrites presented as live reference content.

### Decision

Wave-based release is acceptable only when pages are real, public-safe, internally linked, indexable, and free from governance leakage. Wave release does not authorize bulk publication of the 14K scaffold.

Sprint 97A produced the first real public atlas wave:

- 52 real indexable pages written
- 39 new directories
- 13 scaffold overwrites
- sitemap expanded to 60 entries
- public routes verified from sitemap
- 14K scaffold governance left untouched

### Outcome

Bisulfid moved from a small repaired public surface to the first visible indexable atlas layer. The full 14,000-page corpus was not claimed live.

---

## Decision: Route Path Reality and Sitemap as Source of Truth

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Scope:** Public route verification; live indexing workflow

### Context

Live verification showed that some expected nested routes — such as `/materials/mos2/` or `/languages/sulfid-vs-sulfide/` — were not present in the public sitemap. Sprint 97A published several pages as root-level routes such as `/molybdenum-disulfide/`, `/sulfur-compounds/`, and `/sulfid-vs-sulfide/`.

### Decision

For live verification, Google submission, and internal release auditing, `sitemap.xml` and sitemap shards are the source of truth for currently public indexable routes. Expected route patterns must not be assumed unless present in the sitemap or release ledger.

### Outcome

Future route cleanup may add aliases or canonical redirects. No public indexing workflow may rely on guessed routes.

---

## Decision: Sprint 98 — 14K Sovereign Reference Atlas Production Pipeline

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #98  
**Scope:** 14K production pipeline, source packs, claim library, release ledger, sitemap shards

### Context

After Wave 1, Bisulfid required an operational system to scale from a small public atlas toward the full 14,000-route reference corpus without publishing fake, thin, or unsupported pages.

### Decision

The path to 14K must proceed through:

verified source packs → approved claims → release ledger → governed rendering → sitemap inclusion → validation → deployment

No page may bypass this chain. The release ledger is the source of truth for which routes are public.

Sprint 98 created the operational production system:

- classified all 14,000 routes into production lanes A–M + HUB
- released 26 clean public atlas hub pages (foundation, methodology, index maps, home, sources)
- blocked 13,974 source-required terminology routes
- created source-pack architecture (`main/data/source_packs/source_pack_registry.json`)
- created claim-library architecture (`main/data/claims/claim_library.json`)
- created page-type templates (`main/data/atlas_page_type_templates.json`, `main/templates/atlas/`)
- created audience-layer partials
- created internal link graph for hub pages
- created release ledger (`main/data/release_ledger.json`)
- created sitemap index and shards (`sitemap.xml`, `sitemap-core.xml`, `sitemap-languages.xml`, `sitemap-context.xml`)
- created production runtime (`scripts/atlas_production_runtime_l2.py`)
- created public-release validator (`scripts/atlas_validate_public_release_l1.py`)
- validation passed
- blocker reports documented why the 500-page expansion threshold was not met

Hub pages use curated cautious-framing content only. Governance draft markdown is not dumped into public output.

### Outcome

Bisulfid now has a measurable production pipeline for scaling from hub pages toward the full 14K reference atlas without publishing fake or unsupported pages. **26 hub pages are public; 13,974 terminology routes remain blocked.** The full 14,000-page atlas is not live.

---

## Decision: Claim Library Lock Compliance

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related commit:** `c07e2c3c6`  
**Scope:** `main/data/claims/claim_library.json`, `.gitignore`

### Context

Sprint 98 initially failed CI in Layer 1 corpus validation because `claim_library.json` used `status: architecture_active`, while L1 claim registry governance requires all claim registry files under `main/data/claims/` to remain `inactive` unless explicitly opened by governance.

### Decision

`claim_library.json` must remain `status: inactive` until claim publication is explicitly authorized by governance. Architectural presence of a claim library does not imply publication readiness or route unlock.

Python cache artifacts (`__pycache__/`, `*.pyc`) must never enter version control.

### Outcome

The claim library remains architecturally present but publication-locked. CI corpus validation passes. `.gitignore` excludes Python cache artifacts.

---

## Current Standing After Sprint 98

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Status:** Operational checkpoint — production pipeline live; full corpus not public

### What Bisulfid.com now has

- public atlas surface (repaired, refined, compliance-patched)
- first public atlas wave (52 indexable pages, Sprint 97A)
- Sprint 98 hub release (26 additional governed hub pages via release ledger)
- sitemap infrastructure (index + shards)
- source-pack architecture (8 packs defined; no invented sources)
- claim-library architecture (publication-locked registry)
- release ledger (source of truth for public routes)
- 14K corpus classification (all 14,000 routes classified into production lanes)
- validation runtime (L1 corpus validation + Sprint 98 public-release validator)
- blocker transparency (`BLOCKERS_TO_14K_PUBLIC_RELEASE.md`)

### What is not yet public

- the full 14,000-page reference atlas
- the terminology corpus at scale (13,974 routes blocked — source-required)
- verified source-pack coverage sufficient for 500+ page expansion
- approved claim coverage sufficient for terminology lane release

The 14K route scaffold is classified and operationally measurable. It is not published as completed reference content.

### Publication rule (permanent)

Public release must proceed only through:

1. verified source packs  
2. approved claims  
3. release ledger authorization  
4. governed rendering (no governance draft leakage)  
5. sitemap inclusion  
6. validation pass  
7. deployment  

### Next approved path

*(Superseded — executed as Sprint 99 through Sprint 99B-H; see decision entries below. SPK-LEX-EN-MW terminology lane wave was not started.)*

---

## Decision: Sprint 99 — 14K Public Reference Dossier Release

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #100  
**Scope:** 14K public reference dossier release; release ledger; sitemap shards; governed rendering

### Context

After Sprint 98 established the production pipeline and blocked 13,974 source-required routes, Bisulfid required a controlled public release of reference-grade dossier pages at atlas scale — without falsely presenting the corpus as fully source-verified scientific articles.

### Decision

Public dossier release at 14K scale is authorized only when pages use cautious reference framing, pass validation, appear in the release ledger and sitemap, and do not convert source-required terminology into unsupported scientific claims.

Sprint 99 released the first full public reference dossier atlas wave:

- 14,000 routes audited
- **13,998 public dossier pages released**
- **2 routes blocked:** `acquire`, `newsletter`
- **13,998 sitemap URLs** across **9 shards**
- release model distribution:
  - `cautious_reference_dossier`: 13,846
  - `source_verified_page`: 152
  - `blocked_high_risk`: 2
- validation **PASS**
- `routes.json` **unchanged**
- corpus governance **preserved**
- `claim_library.json` remained **`inactive`**
- source-required terminology corpus was **not** falsely converted into source-verified scientific articles

### Honest framing (permanent)

Bisulfid.com is a **public reference dossier atlas**, not 14,000 fully source-verified scientific articles. Dossier pages provide governed structure, terminology orientation, and cautious context — not primary-source scientific publication.

### Outcome

The 13,998-page public reference dossier atlas was released to `main` via PR #100. The full terminology corpus remains source-disciplined; only ledger-authorized dossier pages are public.

---

## Decision: Sprint 99A — 14K Public Dossier Quality Repair

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #101  
**Scope:** Public dossier quality gate; CSS shell; forbidden-string removal; breadcrumb and footer repair

### Context

After Sprint 99 released 13,998 dossier pages, live and validation review found quality defects: missing sovereign stylesheet contract, visible internal machine labels, draft language, forbidden strings, duplicate breadcrumb entries, and incorrect footer hub paths.

### Decision

All released public dossier pages must pass a quality repair gate before further interface work or Search Console submission. Repairs must not expand the corpus, alter `routes.json`, or activate the claim library.

Sprint 99A repaired all **13,998 released pages**:

- sovereign CSS shell applied through `/assets/bisulfid-design-system/bisulfid-frame.css`
- visible internal labels removed (`Lane A`, `terminology_node`, `cautious_reference_dossier`, etc.)
- draft language removed
- forbidden strings removed
- duplicate breadcrumb Atlas link removed
- footer hub paths corrected
- validation **PASS**
- sitemap URL count **unchanged** (13,998)
- `routes.json` **unchanged**
- no corpus/source-pack expansion started

### Outcome

PR #101 merged Sprint 99A on top of PR #100. `main` contained the quality-repaired 13,998-page public atlas.

---

## Decision: PR #100 and PR #101 Publication Chain

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PRs:** #100, #101  
**Scope:** Merge sequence; deployment from `main`

### Context

Sprint 99 and Sprint 99A were delivered as sequential PRs to preserve reviewability between initial 14K release and quality repair.

### Decision

- **PR #100** merged Sprint 99 — 14K dossier release
- **PR #101** merged Sprint 99A — quality repair gate
- `main` contained the **13,998-page public atlas** after Sprint 99A
- **Pages public deploy ran successfully from `main`** after merge

### Outcome

The public atlas was live-deployed with quality repairs applied. Deployment authorized only ledger-listed routes; governance files remained unchanged.

---

## Decision: Sprint 99B — Semantic Sovereign Shell Repair

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Scope:** Semantic interface system; CSS contract; sovereign shell; lane/domain body classes

### Context

After Sprint 99A, dossier pages linked `bisulfid-frame.css` but still rendered with weak or default interface behavior. Root cause: template class names (`atlas-header`, `atlas-footer`) were not aligned with design-system shell classes (`bs-control-room`, `site-header`, `site-footer`). `public-surface.css` and lane-specific semantic CSS were not chained into the frame bundle.

### Decision

Every public dossier page must render through a single sovereign shell contract and carry semantic lane/domain/audience classes for governed interface treatment — not decorative CSS alone.

Sprint 99B implemented the semantic sovereign interface system:

- **Root cause addressed:** dossier pages linked `bisulfid-frame.css`, but template classes and design-system classes were not fully aligned
- `bisulfid-frame.css` imported `public-surface.css` and `atlas-semantic-interface.css`
- all dossier pages moved into the sovereign shell contract:
  `bs-control-room` → `bs-control-room__shell` → `site-header` → `#main-content` → `site-footer`
- body classes and `data-atlas-lane` attributes introduced for semantic styling:
  `atlas-lane-terminology`, `atlas-lane-language`, `atlas-lane-compound`, `atlas-lane-material`, `atlas-lane-methodology`, domain classes, audience classes
- human-facing labels replaced machine-facing labels
- strategic interface components added (`atlas-dossier-hero`, `atlas-role-panel`, `atlas-context-layer-grid`, etc.)
- validation **PASS:**
  - released pages: **13,998**
  - sitemap URLs: **13,998**
  - CSS import errors: **0**
  - shell failures: **0**
  - lane failures: **0**
  - sample failures: **0**

### Outcome

All 13,998 dossier pages render with the sovereign semantic shell. Deep routes no longer present as raw/default HTML.

---

## Decision: Sprint 99B-H — Legacy Hub Semantic Shell Alignment

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Scope:** Legacy public hub entry pages; hub template; semantic shell parity with dossier pages

### Context

Sprint 99B validation showed all 13,998 dossier pages passing, but manual sample review found legacy hub entry routes (`/atlas/`, `/terms/`, `/compounds/`, etc.) still outside the semantic shell. These hubs are public entry points and must not present a different interface contract than dossier pages.

### Decision

All public hub and legacy entry pages must use the same sovereign semantic interface shell as dossier pages before Search Console submission. Hub alignment must preserve public-safe content, canonical/meta/title, and sitemap structure.

Sprint 99B-H aligned legacy hub routes:

- `/`
- `/atlas/`
- `/terms/`
- `/compounds/`
- `/materials/`
- `/languages/`
- `/methodology/`
- `/sources/`
- `/glossary/`
- `/what-is-bisulfid/`
- `/bisulfid-vs-bisulfide/`
- `/de/`

Repairs included:

- hub template introduced (`main/templates/atlas/hub.html`) and aligned via `scripts/atlas_align_legacy_hubs_99bh.py`
- forbidden strings sanitized in preserved hub body content
- duplicate `public-surface.css` links removed (frame import chain only)
- semantic lane/domain/audience classes applied per hub role
- validation **PASS:**
  - **13,998 dossier pages PASS**
  - **12 hub entry pages PASS**
  - sitemap **PASS**
  - CSS import chain **PASS**
  - hub samples **PASS**

### Outcome

Homepage, atlas hubs, and deep dossier routes share the same sovereign semantic shell contract.

---

## Decision: Deployment After Sprint 99B-H

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Related PR:** #102  
**Branch:** `fix/sprint-99b-semantic-interface`  
**Scope:** Semantic interface runtime; CI; Pages public deploy

### Context

Sprint 99B and 99B-H required a full render-align-validate cycle before live deployment.

### Decision

Deployment proceeds only after semantic interface runtime passes end-to-end validation.

Execution record:

- branch `fix/sprint-99b-semantic-interface` created
- semantic interface runtime executed:
  `py -3 scripts/atlas_semantic_interface_runtime_99b.py`
- runtime result:
  - rendered: **13,998**
  - aligned hubs: **12**
  - CSS import errors: **0**
  - shell failures: **0**
  - lane failures: **0**
  - hub failures: **0**
  - sample checked: **56**
  - validation summary: **PASS**
- **PR #102** / semantic shell fix branch passed **Corpus Governance CI**
- **Pages public deploy #16 succeeded** from `main`
- live site displayed the repaired semantic shell

### Outcome

Bisulfid.com deployed with 13,998 dossier pages and 12 aligned hub entry pages under the semantic sovereign shell.

---

## Decision: Critical Design Finding After Sprint 99B-H

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Scope:** Conceptual interface depth; Search Console submission pause

### Context

Although the site became technically valid, indexable, and semantically structured after Sprint 99B-H, manual review found the interface had become too generic. Pages retained the color palette but lost part of the earlier sovereign conceptual interface language.

### Decision

The issue is **not** deployment, sitemap, or indexability. The issue is **conceptual interface depth:**

- missing stronger control-room feeling
- underused sulfur/language-boundary visual system
- weak distinction between terminology, language, materials, compound, methodology, and audience layers
- homepage reads too much like a generic dossier

**Search Console submission is intentionally paused** until conceptual interface restoration is completed.

### Outcome

Technical readiness and interface sovereignty are decoupled. Crawlability does not authorize Search Console submission until the distinctive sovereign chemical-language control-room interface is restored.

---

## Decision: Sprint 99C — Sovereign Conceptual Interface Restoration (Approved Next Phase)

**Date:** 2026-06-05  
**Asset:** Bisulfid.com  
**Decision status:** Approved — not yet executed  
**Scope:** Template/CSS/copy sanitation; conceptual interface depth recovery

### Context

Sprint 99B-H achieved shell contract parity and validation pass, but manual review confirmed insufficient conceptual interface differentiation across atlas lanes and entry pages.

### Decision

**Sprint 99C is approved** as the next phase. Sprint 99C must restore the sovereign conceptual interface **without** changing route count or sitemap inventory.

Sprint 99C constraints:

- template/CSS/copy sanitation **only**
- **preserve:**
  - 13,998 public URLs
  - 9 sitemap shards
  - `robots.txt`
  - `routes.json`
  - release ledger
  - `claim_library` inactive status
  - corpus governance
  - no new unsupported scientific claims
- **must not:**
  - start SPK-LEX-EN-MW
  - expand source packs or claim library activation
  - add or remove released routes

### Acceptance criterion

Bisulfid.com must remain **technically valid** while recovering the **distinctive sovereign chemical-language control-room interface** — terminology, language-boundary, materials, compound, methodology, and audience layers must be visually and structurally distinguishable without governance leakage.

### Outcome

*(Executed — see Sprint 99C decision entry below.)*

---

## Decision: Sprint 99C — Sovereign Conceptual Interface Restoration

**Date:** 2026-06-06  
**Asset:** Bisulfid.com  
**Decision status:** Accepted  
**Scope:** Template/CSS/copy sanitation; control-room conceptual interface; no URL surface change

### Context

After Sprint 99B-H, the public atlas was technically valid and semantically structured, but manual review found the interface too generic: control-room depth, sulfur/language-boundary visual language, and lane differentiation were under-expressed. Search Console submission remained paused.

### Decision

Sprint 99C restores the sovereign chemical-language control-room interface through template, CSS, and copy sanitation only — without changing the 13,998 released URL surface, sitemap inventory, or corpus governance locks.

Sprint 99C applied:

- **Control-room shell on every page:** `atlas-control-strip`, `bs-control-room-hero` with glow/perspective, `atlas-control-room-page`
- **Lane-specific interface preludes** using design-system components:
  - hub command entry (`bs-relation-lattice`, `bs-term-node`)
  - terminology term-node lattice
  - language missing-E boundary (`bs-missing-e-boundary-system`, `bs-language-depth`)
  - compound crystal mapping
  - material strata panels
  - governance source crystal (`bs-source-crystal`)
  - audience-layer beacons
- **Copy repair:** removed duplicated "dossier dossier" phrasing; summaries use governed role pages
- **CSS restoration:** Sprint 99C block in `atlas-semantic-interface.css` — lane atmosphere, hub command hero, prelude treatments
- **Regenerated:** 13,998 dossier pages + 12 hub entry pages
- **Preserved:** `routes.json`, release ledger, `claim_library.json` inactive, 9 sitemap shards (13,998 URLs), `robots.txt`
- **Not started:** SPK-LEX-EN-MW, new logo, corpus/source-pack expansion

Validation **PASS:**

- released pages: **13,998**
- hub entry pages: **12**
- sitemap URLs: **13,998**
- conceptual marker failures: **0**
- dossier duplication failures: **0**
- forbidden string / governance leakage: **0**
- corpus claims L1: **PASS**

Runtime: `py -3 scripts/atlas_conceptual_interface_runtime_99c.py`

### Outcome

Bisulfid.com retains full technical indexability while visibly recovering the sovereign chemical-language control-room identity. Hub pages read as command entries; terminology, language, materials, compound, methodology, and audience layers are structurally distinguishable. Search Console submission may proceed after manual live verification — not automatically from this sprint alone.

---

## Current Standing After Sprint 99C

**Date:** 2026-06-06  
**Asset:** Bisulfid.com  
**Status:** Live 13,998-page public reference dossier atlas — technically and conceptually restored; ready for manual live verification before Search Console

### What Bisulfid.com now has

- **live 13,998-page public reference dossier atlas**
- sharded sitemap infrastructure (9 shards, 13,998 URLs)
- `robots.txt`
- CI-passing governance posture (Corpus Governance CI)
- Sprint 99B semantic shell + Sprint 99C conceptual control-room interface
- lane-specific preludes (terminology lattice, language boundary, compound crystal, material strata, governance crystal)
- Sprint 99B-H legacy hub shell alignment (12 public entry routes)
- release ledger as source of truth for public routes
- `claim_library.json` remains **inactive**
- `routes.json` unchanged since 14K release wave

### What remains paused

- **SPK-LEX-EN-MW terminology lane wave** — not started
- claim library activation — not authorized
- new BISULFID logo — not deployed

### Honest publication framing (permanent)

Bisulfid.com is a **governed public reference dossier atlas** — not 14,000 fully source-verified scientific articles.

### Next step

Manual live verification of hub and deep-route samples, then Search Console submission when confirmed.

---

## Sprint — Authority & Dimension Reconciliation (implementation 1: governance scaffolding)

**Date:** 2026-09-19
**Scope:** governance scaffolding only. No production data, HTML, sitemap, robots, Search Console, route publication/indexation flags, source statuses, claim statuses, ontology, or corpus content modified. No new public routes. No PR.
**Baseline:** `DOCTRINE_TO_CORPUS_RECONCILIATION.md` v2; `BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md` incl. Architecture Integrity Pass (IP-1…IP-16).

### Ratified principle (owner-approved) — Contract C: Derived Canonical State

The following **principles** are ratified as the target authority architecture:

1. **Publication and indexation are derived states**, not hand-set flags. Deploy, sitemap, and robots consume only the derived state.
2. **No single legacy file independently controls indexation.**
3. **`routes.json` owns governed route posture.**
4. **`release_ledger.json` owns release authorization + the historical release record.**
5. **Source, evidence, claim, validation, and Information-Gain are independent veto/eligibility inputs** to the derived state; each can veto, none alone can promote.
6. **Knowledge Object Before URL** — an independent URL is promoted only after evidence sufficiency AND Information-Gain review; a knowledge object may otherwise remain a module, section, relationship edge, table/data record, or machine-readable node.
7. **Semantic dimensions remain distinct** — entity, subject_domain, reference_layer, audience, page_type, language, geography, jurisdiction, relationship, temporal_scope, evidence — and none alone creates a URL.
8. **Source ≠ Evidence ≠ Claim** — three independently-owned postures.
9. **One fact → one authoritative owner** — every other representation is derived (no duplicated authoritative fields).
10. **Vocabulary existence ≠ relationship-instance truth** — a place/domain/relationship-class may be registered without evidence; an instantiated relationship requires evidence.

### Historical fact preserved

Sprint 99 (2026-06-05) authorized the release of 13,998 dossier pages under "cautious reference framing" and declared the release ledger the public-route source of truth. **This remains a historical fact and is not erased.** Contract C supersedes only its *operational effect on indexation*; the existing corpus is **not** de-indexed by this entry, and its indexation will be recomputed from true postures only under a later, separately-approved sprint.

### NOT ratified here (remain provisional — must not be treated as settled doctrine)

- Concept↔Lexeme representation (blocks any ontology mutation and any real MoS₂ evidence record);
- source-lock workflow;
- claim-registry activation policy;
- final subject-domain admissions (which reserved domains become evidence_active);
- final relationship-class admissions and any relationship instances;
- new audience admissions;
- 14K disposition policy;
- the exact Contract C transition constants / non-factual-class certification list.

### Scaffolding created this sprint (control infrastructure only)

- `main/data/subject_domain_registry.json` (registered vocabulary; none evidence_active)
- `main/data/geography_registry.json` (place identities only; no evidence state)
- `main/data/jurisdiction_registry.json` (schema + identity; no active instruments)
- `main/data/relationship_class_registry.json` (classes only; zero instances)
- `main/data/evidence/` (schema + README + test-only fixtures; **no real evidence record**; `EVD-MOS2-DE-001` deferred pending Concept↔Lexeme ratification)
- `main/data/information_gain/calibration_pairs.json` (empty; five labels; no threshold)
- `scripts/governance_scaffolding/` (Contract C derive spec + 7 property tests + scaffolding validator; **unwired from deploy/CI**)

Contract C property tests: PASS (7/7, 23,040 combinations). Scaffolding validator: PASS (105 checks). Existing Corpus Governance CI (L0/L1/L2) re-run: PASS (unaffected).

---

## Sprint — Concept ↔ Lexeme Resolution

**Date:** 2026-09-19
**Scope:** design + minimal schema. No 14K route, release ledger, public HTML, sitemap, robots, Search Console, indexation posture, source status, or claim status modified. The live ontology `sulfur_terms.json` is **not mutated**. No new public routes. No PR.
**Baseline:** `DOCTRINE_TO_CORPUS_RECONCILIATION.md`, `BISULFID_AUTHORITY_DIMENSION_ARCHITECTURE.md` (incl. IP-16), scaffolding commit `ae7980fe06`.

### Ratified (narrow)

1. **Concept and Lexeme are distinct semantic object types.**
2. **Concepts are language-neutral;** internal `concept_id` strings are identifiers, not language claims.
3. **Lexemes are language-specific naming forms;** every lexeme resolves to exactly one governed concept.
4. **Evidence and claims attach to the semantic level they actually support** (`claim_level ∈ {concept, lexeme, relationship}`); lexical evidence can never satisfy a concept-level chemical claim.
5. **Lexeme existence does not create a URL** (Knowledge Object Before URL remains absolute).
6. **Chosen model: Option B** — concept graph stays in `main/data/ontology/sulfur_terms.json`; a new `main/data/lexeme_registry.json` holds lexemes (least disruptive, cleanest multilingual scaling, no duplicated authority). Full rationale + ontology-node audit/migration mapping: `main/data/CONCEPT_LEXEME_MODEL.md`.

### NOT ratified (remain provisional)

- Any collapse of `sodium_bisulfide`/`sodium_hydrosulfide` (needs equivalence evidence);
- the HS⁻ grouping of `bisulfid`/`bisulfide`/`hydrosulfide` (high-risk; migration);
- folding `molybdenum_disulfide_mos2` into a formula-alias lexeme (recommended; deferred to migration);
- source-lock workflow, claim-registry activation, 14K disposition — unchanged from prior sprints.

### Schema corrections (no real legacy data depended on them)

- **Evidence schema:** generic `entities` → explicit `concept_ids` + `lexeme_ids`; added `claim_level`; **`risk_class` removed** (no independent meaning vs route/claim/source risk — `CONCEPT_LEXEME_MODEL.md` §7); `source_type`/`used_by`/`confidence` remain forbidden.
- **`GEO-GULF` → `GEO-GCC`** ("GCC member states") — its members were exactly the six GCC states; a broader Gulf-region scope, if needed, will be a separate governed object.
- **Jurisdiction model separated** into distinct `jurisdiction` → `authority` → `instrument` records (a jurisdiction is no longer "authority + instrument"); all record lists empty.
- **Trade/economic relationship classes** (importer/exporter/producer/industrial_user) now require **primary authoritative** source categories; `market_report`/`industry_publication` reclassified secondary/contextual. Proposed new source-taxonomy categories (`official_customs_data`, `official_trade_statistics`, `national_statistical_authority`, `intergovernmental_trade_database`, `official_production_statistics`) are recorded as **proposals only** — not added to `source_registry.json`, no sources invented.

### First real governed evidence object (created; NOT published)

Chain: `molybdenum_disulfide` (concept) → `LEX-DE-MOS2-001` "Molybdän(IV)-sulfid" (lexeme) → `EVD-MOS2-DE-001` (lexeme-level, terminological, de) → `SRC-SPEKTRUM-MOS2-DE` (verified; lock **candidate**, unchanged) → `CLM-TERM-MOS2-DE-001` (approved; registry **inactive**, unchanged). Created strictly within already-verified source and already-approved claim scope; changes no source/claim status; authorizes no route. **Derived Contract-C state = (not_public, noindex).**

Validators: scaffolding PASS (131 checks); concept↔lexeme PASS (16 checks, 1 lexeme, 1 governed evidence record); Contract C property tests PASS (7/7); existing Corpus Governance CI (L0/L1/L2) PASS (unaffected).

---

## Sprint — Semantic Integrity Hardening

**Date:** 2026-09-19
**Scope:** narrow hardening of the NEW governance architecture only. No 14K route, release ledger, public HTML, sitemap, robots, Search Console, indexation, source status, or claim status changed. Live ontology `sulfur_terms.json` **not** mutated. No new public URL. No source acquisition. No relationship instances. No PR.
**Baseline:** commit `c299af81c1`.

### Ratified (narrow)

1. **The lexeme registry owns lexical identity, not evidence backlinks.** `source_ids`/`evidence_ids` removed from lexeme records; reverse `lexeme→evidence` view is derived. One relationship fact → one authoritative direction → reverse edges derived.
2. **Lexeme registration state ≠ evidence support.** `registration_state` is the manual lexical-identity fact; evidence support is derived from the evidence store (single authority).
3. **Concept eligibility is explicitly governed.** New sidecar `main/data/ontology_node_roles.json`; existence of a legacy ontology term_id does **not** make it a Concept target. Only `concept_eligible` nodes may be `concept_id` targets.
4. **Relationship facts use typed subject → predicate → object semantics;** endpoint contracts per class; inverse views derived; the data encodes the real proposition direction.
5. **Language and geography are orthogonal;** geography is never derived from a lexeme's language.
6. **Evidence transformations cannot broaden an approved claim's scope** (MoS₂ narrowed `accepted` → `observed_usage`; `claim_scope` mirrors `CLM-TERM-MOS2-DE-001`; the approved claim was not modified).

*No specific trade/geography fact is ratified.*

### Ontology node roles (all 14 legacy nodes classified; ontology unchanged)

concept_eligible (6): `sulfur`, `sulfide`, `disulfide`, `hydrosulfide`, `hydrogen_sulfide`, `molybdenum_disulfide`. legacy_lexeme (2): `sulfid`, `disulfid`. conflated_pending_migration (4): `bisulfid`, `bisulfide`, `sodium_bisulfide`, `sodium_hydrosulfide`. notation_alias (1): `molybdenum_disulfide_mos2`. control_object (1): `bisulfite_disambiguation`.

### MoS₂ chain (unchanged status; still not published)

`molybdenum_disulfide` (concept_eligible) → `LEX-DE-MOS2-001` (`observed_usage`, de, `registration_state=registered`, no backlinks) → `EVD-MOS2-DE-001` (lexeme-level; `claim_scope` mirrors the approved claim) → `SRC-SPEKTRUM-MOS2-DE` (verified; lock **candidate**, unchanged) → `CLM-TERM-MOS2-DE-001` (approved; registry **inactive**, unchanged). **Derived Contract-C state = (not_public, noindex).**

Validators/tests: scaffolding PASS (153 checks); concept↔lexeme PASS (47 checks); relationship grammar tests PASS (8/8, synthetic; correct directions accepted, reversed rejected); Contract C property tests PASS (7/7); existing Corpus Governance CI (L0/L1/L2) PASS (unaffected).

---

## Sprint — Source Qualification & Evidence Admission Protocol

**Date:** 2026-09-19
**Scope:** design + minimal schema + validators. No 14K route, release ledger, ontology, public HTML, sitemap, robots, Search Console, indexation, source status/lock, or claim status changed. No external source acquired. No relationship instance. No registry activated. No PR.
**Baseline:** commit `41aeb1f56f`.

### Ratified principles

1. **Source authority is use-scoped.** A verified/locked source is not universally authoritative.
2. **Source category alone is insufficient** to admit evidence.
3. **Source identity, source-use qualification, evidence review, claim approval, and publication are distinct layers** — none silently implies another.
4. **Evidence admission is domain/claim-level/scope aware** (`admissible(source, qualification, context)` is deterministic; category alone never returns admissible).
5. **Qualification can regress without deleting history;** downstream privilege moves equal-or-lower, never higher.
6. **Official/original evidence is mandatory where official status itself is claimed** (current-law → governing instrument; importer/exporter → official records, not market/industry pubs alone).
7. **Source qualification never authorizes route publication.**

*No external factual claim (trade/geography/etc.) is ratified.*

### `source_lock_status` decision — Option B

Remains a bibliographic/source-record stability lock (historical Sprint 5N-R meaning preserved) and is **explicitly insufficient** without a source-use qualification. Not modified this sprint (all 15 stay `candidate`).

### Architecture created (machine-readable, unwired from deploy/CI)

- `source_use_qualification_registry.json` — use-scoped qualification (states candidate→reviewed→qualified_narrow→qualified, +suspended/superseded); references exactly one source; duplicates no bibliographic metadata. One record: `QUAL-SPEKTRUM-MOS2-DE-001` (qualified_narrow), mirroring the already-reviewed Spektrum MoS₂ scope — broadens nothing.
- `source_admissibility_policy.json` — evidence roles; 7 newly-ratified categories (policy vocabulary only, not written to source_registry); category→role map; domain admissibility matrix; sufficiency patterns; 9 hard rules.
- `evidence_admission_policy.json` — evidence-review lifecycle transitions; type-specific locators; version/temporal/freshness; regression; conflicting-evidence representation; quantitative/legal/scientific admission provenance.
- `claim_activation_policy.json` — four independent claim layers; finding that registry-wide activation is too coarse; scoped per-claim activation **proposal** (not applied). Nothing activated.
- `SOURCE_QUALIFICATION_PROTOCOL.md` + `SOURCE_REGISTRY_QUALIFICATION_AUDIT.md` (design + 15-source audit).
- `scripts/governance_scaffolding/source_admissibility.py` + `source_admissibility_tests.py`.

### 15-source audit outcome

14 sources `seeded` → **no qualification granted** (pending scope review). 1 source (`SRC-SPEKTRUM-MOS2-DE`, verified) → one narrow qualification mirroring its reviewed boundary. No `use_for` broadened; no source promoted for reputation.

### MoS₂ result

`admissible()` = True for the German dictionary-entry terminology/lexeme boundary only; False for concept/scientific/economic/publication uses. `EVD-MOS2-DE-001` stays `scope_reviewed` (not upgraded). Source status/lock, claim, activation, route, release **unchanged**. **Contract-C derived state = (not_public, noindex).**

Validators/tests: scaffolding PASS; concept↔lexeme PASS; relationship grammar PASS (8/8); Contract C PASS (7/7); **source admissibility PASS (13/13 proofs)**; existing Corpus Governance CI (L0/L1/L2) PASS (unaffected).

### Unresolved before real evidence acquisition

Admission rules for the 7 new categories into `source_registry.json`; the scoped per-claim activation mechanism; possible `source_lock_status` deprecation (Option C); corroboration thresholds per domain; biomedical claim-restriction specifics.

---

## Sprint — Admission Enforcement Closure

**Date:** 2026-09-19
**Scope:** enforcement only (make `admissible()` enforce the ratified policy). No 14K route, release ledger, ontology, public HTML, sitemap, robots, Search Console, indexation, claim status, or existing source status/lock change. No external source acquired. No relationship instance. No registry activated. No PR.
**Baseline:** commit `47fa8b5d29`.

### What changed (executable enforcement, still unwired from deploy/CI)

- `admissible()` now enforces **every advertised input**: `allowed_uses` is an **allowlist** (deny-by-default) with `prohibited_uses` as absolute veto; domain `allowed_categories` allowlist (role is an *additional* constraint, not a substitute); declared+permitted `evidence_role`; `geography_limitation`, `jurisdiction_limitation`, `temporal_boundary`; and source-revision match. Category alone still never admits.
- **Source-version ownership (one-fact-one-owner fix):** removed `source_edition` (bibliographic string) from the qualification; added immutable `identity_revision` to the source record (`SRC-SPEKTRUM-MOS2-DE` = `rev-2026-05-30-1`); qualification now carries only `qualified_against_source_revision`. Revision mismatch → review-required (not admissible).
- **Governed `derive_evidence_posture()`** replaces manual assertion of Contract C's evidence input, from admission + review posture + qualification state + source lock + sufficiency + regression. **Qualification suspension regresses** posture automatically (never `evidence_locked`).
- **Executable sufficiency evaluator** for the five patterns, with an **independence** rule (same source/dataset/publisher/study cannot self-corroborate); `multi_source_synthesis` returns `governance_threshold_required` (cannot silently pass).
- **Category vocabulary reconciled:** the 7 ratified categories added to `source_registry.json` `source_categories` (**vocabulary only**, no source uses them, no status/lock change); validator now fails on policy↔registry category drift.
- **Legal context field:** current-law claims require an official instrument; not every regulation-domain sentence is a current-law claim.

### MoS₂

`admissible()` = True only for `cautious_terminology_framing_de_dictionary_entry` (de terminology/lexeme, role primary_authoritative); denies unspecified/other/concept/industry/market/trade uses, Germany-geography inference, jurisdiction inference, temporal-out-of-range, revision mismatch, and publication. `derive_evidence_posture` = `evidence_sufficient` (source lock still `candidate`), so **Contract-C state = (not_public, noindex)**. No source/claim status changed.

### Tests

Source admission enforcement **21/21**; scaffolding validator, concept↔lexeme, relationship grammar (8/8), Contract C (7/7), and existing Corpus Governance CI (L0/L1/L2) all PASS.

### Still unresolved before acquisition

Real-source admission rules per new category; scoped per-claim activation; `source_lock_status` deprecation (Option C); per-domain corroboration/`multi_source_synthesis` thresholds; biomedical claim restrictions.

---

## Pilot 01 — Morocco × Sulfur Trade (first real evidence acquisition)

**Date:** 2026-09-19
**Scope:** `GEO-MA × sulfur × SD-TRADE`, relationship `GEO-MA → REL-IMPORTER → sulfur`. Max 3 claims. No public page, route, sitemap, robots, indexation, 14K, OCP, GCC/China/Germany, or language expansion. No existing source/claim status/lock changed. No claim registry activated. No PR.
**Baseline:** commit `bc20510d4c`.

### Source acquired (official)
Office des Changes (Royaume du Maroc), *Commerce extérieur du Maroc — Rapport annuel 2024* (official PDF). Registered canonically as `SRC-OC-MA-TRADE`, **category `official_trade_statistics`**, `status: seeded`, `source_lock_status: candidate`, `identity_revision: rev-2026-09-19-1`. The login-gated interactive database was not used; no credentials in git. **SOURCE_POLICY preflight:** existing governance permits canonical **seeded (registered/unverified)** registration (14 seeded precedents; all CI stayed green), so canonical registration was used — with `identity_revision` from first registration (no incremental exception).

### Results (3 claims)
- **A — HS classification identity: BLOCKED.** No HS code in the source; no authoritative classification source fetched; label "Soufres bruts et non raffinés" is a crude/unrefined **subset** of the `sulfur` concept. Not fabricated from memory.
- **B — import observation: PROVEN.** Morocco recorded imports of "Soufres bruts et non raffinés" in 2024.
- **C — quantitative measure: PARTIAL.** 2024 **TOTAL import value = 9108 MDH** (T1-10; source literal "9.108", dot = thousands separator), avg unit price **1099 DH/T** (literal "1.099"). ATPA-with-payment 9102 MDH (T3-4) and Asia-origin 8737 MDH (T4-9) are **different scopes**, not variants. **Tonnage BLOCKED** (not stated; not derived). *[Corrected 2026-09-19 — see Pilot 01 Data Semantics Correction below.]*

### Governed outcome (computed, not targeted)
Qualification `QUAL-OC-MA-TRADE-001` = **`reviewed`** (new source not identity-verified → not admitting); and `SD-TRADE` requires primary_plus_corroborating with only one non-independent official source. Governed **evidence posture = `evidence_collecting`**; relationship `REL-INST-MA-SULFUR-IMPORT-2024` = `evidence_collecting`; **Contract-C = `(not_public, noindex)`**.

### Ratified (narrow)
- Source authority is use-scoped and admission is deterministic; a brand-new official source does not admit evidence until identity-verified.
- Trade relationships are directed, period-bounded, evidence-referenced (`GEO-MA → imports → sulfur`, 2024); language ≠ geography still holds.
- Evidence posture is **derived via the admission bridge** (a forged `admitted:true` is ignored).
- **No trade/geography fact is ratified as published.** Nothing activated.

### Policy findings (report only; NOT applied)
1. `primary_plus_corroborating` may be too strict for a narrowly-scoped recorded-observation claim from the national official statistics authority (independent corroboration effectively does not exist — Comtrade/ITC/WITS derive from the same chain). Proposed `single_official_record_sufficient` pattern — deferred.
2. A defined verification path for a new official source is needed before Pilot 02.
3. Quantitative trade admission depends on a classification (HS) identity the summary report lacks → a classification-acquisition step must precede it.
4. Locale numeric normalization + scope discipline (dots are thousands separators; 9108 total vs 9102 ATPA vs 8737 Asia are different scopes, not variants). *[Corrected 2026-09-19.]*

### Tests
Pilot 01 chain **16/16**; source admission enforcement 21/21; scaffolding, concept↔lexeme, relationship grammar 8/8, Contract C 7/7; existing Corpus Governance CI (L0/L1/L2) all PASS. Existing source statuses/locks unchanged (now 15 seeded + 1 verified; all candidate).

### Not started
Pilot 02 (Morocco Industrial Chain / OCP); GCC/China/Germany; language localization; classification acquisition; policy amendments.

---

## Pilot 01 — Data Semantics Correction

**Date:** 2026-09-19
**Scope:** correction only. No new source, no HS classification acquisition, no Pilot 02, no change to source status/lock, claim activation, routes, public HTML, sitemap, robots, indexation, or the 14K. No PR.
**Baseline:** commit `976f25a055`.

Two data-semantics defects in Pilot 01 were corrected after an independent re-check of the official Office des Changes PDF (scope identities confirmed against the extracted text: ATPA appears 51×; T1-10 / T3-4 / T4-9 present):

1. **Locale numeric normalization.** The report's dots are **thousands separators**. Every quantitative measure now stores `source_literal` + `normalized_value` + `unit` + a `numeric_convention` note. Corrected series:
   - **TOTAL imports (T1-10):** 2022 `18.768`=18768, 2023 `8.007`=8007, **2024 `9.108`=9108 MDH**; Δ `+1.101`=+1101 MDH / +13,8%.
   - **Average unit price (G1-5):** 2023 `1.231`=1231, **2024 `1.099`=1099 DH/T**.
2. **False "9.102 vs 9.108" conflict removed.** They are different **scopes**, not variants:
   - **9102 MDH** = ATPA-with-payment customs regime (**T3-4**) — ancillary, `customs_regime=ATPA_with_payment`, never substitutes for total.
   - **8737 MDH** = Asia-origin subset (**T4-9**) — ancillary, `origin=Asia`, not a world total.
   - The total-import series (18.768/8.007/9.108) and the ATPA series (18.758/7.994/9.102) are no longer mixed.

**Quantity:** `quantity_change_pct = 27.4`; `absolute_quantity_tonnes = null` (not derived).
**Classification:** Claim A remains **BLOCKED**; the source label is narrower than the generic `sulfur` concept.
**Relationship & Contract-C:** `REL-INST-MA-SULFUR-IMPORT-2024` remains `evidence_collecting`; **Contract-C = (not_public, noindex)** (unchanged).

**Numeric-normalization law added:** `evidence_admission_policy.json` (quantitative_normalization_law) + `scripts/governance_scaffolding/numeric_normalization.py`, wired into the scaffolding validator so any locale-literal used as a naive machine float is caught. Convention is source-specific.

**Artifacts corrected:** `EVD-MA-SULFUR-IMPORT-2024.json`, `PILOT_01_claims.json`, `MOROCCO_SULFUR_TRADE_PILOT_01.md`, `PILOT_01_source_acquisition_dossier.md`, this DECISION_LOG Pilot 01 entry (lines above), evidence-admission policy, validators.

**Tests:** Pilot 01 correction 14/14 (incl. no-variant-framing guard); Pilot 01 16/16; source admission 21/21; scaffolding, concept↔lexeme, relationship grammar 8/8, Contract C 7/7; existing L0/L1/L2 PASS. Source statuses/locks unchanged (15 seeded + 1 verified; all candidate).

---

## Pilot 01 — Classification Resolution

**Date:** 2026-09-19
**Baseline:** commit `da896cf0b7`. Two purposes: (A) source-specific numeric normalization fix; (B) commodity-classification identity. No Pilot 02, no OCP, no GCC/China/Germany, no route/sitemap/robots/indexation/public-HTML/14K change. No existing source status/lock change; no claim activation. No PR.

### A. Source-specific numeric normalization (bug fixed)
`numeric_normalization.py` rebuilt with governed convention ids — `NUM-FR-DOT-THOUSANDS`, `NUM-EN-DOT-DECIMAL`, `NUM-PLAIN-INT`. Each quantitative evidence record MUST declare `numeric_convention_id`; a record with measures but no governed convention **fails** — no silent French fallback, never inferred from language/country/extension. Morocco evidence declares `NUM-FR-DOT-THOUSANDS`. Policy updated (`evidence_admission_policy.json`). An English `1.099` is now normalized to 1.099, not 1099.

### B. Classification identity
- **HS 2022 — PROVEN** from the official **UN Comtrade H6 reference** (WCO HS 2022; WCO artifact itself interactive/not fetchable): **2503.00 = "Sulphur of all kinds; other than sublimed, precipitated and colloidal sulphur"**; excluded forms → **2802.00**; chapter 25. Object `CLS-HS2022-2503-00`.
- **Moroccan national code / OdC-label→HS mapping — BLOCKED** (douane.gov.ma WAF/access-restricted; no login workaround). The OdC "Soufres bruts et non raffinés" is modelled as a `statistical_product_grouping` (`CLS-MA-ODC-SOUFRES-BRUTS`); label↔2503 is a hypothesis only.
- **Claim A: BLOCKED → PARTIAL** (HS side proven; Moroccan mapping blocked).
- **Claim B/C:** unchanged (B proven; C total 9108 MDH / 1099 DH/T; tonnage blocked).
- **Relationship** `GEO-MA → REL-IMPORTER → sulfur`: stays **evidence_collecting** (Outcome 2 — OdC→HS mapping unproven, so the generic `sulfur` object is not upgraded); trade sufficiency policy **unchanged**.

### Taxonomy amendment
Added governed category **`customs_nomenclature_authority`** (policy + source-registry vocabulary; validator no-drift) rather than mislabel HS as a scientific/technical standard (§M). Registered `SRC-UN-COMTRADE-HS2022` (seeded/candidate, identity_revision) with classification-only qualification `QUAL-UN-HS2022-001` (state `reviewed`; prohibits Morocco trade totals / industrial / scientific / market).

### New governed object
`classification_registry.json` (minimal: system → version → code → official_label → exclusions; HS6 and national_code kept as distinct nullable fields; statistical grouping vs HS commodity distinguished).

### Contract-C
Derived evidence posture `evidence_collecting`; **Contract-C = (not_public, noindex)** (unchanged).

### Tests
Classification resolution **17/17**; source admission 21/21; Pilot 01 16/16; Pilot 01 correction 14/14; scaffolding, concept↔lexeme, relationship grammar 8/8, Contract C 7/7; existing L0/L1/L2 PASS. Sources now 16 seeded + 1 verified; all candidate (existing statuses/locks unchanged).

### Not started
Pilot 02 (OCP / Morocco Industrial Chain); GCC/China/Germany; language localization; Moroccan national-code acquisition; trade sufficiency-policy amendment.

---

## Pilot 01 — Evidence Admission Closure

**Date:** 2026-09-19
**Baseline:** commit `cb3ed350b6`. Purpose: make the classification path obey **Source → Qualification → Evidence → Claim** (like the trade path), so the HS identity is *admitted evidence*, not a bare assertion. No Pilot 02, no new external source (the two Pilot-01 sources were re-fetched for identity verification only), no OCP/GCC/China/Germany, no route/sitemap/robots/indexation/public-HTML/14K change, no claim activation, no source-locking, no PR.

### What changed
- **New governed subject domain `SD-CUSTOMS-CLASSIFICATION`** (`subject_domain_registry.json`), distinct from the chemical `SD-NOMENCLATURE`: goods/customs/statistical classification is a different fact type from chemical naming. State `registered` (domain evidence-activation deliberately deferred; no publication effect).
- **Evidence schema extended** (`evidence/evidence_schema.json`): `evidence_kind = classification`, `claim_level = classification`, reference field `classification_ids → classification_registry.json`, and a classification level-rule (requires kind `classification` + non-empty `classification_ids`).
- **Domain admissibility policy for SD-CUSTOMS-CLASSIFICATION** (`source_admissibility_policy.json`): sufficiency `single_authoritative_sufficient` (a nomenclature identity is definitional, not a contested measurement — unlike trade totals). Allowed categories = nomenclature/customs authorities; trade-statistics sources are **not** allowed to establish the nomenclature.
- **Real classification evidence `EVD-HS2022-2503-00`** created, binding `SRC-UN-COMTRADE-HS2022` / `QUAL-UN-HS2022-001` / `CLS-HS2022-2503-00`. `admissible()` returns **TRUE**; review posture `evidence_verified` (only because admissible TRUE).
- **One-fact-one-owner for classification objects** (`classification_registry.json`): `source_id` is now **forbidden** on a classification object; the source binding lives on the evidence record, referenced via `supporting_evidence_ids`. `CLS-HS2022-2503-00.supporting_evidence_ids = ["EVD-HS2022-2503-00"]`; `CLS-MA-ODC-SOUFRES-BRUTS.supporting_evidence_ids = []` (Moroccan mapping stays **UNPROVEN/BLOCKED**).
- **Source identity verification** (`SOURCE_IDENTITY_VERIFICATION_CHECKLIST.md`, C1–C8) applied to **exactly the two Pilot-01 sources**: both re-fetched (UN Comtrade H6 JSON re-confirmed 250300/280200 verbatim; OdC PDF HTTP 200 / `application/pdf` / `%PDF-`). Both `status: seeded → verified` under `verification_limited`, **lock stays `candidate`**, added to `verification_ready_sources`. No credentials, no gate bypass.
- **Qualification promotion:** `QUAL-UN-HS2022-001` `reviewed → qualified_narrow` (identity verified + narrow scope reviewed), domain moved `SD-NOMENCLATURE → SD-CUSTOMS-CLASSIFICATION`. `QUAL-OC-MA-TRADE-001` **deliberately NOT promoted** (stays `reviewed`) — the trade path is unchanged.
- **Claim A** (`PILOT_01_claims.json`): HS side now references `supporting_evidence_ids = ["EVD-HS2022-2503-00"]` (not classification IDs as a substitute); wording softened from bare "PROVEN" to the governed posture ("ADMITTED / evidence_sufficient, not locked, not published"); outcome stays **PARTIAL**; Moroccan side stays blocked.
- **SOURCE_POLICY drift audit** (`SOURCE_POLICY_DRIFT_AUDIT.md`, D1–D6) + minimum-sync "Supersession & Layering" pointer appended to `doctrine/SOURCE_POLICY.md`. No core rule changed.

### Derived state (governed, not asserted)
- Classification path: `admissible=TRUE` → posture **`evidence_sufficient`** (NOT `evidence_locked`, because source lock is `candidate`) → **Contract-C = (not_public, noindex)**.
- Trade path: **unchanged** — sufficiency `primary_plus_corroborating`, posture `evidence_collecting`, qualification `reviewed`, `admissible=FALSE` → Contract-C = (not_public, noindex).

### Tests
New **admission-closure 19/19**; classification resolution 17/17; source admission 21/21; Pilot 01 16/16; Pilot 01 correction 14/14; scaffolding + concept↔lexeme validators PASS; relationship grammar 8/8; Contract C 7/7. **Wired CI** (L0/L1/L2 incl. `validate_source_registry_lock_l1.py`) PASS. Sources now 15 seeded + **3 verified** (SPEKTRUM, OC-MA, UN-COMTRADE); **all `source_lock_status = candidate`**.

### Not started
Pilot 02; GCC/China/Germany; language localization; Moroccan national-code acquisition; trade sufficiency-policy amendment; domain evidence-activation; source-locking; any route/claim activation.

---

## Pilot 02 — Morocco OCP Sulfur Industrial Chain

**Date:** 2026-09-19
**Baseline:** commit `c2c390b670`. Purpose: test whether BISULFID can REPRESENT a real industrial actor (OCP Group) and its relationship to sulfur without turning corporate disclosures into national statistics/market claims. Scope "OCP × sulfur × Morocco industrial context × FY2024", max 3 claims. Issuer-primary OCP official disclosures only. No public page/route/indexation/14K, no GCC/China/Germany, no Arabic/French lexeme expansion, no Pilot 03, no PR.

### Outcome: governance success by withholding
The corporate-actor governance architecture was built and PROVES correct withholding. **All three principal claims are BLOCKED** because the OCP primary PDFs could not be opened in this environment: `www.ocpgroup.ma` serves a Cloudflare JS bot-challenge (HTTP 403) to curl and WebFetch, and Chromium could not be granted trust of the egress-proxy CA without a TLS-trust change that the environment disallowed (attempt denied). No credentials, login, or TLS-verification bypass were used (parallels the douane.gov.ma block in Pilot 01). **No figure/sentence was taken from prompt text or search snippets.**

### Built (acquisition-independent architecture)
- **Organization registry** (`organization_registry.json`): `ORG-OCP-GROUP` identity ONLY (canonical name + disambiguation). Forbids financials/market/ownership/relationship/route fields; forbids ID collision with a geography. Creating the org implies NO relationship, and OCP is never substitutable for GEO-MA.
- **Two governed source categories** (`corporate_financial_report`, `corporate_sustainability_report`), authority strictly limited to the issuer's own disclosed facts (issuer-primary, not market/industry press). Added to policy + registry vocabulary (no drift).
- **New domain `SD-CORPORATE-FINANCIALS`** (distinct from SD-TRADE): a narrow issuer accounting line may use `single_authoritative_sufficient` for that exact fact type; trade/economics sufficiency unchanged (`primary_plus_corroborating`). **SD-INDUSTRIAL** now distinguishes issuer-primary vs analytical; broader industrial relationships still require corroboration.
- **Accounting numeric convention `NUM-ACCOUNTING-PAREN-NEG`** (`numeric_normalization.py` + policy): comma-thousands, dot-decimal, PARENTHESES = NEGATIVE. `(8,344)` → signed `-8344`; a `magnitude()` helper yields a labelled positive for prose only. Validator rejects a parenthesised literal stored as positive (no silent parentheses drop).
- **Two OCP sources registered** (`SRC-OCP-AFR-2024`, `SRC-OCP-SUSTAINABILITY-2024`) with `identity_revision`, status **seeded** / lock **candidate**. C1–C8 identity verification attempted; **C1 (reachable) FAILS** here → not verified.
- **Two deny-by-default qualifications** (`QUAL-OCP-AFR-001` SD-CORPORATE-FINANCIALS/quantitative; `QUAL-OCP-SUS-001` SD-INDUSTRIAL/qualitative), state **candidate** (source unverified + scope unreviewable) → not admissible.
- **Non-operational Pilot-02 claim store** (`PILOT_02_claims.json`): Claims A/B/C all BLOCKED, `supporting_evidence_ids: []`.

### Not created / not asserted
- No evidence records (nothing extracted). No `ORG-OCP-GROUP → REL-INDUSTRIAL-USER → sulfur` instance (no admitted evidence; and REL-INDUSTRIAL-USER requires primary production/statistical/scientific categories a single corporate self-report cannot satisfy — not weakened). No `sulfuric_acid` ontology concept fabricated. The sulfur price statement is OUT OF SCOPE and not ingested (unresolved prose/figure inconsistency; requires original-page recheck).
- Independence: the two reports share the issuer → recorded as **non-independent**; corroboration-requiring patterns correctly return `evidence_collecting`.

### Derived state
No admitted evidence → posture `evidence_collecting` → **Contract-C = (not_public, noindex)**.

### Tests
`pilot_02_tests.py` (26 proofs) PASS; all prior suites regress green — Pilot-01 admission-closure 19/19, classification 17/17, source admission 21/21, Pilot 01 16/16, correction 14/14, Contract C 7/7, relationship grammar 8/8, scaffolding + concept↔lexeme validators PASS; **wired L0/L1/L2 CI PASS**. Sources now 17 seeded + 3 verified (unchanged verified set) + 2 new OCP seeded; **all locks candidate**.

### Blocked — needs a decision
Extracting the three OCP facts needs either (a) a permitted way for Chromium to trust the egress-proxy CA so it can clear the Cloudflare challenge, or (b) the user supplying the two official OCP PDFs. Until then Claims A/B/C stay BLOCKED. No Pilot 03.

---

## Pilot 02 — Evidence Completion (from original uploaded PDF)

**Date:** 2026-09-20
**Baseline:** commit `4a685bc2a9`. The user supplied the **original OCP Consolidated Financial Statements at 31 December 2024** PDF locally (the Sustainability Integrated Report PDF was NOT supplied). Completed only the previously-blocked Pilot-02 chain; architecture unchanged; no Pilot 03. Everything extracted verbatim from the original PDF (pdfminer.six via the local crypto-stub workaround); nothing taken from prompt text or search snippets.

### Source verification (§1)
- `SRC-OCP-AFR-2024`: C1–C8 **PASS** against the original PDF (independent auditors' report present; Note 4.2.2 figures verbatim). status `seeded → verified`, **lock stays candidate**, added to `verification_ready_sources`. Verification ≠ qualification/admission/claim/publication. (Uploaded file's edition datestamp 20 Mar 2025 vs URL 27 Mar 2025 — same FY2024 work; `identity_revision` unchanged.)
- `SRC-OCP-SUSTAINABILITY-2024`: **C1 FAILS** (PDF not uploaded) → stays `seeded`; `QUAL-OCP-SUS-001` stays `candidate`.

### Qualification (§2)
`QUAL-OCP-AFR-001` promoted `candidate → qualified_narrow` for two explicitly-reviewed issuer-primary uses (FY2024 accounting sulfur line; FY2024 sulfur-consumption observation), domains `[SD-CORPORATE-FINANCIALS, SD-INDUSTRIAL]`, kinds `[quantitative, qualitative]`. Prohibits Morocco/national/market demand, import value, tonnage-from-value, and the sulfur price statement.

### Claim A — sulfur accounting amount (§3) — SUPPORTED
Evidence `EVD-OCP-SULFUR-PURCHASE-FY2024` from **Note 4.2.2, "Purchases consumed", "In millions of dirhams", page 21**: **Sulfur FY2024 source literal `(8,344)` → signed `-8344` MDH; FY2023 `(8,088)` → `-8088` MDH** (`NUM-ACCOUNTING-PAREN-NEG`). Derived magnitude 8,344 (prose only). 'Sulfuric acid' `(2,364)` kept as a **distinct** line, not merged. Means only OCP's own accounting line — not import value / tonnage / Morocco demand / market size. admissible()=True; single_authoritative_sufficient → **evidence_sufficient** (not locked).

### Claim B — sulfur consumption observation (§4) — SUPPORTED
Evidence `EVD-OCP-SULFUR-CONSUMPTION-FY2024`, verbatim (p21): *"sulfur consumption volumes increased in correlation with the rise in sulfuric acid production."* Issuer-reported, FY2024-scoped. No tonnage/percentage/causality/national inference. admissible()=True; SD-INDUSTRIAL primary_plus_corroborating → relationship stays **evidence_collecting**.

### Price inconsistency quarantined (§5)
Same paragraph: "drop in price per ton" but prints **$127/T CFR (2024) vs $113/T CFR (2023)** (rise, not drop), and "decreased by 256" while the Note 4.2.2 magnitude rises 8,088→8,344. Recorded in `EVD-OCP-SULFUR-CONSUMPTION-FY2024.quarantined_not_admitted` (`excluded_from_claims: true`, `resolution: none`). Not silently fixed, years not reversed, no external knowledge, not used to explain Claim A. A test proves it cannot be promoted without an explicit resolution step.

### Claim C — industrial process (§6) — BLOCKED
Sustainability PDF not uploaded → not extracted/asserted. Financial evidence cannot substitute. No `sulfuric_acid` concept fabricated. Site scope (Jorf Lasfar/Safi) recorded as the target for when the PDF is supplied.

### Relationship (§7) + independence (§8)
`REL-INST-OCP-SULFUR-FY2024`: **ORG-OCP-GROUP → REL-INDUSTRIAL-USER → sulfur**, FY2024-bounded, `evidence_collecting` (NOT `evidence_qualified`). Not `GEO-MA → … → sulfur`. Same-issuer reports are **not** independent; policy not weakened.

### Postures (§9) / Contract-C (§13)
Purchase: admitted True, evidence_verified, evidence_sufficient (lock candidate → not locked). Consumption/relationship: admitted True, evidence_collecting. **Contract-C = (not_public, noindex)** everywhere. No publication/route/sitemap/robots/indexation/14K change.

### Tests (§11)
`pilot_02_tests.py` rewritten (37 assertions) PASS; all prior governance + Pilot-01 suites regress green; **wired L0/L1/L2 CI PASS**. Sources now 3 verified (SPEKTRUM, OC-MA/UN-COMTRADE, **+ OCP-AFR**), all locks candidate; SRC-OCP-SUSTAINABILITY-2024 still seeded.

### Stop
No Pilot 03.

---

## Pilot 02 — Claim C Completion (Sustainability page-excerpt)

**Date:** 2026-09-20
**Baseline:** commit `9aee972f95`. The user supplied a direct **page-excerpt** of the original OCP Sustainability Integrated Report 2024 (original report **page 20** = industrial-process statement; **pages 305–306** = third-party assurance, for bounding only). Completed only the previously-blocked Claim C chain (`SRC-OCP-SUSTAINABILITY-2024 → QUAL-OCP-SUS-001 → evidence → Claim C`). Claims A/B untouched; architecture unchanged; no Pilot 03. Extracted verbatim from the original excerpt (pdfminer.six); nothing from prompt text.

### Source verification (§1)
`SRC-OCP-SUSTAINABILITY-2024`: C1–C8 **PASS** against the page-excerpt → status `seeded → verified`, **lock stays candidate**, added to `verification_ready_sources`. Verification ≠ qualification/admission/claim/publication.

### Qualification (§2)
`QUAL-OCP-SUS-001` promoted `candidate → qualified_narrow` for the reviewed use `issuer_own_process_context_ocp` (SD-INDUSTRIAL, qualitative), site-scoped Jorf Lasfar/Safi. Prohibits financial amount, sulfur feedstock quantity, national/market demand, universal/chemistry claims, and third-party assurance of the process statement.

### Claim C — industrial process (SUPPORTED)
Evidence `EVD-OCP-PHOSPHATE-PROCESS-2024`, verbatim **page 20**: OCP's phosphate processing at **Jorf Lasfar and Safi** combines phosphate rock with sulphuric acid to create phosphoric acid; sites equipped with sulphuric-acid and phosphoric-acid production lines. Issuer-primary, organization-scoped, site-scoped. admissible()=True; SD-INDUSTRIAL primary_plus_corroborating → **evidence_collecting** (third OCP-issuer, non-independent). No `sulfuric_acid` ontology concept fabricated (kept as qualitative text).

### Assurance bounding (§ user instruction)
Pages 305–306 third-party assurance (ISO 14064-1/-3, "reasonable assurance", GUTcert, Berlin 29 Jul 2025) is scoped to **environmental metrics only** — GHG (Scope 1/2/3 CO₂e), clean-electricity use ratio (80.00%), waste ratios, non-conventional-waters ratio. Recorded in the evidence's `assurance_bounding` block (`assured_metrics_are_pilot02_claims: false`). It does **NOT** assure the page-20 process statement, and those metrics are **not** admitted as Pilot-02 claims.

### Relationship / independence / Contract-C
`REL-INST-OCP-SULFUR-FY2024` now carries 3 issuer evidence_ids (purchase, consumption, process); stays **evidence_collecting** (same-issuer non-independence; policy not weakened; not `GEO-MA`). Contract-C = **(not_public, noindex)** everywhere. No route/claim activation, no source-lock.

### Tests
`pilot_02_tests.py` updated (Claim C supported; site scope; assurance bounded; sustainability≠financial; no sulfuric_acid concept) — PASS; all prior governance + Pilot-01 suites regress green; **wired L0/L1/L2 CI PASS**. Sources now **5 verified** (SPEKTRUM, OC-MA, UN-COMTRADE, OCP-AFR, OCP-SUSTAINABILITY) — all locks candidate.

### Stop
Pilot 02 is complete: Claims A, B, C all supported at their reviewed scope; relationship evidence_collecting; nothing published. No Pilot 03.
