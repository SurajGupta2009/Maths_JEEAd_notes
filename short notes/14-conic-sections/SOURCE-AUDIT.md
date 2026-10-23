# Source Audit — Chapter 14: Conic Sections

## Sources reviewed

- `notes/Conic-Sections/Conic-Sections.md` — the 2,048-line canonical module; its conic-family, parabola, ellipse, hyperbola, unified-machinery and frontier chapters, formula appendix, and relevant worked examples were reviewed for scope and conventions.
- `notes/Conic-Sections/Conic-Sections — Paper.md` (398 lines) and `Conic-Sections — Solutions.md` (961 lines) — companion question types and corresponding solution conventions were inspected. The short notes do not reproduce mixed-level practice answers uncritically.
- Official JEE Advanced 2026 Mathematics syllabus, Analytical Geometry (two dimensions): <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The standard-form, focus/directrix/eccentricity, parametrization, tangent/normal and locus bullets are mapped in `SCOPE.md`.

## Scope decisions

Part I covers the official parabola, ellipse and hyperbola material and direct derivable applications such as focal chords, director loci, chords of contact, midpoint chords and polarity. Reflection/confocal geometry, rectangular-hyperbola triangle geometry, and the general second-degree classification are clearly separated in Part II. The broader vault topics Poncelet, isogonal conjugates and Carnot are not silently declared part of the official JEE conic syllabus.

## Independent verification

`scripts/math_checks.py` contains **233 exact/rational, numerical and editable-figure checks**. These cover focus–directrix data; standard anatomy; parabola parameters, chords, tangents and normal cubics; ellipse focal distances, auxiliary-circle squashing, director tangents and exact focal chords; hyperbola parameters, asymptotes, conjugate eccentricities and rectangular form; unified chord/midpoint/polar tools; confocal orthogonality; the orthocentre formula; and general-conic invariants and rotation. The visual lab has targeted checks, and an opposite-branch hyperbola example guards against an overgeneralized reciprocal rule. These are targeted numerical checks, not automated proof verification.

## Corrections to the source (do not reproduce)

- **P12, parabola tangent intersection:** for $y^2=4x$, the points $(4,\pm4)$ have parameters $t=\pm2$, so their tangents meet at $T=(-4,0)$. However, the directrix is $x=-1$, not $x=-4$. The tangent slopes are $1/2$ and $-1/2$, whose product is $-1/4$, so the tangents are not perpendicular either. The chord of contact is indeed $x=4$. Chapter 14 instead uses the genuine focal-chord parameters $2$ and $-1/2$ on $y^2=8x$, whose tangents meet at $(-2,3)$ on the correct directrix and are perpendicular.
- **P21, ellipse focal chord:** for $x^2/25+y^2/9=1$ at eccentric angle $60^\circ$, the source's alleged second point near $(8.5,-2.598)$ lies outside the ellipse. The exact second point on the line through $P=(5/2,3\sqrt3/2)$ and $F=(4,0)$ is $Q=(65/14,-9\sqrt3/14)$. The focal segments are $PF=3$ and $QF=9/7$, not $3$ and $4.5$. The correct reciprocal sum is $1/3+7/9=10/9$, giving harmonic mean $9/5=b^2/a$.
- **Blanket hyperbola harmonic-mean transfer:** the source says the unsigned focal-chord harmonic-mean rule survives verbatim for the hyperbola. This needs a same-branch hypothesis. For $x^2/9-y^2/16=1$, the transverse-axis chord through $(5,0)$ has opposite-branch endpoints $(\pm3,0)$ and focal segments $8,2$; their reciprocal sum is $5/8=2c/b^2$, not $3/8=2a/b^2$. The sheets restrict the unsigned same-branch rule and include both the vertical same-branch check and this counterexample.

## Additional convention checks

The parabola normal at $t=0$ is identified as the axis itself, avoiding a false unique-intercept claim. Hyperbola tangent-slope restrictions and director-locus reality cases are stated explicitly. General-conic classification distinguishes real, imaginary and degenerate loci instead of relying on one determinant sign. The rotated example's asymptotes are computed in the rotated coordinates rather than assumed perpendicular.

## IOQM boundary

These notes provide conic-related extensions only. They are not a complete IOQM/RMO syllabus, and no extension is claimed to be impossible in JEE. Proof-level theorems are distinguished from the targeted numerical evidence in the check suite.
