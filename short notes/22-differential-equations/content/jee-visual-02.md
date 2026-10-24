---
id: jee-visual-02
part: jee
title: "Visual Lab 2 — A Linear Field and the IVP Curve"
---

## The integrating-factor solution must follow the field

:::diagram
{
  "type": "graph",
  "title": "Slope field for y-prime + y = exp(x)",
  "xrange": [-2, 2], "yrange": [-3, 4],
  "xticks": [-2, -1, 0, 1, 2], "yticks": [-3, -2, -1, 0, 1, 2, 3, 4],
  "slope_fields": [{"expr": "exp(x)-y", "nx": 17, "ny": 15, "length": 0.14, "max_slope": 20}],
  "curves": [
    {"expr": "0.5*(exp(x)-exp(-x))", "from": -1.7, "to": 1.45, "color": "#0F766E", "lw": 3.1},
    {"expr": "0.5*exp(x)", "from": -2, "to": 1.55, "color": "#B91C1C", "lw": 2.4, "ls": "--"}
  ],
  "points": [{"x": 0, "y": 0, "label": "IVP (0,0)", "dx": 0.12, "dy": 0.18}],
  "caption": "The solid curve is sinh x, the Q12 IVP solution. The dashed curve exp(x)/2 is the C=0 member of the same general family. Both have local slope exp(x)-y."
}
:::

## Read C from the initial point

The general solution is
$$
y=\frac{1}{2}e^x+Ce^{-x}.
$$
At $x=0$, $y(0)=1/2+C$. Thus the solid IVP curve has $C=-1/2$, while the dashed curve has $C=0$. They are distinct and cannot intersect: uniqueness for $y'=e^x-y$ follows because the right-hand side is smooth and has bounded $y$-derivative on every finite region.

:::example title="Verify a tangent without the graph"
For the solid curve $y=\sinh x$,
$$
y'=\cosh x,
\qquad e^x-y=e^x-\frac{e^x-e^{-x}}{2}=\frac{e^x+e^{-x}}{2}=\cosh x.
$$
The identity holds for all real $x$, not only at the plotted points.
:::

:::warn title="Nearby-looking curves are not interchangeable solutions"
Changing C changes the initial value. A curve can only be called the IVP solution after both the differential equation and the initial point have been checked.
:::
