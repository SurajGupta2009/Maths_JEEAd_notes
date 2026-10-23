---
id: olympiad-01
part: olympiad
title: "Extension I — Sphere Foundations"
---

## A sphere is a fixed-distance locus

With centre $C=(h,k,l)$ and radius $R>0$,
$$
(x-h)^2+(y-k)^2+(z-l)^2=R^2.
$$
Expanding and renaming coefficients gives
$$
x^2+y^2+z^2+2ux+2vy+2wz+d=0,
$$
with
$$
C=(-u,-v,-w),\qquad R^2=u^2+v^2+w^2-d.
$$
The sign of $R^2$ classifies the locus: positive gives a real sphere, zero a single point, and negative no real points.

:::example title="Complete squares instead of guessing signs"
For
$$
x^2+y^2+z^2+2x-4y+6z-11=0,
$$
move the constant and complete three squares:
$$
(x+1)^2+(y-2)^2+(z-3)^2=25.
$$
Thus the centre is $(-1,2,-3)$ and the radius is $5$. Equivalently, $(u,v,w)=(1,-2,3)$ and $R^2=1+4+9-(-11)=25$.
:::

## The diameter form is a perpendicularity condition

If $AB$ is a diameter, every other point $P$ of the sphere satisfies $\angle APB=90^\circ$. Hence
$$
(P-A)\cdot(P-B)=0.
$$
The centre is the midpoint of $AB$ and the radius is $AB/2$.

:::example title="A sphere from two diameter endpoints"
For $A=(1,0,0)$ and $B=(0,2,0)$,
$$
C=\left(\frac{1}{2},1,0\right),
\qquad R=\frac{\sqrt{5}}{2}.
$$
The equation is
$$
\left(x-\frac{1}{2}\right)^2+(y-1)^2+z^2=\frac{5}{4},
$$
or $x^2+y^2+z^2-x-2y=0$. The origin, $A$ and $B$ all satisfy it.
:::

:::diagram
{
  "type": "vector3d",
  "title": "The midpoint of a diameter is the sphere's centre",
  "xrange": [-1.5, 2], "yrange": [-1, 2.8], "zrange": [-1.8, 1.8],
  "elev": 22, "azim": -55,
  "elements": [
    {"kind": "sphere", "centre": [0.5, 1, 0], "r": 1.118034, "fill": "#DCEFED", "color": "#5B6B84", "alpha": 0.10, "wire_alpha": 0.28},
    {"kind": "segment", "a": [1, 0, 0], "b": [0, 2, 0], "color": "#B91C1C", "lw": 2.8},
    {"kind": "point", "at": [1, 0, 0], "label": "A", "offset": [0.25, -0.15, 0]},
    {"kind": "point", "at": [0, 2, 0], "label": "B", "offset": [-0.2, 0.2, 0]},
    {"kind": "point", "at": [0.5, 1, 0], "label": "C", "offset": [0.25, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 0, 0], "label": "O", "offset": [-0.25, 0, -0.2]}
  ],
  "caption": "C=(1/2,1,0), AB=sqrt(5), and R=sqrt(5)/2. The origin also lies on the sphere because OA is perpendicular to OB."
}
:::

## Four noncoplanar points determine a unique sphere

Substitute the four points into the general equation. Subtracting one equation from the other three eliminates $d$ and leaves three linear equations for the centre coordinates. Noncoplanarity guarantees uniqueness.

:::example title="A four-point sphere with exact centre and radius"
For
$$
A=(1,0,0),\quad B=(0,2,0),\quad C=(0,0,3),\quad D=(1,1,1),
$$
equal squared distances from $O=(x,y,z)$ give
$$
-2x+4y=3,\qquad -2x+6z=8,\qquad y+z=1.
$$
Solving,
$$
O=\left(-\frac{13}{10},\frac{1}{10},\frac{9}{10}\right).
$$
Then
$$
R^2=OA^2=\left(\frac{23}{10}\right)^2+\left(-\frac{1}{10}\right)^2+\left(-\frac{9}{10}\right)^2
=\frac{611}{100}.
$$
Thus $R=\sqrt{611}/10\approx2.4718$. The other three distance checks agree.
:::

:::warn title="Centre signs and the constant term are independent"
In the general equation, the centre is $(-u,-v,-w)$, while $d=u^2+v^2+w^2-R^2$. Do not read the centre directly from the linear coefficients without the minus signs, and do not use $R^2$ itself as the constant $d$.
:::

:::key title="Second read: four equal squared distances"
For the four-point example,
$$
|OA|^2=|OB|^2=|OC|^2=|OD|^2=\frac{611}{100}.
$$
After clearing denominators, the four squared-distance numerators are $529+1+81$, $169+361+81$, $169+1+441$ and $529+81+1$, all equal to $611$. Thus the centre and radius are checked without solving the system again.
:::
