---
id: jee-02
part: jee
title: "Tangents, Normals and Angles Between Curves"
---

## Point, slope, then perpendicular slope

At $(a,f(a))$ with finite derivative $m=f'(a)$, the tangent is
$$
y-f(a)=m(x-a).
$$
If $m\ne0$, the normal has slope $-1/m$. If $m=0$, the tangent is horizontal and the normal is vertical. A vertical tangent such as $x=0$ for $y=x^{1/3}$ needs a geometric statement, not substitution into a finite-slope formula.

:::example title="A cubic tangent and normal at x=2"
For $f(x)=x^3-3x$, $f(2)=2$ and $f'(2)=3(4)-3=9$. Thus
$$
\text{tangent: }y-2=9(x-2)\quad\Longrightarrow\quad y=9x-16,
$$
and
$$
\text{normal: }y-2=-\frac{1}{9}(x-2)
\quad\Longrightarrow\quad x+9y=20.
$$
For comparison, the normal to $y=x^2$ at $(1,1)$ has slope $-1/2$, hence equation $x+2y=3$.
:::

:::diagram
{
  "type": "graph",
  "title": "The cubic tangent and normal are perpendicular at (2,2)",
  "xrange": [0.4, 3.3], "yrange": [-5, 14],
  "xticks": [0, 1, 2, 3], "yticks": [-5, 0, 5, 10],
  "curves": [
    {"expr": "x**3-3*x", "from": 0.4, "to": 2.85},
    {"expr": "9*x-16", "from": 1.35, "to": 3.2, "color": "#B91C1C"},
    {"expr": "(20-x)/9", "from": 0.5, "to": 3.2, "color": "#5B6B84"}
  ],
  "points": [{"x": 2, "y": 2, "label": "P(2,2)", "dx": 0.12, "dy": 0.35}],
  "caption": "The teal cubic has tangent y=9x-16 in red and normal x+9y=20 in slate. Their slopes 9 and -1/9 multiply to -1."
}
:::

## Parallel chords and angles use tangent slopes

The chord of $y=x^2$ joining $(1,1)$ and $(3,9)$ has slope $(9-1)/(3-1)=4$. Solving $2x=4$ gives the parallel tangent at $(2,4)$.

For nonvertical tangents of slopes $m_1,m_2$ with $m_1m_2\ne-1$, the acute angle $\theta$ between them satisfies
$$
\tan\theta=\left|\frac{m_1-m_2}{1+m_1m_2}\right|.
$$
At $(1,1)$, $y=x^2$ and $y=x^3$ have slopes $2$ and $3$, so $\tan\theta=1/7$ and $\theta=\arctan(1/7)\approx8.13^\circ$. Orthogonal curves instead have $m_1m_2=-1$; the angle formula's denominator then vanishes.

:::example title="Check orthogonality at the actual intersections"
For $y^2=4x$ and $x^2+y^2=5$, substitution gives $x^2+4x-5=0$. The real intersections are $(1,2)$ and $(1,-2)$. Implicit differentiation gives
$$
m_1=\frac{2}{y},\qquad m_2=-\frac{x}{y},
\qquad m_1m_2=-\frac{2x}{y^2}=-\frac{1}{2}
$$
at either intersection. The curves are therefore **not** orthogonal.
:::

:::warn title="Do not use the angle formula when the tangents are perpendicular"
The condition $m_1m_2=-1$ is handled separately. Vertical tangents also require a line-angle or implicit-geometric analysis rather than the displayed slope quotient.
:::
