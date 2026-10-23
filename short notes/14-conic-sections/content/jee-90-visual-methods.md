---
id: jee-90
part: jee
title: "Visual Conic Lab — Focal Chords, Parameters, Asymptotes and Polars"
---

## A focal chord makes its tangents meet on the directrix

For $y^2=8x$, the focal chord parameters are $t=2$ and $t=-1/2$. Its endpoints are $P=(8,8)$ and $Q=(1/2,-2)$, and it passes through $F=(2,0)$. The tangents are $2y=x+8$ and $y=-2x-1$; they meet at $T=(-2,3)$ on the directrix and are perpendicular.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Parameters 2 and -1/2 produce a focal chord and perpendicular tangents",
  "xrange": [-4.2, 10], "yrange": [-5.5, 10],
  "elements": [
    {"kind": "parabola", "a": 2, "trange": [-2.12, 2.12], "color": "#0F766E"},
    {"kind": "segment", "a": [0.5, -2], "b": [8, 8], "label": "focal chord", "label_pos": 0.42, "dx": 0.2, "color": "#16295C"},
    {"kind": "line", "a": [0, 4], "b": [8, 8], "color": "#B8860B"},
    {"kind": "line", "a": [0, -1], "b": [0.5, -2], "color": "#B91C1C"},
    {"kind": "line", "a": [-2, -4], "b": [-2, 8], "label": "x = -2", "label_pos": 0.85, "dx": -0.2, "ha": "right", "color": "#5B6B84"},
    {"kind": "point", "at": [8, 8], "label": "P(8,8)", "dx": -1.2, "dy": 0.3},
    {"kind": "point", "at": [0.5, -2], "label": "Q(1/2,-2)", "dx": 1.0, "dy": -0.6},
    {"kind": "point", "at": [2, 0], "label": "F", "dx": 0.2, "dy": 0.25, "color": "#B8860B"},
    {"kind": "point", "at": [-2, 3], "label": "T(-2,3)", "dx": -1.5, "dy": 0.3, "color": "#B91C1C"},
    {"kind": "text", "at": [3.0, -4.4], "text": "tangent slopes: 1/2 and -2", "color": "#16295C"}
  ],
  "caption": "The tangent slopes are 1/2 and -2. Their product is -1, and the intersection formula gives T = (a*t1*t2,a*(t1+t2)) = (-2,3)."
}
:::

The picture is a checklist: $t_1t_2=-1$ gives the focal chord, perpendicular tangents, and directrix intersection together. Without that product, none of these three conclusions should be assumed.

<!-- pagebreak -->
## The eccentric angle is seen on the auxiliary circle

For $x^2/16+y^2/9=1$ at $\theta=45^\circ$, the circle point is $Q=(2\sqrt{2},2\sqrt{2})$ and the ellipse point is $P=(2\sqrt{2},3/\sqrt{2})$. The circle tangent $x+y=4\sqrt{2}$ and ellipse tangent $3x+4y=12\sqrt{2}$ meet the $x$-axis at the same point $(4\sqrt{2},0)$.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Squashing preserves the common axis intercept of the tangents",
  "xrange": [-4.8, 6.8], "yrange": [-4.5, 6.5],
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 4, "color": "#5B6B84", "ls": "--"},
    {"kind": "ellipse", "a": 4, "b": 3, "fill": "#E6F4F3", "alpha": 0.3},
    {"kind": "segment", "a": [2.828, 2.121], "b": [2.828, 2.828], "color": "#B8860B"},
    {"kind": "line", "a": [0, 5.657], "b": [5.657, 0], "label": "circle tangent", "label_pos": 0.25, "dx": -1.2, "dy": 0.2, "color": "#5B6B84"},
    {"kind": "line", "a": [0, 4.243], "b": [5.657, 0], "label": "ellipse tangent", "label_pos": 0.72, "dx": 0.2, "dy": 0.2, "color": "#B91C1C"},
    {"kind": "point", "at": [2.828, 2.828], "label": "Q", "dx": 0.15},
    {"kind": "point", "at": [2.828, 2.121], "label": "P", "dx": -0.55, "dy": -0.2, "color": "#B91C1C"},
    {"kind": "point", "at": [5.657, 0], "label": "common intercept", "dx": -1.4, "dy": -0.55, "color": "#B8860B"},
    {"kind": "text", "at": [-4.4, -4.1], "text": "scale = 3/4", "color": "#B8860B"}
  ],
  "caption": "The eccentric angle belongs to Q on the circle. P has the same x-coordinate but its y-coordinate is multiplied by b/a = 3/4."
}
:::

When an ellipse problem becomes algebraically heavy, unsquash it to the auxiliary circle, use circle geometry, and then squash back. Keep the distinction between eccentric angle and polar angle explicit.

<!-- pagebreak -->
## A focal chord can be checked exactly, not approximately

On $x^2/25+y^2/9=1$, the line through $P=(5/2,3\sqrt{3}/2)$ and $F=(4,0)$ meets the ellipse again at $Q=(65/14,-9\sqrt{3}/14)$. The focal segments are $PF=3$ and $FQ=9/7$.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "PF = 3 and FQ = 9/7 on one exact focal chord",
  "xrange": [-6, 6], "yrange": [-4, 4], "grid": true,
  "elements": [
    {"kind": "ellipse", "a": 5, "b": 3, "fill": "#E6F4F3", "alpha": 0.3},
    {"kind": "segment", "a": [2.5, 2.598], "b": [4.6429, -1.113], "label": "focal chord", "label_pos": 0.45, "dx": 0.25, "color": "#16295C"},
    {"kind": "point", "at": [2.5, 2.598], "label": "P; PF = 3", "dx": -1.5, "dy": 0.25},
    {"kind": "point", "at": [4.6429, -1.113], "label": "Q; FQ = 9/7", "dx": -1.2, "dy": -0.55, "color": "#B91C1C"},
    {"kind": "point", "at": [4, 0], "label": "F(4,0)", "dx": -1.1, "dy": 0.25, "color": "#B8860B"},
    {"kind": "text", "at": [-5.4, -3.5], "text": "1/3 + 7/9 = 10/9 = 2a/b^2", "color": "#0F766E"}
  ],
  "caption": "The harmonic mean of the two segment lengths is 9/5 = b^2/a. Q has x = 65/14 < 5 and satisfies the ellipse equation exactly."
}
:::

