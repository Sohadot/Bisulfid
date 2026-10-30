"""distinctiveness_core.py — Gate 12 (Page Distinctiveness & Information Gain) engine.

Policy: main/data/distinctiveness/gate12_policy.json (versioned, blocking).
CLI:    scripts/validators/validate_distinctiveness.py

WHAT THIS DOES
--------------
Separates reusable site infrastructure from substantive page knowledge, then measures
each page on four independent dimensions:

  A. text similarity     — entity-masked word 5-gram shingles; MinHash/LSH candidate
                           discovery for the corpus audit; exact Jaccard + overlap
                           coefficient confirmation; exhaustive exact comparison for
                           publication candidates.
  B. structure           — substantive heading skeleton shared with siblings.
  C. boilerplate ratio   — share of substantive prose made of sentences that recur
                           (entity-masked) on many pages.
  D. information gain    — governed, evidence-backed, page-specific knowledge units
                           (main/data/distinctiveness/ig_unit_registry.json).

LAWS
----
* Low similarity never passes Gate 12 by itself; IG and structure must also pass.
* Infrastructure is excluded only by explicitly registered patterns, never because text
  recurs across pages (recurrence is what this gate measures).
* Gate 12 never writes publication state. Combined eligibility requires Contract C AND
  Gate 12 (combined_publication_eligibility); neither overrides the other.

Stdlib only. Deterministic (blake2b hashing, fixed MinHash seeds). No network.
"""

import difflib
import glob
import hashlib
import html.parser
import json
import os
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
POLICY_PATH = os.path.join(DATA, "distinctiveness", "gate12_policy.json")
IG_REGISTRY_PATH = os.path.join(DATA, "distinctiveness", "ig_unit_registry.json")

SLOT = "xentx"  # entity slot token (survives tokenization as one word)
_TOKEN_RE = re.compile(r"[^\W_]+", re.UNICODE)
_SENT_SPLIT_RE = re.compile(r"(?<=[.!?;])\s+")
_MERSENNE = (1 << 61) - 1


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_policy(path=POLICY_PATH):
    return load_json(path)


def rel(path):
    p = os.path.abspath(path)
    return os.path.relpath(p, ROOT) if p.startswith(ROOT) else p


# --------------------------------------------------------------------------- text utils

def normalize_text(text):
    """Lowercase, NFKC, strip markdown emphasis/links/code ticks; keep words and digits."""
    t = unicodedata.normalize("NFKC", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)          # [text](url) -> text
    t = t.replace("`", " ").replace("*", " ").replace("_", " ")
    return t.lower()


def tokens(text):
    return _TOKEN_RE.findall(text)


def phrase_index(phrases):
    """Entity phrases -> {first_token: [token tuples, longest first]} for token-level masking."""
    idx = defaultdict(set)
    for p in phrases:
        toks = tuple(tokens(normalize_text(p)))
        if toks:
            idx[toks[0]].add(toks)
    return {k: sorted(v, key=len, reverse=True) for k, v in idx.items()}


def mask_tokens(toks, pindex):
    """Replace every occurrence of a page entity phrase in a token list by one slot token."""
    if not pindex:
        return list(toks)
    out, i, n = [], 0, len(toks)
    while i < n:
        cands = pindex.get(toks[i])
        hit = None
        if cands:
            for c in cands:
                if tuple(toks[i:i + len(c)]) == c:
                    hit = c
                    break
        if hit:
            if not out or out[-1] != SLOT:
                out.append(SLOT)
            i += len(hit)
        else:
            out.append(toks[i])
            i += 1
    return out


def mask_entities(text, phrases):
    """Entity-masked token string of `text` (normalized); used for statements and headings."""
    return " ".join(mask_tokens(tokens(normalize_text(text)), phrase_index(phrases)))


def masked_sentences(text, pindex):
    """Split text into sentences (per line, on . ! ? ;), normalize, tokenize, entity-mask."""
    out = []
    for line in text.split("\n"):
        for snt in split_sentences(line):
            out.append(mask_tokens(tokens(normalize_text(snt)), pindex))
    return out


def h64(s):
    return int.from_bytes(hashlib.blake2b(s.encode("utf-8"), digest_size=8).digest(), "big")


def shingles(toks, k):
    if len(toks) < k:
        return {h64(" ".join(toks))} if toks else set()
    return {h64(" ".join(toks[i:i + k])) for i in range(len(toks) - k + 1)}


def similarity(a, b, oc_min):
    """Return (S, jaccard, overlap_coefficient_or_None) for two shingle sets."""
    if not a or not b:
        return 0.0, 0.0, None
    inter = len(a & b)
    if not inter:
        return 0.0, 0.0, (0.0 if min(len(a), len(b)) >= oc_min else None)
    j = inter / (len(a) + len(b) - inter)
    oc = inter / min(len(a), len(b)) if min(len(a), len(b)) >= oc_min else None
    return max(j, oc or 0.0), j, oc


def split_sentences(text):
    out = []
    for line in text.split("\n"):
        line = line.strip(" -•\t")
        if not line:
            continue
        out.extend(s for s in _SENT_SPLIT_RE.split(line) if s.strip())
    return out


# --------------------------------------------------------------------------- page model

class Page:
    """One page reduced to infrastructure vs substantive content."""

    __slots__ = ("id", "surface", "route_id", "language", "title", "entity_phrases",
                 "front", "family", "ko_family", "cohort", "is_draft", "publication_candidate",
                 "public_indexable", "sections", "substantive_text", "infra_tokens",
                 "masked_tokens", "raw_tokens", "skeleton", "shape", "sentences",
                 "shingle_set", "raw_shingle_set", "body_hash", "control", "robots", "canonical")

    def __init__(self, pid, surface):
        self.id = pid
        self.surface = surface
        self.route_id = None
        self.language = None
        self.title = ""
        self.entity_phrases = []
        self.front = {}
        self.family = "unknown"
        self.ko_family = "unclassified"
        self.cohort = None
        self.is_draft = True
        self.publication_candidate = False
        self.public_indexable = False
        self.sections = []          # list of (heading, kind, [blocks])
        self.substantive_text = ""
        self.infra_tokens = 0
        self.masked_tokens = []
        self.raw_tokens = []
        self.skeleton = ()
        self.shape = ()
        self.sentences = []         # list of (masked_sentence_hash, token_count, masked_sentence)
        self.shingle_set = set()
        self.raw_shingle_set = set()
        self.body_hash = None
        self.control = False
        self.robots = None          # HTML only: robots meta content as served
        self.canonical = None       # HTML only: rel=canonical href as served


