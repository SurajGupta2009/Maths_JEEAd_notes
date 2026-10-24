# Chapter 21 — Definite Integration & Areas

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter completes the canonical Integration module: Riemann accumulation, the Fundamental Theorem, definite techniques and symmetry, improper convergence, geometric area, and the Wallis/Beta/Gamma/Gaussian/Frullani/Feynman/Dirichlet frontier, all in one top-to-bottom reading stream.

## Current edition

- **Part I — JEE Main + Advanced:** 28 sheets across 17 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 14 sheets across 7 source lessons in `Olympiad/`.
- **Total:** 42 A4 sheets and 24 editable diagram blocks: 11 graphs, 6 workflows and 7 decision tables.
- **Visual lab:** six dedicated sheets for Riemann rectangles, FTC accumulation, King reflection, an infinite tail, signed versus total area, and the area between sine and cosine.
- **Mathematical verification:** 417 exact/rational, numerical, source-correction, visual-lab and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/21-definite-integration-and-areas-combined-sheets.zip`](exports/21-definite-integration-and-areas-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/21-definite-integration-and-areas-JEE-sheets.zip`](exports/21-definite-integration-and-areas-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/21-definite-integration-and-areas-Olympiad-sheets.zip`](exports/21-definite-integration-and-areas-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/21-definite-integration-and-areas-combined.pdf`](exports/21-definite-integration-and-areas-combined.pdf) |
| JEE bookmarked PDF | [`exports/21-definite-integration-and-areas-JEE.pdf`](exports/21-definite-integration-and-areas-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/21-definite-integration-and-areas-Olympiad-extensions.pdf`](exports/21-definite-integration-and-areas-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Definite Integrals as Limits of Riemann Sums (**JEE 1–2**).
- `jee-02.md` — The Fundamental Theorem of Calculus (**JEE 3–4**).
- `jee-03.md` — Definite Substitution — Change the Limits (**JEE 5–6**).
- `jee-04.md` — Definite By Parts, Partial Fractions and Half-Angle (**JEE 7–8**).
- `jee-05.md` — Definite-Integral Properties and Symmetry (**JEE 9–10**).
- `jee-06.md` — King's Property and Reflection Symmetry (**JEE 11–12**).
- `jee-07.md` — Improper Integrals I — Infinite Intervals (**JEE 13–14**).
- `jee-08.md` — Improper Integrals II — Singular Endpoints and Logarithms (**JEE 15–16**).
- `jee-09.md` — Inversion and Absolute versus Conditional Convergence (**JEE 17–18**).
- `jee-10.md` — Area I — Vertical Slices and Total Area (**JEE 19–20**).
- `jee-11.md` — Area II — Split Slices, Horizontal Strips and Ellipses (**JEE 21–22**).
- `jee-visual-01.md` — Visual Lab 1 — Right-Endpoint Rectangles (**JEE 23**).
- `jee-visual-02.md` — Visual Lab 2 — Accumulated Area and Its Derivative (**JEE 24**).
- `jee-visual-03.md` — Visual Lab 3 — King's Reflection (**JEE 25**).
- `jee-visual-04.md` — Visual Lab 4 — An Infinite Tail with Finite Area (**JEE 26**).
- `jee-visual-05.md` — Visual Lab 5 — Signed Area versus Total Area (**JEE 27**).
- `jee-visual-06.md` — Visual Lab 6 — Area between Sine and Cosine (**JEE 28**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Wallis Reduction and the Wallis Product (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Beta and Gamma Functions, Reflection and Duplication (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — The Gaussian Integral, Scaling and Its Cosine Transform (**Olympiad 5–6**).
- `olympiad-04.md` — Extension IV — Frullani Integrals and the Sine-Difference Correction (**Olympiad 7–8**).
- `olympiad-05.md` — Extension V — Feynman Differentiation under the Integral Sign (**Olympiad 9–10**).
- `olympiad-06.md` — Extension VI — Q37, the Dirichlet Integral (**Olympiad 11–12**).
- `olympiad-07.md` — Extension VII — Additional Special Values and Logarithmic Trigonometry (**Olympiad 13–14**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes and JSON diagram specifications. Lessons start on fresh sheets; long lessons continue automatically without shrinking body text or clipping formulas. Running headers retain lesson or section context and the current sheet count.

The shared graph builder supports editable curves, points, right-endpoint rectangles and signed area fills, including numeric fill baselines. The mathematical suite reads the actual JSON specifications and checks curve values, rectangle heights, fill expressions, intersections, areas, table dimensions and workflow labels. Both source SVG concepts are recreated as editable graphs rather than embedded screenshots.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 417 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite uses exact `Fraction` identities, fourth-order finite differences, composite Simpson quadrature, transformed improper-integral checks, Wallis recurrences, Gamma identities and an accelerated Dirichlet-arch calculation. It tests every deferred paper question, explicitly rejects the source's incorrect Q36/Gamma/Q45 candidates, verifies the corrected sine-Frullani limit, and checks all six visual-lab models.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the lesson ribbons and read straight down each sheet, then continue on the next sheet. See [`SCOPE.md`](SCOPE.md) for official/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for the complete S/P/Q/SVG map and correction notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
