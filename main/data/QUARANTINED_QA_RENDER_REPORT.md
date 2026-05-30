# Quarantined QA Render Report

**Sprint:** 6M-C  
**Date:** 2026-05-30  
**Render command:** `python scripts/build.py --render-quarantined-sample`

---

## QA sample purpose

Produce a **tiny deterministic non-public HTML proof** that the 14,000-page publication frame can render visible pages under strict governance locks — without publishing routes, enabling indexation, or exposing sitemap/navigation.

---

## Sample page count

**8** rendered pages (within suggested 5–10 range).

---

## Selected route_ids

| route_id | Output path |
|---|---|
| `home` | `site/_sample/home.html` |
| `what_is_bisulfid` | `site/_sample/what_is_bisulfid.html` |
| `de_core_mos2` | `site/_sample/de_core_mos2.html` |
| `en_index_disambiguation_map` | `site/_sample/en_index_disambiguation_map.html` |
| `sources` | `site/_sample/sources.html` |
| `corpus_methodology_overview` | `site/_sample/corpus_methodology_overview.html` |
| `de_bisulfide_hydrosulfide_sulfide` | `site/_sample/de_bisulfide_hydrosulfide_sulfide.html` |
| `bisulfide_hydrosulfide_sulfide` | `site/_sample/bisulfide_hydrosulfide_sulfide.html` |

---

## Selected languages

| Language | Count | route_ids |
|---|---:|---|
| English (`en`) | 6 | home, what_is_bisulfid, en_index_disambiguation_map, sources, corpus_methodology_overview, bisulfide_hydrosulfide_sulfide |
| German (`de`) | 2 | de_core_mos2, de_bisulfide_hydrosulfide_sulfide |

---

## Selected page types

| Type | route_ids |
|---|---|
| Gateway / home | `home` |
| English terminology | `what_is_bisulfid` |
| German terminology | `de_core_mos2` |
| Disambiguation (EN index + EN triad + DE triad) | `en_index_disambiguation_map`, `bisulfide_hydrosulfide_sulfide`, `de_bisulfide_hydrosulfide_sulfide` |
| Reference / governance | `sources`, `corpus_methodology_overview` |
| Source-required emphasis | `de_core_mos2` (`source_required: true`, `[SOURCE REQUIRED]` in draft) |

---

## Why each page was selected

- **home** — Primary gateway frame; validates `home.html` + base shell.
- **what_is_bisulfid** — Core EN terminology via `term_page.html` bridge.
- **de_core_mos2** — DE terminology with explicit source-required posture and draft markers.
- **en_index_disambiguation_map** — Disambiguation cluster index (reference layer).
- **sources** — Source governance utility page.
- **corpus_methodology_overview** — Methodology / governance reference framing.
- **de_bisulfide_hydrosulfide_sulfide** — DE triad disambiguation authority.
- **bisulfide_hydrosulfide_sulfide** — EN triad disambiguation authority.

Selection is **fixed in build.py** (`QUARANTINED_SAMPLE_ROUTE_IDS`) for reproducibility.

---

## noindex posture

Every sample page includes:

- `<meta name="robots" content="noindex, nofollow">`
- Governance banner robots line: `noindex, nofollow`
- HTML comment preamble stating non-indexable QA posture

---

## Non-public QA marker posture

Every sample page includes:

- HTML comment: `QUARANTINED NON-PUBLIC QA RENDER — NOT A LAUNCH`
- Visible QA notice div with `data-publication-posture="non_public"`
- Governance banner title: `Non-public QA render — NOT A LAUNCH`
- Footer and frame notes referencing 14,000-page corpus **not** being a launch

---

## Source-required display result

- **de_core_mos2** and **what_is_bisulfid** visibly preserve `[SOURCE REQUIRED]` markers (highlighted in body; source bar states markers remain binding).
- Meta `bisulfid:source-required` set appropriately.
- **No source approval implied** — `claim_approval_state: no_claims_approved`, source registry posture inactive.

---

## Navigation / sitemap exclusion result

- All routes remain `in_sitemap: false`, `in_navigation: false` in registry (unchanged).
- Sample HTML displays `false` for both flags in governance banner and meta tags.
- Nav partial shows inactive navigation note; no nav links emitted.
- No sitemap XML generated.

---

## What rendered correctly

- Full base shell composition (head, governance banner, nav slot, breadcrumbs, footer)
- Template bridge from `reference_page.html` / `term_page.html` to hardened frames
- Markdown body conversion with headings, lists, tables, and `[SOURCE REQUIRED]` preservation
- Multilingual DE pages with correct `lang="de"` and LTR direction
- Route status `planned` visible in banner, meta, and body attributes

---

## What remains weak

- Minimal markdown renderer (not production-grade)
- Empty slots for term map, related terms, hreflang, internal links (expected under locks)
- `glossary.html` / `newsletter.html` / `acquire.html` skeleton files not individually QA-rendered (only 1 route each; bridged at build time)
- Publication lock validator required quarantine exception for `site/_sample/` (aligned with sample output validator)

---

## Why this is not a launch

- 0 published routes; all locks **LOCKED**
- `production_can_safely_proceed: no`
- Output quarantined under `site/_sample/` only
- Every page marked NOT A LAUNCH / non-public QA
- No sitemap, navigation, or indexation enabled

---

## Why this is not a reduced 14,000-page target

The QA sample is **8 pages** for engineering proof only. The **14,000-page minimum launch corpus** objective is unchanged. Current registry holds **1,043 planned routes** toward that objective — not a pilot or blog substitute.
