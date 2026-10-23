# Chapter 15 — Vectors

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter covers vector algebra, dot and cross products, scalar triple products and their geometric interpretations in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated visual vector lab.

## Current edition

- **Part I — JEE Main + Advanced:** 24 sheets across 10 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 6 sheets across 3 source lessons in `Olympiad/`.
- **Total:** 30 A4 sheets and 22 editable diagram blocks.
- **Visual expansion:** `jee-90-visual-methods.md` adds 6 sheets with five exact geometric figures, a problem-selection workflow and a product-comparison table.
- **Mathematical verification:** 204 exact/rational, numerical, visual-lesson and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/15-vectors-combined-sheets.zip`](exports/15-vectors-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/15-vectors-JEE-sheets.zip`](exports/15-vectors-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/15-vectors-Olympiad-sheets.zip`](exports/15-vectors-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/15-vectors-combined.pdf`](exports/15-vectors-combined.pdf) |
| JEE bookmarked PDF | [`exports/15-vectors-JEE.pdf`](exports/15-vectors-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/15-vectors-Olympiad-extensions.pdf`](exports/15-vectors-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Vector Language — Components, Magnitude and Direction (**JEE 1–2**).
- `jee-02.md` — Addition, Scalar Multiplication and Linear Combinations (**JEE 3–4**).
- `jee-03.md` — Points, Section Formula and Centroids (**JEE 5–6**).
- `jee-04.md` — The Dot Product — Angles and Perpendicularity (**JEE 7–8**).
- `jee-05.md` — Projection, Resolution and Dot-Product Applications (**JEE 9–10**).
- `jee-06.md` — The Cross Product — Normal Direction and Area (**JEE 11–12**).
- `jee-07.md` — Areas and Vector Geometry (**JEE 13–14**).
- `jee-08.md` — The Scalar Triple Product — Volume and Coplanarity (**JEE 15–16**).
- `jee-09.md` — Tetrahedra and Mixed Vector Strategy (**JEE 17–18**).
- `jee-90-visual-methods.md` — Visual Vector Lab (**JEE 19–24**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Vector Triple Products and Jacobi (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Barycentric Coordinates, Ceva and Routh (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — Vector Proofs and the Euler Line (**Olympiad 5–6**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

In addition to the shared geometry, table and flow builders, the registered `vector3d` builder supports labelled 3D arrows, points, segments, polygons and parallelepipeds with configurable axes, view angles and viewport zoom. The mathematical suite reads selected JSON figures directly, so their encoded geometry is checked as well as their captions.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 204 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks vector arithmetic, section and centroid formulas, projection/rejection, dot/cross/triple-product identities, areas, volumes, coplanarity, vector triple products, Jacobi, barycentrics, Ceva, Routh, Varignon and the Euler line. It includes targeted visual-lab assertions and direct checks of the editable diagram coordinates. These checks supplement—not replace—proofs and visual review.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for the official/extension boundaries and the explicit Chapter 16 line-and-plane boundary, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source corrections and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
