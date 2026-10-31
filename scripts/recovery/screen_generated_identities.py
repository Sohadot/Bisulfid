#!/usr/bin/env python3
"""screen_generated_identities.py — Recovery-03 E: identity screen for the German element-sulfide family.

The generated German pages /de/terminology/cohort0x/<element>-sulfid/ each name a binary "element sulfide"
that no governed evidence identifies. This screen asks one open, reproducible question per page:
does PubChem resolve the English name "<element> sulfide" to a compound record?

  resolved      -> PubChem has a record under that name (identity is checkable; the PAGE is still unverified)
  not_resolved  -> no record under that name (identity not verifiable by name; NOT proof the compound
                   does not exist, and never published as such)

The mapping German slug -> English element name is written out below and reviewable. No credentials;
PubChem PUG REST only. Output: main/data/recovery/R03_IDENTITY_SCREEN.json.
"""

import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "main", "data", "recovery", "R03_IDENTITY_SCREEN.json")
DISP = os.path.join(ROOT, "main", "data", "recovery", "seo_url_disposition.jsonl")
PUG = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{}/cids/JSON"

# German slug (as served) -> (English element name, atomic number)
ELEMENTS = {
    "actinium": ("actinium", 89), "aluminium": ("aluminum", 13), "americium": ("americium", 95), "antimon": ("antimony", 51),
    "barium": ("barium", 56), "berkelium": ("berkelium", 97), "blei": ("lead", 82), "bohrium": ("bohrium", 107),
    "bor": ("boron", 5), "cadmiun": ("cadmium", 48), "caesium": ("cesium", 55), "cer": ("cerium", 58),
    "chrom": ("chromium", 24), "copernicium": ("copernicium", 112), "curium": ("curium", 96),
    "darmstadtium": ("darmstadtium", 110), "dubnium": ("dubnium", 105), "dysprosium": ("dysprosium", 66),
    "einsteinium": ("einsteinium", 99), "eisen": ("iron", 26), "erbium": ("erbium", 68), "europium": ("europium", 63),
    "fermium": ("fermium", 100), "flerovium": ("flerovium", 114), "gadolinium": ("gadolinium", 64),
    "gallium": ("gallium", 31), "germanium": ("germanium", 32), "gold": ("gold", 79), "hafnium": ("hafnium", 72),
    "hassium": ("hassium", 108), "holmium": ("holmium", 67), "indium": ("indium", 49), "iridium": ("iridium", 77),
    "kalifornium": ("californium", 98), "kalium": ("potassium", 19), "kobalt": ("cobalt", 27), "kupfer": ("copper", 29),
    "lanthan": ("lanthanum", 57), "lawrencium": ("lawrencium", 103), "lithium": ("lithium", 3),
    "livermorium": ("livermorium", 116), "lutetium": ("lutetium", 71), "magnesium": ("magnesium", 12),
    "mangan": ("manganese", 25), "meitnerium": ("meitnerium", 109), "mendelevium": ("mendelevium", 101),
    "molybdaen": ("molybdenum", 42), "moscovium": ("moscovium", 115), "natrium": ("sodium", 11),
    "neodym": ("neodymium", 60), "neptunium": ("neptunium", 93), "nickel": ("nickel", 28), "nihonium": ("nihonium", 113),
    "niob": ("niobium", 41), "nobelium": ("nobelium", 102), "oganesson": ("oganesson", 118), "osmium": ("osmium", 76),
    "palladium": ("palladium", 46), "phosphor": ("phosphorus", 15), "platin": ("platinum", 78),
    "plutonium": ("plutonium", 94), "praseodym": ("praseodymium", 59), "quecksilber": ("mercury", 80),
    "rhenium": ("rhenium", 75), "rhodium": ("rhodium", 45), "roentgenium": ("roentgenium", 111),
    "rubidium": ("rubidium", 37), "ruthenium": ("ruthenium", 44), "rutherfordium": ("rutherfordium", 104),
    "samarium": ("samarium", 62), "scandium": ("scandium", 21), "seaborgium": ("seaborgium", 106),
    "selen": ("selenium", 34), "silber": ("silver", 47), "silicium": ("silicon", 14), "strontium": ("strontium", 38),
    "tantal": ("tantalum", 73), "technetium": ("technetium", 43), "tellur": ("tellurium", 52),
    "tenness": ("tennessine", 117), "terbium": ("terbium", 65), "thallium": ("thallium", 81), "thorium": ("thorium", 90),
    "thulium": ("thulium", 69), "titan": ("titanium", 22), "uran": ("uranium", 92), "vanadium": ("vanadium", 23),
    "wismut": ("bismuth", 83), "wolfram": ("tungsten", 74), "ytterbium": ("ytterbium", 70), "yttrium": ("yttrium", 39),
    "zink": ("zinc", 30), "zinn": ("tin", 50), "zirkonium": ("zirconium", 40),
}


def lookup(name):
    url = PUG.format(urllib.parse.quote(name))
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "bisulfid.com identity screen"}), timeout=60) as r:
            return r.status, json.loads(r.read()).get("IdentifierList", {}).get("CID", [])
    except urllib.error.HTTPError as e:
        return e.code, []


def main():
    rows = [json.loads(line) for line in open(DISP, encoding="utf-8")]
    pages = sorted(r["path"] for r in rows if r["seo_class"] == "generated_unverified_identity"
                   and r["path"].startswith("/de/terminology/") and r["path"].rstrip("/").endswith("-sulfid"))
    out = []
    for p in pages:
        slug = p.rstrip("/").split("/")[-1][: -len("-sulfid")]
        if slug not in ELEMENTS:
            out.append({"path": p, "slug": slug, "screen": "unmapped"})
            continue
        en, z = ELEMENTS[slug]
        status, cids = lookup(f"{en} sulfide")
        out.append({"path": p, "slug": slug, "element_en": en, "atomic_number": z, "query": f"{en} sulfide",
                    "http_status": status, "cids": cids[:5],
                    "screen": "resolved" if cids else ("not_resolved" if status == 404 else f"error_{status}")})
        time.sleep(0.25)  # PubChem asks for <= 5 requests/second
    summary = {}
    for o in out:
        summary[o["screen"]] = summary.get(o["screen"], 0) + 1
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"screen_id": "R03-IDENTITY-SCREEN-DE-ELEMENT-SULFID", "run_on": datetime.date.today().isoformat(),
                   "question": "Does PubChem resolve '<element> sulfide' (English) to a compound record?",
                   "interpretation": "not_resolved means identity is not verifiable by name; it is not evidence that no such compound exists.",
                   "summary": summary, "pages": out}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(summary)
    return 1 if any(k.startswith("error") or k == "unmapped" for k in summary) else 0


if __name__ == "__main__":
    sys.exit(main())
