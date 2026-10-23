---
id: olympiad-02
part: olympiad
title: "Extension II — Sphere Sections and Tangent Planes"
---

## Compare centre–plane distance with the radius

For a sphere of radius $R$ and a plane at distance $d$ from its centre:
- $d<R$: the section is a circle;
- $d=R$: the plane is tangent at one point;
- $d>R$: there is no real intersection.

For a secant plane, the circle's centre $Q$ is the foot of the perpendicular from the sphere's centre $C$. Pythagoras gives its radius:
$$
r^2=R^2-d^2.
$$
The vector $CQ$ is normal to the plane, while every radius of the section circle lies in the plane.

:::example title="An axis-aligned section makes Pythagoras visible"
The plane $z=3$ meets $x^2+y^2+z^2=25$ in
$$
x^2+y^2=16,\qquad z=3.
$$
Its centre is $(0,0,3)$ and radius is $4$. The sphere radius $5$ is the hypotenuse of a $3$-$4$-$5$ right triangle.
:::

:::diagram
{
  "type": "vector3d",
  "title": "A plane section is a circle whose centre is the perpendicular foot",
  "xrange": [-5.5, 5.5], "yrange": [-5.5, 5.5], "zrange": [-5.5, 5.5],
  "elev": 22, "azim": -55, "zoom": 1.12,
  "elements": [
    {"kind": "sphere", "centre": [0, 0, 0], "r": 5, "fill": "#DCEFED", "color": "#5B6B84", "alpha": 0.08, "wire_alpha": 0.24},
    {"kind": "circle3d", "centre": [0, 0, 3], "r": 4, "normal": [0, 0, 1], "color": "#B91C1C", "lw": 3},
    {"kind": "segment", "a": [0, 0, 0], "b": [0, 0, 3], "label": "3", "label_at": [0, 0, 1.5], "offset": [0.35, 0, 0], "color": "#5B6B84"},
    {"kind": "segment", "a": [0, 0, 3], "b": [4, 0, 3], "label": "4", "label_at": [2, 0, 3], "offset": [0, -0.35, 0], "color": "#B8860B"},
    {"kind": "segment", "a": [0, 0, 0], "b": [4, 0, 3], "label": "5", "label_at": [2, 0, 1.5], "offset": [0.35, 0, 0], "color": "#0F766E"},
    {"kind": "point", "at": [0, 0, 0], "label": "C", "offset": [-0.3, 0, -0.25]},
    {"kind": "point", "at": [0, 0, 3], "label": "Q", "offset": [-0.3, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [4, 0, 3], "label": "T", "offset": [0.3, 0, 0.2]}
  ],
  "caption": "CQ=3 is perpendicular to the section plane, QT=4 lies in it, and CT=5 is a sphere radius. Hence 3^2+4^2=5^2."
}
:::

:::example title="A non-axis-aligned section with exact centre"
For $2x-3y+4z=20$ and $x^2+y^2+z^2=25$,
$$
d=\frac{20}{\sqrt{29}}<5.
$$
The section centre is the foot from the origin:
$$
Q=\frac{20}{29}(2,-3,4)
=\left(\frac{40}{29},-\frac{60}{29},\frac{80}{29}\right).
$$
Its radius is
$$
r=\sqrt{25-\frac{400}{29}}=\sqrt{\frac{325}{29}}\approx3.3477.
$$
:::

## The tangent plane is perpendicular to the radius

At a point $T$ on a sphere with centre $C$, every tangent direction is perpendicular to $CT$. Therefore the tangent plane is
$$
(\mathbf{r}-\mathbf{t})\cdot(\mathbf{t}-\mathbf{c})=0.
$$
For $x^2+y^2+z^2=R^2$, this reduces to $\mathbf{t}\cdot\mathbf{r}=R^2$.

:::example title="Tangency checked by distance"
At $T=(3,0,4)$ on $x^2+y^2+z^2=25$, the tangent plane is
$$
3x+4z=25.
$$
The origin is at distance $25/\sqrt{3^2+4^2}=5$ from this plane, exactly the sphere radius. In contrast, $x+2y+2z=9$ has distance $3<5$, so it cuts the sphere in a circle rather than touching it.
:::

:::key title="Section centre, section radius and tangent plane are linked"
The foot formula supplies the section centre, $r^2=R^2-d^2$ supplies its radius, and $d=R$ is the boundary where the circle shrinks to the tangency point. Always compare $d$ with $R$ before declaring an intersection.
:::
