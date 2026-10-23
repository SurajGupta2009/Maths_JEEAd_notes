"""Build pipeline: render sheets -> PNGs, export ZIPs + bookmarked A4 PDFs + index.html.

Usage (from a chapter folder):
    python3 ../_engine/build.py render
    python3 ../_engine/build.py export
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image

from compose import Block, compose_sheet, parse_content, FULL_W, PAGE_H, PAGE_W
from core import DPI

PART_LABELS = {
    "jee": "PART I — JEE MAIN + ADVANCED",
    "olympiad": "PART II — OLYMPIAD / EXTENSIONS",
}


def chapter_dir() -> Path:
    return Path.cwd()


def load_content(cdir: Path):
    content = cdir / "content"
    sheets = []
    for p in sorted(content.glob("*.md")):
        src = p.read_text(encoding="utf-8")
        fm, blocks = parse_content(src)
        if "id" not in fm:
            raise SystemExit(f"{p}: frontmatter missing id")
        sheets.append({"file": p, "fm": fm, "blocks": blocks})
    jee = [s for s in sheets if s["fm"].get("part") == "jee"]
    oly = [s for s in sheets if s["fm"].get("part") == "olympiad"]
    unknown = [s for s in sheets if s["fm"].get("part") not in ("jee", "olympiad")]
    if unknown:
        raise SystemExit(f"bad part in {[s['file'].name for s in unknown]}")
    jee.sort(key=lambda s: s["fm"]["id"])
    oly.sort(key=lambda s: s["fm"]["id"])
    return jee, oly


def render(chapter_slug: str):
    cdir = chapter_dir()
    jee, oly = load_content(cdir)
    problems = []
    manifest = {"chapter": chapter_slug, "parts": {}}

    from compose import BlockRenderer, paginate, draw_sheet
    for part, group in (("jee", jee), ("olympiad", oly)):
        outdir = cdir / ("JEE" if part == "jee" else "Olympiad")
        if outdir.exists():
            shutil.rmtree(outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        # Render every lesson in one reading stream; lessons start on fresh sheets.
        combined = []          # (fm, block, is_first_of_file)
        for unit_no, sheet in enumerate(group, start=1):
            fm = sheet["fm"]
            # Keep source-unit transitions visible in the reading stream. These
            # ribbons make a page that contains adjacent lessons navigable,
            # without reducing or rearranging the authored prose.
            label = f"LESSON {unit_no:02d} / {len(group):02d}"
            combined.append((fm, Block("lesson", text=label), True))
            for j, b in enumerate(sheet["blocks"]):
                combined.append((fm, b, j == 0))
        br = BlockRenderer()
        pages, errors = paginate([b for _, b, _ in combined], br)
        problems += [f"{part}: {e}" for e in errors]
        problems += [f"{part}: MATH {m}" for m in br.math_bad]
        block_fm = {id(b): (fm, first) for fm, b, first in combined}
        all_pages = []
        for pg in pages:
            if not pg.items:
                continue
            first_block = pg.items[0][0]
            fm, is_first = block_fm[id(first_block)]
            all_pages.append((fm, pg, 0 if is_first else 1))
        n = len(all_pages)
        entries = []
        for k, (fm, pg, pidx) in enumerate(all_pages, start=1):
            if pidx == 0:
                title = fm.get("title", pg.title)
            elif pg.items and pg.items[0][0].kind == "head2":
                title = pg.items[0][0].text
            else:
                title = fm.get("title", pg.title) + " (cont.)"
            pg.title = title
            pid = f"{'JEE' if part == 'jee' else 'OLY'}-{k:02d}"
            img = draw_sheet(fm, pg, chapter_slug, PART_LABELS[part], k, n,
                             page_id=pid)
            name = f"{k:02d}.png"
            out = outdir / name
            img.save(out, dpi=(DPI, DPI))
            tag = f"{part}/{name}"
            print(f"  {tag}  '{title[:70]}'")
            plain = title.replace("$", "").replace("\\", "")
            entries.append({
                "no": k, "file": f"{'JEE' if part == 'jee' else 'Olympiad'}/{name}",
                "id": pid, "title": title, "plain_title": plain,
                "subtitle": fm.get("title", ""),
                "bookmark": f"{'JEE' if part == 'jee' else 'OLY'} {k} — {plain}",
            })
        manifest["parts"][part] = entries

    (cdir / "manifest.json").write_text(json.dumps(manifest, indent=2),
                                        encoding="utf-8")
    if problems:
        print("\nRENDER PROBLEMS:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    print("render OK")


# --------------------------------------------------------------------------
# Export: ZIPs + PDFs + index.html
# --------------------------------------------------------------------------
def export(chapter_slug: str):
    cdir = chapter_dir()
    man = json.loads((cdir / "manifest.json").read_text(encoding="utf-8"))
    ex = cdir / "exports"
    ex.mkdir(exist_ok=True)
    jee_files = [cdir / e["file"] for e in man["parts"]["jee"]]
    oly_files = [cdir / e["file"] for e in man["parts"]["olympiad"]]
    jee_bm = [e["bookmark"] for e in man["parts"]["jee"]]
    oly_bm = [e["bookmark"] for e in man["parts"]["olympiad"]]

    def zip_of(path: Path, files: list[Path]):
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in files:
                z.write(f, arcname=f"{f.parent.name}/{f.name}")
        print("wrote", path.name)

    zip_of(ex / f"{chapter_slug}-JEE-sheets.zip", jee_files)
    zip_of(ex / f"{chapter_slug}-Olympiad-sheets.zip", oly_files)
    zip_of(ex / f"{chapter_slug}-combined-sheets.zip", jee_files + oly_files)

    def pdf_of(path: Path, files: list[Path], bookmarks: list[str], root: str):
        from reportlab.lib.utils import ImageReader
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        c = canvas.Canvas(str(path), pagesize=A4)
        c.setTitle(chapter_slug)
        width, height = A4
        c.bookmarkPage("start")
        c.addOutlineEntry(root, "start", level=0)
        prev = None
        for idx, (f, bm) in enumerate(zip(files, bookmarks)):
            key = f"p{idx}"
            c.bookmarkPage(key)
            c.addOutlineEntry(bm, key, level=1)
            img = ImageReader(str(f))
            iw, ih = img.getSize()
            scale = min(width / iw, height / ih)
            w, h = iw * scale, ih * scale
            c.drawImage(img, (width - w) / 2, (height - h) / 2, w, h)
            c.showPage()
            prev = key
        c.save()
        print("wrote", path.name)

    pdf_of(ex / f"{chapter_slug}-JEE.pdf", jee_files, jee_bm,
           "Part I — JEE Main + Advanced")
    pdf_of(ex / f"{chapter_slug}-Olympiad-extensions.pdf", oly_files, oly_bm,
           "Part II — Olympiad / Extensions")
    pdf_of(ex / f"{chapter_slug}-combined.pdf", jee_files + oly_files,
           jee_bm + oly_bm, "Combined (JEE first, then Olympiad)")

    write_index(chapter_slug, man, cdir)
    print("export OK")


def write_index(chapter_slug: str, man: dict, cdir: Path):
    title = man["chapter"]
    rows_jee = ""
    for e in man["parts"]["jee"]:
        rows_jee += sheet_card(e)
    rows_oly = ""
    for e in man["parts"]["olympiad"]:
        rows_oly += sheet_card(e)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Short Notes — {title}</title>
<style>
  body {{ font-family: "Segoe UI", system-ui, sans-serif; margin: 0; background: #f4f6fa; color: #16295c; }}
  header {{ background: #0f766e; color: #fff; padding: 28px 40px; }}
  header h1 {{ margin: 0 0 6px; font-size: 30px; }}
  header p {{ margin: 2px 0; opacity: .95; }}
  nav a {{ color: #fff; margin-right: 18px; text-decoration: underline; }}
  main {{ padding: 28px 40px; max-width: 1280px; margin: 0 auto; }}
  h2 {{ color: #0f766e; border-bottom: 3px solid #0f766e; padding-bottom: 6px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 18px; }}
  .card {{ background: #fff; border: 1px solid #dbe4f0; border-radius: 10px; padding: 12px; }}
  .card img {{ width: 100%; border: 1px solid #e5ebf4; border-radius: 6px; }}
  .card .cap {{ font-size: 13px; margin-top: 8px; }}
  .card .no {{ font-weight: 700; color: #b8860b; }}
  .dl a {{ display: inline-block; background: #0f766e; color: #fff; padding: 10px 16px;
          border-radius: 8px; margin: 6px 8px 6px 0; text-decoration: none; }}
  .dl a.alt {{ background: #16295c; }}
  .note {{ background: #fffbe8; border-left: 6px solid #e0a800; padding: 12px 16px; border-radius: 6px; }}
  footer {{ text-align: center; color: #5b6b84; padding: 24px; font-size: 13px; }}
</style>
</head>
<body>
<header>
  <h1>Handwritten-style Short Notes — {title}</h1>
  <p>Part I: JEE Main + Advanced core &nbsp;|&nbsp; Part II: Olympiad (IOQM/RMO) extensions</p>
  <nav>
    <a href="README.md">README</a>
    <a href="SCOPE.md">SCOPE</a>
    <a href="SOURCE-AUDIT.md">SOURCE AUDIT</a>
    <a href="PRINTING.txt">PRINTING</a>
  </nav>
</header>
<main>
  <h2>Downloads</h2>
  <div class="dl">
    <a href="exports/{chapter_slug}-combined-sheets.zip">Combined PNG ZIP (JEE first)</a>
    <a href="exports/{chapter_slug}-JEE-sheets.zip">JEE PNG ZIP</a>
    <a href="exports/{chapter_slug}-Olympiad-sheets.zip">Olympiad PNG ZIP</a>
    <a class="alt" href="exports/{chapter_slug}-combined.pdf">Combined PDF (bookmarked)</a>
    <a class="alt" href="exports/{chapter_slug}-JEE.pdf">JEE PDF (bookmarked)</a>
    <a class="alt" href="exports/{chapter_slug}-Olympiad-extensions.pdf">Olympiad PDF (bookmarked)</a>
  </div>
  <p class="note"><b>Printing:</b> A4 portrait, one sheet per page, <b>Fit</b> (not Fill/Crop).
     Every PNG is already exact A4 proportion at 300&nbsp;DPI (2480×3508).</p>

  <h2>Part I — JEE Main + Advanced ({len(man["parts"]["jee"])} sheets)</h2>
  <div class="grid">{rows_jee}</div>

  <h2>Part II — Olympiad / Extensions ({len(man["parts"]["olympiad"])} sheets)</h2>
  <div class="grid">{rows_oly}</div>
</main>
<footer>Generated from editable content in <code>content/</code> · render: <code>python3 scripts/render.py</code></footer>
</body>
</html>
"""
    (cdir / "index.html").write_text(html, encoding="utf-8")
    print("wrote index.html")


def sheet_card(e: dict) -> str:
    return f"""<div class="card"><a href="{e['file']}"><img src="{e['file']}" loading="lazy" alt="{e['title']}"></a>
<div class="cap"><span class="no">{e['id'].upper()}</span> — {e['title']}<br>{e.get('subtitle','')}</div></div>"""


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    slug = Path.cwd().name
    if cmd in ("render", "all"):
        render(slug)
    if cmd in ("export", "all"):
        export(slug)
