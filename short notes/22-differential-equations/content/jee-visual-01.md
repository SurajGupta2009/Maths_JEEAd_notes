---
id: jee-visual-01
part: jee
title: "Visual Lab 1 — A Real Slope Field and Its Branches"
---

## Every short segment has slope x/y

:::diagram
{
  "type": "graph",
  "title": "The slope field for y-prime = x/y with three solution branches",
  "xrange": [-3, 3], "yrange": [-3.4, 3.4],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-3, -2, -1, 0, 1, 2, 3],
  "slope_fields": [{"expr": "x/y", "nx": 19, "ny": 17, "length": 0.13, "max_slope": 30}],
  "curves": [
    {"expr": "sqrt(x**2+1)", "from": -3, "to": 3, "color": "#0F766E", "lw": 3.1},
    {"expr": "-sqrt(x**2+1)", "from": -3, "to": 3, "color": "#0F766E", "lw": 2.4, "ls": "--"},
    {"expr": "sqrt(x**2-1)", "from": 1, "to": 3, "color": "#B91C1C", "lw": 2.8}
  ],
  "points": [{"x": 0, "y": 1, "label": "y(0)=1", "dx": 0.16, "dy": 0.12}],
  "caption": "The teal branches have y^2-x^2=1; the red branch has y^2-x^2=-1. Segments on y=0 are omitted because x/y is undefined there. The formerly cropped lower branch is now visible."
}
:::

## Read the geometry algebraically

Differentiate $y^2-x^2=C$:
$$
2yy'-2x=0
\quad\Longrightarrow\quad y'=\frac{x}{y}.
$$
Conversely, separation gives $y^2-x^2=C$ on any nonzero-$y$ solution interval. The initial point $(0,1)$ selects $C=1$ and the positive branch $y=\sqrt{x^2+1}$.

:::example title="Check three displayed tangent directions"
At $(0,1)$ the slope is $0$, so the teal upper branch is horizontal. At $(1,\sqrt{2})$ its slope is $1/\sqrt{2}$. At $(2,\sqrt{3})$ on the red branch its slope is $2/\sqrt{3}$. Each agrees with the local line element.
:::

:::warn title="A slope field is not a set of arrows to follow across discontinuities"
The equation is undefined at $y=0$. Do not join upper and lower branches through the x-axis merely because their formulas share the same constant C.
:::
