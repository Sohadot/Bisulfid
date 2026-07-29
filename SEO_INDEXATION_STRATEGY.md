# Bisulfid Atlas — Indexation Diagnosis & Strategy

Status: diagnosis + phase 1 remediation shipped. Phases 2–4 are proposals for review.

## 1. What Search Console reports (24/07/2026)

| Metric | Value |
| --- | --- |
| Pages **in the index** | **3** |
| Pages **not indexed** | ~3,510 (5 reasons) |
| Sitemap URLs submitted | ~13,998 |

Breakdown of "not indexed":

| Reason (GSC) | Pages | Meaning |
| --- | --- | --- |
| Détectée, actuellement non indexée (Discovered – not indexed) | 3,369 | Google knows the URL but **declined to even crawl it** |
| Explorée, actuellement non indexée (Crawled – not indexed) | 132 | Crawled, then **judged not worth indexing** |
| Introuvable (404) | 3 | Directory URLs with no page (see §3) |
| Exclue par la balise "noindex" | 2 | Intentional `noindex` |
| Page avec redirection | 2 | Redirects |

The headline number — **only 3 of ~14,000 pages indexed** — is driven almost entirely by the first two rows, not by the 404s.

## 2. Root cause of non-indexation: thin, near-duplicate pages at scale

The atlas generates pages by a combinatorial expansion:

```
{compound} × {facet: cmp|aud|air|term} × {audience: ai|res|stu|chem…} × {sub: tech|res|know|edu…}
```

This yields ~14,000 URLs. Two sibling leaf pages were compared directly and found **~99 % identical** — the only differences were a swapped audience phrase:

- `.../cmp/ai/tech/` → "analysts and institutional readers"
- `.../cmp/res/res/` → "researchers and journalists"

Each page is ~365 words of the same template. Google classifies this pattern as **doorway / thin content** and, at 14 K scale, applies "Discovered – currently not indexed" as a crawl-budget/quality verdict. **No code change forces indexation** — the fix is to reduce and enrich the indexable surface. This is a content-strategy decision, documented below for review.

## 3. Phase 1 — 404 repair (shipped)

**Symptom:** Search Console "Introuvable (404)" on directory URLs such as
`/en/terminology/`, `/en/terminology/sodium-hydrosulfide/cmp/`.

**Cause:** `build_breadcrumbs()` emitted an `<a href="/ancestor/">` link for
*every* breadcrumb ancestor, even though only leaf routes have an `index.html`.
Each page therefore linked to several directory URLs that return 404. Across the
site this produced **67,069 dead links** pointing at **21,690 non-existent
directory URLs**.

**Fix:**
- `scripts/atlas_dossier_common_l3.py` — `build_breadcrumbs()` now takes a
  `valid_paths` set and renders an ancestor as plain text (`<span>`) instead of a
  link when no page exists at that path. Both renderers
  (`atlas_render_dossier_l3.py`, `atlas_render_release_l2.py`) pass the set.
- `scripts/fix_breadcrumb_dead_links_l1.py` — one-off, idempotent pass that
  repaired the already-published HTML in place (13,949 files, 67,069 dead links
  → text) without re-rendering, so later hub refinements are preserved.

Real links (`/`, `/en/`, …) are untouched; the current-page marker is untouched.
This removes the 404 crawl targets and concentrates crawl budget on real pages.

## 4. Phase 2 (proposed) — shrink the indexable surface

Goal: stop asking Google to index ~14 K near-duplicates.

1. **Choose a canonical/pillar set** — one strong page per real concept
   (e.g. `sodium-hydrosulfide`), not per audience×facet permutation.
2. **`noindex` the thin permutation leaves** (the `/cmp/ai/tech/` family) and
   **remove them from the sitemaps**. Keep them reachable for humans, but stop
   competing for index slots.
3. Expected effect: the indexable count drops from ~14 K to a few hundred *high
   quality* URLs — the set Google will actually index.

## 5. Phase 3 (proposed) — consolidate & enrich

1. **Collapse the audience/sub permutations** into a single richer page per
   concept, with audience framing as *sections* rather than *separate URLs*.
2. Raise per-page uniqueness well above the current ~1 %: concept-specific
   definitions, properties, relationships, and cited sources.
3. **Build real section hubs** at the levels breadcrumbs used to link to
   (`/en/terminology/`, per-compound roots) with curated child listings — these
   become legitimate indexable navigation pages instead of 404s.

## 6. Phase 4 (proposed) — sitemap hygiene & re-validation

1. Sitemaps list **only indexable URLs**; add `lastmod`.
2. In GSC, use **"Valider la correction"** on the 404 report after Phase 1
   deploys, and re-inspect a sample of pillar URLs.
3. Track "in index" count weekly; expect gradual recovery as quality signals
   improve.

## 7. Deploy note

Changes live in the repository source only. Publishing to `bisulfid.com`
(GitHub Pages) requires running the **"Pages public deploy"** workflow
(`workflow_dispatch`). Page count remains 14,041 (no pages added or removed in
Phase 1).
