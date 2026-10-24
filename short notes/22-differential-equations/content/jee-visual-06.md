---
id: jee-visual-06
part: jee
title: "Visual Lab 6 — Clairaut Tangents and Their Envelope"
---

## The singular solution is touched by every straight-line member

:::diagram
{
  "type": "graph",
  "title": "Lines y = Cx + C^2 and the envelope y = -x^2/4",
  "xrange": [-4.4, 4.4], "yrange": [-5, 4.5],
  "xticks": [-4, -3, -2, -1, 0, 1, 2, 3, 4], "yticks": [-4, -3, -2, -1, 0, 1, 2, 3, 4],
  "curves": [
    {"expr": "-x**2/4", "from": -4.35, "to": 4.35, "color": "#B91C1C", "lw": 3.2},
    {"expr": "-2*x+4", "from": -4.4, "to": 4.4, "color": "#16295C", "lw": 1.8},
    {"expr": "-x+1", "from": -4.4, "to": 4.4, "color": "#16295C", "lw": 1.8},
    {"expr": "0*x", "from": -4.4, "to": 4.4, "color": "#16295C", "lw": 1.8},
    {"expr": "x+1", "from": -4.4, "to": 4.4, "color": "#16295C", "lw": 1.8},
    {"expr": "2*x+4", "from": -4.4, "to": 4.4, "color": "#16295C", "lw": 1.8}
  ],
  "points": [
    {"x": 4, "y": -4, "label": ""}, {"x": 2, "y": -1, "label": ""},
    {"x": 0, "y": 0, "label": "C=0", "dx": 0.15, "dy": 0.15},
    {"x": -2, "y": -1, "label": ""}, {"x": -4, "y": -4, "label": ""}
  ],
  "caption": "For each C, the line touches the red parabola at x=-2C and y=-C^2. The line and envelope have the same value and derivative there."
}
:::

## Eliminate C by envelope conditions

A line satisfies $F(x,y,C)=y-Cx-C^2=0$. Its envelope also satisfies
$$
F_C=-x-2C=0.
$$
Thus $C=-x/2$ and
$$
y=Cx+C^2=-\frac{x^2}{2}+\frac{x^2}{4}=-\frac{x^2}{4}.
$$
Direct differentiation gives $y'=-x/2=C$ at the contact point, confirming both value and slope agreement.

:::example title="The envelope also solves the differential equation"
If $y=-x^2/4$, then $p=y'=-x/2$ and
$$
xp+p^2=-\frac{x^2}{2}+\frac{x^2}{4}=-\frac{x^2}{4}=y.
$$
This is why the envelope is a genuine singular solution, not merely a visual boundary. No finite C produces the parabola; it is an additional solution and must be listed separately.
:::
