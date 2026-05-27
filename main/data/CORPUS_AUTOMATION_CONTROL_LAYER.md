# Corpus Automation Control Layer (Sprint 5I-A)

## Why this sprint exists

Sprint **5H** raised the minimum public launch threshold to **500 governed pages** and defined **wave-based production** (`CORPUS_PRODUCTION_WAVE_MODEL.md`). The next major work—route registration waves (80–120), draft production waves (40–60), source mapping, claim boundary review, internal-link wiring, SEO/metadata validation, and technical validation—**cannot** scale safely through ad hoc manual sprints alone.

Sprint **5I-A** establishes the **governed automation control layer**: the doctrine for what future scripts, validators, and wave runners **may** automate—and what they **must never** automate without human governance. **This sprint creates documentation only.** No scripts, workflows, dependencies, routes, content, or publication artifacts.

---

## Why automation is now necessary

| Pressure | Why manual-only fails |
| --- | --- |
| **500-page launch floor** | Repetitive validation across hundreds of routes, drafts, markers, and links exceeds sustainable manual audit |
| **1,000+ / 3,000+ expansion** | Multilingual layers multiply registry, metadata, and hreflang consistency checks |
| **Wave cadence** | 80–120 route registrations and 40–60 draft waves require repeatable pre-flight and post-wave checks |
| **Broken-link prevention** | Graph integrity must be verified on every internal-link wiring wave |
| **Anti-thin / anti-placeholder** | Structural validators catch weak pages before they accumulate |
| **Publication accident risk** | Without explicit automation boundaries, tooling could flip `indexable`, approve claims, or strip markers |

Automation is **infrastructure for discipline at scale**, not a substitute for editorial judgment.

---

## Why automation was not introduced earlier

1. **Governance first:** Sprints **5A–5H** established architecture, blueprint, launch threshold, wave model, and manual proof batches (5E, 5G) **before** tooling could encode the rules.
2. **Small corpus size:** With **26** registered routes and **18** draft-backed pages, manual sprints were sufficient to **prove** discipline.
3. **Registry posture:** Claim and source registries remain **inactive**; automation before policy definition would have encoded wrong defaults.
4. **No premature CI:** GitHub workflows and dependencies were deliberately deferred until automation **requirements** were written (this sprint).

**Rule:** Automation follows doctrine; doctrine does not follow tooling.

---

## What automation is allowed to do later

Future governed automation **may**:

| Domain | Permitted automation |
| --- | --- |
| **Route registration** | Validate blueprint rows; check `route_id` uniqueness; emit **planned** `routes.json` patches for human-reviewed merge; verify `indexable: false`, `in_sitemap: false` |
| **Draft production** | Validate frontmatter; check required sections; count `[SOURCE REQUIRED]` markers; detect forbidden claim patterns; verify `content_file` path alignment |
| **Source mapping** | Cross-check draft markers against `source_registry.json`; flag unmapped factual lines; propose registry row drafts for review |
| **Claim boundaries** | Scan for forbidden market/safety/medical/procurement language; verify `required_claim_groups` alignment; **report only**—no approval |
| **Internal links** | Validate `route_id` targets exist; detect broken edges; enforce cluster rules; **no** raw URL sprawl |
| **SEO / metadata** | Validate title, description, H1, hreflang fields against route records |
| **Technical / security** | Run build checks; verify no accidental indexation flags; scan for security regressions in config |
| **Pre-publication** | Aggregate gate status; block merge if severity-1 failures; **never** auto-publish |
| **Audit logging** | Emit wave reports, diff summaries, validation manifests |

All automated outputs are **candidates for human review** unless explicitly classified as read-only validation (no file writes).

---

## What automation must never do automatically

| Forbidden automatic action | Rationale |
| --- | --- |
| Set `status: published` on any route | Publication is owner/editorial Quality Gate decision |
| Set `indexable: true` or `in_sitemap: true` | Indexation requires launch program authorization |
| Approve claims (`status: approved`) | Claim registries require explicit activation sprint + human review |
| Activate claim registries (`inactive` → `active`) | Owner-governed activation only |
| Remove or satisfy `[SOURCE REQUIRED]` markers | Source-locking is a dedicated human-governed sprint |
| Mark ontology terms verified | Ontology activation is registry-governed |
| Generate public HTML output before launch gates pass | No public output before 500-page threshold |
| Bulk MT EN→DE/AR/ZH/JA without human sign-off | Translation spam destroys multilingual authority |
| Create thin or placeholder pages to hit counts | Volume without substance violates sovereign standard |
| Add market data, CAGR, safety handling, medical, procurement content | SOURCE_POLICY and sprint boundaries |
| Modify `README.md`, add dependencies, or create workflows without charter | Out-of-scope surfaces |
| Bypass merge-blocking validation failures | Stop-the-line discipline |

---

## Automation role in reaching 500 governed pages

Automation supports the **500-page floor** by:

1. **Accelerating validation**, not lowering standards.
2. **Enforcing wave protocol** (`CORPUS_AUTOMATION_WAVE_PROTOCOL.md`) on every batch.
3. **Preventing regression**—broken links, duplicate routes, marker stripping, accidental indexation.
4. **Producing audit trails** so each wave leaves a reviewable manifest.
5. **Blocking merge** when severity-1 gates fail (`CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`).

