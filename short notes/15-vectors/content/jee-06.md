---
id: jee-06
part: jee
title: "The Cross Product — Normal Direction and Area"
---

## A cross product is a vector perpendicular to both inputs

For nonzero, nonparallel $\mathbf{a},\mathbf{b}$, the vector $\mathbf{a}\times\mathbf{b}$ is perpendicular to both, has magnitude
$$
|\mathbf{a}\times\mathbf{b}|=|\mathbf{a}||\mathbf{b}|\sin\theta,
$$
and follows the right-hand rule from $\mathbf{a}$ to $\mathbf{b}$. Its magnitude is the area of the parallelogram they span.

In components,
$$
\mathbf{a}\times\mathbf{b}=
(a_2b_3-a_3b_2,\;a_3b_1-a_1b_3,\;a_1b_2-a_2b_1).
$$
Notice the **minus sign in the middle component's expansion**, while the displayed component formula already includes the correct ordering.

:::diagram
{
  "type": "vector3d",
  "label_fontsize": 10,
  "title": "The cross product is normal to the spanned plane",
  "xrange": [-0.5, 4], "yrange": [-0.5, 3], "zrange": [-0.5, 6.5],
  "elev": 22, "azim": -58,
  "elements": [
    {"kind": "polygon", "points": [[0, 0, 0], [3, 0, 0], [4, 2, 0], [1, 2, 0]], "fill": "#DCEFED", "alpha": 0.35, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [3, 0, 0], "label": "u", "label_at": [1.5, 0, 0], "offset": [0, -0.35, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 2, 0], "label": "v", "label_at": [0.5, 1, 0], "offset": [-0.4, 0, 0], "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [0, 0, 6], "label": "u × v", "label_at": [0, 0, 3.2], "offset": [0.8, 0, 0], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.3, -0.2, 0]}
  ],
  "caption": "u=(3,0,0), v=(1,2,0), and u×v=(0,0,6). The shaded parallelogram has area 6, equal to the normal vector's length."
}
:::

## Order matters; parallelism gives zero

The cross product is anti-commutative and distributive:
$$
\mathbf{a}\times\mathbf{b}=-\mathbf{b}\times\mathbf{a},
\qquad
\mathbf{a}\times(\mathbf{b}+\mathbf{c})=\mathbf{a}\times\mathbf{b}+\mathbf{a}\times\mathbf{c}.
$$
For any vectors, $\mathbf{a}\times\mathbf{a}=\mathbf{0}$. Two nonzero vectors are parallel exactly when their cross product is $\mathbf{0}$. In general it is **not associative**; the vector triple product belongs to the extension lesson.

:::example title="Compute and verify both perpendicularities"
For $\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(4,5,6)$,
$$
\mathbf{a}\times\mathbf{b}=(-3,6,-3),\qquad
\mathbf{b}\times\mathbf{a}=(3,-6,3).
$$
Check:
$$
(-3,6,-3)\cdot(1,2,3)=0,
\qquad
(-3,6,-3)\cdot(4,5,6)=0.
$$
The area is $|(-3,6,-3)|=3\sqrt{6}$, and a unit normal is $(-1,2,-1)/\sqrt{6}$.
:::

## Lagrange's identity joins dot and cross products

For every pair of vectors,
$$
|\mathbf{a}\times\mathbf{b}|^2+(\mathbf{a}\cdot\mathbf{b})^2
=|\mathbf{a}|^2|\mathbf{b}|^2.
$$
This is the algebraic form of $\sin^2\theta+\cos^2\theta=1$. It can compute a cross-product magnitude without finding its components, or check an already computed pair.

:::example title="A complete identity check"
With $\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(4,5,6)$, the previous example gives
$$
|\mathbf{a}\times\mathbf{b}|^2=54,
\qquad (\mathbf{a}\cdot\mathbf{b})^2=32^2=1024.
$$
Therefore $54+1024=1078=14\cdot77$, exactly $|\mathbf{a}|^2|\mathbf{b}|^2$.

For a second pair $\mathbf{u}=(3,-1,2)$ and $\mathbf{v}=(1,4,-2)$,
$$
\mathbf{u}\times\mathbf{v}=(-6,8,13),\qquad \mathbf{u}\cdot\mathbf{v}=-5,
$$
so $269+25=294=14\cdot21$. Thus $\cos\theta=-5/(7\sqrt{6})$ and $\sin^2\theta=269/294$.
:::

:::warn title="Area is nonnegative; orientation is not"
Use $|\mathbf{a}\times\mathbf{b}|$ for area. The vector itself points along one of two opposite normals, determined by factor order. Reversing the order preserves area but reverses oriented area and normal direction.
:::
