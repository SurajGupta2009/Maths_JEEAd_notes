---
id: jee-90
part: jee
title: "Visual Probability and Statistics Lab — Trees, Distributions and Spread"
---

## A probability tree multiplies along a path

A bag has three red and two blue balls. Draw two without replacement. Along a path, multiply conditional probabilities; across disjoint paths with the same desired property, add.

:::diagram
{
  "type": "tree",
  "title": "Two draws without replacement",
  "ratio": 0.72, "node_width": 1.65,
  "nodes": [
    {"id": "s", "at": [0, 3], "label": "5 balls"},
    {"id": "r", "at": [-2, 1.6], "label": "red first"}, {"id": "b", "at": [2, 1.6], "label": "blue first"},
    {"id": "rr", "at": [-3, 0], "label": "RR"}, {"id": "rb", "at": [-1, 0], "label": "RB"},
    {"id": "br", "at": [1, 0], "label": "BR"}, {"id": "bb", "at": [3, 0], "label": "BB"}
  ],
  "edges": [
    {"from": "s", "to": "r", "label": "3/5"}, {"from": "s", "to": "b", "label": "2/5"},
    {"from": "r", "to": "rr", "label": "2/4"}, {"from": "r", "to": "rb", "label": "2/4"},
    {"from": "b", "to": "br", "label": "3/4"}, {"from": "b", "to": "bb", "label": "1/4"}
  ],
  "caption": "The second probabilities use four remaining balls. P(same colour) = (3/5)(2/4) + (2/5)(1/4) = 2/5. All four path probabilities sum to 1."
}
:::

If the first ball is replaced, the second-stage denominators return to $5$ and the draws become independent. The sampling rule changes the tree, so it must be read before any probability is assigned.

<!-- pagebreak -->
## A distribution lists every value and its probability

For $X\sim\operatorname{Binomial}(4,1/2)$, $P(X=k)=\binom{4}{k}/16$. The probabilities sum to $1$, the mean is $np=2$, and the variance is $np(1-p)=1$.

:::diagram
{
  "type": "bars",
  "title": "Binomial distribution with n = 4 and p = 1/2",
  "labels": ["0", "1", "2", "3", "4"],
  "values": [0.0625, 0.25, 0.375, 0.25, 0.0625], "value_format": "{:.4f}",
  "xlabel": "number of successes k", "ylabel": "P(X = k)",
  "caption": "Symmetry about k = 2 reflects p = 1/2. The probabilities are 1/16, 4/16, 6/16, 4/16, 1/16 and sum to 1."
}
:::

The binomial model requires a fixed number of independent trials, the same success probability on each trial, and exactly two outcomes per trial. Without replacement from a small population, these conditions fail and a hypergeometric model is usually appropriate.

<!-- pagebreak -->
## Mean locates; variance measures squared spread

For the data $2,4,4,4,5,5,7,9$, the mean is $5$ and the population variance is $4$. Deviations from the mean sum to zero, but squared deviations do not cancel.

:::diagram
{
  "type": "bars",
  "title": "Frequencies of the eight observations",
  "labels": ["2", "4", "5", "7", "9"], "values": [1, 3, 2, 1, 1],
  "xlabel": "observed value", "ylabel": "frequency",
  "caption": "The total frequency is 8 and the weighted sum is 40, so the mean is 5. The squared-deviation total is 32, giving population variance 32/8 = 4."
}
:::

:::diagram
{
  "type": "numberline",
  "title": "The mean is a balance point, not necessarily an observation",
  "range": [1, 10], "ticks": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "items": [
    {"kind": "points", "xs": [2, 4, 5, 7, 9], "label": "observed values (4 and 5 repeat)", "label_x": 5.5, "label_y": 0.95},
    {"kind": "points", "xs": [5], "label": "mean = 5", "label_x": 5, "label_y": -1.0, "y": 0.0, "color": "#B91C1C"}
  ],
  "caption": "Positive and negative deviations from 5 cancel. Variance instead averages their squares; standard deviation returns that squared-spread measure to the original units."
}
:::

For a sample variance with denominator $n-1$, state that convention explicitly. Do not mix population and sample formulas in one calculation.

<!-- pagebreak -->
## One workflow for probability and statistics

:::diagram
{
  "type": "flow",
  "title": "Model, calculate, then check the units and total",
  "steps": [
    {"title": "Define the experiment or data convention", "detail": "State replacement, independence, trial count, grouping, and whether variance is population or sample."},
    {"title": "Draw the structure", "detail": "Use a tree for conditional stages, a distribution for random values, and a spread picture for numerical data."},
    {"title": "Apply the matching formula", "detail": "Multiply along paths, add disjoint paths, use np and np(1-p) only for binomial models, and weight grouped values."},
    {"title": "Run consistency checks", "detail": "Probabilities must be in [0,1] and sum to 1; variance is nonnegative; standard deviation has the data's units."}
  ],
  "caption": "A numerical answer is credible only when its model assumptions and units are also correct. The picture makes those assumptions easier to audit."
}
:::

:::key title="Two checks that catch many errors"
For any discrete distribution, recompute $\sum p_i=1$ and $\sum x_i p_i$ for the mean. For any data set, verify that shifting every value by a constant leaves variance unchanged but shifts the mean by the same constant.
:::
