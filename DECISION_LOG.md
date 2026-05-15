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

**Decision:** Create a minimal standard-library-only static build system skeleton.

**Rationale:** The governance layer (doctrine, data, content skeleton, validators) is in place. The next layer is the technical build mechanism. The build system must exist as a skeleton before any content or UI can be assembled. Creating the skeleton at this stage reserves the build contract: routes.json governs what gets generated; no planned route produces output; prelaunch robots and sitemap policies are enforced from day one. No dependencies are introduced. No public pages are generated. The build system is not launch-ready at this stage.

**Doctrine reference:** `doctrine/QUALITY_GATE.md`, `doctrine/SECURITY_POLICY.md`, `doctrine/PROJECT_DOCTRINE.md`

**Sprint 1 constraints (all observed):**
- Python standard library only. No external dependencies.
- No package.json. No requirements.txt with packages.
- No GitHub Actions. No deployment workflow.
- No Cloudflare config.
- No routes marked published.
- No routes set indexable: true.
- No routes set in_sitemap: true.
- No claim files modified.
- No source entries added.
- No real content pages created.
- No visual UI, advanced CSS, animations, or JavaScript.
- README.md not modified.
- build.py generates 0 public pages (all routes are planned).
- sitemap.xml contains 0 URLs.
- robots.txt blocks all indexing (prelaunch policy).

**Files created:**

- `main/config/site.json` — site identity and status configuration.
- `main/config/build.json` — build system configuration.
- `main/config/seo.json` — SEO policy configuration.
- `main/config/security.json` — security policy configuration.
- `main/config/navigation.json` — navigation registry (inactive, no items).
- `main/templates/base.html` — base layout skeleton.
- `main/templates/home.html` — homepage skeleton.
- `main/templates/reference_page.html` — reference page skeleton.
- `main/templates/term_page.html` — term record page skeleton.
- `main/templates/glossary.html` — glossary page skeleton.
- `main/templates/newsletter.html` — newsletter page skeleton.
- `main/templates/acquire.html` — acquire page skeleton.
- `main/templates/partials/head.html` — \<head\> partial skeleton.
- `main/templates/partials/nav.html` — navigation partial skeleton (inactive).
- `main/templates/partials/footer.html` — footer partial skeleton.
- `main/templates/partials/hreflang.html` — hreflang partial skeleton (inactive).
- `main/templates/partials/internal_links.html` — internal link block skeleton.
- `main/templates/partials/source_bar.html` — source attribution bar skeleton.
- `main/templates/partials/safety_notice.html` — safety notice partial skeleton.
- `main/templates/partials/interactive_term_map.html` — Interactive Term Map partial skeleton (data-driven from ontology files).
- `scripts/build.py` — static build orchestrator; generates site/build-status.json only.
- `scripts/generate_sitemap.py` — prelaunch sitemap generator; 0 URLs.
- `scripts/generate_robots.py` — prelaunch robots.txt generator; full Disallow.
- `scripts/serve.py` — local development server using http.server.
- `scripts/README.md` — build scripts documentation.
- `site/.gitkeep` — reserves site/ output directory.

**Files updated:**

- `DECISION_LOG.md` — Sprint 0D and Sprint 1 entries appended.

**Not created in this sprint:** real content pages, GitHub Actions, deployment workflows, Cloudflare config, package.json, CSS files, JavaScript files, advanced UI, site HTML output, published routes, active sitemap entries.
