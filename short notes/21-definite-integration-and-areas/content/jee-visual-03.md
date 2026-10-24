---
id: jee-visual-03
part: jee
title: "Visual Lab 3 — King's Reflection"
---

## Reflection swaps sine squared and cosine squared

:::diagram
{
  "type": "graph",
  "title": "Mirror-related integrands on [0,pi/2]",
  "xrange": [-0.12, 1.75], "yrange": [-0.10, 1.15],
  "xticks": [0, 0.7853981634, 1.5707963268], "yticks": [0, 0.5, 1],
  "fills": [
    {"from": 0, "to": 1.5707963268, "y1": 0, "y2": "sin(x)**2", "color": "#F6C445", "alpha": 0.25}
  ],
  "curves": [
    {"expr": "sin(x)**2", "from": 0, "to": 1.5707963268},
    {"expr": "cos(x)**2", "from": 0, "to": 1.5707963268, "color": "#B91C1C"}
  ],
  "points": [
    {"x": 0.7853981634, "y": 0.5, "label": "x=pi/4", "dx": 0.10, "dy": 0.10}
  ],
  "caption": "Teal sin^2(x) and red cos^2(x) interchange under x->pi/2-x. Each has area pi/4, and their ordinates add to 1 at every x."
}
:::

## Facts to retain

- Reflection preserves the interval $[0,\pi/2]$ and the integral, not each individual height.
- At every $x$, $\sin^2x+\cos^2x=1$; hence the two equal areas sum to the rectangle area $\pi/2$.
- The crossing at $x=\pi/4$ has common height $1/2$.

:::example title="Read the two areas from the diagram"
If $I$ is either shaded area, then $2I=\int_0^{\pi/2}1\,dx=\pi/2$, so $I=\pi/4\approx0.7853981634$. The vertical midpoint $\pi/4$ and the area value $\pi/4$ are numerically equal here only because the interval length is $\pi/2$.
:::
