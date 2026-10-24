---
id: jee-01
part: jee
title: "The Derivative from First Principles"
---

## The derivative is a limit of secant slopes

If the limit exists, the derivative of $f$ at $x$ is
$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}
=\lim_{z\to x}\frac{f(z)-f(x)}{z-x}.
$$
The quotient is the slope of the secant through $(x,f(x))$ and $(x+h,f(x+h))$. Its limiting value is the tangent slope and the instantaneous rate of change. A derivative must be a **finite** limit for ordinary differentiability.

:::example title="Expand, cancel h, then take the limit"
For $f(x)=x^2$ and $h\ne0$,
$$
\frac{(x+h)^2-x^2}{h}=2x+h\longrightarrow2x.
$$
Similarly, for $x\ne0$ and $x+h\ne0$,
$$
\frac{1/(x+h)-1/x}{h}
=-\frac{1}{x(x+h)}\longrightarrow-\frac{1}{x^2}.
$$
At $x=2$, the cubic quotient gives
$$
\frac{(2+h)^3-8}{h}=12+6h+h^2\longrightarrow12.
$$
:::

:::diagram
{
  "type": "graph",
  "title": "The secant slope approaches the tangent slope",
  "xrange": [-0.5, 2.6], "yrange": [-1, 5],
  "curves": [
    {"expr": "x**2", "from": -0.5, "to": 2.2},
    {"expr": "3*x-2", "from": 0.3, "to": 2.2, "label": "secant: slope 3", "labpos": 0.42, "label_dx": -0.75, "label_dy": 0.35, "color": "#B8860B"},
    {"expr": "2*x-1", "from": 0, "to": 2.4, "label": "tangent: slope 2", "labpos": 0.72, "label_dx": -0.55, "label_dy": -0.35, "color": "#B91C1C"}
  ],
  "points": [{"x": 1, "y": 1, "label": "P(1,1)", "dx": -0.65, "dy": 0.18}, {"x": 2, "y": 4, "label": "Q(2,4)", "dx": 0.15, "dy": 0.15}],
  "annotations": [{"text": "y=x^2", "x": 0.8, "y": 0.64, "tx": -0.25, "ty": 2.8}],
  "caption": "For h=1 the secant slope is (4-1)/(2-1)=3. As Q approaches P, the secant slope tends to f'(1)=2 and the line tends to y=2x-1."
}
:::

## Differentiability forces continuity, but not conversely

If $f'(a)$ exists, then
$$
f(x)-f(a)=\frac{f(x)-f(a)}{x-a}(x-a)
\longrightarrow f'(a)\cdot0=0.
$$
Thus $f$ is continuous at $a$. The converse is false: $|x|$ is continuous at $0$ but its left and right difference quotients are $-1$ and $1$.

## The tangent uses a point and the derivative slope

At $(a,f(a))$, a nonvertical tangent is
$$
y-f(a)=f'(a)(x-a).
$$
For $y=x^2$ at $a=1$, the point is $(1,1)$ and the slope is $2$, so the tangent is $y-1=2(x-1)$, or $y=2x-1$. Advanced tangent, normal and curve-sketching problems are developed in Chapter 19.

:::warn title="Recognize a derivative before calculating a new limit"
The limit
$$
\lim_{h\to0}\frac{\ln(e+h)-1}{h}
$$
is $f'(e)$ for $f(x)=\ln x$, hence it equals $1/e$. Matching $f(a+h)-f(a)$ is often faster than applying L'Hôpital's rule.
:::