class _Rules:
    """Compiled infrastructure-exclusion rules from the policy."""

    def __init__(self, policy):
        ie = policy["infrastructure_exclusion"]
        self.heading_rx = [re.compile(p, re.I) for p in ie["section_heading_patterns"]]
        self.line_rx = [re.compile(p, re.I) for p in ie["line_patterns"]]
        self.inline_rx = [re.compile(p) for p in ie["inline_strip_patterns"]]
        self.skip_tags = set(ie["html_skip_tags"])
        self.skip_aria_hidden = bool(ie.get("html_skip_aria_hidden", True))
        self.disclaimer_lines = set()
        ddir = os.path.join(ROOT, ie["shared_disclaimer_dir"])
        for f in glob.glob(os.path.join(ddir, "*.md")):
            with open(f, encoding="utf-8") as fh:
                for line in fh:
                    n = " ".join(tokens(normalize_text(line)))
                    if len(n.split()) >= 4:
                        self.disclaimer_lines.add(n)

    def infra_heading(self, heading):
        h = " ".join(normalize_text(heading).split()).strip(" :")
        return any(rx.search(h) for rx in self.heading_rx)

    def infra_line(self, line):
        s = line.strip()
        if any(rx.search(s) for rx in self.line_rx):
            return True
        return " ".join(tokens(normalize_text(s))) in self.disclaimer_lines

    def strip_inline(self, line):
        for rx in self.inline_rx:
            line = rx.sub(" ", line)
        return line


def _parse_front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    front = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            front[k.strip()] = v.strip().strip("'\"")
    return front, text[end + 4:]


def _truthy(v):
    return str(v).strip().lower() in ("true", "yes", "1")


_TITLE_SEP_RE = re.compile(r"\s+[—–|]\s+|\s+-\s+|:\s+")
_GENERIC_TITLE_PART_RE = re.compile(
    r"^(bisulfid( atlas| com)?|(\w+ ){0,2}(reference|referenz|terminologie)|de terminologie|"
    r"(ai|student|researcher|investor|child|public) (reference|explainer)|learn|explore|guide|overview|explainer)$", re.I)


def _entity_phrases(route_id, h1, title):
    """The page's own entity phrases: non-generic title/H1 parts (+ 'for <audience>' stems), slugs, route_id."""
    phrases = []
    for t in (h1, title):
        if not t:
            continue
        for part in _TITLE_SEP_RE.split(t):
            part = part.strip()
            norm = " ".join(tokens(normalize_text(part)))
            if not norm or _GENERIC_TITLE_PART_RE.match(norm):
                continue
            phrases.append(part)
            stem = re.sub(r"\s+for\s+[\w /-]+$", "", part, flags=re.I)
            if stem != part:
                phrases.append(stem)
            phrases.append(stem.replace(" ", "_").lower())
    if route_id:
        phrases.append(route_id)
    return [p for p in dict.fromkeys(phrases) if tokens(normalize_text(p))]


def entity_key(page):
    """Reporting key for 'which entity is this page about' (longest non-slug entity phrase)."""
    cands = [p for p in page.entity_phrases if "_" not in p]
    return max(cands, key=lambda p: len(tokens(normalize_text(p))), default=page.route_id or page.id)


def _sections_from_lines(lines):
    """Split markdown-ish lines into [(heading, level, [lines])]; H1 opens a level-1 section."""
    sections = [("", 0, [])]
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m:
            sections.append((m.group(2).strip(), len(m.group(1)), []))
        else:
            sections[-1][2].append(line)
    return sections


def _finalize(page, raw_sections, rules, policy):
    """Classify sections/lines, mask entities, compute tokens/shingles/sentences/skeleton."""
    k = policy["text_similarity"]["shingle_size"]
    sent_min = policy["boilerplate"]["sentence_min_tokens"]
    subst_lines, skeleton, shape = [], [], []
    infra_tok = 0
    page.sections = []
    for heading, level, lines in raw_sections:
        kind = "infra" if (level >= 2 and rules.infra_heading(heading)) else "substantive"
        kept = []
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if kind == "infra" or rules.infra_line(s):
                infra_tok += len(tokens(normalize_text(s)))
                continue
            s = rules.strip_inline(s)
            if tokens(normalize_text(s)):
                kept.append(s)
        page.sections.append((heading, kind, kept))
        if kind == "infra":
            infra_tok += len(tokens(normalize_text(heading)))
            continue
        if level >= 2:
            skeleton.append(heading)
            bullets = sum(1 for x in kept if re.match(r"^([-*+]|\d+\.)\s", x))
            rows = sum(1 for x in kept if x.startswith("|"))
            shape.append((len(kept) - bullets - rows, bullets, rows))
        subst_lines.extend(kept)

    page.substantive_text = "\n".join(subst_lines)
    page.infra_tokens = infra_tok
    pindex = phrase_index(page.entity_phrases)
    page.raw_tokens = tokens(normalize_text(page.substantive_text))
    sent_toks = masked_sentences(page.substantive_text, pindex)
    page.masked_tokens = [t for st in sent_toks for t in st]
    page.skeleton = tuple(" ".join(mask_tokens(tokens(normalize_text(h)), pindex)) for h in skeleton)
    page.shape = tuple(shape)
    page.body_hash = h64(" ".join(page.masked_tokens))
    page.shingle_set = shingles(page.masked_tokens, k)
    page.raw_shingle_set = shingles(page.raw_tokens, k)
    sents = [(h64(" ".join(st)), len(st), " ".join(st)) for st in sent_toks if len(st) >= sent_min]
    page.sentences = sents
    return page


