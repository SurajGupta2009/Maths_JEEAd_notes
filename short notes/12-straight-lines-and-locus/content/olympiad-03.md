---
id: olympiad-03
part: olympiad
title: "Loci Beyond the First Examples"
---

## Two distance constraints: translate before expanding

A condition involving distances to fixed points is often quadratic after squaring. Translate the midpoint of the fixed segment to the origin and rotate the axes to put the segment on the $x$-axis; translation and rotation preserve distances, so the algebra becomes one-dimensional in the fixed-point coordinates.

:::example title="A ratio locus becomes a circle"
With foci $A=(-c,0)$ and $B=(c,0)$, $PA/PB=k\ne1$ yields
$$(x+c)^2+y^2=k^2((x-c)^2+y^2).$$
Completing squares gives a circle on the $x$-axis. If $k=1$, the quadratic terms cancel and the locus is $x=0$, the perpendicular bisector. This is the Apollonius circle / bisector dichotomy.
:::

## A linear condition plus a distance condition

The intersection of a line and a circle has zero, one (tangent), or two points. Substituting the line parametrization into the circle gives a quadratic; its discriminant records these cases. The shortest-distance-to-line bound can often decide existence before solving.

:::warn title="Locus proofs need both directions"
An equation obtained by squaring is only a candidate locus until every point on it is checked in the original unsquared relation. Keep sign restrictions and any excluded denominator values.
:::

:::assume title="Extension boundary"
The coordinate methods here are extensions and problem-solving tools. The official JEE Advanced line syllabus lists the specific line forms, intersection-pencil, bisector, concurrency, and four triangle centres; it does not name every possible distance locus or every olympiad theorem.
:::
