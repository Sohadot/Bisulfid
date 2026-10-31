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
# Explicit editorial classification by institutional function and section, not a
# keyword-only PASS. This audit is not a scientific peer review or Gate 12-I.
SECTION_AUDIT = {
    "INST-HOME-EN": {
        "The question behind our name": ("terminology_boundary", "Matches the lexical/evidence separation established by KO-BISULFID-TERMINOLOGY-001 without asserting chemical synonymy."),
        "Different sources answer different questions": ("source_method", "Distinguishes authoritative dictionary, chemical-database, nomenclature and primary-research uses; no new species claims."),
        "How evidence becomes a reference": ("governed_method", "Matches the source/evidence/claim separation and documentary-review disclosure implemented in Release-01."),
        "Identity, structure and material form": ("scientific_scope", "Describes material-form limits of the MoS2 research object without presenting its draft as an authorized public reference."),
        "English and German reference questions": ("language_scope", "EN/DE pages have reciprocal distinct native-language editorial tasks; no fabricated scientific translation."),
        "Publisher and limits": ("publisher_scope", "Sohadot (sohadot.com) was expressly identified as the project owner and publisher in the owner conversation; no expert signature is represented."),
    },
    "INST-HOME-DE": {
        "Ähnliche Wörter sind keine Stoffdefinition": ("terminology_boundary", "Nennt bewusst keine ungeprüfte chemische Gleichsetzung; entspricht den Grenzen des vorhandenen Terminologie-Objekts."),
        "Wörterbücher, Datenbanken und Regeln unterscheiden": ("source_method", "Unterscheidung von Wörterbuch, Datenbank und Nomenklatur ohne neue Stoffbehauptungen."),
        "Was einen Fachbeleg brauchbar macht": ("governed_method", "Entspricht der Quellen- und Nachweiskette; unterscheidet Dokumentationskontrolle und unabhängige Begutachtung."),
        "Wissenschaftliche Begriffe brauchen Kontext": ("scientific_scope", "Beschreibt Materialform und Unsicherheit, ohne den unveröffentlichten MoS2-Entwurf als freigegeben auszugeben."),
        "Deutschsprachige Fragen eigenständig behandeln": ("language_scope", "Ein eigenständiger deutschsprachiger Zugang, nicht automatisch übersetzte chemische Fakten."),
        "Herausgeber und Grenzen": ("publisher_scope", "Sohadot (sohadot.com) wurde vom Projekteigentümer ausdrücklich als Inhaber benannt; keine erfundene Begutachtung."),
    },
}


def build():
    gov = ri.gov_values()
    items = []
    for name in ("INST-HOME-EN.json", "INST-HOME-DE.json"):
        spec = json.load(open(os.path.join(ri.SPEC_DIR, name), encoding="utf-8"))
        sid = spec["spec_id"]
        sections = SECTION_AUDIT.get(sid, {})
        sources = [*spec.get("nav", []), *(l for section in spec["sections"] for l in section["links"])]
        if any(link["path"] in ("/molybdenum-disulfide/", "/bisulfid-vs-bisulfide/") for link in sources):
            raise ValueError(f"{sid}: unreleased scientific reference must not be advertised as live")
        inputs = [("lead", spec["lead"])] + [(section["heading"], paragraph)
                 for section in spec["sections"] for paragraph in section["paragraphs"]]
        for where, source_text in inputs:
            rendered = ri.resolve(source_text, gov)
            entry = {"spec": sid, "version": spec["version"], "section": where,
                     "text": rendered, "has_governed_value": "{{GOV:" in source_text,
                     "claim_class": "unclassified", "status": "REVIEW"}
            if where == "lead":
                entry.update(claim_class="intro", status="not_a_factual_claim",
                             basis="Institutional mission statement, not a chemical or scientific claim.")
            elif where in sections:
                category, basis = sections[where]
                status = "owner_confirmed" if category == "publisher_scope" else "verified"
                entry.update(claim_class=category, status=status, basis=basis)
                if category == "publisher_scope" and "sohadot.com" not in rendered.lower():
                    raise ValueError(f"{sid}: owner-identity text lost its source")
            items.append(entry)
    result = {"audit_id": "HOMEPAGE-CLAIM-AUDIT-R01",
              "generated_by": "scripts/release/build_homepage_claim_audit.py",
              "method": "Explicit section-level editorial classification with complete paragraph listing, live-link restrictions and owner-identity confirmation. This is not an external peer review and does not certify Google rankings or replace Gate 12-I.",
              "governed_values": gov, "items": items,
              "summary": {"items": len(items),
                          "verified": sum(i["status"] == "verified" for i in items),
                          "owner_confirmation_required": sum(i["status"].startswith("OWNER") for i in items),
                          "owner_confirmed": sum(i["status"] == "owner_confirmed" for i in items),
                          "not_a_factual_claim": sum(i["status"] == "not_a_factual_claim" for i in items),
                          "unclassified": sum(i["status"] == "REVIEW" for i in items)}}
    return result


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
