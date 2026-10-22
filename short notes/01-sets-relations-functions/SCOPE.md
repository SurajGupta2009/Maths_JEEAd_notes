# SCOPE — Complete JEE Advanced Mathematics Chapter List & Build Status

**Master list lives in [`../README.md`](../README.md)** (the `short notes/`
index). This file records, for Chapter 1, exactly what is covered, how it is
classified, and how the complete list was derived.

## Source of the chapter list

The complete chapter list is taken from the **official JEE (Advanced) 2026
Syllabus — MATHEMATICS** (published by the JEE Advanced organising institute at
`jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf`, retrieved 2026-10-22;
the 2026 syllabus is officially unchanged from 2025). The official document
lists **nine units**: Sets, Relations and Functions · Algebra · Matrices ·
Probability and Statistics · Trigonometry · Analytical Geometry (two and three
dimensions) · Differential Calculus · Integral Calculus · Vectors.

For study purposes the units are split into **22 chapters** in prerequisite
order (every official bullet maps into exactly one chapter — see the master
list). Chapter 1 is **Sets, Relations and Functions**, the official first unit.

## Coverage of this chapter (syllabus bullet → sheet)

Official unit text: *sets and their representations, different kinds of sets
(empty, finite and infinite), algebra of sets, intersection, complement,
difference and symmetric difference of sets and their algebraic properties,
De-Morgan's laws … practical problems; Cartesian product of finite sets,
ordered pair, relations, domain and codomain of relations, equivalence
relation; function as a special case of relation, functions as mappings,
domain, codomain, range, invertible functions, even and odd functions, into,
onto and one-to-one functions, special functions (polynomial, trigonometric,
exponential, logarithmic, power, absolute value, greatest integer, etc.), sum,
difference, product and composition of functions.*

| Official bullet | Where |
|---|---|
| Set representations; empty/finite/infinite | JEE 01 |
| Algebra of sets; ∩, complement, difference, symmetric difference; algebraic properties | JEE 03 (definitions), JEE 03–04 (laws) |
| De Morgan's laws (finite families), practical problems | JEE 03 (derived, n-set form), JEE 04 (counting model) |
| Cartesian product, ordered pair | JEE 05 |
| Relations; domain and codomain of relations | JEE 05–06 |
| Equivalence relation | JEE 07–08 |
| Function as special relation; mappings; domain, codomain, range | JEE 09–10 |
| Invertible functions | JEE 11 (inverse; $f^{-1}$ exists iff bijective) |
| Even and odd functions | JEE 12 |
| Into, onto, one-to-one | JEE 12 |
| Special functions (polynomial, trig, exp, log, power, abs, greatest integer, etc.) | JEE 09 (domain rules incl. trig/exp/log), JEE 11 (abs, sgn, floor, frac graphs) |
| Sum, difference, product, composition of functions | JEE 11 (composition, domains of composites; sums/products covered by domain rules and examples) |

Classification is **concept-by-concept by relevance and prerequisites**, not by
source-heading order: language → operations → products/relations → equivalence
→ functions → special functions → classification (one-one/onto/even/odd/
periodic) → composition & inverse → recap.

## Part I vs Part II

- **Part I (JEE Main + Advanced core + useful derivable applications)**
  includes everything the official bullet list names, plus directly derivable
  applications JEE papers actually ask: $n(A\cup B\cup C)$, relation/function
  counting with axiom constraints, small-case onto counts, graph
  transformations, composite domains, boundary-conditioned domain/range
  problems. Difficult-but-useful JEE applications are kept **in Part I**, not
  pushed to Part II.
- **Part II (Olympiad IOQM/RMO / specialised extensions)**: the full
  antisymmetric/surjection catalogue with inclusion–exclusion and Stirling
  cross-checks; Bell numbers; Cauchy/Pexider/Jensen/involution functional
  equations; Hermite's identity; floor-equation and fixed-point toolkit. Each
  Part II sheet opens with a **status note** distinguishing *additional theory*
  from *models derivable with supplied information*. We do **not** claim any
  extension "can never appear in JEE" — JEE has historically leaked
  olympiad-flavoured models; what is not promised is theory beyond the stated
  statements.

## Assumptions & interpretation choices (see SOURCE-AUDIT.md for the full log)

- The official list's "special functions (…, etc.)" is open-ended; we include
  $\operatorname{sgn} x$ and $\{x\}$ as standard companions of $|x|$ and $[x]$
  (all reducible to listed functions).
- $\subset$ is used for *proper* subset on the sheets; $\subseteq$ for general
  subset (stated explicitly — conventions differ across textbooks).
- "Into" is treated as "not onto" (the modern reading); the old "into =
  any function" sense is flagged as deprecated.
- Counting statements assume finite sets with labelled elements unless stated.

## Build status of the 22-chapter programme

| # | Chapter | Status |
|---|---|---|
| 1 | sets-relations-functions | ✅ **delivered** (this folder: 12 JEE + 6 Olympiad sheets) |
| 2–22 | exponents-logarithms … differential-equations | ⏳ pending — to be authored one by one in this format |

No other chapter folders exist yet, so there are no duplicate editions. Each
future chapter gets its own `short notes/<slug>/` folder with the same
deliverable set; the shared engine in `short notes/_engine/` is reused as-is.
