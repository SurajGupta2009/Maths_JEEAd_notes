---
id: olympiad-05
part: olympiad
title: "Extension V — Spherical Geometry & Tetrahedra"
---

## Spherical excess measures area

A spherical triangle is bounded by arcs of three great circles. Its angles are the angles between the corresponding great-circle planes. On a sphere of radius $R$, Girard's theorem gives
$$
E=A+B+C-\pi>0,
\qquad \text{area}=R^2E.
$$
Angles must be in radians in this formula. The fraction of the whole sphere covered is $E/(4\pi)$.

:::example title="Area from three spherical angles"
On a unit sphere, angles $80^\circ,70^\circ,60^\circ$ give
$$
E=(80+70+60-180)^\circ=30^\circ=\frac{\pi}{6}.
$$
Thus the area is $\pi/6\approx0.5236$, and the fraction of the sphere is
$$
\frac{\pi/6}{4\pi}=\frac{1}{24}.
$$
If a sphere of radius $2$ has spherical-triangle area $1$, its excess is $1/4$ radian.
:::

:::diagram
{
  "type": "vector3d",
  "title": "One octant is a spherical triangle with three right angles",
  "xrange": [-1.3, 1.3], "yrange": [-1.3, 1.3], "zrange": [-1.3, 1.3],
  "elev": 22, "azim": -55, "zoom": 1.25,
  "elements": [
    {"kind": "sphere", "centre": [0, 0, 0], "r": 1, "fill": "#DCEFED", "color": "#5B6B84", "alpha": 0.08, "wire_alpha": 0.24, "longitude_steps": 32, "latitude_steps": 18},
    {"kind": "circle3d", "centre": [0, 0, 0], "r": 1, "u": [1, 0, 0], "v": [0, 1, 0], "tstart": 0, "tend": 90, "color": "#B91C1C", "lw": 3},
    {"kind": "circle3d", "centre": [0, 0, 0], "r": 1, "u": [0, 1, 0], "v": [0, 0, 1], "tstart": 0, "tend": 90, "color": "#B8860B", "lw": 3},
    {"kind": "circle3d", "centre": [0, 0, 0], "r": 1, "u": [0, 0, 1], "v": [1, 0, 0], "tstart": 0, "tend": 90, "color": "#0F766E", "lw": 3},
    {"kind": "point", "at": [1, 0, 0], "label": "X", "offset": [0, 0, 0.25]},
    {"kind": "point", "at": [0, 1, 0], "label": "Y", "offset": [-0.2, 0, 0.2]},
    {"kind": "point", "at": [0, 0, 1], "label": "Z", "offset": [0.25, 0, 0]}
  ],
  "caption": "The three arcs lie in perpendicular coordinate planes. E=3(pi/2)-pi=pi/2, so the area is pi/2, exactly one eighth of 4 pi."
}
:::

## A regular tetrahedron from symmetric coordinates

Take
$$
A=(1,1,1),\quad B=(1,-1,-1),\quad C=(-1,1,-1),\quad D=(-1,-1,1).
$$
Every edge has length $2\sqrt{2}$. The centroid and circumcentre are the origin, so $R=\sqrt{3}$. The face $BCD$ lies in $x+y+z=-1$, whose distance from the origin is $1/\sqrt{3}$; hence $r=1/\sqrt{3}$ and $R=3r$.

Scaling to edge length $a$ gives
$$
R=\frac{a\sqrt{6}}{4},\qquad r=\frac{a\sqrt{6}}{12},\qquad V=\frac{a^3}{6\sqrt{2}}.
$$
The internal dihedral angle between any two faces is
$$
\theta=\cos^{-1}\!\left(\frac{1}{3}\right)\approx70.53^\circ.
$$

:::diagram
{
  "type": "vector3d",
  "title": "In a regular tetrahedron, the circumradius is three times the inradius",
  "xrange": [-2, 2], "yrange": [-2, 2], "zrange": [-2, 2],
  "elev": 22, "azim": -55, "zoom": 1.18,
  "elements": [
    {"kind": "polygon", "points": [[1, 1, 1], [1, -1, -1], [-1, 1, -1]], "fill": "#DCEFED", "alpha": 0.16, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[1, 1, 1], [1, -1, -1], [-1, -1, 1]], "fill": "#DCEFED", "alpha": 0.13, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[1, 1, 1], [-1, 1, -1], [-1, -1, 1]], "fill": "#DCEFED", "alpha": 0.13, "color": "#5B6B84"},
    {"kind": "polygon", "points": [[1, -1, -1], [-1, 1, -1], [-1, -1, 1]], "fill": "#FFF3B0", "alpha": 0.16, "color": "#B8860B"},
    {"kind": "segment", "a": [0, 0, 0], "b": [1, 1, 1], "label": "R", "label_at": [0.5, 0.5, 0.5], "offset": [0.25, 0, 0], "color": "#0F766E"},
    {"kind": "segment", "a": [0, 0, 0], "b": [-0.3333, -0.3333, -0.3333], "label": "r", "label_at": [-0.1667, -0.1667, -0.1667], "offset": [0.25, 0, 0], "color": "#B91C1C", "ls": "--"},
    {"kind": "point", "at": [1, 1, 1], "label": "A", "offset": [0.25, 0, 0.3]},
    {"kind": "point", "at": [1, -1, -1], "label": "B", "offset": [0.35, 0, -0.1]},
    {"kind": "point", "at": [-1, 1, -1], "label": "C", "offset": [-0.35, 0, -0.1]},
    {"kind": "point", "at": [-1, -1, 1], "label": "D", "offset": [-0.35, 0, 0.25]},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [0.25, 0, 0.2]}
  ],
  "caption": "For edge 2 sqrt(2), OA=R=sqrt(3). The foot to BCD is its centroid (-1/3,-1/3,-1/3), at distance r=1/sqrt(3)."
}
:::

:::example title="Recover every measurement from the inradius"
If $r=1$, then
$$
a=\frac{12}{\sqrt{6}}=2\sqrt{6},\qquad R=3,
$$
and
$$
V=\frac{(2\sqrt{6})^3}{6\sqrt{2}}=8\sqrt{3}\approx13.8564.
$$
:::

## The solid angle uses dihedral angles, not face angles

At a vertex, a small sphere cuts out a spherical triangle whose **angles** are the tetrahedron's dihedral angles $\theta$, while its **sides** are the face angles $\pi/3$. Girard's theorem therefore gives the solid angle
$$
\Omega=3\theta-\pi
=3\cos^{-1}\!\left(\frac{1}{3}\right)-\pi
\approx0.5513\ \text{sr}.
$$
