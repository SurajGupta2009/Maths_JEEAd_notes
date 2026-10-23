"""Reproducible delivery checks for a short-notes chapter folder.

Usage:  python3 ../_engine/check.py        (from the chapter folder)
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

from PIL import Image

from compose import parse_content
from core import (FALLBACK, HAND, HAND_BOLD, has_glyph, math_check,
                  missing_glyphs, split_runs)

PAGE_W, PAGE_H = 2480, 3508
SAFE = 120  # 10 mm at 300 DPI
PROBLEMS: list[str] = []
CHECKS: list[str] = []


def ok(msg: str):
    CHECKS.append(msg)


def bad(msg: str):
    PROBLEMS.append(msg)


def check_png(path: Path):
    img = Image.open(path)
    if img.size != (PAGE_W, PAGE_H):
        bad(f"{path.name}: size {img.size} != {(PAGE_W, PAGE_H)}")
        return
    dpi = img.info.get("dpi")
    if not dpi or abs(dpi[0] - 300) > 1 or abs(dpi[1] - 300) > 1:
        bad(f"{path.name}: dpi {dpi} != (300, 300)")
    # ink must stay inside safe margins
    rgb = img.convert("RGB")
    px = rgb.load()
    step = 3
    for y in range(0, PAGE_H, step):
        for x in range(0, PAGE_W, step):
            if SAFE <= x <= PAGE_W - SAFE and SAFE <= y <= PAGE_H - SAFE:
                continue
            r, g, b = px[x, y]
            if min(r, g, b) < 200:  # anything darker than faint rules
                bad(f"{path.name}: ink outside safe margin at ({x},{y}) rgb={(r,g,b)}")
                return
    ok(f"{path.name}: 2480x3508 @300dpi, ink inside 10mm margins")


def check_content_fonts_math(content_dir: Path):
    texts: list[tuple[str, str]] = []
    maths: list[str] = []

    def add_text(kind: str, text: str):
        if not isinstance(text, str) or not text:
            return
        texts.append((kind, text))
        if kind == "display":
            # parse_content stores display-math bodies without the surrounding $$
            maths.append(text)
        else:
            # Strip any display blocks first so their doubled dollar delimiters
            # cannot pair with inline math in a neighbouring paragraph.
            inline_source = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
            maths.extend(re.findall(r"\$([^$]+)\$", inline_source))

    for p in sorted(content_dir.glob("*.md")):
        src = p.read_text(encoding="utf-8")
        fm, blocks = parse_content(src)
        stack = list(blocks)
        while stack:
            b = stack.pop()
            add_text(b.kind, b.text)
            if isinstance(b.items, list) and all(isinstance(x, str) for x in b.items):
                for item in b.items:
                    add_text("inline", item)
            stack.extend(b.blocks)
            if b.kind == "box":
                stack.extend(b.items)

    # Non-math plain text for font coverage (display formulas are excluded).
    plain_parts = []
    for kind, text in texts:
        if kind == "display":
            continue
        piece = re.sub(r"\$[^$]*\$", " ", text).replace("**", "")
        plain_parts.append(piece)
    plain = "\n".join(plain_parts)
    miss = missing_glyphs(HAND, plain) | missing_glyphs(HAND_BOLD, plain)
    # fallback must cover everything missing from handwriting fonts
    uncovered = {ch for ch in miss if not has_glyph(FALLBACK, ch)}
    if uncovered:
        bad(f"uncovered glyphs even after fallback: {sorted(uncovered)}")
    else:
        ok(f"font coverage OK (fallback covers {len(miss)} non-handwritten glyphs)")
    badmath = [m for m in maths if not math_check(m)]
    if badmath:
        for m in badmath:
            bad(f"math parse failed: {m[:60]}")
    else:
        ok(f"math parse OK ({len(maths)} inline/display formulas)")


def check_manifest(cdir: Path, man: dict):
    for part, folder in (("jee", "JEE"), ("olympiad", "Olympiad")):
        entries = man["parts"][part]
        pngs = sorted((cdir / folder).glob("*.png"))
        if len(pngs) != len(entries):
            bad(f"{folder}: {len(pngs)} pngs vs {len(entries)} manifest entries")
        else:
            ok(f"{folder}: {len(pngs)} sheets, numbered 01..{len(pngs):02d} independently")
        for i, e in enumerate(entries, start=1):
            if e["file"] != f"{folder}/{i:02d}.png":
                bad(f"manifest order broken: {e['file']}")
    # visible labels present in rendered text? (checked via compose metadata)
    for part in ("jee", "olympiad"):
        for e in man["parts"][part]:
            if not e.get("title"):
                bad(f"{e['file']}: missing title")


def check_exports(cdir: Path, man: dict, slug: str):
    ex = cdir / "exports"
    jee = [f"JEE/{e['file'].split('/')[1]}" for e in man["parts"]["jee"]]
    oly = [f"Olympiad/{e['file'].split('/')[1]}" for e in man["parts"]["olympiad"]]
    expect = {
        f"{slug}-JEE-sheets.zip": jee,
        f"{slug}-Olympiad-sheets.zip": oly,
        f"{slug}-combined-sheets.zip": jee + oly,
    }
    for name, entries in expect.items():
        zp = ex / name
        if not zp.exists():
            bad(f"missing zip {name}")
            continue
        with zipfile.ZipFile(zp) as z:
            if z.testzip() is not None:
                bad(f"{name}: corrupt entry")
            names = z.namelist()
            if names != entries:
                bad(f"{name}: entries {names} != expected {entries}")
            else:
                ok(f"{name}: intact, {len(names)} pngs, order OK")
    # PDFs
    from pypdf import PdfReader
    pdf_expect = {
        f"{slug}-JEE.pdf": (len(jee), "JEE first"),
        f"{slug}-Olympiad-extensions.pdf": (len(oly), "Olympiad only"),
        f"{slug}-combined.pdf": (len(jee) + len(oly), "JEE then Olympiad"),
    }
    for name, (n, desc) in pdf_expect.items():
        p = ex / name
        if not p.exists():
            bad(f"missing pdf {name}")
            continue
        r = PdfReader(str(p))
        if len(r.pages) != n:
            bad(f"{name}: {len(r.pages)} pages != {n}")
        box = r.pages[0].mediabox
        w, h = float(box.width), float(box.height)
        if abs(w - 595.276) > 1 or abs(h - 841.89) > 1:
            bad(f"{name}: page size {w}x{h} not A4 portrait")
        # bookmarks
        ol = r.outline
        tops = []
        def walk(items, depth=0):
            for it in items:
                if isinstance(it, list):
                    walk(it, depth + 1)
                else:
                    tops.append((depth, it.title))
        walk(ol)
        tops = [t for _, t in tops]
        jee_marks = [e["bookmark"] for e in man["parts"]["jee"]]
        oly_marks = [e["bookmark"] for e in man["parts"]["olympiad"]]
        want = {"JEE": jee_marks, "OLY": oly_marks, "combined": jee_marks + oly_marks}
        key = "JEE" if "-JEE.pdf" in name else ("OLY" if "Olympiad" in name else "combined")
        marks = [t for t in tops if t.startswith(("JEE ", "OLY "))]
        if marks != want[key]:
            bad(f"{name}: bookmarks {marks[:3]}... != expected order ({desc})")
        else:
            ok(f"{name}: A4 portrait, {n} pages, bookmarks in order ({desc})")


def check_index(cdir: Path):
    html = (cdir / "index.html").read_text(encoding="utf-8")
    links = re.findall(r'href="([^"]+)"', html) + re.findall(r'src="([^"]+)"', html)
    missing = [l for l in links if not l.startswith(("http", "#"))
               and not (cdir / l).exists()]
    if missing:
        bad(f"index.html broken links: {missing}")
    else:
        ok(f"index.html: all {len(links)} local links resolve")


def check_docs(cdir: Path):
    for name in ["README.md", "SCOPE.md", "SOURCE-AUDIT.md", "PRINTING.txt",
                 "index.html", "manifest.json"]:
        if not (cdir / name).exists():
            bad(f"missing deliverable {name}")
    for p in (cdir / "content").glob("*.md"):
        src = p.read_text(encoding="utf-8")
        if not src.startswith("---"):
            bad(f"{p.name}: missing frontmatter")
        if src.count(":::") % 2 != 0:
            bad(f"{p.name}: unbalanced ::: fences")
    ok("deliverable files + content fences OK")


def main():
    cdir = Path.cwd()
    slug = cdir.name
    man = json.loads((cdir / "manifest.json").read_text(encoding="utf-8"))

    check_docs(cdir)
    check_content_fonts_math(cdir / "content")
    for folder in ("JEE", "Olympiad"):
        for p in sorted((cdir / folder).glob("*.png")):
            check_png(p)
    check_manifest(cdir, man)
    check_exports(cdir, man, slug)
    check_index(cdir)

    print("\n".join("PASS  " + c for c in CHECKS))
    if PROBLEMS:
        print("\n".join("FAIL  " + p for p in PROBLEMS))
        print(f"\n{len(CHECKS)} checks passed, {len(PROBLEMS)} FAILED")
        raise SystemExit(1)
    print(f"\nALL CHECKS PASS ({len(CHECKS)} checks)")


if __name__ == "__main__":
    main()
