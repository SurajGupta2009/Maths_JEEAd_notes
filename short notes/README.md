# Short Notes — Handwritten-Style Explanatory Sheets for JEE Advanced Maths

Dense, teacher-style short-note **image sets** (exact-A4 PNG sheets at 300 DPI
\+ bookmarked A4 PDFs + ZIPs), built one chapter at a time in prerequisite
order. Each chapter folder is self-contained: editable Markdown content,
render/export scripts, reproducible checks, gallery and audit documents.

Shared engine: [`_engine/`](_engine/) (renderer, diagrams, exports, checks) ·
fonts: [`_assets/fonts/`](_assets/fonts/) (Kalam OFL + DejaVu fallback).

## The complete JEE Advanced Mathematics chapter list (22 chapters)

Derived from the **official JEE (Advanced) 2026 syllabus** (MATHEMATICS,
`jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf`, retrieved 2026-10-22;
2026 = 2025 syllabus). The official nine units — Sets/Relations/Functions,
Algebra, Matrices, Probability & Statistics, Trigonometry, Analytical Geometry
(2D + 3D), Differential Calculus, Integral Calculus, Vectors — are split into
22 study chapters in prerequisite order. Every official bullet maps into
exactly one chapter.

For the 2026 second-pass coverage and page-flow review of delivered chapters 1–13, see [`REVIEW-AND-REORDER-AUDIT.md`](REVIEW-AND-REORDER-AUDIT.md). For the complete Chapter 14–22 request queue and current status, see [`CHAPTER-QUEUE.md`](CHAPTER-QUEUE.md).

