---
id: jee-06
part: jee
title: "Local Maxima and Minima"
---

## A critical point is a candidate, not yet an extremum

A local maximum at an interior point requires nearby values to be no larger; a local minimum requires nearby values to be no smaller. Endpoints are not local extrema in the two-sided interior sense, but they are essential in absolute-extremum problems.

**First-derivative test.** If $f'$ changes from $+$ to $-$ at $c$, then $f$ has a local maximum at $c$; a change from $-$ to $+$ gives a local minimum. If the sign does not change, there is no local extremum.

**Second-derivative test.** If $f'(c)=0$ and $f''(c)>0$, there is a strict local minimum; if $f''(c)<0$, there is a strict local maximum. When $f''(c)=0$, the test is inconclusive: compare $x^3$, $x^4$ and $-x^4$ at the origin.

:::example title="Factor the derivative and read both signs"
For $f(x)=x^3-3x$,
$$
f'(x)=3(x-1)(x+1).
$$
At $x=-1$, the sign changes from positive to negative, so the local maximum is $f(-1)=2$. At $x=1$, it changes from negative to positive, so the local minimum is $f(1)=-2$.

For $g(x)=x^3-6x^2+9x+2$,
$$
g'(x)=3(x-1)(x-3).
$$
Hence $g$ has a local maximum $g(1)=6$ and a local minimum $g(3)=2$. The requested local maximum value is therefore $6$.
:::

:::diagram
{
  "type": "graph",
  "title": "A quartic can have two local minima and one local maximum",
  "xrange": [-2.3, 2.3], "yrange": [-5, 4.5],
  "curves": [{"expr": "x**4-4*x**2", "from": -2.25, "to": 2.25}],
  "points": [
    {"x": -1.4142135624, "y": -4, "label": "minimum -4", "dx": -0.65, "dy": -0.25},
    {"x": 0, "y": 0, "label": "local maximum 0", "dx": 0.2, "dy": 0.3},
    {"x": 1.4142135624, "y": -4, "label": "minimum -4", "dx": 0.2, "dy": -0.25}
  ],
  "caption": "For x^4-4x^2, the derivative 4x(x^2-2) gives critical points -sqrt(2), 0 and sqrt(2)."
}
:::

For this quartic, $h''(x)=12x^2-8$ confirms minima at $\pm\sqrt{2}$ and a maximum at $0$. Both minima are also global: $x^4-4x^2=(x^2-2)^2-4\geq-4$, with equality at both points.

:::warn title="A point with f'(c)=0 can be none of the three"
The origin for $x^3$ is stationary but is neither a local maximum nor a local minimum. A sign chart is safer than memorising a label for every stationary point.
:::
