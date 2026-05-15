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