def parse_markdown(path, text, policy, rules=None, page_id=None):
    rules = rules or _Rules(policy)
    front, body = _parse_front_matter(text)
    page = Page(page_id or rel(path), "markdown")
    page.front = front
    page.route_id = front.get("route_id")
    page.language = front.get("language") or front.get("locale")
    h1 = ""
    m = re.search(r"^#\s+(.+)$", body, re.M)
    if m:
        h1 = m.group(1).strip()
    page.title = front.get("title") or h1
    page.entity_phrases = _entity_phrases(page.route_id, h1, front.get("title"))
    page.cohort = front.get("cohort_id") or _dir_family(page.id)
    ptype = front.get("page_type_id") or "PT_UNSPECIFIED"
    fam_map = policy["page_family_map"]["page_type_to_family"]
    page.ko_family = fam_map.get(ptype, "unclassified")
    page.family = "|".join([page.language or "?", page.cohort or "?", ptype])
    status = (front.get("status") or "").lower()
    pub = (front.get("publication_status") or "").lower()
    page.is_draft = status in ("draft", "planned", "") or pub == "non_public"
    page.publication_candidate = (
        _truthy(front.get("publication_eligibility")) or _truthy(front.get("indexable"))
        or _truthy(front.get("in_sitemap")) or pub in ("public", "published", "live")
        or status in ("published", "live", "released"))
    page.control = _truthy(front.get("gate12_control"))
    raw = _sections_from_lines(body.splitlines())
    return _finalize(page, raw, rules, policy)


def _dir_family(pid):
    parts = pid.replace("\\", "/").split("/")
    if "pages" in parts:
        i = parts.index("pages")
        sub = parts[i + 1] if len(parts) > i + 2 else "root"
        return f"{parts[i - 1]}/{sub}"
    return "other"


class _HTMLExtract(html.parser.HTMLParser):
    """Collect <main> text as markdown-ish lines; skip nav/header/footer/aria-hidden/script."""

    BLOCK = {"p", "li", "td", "th", "dt", "dd", "figcaption", "blockquote", "caption"}
    VOID = {"br", "img", "meta", "link", "input", "hr", "source", "wbr", "area", "base", "col", "embed", "param", "track"}

    def __init__(self, skip_tags, skip_aria):
        super().__init__(convert_charrefs=True)
        self.skip_tags, self.skip_aria = skip_tags, skip_aria
        self.stack = []             # (tag, skipping)
        self.in_main = 0
        self.lines, self.buf, self.cur = [], [], None
        self.title, self.robots, self.lane, self.lang, self.h1 = "", "", None, None, ""
        self.canonical = None
        self._in_title = False

    def _skipping(self):
        return any(s for _, s in self.stack)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.canonical = a.get("href")
        if tag == "meta" and (a.get("name") or "").lower() == "robots":
            self.robots = (a.get("content") or "").lower()
        if tag == "title":
            self._in_title = True
        if tag == "body":
            self.lane = a.get("data-atlas-lane")
        if tag in self.VOID:
            return
        skip = tag in self.skip_tags or (self.skip_aria and a.get("aria-hidden") == "true")
        if tag == "main":
            self.in_main += 1
            skip = False
        self.stack.append((tag, skip))
        if tag in self.BLOCK or re.fullmatch(r"h[1-6]", tag):
            self._flush()
            self.cur = tag

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in self.VOID:
            return
        if tag in self.BLOCK or re.fullmatch(r"h[1-6]", tag):
            self._flush()
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break
        if tag == "main":
            self.in_main -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if self.in_main and not self._skipping():
            self.buf.append(data)

    def _flush(self):
        text = " ".join("".join(self.buf).split())
        self.buf = []
        if text:
            tag = self.cur or "p"
            if re.fullmatch(r"h[1-6]", tag):
                lvl = int(tag[1])
                if lvl == 1 and not self.h1:
                    self.h1 = text
                self.lines.append("#" * lvl + " " + text)
            elif tag == "li":
                self.lines.append("- " + text)
            else:
                self.lines.append(text)
        self.cur = None


def parse_html(path, text, policy, rules=None, page_id=None, surface_root=None):
    rules = rules or _Rules(policy)
    ex = _HTMLExtract(rules.skip_tags, rules.skip_aria_hidden)
    ex.feed(text)
    ex._flush()
    pid = page_id or rel(path)
    page = Page(pid, "html")
    page.language = ex.lang
    page.title = " ".join(ex.title.split())
    route = os.path.dirname(os.path.relpath(path, surface_root)) if surface_root else os.path.dirname(pid)
    route = route.replace(os.sep, "/").strip("/")
    page.route_id = "/" if route in ("", ".") else "/" + route + "/"
    page.entity_phrases = _entity_phrases(None, ex.h1, page.title)
    lane = ex.lane or "unknown"
    page.ko_family = policy["page_family_map"]["html_lane_to_family"].get(lane, "unclassified")
    segs = [s for s in page.route_id.strip("/").split("/") if s]
    fam_segs = segs[:3] if len(segs) > 3 else segs[:1]
    page.cohort = "/".join(fam_segs) or "root"
    page.family = "|".join([page.language or "?", lane, page.cohort])
    page.public_indexable = ("index" in ex.robots and "noindex" not in ex.robots)
    page.robots = ex.robots or None
    page.canonical = ex.canonical
    page.is_draft = False
    page.publication_candidate = page.public_indexable
    raw = _sections_from_lines(ex.lines)
    return _finalize(page, raw, rules, policy)


# --------------------------------------------------------------------------- loading corpora

def iter_markdown_corpus(policy, root=ROOT):
    pattern = os.path.join(root, "main", "content", "*", "pages", "**", "*.md")
    return sorted(glob.glob(pattern, recursive=True))