The diagram immediately rejects an impossible alleged endpoint beyond $x=5$. Algebraic exactness and geometric membership should reinforce each other.

<!-- pagebreak -->
## Parallel to an asymptote means one finite intersection

For $x^2/4-y^2/9=1$, the line $y=3x/2+1$ is parallel to the asymptote $y=3x/2$. Substitution becomes linear and gives the single finite intersection $(-10/3,-4)$.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "The quadratic collapses along an asymptote direction",
  "xrange": [-6.5, 6.5], "yrange": [-7, 7], "grid": true,
  "elements": [
    {"kind": "hyperbola", "a": 2, "b": 3, "umax": 1.25, "color": "#0F766E"},
    {"kind": "line", "a": [0, 0], "b": [2, 3], "label": "y = 3x/2", "label_pos": 0.8, "dx": 0.2, "dy": 0.2, "color": "#5B6B84"},
    {"kind": "line", "a": [0, 0], "b": [2, -3], "label": "y = -3x/2", "label_pos": -0.8, "dx": -0.2, "dy": 0.2, "ha": "right", "color": "#5B6B84"},
    {"kind": "line", "a": [0, 1], "b": [2, 4], "label": "y = 3x/2 + 1", "label_pos": -1.15, "dx": 0.2, "dy": 0.45, "color": "#B91C1C"},
    {"kind": "point", "at": [-3.3333, -4], "label": "(-10/3,-4)", "dx": 0.2, "dy": -0.45, "color": "#B91C1C"}
  ],
  "caption": "The curve never meets the asymptote itself. A distinct parallel line has one finite intersection; the second intersection is at infinity."
}
:::

This is why discriminant formulas must be applied after checking the degree of the substituted equation. If the quadratic coefficient vanishes, the equation is linear and the usual two-root language no longer applies.

<!-- pagebreak -->
## Pole and polar preserve incidence

For the ellipse $x^2/16+y^2/9=1$, the polar of $P=(4,3)$ is $x/4+y/3=1$. It meets the ellipse at $Q=(4,0)$ and $R=(0,3)$. The tangents at those contacts are $x=4$ and $y=3$, and both pass through $P$.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "The chord of contact joins Q(4,0) and R(0,3)",
  "xrange": [-5, 6], "yrange": [-4.5, 5],
  "elements": [
    {"kind": "ellipse", "a": 4, "b": 3, "fill": "#E6F4F3", "alpha": 0.3},
    {"kind": "line", "a": [4, -4], "b": [4, 4], "label": "tangent x = 4", "label_pos": 0.1, "dx": 0.15, "color": "#B8860B"},
    {"kind": "line", "a": [-4, 3], "b": [5, 3], "color": "#B8860B"},
    {"kind": "line", "a": [4, 0], "b": [0, 3], "color": "#B91C1C"},
    {"kind": "point", "at": [4, 3], "label": "P(4,3)", "dx": 0.2, "color": "#B91C1C"},
    {"kind": "point", "at": [4, 0], "label": "Q", "dx": -0.6, "dy": -0.55},
    {"kind": "point", "at": [0, 3], "label": "R", "dx": -0.8, "dy": -0.6},
    {"kind": "text", "at": [-4.5, 4.1], "text": "y = 3", "color": "#B8860B"},
    {"kind": "text", "at": [-4.5, -4.0], "text": "polar: 3x + 4y = 12", "color": "#B91C1C"}
  ],
  "caption": "Q and R lie on the polar of P. La Hire's theorem says that P must lie on the polar of Q and on the polar of R; those polars are the two displayed tangents."
}
:::

Polarity is not a new computational trick so much as a way to read tangency and incidence backwards. Use it when a problem asks for a pole, a chord of contact, or a concurrent family of polars.

<!-- pagebreak -->
## Visual conic strategy

:::diagram
{
  "type": "flow",
  "title": "Let the geometry choose the shortest reliable computation",
  "steps": [
    {"title": "Draw the named objects", "detail": "Mark foci, directrices, vertices, contact points and asymptotes with their coordinate restrictions."},
    {"title": "Choose the natural parameter", "detail": "Parabola t, ellipse eccentric angle, hyperbola sec/tan, or rectangular-hyperbola ct,c/t."},
    {"title": "Translate one geometric condition", "detail": "Focal chord, tangent, normal, midpoint, perpendicularity, or pole-polar incidence."},
    {"title": "Inspect and verify", "detail": "Check branch, membership, allowed slope, real intersections, and the original distance or incidence condition."}
  ],
  "caption": "A sketch is not a substitute for algebra, but it is an excellent error detector. Use both: geometry to choose and check, algebra to compute exactly."
}
:::

:::key title="The final ten-second check"
Ask: Is the point on the curve? Is the focus on the correct side? Does the directrix have the right coordinate? Are tangent slopes allowed? Does a focal chord pass through the focus? These questions catch most conic mistakes before an answer is written.
:::
