---
id: jee-03
part: jee
title: "Line Relationships — Angles, Intersection and Coplanarity"
---

## Directions determine the angle, not the points

For lines with nonzero directions $\mathbf{b}_1,\mathbf{b}_2$, the acute angle $\theta$ between the lines satisfies
$$
\cos\theta=\frac{|\mathbf{b}_1\cdot\mathbf{b}_2|}{|\mathbf{b}_1||\mathbf{b}_2|},
\qquad 0\leq\theta\leq\frac{\pi}{2}.
$$
The absolute value removes the arbitrary choice of arrow orientation. Perpendicular lines have dot product $0$; parallel lines have cross product $\mathbf{0}$.

:::example title="An exact angle between two directions"
For $\mathbf{b}_1=(1,2,2)$ and $\mathbf{b}_2=(2,1,-1)$,
$$
\mathbf{b}_1\cdot\mathbf{b}_2=2,
\qquad |\mathbf{b}_1|=3,\quad |\mathbf{b}_2|=\sqrt{6}.
$$
Therefore
$$
\theta=\cos^{-1}\!\left(\frac{2}{3\sqrt{6}}\right)\approx74.21^\circ.
$$
For directions $(2,3,4)$ and $(4,3,2)$, the dot product is $25\ne0$, so those directions are not perpendicular.
:::

## Coplanarity is a scalar-triple-product test

Let $L_1:\mathbf{r}=\mathbf{a}_1+t\mathbf{b}_1$ and $L_2:\mathbf{r}=\mathbf{a}_2+s\mathbf{b}_2$ be nonparallel. They are coplanar exactly when
$$
(\mathbf{a}_2-\mathbf{a}_1)\cdot(\mathbf{b}_1\times\mathbf{b}_2)=0.
$$
In three dimensions, nonparallel coplanar lines intersect. If the triple product is nonzero, the lines are **skew**: they neither intersect nor lie in one plane. Parallel lines are always coplanar and need a separate coincident-versus-distinct test.

:::example title="A zero or nonzero test with a geometric conclusion"
For $L_1:\mathbf{r}=t(1,0,0)$ and $L_2:\mathbf{r}=(0,1,0)+s(0,0,1)$,
$$
(0,1,0)\cdot\left((1,0,0)\times(0,0,1)\right)=-1\ne0.
$$
Thus the lines are skew. For $L_3:\mathbf{r}=t(1,2,3)$ and $L_4:\mathbf{r}=(1,0,1)+s(0,1,1)$, the same test is zero. Solving gives $t=1$, $s=2$ and the intersection $(1,2,3)$.
:::

:::diagram
{
  "type": "vector3d",
  "title": "Nonparallel coplanar lines meet at one point",
  "xrange": [-1, 3], "yrange": [-1, 4], "zrange": [-1, 5],
  "elev": 23, "azim": -55,
  "elements": [
    {"kind": "segment", "a": [-0.5, -1, -1.5], "b": [1.5, 3, 4.5], "label": "L3", "label_at": [1.2, 2.4, 3.6], "offset": [0.4, 0, 0], "color": "#0F766E"},
    {"kind": "segment", "a": [1, -0.5, 0.5], "b": [1, 2.5, 3.5], "label": "L4", "label_at": [1, 2.2, 3.2], "offset": [-0.45, 0, 0], "color": "#B8860B"},
    {"kind": "point", "at": [1, 2, 3], "label": "(1,2,3)", "offset": [0.55, 0.2, 0.25], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.3, 0, -0.25]}
  ],
  "caption": "L3=t(1,2,3) and L4=(1,0,1)+s(0,1,1) meet when t=1 and s=2. Their directions are not parallel."
}
:::

## Intersection means solving for parameters, not guessing

Equate the three coordinates of $\mathbf{a}_1+t\mathbf{b}_1$ and $\mathbf{a}_2+s\mathbf{b}_2$. Two equations usually determine $t,s$; the third is the essential consistency check. If the system is inconsistent, the lines do not intersect.

:::warn title="Parallel directions do not distinguish coincident from distinct"
For
$$
L_1:\mathbf{r}=t(1,2,3),\qquad L_2:\mathbf{r}=(1,2,3)+s(1,2,3),
$$
the directions are identical, but $(1,2,3)$ also lies on $L_1$ at $t=1$. Therefore the lines **coincide**. Replacing the second base point by $(1,0,0)$ would make them distinct and parallel. Always test the base point.
:::

:::key title="Classify in a fixed order"
First test directions: parallel or not? If parallel, test coincidence. If nonparallel, compute the coplanarity triple product. Zero means an intersection; nonzero means skew lines and leads to the shortest-distance formula.
:::
