# Short Notes — Chapter 1: Sets, Relations and Functions

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 26 sheets across 9 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 9 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 4 editable figures; the chapter has 14 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/01-sets-relations-functions-combined-sheets.zip`](exports/01-sets-relations-functions-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/01-sets-relations-functions-JEE-sheets.zip`](exports/01-sets-relations-functions-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/01-sets-relations-functions-Olympiad-sheets.zip`](exports/01-sets-relations-functions-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/01-sets-relations-functions-combined.pdf`](exports/01-sets-relations-functions-combined.pdf) |
| JEE bookmarked PDF | [`exports/01-sets-relations-functions-JEE.pdf`](exports/01-sets-relations-functions-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/01-sets-relations-functions-Olympiad-extensions.pdf`](exports/01-sets-relations-functions-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Sets — Language, Representation, Subsets (**JEE 1–3**).
- `jee-02.md` — Operations on Sets — Union, Intersection, Difference, De Morgan (**JEE 4–6**).
- `jee-03.md` — Cartesian Products & Relations — Definitions, Types, Counting (**JEE 7–8**).
- `jee-04.md` — Equivalence Relations & Partitions — with JEE-style Counting (**JEE 9–11**).
- `jee-05.md` — Functions — Definition, Domain, Range, Image & Preimage (**JEE 12–14**).
- `jee-06.md` — Special Functions & Graph Transformations — |x|, sgn, [x], {x} (**JEE 15–16**).
- `jee-07.md` — One-one, Onto, Even / Odd, Periodic — the Classification Sheet (**JEE 17–19**).
- `jee-08.md` — Composition & Inverse Functions — and the Chapter Recap (**JEE 20–21**).
- `jee-90-visual-methods.md` — Visual Function Lab — Domain, Range, Graph Tests and Inverses (**JEE 22–26**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Counting Relations & Functions — Rigorous Catalogue (**Olympiad 1–3**).
- `olympiad-02.md` — Functional Equations — Cauchy, Pexider, Involutions (**Olympiad 4–6**).
- `olympiad-03.md` — Floor Toolkit & Fixed-Point Counting — Hermite, Equations, Involution Sets (**Olympiad 7–9**).

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
