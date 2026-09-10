#!/usr/bin/env python3
"""Cross-check a generated mind map against its source pages (completeness).

Usage:
  python3 tools/verify-mindmap.py [module|all]

`module` is a module folder name (or a pinned alias, e.g. `cn`); default `all`
checks every discovered module. Reuses the discovery of build-mindmap.py, then
verifies that the generated `*-mindmap.html` holds every question, box,
subtopic, section, q-id, h2 title and math delimiter that exists in the source
pages (i.e. inside each page's banner + kept cards — the same slice the builder
embeds), and that its tags are balanced. Prints PASS/FAIL per module and exits
non-zero on any failure, so it is CI-safe.

This is a *completeness* check for mind maps only. The per-file quality gate
for every note page is still tools/verify-math.py — run both.
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
    non_idx = [f for f in srcs if f != 'index.html']

    def retained(f):
        """Exactly what the builder embeds from file f: banner + kept cards,
        where each card keeps its first child as flattened title text and all
        other children verbatim (bare text nodes between elements are dropped
        by design). Expected counts are measured against THIS slice, so the
        checks stay honest even though the mind map is not a lossless copy."""
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
                # mirror render_section: first child is the h2 line, flattened
                h2 = kids[0][0]
                rest = re.sub(r'<span class="q-meta">.*?</span>', '', h2, flags=re.S)
                rest = re.sub(r'<span class="no">.*?</span>', '', rest, flags=re.S)
                ctitles.append(mmb.text_of(rest))
                pieces.append(mmb.text_of(h2) + ''.join(h for h, _, _ in kids[1:]))
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

    # --- interactive content preserved verbatim
    for label, pat in (('answers', '<details class="ans"'), ('figures', '<div class="figure">'),
                       ('tables', '<table class="data">'), ('formulas', '<div class="formula">')):
        report(label, s.count(pat) == tot(srcs, re.escape(pat)),
               f'out={s.count(pat)} src={tot(srcs, re.escape(pat))}')

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
        ok = check_module(name) and ok
    sys.exit(0 if ok else 1)
