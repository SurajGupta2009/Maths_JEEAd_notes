#!/usr/bin/env python3
"""Build single-file recursive mind maps from the note pages of a module.

Usage:
  python3 tools/build-mindmap.py <module|all>

  <module>  module folder name — case-insensitive, spaces and hyphens
            interchangeable (`Complex Numbers`, `complex-numbers`, ...);
            CLI aliases (e.g. `cn`) may be pinned in
            tools/mindmap-overrides.json
  all       every module found in the repo

A "module" is any top-level repo folder that contains an index.html.
The mind map node list is auto-discovered from the folder:

  index.html                     -> (house)  Course map, usage & roadmap
  NN-slug.html  (chapter files)  ->    N     Ch N · <chapter <h1> text>
  olympiad-paper.html            ->  (Sigma)  Olympiad Paper · K questions  (K counted)
  olympiad-paper-solutions.html  ->  (pen)    Olympiad Paper · Solutions & marking guide

Exact chapter labels can be pinned per module in tools/mindmap-overrides.json
(this is how the two golden modules keep their hand-tuned labels).

Output file: the module folder's existing `*-mindmap.html` is regenerated in
place (so re-running is idempotent); a brand-new module gets
`<folder-slug>-mindmap.html`, where the slug is the folder name lowercased
with runs of spaces/hyphens collapsed to a single hyphen
(`Quadratic-Equations` -> `quadratic-equations-mindmap.html`).

Never hand-edit a generated mind map — edit the source pages and rebuild.
"""
import json, os, re, sys, html as H

TOOLS = os.path.dirname(os.path.abspath(__file__))          # repo/tools
ROOT = os.path.dirname(TOOLS)                                # repo root
OVERRIDES_PATH = os.path.join(TOOLS, 'mindmap-overrides.json')

def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def slug(name):
    """Normalize a folder/CLI name: lowercase, spaces/hyphens -> single hyphen."""
    return re.sub(r'[\s_-]+', '-', name.strip().lower()).strip('-')

# ---------------------------------------------------------------- discovery

CHAPTER_RE = re.compile(r'^(\d+)-[^/\\]+\.html$')

def find_modules():
    """Every top-level repo folder that contains an index.html."""
    out = []
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if d.startswith('.'):
            continue
        if os.path.isdir(p) and os.path.isfile(os.path.join(p, 'index.html')):
            out.append(d)
    return out

def load_overrides():
    if os.path.exists(OVERRIDES_PATH):
        with open(OVERRIDES_PATH, encoding='utf-8') as f:
            return json.load(f)
    return {}

def module_config(folder):
    """Auto-discover a module folder; optional pins from mindmap-overrides.json."""
    base = os.path.join(ROOT, folder)
    if not os.path.isfile(os.path.join(base, 'index.html')):
        raise SystemExit(f'error: {folder}/ has no index.html — not a module')
    css = os.path.join(base, 'assets', 'notes.css')
    if not os.path.isfile(css):
        raise SystemExit(f'error: {folder}/assets/notes.css missing — copy it from an existing module')

    ov = {}
    for k, v in load_overrides().items():
        if slug(k) == slug(folder):
            ov = v
    labels = ov.get('labels', {})

    chapters = sorted(f for f in os.listdir(base) if CHAPTER_RE.match(f))
    nodes = [('🏠', 'index.html', labels.get('index.html', 'Course map, usage & roadmap'))]
    for f in chapters:
        n = int(CHAPTER_RE.match(f).group(1))
        m = re.search(r'<h1[^>]*>(.*?)</h1>', read(os.path.join(base, f)), re.S)
        fallback = f'Ch {n} · {text_of(m.group(1))}' if m else f'Ch {n} · {f}'
        nodes.append((str(n), f, labels.get(f, fallback)))
    if os.path.isfile(os.path.join(base, 'olympiad-paper.html')):
        nq = len(re.findall(r'<span class="q-id">Q\d+', read(os.path.join(base, 'olympiad-paper.html'))))
        nodes.append(('Σ', 'olympiad-paper.html',
                      labels.get('olympiad-paper.html', f'Olympiad Paper · {nq} questions')))
    if os.path.isfile(os.path.join(base, 'olympiad-paper-solutions.html')):
        nodes.append(('✎', 'olympiad-paper-solutions.html',
                      labels.get('olympiad-paper-solutions.html', 'Olympiad Paper · Solutions & marking guide')))

    existing = [f for f in sorted(os.listdir(base)) if f.endswith('-mindmap.html')]
    derived = slug(folder) + '-mindmap.html'
    out_name = derived if derived in existing else (existing[0] if existing else derived)

    return {
        'base': base,
        'out': os.path.join(base, out_name),
        'css': css,
        'title': ov.get('title', f'{folder} · Complete Course — single-file mind map'),
        'brand': ov.get('brand', f'{folder} · Complete Course'),
        'skip': f'href="{chapters[0]}"' if chapters else None,
        'back': ('index.html', 'index.html'),
        'nodes': nodes,
    }

