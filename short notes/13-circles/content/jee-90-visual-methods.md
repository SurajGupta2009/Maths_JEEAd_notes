---
id: jee-90
part: jee
title: "Visual Circle Lab — Chords, Tangents, Power and Radical Axes"
---

## A perpendicular from the centre bisects a chord

On $x^2+y^2=25$, the vertical line $x=3$ meets the circle at $(3,4)$ and $(3,-4)$. The chord length is $8$. More generally, a chord at distance $d$ from the centre of a radius-$r$ circle has length $2\sqrt{r^2-d^2}$, provided $|d|\leq r$.

:::diagram
{
  "type": "geometry",
  "title": "Chord length follows from a right triangle",
  "xrange": [-6, 6], "yrange": [-6, 6],
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 5, "color": "#5B6B84"},
    {"kind": "line", "a": [3, -5], "b": [3, 5], "label": "x = 3", "label_pos": 0.15, "dx": 0.2, "color": "#B91C1C"},
    {"kind": "segment", "a": [0, 0], "b": [3, 4], "label": "radius 5", "label_pos": 0.35, "dx": 0.15},
    {"kind": "segment", "a": [0, 0], "b": [3, 0], "label": "distance 3", "label_pos": 0.5, "dy": -0.45, "color": "#B8860B"},
    {"kind": "segment", "a": [3, -4], "b": [3, 4], "label": "chord 8", "label_pos": 0.5, "dx": 0.2, "color": "#B91C1C"},
    {"kind": "point", "at": [3, 4], "label": "(3,4)", "dx": 0.15}, {"kind": "point", "at": [3, -4], "label": "(3,-4)", "dx": 0.15, "dy": -0.35}
  ],
  "caption": "The right triangle has hypotenuse 5 and one leg 3, so half the chord is 4. The full chord is 2*4 = 8."
}
:::

The same right triangle classifies a line: $d<r$ gives two intersections, $d=r$ gives tangency, and $d>r$ gives no real intersection. This is often shorter than forming a quadratic discriminant.

<!-- pagebreak -->
## The tangent is perpendicular to the radius

At $P=(3,4)$ on $x^2+y^2=25$, the radius slope is $4/3$, so the tangent slope is $-3/4$. Its equation is
$$
3(x-3)+4(y-4)=0\quad\Longrightarrow\quad3x+4y=25.
$$
The normal at $P$ is the line through $O$ and $P$, namely $4x-3y=0$.

:::diagram
{
  "type": "geometry",
  "title": "Tangent and normal at P(3,4) on x^2 + y^2 = 25",
  "xrange": [-6, 6], "yrange": [-6, 6],
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 5, "color": "#5B6B84"},
    {"kind": "segment", "a": [0, 0], "b": [3, 4], "label": "radius 5", "label_pos": 0.35, "dx": 0.15, "color": "#B91C1C"},
    {"kind": "line", "a": [0, 6.25], "b": [8.3333, 0], "label": "tangent 3x + 4y = 25", "label_pos": 0.52, "dx": 0.2, "color": "#B8860B"},
    {"kind": "line", "a": [0, 0], "b": [3, 4], "label": "normal", "label_pos": -0.65, "dx": 0.15},
    {"kind": "point", "at": [3, 4], "label": "P(3,4)", "dx": 0.15, "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0], "label": "O", "dx": 0.15, "dy": -0.35}
  ],
  "caption": "The tangent direction is (4,-3), whose dot product with the radius direction (3,4) is zero. The tangent touches the circle at exactly one point."
}
:::

For $x^2+y^2+2gx+2fy+c=0$, the tangent at an on-circle point $(x_1,y_1)$ uses the replacement rule $x^2\mapsto xx_1$, $y^2\mapsto yy_1$, $2x\mapsto x+x_1$, and $2y\mapsto y+y_1$. Verify first that the point lies on the circle.

<!-- pagebreak -->
## Power of a point unifies secants and tangents

For external point $P$ and a circle with centre $O$ and radius $r$, the power is $PO^2-r^2$. If a secant through $P$ meets the circle at $A$ and $B$, and a tangent touches at $T$, then $PA\cdot PB=PT^2=PO^2-r^2$ with directed lengths in the general formulation.

