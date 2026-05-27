# Corpus Automation Validation Requirements (Sprint 5I-A)

## Purpose

This document defines **validation gates** for future corpus automation scripts, wave runners, and CI checks. Validators enforce sovereign-grade discipline across the **500-page launch program** and **1,000+ / 3,000+** expansion—without replacing human review.

**Sprint 5I-A defines requirements only.** No validators are implemented. No files are modified.

---

## Validation scope overview

| Domain | Primary registry / surface | When run |
| --- | --- | --- |
| Route registry | `routes.json` | S1, every PR touching routes |
| Content frontmatter | `main/content/**/*.md` | S2, every content PR |
| Content quality | Draft bodies | S2 post-wave, sample audit |
| Source markers | Drafts + `source_registry.json` | S2, S3, pre-launch |
| Claim registry | `main/data/claims/*.json` | S4, pre-launch |
| Internal links | `internal_links.json` | S5, pre-launch |
| Sitemap / indexation | `routes.json`, `sitemap_policy.json` | S6, S7, pre-launch |
| Navigation | `navigation.json` | S6, pre-launch |
| hreflang / translation | `hreflang_groups.json`, route metadata | S6, multilingual waves |
| Multilingual quality | Cross-language draft pairs | S4, S6 |
| SEO metadata | Route rows + frontmatter | S6 |
| Security / technical | Build, deps, configs | S7, every PR (when implemented) |
| Generated HTML | Output dirs / templates | S7, pre-launch |
| Launch threshold | Cohort count + gates | S8 only |

---

## Route registry validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **RV-01** | Every route has unique `route_id` | 1 |
| **RV-02** | Every route has unique `content_file` path (if set) | 1 |
| **RV-03** | Pre-launch routes: `status: planned` unless S9 charter | 1 |
| **RV-04** | Pre-launch: `indexable: false`, `in_sitemap: false` | 1 |
| **RV-05** | Valid `language`, `locale`, `source_language` | 1 |
| **RV-06** | `route_id` in blueprint or wave charter appendix | 2 |
| **RV-07** | `required_claim_groups` aligned to page class | 2 |
| **RV-08** | `risk_level` set; high-risk routes flagged | 2 |

---

## Content frontmatter validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **FV-01** | `route_id` matches owning route row | 1 |
| **FV-02** | `status: draft` for non-public production | 1 |
| **FV-03** | `publication_status: non_public` | 1 |
| **FV-04** | `indexable: false`, `in_sitemap: false` in frontmatter | 1 |
| **FV-05** | `language`, `locale`, `source_language` present | 1 |
| **FV-06** | Frontmatter YAML valid | 1 |

---

## Content quality validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **CQ-01** | Draft notice present (non-public, not publication-ready) | 1 |
| **CQ-02** | Required sections: purpose, corpus role, boundaries, blockers | 1 |
| **CQ-03** | Minimum substance threshold met (anti-thin) | 1 |
| **CQ-04** | No generic blog / textbook voice patterns (heuristic) | 2 |
| **CQ-05** | No raw URLs in body | 1 |
| **CQ-06** | No markdown links assuming published routes | 1 |
| **CQ-07** | Internal refs use `route_id` or plain text | 2 |
| **CQ-08** | Forbidden content absent (market, safety handling, medical, procurement, CAGR, acquisition) | 1 |

---

## Source marker validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **SM-01** | Factual lines without registry backing retain `[SOURCE REQUIRED]` | 1 |
| **SM-02** | No marker stripped in diff without source-mapping charter | 1 |
| **SM-03** | Draft does not claim source-locking complete unless charter | 1 |
| **SM-04** | Public render path: zero unresolved markers | 1 (pre-launch / S8) |

---

## Claim registry validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **CL-01** | No `status: approved` unless activation sprint | 1 |
| **CL-02** | Registries remain `inactive` pre-activation | 1 |
| **CL-03** | Draft does not imply claim approval | 1 |
| **CL-04** | Page `required_claim_groups` satisfied before publication | 1 (S8/S9) |

---

## Internal-link validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **IL-01** | Every edge source/target `route_id` exists in `routes.json` | 1 |
| **IL-02** | No raw URL edges where policy forbids | 1 |
| **IL-03** | Required cluster edges present at launch | 1 (S8) |
| **IL-04** | No self-referential broken placeholders | 1 |

---

## Sitemap / indexation validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **SI-01** | Sitemap includes only launch-authorized routes | 1 (S9) |
| **SI-02** | Pre-launch: no route `in_sitemap: true` without S9 | 1 |
| **SI-03** | Pre-launch: no route `indexable: true` without S9 | 1 |
| **SI-04** | `sitemap_policy.json` consistent with route flags | 1 (S8) |

---

## Navigation validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **NV-01** | Navigation entries reference existing planned/published routes | 1 |
| **NV-02** | Pre-launch: production nav excludes non-eligible routes | 1 |

---

