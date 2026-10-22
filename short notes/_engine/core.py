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
    if not body.startswith("$"):
        body = "$" + body + "$"
    try:
        parser = mathtext.MathTextParser("path")
        parser.parse(body, dpi=DPI, prop=FontProperties(size=pt))
        return True
    except Exception:
        return False
