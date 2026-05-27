# Corpus Automation Manifest (Sprint 5I-A)

## Automation purpose

This manifest defines the **controlled contract** for all future Bisulfid.com corpus automation: what each stage may read, what it may write, where human review is mandatory, and what conditions **block merge** or **block publication**.

Automation serves the **500-page sovereign launch program** and subsequent **1,000+ / 3,000+** expansion—**without** weakening source, claim, multilingual, SEO, or technical governance.

**No automation stage is authorized by this document alone.** Each wave sprint must declare an explicit manifest binding referencing this file.

---

## Automation stages

| Stage ID | Name | Primary function |
| --- | --- | --- |
| **S0** | Pre-flight | Charter check; forbidden-surface scan; wave size validation |
| **S1** | Route registration | Add **planned** routes from blueprint |
| **S2** | Draft production | Create non-public `content_file` bodies |
| **S3** | Source mapping | Align markers with `source_registry.json` |
| **S4** | Claim boundary | Boundary reports; forbidden-claim scans |
| **S5** | Internal-link wiring | Add `internal_links.json` cluster edges |
| **S6** | SEO / metadata validation | Route metadata coherence |
| **S7** | Technical / security validation | Build, indexation guards, config |
| **S8** | Pre-publication validation | Aggregate launch gate status |
| **S9** | Launch authorization | **Human-only** — not automatable |

Stages **S1–S8** may use tooling; **S9** is **never** automated.

---

## Stage inputs and outputs

| Stage | Inputs | Outputs | Human review |
| --- | --- | --- | --- |
| **S0** | Wave charter; blueprint slice; `routes.json` snapshot | Pre-flight pass/fail report | Required before S1+ |
| **S1** | Blueprint rows; readiness matrix | `routes.json` patch or manual edit plan | Required before merge |
| **S2** | Registered routes; draft templates | New `content_file` Markdown | Sample audit ≥ 10% |
| **S3** | Drafts; `source_registry.json`; SOURCE_POLICY | Mapping report; registry patch proposal | Required before marker removal |
| **S4** | Drafts; claim registries; route metadata | Boundary report per page/batch | Required before publication talk |
| **S5** | Routes; cluster spec; existing link graph | `internal_links.json` patch proposal | Required before merge |
| **S6** | Routes; hreflang groups; templates | SEO/metadata validation report | Required on failures |
| **S7** | Repo; build config; route flags | Technical/security report | Required on severity-1 |
| **S8** | All registries; content; gates doc | Launch readiness matrix | Owner signoff |
| **S9** | S8 pass + owner authorization | Publication flip (manual sprint) | **Owner only** |

---

## Allowed files per stage

| Stage | May read | May write (with review) |
| --- | --- | --- |
| **S0** | All governance docs; registries (read-only) | `main/data/*_PREFLIGHT_REPORT.md` only |
| **S1** | Blueprint; readiness matrix; `routes.json` | `routes.json`; wave report |
| **S2** | `routes.json`; templates; doctrine | `main/content/**` new drafts only; wave report |
| **S3** | Drafts; `source_registry.json`; SOURCE_POLICY | `source_registry.json` (dedicated sprint); mapping report |
| **S4** | Drafts; claims; routes | Boundary report only (default) |
| **S5** | Routes; `internal_links.json` | `internal_links.json`; link report |
| **S6** | Routes; sitemap policy; navigation | Validation report only |
| **S7** | Full repo (excl. secrets) | Validation report only |
| **S8** | All governance surfaces | Readiness report only |
| **S9** | S8 outputs | Per launch charter only |

---

## Prohibited files per stage (all stages)

Automation **must never** modify without explicit owner launch charter:

- Root `README.md`
- `package.json`, lockfiles, dependency manifests
- `.github/workflows/**` (unless dedicated workflow charter sprint)
- Generated public HTML output directories
- Cloudflare / deployment configs (unless dedicated infra sprint)
- Claim registry `status: inactive` → `active` flips
- Ontology verified flags without activation sprint

---

## Required human review points

| Checkpoint | Trigger | Blocker if skipped |
| --- | --- | --- |
| **Manifest binding** | Start of any S1–S8 wave | Wave invalid |
| **Pre-flight pass** | Before file writes | No automation runs |
| **Merge review** | Any registry or content patch | PR cannot merge |
| **Sample audit** | End of S2 draft wave | Wave incomplete |
| **Source signoff** | Before marker removal | Markers stay |
| **Claim signoff** | Before publication discussion | Routes stay planned |
| **Owner launch** | S9 only | No publication |