def iter_html_surface(policy, surface_root):
    excluded = set(policy["scope"]["html_surface_excluded_dirs"])
    out = []
    for dirpath, dirnames, filenames in os.walk(surface_root):
        if os.path.abspath(dirpath) == os.path.abspath(surface_root):
            dirnames[:] = [d for d in dirnames if d not in excluded]
        dirnames.sort()
        if "index.html" in filenames:
            out.append(os.path.join(dirpath, "index.html"))
    return sorted(out)


def load_markdown_pages(policy, paths=None, rules=None):
    rules = rules or _Rules(policy)
    pages = []
    for p in (paths if paths is not None else iter_markdown_corpus(policy)):
        with open(p, encoding="utf-8") as fh:
            pages.append(parse_markdown(p, fh.read(), policy, rules))
    return pages


def load_html_pages(policy, surface_root, rules=None):
    rules = rules or _Rules(policy)
    pages = []
    for p in iter_html_surface(policy, surface_root):
        with open(p, encoding="utf-8", errors="replace") as fh:
            pages.append(parse_html(p, fh.read(), policy, rules, surface_root=surface_root))
    return pages


# --------------------------------------------------------------------------- MinHash / LSH

class MinHasher:
    def __init__(self, num_perm, seed=12):
        rng = random.Random(seed)
        self.params = [(rng.randrange(1, _MERSENNE), rng.randrange(0, _MERSENNE)) for _ in range(num_perm)]

    def signature(self, shingle_set):
        if not shingle_set:
            return None
        hs = list(shingle_set)
        return tuple(min(((a * h + b) % _MERSENNE) for h in hs) for a, b in self.params)


def lsh_candidates(signatures, bands, rows):
    """signatures: {rep_index: sig}. Returns a set of (i, j) candidate pairs, i < j."""
    cands = set()
    for b in range(bands):
        buckets = defaultdict(list)
        lo = b * rows
        for idx, sig in signatures.items():
            buckets[sig[lo:lo + rows]].append(idx)
        for members in buckets.values():
            if len(members) < 2:
                continue
            members.sort()
            for x in range(len(members)):
                for y in range(x + 1, len(members)):
                    cands.add((members[x], members[y]))
    return cands


# --------------------------------------------------------------------------- corpus analysis

class Universe:
    """A comparison universe (one surface): exact-body groups, sentence DF, skeleton index."""

    def __init__(self, pages, policy):
        self.policy = policy
        self.pages = pages
        self.by_id = {p.id: p for p in pages}
        self.groups = defaultdict(list)                 # body_hash -> [page index]
        for i, p in enumerate(pages):
            if p.masked_tokens:
                self.groups[p.body_hash].append(i)
        self.reps = [members[0] for members in self.groups.values()]
        self.rep_of_hash = {h: m[0] for h, m in self.groups.items()}
        self.sent_df = Counter()
        for p in pages:
            for h in {s[0] for s in p.sentences}:
                self.sent_df[h] += 1
        self.skeleton_count = Counter(p.skeleton for p in pages if p.skeleton)
        self.top_skeletons = [s for s, _ in self.skeleton_count.most_common(
            policy["structure"]["near_identical_compare_top_k_skeletons"])]

    # --- C. boilerplate
    def sentence_occurrences(self, page, sentence_hash):
        """(others, total): pages OTHER than `page` carrying the masked sentence, and total incl. page."""
        mine = sentence_hash in {s[0] for s in page.sentences}
        in_u = page.id in self.by_id
        others = self.sent_df.get(sentence_hash, 0) - (1 if (in_u and mine) else 0)
        return others, others + (1 if mine else 0)

    def template_ratio(self, page):
        min_pages = self.policy["boilerplate"]["template_sentence_min_pages"]
        total = tmpl = 0
        for h, n, _ in page.sentences:
            total += n
            if self.sentence_occurrences(page, h)[1] >= min_pages:
                tmpl += n
        return (tmpl / total) if total else 0.0

    # --- B. structure
    def skeleton_match(self, page):
        """(shared_count, best_ratio): how many OTHER pages share the skeleton exactly, and the best
        near-identical ratio against the most common skeletons (excluding an exact self-only match)."""
        if not page.skeleton:
            return 0, 0.0
        own = 1 if page.id in self.by_id else 0
        exact_others = self.skeleton_count.get(page.skeleton, 0) - own
        if exact_others > 0:
            return exact_others, 1.0
        best, best_n = 0.0, 0
        for sk in self.top_skeletons:
            if sk == page.skeleton:
                continue
            r = difflib.SequenceMatcher(None, page.skeleton, sk).ratio()
            if r > best:
                best, best_n = r, self.skeleton_count[sk]
        return (best_n if best >= self.policy["structure"]["near_identical_sequence_ratio"] else 0), best

    # --- A. exhaustive exact nearest neighbour (publication candidates)
    def nearest(self, page, exclude_ids=()):
        oc_min = self.policy["text_similarity"]["overlap_coefficient_min_shingles"]
        best = (-1.0, 0.0, None, None)
        excl = set(exclude_ids) | {page.id}
        for h, members in self.groups.items():
            other = [m for m in members if self.pages[m].id not in excl]
            if not other:
                continue
            q = self.pages[other[0]]
            s, j, oc = similarity(page.shingle_set, q.shingle_set, oc_min)
            if s > best[0]:
                best = (s, j, oc, q.id)
        return {"similarity": round(max(best[0], 0.0), 4), "jaccard": round(best[1], 4),
                "overlap_coefficient": None if best[2] is None else round(best[2], 4),
                "closest_page": best[3]}

    # --- A. corpus-wide LSH (audit)
    def audit_pairs(self):
        """Candidate discovery over distinct entity-masked bodies.

        MinHash/LSH proposes candidates; exact Jaccard/overlap confirms them. When the number of
        distinct bodies is small enough, every pair is also confirmed exhaustively and the LSH
        recall is reported (the exhaustive set is then authoritative).
        Returns (confirmed [(i, j, S, J, OC)], stats dict).
        """
        ts = self.policy["text_similarity"]
        oc_min = ts["overlap_coefficient_min_shingles"]
        mh = MinHasher(ts["minhash_permutations"])
        sigs = {}
        for r in self.reps:
            sig = mh.signature(self.pages[r].shingle_set)
            if sig is not None:
                sigs[r] = sig
        cands = lsh_candidates(sigs, ts["lsh_bands"], ts["lsh_rows"])

        def confirm(pairs):
            out = []
            for i, j in pairs:
                s_, jac, oc = similarity(self.pages[i].shingle_set, self.pages[j].shingle_set, oc_min)
                if s_ >= 0.30:
                    out.append((i, j, s_, jac, oc))
            return out

        lsh_conf = confirm(cands)
        stats = {"method": "minhash_lsh", "distinct_bodies": len(self.reps), "lsh_candidate_pairs": len(cands)}
        if len(self.reps) <= ts["exhaustive_confirmation_max_representatives"]:
            reps = sorted(self.reps)
            all_pairs = [(reps[x], reps[y]) for x in range(len(reps)) for y in range(x + 1, len(reps))]
            exh = confirm(all_pairs)
            found = {(i, j) for i, j, *_ in lsh_conf}
            for lo in (ts["review_at_or_above"], ts["fail_at_or_above"]):
                truth = [(i, j) for i, j, s_, *_ in exh if s_ >= lo]
                key = "lsh_recall_ge_" + str(lo).replace(".", "_")
                stats[key] = round(sum(1 for t in truth if t in found) / len(truth), 4) if truth else None
            stats["method"] = "minhash_lsh + exhaustive exact confirmation over distinct bodies"
            stats["exhaustive_pairs"] = len(all_pairs)
            return exh, stats
        return lsh_conf, stats