VOID = {'meta', 'link', 'br', 'img', 'hr', 'input'}
TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:[^>"\'/]|"[^"]*"|\'[^\']*\')*)(/?)>')

def get_class(attrs):
    m = re.search(r'class="([^"]*)"', attrs or '')
    return m.group(1) if m else ''

def text_of(h):
    t = re.sub(r'<[^>]+>', ' ', h)
    t = H.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

def strip_outer(html, tag):
    m = re.match(rf'<{tag}\b[^>]*>(.*)</{tag}>\s*$', html, re.S)
    if not m:
        raise ValueError(f'cannot strip outer <{tag}>: {html[:80]!r}')
    return m.group(1)

def direct_children(s):
    """Split inner html into direct child elements -> [(html, name, attrs)].
    Assumes well-formed html (all note files pass a strict balance check)."""
    out = []
    i, n = 0, len(s)
    while i < n:
        j = s.find('<', i)
        if j == -1:
            break
        if s.startswith('<!--', j):
            k = s.find('-->', j)
            i = (k + 3) if k != -1 else n
            continue
        m = TAG_RE.match(s, j)
        if not m:
            i = j + 1
            continue
        close, name, attrs, selfc = m.groups()
        if close or name in VOID or selfc:
            i = m.end()
            continue
        depth, k = 1, m.end()
        while k < n and depth:
            j2 = s.find('<', k)
            if j2 == -1:
                break
            if s.startswith('<!--', j2):
                k2 = s.find('-->', j2)
                k = (k2 + 3) if k2 != -1 else n
                continue
            m2 = TAG_RE.match(s, j2)
            if not m2:
                k = j2 + 1
                continue
            c2, n2, a2, sc2 = m2.groups()
            if not (n2 in VOID or sc2):
                if c2:
                    depth -= 1
                else:
                    depth += 1
            k = m2.end()
        out.append((s[j:k], name, attrs))
        i = k
    return out

def esc(t):
    return H.escape(t, quote=False)

# ---------------------------------------------------------------- rendering

def _attrs_of(el_html):
    m = re.match(r'<[a-zA-Z][^>]*>', el_html)
    return m.group(0) if m else ''

def render_q(q_html):
    cls = get_class(_attrs_of(q_html))
    inner = strip_outer(q_html, 'div')
    kids = direct_children(inner)
    qhead, body = None, []
    for h, name, attrs in kids:
        if name == 'div' and get_class(attrs).split() == ['q-head']:
            qhead = h
        else:
            body.append(h)
    qid = re.search(r'<span class="q-id">(.*?)</span>', qhead)
    qid = text_of(qid.group(1)) if qid else 'Q'
    badges = re.findall(r'<span class="badge[^"]*">.*?</span>', qhead)
    preview = ''
    for h, name, attrs in kids:  # first content child after q-head?
        if name == 'div' and get_class(attrs).split() == ['q-head']:
            continue
        if name == 'div':
            break  # solution wrapper follows: no problem text to preview
        if name == 'p':
            preview = text_of(h)
            break
    preview = re.sub(r'\\\(.*?\\\)', ' ', preview)   # drop inline math from the hint
    preview = re.sub(r'\\\[.*?\\\]', ' ', preview)   # drop display math too
    preview = re.sub(r'\$\$.*?\$\$', ' ', preview)   # and $$...$$
    preview = re.sub(r'\s+', ' ', preview).strip()
    preview = (preview[:78] + '…') if len(preview) > 78 else preview
    summary = (f'<span class="q-id">{esc(qid)}</span>{"".join(badges)}'
               f'<span class="mm-preview">{esc(preview)}</span>')
    return (f'<details class="{cls} mm-node"><summary class="q-head">{summary}</summary>'
            f'{" ".join(body)}</details>')

def render_box(box_html):
    cls = get_class(_attrs_of(box_html))
    inner = strip_outer(box_html, 'div')
    kids = direct_children(inner)
    title, body = None, []
    for h, name, attrs in kids:
        if name == 'div' and get_class(attrs).split() == ['box-title']:
            title = h
        else:
            body.append(h)
    return (f'<details class="{cls} mm-node">'
            f'<summary class="box-title">{title}</summary>'
            f'{" ".join(body)}</details>')

def render_section(card_html):
    inner = strip_outer(card_html, 'div')
    kids = direct_children(inner)
    h2 = kids[0][0]
    m = re.search(r'<span class="no">(.*?)</span>', h2)
    no = m.group(1) if m else ''
    rest = re.sub(r'<span class="no">.*?</span>', '', h2, flags=re.S)
    rest = re.sub(r'<span class="q-meta">.*?</span>', '', rest, flags=re.S)
    title = text_of(rest)
    qm = re.search(r'<span class="q-meta">(.*?)</span>', h2)
    meta_bits = []
    if qm:
        meta_bits.append(text_of(qm.group(1)))

    items, current, current_title = [], [], None
    def flush():
        nonlocal current, current_title
        if current_title is None:
            if any(x.strip() for x in current):
                items.append(''.join(current))
        else:
            items.append(
                f'<details class="mm-sub"><summary class="mm-sum2">{current_title}</summary>'
                f'<div class="mm-body">{" ".join(current)}</div></details>')
        current, current_title = [], None

    for h, name, attrs in kids[1:]:
        cls = get_class(attrs).split()
        if name == 'h3':
            flush()
            current_title = h[3:-4]
        elif name == 'div' and cls and cls[0] == 'q':
            current.append(render_q(h))
        elif name == 'div' and cls and cls[0] == 'box':
            current.append(render_box(h))
        else:
            current.append(h)
    flush()

    n_sub = sum(1 for it in items if it.startswith('<details class="mm-sub"'))
    n_q = len(re.findall(r'<div class="q( |")', card_html))
    if n_sub or n_q:
        meta_bits.append(f'{n_sub} subtopics · {n_q} questions' if n_sub else f'{n_q} questions')
    meta = ' · '.join(meta_bits)
    return (f'<details class="mm-sec mm-node"><summary class="mm-sum">'
            f'<span class="mm-no">{esc(no)}</span><span class="mm-t">{esc(title)}</span>'
            f'<span class="mm-meta">{esc(meta)}</span></summary>'
            f'<div class="mm-body">{"".join(items)}</div></details>')

def page_parts(src):
    """Return (banner_html, [card_html...]) for a note page."""
    m = re.search(r'<div class="page"[^>]*>(.*)</div>\s*</body>\s*</html>\s*$', src, re.S)
    if not m:
        m = re.search(r'<div class="page"[^>]*>(.*)</div>\s*</body>', src, re.S)
    if not m:
        raise ValueError('page div not found')
    page = m.group(1)
    kids = direct_children(page)
    banner, cards = '', []
    for h, name, attrs in kids:
        cls = get_class(attrs).split()
        if cls and cls[0] == 'banner':
            banner = h
        elif cls and cls[0] == 'card':
            cards.append(h)
    return banner, cards

def chapter_node(base, icon, file, label, skip_marker):
    src = read(os.path.join(base, file))
    banner, cards = page_parts(src)
    if banner:
        banner = banner.replace('class="banner"', 'class="banner mm-banner"', 1)
    kept = [c for c in cards if skip_marker is None or skip_marker not in c]
    n_q = src.count('class="q"') + src.count('class="q solved"')
    meta = f'{len(kept)} sections · {n_q} questions'
    return (f'<details class="mm-ch mm-node"><summary class="mm-sum">'
            f'<span class="mm-ico">{icon}</span><span class="mm-t">{esc(label)}</span>'
            f'<span class="mm-meta">{esc(meta)}</span></summary>'
            f'<div class="mm-body">{banner}{"".join(render_section(c) for c in kept)}</div></details>')

# ---------------------------------------------------------------- assemble

EXTRA_CSS = """
/* ===== single-file mind map ===== */
.mm-topbar { position: sticky; top: 0; z-index: 60; background: rgba(250,251,254,.93);
  backdrop-filter: blur(8px); border-bottom: 1px solid #e3e6f0; }
.mm-topbar .inner { max-width: 1100px; margin: 0 auto; display: flex; align-items: center;
  gap: 12px; padding: 10px 20px; flex-wrap: wrap; }
.mm-topbar .brand { font-weight: 800; color: #2a3550; font-size: 15px; }
.mm-topbar .brand small { font-weight: 600; color: #8a93b5; margin-left: 8px; }
.mm-topbar .btns { margin-left: auto; display: flex; gap: 6px; }
.mm-topbar button { border: 1px solid #cdd4e8; background: #fff; color: #2a3550;
  border-radius: 8px; padding: 5px 11px; font-size: 12.5px; cursor: pointer; font-weight: 700; }
.mm-topbar button:hover { background: #f2f4fa; border-color: #b9c2e0; }
.mm-app { max-width: 1100px; margin: 0 auto; padding: 22px 20px 90px; }
.mm-hint { font-size: 13px; color: #7a83a5; margin: 2px 2px 16px; line-height: 1.5; }

.mm-ch, .mm-sec, .mm-sub { background: #fff; border: 1px solid #e2e6f2; border-radius: 13px;
  box-shadow: 0 1px 2px rgba(30,40,90,.04); }
.mm-ch { margin: 16px 0; border-color: #d9ccf8; }
.mm-sec { margin: 12px 0; }
.mm-sub { margin: 12px 0; border-left: 3px solid #c9d2f0; }

.mm-node > summary { cursor: pointer; list-style: none; display: flex; align-items: center;
  gap: 10px; padding: 12px 16px; user-select: none; }
.mm-node > summary::-webkit-details-marker { display: none; }
.mm-node > summary::before { content: "▸"; flex: none; color: #8a93b5; font-size: 13px;
  transition: transform .15s ease; }
.mm-node[open] > summary::before { transform: rotate(90deg); }
.mm-node[open] > summary { border-bottom: 1px dashed #e2e6f2; }
.mm-node > summary:hover { background: #f7f8fd; }
.mm-ch > summary { padding: 15px 18px; }
.mm-ch[open] > summary { border-bottom-color: #d9ccf8; }

.mm-ch > summary .mm-t { font-size: 1.22rem; font-weight: 800; color: #2a3550; }
.mm-sec > summary .mm-t { font-size: 1.05rem; font-weight: 700; color: #2a3550; }
.mm-sub > summary .mm-sum2 { font-size: .98rem; font-weight: 700; color: #3a4468; flex: 1 1 auto; }
.mm-ico { flex: none; font-size: 1.05rem; }
.mm-no { flex: none; font: 700 11.5px ui-monospace, SFMono-Regular, Menlo, monospace;
  color: #6d3fd4; background: #f3efff; border: 1px solid #d9ccf8; border-radius: 6px;
  padding: 2px 7px; white-space: nowrap; }
.mm-t { flex: 1 1 auto; min-width: 0; }
.mm-meta { flex: none; font-size: 11.5px; color: #8a93b5; font-weight: 600; white-space: nowrap; }
.mm-preview { flex: 0 1 auto; min-width: 0; font-weight: 400; font-size: 12.5px;
  color: #7a83a5; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.mm-ch > .mm-body, .mm-sec > .mm-body, .mm-sub > .mm-body { padding: 14px 18px 16px; }
.mm-sec > .mm-body > .mm-sub { margin-left: 8px; }
.mm-banner { margin: 0 0 14px; }
.mm-banner h1 { font-size: 1.45rem; }
.mm-banner .sub { font-size: .92rem; }
.mm-node .q, .mm-node .box { margin: 12px 0; }
.mm-node .q > summary.q-head, .mm-node .box > summary.box-title { padding: 11px 14px; }
.mm-node details.ans > summary { cursor: pointer; }
@media (max-width: 640px) { .mm-meta { display: none; } .mm-preview { display: none; } }
"""

JS = """
(function () {
  function each(f) { document.querySelectorAll('details').forEach(f); }
  function depthOf(d) { var n = 0, e = d.parentElement; while (e) { if (e.tagName === 'DETAILS') n++; e = e.parentElement; } return n; }
  var map = { all: 99, l3: 3, l2: 2, l1: 1, none: 0 };
  document.querySelectorAll('.mm-topbar button[data-lv]').forEach(function (b) {
    b.addEventListener('click', function () {
      var lv = map[b.getAttribute('data-lv')];
      each(function (d) { d.open = depthOf(d) < lv; });
    });
  });
  var first = document.querySelector('.mm-ch');
  if (first) first.open = true;
})();
"""

def build(name):
    cfg = module_config(name)
    base = cfg['base']
    css = read(cfg['css'])
    mjsrc = cfg['nodes'][1][1] if len(cfg['nodes']) > 1 else 'index.html'
    first = read(os.path.join(base, mjsrc))
    mj_cfg = re.search(r'<script>\s*window\.MathJax.*?</script>', first, re.S).group(0)
    mj_cdn = re.search(r'<script async src="https://cdn\.jsdelivr[^"]*"></script>', first).group(0)

    parts = []
    for icon, file, label in cfg['nodes']:
        skip = cfg['skip'] if file == 'index.html' else None
        parts.append(chapter_node(base, icon, file, label, skip))

    srcs = [os.path.join(base, f) for _, f, _ in cfg['nodes']]
    src_kb = sum(os.path.getsize(f) for f in srcs if os.path.exists(f)) // 1024

    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cfg['title']}</title>
