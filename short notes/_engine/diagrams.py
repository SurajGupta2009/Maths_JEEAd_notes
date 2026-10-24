"""Native diagram builders (matplotlib, vector construction -> 300-DPI PNG).

Each builder takes a spec dict and target width in pixels, returns a PIL image.
Every diagram labels axes/parameters/constraints explicitly.
"""
from __future__ import annotations

import ast
import json
from io import BytesIO

import numpy as np
from PIL import Image

DPI = 300

NAVY = "#16295C"
TEAL = "#0F766E"
RED = "#B91C1C"
GOLD = "#B8860B"
GRAY = "#5B6B84"
LIGHT = "#C8D4E6"


def _fig_to_img(fig, width_px: int) -> Image.Image:
    fig.canvas.draw()
    bb = fig.bbox_inches
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, transparent=False,
                facecolor="white", bbox_inches="tight", pad_inches=0.02)
    import matplotlib.pyplot as plt
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf).convert("RGB")
    if img.width != width_px:
        h = int(img.height * width_px / img.width)
        img = img.resize((width_px, h), Image.LANCZOS)
    return img


def _mkfig(width_px: int, height_px: int):
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(width_px / DPI, height_px / DPI), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor("white")
    return fig, ax


# ---------------------------------------------------------------- venn2
VENN2_REGIONS = {
    "Aonly": ["10"], "Bonly": ["01"], "AnB": ["11"],
    "AorB": ["10", "01", "11"], "AminusB": ["10"], "BminusA": ["01"],
    "AdB": ["10", "11"], "BdA": ["01", "11"],
    "AxB_sym": ["10", "01"],  # symmetric difference
}


def venn2(spec: dict, width_px: int) -> Image.Image:
    fig, ax = _mkfig(width_px, int(width_px * 0.66))
    shade = spec.get("shade", [])
    if isinstance(shade, str):
        shade = [shade]
    shaded = set()
    for s in shade:
        shaded |= set(VENN2_REGIONS.get(s, []))
    from matplotlib.patches import Circle

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ylw = "#FFE58F"
    ylw2 = "#F6C445"
    cA = Circle((3.85, 3.15), 2.45, facecolor="none", edgecolor="none")
    cB = Circle((6.15, 3.15), 2.45, facecolor="none", edgecolor="none")
    # fill lobes with clipping so shading never leaves the circles
    fillA = Circle((3.85, 3.15), 2.45, facecolor=ylw, edgecolor="none", zorder=1)
    fillB = Circle((6.15, 3.15), 2.45, facecolor=ylw, edgecolor="none", zorder=1)
    lens_in_A = Circle((6.15, 3.15), 2.45, facecolor=ylw2, edgecolor="none", zorder=2)
    lens_white = Circle((6.15, 3.15), 2.45, facecolor="white", edgecolor="none", zorder=2)
    if "10" in shaded and "01" in shaded and "11" not in shaded:
        ax.add_patch(fillA)
        ax.add_patch(fillB)
        lens_white.set_clip_path(Circle((3.85, 3.15), 2.45, transform=ax.transData))
        ax.add_patch(lens_white)
    else:
        if "10" in shaded:
            ax.add_patch(fillA)
            erase = Circle((6.15, 3.15), 2.45, facecolor="white", edgecolor="none",
                           zorder=2)
            erase.set_clip_path(Circle((3.85, 3.15), 2.45, transform=ax.transData))
            ax.add_patch(erase)
        if "01" in shaded:
            ax.add_patch(fillB)
            erase = Circle((3.85, 3.15), 2.45, facecolor="white", edgecolor="none",
                           zorder=2)
            erase.set_clip_path(Circle((6.15, 3.15), 2.45, transform=ax.transData))
            ax.add_patch(erase)
        if "11" in shaded:
            lens_in_A.set_clip_path(Circle((3.85, 3.15), 2.45, transform=ax.transData))
            ax.add_patch(lens_in_A)
    c1 = Circle((3.85, 3.15), 2.45, facecolor="none", edgecolor=TEAL, lw=3.2, zorder=3)
    c2 = Circle((6.15, 3.15), 2.45, facecolor="none", edgecolor=NAVY, lw=3.2, zorder=3)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(2.15, 4.9, spec.get("A", "A"), fontsize=16, color=TEAL,
            ha="center", va="center", style="italic", weight="bold")
    ax.text(7.85, 4.9, spec.get("B", "B"), fontsize=16, color=NAVY,
            ha="center", va="center", style="italic", weight="bold")
    pos_map = {"10": (3.15, 2.5), "01": (6.85, 2.5), "11": (5.0, 2.5),
               "Aonly": (3.15, 2.5), "Bonly": (6.85, 2.5), "AnB": (5.0, 2.5)}
    for lab, key in spec.get("labels", {}).items():
        pos = pos_map.get(key, (5.0, 2.5))
        ax.text(pos[0], pos[1], lab, fontsize=13, color=NAVY,
                ha="center", va="center", weight="bold")
    ax.text(0.25, 0.4, spec.get("universe", "Universe U (rectangle not shown)"),
            fontsize=10, color=GRAY, ha="left", va="center")
    if spec.get("title"):
        ax.text(5.0, 6.25, spec["title"], fontsize=12, color=TEAL,
                ha="center", va="center", weight="bold")
    return _fig_to_img(fig, width_px)


