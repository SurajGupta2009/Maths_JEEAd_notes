---
id: jee-02
part: jee
title: "Addition, Scalar Multiplication and Linear Combinations"
---

## Addition follows arrows; scalar multiplication scales them

Vectors add componentwise:
$$
\mathbf{a}+\mathbf{b}=(a_1+b_1,a_2+b_2,a_3+b_3).
$$
Geometrically, place the tail of $\mathbf{b}$ at the head of $\mathbf{a}$. The same resultant is the diagonal of the parallelogram spanned by $\mathbf{a}$ and $\mathbf{b}$. Subtraction adds the negative: $\mathbf{a}-\mathbf{b}=\mathbf{a}+(-\mathbf{b})$.

For $\lambda\in\mathbb{R}$, $\lambda\mathbf{a}$ scales length by $|\lambda|$. If $\lambda<0$, it also reverses direction.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "ratio": 0.55,
  "title": "The resultant is the parallelogram diagonal",
  "xrange": [-2, 4.5], "yrange": [-1, 4.5], "grid": true,
  "elements": [
    {"kind": "polygon", "points": [[0, 0], [3, 1], [2, 3], [-1, 2]], "fill": "#DCEFED", "alpha": 0.35, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0], "b": [3, 1], "label": "a", "dx": 0, "dy": -0.45, "color": "#0F766E"},
    {"kind": "arrow", "a": [3, 1], "b": [2, 3], "label": "b", "dx": 0.3, "dy": 0, "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0], "b": [2, 3], "label": "a+b", "dx": -0.9, "dy": 0.1, "color": "#B91C1C"},
    {"kind": "arrow", "a": [0, 0], "b": [-1, 2], "color": "#B8860B", "ls": "--"}
  ],
  "caption": "Tip-to-tail addition and the parallelogram diagonal give the same vector a+b. The shaded region will later be measured by a cross product."
}
:::

## Linear combinations reveal dependence

An expression $\lambda\mathbf{a}+\mu\mathbf{b}+\nu\mathbf{c}$ is a **linear combination**. Three vectors are linearly dependent if one is a combination of the other two; for three vectors in one plane, this is the algebraic meaning of coplanarity through the origin.

Two nonzero vectors are parallel precisely when $\mathbf{b}=\lambda\mathbf{a}$. In component problems, try scalar multiplication before dividing corresponding components: zero components make ratio shortcuts fragile.

:::example title="Compute first, then interpret"
Let $\mathbf{a}=(3,1)$ and $\mathbf{b}=(-1,2)$. Then
$$
\mathbf{a}+\mathbf{b}=(2,3),\qquad
\mathbf{a}-\mathbf{b}=(4,-1),\qquad
2\mathbf{a}-3\mathbf{b}=(9,-4).
$$
The parallelogram law is checked immediately:
$$
|\mathbf{a}+\mathbf{b}|^2+|\mathbf{a}-\mathbf{b}|^2=13+17=30
=2(10+5)=2(|\mathbf{a}|^2+|\mathbf{b}|^2).
$$
:::

## Three structural identities save repeated work

For all vectors and scalars,
$$
|\mathbf{a}+\mathbf{b}|^2=|\mathbf{a}|^2+2\mathbf{a}\cdot\mathbf{b}+|\mathbf{b}|^2,
$$
$$
|\mathbf{a}+\mathbf{b}|^2+|\mathbf{a}-\mathbf{b}|^2=2|\mathbf{a}|^2+2|\mathbf{b}|^2.
$$
The second is the **parallelogram law**: adding the plus/minus expansions cancels the two dot-product terms, so the squares of the diagonals equal the sum of the squares of the four sides. The triangle inequality
$$
\left||\mathbf{a}|-|\mathbf{b}|\right|\leq|\mathbf{a}\pm\mathbf{b}|\leq|\mathbf{a}|+|\mathbf{b}|
$$
records that one side of a triangle cannot exceed the sum of the other two. Equality cases require parallel directions: for the upper bound, $|\mathbf{a}+\mathbf{b}|$ needs the same direction, while $|\mathbf{a}-\mathbf{b}|$ needs opposite directions.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "ratio": 0.55,
  "title": "Scalar multiplication changes length and possibly direction",
  "xrange": [-3, 5], "yrange": [-2, 3], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [2, 1], "label": "a", "dx": -0.2, "dy": 0.35, "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0], "b": [4, 2], "label": "2a", "dx": 0.2, "dy": 0.1, "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0], "b": [-2, -1], "label": "-a", "dx": -0.6, "dy": -0.35, "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0], "label": "O", "dx": -0.35, "dy": 0.15}
  ],
  "caption": "The vector 2a has twice the length in the same direction. The vector -a has the same length in the opposite direction."
}
:::
