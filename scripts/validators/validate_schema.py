#!/usr/bin/env python3
"""validate_schema.py — Future structured-data (JSON-LD) enforcement.

Currently a placeholder. Full enforcement is not active.

Future checks (when build system is active):
- Every published page with structured data has valid, parseable JSON-LD
- Schema @type matches expected page type per routes.json route_type field
- Homepage is not incorrectly marked as ChemicalSubstance
- Term pages use appropriate schema (e.g., DefinedTerm where applicable)
- No schema references unapproved external vocabulary
- @context is present and uses a recognized vocabulary
- Required properties present per @type (name, url for WebPage at minimum)
"""

import json

# TODO: When build system generates HTML, scan for <script type="application/ld+json"> blocks
# TODO: Extract JSON-LD content and parse with json module (stdlib)
# TODO: Report parse errors with file path and character offset
# TODO: Check @type matches expected type per route type from routes.json
# TODO: Verify homepage uses WebSite or WebPage, not ChemicalSubstance
# TODO: Verify term records use appropriate schema type per ontology classification
# TODO: Validate required properties per @type (name and url for WebPage at minimum)
# TODO: Flag any @context URLs that are not in the approved vocabulary list


def main():
    print("PLACEHOLDER: validate_schema is not yet enforcing full validation.")
    print("  Future: Structured data (JSON-LD) schema correctness enforcement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