# ---------------------------------------------------------------- venn3
def venn3(spec: dict, width_px: int) -> Image.Image:
    fig, ax = _mkfig(width_px, int(width_px * 0.78))
    from matplotlib.patches import Circle
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")
    R = 2.05
    centers = [(5.0, 5.1, "A", TEAL), (3.65, 2.85, "B", NAVY), (6.35, 2.85, "C", RED)]
    for cx, cy, name, col in centers:
        ax.add_patch(Circle((cx, cy), R, facecolor="none", edgecolor=col, lw=3.0))
    ax.text(5.0, 7.35, "A", fontsize=15, color=TEAL, ha="center", weight="bold", style="italic")
    ax.text(2.35, 1.55, "B", fontsize=15, color=NAVY, ha="center", weight="bold", style="italic")
    ax.text(7.65, 1.55, "C", fontsize=15, color=RED, ha="center", weight="bold", style="italic")
    # region labels (classic 7-region layout)
    pos = {
        "Aonly": (5.0, 6.1), "Bonly": (3.0, 2.0), "Conly": (7.0, 2.0),
        "ABn": (3.75, 3.9), "ACn": (6.25, 3.9), "BCn": (5.0, 2.15), "ABCn": (5.0, 3.55),
    }
    for r, (x, y) in pos.items():
        lab = spec.get("labels", {}).get(r, "")
        if lab:
            ax.text(x, y, lab, fontsize=11, color=NAVY, ha="center", va="center", weight="bold")
    if spec.get("title"):
        ax.text(5.0, 0.45, spec["title"], fontsize=11.5, color=TEAL,
                ha="center", va="center", weight="bold")
    return _fig_to_img(fig, width_px)


