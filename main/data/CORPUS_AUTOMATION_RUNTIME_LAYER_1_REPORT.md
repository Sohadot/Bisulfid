# Corpus Automation Runtime Layer 1 Report

**Sprint:** 5K  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5k-corpus-automation-runtime-layer-1`

---

## Why this sprint exists

Sprints **5I-A** through **5J** established automation doctrine and two isolated **L0** validators for the first route registration wave (126 routes) and first draft production wave (50 drafts, 68 draft-backed total). Manual repetition of the same governance checks before every future wave does not scale toward **500**, **1,000+**, or **3,000+** governed pages.

Sprint **5K** creates the first **executable read-only automation runtime** — Layer 1 — that validates the **entire current corpus state** in one local command without modifying routes, content, registries, or generating public output.

---

## Why automation is necessary now

| Metric | Value |
| --- | ---: |
| Planned routes | 126 |
| Draft-backed routes | 68 |
| Routes without drafts | 58 |
| Gap to 500-page launch floor | 374 routes (minimum) |

At **126 routes** and **68 drafts**, cross-checking registry integrity, draft discipline, publication locks, claim locks, and reference rules manually before each wave is error-prone. L1 automation encodes the control doctrine into repeatable, stdlib-only scripts that operators can run locally and (later) in CI.

---

## Relationship to the 500-page sovereign launch threshold

Sprint **5H** (`CORPUS_LAUNCH_THRESHOLD.md`, `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`) requires **500 governed pages** before public launch. The corpus remains far below that floor (**126** registered routes, **68** with draft bodies).

L1 validators **enforce** that:

- No route is published, indexable, in sitemap, or in navigation
- No public HTML output exists
- The 500-page threshold is not bypassed by documentation or config
- Claim and source registries remain inactive with zero approved claims

Automation accelerates **validation toward** 500 pages; it does not lower the bar or authorize launch.

---

## Relationship to 1,000+ and 3,000+ corpus scale

The L1 layer is designed as **foundation infrastructure**:

- **Corpus-wide** checks (not wave-scoped only like L0)
- **Additive** validators per concern (routes, drafts, publication, claims, references)
- **Read-only** and dependency-free for safe local and future CI use
- **Warning vs error** tiers for legacy content vs new wave strictness

Future waves add routes and drafts in batches of 40–120; L1 runs after each batch to prevent governance debt accumulation. L2 wave runners and L3 source/claim tooling will build on this runtime without rewriting L0/L1 validators.

---

## Why this sprint creates validators but no pages or routes

| Action | Sprint 5K |
| --- | --- |
| New routes | **No** |
| New content pages | **No** |
| Publish routes | **No** |
| Approve claims | **No** |
| Generate public HTML | **No** |
| Modify registries | **No** |
| Add dependencies | **No** |
| Create GitHub workflows | **No** |
| L1 validation scripts + reports | **Yes** |

Production waves (5I-B, 5J) and automation infrastructure (5K) are **separated** so tooling never races ahead of corpus state and governance locks stay intact.

---

## Scripts created

| Script | Responsibility |
| --- | --- |
| `scripts/corpus_validation_runtime_l1.py` | Orchestrates L1 + informational L0; PASS/FAIL summary |
| `scripts/validate_corpus_routes_l1.py` | Full route registry integrity and publication posture |
| `scripts/validate_corpus_drafts_l1.py` | All draft-backed content discipline |
| `scripts/validate_corpus_publication_lock_l1.py` | Hard publication lock |
| `scripts/validate_corpus_claims_l1.py` | Claim and source-lock registry lock |
| `scripts/validate_corpus_references_l1.py` | URL, link, and internal reference discipline |

Existing L0 validators were **not rewritten**; they remain wave-scoped complements invoked by the runtime.

---

## Validation responsibilities (L1)

| Domain | Validator | Key guarantees |
| --- | --- | --- |
| Route registry | `validate_corpus_routes_l1.py` | JSON valid; no duplicates; all planned; naming and language alignment |
| Draft content | `validate_corpus_drafts_l1.py` | Frontmatter, sections, markers, forbidden frames |
| Publication lock | `validate_corpus_publication_lock_l1.py` | No public exposure path active |
| Claim lock | `validate_corpus_claims_l1.py` | Inactive registries; no implied approval |
| References | `validate_corpus_references_l1.py` | No raw URLs; no unpublished markdown links |

---

## Publication lock responsibilities

The publication lock validator ensures **zero** published or indexable routes, inactive sitemap and navigation policies, no HTML in output directories, and no documentation recommending immediate public launch. This is the primary **accident prevention** layer for a corpus that will eventually generate static site output.

---

## Claim lock responsibilities

All claim registries remain **inactive**. No claim has `status: approved`. Content must not imply source-locking is complete. `[SOURCE REQUIRED]` markers are **not** treated as satisfied. Claim-sensitive pages remain blocked from publication until dedicated source/claim sprints.

---

## Content quality responsibilities

L1 draft validation enforces structural discipline (frontmatter, non-public notices, publication blockers, source/claim sections on wave-1 strict targets) and scans for forbidden frames (safety guides, medical advice, market reports, CAGR, etc.). **Editorial quality** and sample audit remain human responsibilities per `CORPUS_AUTOMATION_CONTROL_LAYER.md`.

---

## Security and technical discipline

- All scripts: **Python standard library only**
- All scripts: **read-only** (no file writes)
- No network access required
- Safe to run repeatedly on developer machines
- Unicode-safe orchestration output on Windows

Technical validation of builds, hreflang, and security regressions remains future **L4** work.

---

## Why no workflows were created yet

Sprint **5I-A** deferred CI until automation requirements and a local runtime existed. L1 must be proven locally and documented before merge-blocking GitHub Actions are wired. Workflows without stable validators risk false confidence or blocking merges on undefined behavior.

---

## Why no dependencies were added

Governed automation must remain auditable and portable. Stdlib-only scripts require no `pip install`, no supply-chain surface, and no version lock-in. Future L4 CI may add tooling only under explicit charter.

---

## Why no public output was generated

Public HTML generation is gated behind the **500-page** program, publication authorization, and passing L1 publication/claim locks. This sprint validates governance state only.

---

## Support for future waves

| Future work | L1 support |
| --- | --- |
| Route registration wave 2 | `validate_corpus_routes_l1.py` catches registry regressions immediately |
| Draft production wave 2 | `validate_corpus_drafts_l1.py` strict mode via manifest pattern |
| Source mapping sprint | Claim/reference validators flag premature satisfaction |
| Internal-link wiring | Reference validator documents wiring debt |
| Claim boundary review | Claims validator enforces inactive/approved lock |

Recommended operator habit: run `corpus_validation_runtime_l1.py` after every wave and archive results in `CORPUS_L1_VALIDATION_REPORT.md`.

---

## Recommended next sprint

**Sprint 5L:** Source and claim boundary review for the **50 Sprint 5J drafts** before draft production wave 2. Align `[SOURCE REQUIRED]` markers with registry posture, triage the 14 `pending_review` claims, and resolve legacy draft warnings for the 18 pre-5J pages in a dedicated normalization sprint or fold into 5L scope.

See `CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md` for full wave ordering rationale.

---

## Artifacts created (Sprint 5K)

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
- `DECISION_LOG.md` — Sprint 5K entry

**Not modified:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, navigation configs, source/claim/ontology registries, all content pages, root `README.md`, workflows, package files, generated HTML.
