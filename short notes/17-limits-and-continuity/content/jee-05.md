---
id: jee-05
part: jee
title: "Limits at Infinity, Growth and Asymptotes"
---

## At infinity, divide by the dominant power

For a rational function, equal highest degrees give the ratio of leading coefficients. Lower-degree terms disappear after division.

:::example title="Normalize numerator and denominator by the same power"
$$
\frac{3x^2-x+4}{2x^2+5}
=\frac{3-1/x+4/x^2}{2+5/x^2}
\longrightarrow\frac{3}{2}
\qquad(x\to\infty).
$$
Dividing by $x$ instead of $x^2$ would leave a more complicated expression; choose the highest power present in the denominator after comparing degrees.
:::

## Growth hierarchies settle many apparent infinities

For fixed $p>0$ and $a>1$,
$$
\ln x\ll x^p\ll a^x
\qquad\text{as }x\to\infty.
$$
In particular, $\ln x/x\to0$ and $x/e^x\to0$. These are not products of separate finite limits: they result from the relative growth of the numerator and denominator.

## Limits define three kinds of asymptote

- **Horizontal:** $f(x)\to L$ as $x\to\infty$ or $x\to-\infty$ gives $y=L$ on that side.
- **Vertical:** a one-sided infinite approach at finite $x=a$ gives $x=a$.
- **Oblique:** $f(x)-(mx+b)\to0$ gives $y=mx+b$, with $m\ne0$.

:::example title="Read a hyperbola from two limits"
For
$$
f(x)=\frac{2x+1}{x-3}=2+\frac{7}{x-3}\qquad(x\ne3),
$$
$f(x)\to2$ as $x\to\pm\infty$, so $y=2$ is horizontal. The residual term is unbounded near $x=3$, so $x=3$ is vertical.
:::

:::diagram
{
  "type": "graph",
  "title": "The decomposition 2 + 7/(x-3) explains both asymptotes",
  "xrange": [-4, 8], "yrange": [-8, 10],
  "curves": [
    {"expr": "(2*x+1)/(x-3)", "from": -4, "to": 2.9, "clip": 11, "label": "left branch", "labpos": 0.20, "label_dy": 0.5},
    {"expr": "(2*x+1)/(x-3)", "from": 3.1, "to": 8, "clip": 11, "label": "right branch", "labpos": 0.78, "label_dy": 0.5}
  ],
  "hlines": [{"y": 2, "label": "y = 2"}],
  "vlines": [{"x": 3, "label": "x = 3", "dx": 0.25}],
  "points": [{"x": 4, "y": 9, "label": "(4,9)", "dx": 0.2, "dy": -0.8}, {"x": 0, "y": -0.333333, "label": "(0,-1/3)", "dx": 0.2, "dy": -0.7}],
  "caption": "Large x makes 7/(x-3) vanish, while x near 3 makes it unbounded. The two branches must be checked separately near the excluded point."
}
:::

:::warn title="A cancelled factor makes a hole, not a vertical asymptote"
For
$$
\frac{x+2}{x^2-x-6}=\frac{x+2}{(x-3)(x+2)}=\frac{1}{x-3}\qquad(x\ne3,-2),
$$
there is a removable hole at $x=-2$ and a vertical asymptote only at $x=3$. Always factor before declaring every denominator zero a pole.
:::
