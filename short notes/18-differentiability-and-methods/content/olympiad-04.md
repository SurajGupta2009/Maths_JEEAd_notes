---
id: olympiad-04
part: olympiad
title: "Extension IV — Discontinuous Derivatives and Darboux"
---

## A derivative can exist everywhere yet fail to be continuous

Define $f(0)=0$ and, for $x\ne0$,
$$
f(x)=x^2\sin(1/x).
$$
At the origin,
$$
\left|\frac{f(x)-f(0)}{x}\right|=|x\sin(1/x)|\leq|x|\to0,
$$
so $f'(0)=0$. Away from the origin,
$$
f'(x)=2x\sin(1/x)-\cos(1/x).
$$
Along $x_n=1/(2n\pi)$, this equals $-1$; along $y_n=1/((2n+1)\pi)$, it equals $1$. Both input sequences tend to $0$, so $f'(x)$ has no limit at $0$. Thus $f'$ exists everywhere but is discontinuous there.

:::diagram
{
  "type": "graph",
  "title": "This everywhere-existing derivative oscillates near zero",
  "xrange": [-0.35, 0.35], "yrange": [-1.5, 1.5],
  "xticks": [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3], "yticks": [-1, 0, 1],
  "curves": [
    {"expr": "2*x*sin(1/x)-cos(1/x)", "from": -0.35, "to": -0.006, "n": 3000},
    {"expr": "2*x*sin(1/x)-cos(1/x)", "from": 0.006, "to": 0.35, "n": 3000}
  ],
  "points": [{"x": 0, "y": 0, "color": "#B91C1C"}],
  "annotations": [{"text": "f'(0)=0", "x": 0, "y": 0, "tx": 0.08, "ty": 1.25, "color": "#B91C1C"}],
  "caption": "The plotted formula applies away from 0; the marked value at 0 comes from the difference quotient. No single limiting value matches the oscillating branches."
}
:::

## Darboux's theorem still forces intermediate values

If $f$ is differentiable on an interval, then $f'$ has the **intermediate value property**: between any two attained derivative values, every intermediate value is also attained. Continuity of $f'$ is not required.

Consequently, a genuine derivative cannot have a simple jump discontinuity: values immediately on either side could not skip an entire interval of intermediate slopes. The example above instead has an oscillatory discontinuity, which is compatible with Darboux's theorem.

:::key title="Separate three statements"
Differentiability of $f$ does not imply continuity of $f'$. Continuity of $f'$ is stronger. Darboux's intermediate value property follows from differentiability alone and rules out jump discontinuities, but not oscillation.
:::
