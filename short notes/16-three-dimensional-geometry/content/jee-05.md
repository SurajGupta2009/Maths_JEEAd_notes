---
id: jee-05
part: jee
title: "Skew Lines and the Common Perpendicular"
---

## Shortest distance is volume divided by base area

For nonparallel lines
$$
L_1:\mathbf{r}=\mathbf{a}_1+t\mathbf{b}_1,
\qquad
L_2:\mathbf{r}=\mathbf{a}_2+s\mathbf{b}_2,
$$
their common-perpendicular direction is $\mathbf{b}_1\times\mathbf{b}_2$. The shortest distance is
$$
d=\frac{|(\mathbf{a}_2-\mathbf{a}_1)\cdot(\mathbf{b}_1\times\mathbf{b}_2)|}{|\mathbf{b}_1\times\mathbf{b}_2|}.
$$
The numerator is a parallelepiped volume and the denominator is the area of the base spanned by the two directions. Their quotient is the perpendicular height.

If the numerator is zero, the lines are coplanar and intersect because they are nonparallel. A positive value means genuinely skew lines.

:::example title="A complete skew-line distance"
For
$$
L_1:(1,2,3)+t(2,-1,2),
\qquad
L_2:(4,5,6)+s(3,1,-1),
$$
compute
$$
\mathbf{b}_1\times\mathbf{b}_2=(-1,8,5),
\qquad \mathbf{a}_2-\mathbf{a}_1=(3,3,3).
$$
Thus the signed numerator is $-3+24+15=36$ and
$$
d=\frac{36}{\sqrt{90}}=\frac{12}{\sqrt{10}}\approx3.7947.
$$
The nonzero cross product and numerator independently confirm that the lines are skew.
:::

## The common perpendicular can be located exactly

Let $F_1=\mathbf{a}_1+t\mathbf{b}_1$ and $F_2=\mathbf{a}_2+s\mathbf{b}_2$ be its feet. Solve
$$
(F_2-F_1)\cdot\mathbf{b}_1=0,
\qquad
(F_2-F_1)\cdot\mathbf{b}_2=0.
$$
For the same lines, these equations become
$$
9+3s-9t=0,\qquad 9+11s-3t=0,
$$
so $t=4/5$ and $s=-3/5$. Therefore
$$
F_1=\left(\frac{13}{5},\frac{6}{5},\frac{23}{5}\right),
\qquad
F_2=\left(\frac{11}{5},\frac{22}{5},\frac{33}{5}\right).
$$
Indeed $F_2-F_1=(2/5)(-1,8,5)$, whose length is $(2/5)\sqrt{90}=12/\sqrt{10}$.

:::diagram
{
  "type": "vector3d",
  "title": "The common perpendicular is parallel to b1 × b2",
  "xrange": [-2, 8], "yrange": [-2, 8], "zrange": [0, 9],
  "elev": 23, "azim": -57, "zoom": 1.12,
  "elements": [
    {"kind": "segment", "a": [-1, 3, 1], "b": [5, 0, 7], "label": "L1", "label_at": [4, 0.5, 6], "offset": [0.5, 0, 0], "color": "#0F766E"},
    {"kind": "segment", "a": [1, 4, 7], "b": [7, 6, 5], "label": "L2", "label_at": [6, 5.7, 5.3], "offset": [0.4, 0, 0.4], "color": "#B8860B"},
    {"kind": "segment", "a": [2.6, 1.2, 4.6], "b": [2.2, 4.4, 6.6], "color": "#B91C1C", "lw": 3},
    {"kind": "point", "at": [2.6, 1.2, 4.6], "label": "F1", "offset": [0.45, 0, -0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [2.2, 4.4, 6.6], "label": "F2", "offset": [-0.45, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [1, 2, 3], "label": "A1", "offset": [-0.35, 0, -0.25]},
    {"kind": "point", "at": [4, 5, 6], "label": "A2", "offset": [0.4, 0, 0.2]}
  ],
  "caption": "F1=(13/5,6/5,23/5), F2=(11/5,22/5,33/5), and F2-F1=(2/5)(-1,8,5). The red connector is perpendicular to both lines."
}
:::

## Do not divide by a zero cross product

The skew-line formula requires nonparallel directions. For parallel lines, choose a point $A_2$ on the second line and compute its distance to the first:
$$
d=\frac{|(\mathbf{a}_2-\mathbf{a}_1)\times\mathbf{b}_1|}{|\mathbf{b}_1|}.
$$
For example, the $x$-axis and $(0,2,0)+s(1,0,0)$ are distinct parallel lines with distance $2$. Coincident lines have distance $0$.

:::key title="The numerator and denominator answer different questions"
A zero denominator means parallel directions. A zero numerator with nonzero denominator means coplanar intersecting lines. Both nonzero means skew lines with positive shortest distance. Classify before substituting.
:::
