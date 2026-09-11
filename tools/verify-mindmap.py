#!/usr/bin/env python3
"""Verify a generated or published standalone mind map.

Usage:
  python3 tools/verify-mindmap.py [module|all]

`module` is a module folder name (or a pinned alias, e.g. `cn`); default `all`
checks every discovered module. It reuses the discovery logic from
build-mindmap.py. While source pages are present, it cross-checks every
question, box, subtopic, section, q-id, title, diagram, table, formula and
MathJax delimiter against the
exact source slice embedded by the builder. After publication, when the source
index is absent, it checks stable node anchors, embedded audit counts, link
closure, SVG-ID namespacing, structure and delimiter balance. It is CI-safe in
both states.

The per-file quality gate for remaining HTML is tools/verify-math.py — run both.
"""
import importlib.util, os, re, sys, html as H
from html.parser import HTMLParser

TOOLS = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('mmbuild', os.path.join(TOOLS, 'build-mindmap.py'))
mmb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mmb)

B = chr(92)  # backslash

def check_module(folder):
    cfg = mmb.module_config(folder)
    base = cfg['base']
    s = mmb.read(cfg['out'])
    srcs = [f for _, f, _ in cfg['nodes']]
    def retained(f):
        """Exactly what the builder embeds from file f: banner + kept cards,
        where each card keeps its first child as flattened title text and all
        other children verbatim. Source pages use element children for content;
        only formatting whitespace between those elements is dropped."""
        banner, cards = mmb.page_parts(mmb.read(os.path.join(base, f)))
        if f == 'index.html' and cfg['skip']:
            cards = [c for c in cards if cfg['skip'] not in c]
        pieces, ctitles = [banner or ''], []
        for c in cards:
            try:
                kids = mmb.direct_children(mmb.strip_outer(c, 'div'))
            except ValueError:
                pieces.append(c)
                continue
            if kids:
                # Mirror render_section: remove only an h2 title when present;
                # h2-less supplement cards keep every child, including a first
                # technique box.
                h2_index = next((i for i, (_, name, _) in enumerate(kids)
                                 if name == 'h2'), None)
                if h2_index is not None:
                    h2 = kids[h2_index][0]
                    rest = re.sub(r'<span class="q-meta">.*?</span>', '', h2, flags=re.S)
                    rest = re.sub(r'<span class="no">.*?</span>', '', rest, flags=re.S)
                    ctitles.append(mmb.text_of(rest))
                    body_kids = [h for i, (h, _, _) in enumerate(kids)
                                 if i != h2_index]
                    pieces.append(mmb.text_of(h2) + ''.join(body_kids))
                else:
                    pieces.append(''.join(h for h, _, _ in kids))
        return ''.join(pieces), len(cards), ctitles

    n_sec = 0
    parts = {}
    titles = []
    for f in srcs:
        t, n_cards, ctitles = retained(f)
        parts[f] = t
        titles += ctitles
        n_sec += n_cards

    def tot(files, pat):
        return sum(len(re.findall(pat, parts[f])) for f in files)

    bad = []
    def report(label, ok, msg):
        print(f'  {label:<11} {"OK " if ok else "FAIL"} {msg}')
        if not ok:
            bad.append(label)

    # --- math delimiters: every \( \) of the embedded slices is in the mind map
    #     (counted as literal two-char sequences on both sides — str.count, not
    #     regex; the mind map body starts at <body>, its <head> only carries the
    #     copied MathJax config and CSS, no math of its own)
    body = s[s.find('<body>'):]
    so, sc = body.count(B + '('), body.count(B + ')')
    want = sum(parts[f].count(B + '(') for f in srcs)
    report('math delims', so == sc == want, f'(src \\(={want} out \\(={so} \\)={sc})')

    # --- every q div of the retained slices is in the mind map (details or raw)
    dq = len(re.findall(r'<(?:details|div) class="q[ "]', s))
    want_q = tot(srcs, r'<div class="q[ "]')
    report('q nodes', dq == want_q, f'nodes={dq} src={want_q}')

    # --- boxes likewise (nested boxes stay raw divs by design — still counted)
    db = len(re.findall(r'<(?:details|div) class="box[ "]', s))
    want_b = tot(srcs, r'<div class="box[ "]')
    report('box nodes', db == want_b, f'nodes={db} src={want_b}')

    # --- each <h3> became one mm-sub wrapper; no raw h3 remain
    n_sub, n_h3 = s.count('<details class="mm-sub"'), tot(srcs, '<h3')
    report('sub nodes', n_sub == n_h3 and s.count('<h3') == 0,
           f'mm-sub={n_sub} src h3={n_h3}')

    # --- each kept card became one mm-sec section
    n_ms = s.count('<details class="mm-sec')
    report('sec nodes', n_ms == n_sec and s.count('<div class="card') == 0,
           f'mm-sec={n_ms} src cards={n_sec}')

    # --- interactive content preserved verbatim. Figures use both the older
    # div.figure convention and the newer semantic figure.fig convention.
    figure_re = r'<div class="figure"(?:\s|>)|<figure\b'
    checks = [
        ('answers', s.count('<details class="ans"'),
         tot(srcs, re.escape('<details class="ans"'))),
        ('figures', len(re.findall(figure_re, s)),
         sum(len(re.findall(figure_re, parts[f])) for f in srcs)),
        ('tables', s.count('<table class="data">'),
         tot(srcs, re.escape('<table class="data">'))),
        ('formulas', s.count('<div class="formula">'),
         tot(srcs, re.escape('<div class="formula">'))),
    ]
    for label, out_count, src_count in checks:
        report(label, out_count == src_count,
               f'out={out_count} src={src_count}')

    # --- every q-id of the sources appears in the mind map summaries
    qids = []
    for f in srcs:
        qids += re.findall(r'class="q-id">([^<]+)<', parts[f])
    s_plain = H.unescape(s)
    missing = sorted(set(q for q in qids if f'>{q}</span>' not in s_plain))
    report('q-ids', not missing, f'src={len(qids)} unique={len(set(qids))} missing={missing[:8]}')

    # --- every card title (h2 with the builder's no/q-meta spans stripped) survives
    s_norm = re.sub(r'\s+', ' ', s_plain)
    miss = [t for t in titles if t and t not in s_norm]
    report('h2 titles', not miss, f'src={len(titles)} missing={miss[:8]}')

    # --- structural sanity of the generated file itself
    class Checker(HTMLParser):
        VOID = {'meta', 'link', 'br', 'img', 'hr', 'input', 'circle', 'rect', 'line',
                'polyline', 'path', 'text', 'ellipse', 'polygon', 'use', 'stop'}
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stack = []
            self.errors = []
        def handle_starttag(self, tag, attrs):
            if tag not in self.VOID:
                self.stack.append((tag, self.getpos()))
        def handle_endtag(self, tag):
            if tag in self.VOID:
                return
            if not self.stack:
                self.errors.append(f'unexpected </{tag}> at {self.getpos()}')
                return
            if self.stack[-1][0] != tag:
                names = [t for t, _ in self.stack]
                if tag in names:
                    while self.stack and self.stack[-1][0] != tag:
                        t, p = self.stack.pop()
                        self.errors.append(f'unclosed <{t}> at {p}')
                    self.stack.pop()
                else:
                    self.errors.append(f'stray </{tag}> at {self.getpos()}')
            else:
                self.stack.pop()

    c = Checker()
    c.feed(s)
    leftover = [(t, p) for t, p in c.stack if t not in ('html', 'body')]
    report('tag balance', not c.errors and not leftover,
           'OK' if not c.errors and not leftover else f'{c.errors[:4]} {leftover[:4]}')

    depth, neg, i = 0, False, 0
    while i < len(s) - 1:
        if s[i] == B and s[i + 1] == '(':
            depth += 1; i += 2; continue
        if s[i] == B and s[i + 1] == ')':
            depth -= 1
            neg = neg or depth < 0
            depth = max(0, depth); i += 2; continue
        i += 1
    report('math walk', depth == 0 and not neg, 'OK' if depth == 0 and not neg else f'depth={depth} neg={neg}')

    print(f'[{folder}] {os.path.relpath(cfg["out"], mmb.ROOT)} -> {"PASS" if not bad else "FAIL: " + ", ".join(bad)}')
    return not bad

