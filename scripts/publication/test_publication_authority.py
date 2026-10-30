#!/usr/bin/env python3
"""test_publication_authority.py — Recovery-02 proofs: directive authority, renderer conformance,
sitemaps, surface negative cases, previews and evidence blockers.

Run: python3 scripts/publication/test_publication_authority.py   (stdlib unittest; exit 0 = all pass)
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "validators"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "reference_production"))
import publication_authority as pa  # noqa: E402
import validate_publication_authority as vpa  # noqa: E402
import generate_sitemaps as gs  # noqa: E402
import distinctiveness_core as dc  # noqa: E402

POLICY = dc.load_policy()
GREEN = {"governance": "governed", "evidence": "evidence_locked", "claim": "claim_approved",
         "validation": "validated", "ig": "ig_reviewed_pass", "release": "authorized"}

PAGE = """<!DOCTYPE html><html lang="en"><head><title>{name} — Bisulfid Atlas</title>
<meta name="robots" content="{robots}"><link rel="canonical" href="https://bisulfid.com{canon}"></head>
<body><main><h1>{name}</h1><h2>Term and topic boundary</h2>
<p>This node situates {name} within the cohort family as a terminology reference entry.</p>
<p>It clarifies how neighbouring atlas routes relate without asserting unsupported chemical facts.</p>
<h2>Context layers</h2><p>Structured reference for analysts and journalists; not a primary-source citation.</p>
<p>Context framing without operational, market, or investment advice for {name} readers.</p>{extra}
</main></body></html>"""


def write_page(root, path, name, robots="index, follow", canon=None, extra=""):
    d = os.path.join(root, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(PAGE.format(name=name, robots=robots, canon=canon or path, extra=extra))


class Fixture:
    """A small surface with its own sealed baseline, decisions and certifications."""

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix="pubauth-")
        write_page(self.root, "/t/alpha/", "Alpha Sulfide")
        write_page(self.root, "/t/beta/", "Beta Sulfide")
        write_page(self.root, "/t/gamma/", "Gamma Sulfide", robots="noindex, follow")
        self.sitemap(["/t/alpha/", "/t/beta/"])
        pages = dc.load_html_pages(POLICY, self.root)
        entries = []
        for p in pages:
            path = dc.surface_url_path(p, self.root)
            entries.append({"p": path, "h": dc.body_hash_hex(p), "r": None, "g": "FAIL", "robots": p.robots,
                            "sm": path in ("/t/alpha/", "/t/beta/"), "c": path})
        self.baseline = self.dump({"entries": entries, "entry_count": len(entries),
                                   "entries_sha256": dc.hold_entries_digest(entries)})
        self.decisions = self.dump({"decisions": []})
        self.certs = self.dump({"certifications": []})

    def dump(self, obj):
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, dir=self.root + "_meta" if False else None)
        json.dump(obj, f)
        f.close()
        return f.name

    def sitemap(self, paths):
        body = "".join(f"<url><loc>https://bisulfid.com{p}</loc></url>" for p in paths)
        with open(os.path.join(self.root, "sitemap-001.xml"), "w") as fh:
            fh.write(f"<urlset>{body}</urlset>")

    def authority(self, decisions=None, certs=None, postures=None):
        if decisions is not None:
            with open(self.decisions, "w") as fh:
                json.dump({"decisions": decisions}, fh)
        if certs is not None:
            with open(self.certs, "w") as fh:
                json.dump({"certifications": certs}, fh)
        return pa.Authority(self.baseline, self.decisions, self.certs, postures_override=postures)

    def states(self, authority, inst=None):
        pages = dc.load_html_pages(POLICY, self.root)
        u = dc.Universe(pages, POLICY)
        ctx = dc.IGContext(os.path.join(self.root, "none.json"))
        verdicts = [dc.gate12_verdict(p, u, POLICY, ctx, institutional=(inst or {}).get(dc.surface_url_path(p, self.root)))
                    for p in pages]
        return {s["path"]: s["state"] for s in vpa.check_surface(self.root, authority, POLICY, pages=pages, verdicts=verdicts)}

    def close(self):
        shutil.rmtree(self.root)
        for f in (self.baseline, self.decisions, self.certs):
            os.unlink(f)


class ResolverTests(unittest.TestCase):

    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        self.f.close()

    def test_status_quo_keeps_exactly_the_served_directives(self):
        a = self.f.authority()
        r = a.resolve("/t/alpha/")
        self.assertEqual((r["robots"], r["sitemap"], r["canonical"], r["basis"]),
                         ("index, follow", True, "/t/alpha/", "legacy_status_quo"))
        self.assertEqual(a.resolve("/t/gamma/")["robots"], "noindex, follow", "a noindex page never escalates")
        self.assertFalse(a.resolve("/t/alpha/", "approved_only")["sitemap"], "approved-only sitemaps exclude legacy URLs")

    def test_unknown_page_is_not_authorized(self):
        r = self.f.authority().resolve("/t/new/")
        self.assertFalse(r["render"])
        self.assertEqual(r["basis"], "not_authorized")

    def test_gate12i_pass_alone_never_grants_indexation(self):
        # Nothing in the resolver reads Gate 12 / 12-I: a brand-new institutional page has no authority.
        self.assertFalse(self.f.authority().resolve("/new-hub/")["render"])
        cert = {"certification_id": "R11-T", "path": "/new-hub/", "governance": "governed", "validation": "validated",
                "release": "authorized", "status": "certified"}
        r = self.f.authority(certs=[cert]).resolve("/new-hub/")
        self.assertEqual(r["robots"], "index, follow", "only a Contract-C R11 certification makes it indexable")
        r = self.f.authority(certs=[dict(cert, status="proposed")]).resolve("/new-hub/")
        self.assertFalse(r["render"], "an unapproved certification is ignored")

    def test_contract_c_governs_bound_urls(self):
        a = self.f.authority(postures={"/t/alpha/": (GREEN, "fixture")})
        self.assertEqual(a.resolve("/t/alpha/")["robots"], "index, follow")
        a = self.f.authority(postures={"/t/alpha/": (dict(GREEN, evidence="evidence_sufficient"), "fixture")})
        r = a.resolve("/t/alpha/")
        self.assertEqual((r["robots"], r["sitemap"]), ("noindex, follow", False), "public_noindex (R9)")
        a = self.f.authority(postures={"/t/alpha/": (dict(GREEN, claim="claim_pending"), "fixture")})
        self.assertEqual(a.resolve("/t/alpha/")["basis"], "legacy_status_quo",
                         "a not-yet-public governed object leaves the legacy page holding the URL")

    def test_release_ledger_block_downgrades_acquire(self):
        r = pa.Authority().resolve("/acquire/")
        self.assertEqual(r["robots"], "noindex, follow")
        self.assertTrue(any("release_ledger" in n for n in r["notes"]))

    def test_decisions_only_downgrade_and_respect_status(self):
        d = {"decision_id": "D1", "path": "/t/beta/", "decision": "noindex", "status": "approved"}
        r = self.f.authority(decisions=[d]).resolve("/t/beta/")
        self.assertEqual((r["robots"], r["sitemap"]), ("noindex, follow", False))
        r = self.f.authority(decisions=[dict(d, status="proposed")]).resolve("/t/beta/")
        self.assertEqual(r["robots"], "index, follow", "proposals are never applied")
        canon = {"decision_id": "D2", "path": "/t/beta/", "decision": "canonical_to", "target": "/t/alpha/", "status": "approved"}
        r = self.f.authority(decisions=[canon]).resolve("/t/beta/")
        self.assertEqual((r["canonical"], r["sitemap"]), ("/t/alpha/", False))
        bad = dict(canon, target="/t/gamma/")
        r = self.f.authority(decisions=[bad]).resolve("/t/beta/")
        self.assertEqual(r["canonical"], "/t/beta/", "canonical to a noindex target is refused")
        red = {"decision_id": "D3", "path": "/t/beta/", "decision": "redirect_to", "target": "/t/alpha/", "status": "approved"}
        self.assertFalse(self.f.authority(decisions=[red]).resolve("/t/beta/")["render"])


class SurfaceTests(unittest.TestCase):

    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        self.f.close()

    def test_untouched_legacy_surface_passes_no_deadlock(self):
        st = self.f.states(self.f.authority())
        self.assertEqual(set(st.values()), {"LEGACY_STATUS_QUO"})

    def test_reactivating_index_on_a_noindex_page_blocks(self):
        write_page(self.f.root, "/t/gamma/", "Gamma Sulfide", robots="index, follow")
        self.assertEqual(self.f.states(self.f.authority())["/t/gamma/"], "BLOCK_DIRECTIVE_ESCALATION")

    def test_adding_a_sitemap_entry_blocks(self):
        self.f.sitemap(["/t/alpha/", "/t/beta/", "/t/gamma/"])
        self.assertEqual(self.f.states(self.f.authority())["/t/gamma/"], "BLOCK_SITEMAP_ESCALATION")

    def test_new_page_blocks_even_if_noindex(self):
        write_page(self.f.root, "/t/delta/", "Delta Sulfide", robots="noindex, follow")
        self.assertEqual(self.f.states(self.f.authority())["/t/delta/"], "BLOCK_UNAUTHORIZED_PAGE")

    def test_modified_indexed_page_blocks_but_noindex_repair_is_allowed(self):
        write_page(self.f.root, "/t/beta/", "Beta Sulfide", extra="<p>Repaired paragraph with new wording.</p>")
        self.assertEqual(self.f.states(self.f.authority())["/t/beta/"], "BLOCK_MODIFIED_INDEXED")
        write_page(self.f.root, "/t/beta/", "Beta Sulfide", robots="noindex, follow", extra="<p>Repaired paragraph.</p>")
        self.f.sitemap(["/t/alpha/"])
        self.assertEqual(self.f.states(self.f.authority())["/t/beta/"], "LEGACY_REPAIR_NOINDEX")

    def test_noindex_with_new_cross_canonical_blocks(self):
        write_page(self.f.root, "/t/gamma/", "Gamma Sulfide", robots="noindex, follow", canon="/t/alpha/")
        st = self.f.states(self.f.authority())
        self.assertIn(st["/t/gamma/"], ("BLOCK_CANONICAL_MISMATCH", "BLOCK_CANONICAL_CONFLICT"))

    def test_removal_needs_an_approved_decision(self):
        shutil.rmtree(os.path.join(self.f.root, "t", "beta"))
        self.f.sitemap(["/t/alpha/"])
        self.assertEqual(self.f.states(self.f.authority())["/t/beta/"], "BLOCK_UNAPPROVED_REMOVAL")
        d = {"decision_id": "D4", "path": "/t/beta/", "decision": "retire", "status": "approved"}
        self.assertNotIn("/t/beta/", self.f.states(self.f.authority(decisions=[d])))

    def test_index_approved_page_failing_gate12_is_vetoed(self):
        a = self.f.authority(postures={"/t/alpha/": (GREEN, "fixture")})
        self.assertEqual(self.f.states(a)["/t/alpha/"], "BLOCK_GATE12_VETO")

    def test_applied_canonical_decision_is_served_correctly(self):
        d = {"decision_id": "D5", "path": "/t/beta/", "decision": "canonical_to", "target": "/t/alpha/", "status": "approved"}
        write_page(self.f.root, "/t/beta/", "Beta Sulfide", canon="/t/alpha/")
        self.f.sitemap(["/t/alpha/"])
        self.assertEqual(self.f.states(self.f.authority(decisions=[d]))["/t/beta/"], "LEGACY_STATUS_QUO")


class SitemapTests(unittest.TestCase):

    def test_approved_only_lists_exactly_index_approved_urls(self):
        f = Fixture()
        out = tempfile.mkdtemp()
        try:
            a = f.authority(postures={"/t/alpha/": (GREEN, "fixture")})
            urls = gs.build(a, "approved_only")
            self.assertEqual(urls, ["/t/alpha/"])
            gs.write(urls, out)
            n, errs = gs.validate(out, a, "approved_only")
            self.assertEqual((n, errs), (1, []))
            self.assertEqual(gs.build(f.authority(), "approved_only"), [], "nothing is approved today")
            self.assertEqual(gs.build(f.authority(), "status_quo"), ["/t/alpha/", "/t/beta/"], "status quo never adds")
        finally:
            f.close()
            shutil.rmtree(out)

    def test_refuses_to_write_into_site_public(self):
        self.assertEqual(gs.main(["--out", os.path.join(ROOT, "site", "public")]), 2)


class RendererConformanceTests(unittest.TestCase):

    def test_template_has_no_hard_coded_robots(self):
        with open(os.path.join(ROOT, "main", "templates", "atlas", "base.html"), encoding="utf-8") as fh:
            t = fh.read()
        self.assertNotIn('content="index, follow"', t)
        self.assertIn("{{robots_directive}}", t)

    def test_renderer_takes_directives_from_the_authority(self):
        sys.path.insert(0, os.path.join(ROOT, "scripts"))
        import atlas_render_dossier_l3 as rd

        class Fake(pa.Authority):
            def render_directives(self, path):
                if path == "/molybdenum-disulfide/":
                    raise PermissionError("not authorized (test)")
                if path == "/bisulfid/":
                    return "noindex, follow", pa.SITE + "/bisulfid/"
                return super().render_directives(path)

        out = tempfile.mkdtemp()
        old_auth, old_argv = rd.Authority, sys.argv
        try:
            rd.Authority = Fake
            sys.argv = ["x", "--out", out]
            self.assertEqual(rd.main(), 0)
        finally:
            rd.Authority, sys.argv = old_auth, old_argv
        try:
            self.assertFalse(os.path.exists(os.path.join(out, "molybdenum-disulfide", "index.html")),
                             "an unauthorized page is not rendered at all")
            b = open(os.path.join(out, "bisulfid", "index.html"), encoding="utf-8").read()
            self.assertIn('<meta name="robots" content="noindex, follow">', b, "a downgraded page stays downgraded")
            h = open(os.path.join(out, "what-is-bisulfid", "index.html"), encoding="utf-8").read()
            self.assertIn('<meta name="robots" content="index, follow">', h, "a status-quo page keeps what it was served")
            self.assertNotIn("{{", h)
            for inst in ("index.html", os.path.join("de", "index.html"), os.path.join("methodology", "index.html")):
                self.assertFalse(os.path.exists(os.path.join(out, inst)),
                                 f"institutional page {inst} must not be wrapped in dossier boilerplate")
        finally:
            shutil.rmtree(out)

    def test_unresolved_placeholder_is_refused(self):
        sys.path.insert(0, os.path.join(ROOT, "scripts"))
        import atlas_render_release_l2 as rr
        errors = []
        self.assertIsNone(rr._finalize("<meta content=\"{{robots_directive}}\">", "x", errors))
        self.assertTrue(errors)


class AcquireProposalTests(unittest.TestCase):
    """Recovery-03 A: /acquire/ is corrected by a STAGED robots change, never by editing the ledger."""

    def test_proposed_decision_is_not_applied(self):
        a = pa.Authority()
        self.assertNotIn("/acquire/", a.decisions, "a 'proposed' decision must not be applied by the resolver")
        d = json.load(open(os.path.join(ROOT, "main", "data", "publication", "url_decisions.json")))
        prop = [x for x in d["decisions"] if x["path"] == "/acquire/"]
        self.assertEqual([x["status"] for x in prop], ["proposed"])

    def test_ledger_still_blocks_acquire(self):
        led = json.load(open(os.path.join(ROOT, "main", "data", "release_ledger.json")))
        rows = led["records"]
        row = next(r for r in rows if r.get("route_id") == "acquire")
        self.assertEqual(row["release_status"], "blocked")

    def test_staged_page_changes_only_robots_and_keeps_contact(self):
        sys.path.insert(0, os.path.join(ROOT, "scripts", "recovery"))
        import stage_acquire_proposal as sap
        self.assertEqual(sap.main(["--check"]), 0)
        live = open(os.path.join(ROOT, "site", "public", "acquire", "index.html"), encoding="utf-8").read()
        staged = open(os.path.join(ROOT, "main", "data", "recovery", "staged", "acquire", "index.html"), encoding="utf-8").read()
        diff = [(x, y) for x, y in zip(live.splitlines(), staged.splitlines()) if x != y]
        self.assertEqual(len(live.splitlines()), len(staged.splitlines()))
        self.assertEqual(diff, [(sap.OLD, sap.NEW)])
        self.assertIn('href="mailto:', staged)
        self.assertEqual(pa.Authority().resolve("/acquire/")["robots"], "noindex, follow")


class IndexationPlanTests(unittest.TestCase):
    """Recovery-03 E: a risk-based plan, never a mass noindex."""

    def setUp(self):
        self.plan = json.load(open(os.path.join(ROOT, "main", "data", "recovery", "R03_INDEXATION_REDUCTION_PLAN.json"), encoding="utf-8"))

    def test_every_generated_page_is_classified_once(self):
        self.assertEqual(sum(f["pages"] for f in self.plan["families"]), 12289)

    def test_first_wave_is_small_and_unapplied(self):
        w = self.plan["wave_1"]["pages"]
        self.assertLessEqual(len(w), 0.01 * 12289)
        a = pa.Authority()
        d = json.load(open(os.path.join(ROOT, "main", "data", "publication", "url_decisions.json")))
        self.assertTrue(all(x["status"] == "proposed" for x in d["decisions"]), "nothing is approved by this sprint")
        for p in w:
            self.assertNotIn(p, a.decisions)

    def test_similarity_alone_never_authorizes_canonical(self):
        r = json.load(open(os.path.join(ROOT, "main", "data", "publication", "url_decision_rules.json")))
        canon = next(x for x in r["rules"] if x["id"] == "R-CANON-1")
        self.assertIn("never authorizes a canonical by itself", canon["when"])
        self.assertEqual(self.plan["canonical_consolidation"]["eligible_under_R_CANON_1_v1_1"], 0)


class PreviewTests(unittest.TestCase):

    def test_previews_are_current_and_noindex(self):
        import render_ko_reference as rk
        import render_institutional_preview as ri
        self.assertEqual(rk.main(["--check"]), 0)
        self.assertEqual(ri.main(["--check"]), 0)
        for p in ("molybdenum-disulfide", "bisulfid-vs-bisulfide", "home", "de"):
            t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", p, "index.html"), encoding="utf-8").read()
            self.assertIn('<meta name="robots" content="noindex, nofollow">', t)

    def test_homepage_asserts_no_unapproved_terminology_claim(self):
        t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", "home", "index.html"), encoding="utf-8").read().lower()
        for phrase in ("bisulfid is the german", "german spelling of bisulfide.", "bisulfide is hs"):
            self.assertNotIn(phrase, t)
        self.assertIn("will be stated as fact only after its sources are verified and admitted", t)

    def test_homepage_hreflang_is_reciprocal_or_absent(self):
        import render_institutional_preview as ri
        en = json.load(open(os.path.join(ri.SPEC_DIR, "INST-HOME-EN.json"), encoding="utf-8"))
        self.assertEqual(dict(ri.alternates(en)), {"en": "/", "de": "/de/", "x-default": "/"})
        for p in ("home", "de"):
            t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", p, "index.html"), encoding="utf-8").read()
            self.assertIn('<link rel="alternate" hreflang="de" href="https://bisulfid.com/de/">', t)
            self.assertIn('<link rel="alternate" hreflang="en" href="https://bisulfid.com/">', t)
        one_sided = dict(en, alternates={"en": "/", "fr": "/fr/"})
        with self.assertRaises(ri.RenderError):
            ri.alternates(one_sided)

    def test_r11_home_certifications_are_proposals_only(self):
        a = pa.Authority()
        for path in ("/", "/de/"):
            self.assertEqual(a.contract_c(path), (None, None), "a proposed R11 certification binds nothing")
        d = json.load(open(os.path.join(ROOT, "main", "data", "publication", "nonfactual_certifications.json")))
        self.assertTrue(d["certifications"])
        self.assertTrue(all(c["status"] == "proposed" and c["certified_by"] is None for c in d["certifications"]))

    def test_homepage_claims_no_credentials(self):
        for p in ("home", "de"):
            t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", p, "index.html"), encoding="utf-8").read().lower()
            for phrase in ("dr.", "phd", "professor", "our experts", "reviewed by", "editor-in-chief"):
                self.assertNotIn(phrase, t)

    def test_homepage_numbers_come_from_registries(self):
        import render_institutional_preview as ri
        gov = ri.gov_values()
        t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", "home", "index.html"), encoding="utf-8").read()
        self.assertIn(f"rests on {gov['mos2_admitted_evidence']} admitted evidence records", t)
        with self.assertRaises(ri.RenderError):
            ri.resolve("{{GOV:invented_number}}", gov)

    def test_mos2_json_ld_values_come_from_evidence(self):
        t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", "molybdenum-disulfide", "index.html"), encoding="utf-8").read()
        ld = json.loads(t.split('<script type="application/ld+json">')[1].split("</script>")[0])
        ev = json.load(open(os.path.join(ROOT, "main", "data", "evidence", "EVD-MOS2-FORMULA-PUBCHEM.json")))
        self.assertEqual(ld["molecularFormula"], ev["locator"]["fields_quoted"]["MolecularFormula"])
        self.assertIn(ev["locator"]["url"], ld["sameAs"])
        self.assertNotIn('rel="alternate" hreflang', t, "no equivalent page exists, so no hreflang link is emitted")

    def test_bisulfid_boundary_renders_only_admitted_modules(self):
        r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "reference_production", "evidence_blockers.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)
        b = json.load(open(os.path.join(ROOT, "main", "data", "reference_production", "blockers",
                                        "PLAN-BISULFID-BISULFIDE-BOUNDARY_BLOCKERS.json")))
        blocked = {m["module_id"] for m in b["modules"] if not m["renderable"]}
        self.assertEqual(blocked, {"de_usage"}, "German industry usage has no admissible terminology source")

    def test_bisulfid_preview_asserts_no_spelling_equivalence(self):
        t = open(os.path.join(ROOT, "main", "data", "reference_production", "previews", "bisulfid-vs-bisulfide", "index.html"),
                 encoding="utf-8").read()
        low = t.lower()
        for phrase in ("same underlying compound", "two spellings, one compound", "is the german spelling of bisulfide",
                       "is the german equivalent of"):
            self.assertNotIn(phrase, low)
        self.assertIn('<meta name="robots" content="noindex, nofollow">', t)
        self.assertNotIn("EVD-TERM-BADGER", t, "industry usage evidence is a recorded boundary, never rendered as support")

    def test_terminology_locators_are_captured_verbatim(self):
        cap = json.load(open(os.path.join(ROOT, "main", "data", "evidence", "captures", "R03_TERMINOLOGY_CAPTURES.json")))["captures"]
        import glob
        for f in glob.glob(os.path.join(ROOT, "main", "data", "evidence", "EVD-TERM-*.json")):
            e = json.load(open(f, encoding="utf-8"))
            loc = e["locator"]
            found = {p["quote"] for k in loc["capture_keys"] for p in cap[k]["passages"] if p["found"]}
            for q in loc["verbatim"]:
                self.assertIn(q, found, f"{e['evidence_id']}: {q!r} not captured verbatim")
            self.assertEqual(loc["sha256"], cap[loc["capture_keys"][0]]["sha256"])

    def test_pilot_claims_count_as_unapproved_for_publication(self):
        import evidence_blockers as eb
        claims, sources, quals, evidence = eb.stores()
        b = eb.claim_blockers("CLM-MOS2-FORMULA", claims, sources, quals, evidence, None)
        self.assertTrue(any(x["step"] == 2 for x in b), "pilot claims are non-operational: consistent with Contract C claim_pending")


class Stage2GuardTests(unittest.TestCase):

    def test_mass_noindex_tool_still_refuses_site_public(self):
        sys.path.insert(0, os.path.join(ROOT, "scripts", "recovery"))
        import stage2_legacy_noindex as s2
        self.assertEqual(s2.main(["--out", os.path.join(ROOT, "site", "public")]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