:::diagram
{
  "type": "geometry",
  "title": "The same power appears on a secant and a tangent",
  "xrange": [-6, 9], "yrange": [-6, 6],
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 5, "color": "#5B6B84"},
    {"kind": "segment", "a": [-5, 0], "b": [8, 0], "label": "secant through P", "label_pos": 0.35, "dy": 0.35},
    {"kind": "segment", "a": [8, 0], "b": [3.125, 3.905], "label": "tangent PT", "label_pos": 0.55, "dx": 0.2, "color": "#B8860B"},
    {"kind": "point", "at": [8, 0], "label": "P(8,0)", "dx": -0.7, "dy": -0.45, "color": "#B91C1C"},
    {"kind": "point", "at": [5, 0], "label": "A", "dx": 0.15, "dy": 0.2}, {"kind": "point", "at": [-5, 0], "label": "B", "dx": -0.35, "dy": 0.2},
    {"kind": "point", "at": [3.125, 3.905], "label": "T", "dx": 0.15, "color": "#B8860B"}
  ],
  "caption": "PA = 3 and PB = 13 give PA*PB = 39. Also PO^2 - r^2 = 64 - 25 = 39, so PT = sqrt(39)."
}
:::

The power is positive outside, zero on, and negative inside the circle. Tangent length is real only for an external or on-circle point.

<!-- pagebreak -->
## Radical axis: equal power, common chord

For $C_1:x^2+y^2=9$ and $C_2:(x-4)^2+y^2=16$, subtracting the equations gives $x=9/8$. This is the radical axis; when the circles intersect, it is their common chord.

:::diagram
{
  "type": "geometry", "ratio": 0.52,
  "title": "The radical axis x = 9/8 is the common chord",
  "xrange": [-3.5, 8.5], "yrange": [-4.5, 4.5],
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 3, "fill": "#E6F4F3", "alpha": 0.35},
    {"kind": "circle", "centre": [4, 0], "r": 4, "fill": "#FFF3B0", "alpha": 0.25, "color": "#B8860B"},
    {"kind": "line", "a": [1.125, -3], "b": [1.125, 3], "label": "x = 9/8", "label_pos": -0.2, "dx": 0.2, "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0], "label": "C1", "dx": -0.4, "dy": 0.25}, {"kind": "point", "at": [4, 0], "label": "C2", "dx": 0.2, "dy": 0.25, "color": "#B8860B"},
    {"kind": "point", "at": [1.125, 2.781], "label": "intersection", "dx": 0.2}, {"kind": "point", "at": [1.125, -2.781], "label": "intersection", "dx": 0.2, "dy": -0.35}
  ],
  "caption": "Subtracting the equations gives the chord line immediately. Substitution is needed only when the actual intersection coordinates are requested."
}
:::

:::diagram
{
  "type": "table", "ratio": 0.52,
  "title": "Position and number of common points",
  "columns": ["Centre distance condition", "Geometric position", "Common points"],
  "rows": [
    ["d > r + R", "separate externally", "0"],
    ["d = r + R", "touch externally", "1"],
    ["|r-R| < d < r+R", "intersect", "2"],
    ["d = |r-R|, d > 0", "touch internally", "1"],
    ["0 <= d < |r-R|", "one inside the other", "0"]
  ],
  "caption": "Use d = distance between centres and r, R > 0. Identical coincident circles are a separate degenerate case with infinitely many common points."
}
:::

<!-- pagebreak -->
## Circle strategy

:::diagram
{
  "type": "flow",
  "title": "Choose the shortest circle tool that preserves the geometry",
  "steps": [
    {"title": "Start with centre, radius and reality", "detail": "Complete squares if needed and require radius squared > 0 for a real nondegenerate circle."},
    {"title": "Classify before solving intersections", "detail": "Compare centre-line distance with radius, or centre-centre distance with both radii."},
    {"title": "Use the matching theorem", "detail": "Perpendicular bisector for chords, radius perpendicular for tangents, power for secants, subtraction for radical axes."},
    {"title": "Verify the point and the configuration", "detail": "Check on-circle equations, perpendicularity, directed-length conventions and tangency or intersection counts."}
  ],
  "caption": "Many circle questions collapse to one right triangle or one subtraction. Solving a large quadratic first often hides the simple geometric relationship."
}
:::

:::example title="A rapid chord check"
For $x^2+y^2=25$ and $x=3$, the centre-line distance is $3$, so the chord is $2\sqrt{25-9}=8$. Direct substitution gives $y=\pm4$, whose separation is also $8$. The geometric and algebraic methods agree.
:::
