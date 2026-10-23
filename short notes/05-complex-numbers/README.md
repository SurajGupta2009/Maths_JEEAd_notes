# Chapter 5 — Complex Numbers and Quadratic Equations (Complex Numbers strand)

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 36 sheets across 12 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 17 sheets across 6 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 4 editable figures; the chapter has 9 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/05-complex-numbers-combined-sheets.zip`](exports/05-complex-numbers-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/05-complex-numbers-JEE-sheets.zip`](exports/05-complex-numbers-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/05-complex-numbers-Olympiad-sheets.zip`](exports/05-complex-numbers-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/05-complex-numbers-combined.pdf`](exports/05-complex-numbers-combined.pdf) |
| JEE bookmarked PDF | [`exports/05-complex-numbers-JEE.pdf`](exports/05-complex-numbers-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/05-complex-numbers-Olympiad-extensions.pdf`](exports/05-complex-numbers-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Complex Numbers — Arithmetic, Conjugate, Modulus, the Two Languages (**JEE 1–3**).
- `jee-02.md` — Argument and Polar Form — Multiplication is Stretch × Rotate (**JEE 4–6**).
- `jee-03.md` — De Moivre and Euler — Powers, Roots, and Where Trig Identities Come From (**JEE 7–9**).
- `jee-04.md` — n-th Roots — Exactly n, Regular Polygons; the Square-Root Formula (**JEE 10–11**).
- `jee-05.md` — Roots of Unity — The ω Toolkit and Vanishing Sums (**JEE 12–14**).
- `jee-06.md` — Product Formulas and the Roots-of-Unity Filter (**JEE 15–17**).
- `jee-07.md` — Equations in z and z̄ — Two Methods, One Discipline (**JEE 18–20**).
- `jee-08.md` — Loci I — Modulus Conditions: Circles, Bisectors, Apollonius, Regions (**JEE 21–23**).
- `jee-09.md` — Loci II — Argument Conditions: Arcs of Circles; the Ellipse Case (**JEE 24–26**).
- `jee-10.md` — Optimization — Triangle Inequality with Equality Conditions, Chords, Regions (**JEE 27–29**).
- `jee-11.md` — Recap Toolkit — The Whole Chapter on One Sheet (**JEE 30–32**).
- `jee-90-visual-methods.md` — Visual Complex-Number Lab — Argand Plane, Roots and Transformations (**JEE 33–36**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension — The Rotation Engine: Equilateral Condition, Tests, Area, Circumcenter (**Olympiad 1–2**).
- `olympiad-02.md` — Extension — Ptolemy from One Identity; Distance Theorems by Expansion (**Olympiad 3–5**).
- `olympiad-03.md` — Extension — Van Aubel and Napoleon: Squares and Equilaterals on the Sides (**Olympiad 6–8**).
- `olympiad-04.md` — Extension — Centroid Sums, Unit-Circle Configurations, w = z + 1/z (**Olympiad 9–11**).
- `olympiad-05.md` — Extension — The Quadratic Gauss Sum: Squaring, Filtering, Phase Mod 4 (**Olympiad 12–14**).
- `olympiad-06.md` — Extension — Gauss–Lucas, Marden, Pompeiu: Structure Theorems (**Olympiad 15–17**).

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
