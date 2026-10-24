---
id: jee-visual-05
part: jee
title: "Visual Lab 5 — Signed Area versus Total Area"
---

## Opposite signs cancel; geometric areas add

:::diagram
{
  "type": "graph",
  "title": "The cubic on [-1,1] has signed integral zero",
  "xrange": [-1.25, 1.25], "yrange": [-1.25, 1.25],
  "xticks": [-1, 0, 1], "yticks": [-1, 0, 1],
  "fills": [
    {"from": -1, "to": 0, "y1": "x**3", "y2": 0, "color": "#B91C1C", "alpha": 0.20},
    {"from": 0, "to": 1, "y1": 0, "y2": "x**3", "color": "#F6C445", "alpha": 0.38}
  ],
  "curves": [{"expr": "x**3", "from": -1.1, "to": 1.1}],
  "points": [
    {"x": -1, "y": -1, "label": "negative contribution", "dx": 0.12, "dy": -0.12},
    {"x": 1, "y": 1, "label": "positive contribution", "dx": -0.90, "dy": 0.10}
  ],
  "caption": "The red and gold geometric areas are each 1/4. Their signed contributions are -1/4 and +1/4, so the definite integral is 0 while total area is 1/2."
}
:::

## Facts to retain

- Oddness on a symmetric interval explains signed cancellation immediately.
- Total area uses $|x^3|$ and is twice the positive piece on $[0,1]$.
- The zero at $x=0$ is the required splitting point for the absolute-value calculation.

:::example title="Compute both quantities without confusing them"
$$
\int_{-1}^1x^3dx=0,\qquad
\int_{-1}^1|x^3|dx=2\int_0^1x^3dx=\frac{1}{2}.
$$
The first is an oriented algebraic quantity; the second is the shaded geometric area.
:::
