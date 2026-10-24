# Chapter 20 — Indefinite Integration

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter develops antiderivatives, constants and domains, substitution, standard forms, trigonometric preparation, integration by parts, partial fractions and the half-angle substitution in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated six-page visual lab.

## Current edition

- **Part I — JEE Main + Advanced:** 30 sheets across 13 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 10 sheets across 5 source lessons in `Olympiad/`.
- **Total:** 40 A4 sheets and 25 editable diagram blocks: 10 graphs, 6 workflows and 9 decision tables.
- **Visual expansion:** `jee-90-visual-integration.md` adds 6 sheets on vertical antiderivative families, logarithm branches, by-parts slopes, partial fractions, equivalent answers and half-angle branches.
- **Mathematical verification:** 631 exact/rational, numerical, visual-lab and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/20-indefinite-integration-combined-sheets.zip`](exports/20-indefinite-integration-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/20-indefinite-integration-JEE-sheets.zip`](exports/20-indefinite-integration-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/20-indefinite-integration-Olympiad-sheets.zip`](exports/20-indefinite-integration-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/20-indefinite-integration-combined.pdf`](exports/20-indefinite-integration-combined.pdf) |
| JEE bookmarked PDF | [`exports/20-indefinite-integration-JEE.pdf`](exports/20-indefinite-integration-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/20-indefinite-integration-Olympiad-extensions.pdf`](exports/20-indefinite-integration-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Antiderivatives, Constants and the Standard Library (**JEE 1–2**).
- `jee-02.md` — Substitution — Reverse the Chain Rule (**JEE 3–4**).
- `jee-03.md` — Logarithmic Substitution and Trigonometric Integrals (**JEE 5–6**).
- `jee-04.md` — Algebra and Trigonometric Preparation (**JEE 7–8**).
- `jee-05.md` — Inverse-Trigonometric Standard Forms (**JEE 9–10**).
- `jee-06.md` — Difference-of-Squares and Radical Standard Forms (**JEE 11–12**).
- `jee-07.md` — Integration by Parts — Polynomial, Logarithm and Inverse (**JEE 13–14**).
- `jee-08.md` — Integration by Parts — Cyclic and Algebraic Products (**JEE 15–16**).
- `jee-09.md` — Partial Fractions — Division and Linear Factors (**JEE 17–18**).
- `jee-10.md` — Partial Fractions — Quadratics and the P8 Correction (**JEE 19–20**).
- `jee-11.md` — The Half-Angle Substitution (**JEE 21–22**).
- `jee-12.md` — Method Selection, Equivalent Answers and Final Verification (**JEE 23–24**).
- `jee-90-visual-integration.md` — Visual Lab — Six Ways to See an Antiderivative (**JEE 25–30**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Euler Substitution for Radicals (**Olympiad 1–2**).
- `olympiad-02.md` — Extension II — Reduction Formulae and Recurrence (**Olympiad 3–4**).
- `olympiad-03.md` — Extension III — Parameter Differentiation (**Olympiad 5–6**).
- `olympiad-04.md` — Extension IV — Non-Elementary Antiderivatives (**Olympiad 7–8**).
- `olympiad-05.md` — Extension V — Complexification and Ansatz (**Olympiad 9–10**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

The shared graph builder evaluates the actual antiderivative and integrand expressions. The mathematical suite differentiates those plotted functions numerically, checks point and tangent anchors, tests table dimensions and workflow labels, and independently inspects all six visual-lab models.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 631 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks the standard library, substitutions, logarithmic and inverse-trigonometric forms, trigonometric preparation, by-parts, partial fractions, the half-angle branch, Euler substitution, reduction recurrences, parameter differentiation, special-function derivatives and complexification. Fourth-order finite differences supplement exact Fraction identities, independent coefficient solves, recursive closed forms, an `erf` derivative check and a power-series oracle for `Si`. The incorrect source P8 answer is explicitly differentiated and rejected.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for the official/extension boundaries and the Chapter 21 partition, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source/question coverage and correction notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.