# ---------------------------------------------------------------- number line
def numberline(spec: dict, width_px: int) -> Image.Image:
    fig, ax = _mkfig(width_px, int(width_px * 0.30))
    lo, hi = spec.get("range", [-6.5, 6.5])
    ax.set_xlim(lo, hi)
    ax.set_ylim(-1.35, 1.35)
    ax.axhline(0, color=NAVY, lw=2.4)
    ax.annotate("", xy=(hi - 0.15, 0), xytext=(hi - 0.75, 0),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2.2))
    ticks = spec.get("ticks")
    if ticks is None:
        ticks = [t for t in range(int(np.floor(lo)) + 1, int(np.ceil(hi)))]
    for t in ticks:
        ax.plot([t, t], [-0.12, 0.12], color=NAVY, lw=1.8)
        ax.text(t, -0.42, str(t), fontsize=11, color=NAVY, ha="center", va="top")
    for item in spec.get("items", []):
        kind = item.get("kind", "interval")
        col = item.get("color", TEAL)
        y = item.get("y", 0.32)
        if kind == "interval":
            a, b = item["a"], item["b"]
            ax.plot([a, b], [y, y], color=col, lw=6, solid_capstyle="butt",
                    alpha=0.75, zorder=2)
            ax.plot([a], [y], "o" if item.get("closed_a", True) else "o",
                    markersize=11, markerfacecolor=col if item.get("closed_a", True) else "white",
                    markeredgecolor=col, zorder=3)
            ax.plot([b], [y], "o" if item.get("closed_b", True) else "o",
                    markersize=11, markerfacecolor=col if item.get("closed_b", True) else "white",
                    markeredgecolor=col, zorder=3)
            ax.text(item.get("label_x", (a + b) / 2), item.get("label_y", y + 0.34),
                    item.get("label", ""), fontsize=11.5, color=col,
                    ha="center", va="bottom", weight="bold")
        elif kind == "points":
            for x in item["xs"]:
                ax.plot([x], [y], "o", markersize=11, markerfacecolor=col,
                        markeredgecolor=col, zorder=3)
            ax.text(item.get("label_x", np.mean(item["xs"]) if item["xs"] else 0),
                    item.get("label_y", y + 0.34), item.get("label", ""),
                    fontsize=11.5, color=col, ha="center", va="bottom", weight="bold")
    if spec.get("xlabel"):
        ax.text(hi - 0.2, -0.95, spec["xlabel"], fontsize=11, color=GRAY, ha="right")
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12, color=TEAL, pad=10, weight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    return _fig_to_img(fig, width_px)


# ---------------------------------------------------------------- mapping
def mapping(spec: dict, width_px: int) -> Image.Image:
    fig, ax = _mkfig(width_px, int(width_px * 0.58))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
    A = spec.get("A", [])
    B = spec.get("B", [])
    arrows = spec.get("arrows", [])  # [[a, b], ...]
    nA, nB = max(len(A), 1), max(len(B), 1)
    posA, posB = {}, {}
    for i, a in enumerate(A):
        y = 5.9 - i * (3.8 / max(nA - 1, 1)) if nA > 1 else 3.6
        posA[str(a)] = (2.2, y)
    for i, b in enumerate(B):
        y = 5.9 - i * (3.8 / max(nB - 1, 1)) if nB > 1 else 3.6
        posB[str(b)] = (7.6, y)
    for name, pos, col, lab in [(spec.get("Aname", "A"), posA, TEAL, spec.get("Aname", "A")),
                                (spec.get("Bname", "B"), posB, NAVY, spec.get("Bname", "B"))]:
        xs = [p[0] for p in pos.values()] or [2.2]
        ys = [p[1] for p in pos.values()] or [3.0]
        cx = np.mean(xs)
        w = 1.5
        h = max(4.6, max(ys) - min(ys) + 1.5) if pos else 4.6
        cy = np.mean(ys) if pos else 3.6
        e = Ellipse((cx, cy), w * 2, h, facecolor="#F4F8FC", edgecolor=col, lw=2.6)
        ax.add_patch(e)
        ax.text(cx, cy + h / 2 + 0.28, lab, fontsize=13, color=col,
                ha="center", va="bottom", weight="bold", style="italic")
    for a, p in posA.items():
        ax.text(p[0], p[1], a, fontsize=12.5, color=NAVY, ha="center", va="center")
    for b, p in posB.items():
        ax.text(p[0], p[1], b, fontsize=12.5, color=NAVY, ha="center", va="center")
    for a, b in arrows:
        pa, pb = posA.get(str(a)), posB.get(str(b))
        if pa and pb:
            ax.add_patch(FancyArrowPatch(pa, pb, arrowstyle="-|>",
                                         mutation_scale=16, lw=2.0, color=RED,
                                         shrinkA=8, shrinkB=8,
                                         connectionstyle="arc3,rad=0.12"))
    if spec.get("title"):
        ax.text(5.0, 0.45, spec["title"], fontsize=11.5, color=TEAL,
                ha="center", va="center", weight="bold")
    return _fig_to_img(fig, width_px)


