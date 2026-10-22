# Chapter 3 — Trigonometric Identities & Equations (handwritten-style short notes)

Print-ready explanatory sheet set for the JEE Advanced Mathematics chapter **Trigonometric Identities & Equations** (syllabus sentence: "Trigonometric functions. General solution of trigonometric equations. Identities."). Dense teacher-style notes — intuition, derivations, formulas, applications, assumptions and common mistakes together — not a formula sheet.

## Parts and sheets

- **`JEE/` — Part I (JEE Main + Advanced core): 10 sheets** (`01.png`…`10.png`), independently numbered with visible part/page labels.
- **`Olympiad/` — Part II (extensions): 6 sheets** (`01.png`…`06.png`), independently numbered, each with a status banner.
- PNG specs: 2480×3508 px portrait, nominal 300 DPI metadata, ~10 mm safe margins, one sheet = one A4 page when printed **Fit**.

## Deliverables

| File | What |
|---|---|
| `exports/03-trigonometric-identities-equations-JEE-sheets.zip` | Part I PNGs |
| `exports/03-trigonometric-identities-equations-Olympiad-sheets.zip` | Part II PNGs |
| `exports/03-trigonometric-identities-equations-combined-sheets.zip` | all 16 PNGs, JEE first |
| `exports/03-trigonometric-identities-equations-JEE.pdf` | bookmarked A4 PDF, Part I |
| `exports/03-trigonometric-identities-equations-Olympiad-extensions.pdf` | bookmarked A4 PDF, Part II |
| `exports/03-trigonometric-identities-equations-combined.pdf` | bookmarked A4 PDF, JEE first |
| `index.html` | gallery (open in a browser) |

## Content map (sheet → topic)

**Part I.** 01 six ratios, unit-circle definition, Pythagorean/reciprocal identities, domains & ranges · 02 quadrant signs, allied angles (rotation derivation), standard values, periods · 03 compound angles with the $\cos(A-B)$ chord derivation and the $a\sin x + b\cos x$ bound · 04 double/triple/half angles, power reduction, quadrant-resolved radicals · 05 product↔sum transformation formulae · 06 general solutions (unit-circle derivation, $(-1)^{n}$ explained), solution counting · 07 equation methods: factorise-not-divide, harmonic form + compatibility, polynomial-in-ratio, squaring + filtering · 08 conditional identities $A+B+C=\pi$ with worked $\tan 20^{\circ}\tan 40^{\circ}\tan 80^{\circ} = \sqrt{3}$ · 09–10 recap toolkit, assumptions, trap sweep.

**Part II (extensions — see SCOPE.md).** 01 Weierstrass substitution $t = \tan\frac{A}{2}$ with the $A = \pi$ blind spot · 02 products of sines/cosines from roots of unity · 03 telescoping trig series and square sums $\sum \cot^{2}, \sum \csc^{2}$ · 04–05 triangle toolkit (sine/cosine rules, $\Delta$, $R$, $r$) + derived special values $\sin 18^{\circ}, \cos 36^{\circ}$ — **explicitly labelled** as outside the current Advanced syllabus sentence.

## What was verified (not a claim of exhaustive mathematical verification)

- **Independent numeric checks** — `scripts/math_checks.py`: **194/194 PASS** (Pythagorean/reciprocal identities at random angles, every compound/multiple/half-angle identity, transformation formulae, general-solution families at $n = -3\ldots3$, every equation worked example re-substituted, conditional identities on several triangles, $\tan 20^{\circ}\tan 40^{\circ}\tan 80^{\circ} = \sqrt{3}$, Weierstrass conversions, roots-of-unity products $n = 5, 6, 7$, $\sum \cot^{2}/\csc^{2}$ for $n = 3\ldots7$, series closed forms, $\sin 18^{\circ}/\cos 36^{\circ}$, triangle worked example including $R$, $r$, $\tan\frac{A}{2}$ cross-check).
- **Automated render checks** — `scripts/check.py`: formula parsing, font/glyph coverage, sheet size/DPI/margin ink scans, numbering, ZIP/PDF integrity + bookmarks, gallery links.
- **Visual** — all 16 sheets reviewed at contact-sheet resolution; every diagram (unit circle ×2, sin/cos waves, general-solution wave, solution number line) inspected at full resolution; label collisions found in review were corrected and re-rendered.

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
