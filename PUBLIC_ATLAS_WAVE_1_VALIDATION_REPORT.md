# Public Atlas Wave 1 — Validation Report

## Validation Summary

All 52 Wave 1 pages passed content validation criteria.

---

## Page-Level Validation Checklist

Each page was validated against:

| Check | Pass/Fail |
|-------|-----------|
| `robots: index, follow` (no noindex) | PASS — all 52 pages |
| Unique canonical URL per page | PASS — all 52 pages |
| Unique, descriptive title tag | PASS — all 52 pages |
| Unique meta description (under 160 chars) | PASS — all 52 pages |
| Single H1 matching page topic | PASS — all 52 pages |
| Minimum 4 internal links | PASS — all 52 pages |
| Breadcrumb navigation | PASS — all 52 pages |
| Source posture section present | PASS — all 52 pages |
| No `[SOURCE REQUIRED]` markers | PASS — all 52 pages |
| No draft language | PASS — all 52 pages |
| No noindex directive | PASS — all 52 pages |
| No medical claims | PASS — all 52 pages |
| No safety claims | PASS — all 52 pages |
| No procurement claims | PASS — all 52 pages |
| No market performance claims | PASS — all 52 pages |
| `data-route-status="published"` | PASS — all 52 pages |
| Design system classes present | PASS — all 52 pages |
| CSP meta tag present | PASS — all 52 pages |

---

## Bisulfide/Bisulfite Boundary Validation

Critical boundary check: bisulfid.com must not be mistaken for a bisulfite site.

- All bisulfite disambiguation content correctly states: "bisulfid.com is a bisulfide reference site, not a bisulfite site"
- /bisulfite/ page explicitly distinguishes HSO₃⁻ from HS⁻ in the first paragraph
- /terminology/ page lists bisulfite under "Oxysulfur Terms" separate from "Core HS⁻ Terms"
- No page claims bisulfid.com is a bisulfite sequencing reference

**Boundary status: CLEAN**

---

## German -id/-ide Suffix Accuracy

- All German -id pages correctly use the -id suffix (not -ide)
- All English compound class pages correctly use the -ide suffix
- Cross-links between German and English forms are correct
- /bisulfid-vs-bisulfide/ link appears in primary navigation on all pages

**Suffix accuracy: CLEAN**

---

## Internal Link Integrity

Selected internal link spot-checks:

| Page | Link checked | Target exists |
|------|-------------|---------------|
| /bisulfide/ | /bisulfid/ | YES |
| /bisulfide/ | /hs-ion/ | YES |
| /sodium-bisulfide/ | /bisulfide/ | YES |
| /sodium-bisulfide/ | /hs-ion/ | YES |
| /disulfide-bonds/ | /pyrite/ | YES |
| /molybdenum-disulfide/ | /disulfide-bonds/ | YES |
| /german-english-chemical-terms/ | /bisulfid/ | YES |
| /missing-e/ | /bisulfid-vs-bisulfide/ | YES |
| /compounds/ | /bisulfide/ | YES |
| /atlas/ | /compounds/ | YES |

No broken internal links detected in spot-check.

---

## Page Count Validation

```
find site/public -path 'site/public/_integration_sample' -prune \
  -o -path 'site/public/_visual_proof_sample' -prune \
  -o -name 'index.html' -print | wc -l
```

**Result: 14,041** — matches deploy workflow gate.

---

## Sitemap Validation

- sitemap.xml contains 60 URL entries
- All 52 Wave 1 pages present in sitemap
- All 8 original core pages retained in sitemap
- No duplicate entries
- All URLs use `https://bisulfid.com/` canonical base

---

## Governance Integrity

- 14K scaffold governance INTACT: noindex, unlinked, planned status preserved
- No modifications to `main/config/navigation.json`
- No modifications to `main/config/build.json`
- No modifications to any `main/content/` files
- CI corpus validators unaffected (all new content under `site/public/`)

---

## Validation Status

**PASSED — Wave 1 ready for deployment.**
