---
id: jee-09
part: jee
title: "Curve Sketching as a Synthesis"
---

## Combine features instead of plotting isolated points

A reliable sketch records the domain, symmetry, intercepts, asymptotic behaviour, monotone intervals, local extrema, concavity and inflection points. Each feature should agree with the others: a local maximum on a concave cap, for example, cannot sit in an interval where the second derivative is positive.

:::diagram
{
  "type": "flow",
  "title": "A curve-sketching checklist turns derivatives into shape",
  "steps": [
    {"title": "Domain and symmetry", "detail": "Exclude singular inputs; identify even, odd or periodic structure."},
    {"title": "Intercepts and limits", "detail": "Find axes crossings, end behaviour and any asymptotes."},
    {"title": "First derivative", "detail": "Mark monotone intervals and classify stationary points."},
    {"title": "Second derivative", "detail": "Mark concavity and verify inflection by a sign change."},
    {"title": "Assemble and check", "detail": "Join the features smoothly and test one value on each branch."}
  ],
  "caption": "The graph is the final consistency check of the algebra, not a replacement for it."
}
:::

:::example title="A complete feature list for y=x^4-4x^2"
The function is even, so its graph is symmetric about the $y$-axis. Its intercepts satisfy
$$
x^2(x^2-4)=0,
$$
giving $(0,0)$, $(-2,0)$ and $(2,0)$. The origin is a double root, so the graph touches the $x$-axis there rather than crossing it.

From $f'(x)=4x(x^2-2)$, the function decreases on $(-\infty,-\sqrt{2})$ and $(0,\sqrt{2})$, and increases on $(-\sqrt{2},0)$ and $(\sqrt{2},\infty)$. Its local minimum value is $-4$ at $x=\pm\sqrt{2}$, and its local maximum value is $0$ at $x=0$.

From $f''(x)=12x^2-8$, it is convex outside $\pm\sqrt{2/3}$ and concave between them. The inflection points are
$$
\left(-\sqrt{\frac{2}{3}},-\frac{20}{9}\right),
\qquad
\left(\sqrt{\frac{2}{3}},-\frac{20}{9}\right).
$$
Finally $f(x)\to\infty$ as $x\to\pm\infty$, so both outer branches rise.
:::

## Translate the feature list into a shape

Start at the upper-left branch, descend to the left minimum, rise to the origin, descend to the right minimum, and then rise to the upper-right. The tangent is horizontal at all three turning points; at the origin the horizontal tangent is also the $x$-axis.

:::warn title="An intercept's multiplicity affects the sketch"
At $x=0$ in this example the factor $x^2$ has even multiplicity. The graph touches the axis. At $x=\pm2$ the factors have odd multiplicity, so the graph crosses it.
:::
