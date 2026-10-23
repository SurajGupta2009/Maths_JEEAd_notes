---
id: jee-08
part: jee
title: "Plane Distances, Feet and Reflections"
---

## Distance is the absolute normalized residual

For $P$ with position vector $\mathbf{p}$ and plane $\mathbf{n}\cdot\mathbf{r}=d$,
$$
\operatorname{dist}(P,\text{plane})=\frac{|\mathbf{p}\cdot\mathbf{n}-d|}{|\mathbf{n}|}.
$$
The numerator measures how far $P$ is from satisfying the equation; division by $|\mathbf{n}|$ converts that algebraic residual to a length.

For parallel planes $\mathbf{n}\cdot\mathbf{r}=d_1$ and $\mathbf{n}\cdot\mathbf{r}=d_2$ with the **same** normal coefficients,
$$
d_{\text{planes}}=\frac{|d_1-d_2|}{|\mathbf{n}|}.
$$
If one equation is scaled differently, normalize or rewrite it first.

:::example title="Point distance and parallel-plane distance"
For $P=(1,1,1)$ and $2x-3y+4z=5$,
$$
\frac{|2-3+4-5|}{\sqrt{29}}=\frac{2}{\sqrt{29}}.
$$
The distance between $2x-3y+4z=5$ and $2x-3y+4z=10$ is
$$
\frac{|10-5|}{\sqrt{29}}=\frac{5}{\sqrt{29}}.
$$
:::

## Foot and image move along the normal

Write the foot as $F=P+t\mathbf{n}$ and impose $\mathbf{n}\cdot F=d$. This yields
$$
F=P-\frac{\mathbf{p}\cdot\mathbf{n}-d}{|\mathbf{n}|^2}\,\mathbf{n},
\qquad I=2F-P.
$$
The image $I$ is the reflection of $P$ in the plane; $F$ is the midpoint of $PI$, and $PI$ is perpendicular to the plane.

:::example title="Reflection in x+y+z=1"
For $P=(1,2,3)$ and $\mathbf{n}=(1,1,1)$,
$$
\frac{\mathbf{p}\cdot\mathbf{n}-d}{|\mathbf{n}|^2}=\frac{6-1}{3}=\frac{5}{3}.
$$
Therefore
$$
F=\left(-\frac{2}{3},\frac{1}{3},\frac{4}{3}\right),
\qquad
I=\left(-\frac{7}{3},-\frac{4}{3},-\frac{1}{3}\right).
$$
The foot satisfies $x+y+z=1$, and $P+I=2F$.
:::

:::diagram
{
  "type": "vector3d",
  "title": "Reflection in a plane is symmetric about the perpendicular foot",
  "xrange": [-3.5, 2.5], "yrange": [-3, 3.5], "zrange": [-2, 4],
  "elev": 23, "azim": -55, "zoom": 1.12,
  "elements": [
    {"kind": "plane", "centre": [0.3333, 0.3333, 0.3333], "u": [1.4, -1.4, 0], "v": [1.1, 0, -1.1], "fill": "#DCEFED", "alpha": 0.20, "color": "#5B6B84", "label": "x+y+z=1", "offset": [-1.2, 1, 0]},
    {"kind": "segment", "a": [1, 2, 3], "b": [-0.6667, 0.3333, 1.3333], "ls": "--", "color": "#B91C1C"},
    {"kind": "segment", "a": [-0.6667, 0.3333, 1.3333], "b": [-2.3333, -1.3333, -0.3333], "ls": "--", "color": "#B8860B"},
    {"kind": "point", "at": [1, 2, 3], "label": "P", "offset": [0.3, 0, 0.2]},
    {"kind": "point", "at": [-0.6667, 0.3333, 1.3333], "label": "F", "offset": [-0.35, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [-2.3333, -1.3333, -0.3333], "label": "I", "offset": [-0.3, 0, -0.2]}
  ],
  "caption": "The plotted points use the exact values P=(1,2,3), F=(-2/3,1/3,4/3), I=(-7/3,-4/3,-1/3), rounded only for rendering."
}
:::

:::example title="A second foot with a distance check"
For the same $P$ and $2x-3y+4z=5$,
$$
\frac{\mathbf{p}\cdot\mathbf{n}-d}{|\mathbf{n}|^2}=\frac{3}{29},
$$
so
$$
F=\left(\frac{23}{29},\frac{67}{29},\frac{75}{29}\right).
$$
Substitution gives $2F_x-3F_y+4F_z=5$, and $PF=3/\sqrt{29}$.
:::

:::key title="The residual controls all three answers"
The same signed quantity $\mathbf{p}\cdot\mathbf{n}-d$ gives the distance after normalization, the foot after multiplication by $\mathbf{n}/|\mathbf{n}|^2$, and the image after doubling the displacement from $P$ to $F$.
:::
