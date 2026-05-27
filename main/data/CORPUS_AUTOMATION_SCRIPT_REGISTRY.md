# Corpus Automation Script Registry

**Sprint:** 5K  
**Status:** Active reference for governed automation scripts  
**Last updated:** 2026-05-27

---

## Why this registry exists

Bisulfid.com’s sovereign reference corpus is scaling toward **500 governed pages** and later **1,000+** and **3,000+** layers. Sprint **5I-A** established automation **doctrine**; Sprints **5I-B** and **5J** introduced isolated **L0** validators for route registration and draft production waves. Sprint **5K** introduces the first **L1 runtime layer** — a coordinated, read-only validation stack that operators can run locally before and after every production wave.

This registry documents **every current automation script**, what it reads, what it must never modify, whether it can block merge or publication, and how future **L2–L4** layers will extend the stack. Human review remains mandatory at merge, sample audit, source/claim signoff, and launch authorization.

---

## Script inventory

### Runtime orchestrator (L1)

| Script | Layer | Purpose |
| --- | --- | --- |
| `scripts/corpus_validation_runtime_l1.py` | L1 | Orchestrates all L1 validators and runs L0 validators in informational mode; prints PASS/FAIL summary |

### L1 validators (corpus-wide)

| Script | Layer | Purpose |
| --- | --- | --- |
| `scripts/validate_corpus_routes_l1.py` | L1 | Full `routes.json` integrity, publication posture, naming discipline, forbidden metadata frames |
| `scripts/validate_corpus_drafts_l1.py` | L1 | All draft-backed content files: frontmatter, sections, markers, forbidden frames |
| `scripts/validate_corpus_publication_lock_l1.py` | L1 | Publication lock: no published/indexable routes, no HTML output, 500-page threshold awareness |
| `scripts/validate_corpus_claims_l1.py` | L1 | Claim registry lock: inactive registries, no approved claims, no implied source-lock completion |
| `scripts/validate_corpus_references_l1.py` | L1 | Reference discipline: no raw URLs, no markdown links to unpublished routes, internal-link posture |

### L0 validators (wave-scoped)

| Script | Layer | Purpose |
| --- | --- | --- |
| `scripts/validate_route_registry_l0.py` | L0 | Sprint 5I-B wave-1 route registration checks (100 new routes) |
| `scripts/validate_content_drafts_l0.py` | L0 | Sprint 5J wave-1 draft production checks (50 new drafts via manifest) |

---

## Per-script specification

### `corpus_validation_runtime_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | Invokes other scripts; no direct corpus file reads |
| **Must not modify** | Any repository file |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — when run in CI (future); locally advisory until wired |
| **Can block publication** | Yes — intended pre-publication gate aggregator |
| **Human review** | Operator must review console output and linked reports |

---