# --------------------------------------------------------------------------- Information Gain

class IGContext:
    """Governed evidence/claim/audience lookups for IG-unit validation."""

    def __init__(self, registry_path=IG_REGISTRY_PATH):
        self.registry = load_json(registry_path) if os.path.exists(registry_path) else {"pages": []}
        self.evidence = {}
        for f in glob.glob(os.path.join(DATA, "evidence", "*.json")):
            if os.path.basename(f) in ("evidence_schema.json",):
                continue
            try:
                d = load_json(f)
            except ValueError:
                continue
            if isinstance(d, dict) and d.get("evidence_id"):
                self.evidence[d["evidence_id"]] = d
        self.claims = {}
        for f in sorted(glob.glob(os.path.join(DATA, "pilots", "*claims.json")) +
                        glob.glob(os.path.join(DATA, "claims", "*.json"))):
            d = load_json(f)
            for c in (d.get("claims") or []) if isinstance(d, dict) else []:
                if isinstance(c, dict) and c.get("claim_id"):
                    ev = set(c.get("supporting_evidence_ids") or [])
                    for comp in (c.get("components") or {}).values():
                        if isinstance(comp, dict):
                            ev |= set(comp.get("supporting_evidence_ids") or [])
                    self.claims[c["claim_id"]] = ev
        aud = load_json(os.path.join(DATA, "audience_layer_registry.json"))
        self.audiences = {a["audience_id"] for a in aud.get("audiences", [])}
        self.by_page = {e["page"]: e for e in self.registry.get("pages", [])}

    def entry(self, page_id):
        return self.by_page.get(page_id)


def _unit_key(u):
    return (u.get("claim_id") or "", tuple(sorted(u.get("evidence_ids") or [])))


