---
id: jee-07
part: jee
title: "Hyperbola — Tangents, Normals and the Rectangular Form"
---

## Tangency conditions carry slope restrictions

At $(x_1,y_1)$ on $x^2/a^2-y^2/b^2=1$,
$$
\frac{xx_1}{a^2}-\frac{yy_1}{b^2}=1.
$$
Using $P(\theta)=(a\sec\theta,b\tan\theta)$ gives
$$
\frac{x\sec\theta}{a}-\frac{y\tan\theta}{b}=1.
$$
For a finite-slope tangent,
$$
y=mx\pm\sqrt{a^2m^2-b^2},\qquad |m|>\frac{b}{a}.
$$
The radicand itself explains the restriction: a tangent cannot be as flat as an asymptote direction. Vertex tangents are vertical and come directly from the point form.

The normal at parameter $\theta$ can be written
$$
ax\sin\theta+by=(a^2+b^2)\tan\theta.
$$
The director locus for perpendicular tangents is $x^2+y^2=a^2-b^2$. It is a real circle only when $a>b$; when $a=b$, a rectangular hyperbola has no real pair of perpendicular tangents, and when $a<b$ the formal radius squared is negative.

:::example title="A line parallel to an asymptote leaves one finite intersection"
Intersect $y=3x/2+1$ with $x^2/4-y^2/9=1$. The line is parallel to the asymptote $y=3x/2$. Substitution cancels the quadratic terms:
$$
-\frac{x}{3}-\frac{1}{9}=1
\quad\Longrightarrow\quad x=-\frac{10}{3},\qquad y=-4.
$$
There is exactly one finite intersection, $(-10/3,-4)$; the other algebraic intersection has escaped to infinity.
:::

## Rotate the rectangular hyperbola into $xy=c^2$

The curve $xy=c^2$ is a rectangular hyperbola with coordinate axes as asymptotes and $e=\sqrt{2}$. Its parameter and tangent/normal pair are
$$
P(t)=\left(ct,\frac{c}{t}\right),\qquad
\frac{x}{t}+ty=2c,
$$
$$
y=t^2x-ct^3+\frac{c}{t},\qquad t\ne0.
$$
The tangent slope is $-1/t^2<0$, so the normal slope is $t^2$.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Tangent and normal to xy = 4 at P(4,1)",
  "xrange": [-5.5, 8.5], "yrange": [-4.5, 5.5],
  "elements": [
    {"kind": "rectangular", "c": 2, "trange": [0.38, 3.2], "color": "#0F766E"},
    {"kind": "line", "a": [0, 2], "b": [8, 0], "label": "x + 4y = 8", "label_pos": -0.35, "dx": 0.2, "dy": 0.25, "color": "#B8860B"},
    {"kind": "line", "a": [3.75, 0], "b": [5, 5], "label": "normal y = 4x - 15", "label_pos": 0.58, "dx": 0.2, "color": "#B91C1C"},
    {"kind": "point", "at": [4, 1], "label": "P(4,1), t = 2", "dx": 0.2}
  ],
  "caption": "With c = 2 and t = 2, P = (ct,c/t) = (4,1). The coordinate axes are the asymptotes. The tangent and normal slopes are -1/4 and 4, whose product is -1."
}
:::

:::example title="Read both lines from one parameter"
For $xy=4$, $c=2$. At $t=2$, the contact point is $(4,1)$, the tangent is
$$
\frac{x}{2}+2y=4\quad\Longleftrightarrow\quad x+4y=8,
$$
and the normal is $y=4x-15$. Substitution of $(4,1)$ verifies both equations immediately.
:::

:::warn title="Asymptotes are not tangent lines"
They describe limiting direction, not finite contact. In particular, a point lying on $y=\pm(b/a)x$ cannot belong to the standard hyperbola. This membership check can prove that requested data are impossible before any lengthy calculation.
:::
