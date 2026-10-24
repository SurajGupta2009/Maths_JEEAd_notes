---
id: jee-11
part: jee
title: "Area II — Split Slices, Horizontal Strips and Ellipses"
---

## Split when the upper and lower curves exchange places

Between $y=\sin x$ and $y=\cos x$ on $[0,\pi/2]$, the intersection is $x=\pi/4$. Therefore
$$
A=\int_0^{\pi/4}(\cos x-\sin x)dx
+\int_{\pi/4}^{\pi/2}(\sin x-\cos x)dx.
$$
Each piece equals $\sqrt{2}-1$, so
$$
A=2\sqrt{2}-2.
$$
Visual lab sheet 6 shades both positive pieces.

## Horizontal slices can avoid splitting

For the region between $x=y^2$ and $x=y+2$, solve
$$
y^2=y+2\quad\Longrightarrow\quad y=-1,2.
$$
For $-1\leq y\leq2$, the line is to the right: $y+2\geq y^2$. Thus
$$
A=\int_{-1}^{2}(y+2-y^2)dy
=\left[\frac{y^2}{2}+2y-\frac{y^3}{3}\right]_{-1}^{2}
=\frac{9}{2}.
$$
Here the strip height is $dy$ and its horizontal length is right-minus-left.

## An ellipse is a stretched circle

For $x^2/a^2+y^2/b^2=1$ with $a,b>0$,
$$
y=\pm b\sqrt{1-\frac{x^2}{a^2}}.
$$
Hence
$$
A=2b\int_{-a}^{a}\sqrt{1-\frac{x^2}{a^2}}dx.
$$
With $x=au$, the integral becomes $2ab\int_{-1}^{1}\sqrt{1-u^2}du=2ab(\pi/2)$, so
$$
A=\pi ab.
$$
This also gives the circle area $\pi a^2$ when $b=a$.

:::diagram
{
  "type": "graph",
  "title": "Vertical slices of an ellipse give area pi ab",
  "xrange": [-2.4, 2.4], "yrange": [-1.5, 1.5],
  "xticks": [-2, -1, 0, 1, 2], "yticks": [-1, 0, 1],
  "fills": [
    {"from": -2, "to": 2, "y1": "-sqrt(1-x**2/4)", "y2": "sqrt(1-x**2/4)", "color": "#F6C445", "alpha": 0.30}
  ],
  "curves": [
    {"expr": "sqrt(1-x**2/4)", "from": -2, "to": 2},
    {"expr": "-sqrt(1-x**2/4)", "from": -2, "to": 2, "color": "#B91C1C"}
  ],
  "points": [
    {"x": -2, "y": 0, "label": ""}, {"x": 2, "y": 0, "label": ""},
    {"x": 0, "y": 1, "label": "b=1", "dx": 0.15, "dy": 0.10},
    {"x": 0, "y": -1, "label": "-b", "dx": 0.15, "dy": -0.10}
  ],
  "caption": "The ellipse has a=2 and b=1. Its vertical height is 2b sqrt(1-x^2/a^2), and the shaded area is pi ab=2pi."
}
:::

:::warn title="Choose the variable that matches the boundary equations"
Use top-minus-bottom with $dx$ and right-minus-left with $dy$. Do not insert $x$-equations into a $dy$ integral without first expressing both boundaries as functions of $y$.
:::
