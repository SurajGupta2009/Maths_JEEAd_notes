---
id: jee-90
part: jee
title: "Visual Sequences Lab — Growth, Partial Sums and Cancellation"
---

## A sequence is a list; a series is a running total

For an arithmetic progression, the difference $a_{k+1}-a_k=d$ is constant. For a geometric progression, the ratio $a_{k+1}/a_k=r$ is constant when the terms are nonzero. Confusing these two invariants leads to the wrong general term.

:::diagram
{
  "type": "bars",
  "title": "Geometric growth accelerates when r > 1",
  "labels": ["a1", "a2", "a3", "a4", "a5", "a6"],
  "values": [1, 2, 4, 8, 16, 32],
  "xlabel": "term", "ylabel": "value",
  "caption": "For a_k = 2^(k-1), equal multiplicative steps produce increasingly large additive jumps. The sixth term is 32, while the sum of all six terms is 63."
}
:::

For the geometric progression above, $S_6=1(2^6-1)/(2-1)=63$. The formula for an infinite geometric sum applies only when $|r|<1$; this example has $r=2$, so no finite infinite-series sum exists.

<!-- pagebreak -->
## Partial sums reveal the arithmetic structure

For an AP with first term $a$ and difference $d$, $S_n=n(2a+(n-1)d)/2$. The factor $n$ counts terms, while $(a+a_n)/2$ is the average of the first and last terms.

:::diagram
{
  "type": "bars",
  "title": "Partial sums of 2, 3, 4, 5, 6",
  "labels": ["S1", "S2", "S3", "S4", "S5"],
  "values": [2, 5, 9, 14, 20], "colors": ["#0F766E", "#0F766E", "#B8860B", "#B8860B", "#16295C"],
  "xlabel": "number of terms added", "ylabel": "running total",
  "caption": "The increments S_n - S_(n-1) are exactly 2, 3, 4, 5, 6. Thus S5 = 20, and S5 - S4 = 6 recovers the fifth term rather than another partial sum."
}
:::

:::example title="Recover a term from two sums"
If $S_5=20$ and $S_4=14$, then $a_5=S_5-S_4=6$. Conversely, knowing only $S_5$ does not determine every term: many sequences can share one partial sum. Use consecutive sums to isolate a term.
:::

<!-- pagebreak -->
## AM–GM has a visible equality point

For positive $x$, $(x+1/x)/2\geq\sqrt{x\cdot1/x}=1$, so $x+1/x\geq2$. Equality requires $x=1/x$, hence $x=1$ because $x>0$.

:::diagram
{
  "type": "graph",
  "title": "A visible AM-GM special case: x + 1/x >= 2 for x > 0",
  "xrange": [0, 4], "yrange": [0, 6],
  "curves": [{"expr": "x+1/x", "from": 0.2, "to": 4, "label": "x + 1/x", "labpos": 0.82}],
  "hlines": [{"y": 2, "label": "minimum 2"}],
  "points": [{"x": 1, "y": 2, "label": "equality at x = 1", "dx": 0.2, "dy": 0.25}],
  "caption": "For positive x, AM-GM gives (x + 1/x)/2 >= sqrt(x * 1/x) = 1. The graph touches the equality line only at x = 1."
}
:::

When using AM–GM in an optimisation problem, write the equality condition immediately. A lower bound that cannot be attained does not establish a minimum. For example, after obtaining an expression $\geq4$, still find the admissible variable value that makes all the AM–GM inputs equal.

<!-- pagebreak -->
## Telescoping means preserving the uncancelled boundary

A telescoping sum is not just “everything cancels”. Write at least the first two and last two indexed terms so that the surviving terms are visible.

:::example title="Cancellation with a surviving boundary"
For $a_k=1/k-1/(k+1)$,
$$
S_n=\left(1-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\cdots+\left(\frac{1}{n}-\frac{1}{n+1}\right)=1-\frac{1}{n+1}.
$$
The intermediate terms cancel, but $1$ and $-1/(n+1)$ remain. As $n\to\infty$, $S_n\to1$.
:::

:::diagram
{
  "type": "flow",
  "title": "A summation method chooser",
  "steps": [
    {"title": "Identify the term structure", "detail": "Constant difference suggests AP; constant ratio suggests GP; a difference suggests telescoping."},
    {"title": "Write indexed terms", "detail": "Show the first two and last two terms so limits, shifts and surviving boundaries are explicit."},
    {"title": "Apply the matching sum engine", "detail": "Use AP averaging, finite GP ratio, differences, or coefficient extraction only under its hypotheses."},
    {"title": "Check by small n", "detail": "Compute n = 1 and n = 2 directly. A shifted index or wrong term count usually fails immediately."}
  ],
  "caption": "For the telescoping example, n = 1 gives S1 = 1/2 and the closed form gives 1 - 1/2. The small-n check confirms the boundary before limits are taken."
}
:::

:::key title="Separate finite formulas from limit statements"
A finite partial sum can be valid for every $n$ even when the infinite series diverges. State the formula, its admissible ratio or index range, and the limit separately.
:::
