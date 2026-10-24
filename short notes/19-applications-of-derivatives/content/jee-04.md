---
id: jee-04
part: jee
title: "Monotonicity — Read the Sign of the Derivative"
---

## The Mean Value Theorem turns derivative sign into graph direction

If $f'>0$ throughout an interval, then for $a<b$ in that interval, MVT gives $c$ with
$$
f(b)-f(a)=f'(c)(b-a)>0.
$$
Thus $f$ is strictly increasing. Similarly, $f'<0$ implies strictly decreasing. Positive derivative is sufficient for strict increase, but not necessary: $x^3$ is strictly increasing on $\mathbb{R}$ even though its derivative is zero at $0$.

:::example title="Factor the derivative before drawing the sign chart"
For $f(x)=x^3-3x$,
$$
f'(x)=3(x-1)(x+1).
$$
Therefore $f$ increases on $(-\infty,-1)$ and $(1,\infty)$, and decreases on $(-1,1)$.

For $f(x)=2x^3-9x^2+12x$,
$$
f'(x)=6(x-1)(x-2),
$$
so it increases on $(-\infty,1)$ and $(2,\infty)$, and decreases on $(1,2)$.
:::

:::diagram
{
  "type": "graph",
  "title": "The derivative sign partitions the cubic into three monotone pieces",
  "xrange": [-2.3, 2.3], "yrange": [-3.2, 3.2],
  "curves": [{"expr": "x**3-3*x", "from": -2.15, "to": 2.15}],
  "vlines": [{"x": -1, "dx": -0.25}, {"x": 1, "dx": 0.25}],
  "points": [
    {"x": -1, "y": 2, "label": "turning point", "dx": -0.45, "dy": 0.25},
    {"x": 1, "y": -2, "label": "turning point", "dx": -0.45, "dy": -0.45}
  ],
  "caption": "For x^3-3x, the derivative is positive on the outer intervals and negative between -1 and 1. The marked points are where the sign changes."
}
:::

## Monotonicity proves inequalities and global extrema

For $x>0$, let
$$
g(x)=x-1-\ln x,\qquad g'(x)=1-\frac{1}{x}.
$$
Then $g$ decreases on $(0,1)$ and increases on $(1,\infty)$, so its global minimum is $g(1)=0$. Hence $\ln x\leq x-1$, with equality only at $x=1$.

Similarly, $F(x)=x-\ln x$ has $F'(x)=1-1/x$, so its minimum value on $x>0$ is $F(1)=1$.

:::warn title="A zero at an isolated point does not destroy strict monotonicity"
The correct refinement is: if $f'\geq0$ and $f'$ is not identically zero on any subinterval, then $f$ is strictly increasing. Do not replace this with the false claim that $f'(x)>0$ at every single point is necessary.
:::