## hreflang / translation validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **HF-01** | hreflang groups bidirectionally consistent | 1 (S8 multilingual) |
| **HF-02** | No orphan language route without group policy | 2 |
| **HF-03** | Translation status fields coherent with MULTILINGUAL_POLICY | 2 |

---

## Multilingual quality validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **MQ-01** | Non-EN pages flagged if MT-only heuristic triggers | 1 |
| **MQ-02** | DE pages not treated as EN copies (structural divergence check) | 2 |
| **MQ-03** | Per-language source posture documented | 2 |

---

## SEO metadata validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **SEO-01** | title, description, h1 present on route row | 1 |
| **SEO-02** | Metadata matches corpus role (no empty SEO spam) | 2 |
| **SEO-03** | hreflang metadata complete for public multilingual routes | 1 (S8) |

---

## Security / technical validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **TS-01** | Build completes without error | 1 |
| **TS-02** | No new dependencies without charter | 1 |
| **TS-03** | No new workflows without charter | 1 |
| **TS-04** | No secrets in tracked files | 1 |
| **TS-05** | Indexation guards unchanged without S9 | 1 |

---

## Generated HTML validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **GH-01** | No new public HTML output before S8 pass | 1 |
| **GH-02** | Generated pages map to authorized routes only | 1 (S9) |
| **GH-03** | No unresolved markers in public HTML | 1 (S9) |

---

## Broken-link validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **BL-01** | All required internal edges resolve | 1 |
| **BL-02** | No dead `route_id` in content plain-text refs (warn) | 2 |
| **BL-03** | External links policy-compliant (if any) | 2 |

---

## No-placeholder validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **NP-01** | Page body word/section count above category floor | 1 |
| **NP-02** | No lorem / TODO-only / single-sentence stubs | 1 |
| **NP-03** | Lists have prose rationale sections | 2 |

---

## No-thin-page validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **NT-01** | Terminology pages include scope, boundaries, source posture, related terms | 1 |
| **NT-02** | Disambiguation pages name all canonical records separated | 1 |
| **NT-03** | Index pages outbound-only to governed routes with structure | 1 |

---

## No-publication-before-500 validation

| Check ID | Requirement | Severity |
| --- | --- | --- |
| **L5-01** | Certified page count ≥ 500 | 1 (S8) |
| **L5-02** | Every certified page passes RV, FV, CQ, SM, CL, IL, SI, SEO gates | 1 (S8) |
| **L5-03** | No partial launch surfaces | 1 |
| **L5-04** | Owner authorization recorded before S9 | 1 |

---

## Failure severity levels

| Level | Meaning | Merge | Publication |
| --- | --- | --- | --- |
| **1 — Critical** | Governance breach; data integrity risk | **Block** | **Block** |
| **2 — Major** | Quality drift; fix before wave close | Block until fixed or owner waiver | Block |
| **3 — Minor** | Advisory; document in report | Warn | Block at S8 if uncorrected |
| **4 — Info** | Informational only | Pass | Pass |

---

## Conditions that block merge

Any **severity-1** failure in scope of the PR **blocks merge**, including but not limited to:

- Duplicate `route_id` or `content_file`
- Missing required frontmatter
- `[SOURCE REQUIRED]` stripped without charter
- Claim approved or registry activated without charter
- `indexable: true` / `in_sitemap: true` / `status: published` without S9
- Forbidden content patterns
- Broken required internal links
- Thin / placeholder page detected
- New dependencies or workflows without charter
- Build failure

Owner **documented waiver** may downgrade specific checks to severity-3 for merge only—never for S8/S9 without re-validation.

---

## Conditions that block publication

Publication (S9) is blocked while **any** of the following holds:

1. Certified governed page count **< 500**.
2. Any severity-1 failure on any launch-cohort page.
3. Any public `[SOURCE REQUIRED]` marker unresolved.
4. Claim registries inactive where approval required.
5. Broken internal link graph for required edges.
6. SEO / technical / security validation incomplete.
7. Owner authorization not recorded.
8. `CORPUS_LAUNCH_THRESHOLD.md` final conditions not all true.

---

## Validator implementation notes (future)

- Validators should emit **machine-readable reports** (JSON or Markdown tables) under `main/data/`.
- Check IDs (RV-01, FV-01, etc.) must appear in output for traceability.
- Read-only validators (L0) ship before any patch proposers (L2).
- CI integration requires dedicated workflow charter sprint—not this sprint.

---

## Relationship to other documents

- `CORPUS_AUTOMATION_CONTROL_LAYER.md` — what automation may/may not do.
- `CORPUS_AUTOMATION_MANIFEST.md` — stage file permissions and failure IDs.
- `CORPUS_AUTOMATION_WAVE_PROTOCOL.md` — when validators run in wave lifecycle.
- `CORPUS_LAUNCH_THRESHOLD.md` — authoritative launch gate list for L5-* checks.

---

*Sprint 5I-A — validation requirements only. No validators implemented.*
