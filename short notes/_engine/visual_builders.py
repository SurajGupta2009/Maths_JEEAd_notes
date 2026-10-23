"""Additional editable visual builders for the expanded notebook lessons."""
from __future__ import annotations

import math
import textwrap

import numpy as np
from PIL import Image, ImageDraw

from diagrams import DPI, GOLD, GRAY, LIGHT, NAVY, RED, TEAL, _fig_to_img, _mkfig


def geometry(spec: dict, width_px: int) -> Image.Image:
    """General labelled coordinate/Euclidean construction."""
    from matplotlib.patches import Circle, FancyArrowPatch, Polygon

    fig, ax = _mkfig(width_px, int(width_px * spec.get("ratio", 0.68)))
    xr, yr = spec.get("xrange", [-5, 5]), spec.get("yrange", [-4, 4])
    ax.set_xlim(*xr)
    ax.set_ylim(*yr)
    if spec.get("equal", True):
        ax.set_aspect("equal")
    if spec.get("axes", True):
        ax.axhline(0, color=GRAY, lw=1.3, zorder=0)
        ax.axvline(0, color=GRAY, lw=1.3, zorder=0)
    else:
        ax.axis("off")
    if spec.get("grid", False):
        ax.set_xticks(spec.get("xticks", list(range(int(np.ceil(xr[0])), int(xr[1]) + 1))))
        ax.set_yticks(spec.get("yticks", list(range(int(np.ceil(yr[0])), int(yr[1]) + 1))))
        ax.grid(True, color="#E3E9F2", lw=0.8, zorder=-2)
        ax.tick_params(labelsize=10, colors=NAVY)
    else:
        ax.set_xticks([])
        ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    for el in spec.get("elements", []):
        kind = el.get("kind")
        col = el.get("color", TEAL)
        lw, ls, z = el.get("lw", 2.4), el.get("ls", "-"), el.get("z", 3)
        if kind in ("segment", "ray", "line"):
            a = np.array(el["a"], dtype=float)
            b = np.array(el["b"], dtype=float)
            direction = b - a
            if np.allclose(direction, 0):
                raise ValueError("line/ray endpoints must be distinct")
            if kind == "segment":
                pts = np.array([a, b])
            else:
                ts = np.array([0.0, 1.0]) if kind == "ray" else np.array([-100.0, 100.0])
                pts = np.array([a + ts[0] * direction, a + ts[1] * direction])
            ax.plot(pts[:, 0], pts[:, 1], color=col, lw=lw, ls=ls,
                    solid_capstyle="round", zorder=z)
            if el.get("label"):
                t = el.get("label_pos", 0.5)
                q = a + t * direction
                ax.text(q[0] + el.get("dx", 0.12), q[1] + el.get("dy", 0.16),
                        el["label"], fontsize=el.get("fontsize", 11.5), color=col,
                        ha=el.get("ha", "left"), va=el.get("va", "bottom"),
                        weight="bold", zorder=z + 1)
        elif kind == "point":
            x, y = el["at"]
            ax.plot([x], [y], "o", ms=el.get("size", 8),
                    markerfacecolor=el.get("face", col), markeredgecolor=col,
                    markeredgewidth=1.8, zorder=z + 2)
            if el.get("label"):
                ax.text(x + el.get("dx", 0.14), y + el.get("dy", 0.16), el["label"],
                        fontsize=el.get("fontsize", 11.5),
                        color=el.get("label_color", NAVY),
                        ha=el.get("ha", "left"), va=el.get("va", "bottom"),
                        weight="bold", zorder=z + 3)
        elif kind == "circle":
            centre = tuple(el.get("centre", el.get("center", [0, 0])))
            ax.add_patch(Circle(centre, el["r"], facecolor=el.get("fill", "none"),
                                edgecolor=col, lw=lw, ls=ls,
                                alpha=el.get("alpha", 1), zorder=z))
            if el.get("label"):
                angle = np.deg2rad(el.get("label_angle", 45))
                ax.text(centre[0] + el["r"] * np.cos(angle) + el.get("dx", 0),
                        centre[1] + el["r"] * np.sin(angle) + el.get("dy", 0),
                        el["label"], fontsize=el.get("fontsize", 11.5), color=col,
                        weight="bold", ha=el.get("ha", "left"),
                        va=el.get("va", "bottom"))
        elif kind == "polygon":
            ax.add_patch(Polygon(el["points"], closed=True,
                                 facecolor=el.get("fill", "none"), edgecolor=col,
                                 lw=lw, alpha=el.get("alpha", 1), zorder=z))
        elif kind == "arrow":
            a, b = tuple(el["a"]), tuple(el["b"])
            ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=18,
                                         lw=lw, color=col, zorder=z))
            if el.get("label"):
                ax.text((a[0] + b[0]) / 2 + el.get("dx", 0.1),
                        (a[1] + b[1]) / 2 + el.get("dy", 0.1), el["label"],
                        fontsize=el.get("fontsize", 11.5), color=col,
                        ha=el.get("ha", "left"), weight="bold")
        else:
            raise ValueError(f"unknown geometry element: {kind}")
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12.5, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)