def evaluate_ig(page, universe, policy, ctx, all_unit_statements=None):
    """Validate the page's registered IG units. Returns a dict with valid count + per-unit reasons."""
    igp = policy["information_gain"]
    entry = ctx.entry(page.id)
    result = {"registered_units": 0, "valid_units": 0, "required": igp["min_valid_units"],
              "status": "FAIL", "units": [], "localization_of": None}
    if not entry:
        result["reason"] = "no governed IG units registered for this page"
        return result
    result["localization_of"] = entry.get("localization_of")
    units = entry.get("units") or []
    result["registered_units"] = len(units)
    oc_min = policy["text_similarity"]["overlap_coefficient_min_shingles"]
    fail_at = policy["text_similarity"]["fail_at_or_above"]
    min_pages = policy["boilerplate"]["template_sentence_min_pages"]
    rules = _Rules(policy)
    body3 = shingles(tokens(normalize_text(page.substantive_text)), 3)
    # Keys owned by other (non-localization) registry pages.
    foreign_keys = defaultdict(set)
    for e in ctx.registry.get("pages", []):
        if e["page"] == page.id:
            continue
        related = e.get("localization_of") == page.id or entry.get("localization_of") == e["page"]
        if related:
            continue
        for u in e.get("units") or []:
            foreign_keys[_unit_key(u)].add(e["page"])
    seen_keys = set()
    for u in units:
        reasons = []
        # A multi-concept reference (e.g. a terminology boundary page) declares entity_ids; each unit
        # must still be specific to ONE of them, and its evidence must be about that same concept.
        page_ents = entry.get("entity_ids") or [entry.get("entity_id")]
        ent = u.get("entity_id")
        if ent not in page_ents:
            reasons.append("not page-specific: unit entity_id differs from page entity_id")
        evs = u.get("evidence_ids") or []
        if not evs:
            reasons.append("unsourced: no evidence_ids")
        for eid in evs:
            e = ctx.evidence.get(eid)
            if not e:
                reasons.append(f"unsourced: evidence {eid} does not exist")
                continue
            if not e.get("governed") or e.get("test_fixture"):
                reasons.append(f"evidence {eid} is not governed (or is a test fixture)")
            if e.get("evidence_review_posture") != "evidence_verified":
                reasons.append(f"evidence {eid} is not evidence_verified")
            if ent not in (e.get("concept_ids") or []):
                reasons.append(f"not page-specific: evidence {eid} is not about {ent}")
        cid = u.get("claim_id")
        dim = u.get("dimension")
        if cid:
            if cid not in ctx.claims:
                reasons.append(f"claim {cid} does not exist in any governed claim set")
            else:
                for eid in evs:
                    e = ctx.evidence.get(eid) or {}
                    if eid not in ctx.claims[cid] and e.get("claim_id") != cid:
                        reasons.append(f"evidence {eid} does not support claim {cid}")
        else:
            if dim not in igp["claimless_boundary_dimensions"]:
                reasons.append("claim-less unit allowed only for boundary dimensions")
            for eid in evs:
                if (ctx.evidence.get(eid) or {}).get("claim_id"):
                    reasons.append(f"claim-less boundary unit must use claim-free boundary evidence ({eid} names a claim)")
        if dim not in igp["dimensions"]:
            reasons.append(f"dimension '{dim}' is not a governed IG dimension")
        auds = u.get("audience_ids") or []
        if not auds or any(a not in ctx.audiences for a in auds):
            reasons.append("useful-to-audience not established: audience_ids missing or ungoverned")
        stmt = u.get("statement") or ""
        if rules.infra_line(stmt):
            reasons.append("boilerplate: statement matches an infrastructure pattern")
        pindex = phrase_index(page.entity_phrases)
        st_sents = masked_sentences(stmt, pindex)
        stoks = [t for x in st_sents for t in x]
        sent_hashes = [h64(" ".join(x)) for x in st_sents if len(x) >= policy["boilerplate"]["sentence_min_tokens"]]
        for sh in sent_hashes:
            others, total = universe.sentence_occurrences(page, sh)
            if total >= min_pages:
                reasons.append("boilerplate: statement sentence recurs as template prose across the corpus")
                break
            if others >= 1:
                reasons.append("entity substitution: the entity-masked statement occurs on another page")
                break
        if all_unit_statements:
            ush = shingles(stoks, policy["text_similarity"]["shingle_size"])
            for other_pid, other_set in all_unit_statements:
                if other_pid == page.id or other_pid == entry.get("localization_of"):
                    continue
                if similarity(ush, other_set, oc_min)[0] >= fail_at:
                    reasons.append(f"entity substitution: statement near-matches a unit of {other_pid}")
                    break
        st3 = shingles(tokens(normalize_text(stmt)), 3)
        contain = (len(st3 & body3) / len(st3)) if st3 else 0.0
        if contain < igp["rendered_min_containment"]:
            reasons.append(f"not rendered: statement not present in the substantive body (containment {contain:.2f})")
        key = _unit_key(u)
        if key in seen_keys:
            reasons.append("duplicate unit: same (claim, evidence) key already counted on this page")
        if key in foreign_keys and not entry.get("localization_of"):
            reasons.append("cross-page duplicate: the same governed (claim, evidence) key is owned by "
                           + ", ".join(sorted(foreign_keys[key])))
        valid = not reasons
        if valid:
            seen_keys.add(key)
        result["units"].append({"unit_id": u.get("unit_id"), "dimension": dim, "valid": valid, "reasons": reasons})
    result["valid_units"] = sum(1 for x in result["units"] if x["valid"])
    if entry.get("localization_of"):
        result["status"] = "LOCALIZATION"
        result["reason"] = ("declared localization: knowledge units are inherited from "
                            f"{entry['localization_of']} and do not create distinctiveness; Gate 11 governs language integrity")
    else:
        result["status"] = "PASS" if result["valid_units"] >= igp["min_valid_units"] else "FAIL"
    return result


def unit_statement_index(ctx, policy, pages_by_id):
    out = []
    for e in ctx.registry.get("pages", []):
        p = pages_by_id.get(e["page"])
        phrases = p.entity_phrases if p else []
        for u in e.get("units") or []:
            st = mask_entities(u.get("statement") or "", phrases).split()
            out.append((e["page"], shingles(st, policy["text_similarity"]["shingle_size"])))
    return out


# --------------------------------------------------------------------------- Gate 12 verdict

def classify_similarity(s, policy):
    """Pairwise textual component only: FAIL (>= fail bound), REVIEW (review band), else PASS_TEXT_ONLY.
    PASS_TEXT_ONLY never passes Gate 12 by itself."""
    ts = policy["text_similarity"]
    if s >= ts["fail_at_or_above"]:
        return "FAIL"
    if s >= ts["review_at_or_above"]:
        return "REVIEW"
    return "PASS_TEXT_ONLY"