def check_standalone(folder):
    """Quality-check a published map after its source HTML has been removed."""
    fn = mmb.standalone_map(folder)
    s = mmb.read(fn)
    bad = []

    def report(label, ok, msg):
        print(f'  {label:<11} {"OK " if ok else "FAIL"} {msg}')
        if not ok:
            bad.append(label)

    expected = ['course-map'] + [f'chapter-{n}' for n in range(1, 7)] \
               + ['olympiad-paper', 'solutions']
    ids = re.findall(r'<details id="([^"]+)" class="mm-ch', s)
    report('top nodes', ids == expected, f'found={ids}')
    hero_count = s.count('<div class="banner mm-banner">')
    q_count = len(re.findall(r'<details class="q(?: |")', s))
    answer_count = s.count('<details class="ans">')
    paper_answer_count = s.count('class="answer-pill"')
    figure_count = len(re.findall(r'<div class="figure"(?:\s|>)|<figure\b', s))
    table_count = s.count('<table')
    formula_count = s.count('<div class="formula"')
    section_count = len(re.findall(r'<details class="mm-sec(?: |")', s))
    subtopic_count = len(re.findall(r'<details class="mm-sub(?: |")', s))
    report('heroes', hero_count == len(expected),
           f'count={hero_count} expected={len(expected)}')
    report('q nodes', q_count > 0, f'nodes={q_count}')
    report('answers', answer_count > 0 and paper_answer_count > 0,
           f'details={answer_count} paper-pills={paper_answer_count}')
    report('visuals', figure_count > 0 and formula_count > 0,
           f'figures={figure_count} tables={table_count} formulas={formula_count}')

    audit = re.search(r'<!-- embedded source audit: ([^>]+) -->', s)
    audit_values = dict(re.findall(r'(\w+)=(\d+)', audit.group(1))) if audit else {}
    actual = {
        'questions': q_count, 'answers': answer_count,
        'paper_answers': paper_answer_count, 'figures': figure_count,
        'tables': table_count, 'formulas': formula_count,
        'sections': section_count, 'subtopics': subtopic_count,
    }
    audit_ok = bool(audit) and all(audit_values.get(k) == str(v)
                                   for k, v in actual.items())
    report('audit counts', audit_ok,
           f'embedded={audit_values} actual={actual}')
    report('no source cards', '<div class="card"' not in s and '<h3' not in s,
           'all cards/subtopics normalized')
    report('box summaries', '<summary class="box-title"><div class="box-title"' not in s,
           'no nested duplicate title blocks')

    # Every link must either target a node in this file or be an external URL.
    hrefs = re.findall(r'href="([^"]+)"', s)
    local = [h for h in hrefs if not re.match(r'^(?:https?:|mailto:|#)', h)]
    fragments = [h[1:] for h in hrefs if h.startswith('#')]
    report('links', not local and all(f in set(ids) for f in fragments),
           f'bad={local[:4] + ["#" + f for f in fragments if f not in set(ids)][:4]}')

    # Concatenated SVGs must not share document-global IDs, and every fragment
    # reference must resolve. This catches the most common combined-map defect:
    # one diagram accidentally borrowing another diagram's arrow marker.
    all_ids = re.findall(r'\bid="([^"]+)"', s)
    counts = {}
    for ident in all_ids:
        counts[ident] = counts.get(ident, 0) + 1
    refs = re.findall(r'(?:url\(#|(?:xlink:)?href="#)([^)" ]+)', s)
    duplicate_ids = sorted(k for k, v in counts.items() if v > 1)
    missing_refs = sorted(set(refs) - set(all_ids))
    report('SVG ids', not duplicate_ids and not missing_refs,
           f'duplicate={duplicate_ids[:4]} missing={missing_refs[:4]}')

    # Structural and delimiter sanity mirrors the repo-wide math gate without
    # requiring the deleted source pages.
    class Checker(HTMLParser):
        VOID = {'meta', 'link', 'br', 'img', 'hr', 'input', 'circle', 'rect', 'line',
                'polyline', 'path', 'text', 'ellipse', 'polygon', 'use', 'stop'}
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stack = []
            self.errors = []
        def handle_starttag(self, tag, attrs):
            if tag not in self.VOID:
                self.stack.append((tag, self.getpos()))
        def handle_endtag(self, tag):
            if tag in self.VOID:
                return
            if not self.stack:
                self.errors.append(f'unexpected </{tag}> at {self.getpos()}')
            elif self.stack[-1][0] != tag:
                self.errors.append(f'mismatch </{tag}> at {self.getpos()} top={self.stack[-1][0]}')
            else:
                self.stack.pop()

    c = Checker(); c.feed(s); c.close()
    report('tag balance', not c.errors and not c.stack,
           'OK' if not c.errors and not c.stack else f'{c.errors[:3]} {c.stack[:3]}')
    body = s[s.find('<body>'):]
    left, right = body.count('\\('), body.count('\\)')
    dollars = body.count('$$')
    report('math delimiters', left == right and dollars % 2 == 0,
           f'inline={left}/{right} dollars={dollars // 2}/bad={dollars % 2}')

    print(f'[{folder}] {os.path.relpath(fn, mmb.ROOT)} -> '
          f'{"PASS" if not bad else "FAIL: " + ", ".join(bad)}')
    return not bad

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    mods = mmb.find_modules()
    if which.lower() == 'all':
        targets = mods
    else:
        aliases = {}
        for k, v in mmb.load_overrides().get('aliases', {}).items():
            aliases[mmb.slug(k)] = v
        want = aliases.get(mmb.slug(which), which)
        targets = [m for m in mods if mmb.slug(m) == mmb.slug(want)]
        if not targets:
            raise SystemExit(f'no module folder matching {which!r}; found: '
                             + (', '.join(mods) if mods else '(none)'))
    ok = True
    for name in targets:
        result = check_standalone(name) if mmb.is_standalone(name) else check_module(name)
        ok = result and ok
    sys.exit(0 if ok else 1)
