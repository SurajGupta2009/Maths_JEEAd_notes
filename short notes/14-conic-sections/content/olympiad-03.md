---
id: olympiad-03
part: olympiad
title: "Extension III — The General Second-Degree Conic"
---

## Read a general conic through invariants

Write
$$
F(x,y)=ax^2+2hxy+by^2+2gx+2fy+c=0,
$$
and define
$$
I=a+b,\qquad \delta=ab-h^2,\qquad
\Delta=a(bc-f^2)-h(hc-fg)+g(hf-bg).
$$
Here $\Delta$ is the determinant of the symmetric coefficient matrix with rows $(a,h,g)$, $(h,b,f)$ and $(g,f,c)$. The quadratic part controls directions at infinity, while $\Delta$ detects many degeneracies. For nondegenerate real conics: $\delta>0$ is elliptic, $\delta=0$ parabolic, and $\delta<0$ hyperbolic. In the elliptic case, $\Delta\ne0$ and $I\Delta<0$ gives a real ellipse; $I\Delta>0$ gives no real locus.

:::warn title="Use signs and the coefficient convention together"
For example, $x^2+y^2+1=0$ has $\delta>0$ but no real points. When $\Delta=0$, factor or complete squares to distinguish points, line pairs and empty loci. Preserve the coefficients $2h,2g,2f$; nonzero scaling leaves the locus unchanged but scales $\Delta$, so use nonvanishing and consistent sign patterns, never the determinant's numerical size.
:::

:::diagram
{
  "type": "table",
  "title": "General conic decision table for real coefficients",
  "columns": ["Algebraic signal", "Nondegenerate reading", "Degenerate caution"],
  "rows": [
    ["delta > 0, Delta != 0", "elliptic; use I*Delta for reality", "Delta = 0 can collapse to a point"],
    ["delta = 0, Delta != 0", "parabola", "Delta = 0 can give parallel/repeated lines or no real locus"],
    ["delta < 0, Delta != 0", "hyperbola", "Delta = 0 can give two intersecting lines"],
    ["Delta = 0", "do not use the nondegenerate rule", "factor or complete squares to identify the actual locus"]
  ],
  "col_widths": [0.25, 0.35, 0.4],
  "caption": "These are classification guides, not substitutes for checking real points and degeneracy. The notation Delta is the 3 by 3 determinant and delta = ab - h^2."
}
:::

## Rotation removes the cross term

A rotation of axes through an angle $\theta$ satisfying
$$
\tan(2\theta)=\frac{2h}{a-b}
$$
removes the $xy$ term; when $a=b\ne0$, use $\theta=\pi/4$. Translations then complete the squares for central conics. Orthogonal changes preserve lengths and angles, so they are preferable when the geometry itself matters.

:::example title="Classify and rotate in one example"
For
$$
F=x^2+4xy+y^2-1=0,
$$
we have $a=b=1,h=2,c=-1$, so $\delta=1-4=-3$ and $\Delta=3\ne0$. It is a hyperbola. Set $x=(X-Y)/\sqrt{2}$ and $y=(X+Y)/\sqrt{2}$; then
$$
F=3X^2-Y^2-1.
$$
Thus the rotated standard form is $3X^2-Y^2=1$, whose asymptotes are $Y=\pm\sqrt{3}X$ in the rotated coordinates.
:::

## Degeneracy is exact algebra, not a drawing judgement

If the full expression factors into real linear factors, the locus is the union of their lines. For instance,
$$
4x^2-12xy+9y^2=(2x-3y)^2=0
$$
is one repeated line, while $x^2-y^2=(x-y)(x+y)$ is two intersecting lines. Both have $\Delta=0$. Completing squares can also expose a point or an empty real locus.

## Pascal and Brianchon: projective companions

For a nondegenerate conic, **Pascal's theorem** says that for a hexagon inscribed in the conic, the intersections of the three pairs of opposite sides are collinear. **Brianchon's theorem** is dual: for a hexagon whose sides are tangent to a conic, the three principal diagonals are concurrent. Degenerate conic versions give classical line theorems such as Pappus.

:::key title="When these tools help"
Use invariants for classification without heavy rotation, and Pascal/Brianchon for incidence problems with many intersections or tangents. They are projective statements: keep track of the six-point or six-line ordering, and allow parallel-line intersections to be interpreted at infinity when needed.
:::
