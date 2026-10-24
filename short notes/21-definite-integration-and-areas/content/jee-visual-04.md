---
id: jee-visual-04
part: jee
title: "Visual Lab 4 — An Infinite Tail with Finite Area"
---

## The tail continues forever but shrinks exponentially

:::diagram
{
  "type": "graph",
  "title": "The exponential area on [0,infinity) equals one",
  "xrange": [-0.15, 5.15], "yrange": [-0.06, 1.10],
  "xticks": [0, 1, 2, 3, 4, 5], "yticks": [0, 0.5, 1],
  "fills": [
    {"from": 0, "to": 2, "y1": 0, "y2": "exp(-x)", "color": "#F6C445", "alpha": 0.32},
    {"from": 2, "to": 5, "y1": 0, "y2": "exp(-x)", "color": "#0F6B5C", "alpha": 0.20}
  ],
  "curves": [{"expr": "exp(-x)", "from": 0, "to": 5}],
  "points": [
    {"x": 2, "y": 0.1353352832, "label": "x=2", "dx": 0.15, "dy": 0.10}
  ],
  "caption": "The gold area on [0,2] is 1-exp(-2)=0.8646647. The entire tail beyond 2 has area exp(-2)=0.1353353; only its portion up to 5 is visible."
}
:::

## Facts to retain

- $\int_0^2e^{-x}dx=1-e^{-2}$, while $\int_2^\infty e^{-x}dx=e^{-2}$.
- The two contributions add to $1$, exactly matching $\int_0^\infty e^{-x}dx$.
- A finite plotting window illustrates a tail but does not replace the limit $R\to\infty$.

:::example title="Check tail additivity"
For any $R>2$,
$$
\int_0^2e^{-x}dx+\int_2^Re^{-x}dx=1-e^{-R}.
$$
Taking $R\to\infty$ gives $(1-e^{-2})+e^{-2}=1$.
:::
