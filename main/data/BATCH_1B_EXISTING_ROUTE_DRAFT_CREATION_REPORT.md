# Batch 1B Existing Planned Route Draft Creation Report (Sprint 5G)

## Why this sprint exists

Sprint **5F** completed a **report-only** governance review of Batch **1A** methodology drafts. The strategic posture now shifts from planning-only artifacts toward **controlled corpus production**: increasing the **real non-public draft page base** while preserving sovereign-grade discipline.

Sprint **5G** creates the next batch of **non-public Markdown bodies** for **existing planned routes** already registered in `routes.json`—**without** adding routes, publishing anything, modifying registries, or wiring internal links.

**Sprint 5G did not modify** `routes.json`, `internal_links.json`, claim or source registries, ontology files, templates, or any forbidden surface.

---

## Relationship to Sprint 5F

Sprint **5F** mapped source requirements, claim boundaries, German authority constraints, and publication blockers for the five Batch **1A** methodology routes. Sprint **5G** **extends corpus inventory** into the next safe slice of **missing** planned routes—gateway and future-materials **terminology infrastructure**—while honoring the same non-public posture:

- All routes remain **`planned`**
- Claim registries remain **inactive**
- **`[SOURCE REQUIRED]`** markers remain wherever factual support is pending
- **No publication**, **no indexability**, **no sitemap inclusion**

---

## Files reviewed (read-only)

| Path | Role in selection |
| --- | --- |
| `main/data/routes.json` | Authoritative route registry; `content_file` paths and risk metadata |
| `main/data/ENGLISH_DRAFT_INVENTORY_REVIEW.md` | Prior draft inventory posture |
| `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` | Readiness classifications for Batch 1 concepts |
| `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` | Corpus category priorities and deferred high-risk buckets |
| `main/data/BATCH_1A_SOURCE_CLAIM_BOUNDARY_REVIEW.md` | Batch 1A boundary precedent |
| `main/data/CORPUS_LAUNCH_THRESHOLD.md` | Launch cohort scale framing |
| `main/content/en/pages/` | Existing EN drafts—skip if file present |
| `main/content/de/pages/` | Existing DE drafts—skip if file present |
| `DECISION_LOG.md` | Sprint lineage |

---

## Route selection method

1. Enumerate all **`routes`** in `routes.json` (`status: planned`).
2. For each route, test whether **`content_file`** exists on disk.
3. **Exclude** routes whose topics require safety, medical, market, procurement, production, trade, handling, or acquisition claims—or whose registry metadata flags **`risk_level: high`**, **`safety_claims`**, **`acquisition_claims`**, or industrial/procurement framing incompatible with this sprint.
4. **Prioritize** low-risk gateway, terminology spine, disambiguation-adjacent, and future-materials **vocabulary** routes.
5. **Skip** any route whose `content_file` already exists (no overwrite).
6. Target **8–12** drafts if enough safe eligible routes exist; otherwise create **all safe eligible** routes and document the shortfall.

---

## Eligible planned routes found (missing `content_file`)

**11** of **26** registered routes had no existing `content_file` at sprint start:

| route_id | content_file | Selection |
| --- | --- | --- |
| `what_is_sulfur` | `main/content/en/pages/what-is-sulfur.md` | **Selected** — gateway vocabulary; low risk with strict safety deferral |
| `sulfur_uses` | `main/content/en/pages/sulfur-uses.md` | **Skipped** — `industry_claims`; production/uses framing; claim-boundary sprint required first |
| `sodium_bisulfide` | `main/content/en/pages/sodium-bisulfide.md` | **Skipped** — `risk_level: high`; `safety_claims`; substance operations |
| `disulfide_bonds` | `main/content/en/pages/disulfide-bonds.md` | **Selected** — future materials; structure vocabulary only |
| `industrial_sulfur_systems` | `main/content/en/pages/industrial-sulfur-systems.md` | **Skipped** — procurement/supply-chain language; `industry_claims` |
| `sulfur_safety_context` | `main/content/en/pages/sulfur-safety-context.md` | **Skipped** — safety governance; `risk_level: high` |
| `hydrogen_sulfide_risk` | `main/content/en/pages/hydrogen-sulfide-risk.md` | **Skipped** — safety governance; highest hazard tier |
| `sds_and_sulfur_terms` | `main/content/en/pages/sds-and-sulfur-terms.md` | **Skipped** — safety governance; SDS context |
| `protein_disulfide_structure` | `main/content/en/pages/protein-disulfide-structure.md` | **Selected** — future materials; structure vocabulary; explicit medical exclusion |
| `molybdenum_disulfide` | `main/content/en/pages/molybdenum-disulfide.md` | **Skipped** — `industry_claims`; industrial lubricant/materials ops adjacency |
| `newsletter` | `main/content/en/pages/newsletter.md` | **Skipped** — utility/revenue layer; not sovereign reference corpus production |

