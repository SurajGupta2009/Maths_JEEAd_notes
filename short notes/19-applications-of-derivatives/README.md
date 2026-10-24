# Chapter 19 — Applications of Derivatives

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter develops rates, tangent geometry, approximation, monotonicity, extrema, convexity, curve sketching and feasible optimisation in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated six-page visual lab.

## Current edition

- **Part I — JEE Main + Advanced:** 28 sheets across 12 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 10 sheets across 5 source lessons in `Olympiad/`.
- **Total:** 38 A4 sheets and 22 editable diagram blocks: 15 graphs, 4 workflows and 3 decision tables.
- **Visual expansion:** `jee-90-visual-applications.md` adds 6 sheets on related rates, angles between tangents, linearisation error, root counting, endpoint extrema and the corrected window model.
- **Mathematical verification:** 469 exact/rational, numerical, visual-lab and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/19-applications-of-derivatives-combined-sheets.zip`](exports/19-applications-of-derivatives-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/19-applications-of-derivatives-JEE-sheets.zip`](exports/19-applications-of-derivatives-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/19-applications-of-derivatives-Olympiad-sheets.zip`](exports/19-applications-of-derivatives-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/19-applications-of-derivatives-combined.pdf`](exports/19-applications-of-derivatives-combined.pdf) |
| JEE bookmarked PDF | [`exports/19-applications-of-derivatives-JEE.pdf`](exports/19-applications-of-derivatives-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/19-applications-of-derivatives-Olympiad-extensions.pdf`](exports/19-applications-of-derivatives-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Rates of Change and Related Rates (**JEE 1–2**).
- `jee-02.md` — Tangents, Normals and Angles Between Curves (**JEE 3–4**).
- `jee-03.md` — Tangent Lengths, Differentials and Approximation (**JEE 5–6**).
- `jee-04.md` — Monotonicity — Read the Sign of the Derivative (**JEE 7–8**).
- `jee-05.md` — Root Counting with Monotone Branches (**JEE 9–10**).
- `jee-06.md` — Local Maxima and Minima (**JEE 11–12**).
- `jee-07.md` — Absolute Extrema — Closed Intervals and Endpoints (**JEE 13–14**).
- `jee-08.md` — Convexity, Concavity and Inflection (**JEE 15–16**).
- `jee-09.md` — Curve Sketching as a Synthesis (**JEE 17–18**).
- `jee-10.md` — Feasible Optimisation — Standard Models (**JEE 19–20**).
- `jee-11.md` — Model Audits — Ellipse and Rectangle-with-Semicircle (**JEE 21–22**).
- `jee-90-visual-applications.md` — Visual Lab — Six Derivative Applications (**JEE 23–28**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Supporting Lines, Jensen and a Cosine Bound (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Young, Cauchy and AM–GM (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — Envelopes and the Parabola Directrix (**Olympiad 5–6**).
- `olympiad-04.md` — Extension IV — Director Circles and Lagrange Multipliers (**Olympiad 7–8**).
- `olympiad-05.md` — Extension V — Symmetric Optimisation and Its Frontier (**Olympiad 9–10**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

The shared graph builder supports curves, open and filled points, horizontal and vertical lines, sampled rays, feasibility bands and arrowed annotations. The mathematical suite evaluates the actual JSON curve expressions and point coordinates, including tangent intersections, inflection points, open endpoints and the positive-area semicircle endpoint of the window model.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 469 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks exact related rates, tangent and normal geometry, differential errors, monotonicity, root counts, local and absolute extrema, convexity, corrected inflection points, feasible optimisation and all extension topics. Independent bisection and NumPy polynomial roots, numerical grids, direct numerical evaluation and completed-square identities supplement the printed derivations. The suite also checks the editable figure inventory and six-page visual lab. These checks supplement—not replace—proofs and native-size visual review.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for the official/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for all source/question coverage and correction notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
