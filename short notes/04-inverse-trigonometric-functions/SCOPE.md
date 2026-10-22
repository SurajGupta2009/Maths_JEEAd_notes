# Scope — Chapter 4: Inverse Trigonometric Functions

## In Part I (JEE core) — 13 sheets

- **Why branches exist**: sine/cosine/tangent are not injective; the inverse
  needs a restricted domain; the three principal branches as *definitions*
  (greatest range convention), with domains and ranges stated for all six
  functions (`sin⁻¹`, `cos⁻¹`, `tan⁻¹`, `cot⁻¹`, `sec⁻¹`, `csc⁻¹`).
- **Graphs**: each inverse graph with its domain on the x-axis and branch on
  the y-axis; the reflection construction; monotonicity on each branch.
- **Standard values** at 0, ±1/2, ±√2/2, ±√3/2, ±1 and 0, ±1/√3, ±1, ±√3, ±∞.
- **Compositions**: `sin⁻¹(sin x)` (triangle-wave), `cos⁻¹(cos x)`,
  `tan⁻¹(tan x)`, with full piecewise closed forms on the stated intervals;
  the related `sin⁻¹(cos x)`, `cos⁻¹(sin x)` reductions.
- **Trig of an inverse**: `sin(sin⁻¹x) = x` on [-1,1]; `cos(sin⁻¹x) = √(1−x²)`;
  `tan(sin⁻¹x)`, `tan(cos⁻¹x)`, `sin(tan⁻¹x)`, `cos(tan⁻¹x)` with domains.
- **`2tan⁻¹x`**: the three faces (`sin⁻¹` form on |x| ≤ 1, `cos⁻¹` form on
  x ≥ 0, `tan⁻¹` form on |x| < 1) with the sign/branch conditions.
- **Addition formulas**: `tan⁻¹x + tan⁻¹y` with the xy < 1, xy > 1 faces and
  the subtraction formula; `sin⁻¹x ± sin⁻¹y` and `cos⁻¹x ± cos⁻¹y` derived
  from the addition laws with their case conditions (not recited blind).
- **Worked set**: standard values/identities, equations (`tan⁻¹x = cos⁻¹x`
  giving x = √((√5−1)/2)), piecewise functions and their ranges, extrema of
  `tan⁻¹(sinx) + tan⁻¹(cosx)` (max = tan⁻¹(2√2)).
- **Equations/inequalities/parameters**: domain-first method, monotonicity
  flipping, range as a constraint, parameter hits.
- **Recap toolkit** + **forward map** (calculus: `d/dx sin⁻¹x`, `∫dx/(1+x²)`;
  complex: Arg; coordinate geometry).

## In Part II (Olympiad extensions) — 6 sheets

- Piecewise masters: the full closed form of `f(x) = sin⁻¹(sinx) + cos⁻¹(cosx)`
  (peaks/triangles construction; range [0,π]; max 3π/2 problem); similar
  masters (`tan⁻¹(sinx)+tan⁻¹(cosx)`, `sin⁻¹(sinx)+sin⁻¹(cosx)`).
- Telescoping arctan series: the three splits
  `tan⁻¹(k+1)−tan⁻¹k`, `tan⁻¹(k+1)−tan⁻¹(k−1)`, `tan⁻¹(k−1)−tan⁻¹k`, with
  closed forms, limits (3π/4, π, π/2, π/4 as computed), products, and
  variants (`2k/(k⁴+k²+2)`, `2/(k²−k+1)` partial-range case).
- Hidden-structure identities: `x+y+z = xyz ⇒ sum = π` (x,y,z > 0; degenerate
  face when xy+yz+zx > 1 with the correction term), `xy+yz+zx = 1 ⇒ sum = π/2`,
  with proofs from the tan addition law and worked examples; min-max under
  linear constraints (`x+y = k`), convexity/monotonicity facts; parameterised
  equations (`tan⁻¹x = α`).

## Explicitly out of scope

- Hyperbolic functions and their inverses (not in the JEE Advanced syllabus).
- Heavy ε–δ analysis of continuity/differentiability of the inverse functions
  (that is the calculus chapter's job; only the needed facts appear).
- Values of `tan⁻¹x + tan⁻¹y` beyond the stated cases (they follow from the
  case table by symmetry; the table itself is complete).

## Classification notes

- The `tan⁻¹` addition case table is treated as core (it is the exam's
  favourite trap) and derived in Part I, not deferred to Part II.
- The `x+y+z = xyz` identity family is Part II: the *statement* is
  exam-accessible, but the careful treatment of degenerate cases and
  constrained min-max is technique-heavy olympiad style. Nothing in it
  "can never appear in JEE" — it is simply the harder, technique-heavy end,
  and everything used is derived in Part I.
