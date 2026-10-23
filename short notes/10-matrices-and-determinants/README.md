# Chapter 10 — Matrices & Determinants

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 13 sheets across 6 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 4 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 4 editable figures; the chapter has 4 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/10-matrices-and-determinants-combined-sheets.zip`](exports/10-matrices-and-determinants-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/10-matrices-and-determinants-JEE-sheets.zip`](exports/10-matrices-and-determinants-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/10-matrices-and-determinants-Olympiad-sheets.zip`](exports/10-matrices-and-determinants-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/10-matrices-and-determinants-combined.pdf`](exports/10-matrices-and-determinants-combined.pdf) |
| JEE bookmarked PDF | [`exports/10-matrices-and-determinants-JEE.pdf`](exports/10-matrices-and-determinants-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/10-matrices-and-determinants-Olympiad-extensions.pdf`](exports/10-matrices-and-determinants-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Matrix Language — Shapes, Operations, Transpose (**JEE 1–2**).
- `jee-02.md` — Determinants — Cofactors & Rules (**JEE 3–4**).
- `jee-03.md` — Adjoint & Inverse — The Reversible Case (**JEE 5**).
- `jee-04.md` — Linear Systems — Cramer & Consistency (**JEE 6–7**).
- `jee-05.md` — Special Matrices — Symmetry, Orthogonality, Structure (**JEE 8–9**).
- `jee-90-visual-methods.md` — Visual Matrix Lab — Transformations, Determinants and Linear Systems (**JEE 10–13**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Cayley–Hamilton — Reduce Every Power (**Olympiad 1**).
- `olympiad-02.md` — Determinant Geometry — Bounds and Updates (**Olympiad 2**).
- `olympiad-03.md` — Trace, Rank–Nullity, Block Structure (**Olympiad 3–4**).

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