| # | Chapter (slug) | Official unit(s) | Status |
|---|---|---|---|
| 1 | **Sets, Relations & Functions** (`01-sets-relations-functions`) | Sets, Relations and Functions | ✅ **delivered** — 26 JEE + 9 Olympiad sheets |
| 2 | **Exponents & Logarithms** (`02-exponents-logarithms`) | Algebra (logarithms and their properties) | ✅ **delivered** — 20 JEE + 4 Olympiad sheets |
| 3 | **Trigonometric Identities & Equations** (`03-trigonometric-identities-equations`) | Trigonometry | ✅ **delivered** — 23 JEE + 8 Olympiad sheets |
| 4 | **Inverse Trigonometric Functions** (`04-inverse-trigonometric-functions`) | Trigonometry | ✅ **delivered** — 28 JEE + 9 Olympiad sheets |
| 5 | **Complex Numbers** (`05-complex-numbers`) | Algebra (complex numbers, FTA) | ✅ **delivered** — 36 JEE + 17 Olympiad sheets |
| 6 | **Quadratic Equations** (`06-quadratic-equations`) | Algebra (quadratics with real coefficients) | ✅ **delivered** — 18 JEE + 6 Olympiad sheets |
| 7 | **Sequences & Series** (`07-sequences-and-series`) | Algebra (AP, GP, AM, GM, special sums) | ✅ **delivered** — 14 JEE + 6 Olympiad sheets |
| 8 | **Permutations & Combinations** (`08-permutations-and-combinations`) | Algebra (P&C) | ✅ **delivered** — 17 JEE + 4 Olympiad sheets |
| 9 | **Binomial Theorem** (`09-binomial-theorem`) | Algebra (binomial theorem, positive integral index) | ✅ **delivered** — 11 JEE + 3 Olympiad sheets |
| 10 | **Matrices & Determinants** (`10-matrices-and-determinants`) | Matrices | ✅ **delivered** — 13 JEE + 4 Olympiad sheets |
| 11 | **Probability & Statistics** (`11-probability-and-statistics`) | Probability and Statistics | ✅ **delivered** — 15 JEE + 4 Olympiad sheets |
| 12 | **Straight Lines & Locus** (`12-straight-lines-and-locus`) | Analytical Geometry 2D (lines, triangle centres, locus tools) | ✅ **delivered** — 17 JEE + 3 Olympiad sheets |
| 13 | **Circles** (`13-circles`) | Analytical Geometry 2D (circle) | ✅ **delivered** — 15 JEE + 4 Olympiad sheets |
| 14 | **Conic Sections** (`14-conic-sections`) | Analytical Geometry 2D (parabola, ellipse, hyperbola) | ✅ **delivered** — 29 JEE + 6 Olympiad sheets |
| 15 | **Vectors** (`15-vectors`) | Vectors | ✅ **delivered** — 24 JEE + 6 Olympiad sheets |
| 16 | **Three-Dimensional Geometry** (`16-three-dimensional-geometry`) | Analytical Geometry 3D | ✅ **delivered** — 25 JEE + 13 Olympiad sheets |
| 17 | **Limits & Continuity** (`17-limits-and-continuity`) | Differential Calculus (limits, continuity, L'Hospital, IVT) | ✅ **delivered** — 25 JEE + 10 Olympiad sheets |
| 18 | **Differentiability & Methods** (`18-differentiability-and-methods`) | Differential Calculus (derivatives, chain rule, implicit) | ✅ **delivered** — 24 JEE + 10 Olympiad sheets |
| 19 | **Applications of Derivatives** (`19-applications-of-derivatives`) | Differential Calculus (tangents, monotonicity, extrema, Rolle, LMVT) | ✅ **delivered** — 28 JEE + 10 Olympiad sheets |
| 20 | **Indefinite Integration** (`20-indefinite-integration`) | Integral Calculus (indefinite integrals, substitution, parts, partial fractions) | ✅ **delivered** — 30 JEE + 10 Olympiad sheets |
| 21 | Definite Integration & Areas (`21-definite-integration-and-areas`) | Integral Calculus (limit of sums, FTC, properties, area) | ⏳ pending — next chapter |
| 22 | Differential Equations (`22-differential-equations`) | Integral Calculus (formation, homogeneous 1st order, separation, linear 1st order) | ⏳ pending |

Chapters 21–22 are **pending**. Chapters 1–20 are delivered in the expanded,
single-stream format: **438 JEE + 146 Olympiad = 584 sheets**. Repo vault notes (`notes/`) are the primary source
wherever they cover a chapter; source coverage and missing material are
documented chapter by chapter in each `SOURCE-AUDIT.md`. Chapters 12–13 draw
on `notes/Coordinate-Geometry-Lines-and-Circles/`; Chapter 14 draws on
`notes/Conic-Sections/`; Chapter 15 draws on `notes/Vectors/`; Chapter 16 draws
on `notes/3D-Geometry/`; Chapter 17 draws on `notes/Limits-and-Continuity/`; Chapter 18 draws on `notes/Differentiation-and-Methods/`; Chapter 19 draws on `notes/Applications-of-Derivatives/`; Chapter 20 draws on `notes/Integration/`; Chapter 3 draws on `notes/Trigonometry/`. Chapter 2
has **no** vault source module (disclosed in its audit).

## Per-chapter deliverables (as in Chapter 1)

`short notes/<slug>/:` `JEE/` numbered PNG sheets · `Olympiad/` numbered PNG
sheets · `exports/` **three PNG ZIPs + three bookmarked A4 PDFs** (JEE,
extensions, combined — JEE first) · `index.html` gallery · `README.md` ·
`SCOPE.md` · `SOURCE-AUDIT.md` · `PRINTING.txt` · `content/` editable Markdown
· `scripts/` render/export/check + mathematical checks.

Format: 2480×3508 px @ 300 DPI, 10 mm safe margins, faintly ruled paper,
handwriting body ≈ 12 pt; navy prose · teal headings/explanations · yellow
key results · red common traps; properly typeset math; programmatically drawn
diagrams with labelled axes/asymptotes/regions. Printing: A4 portrait, one
sheet per page, **Fit** (not Fill/Crop).

## Programme conventions

- **Part I** = JEE Main + Advanced core and useful derivable applications
  (difficult-but-useful JEE applications stay in Part I).
- **Part II** = Olympiad (IOQM/RMO) / specialised extensions, each sheet
  distinguishing additional theory from models derivable from Part I. No
  extension is ever declared impossible in JEE.
- Coverage decides page count: prose is never shrunk to meet a page limit —
  the renderer paginates automatically and the set expands.
- Each sheet shows visible part/page labels; JEE and Olympiad sheets are
  numbered **independently** from 1.
