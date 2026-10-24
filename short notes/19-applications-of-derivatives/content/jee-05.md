---
id: jee-05
part: jee
title: "Root Counting with Monotone Branches"
---

## Separate existence from uniqueness

The Intermediate Value Theorem supplies a root when a continuous function changes sign. Strict monotonicity on an interval prevents two roots there. First split the domain at turning points and singularities; then apply these two ideas branch by branch.

:::diagram
{
  "type": "flow",
  "title": "A root count is an interval-by-interval argument",
  "steps": [
    {"title": "Locate critical points", "detail": "Solve f'(x)=0 and include points where the derivative is undefined."},
    {"title": "Partition the domain", "detail": "On each branch, record whether f is increasing or decreasing."},
    {"title": "Evaluate signs and limits", "detail": "Use endpoint values, asymptotic behaviour and IVT where a sign changes."},
    {"title": "Count with multiplicity of branches", "detail": "A monotone branch has at most one root; add only branches with proved existence."}
  ],
  "caption": "A sign change alone does not prove uniqueness, and monotonicity alone does not prove existence."
}
:::

:::example title="The cubic x^3-3x+1 has exactly three real roots"
For $f(x)=x^3-3x+1$, the critical points are $-1$ and $1$, and
$$
f(-2)=-1,\qquad f(-1)=3,\qquad f(1)=-1,\qquad f(2)=3.
$$
The derivative $3(x^2-1)$ makes $f$ strictly monotone on
$$
(-\infty,-1),\qquad(-1,1),\qquad(1,\infty).
$$
Its end behaviour is $f(x)\to-\infty$ as $x\to-\infty$ and $f(x)\to\infty$ as $x\to\infty$. Thus IVT gives one root on each branch, and monotonicity rules out a second: exactly three real roots in total.
:::

:::example title="A line cannot intersect a strictly convex parabola more than twice"
For $y=x^2$ and $y=mx+c$, intersections satisfy
$$
x^2-mx-c=0.
$$
This quadratic has two, one or no real solutions according as its discriminant $m^2+4c$ is positive, zero or negative. More generally, subtracting the proposed line and counting turning points converts an intersection question into a root count.
:::

:::warn title="Do not infer the number of roots from the degree alone"
A cubic has at most three real roots, not necessarily three. The derivative sign chart and endpoint information determine the actual count.
:::