def gate12_verdict(page, universe, policy, ctx, text=None, unit_index=None, exclude_ids=(), institutional=None):
    """Full Gate-12 evaluation of one page against a universe.

    text: precomputed text-similarity dict (audit mode); None => exhaustive exact nearest().
    institutional: Gate 12-I binding from institutional_lookup() for a registered non-factual
      institutional surface. It replaces ONLY the Information-Gain requirement with a closed,
      singleton function check; text, template, structure and thin-body rules are unchanged.
    """
    ts, bp, st = policy["text_similarity"], policy["boilerplate"], policy["structure"]
    failures, reviews = [], []
    if text is None:
        text = universe.nearest(page, exclude_ids=exclude_ids)
    s = text["similarity"]
    text_status = classify_similarity(s, policy)
    if text_status == "FAIL":
        failures.append(f"near_duplicate: S={s:.3f} >= {ts['fail_at_or_above']} vs {text['closest_page']}")
    elif text_status == "REVIEW":
        reviews.append(f"similarity_review_band: S={s:.3f} vs {text['closest_page']}")

    n_tok = len(page.masked_tokens)
    if n_tok < policy["thin_body"]["min_substantive_tokens"]:
        failures.append(f"thin_body: {n_tok} substantive tokens < {policy['thin_body']['min_substantive_tokens']}")

    tr = universe.template_ratio(page)
    if tr >= bp["fail_at_or_above"]:
        failures.append(f"template_prose: template_sentence_ratio={tr:.3f} >= {bp['fail_at_or_above']}")
    elif tr >= bp["review_at_or_above"]:
        reviews.append(f"template_prose_review: template_sentence_ratio={tr:.3f}")

    shared, ratio = universe.skeleton_match(page)
    structural_template = shared > 0 and (tr >= st["structural_template_prose_min"] or s >= ts["review_at_or_above"])
    if structural_template:
        failures.append(f"structural_template: substantive skeleton shared with {shared} other page(s) "
                        f"(sequence ratio {ratio:.2f}) with template prose/similarity")

    if institutional is not None:
        ig = {"status": "NOT_REQUIRED_INSTITUTIONAL", "registered_units": 0, "valid_units": 0, "required": 0,
              "units": [], "localization_of": None, "institutional_function": institutional["function"],
              "reason": "Gate 12-I: registered institutional surface; IG units replaced by a closed singleton function check"}
        if not institutional["singleton"]:
            failures.append(f"institutional_duplicate_function: function '{institutional['function']}' "
                            f"({institutional['language']}) is already served by {', '.join(institutional['others'])}")
    else:
        ig = evaluate_ig(page, universe, policy, ctx, unit_index)
        if ig["status"] == "FAIL":
            failures.append(f"information_gain: {ig['valid_units']} valid unit(s) < {ig['required']}")

    # Entity substitution diagnostic: masked identical/near but raw text differs.
    entity_sub = False
    if text.get("closest_page") and s >= ts["fail_at_or_above"]:
        other = universe.by_id.get(text["closest_page"])
        if other is not None:
            raw_s = similarity(page.raw_shingle_set, other.raw_shingle_set, ts["overlap_coefficient_min_shingles"])[0]
            entity_sub = raw_s < s - 1e-9

    if ig["status"] == "LOCALIZATION":
        verdict = "LOCALIZATION"
    elif failures:
        verdict = "FAIL"
    elif reviews:
        verdict = "REVIEW"
    else:
        verdict = "PASS"
    return {
        "page": page.id, "surface": page.surface, "route_id": page.route_id, "language": page.language,
        "family": page.family, "ko_family": page.ko_family, "is_draft": page.is_draft,
        "publication_candidate": page.publication_candidate, "public_indexable": page.public_indexable,
        "verdict": verdict, "failures": failures, "reviews": reviews,
        "text": dict(text, status=text_status),
        "entity_substitution_detected": entity_sub,
        "structure": {"skeleton": list(page.skeleton), "shared_with_pages": shared, "best_sequence_ratio": round(ratio, 3),
                      "structural_template": structural_template},
        "boilerplate": {"template_sentence_ratio": round(tr, 4)},
        "substantive_tokens": n_tok, "infra_tokens": page.infra_tokens,
        "information_gain": ig,
        "page_class": "institutional" if institutional is not None else "knowledge_reference",
        "gate12_blocks_publication": verdict != "PASS",
    }


def combined_publication_eligibility(gate12, contract_c_inputs):
    """Publication contract: Contract C AND Gate 12. Neither overrides the other.

    contract_c_inputs: dict of contract_c_derive.derive kwargs, or None (unknown => fail closed).
    Returns {publication_state, indexation_state, contract_c, gate12_verdict, eligible, reasons}.
    """
    sys.path.insert(0, os.path.join(ROOT, "scripts", "governance_scaffolding"))
    import contract_c_derive  # noqa: E402  (canonical Contract-C; never modified here)
    reasons = []
    if contract_c_inputs is None:
        cc = ("not_public", "noindex")
        reasons.append("Contract C inputs unknown: fail-closed (not_public, noindex)")
    else:
        cc = contract_c_derive.derive(**contract_c_inputs)
    verdict = gate12 if isinstance(gate12, str) else gate12["verdict"]
    if verdict != "PASS":
        reasons.append(f"Gate 12 verdict {verdict}: publication and indexation prohibited")
        out = ("not_public", "noindex")
    else:
        out = cc
        if cc == ("not_public", "noindex"):
            reasons.append("Contract C denies publication (Gate 12 cannot override)")
    return {"publication_state": out[0], "indexation_state": out[1], "contract_c": list(cc),
            "gate12_verdict": verdict, "eligible": out[0] != "not_public", "reasons": reasons}


# --------------------------------------------------------------------------- Gate 12-I (institutional)

INSTITUTIONAL_REGISTRY_PATH = os.path.join(DATA, "distinctiveness", "institutional_surface_registry.json")


class InstitutionalRegistry:
    """Closed registry of non-factual institutional surfaces (home, methodology, policy, navigation).

    Each binding names ONE function from a closed vocabulary; a function may be served by exactly one
    surface per language. Pages not bound here are knowledge references (full IG requirement)."""

    def __init__(self, path=INSTITUTIONAL_REGISTRY_PATH):
        self.data = load_json(path) if os.path.exists(path) else {"functions": [], "bindings": []}
        self.functions = {f["function_id"] for f in self.data.get("functions", [])}
        self.by_route = {}
        self.by_path = {}
        seen = defaultdict(list)
        for b in self.data.get("bindings", []):
            key = b.get("route_id") or b.get("path")
            seen[(b["function_id"], b["language"])].append(key)
            if b.get("route_id"):
                self.by_route[b["route_id"]] = b
            if b.get("path"):
                self.by_path[b["path"]] = b
        self.function_holders = seen

    def lookup(self, route_id=None, path=None):
        b = (self.by_route.get(route_id) if route_id else None) or (self.by_path.get(path) if path else None)
        if not b or b["function_id"] not in self.functions:
            return None
        holders = self.function_holders[(b["function_id"], b["language"])]
        key = b.get("route_id") or b.get("path")
        return {"function": b["function_id"], "language": b["language"], "binding": key,
                "singleton": holders[0] == key, "others": [h for h in holders if h != key]}


# --------------------------------------------------------------------------- legacy hold (Contract C RL)

LEGACY_HOLD_PATH = os.path.join(DATA, "distinctiveness", "legacy_surface_hold.json")


def body_hash_hex(page):
    return format(page.body_hash, "016x")


def surface_url_path(page, surface_root):
    rel_dir = os.path.dirname(os.path.relpath(page.id if os.path.isabs(page.id) else os.path.join(ROOT, page.id),
                                              surface_root))
    return "/" if rel_dir in ("", ".") else "/" + rel_dir.replace(os.sep, "/").strip("/") + "/"


