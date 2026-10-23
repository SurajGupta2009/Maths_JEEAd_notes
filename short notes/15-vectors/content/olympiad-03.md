---
id: olympiad-03
part: olympiad
title: "Extension III — Vector Proofs and the Euler Line"
---

## Choose an origin that makes the theorem disappear

Vector proofs become short when the origin matches the symmetry. For a parallelogram, use vertices $0,\mathbf{a},\mathbf{a}+\mathbf{b},\mathbf{b}$. For a triangle's medians, put one vertex at the origin. For a circumcentre problem, put the circumcentre at the origin.

:::example title="Varignon's parallelogram in one subtraction"
Let $A,B,C,D$ be any four points in a plane, and let $P,Q,R,S$ be the midpoints of $AB,BC,CD,DA$. Then
$$
Q-P=\frac{B+C-A-B}{2}=\frac{C-A}{2},
$$
$$
R-S=\frac{C+D-D-A}{2}=\frac{C-A}{2}.
$$
Thus $PQ\parallel SR$ and $PQ=SR$; similarly $QR\parallel PS$. The midpoint quadrilateral is always a parallelogram, even when the original quadrilateral is not one.
:::

## With the circumcentre at O = 0, H = A+B+C

Suppose the circumcentre $O$ of $\triangle ABC$ is the origin, so $|A|=|B|=|C|=R$. Define $H=A+B+C$. Then
$$
(H-A)\cdot(C-B)=(B+C)\cdot(C-B)=|C|^2-|B|^2=0.
$$
Thus $AH\perp BC$; cyclic relabelling gives the other two altitudes. Hence $H$ is the orthocentre.

The centroid is $G=(A+B+C)/3=H/3$. Therefore $O,G,H$ are collinear and
$$
OG:GH=1:2.
$$
With a general circumcentre $O$, translate back to obtain $H=A+B+C-2O$ and $G-O=(H-O)/3$.

:::warn title="Equal distances from a sphere centre are not enough in 3D"
For three points in space, a triangle's circumcentre must lie **in the triangle's plane** as well as be equidistant from its vertices. A sphere centre equidistant from all three need not lie in that plane. Before using $H=A+B+C$ with $O=0$, verify both the equal lengths and that $O$ belongs to the plane of $A,B,C$.
:::

:::diagram
{
  "type": "geometry",
  "label_fontsize": 9,
  "ratio": 0.55,
  "title": "O, G and H lie on one Euler line",
  "xrange": [-6, 6], "yrange": [-5.5, 6], "grid": true,
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 5, "color": "#5B6B84", "ls": "--"},
    {"kind": "polygon", "points": [[5, 0], [0, 5], [-4, -3]], "fill": "#DCEFED", "alpha": 0.22, "color": "#0F766E"},
    {"kind": "line", "a": [-2, -4], "b": [2, 4], "color": "#B8860B"},
    {"kind": "segment", "a": [5, 0], "b": [1, 2], "color": "#B91C1C", "ls": "--"},
    {"kind": "segment", "a": [0, 5], "b": [1, 2], "color": "#B91C1C", "ls": "--"},
    {"kind": "segment", "a": [-4, -3], "b": [1, 2], "color": "#B91C1C", "ls": "--"},
    {"kind": "point", "at": [5, 0], "label": "A(5,0)", "dx": 0.2, "dy": -0.4},
    {"kind": "point", "at": [0, 5], "label": "B(0,5)", "dx": 0.2, "dy": 0.15},
    {"kind": "point", "at": [-4, -3], "label": "C(-4,-3)", "dx": -1.25, "dy": -0.4},
    {"kind": "point", "at": [0, 0], "label": "O", "dx": -0.5, "dy": -0.4},
    {"kind": "point", "at": [0.3333, 0.6667], "label": "G", "dx": -0.55, "dy": 0.15, "color": "#B8860B"},
    {"kind": "point", "at": [1, 2], "label": "H(1,2)", "dx": 0.25, "dy": 0.15, "color": "#B91C1C"}
  ],
  "caption": "All three vertices lie on x^2+y^2=25. H=A+B+C=(1,2), G=H/3, and the dashed segments are altitudes."
}
:::

## Verify the example with lengths and dot products

For $A=(5,0)$, $B=(0,5)$ and $C=(-4,-3)$,
$$
|A|^2=|B|^2=|C|^2=25,
$$
so the origin is genuinely the circumcentre. Set $H=(1,2)$. Then
$$
(H-A)\cdot(C-B)=(-4,2)\cdot(-4,-8)=16-16=0,
$$
$$
(H-B)\cdot(A-C)=(1,-3)\cdot(9,3)=9-9=0.
$$
The third altitude follows by the same calculation. Also $G=(1/3,2/3)=H/3$, so
$$
OG^2=\frac{5}{9},\qquad GH^2=\frac{20}{9}=4OG^2.
$$
This verifies both collinearity and $OG:GH=1:2$ without relying on the drawing.
