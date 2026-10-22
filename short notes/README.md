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

| # | Chapter (slug) | Official unit(s) | Status |
|---|---|---|---|
| 1 | **Sets, Relations & Functions** (`01-sets-relations-functions`) | Sets, Relations and Functions | ✅ **delivered** — 12 JEE + 6 Olympiad sheets |
| 2 | **Exponents & Logarithms** (`02-exponents-logarithms`) | Algebra (logarithms and their properties) | ✅ **delivered** — 9 JEE + 3 Olympiad sheets |
| 3 | **Trigonometric Identities & Equations** (`03-trigonometric-identities-equations`) | Trigonometry | ✅ **delivered** — 11 JEE + 6 Olympiad sheets |
| 4 | **Inverse Trigonometric Functions** (`04-inverse-trigonometric-functions`) | Trigonometry | ✅ **delivered** — 13 JEE + 6 Olympiad sheets |
| 5 | **Complex Numbers** (`05-complex-numbers`) | Algebra (complex numbers, FTA) | ✅ **delivered** — 18 JEE + 11 Olympiad sheets |
| 6 | **Quadratic Equations** (`06-quadratic-equations`) | Algebra (quadratics with real coefficients) | ✅ **delivered** — 8 JEE + 3 Olympiad sheets |
| 7 | **Sequences & Series** (`07-sequences-and-series`) | Algebra (AP, GP, AM, GM, special sums) | ✅ **delivered** — 5 JEE + 3 Olympiad sheets |
| 8 | **Permutations & Combinations** (`08-permutations-and-combinations`) | Algebra (P&C) | ✅ **delivered** — 7 JEE + 3 Olympiad sheets |
| 9 | **Binomial Theorem** (`09-binomial-theorem`) | Algebra (binomial theorem, positive integral index) | ✅ **delivered** — 4 JEE + 2 Olympiad sheets |
| 10 | Matrices & Determinants (`10-matrices-and-determinants`) | Matrices | ⏳ pending |
| 11 | Probability & Statistics (`11-probability-and-statistics`) | Probability and Statistics | ⏳ pending |
| 12 | Straight Lines & Locus (`12-straight-lines-and-locus`) | Analytical Geometry 2D (lines, triangle centres, locus) | ⏳ pending |
| 13 | Circles (`13-circles`) | Analytical Geometry 2D (circle) | ⏳ pending |
| 14 | Conic Sections (`14-conic-sections`) | Analytical Geometry 2D (parabola, ellipse, hyperbola) | ⏳ pending |
| 15 | Vectors (`15-vectors`) | Vectors | ⏳ pending |
| 16 | Three-Dimensional Geometry (`16-three-dimensional-geometry`) | Analytical Geometry 3D | ⏳ pending |
| 17 | Limits & Continuity (`17-limits-and-continuity`) | Differential Calculus (limits, continuity, L'Hospital, IVT) | ⏳ pending |
| 18 | Differentiability & Methods (`18-differentiability-and-methods`) | Differential Calculus (derivatives, chain rule, implicit) | ⏳ pending |
| 19 | Applications of Derivatives (`19-applications-of-derivatives`) | Differential Calculus (tangents, monotonicity, extrema, Rolle, LMVT) | ⏳ pending |
| 20 | Indefinite Integration (`20-indefinite-integration`) | Integral Calculus (indefinite integrals, substitution, parts, partial fractions) | ⏳ pending |
| 21 | Definite Integration & Areas (`21-definite-integration-and-areas`) | Integral Calculus (limit of sums, FTC, properties, area) | ⏳ pending |
| 22 | Differential Equations (`22-differential-equations`) | Integral Calculus (formation, homogeneous 1st order, separation, linear 1st order) | ⏳ pending |

Chapters 4–22 are **pending** — they will be authored one by one in exactly
the Chapter-1 format. Repo vault notes (`notes/`) are the primary source
wherever they cover a chapter (they cover 15 of these + extra olympiad
machinery); missing coverage is authored from the official syllabus and
disclosed per chapter in that chapter's `SOURCE-AUDIT.md`. Chapter 2 had **no**
vault source module (disclosed in its SOURCE-AUDIT); chapter 3 drew on
`notes/Trigonometry/`.

## Per-chapter deliverables (as in Chapter 1)

`short notes/<slug>/:` `JEE/` numbered PNG sheets · `Olympiad/` numbered PNG
sheets · `exports/` **three PNG ZIPs + three bookmarked A4 PDFs** (JEE,
extensions, combined — JEE first) · `index.html` gallery · `README.md` ·
`SCOPE.md` · `SOURCE-AUDIT.md` · `PRINTING.txt` · `content/` editable Markdown
· `scripts/` render/export/check + mathematical checks.

Format: 2480×3508 px @ 300 DPI, 10 mm safe margins, faintly ruled paper,
handwriting body ≈ 11.5 pt; navy prose · teal headings/explanations · yellow
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
