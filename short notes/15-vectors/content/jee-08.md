---
id: jee-08
part: jee
title: "The Scalar Triple Product — Volume and Coplanarity"
---

## A signed volume in one scalar

The **scalar triple product** is
$$
[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]
=\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c}).
$$
First $\mathbf{b}\times\mathbf{c}$ gives the oriented base area; the dot product with $\mathbf{a}$ then multiplies its magnitude by the signed height. Consequently,
$$
V_{\text{parallelepiped}}=|[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]|.
$$
The sign records orientation, not a negative physical volume.

:::diagram
{
  "type": "vector3d",
  "label_fontsize": 10,
  "title": "Volume = base area × perpendicular height",
  "xrange": [-0.5, 4.5], "yrange": [-0.5, 4], "zrange": [-0.5, 3],
  "elev": 22, "azim": -56,
  "elements": [
    {"kind": "parallelepiped", "origin": [0, 0, 0], "u": [2, 0, 0], "v": [1, 2, 0], "w": [1, 1, 2], "fill": "#DCEFED", "alpha": 0.16, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [2, 0, 0], "label": "u", "label_at": [1, 0, 0], "offset": [0, -0.35, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 2, 0], "label": "v", "label_at": [0.5, 1, 0], "offset": [-0.4, 0, 0], "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 1, 2], "label": "w", "label_at": [0.5, 0.5, 1], "offset": [-0.5, 0, 0.2], "color": "#B91C1C"}
  ],
  "caption": "For u=(2,0,0), v=(1,2,0), w=(1,1,2), the triple product is 8. The base area is 4 and the perpendicular height is 2."
}
:::

## Permutations follow determinant rules

Cyclic permutations preserve the scalar triple product, while swapping two factors reverses its sign:
$$
[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]
=[\mathbf{b}\ \mathbf{c}\ \mathbf{a}]
=[\mathbf{c}\ \mathbf{a}\ \mathbf{b}],
$$
$$
[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]
=-[\mathbf{b}\ \mathbf{a}\ \mathbf{c}].
$$
Also $[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]=(\mathbf{a}\times\mathbf{b})\cdot\mathbf{c}$. If any two factors are equal, the triple product is zero.

:::example title="Compute once, then use permutations"
For $\mathbf{a}=(1,2,3)$, $\mathbf{b}=(4,5,6)$ and $\mathbf{c}=(-1,0,2)$,
$$
\mathbf{b}\times\mathbf{c}=(10,-14,5),
\qquad
[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]=10-28+15=-3.
$$
Thus the parallelepiped volume is $3$, while $[\mathbf{b}\ \mathbf{a}\ \mathbf{c}]=+3$ and $[\mathbf{b}\ \mathbf{c}\ \mathbf{a}]=-3$.
:::

## Zero is the coplanarity/dependence test

Three vectors are linearly dependent exactly when their scalar triple product is zero. Geometrically, their spans have no nonzero three-dimensional volume. This includes coplanar position vectors through the origin, parallel factors, and the zero vector.

For four **points** $A,B,C,D$, first form edge vectors from one vertex:
$$
[\mathbf{b}-\mathbf{a}\;\mathbf{c}-\mathbf{a}\;\mathbf{d}-\mathbf{a}]=0
\quad\Longleftrightarrow\quad
A,B,C,D\text{ are coplanar}.
$$
If the first two edges are parallel, the four points can be collinear or otherwise degenerate; zero still correctly signals dependence, but not necessarily a unique plane.

:::example title="A four-point test with exact edges"
Test $A=(1,2,3)$, $B=(4,5,6)$, $C=(-1,0,2)$, $D=(2,-1,4)$. From $A$,
$$
\mathbf{u}=(3,3,3),\quad \mathbf{v}=(-2,-2,-1),\quad \mathbf{w}=(1,-3,1).
$$
Then $\mathbf{v}\times\mathbf{w}=(-5,1,8)$ and
$$
[\mathbf{u}\ \mathbf{v}\ \mathbf{w}]=3(-5)+3(1)+3(8)=12\ne0.
$$
The four points are not coplanar; their edge parallelepiped has volume $12$ and their tetrahedron has volume $2$.
:::

:::warn title="Signed triple product versus volume"
Never report a negative volume. Keep the sign while proving permutation or orientation identities, then take the absolute value only when the question asks for volume. For a tetrahedron, also apply the factor $1/6$.
:::