### `validate_corpus_routes_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/routes.json`; checks `content_file` paths exist on disk for draft-backed summary |
| **Must not modify** | `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, registries, content pages |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — severity-1 route integrity failures |
| **Can block publication** | Yes — any indexable/published route flag |
| **Human review** | Required for warnings on pre-existing routes (e.g. safety-context route metadata keywords) |

**Checks:** JSON parse; duplicate `route_id`/`path`/`content_file`; required schema fields; all `status: planned`; no `indexable`/`in_sitemap`/`in_navigation` true; language/path/content_file alignment; naming discipline; forbidden public-launch and market/safety/medical/procurement/acquisition metadata; route and draft-backed counts.

---

### `validate_corpus_drafts_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/routes.json`, all referenced `content_file` Markdown paths, `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md` (wave-1 strict target list) |
| **Must not modify** | Content pages, registries, `routes.json` |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — errors on wave-1 strict targets or blocking draft violations |
| **Can block publication** | Yes — missing markers, forbidden frames, or public-ready language |
| **Human review** | Required for legacy draft warnings (18 pre-Sprint-5J drafts) |

**Checks:** Frontmatter vs registry; `status: draft`; `publication_status: non_public`; non-indexable; no raw URLs; no markdown links; `[SOURCE REQUIRED]` where needed; non-public notice; publication blockers and source/claim sections (strict on wave-1 targets); forbidden frames with negation-aware scanning.

---

### `validate_corpus_publication_lock_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/routes.json`, `main/data/sitemap_policy.json`, `main/config/navigation.json` (or `main/data/navigation.json` if present), `main/data/CORPUS_LAUNCH_THRESHOLD.md`, candidate HTML output dirs (`site/`, `public/`, `dist/`, `output/`, `build/`) |
| **Must not modify** | Any governance or output file |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes |
| **Can block publication** | Yes — primary publication lock validator |
| **Human review** | Required before any launch authorization sprint |

**Checks:** No published routes; no indexable/sitemap/navigation activation; no generated public HTML; sitemap/navigation inactive; no “launch now” language in threshold doc; 500-page floor enforced.

---

### `validate_corpus_publication_lock_l1.py` — publication lock role

This script is the **hard stop** against accidental public exposure. It must pass before any future sprint that generates HTML, activates sitemap entries, or flips route status.

---

### `validate_corpus_claims_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/claims/*.json`, `main/data/sources/source_registry.json`, draft content files referenced by `routes.json` |
| **Must not modify** | Claim registries, source registry, content pages |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — approved claims or active registry without authorization |
| **Can block publication** | Yes |
| **Human review** | Required for `[SOURCE REQUIRED]` satisfaction warnings |

**Checks:** All claim registries inactive; zero `status: approved`; pending_review unchanged; no content implies claim approval or source-lock completion; `[SOURCE REQUIRED]` not treated as satisfied.

---

### `validate_corpus_references_l1.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/routes.json`, `main/data/internal_links.json`, all draft content files |
| **Must not modify** | `internal_links.json`, content pages |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — raw URLs or markdown links to unpublished routes |
| **Can block publication** | Yes — missing internal link wiring is a documented pre-publication blocker |
| **Human review** | Required; draft-only pages do not require `internal_links.json` changes until wiring sprint |

**Checks:** Route_id/plain-text references preferred; no raw external URLs; no markdown links to planned unpublished routes; internal reference language non-public; documents missing link graph as pre-publication debt.

---

### `validate_route_registry_l0.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/routes.json` |
| **Must not modify** | `routes.json` or any other file |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — for wave-1 route registration PRs |
| **Can block publication** | Indirect — ensures registry discipline |
| **Human review** | Required for pre-existing route keyword warnings |

**Scope:** Sprint 5I-B wave-1 additions (100 routes). Does not replace L1 corpus-wide route validation.

---

### `validate_content_drafts_l0.py`

| Field | Value |
| --- | --- |
| **Reads** | `main/data/routes.json`, `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`, wave-1 target content files |
| **Must not modify** | Content pages or registries |
| **Read-only** | Yes |
| **Dependencies** | Python standard library only |
| **Network** | Not required |
| **Can block merge** | Yes — for wave-1 draft production PRs |
| **Can block publication** | Indirect |
| **Human review** | Required |

**Scope:** Sprint 5J wave-1 targets only (50 drafts). L1 draft validator covers all 68 draft-backed routes with legacy warnings for 18 pre-existing drafts.

---

## Future automation layers

| Layer | Planned role | Examples (not yet implemented) |
| --- | --- | --- |
| **L2** | Wave runners with manifest-driven scope | Route registration wave 2 runner; draft production wave 2 runner; post-wave report emitter |
| **L3** | Source/claim boundary automation | Marker-to-registry cross-check; forbidden-claim scanner with claim-group alignment; source proposal drafts (report-only) |
| **L4** | Pre-publication and CI integration | GitHub workflow wiring; merge-blocking on L1 FAIL; HTML build validation; hreflang/SEO metadata gate |

**Rule:** L2+ scripts must inherit L1 publication and claim locks. No layer may auto-publish, auto-approve claims, or strip `[SOURCE REQUIRED]` markers.

---

## Operator workflow

1. After any route or draft wave, run: `python scripts/corpus_validation_runtime_l1.py`
2. Review `main/data/CORPUS_L1_VALIDATION_REPORT.md` (updated per validation sprint)
3. Resolve **errors** before merge; triage **warnings** (legacy vs new)
4. Do not publish until L1 publication lock and claim lock both **PASS** and human launch authorization (S9) is granted

---

## Human review requirement

| Stage | Human action |
| --- | --- |
| **Local run** | Operator reads PASS/FAIL and warning list |
| **Merge** | Reviewer confirms L1 PASS for changed corpus scope |
| **Sample audit** | Editorial sample on draft quality (automation does not replace) |
| **Source/claim sprint** | Human approves sources and claim boundaries |
| **Launch authorization** | Owner signoff; 500-page threshold; all locks green |

Automation **reports**; humans **decide**.
