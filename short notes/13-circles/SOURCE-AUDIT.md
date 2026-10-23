# Source Audit — Chapter 13: Circles

## Sources reviewed

- `notes/Coordinate-Geometry-Lines-and-Circles/Coordinate-Geometry-Lines-and-Circles.md` — all 827 lines reviewed, including circle chapters, Olympiad frontier and appendix.
- Companion paper and solutions (249 and 238 lines) read in full; the sheets do not reproduce their mixed-level questions uncritically.
- Official JEE Advanced 2026 Mathematics syllabus, Analytical Geometry (two dimensions), official PDF: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The circle bullets, including parametrization and line intersection, are mapped in `SCOPE.md`.

## Scope decisions

Part I covers the official circle forms, tangent/normal/chord, parametrization and line intersection, with power and radical-axis methods as useful direct applications. Coaxal families, inversion, Simson and Ptolemy are extensions in Part II. This is not a claim that the two JEE chapters constitute a complete IOQM syllabus.

## Independent verification

`scripts/math_checks.py` contains **56 exact/rational and numerical checks** for completion of squares and real-radius cases; diameter/three-point circles; both parametrizations; secant length and tangent equations; power and tangent lengths; chord-of-contact points; radical axes and a radical centre; two-circle intersection; coaxal base points; inversion involution and line-to-circle image; an exact Simson example; Ptolemy for a rectangle; and an impossible source-paper side/diagonal dataset. These targeted checks complement, but do not replace, proofs.

## Corrections to the source (do not reproduce)

- A radical-centre exercise differs between the theory note and companion paper. The theory version first uses concentric circles $x^2+y^2=1$ and $x^2+y^2=4$, whose equal-power equation is the contradiction $-1=-4$ and has no finite radical axis. The sheets use the nonconcentric set from the paper and verify the common-power point $(1/4,3/4)$.
- The companion's cyclic quadrilateral example with successive sides $3,4,5,6$ and a diagonal of $7$ is impossible: the diagonal and adjacent sides $3,4$ violate strict triangle inequality. It is not presented as an existent cyclic quadrilateral; the notes show why Ptolemy's equation alone does not prove existence.
- The source's Pythagoras-from-Ptolemy wording is too broad if it suggests any cyclic quadrilateral with a diameter diagonal reduces directly to Pythagoras. The extension states the valid rectangle case, where both diagonals are equal.
- Source descriptions of the Simson line are retained only with the exact nondegenerate-triangle and extended-side hypotheses; the notes include a directed-angle proof and distinguish finite numerical evidence from a general proof.
- Source coaxal notation is normalized before subtracting circle equations. This avoids treating a linear equation as an ordinary circle and makes the common radical-axis argument explicit.

## IOQM boundary

These notes provide circle-related extensions only. Dedicated number theory and broader Euclidean geometry are not supplied here, so no complete IOQM coverage is claimed.
