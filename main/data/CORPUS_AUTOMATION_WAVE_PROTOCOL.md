# Corpus Automation Wave Protocol (Sprint 5I-A)

## Purpose

This document defines **how future production waves execute** under the corpus automation control layer. It operationalizes `CORPUS_PRODUCTION_WAVE_MODEL.md` and `CORPUS_AUTOMATION_MANIFEST.md` into repeatable **pre-flight**, **execution**, and **post-wave** procedures.

**Sprint 5I-A creates protocol only.** No waves are executed. No routes, content, or registries are modified.

---

## Wave types and sizes

| Wave | Size | Stage | Output |
| --- | --- | --- | --- |
| **Route planning / registration** | **80–120 routes** | S1 | New **planned** rows in `routes.json` |
| **Draft production** | **40–60 pages** | S2 | Non-public `content_file` bodies |
| **Source mapping** | **40–60 pages** | S3 | Registry alignment + mapping reports |
| **Claim boundary** | **40–60 pages** | S4 | Boundary reports; forbidden-claim scans |
| **Internal-link wiring** | **40–60 edges** | S5 | Cluster slice in `internal_links.json` |
| **SEO / metadata validation** | Full cluster or cohort sample | S6 | Metadata validation report |
| **Technical / security validation** | Full repo or PR scope | S7 | Build/security report |
| **Pre-publication validation** | Launch cohort (**500** pages) | S8 | Readiness matrix |

**Launch (S9)** is **not** a wave type—it is a **separate owner-authorized sprint** after S8 pass.

---

## Universal wave lifecycle

```
CHARTER → S0 PRE-FLIGHT → EXECUTE STAGE(S) → S-VALIDATE → POST-WAVE AUDIT → REPORT → DECISION_LOG
```

1. **Charter** — Sprint declares wave type, size, blueprint slice, forbidden surfaces.
2. **S0 pre-flight** — Validate charter against manifest; scan forbidden modifications.
3. **Execute** — Human and/or governed tooling performs stage work.
4. **S-validate** — Run stage validators (`CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`).
5. **Post-wave audit** — Sample review (draft waves); merge review (registry waves).
6. **Report** — Write `main/data/*_WAVE_REPORT.md` or sprint report.
7. **DECISION_LOG** — Append entry when wave completes.

---

## Route planning wave (80–120 routes)

### Pre-flight checks

- [ ] Blueprint rows identified with `proposed_route_id` list attached to charter.
- [ ] No row already in `routes.json` unless charter says update (default: skip duplicates).
- [ ] Readiness matrix consulted for high-risk exclusions.
- [ ] Wave size within 80–120 (or documented exception).
- [ ] Charter forbids: `published`, `indexable: true`, `in_sitemap: true`.

### Execution rules

- Add rows as **`status: planned`** only.
- Set **`indexable: false`**, **`in_sitemap: false`** on every new row.
- Assign unique `route_id`, unique `content_file` path, valid language/locale.
- Do **not** create `content_file` bodies in route-only wave unless charter explicitly combines stages.

### Post-wave checks

- [ ] Row count matches manifest.
- [ ] No duplicate `route_id` or paths.
- [ ] All new routes **planned** and non-indexable.
- [ ] Validation report severity-1 = 0.

---

## Draft production wave (40–60 pages)

### Pre-flight checks

- [ ] Every target `route_id` exists in `routes.json`.
- [ ] Every target `content_file` **does not exist** (no overwrite).
- [ ] Wave size 40–60 (or documented exception).
- [ ] Draft template and frontmatter spec attached to charter.

### Execution rules

- Create Markdown only at exact `content_file` paths from `routes.json`.
- Frontmatter: `route_id`, `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`, language/locale/source_language.
- Include draft notice, corpus role, boundaries, markers, publication blockers.
- Preserve `[SOURCE REQUIRED]` on factual lines pending source-lock.

### Post-wave checks

- [ ] File count matches manifest.
- [ ] Sample audit ≥ 10% (min 3 pages) passes.
- [ ] No forbidden content patterns (market, safety handling, medical, etc.).
- [ ] No raw URLs; no published-route markdown links.

---

## Source mapping wave (40–60 pages)

### Pre-flight checks

- [ ] Draft bodies exist for target routes.
- [ ] Charter allows `source_registry.json` edits if registry writes planned.
- [ ] SOURCE_POLICY categories identified per page class.

### Execution rules

- Map markers to registry rows or document mapping gaps.
- **Do not** remove markers without human signoff sprint.
- **Do not** auto-verify sources.

