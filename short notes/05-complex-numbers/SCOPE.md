# Scope — Chapter 5: Complex Numbers and Quadratic Equations (Complex Numbers strand)

## In Part I (JEE core) — 18 sheets

- **Algebra of ℂ**: why `i` is forced; conjugate, modulus, real/imaginary
  part as coordinates; division by multiplying by the conjugate; ℂ as a
  field; `z = x + iy` vs `z = r(cosθ + isinθ)` as two languages; conjugation
  is reflection, multiplication by `i` is a 90° rotation.
- **Argument**: principal value `Arg z ∈ (−π, π]`, the four-quadrant
  conventions (with the atan(y/x) quadrant correction), arg of products and
  quotients (mod 2π caveats and the classic `z₁ = 1, z₂ = −1` trap),
  argument of `z − a` as direction.
- **Polar/De Moivre**: Euler's formula, `zⁿ = rⁿe^{inθ}`, powers and roots
  via De Moivre; extracting cos/sin of multiple angles from `(cosθ + isinθ)ⁿ`.
- **Roots**: `zⁿ = w` has exactly n roots (geometric progression of angles),
  the regular n-gon picture, the explicit square-root formula
  ±(√((r+a)/2) + i·sgn(b)√((r−a)/2)) with its b = 0 caveat.
- **Roots of unity**: ω = e^{2πi/3} and the identities 1+ω+ω² = 0,
  ω³ = 1, (1−ω)² = 3ω, 1−ω = √3 e^{−iπ/6}; vanishing sums Σζᵏ = 0;
  roots-of-unity filter Σ_{k≡r} C(N,k) = (1/n)Σ e^{−2πirj/n}(1+e^{2πij/n})^N
  with worked totals (170, 171, 171, 29).
- **Products**: ∏(k=1..n−1)(1−ζₖ) = n and ∏sin(πk/n) = n/2^{n−1}, both derived.
- **Loci**: |z − a| = r (circle), |z − a| ≤ r (disk), argument conditions as
  arcs of circles (the inscribed-angle condition), ellipse
  |z−A| + |z−B| = 2a₀ (with b = √(a₀² − c²)); ranges of |z| over regions
  (min |z−a| = ||a|−r| at z = r·a/|a|, etc.); chords |z−w|² = 2 − 2Re(zw̄).
- **Equations in z and z̄**: the conjugate method (P28: 2x² + 2y² − 6y − 9 = 0)
  and the real/imaginary decomposition method (P29: z = 8/3 − i/3).
- **Optimization**: triangle inequality with equality conditions, the
  P31 range [2, 2√2] verified, extrema over circles/disks.

## In Part II (Olympiad extensions) — 11 sheets

- Rotation engine: `X ↦ A + e^{iθ}(X − A)`; equilateral ⟺ a + ωb + ω²c = 0
  (both orientations); the incenter-120° distance condition; areas
  `½|Im((z₂−z₁)‾(z₃−z₁))|` (P37 = 7/2 checked); circumcenter by 2×2 solve;
  four unit vectors summing to 0 force a rectangle.
- Ptolemy from the identity `(a−c)(b−d) = (a−b)(c−d) + (b−c)(a−d)`;
  British-flag theorem for rectangles; Van Aubel centers
  ((1+i)p + (1−i)q)/2 with the perpendicular-equal-diagonals fact;
  Napoleon's theorem (outer centers equilateral; full ω-proof; numeric
  check with all three mutual distances equal); the general
  "affine combination of side centers" method.
- Leibniz: Σ|z−vᵢ|² = 3|z−g|² + Σ|g−vᵢ|², min at centroid (value 30 verified).
- Unit-circle configurations: `z̄ = 1/z`, the chord identity
  `|z−w|² = (z−w)(z̄−w̄)`, distance products ∏|z−ζₖ| = |zⁿ−1|, the P45 sum.
- Joukowski map `w = z + 1/z`: circles |z| = R > 1 map to ellipses
  (axes R ± 1/R), the unit circle to [−2, 2] traced twice.
- Quadratic Gauss sum `G(n) = Σζ^{k²}`: closed form by n mod 4
  (√n, i√n, (1+i)√n, 0); the full square-and-filter evaluation; small cases
  G(2..8) computed exactly; Legendre-symbol context quoted.
- Gauss–Lucas (critical points inside the convex hull of the roots, via
  Re(e^{iθ}p′/p) > 0 outside), Marden's theorem for cubics with worked
  critical points of z(z−2)(z−1−2i) (both inside the root triangle).
- Pompeiu's theorem (u + ωv + ω²w = 0; degenerate exactly when P lies on
  the circumcircle), with worked distance triples.

## Explicitly out of scope

- The quadratic-equations strand (roots, discriminants, Vieta, common roots,
  range of a quadratic on an interval) is chapter 6, not here. This chapter
  is the complex-numbers strand of the syllabus bullet
  "Complex numbers and quadratic equations".
- Heavy analytic number theory behind the Gauss sum (quadratic reciprocity
  proofs); the reciprocity connection is quoted as context only.
- Solid geometry of complex numbers beyond the stated identities.

## Classification notes

- The rotation/equilateral machinery is Part II because its exam use is the
  technique-heavy end; the *identity* a + ωb + ω²c = 0 appears in
  JEE-Advanced-flavoured problems regularly and is therefore stated with
  full derivation and worked problems, not as an exotic extension.
  Nothing here "can never appear in JEE" — it is simply deeper technique.
- Ptolemy's theorem and the British-flag theorem follow from Part I facts
  (modulus algebra) and are derived completely in Part II.
- The Gauss sum is the only item requiring number theory beyond Part I; its
  evaluation mechanism (square, re-index, filter) uses only Part I tools.
