---
id: jee-04
part: jee
title: "The Dot Product — Angles and Perpendicularity"
---

## Two definitions describe the same scalar

For $\mathbf{a}=(a_1,a_2,a_3)$ and $\mathbf{b}=(b_1,b_2,b_3)$,
$$
\mathbf{a}\cdot\mathbf{b}=a_1b_1+a_2b_2+a_3b_3
=|\mathbf{a}||\mathbf{b}|\cos\theta,
$$
where $\theta\in[0,\pi]$ is the angle between two **nonzero** vectors. The dot product is commutative and distributes over addition, but its output is a scalar, not a vector.

:::derive title="The cosine rule connects the two forms"
The third side of the triangle on $\mathbf{a},\mathbf{b}$ is $\mathbf{a}-\mathbf{b}$. Expand its squared length:
$$
|\mathbf{a}-\mathbf{b}|^2
=|\mathbf{a}|^2+|\mathbf{b}|^2-2\mathbf{a}\cdot\mathbf{b}.
$$
The cosine rule gives the same expression with $2|\mathbf{a}||\mathbf{b}|\cos\theta$ as the subtracted term. Compare coefficients to obtain the geometric dot product.
:::

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "ratio": 0.55,
  "title": "The dot product extracts the angle",
  "xrange": [-1, 5], "yrange": [-1, 4], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [3, 1], "label": "a = (3,1)", "dx": 0.2, "dy": -0.45, "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0], "b": [1, 2], "label": "b = (1,2)", "dx": -1.15, "dy": 0.15, "color": "#B8860B"},
    {"kind": "point", "at": [0, 0], "label": "O", "dx": -0.35, "dy": -0.35},
    {"kind": "text", "at": [-0.6, 3.3], "text": "a·b = 5 and |a||b| = 5 sqrt(2)", "color": "#16295C"},
    {"kind": "text", "at": [1.0, 2.9], "text": "theta = 45 degrees", "color": "#B91C1C"}
  ],
  "caption": "cos(theta)=5/(sqrt(10) sqrt(5))=1/sqrt(2), so the smaller angle is 45 degrees."
}
:::

## Read geometry from the sign

For nonzero vectors:
- $\mathbf{a}\cdot\mathbf{b}=0$ means perpendicular directions.
- $\mathbf{a}\cdot\mathbf{b}>0$ means an acute angle.
- $\mathbf{a}\cdot\mathbf{b}<0$ means an obtuse angle.
- $\cos\theta=(\mathbf{a}\cdot\mathbf{b})/(|\mathbf{a}||\mathbf{b}|)$ gives the actual angle.

The zero vector has no angle. A statement such as “$\mathbf{a}\cdot\mathbf{b}=0$, so the angle is $90^\circ$” silently needs $\mathbf{a},\mathbf{b}\ne\mathbf{0}$.

:::example title="An exact perpendicular pair and an exact angle"
For $\mathbf{a}=(1,2,2)$ and $\mathbf{b}=(2,-2,1)$,
$$
\mathbf{a}\cdot\mathbf{b}=2-4+2=0,
\qquad |\mathbf{a}|=|\mathbf{b}|=3,
$$
so the vectors are perpendicular. For $(3,1)$ and $(1,2)$ in the figure, the same calculation gives $\theta=45^\circ$ without a diagram-based estimate.
:::

## Cauchy–Schwarz is a one-line dot-product inequality

For $t\in\mathbb{R}$ and $\mathbf{b}\ne\mathbf{0}$,
$$
0\leq|\mathbf{a}-t\mathbf{b}|^2
=|\mathbf{a}|^2-2t\mathbf{a}\cdot\mathbf{b}+t^2|\mathbf{b}|^2.
$$
Choose $t=(\mathbf{a}\cdot\mathbf{b})/|\mathbf{b}|^2$ to get
$$
(\mathbf{a}\cdot\mathbf{b})^2\leq|\mathbf{a}|^2|\mathbf{b}|^2.
$$
Equality holds exactly when the vectors are linearly dependent. This also explains why the cosine ratio lies between $-1$ and $1$.

:::example title="A numerical angle from components"
For $\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(4,5,6)$,
$$
\mathbf{a}\cdot\mathbf{b}=32,\qquad |\mathbf{a}|^2=14,\qquad |\mathbf{b}|^2=77.
$$
Therefore
$$
\theta=\cos^{-1}\!\left(\frac{32}{\sqrt{1078}}\right)\approx12.93^\circ.
$$
Cauchy–Schwarz is satisfied strictly: $32^2=1024<1078=14\cdot77$, so the vectors are not parallel.
:::
