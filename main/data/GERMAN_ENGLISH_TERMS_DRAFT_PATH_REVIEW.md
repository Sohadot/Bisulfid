# German-English Terms Draft Path Review

## Why This Sprint Exists

Sprint 4F documented that `main/content/en/pages/german-english-chemical-terms.md` was not found at the expected path. Sprint 4G reviews the route/content alignment state without creating the missing page, modifying routes, publishing routes, approving claims, or removing `[SOURCE REQUIRED]` markers.

## Files Reviewed

- `main/data/routes.json`
- `main/data/internal_links.json`
- `main/data/hreflang_groups.json`
- `main/data/translation_registry.json`
- `main/content/en/pages/`
- `main/content/en/README.md`
- `main/data/ACADEMIC_SOURCE_CLAIM_BOUNDARY_REPORT.md`
- `DECISION_LOG.md`

## Route Existence

The route `german_english_chemical_terms` exists in `main/data/routes.json`.

## Current Route State

- route_id: `german_english_chemical_terms`
- path: `/german-english-chemical-terms/`
- content_file: `main/content/en/pages/german-english-chemical-terms.md`
- status: `planned`
- publication_status: not present as a separate route field
- indexable: `false`
- in_sitemap: `false`
- required_internal_links: `[]`
- required_claim_groups: `["terminology_claims"]`
- risk_level: `low`
- translation_status: `source_planned`
- hreflang_group: `german_english_chemical_terms`
- source_required: `true`

## Expected Content File Path

Expected path:

- `main/content/en/pages/german-english-chemical-terms.md`

## Draft File Existence

The expected draft file does not exist.

No similarly named file was found under:

- `main/content/en/pages/`
- `main/content/en/`
- `main/content/en/fragments/`
- `main/content/en/term-records/`

## Existing English Draft Pages

Existing English route content drafts:

- `home` — `main/content/en/pages/index.md`
- `what_is_bisulfid` — `main/content/en/pages/what-is-bisulfid.md`
- `bisulfid_vs_bisulfide` — `main/content/en/pages/bisulfid-vs-bisulfide.md`
- `sulfid_vs_sulfide` — `main/content/en/pages/sulfid-vs-sulfide.md`
- `sources` — `main/content/en/pages/sources.md`
- `acquire` — `main/content/en/pages/acquire.md`

## Planned English Routes Without Content Drafts

The following planned routes currently point to content files that do not exist:

- `what_is_sulfur` — `main/content/en/pages/what-is-sulfur.md`
- `sulfur_compounds` — `main/content/en/pages/sulfur-compounds.md`
- `sulfur_uses` — `main/content/en/pages/sulfur-uses.md`
- `bisulfide_hydrosulfide_sulfide` — `main/content/en/pages/bisulfide-hydrosulfide-sulfide.md`
- `sodium_bisulfide` — `main/content/en/pages/sodium-bisulfide.md`
- `disulfide_bonds` — `main/content/en/pages/disulfide-bonds.md`
- `industrial_sulfur_systems` — `main/content/en/pages/industrial-sulfur-systems.md`
- `sulfur_safety_context` — `main/content/en/pages/sulfur-safety-context.md`
- `hydrogen_sulfide_risk` — `main/content/en/pages/hydrogen-sulfide-risk.md`
- `sds_and_sulfur_terms` — `main/content/en/pages/sds-and-sulfur-terms.md`
- `protein_disulfide_structure` — `main/content/en/pages/protein-disulfide-structure.md`
- `molybdenum_disulfide` — `main/content/en/pages/molybdenum-disulfide.md`
- `german_english_chemical_terms` — `main/content/en/pages/german-english-chemical-terms.md`
- `glossary` — `main/content/en/pages/glossary.md`
- `newsletter` — `main/content/en/pages/newsletter.md`

The missing `german_english_chemical_terms` draft is not a unique route/content gap. It is one of multiple planned routes awaiting future content drafts.

## Internal Link References

`main/data/internal_links.json` references `german_english_chemical_terms` by route ID, not by raw URL or file path.

Route groups that link to `german_english_chemical_terms`:

- `what_is_bisulfid`
- `bisulfid_vs_bisulfide`
- `sulfid_vs_sulfide`

`german_english_chemical_terms` also has its own planned internal link group with intended links to:

- `what_is_bisulfid`
- `bisulfid_vs_bisulfide`
- `sulfid_vs_sulfide`
- `glossary`
- `sources`

All link groups remain `planned`.

## Hreflang and Translation Registries

`main/data/hreflang_groups.json` remains inactive and contains no active groups.

`main/data/translation_registry.json` remains inactive and contains no translations.

The missing draft does not affect active hreflang or translation state because both registries are inactive and no route is published.

## Impact on Current Publication State

No public route is affected because all routes remain planned, non-indexable, and excluded from the sitemap.

The missing draft blocks future content alignment for `german_english_chemical_terms`, but it does not create a live publication error in the current prelaunch state.

## Why No Route Was Published

No route was published because this sprint is diagnostic only. The route remains `status: planned`, `indexable: false`, and `in_sitemap: false`.

## Why No Content Page Was Created

The missing draft was not created because Sprint 4G is a path and alignment review sprint only. Creating the draft should happen in a future content-alignment sprint with its own source-marker and claim-boundary rules.

## Why No Content Page Was Modified

No content page was modified because the task was to review route/content alignment only. Existing draft wording and metadata remain untouched.

## Why No `[SOURCE REQUIRED]` Marker Was Removed

No `[SOURCE REQUIRED]` marker was removed because no claim was approved, no source-locking occurred, and no content page was edited.

## Classification

A. Missing draft file: yes.

B. Incorrect route `content_file` path: no evidence. The route points to the expected governed pages directory and expected slug.

C. Inactive planned route awaiting future content: yes.

D. Broader route/content inventory issue: yes. `german_english_chemical_terms` is one of multiple planned routes whose content file does not yet exist.

## Recommended Next Sprint

Sprint 4H should be a content-alignment planning sprint or a narrow draft-creation sprint.

Recommended constraints:

- Create only the missing `german-english-chemical-terms.md` draft if explicitly authorized.
- Keep `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`, and `generated: false`.
- Keep all relevant `[SOURCE REQUIRED]` markers.
- Do not publish routes.
- Do not approve claims.
- Do not modify `routes.json` unless a separate route-alignment issue is identified and explicitly authorized.
