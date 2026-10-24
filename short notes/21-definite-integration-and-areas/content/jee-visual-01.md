---
id: jee-visual-01
part: jee
title: "Visual Lab 1 — Right-Endpoint Rectangles"
---

## Read the approximation before taking the limit

:::diagram
{
  "type": "graph",
  "title": "Four right-endpoint rectangles for y=x^2 on [0,2]",
  "xrange": [-0.15, 2.25], "yrange": [-0.3, 4.65],
  "xticks": [0, 0.5, 1, 1.5, 2], "yticks": [0, 1, 2, 3, 4],
  "rectangles": [
    {"x": 0, "width": 0.5, "height": 0.25},
    {"x": 0.5, "width": 0.5, "height": 1},
    {"x": 1, "width": 0.5, "height": 2.25},
    {"x": 1.5, "width": 0.5, "height": 4}
  ],
  "curves": [{"expr": "x**2", "from": 0, "to": 2.08}],
  "points": [
    {"x": 2, "y": 4, "label": "right endpoints", "dx": -0.85, "dy": 0.25},
    {"x": 1, "y": 1, "label": ""}, {"x": 1.5, "y": 2.25, "label": ""}
  ],
  "caption": "The four heights are 1/4, 1, 9/4 and 4, with common width 1/2. Their sum is 3.75, above the exact integral 8/3 because x^2 is increasing."
}
:::

## Facts to retain

- A right-endpoint sum uses $f(x_i)$ with $x_i=a+i\Delta x$.
- For an increasing nonnegative function, right-endpoint rectangles overestimate the area; left endpoints underestimate it.
- Refinement changes both the number and widths of rectangles, not the target interval.

:::example title="Check the displayed finite sum"
$$
R_4=\frac{1}{2}\left(\frac{1}{4}+1+\frac{9}{4}+4\right)
=\frac{15}{4}=3.75.
$$
As $n\to\infty$, $R_n\to8/3\approx2.6666667$. The finite sum and its limit are both useful, but they are not equal.
:::
