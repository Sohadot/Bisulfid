# Corpus L1 Validation Report

**Sprint:** 5K  
**Validation date:** 2026-05-27  
**Runtime:** `scripts/corpus_validation_runtime_l1.py`  
**Mode:** Read-only; Python standard library only

---

## Scripts run

| Script | Layer | Exit code | Result |
| --- | --- | ---: | --- |
| `validate_corpus_routes_l1.py` | L1 | 0 | **PASS** |
| `validate_corpus_drafts_l1.py` | L1 | 0 | **PASS** |
| `validate_corpus_publication_lock_l1.py` | L1 | 0 | **PASS** |
| `validate_corpus_claims_l1.py` | L1 | 0 | **PASS** |
| `validate_corpus_references_l1.py` | L1 | 0 | **PASS** |
| `validate_route_registry_l0.py` | L0 (informational) | 0 | **PASS** |
| `validate_content_drafts_l0.py` | L0 (informational) | 0 | **PASS** |

**Runtime summary:** **PASS** — all L1 validators passed.

---

## Files checked

| File / scope | Checked by |
| --- | --- |
| `main/data/routes.json` | routes L1, publication lock L1, claims L1, references L1, L0 validators |
| `main/data/sitemap_policy.json` | publication lock L1 |
| `main/config/navigation.json` | publication lock L1 |
| `main/data/CORPUS_LAUNCH_THRESHOLD.md` | publication lock L1 |
| `main/data/internal_links.json` | references L1 |
| `main/data/claims/*.json` | claims L1 |
| `main/data/sources/source_registry.json` | claims L1 |
| `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md` | drafts L1, content drafts L0 |
| **68** draft Markdown files (all `content_file` paths with existing files) | drafts L1, claims L1, references L1 |
| HTML output dirs (`site/`, `public/`, `dist/`, `output/`, `build/`) | publication lock L1 |

**Not modified by validation run:** all of the above remain unchanged.

---

## Corpus counts

| Metric | Count |
| --- | ---: |
| Total planned routes | 126 |
| Draft-backed routes | 68 |
| Routes missing drafts | 58 |
| Sprint 5J wave-1 strict draft targets | 50 |
| Pre-existing legacy drafts (warnings tier) | 18 |
| Published routes | 0 |
| Indexable routes | 0 |
| Approved claims | 0 |
| Pending review claims | 14 |
| Markdown links in drafts | 0 |
| Raw URLs in drafts | 0 |

---

## Route registry result

**PASS** (0 errors, 4 warnings)

| Check | Result |
| --- | --- |
| JSON parse | **PASS** |
| Duplicate `route_id` | **PASS** |
| Duplicate `path` | **PASS** |
| Duplicate `content_file` | **PASS** |
| Required schema fields | **PASS** |
| All `status: planned` | **PASS** |
| No `indexable: true` | **PASS** |
| No `in_sitemap: true` | **PASS** |
| No `in_navigation: true` | **PASS** |
| `content_file` language alignment | **PASS** |
| Naming discipline | **PASS** |

**Warnings (pre-existing route metadata keywords):**

- `sodium_bisulfide`: forbidden keyword `handling instruction`
- `sulfur_safety_context`: forbidden keywords `handling instruction`, `dosage`
- `hydrogen_sulfide_risk`: forbidden keyword `handling instruction`

These routes remain **planned** and **non-public**; keywords appear in safety-context route metadata registered before wave 1. Human review recommended before any future publication consideration.

---

## Draft frontmatter result

**PASS** (0 errors, 92 warnings)

| Check | Result |
| --- | --- |
| All referenced content files exist | **PASS** |
| `route_id` matches registry | **PASS** |
| Wave-1 strict: language/locale/source_language | **PASS** |
| Wave-1 strict: `status: draft`, `publication_status: non_public` | **PASS** |
| Wave-1 strict: non-indexable, not in sitemap | **PASS** |
| No raw URLs | **PASS** |
| No markdown links to unpublished routes | **PASS** |
| Wave-1 strict: required sections and markers | **PASS** |
| Wave-1 strict: forbidden frames | **PASS** |

