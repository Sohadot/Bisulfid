# Validator Skeleton — scripts/validators/

## Status: Placeholder Only

The validators in this directory are **not yet enforcing** any quality gates.
They exist to reserve Quality Gate boundaries and document future check requirements.

## Purpose

These files were created in Sprint 0D to establish the validator skeleton
aligned with the 11 Quality Gates defined in `doctrine/QUALITY_GATE.md`.

Full enforcement begins in a later build-system sprint when a build system
is introduced and validators are wired into the build pipeline.

## Important

- No deployment should rely on placeholder validators as proof of launch readiness.
- Quality Gate remains doctrine-enforced until validators are fully implemented.
- Each validator currently exits 0 and prints a non-enforcement warning.
- Passing placeholder validators does not mean any Quality Gate has passed.

## Validator Mapping

| File | Future Gate(s) | Description |
|------|----------------|-------------|
| validate_links.py | Gate 01, Gate 08 | Internal link integrity and orphan detection |
| validate_content.py | Gate 02, Gate 09 | Placeholder and content standard checks |
| validate_indexation.py | Gate 03 | Sitemap and navigation indexation checks |
| validate_sources.py | Gate 04 | Source registry and factual claim checks |
| validate_claims.py | Gate 04 + blocked | Claim integrity and blocked pattern checks |
| validate_seo.py | Gate 05 | SEO metadata checks |
| validate_security.py | Gate 06 | Security posture checks |
| validate_accessibility.py | Gate 07 | Accessibility compliance checks |
| validate_routes.py | Route governance | Route registry integrity checks |
| validate_schema.py | Structured data | JSON-LD schema correctness checks |
| validate_hreflang.py | Gate 11 | Hreflang correctness checks |
| validate_translations.py | Gate 11 | Translation integrity checks |
| validate_language_routes.py | Gate 11 | Language route governance checks |
| validate_supply_chain.py | Gate 06 + security | Supply chain and dependency checks |
| validate_all.py | All gates | Orchestrator — runs all validators in gate order |

## Do Not Treat As Launch Proof

Placeholder validators exit 0 by design. Exit 0 at this stage means:
"The skeleton exists and is structurally consistent."

It does not mean: "The Quality Gate has passed."

All 11 Quality Gates remain doctrine-enforced per `doctrine/QUALITY_GATE.md`
until full validator implementations replace these stubs.
