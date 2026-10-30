#!/usr/bin/env python3
"""simulate_release.py — what the deploy gate would say if the staged release candidates went live.

Builds a hard-linked copy of site/public (scratch directory, never the real one), places every staged
candidate (main/data/release/staged/*/index.html) at its URL, and runs the publication-authority gate in
two scenarios:
  now        the governance stores as they are (no owner or reviewer act exists)
  all_acts   SIMULATED: every human act signed (independent review, source locks, owner claim activation,
             release authorization, R11 certifications). Labelled as a simulation; it proves only that the
             package itself (HTML, directives, Gate 12) is publishable once the real acts exist.
Writes main/data/release/RELEASE_SIMULATION.json. Read-only for site/public.
"""

import glob
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "publication"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "validators"))
import publication_authority as pa  # noqa: E402
import validate_publication_authority as vpa  # noqa: E402
import distinctiveness_core as dc  # noqa: E402

SIM_KO = {"governance": "governed", "evidence": "evidence_locked", "claim": "claim_approved_narrow", "validation": "validated",
          "ig": "ig_reviewed_route_realization", "release": "authorized"}
SIM_R11 = {"governance": "governed", "evidence": "evidence_not_required", "claim": "claim_not_required", "validation": "validated",
           "ig": "ig_not_required", "release": "authorized", "non_factual_class_certified": True}


def main():
    staged = {}
    for m in sorted(glob.glob(os.path.join(ROOT, "main", "data", "release", "staged", "*", "release.json"))):
        man = json.load(open(m, encoding="utf-8"))
        staged[man["page"]] = (os.path.join(os.path.dirname(m), "index.html"), man["kind"])
    tmp = tempfile.mkdtemp(prefix="relsim-")
    surface = os.path.join(tmp, "public")
    try:
        shutil.copytree(os.path.join(ROOT, "site", "public"), surface, copy_function=os.link)
        for page, (src, _) in staged.items():
            dest = os.path.join(surface, page.strip("/"), "index.html") if page != "/" else os.path.join(surface, "index.html")
            os.remove(dest)
            shutil.copyfile(src, dest)
        policy = dc.load_policy()
        pages = dc.load_html_pages(policy, surface)
        import validate_distinctiveness as vd
        inst = dc.InstitutionalRegistry()
        _, verdicts, _ = vd.analyse_universe("surface", pages, policy, dc.IGContext())
        out = {}
        for name, override in (("now", None),
                               ("all_acts", {p: (SIM_KO if k == "knowledge_reference" else SIM_R11, "SIMULATED owner/reviewer acts")
                                             for p, (_, k) in staged.items()})):
            auth = pa.Authority(postures_override=override)
            states = vpa.check_surface(surface, auth, policy, pages=pages, verdicts=verdicts)
            s = vpa.summarize(states)
            out[name] = {"summary": s, "staged_pages": {x["path"]: {"state": x["state"], "gate12": x.get("gate12"),
                                                                  "served_robots": (x.get("served") or {}).get("robots"),
                                                                  "basis": x["basis"]}
                                                       for x in states if x["path"] in staged}}
            print(name, s["counts"], {p: v["state"] for p, v in out[name]["staged_pages"].items()})
        del inst
    finally:
        shutil.rmtree(tmp)
    rec = {"note": "Scenario all_acts SIMULATES signatures that do not exist. It is evidence that the staged HTML would pass the "
                   "deploy gate once the real acts are recorded, not an authorization.", "staged": sorted(staged), **out}
    with open(os.path.join(ROOT, "main", "data", "release", "RELEASE_SIMULATION.json"), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
