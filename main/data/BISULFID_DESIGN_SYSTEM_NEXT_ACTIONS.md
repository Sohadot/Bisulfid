# Bisulfid Design System Next Actions — Post Sprint 6N-A

## Is the foundation ready for template integration?

**Yes, for a dedicated integration sprint** — after PR merge and design review. Foundation tokens, components, SVGs, and motion governor exist. No live public HTML changes yet.

## Criteria for integrating tokens into base.html

- [ ] Sprint 6N-B (or equivalent) authorized for template integration only
- [ ] Link token CSS files in hardened publication frame `<head>` — local paths only
- [ ] All existing governance banners and meta tags preserved
- [ ] Validator suite PASS after integration on sample routes
- [ ] No CDN, no npm, no external stylesheets

## Criteria for integrating components into reference/term frames

- [ ] Map existing governance banner to `.bs-governance-banner` classes without removing text
- [ ] Source bar maps to `.bs-source-crystal--required` when `[SOURCE REQUIRED]` present
- [ ] Term body maps to `.bs-term-card` structure
- [ ] Pilot on ≤10 routes before 14,000-page re-render
- [ ] Re-run public foundation validator after any public HTML change

## Criteria for designer-authored SVG replacements

- [ ] SVG remains local, lightweight, original
- [ ] No external references or embedded scripts
- [ ] Accessibility labels preserved
- [ ] Validator PASS

## Criteria for future WebGL prototype

- [ ] Static system integrated and live-verified
- [ ] Separate sprint authorization
- [ ] Module under `engine/webgl/` with dedicated validator
- [ ] Progressive enhancement only — static fallback required
- [ ] Never overrides source-required visibility

## Criteria for future AR prototype

- [ ] WebGL prototype validated first
- [ ] WebXR boundary sprint with governance review
- [ ] No public integration without indexation/gate review

## Why integration must not break 14,000 public output

Any template change affecting public HTML requires controlled re-render, full validator pass, and deployment verification. Integration is incremental — not mass unvalidated restyle.

## Recommended next sprint

**Sprint 6N-B (proposed):** Template integration pilot — link tokens + governance banner + source crystal into publication frames on a governed sample (8–50 routes), validate, then plan staged 14,000 re-render authorization.

## Operational note

Deployment workflow (6M-H) remains unchanged. Run live deployment verification separately from design-system integration.