---

## Route generation manifest rules (S1)

1. Every `route_id` must exist in `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` or explicit wave charter appendix.
2. Default: `status: planned`, `indexable: false`, `in_sitemap: false`.
3. `content_file` path must be unique and follow existing conventions.
4. No duplicate `route_id` or path collisions.
5. Wave size: **80–120** routes unless charter documents exception.
6. Automation emits **manifest diff** listing every new row before merge.

---

## Draft generation manifest rules (S2)

1. Target routes must already exist in `routes.json` as **planned**.
2. Do not overwrite existing `content_file` bodies.
3. Required frontmatter: `route_id`, `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`, language/locale fields.
4. Preserve `[SOURCE REQUIRED]` where factual support pending.
5. Wave size: **40–60** pages unless charter exception.
6. No raw URLs; no markdown links assuming publication; `route_id` plain text only.

---

## Source mapping manifest rules (S3)

1. Registry remains **inactive** for normative activation unless charter says otherwise.
2. No auto-verification of sources.
3. Marker removal requires mapped registry row + human signoff sprint.
4. Wave size: **40–60** pages per mapping wave.

---

## Claim boundary manifest rules (S4)

1. **No** `status: approved` writes.
2. Registries stay **inactive** unless activation sprint.
3. Output is reports only by default.
4. Flag market, safety, medical, procurement, CAGR, acquisition patterns.

---

## Internal-link manifest rules (S5)

1. Targets must be existing `route_id` values in `routes.json`.
2. No raw external URLs in policy-violating ways.
3. No edges implying public availability until launch.
4. Wave size: **40–60** edges per cluster slice.

---

## Validation manifest rules (S6–S8)

1. Read-only by default.
2. Severity-1 failures **block merge**.
3. Launch aggregation (S8) requires **500** pages passing all gates in `CORPUS_LAUNCH_THRESHOLD.md`.

---

## Publication lock rules

| Lock | Condition |
| --- | --- |
| **Route lock** | No `status: published` except S9 owner sprint |
| **Indexation lock** | No `indexable: true` / `in_sitemap: true` except S9 |
| **Claim lock** | No approved claims except activation + review sprint |
| **Output lock** | No public HTML generation before S8 pass |
| **Count lock** | No launch before **500** governed pages certified |

---

## No-public-output rule before 500 governed pages

**Hard rule:** No generated **public** HTML, no sitemap publication, no production indexation, and no CDN deploy of reference pages until:

1. **≥ 500** pages pass all gates in `CORPUS_LAUNCH_THRESHOLD.md`, and  
2. **S9** owner authorization sprint completes.

Automation validators may run against **non-public** drafts and **planned** routes at any time.

---

## Failure conditions

| ID | Condition | Default severity |
| --- | --- | --- |
| **F1** | Duplicate `route_id` | 1 — block merge |
| **F2** | `content_file` path collision | 1 — block merge |
| **F3** | Missing required frontmatter | 1 — block merge |
| **F4** | `[SOURCE REQUIRED]` stripped without mapping | 1 — block merge |
| **F5** | Claim approved by automation | 1 — block merge |
| **F6** | Route published / indexable flipped without S9 | 1 — block merge |
| **F7** | Broken required internal link | 1 — block merge |
| **F8** | Thin / placeholder page detected | 1 — block merge |
| **F9** | Forbidden claim pattern in draft | 2 — block wave completion |
| **F10** | SEO metadata missing on route row | 2 — block wave completion |
| **F11** | hreflang inconsistency | 2 — block wave completion |
| **F12** | Technical build failure | 1 — block merge |

---

## Rollback expectations

1. Every wave produces a **manifest report** with before/after hashes or diffs.
2. Registry and content changes land via **reviewed PR**—revert by git revert, not silent automation rollback.
3. Automation must **never** force-push or hard-reset.
4. If severity-1 failure detected post-merge, **stop-the-line** on next wave until remediated.

---

## Audit logging expectations

Each automated or semi-automated wave must leave:

1. **Wave ID** (e.g., `5I-B-route-wave-1`)
2. **Stage(s) executed** (S0–S8)
3. **Input manifest** (blueprint row range, route_ids)
4. **Output manifest** (files touched, row counts)
5. **Validation summary** (pass/fail by gate)
6. **Human reviewer** (name/role when applicable)
7. **DECISION_LOG** entry or reference in sprint report

Reports live in `main/data/` unless charter specifies otherwise.

---

*Sprint 5I-A — manifest doctrine only. No automation executed in this sprint.*