Automation does **not** reduce the **500** count requirement or waive any gate in `CORPUS_LAUNCH_THRESHOLD.md`.

---

## Automation role in scaling to 1,000+ and 3,000+

| Horizon | Automation role |
| --- | --- |
| **1,000+ authority corpus** | Batch validators; multilingual drift detection; pruning reports for weak concepts |
| **3,000+ multilingual system** | hreflang coherence checks; per-language source posture validation; anti–translation-spam scanners |
| **5,000+ (optional)** | Expansion cap enforcement; mandatory validation waves before each scale tier |

Scaling automation **tightens** checks proportionally to language count and claim risk—never relaxes them for speed.

---

## Domain boundaries (summary)

### Route registration automation boundaries

- **In scope:** Blueprint cross-check; duplicate `route_id` detection; path/locale validation; default `planned` + non-indexable flags.
- **Out of scope:** Inventing routes not in blueprint without charter; publishing; modifying existing route state without wave manifest.

### Draft creation automation boundaries

- **In scope:** Frontmatter schema; required section headers; marker presence; forbidden content pattern scan.
- **Out of scope:** Writing substantive prose without human editorial pass; overwriting existing drafts; removing markers.

### Source mapping automation boundaries

- **In scope:** Marker-to-registry gap reports; category mismatch flags; proposed registry row templates.
- **Out of scope:** Marking sources verified without review; auto-clearing markers.

### Claim boundary automation boundaries

- **In scope:** Forbidden-pattern detection; `required_claim_groups` cross-check; boundary report generation.
- **Out of scope:** Claim approval; registry activation.

### Internal-link automation boundaries

- **In scope:** Dead `route_id` detection; cluster completeness reports; edge count limits.
- **Out of scope:** Wiring links to unpublished routes as if public; raw URL injection.

### SEO / metadata validation boundaries

- **In scope:** Field presence; length bounds; hreflang pair consistency (when registries exist).
- **Out of scope:** SEO-first thin page generation; auto-indexation.

### Technical / security validation boundaries

- **In scope:** Build pass; config drift detection; indexation flag scans; dependency charter compliance.
- **Out of scope:** Deploying to production; bypassing security review.

---

## Anti-rules (automation-enforced where scripted)

| Rule | Enforcement |
| --- | --- |
| **Anti-thin-content** | Minimum section count; reject stubs below category floor |
| **Anti-placeholder** | Detect boilerplate-only pages; block merge |
| **Anti-translation-spam** | Flag MT-only drafts; require human review marker |
| **Anti-publication-accident** | Any `published` / `indexable` / `in_sitemap` flip requires explicit launch manifest + human approval |

---

## Human review requirements

Human review is **mandatory** at:

1. **Wave manifest approval** — before any automation writes registry or content files.
2. **Post-wave sample audit** — ≥ 10% of draft wave (minimum 3 pages).
3. **Source mapping signoff** — before marker removal sprint.
4. **Claim boundary signoff** — before publication discussion.
5. **Pre-publication review** — Quality Gate; owner acknowledgment.
6. **Launch authorization** — only after ≥ 500 pages pass all gates.

Automation **reports**; humans **authorize**.

---

## Recommended future script layers (not created in 5I-A)

| Layer | Purpose | Writes files? |
| --- | --- | --- |
| **L0 — Read-only validators** | Schema, frontmatter, link graph, marker scans | No |
| **L1 — Manifest generators** | Wave reports, diff plans, audit logs | Report files only (`main/data/*_REPORT.md`) |
| **L2 — Patch proposers** | Emit JSON/Markdown patches for human merge | Patch artifacts; no direct merge |
| **L3 — CI gate runners** | Block PR merge on severity-1 failures | No (exit codes only) |
| **L4 — Launch orchestrator** | Aggregate gate status pre-launch | Read-only until owner flag |

**No L2+ script runs in CI without** `CORPUS_AUTOMATION_MANIFEST.md` stage authorization.

---

## Recommended next sprint

**Sprint 5I-B (suggested): Route registration wave 1 + L0 validators**

1. Implement **read-only** route registry validator (L0)—no file writes.
2. Execute **route registration wave 1** (80–120 blueprint concepts) as **manual or patch-proposer sprint** with manifest.
3. **Do not** publish; **do not** draft at scale until registration wave validates.

Alternate: **Sprint 5I-B scripts charter** — implement L0 validators only, still no workflows.

---

## Relationship to other documents

- `CORPUS_AUTOMATION_MANIFEST.md` — stage inputs/outputs and file permissions.
- `CORPUS_AUTOMATION_WAVE_PROTOCOL.md` — wave execution procedure.
- `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md` — validation gates and severity levels.
- `CORPUS_PRODUCTION_WAVE_MODEL.md` — wave sizes and production sequence.
- `CORPUS_LAUNCH_THRESHOLD.md` — launch gates automation must enforce.

---

*Sprint 5I-A — automation control doctrine only. No scripts, workflows, or registries modified.*
