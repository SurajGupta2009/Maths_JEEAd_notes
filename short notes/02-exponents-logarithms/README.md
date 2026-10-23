# Chapter 2 — Exponents & Logarithms (handwritten-style short notes)

Print-ready explanatory sheet set for the JEE Advanced Mathematics chapter **Exponents & Logarithms** (Algebra: "Logarithms and their properties", with the exponent/indices machinery the topic presupposes). Dense teacher-style notes — intuition, derivations, formulas, applications, assumptions and common mistakes together — not a formula sheet.

## Parts and sheets

- **`JEE/` — Part I (JEE Main + Advanced core): 9 sheets** (`01.png`…`09.png`), independently numbered with visible part/page labels.
- **`Olympiad/` — Part II (extensions): 3 sheets** (`01.png`…`03.png`), independently numbered, each with a status banner.
- PNG specs: 2480×3508 px portrait, nominal 300 DPI metadata, ~10 mm safe margins, one sheet = one A4 page when printed **Fit**.

## Deliverables

| File | What |
|---|---|
| `exports/02-exponents-logarithms-JEE-sheets.zip` | Part I PNGs |
| `exports/02-exponents-logarithms-Olympiad-sheets.zip` | Part II PNGs |
| `exports/02-exponents-logarithms-combined-sheets.zip` | all 12 PNGs, JEE first |
| `exports/02-exponents-logarithms-JEE.pdf` | bookmarked A4 PDF, Part I |
| `exports/02-exponents-logarithms-Olympiad-extensions.pdf` | bookmarked A4 PDF, Part II |
| `exports/02-exponents-logarithms-combined.pdf` | bookmarked A4 PDF, JEE first |
| `index.html` | gallery (open in a browser) |

## Content map (sheet → topic)

**Part I.** 01 laws of indices, base/rational-exponent conventions, parity repairs · 02 the exponential function $a^{x}$, monotonicity, $e$, substitution method · 03 logarithm definition, laws (derived), change of base, graphs · 04 simplification, sign rule, digit formula, comparisons ($e^{\pi}$ vs $\pi^{e}$) · 05 exponential & logarithmic equations with domain-first discipline · 06 inequalities, digits & magnitude models, growth models, parameters · 07–09 recap toolkit, assumptions, trap sweep.

**Part II (extensions — see SCOPE.md for classification).** 01 $x^{y} = y^{x}$ full classification, multi-base log systems, towers · 02 growth hierarchy, digits, Legendre's formula · 03 series/log estimates.

## What was verified (not a claim of exhaustive mathematical verification)

- **Independent numeric checks** — `scripts/math_checks.py`: **163/163 PASS** (index laws, parity repairs through real odd roots, every worked example's solutions re-substituted, log laws/change of base/sign rule at random bases, digits of $2^{100}$ and $3^{50}$, $e^{\pi} > \pi^{e}$, $x^{y}=y^{x}$ parametrisation, Legendre's formula for several $n, p$, harmonic bounds).
- **Automated render checks** — `scripts/check.py`: formula parsing, font/glyph coverage, sheet size/DPI/margin ink scans, numbering, ZIP/PDF integrity + bookmarks, gallery links.
- **Visual** — every sheet reviewed at contact-sheet resolution; both diagrams (exponential family, log curves) inspected at full resolution for label collisions and clipping.

## Rebuild

```bash
python3 scripts/render.py    # content/*.md -> JEE/, Olympiad/ PNGs
python3 scripts/export.py    # ZIPs + PDFs + index.html
python3 scripts/check.py     # reproducible deliverable checks
python3 scripts/math_checks.py
```

Requires the shared engine in `../_engine/` (see `../_engine/requirements.txt`). Sources are editable in `content/*.md`.

## Printing

A4 portrait, one sheet per page, **Fit** (not Fill/Crop) — see `PRINTING.txt`.

## Reading order

Follow the `LESSON n / total` ribbons; read down the left column, then down the right column, and continue to the next sheet. This sequence follows the chapter’s prerequisite path.