def bars(spec: dict, width_px: int) -> Image.Image:
    fig, ax = _mkfig(width_px, int(width_px * spec.get("ratio", 0.56)))
    labels, values = spec.get("labels", []), spec.get("values", [])
    if not values or len(labels) != len(values):
        raise ValueError("bars needs matching nonempty labels and values")
    x = np.arange(len(values))
    colors = spec.get("colors", [TEAL] * len(values))
    if isinstance(colors, str):
        colors = [colors] * len(values)
    ax.bar(x, values, color=colors, width=spec.get("bar_width", 0.68), zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=spec.get("tick_fontsize", 10.5))
    ax.tick_params(axis="y", labelsize=10.5, colors=NAVY)
    ax.grid(axis="y", color="#E3E9F2", lw=0.9, zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(LIGHT)
    if spec.get("hline") is not None:
        ax.axhline(spec["hline"], color=RED, ls="--", lw=1.8)
        if spec.get("hline_label"):
            ax.text(len(values) - 0.5, spec["hline"], spec["hline_label"],
                    color=RED, ha="right", va="bottom", fontsize=11, weight="bold")
    if spec.get("value_labels", True):
        span = max(values) - min(0, min(values)) or 1
        for xi, value in zip(x, values):
            ax.text(xi, value + 0.025 * span,
                    spec.get("value_format", "{}").format(value),
                    ha="center", va="bottom", fontsize=spec.get("value_fontsize", 10.5),
                    color=NAVY, weight="bold")
    if spec.get("xlabel"):
        ax.set_xlabel(spec["xlabel"], fontsize=11.5, color=NAVY)
    if spec.get("ylabel"):
        ax.set_ylabel(spec["ylabel"], fontsize=11.5, color=NAVY)
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12.5, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)


def tree(spec: dict, width_px: int) -> Image.Image:
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    nodes = {n["id"]: n for n in spec.get("nodes", [])}
    if not nodes:
        raise ValueError("tree needs nodes")
    fig, ax = _mkfig(width_px, int(width_px * spec.get("ratio", 0.62)))
    xs = [float(n["at"][0]) for n in nodes.values()]
    ys = [float(n["at"][1]) for n in nodes.values()]
    ww, hh = spec.get("node_width", 1.8), spec.get("node_height", 0.65)
    ax.set_xlim(min(xs) - ww, max(xs) + ww)
    ax.set_ylim(min(ys) - 1.0, max(ys) + 1.0)
    ax.axis("off")
    for edge in spec.get("edges", []):
        a, b = nodes[edge["from"]]["at"], nodes[edge["to"]]["at"]
        ax.add_patch(FancyArrowPatch(tuple(a), tuple(b), arrowstyle="-|>",
                                     mutation_scale=15, lw=edge.get("lw", 1.8),
                                     color=edge.get("color", GRAY), shrinkA=18,
                                     shrinkB=18, zorder=1))
        if edge.get("label"):
            t = edge.get("label_pos", 0.5)
            ax.text(a[0] + t * (b[0] - a[0]) + edge.get("dx", 0),
                    a[1] + t * (b[1] - a[1]) + edge.get("dy", 0.12), edge["label"],
                    fontsize=edge.get("fontsize", 10.5),
                    color=edge.get("label_color", NAVY),
                    ha=edge.get("ha", "center"), va="bottom", weight="bold", zorder=4,
                    bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.6))
    for node in nodes.values():
        x, y = node["at"]
        col = node.get("color", TEAL)
        ax.add_patch(FancyBboxPatch((x - ww / 2, y - hh / 2), ww, hh,
                                    boxstyle="round,pad=.06,rounding_size=.1",
                                    fc=node.get("fill", "#F4F8FC"), ec=col, lw=2, zorder=2))
        label = textwrap.fill(str(node.get("label", node["id"])),
                              width=node.get("wrap", 18))
        ax.text(x, y, label, fontsize=node.get("fontsize", 10.5),
                color=node.get("label_color", NAVY), ha="center", va="center",
                weight="bold", zorder=3)
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12.5, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)


