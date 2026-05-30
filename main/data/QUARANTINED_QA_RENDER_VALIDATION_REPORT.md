# Quarantined QA Render Validation Report

**Sprint:** 6M-C  
**Validation date:** 2026-05-30  
**Branch:** `claude/sprint-6m-c-template-registry-migration-and-quarantined-qa-render`

---

## Scripts run

| Script | Result |
|---|---|
| `scripts/validate_template_registry_l1.py` | **PASS** |
| `scripts/validate_template_layer_l1.py` | **PASS** |
| `scripts/validate_sample_output_l1.py` | **PASS** (8 quarantined files) |
| `scripts/validate_build_engine_l1.py` | **PASS** |
| `scripts/build.py --dry-run` | **PASS** |
| `scripts/build.py --dry-run --strict` | **PASS** |
| `scripts/build.py --render-quarantined-sample` | **PASS** (8 files written) |
| `scripts/corpus_production_runtime_l2.py` | **PASS** |
| `scripts/corpus_validation_runtime_l1.py` | **PASS** |
| `scripts/source_claim_guardrail_runtime_l1.py` | **PASS** |
| `scripts/corpus_production_planner_l2.py` | **PASS** |

---

## Sample output checked

- `site/_sample/home.html`
- `site/_sample/what_is_bisulfid.html`
- `site/_sample/de_core_mos2.html`
- `site/_sample/en_index_disambiguation_map.html`
- `site/_sample/sources.html`
- `site/_sample/corpus_methodology_overview.html`
- `site/_sample/de_bisulfide_hydrosulfide_sulfide.html`
- `site/_sample/bisulfide_hydrosulfide_sulfide.html`

No HTML outside `site/_sample/`.

---

## Template registry migration result

- **PASS** — `reference_page.html` and `term_page.html` bridged to hardened frames
- **PASS** — `build.py` `TEMPLATE_FRAME_BRIDGE` maps 6 registry template names
- **PASS** — `routes.json` not modified
- **WARN** — `glossary.html`, `newsletter.html`, `acquire.html` skeleton files remain; build bridges to hardened frames

---

## Governance confirmation

| Check | Result |
|---|---|
| No public HTML outside `site/_sample/` | **PASS** |
| No sitemap output | **PASS** |
| No navigation output | **PASS** |
| No route status changes | **PASS** |
| No registry changes | **PASS** |
| No content changes | **PASS** |
| No source approval | **PASS** |
| No claim approval | **PASS** |
| No `[SOURCE REQUIRED]` removal | **PASS** |
| noindex on all sample pages | **PASS** |
| Non-public QA markers present | **PASS** |
| Publication locks remain LOCKED | **PASS** |
| `production_can_safely_proceed` | **no** |

---

## Corpus posture (unchanged)

| Metric | Value |
|---|---:|
| Routes | 1,043 |
| Draft-backed | 985 |
| Missing drafts | 58 |
| Published | 0 |
| Indexable | 0 |
| in_sitemap | 0 |
| in_navigation | 0 |

---

## Publication lock quarantine exception

`validate_corpus_publication_lock_l1.py` was updated to permit HTML **only** under `site/_sample/`, aligned with `validate_sample_output_l1.py` (Sprint 6M-B design intent; deferred from 6M-B because no HTML was committed). HTML outside quarantine still fails the lock validator.

---

## Final validation conclusion

**PASS** — Template registry migration and quarantined QA render completed successfully. All listed validators and runtimes pass. The publication frame generates visible non-public HTML under quarantine without weakening publication, indexation, sitemap, navigation, source, or claim locks. Corpus Governance CI remains required on PR merge.

**This sprint does not authorize public launch.**