### Post-wave checks

- [ ] Mapping report covers every target page.
- [ ] No unauthorized marker removal.
- [ ] Registry diff reviewed if touched.

---

## Claim boundary wave (40–60 pages)

### Pre-flight checks

- [ ] Claim registries expected **inactive** unless activation charter.
- [ ] `required_claim_groups` known per route.

### Execution rules

- Produce boundary reports; forbidden-claim pattern scans.
- **No** `status: approved` writes.
- **No** registry activation by automation.

### Post-wave checks

- [ ] Every page has documented claim boundary.
- [ ] No approval implied in drafts.
- [ ] High-risk routes flagged for deferred review.

---

## Internal-link wiring wave (40–60 edges)

### Pre-flight checks

- [ ] Cluster spec identifies hub and spoke `route_id` set.
- [ ] All target `route_id` values exist in `routes.json`.

### Execution rules

- Add **route_id → route_id** edges only (no raw URLs).
- Do not imply routes are public.
- Prefer **planned** edge semantics until launch.

### Post-wave checks

- [ ] No dead `route_id` references.
- [ ] Edge count within wave limit.
- [ ] Link validation report pass.

---

## SEO / metadata validation wave

### Scope

- Validate title, description, H1, hreflang fields on route rows and frontmatter alignment.
- May run on full cluster or statistical sample pre-launch.

### Post-wave checks

- [ ] All severity-1 SEO failures resolved or waived by owner (documented).
- [ ] No indexation flags enabled.

---

## Technical / security validation wave

### Scope

- Build passes; no accidental public output; indexation guard scan; dependency charter compliance; config drift.

### Post-wave checks

- [ ] Build green.
- [ ] No new dependencies without charter.
- [ ] No workflow changes without charter.
- [ ] Security scan severity-1 = 0.

---

## Pre-publication validation wave

### Scope

- Aggregate **all** launch gates for **≥ 500** pages.
- Produce readiness matrix: pass/fail per page and per gate category.

### Hard rule

**No S9 launch** unless this wave reports **500** pages passing **all** gates in `CORPUS_LAUNCH_THRESHOLD.md`.

---

## Identity and path rules

### route_id uniqueness

- **Globally unique** across `routes.json`.
- Pattern: lowercase snake_case aligned to blueprint.
- Automation **must reject** duplicates at S0.

### content_file path rules

- Must match `routes.json` exactly when draft exists.
- One primary `content_file` per route.
- Paths under `main/content/{lang}/pages/` unless charter exception.
- **No overwrite** of existing files in default draft wave.

### language / locale rules

- `language` and `locale` must match route charter (en, de, ar, zh, ja).
- `source_language` set per route record.
- Multilingual pages are **controlled terminology records**—not MT clones.

---

## Content integrity rules

| Rule | Enforcement |
| --- | --- |
| **No duplicate pages** | Same corpus role + same term → merge concept, do not duplicate |
| **No fake pages** | Registry row without charter draft plan → flag as registry-only |
| **No broken links** | internal_links targets must resolve to `route_id` in registry |
| **No unresolved public markers** | Public tier forbidden while `[SOURCE REQUIRED]` present |
| **No claim approval by automation** | Reports only |
| **No public route activation by automation** | S9 human only |

---

## Wave sequencing discipline

Recommended order per vertical slice (repeat until 500):

```
S1 → S2 → S3 → S4 → S5 → (S6/S7 periodic) → … → S8 → S9
```

- **Do not** run S5 before S1 for the same cluster (no links to unregistered routes).
- **Do not** run S8 until cohort size ≥ 500 and prior stage reports archived.
- S6/S7 may run **every N waves** or on every PR—charter decides.

---

## Stop-the-line conditions

Halt wave and remediate before continuing if:

1. Severity-1 validation failure.
2. Sample audit failure on draft wave.
3. Marker stripping detected.
4. Accidental indexation or publication flag.
5. Forbidden content pattern in batch.
6. Wave size exceeded without audit capacity.

---

## Relationship to other documents

- `CORPUS_AUTOMATION_CONTROL_LAYER.md` — automation boundaries and philosophy.
- `CORPUS_AUTOMATION_MANIFEST.md` — stage I/O and file permissions.
- `CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md` — gate definitions and severity.
- `CORPUS_PRODUCTION_WAVE_MODEL.md` — strategic wave sizes and rejected shortcuts.

---

*Sprint 5I-A — wave protocol doctrine only. No waves executed.*