def flow(spec: dict, width_px: int) -> Image.Image:
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    steps = spec.get("steps", [])
    if not steps:
        raise ValueError("flow needs steps")
    n = len(steps)
    fig, ax = _mkfig(width_px, int(width_px * spec.get("ratio", 0.19 * n + 0.12)))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.55 * n + 0.35)
    ax.axis("off")
    for i, step in enumerate(steps):
        y = 1.55 * (n - 1 - i) + 0.45
        col = TEAL if i == 0 else NAVY
        ax.add_patch(FancyBboxPatch((1.35, y), 7.3, 1.02,
                                    boxstyle="round,pad=.06,rounding_size=.12",
                                    fc="#F4F8FC" if i else "#E6F4F3", ec=col, lw=2.2))
        ax.text(1.85, y + 0.51, str(i + 1), fontsize=13, color="white",
                ha="center", va="center", weight="bold",
                bbox=dict(boxstyle="circle,pad=.32", fc=col, ec=col))
        ax.text(2.5, y + 0.72, step.get("title", ""), fontsize=12.2,
                color=col, ha="left", va="center", weight="bold")
        detail = textwrap.fill(step.get("detail", ""), width=step.get("wrap", 76))
        ax.text(2.5, y + 0.33, detail, fontsize=10.4, color=NAVY,
                ha="left", va="center")
        if i < n - 1:
            ax.add_patch(FancyArrowPatch((5, y - 0.02), (5, y - 0.48),
                                         arrowstyle="-|>", mutation_scale=18,
                                         lw=2, color=GOLD))
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12.5, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)


def pascal(spec: dict, width_px: int) -> Image.Image:
    rows = spec.get("rows", 6)
    fig, ax = _mkfig(width_px, int(width_px * spec.get("ratio", 0.62)))
    ax.set_xlim(-rows / 2 - 0.8, rows / 2 + 0.8)
    ax.set_ylim(-0.8, rows + 0.25)
    ax.axis("off")
    highlight = {tuple(x) for x in spec.get("highlight", [])}
    for n in range(rows):
        for k in range(n + 1):
            x, y = k - n / 2, rows - 1 - n
            chosen = (n, k) in highlight
            ax.text(x, y, str(math.comb(n, k)), fontsize=spec.get("fontsize", 12),
                    color=TEAL if chosen else NAVY, ha="center", va="center",
                    weight="bold",
                    bbox=dict(boxstyle="circle,pad=.28",
                              fc="#FFF3B0" if chosen else "#F4F8FC",
                              ec=GOLD if chosen else LIGHT, lw=1.4))
    if spec.get("labels", True):
        ax.text(-rows / 2 - 0.55, rows - 0.5, "row n", fontsize=10.5,
                color=GRAY, rotation=90, ha="center", va="center")
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12.5, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)


def table(spec: dict, width_px: int) -> Image.Image:
    columns, rows = spec.get("columns", []), spec.get("rows", [])
    if not columns or not rows:
        raise ValueError("table needs columns and rows")
    ratio = spec.get("ratio", 0.16 + 0.085 * (len(rows) + 1))
    fig, ax = _mkfig(width_px, int(width_px * ratio))
    ax.axis("off")
    tbl = ax.table(cellText=rows, colLabels=columns, cellLoc="center", colLoc="center",
                   loc="center", colWidths=spec.get("col_widths"))
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(spec.get("fontsize", 10.5))
    tbl.scale(1, spec.get("row_scale", 1.65))
    for (r, _), cell in tbl.get_celld().items():
        cell.set_edgecolor(LIGHT)
        cell.set_linewidth(1.0)
        if r == 0:
            cell.set_facecolor("#DCEFED")
            cell.set_text_props(color=TEAL, weight="bold")
        else:
            cell.set_facecolor("#F7F9FC" if r % 2 else "white")
            cell.set_text_props(color=NAVY)
        if spec.get("highlight_rows") and r in spec["highlight_rows"]:
            cell.set_facecolor("#FFF3B0")
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for cell in tbl.get_celld().values():
        text = cell.get_text()
        available = cell.get_window_extent(renderer=renderer).width - 18
        size = text.get_fontsize()
        while (text.get_text() and
               text.get_window_extent(renderer=renderer).width > available and size > 7.5):
            size -= 0.5
            text.set_fontsize(size)
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12.5, color=TEAL, pad=10, weight="bold")
    return _fig_to_img(fig, width_px)


def with_caption(img: Image.Image, spec: dict) -> Image.Image:
    caption = spec.get("caption")
    if not caption:
        return img
    from core import HAND, HAND_BOLD, get_font

    label_font = get_font(HAND_BOLD, 30)
    body_font = get_font(HAND, 32)
    words = caption.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if current and body_font.getlength(trial) > img.width - 40:
            lines.append(current)
            current = word
        else:
            current = trial
    if current:
        lines.append(current)
    height = 46 + 45 * len(lines) + 22
    out = Image.new("RGB", (img.width, img.height + height), "white")
    out.paste(img, (0, 0))
    draw = ImageDraw.Draw(out)
    draw.text((20, img.height + 8), "READ THE FIGURE", font=label_font, fill=TEAL)
    y = img.height + 44
    for line in lines:
        draw.text((20, y), line, font=body_font, fill=NAVY)
        y += 45
    draw.line([20, out.height - 8, img.width - 20, out.height - 8], fill=LIGHT, width=2)
    return out


VISUAL_BUILDERS = {
    "geometry": geometry,
    "bars": bars,
    "tree": tree,
    "flow": flow,
    "pascal": pascal,
    "table": table,
}