<style>
{css}
{EXTRA_CSS}
</style>
{mj_cfg}
{mj_cdn}
</head>
<body>
<nav class="topbar mm-topbar">
  <div class="inner">
    <span class="brand">{cfg['brand']} <small>one file · recursive mind map · {src_kb} KB of source notes</small></span>
    <span class="btns">
      <button data-lv="all">Expand all</button>
      <button data-lv="l3">To subtopics</button>
      <button data-lv="l2">To sections</button>
      <button data-lv="l1">Top only</button>
      <button data-lv="none">Collapse</button>
    </span>
  </div>
</nav>
<main class="mm-app">
  <p class="mm-hint">Click any line to expand it. The tree goes <strong>course → chapter → section → subtopic → question → answer</strong> —
  every node that shows a ▸ marker has children. Equations are typeset by MathJax on load (jsdelivr CDN).</p>
{chr(10).join('  ' + p for p in parts)}
</main>
<footer class="foot mm-foot" style="max-width:1100px;margin:0 auto;padding:0 20px 40px;color:#8a93b5;font-size:12.5px;">
  Generated from the note pages by <code>build-mindmap.py</code> — the paginated originals remain in this folder (see <a href="{cfg['back'][0]}">{cfg['back'][1]}</a>).
</footer>
<script>
{JS}
</script>
</body>
</html>
"""
    with open(cfg['out'], 'w', encoding='utf-8') as f:
        f.write(out)
    print(f"[{name}] wrote {os.path.relpath(cfg['out'], ROOT)} ({len(out):,} bytes, {len(parts)} top nodes)")

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    mods = find_modules()
    if which.lower() == 'all':
        targets = mods
    else:
        aliases = {}
        for k, v in load_overrides().get('aliases', {}).items():
            aliases[slug(k)] = v
        want = aliases.get(slug(which), which)
        targets = [m for m in mods if slug(m) == slug(want)]
        if not targets:
            raise SystemExit(f'no module folder matching {which!r}; found: '
                             + (', '.join(mods) if mods else '(none)'))
    for name in targets:
        build(name)
