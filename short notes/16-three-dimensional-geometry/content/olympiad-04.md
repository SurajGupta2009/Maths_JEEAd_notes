---
id: olympiad-04
part: olympiad
title: "Extension IV — Inspheres and the Monge Point"
---

## Volume and surface area determine the inradius

Join the incentre of a tetrahedron to its four vertices. This decomposes the solid into four pyramids whose heights are the inradius $r$. If $V$ is the volume and $S$ the total surface area,
$$
V=\frac{1}{3}rS,
\qquad r=\frac{3V}{S}.
$$
With one vertex at the origin and the others at $\mathbf{a},\mathbf{b},\mathbf{c}$,
$$
V=\frac{1}{6}|[\mathbf{a}\ \mathbf{b}\ \mathbf{c}]|,
$$
and four cross products give the face areas.

:::example title="An exact inradius and incentre"
For the tetrahedron
$$
O=(0,0,0),\quad A=(4,0,0),\quad B=(0,4,0),\quad C=(0,0,3),
$$
the coordinate-face areas are $8,6,6$, and the slant face has area $2\sqrt{34}$. Thus
$$
S=20+2\sqrt{34},\qquad V=\frac{4\cdot4\cdot3}{6}=8,
$$
so
$$
r=\frac{24}{20+2\sqrt{34}}=\frac{12}{10+\sqrt{34}}\approx0.7580.
$$
The incentre is $I=(r,r,r)$: its distances to the three coordinate planes are $r$. The slant plane is $3x+3y+4z=12$, and
$$
\frac{12-10r}{\sqrt{34}}=r
$$
is exactly the defining equation $12=(10+\sqrt{34})r$.
:::

:::diagram
{
  "type": "vector3d",
  "title": "The insphere is tangent to all four faces",
  "xrange": [-1, 4.8], "yrange": [-1, 4.8], "zrange": [-1, 3.8],
  "elev": 22, "azim": -55, "zoom": 1.12,
  "elements": [
    {"kind": "polygon", "points": [[0, 0, 0], [4, 0, 0], [0, 4, 0]], "fill": "#DCEFED", "alpha": 0.15, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[0, 0, 0], [4, 0, 0], [0, 0, 3]], "fill": "#DCEFED", "alpha": 0.12, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[0, 0, 0], [0, 4, 0], [0, 0, 3]], "fill": "#DCEFED", "alpha": 0.12, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[4, 0, 0], [0, 4, 0], [0, 0, 3]], "fill": "#FFF3B0", "alpha": 0.13, "color": "#B8860B"},
    {"kind": "sphere", "centre": [0.758, 0.758, 0.758], "r": 0.758, "fill": "#F8D7DA", "color": "#B91C1C", "alpha": 0.12, "wire_alpha": 0.38, "longitude_steps": 28, "latitude_steps": 16},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.25, 0, -0.2]},
    {"kind": "point", "at": [4, 0, 0], "label": "A", "offset": [-0.1, 0, 0.35]},
    {"kind": "point", "at": [0, 4, 0], "label": "B", "offset": [-0.35, 0, 0.2]},
    {"kind": "point", "at": [0, 0, 3], "label": "C", "offset": [0.35, 0, 0]},
    {"kind": "point", "at": [0.758, 0.758, 0.758], "label": "I", "offset": [0.3, 0, 0.2], "color": "#B91C1C"}
  ],
  "caption": "The rounded plotted radius is r=0.758; the exact value is 12/(10+sqrt(34)). Its centre I=(r,r,r) is equidistant from all four faces."
}
:::

## Monge's six midplanes concur

For each edge $AB$ of a tetrahedron, form the plane through the midpoint of $AB$ and perpendicular to the opposite edge $CD$. These six **Monge planes** are concurrent.

Place the circumcentre at the origin, so $|\mathbf{a}|=|\mathbf{b}|=|\mathbf{c}|=|\mathbf{d}|=R$, and define
$$
\mathbf{m}=\frac{\mathbf{a}+\mathbf{b}+\mathbf{c}+\mathbf{d}}{2}.
$$
For the midplane associated with $AB$,
$$
\left(\mathbf{m}-\frac{\mathbf{a}+\mathbf{b}}{2}\right)\cdot(\mathbf{d}-\mathbf{c})
=\frac{\mathbf{c}+\mathbf{d}}{2}\cdot(\mathbf{d}-\mathbf{c})
=\frac{|\mathbf{d}|^2-|\mathbf{c}|^2}{2}=0.
$$
Cyclic relabelling proves all six concurrences. In general coordinates,
$$
\mathbf{m}=2\mathbf{g}-\mathbf{o},
$$
where $\mathbf{g}$ is the centroid and $\mathbf{o}$ the circumcentre. Thus the Monge point is the reflection of the circumcentre in the centroid.

:::example title="An exact Monge point for a nonregular tetrahedron"
For
$$
A=(1,0,0),\quad B=(0,2,0),\quad C=(0,0,3),\quad D=(2,1,4),
$$
solving equal distances to the four vertices gives
$$
O=\left(\frac{47}{34},\frac{49}{34},\frac{61}{34}\right).
$$
The centroid is $G=(3/4,3/4,7/4)$, so
$$
M=2G-O=\left(\frac{2}{17},\frac{1}{17},\frac{29}{17}\right).
$$
Substitution into all six midplane equations confirms the concurrence exactly.
:::

:::derive title="One of the six midplane checks"
For edge $AB$, the midpoint is $(1/2,1,0)$ and the opposite direction is $D-C=(2,1,1)$. Hence
$$
M-\left(\frac{1}{2},1,0\right)
=\left(-\frac{13}{34},-\frac{16}{17},\frac{29}{17}\right).
$$
Its dot product with $(2,1,1)$ is $(-26-32+58)/34=0$. The other five checks use the same perpendicularity condition.
:::
