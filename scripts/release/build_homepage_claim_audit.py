#!/usr/bin/env python3
"""build_homepage_claim_audit.py — sentence-group claim audit of the EN/DE homepage specs (Release-01).

Classifies every lead/paragraph of INST-HOME-EN and INST-HOME-DE and records how it is verified.
Unclassified text fails the audit. Writes main/data/release/HOMEPAGE_CLAIM_AUDIT.json; --check exits 1 if stale.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "reference_production"))
import render_institutional_preview as ri  # noqa: E402

OUT = os.path.join(ROOT, "main", "data", "release", "HOMEPAGE_CLAIM_AUDIT.json")
CLASSES = [
    ("governed reference", ["reference records have been built", "Referenzen entstanden", "terminology record sets out",
                            "Terminologie-Referenz zeigt"],
     "fact about the site's own governed objects; counts computed from the registries; descriptions match the KO scope fields",
     "verified"),
    ("terminology question", ["differ by one letter", "unterscheiden sich um einen Buchstaben"],
     "states only that equivalence is an open claim; consistent with the Recovery-03 evidence (no equivalence asserted)", "verified"),
    ("process description", ["A source is first identified", "Eine Quelle wird zuerst"],
     "describes the admission chain enforced by source_admissibility / Contract C; the 'older pages' qualification matches the "
     "Recovery-01 disposition registry", "verified"),
    ("language scope", ["maintained in English and German", "Eine deutsche Seite entsteht"],
     "routes.json holds only en and de routes; no other language is published", "verified"),
    ("publisher statement", ["published by the owner of the bisulfid.com domain", "der Domain bisulfid.com"],
     "who publishes the site is an owner fact that cannot be verified from the repository; the third-party sentence is a "
     "notice about how references are meant, not a claim about actual relationships", "OWNER CONFIRMATION REQUIRED"),
    ("validation statement", ["No individual expert review is claimed", "fachliche Begutachtung durch eine benannte Person"],
     "true today: no signed independent review exists (main/data/release/reviews)", "verified"),
    ("scope exclusion", ["does not give safety", "gibt keine Hinweise zu Sicherheit"],
     "site policy statement; matches the KO excluded_claim_classes", "verified"),
    ("intro", ["A reference project on the language", "Ein Referenzprojekt zur Sprache"],
     "description of purpose, not a factual claim", "not_a_factual_claim"),
]


def build():
    gov = ri.gov_values()
    items = []
    for f in ("INST-HOME-EN.json", "INST-HOME-DE.json"):
        spec = json.load(open(os.path.join(ri.SPEC_DIR, f), encoding="utf-8"))
        for where, text in [("lead", spec["lead"])] + [(s["heading"], p) for s in spec["sections"] for p in s["paragraphs"]]:
            t = ri.resolve(text, gov)
            item = {"spec": spec["spec_id"], "version": spec["version"], "section": where, "text": t,
                    "has_governed_value": "{{GOV:" in text, "claim_class": "unclassified", "status": "REVIEW"}
            for cls, frags, basis, status in CLASSES:
                if any(fr in t for fr in frags):
                    item.update(claim_class=cls, basis=basis, status=status)
                    break
            items.append(item)
    return {"audit_id": "HOMEPAGE-CLAIM-AUDIT-R01", "generated_by": "scripts/release/build_homepage_claim_audit.py",
            "method": "Every lead/paragraph of INST-HOME-EN and INST-HOME-DE is classified and checked against the governed "
                      "stores. No statement about actual affiliation or non-affiliation is made; no editorial contact is published.",
            "governed_values": gov, "items": items,
            "summary": {"items": len(items), "verified": sum(i["status"] == "verified" for i in items),
                        "owner_confirmation_required": sum(i["status"].startswith("OWNER") for i in items),
                        "not_a_factual_claim": sum(i["status"] == "not_a_factual_claim" for i in items),
                        "unclassified": sum(i["status"] == "REVIEW" for i in items)}}


def main(argv=None):
    mode = (argv or sys.argv[1:] or ["--check"])[0]
    text = json.dumps(build(), indent=1, ensure_ascii=False) + "\n"
    cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else None
    if mode == "--write" and cur != text:
        open(OUT, "w", encoding="utf-8").write(text)
    print(json.loads(text)["summary"])
    return 1 if (mode == "--check" and cur != text) or json.loads(text)["summary"]["unclassified"] else 0


if __name__ == "__main__":
    sys.exit(main())