**Warnings:** **18 pre-Sprint-5J legacy drafts** lack full Sprint 5J frontmatter and section structure (`locale`, `source_language`, source/claim status section, publication blockers). Several legacy pages list forbidden frames in **non-goals** sections (e.g. `what_is_sulfur`, `disulfide_bonds`, `sources`); L1 downgrades these to warnings for pre-existing content.

**Legacy draft route_ids with warnings:** `home`, `what_is_sulfur`, `sulfur_compounds`, `what_is_bisulfid`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `bisulfide_hydrosulfide_sulfide`, `disulfide_bonds`, `protein_disulfide_structure`, `german_english_chemical_terms`, `glossary`, `sources`, `corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, `de_method_translator_playbook`, `acquire`.

**Not auto-fixed:** per sprint charter, legacy draft normalization is deferred to a future sprint.

---

## Publication lock result

**PASS** (0 errors, 0 warnings)

| Check | Result |
| --- | --- |
| No published routes | **PASS** |
| No indexable routes | **PASS** |
| No sitemap activation | **PASS** |
| No navigation activation | **PASS** |
| No generated public HTML | **PASS** |
| 500-page threshold enforced | **PASS** |
| Below 500-page floor | **PASS** (126 routes) |

---

## Claim registry result

**PASS** (0 errors, 2 warnings)

| Check | Result |
| --- | --- |
| All claim registries inactive | **PASS** |
| Zero approved claims | **PASS** |
| Pending review unchanged (14) | **PASS** |
| No content claims source-lock complete | **PASS** |
| `[SOURCE REQUIRED]` not satisfied globally | **PASS** |

**Warnings:**

- `sulfur_compounds`: language may treat `[SOURCE REQUIRED]` as satisfied
- `quality_gate_public_explainer`: language may treat `[SOURCE REQUIRED]` as satisfied

Human editorial review recommended; no registry or content changes in Sprint 5K.

---

## Reference and link discipline result

**PASS** (0 errors, 2 warnings)

| Check | Result |
| --- | --- |
| No markdown links in drafts | **PASS** (0 found) |
| No raw external URLs in drafts | **PASS** (0 found) |
| `internal_links.json` status | **planned** (not activated) |
| Missing internal link wiring | **68** routes (expected pre-wiring) |

**Warnings:**

- `sources`: language may assume published pages
- Internal link graph wiring remains a **pre-publication blocker**; draft-only pages do not require `internal_links.json` changes in Sprint 5K

---

## Forbidden frame result

| Scope | Result |
| --- | --- |
| Wave-1 strict targets (50 drafts) | **PASS** — no blocking forbidden frames |
| Legacy drafts (18) | **Warnings only** — frames often appear in non-goals lists |

---

## Raw URL and markdown link result

| Check | Count | Result |
| --- | ---: | --- |
| Raw URLs in draft bodies | 0 | **PASS** |
| Markdown links in draft bodies | 0 | **PASS** |

---

## Unresolved warnings (summary)

| Category | Count | Disposition |
| --- | ---: | --- |
| Route metadata forbidden keywords | 4 | Pre-existing safety-context routes; review before publication |
| Legacy draft structure | ~76 | Normalize in future sprint (5L or dedicated legacy pass) |
| Legacy forbidden-frame mentions in non-goals | ~16 | Warnings only; strict on new waves |
| `[SOURCE REQUIRED]` satisfaction language | 2 | Source/claim boundary review (recommended 5L) |
| Internal link wiring debt | 68 | Expected; wiring sprint before publication |
| Reference language assumes publication | 1 | Editorial review |

**Total L1 errors:** 0  
**Total L1 warnings:** ~100 (non-blocking)

---

## Final validation conclusion

**L1 corpus validation: PASS**

The Bisulfid sovereign reference corpus at **126 planned routes** and **68 draft-backed pages** satisfies Layer 1 automation checks. Publication locks, claim locks, and reference discipline hold. Pre-existing legacy draft and safety-route metadata warnings are **documented** and **not auto-fixed** in Sprint 5K.

**Publication readiness:** **Not ready for publication.** Corpus remains below the **500-page** launch threshold. All routes **planned**; all claim registries **inactive**; zero approved claims.

**Operator command:**

```bash
python scripts/corpus_validation_runtime_l1.py
```

Re-run after every future route, draft, source, claim, or internal-link wave.
