---
id: jee-04
part: jee
title: "Foot, Image and Distance to a Line"
---

## The foot is the perpendicular projection

For $L:\mathbf{r}=\mathbf{a}+t\mathbf{b}$ and a point $P$ with position vector $\mathbf{p}$, let $F=\mathbf{a}+t_0\mathbf{b}$ be the foot of the perpendicular. The condition $(P-F)\cdot\mathbf{b}=0$ gives
$$
t_0=\frac{(\mathbf{p}-\mathbf{a})\cdot\mathbf{b}}{|\mathbf{b}|^2},
\qquad
F=\mathbf{a}+t_0\mathbf{b}.
$$
The image of $P$ in the line is $I=2F-P$, because $F$ is the midpoint of $PI$. The point-line distance is simply $|P-F|$.

:::derive title="The same parameter minimizes distance"
Expanding $|P-(\mathbf{a}+t\mathbf{b})|^2$ gives a quadratic in $t$. Its minimum occurs when the derivative is zero, which is exactly $(P-F)\cdot\mathbf{b}=0$. Thus nearest point, perpendicular foot and orthogonal projection are three descriptions of the same point.
:::

:::example title="Foot, image and distance in one calculation"
Take $P=(1,2,3)$ and $L:\mathbf{r}=t(2,-1,2)$. Since
$$
t_0=\frac{(1,2,3)\cdot(2,-1,2)}{9}=\frac{2}{3},
$$
the foot and image are
$$
F=\left(\frac{4}{3},-\frac{2}{3},\frac{4}{3}\right),
\qquad
I=2F-P=\left(\frac{5}{3},-\frac{10}{3},-\frac{1}{3}\right).
$$
Also $P-F=(-1/3,8/3,5/3)$, whose dot product with $(2,-1,2)$ is zero. Hence
$$
PF=\sqrt{\frac{1+64+25}{9}}=\sqrt{10}.
$$
:::

:::diagram
{
  "type": "vector3d",
  "title": "The foot bisects the point and its reflected image",
  "xrange": [-2.5, 4.5], "yrange": [-4.5, 3.5], "zrange": [-2.5, 4.5],
  "elev": 22, "azim": -55,
  "elements": [
    {"kind": "segment", "a": [-2, 1, -2], "b": [4, -2, 4], "label": "L", "label_at": [3, -1.5, 3], "offset": [0.4, 0, 0], "color": "#5B6B84"},
    {"kind": "segment", "a": [1, 2, 3], "b": [1.3333, -0.6667, 1.3333], "ls": "--", "color": "#B91C1C"},
    {"kind": "segment", "a": [1.3333, -0.6667, 1.3333], "b": [1.6667, -3.3333, -0.3333], "ls": "--", "color": "#B8860B"},
    {"kind": "point", "at": [1, 2, 3], "label": "P", "offset": [0.3, 0, 0.2]},
    {"kind": "point", "at": [1.3333, -0.6667, 1.3333], "label": "F", "offset": [-0.4, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [1.6667, -3.3333, -0.3333], "label": "I", "offset": [0.35, 0, -0.2]},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.3, 0, -0.2]}
  ],
  "caption": "L=t(2,-1,2). PF is perpendicular to L and F is the midpoint of PI. The rounded plotted F is (4/3,-2/3,4/3)."
}
:::

## A cross product computes the distance without finding F

The perpendicular distance from $P$ to $L$ is also
$$
d=\frac{|(\mathbf{p}-\mathbf{a})\times\mathbf{b}|}{|\mathbf{b}|}.
$$
The numerator is the parallelogram area with base $|\mathbf{b}|$; dividing by the base leaves the height. This is useful when only the distance is requested.

:::example title="Check the same distance by area"
For the example above, $\mathbf{p}-\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(2,-1,2)$:
$$
(1,2,3)\times(2,-1,2)=(7,4,-5).
$$
Therefore
$$
d=\frac{\sqrt{49+16+25}}{3}=\frac{\sqrt{90}}{3}=\sqrt{10}.
$$
This agrees with $|P-F|$ and avoids rounding the foot.
:::

:::key title="Compute only what the question needs"
Use $t_0$ when the foot or image is required. Use the cross-product height when only the distance is required. In either method, finish with an independent perpendicularity or length check.
:::
