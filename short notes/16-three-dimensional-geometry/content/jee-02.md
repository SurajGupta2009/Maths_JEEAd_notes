---
id: jee-02
part: jee
title: "Lines in Space — Vector and Cartesian Forms"
---

## One point and one nonzero direction determine a line

Through $A$ with position vector $\mathbf{a}$ and direction $\mathbf{b}\ne\mathbf{0}$, every point of the line is
$$
\mathbf{r}=\mathbf{a}+t\mathbf{b},\qquad t\in\mathbb{R}.
$$
If $\mathbf{a}=(x_1,y_1,z_1)$ and $\mathbf{b}=(a,b,c)$, the parametric equations are
$$
x=x_1+at,\qquad y=y_1+bt,\qquad z=z_1+ct.
$$
When $a,b,c$ are all nonzero, eliminate $t$ to obtain symmetric form:
$$
\frac{x-x_1}{a}=\frac{y-y_1}{b}=\frac{z-z_1}{c}.
$$
For a second point $B$, use $\mathbf{b}=\overrightarrow{AB}$; this gives the two-point form.

:::example title="Two points become one vector equation"
For $A=(1,2,3)$ and $B=(4,6,9)$, $\overrightarrow{AB}=(3,4,6)$. Hence
$$
\mathbf{r}=(1,2,3)+t(3,4,6),
$$
or
$$
\frac{x-1}{3}=\frac{y-2}{4}=\frac{z-3}{6}.
$$
At $t=1$ the point is $B$; at $t=1/2$ it is the midpoint $(5/2,4,6)$.
:::

:::warn title="A zero denominator needs a coordinate equation"
Through $(1,2,3)$ parallel to the $z$-axis, write
$$
x=1,\qquad y=2,\qquad z=3+t.
$$
Do not place zero under $x-1$ or $y-2$ in the symmetric formula. The vector and parametric forms remain valid without special cases.
:::

:::diagram
{
  "type": "vector3d",
  "title": "A line is one point plus all scalar multiples of a direction",
  "xrange": [0, 5], "yrange": [0, 7], "zrange": [0, 10],
  "elev": 22, "azim": -58,
  "elements": [
    {"kind": "segment", "a": [0.4, 1.2, 1.8], "b": [4.6, 6.8, 9.6], "color": "#5B6B84", "lw": 2},
    {"kind": "arrow", "a": [1, 2, 3], "b": [4, 6, 9], "label": "b = AB", "label_at": [2.5, 4, 6], "offset": [0.2, 0.8, 0.8], "color": "#0F766E"},
    {"kind": "point", "at": [1, 2, 3], "label": "A(1,2,3)", "offset": [-0.5, 0, -0.4]},
    {"kind": "point", "at": [4, 6, 9], "label": "B(4,6,9)", "offset": [0.5, 0, 0.5]},
    {"kind": "point", "at": [2.5, 4, 6], "label": "t = 1/2", "offset": [-1.0, 0, -0.4], "color": "#B91C1C"}
  ],
  "caption": "The segment AB supplies the direction, but the line continues beyond both endpoints. Parameter values locate every point on it."
}
:::

## Two independent planes also describe a line

The intersection of nonparallel planes
$$
P_1=n_{11}x+n_{12}y+n_{13}z-d_1=0,
\qquad
P_2=n_{21}x+n_{22}y+n_{23}z-d_2=0
$$
is a line. Its direction is
$$
\mathbf{b}=\mathbf{n}_1\times\mathbf{n}_2,
$$
because a vector along both planes must be perpendicular to both normals. Find one point by assigning a convenient coordinate and solving the remaining two equations.

:::example title="From general form to symmetric form"
For
$$
x+y+z=1,\qquad 2x-3y+4z=5,
$$
the normals give
$$
(1,1,1)\times(2,-3,4)=(7,-2,-5).
$$
Set $z=0$. Then $x+y=1$ and $2x-3y=5$, so the point is
$$
P=\left(\frac{8}{5},-\frac{3}{5},0\right).
$$
Thus
$$
\frac{x-8/5}{7}=\frac{y+3/5}{-2}=\frac{z}{-5}.
$$
Substitution checks both plane equations, and $(7,-2,-5)$ dots both normals to zero.
:::

:::key title="Convert only after checking independence"
If $\mathbf{n}_1\times\mathbf{n}_2=\mathbf{0}$, the plane normals are parallel: the planes may be parallel distinct or coincident, but they do not determine a unique intersection line. Compute the cross product before hunting for a point.
:::
