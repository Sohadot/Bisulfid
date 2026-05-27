# Corpus Launch Threshold — First Public Launch and No-Go Conditions

## Minimum page count threshold

- **Minimum public launch cohort:** **500 governed reference pages**, each passing all gates below.
- **500 is the floor, not the ceiling:** The long-term sovereign corpus is intended to grow **well beyond** 500 pages (1,000+ authority corpus, 3,000+ multilingual system, optional 5,000+ only if governance remains strong) **only if** quality and governance remain non-negotiable.
- **300 pages is no longer the launch threshold** (Sprint 5H strategic correction). Prior 300-page framing was a minimum that the owner has judged **insufficient** for a sovereign-grade first public surface.

## Page quality gates (every public page)

1. **Substance:** Not thin; meets category minimum structure defined in blueprint + expansion model.
2. **Corpus role:** Explicit, singular primary role (terminology record, disambiguation, methodology, hub, etc.).
3. **Non-generic:** No placeholder “visibility” copy; no weak SEO gate pages; **no generic AI glossary pages**.
4. **Markers:** **No unresolved `[SOURCE REQUIRED]` markers** in publicly renderable output.
5. **Internal links:** **No broken links**; required internal links satisfied; clusters documented.
6. **Metadata:** Valid **`route_id`**, language, template alignment, SEO metadata, and governance metadata before `status: published`.
7. **Claims:** **No unapproved scientific, terminology, industrial, or safety claims** on public pages where registries require approval.

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
- **Strong internal-linking cluster** at launch: hubs, spines, disambiguation nodes wired without dead targets.
- No `route_id` targets public without meeting this document’s thresholds.

## Multilingual gates

- Non-English public pages are **controlled terminology records**, not bulk translations.
- Each language page has source posture applicable to **that language’s** authorities (where used).
- hreflang groups coherent; no mixed-language public body without explicit design.

## Sitemap / indexation gates

- **Sitemap/indexation readiness:** inclusion **only** for routes explicitly cleared and policy-aligned.
- Default for pre-launch corpus: **planned**, **non-indexable**—unchanged until launch program.

## SEO metadata gates

- Title, description, H1, and hreflang metadata validated per route before publication.
- No SEO-first thin pages; metadata must reflect real corpus role.

## Technical / security gates

- **Technical/security validation** passes before any generated public output ships.
- **No generated public output** until all gates in this document pass for the full launch cohort.
- No broken build, no security regression, no unauthorized indexation toggles.

## Content drift gates

- **No safety/medical/procurement/market drift** unless separately governed under SOURCE_POLICY and dedicated review programs.
- Industrial/economic pages remain **document-language** only at launch unless explicitly cleared.

## No-publication conditions (hard stops)

Publication is **forbidden** while **any** of the following holds:

1. Fewer than **500** pages meet **all** launch gates.
2. Any public page retains `[SOURCE REQUIRED]` without resolution.
3. Any scientific/industrial/safety/terminology claim on a public page lacks approved, sourced registry support where required.
4. Claim registries intentionally **inactive** and not overridden by a governed activation process.
5. Broken internal link graph for required edges.
6. Generic, thin, or placeholder page inventory detected above acceptable audit threshold.
7. Owner doctrine breach: weak visibility, placeholder launch, or “small public gate” contrary to sovereign reference thesis.
8. SEO or technical/security validation failures.

## Final launch conditions (all must be true)

1. **≥ 500** governed pages certified against this threshold.
2. **Every public page** has: `route_id`, valid metadata, defined corpus role, resolved public markers (where applicable), approved claims (where required), working internal links, non-thin substance.
3. Owner acknowledgement of **authority-first** launch (not traffic-first).
4. Quality Gate workflow executed per `doctrine/QUALITY_GATE.md`.
5. Safety-adjacent pages reviewed for **non-manual** compliance.
6. Multilingual cohort (if any is public at launch) passes multilingual gates above.
7. Sitemap/indexation policy aligned; SEO metadata validated.
8. Technical/security validation complete.
9. Monitoring plan for post-launch regression (link rot, marker drift, claim stalemate).
10. **Launch only after 500-page threshold** — no partial public surfaces below the minimum cohort.

## Long-term posture

After first launch, **additional pages** may be added toward 1,000 / 3,000 / 5,000+ **only** under:

- `CORPUS_EXPANSION_MODEL.md` rules,
- `CORPUS_PRODUCTION_WAVE_MODEL.md` wave discipline,
- strict batch audits,
- pruning of weak concepts,

so the corpus remains **large, trusted, academically disciplined, and sovereign-grade**—not a **500-page stunt** and not an **unbounded thin site**.

## Sprint notes

- **Sprint 5A:** Initial threshold document (300-page minimum; superseded by Sprint 5H).
- **Sprint 5H:** Threshold upgraded to **500 governed pages**. Architecture-only; **no** routes, claims, or content published or modified.
