#!/usr/bin/env python3
"""
Convert standalone mindmap HTML notes (published/) into well-ordered Markdown
with proper formatting, math, and diagrams.

- Parses each published/<Module>/*-mindmap.html
- Extracts course map, chapters, sections, subtopics, boxes, questions, figures
- Saves diagrams as SVG files
- Generates Markdown with Mermaid where possible
- Outputs to notes/<Module>/ — ONE FOLDER PER CHAPTER
  (notes/<Module>/NN-<chapter-slug>/README.md holds the whole chapter),
  plus paper, solutions, assets and the module README
- Also generates the top-level notes/README.md index

The per-chapter folders are the canonical note layout; after conversion the
files are hand-owned. Re-run this tool only to re-export a published map.
The single-file <slug>-complete.md snapshot is built by tools/build-complete.py.

Usage: python3 tools/convert_to_md.py all
       python3 tools/convert_to_md.py PnC
"""
import os, re, html as H, json, sys, pathlib
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
PUBLISHED_DIR = os.path.join(ROOT, "published")
NOTES_ROOT = os.path.join(ROOT, "notes")

# Reuse parsing logic from build-mindmap.py
VOID = {'meta', 'link', 'br', 'img', 'hr', 'input'}
TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:[^>"\'/]|"[^"]*"|\'[^\']*\')*)(/?)>')

def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def slug(name):
    return re.sub(r'[\s_-]+', '-', name.strip().lower()).strip('-')

def display(name):
    """Human-readable module title from a kebab-case folder name."""
    return name.replace('-', ' ')

def chapter_folder_slug(title):
    """One folder per chapter, named after the chapter:
    'Ch 1 · What (a+b)^n Counts' -> 'what-a-b-n-counts'."""
    t = re.sub(r'^ch\s*\d+\s*[·:.\-]?\s*', '', title.strip(), flags=re.I)
    t = t.replace('&', ' and ')
    t = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
    return t

def text_of(h):
    t = re.sub(r'<[^>]+>', ' ', h)
    t = H.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

def get_class(attrs):
    m = re.search(r'class="([^"]*)"', attrs or '')
    return m.group(1) if m else ''

def strip_outer(html, tag):
    m = re.match(rf'<{tag}\b[^>]*>(.*)</{tag}>\s*$', html, re.S)
    if not m:
        # try without requiring end at string end
        m2 = re.search(rf'<{tag}\b[^>]*>(.*)</{tag}>', html, re.S)
        if m2:
            return m2.group(1)
        raise ValueError(f'cannot strip outer <{tag}>: {html[:120]!r}')
    return m.group(1)

def direct_children(s):
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

def find_modules():
    out = []
    for d in sorted(os.listdir(PUBLISHED_DIR)):
        p = os.path.join(PUBLISHED_DIR, d)
        if d.startswith('.') or not os.path.isdir(p):
            continue
        has_map = any(f.endswith('-mindmap.html') for f in os.listdir(p))
        if has_map:
            out.append(d)
    return out

def normalize_math(text):
    """Convert MathJax delimiters to standard markdown math."""
    # Preserve display math
    # \(...\) -> $...$
    # \[...\] -> $$...$$
    # $$...$$ stays $$...$$
    # Replace \(...\) with $...$ but careful not to break inside
    # Use regex
    def repl_inline(m):
        inner = m.group(1).strip()
        # Escape? keep as is
        return f"${inner}$"
    def repl_display_bracket(m):
        inner = m.group(1).strip()
        return f"\n$$ {inner} $$\n"
    # \[...\] -> display
    text = re.sub(r'\\\[(.*?)\\\]', repl_display_bracket, text, flags=re.S)
    # \(...\) -> inline
    text = re.sub(r'\\\((.*?)\\\)', repl_inline, text, flags=re.S)
    # Already $$...$$ keep
    # Clean double $$ with spaces
    return text

def html_inline_to_md(html_fragment):
    """Convert inline HTML to markdown text, preserving math."""
    # First, protect math blocks by replacing them with placeholders
    math_placeholders = []
    def save_math(m):
        math_placeholders.append(m.group(0))
        return f"__MATH_{len(math_placeholders)-1}__"
    # Protect \(...\), \[...\], $$...$$
    tmp = re.sub(r'\\\(.*?\\\)', save_math, html_fragment, flags=re.S)
    tmp = re.sub(r'\\\[.*?\\\]', save_math, tmp, flags=re.S)
    tmp = re.sub(r'\$\$.*?\$\$', save_math, tmp, flags=re.S)

    # Replace tags
    # <strong> <b> -> ** **
    tmp = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', tmp, flags=re.S|re.I)
    tmp = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', tmp, flags=re.S|re.I)
    tmp = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', tmp, flags=re.S|re.I)
    tmp = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', tmp, flags=re.S|re.I)
    tmp = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', tmp, flags=re.S|re.I)
    tmp = re.sub(r'<span class="answer-pill"[^>]*>(.*?)</span>', r'**Answer: \1**', tmp, flags=re.S)
    tmp = re.sub(r'<span class="chip"[^>]*>(.*?)</span>', r'`\1`', tmp, flags=re.S)
    tmp = re.sub(r'<span class="badge[^"]*"[^>]*>(.*?)</span>', r'[\1]', tmp, flags=re.S)
    tmp = re.sub(r'<span class="q-id"[^>]*>(.*?)</span>', r'**\1**', tmp, flags=re.S)
    tmp = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', tmp, flags=re.S)
    # Remove other spans
    tmp = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', tmp, flags=re.S)
    # <br> -> newline
    tmp = re.sub(r'<br\s*/?>', r'\n', tmp, flags=re.I)
    # Remove remaining tags
    tmp = re.sub(r'<[^>]+>', ' ', tmp)
    tmp = H.unescape(tmp)
    tmp = re.sub(r'\s+', ' ', tmp).strip()

    # Restore math
    for i, ph in enumerate(math_placeholders):
        tmp = tmp.replace(f"__MATH_{i}__", ph)
    # Now normalize math delimiters
    tmp = normalize_math(tmp)
    return tmp

def strip_outer_generic(fragment):
    """Return inner HTML of outermost element, regardless of tag."""
    # Find first '>' after '<'
    first_gt = fragment.find('>')
    if first_gt == -1:
        return fragment
    # Find last '</'
    last_lt = fragment.rfind('</')
    if last_lt == -1:
        # self-closing? return empty
        return ""
    return fragment[first_gt+1:last_lt]

def get_outer_class(fragment):
    m = re.match(r'<[^>]*class="([^"]*)"', fragment)
    return m.group(1) if m else ""

def html_block_to_md(fragment, assets_dir, fig_counter, module_slug):
    """Convert a block-level HTML fragment to markdown."""
    fragment = fragment.strip()
    if not fragment:
        return ""
    # Detect tag name
    tag_match = re.match(r'<([a-zA-Z0-9]+)', fragment)
    tag = tag_match.group(1) if tag_match else ""
    outer_class = get_outer_class(fragment)
    # Check type
    # Paragraph
    if tag == 'p':
        try:
            inner = strip_outer(fragment, 'p')
        except:
            inner = strip_outer_generic(fragment)
        md = html_inline_to_md(inner)
        return md + "\n\n" if md else ""
    # Formula div
    if 'formula' in outer_class:
        try:
            inner = strip_outer(fragment, 'div')
        except:
            inner = strip_outer_generic(fragment)
        inner = re.sub(r'<span class="label"[^>]*>.*?</span>', '', inner, flags=re.S)
        md = html_inline_to_md(inner)
        if '$$' not in md and '$' in md:
            md = md.replace('$', '').strip()
            md = f"\n$$ {md} $$\n\n"
        else:
            md = md.strip() + "\n\n"
        return md
    # Box - can be div.box or details.box - check outer class only
    if 'box' in outer_class and ('box-first' in outer_class or 'box-idea' in outer_class or 'box-warn' in outer_class or 'box-olymp' in outer_class or 'box-note' in outer_class or 'box-check' in outer_class or 'box-bridge' in outer_class or 'box-identity' in outer_class):
        # Determine class
        cls_match = re.search(r'class="([^"]*)"', fragment)
        cls = cls_match.group(1) if cls_match else ""
        # Inner content
        try:
            inner = strip_outer(fragment, tag) if tag else strip_outer_generic(fragment)
        except:
            inner = strip_outer_generic(fragment)
        # Try to extract title from summary or div.box-title
        title = ""
        body_html = inner
        # If details, summary contains title
        sum_match = re.search(r'<summary[^>]*class="box-title"[^>]*>(.*?)</summary>', inner, re.S)
        if sum_match:
            title = html_inline_to_md(sum_match.group(1))
            # Remove summary from body
            body_html = re.sub(r'<summary[^>]*>.*?</summary>', '', inner, flags=re.S)
        else:
            # Look for div.box-title
            bt_match = re.search(r'<div class="box-title"[^>]*>(.*?)</div>', inner, re.S)
            if bt_match:
                title = html_inline_to_md(bt_match.group(1))
                body_html = re.sub(r'<div class="box-title"[^>]*>.*?</div>', '', inner, flags=re.S)
        # Parse remaining body
        kids = direct_children(body_html)
        body_parts = []
        if kids:
            for child_html, name, attrs in kids:
                body_parts.append(html_block_to_md(child_html, assets_dir, fig_counter, module_slug))
        else:
            # Fallback: treat as inline
            if body_html.strip():
                body_parts.append(html_block_to_md(f"<p>{body_html}</p>", assets_dir, fig_counter, module_slug) if not body_html.strip().startswith('<') else html_inline_to_md(body_html) + "\n\n")
        body_md = "\n".join(body_parts).strip()
        box_type = "NOTE"
        if 'box-first' in cls:
            box_type = "First Principles"
        elif 'box-idea' in cls:
            box_type = "Key Idea"
        elif 'box-warn' in cls:
            box_type = "Common Trap"
        elif 'box-olymp' in cls:
            box_type = "Olympiad Extension"
        elif 'box-check' in cls:
            box_type = "Check"
        elif 'box-bridge' in cls:
            box_type = "Bridge"
        elif 'box-identity' in cls:
            box_type = "Identity"
        elif 'box-note' in cls:
            box_type = "Note"
        lines = []
        lines.append(f"> **{title}**" if title else f"> **{box_type}**")
        lines.append(">")
        for line in body_md.split("\n"):
            if line.strip() == "":
                lines.append(">")
            else:
                lines.append(f"> {line}")
        return "\n".join(lines) + "\n\n"
    # Question detection: outer class is q (e.g., "q solved mm-node" or "q mm-node")
    # Also check if outer class token is exactly 'q'
    outer_tokens = outer_class.split()
    is_q = 'q' in outer_tokens
    if is_q:
        # Parse q-head and body - handle both div and details outer
        # For mindmap, outer is details, so try details first
        try:
            inner = strip_outer(fragment, 'details')
        except:
            try:
                inner = strip_outer(fragment, 'div')
            except:
                inner = strip_outer_generic(fragment)
        kids = direct_children(inner)
        qhead_html = None
        body_htmls = []
        for child_html, name, attrs in kids:
            # q-head can be div or summary
            if 'q-head' in get_class(attrs):
                qhead_html = child_html
            else:
                body_htmls.append(child_html)
        qhead_text = html_inline_to_md(qhead_html) if qhead_html else ""
        # Extract problem and answer
        problem_parts = []
        answer_md = ""
        for b in body_htmls:
            if '<details class="ans"' in b or 'class="solution"' in b or 'class="ans-body"' in b or 'ans-body' in b:
                # Answer
                # Try to extract ans-body
                m = re.search(r'<div class="ans-body"[^>]*>(.*)</div>\s*</details>', b, re.S)
                if m:
                    ans_inner = m.group(1)
                else:
                    m2 = re.search(r'<div class="solution"[^>]*>(.*)</div>', b, re.S)
                    if m2:
                        ans_inner = m2.group(1)
                    else:
                        # details ans
                        m3 = re.search(r'<details class="ans"[^>]*>.*?<div class="ans-body"[^>]*>(.*?)</div>.*?</details>', b, re.S)
                        if m3:
                            ans_inner = m3.group(1)
                        else:
                            ans_inner = b
                # Convert ans_inner children
                ans_kids = direct_children(ans_inner) if '<div' in ans_inner or '<p' in ans_inner else [ans_inner]
                ans_blocks = []
                for ak in ans_kids:
                    if isinstance(ak, tuple):
                        ans_blocks.append(html_block_to_md(ak[0], assets_dir, fig_counter, module_slug))
                    else:
                        # ak might be string
                        if isinstance(ak, str) and ak.strip().startswith('<'):
                            ans_blocks.append(html_block_to_md(ak, assets_dir, fig_counter, module_slug))
                        else:
                            ans_blocks.append(html_inline_to_md(ak) + "\n\n")
                answer_md = "\n".join(ans_blocks).strip()
            else:
                problem_parts.append(html_block_to_md(b, assets_dir, fig_counter, module_slug))
        problem_md = "\n".join(problem_parts).strip()
        # Build markdown for question
        md = f"#### {qhead_text}\n\n"
        md += problem_md + "\n\n"
        if answer_md:
            md += "<details>\n<summary>Answer + Reasoning</summary>\n\n"
            md += answer_md + "\n\n"
            md += "</details>\n\n"
        return md
    # Figure - check outer class
    if 'figure' in outer_class:
        # Extract SVG and caption
        inner = strip_outer(fragment, 'div')
        svg_match = re.search(r'<svg.*?</svg>', inner, re.S)
        cap_match = re.search(r'<div class="cap"[^>]*>(.*?)</div>', inner, re.S)
        caption = html_inline_to_md(cap_match.group(1)) if cap_match else "Diagram"
        fig_counter[0] += 1
        fig_name = f"fig-{fig_counter[0]:02d}.svg"
        fig_path = os.path.join(assets_dir, fig_name)
        os.makedirs(assets_dir, exist_ok=True)
        if svg_match:
            svg_content = svg_match.group(0)
            # Save SVG
            with open(fig_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            # Also try to generate mermaid for simple diagrams? We'll include reference
            md = f"**{caption}**\n\n"
            md += f"![{caption}](assets/{fig_name})\n\n"
            # Add mermaid placeholder for key diagrams based on caption keywords
            # We'll generate simple mermaid for decision tree, circular, etc.
            # For now, include SVG as code block fallback
            # If caption mentions decision tree, add mermaid
            if 'decision tree' in caption.lower() or 'product rule' in caption.lower():
                md += "```mermaid\nflowchart TD\n    Start --> Red\n    Start --> Blue\n    Start --> Black\n    Red --> RB[\"red·bold\"]\n    Red --> RI[\"red·ital\"]\n    Blue --> BB[\"blue·bold\"]\n    Blue --> BI[\"blue·ital\"]\n    Black --> KB[\"blk·bold\"]\n    Black --> KI[\"blk·ital\"]\n```\n\n"
            elif 'circular' in caption.lower() or 'rotation' in caption.lower():
                md += "```mermaid\nflowchart LR\n    A -- rotation --> B\n    B -- same circular seating --> A\n```\n\n"
            elif 'pascal' in caption.lower():
                md += "```mermaid\nflowchart TD\n    R0[\"1\"] --> R1A[\"1\"] & R1B[\"1\"]\n    R1A --> R2A[\"1\"] & R2B[\"2\"]\n    R1B --> R2B & R2C[\"1\"]\n```\n\n"
            elif 'stars and bars' in caption.lower():
                md += "```mermaid\nflowchart LR\n    S[\"*** | * | ********* = (3,1,6)\"] --> D[\"Distribution\"]\n```\n\n"
            elif 'lattice' in caption.lower() or 'reflection' in caption.lower():
                md += "```mermaid\nflowchart TD\n    O[\"(0,0)\"] --> G[\"Good path stays <= diagonal\"]\n    O --> B[\"Bad path crosses y=x+1\"]\n    B --> R[\"Reflected to (-1,1) start\"]\n```\n\n"
            elif 'young' in caption.lower() or 'conjugation' in caption.lower():
                md += "```mermaid\nflowchart LR\n    P[\"5+3+2+1\"] <-->|Transpose| C[\"5+4+3+2+1\"]\n```\n\n"
            return md
        else:
            return f"*{caption}*\n\n"
    # Table - check tag
    if tag == 'table' or '<table' in fragment[:200]:
        # Convert HTML table to markdown
        # Extract rows
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', fragment, re.S)
        md_rows = []
        for r in rows:
            cols = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, re.S)
            md_cols = [html_inline_to_md(c).replace('|', '\\|') for c in cols]
            md_rows.append(md_cols)
        if not md_rows:
            return ""
        # Build markdown table
        # Determine max columns
        max_cols = max(len(r) for r in md_rows)
        # Pad
        for r in md_rows:
            while len(r) < max_cols:
                r.append("")
        # Header separator
        md = ""
        # First row as header
        md += "| " + " | ".join(md_rows[0]) + " |\n"
        md += "| " + " | ".join(["---"]*max_cols) + " |\n"
        for r in md_rows[1:]:
            md += "| " + " | ".join(r) + " |\n"
        md += "\n"
        return md
    # List
    if fragment.startswith('<ul') or fragment.startswith('<ol'):
        inner = strip_outer(fragment, 'ul') if fragment.startswith('<ul') else strip_outer(fragment, 'ol')
        items = re.findall(r'<li[^>]*>(.*?)</li>', inner, re.S)
        md = ""
        for it in items:
            md += f"- {html_inline_to_md(it)}\n"
        md += "\n"
        return md
    # Details mm-sub - check outer class
    if 'mm-sub' in outer_class:
        m = re.search(r'<summary class="mm-sum2"[^>]*>(.*?)</summary>', fragment, re.S)
        title = html_inline_to_md(m.group(1)) if m else "Subtopic"
        # Use direct_children to find mm-body
        inner_kids = direct_children(strip_outer_generic(fragment))
        body_html = ""
        for ch_html, ch_name, ch_attrs in inner_kids:
            if ch_name == 'div' and 'mm-body' in get_outer_class(ch_html):
                body_html = strip_outer_generic(ch_html)
                break
        kids = direct_children(body_html) if body_html else []
        body_md = ""
        for child_html, name, attrs in kids:
            body_md += html_block_to_md(child_html, assets_dir, fig_counter, module_slug)
        return f"#### {title}\n\n{body_md}\n"
    # Details mm-sec - check outer class
    if 'mm-sec' in outer_class:
        t_match = re.search(r'<span class="mm-t"[^>]*>(.*?)</span>', fragment, re.S)
        no_match = re.search(r'<span class="mm-no"[^>]*>(.*?)</span>', fragment, re.S)
        title = html_inline_to_md(t_match.group(1)) if t_match else "Section"
        no = html_inline_to_md(no_match.group(1)) if no_match else ""
        inner_kids = direct_children(strip_outer_generic(fragment))
        body_html = ""
        for ch_html, ch_name, ch_attrs in inner_kids:
            if ch_name == 'div' and 'mm-body' in get_outer_class(ch_html):
                body_html = strip_outer_generic(ch_html)
                break
        kids = direct_children(body_html) if body_html else []
        body_md = ""
        for child_html, name, attrs in kids:
            body_md += html_block_to_md(child_html, assets_dir, fig_counter, module_slug)
        heading = f"### {no} {title}".strip() if no else f"### {title}"
        return f"{heading}\n\n{body_md}\n"
    # Details mm-ch (should be handled higher, but fallback) - check outer class
    if 'mm-ch' in outer_class:
        t_match = re.search(r'<span class="mm-t"[^>]*>(.*?)</span>', fragment, re.S)
        title = html_inline_to_md(t_match.group(1)) if t_match else "Chapter"
        inner_kids = direct_children(strip_outer_generic(fragment))
        body_html = ""
        for ch_html, ch_name, ch_attrs in inner_kids:
            if ch_name == 'div' and 'mm-body' in get_outer_class(ch_html):
                body_html = strip_outer_generic(ch_html)
                break
        kids = direct_children(body_html) if body_html else []
        md = f"## {title}\n\n"
        for child_html, name, attrs in kids:
            md += html_block_to_md(child_html, assets_dir, fig_counter, module_slug)
        return md if body_html else html_inline_to_md(fragment) + "\n\n"
    # Banner - check outer class
    if 'banner' in outer_class:
        inner = strip_outer(fragment, 'div')
        # Extract h1, sub, kicker, chips
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', inner, re.S)
        sub = re.search(r'<p class="sub"[^>]*>(.*?)</p>', inner, re.S)
        kicker = re.search(r'<div class="kicker"[^>]*>(.*?)</div>', inner, re.S)
        chips = re.findall(r'<span class="chip"[^>]*>(.*?)</span>', inner, re.S)
        md = ""
        if kicker:
            md += f"*{html_inline_to_md(kicker.group(1))}*\n\n"
        if h1:
            md += f"# {html_inline_to_md(h1.group(1))}\n\n"
        if sub:
            md += f"{html_inline_to_md(sub.group(1))}\n\n"
        if chips:
            md += " ".join([f"`{html_inline_to_md(c)}`" for c in chips]) + "\n\n"
        return md
    # Default: try to extract inner and convert
    # If contains <p> etc, parse children
    if '<div' in fragment or '<p' in fragment:
        # Try direct_children
        try:
            kids = direct_children(fragment)
            if kids:
                md = ""
                for child_html, name, attrs in kids:
                    md += html_block_to_md(child_html, assets_dir, fig_counter, module_slug)
                return md
        except:
            pass
    # Fallback: inline
    return html_inline_to_md(fragment) + "\n\n"

def extract_mm_app(html_content):
    m = re.search(r'<main class="mm-app"[^>]*>(.*)</main>', html_content, re.S)
    if not m:
        raise ValueError("mm-app not found")
    return m.group(1)

def parse_top_level_details(mm_app_inner):
    # Use direct_children to get top-level details
    kids = direct_children(mm_app_inner)
    details = []
    for child_html, name, attrs in kids:
        if name == 'details':
            details.append((child_html, attrs))
    return details

def extract_summary_info(details_html):
    id_match = re.search(r'id="([^"]+)"', details_html)
    did = id_match.group(1) if id_match else ""
    t_match = re.search(r'<span class="mm-t"[^>]*>(.*?)</span>', details_html, re.S)
    title = html_inline_to_md(t_match.group(1)) if t_match else did
    no_match = re.search(r'<span class="mm-no"[^>]*>(.*?)</span>', details_html, re.S)
    no = html_inline_to_md(no_match.group(1)) if no_match else ""
    meta_match = re.search(r'<span class="mm-meta"[^>]*>(.*?)</span>', details_html, re.S)
    meta = html_inline_to_md(meta_match.group(1)) if meta_match else ""
    # Extract mm-body using direct_children to avoid greedy regex issues
    inner = strip_outer_generic(details_html)
    inner_kids = direct_children(inner)
    body = ""
    for ch_html, ch_name, ch_attrs in inner_kids:
        if ch_name == 'div' and 'mm-body' in get_outer_class(ch_html):
            body = strip_outer_generic(ch_html)
            break
    return did, no, title, meta, body

def convert_module(module_folder):
    print(f"Converting {module_folder} ...")
    base_path = os.path.join(PUBLISHED_DIR, module_folder)
    # Find mindmap html
    maps = [f for f in os.listdir(base_path) if f.endswith('-mindmap.html')]
    if not maps:
        print(f"  No mindmap found in {module_folder}")
        return
    map_file = os.path.join(base_path, maps[0])
    html_content = read(map_file)
    mm_app_inner = extract_mm_app(html_content)
    top_details = parse_top_level_details(mm_app_inner)

    # Prepare output directory
    module_slug = slug(module_folder)
    out_dir = os.path.join(NOTES_ROOT, module_folder)
    os.makedirs(out_dir, exist_ok=True)
    assets_dir = os.path.join(out_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    fig_counter = [0]

    # Collect chapters
    chapters = []  # list of dicts
    course_map = None
    paper = None
    solutions = None

    for d_html, attrs in top_details:
        did, no, title, meta, body = extract_summary_info(d_html)
        if did == "course-map":
            course_map = {"id": did, "title": title, "body": body, "html": d_html}
        elif did.startswith("chapter-"):
            chapters.append({"id": did, "no": did.replace("chapter-", ""), "title": title, "meta": meta, "body": body, "html": d_html})
        elif did == "olympiad-paper":
            paper = {"id": did, "title": title, "body": body, "html": d_html}
        elif did == "solutions":
            solutions = {"id": did, "title": title, "body": body, "html": d_html}

    # Sort chapters by number
    chapters.sort(key=lambda x: int(x["no"]) if x["no"].isdigit() else 0)

    # Helper to convert body to markdown
    def body_to_md(body_html):
        kids = direct_children(body_html)
        md = ""
        for child_html, name, attrs in kids:
            md += html_block_to_md(child_html, assets_dir, fig_counter, module_slug)
        return md

    # Generate index.md (course map)
    index_md = f"# {module_folder} — Complete Course Notes\n\n"
    index_md += f"*Source: `{maps[0]}` converted to Markdown with diagrams*\n\n"
    if course_map:
        index_md += body_to_md(course_map["body"])
    index_md += "\n## Roadmap\n\n"
    for ch in chapters:
        index_md += f"- **Chapter {ch['no']}**: {ch['title']} — {ch['meta']}\n"
    if paper:
        index_md += f"- **Olympiad Paper**: {paper['title']} — {paper['meta'] if 'meta' in paper else ''}\n"
    if solutions:
        index_md += f"- **Solutions**: {solutions['title']}\n"

    # Write index
    with open(os.path.join(out_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(index_md)

    # Generate one folder per chapter:
    #   notes/<Module>/NN-<chapter-slug>/README.md
    # The folder is the chapter's home — all of its content lives in it.
    for ch in chapters:
        # Mindmap titles carry a "Ch N · " prefix; the H1 adds its own.
        ch_title = re.sub(r'^ch\s*\d+\s*·\s*', '', ch['title'].strip(), flags=re.I)
        ch_md = f"# Chapter {ch['no']} — {ch_title}\n\n"
        ch_md += f"*{ch['meta']}*\n\n"
        ch_md += body_to_md(ch['body'])
        ch_md += "\n---\n\n"
        # Chapter files sit one level below the module assets/ directory.
        ch_md = ch_md.replace('](assets/', '](../assets/')
        ch_dir = os.path.join(out_dir, f"{int(ch['no']):02d}-{chapter_folder_slug(ch['title'])}")
        os.makedirs(ch_dir, exist_ok=True)
        with open(os.path.join(ch_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(ch_md)

    # Paper
    if paper:
        paper_md = f"# {paper['title']}\n\n"
        paper_md += body_to_md(paper['body'])
        with open(os.path.join(out_dir, "olympiad-paper.md"), 'w', encoding='utf-8') as f:
            f.write(paper_md)

    if solutions:
        sol_md = f"# {solutions['title']}\n\n"
        sol_md += body_to_md(solutions['body'])
        with open(os.path.join(out_dir, "olympiad-paper-solutions.md"), 'w', encoding='utf-8') as f:
            f.write(sol_md)

    # The single-file <slug>-complete.md snapshot is generated from the
    # canonical Markdown by tools/build-complete.py — not here.

    print(f"  -> Generated {len(chapters)} chapter folders + paper + solutions in {out_dir}")

def main():
    args = sys.argv[1:]
    if not args:
        args = ["all"]
    if "all" in args:
        modules = find_modules()
    else:
        modules = []
        for a in args:
            # normalize: find folder matching slug
            for d in os.listdir(PUBLISHED_DIR):
                if os.path.isdir(os.path.join(PUBLISHED_DIR, d)) and slug(d) == slug(a):
                    modules.append(d)
                    break
            else:
                # direct name
                if os.path.isdir(os.path.join(PUBLISHED_DIR, a)):
                    modules.append(a)
    os.makedirs(NOTES_ROOT, exist_ok=True)
    for mod in modules:
        try:
            convert_module(mod)
        except Exception as e:
            print(f"Error converting {mod}: {e}")
            import traceback
            traceback.print_exc()

    # Generate master README
    master_path = os.path.join(NOTES_ROOT, "README.md")
    with open(master_path, 'w', encoding='utf-8') as f:
        f.write("# Maths JEE Advanced + Olympiad — Markdown Notes\n\n")
        f.write("The canonical, hand-owned notes: one folder per chapter under each module. "
                "Re-exported from the standalone HTML mindmaps in `published/` with proper formatting, math, and diagrams.\n\n")
        f.write("All theory is ordered from **board-level basics → JEE Main → JEE Advanced → Olympiad**.\n\n")
        f.write("## Modules\n\n")
        for mod in find_modules():
            f.write(f"### {display(mod)}\n")
            f.write(f"- [Overview & Roadmap]({mod}/README.md)\n")
            f.write(f"- [Complete Single File]({mod}/{slug(mod)}-complete.md) — all chapters + paper + solutions\n")
            # List chapter folders
            out_dir = os.path.join(NOTES_ROOT, mod)
            if os.path.isdir(out_dir):
                ch_dirs = sorted(d for d in os.listdir(out_dir)
                                 if re.match(r'\d\d-', d) and os.path.isdir(os.path.join(out_dir, d)))
                for cd in ch_dirs:
                    label = cd
                    try:
                        with open(os.path.join(out_dir, cd, 'README.md'), encoding='utf-8') as cf:
                            first = cf.readline().strip()
                        if first.startswith('#'):
                            label = first.lstrip('#').strip()
                    except OSError:
                        pass
                    f.write(f"  - [{label}]({mod}/{cd}/)\n")
            f.write(f"- [Olympiad Paper]({mod}/olympiad-paper.md) | [Solutions]({mod}/olympiad-paper-solutions.md)\n\n")
        f.write("\n## Formatting Conventions\n\n")
        f.write("- **Math**: inline `$...$`, display `$$...$$` (MathJax compatible)\n")
        f.write("- **Callouts**: blockquote with bold title — First Principles, Key Idea, Common Trap, Olympiad Extension\n")
        f.write("- **Diagrams**: SVG assets in `assets/` + Mermaid flowcharts where applicable\n")
        f.write("- **Questions**: `#### P1 ...` with collapsible `<details>` for answers\n")
        f.write("- **Tables**: GitHub Flavored Markdown tables\n")
        f.write("- **Theory Order**: Each module follows 6 chapters building from foundations to Olympiad frontier, with worked examples (S), practice (P), and capstone paper (Q)\n\n")
        f.write("## Coverage — JEE Advanced & Olympiad\n\n")
        f.write("Each module includes:\n")
        f.write("- **JEE Main**: direct formula application, product/sum rule, basic permutations\n")
        f.write("- **JEE Advanced**: restricted selections, gap method, derangements, stars & bars with bounds, binomial identities, generating functions\n")
        f.write("- **Olympiad**: bijections, involutions, double counting, inclusion–exclusion, rook polynomials, Catalan & reflection principle, Burnside–Pólya, partitions, Stirling/Bell numbers, Sperner, Erdős–Szekeres, probabilistic method, cycle lemma\n\n")

if __name__ == "__main__":
    main()
