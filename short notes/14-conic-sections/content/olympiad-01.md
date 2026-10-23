---
id: olympiad-01
part: olympiad
title: "Extension I — Reflection Properties and Confocal Conics"
---

## The focal properties are geometric angle laws

A parabola sends rays parallel to its axis through the focus. At an ellipse point, the tangent makes equal angles with the two focal segments, so a ray from one focus reflects toward the other. For a hyperbola, a directed ray toward one focus reflects so that its line passes through the other focus; state the directed-ray convention carefully because a hyperbola has two branches.

A convenient unifying statement uses the normal: at a central conic, the normal makes equal angles with the lines joining the point to the two foci. For the parabola, the normal bisects the angle between the focal segment and a line parallel to the axis.

:::derive title="Why the ellipse reflects between its foci"
Along a line $PF_1+PF_2$ changes by the sum of two projected displacements. On a tangent to the level curve $PF_1+PF_2=2a$, the total first-order change is zero. Hence the two unit focal directions have opposite tangential projections, which is exactly the equal-angle law. The same level-set idea gives the directed hyperbola version.
:::

## Confocal means shared foci, not merely shared centre

An ellipse and hyperbola are confocal when their foci coincide. In centred horizontal form,
$$
\frac{x^2}{A}+\frac{y^2}{B}=1,\qquad A>B>0,
$$
has $c^2=A-B$, while
$$
\frac{x^2}{C}-\frac{y^2}{D}=1
$$
has $c^2=C+D$. Confocality therefore requires $A-B=C+D$. Two confocal central conics through a common point have orthogonal tangents there.

:::example title="An exact orthogonal confocal intersection"
The ellipse $x^2/25+y^2/9=1$ and hyperbola $x^2/4-y^2/12=1$ both have foci $(\pm4,0)$ because $25-9=4+12=16$. They meet at
$$
P=\left(\frac{5}{2},\frac{3\sqrt{3}}{2}\right).
$$
The tangent slopes at $P$ are respectively $-\sqrt{3}/5$ and $5/\sqrt{3}$, whose product is $-1$. Thus the two curves and their tangent lines are orthogonal at $P$.
:::

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Confocal ellipse and hyperbola meet orthogonally",
  "xrange": [-6, 6], "yrange": [-5, 5], "grid": true,
  "elements": [
    {"kind": "ellipse", "a": 5, "b": 3, "color": "#0F766E"},
    {"kind": "hyperbola", "a": 2, "b": 3.4641, "umax": 1.0, "color": "#B91C1C"},
    {"kind": "line", "a": [2.5, 2.598], "b": [3.5, 2.2516], "color": "#B8860B"},
    {"kind": "line", "a": [2.5, 2.598], "b": [3.5, 5.4848], "color": "#16295C"},
    {"kind": "point", "at": [2.5, 2.598], "label": "P", "dx": -0.35, "dy": 0.2},
    {"kind": "point", "at": [4, 0], "label": "shared F2", "dx": -0.9, "dy": 0.25, "color": "#B8860B"},
    {"kind": "point", "at": [-4, 0], "label": "shared F1", "dx": -0.9, "dy": 0.25, "color": "#B8860B"},
    {"kind": "text", "at": [-0.5, 4.4], "text": "ellipse tangent", "color": "#B8860B"},
    {"kind": "text", "at": [3.0, -3.5], "text": "hyperbola tangent", "color": "#16295C"}
  ],
  "caption": "The ellipse is x^2/25 + y^2/9 = 1 and the hyperbola is x^2/4 - y^2/12 = 1. Both use c^2 = 16. The tangent slopes are -sqrt(3)/5 and 5/sqrt(3), whose product is -1."
}
:::

:::key title="Two useful problem transformations"
Reflection problems often become straight-line problems after reflecting a focus across a tangent. Confocal problems often become elliptic-coordinate problems after introducing a parameter $\lambda$ and studying $x^2/(a^2+\lambda)+y^2/(b^2+\lambda)=1$. Check the denominator signs to determine whether a member is an ellipse, hyperbola, or degenerate locus.
:::

:::warn title="Do not reverse the reflection direction"
An ellipse ray from one focus reaches the other. A hyperbola statement needs directed lines and branch awareness; saying simply that both foci always receive the same physical ray is imprecise. Draw the incoming and reflected directions before applying an optical argument.
:::
