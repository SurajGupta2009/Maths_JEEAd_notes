---
id: jee-07
part: jee
title: "Angles Between Lines and Planes"
---

## Plane–plane angle uses the normals

For planes with nonzero normals $\mathbf{n}_1,\mathbf{n}_2$, the acute angle $\theta$ between the planes satisfies
$$
\cos\theta=\frac{|\mathbf{n}_1\cdot\mathbf{n}_2|}{|\mathbf{n}_1||\mathbf{n}_2|}.
$$
Parallel normals give parallel or coincident planes. Perpendicular normals give perpendicular planes. An oriented dihedral angle may require a sign convention, but the standard acute angle uses the absolute value.

:::example title="Angle between two planes"
For $x+y+z=0$ and $x-y+z=0$, the normals are $(1,1,1)$ and $(1,-1,1)$. Their dot product is $1$ and both lengths are $\sqrt{3}$, so
$$
\cos\theta=\frac{1}{3},
\qquad \theta=\cos^{-1}\!\left(\frac{1}{3}\right)\approx70.53^\circ.
$$
:::

## Line–plane angle is complementary to line–normal angle

For a line with direction $\mathbf{b}$ and a plane with normal $\mathbf{n}$, the acute angle $\theta$ between the line and plane satisfies
$$
\sin\theta=\frac{|\mathbf{b}\cdot\mathbf{n}|}{|\mathbf{b}||\mathbf{n}|}.
$$
If $\phi$ is the acute angle between $\mathbf{b}$ and $\mathbf{n}$, then $\theta=90^\circ-\phi$. A line parallel to the plane has $\mathbf{b}\cdot\mathbf{n}=0$ and $\theta=0$; a line perpendicular to the plane has $\mathbf{b}\parallel\mathbf{n}$ and $\theta=90^\circ$.

:::example title="Use sine, then verify by complement"
For $\mathbf{b}=(2,3,4)$ and the plane $2x-3y+4z=5$, the normal is $\mathbf{n}=(2,-3,4)$. Both lengths are $\sqrt{29}$, while $\mathbf{b}\cdot\mathbf{n}=11$. Hence
$$
\sin\theta=\frac{11}{29},
\qquad \theta\approx22.29^\circ.
$$
The line–normal angle is $\phi=\cos^{-1}(11/29)\approx67.71^\circ$, and indeed $\theta+\phi=90^\circ$.
:::

:::diagram
{
  "type": "vector3d",
  "title": "Line–plane angle is the complement of line–normal angle",
  "xrange": [-3, 4], "yrange": [-4, 4], "zrange": [-2, 5],
  "elev": 22, "azim": -55,
  "elements": [
    {"kind": "plane", "centre": [0, 0, 0], "u": [1.5, 0, -0.75], "v": [0, 1.5, 1.125], "fill": "#DCEFED", "alpha": 0.22, "color": "#5B6B84", "label": "plane", "label_at": [-1.2, 1.2, 0.8], "offset": [-0.2, 0, 0.2]},
    {"kind": "arrow", "a": [0, 0, 0], "b": [2, 3, 4], "label": "b", "label_at": [1, 1.5, 2], "offset": [0.4, 0, 0.2], "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [2, -3, 4], "label": "n", "label_at": [1, -1.5, 2], "offset": [0.4, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.3, 0, -0.2]}
  ],
  "caption": "b=(2,3,4), n=(2,-3,4), and the plane is 2x-3y+4z=0. The displayed angle formula gives sin(theta)=11/29."
}
:::

## The intersection direction is perpendicular to both normals

For nonparallel planes, their line of intersection has direction $\mathbf{n}_1\times\mathbf{n}_2$. This also explains why a line lying in both planes must have zero dot product with each normal.

:::warn title="Do not use the line–line formula for a line and a plane"
The line–plane formula contains $\sin\theta$ because $\theta$ is measured from the plane, not from its normal. Using $\cos\theta$ there gives the complementary angle.
:::

:::key title="Second read: cosine and tangent of the same angle"
For the worked line–plane example,
$$
\cos\theta=\sqrt{1-\left(\frac{11}{29}\right)^2}=\frac{12\sqrt{5}}{29},
\qquad \tan\theta=\frac{11}{12\sqrt{5}}.
$$
These follow from the same right triangle and provide an independent exact check.
:::
