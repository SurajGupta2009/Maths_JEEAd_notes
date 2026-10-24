# Chapter 22 — Differential Equations

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This final programme chapter covers formation, classification and verification; the first-order JEE methods; exact and orthogonal equations; second-order linear and Euler equations; models and damping; and the Clairaut/Lagrange/Riccati/existence frontier in one top-to-bottom reading stream.

## Current edition

- **Part I — JEE Main + Advanced:** 30 sheets across 18 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 12 sheets across 6 source lessons in `Olympiad/`.
- **Total:** 42 A4 sheets and 24 editable diagram blocks: 8 graphs, 8 workflows and 8 decision tables.
- **Visual lab:** six dedicated sheets for a true slope field, a linear IVP field, orthogonal families, damped envelopes, non-uniqueness and Clairaut envelopes.
- **Mathematical verification:** 711 exact, numerical, source-correction, domain and editable-figure assertions in `scripts/math_checks.py`.
- **Delivery verification:** 56 checks, 628 parsed formulas and 94 valid local gallery links; earlier Chapters 1–21 mathematical suites also pass after the shared-engine additions.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/22-differential-equations-combined-sheets.zip`](exports/22-differential-equations-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/22-differential-equations-JEE-sheets.zip`](exports/22-differential-equations-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/22-differential-equations-Olympiad-sheets.zip`](exports/22-differential-equations-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/22-differential-equations-combined.pdf`](exports/22-differential-equations-combined.pdf) |
| JEE bookmarked PDF | [`exports/22-differential-equations-JEE.pdf`](exports/22-differential-equations-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/22-differential-equations-Olympiad-extensions.pdf`](exports/22-differential-equations-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Terminology, Verification and Solution Intervals (**JEE 1–2**).
- `jee-02.md` — Formation — Eliminate Every Arbitrary Constant (**JEE 3–4**).
- `jee-03.md` — Variables Separable — Integrate, Then Apply the IVP (**JEE 5–6**).
- `jee-04.md` — Homogeneous First-Order Equations (**JEE 7–8**).
- `jee-05.md` — Linear First-Order Equations — Integrating Factors (**JEE 9–10**).
- `jee-06.md` — Bernoulli Equations and Trigonometric Forcing (**JEE 11–12**).
- `jee-07.md` — Exact Equations and Potential Functions (**JEE 13–14**).
- `jee-08.md` — Orthogonal Trajectories — Replace Slope Correctly (**JEE 15–16**).
- `jee-09.md` — Constant-Coefficient Second-Order Equations (**JEE 17–18**).
- `jee-10.md` — Cauchy–Euler Equations — Trial Powers (**JEE 19–20**).
- `jee-11.md` — Growth, Cooling and Reduction for Autonomous Equations (**JEE 21–22**).
- `jee-12.md` — Damping — Under, Critical and Over (**JEE 23–24**).
- `jee-visual-01.md` — Visual Lab 1 — A Real Slope Field and Its Branches (**JEE 25**).
- `jee-visual-02.md` — Visual Lab 2 — A Linear Field and the IVP Curve (**JEE 26**).
- `jee-visual-03.md` — Visual Lab 3 — Parabolas Meeting Ellipses at Right Angles (**JEE 27**).
- `jee-visual-04.md` — Visual Lab 4 — Damped Oscillation and Its Envelope (**JEE 28**).
- `jee-visual-05.md` — Visual Lab 5 — One IVP, Infinitely Many Departures (**JEE 29**).
- `jee-visual-06.md` — Visual Lab 6 — Clairaut Tangents and Their Envelope (**JEE 30**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Reduction of Order and Wronskians (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Clairaut Equations and Singular Envelopes (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — Existence, Uniqueness and Delayed Solutions (**Olympiad 5–6**).
- `olympiad-04.md` — Extension IV — Lagrange's Equation and Q38 (**Olympiad 7–8**).
- `olympiad-05.md` — Extension V — Riccati Equations from a Known Solution (**Olympiad 9–10**).
- `olympiad-06.md` — Extension VI — Nonhomogeneous Second-Order Linear Equations (**Olympiad 11–12**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes and JSON diagram specifications. Lessons start on fresh sheets; long lessons continue automatically without shrinking body text or clipping formulas. Running headers retain lesson or section context and the current sheet count.

The shared graph builder now supports editable `slope_fields`: short, unarrowed line elements evaluated from a restricted expression in both `x` and `y`, with invalid or infinite slopes omitted. Curves, envelopes, branches, points and axes remain JSON-defined. The table builder also has opt-in `strict_fit` and `min_fontsize` settings; all eight Chapter 22 tables use them, so a cell that still overflows at 9 pt fails the render rather than silently overlapping.

Both source SVG concepts are recreated as editable graphs. The slope-field source had no actual field strokes and placed its lower branch outside the viewBox; Visual Lab 1 corrects both issues. Visual Lab 3 recreates the parabola/ellipse orthogonality concept with exact intersections.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 711 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite uses exact residual calculations, fourth-order finite differences, pure-Python scalar and second-order RK4 integration, joining-limit checks, Wronskians and direct branch/domain tests. It covers every Q1–Q41, S1–S21 and P1–P16 destination; explicitly rejects the source's Q38 differentiation and Q34 Wronskian-sign errors; verifies omitted equilibrium/singular branches; and reads the actual JSON figure expressions, slope fields, points and tangent contacts.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links. All 42 pages were reviewed in contact sheets; dense tables, graphs, correction pages and continuations were also inspected at native size.

## Reading order, scope and printing

Follow the lesson ribbons and read straight down each sheet, then continue on the next sheet. See [`SCOPE.md`](SCOPE.md) for official/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for the complete S/P/Q/SVG map and correction notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
