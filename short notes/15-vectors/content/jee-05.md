---
id: jee-05
part: jee
title: "Projection, Resolution and Dot-Product Applications"
---

## Projection keeps one component; rejection removes it

For $\mathbf{b}\ne\mathbf{0}$, the scalar projection of $\mathbf{a}$ along $\mathbf{b}$ and the vector projection are
$$
\operatorname{scal}_{\mathbf{b}}\mathbf{a}=\frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{b}|},
\qquad
\operatorname{proj}_{\mathbf{b}}\mathbf{a}
=\frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{b}|^2}\mathbf{b}.
$$
The scalar projection is signed. The vector projection points along $\mathbf{b}$ or $-\mathbf{b}$ according to that sign.

The perpendicular remainder, called the **rejection**, is
$$
\mathbf{a}_{\perp}=\mathbf{a}-\operatorname{proj}_{\mathbf{b}}\mathbf{a},
\qquad
\mathbf{a}_{\perp}\cdot\mathbf{b}=0.
$$
Thus projection plus rejection reconstructs $\mathbf{a}$ exactly.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "ratio": 0.55,
  "title": "a = projection + perpendicular rejection",
  "xrange": [-1, 4], "yrange": [-1, 3.5], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [2, 2], "label": "a = (2,2)", "dx": 0.2, "dy": 0.15, "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0], "b": [3, 0], "label": "direction b", "dx": -0.5, "dy": -0.5, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0], "b": [2, 0], "label": "projection", "dx": -0.6, "dy": 0.25, "color": "#B8860B"},
    {"kind": "segment", "a": [2, 0], "b": [2, 2], "label": "rejection", "label_pos": 0.5, "dx": 0.2, "dy": 0, "color": "#B91C1C", "ls": "--"}
  ],
  "caption": "Along the x-direction, a=(2,2) has projection (2,0) and rejection (0,2). The two perpendicular pieces add back to a."
}
:::

:::example title="A 3D projection and rejection"
Let $\mathbf{a}=(2,2,1)$ and $\mathbf{b}=(1,2,2)$. Since $\mathbf{a}\cdot\mathbf{b}=8$ and $|\mathbf{b}|^2=9$,
$$
\operatorname{proj}_{\mathbf{b}}\mathbf{a}=\frac{8}{9}(1,2,2)
=\left(\frac{8}{9},\frac{16}{9},\frac{16}{9}\right).
$$
The scalar projection is $8/3$, and
$$
\mathbf{a}_{\perp}=\left(\frac{10}{9},\frac{2}{9},-\frac{7}{9}\right).
$$
A direct dot product with $(1,2,2)$ gives $10/9+4/9-14/9=0$.
:::

## Unit vectors construct angle bisectors

If $\mathbf{a},\mathbf{b}$ are nonzero, then $\widehat{\mathbf{a}}+\widehat{\mathbf{b}}$ points along an internal angle bisector, provided it is nonzero. Their difference gives an external bisector direction. Normalizing first is essential: unequal lengths would otherwise pull the sum toward the longer vector.

:::example title="An internal and an external bisector"
For $\mathbf{a}=(3,0,0)$ and $\mathbf{b}=(0,4,0)$, the unit vectors are $(1,0,0)$ and $(0,1,0)$. Hence $(1,1,0)$ is an internal bisector direction and $(1,-1,0)$ an external one. Their dot product is zero, as perpendicular internal and external bisectors require.
:::

## Work is a dot product; perpendicular force does none

For a constant force $\mathbf{F}$ acting through displacement $\mathbf{s}$, the work is
$$
W=\mathbf{F}\cdot\mathbf{s}=|\mathbf{F}||\mathbf{s}|\cos\theta.
$$
Only the component of force along displacement contributes. Negative work is meaningful: the force component opposes the displacement.

:::example title="Work with exact components"
For $\mathbf{F}=(3,4,5)$ and $\mathbf{s}=(1,0,2)$,
$$
W=3\cdot1+4\cdot0+5\cdot2=13.
$$
The $y$-component of force contributes nothing because the displacement has no $y$-component.
:::

:::warn title="Projection onto b is not projection onto a"
In general $\operatorname{proj}_{\mathbf{b}}\mathbf{a}\ne\operatorname{proj}_{\mathbf{a}}\mathbf{b}$. Also, scalar projection can be negative, while distance and magnitude cannot. Read the direction of “onto” before substituting.
:::
