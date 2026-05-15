#!/usr/bin/env python3
"""validate_sources.py — Future Gate 04 source registry enforcement.

Currently a placeholder. Full enforcement is not active.

Future checks (when build system is active):
- Every factual claim in published content has a verified entry in source_registry.json
- No source entry has a fake or unverified URL
- No AI-generated text or AI summary is recorded as a source
- No market statistics appear in published claims without a source lock
- Source IDs referenced in claims exist in source_registry.json
- No source with a blocked category is used for any claim
"""

# TODO: Load main/data/sources/source_registry.json
# TODO: Load all claim registries from main/data/claims/
# TODO: For each active claim, verify source_ids is non-empty
# TODO: For each source_id in a claim, verify it exists in source_registry.json
# TODO: Verify no source has a category listed in blocked_source_uses
# TODO: Verify no source has source_type: AI_generated or AI_summary
# TODO: Check that market_claims.json active claims all have verified source entries
# TODO: Verify source_registry.json status is active before any sources are used


def main():
    print("PLACEHOLDER: validate_sources is not yet enforcing full validation.")
    print("  Future: Gate 04 (zero unsourced claims) enforcement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