# ---------------------------------------------------------------- compose (f:A->B->C)
def compose(spec: dict, width_px: int) -> Image.Image:
    fig, ax = _mkfig(width_px, int(width_px * 0.34))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.4)
    ax.axis("off")
    from matplotlib.patches import FancyArrowPatch, Ellipse
    names = [spec.get("Aname", "A"), spec.get("Bname", "B"), spec.get("Cname", "C")]
    cols = [TEAL, NAVY, RED]
    xs = [1.6, 5.0, 8.4]
    for x, name, col in zip(xs, names, cols):
        e = Ellipse((x, 1.7), 1.7, 2.1, facecolor="#F4F8FC", edgecolor=col, lw=2.6)
        ax.add_patch(e)
        ax.text(x, 1.7, name, fontsize=14, color=col, ha="center", va="center",
                weight="bold", style="italic")
    for x0, x1, lab, col in [(2.55, 4.15, spec.get("f", "f"), RED),
                             (5.85, 7.55, spec.get("g", "g"), RED)]:
        ax.add_patch(FancyArrowPatch((x0, 1.7), (x1, 1.7), arrowstyle="-|>",
                                     mutation_scale=18, lw=2.2, color=col))
        ax.text((x0 + x1) / 2, 2.05, lab, fontsize=12.5, color=col,
                ha="center", va="bottom", weight="bold", style="italic")
    ax.add_patch(FancyArrowPatch((2.55, 1.15), (7.55, 1.15), arrowstyle="-|>",
                                 mutation_scale=18, lw=2.0, color=TEAL,
                                 connectionstyle="arc3,rad=-0.35"))
    ax.text(5.05, 0.28, spec.get("comp", "g ∘ f"), fontsize=12.5, color=TEAL,
            ha="center", va="center", weight="bold", style="italic")
    return _fig_to_img(fig, width_px)


# ---------------------------------------------------------------- graph
_SAFE_FUNCS = {
    "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp,
    "log": np.log, "sqrt": np.sqrt, "abs": np.abs, "floor": np.floor,
    "asin": np.arcsin, "acos": np.arccos, "atan": np.arctan,
    "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
    "pi": np.pi, "e": np.e,
}


