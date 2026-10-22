"""Sheet composer: parse editable markdown-ish content, lay out on A4 canvas.

Content DSL (see chapter README):
  --- yaml frontmatter: id, part ('jee'|'olympiad'), title ---
  ## Section heading        -> teal section band (also becomes sheet title when
                               it opens a new sheet)
  ### Subheading            -> in-column teal heading
  prose paragraphs with inline $math$ and **bold**
  - bullets / 1. numbered items
  $$ display math $$        -> centred; auto-shrinks to fit the column
  :::key|warn|intuition|derive|example|app|assume [title="..."]  ... :::
  :::diagram {json spec} :::   (add "wide": true in the spec to span both columns)

Layout: two text columns (1060 px each) on a 2480x3508 canvas. Content is
auto-paginated: when the current sheet is full, a new sheet is started at the
next block boundary — prose is never shrunk or cut, the set expands instead.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from PIL import Image, ImageDraw

from core import (BLUE_BG, FALLBACK, FALLBACK_BOLD, GOLD, GRAY_BG, HAND, HAND_BOLD,
                  INK_FAINT, NAVY, PX_PER_PT, RED, RED_BG, RULE, TEAL, TEAL_BG,
                  WHITE, YELLOW_BAR, YELLOW_BG, Drawer, Run, get_font,
                  math_check, math_image)
from diagrams import build_diagram

PAGE_W, PAGE_H = 2480, 3508
MARGIN = 120
COL_W = 1060
COL_GAP = 120
COL0_X = MARGIN
COL1_X = MARGIN + COL_W + COL_GAP          # 1300
FULL_W = PAGE_W - 2 * MARGIN               # 2240
CONTENT_TOP = 300
CONTENT_BOTTOM = 3280
ITEM_GAP = 26
LINE_H = 66
BODY = 48
BODY_PT = BODY / PX_PER_PT                 # 11.52 pt
DISPLAY = 54
BOX_PAD = 26

BOX_STYLES = {
    "key": dict(bg=YELLOW_BG, bar=YELLOW_BAR, label="KEY RESULT", label_col=GOLD,
                text=NAVY, title_col=GOLD),
    "warn": dict(bg=RED_BG, bar=RED, label="COMMON TRAP", label_col=RED,
                 text=NAVY, title_col=RED),
    "intuition": dict(bg=TEAL_BG, bar=TEAL, label="INTUITION", label_col=TEAL,
                      text=NAVY, title_col=TEAL),
    "derive": dict(bg=BLUE_BG, bar=TEAL, label="SHORT DERIVATION", label_col=TEAL,
                   text=NAVY, title_col=TEAL),
    "example": dict(bg=GRAY_BG, bar=NAVY, label="WORKED EXAMPLE", label_col=NAVY,
                    text=NAVY, title_col=NAVY),
    "app": dict(bg=TEAL_BG, bar=TEAL, label="STANDARD APPLICATION", label_col=TEAL,
                text=NAVY, title_col=TEAL),
    "assume": dict(bg=BLUE_BG, bar=NAVY, label="ASSUMPTIONS & CONVENTIONS",
                   label_col=NAVY, text=NAVY, title_col=NAVY),
}


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------
@dataclass
class Block:
    kind: str
    text: str = ""
    items: list = field(default_factory=list)      # bullets / nested blocks
    blocks: list = field(default_factory=list)     # box children
    title: str = ""
    spec: dict = field(default_factory=dict)
    wide: bool = False


_FENCE_RE = re.compile(r"^:::(\w+)\s*(.*)$")
_INLINE_SPLIT = re.compile(r"(\$\$[^$]*\$\$|\$[^$]+\$|\*\*[^*]+\*\*|\*[^*]+\*)")


def _parse_inline_runs(text: str, size: int = BODY, color=NAVY,
                       bold: bool = False, emph: bool = False) -> list[Run]:
    runs: list[Run] = []
    for part in _INLINE_SPLIT.split(text):
        if not part:
            continue
        if part.startswith("$") and part.endswith("$") and len(part) > 2:
            runs.append(Run("math", part.strip("$"), bold=bold, color=color, size=size))
        elif part.startswith("**") and part.endswith("**") and len(part) > 4:
            runs.extend(_parse_inline_runs(part[2:-2], size=size, color=color,
                                           bold=True, emph=emph))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            runs.extend(_parse_inline_runs(part[1:-1], size=size,
                                           color=TEAL if not emph else color,
                                           bold=bold, emph=True))
        else:
            runs.append(Run("text", part, bold=bold, color=color, size=size))
    return runs


def parse_content(src: str):
    lines = src.splitlines()
    fm = {}
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            k, _, v = lines[i].partition(":")
            v = v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
            fm[k.strip()] = v
            i += 1
        i += 1

    def parse_blocks(until_fence: bool = False):
        nonlocal i
        out: list[Block] = []
        para_buf: list[str] = []

        def flush_para():
            nonlocal para_buf
            if para_buf:
                out.append(Block("para", text=" ".join(para_buf)))
                para_buf = []

        while i < len(lines):
            raw = lines[i]
            line = raw.rstrip()
            if line.strip() == ":::":
                i += 1
                if until_fence:
                    flush_para()
                    return out
                continue
            m = _FENCE_RE.match(line.strip())
            if m:
                flush_para()
                name, rest = m.group(1), m.group(2).strip()
                i += 1
                title = ""
                if rest.startswith("title="):
                    title = rest[6:].strip().strip('"').strip("'")
                if name == "diagram":
                    body = []
                    while i < len(lines) and lines[i].strip() != ":::":
                        body.append(lines[i])
                        i += 1
                    i += 1  # closing
                    spec = json.loads("\n".join(body))
                    out.append(Block("diagram", spec=spec,
                                     wide=bool(spec.get("wide", False))))
                else:
                    inner = parse_blocks(until_fence=True)
                    out.append(Block("box", items=inner, title=title,
                                     text=name))
                continue
            if line.startswith("$$") and line.strip().endswith("$$") and len(line.strip()) > 4:
                flush_para()
                out.append(Block("display", text=line.strip()[2:-2].strip()))
                i += 1
                continue
            if line.strip() == "$$":
                flush_para()
                i += 1
                body = []
                while i < len(lines) and lines[i].strip() != "$$":
                    body.append(lines[i])
                    i += 1
                i += 1
                out.append(Block("display", text="\n".join(body)))
                continue
            if line.startswith("## "):
                flush_para()
                out.append(Block("head2", text=line[3:].strip()))
                i += 1
                continue
            if line.startswith("### "):
                flush_para()
                out.append(Block("head3", text=line[4:].strip()))
                i += 1
                continue
            if re.match(r"^\s*[-*] ", line):
                flush_para()
                items = []
                while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                    items.append(re.sub(r"^\s*[-*] ", "", lines[i].rstrip()))
                    i += 1
                out.append(Block("bullets", items=items))
                continue
            if re.match(r"^\s*\d+\. ", line):
                flush_para()
                items = []
                while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                    items.append(re.sub(r"^\s*\d+\. ", "", lines[i].rstrip()))
                    i += 1
                out.append(Block("numbered", items=items))
                continue
            if not line.strip():
                flush_para()
                i += 1
                continue
            para_buf.append(line.strip())
            i += 1
        flush_para()
        return out

    blocks = parse_blocks()
    return fm, blocks


# --------------------------------------------------------------------------
# Block rendering
# --------------------------------------------------------------------------
class BlockRenderer:
    def __init__(self):
        self.math_bad = []

    def _lines_from_runs(self, runs: list[Run], width: int) -> list[list[Run]]:
        lines: list[list[Run]] = [[]]
        cur_w = 0
        for run in runs:
            if run.kind == "math":
                img = math_image(run.text, pt=BODY_PT, color=_hex(run.color))
                w = img.width + 6
                if cur_w + w > width and lines[-1]:
                    lines.append([])
                    cur_w = 0
                lines[-1].append(run)
                cur_w += w
                continue
            tokens = re.findall(r"\s*\S+\s*|\s+", run.text)
            for tok in tokens:
                drawer_font = HAND_BOLD if run.bold else HAND
                w = int(_measure(tok, drawer_font, run.size)) + 2
                if cur_w + w > width and lines[-1] and tok.strip():
                    lines.append([])
                    cur_w = 0
                if not lines[-1] and not tok.strip():
                    continue
                if not lines[-1] and tok[0].isspace():
                    tok = tok.lstrip()
                    w = int(_measure(tok, drawer_font, run.size)) + 2
                lines[-1].append(Run("text", tok, bold=run.bold, color=run.color,
                                     size=run.size, font_name=run.font_name))
                cur_w += w
        return lines

    def _draw_paragraph(self, img: Image.Image, x: int, y: int, text: str,
                        width: int, size: int = BODY, color=NAVY, bold: bool = False,
                        line_h: int = LINE_H) -> int:
        runs = _parse_inline_runs(text, size=size, color=color, bold=bold)
        for r in runs:
            if r.kind == "math" and not math_check(r.text, pt=size / PX_PER_PT):
                self.math_bad.append(r.text)
        lines = self._lines_from_runs(runs, width)
        d = Drawer(img)
        for ln in lines:
            cx = x
            line_h_eff = line_h
            for r in ln:
                if r.kind == "math":
                    im = math_image(r.text, pt=size / PX_PER_PT, color=_hex(r.color))
                    line_h_eff = max(line_h_eff, int(im.height * 1.15))
            yy = y + (line_h_eff - line_h) // 2
            for r in ln:
                cx, _ = d.draw_run((cx, yy), r)
            y += line_h_eff
        return y

    def _draw_display(self, img: Image.Image, x: int, y: int, tex: str,
                      width: int) -> int:
        if not math_check(tex, pt=DISPLAY / PX_PER_PT):
            self.math_bad.append(tex)
        im = math_image(tex, pt=DISPLAY / PX_PER_PT, color=_hex(NAVY), display=True)
        if im.width > width - 20:
            scale = (width - 20) / im.width
            if scale < 0.72:
                self.math_bad.append(f"[too wide {im.width}>{width}] {tex}")
            else:
                im = im.resize((int(im.width * scale), int(im.height * scale)),
                               Image.LANCZOS)
        px = x + max((width - im.width) // 2, 0)
        img.paste(im, (px, y + 8), im)
        return y + im.height + 26

    def render(self, block: Block, width: int) -> Image.Image:
        k = block.kind
        if k in ("para",):
            h = self._estimate_para(block.text, width)
            img = Image.new("RGBA", (width, h), (0, 0, 0, 0))
            self._draw_paragraph(img, 0, 0, block.text, width)
            return img
        if k == "display":
            im = math_image(block.text, pt=DISPLAY / PX_PER_PT,
                            color=_hex(NAVY), display=True)
            img = Image.new("RGBA", (width, im.height + 34), (0, 0, 0, 0))
            self._draw_display(img, 0, 0, block.text, width)
            return img
        if k in ("bullets", "numbered"):
            parts = []
            total = 0
            for it in block.items:
                ph = self._estimate_para(it, width - 56)
                parts.append(ph)
                total += ph + 8
            img = Image.new("RGBA", (width, total), (0, 0, 0, 0))
            y = 0
            for idx, it in enumerate(block.items):
                d = ImageDraw.Draw(img)
                if k == "bullets":
                    d.ellipse([8, y + 22, 22, y + 36], fill=TEAL)
                else:
                    lab = f"{idx + 1}."
                    d.text((2, y + 12), lab, font=get_font(HAND_BOLD, 40), fill=TEAL)
                self._draw_paragraph(img, 56, y, it, width - 56)
                y += parts[idx] + 8
            return img
        if k == "head3":
            img = Image.new("RGBA", (width, 84), (0, 0, 0, 0))
            d = Drawer(img)
            d.draw_run((0, 4), Run("text", block.text, bold=True, color=TEAL, size=54))
            dr = ImageDraw.Draw(img)
            dr.line([0, 76, min(width, 700), 76], fill=TEAL, width=3)
            return img
        if k == "box":
            return self._render_box(block, width)
        if k == "diagram":
            return build_diagram(block.spec, width).convert("RGBA")
        if k == "head2":
            size = 52
            runs = _parse_inline_runs(block.text, size=size, color=TEAL, bold=True)
            while True:
                lines = self._lines_from_runs(runs, width - 36)
                if len(lines) <= 1 or size <= 40:
                    break
                size -= 4
                runs = _parse_inline_runs(block.text, size=size, color=TEAL, bold=True)
            h = 44 + size * len(lines) + 26
            img = Image.new("RGBA", (width, h), (0, 0, 0, 0))
            d = ImageDraw.Draw(img)
            d.rectangle([0, 0, width, 12], fill=TEAL)
            dr = Drawer(img)
            y = 34
            for ln in lines:
                cx = 18
                for r in ln:
                    cx, _ = dr.draw_run((cx, y), r)
                y += size + 8
            d.rectangle([0, h - 8, width, h - 2], fill=(176, 214, 212))
            return img
        raise ValueError(f"unknown block kind {k}")

    def _estimate_para(self, text: str, width: int) -> int:
        runs = _parse_inline_runs(text)
        lines = self._lines_from_runs(runs, width)
        total = 0
        for ln in lines:
            lh = LINE_H
            for r in ln:
                if r.kind == "math":
                    im = math_image(r.text, pt=BODY_PT, color=_hex(r.color))
                    lh = max(lh, int(im.height * 1.15))
            total += lh
        return total + 6

    def _render_box(self, block: Block, width: int) -> Image.Image:
        style = BOX_STYLES.get(block.text, BOX_STYLES["key"])
        inner_w = width - 2 * BOX_PAD - 14
        heights = []
        for child in block.items:
            heights.append(self.render(child, inner_w).height)
        label_h = 58
        gap = 14
        # wrap the box title to the inner width (no clipping)
        title_lines = []          # list of (line_runs, line_height)
        if block.title:
            probe = Drawer(Image.new("RGBA", (8, 8)))
            runs = _parse_inline_runs(block.title, size=44, color=style["title_col"],
                                      bold=True)
            tokens = []
            for r in runs:
                if r.kind == "math":
                    tokens.append(r)
                else:
                    for tok in re.split(r"(\s+)", r.text):
                        if tok:
                            tokens.append(Run(r.kind, tok, bold=r.bold, color=r.color,
                                              font_name=r.font_name, size=r.size))
            cur, curw = [], 0.0
            for t in tokens:
                if t.text.isspace() and not cur:
                    continue
                w, h = probe.measure_run(t)
                if cur and curw + w > inner_w:
                    title_lines.append(cur)
                    cur, curw = ([], 0.0) if t.text.isspace() else ([t], float(w))
                else:
                    cur.append(t)
                    curw += w
            if cur:
                title_lines.append(cur)
        def _line_h(ln):
            mh = 0
            for t in ln:
                _, th = probe.measure_run(t)
                mh = max(mh, th)
            return max(56, mh + 10)
        title_h = sum(_line_h(ln) for ln in title_lines) if title_lines else 0
        body_h = sum(heights) + gap * max(len(heights) - 1, 0)
        total = BOX_PAD + label_h + title_h + body_h + BOX_PAD
        img = Image.new("RGBA", (width, total), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([0, 0, width - 2, total - 2], radius=18,
                            fill=style["bg"], outline=style["bar"], width=3)
        d.rectangle([0, 0, 12, total - 2], fill=style["bar"])
        d.text((BOX_PAD + 14, BOX_PAD - 6), style["label"],
               font=get_font(HAND_BOLD, 38), fill=style["label_col"])
        y = BOX_PAD + label_h
        if title_lines:
            drawer = Drawer(img)
            for ln in title_lines:
                lh = _line_h(ln)
                cx = BOX_PAD + 14
                cy = y - 2
                for r in ln:
                    cx, _ = drawer.draw_run((cx, cy), r)
                y += lh
        for child, h in zip(block.items, heights):
            sub = self.render(child, inner_w)
            img.alpha_composite(sub, (BOX_PAD + 14, y))
            y += h + gap
        return img


def _measure(text: str, font_name: str, size: int) -> float:
    from core import split_runs
    total = 0.0
    for fname, seg in split_runs(text, font_name,
                                 FALLBACK_BOLD if "Bold" in font_name else FALLBACK):
        total += get_font(fname, size).getlength(seg)
    return total


def _hex(c) -> str:
    return "#%02x%02x%02x" % c


# --------------------------------------------------------------------------
# Pagination: measure -> split into pages at block boundaries
# --------------------------------------------------------------------------
@dataclass
class Page:
    items: list = field(default_factory=list)   # list[(Block, Image)]
    title: str = ""


def paginate(blocks: list[Block], br: BlockRenderer) -> tuple[list[Page], list[str]]:
    """Render all blocks, then flow them into pages. Prose is never cut: an
    overflowing block starts a new page. Section headings are kept with their
    first following block (no orphan headings)."""
    rendered: list[tuple[Block, Image.Image]] = []
    errors = []
    for b in blocks:
        w = FULL_W if b.wide else COL_W
        if b.kind == "diagram":
            w = FULL_W if b.spec.get("wide", False) else COL_W
            b.wide = bool(b.spec.get("wide", False))
        im = br.render(b, w)
        if im.height > (CONTENT_BOTTOM - CONTENT_TOP):
            errors.append(f"block taller than a whole column: {b.kind} {b.text[:40]}")
        rendered.append((b, im))

    pages: list[Page] = []
    cur = Page()
    y0 = y1 = CONTENT_TOP
    col = 0

    def new_page():
        nonlocal cur, y0, y1, col
        if cur.items:
            pages.append(cur)
        cur = Page()
        y0 = y1 = CONTENT_TOP
        col = 0

    idx = 0
    while idx < len(rendered):
        b, im = rendered[idx]
        # orphan-heading rule: a head2 must stay with the first block after it
        extra_h = 0
        if b.kind == "head2" and idx + 1 < len(rendered):
            nb, nim = rendered[idx + 1]
            if not (nb.wide or nim.width == FULL_W):
                extra_h = nim.height + ITEM_GAP

        if b.wide or im.width == FULL_W:
            cut = max(y0, y1) + 14
            if cut + im.height + extra_h > CONTENT_BOTTOM or \
                    (cut > CONTENT_TOP + 14 and col == 0 and y1 == CONTENT_TOP):
                new_page()
                cut = CONTENT_TOP + 14
            cur.items.append((b, im, cut))
            y0 = y1 = cut + im.height + ITEM_GAP
            col = 0
            idx += 1
            continue

        need = im.height + extra_h
        placed = False
        for attempt in (0, 1):
            y = y0 if col == 0 else y1
            if y + need <= CONTENT_BOTTOM:
                cur.items.append((b, im, y, col))
                if col == 0:
                    y0 = y + im.height + ITEM_GAP
                else:
                    y1 = y + im.height + ITEM_GAP
                placed = True
                break
            if col == 0:
                col = 1
        if placed:
            idx += 1
            continue
        new_page()
        if im.height + extra_h > CONTENT_BOTTOM - CONTENT_TOP:
            errors.append(f"block too tall even alone: {b.kind} {b.text[:40]}")
            idx += 1
            continue
        cur.items.append((b, im, CONTENT_TOP, 0))
        y0 = CONTENT_TOP + im.height + ITEM_GAP
        col = 0
        idx += 1

    if cur.items:
        pages.append(cur)

    # page titles: prefer a leading section heading, else "(cont.)"
    base = ""
    for pg in pages:
        first = pg.items[0][0]
        if first.kind == "head2":
            pg.title = first.text
        else:
            pg.title = base + " (cont.)" if base else first.text[:60]
        base = pg.title.replace(" (cont.)", "")
    return pages, errors


# --------------------------------------------------------------------------
# Sheet drawing (header/footer/background + paste pre-rendered blocks)
# --------------------------------------------------------------------------
def draw_sheet(fm: dict, page: Page, chapter_slug: str, part_label: str,
               sheet_no: int, sheet_total: int, show_legend: bool,
               page_id: str = "") -> Image.Image:
    img = Image.new("RGB", (PAGE_W, PAGE_H), WHITE)
    d = ImageDraw.Draw(img)
    for yy in range(CONTENT_TOP - 40, CONTENT_BOTTOM + 40, 54):
        d.line([MARGIN, yy, PAGE_W - MARGIN, yy], fill=(236, 241, 248), width=2)

    title = page.title or fm.get("title", "")
    chip = f"{part_label}  ·  SHEET {sheet_no} / {sheet_total}"
    cw = _measure(chip, HAND_BOLD, 38) + 48
    avail = PAGE_W - 2 * MARGIN - cw - 60
    tsize = 62
    while _measure(title, HAND_BOLD, tsize) > avail and tsize > 42:
        tsize -= 4
    while _measure(title + "…", HAND_BOLD, tsize) > avail and len(title) > 8:
        title = title[:-2]
    if _measure(title + "…", HAND_BOLD, tsize) <= avail and \
            _measure(page.title or fm.get("title", ""), HAND_BOLD, tsize) > avail:
        title = title.rstrip() + "…"
    drawer = Drawer(img)
    cx = MARGIN
    for r in _parse_inline_runs(title, size=tsize, color=TEAL, bold=True):
        cx, _ = drawer.draw_run((cx, 122 + (62 - tsize)), r)
    d.rounded_rectangle([PAGE_W - MARGIN - cw, 128, PAGE_W - MARGIN, 208],
                        radius=16, fill=TEAL_BG, outline=TEAL, width=3)
    d.text((PAGE_W - MARGIN - cw + 24, 148), chip,
           font=get_font(HAND_BOLD, 38), fill=TEAL)
    if show_legend:
        leg = "colour key: navy = prose · teal = headings · yellow = key results · red = common traps"
        d.text((MARGIN, 218), leg, font=get_font(HAND, 34), fill=INK_FAINT)
    d.line([MARGIN, 268, PAGE_W - MARGIN, 268], fill=TEAL, width=4)
    d.line([MARGIN, 280, PAGE_W - MARGIN, 280], fill=(176, 214, 212), width=2)

    part = fm.get("part", "jee")
    foot_l = f"short notes · {chapter_slug}"
    foot_c = page_id or fm.get("id", "")
    foot_r = ("PART I (JEE)" if part == "jee" else "PART II (OLYMPIAD)") + \
             f" · page {sheet_no} of {sheet_total}"
    d.line([MARGIN, 3302, PAGE_W - MARGIN, 3302], fill=(176, 214, 212), width=2)
    f1 = get_font(HAND, 38)
    d.text((MARGIN, 3316), foot_l, font=f1, fill=INK_FAINT)
    d.text((PAGE_W // 2 - 40, 3316), foot_c, font=f1, fill=INK_FAINT)
    d.text((PAGE_W - MARGIN - _measure(foot_r, HAND, 38) - 6, 3316), foot_r,
           font=f1, fill=INK_FAINT)

    for item in page.items:
        if len(item) == 4:
            b, im, y, col = item
            x = COL0_X if col == 0 else COL1_X
            if im.mode == "RGBA":
                img.paste(im, (x, y), im)
            else:
                img.paste(im.convert("RGB"), (x, y))
        else:
            b, im, ycut = item
            if im.mode == "RGBA":
                img.paste(im, (MARGIN, ycut), im)
            else:
                img.paste(im.convert("RGB"), (MARGIN, ycut))
    return img


# legacy entry used by checks for standalone measurement (kept simple)
def compose_sheet(fm, blocks, chapter_slug, part_label, sheet_no, sheet_total):
    br = BlockRenderer()
    pages, errors = paginate(blocks, br)
    img = draw_sheet(fm, pages[0], chapter_slug, part_label, sheet_no,
                     sheet_total, show_legend=(sheet_no == 1))
    return type("R", (), dict(image=img, free_col0=0, free_col1=0,
                              overflow=errors, math_bad=br.math_bad))()
