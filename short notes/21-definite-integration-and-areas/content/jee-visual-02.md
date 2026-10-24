---
id: jee-visual-02
part: jee
title: "Visual Lab 2 — Accumulated Area and Its Derivative"
---

## See FTC as a moving upper boundary

:::diagram
{
  "type": "graph",
  "title": "Height f(x)=2x and accumulation A(x)=x^2",
  "xrange": [-0.15, 2.25], "yrange": [-0.35, 4.65],
  "xticks": [0, 1, 2], "yticks": [0, 1, 2, 3, 4],
  "fills": [
    {"from": 0, "to": 1, "y1": 0, "y2": "2*x", "color": "#F6C445", "alpha": 0.38},
    {"from": 1, "to": 2, "y1": 0, "y2": "2*x", "color": "#0F6B5C", "alpha": 0.14}
  ],
  "curves": [
    {"expr": "2*x", "from": 0, "to": 2.05, "color": "#B91C1C"},
    {"expr": "x**2", "from": 0, "to": 2.05}
  ],
  "points": [
    {"x": 1, "y": 1, "label": "A(1)=1", "dx": -0.55, "dy": -0.35},
    {"x": 2, "y": 4, "label": "A(2)=4", "dx": -0.75, "dy": 0.25}
  ],
  "caption": "The red line is the height 2x; the teal parabola is A(x)=integral from 0 to x of 2t dt=x^2. Gold and pale teal areas accumulate to 1 and 4."
}
:::

## Facts to retain

- $A(x)=\int_0^x2t\,dt=x^2$, while $A'(x)=2x=f(x)$.
- The area added from $x$ to $x+h$ is approximately $f(x)h$ for small $h$.
- The derivative of the area curve is the height curve, not the area under the height curve again.

:::example title="Verify both directions numerically"
At $x=1$, the triangular gold area is $\frac{1}{2}(1)(2)=1=A(1)$. Also $A'(1)=2=f(1)$. At $x=2$, the total triangular area is $\frac{1}{2}(2)(4)=4=A(2)$.
:::
