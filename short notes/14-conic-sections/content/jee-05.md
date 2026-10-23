---
id: jee-05
part: jee
title: "Ellipse — Tangents, Focal Chords and Director Circle"
---

## Tangent and normal in the form that fits the data

At $(x_1,y_1)$ on $x^2/a^2+y^2/b^2=1$, and at eccentric angle $\theta$,
$$
\frac{xx_1}{a^2}+\frac{yy_1}{b^2}=1,
\qquad
\frac{x\cos\theta}{a}+\frac{y\sin\theta}{b}=1.
$$
A finite-slope tangent has the two forms
$$
y=mx\pm\sqrt{a^2m^2+b^2}.
$$
The normal at eccentric angle $\theta$ is
$$
ax\sin\theta-by\cos\theta=(a^2-b^2)\sin\theta\cos\theta.
$$
Point-form equations include axis tangents and normals that a finite-slope formula can miss.

:::example title="Tangent at $\theta=45^\circ$ on $x^2/16+y^2/9=1$"
The contact point is $P=(2\sqrt{2},3/\sqrt{2})$. The tangent is
$$
\frac{x}{4\sqrt{2}}+\frac{y}{3\sqrt{2}}=1
\quad\Longleftrightarrow\quad3x+4y=12\sqrt{2}.
$$
The normal simplifies to $4x-3y=7\sqrt{2}/2$. Their slopes are $-3/4$ and $4/3$, whose product is $-1$.
:::

## Position and perpendicular tangents

For $S=x^2/a^2+y^2/b^2-1$, evaluating $S_1=S(x_1,y_1)$ gives inside when $S_1<0$, on when $S_1=0$, and outside when $S_1>0$. The locus of intersections of perpendicular tangents is the **director circle**
$$
x^2+y^2=a^2+b^2.
$$

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Perpendicular tangents meet on the director circle",
  "xrange": [-6.2, 6.2], "yrange": [-5.8, 6],
  "elements": [
    {"kind": "ellipse", "a": 4, "b": 3, "fill": "#E6F4F3", "alpha": 0.35},
    {"kind": "circle", "centre": [0, 0], "r": 5, "color": "#5B6B84", "ls": "--"},
    {"kind": "line", "a": [-5, 0], "b": [0, 5], "color": "#B8860B"},
    {"kind": "line", "a": [0, 5], "b": [5, 0], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 5], "label": "T(0,5)", "dx": 0.2, "dy": 0.2},
    {"kind": "point", "at": [-3.2, 1.8], "size": 6, "color": "#B8860B"},
    {"kind": "point", "at": [3.2, 1.8], "size": 6, "color": "#B91C1C"}
  ],
  "caption": "For a = 4 and b = 3, slope +/-1 tangents have intercept +/-5. The displayed perpendicular pair meets at (0,5), on x^2 + y^2 = 25."
}
:::

## A focal chord has a constant reciprocal sum

If a focus divides a focal chord into lengths $u,v$, then
$$
\frac{1}{u}+\frac{1}{v}=\frac{2a}{b^2}.
$$
Equivalently, the harmonic mean of $u,v$ is the semi-latus rectum $b^2/a$. This is a relation between the two parts, not a claim that each part equals $b^2/a$.

:::example title="An exact nonvertical focal chord"
On $x^2/25+y^2/9=1$, take $P=(5/2,3\sqrt{3}/2)$ and the right focus $F=(4,0)$. The line $PF$ meets the ellipse again at
$$
Q=\left(\frac{65}{14},-\frac{9\sqrt{3}}{14}\right).
$$
The two segment lengths are $PF=3$ and $QF=9/7$. Hence
$$
\frac{1}{3}+\frac{7}{9}=\frac{10}{9}=\frac{2a}{b^2},
\qquad
\frac{2}{1/3+7/9}=\frac{9}{5}=\frac{b^2}{a}.
$$
Both endpoints satisfy the ellipse equation, and $Q$ lies inside $|x|\leq5$ as it must.
:::

## Reflection explains the foci

At $P$, the tangent makes equal angles with the two focal segments; equivalently, the normal internally bisects the focal angle. Therefore a ray from one focus reflects toward the other. This follows geometrically from the constant sum $PF_1+PF_2=2a$ and the stationary-path property of a tangent.

:::derive title="The director circle from two tangent slopes"
Let a tangent through $T=(h,k)$ have finite slope $m$. Since its intercept is $k-mh$, the ellipse tangency condition gives
$$
(k-mh)^2=a^2m^2+b^2,
$$
or
$$
(h^2-a^2)m^2-2hk\,m+(k^2-b^2)=0.
$$
The two tangent slopes have product $(k^2-b^2)/(h^2-a^2)$. Perpendicularity makes this product $-1$, hence $h^2+k^2=a^2+b^2$. Axis-aligned exceptional cases can be checked directly and lie on the same circle.
:::

:::warn title="A harmonic mean is not an arithmetic mean"
The relation is $1/u+1/v=2a/b^2$. Do not replace it by $(u+v)/2=b^2/a$, and do not accept a numerical endpoint without checking that it lies on the ellipse. Curve membership is the fastest way to catch a false focal-chord example.
:::
