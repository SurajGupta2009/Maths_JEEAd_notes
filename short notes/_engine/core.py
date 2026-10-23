"""Core rendering primitives: fonts with fallback, math (mathtext), text wrapping.

Canvas convention: 2480x3508 px portrait A4 @ 300 DPI (nominal).
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ENGINE_DIR = Path(__file__).resolve().parent
ASSETS = ENGINE_DIR.parent / "_assets"
FONTS = ASSETS / "fonts"

DPI = 300
PX_PER_PT = DPI / 72.0  # 4.1667 px per pt

# ---- palette (handwritten teacher notes) -----------------------------------
NAVY = (22, 41, 92)          # prose
TEAL = (15, 118, 110)        # headings / explanations
RED = (185, 28, 28)          # warnings
GOLD = (150, 100, 0)         # text on yellow
YELLOW_BG = (255, 243, 176)  # key result band
YELLOW_BAR = (224, 168, 0)
TEAL_BG = (230, 244, 243)
RED_BG = (254, 240, 240)
BLUE_BG = (240, 244, 252)
GRAY_BG = (246, 248, 251)
RULE = (200, 214, 234)
INK_FAINT = (120, 138, 170)
WHITE = (255, 255, 255)

HAND = "Kalam-Regular.ttf"
HAND_BOLD = "Kalam-Bold.ttf"
HAND_LIGHT = "Kalam-Light.ttf"
FALLBACK = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FALLBACK_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

_font_cache: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}


def get_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    key = (name, size)
    if key not in _font_cache:
        path = str(FONTS / name) if not name.startswith("/") else name
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


# ---- glyph coverage --------------------------------------------------------
_cmap_cache: dict[str, set] = {}


def _cmap(name: str) -> set:
    if name not in _cmap_cache:
        from fontTools.ttLib import TTFont

        path = str(FONTS / name) if not name.startswith("/") else name
        tt = TTFont(path)
        cmap = set()
        for table in tt["cmap"].tables:
            cmap |= set(table.cmap.keys())
        _cmap_cache[name] = cmap
    return _cmap_cache[name]


def has_glyph(name: str, ch: str) -> bool:
    return ord(ch) in _cmap(name)


def missing_glyphs(name: str, text: str) -> set:
    cmap = _cmap(name)
    return {ch for ch in text if ord(ch) not in cmap and not ch.isspace()}


def split_runs(text: str, prefer: str, fallback: str) -> list[tuple[str, str]]:
    """Split text into (font_name, substring) runs, using fallback for missing glyphs."""
    runs: list[tuple[str, str]] = []
    cur_font, buf = None, []
    cmap_p, cmap_f = _cmap(prefer), _cmap(fallback)
    for ch in text:
        f = prefer if (ord(ch) in cmap_p or ch.isspace()) else fallback
        if f != cur_font:
            if buf:
                runs.append((cur_font, "".join(buf)))
            cur_font, buf = f, []
        buf.append(ch)
    if buf:
        runs.append((cur_font, "".join(buf)))
    return runs


# ---- text measurement / drawing -------------------------------------------
@dataclass
class Run:
    kind: str          # 'text' | 'math'
    text: str          # raw text or latex (without $)
    bold: bool = False
    color: tuple = NAVY
    font_name: str = HAND
    size: int = 48


class Drawer:
    """Measures and draws text runs with per-glyph font fallback."""

    def __init__(self, image: Image.Image):
        self.image = image
        self.draw = ImageDraw.Draw(image)

    def measure_run(self, run: Run) -> tuple[int, int]:
        """returns (width, height_above_baseline_proxy)"""
        if run.kind == "math":
            img = math_image(run.text, pt=run.size / PX_PER_PT, color=rgb_hex(run.color))
            return img.width, img.height
        fname = HAND_BOLD if run.bold else run.font_name
        fnt = get_font(fname, run.size)
        w = 0
        for fname2, seg in split_runs(run.text, fname, FALLBACK_BOLD if run.bold else FALLBACK):
            w += get_font(fname2, run.size).getlength(seg)
        return int(w) + 2, int(run.size * 1.05)

    def draw_run(self, xy: tuple[int, int], run: Run) -> tuple[int, int]:
        x, y = xy  # y = top of em box
        if run.kind == "math":
            img = math_image(run.text, pt=run.size / PX_PER_PT, color=rgb_hex(run.color))
            # vertically centre math image on the text's visual centre
            self.image.paste(img, (int(x), int(y + run.size * 0.62 - img.height / 2)), img)
            return int(x) + img.width, y
        fname = HAND_BOLD if run.bold else run.font_name
        base = get_font(fname, run.size)
        for fname2, seg in split_runs(run.text, fname, FALLBACK_BOLD if run.bold else FALLBACK):
            fnt = get_font(fname2, run.size)
            # keep baselines aligned across fonts
            asc, _ = fnt.getmetrics()
            asc0, _ = base.getmetrics()
            self.draw.text((x, y + asc0 - asc), seg, font=fnt, fill=run.color)
            x += fnt.getlength(seg)
        return x + 2, y


def rgb_hex(c: tuple) -> str:
    return "#%02x%02x%02x" % c


# ---- math rendering (matplotlib mathtext) ----------------------------------
_math_cache: dict[tuple, Image.Image] = {}



# ---- matrices (mathtext has no array environments) -------------------------
import re as _re

_MAT_RE = _re.compile(r"\\begin\{(pmatrix|bmatrix|vmatrix|matrix)\}(.*?)\\end\{\1\}", _re.S)


def _matrix_image(kind: str, body: str, pt: float, color: str) -> Image.Image:
    rows = [r.split("&") for r in body.split(r"\\") if r.strip() or "&" in r]
    ncol = max(len(r) for r in rows)
    cells = []
    for r in rows:
        r = r + [""] * (ncol - len(r))
        cells.append([math_image(c.strip(), pt=pt, color=color) if c.strip()
                      else Image.new("RGBA", (2, 2), (0, 0, 0, 0)) for c in r])
    scale = pt * PX_PER_PT
    pad_x, pad_y = int(scale * 0.42), int(scale * 0.20)
    col_w = [max(cells[i][j].width for i in range(len(rows))) for j in range(ncol)]
    row_h = [max(cells[i][j].height for j in range(ncol)) for i in range(len(rows))]
    grid_w = sum(col_w) + pad_x * (ncol + 1)
    grid_h = sum(row_h) + pad_y * (len(rows) + 1)
    brack_w = 0 if kind == "matrix" else int(scale * 0.55)
    img = Image.new("RGBA", (grid_w + 2 * brack_w, grid_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5)) + (255,)
    y = pad_y
    for i in range(len(rows)):
        x = brack_w + pad_x
        for j in range(ncol):
            c = cells[i][j]
            if c.width > 2:
                img.alpha_composite(c, (x + (col_w[j] - c.width) // 2,
                                        y + (row_h[i] - c.height) // 2))
            x += col_w[j] + pad_x
        y += row_h[i] + pad_y
    lw = max(3, int(scale * 0.09))
    if kind in ("pmatrix", "bmatrix", "vmatrix"):
        for side in (0, 1):
            bx = lw if side == 0 else img.width - lw
            if kind == "vmatrix":
                draw.line([(bx, 2), (bx, img.height - 3)], fill=rgb, width=lw)
            elif kind == "bmatrix":
                draw.line([(bx, 2), (bx, img.height - 3)], fill=rgb, width=lw)
                ex = bx + (brack_w * 0.55 if side == 0 else -brack_w * 0.55)
                draw.line([(bx, 2), (ex, 2)], fill=rgb, width=lw)
                draw.line([(bx, img.height - 3), (ex, img.height - 3)], fill=rgb, width=lw)
            else:  # pmatrix: stretched parenthesis glyph
                ch = "(" if side == 0 else ")"
                f = get_font(FALLBACK, 100)
                tmp = Image.new("RGBA", (60, 100), (0, 0, 0, 0))
                ImageDraw.Draw(tmp).text((0, -12), ch, font=f, fill=rgb)
                tmp = tmp.crop(tmp.getbbox())
                tmp = tmp.resize((brack_w, img.height), Image.LANCZOS)
                img.alpha_composite(tmp, (0 if side == 0 else img.width - brack_w, 0))
    return img


def _math_with_matrices(body: str, pt: float, color: str, display: bool) -> Image.Image:
    parts, pos = [], 0
    for m in _MAT_RE.finditer(body):
        if m.start() > pos and body[pos:m.start()].strip(" ,"):
            parts.append(math_image(body[pos:m.start()], pt=pt, color=color, display=display))
        elif m.start() > pos:
            parts.append(math_image(body[pos:m.start()], pt=pt, color=color, display=display))
        parts.append(_matrix_image(m.group(1), m.group(2), pt, color))
        pos = m.end()
    if pos < len(body) and body[pos:].strip():
        parts.append(math_image(body[pos:], pt=pt, color=color, display=display))
    if not parts:
        return Image.new("RGBA", (2, 2), (0, 0, 0, 0))
    if len(parts) == 1:
        return parts[0]
    h = max(p.height for p in parts)
    img = Image.new("RGBA", (sum(p.width for p in parts), h), (0, 0, 0, 0))
    x = 0
    for p in parts:
        img.alpha_composite(p, (x, (h - p.height) // 2))
        x += p.width
    return img


def math_image(tex: str, pt: float = 11.5, color: str = "#16295C",
               display: bool = False) -> Image.Image:
    """Render LaTeX-ish math via matplotlib mathtext to a tight RGBA image."""
    key = (tex, round(pt, 2), color, display)
    if key in _math_cache:
        return _math_cache[key]
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    body = tex.strip()
    while body.startswith("$"):
        body = body[1:]
    while body.endswith("$"):
        body = body[:-1]
    if "\\begin{" in body:
        return _math_with_matrices(body, pt, color, display)
    body = "$" + body.strip() + "$"

    fig = plt.figure(figsize=(1, 1), dpi=DPI)
    fig.patch.set_alpha(0.0)
    t = fig.text(0.5, 0.5, body, fontsize=pt, color=color,
                 ha="center", va="center")
    fig.canvas.draw()
    bb = t.get_window_extent()
    plt.close(fig)

    w_in = max(bb.width / DPI + 0.12, 0.15)
    h_in = max(bb.height / DPI + 0.12, 0.15)
    fig = plt.figure(figsize=(w_in, h_in), dpi=DPI)
    fig.patch.set_alpha(0.0)
    fig.text(0.5, 0.5, body, fontsize=pt, color=color, ha="center", va="center")
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, transparent=True)
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf).convert("RGBA")
    # crop transparent margins
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    _math_cache[key] = img
    return img


def math_check(tex: str, pt: float = 11.5) -> bool:
    """Return True if mathtext can parse this; False otherwise."""
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib.font_manager import FontProperties
    from matplotlib import mathtext

    body = tex.strip()
    if "\\begin{" in body:
        inner = body.strip("$")
        pos = 0
        for m in _MAT_RE.finditer(inner):
            if inner[pos:m.start()].strip(" ,") and not math_check(inner[pos:m.start()], pt):
                return False
            for row in m.group(2).split(r"\\"):
                for cell in row.split("&"):
                    if cell.strip() and not math_check(cell.strip(), pt):
                        return False
            pos = m.end()
        return math_check(inner[pos:], pt) if inner[pos:].strip(" ,") else True
    if not body.startswith("$"):
        body = "$" + body + "$"
    try:
        parser = mathtext.MathTextParser("path")
        parser.parse(body, dpi=DPI, prop=FontProperties(size=pt))
        return True
    except Exception:
        return False
