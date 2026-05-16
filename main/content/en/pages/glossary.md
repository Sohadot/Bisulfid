---
route_id: glossary
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
language: en
locale: en
source_language: en
---

# Sulfur Terminology Glossary

**Draft notice:** This page is a **non-public draft** for internal reference infrastructure only. It is **not** published, **not** indexable, **not** in the sitemap, **not** approved for public use or citation, and **not publication-ready**. All definitions and scope statements below are **draft review** material: **candidate support** only until **source-locking required** work completes. This page does **not** establish formal source-locking for any claim.

---

## 1. What this glossary is (and is not)

This file is the **controlled terminology chamber** for bisulfid.com: a draft scaffold for how governed term entries will eventually read when the asset is ready for public glossary behavior.

It is **not** a textbook, a general encyclopedia of chemistry, or a substitute for primary nomenclature references. It does **not** exhaust sulfur chemistry. It exists so future sprints can align English prose with registry-backed terms **without** pretending that prose alone equals verified ontology state.

The production glossary is expected to be **driven by** `sulfur_terms.json` and source discipline [SOURCE REQUIRED]. This draft does **not** modify that ontology file and does **not** mark any term as verified.

---

## 2. Operating rules for this chamber

- Every future public-facing definition requires registry and claim workflow alignment [SOURCE REQUIRED].
- Entries here may use **illustrative** headings only. Nothing below is offered as final public definition language.
- **`[SOURCE REQUIRED]`** stays on any factual line that is not yet approved through governed review.
- This draft does **not** remove or satisfy **`[SOURCE REQUIRED]`** markers on other pages.

---

## 3. Illustrative scope map (non-exhaustive)

The glossary is expected to host **controlled** relationships among terminology routes and compound classes. **Candidate** clusters under review (labels only - not verified scope boundaries) [SOURCE REQUIRED]:

- Core identity and DE/EN boundary terms aligned with `what_is_bisulfid`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `german_english_chemical_terms`.
- Sulfur compound class vocabulary that connects the public gateway layer to the terminology system [SOURCE REQUIRED].
- Disambiguation vocabulary for **bisulfide**, **hydrosulfide**, and **sulfide** naming (see `bisulfide_hydrosulfide_sulfide`) [SOURCE REQUIRED].

Exact inclusion rules for each cluster await ontology and source work [SOURCE REQUIRED].

---

## 4. Entry format (draft template)

When terms graduate toward public readiness, each entry should carry:

- Preferred label (English layer)
- Relationship hints to other controlled terms (internal concept graph - not live links)
- Governance status (always **draft** here)
- Explicit **`[SOURCE REQUIRED]`** until source-locked

**Example slot (not a verified definition):**

| Term (draft label) | Role in asset | Notes |
| --- | --- | --- |
| Bisulfide (EN) | Boundary term vs German **Bisulfid** | Relationship language requires DE/EN source stack [SOURCE REQUIRED] |
| Sulfide (EN) | Class term; parallel German **Sulfid** | Scope and exceptions not catalogued in this sprint [SOURCE REQUIRED] |
| Hydrosulfide (EN) | Disambiguation target | Precise ion naming vs operational labels [SOURCE REQUIRED] |

---

## 5. Relationship to other planned routes

Plain **`route_id`** references (routes remain **planned**; not public links):

- `what_is_bisulfid` - center term
- `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `german_english_chemical_terms` - boundary vocabulary
- `sulfur_compounds` - scope map companion
- `bisulfide_hydrosulfide_sulfide` - disambiguation companion
- `sources` - source registry governance

---

## 6. Publication blockers

This glossary route stays **not publication-ready** until:

- `sulfur_terms.json` alignment and terminology claims are handled under active registry rules [SOURCE REQUIRED]
- The `glossary` route passes Quality Gate (still **planned** in `routes.json`; this file does not change route JSON)
- Markers are cleared only through governed review

---

*This page is a draft. It is non-public. It may not be cited, indexed, or treated as published content until its route passes the Quality Gate.*
