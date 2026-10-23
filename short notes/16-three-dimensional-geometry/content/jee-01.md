---
id: jee-01
part: jee
title: "Coordinates and Direction in Space"
---

## Coordinates locate; displacements direct

A point $P=(x,y,z)$ is located by three signed coordinates. The coordinate planes $x=0$, $y=0$ and $z=0$ divide space into eight octants. Reflection in the $xy$-plane changes only the sign of $z$; reflection in the origin reverses all three coordinates.

For $A=(x_1,y_1,z_1)$ and $B=(x_2,y_2,z_2)$, the displacement and distance are
$$
\overrightarrow{AB}=(x_2-x_1,y_2-y_1,z_2-z_1),
$$
$$
AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}.
$$
The displacement supplies direction ratios for the line through $A,B$, provided $A\ne B$.

:::example title="Distance and displacement are different answers"
For $A=(1,2,3)$ and $B=(4,6,9)$,
$$
\overrightarrow{AB}=(3,4,6),\qquad AB=\sqrt{9+16+36}=\sqrt{61}.
$$
The direction ratios are $3:4:6$; the number $\sqrt{61}$ is a length, not a direction.
:::

## Direction cosines are components of a unit direction

A nonzero direction vector $\mathbf{d}=(a,b,c)$ has direction ratios $a:b:c$. Normalize it to obtain the direction cosines
$$
(l,m,n)=\widehat{\mathbf{d}}=\frac{(a,b,c)}{\sqrt{a^2+b^2+c^2}},
\qquad l^2+m^2+n^2=1.
$$
Here $l,m,n$ are the cosines of the angles that the directed line makes with the positive $x,y,z$ axes. Reversing the direction reverses all three cosines.

:::example title="Normalize before calling ratios cosines"
For $\mathbf{d}=(2,-1,2)$, $|\mathbf{d}|=3$, so
$$
(l,m,n)=\left(\frac{2}{3},-\frac{1}{3},\frac{2}{3}\right),
\qquad \frac{4}{9}+\frac{1}{9}+\frac{4}{9}=1.
$$
The original triple $(2,-1,2)$ has squared sum $9$, so it cannot itself be a direction-cosine triple.
:::

:::diagram
{
  "type": "vector3d",
  "title": "Direction cosines come from the normalized displacement",
  "xrange": [-0.5, 3], "yrange": [-2, 1], "zrange": [-0.5, 3],
  "elev": 22, "azim": -55,
  "elements": [
    {"kind": "arrow", "a": [0, 0, 0], "b": [2, -1, 2], "label": "d = (2,-1,2)", "label_at": [1, -0.5, 1], "offset": [0.5, 0, 0.2], "color": "#0F766E"},
    {"kind": "segment", "a": [0, 0, 0], "b": [2, 0, 0], "label": "2", "label_at": [1, 0, 0], "offset": [0, 0.2, 0], "color": "#5B6B84"},
    {"kind": "segment", "a": [2, 0, 0], "b": [2, -1, 0], "label": "-1", "label_at": [2, -0.5, 0], "offset": [0.2, 0, 0], "color": "#B8860B"},
    {"kind": "segment", "a": [2, -1, 0], "b": [2, -1, 2], "label": "2", "label_at": [2, -1, 1], "offset": [0.25, 0, 0], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.25, 0, -0.2]},
    {"kind": "point", "at": [2, -1, 2], "label": "P", "offset": [0.25, 0, 0.15]}
  ],
  "caption": "The component path has signed steps 2,-1,2. Its resultant has length 3 and unit direction (2/3,-1/3,2/3)."
}
:::

## Projection uses a unit direction

The signed projection of $\overrightarrow{AB}$ on a line with nonzero direction $\mathbf{d}$ is
$$
\overrightarrow{AB}\cdot\widehat{\mathbf{d}}
=\frac{\overrightarrow{AB}\cdot\mathbf{d}}{|\mathbf{d}|}.
$$
It is positive when the displacement has a component along the chosen direction and negative when the component opposes it.

:::example title="A segment projected onto another direction"
Using $\overrightarrow{AB}=(3,4,6)$ and $\mathbf{d}=(2,-1,2)$,
$$
\text{projection}=\frac{6-4+12}{3}=\frac{14}{3}.
$$
For direction cosines $(1/2,1/\sqrt{2},1/2)$, the angle with the positive $z$-axis is $\gamma=60^\circ$ because $n=1/2$.
:::

:::warn title="Zero has no direction"
Never normalize $(0,0,0)$. Two coincident points do not determine a line, and a zero direction ratio triple does not define direction cosines or an angle.
:::
