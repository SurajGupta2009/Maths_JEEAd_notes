# Source Audit — Chapter 5: Complex Numbers and Quadratic Equations (Complex Numbers strand)

## Sources

- `notes/Complex-Numbers/Complex-Numbers.md` — the repository's own chapter
  (2079 lines). Read in full before authoring. Additional unread file
  `notes/Complex-Numbers/— Paper.md` and `— Solutions.md` (practice
  problems) and `assets/fig-01..04.svg` exist but the main markdown is the
  complete theory source used here.
- Official JEE Advanced 2026 syllabus (jeeadv.ac.in PDF), MATHEMATICS §2
  (Algebra): "complex numbers ... algebra of complex numbers, polar
  representation, triangle inequality ... fundamental theorem of algebra,
  quadratic equations in real and complex number system and their solutions,
  roots and coefficients" — used to set boundaries (FTOA stated as theorem
  context only; the quadratic-equations strand is chapter 6).

## Independent verification performed

Every numeric and symbolic claim was machine-checked by
`scripts/math_checks.py` (206 assertions, all passing), covering:
arithmetic examples; modulus/argument of every worked value (four-quadrant
atan corrections); polar round-trips; De Moivre powers; roots of 8, 16 and
−27 (all three cube roots); the square-root formula at several points
including the negative-real face; ω identities and vanishing sums;
∏(1−ζₖ) = n at n = 3,4,5,6 and the filter totals (170, 171, 171, 29);
locus test points (P34 circle x² + (y−1)² = 2 upper arc; P35 ellipse
b = 2√2; the [2, 2√2] range at four points); equilateral conditions in both
orientations; area formula (P37 = 7/2); Ptolemy identity on a cyclic
example and the British-flag theorem; Van Aubel perpendicularity and
equal-length segments; Napoleon (all three mutual distances equal at the
quoted numeric value); Leibniz minimum 30; Joukowski limits (image [−2,2],
ellipse axes R ± 1/R); Gauss sums G(2..12) against the closed form;
Gauss–Lucas critical points of z(z−2)(z−1−2i) = 1+i, 1+i/3 (inside the
root triangle); Pompeiu distance triples at two points.

## Corrections to the source and completeness pass

- **Official-syllabus omission found in the prior sheet set:** although the
  scope/audit had named the Fundamental Theorem of Algebra, the theorem
  statement was absent from the rendered JEE content. Added it to JEE-07 as
  a statement-only result, including the nonconstant-polynomial hypothesis
  and multiplicity conclusion; no proof is implied.
- **Arg of a quotient trap**: the source's method "arg(z₁/z₂) = arg z₁ −
  arg z₂" is only true mod 2π; with z₁ = 1, z₂ = −1 the naive difference is
  −π while Arg(1/(−1)) = π. The sheets state the congruence and the
  principal-value correction (±2π) explicitly, with this example.
- The source occasionally writes `2kπ` adjustments in prose only; the sheets
  state the general periodic reduction formulas as displayed piecewise
  results (the sawtooth for sin⁻¹(sin t), the triangle for cos⁻¹(cos t))
  so the adjustment is never left implicit.
- Some source numeric checks are quoted without derivation (e.g. the
  Napoleon centers); the sheets recompute them and `math_checks.py`
  verifies the equal-sides claim independently.
- Nested quotes in problem statements were normalised to dashes; all
  `\pmod`/`\bmod` spellings were converted to `\mathrm{mod}` (renderer
  compatibility) without changing meaning.

## Unresolved assumptions

- The source defines the principal argument with |Arg| ≤ π (Arg = π at the
  negative real axis). Some texts use [0, 2π). The sheets state the
  convention wherever it matters; the worked examples are consistent with
  it.
- The source's square-root formula for √z writes sgn(b) and is silent on
  b = 0; the sheets state the b = 0 face (z real): √z is real for z ≥ 0 and
  purely imaginary for z < 0 under the principal-branch reading of the
  ±-pair. Verified in `math_checks.py`.
- For the ellipse from |z−A| + |z−B| = 2a₀ the sheets require 2a₀ > |A−B|
  (non-degenerate) and note the degenerate face; the source is silent.
- Chapter 6 (quadratic equations) will cover the remaining syllabus bullet;
  the overlap "complex roots of real quadratics" appears here only as needed
  for the loci/argument material.
