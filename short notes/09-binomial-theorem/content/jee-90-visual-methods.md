---
id: jee-90
part: jee
title: "Visual Binomial Lab — Pascal Rows, Term Tracking and Greatest Terms"
---

## Pascal's triangle is a recurrence, not just a table

The identity $\binom{n+1}{k}=\binom{n}{k-1}+\binom{n}{k}$ says that choosing $k$ objects from $n+1$ either excludes a marked object or includes it. Each interior Pascal entry is therefore the sum of the two entries above it.

:::diagram
{
  "type": "pascal",
  "rows": 7, "highlight": [[5, 2], [5, 3], [6, 3]],
  "title": "Two parents create each interior coefficient",
  "caption": "The highlighted 10 + 10 = 20 shows C(6,3) = C(5,2) + C(5,3). Row n contains n + 1 entries indexed by k = 0 through n."
}
:::

Row sums satisfy $\sum_{k=0}^n\binom{n}{k}=(1+1)^n=2^n$. Alternating row sums vanish for $n\geq1$ because $(1-1)^n=0$. Both are substitutions in the same expansion, not unrelated identities.

<!-- pagebreak -->
## Track every factor in the general term

For $(a+b)^n$, $T_{k+1}=\binom{n}{k} a^{n-k}b^k$. The term index is $k+1$, while the binomial lower index and the exponent of $b$ are both $k$.

:::diagram
{
  "type": "table",
  "title": "Term tracking for (2 + 3x)^4",
  "columns": ["k", "C(4,k)", "power of 2", "power of 3x", "complete term"],
  "rows": [
    ["0", "1", "2^4", "(3x)^0", "16"],
    ["1", "4", "2^3", "(3x)^1", "96x"],
    ["2", "6", "2^2", "(3x)^2", "216x^2"],
    ["3", "4", "2^1", "(3x)^3", "216x^3"],
    ["4", "1", "2^0", "(3x)^4", "81x^4"]
  ],
  "caption": "The coefficients include the numerical factors inside a and b. Binomial coefficients alone would give 1, 4, 6, 4, 1 and would not answer the coefficient question."
}
:::

For a specified power $x^r$ in $(p+qx^m)^n$, solve the exponent equation first and check that the resulting $k$ is an integer between $0$ and $n$. Only then calculate the coefficient.

<!-- pagebreak -->
## Greatest numerical terms come from consecutive ratios

For $(2+3x)^8$ at $x=1$, write $t_k=\binom{8}{k}2^{8-k}3^k\geq0$. Then
$$
\frac{t_{k+1}}{t_k}=\frac{8-k}{k+1}\cdot\frac{3}{2}.
$$
The terms increase while this ratio exceeds $1$ and decrease after it falls below $1$.

:::diagram
{
  "type": "bars",
  "title": "Numerical terms of (2 + 3)^8 peak at k = 5",
  "labels": ["k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"],
  "values": [256, 3072, 16128, 48384, 90720, 108864, 81648, 34992, 6561],
  "value_labels": false, "xlabel": "lower binomial index k", "ylabel": "term size",
  "caption": "The largest value is t5 = 108864. It is the sixth written term because the written index is k + 1. The total sum is 5^8 = 390625."
}
:::

:::example title="Check the peak directly"
The ratio exceeds $1$ exactly when $3(8-k)>2(k+1)$, or $k<22/5=4.4$. Thus $t_0<t_1<\cdots<t_5$, while $t_5>t_6>\cdots>t_8$. Direct evaluation gives $t_5=\binom{8}{5} 2^3 3^5=108864$.
:::

<!-- pagebreak -->
## Read the ratio across one

A graph of the ratio makes the turnover visible. It is a guide for locating the maximum, not a replacement for checking integer indices and endpoint terms.

:::diagram
{
  "type": "graph",
  "title": "The term ratio crosses 1 between k = 4 and k = 5",
  "xrange": [0, 7], "yrange": [0, 12], "xticks": [0, 1, 2, 3, 4, 5, 6, 7], "yticks": [0, 1, 3, 6, 9, 12],
  "curves": [{"expr": "1.5*(8-x)/(x+1)", "from": 0, "to": 7, "label": "t(k+1)/t(k)", "labpos": 0.36, "label_dy": 0.35}],
  "hlines": [{"y": 1, "label": "ratio = 1"}],
  "points": [{"x": 4, "y": 1.2, "label": "k=4: increase", "dx": -1.2, "dy": 0.4}, {"x": 5, "y": 0.75, "label": "k=5: decrease", "dx": 0.25, "dy": 1.0}],
  "caption": "Only integer k values represent actual ratios. Since the continuous guide crosses 1 at k = 4.4, the last increase is from t4 to t5 and the peak is t5."
}
:::

If terms can be negative, compare absolute values when “greatest numerical term” is requested. A greatest signed term and a term of greatest modulus are different questions.

<!-- pagebreak -->
## Choose the right binomial operation

:::diagram
{
  "type": "flow",
  "title": "Match the operation to the requested quantity",
  "steps": [
    {"title": "Need one term or coefficient?", "detail": "Write T(k + 1), solve the exponent equation, and check that k is an admissible integer."},
    {"title": "Need a coefficient sum?", "detail": "Substitute x = 1, -1 or another suitable value; use parity combinations when required."},
    {"title": "Need weighted sums such as k*C(n,k)?", "detail": "Differentiate or integrate the master expansion, then substitute; watch the new index limits."},
    {"title": "Need a greatest coefficient or term?", "detail": "Use consecutive ratios and include absolute values when numerical size, rather than signed value, is requested."}
  ],
  "caption": "Start from the same expansion and choose an operation matched to the question. This avoids memorising many disconnected identities."
}
:::

:::key title="Three final checks"
Check the term index, include numerical factors from both binomial inputs, and state the admissible range of $n,k,x$. For truncation estimates, also state which side of the target the partial sum approaches and why.
:::
