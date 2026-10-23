---
id: jee-90
part: jee
title: "Visual Coordinate-Geometry Lab — Lines, Distances, Centres and Loci"
---

## Distance from a point to a line is perpendicular distance

For $P=(0,0)$ and $x+y=4$, the perpendicular foot is $Q=(2,2)$. Hence $PQ=\sqrt{2^2+2^2}=2\sqrt{2}$, matching $|0+0-4|/\sqrt{1^2+1^2}=2\sqrt{2}$.

:::diagram
{
  "type": "geometry",
  "title": "The shortest segment from P to the line is perpendicular to it",
  "xrange": [-1, 5], "yrange": [-1, 5], "grid": true,
  "elements": [
    {"kind": "line", "a": [0, 4], "b": [4, 0], "label": "x + y = 4", "label_pos": 0.25, "dx": 0.15},
    {"kind": "segment", "a": [0, 0], "b": [2, 2], "label": "PQ = 2 sqrt(2)", "label_pos": 0.45, "dx": 0.15, "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0], "label": "P(0,0)", "dy": -0.45},
    {"kind": "point", "at": [2, 2], "label": "Q(2,2)", "dx": 0.15, "color": "#B91C1C"}
  ],
  "caption": "The line has slope -1 and PQ has slope 1, so their product is -1. Any other segment from P to the line is longer than the perpendicular segment."
}
:::

The formula $\left| ax_0+by_0+c\right|/\sqrt{a^2+b^2}$ includes an absolute value because distance is nonnegative. The sign before taking the modulus instead tells which side of the line the point lies on.

<!-- pagebreak -->
## A pencil of lines shares one point

The equation $y-1=m(x-1)$ describes a nonvertical line through $(1,1)$ for every slope $m$. Different values of $m$ rotate the line around the same point. The vertical line $x=1$ must be added separately if the full pencil is required.

:::diagram
{
  "type": "geometry",
  "title": "Three members of the pencil through (1,1)",
  "xrange": [-2, 4], "yrange": [-2, 4], "grid": true,
  "elements": [
    {"kind": "line", "a": [1, 1], "b": [2, 1], "label": "m = 0", "label_pos": 2.0, "dy": 0.15},
    {"kind": "line", "a": [1, 1], "b": [2, 2], "label": "m = 1", "label_pos": 1.4, "dx": 0.15, "color": "#B8860B"},
    {"kind": "line", "a": [1, 1], "b": [2, 0], "label": "m = -1", "label_pos": 1.4, "dx": 0.15, "color": "#B91C1C"},
    {"kind": "point", "at": [1, 1], "label": "common point (1,1)", "dx": -1.4, "dy": 0.25}
  ],
  "caption": "A linear combination of two line equations L1 + lambda L2 = 0 passes through every common solution of L1 = 0 and L2 = 0. This is the algebraic form of a pencil."
}
:::

Concurrency questions often become shorter when a pencil is used: impose one additional point or tangency condition to determine the parameter, rather than solving two line equations repeatedly.

<!-- pagebreak -->
## Triangle centres are coordinate averages or intersections

For $A=(0,0),B=(6,0),C=(2,4)$, the centroid is
$$
G=\frac{A+B+C}{3}=\left(\frac{8}{3},\frac{4}{3}\right).
$$
The perpendicular bisector of $AB$ is $x=3$. Intersecting it with the perpendicular bisector of $AC$ gives circumcentre $O=(3,1)$. The altitudes give orthocentre $H=(2,2)$.

:::diagram
{
  "type": "geometry",
  "title": "Circumcentre, centroid and orthocentre lie on the Euler line",
  "xrange": [-0.7, 6.7], "yrange": [-2.5, 4.7],
  "elements": [
    {"kind": "circle", "centre": [3, 1], "r": 3.1623, "color": "#5B6B84", "ls": "--"},
    {"kind": "polygon", "points": [[0, 0], [6, 0], [2, 4]], "fill": "#E6F4F3", "alpha": 0.45},
    {"kind": "segment", "a": [2, 4], "b": [3, 0], "label": "median", "label_pos": 0.6, "dx": 0.15, "color": "#B8860B"},
    {"kind": "line", "a": [3, 1], "b": [2, 2], "label": "Euler line", "label_pos": -2.0, "dx": -0.2, "dy": -0.25, "ha": "right", "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0], "label": "A", "dx": -0.3, "dy": -0.35}, {"kind": "point", "at": [6, 0], "label": "B", "dx": 0.15, "dy": -0.35}, {"kind": "point", "at": [2, 4], "label": "C", "dx": 0.15},
    {"kind": "point", "at": [3, 1], "label": "O(3, 1)", "dx": 0.15, "dy": -0.55, "color": "#16295C"},
    {"kind": "point", "at": [2.6667, 1.3333], "label": "G", "dx": -0.2, "dy": -0.5, "ha": "right", "color": "#B8860B"},
    {"kind": "point", "at": [2, 2], "label": "H(2, 2)", "dx": -0.9, "dy": 0.15, "color": "#B91C1C"}
  ],
  "caption": "The circumcircle confirms O. On the Euler line, GH = 2 OG, with G between O and H. The median from C passes through G."
}
:::

The centroid always uses equal vertex weights. The incentre instead uses side-length weights, $I=(aA+bB+cC)/(a+b+c)$; do not confuse these two weighted averages.

<!-- pagebreak -->
## A locus must include construction and verification

Find the locus of $P=(x,y)$ satisfying $PA=2PB$, where $A=(-1,0)$ and $B=(1,0)$. Squaring the distances gives
$$
(x+1)^2+y^2=4\left((x-1)^2+y^2\right).
$$
After simplification and completion of squares, $(x-5/3)^2+y^2=(4/3)^2$.

:::diagram
{
  "type": "geometry",
  "title": "The distance-ratio condition PA = 2 PB gives a circle",
  "xrange": [-1.7, 3.7], "yrange": [-1.8, 1.8],
  "elements": [
    {"kind": "circle", "centre": [1.6667, 0], "r": 1.3333, "fill": "#E6F4F3", "alpha": 0.45},
    {"kind": "point", "at": [-1, 0], "label": "A(-1,0)", "dx": -0.4, "dy": 0.2},
    {"kind": "point", "at": [1, 0], "label": "B(1,0)", "dx": -0.25, "dy": 0.25},
    {"kind": "point", "at": [1.6667, 0], "label": "centre", "dx": -0.25, "dy": 0.2, "color": "#B8860B"},
    {"kind": "point", "at": [3, 0], "label": "P(3,0)", "dx": -0.6, "dy": 0.2, "color": "#B91C1C"},
    {"kind": "segment", "a": [-1, 0], "b": [3, 0], "label": "PA = 4", "label_pos": 0.55, "dy": -0.5, "color": "#B91C1C"},
    {"kind": "segment", "a": [1, 0], "b": [3, 0], "label": "PB = 2", "label_pos": 0.5, "dy": 0.45, "color": "#B8860B"}
  ],
  "caption": "At P = (3,0), PA = 4 and PB = 2, so the defining ratio holds. The other x-axis intersection, P = (1/3,0), also satisfies it."
}
:::

Squaring was reversible because both sides were nonnegative. In a general locus problem, check whether an operation introduced or removed points, and test simple points on the final curve against the original condition.

<!-- pagebreak -->
## Coordinate-geometry workflow

:::diagram
{
  "type": "flow",
  "title": "Translate geometry into algebra without losing the geometry",
  "steps": [
    {"title": "Choose coordinates and name every object", "detail": "Place convenient points, write line or circle equations, and record any restrictions."},
    {"title": "Translate the geometric condition", "detail": "Use slopes for perpendicularity, distances for loci, determinants for area, and intersections for centres."},
    {"title": "Solve and simplify", "detail": "Keep factors, normalise line equations when distances or angles require it, and complete squares for circles."},
    {"title": "Verify on the diagram and in the condition", "detail": "Check a point, a slope, a distance or a radius. Exclude degenerate or extraneous configurations explicitly."}
  ],
  "caption": "Coordinates are a method for expressing geometry, not a replacement for geometric reasoning. A quick diagram often reveals a wrong sign or an impossible centre immediately."
}
:::

:::key title="Normalise before comparing"
For angle bisectors and distances, scale matters. If $ax+by+c=0$ is multiplied by a nonzero constant, its geometric line is unchanged but an unnormalised signed expression changes. Divide by $\sqrt{a^2+b^2}$ before comparing distances.
:::
