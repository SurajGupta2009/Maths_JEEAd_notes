---
id: jee-07
part: jee
title: "Areas and Vector Geometry"
---

## Use two edges from the same vertex

For a parallelogram spanned by $\mathbf{u},\mathbf{v}$ and a triangle with the same two sides,
$$
[\![\text{parallelogram}]\!]=|\mathbf{u}\times\mathbf{v}|,
\qquad
[\![\text{triangle}]\!]=\frac{1}{2}|\mathbf{u}\times\mathbf{v}|.
$$
For $\triangle ABC$, take $\mathbf{u}=\mathbf{b}-\mathbf{a}$ and $\mathbf{v}=\mathbf{c}-\mathbf{a}$. Do not use the three position vectors directly unless $A$ is the origin.

:::diagram
{
  "type": "vector3d",
  "label_fontsize": 10,
  "title": "The diagonal halves the edge parallelogram",
  "xrange": [-1.5, 1.5], "yrange": [-0.5, 2.8], "zrange": [-0.5, 3.5],
  "elev": 24, "azim": -52,
  "elements": [
    {"kind": "polygon", "points": [[1, 0, 0], [0, 2, 0], [-1, 2, 3], [0, 0, 3]], "fill": "#DCEFED", "alpha": 0.25, "color": "#5B6B84"},
    {"kind": "segment", "a": [0, 2, 0], "b": [0, 0, 3], "color": "#B91C1C", "ls": "--"},
    {"kind": "arrow", "a": [1, 0, 0], "b": [0, 2, 0], "label": "u = B-A", "label_at": [0.5, 1, 0], "offset": [0, 0.25, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [1, 0, 0], "b": [0, 0, 3], "label": "v = C-A", "label_at": [0.5, 0, 1.5], "offset": [0.45, 0, 0], "color": "#B8860B"},
    {"kind": "point", "at": [1, 0, 0], "label": "A", "offset": [0.25, -0.2, 0]},
    {"kind": "point", "at": [0, 2, 0], "label": "B", "offset": [0, 0.25, 0]},
    {"kind": "point", "at": [0, 0, 3], "label": "C", "offset": [0, 0, 0.25]}
  ],
  "caption": "u=B-A=(-1,2,0), v=C-A=(-1,0,3), and u×v=(6,3,2). Parallelogram area 7 gives triangle area 7/2."
}
:::

:::example title="An exact 3D triangle area"
For $A=(1,0,0)$, $B=(0,2,0)$ and $C=(0,0,3)$,
$$
\mathbf{u}=(-1,2,0),\qquad \mathbf{v}=(-1,0,3),
$$
$$
\mathbf{u}\times\mathbf{v}=(6,3,2),
\qquad |\mathbf{u}\times\mathbf{v}|=\sqrt{36+9+4}=7.
$$
Hence the triangle area is $7/2$ and the parallelogram area is $7$. The oriented vector area of the ordered triangle is $(6,3,2)/2=(3,3/2,1)$.
:::

## Cross products prove area ratios without coordinates

If two triangles share the same base and their third vertices lie on a line parallel to that base, their areas are equal: the cross-product magnitude retains the same perpendicular height. A median divides a triangle into two equal-area triangles because the two new bases are equal and the height is shared.

For a parallelogram on $\mathbf{a},\mathbf{b}$, its diagonals are $\mathbf{a}+\mathbf{b}$ and $\mathbf{a}-\mathbf{b}$. Their squared lengths sum to $2(|\mathbf{a}|^2+|\mathbf{b}|^2)$, while
$$
(\mathbf{a}+\mathbf{b})\times(\mathbf{a}-\mathbf{b})
=-2(\mathbf{a}\times\mathbf{b}).
$$
This gives the area of the parallelogram formed by the diagonals as twice the original parallelogram area.

## The cosine rule and area formula are companion identities

With $c=|\mathbf{a}-\mathbf{b}|$, expansion gives
$$
c^2=|\mathbf{a}|^2+|\mathbf{b}|^2-2\mathbf{a}\cdot\mathbf{b}
=|\mathbf{a}|^2+|\mathbf{b}|^2-2|\mathbf{a}||\mathbf{b}|\cos\theta.
$$
At the same time, the triangle area is
$$
\frac{1}{2}|\mathbf{a}\times\mathbf{b}|
=\frac{1}{2}|\mathbf{a}||\mathbf{b}|\sin\theta.
$$
Thus one expansion handles obtuse angles automatically, and the other handles area without drawing a perpendicular height.

:::derive title="Angle bisector theorem from section weights"
In $\triangle ABC$, let the internal bisector from $A$ meet $BC$ at $D$. Unit directions along $AB$ and $AC$ add to give the bisector direction. Intersecting that direction with $BC$ yields
$$
D=\frac{|AC|B+|AB|C}{|AB|+|AC|}.
$$
Compare this with the section formula to obtain $BD:DC=AB:AC$. The vector proof keeps the side lengths attached to the correct opposite weights.
:::

:::key title="A fast area self-check"
Before accepting a cross-product answer, verify that it is perpendicular to both edge vectors and that its length matches a rough base-times-height estimate. These two checks catch most component-order and sign errors.
:::
