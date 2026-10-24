---
id: jee-10
part: jee
title: "Area I — Vertical Slices and Total Area"
---

## Geometric area uses nonnegative height

If $f(x)\geq0$ on $[a,b]$, the area under $y=f(x)$ is $\int_a^bf(x)dx$. If $f$ changes sign, total area is
$$
\int_a^b|f(x)|dx,
$$
computed by splitting at zeros. Between two curves with $f(x)\geq g(x)$ on an interval, vertical slices give
$$
A=\int_a^b(f(x)-g(x))dx.
$$

:::example title="Signed cancellation and total area are different answers"
For $y=x^3$ on $[-1,1]$,
$$
\int_{-1}^1x^3dx=0,
$$
but
$$
A=\int_{-1}^0(-x^3)dx+\int_0^1x^3dx
=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}.
$$
The visual lab shades the two positive geometric pieces separately.
:::

:::example title="Area between a line and a parabola"
On $[0,1]$, $x\geq x^2$. Hence
$$
A=\int_0^1(x-x^2)dx
=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1
=\frac{1}{6}.
$$
The intersections at $x=0,1$ supply the finite boundary of the shaded region.
:::

:::diagram
{
  "type": "graph",
  "title": "The area between y=x and y=x^2 is one-sixth",
  "xrange": [-0.15, 1.2], "yrange": [-0.15, 1.2],
  "xticks": [0, 0.5, 1], "yticks": [0, 0.5, 1],
  "fills": [
    {"from": 0, "to": 1, "y1": "x**2", "y2": "x", "color": "#F6C445", "alpha": 0.38}
  ],
  "curves": [
    {"expr": "x", "from": -0.1, "to": 1.1, "color": "#B91C1C"},
    {"expr": "x**2", "from": -0.1, "to": 1.1}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "(0,0)", "dx": 0.05, "dy": 0.08},
    {"x": 1, "y": 1, "label": "(1,1)", "dx": -0.25, "dy": 0.06}
  ],
  "caption": "The red line is the upper boundary and the teal parabola is the lower boundary on [0,1]. The gold height is x-x^2, whose integral is 1/6."
}
:::

## A familiar arch confirms the sign convention

For P9, $\sin x\geq0$ on $[0,\pi]$, so its integral and geometric area agree:
$$
\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi=2.
$$
On an interval where the sine is negative, the signed integral would be negative while total area would use $-\sin x$.

:::warn title="Find intersections before choosing upper and lower curves"
The ordering $f\geq g$ can change at an intersection. A single formula $f-g$ over the whole interval would then subtract the two regions instead of adding their positive areas.
:::
