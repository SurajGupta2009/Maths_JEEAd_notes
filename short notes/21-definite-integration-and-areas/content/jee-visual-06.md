---
id: jee-visual-06
part: jee
title: "Visual Lab 6 — Area between Sine and Cosine"
---

## The top curve changes at the intersection

:::diagram
{
  "type": "graph",
  "title": "Two positive regions between sine and cosine",
  "xrange": [-0.12, 1.75], "yrange": [-0.10, 1.15],
  "xticks": [0, 0.7853981634, 1.5707963268], "yticks": [0, 0.5, 1],
  "fills": [
    {"from": 0, "to": 0.7853981634, "y1": "sin(x)", "y2": "cos(x)", "color": "#F6C445", "alpha": 0.34},
    {"from": 0.7853981634, "to": 1.5707963268, "y1": "cos(x)", "y2": "sin(x)", "color": "#0F6B5C", "alpha": 0.20}
  ],
  "curves": [
    {"expr": "sin(x)", "from": 0, "to": 1.5707963268},
    {"expr": "cos(x)", "from": 0, "to": 1.5707963268, "color": "#B91C1C"}
  ],
  "points": [
    {"x": 0.7853981634, "y": 0.7071067812, "label": "x=pi/4", "dx": 0.08, "dy": 0.10}
  ],
  "caption": "Cosine is above sine before pi/4; sine is above cosine afterwards. The gold and pale teal areas are each sqrt(2)-1, giving total area 2sqrt(2)-2."
}
:::

## Facts to retain

- The intersection satisfies $\sin x=\cos x$, hence $x=\pi/4$ on the displayed interval.
- Using one fixed top-minus-bottom formula across $\pi/4$ would produce signed cancellation instead of total area.
- Each positive piece has area $\sqrt{2}-1\approx0.4142135624$.

:::example title="Check the two piecewise antiderivatives"
$$
\int_0^{\pi/4}(\cos x-\sin x)dx
=[\sin x+\cos x]_0^{\pi/4}=\sqrt{2}-1,
$$
$$
\int_{\pi/4}^{\pi/2}(\sin x-\cos x)dx
=[-\cos x-\sin x]_{\pi/4}^{\pi/2}=\sqrt{2}-1.
$$
:::
