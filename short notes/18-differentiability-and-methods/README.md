# Chapter 18 — Differentiability & Methods

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter develops derivatives from first principles, differentiability, all core differentiation methods and higher derivatives in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated six-page visual lab.

## Current edition

- **Part I — JEE Main + Advanced:** 24 sheets across 10 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 10 sheets across 5 source lessons in `Olympiad/`.
- **Total:** 34 A4 sheets and 20 editable diagram blocks: 12 graphs, 5 workflows and 3 decision tables.
- **Visual expansion:** `jee-90-visual-methods.md` adds 6 sheets on secant convergence, smooth joins, chain-rule scaling, implicit/parametric agreement, variable powers and second parametric derivatives.
- **Mathematical verification:** 402 exact/rational, numerical, visual-lab and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/18-differentiability-and-methods-combined-sheets.zip`](exports/18-differentiability-and-methods-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/18-differentiability-and-methods-JEE-sheets.zip`](exports/18-differentiability-and-methods-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/18-differentiability-and-methods-Olympiad-sheets.zip`](exports/18-differentiability-and-methods-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/18-differentiability-and-methods-combined.pdf`](exports/18-differentiability-and-methods-combined.pdf) |
| JEE bookmarked PDF | [`exports/18-differentiability-and-methods-JEE.pdf`](exports/18-differentiability-and-methods-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/18-differentiability-and-methods-Olympiad-extensions.pdf`](exports/18-differentiability-and-methods-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — The Derivative from First Principles (**JEE 1–2**).
- `jee-02.md` — One-Sided Derivatives and Piecewise Differentiability (**JEE 3–4**).
- `jee-03.md` — The Algebra of Derivatives (**JEE 5–6**).
- `jee-04.md` — The Chain Rule and Standard Functions (**JEE 7–8**).
- `jee-05.md` — Inverse Functions and Inverse Trigonometric Derivatives (**JEE 9–10**).
- `jee-06.md` — Implicit Differentiation (**JEE 11–12**).
- `jee-07.md` — Logarithmic Differentiation (**JEE 13–14**).
- `jee-08.md` — Parametric Differentiation (**JEE 15–16**).
- `jee-09.md` — Higher Derivatives and Method Selection (**JEE 17–18**).
- `jee-90-visual-methods.md` — Visual Differentiation Methods Lab (**JEE 19–24**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Higher Derivatives and Leibniz's Rule (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Advanced Closed Forms and Identities (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — Functional Equations by Differentiation (**Olympiad 5–6**).
- `olympiad-04.md` — Extension IV — Discontinuous Derivatives and Darboux (**Olympiad 7–8**).
- `olympiad-05.md` — Extension V — Rolle, Mean Value and Derivative Inequalities (**Olympiad 9–10**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

The shared graph builder supports piecewise curves, open and filled points, horizontal and vertical asymptotes, sampled rays and annotations. The mathematical suite evaluates the actual JSON curve expressions and point coordinates, including principal-branch endpoints, tangent intersections and oscillatory-derivative sequences.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 402 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks exact difference quotients, one-sided derivatives, product/quotient/chain rules, inverse branches, implicit and parametric derivatives, variable powers, higher derivatives, Leibniz closed forms, functional equations, discontinuous derivatives and MVT inequalities. Independent Cauchy-integral differentiation tests the higher-order formulas. The suite also checks the editable figure inventory and six-page visual lab. These checks supplement—not replace—proofs and native-size visual review.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for the official/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for all source/question coverage and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
