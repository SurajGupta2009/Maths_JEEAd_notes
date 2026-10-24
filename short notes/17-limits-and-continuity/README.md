# Chapter 17 — Limits & Continuity

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter develops limits, indeterminate forms, continuity and the Intermediate Value Theorem in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated six-page visual lab.

## Current edition

- **Part I — JEE Main + Advanced:** 25 sheets across 10 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 10 sheets across 5 source lessons in `Olympiad/`.
- **Total:** 35 A4 sheets and 21 editable diagram blocks: 17 graphs, 3 workflows and 1 decision table.
- **Visual expansion:** `jee-90-visual-methods.md` adds 6 sheets on holes, squeeze bounds, trigonometric targets, exponential asymptotes, continuous joins and IVT crossings.
- **Mathematical verification:** 356 exact/rational, numerical, visual-lab and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/17-limits-and-continuity-combined-sheets.zip`](exports/17-limits-and-continuity-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/17-limits-and-continuity-JEE-sheets.zip`](exports/17-limits-and-continuity-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/17-limits-and-continuity-Olympiad-sheets.zip`](exports/17-limits-and-continuity-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/17-limits-and-continuity-combined.pdf`](exports/17-limits-and-continuity-combined.pdf) |
| JEE bookmarked PDF | [`exports/17-limits-and-continuity-JEE.pdf`](exports/17-limits-and-continuity-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/17-limits-and-continuity-Olympiad-extensions.pdf`](exports/17-limits-and-continuity-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — The Meaning of a Limit — Approach and ε–δ (**JEE 1–2**).
- `jee-02.md` — Algebraic Limits — Laws, Factoring and Rationalising (**JEE 3–4**).
- `jee-03.md` — Squeeze and Trigonometric Limits (**JEE 5–6**).
- `jee-04.md` — Exponential, Logarithmic and Power Limits (**JEE 7–8**).
- `jee-05.md` — Limits at Infinity, Growth and Asymptotes (**JEE 9–10**).
- `jee-06.md` — L'Hôpital's Rule and Indeterminate Forms (**JEE 11–12**).
- `jee-07.md` — Continuity — When the Limit Equals the Value (**JEE 13–14**).
- `jee-08.md` — The Intermediate Value Theorem and Roots (**JEE 15–16**).
- `jee-09.md` — Mixed Limit and Continuity Strategy (**JEE 17–19**).
- `jee-90-visual-methods.md` — Visual Limits and Continuity Lab (**JEE 20–25**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Sequential Criteria and Nonexistence (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Stolz–Cesàro and Recursive Sequences (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — Limits of Sums and Products (**Olympiad 5–6**).
- `olympiad-04.md` — Extension IV — Stirling, Harmonic Limits and Rates (**Olympiad 7–8**).
- `olympiad-05.md` — Extension V — Functional Equations and IVT Constructions (**Olympiad 9–10**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

The shared graph builder supports piecewise curves, open and filled points, horizontal and vertical asymptotes, bands, sampled rays and annotations. The mathematical suite evaluates the actual JSON curve expressions and point coordinates, including every Heine-sequence marker, recurrence ordinate and Riemann sample.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 356 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks the ε–δ model, factor and conjugate identities, standard limits, power forms, asymptotes, L'Hôpital examples, continuity parameters, bisection roots, sequential nonexistence, Stolz–Cesàro, recurrences, Riemann sums, product bounds, Stirling, harmonic asymptotics, convergence rates and functional equations. It also tests the editable figure inventory and six-page visual lab. These checks supplement—not replace—proofs and native-size visual review.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for the official/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source coverage and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
