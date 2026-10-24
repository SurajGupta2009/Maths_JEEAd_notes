---
id: jee-visual-03
part: jee
title: "Visual Lab 3 — Parabolas Meeting Ellipses at Right Angles"
---

## Two editable families recreate the orthogonal-trajectory figure

:::diagram
{
  "type": "graph",
  "title": "Parabolas y = c x^2 and ellipses x^2 + 2y^2 = C",
  "xrange": [-3.4, 3.4], "yrange": [-2.5, 4.1],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-2, -1, 0, 1, 2, 3, 4],
  "curves": [
    {"expr": "0.25*x**2", "from": -3.4, "to": 3.4, "color": "#16295C", "lw": 2.4},
    {"expr": "0.5*x**2", "from": -2.75, "to": 2.75, "color": "#16295C", "lw": 2.0, "ls": "--"},
    {"expr": "sqrt((4-x**2)/2)", "from": -2, "to": 2, "color": "#0F766E", "lw": 2.8},
    {"expr": "-sqrt((4-x**2)/2)", "from": -2, "to": 2, "color": "#0F766E", "lw": 2.8},
    {"expr": "sqrt((9-x**2)/2)", "from": -3, "to": 3, "color": "#0F766E", "lw": 2.2, "ls": "--"},
    {"expr": "-sqrt((9-x**2)/2)", "from": -3, "to": 3, "color": "#0F766E", "lw": 2.2, "ls": "--"}
  ],
  "points": [{"x": 1.7111993543, "y": 0.7320508076, "label": "perpendicular", "dx": 0.12, "dy": 0.12}],
  "caption": "Navy curves are the original parabolas; teal curves are their orthogonal ellipses. Upper and lower ellipse branches are plotted separately so every equation remains editable and explicit."
}
:::

## Check the marked intersection exactly

The marked point lies on $y=x^2/4$ and $x^2+2y^2=4$. Put $u=x^2$. Substitution gives
$$
u+\frac{u^2}{8}=4
\quad\Longrightarrow\quad u=4\sqrt{3}-4.
$$
At that point, the parabola slope is $x/2$, while implicit differentiation of the ellipse gives slope $-x/(2y)$. Their product is
$$
\frac{x}{2}\cdot\left(-\frac{x}{2y}\right)
=-\frac{x^2}{4y}=-1
$$
because $y=x^2/4$ and $x\neq0$.

:::warn title="Do not infer orthogonality from a drawing"
The product-of-slopes calculation, supplemented by vertical/horizontal direction checks, is the proof. The figure only makes the two families easier to understand.
:::
