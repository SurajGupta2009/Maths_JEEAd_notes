---
id: jee-07
part: jee
title: "Absolute Extrema — Closed Intervals and Endpoints"
---

## The Extreme Value Theorem supplies the checklist

A continuous function on a closed bounded interval attains both an absolute maximum and an absolute minimum. Compare the values at every interior stationary point, every point where the derivative fails to exist, and both endpoints.

:::diagram
{
  "type": "flow",
  "title": "Absolute extrema are decided by comparing all candidates",
  "steps": [
    {"title": "Check the hypotheses", "detail": "Confirm continuity on the closed bounded interval, or adapt the method."},
    {"title": "List every candidate", "detail": "Include critical points, nondifferentiable points and both endpoints."},
    {"title": "Evaluate f at each", "detail": "Keep exact values; do not compare derivative values instead."},
    {"title": "Select and state locations", "detail": "Report both the extreme value and every point where it occurs."}
  ],
  "caption": "On an open or unbounded interval, values may only approach a supremum or infimum; attainment must be checked separately."
}
:::

:::example title="Four candidates determine the extrema on [-2,2]"
On $[-2,2]$, for $f(x)=x^3-3x$,
$$
f'(x)=3(x-1)(x+1).
$$
Both $-1$ and $1$ are interior critical points. The candidate values are
$$
f(-2)=-2,\qquad f(-1)=2,\qquad f(1)=-2,\qquad f(2)=2.
$$
Thus the absolute minimum is $-2$, attained at $x=-2$ and $x=1$; the absolute maximum is $2$, attained at $x=-1$ and $x=2$.
:::

:::example title="An endpoint may also be the minimum"
For $f(x)=x+1/x$ on $[1/2,4]$,
$$
f'(x)=1-\frac{1}{x^2}=\frac{(x-1)(x+1)}{x^2}.
$$
The interior critical point is $x=1$, and
$$
f(1/2)=5/2,\qquad f(1)=2,\qquad f(4)=17/4.
$$
The absolute minimum is $2$ at $x=1$ and the absolute maximum is $17/4$ at $x=4$.

On the larger interval $(0,\infty)$, the global minimum is still $2$ because $(\sqrt{x}-1/\sqrt{x})^2\geq0$. There is no global maximum since $f(x)\to\infty$ as $x\to\infty$.
:::

:::warn title="On open intervals, distinguish an attained value from a limiting value"
For $x,y>0$ with $x+y=6$, $x^3+y^3=18(x-3)^2+54$. The minimum $54$ occurs at $x=y=3$. The value $216$ is only approached as an endpoint is approached, so there is no attained maximum.
:::
