"""publication_authority.py — the single source of a URL's publication directives.

Every robots meta value, sitemap entry and rel=canonical that BISULFID serves is RESOLVED here from
governance state; templates and renderers never choose them (Recovery-02).

Precedence (first match wins):
  1. Contract C, for a URL bound to a governed object with recorded postures
     (Knowledge Object via a render spec + publication candidate, or a non-factual R11 certification):
        (public_indexable, index_approved)  -> "index, follow", sitemap, self-canonical
        (public_indexable|public_noindex, noindex) -> "noindex, follow", no sitemap, self-canonical
        (not_public, noindex)               -> falls through: a legacy page may still hold the URL
  2. Legacy status quo (the sealed baseline of what was publicly served before Gate 12): the page may
     keep AT MOST the directives it was served with. Release-ledger blocks and approved per-URL
     decisions can only DOWNGRADE them (index -> noindex, sitemap -> out, self -> canonical target,
     page -> redirect/retire). Nothing here can escalate a directive.
  3. Anything else is not authorized to exist as a page.

Gate 12 and Gate 12-I are NOT inputs to the directive: passing them never makes a page indexable.
They are vetoes, enforced by validate_publication_authority.py on the served surface.
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
SITE = "https://bisulfid.com"
sys.path.insert(0, os.path.join(ROOT, "scripts", "governance_scaffolding"))
import contract_c_derive  # noqa: E402
import route_realization  # noqa: E402
sys.path.insert(0, os.path.join(ROOT, "scripts", "release"))
import release_checks  # noqa: E402

INDEX, NOINDEX = "index, follow", "noindex, follow"
BASELINE_PATH = os.path.join(DATA, "distinctiveness", "legacy_surface_hold.json")
DECISIONS_PATH = os.path.join(DATA, "publication", "url_decisions.json")
CERTIFICATIONS_PATH = os.path.join(DATA, "publication", "nonfactual_certifications.json")
DECISION_TYPES = ("noindex", "canonical_to", "redirect_to", "retire")


def _load(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def decision_is_approved(d):
    """An owner decision counts only if it is explicitly approved: status 'approved', a known decision
    type, and a named approver and date (Release-01). 'proposed' or half-filled records bind nothing."""
    return (d.get("status") == "approved" and d.get("decision") in DECISION_TYPES
            and bool(d.get("approved_by")) and bool(d.get("approved_on")))


def requests_index(robots):
    r = (robots or "").lower()
    return "index" in r and "noindex" not in r


class Authority:
    def __init__(self, baseline_path=BASELINE_PATH, decisions_path=DECISIONS_PATH,
                 certifications_path=CERTIFICATIONS_PATH, postures_override=None):
        routes = _load(os.path.join(DATA, "routes.json"))
        routes = routes if isinstance(routes, list) else routes["routes"]
        self.route_by_path = {r["path"]: r for r in routes}
        self.ledger = {x["route_id"]: x for x in _load(os.path.join(DATA, "release_ledger.json"))["records"]}
        base = _load(baseline_path, {"entries": []})
        self.baseline = {e["p"]: e for e in base["entries"]}
        self.decisions = {d["path"]: d for d in (_load(decisions_path, {"decisions": []})["decisions"])
                          if decision_is_approved(d)}
        self.postures = dict(self._governed_postures(certifications_path))
        if postures_override:
            self.postures.update(postures_override)

    # --- governed state ------------------------------------------------------------------------
    def _governed_postures(self, certifications_path):
        """{path: (contract_c_inputs, basis)} for URLs bound to governed objects."""
        out = {}
        pcs = {}
        for f in glob.glob(os.path.join(DATA, "publication_candidates", "*.json")):
            pc = _load(f)
            pcs[pc.get("knowledge_object_id")] = pc
        route_by_id = {r["route_id"]: r for r in self.route_by_path.values()}
        for f in glob.glob(os.path.join(DATA, "reference_production", "render_specs", "*.json")):
            spec = _load(f)
            route = route_by_id.get(spec.get("canonical_route_id"))
            pc = pcs.get(spec.get("knowledge_object_id"))
            if route and pc:
                ps, held = release_checks.honoured_postures(spec["knowledge_object_id"], pc["postures"],
                                                           skip=("information_gain_posture",))
                ig = ps["information_gain_posture"]
                basis = f"{pc['publication_candidate_id']} via {spec['spec_id']}" + (f" [{'; '.join(held)}]" if held else "")
                if ig == route_realization.POSTURE:
                    ok, why = route_realization.check(spec["knowledge_object_id"], self._rr_stores())
                    if not ok:  # fail closed: an unverified realization is no IG pass
                        ig = "ig_reviewed_no_new_route"
                        basis += f" [route realization refused: {'; '.join(why)}]"
                out[route["path"]] = ({"governance": ps["governance_posture"], "evidence": ps["evidence_posture"],
                                       "claim": ps["claim_posture"], "validation": ps["validation_posture"],
                                       "ig": ig, "release": ps["release_authorization"]}, basis)
        for c in (_load(certifications_path, {"certifications": []})["certifications"]):
            if c.get("status") == "certified" and c.get("certified_on") \
                    and not release_checks._is_agent(c.get("certified_by"), release_checks.policy()):
                out[c["path"]] = ({"governance": c["governance"], "evidence": "evidence_not_required",
                                   "claim": "claim_not_required", "validation": c["validation"],
                                   "ig": "ig_not_required", "release": c["release"],
                                   "non_factual_class_certified": True}, f"R11 certification {c['certification_id']}")
        return out

    def _rr_stores(self):
        if not hasattr(self, "_rr"):
            self._rr = route_realization.Stores()
        return self._rr

    def contract_c(self, path):
        if path not in self.postures:
            return None, None
        inputs, basis = self.postures[path]
        return contract_c_derive.derive(**inputs), basis

    # --- resolution ----------------------------------------------------------------------------
    def resolve(self, path, sitemap_policy="status_quo"):
        """Directive for one URL path. sitemap_policy: 'status_quo' (a legacy page may keep the sitemap
        membership it was served with) or 'approved_only' (only Contract-C index_approved URLs)."""
        out = {"path": path, "render": True, "robots": NOINDEX, "canonical": path, "sitemap": False,
               "redirect_to": None, "basis": None, "notes": [], "ledger_enforced": False, "decision": None}
        cc, cc_basis = self.contract_c(path)
        if cc and cc[0] != "not_public":
            out["basis"] = f"contract_c:{cc[0]}/{cc[1]} ({cc_basis})"
            if cc == ("public_indexable", "index_approved"):
                out.update(robots=INDEX, sitemap=True)
            return out
        if cc:
            out["notes"].append(f"governed object not yet public ({cc_basis}); the legacy page holds the URL")
        base = self.baseline.get(path)
        if not base:
            out.update(render=False, basis="not_authorized",
                       notes=out["notes"] + ["no Contract-C approval and no legacy status quo: the page may not exist"])
            return out
        out["basis"] = "legacy_status_quo"
        out["canonical"] = base.get("c") or path          # the canonical it was served with
        robots = base.get("robots") or NOINDEX
        sitemap = bool(base.get("sm")) and sitemap_policy == "status_quo"
        route = self.route_by_path.get(path)
        lg = self.ledger.get(route["route_id"]) if route else None
        if lg and lg.get("release_status") != "released" and requests_index(robots):
            robots = NOINDEX
            sitemap = False
            out["ledger_enforced"] = True
            out["notes"].append(f"release_ledger: {route['route_id']} is {lg['release_status']} "
                                f"({', '.join(lg.get('blockers') or [])}); downgraded to noindex")
        d = self.decisions.get(path)
        if d:
            kind = d["decision"]
            out["decision"] = {"decision_id": d.get("decision_id"), "decision": kind}
            if kind == "noindex":
                robots, sitemap = NOINDEX, False
            elif kind == "canonical_to":
                target = self.resolve(d["target"], sitemap_policy)
                if target["render"] and requests_index(target["robots"]) and target["canonical"] == d["target"]:
                    out["canonical"], sitemap = d["target"], False
                else:
                    out["notes"].append(f"decision canonical_to {d['target']} NOT applied: the target is not an "
                                        f"indexable self-canonical page")
            elif kind in ("redirect_to", "retire"):
                out.update(render=False, redirect_to=d.get("target"))
            out["notes"].append(f"approved decision {d.get('decision_id')}: {kind}")
        out["robots"] = robots
        out["sitemap"] = sitemap and requests_index(robots) and out["canonical"] == path
        return out

    def render_directives(self, path):
        """For renderers: (robots, absolute canonical URL). Raises if the page may not be rendered."""
        r = self.resolve(path)
        if not r["render"]:
            raise PermissionError(f"{path}: {r['basis']} — {'; '.join(r['notes'])}")
        return r["robots"], SITE + r["canonical"]


def canonical_path(href):
    return re.sub(r"^https?://[^/]+", "", href) if href else None
