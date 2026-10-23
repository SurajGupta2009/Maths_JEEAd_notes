---
id: jee-90
part: jee
title: "Visual Quadratic Lab — Discriminant, Vertex and Root Location"
---

## The discriminant describes intersections

For $f(x)=ax^2+bx+c$ with $a\ne0$, the roots are the $x$-intercepts. Completing the square gives $f(x)=a((x+b/(2a))^2-D/(4a^2))$, where $D=b^2-4ac$. The sign of $D$ therefore controls two, one, or no real intersections.

:::diagram
{
  "type": "graph",
  "title": "Discriminant as an intersection count",
  "xrange": [-4, 4], "yrange": [-3, 6],
  "curves": [
    {"expr": "x**2-1", "label": "D > 0", "labpos": 0.78},
    {"expr": "x**2", "label": "D = 0", "labpos": 0.70, "color": "#B8860B"},
    {"expr": "x**2+1", "label": "D < 0", "labpos": 0.62, "color": "#B91C1C"}
  ],
  "points": [{"x": -1, "y": 0, "label": "root", "dx": -0.6, "dy": 0.25}, {"x": 1, "y": 0, "label": "root", "dx": 0.25, "dy": 0.25}, {"x": 0, "y": 0, "label": "double root", "dx": -0.1, "dy": 0.65, "ha": "right", "color": "#B8860B"}],
  "caption": "Vertical translation does not change the leading coefficient or axis. It changes the discriminant and hence the number of real x-intercepts."
}
:::

When $a>0$, the parabola opens upward; when $a<0$, downward. If $D<0$, there are no real roots and the expression keeps the sign of $a$ for every real $x$. This is often faster than attempting a sign table with no roots.

<!-- pagebreak -->
## The vertex gives the extreme value

Completing the square also gives the vertex $(-b/(2a),-D/(4a))$. For $f(x)=x^2-2x-3=(x-1)^2-4$, the vertex is $(1,-4)$, the axis is $x=1$, and the range is $[-4,\infty)$.

:::diagram
{
  "type": "graph",
  "title": "Vertex, axis, intercepts and range in one picture",
  "xrange": [-3, 5], "yrange": [-5, 6],
  "curves": [{"expr": "x**2-2*x-3", "label": "x^2 - 2x - 3", "labpos": 0.82}],
  "vlines": [{"x": 1, "label": "axis x = 1", "dx": 0.15, "ha": "left"}],
  "points": [{"x": 1, "y": -4, "label": "minimum -4", "dx": 0.2}, {"x": -1, "y": 0, "label": "-1", "dy": 0.25}, {"x": 3, "y": 0, "label": "3", "dx": -0.4, "dy": 0.25}],
  "caption": "The roots are symmetric about the axis: their mean is 1. The minimum is attained, so the range includes -4 and every larger real number."
}
:::

Vieta's relations are visible here: the sum of the roots is twice the axis coordinate, $-1+3=2=-b/a$, and their product is $(-1)3=-3=c/a$. Use these as structural checks even when exact roots are not required.

<!-- pagebreak -->
## Root location is a sign-and-axis problem

A root-location question asks more than whether roots exist. To place both roots of an upward parabola to the right of $k$, require a nonnegative discriminant, an axis to the right of $k$, and $f(k)>0$. For a double root, use the corresponding boundary interpretation carefully.

:::diagram
{
  "type": "numberline",
  "title": "The roots -1 and 3 split the sign of x^2 - 2x - 3",
  "range": [-3, 5], "ticks": [-3, -2, -1, 0, 1, 2, 3, 4, 5], "xlabel": "x",
  "items": [
    {"kind": "interval", "a": -2.8, "b": -1, "label": "positive", "label_x": -2, "color": "#0F766E"},
    {"kind": "interval", "a": -1, "b": 3, "label": "negative", "label_x": 1, "label_y": 0.95, "color": "#B91C1C"},
    {"kind": "interval", "a": 3, "b": 4.8, "label": "positive", "label_x": 4, "color": "#0F766E"},
    {"kind": "points", "xs": [-1, 3], "label": "roots", "label_x": 1, "label_y": -1.0, "color": "#B8860B"}
  ],
  "caption": "An upward quadratic is positive outside its distinct roots and negative between them. If roots are repeated or absent, this alternating pattern must be modified."
}
:::

For $x^2-2x-3=(x+1)(x-3)$, the signs follow directly from the factors. The graph and factorisation agree: at $x=0$, $f(0)=-3$, placing the origin in the negative interval.

<!-- pagebreak -->
## A worked parameter filter

Consider $x^2-2mx+m+2$ and ask for both roots greater than $1$. The discriminant is $4(m-2)(m+1)$, the axis is $x=m$, and $f(1)=3-m$. The three conditions become
$$
(m-2)(m+1)\geq0,\qquad m>1,\qquad 3-m>0.
$$
Their intersection is $2\leq m<3$. At $m=2$, the double root is $x=2$, which is allowed; as $m\to3^-$, one root approaches $1$ from above.

:::diagram
{
  "type": "flow",
  "title": "Root-location workflow",
  "steps": [
    {"title": "Fix the leading sign and target intervals", "detail": "Write whether the parabola opens upward or downward and what 'both roots greater than k' means at equality."},
    {"title": "Impose existence, axis and endpoint signs", "detail": "Use discriminant, -b/(2a), and f(k); add further endpoint signs for bounded intervals."},
    {"title": "Intersect all parameter conditions", "detail": "Do not replace the intersection by only the discriminant or only f(k)."},
    {"title": "Test boundary and interior parameters", "detail": "Check repeated-root endpoints and one value strictly inside the claimed parameter set."}
  ],
  "caption": "At m = 2 the equation is (x - 2)^2. At m = 5/2 the roots are (5 +/- sqrt(7))/2, both greater than 1. Boundary and interior checks confirm the parameter interval."
}
:::

:::key title="Keep all three conditions"
For $m=5/2$, the polynomial is $x^2-5x+9/2$, whose roots are $(5\pm\sqrt{7})/2$, both greater than $1$. Discriminant alone would allow unwanted parameters; the axis and endpoint-sign conditions are what locate the roots.
:::
