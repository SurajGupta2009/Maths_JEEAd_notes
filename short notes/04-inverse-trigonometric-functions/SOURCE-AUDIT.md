# Source Audit — Chapter 4: Inverse Trigonometric Functions

## Sources

- **No inverse-trigonometric-functions module exists in this repository.**
  The vault has chapters 2 (exponents-logarithms), 3 (trigonometric
  identities-equations), and `notes/Complex-Numbers/`, but no inverse-trig
  notes were found anywhere under `notes/`.
- Official JEE Advanced 2026 syllabus (jeeadv.ac.in PDF), MATHEMATICS §5
  (Trigonometry): "inverse trigonometric functions (principal value
  branches)" — this sets the scope. Notably the syllabus does **not** list
  properties of triangles or heights-and-distances under Trigonometry.
- Same situation and precedent as Chapter 2: content is freshly authored to
  match the syllabus bullet, with every standard formula re-derived or
  re-checked independently. Nothing was copied from an unreviewed source.

## Independent verification performed

Every numeric and symbolic claim was machine-checked by
`scripts/math_checks.py` (265 assertions, all passing), covering:

- principal values of all standard angles; complementary pairs;
  cofunction identities on their domains;
- the `sin⁻¹(sin x)` / `cos⁻¹(cos x)` / `tan⁻¹(tan x)` piecewise reductions
  at boundary and interior points of each stated interval (including the
  3π/2 face and the kπ construction for `tan⁻¹(tan x)`);
- every face of `2tan⁻¹x` (both the sin⁻¹ and cos⁻¹ faces at |x| = 1, x = 0,
  ±1 boundaries, and the tan⁻¹ faces for x > 1 / x < −1);
- the full `tan⁻¹x + tan⁻¹y` case table (xy < 1, xy > 1 both signs; the
  xy = 1 faces), plus the subtraction formula and the "correction ±π" cases;
- `sin⁻¹x + sin⁻¹y` all three cases (including the π − (·) and −π − (·)
  faces) and the `cos⁻¹x ± cos⁻¹y` sign cases, by direct angle sums;
- the three telescoping series closed forms, by direct numeric summation at
  several n, plus their limits (3π/4, π, π/2, π/4);
- the `x+y+z = xyz ⇒ A+B+C = π` and `xy+yz+zx = 1 ⇒ π/2` identities at many
  parameter triples, and the piecewise `sin⁻¹(sinx)+cos⁻¹(cosx)` function at
  boundary and interior points of every piece;
- solved equations: `tan⁻¹x = cos⁻¹x` (x = √((√5−1)/2)), `tan⁻¹x = cos⁻¹(cos x)`,
  and the parameter equations on both sides of the branch faces.

## Corrections and careful choices made while authoring

- **Branch conditions are attached to every formula that needs them** —
  the bare identity `tan⁻¹x + tan⁻¹y = tan⁻¹((x+y)/(1−xy))` is the classic
  source error reproduced across the internet; the sheets present the case
  table and never the bare form alone. Same for `sin⁻¹x + sin⁻¹y` (three
  cases) and `2tan⁻¹x` (three faces).
- The `sin⁻¹(cos x)` reduction: the usual textbook formula
  `π/2 − x` is only valid on x ∈ [0, π]; the sheets give the correct
  periodic reduction (2kπ-shifted sawtooth), which is what competitive
  problems actually need.
- `cos⁻¹(cos x) = |x|` is wrong outside [0, 2π]; the sheets give the
  triangle-wave statement on [0, 2π] plus the general periodic rule.
- The `xy = 1` faces of `tan⁻¹x + tan⁻¹y` (the sum is ±π/2, not an atan of
  anything) are stated explicitly — most summaries omit them.
- Worked example `tan⁻¹2 + tan⁻¹3 = 3π/4` checks the +π face; `sin⁻¹(4/5) +
  sin⁻¹(12/13) = π − sin⁻¹(56/65)` checks the x²+y² > 1 face (both
  machine-verified).

## Unresolved assumptions

- The definition of `sec⁻¹`/`csc⁻¹` ranges is not uniform across textbooks
  (some use [0,π]\{π/2} for sec⁻¹, others [0,π/2)∪(π,3π/2]). The sheets use
  the greatest-range convention matching NCERT/standard JEE texts and state
  it explicitly; problems never hinge on the difference.
- `tan⁻¹(±∞) = ±π/2` is written as a limit value of the open branch
  (-π/2, π/2); the endpoints are not attained on the open domain. Stated on
  the standard-values sheet.
- No source errors were reproduced (there was no source to reproduce from).