**Note:** `acquire` already had `main/content/en/pages/acquire.md` — **skipped** (pre-existing; acquisition route excluded from Batch 1B scope regardless).

---

## Why fewer than 8 drafts were created

Only **3** of **11** missing routes met safe-eligibility criteria after exclusions. The repository currently registers **26** routes; **15** already had draft bodies before Sprint **5G** (including Batch **1A** methodology pages and prior terminology drafts). The remaining missing routes are predominantly **high-risk safety**, **industrial/procurement**, **substance operations**, or **non-reference utility** routes deferred by Batch 1 policy.

**Batch 1B target was 8–12**; **actual created count: 3** — the maximum safe eligible set from `routes.json` without registry expansion.

---

## Selected routes (created)

| route_id | content_file | lang | layer | risk (registry) |
| --- | --- | --- | --- | --- |
| `what_is_sulfur` | `main/content/en/pages/what-is-sulfur.md` | en | public_gateway | low |
| `disulfide_bonds` | `main/content/en/pages/disulfide-bonds.md` | en | future_materials | low |
| `protein_disulfide_structure` | `main/content/en/pages/protein-disulfide-structure.md` | en | future_materials | low |

---

## Skipped routes (summary)

| route_id | Reason |
| --- | --- |
| `sulfur_uses` | Industrial uses / `industry_claims`; production-adjacent |
| `sodium_bisulfide` | High risk; safety + substance page |
| `industrial_sulfur_systems` | Procurement / industrial systems language |
| `sulfur_safety_context` | Safety governance — dedicated sprint required |
| `hydrogen_sulfide_risk` | Safety governance — highest hazard |
| `sds_and_sulfur_terms` | Safety governance — SDS context |
| `molybdenum_disulfide` | `industry_claims`; industrial materials adjacency |
| `newsletter` | Utility layer — not reference corpus batch |
| `acquire` | Pre-existing content file; acquisition route out of scope |

---

## Files created

| File |
| --- |
| `main/content/en/pages/what-is-sulfur.md` |
| `main/content/en/pages/disulfide-bonds.md` |
| `main/content/en/pages/protein-disulfide-structure.md` |
| `main/data/BATCH_1B_EXISTING_ROUTE_DRAFT_CREATION_REPORT.md` |

**Files updated:** `DECISION_LOG.md`

---

## Frontmatter status (each created draft)

| route_id | status | publication_status | indexable | in_sitemap | language | locale | source_language |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `what_is_sulfur` | draft | non_public | false | false | en | en | en |
| `disulfide_bonds` | draft | non_public | false | false | en | en | en |
| `protein_disulfide_structure` | draft | non_public | false | false | en | en | en |

All paths match **`content_file`** in `routes.json` exactly.

---

## Why each draft remains non-public

Each page states explicitly that it is **not published**, **not indexable**, **not in the sitemap**, **not approved for public use**, and **not publication-ready**. Registry rows for these routes remain **`status: planned`** with **`indexable: false`** and **`in_sitemap: false`**. Quality Gate, source-locking, and claim activation have not occurred.

---

## Governance confirmations

| Topic | Confirmation |
| --- | --- |
| Why `routes.json` was not modified | Sprint charter: draft bodies only; route state changes belong in dedicated routing sprints |
| Why `internal_links.json` was not modified | Link graph updates require explicit linking batch; drafts use plain `route_id` references only |
| Why no claim was approved | Registries remain **inactive**; drafts disclaim approval |
| Why `[SOURCE REQUIRED]` markers remain | Factual/biochemistry/element assertions are not registry-backed |
| Why no route was published | All routes stay **planned**; no indexability or sitemap flags changed |
| Why no generated HTML | Content sprint only; templates and build output untouched |
| Public launch | **This is not public launch** |

---

## Draft-backed route count

| Metric | Count |
| --- | ---: |
| Total routes in `routes.json` | 26 |
| Draft-backed routes before Sprint 5G | 15 |
| Drafts created in Sprint 5G | 3 |
| **Draft-backed routes after Sprint 5G** | **18** |
| Planned routes still missing drafts | **8** |

The **8** remaining missing drafts are the skipped high-risk / industrial / utility routes listed above.

---

## Recommended next sprint

**Sprint 5H (suggested):**

1. **Register additional Batch 1 planned routes** in `routes.json` (still `planned`) from `LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md`—source governance, nomenclature governance, disambiguation, and DE spine concepts not yet in the registry—so future draft sprints have enough low-risk `route_id` targets to reach 8–12 pages per batch.
2. **Source-mapping sprint** for the three new Batch **1B** gateway/materials drafts before any boundary review or linking batch.
3. **Dedicated safety sprint** (separate charter) before drafting `sulfur_safety_context`, `hydrogen_sulfide_risk`, `sds_and_sulfur_terms`, or `sodium_bisulfide`.
4. Optional **Batch 1B review** (report-only) mirroring Sprint **5F** for the three new drafts.

---

*Sprint 5G — controlled corpus production. No registry or route-state mutations.*
