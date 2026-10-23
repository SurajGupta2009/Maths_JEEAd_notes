# Chapter 12 — Straight Lines & Locus

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 17 sheets across 8 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 3 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 5 editable figures; the chapter has 7 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/12-straight-lines-and-locus-combined-sheets.zip`](exports/12-straight-lines-and-locus-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/12-straight-lines-and-locus-JEE-sheets.zip`](exports/12-straight-lines-and-locus-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/12-straight-lines-and-locus-Olympiad-sheets.zip`](exports/12-straight-lines-and-locus-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/12-straight-lines-and-locus-combined.pdf`](exports/12-straight-lines-and-locus-combined.pdf) |
| JEE bookmarked PDF | [`exports/12-straight-lines-and-locus-JEE.pdf`](exports/12-straight-lines-and-locus-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/12-straight-lines-and-locus-Olympiad-extensions.pdf`](exports/12-straight-lines-and-locus-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Coordinates — Displacement, Section, Translation (**JEE 1–2**).
- `jee-02.md` — The Straight Line — Slope and Equations (**JEE 3**).
- `jee-03.md` — Angles, Parallelism, Perpendicularity, Distance (**JEE 4–5**).
- `jee-04.md` — Pencils, Concurrency and Angle Bisectors (**JEE 6–7**).
- `jee-05.md` — Triangle Centres in Coordinates (**JEE 8–9**).
- `jee-06.md` — Locus — Translate the Condition, Then Verify (**JEE 10–11**).
- `jee-07.md` — Pairs of Lines and a Coordinate Toolkit (**JEE 12**).
- `jee-90-visual-methods.md` — Visual Coordinate-Geometry Lab — Lines, Distances, Centres and Loci (**JEE 13–17**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Euler Line — Three Centres, One Ratio (**Olympiad 1**).
- `olympiad-02.md` — Nine-Point Circle: Coordinates (**Olympiad 2**).
- `olympiad-03.md` — Loci Beyond the First Examples (**Olympiad 3**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # independent exact/numeric worked-example checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suites include targeted checks for the visual-methods examples. The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links. These reproducible checks supplement—rather than claim to replace—mathematical and visual review.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for syllabus/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
