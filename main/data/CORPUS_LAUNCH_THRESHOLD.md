# Corpus Launch Threshold — First Public Launch and No-Go Conditions

## Minimum page count threshold

- **Minimum public launch cohort:** **300 governed reference pages**, each passing all gates below.
- **300 is the floor, not the ceiling:** The long-term sovereign corpus is intended to grow **well beyond** 300 pages (500 / 1,000 / 3,000+ horizons) **only if** quality and governance remain non-negotiable.

## Page quality gates (every public page)

1. **Substance:** Not thin; meets category minimum structure defined in blueprint + expansion model.
2. **Corpus role:** Explicit, singular primary role (terminology record, disambiguation, methodology, hub, etc.).
3. **Non-generic:** No placeholder “visibility” copy; no weak SEO gate pages.
4. **Markers:** **No unresolved `[SOURCE REQUIRED]` markers** in publicly renderable output.
5. **Internal links:** No broken required internal links; clusters documented and satisfied.
6. **Metadata:** Valid `route_id`, language, template alignment, and governance metadata before `status: published`.

## Source gates

- Every on-page factual claim supported per `doctrine/SOURCE_POLICY.md`.
- No reliance on `academic_teaching_reference` alone for formal/normative public claims.
- Source registry entries **verified** (not merely seeded) for claims used in public copy.

## Claim gates

- Relevant claim registries **active** only under explicit program control (currently **inactive**).
- **No** `status: approved` without full source lock and review trail.
- Page’s `required_claim_groups` fully satisfied before publication.

## Route gates

- Route records complete in `routes.json` (future sprint).
- **Not published** until Quality Gate passes.
- **Never** `indexable: true` or `in_sitemap: true` until explicitly authorized and linked to sitemap policy.

## Internal link gates

- `internal_links.json` (or successor) consistent with public graph.
- No `route_id` targets public without meeting this document’s thresholds.

## Multilingual gates

- Non-English public pages are **controlled terminology records**, not bulk translations.
- Each language page has source posture applicable to **that language’s** authorities (where used).
- hreflang groups coherent; no mixed-language public body without explicit design.

## Sitemap / indexation gates

- Sitemap inclusion **only** for routes explicitly cleared and policy-aligned.
- Default for pre-launch corpus: **planned**, **non-indexable**—unchanged until launch program.

## No-publication conditions (hard stops)

Publication is **forbidden** while **any** of the following holds:

1. Fewer than **300** pages meet **all** launch gates.
2. Any public page retains `[SOURCE REQUIRED]` without resolution.
3. Any scientific/industrial/safety/terminology claim on a public page lacks approved, sourced registry support where required.
4. Claim registries intentionally **inactive** and not overridden by a governed activation process.
5. Broken internal link graph for required edges.
6. Generic or thin page inventory detected above acceptable audit threshold.
7. Owner doctrine breach: weak visibility, placeholder launch, or “small public gate” contrary to sovereign reference thesis.

## Final launch conditions (all must be true)

1. **≥ 300** governed pages certified against this threshold.
2. Owner acknowledgement of **authority-first** launch (not traffic-first).
3. Quality Gate workflow executed per `doctrine/QUALITY_GATE.md`.
4. Safety-adjacent pages reviewed for **non-manual** compliance.
5. Multilingual cohort (if any is public at launch) passes multilingual gates above.
6. Monitoring plan for post-launch regression (link rot, marker drift, claim stalemate).

## Long-term posture

After first launch, **additional pages** may be added toward 500 / 1,000 / 3,000+ **only** under:

- `CORPUS_EXPANSION_MODEL.md` rules,
- strict batch audits,
- pruning of weak concepts,

so the corpus remains **large, trusted, academically disciplined, and sovereign-grade**—not a **300-page stunt** and not an **unbounded thin site**.

## Sprint 5A note

This threshold document was created in **Sprint 5A** (architecture only). **No** routes, claims, or content were published or modified in this sprint.