def _eval_expr(expr: str, x: np.ndarray, y: np.ndarray | None = None) -> np.ndarray:
    """Evaluate a restricted arithmetic expression in x and, optionally, y."""
    allowed = {k: v for k, v in _SAFE_FUNCS.items()}
    allowed["x"] = x
    if y is not None:
        allowed["y"] = y
    tree = ast.parse(expr, mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call,
                                 ast.Name, ast.Constant, ast.Load, ast.Add, ast.Sub,
                                 ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd,
                                 ast.Mod, ast.FloorDiv, ast.Compare, ast.Gt, ast.Lt,
                                 ast.GtE, ast.LtE, ast.Eq, ast.NotEq, ast.IfExp,
                                 ast.BoolOp, ast.And, ast.Or, ast.BitAnd, ast.BitOr)):
            raise ValueError(f"disallowed expression element: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id not in allowed:
            raise ValueError(f"unknown name {node.id}")
        if isinstance(node, ast.Call) and not isinstance(node.func, ast.Name):
            raise ValueError("only simple calls allowed")
    code = compile(tree, "<expr>", "eval")
    return eval(code, {"__builtins__": {}}, allowed)


def graph(spec: dict, width_px: int) -> Image.Image:
    ratio = spec.get("ratio", 0.62)
    fig, ax = _mkfig(width_px, int(width_px * ratio))
    xr = spec.get("xrange", [-6, 6])
    yr = spec.get("yrange", [-4, 4])
    ax.set_xlim(*xr)
    ax.set_ylim(*yr)
    ax.axhline(0, color=GRAY, lw=1.4)
    ax.axvline(0, color=GRAY, lw=1.4)
    # grid
    gx = spec.get("xticks")
    gy = spec.get("yticks")
    if gx is None:
        gx = [v for v in range(int(np.floor(xr[0])), int(np.ceil(xr[1])) + 1)]
    if gy is None:
        gy = [v for v in range(int(np.floor(yr[0])), int(np.ceil(yr[1])) + 1)]
    ax.set_xticks(gx)
    ax.set_yticks(gy)
    if spec.get("xticklabels"):
        ax.set_xticklabels(spec["xticklabels"], fontsize=11.5)
    if spec.get("yticklabels"):
        ax.set_yticklabels(spec["yticklabels"], fontsize=11.5)
    ax.tick_params(labelsize=11.5, colors=NAVY)
    ax.grid(True, color="#E3E9F2", lw=0.9)
    for s in ax.spines.values():
        s.set_color(LIGHT)
    ax.text(xr[1] - 0.15, yr[0] + 0.18, spec.get("xlabel", "x"), fontsize=12,
            color=NAVY, ha="right", va="bottom", style="italic", weight="bold")
    ax.text(xr[0] + 0.15, yr[1] - 0.15, spec.get("ylabel", "y"), fontsize=12,
            color=NAVY, ha="left", va="top", style="italic", weight="bold")
    for v in spec.get("vlines", []):   # vertical asymptote
        x = v["x"]
        ax.axvline(x, color=RED, lw=1.8, ls=(0, (6, 5)))
        ax.text(x + v.get("dx", 0), yr[1] - 0.25 + v.get("dy", 0),
                v.get("label", ""), fontsize=11, color=RED,
                ha=v.get("ha", "center"), va=v.get("va", "top"))
    for h in spec.get("hlines", []):   # horizontal asymptote
        y = h["y"]
        ax.axhline(y, color=RED, lw=1.8, ls=(0, (6, 5)))
        ax.text(xr[1] - 0.15, y, h.get("label", ""), fontsize=11, color=RED,
                ha="right", va="bottom")
    # Editable slope fields: short, unarrowed line elements centred on a grid.
    # Invalid/infinite slopes are omitted, so domain boundaries remain visible.
    for field in spec.get("slope_fields", []):
        from matplotlib.collections import LineCollection
        fx0, fx1 = field.get("xrange", xr)
        fy0, fy1 = field.get("yrange", yr)
        nx, ny = int(field.get("nx", 17)), int(field.get("ny", 13))
        gx, gy = np.linspace(fx0, fx1, nx), np.linspace(fy0, fy1, ny)
        X, Y = np.meshgrid(gx, gy)
        with np.errstate(all="ignore"):
            slopes = _eval_expr(field["expr"], X, Y)
        finite = np.isfinite(slopes)
        if "max_slope" in field:
            finite &= np.abs(slopes) <= float(field["max_slope"])
        spacing = min((fx1 - fx0) / max(nx - 1, 1),
                      (fy1 - fy0) / max(ny - 1, 1))
        length = float(field.get("length", 0.34 * spacing))
        angles = np.arctan(slopes)
        dx, dy = 0.5 * length * np.cos(angles), 0.5 * length * np.sin(angles)
        segments = [
            [(float(x - ddx), float(y - ddy)),
             (float(x + ddx), float(y + ddy))]
            for x, y, ddx, ddy, keep in zip(
                X.ravel(), Y.ravel(), dx.ravel(), dy.ravel(), finite.ravel())
            if keep
        ]
        ax.add_collection(LineCollection(
            segments, colors=field.get("color", GRAY),
            linewidths=field.get("lw", 1.15), alpha=field.get("alpha", 0.42),
            zorder=field.get("zorder", 0.35), capstyle="round"))
    # Optional editable area primitives. They are drawn before curves so the
    # mathematical boundaries remain crisp; existing specs are unaffected.
    for rect in spec.get("rectangles", []):
        from matplotlib.patches import Rectangle
        patch = Rectangle((rect["x"], rect.get("y0", 0)), rect["width"], rect["height"],
                          facecolor=rect.get("color", "#F6C445"),
                          edgecolor=rect.get("edge", GOLD),
                          alpha=rect.get("alpha", 0.28), lw=rect.get("lw", 1.4),
                          zorder=rect.get("zorder", 0.7))
        ax.add_patch(patch)
    for fill in spec.get("fills", []):
        xs = np.linspace(fill["from"], fill["to"], int(fill.get("n", 600)))
        with np.errstate(all="ignore"):
            raw_y1 = fill.get("y1", 0)
            raw_y2 = fill["y2"]
            y1 = (_eval_expr(raw_y1, xs) if isinstance(raw_y1, str)
                  else np.full_like(xs, float(raw_y1)))
            y2 = (_eval_expr(raw_y2, xs) if isinstance(raw_y2, str)
                  else np.full_like(xs, float(raw_y2)))
        ax.fill_between(xs, y1, y2, color=fill.get("color", "#F6C445"),
                        alpha=fill.get("alpha", 0.24), zorder=fill.get("zorder", 0.6))
    for c in spec.get("curves", []):
        xs = np.linspace(c.get("from", xr[0]), c.get("to", xr[1]), int(c.get("n", 600)))
        with np.errstate(all="ignore"):
            ys = _eval_expr(c["expr"], xs)
            clip = c.get("clip")
            if clip is not None:
                ys = np.where(np.abs(ys) > float(clip), np.nan, ys)
        col = c.get("color", TEAL)
        ax.plot(xs, ys, color=col, lw=c.get("lw", 2.8), ls=c.get("ls", "-"),
                label=c.get("label", None))
        if c.get("label"):
            idx = int(len(xs) * c.get("labpos", 0.82))
            if np.isfinite(ys[idx]):
                ax.text(xs[idx] + c.get("label_dx", 0),
                        ys[idx] + c.get("label_dy", 0), " " + c["label"],
                        fontsize=12.5, color=col, ha=c.get("label_ha", "left"),
                        va=c.get("label_va", "center"), weight="bold")
    for p in spec.get("points", []):
        ax.plot([p["x"]], [p["y"]], "o", color=p.get("color", NAVY), markersize=9,
                markerfacecolor=p.get("face", p.get("color", NAVY)))
        ax.text(p["x"] + p.get("dx", 0.22), p["y"] + p.get("dy", 0.28),
                p.get("label", ""), fontsize=11.5, color=p.get("color", NAVY),
                ha=p.get("ha", "left"), va="bottom", weight="bold")
    for r in spec.get("rays", []):
        ax.plot(r["x"], r["y"], color=r.get("color", GOLD), lw=2.2, ls=(0, (4, 3)))
        ax.text(np.mean(r["x"]), np.mean(r["y"]) + 0.12, r.get("label", ""),
                fontsize=10.5, color=r.get("color", GOLD), ha="center", va="bottom")
    for ann in spec.get("annotations", []):
        ax.annotate(ann["text"], xy=(ann["x"], ann["y"]),
                    xytext=(ann.get("tx", ann["x"] + 0.4), ann.get("ty", ann["y"] + 0.8)),
                    fontsize=11.5, color=ann.get("color", NAVY), weight="bold",
                    arrowprops=dict(arrowstyle="-|>", color=ann.get("color", NAVY), lw=1.6))
    for band in spec.get("bands", []):
        ax.axvspan(band["a"], band["b"], color=band.get("color", "#FFF3B0"),
                   alpha=band.get("alpha", 0.55), zorder=0)
        if band.get("label"):
            ax.text((band["a"] + band["b"]) / 2, yr[0] + 0.35, band["label"],
                    fontsize=10, color=GOLD, ha="center", va="bottom", weight="bold")
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12, color=TEAL, pad=12, weight="bold")
    return _fig_to_img(fig, width_px)




