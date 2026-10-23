# Chapter 7 — Sequences & Series

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 14 sheets across 6 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 6 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 4 editable figures; the chapter has 6 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/07-sequences-and-series-combined-sheets.zip`](exports/07-sequences-and-series-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/07-sequences-and-series-JEE-sheets.zip`](exports/07-sequences-and-series-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/07-sequences-and-series-Olympiad-sheets.zip`](exports/07-sequences-and-series-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/07-sequences-and-series-combined.pdf`](exports/07-sequences-and-series-combined.pdf) |
| JEE bookmarked PDF | [`exports/07-sequences-and-series-JEE.pdf`](exports/07-sequences-and-series-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/07-sequences-and-series-Olympiad-extensions.pdf`](exports/07-sequences-and-series-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Sequences and Series — Arithmetic Progressions: Add the Same Amount Every Time (**JEE 1–2**).
- `jee-02.md` — Geometric Progressions — Multiply by the Same Amount, and the Infinite Sum (**JEE 3–4**).
- `jee-03.md` — AM–GM and the Special Sums Σk, Σk², Σk³ — The Syllabus Power Sums (**JEE 5–6**).
- `jee-04.md` — Arithmetico-Geometric Sums and Telescoping — The Two Summation Engines (Derivable Applications) (**JEE 7–8**).
- `jee-05.md` — Mixed Problem Shapes and the Recap Toolkit — Sequences & Series (**JEE 9–10**).
- `jee-90-visual-methods.md` — Visual Sequences Lab — Growth, Partial Sums and Cancellation (**JEE 11–14**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension — Harmonic Progressions and the A ≥ G ≥ H Chain (**Olympiad 1–2**).
- `olympiad-02.md` — Extension — Recurrences, Characteristic Equations, and Generating Functions (**Olympiad 3–4**).
- `olympiad-03.md` — Extension — Telescoping Products, Wallis, Stolz–Cesàro, and Asymptotics (**Olympiad 5–6**).

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
