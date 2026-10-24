---
id: jee-08
part: jee
title: "Convexity, Concavity and Inflection"
---

## Convexity is about tangents below and secants above

On an interval, a twice-differentiable function with $f''\geq0$ is convex; one with $f''\leq0$ is concave. For a differentiable convex function,
$$
f(x)\geq f(a)+f'(a)(x-a),
$$
so every tangent lies below the graph. A **point of inflection** is a point where the concavity changes sign, not merely a point where $f''$ is zero.

:::example title="A cubic with one inflection point"
For $f(x)=x^3-3x$,
$$
f''(x)=6x.
$$
It is concave on $(-\infty,0)$ and convex on $(0,\infty)$, so $(0,0)$ is an inflection point. The tangent there is $y=-3x$, and
$$
f(x)-(-3x)=x^3,
$$
which changes sign at $0$: the graph crosses its tangent.
:::

:::diagram
{
  "type": "graph",
  "title": "At a cubic inflection point the curve crosses its tangent",
  "xrange": [-2.2, 2.2], "yrange": [-3.2, 3.2],
  "curves": [
    {"expr": "x**3-3*x", "from": -2.1, "to": 2.1},
    {"expr": "-3*x", "from": -1.05, "to": 1.05, "color": "#B91C1C"}
  ],
  "points": [{"x": 0, "y": 0, "label": "inflection", "dx": 0.18, "dy": 0.35}],
  "caption": "The teal cubic is concave left of the origin and convex right of it. Its red tangent y=-3x lies above on the left and below on the right."
}
:::

For $g(x)=x^3-3x^2$, $g''(x)=6(x-1)$, so $g$ is concave before $1$ and convex after $1$; $(1,-2)$ is its inflection point.

:::example title="A quartic has two inflection points, but x^4 has none"
For $h(x)=x^4-4x^2$,
$$
h''(x)=12x^2-8=12\left(x^2-\frac{2}{3}\right).
$$
The sign changes at $x=\pm\sqrt{2/3}$, where $h=-20/9$. Both are inflection points. The companion paper's printed $(\pm1/\sqrt{3},-11/9)$ do not satisfy $12x^2-8=0$; the values here correct that source defect.

For $x^4$, $f''(x)=12x^2$ is zero at $0$ but nonnegative on both sides. The origin is a minimum, not an inflection point.
:::

:::example title="The supporting line of x^2 at a=3"
For $f(x)=x^2$, $f(3)=9$ and $f'(3)=6$, so the supporting line is
$$
y=9+6(x-3)=6x-9.
$$
Convexity gives $x^2\geq6x-9$ for every real $x$. Equality occurs only at $x=3$, as the independent identity $x^2-(6x-9)=(x-3)^2$ confirms.
:::

:::warn title="Always test a sign change"
The condition $f''(c)=0$ is neither necessary in every nonsmooth setting nor sufficient by itself. In the usual twice-differentiable setting, it is only a screening condition for a possible inflection.
:::
