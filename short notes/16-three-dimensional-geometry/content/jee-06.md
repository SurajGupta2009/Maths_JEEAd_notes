---
id: jee-06
part: jee
title: "Planes — Normal, Intercept and Three-Point Forms"
---

## One point and one nonzero normal determine a plane

The plane through $A$ with normal $\mathbf{n}\ne\mathbf{0}$ is
$$
(\mathbf{r}-\mathbf{a})\cdot\mathbf{n}=0.
$$
If $\mathbf{n}=(n_1,n_2,n_3)$, this becomes
$$
n_1x+n_2y+n_3z=d,
\qquad d=\mathbf{a}\cdot\mathbf{n}.
$$
Multiplying the entire equation by a nonzero constant does not change the plane. The normal, however, must remain nonzero.

:::example title="Compute the constant from the given point"
Through $A=(1,2,3)$ with normal $(2,-3,4)$,
$$
d=2-6+12=8,
$$
so the plane is
$$
2x-3y+4z=8.
$$
Substitution of $A$ gives $8$, while the normal dots every displacement inside the plane to zero.
:::

## Three noncollinear points supply a normal

For $A,B,C$ noncollinear, take two edge vectors and cross them:
$$
\mathbf{n}=(B-A)\times(C-A).
$$
Then use any one of the three points to compute $d$. A zero cross product would mean collinear points, which do not determine a unique plane.

:::example title="Three intercepts become one plane equation"
For $A=(1,0,0)$, $B=(0,2,0)$ and $C=(0,0,3)$,
$$
(-1,2,0)\times(-1,0,3)=(6,3,2),
\qquad d=(6,3,2)\cdot(1,0,0)=6.
$$
Thus
$$
6x+3y+2z=6
\quad\Longleftrightarrow\quad
x+\frac{y}{2}+\frac{z}{3}=1.
$$
The second form is the intercept form $x/a+y/b+z/c=1$, here with $a=1,b=2,c=3$.
:::

:::diagram
{
  "type": "vector3d",
  "title": "Two edges fix the plane; their cross product fixes its normal",
  "xrange": [-1, 3], "yrange": [-1, 3.5], "zrange": [-1, 4],
  "elev": 24, "azim": -54,
  "elements": [
    {"kind": "polygon", "points": [[1, 0, 0], [0, 2, 0], [0, 0, 3]], "fill": "#DCEFED", "alpha": 0.32, "color": "#5B6B84"},
    {"kind": "arrow", "a": [1, 0, 0], "b": [2, 0.5, 0.3333], "label": "n = (6,3,2)", "label_at": [1.5, 0.25, 0.1667], "offset": [0.65, 0, 0.25], "color": "#B91C1C"},
    {"kind": "arrow", "a": [1, 0, 0], "b": [0, 2, 0], "label": "B-A", "label_at": [0.5, 1, 0], "offset": [0, 0.2, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [1, 0, 0], "b": [0, 0, 3], "label": "C-A", "label_at": [0.5, 0, 1.5], "offset": [0.4, 0, 0], "color": "#B8860B"},
    {"kind": "point", "at": [1, 0, 0], "label": "A", "offset": [0.25, -0.2, 0]},
    {"kind": "point", "at": [0, 2, 0], "label": "B", "offset": [0, 0.25, 0]},
    {"kind": "point", "at": [0, 0, 3], "label": "C", "offset": [0, 0, 0.25]}
  ],
  "caption": "The normal drawn from A is a scaled (6,3,2). All three vertices satisfy 6x+3y+2z=6, equivalently x+y/2+z/3=1."
}
:::

## Intercepts and normals are reciprocal descriptions

For nonzero intercepts $a,b,c$, the plane
$$
\frac{x}{a}+\frac{y}{b}+\frac{z}{c}=1
$$
has normal $(1/a,1/b,1/c)$, or any nonzero scalar multiple. If an intercept is infinite or zero, do not force this form; return to the normal equation.

:::key title="Membership and perpendicularity are the two fastest checks"
After finding a plane, substitute every required point. After finding a line in a plane, check that its direction dots the plane's normal to zero. These checks catch a wrong constant and a wrong normal independently.
:::
