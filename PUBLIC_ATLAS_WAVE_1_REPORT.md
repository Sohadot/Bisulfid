# Public Atlas Wave 1 Report — Sprint 97A

## Summary

Sprint 97A delivered the first wave of real, indexable public atlas pages for bisulfid.com.

**Pages delivered:** 52 real public pages (38 new + 14 scaffold overwrites)
**Total public page count:** 14,041 (was 14,002)
**Sitemap entries:** 60 (was 8)
**Deploy workflow gate:** updated to 14,041

---

## Pages Written

### Hub Pages (5 new)

| Path | Title |
|------|-------|
| /atlas/ | Atlas — Full Reference Overview |
| /terms/ | Terms — Terminology Index |
| /compounds/ | Compound Classes |
| /materials/ | Materials — Sulfide Minerals and Compounds |
| /methodology/ | Methodology — Atlas Source Discipline |

### Key Concept Pages (5 new)

| Path | Title |
|------|-------|
| /missing-e/ | The Missing E — German -id vs English -ide |
| /hs-ion/ | HS⁻ Ion — The Bisulfide/Hydrosulfide Anion |
| /sulfur-element/ | Sulfur — Element Reference |
| /german-chemical-suffix/ | German Chemical Suffix — The -id Pattern |
| /sulfide-ion/ | Sulfide Ion — S²⁻ Reference |

### German -id Form Pages (9 new)

| Path | Title |
|------|-------|
| /oxid/ | Oxid — German Form of Oxide |
| /hydroxid/ | Hydroxid — German Form of Hydroxide |
| /chlorid/ | Chlorid — German Form of Chloride |
| /fluorid/ | Fluorid — German Form of Fluoride |
| /bromid/ | Bromid — German Form of Bromide |
| /iodid/ | Iodid — German Form of Iodide |
| /nitrid/ | Nitrid — German Form of Nitride |
| /carbid/ | Carbid — German Form of Carbide |
| /phosphid/ | Phosphid — German Form of Phosphide |

### English Compound Class Pages (7 new)

| Path | Title |
|------|-------|
| /bisulfide/ | Bisulfide — HS⁻ Compound Class |
| /sulfide/ | Sulfide — S²⁻ Compound Class |
| /disulfide/ | Disulfide — S–S Bond Compound Class |
| /polysulfide/ | Polysulfide — Chain Sulfur Compounds |
| /bisulfite/ | Bisulfite — HSO₃⁻ Compound Class |
| /sulfite/ | Sulfite — SO₃²⁻ Compound Class |
| /thiosulfate/ | Thiosulfate — S₂O₃²⁻ Compound Class |

### Additional Compound and Mineral Pages (12 new)

| Path | Title |
|------|-------|
| /disulfid/ | Disulfid — German Form of Disulfide |
| /sulfat/ | Sulfat — German Form of Sulfate |
| /hydrogen-sulfide/ | Hydrogen Sulfide — H₂S Reference |
| /sodium-sulfide/ | Sodium Sulfide — Na₂S Reference |
| /iron-sulfide/ | Iron Sulfide — FeS and FeS₂ |
| /zinc-sulfide/ | Zinc Sulfide — ZnS Reference |
| /pyrite/ | Pyrite — FeS₂ Mineral |
| /sphalerite/ | Sphalerite — ZnS Mineral |
| /galena/ | Galena — PbS Mineral |
| /polysulfid/ | Polysulfid — German Form of Polysulfide |
| /thiol/ | Thiol — R–SH Compounds |
| /sulfuric-acid/ | Sulfuric Acid — H₂SO₄ Reference |

### Scaffold Overwrites — Real Content Replacing Governance Boilerplate (14)

| Path | Status |
|------|--------|
| /bisulfid/ | Overwritten |
| /sulfid/ | Overwritten |
| /hydrosulfide/ | Overwritten |
| /what-is-sulfur/ | Overwritten |
| /sulfur-compounds/ | Overwritten |
| /sulfur-uses/ | Overwritten |
| /sulfid-vs-sulfide/ | Overwritten |
| /german-english-chemical-terms/ | Overwritten |
| /bisulfide-hydrosulfide-sulfide/ | Overwritten |
| /disulfide-bonds/ | Overwritten |
| /molybdenum-disulfide/ | Overwritten |
| /sodium-bisulfide/ | Overwritten |
| /terminology/ | Created (did not previously exist) |
| /industrial-sulfur-systems/ | Overwritten |

---

## Quality Criteria — All Pages

All 52 pages satisfy:

- [x] `<meta name="robots" content="index, follow">` — no noindex
- [x] Canonical URL present and correct
- [x] Title tag: unique, descriptive, ends with `| bisulfid.com`
- [x] Meta description: unique, descriptive, under 160 characters
- [x] H1 present and matches page topic
- [x] ≥4 internal links per page
- [x] Breadcrumb navigation with structured markup
- [x] Source posture section on every page
- [x] No draft language, no `[SOURCE REQUIRED]` markers
- [x] No medical, safety, procurement, or industrial performance claims
- [x] No false claims about bisulfid.com being a bisulfite site
- [x] Design system classes: `bisulfid-frame`, `bs-control-room`, `public-page`
- [x] `data-route-status="published"`

---

## Governance Integrity

- 14K scaffold remains intact (noindex, unlinked, planned status)
- No modifications to `main/config/navigation.json`, `main/config/build.json`, or `main/content/`
- CI validators (`validate_corpus_publication_lock_l1.py`, `validate_corpus_drafts_l1.py`) unaffected
- All new content under `site/public/` only

---

## Count Arithmetic

| Category | Count |
|----------|-------|
| Previous public page count | 14,002 |
| New directories (new pages) | 39 |
| Scaffold overwrites (count unchanged) | 13 |
| New public page count | **14,041** |
| Deploy workflow gate | **14,041** |
| Sitemap entries | **60** |

*Note: terminology/ was a net-new directory (no prior scaffold existed), contributing +1 beyond the initial plan estimate of 38 new directories.*