# ---------------------------------------------------------------- unit circle
def unitcircle(spec: dict, width_px: int) -> Image.Image:
    from matplotlib.patches import Circle
    fig, ax = _mkfig(width_px, int(width_px * 0.92))
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-1.95, 2.25)
    ax.set_aspect("equal")
    ax.axis("off")

    th = np.deg2rad(spec.get("angle_deg", 38))
    ax.add_patch(Circle((0, 0), 1, fill=False, color=TEAL, lw=3.0, zorder=3))
    ax.annotate("", xy=(2.0, 0), xytext=(-2.0, 0),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.7))
    ax.annotate("", xy=(0, 2.15), xytext=(0, -1.9),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.7))
    ax.text(1.95, -0.22, "x", fontsize=13, color=NAVY, weight="bold", style="italic")
    ax.text(0.14, 2.08, "y", fontsize=13, color=NAVY, weight="bold", style="italic")
    ax.text(-0.22, -0.30, "O", fontsize=12.5, color=NAVY, weight="bold",
            ha="right", va="top")

    cx, cy = np.cos(th), np.sin(th)
    ax.plot([0, cx], [0, cy], color=NAVY, lw=2.8, zorder=4)
    ax.plot([cx], [cy], "o", color=RED, markersize=10, zorder=5)
    ax.plot([cx, cx], [0, cy], color=GRAY, lw=1.6, ls=(0, (4, 3)), zorder=2)
    ax.plot([0, cx], [cy, cy], color=GRAY, lw=1.6, ls=(0, (4, 3)), zorder=2)
    ax.text(cx / 2 + 0.10, -0.30, spec.get("cos_label", r"$\cos\theta$"),
            fontsize=12, color=NAVY, ha="center", weight="bold")
    ax.text(-0.22, cy / 2, spec.get("sin_label", r"$\sin\theta$"), fontsize=12,
            color=NAVY, ha="right", weight="bold")
    arc = np.linspace(0, th, 60)
    ax.plot(0.32 * np.cos(arc), 0.32 * np.sin(arc), color=RED, lw=2.0)
    ax.text(0.42 * np.cos(th / 2), 0.42 * np.sin(th / 2) - 0.03,
            spec.get("angle_label", r"$\theta$"), fontsize=13, color=RED,
            weight="bold", ha="center")
    ax.text(cx + 0.12, cy + 0.12,
            spec.get("point_label", r"$P(\cos\theta,\;\sin\theta)$"),
            fontsize=12, color=NAVY, weight="bold")

    if spec.get("quadrants", True):
        pos = {"I": (1.32, 1.32), "II": (-1.32, 1.32), "III": (-1.32, -1.32),
               "IV": (1.32, -1.32)}
        for q, (qx, qy) in pos.items():
            ax.text(qx, qy, q, fontsize=14, color=TEAL, weight="bold",
                    ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.18", fc="#EAF4F4", ec=TEAL, lw=1.2))
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)