def sitemap_paths(surface_root):
    """URL paths listed in any sitemap*.xml at the surface root (an indexation request)."""
    out = set()
    for f in glob.glob(os.path.join(surface_root, "sitemap*.xml")):
        with open(f, encoding="utf-8", errors="replace") as fh:
            for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", fh.read()):
                if loc.endswith(".xml"):
                    continue
                path = re.sub(r"^https?://[^/]+", "", loc) or "/"
                out.add(path if path.endswith("/") else path + "/")
    return out


def hold_entries_digest(entries):
    """sha256 over path, body hash and (when recorded) the served directives, so neither the body pin
    nor the recorded robots/sitemap/canonical status quo can be edited without re-sealing."""
    canon = "\n".join("\t".join([e["p"], e["h"]] + [str(e[k]) for k in ("robots", "sm", "c") if k in e])
                      for e in sorted(entries, key=lambda e: e["p"]))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def verify_hold(hold):
    """Integrity of the sealed baseline: count + digest + no duplicate paths."""
    errs = []
    entries = hold.get("entries", [])
    if len({e["p"] for e in entries}) != len(entries):
        errs.append("duplicate paths in legacy hold")
    if hold.get("entry_count") != len(entries):
        errs.append(f"entry_count {hold.get('entry_count')} != {len(entries)} entries")
    if hold.get("entries_sha256") != hold_entries_digest(entries):
        errs.append("entries_sha256 does not match the entries (baseline edited without re-sealing)")
    return errs


def freeze_exception_status(hold, policy, today):
    """Is the indexed-legacy freeze exception active? Returns (active, reason). Default: not active."""
    import datetime
    if policy["legacy_migration"]["freeze_exception"].get("status") == "retired":
        return False, ("freeze exception retired (Recovery-02): an unchanged legacy surface is governed by the "
                       "publication-authority status quo instead")
    fe = hold.get("freeze_exception") or {}
    if fe.get("state") != "authorized":
        return False, "freeze exception not authorized (default): legacy pages that fail Gate 12 must be noindex (Contract C RL)"
    missing = [k for k in ("authorized_by", "authorized_on", "expires_on", "reason") if not fe.get(k)]
    if missing:
        return False, f"freeze exception incomplete: missing {missing}"
    try:
        start = datetime.date.fromisoformat(fe["authorized_on"])
        end = datetime.date.fromisoformat(fe["expires_on"])
    except ValueError:
        return False, "freeze exception dates are not ISO dates"
    max_days = policy["legacy_migration"]["freeze_exception"]["max_days"]
    if (end - start).days > max_days or end < start:
        return False, f"freeze exception window exceeds the policy maximum of {max_days} days"
    if today > end:
        return False, f"freeze exception expired on {fe['expires_on']}"
    return True, f"freeze exception authorized by {fe['authorized_by']} until {fe['expires_on']} (Contract C deviation, reported)"


def apply_legacy_hold(pages, verdicts, surface_root, hold, policy, today, sitemap=None):
    """Classify every page of a surface under the bounded legacy-migration rule.

    PASS                      Gate 12 PASS.
    LEGACY_HOLD_NOINDEX       fails Gate 12, is in the sealed baseline with an unchanged substantive body,
                              and requests no indexation (robots noindex AND absent from sitemaps):
                              Contract C RL (legacy_public_holding -> public_noindex, noindex).
    LEGACY_FREEZE_INDEXED     same, but still indexable, under an authorized, unexpired freeze exception
                              (an explicit, reported Contract-C deviation; default not authorized).
    BLOCK_LEGACY_INDEXED      baseline page that fails Gate 12 and still requests indexation.
    BLOCK_MODIFIED_LEGACY     baseline page whose substantive body changed and that does not pass Gate 12.
    BLOCK_NEW_FAILING         page absent from the baseline that does not pass Gate 12.
    """
    sitemap = sitemap if sitemap is not None else sitemap_paths(surface_root)
    entries = {e["p"]: e for e in (hold or {}).get("entries", []) if e.get("g", "FAIL") != "PASS"}
    fe_active, fe_reason = freeze_exception_status(hold or {}, policy, today) if hold else (False, "no legacy hold supplied")
    out = []
    for page, v in zip(pages, verdicts):
        path = surface_url_path(page, surface_root)
        requests_index = page.public_indexable or path in sitemap
        e = entries.get(path)
        unchanged = bool(e) and e["h"] == body_hash_hex(page)
        if v["verdict"] == "PASS":
            state = "PASS"
        elif e and not unchanged:
            state = "BLOCK_MODIFIED_LEGACY"
        elif not e:
            state = "BLOCK_NEW_FAILING"
        elif not requests_index:
            state = "LEGACY_HOLD_NOINDEX"
        elif fe_active:
            state = "LEGACY_FREEZE_INDEXED"
        else:
            state = "BLOCK_LEGACY_INDEXED"
        out.append({"path": path, "page": page.id, "state": state, "requests_indexation": requests_index,
                    "robots_index": page.public_indexable, "in_sitemap": path in sitemap,
                    "gate12_verdict": v["verdict"], "in_baseline": bool(e), "body_unchanged": unchanged})
    present = {o["path"] for o in out}
    passing = {o["path"] for o in out if o["state"] == "PASS"}
    stale = sorted(p for p in entries if p not in present or p in passing)
    return out, {"freeze_exception_active": fe_active, "freeze_exception": fe_reason,
                 "stale_baseline_entries": stale}


def hold_ratchet(new_hold, old_hold):
    """The baseline may only shrink: every (path, hash) in the new hold must exist in the old hold."""
    errs = []
    old = {(e["p"], e["h"]) for e in old_hold.get("entries", [])}
    added = [e["p"] for e in new_hold.get("entries", []) if (e["p"], e["h"]) not in old]
    if added:
        errs.append(f"{len(added)} baseline entr(y/ies) added or re-pinned (ratchet violation), e.g. {added[:3]}")
    return errs, {"old_count": len(old), "new_count": len(new_hold.get("entries", [])),
                  "removed": len(old) - (len(new_hold.get("entries", [])) - len(added))}
