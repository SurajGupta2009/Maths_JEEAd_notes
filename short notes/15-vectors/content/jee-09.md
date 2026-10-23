---
id: jee-09
part: jee
title: "Tetrahedra and Mixed Vector Strategy"
---

## A tetrahedron is one-sixth of an edge parallelepiped

For vertices $A,B,C,D$, set $\mathbf{u}=\mathbf{b}-\mathbf{a}$, $\mathbf{v}=\mathbf{c}-\mathbf{a}$, $\mathbf{w}=\mathbf{d}-\mathbf{a}$. Then
$$
V_{\text{tetra}}=\frac{1}{6}|[\mathbf{u}\ \mathbf{v}\ \mathbf{w}]|,
\qquad
\mathbf{g}=\frac{\mathbf{a}+\mathbf{b}+\mathbf{c}+\mathbf{d}}{4}.
$$
The factor is $1/6$, not $1/3$: the triangular pyramid on a fixed parallelepiped base has one-third of the corresponding triangular-prism volume, and that prism is half the parallelepiped.

:::diagram
{
  "type": "vector3d",
  "label_fontsize": 10,
  "title": "Use three edges from one tetrahedron vertex",
  "xrange": [-0.5, 1.5], "yrange": [-0.5, 2.5], "zrange": [-0.5, 3.5],
  "elev": 23, "azim": -55,
  "elements": [
    {"kind": "polygon", "points": [[1, 0, 0], [0, 2, 0], [0, 0, 3]], "fill": "#DCEFED", "alpha": 0.22, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[1, 0, 0], [0, 2, 0], [1, 1, 1]], "fill": "#FFF3B0", "alpha": 0.16, "color": "#B8860B"},
    {"kind": "segment", "a": [1, 1, 1], "b": [1, 0, 0], "color": "#B91C1C"},
    {"kind": "segment", "a": [1, 1, 1], "b": [0, 2, 0], "color": "#B91C1C"},
    {"kind": "segment", "a": [1, 1, 1], "b": [0, 0, 3], "color": "#B91C1C"},
    {"kind": "point", "at": [1, 0, 0], "label": "A", "offset": [0.2, -0.2, 0]},
    {"kind": "point", "at": [0, 2, 0], "label": "B", "offset": [0, 0.25, 0]},
    {"kind": "point", "at": [0, 0, 3], "label": "C", "offset": [0, 0, 0.25]},
    {"kind": "point", "at": [1, 1, 1], "label": "D", "offset": [0.25, 0.15, 0.1], "color": "#B91C1C"}
  ],
  "caption": "Taking D as the common tail gives edges A-D, B-D, C-D. Their scalar triple product has absolute value 5, so the tetrahedron volume is 5/6."
}
:::

:::example title="Volume and centroid from four exact vertices"
For $A=(1,0,0)$, $B=(0,2,0)$, $C=(0,0,3)$ and $D=(1,1,1)$, use $D$ as the common tail:
$$
\mathbf{u}=A-D=(0,-1,-1),\quad
\mathbf{v}=B-D=(-1,1,-1),\quad
\mathbf{w}=C-D=(-1,-1,2).
$$
Then $\mathbf{v}\times\mathbf{w}=(1,3,2)$ and $[\mathbf{u}\ \mathbf{v}\ \mathbf{w}]=-5$. Therefore
$$
V=\frac{|-5|}{6}=\frac{5}{6},
\qquad
G=\frac{A+B+C+D}{4}=\left(\frac{1}{2},\frac{3}{4},1\right).
$$
:::

## A parameter problem can be one determinant

Suppose $\mathbf{a}=(1,2,3)$, $\mathbf{b}=(4,5,6)$ and $\mathbf{c}=(-1,0,\lambda)$ are coplanar through the origin. Compute
$$
\mathbf{b}\times\mathbf{c}=(5\lambda,-6-4\lambda,5),
$$
$$
[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]
=5\lambda+2(-6-4\lambda)+15=3(1-\lambda).
$$
Coplanarity forces $\lambda=1$. At $\lambda=2$, the triple product is $-3$, matching the nonzero-volume example in the previous lesson.

## Choose the smallest sufficient computation

:::diagram
{
  "type": "flow",
  "title": "A reliable vector-problem workflow",
  "steps": [
    {"title": "Name the objects", "detail": "Mark position vectors, edge displacements and the common tail. Check for zero vectors before normalizing or taking angles."},
    {"title": "Match the requested geometry", "detail": "Angle or projection: dot. Normal or area: cross. Volume, dependence or coplanarity: scalar triple product."},
    {"title": "Compute in an exact order", "detail": "Keep integer or rational components, preserve cross-product order, and delay square roots until needed."},
    {"title": "Run an independent check", "detail": "Verify perpendicularity, parallel scaling, Lagrange's identity, signed volume, or the original ratio and point membership."}
  ],
  "caption": "The product is chosen by the geometry. A second identity or direct substitution should confirm the result."
}
:::

:::example title="A mixed checklist in action"
If a question asks for a tetrahedron's volume and whether a fourth point lies in a base plane, use the **same three edge vectors** for both. A zero triple product answers coplanarity; otherwise $|[\mathbf{u}\ \mathbf{v}\ \mathbf{w}]|/6$ answers volume. There is no need to compute a plane equation for the vector unit.
:::