# ---------------------------------------------------------------- blocks (partition)
def blocks(spec: dict, width_px: int) -> Image.Image:
    groups = spec.get("groups", [])
    n = max(len(groups), 1)
    fig, ax = _mkfig(width_px, int(width_px * (0.22 + 0.16 * n)))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.2 + 1.35 * n)
    ax.axis("off")
    from matplotlib.patches import FancyBboxPatch
    for i, g in enumerate(groups):
        y = 1.2 + 1.35 * (n - 1 - i)
        box = FancyBboxPatch((1.2, y), 7.6, 1.05,
                             boxstyle="round,pad=0.06,rounding_size=0.12",
                             facecolor="#F4F8FC", edgecolor=TEAL, lw=2.2)
        ax.add_patch(box)
        ax.text(0.55, y + 0.52, g.get("label", ""), fontsize=12.5, color=TEAL,
                ha="center", va="center", weight="bold", style="italic")
        members = " , ".join(str(m) for m in g.get("members", []))
        fs = 12.0
        while fs > 7:
            t = ax.text(5.0, y + 0.52, members, fontsize=fs, color=NAVY,
                        ha="center", va="center")
            fig.canvas.draw()
            bb = t.get_window_extent()
            if bb.width / (fig.get_figwidth() * DPI) < 0.74:
                break
            t.remove()
            fs -= 0.75
    if spec.get("title"):
        ax.text(5.0, 0.35, spec["title"], fontsize=11.5, color=TEAL,
                ha="center", va="center", weight="bold")
    return _fig_to_img(fig, width_px)


# ---------------------------------------------------------------- dispatcher
BUILDERS = {
    "venn2": venn2, "venn3": venn3, "numberline": numberline,
    "mapping": mapping, "compose": compose, "graph": graph, "blocks": blocks,
    "unitcircle": unitcircle,
}


def build_diagram(spec: dict | str, width_px: int) -> Image.Image:
    if isinstance(spec, str):
        spec = json.loads(spec)
    t = spec["type"]
    if t in BUILDERS:
        img = BUILDERS[t](spec, width_px)
    else:
        from visual_builders import VISUAL_BUILDERS
        if t not in VISUAL_BUILDERS:
            raise ValueError(f"unknown diagram type: {t}")
        img = VISUAL_BUILDERS[t](spec, width_px)
    from visual_builders import with_caption
    return with_caption(img, spec)
