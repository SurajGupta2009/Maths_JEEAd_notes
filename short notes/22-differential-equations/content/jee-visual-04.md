---
id: jee-visual-04
part: jee
title: "Visual Lab 4 — Damped Oscillation and Its Envelope"
---

## Phase repeats; amplitude does not

:::diagram
{
  "type": "graph",
  "title": "y = exp(-x) sin(2x) with envelopes plus/minus exp(-x)",
  "xrange": [-0.08, 6.35], "yrange": [-0.48, 1.04],
  "xticks": [0, 1.5707963268, 3.1415926536, 4.7123889804, 6.2831853072],
  "xticklabels": ["0", "pi/2", "pi", "3pi/2", "2pi"],
  "yticks": [-0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
  "curves": [
    {"expr": "exp(-x)*sin(2*x)", "from": 0, "to": 6.2831853072, "color": "#16295C", "lw": 3.0},
    {"expr": "exp(-x)", "from": 0, "to": 6.2831853072, "color": "#0F766E", "lw": 2.1, "ls": "--"},
    {"expr": "-exp(-x)", "from": 0, "to": 6.2831853072, "color": "#0F766E", "lw": 2.1, "ls": "--"}
  ],
  "points": [
    {"x": 0, "y": 0, "label": ""},
    {"x": 1.5707963268, "y": 0, "label": "zero spacing pi/2", "dx": -0.4, "dy": 0.16},
    {"x": 3.1415926536, "y": 0, "label": ""}
  ],
  "caption": "The first positive peak occurs at x=(1/2) arctan(2). After pi the sine phase repeats, but every value is multiplied by exp(-pi), so the damped graph is not periodic."
}
:::

## Three different time intervals

- Consecutive zeros are separated by $\pi/2$.
- Corresponding sine phases are separated by $\pi$; this is the quasi-period.
- The envelope is multiplied by $e^{-h}$ after any time shift $h$, and it halves when $h=\ln2$.

:::example title="Locate the first positive peak"
For $y=e^{-x}\sin2x$,
$$
y'=e^{-x}(2\cos2x-\sin2x).
$$
At the first positive maximum, $\tan2x=2$, so $x=\frac{1}{2}\arctan2$, not $\pi/8$. The maximum value is obtained by substituting this exact x-value into the original formula.
:::

:::warn title="Zeros and maxima generally have different spacing statements"
Zeros of this damped sine are equally spaced, but successive maxima must be found from y-prime = 0, not guessed halfway between zeros.
:::
