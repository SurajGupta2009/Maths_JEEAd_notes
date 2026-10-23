---
id: jee-04
part: jee
title: "Ellipse — Focal Geometry and the Eccentric Angle"
---

## A constant sum determines the ellipse

For foci $F_1=(-c,0)$ and $F_2=(c,0)$, require $PF_1+PF_2=2a$ with $a>c$. Setting $b^2=a^2-c^2$ yields
$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,\qquad a>b>0.
$$
The vertices are $(\pm a,0)$, covertices $(0,\pm b)$, foci $(\pm ae,0)$ where $e=c/a$, directrices $x=\pm a/e$, and latus rectum length $2b^2/a$. The circle is the special case $a=b$ and $e=0$.

:::derive title="Focal distances without square roots"
For $P=(x,y)$ on the ellipse, the right focus-directrix pair gives
$$
PF_{\mathrm{right}}=e\left(\frac{a}{e}-x\right)=a-ex,
$$
and the left focal distance is $a+ex$. Their sum is $2a$. These linear formulas are usually faster than recomputing two radicals.
:::

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "On x^2/25 + y^2/9 = 1, the focal distances are 3 and 7",
  "xrange": [-7.5, 7.5], "yrange": [-4.5, 4.5], "grid": true,
  "elements": [
    {"kind": "ellipse", "a": 5, "b": 3, "fill": "#E6F4F3", "alpha": 0.35},
    {"kind": "segment", "a": [-4, 0], "b": [2.5, 2.598], "label": "7", "label_pos": 0.55, "dx": -0.2, "dy": 0.2},
    {"kind": "segment", "a": [4, 0], "b": [2.5, 2.598], "label": "3", "label_pos": 0.45, "dx": 0.25, "color": "#B8860B"},
    {"kind": "point", "at": [-4, 0], "label": "F1(-4,0)", "dx": -1.25, "dy": -0.5},
    {"kind": "point", "at": [4, 0], "label": "F2(4,0)", "dx": 0.2, "dy": -0.5, "color": "#B8860B"},
    {"kind": "point", "at": [2.5, 2.598], "label": "P(60 deg)", "dx": 0.2},
    {"kind": "text", "at": [-1.2, -3.8], "text": "a = 5, b = 3, c = 4, e = 4/5", "color": "#0F766E"}
  ],
  "caption": "P = (5/2, 3 sqrt(3)/2). Since x = 5/2, a - ex = 3 and a + ex = 7. Their sum is 10 = 2a."
}
:::

## The eccentric angle belongs to the auxiliary circle

The auxiliary circle is $x^2+y^2=a^2$. If $Q=(a\cos\theta,a\sin\theta)$ lies on it, squashing vertically by $b/a$ gives the ellipse point
$$
P(\theta)=(a\cos\theta,b\sin\theta).
$$
Thus $\theta$ is the angle of $Q$ on the circle, not generally the polar angle of $P$. This parametrization is the fastest route to tangent and normal formulas.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "The ellipse is the auxiliary circle squashed vertically",
  "xrange": [-5, 5], "yrange": [-4.8, 4.8],
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 4, "color": "#5B6B84", "ls": "--"},
    {"kind": "ellipse", "a": 4, "b": 3, "fill": "#E6F4F3", "alpha": 0.35},
    {"kind": "segment", "a": [2.828, 0], "b": [2.828, 2.828], "color": "#B8860B"},
    {"kind": "point", "at": [2.828, 2.828], "label": "Q on circle", "dx": 0.15},
    {"kind": "point", "at": [2.828, 2.121], "label": "P on ellipse", "dx": 0.15, "dy": -0.5, "color": "#B91C1C"},
    {"kind": "text", "at": [-4.4, -4.25], "text": "theta = 45 deg; y-scale = b/a = 3/4", "color": "#0F766E"}
  ],
  "caption": "Q = (2 sqrt(2), 2 sqrt(2)) maps to P = (2 sqrt(2), 3/sqrt(2)). The x-coordinate is unchanged; the y-coordinate is multiplied by 3/4."
}
:::

:::example title="Reconstruct an ellipse from foci and one point"
An ellipse centred at the origin has foci $(\pm2,0)$ and passes through $(2,3)$. The two distances at this point are $3$ and $5$, so $2a=8$ and $a=4$. Since $c=2$,
$$
b^2=a^2-c^2=16-4=12.
$$
Therefore the ellipse is $x^2/16+y^2/12=1$, with $e=c/a=1/2$. Substitution at $(2,3)$ gives $1/4+3/4=1$.
:::

:::warn title="Major-axis convention matters"
The formulas above use $a>b$ and foci on the $x$-axis. If the larger denominator is under $y^2$, the major axis is vertical: swap the coordinate roles before naming foci and directrices. Do not force every ellipse into horizontal notation.
:::
