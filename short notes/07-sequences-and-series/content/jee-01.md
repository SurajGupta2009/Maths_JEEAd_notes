---
id: jee-01
part: jee
title: "Sequences and Series — Arithmetic Progressions: Add the Same Amount Every Time"
---

## Definitions and the two formulas

A **sequence** is an ordered list $a_{1}, a_{2}, \ldots$; a **series** is a sum of its terms. $S_{n}$ always means $a_{1} + \cdots + a_{n}$. A sequence is an **arithmetic progression (AP)** when consecutive differences are constant: $a_{n+1} - a_{n} = d$ for all $n$.

:::derive title="The AP formulas from pairing the ends"
$a_{n} = a + (n - 1)d$ by adding $d$ exactly $n - 1$ times. For the sum, write $S_{n}$ forwards and backwards and add: each of the $n$ column pairs totals $a + \ell$ (first + last), so

$$S_{n} = \frac{n}{2}\left(2a + (n - 1)d\right) = \frac{n}{2}(a + \ell)$$

The second form is "number of terms × average of first and last" — and it is also $n \times$ (middle term) when $n$ is odd.
:::

:::example title="Worked — AP basics"
AP $2, 5, 8, \ldots$: $a_{20} = 2 + 19 \cdot 3 = 59$; $S_{20} = \frac{20}{2}(2 + 59) = 610$. Sum of first 20 positive even integers: $2 \cdot \frac{20 \cdot 21}{2} = 420$.

**Means:** three numbers in AP iff the middle is the average: $2b = a + c$. Insert 3 arithmetic means between 2 and 14: $d = \frac{14 - 2}{3 + 1} = 3$, means $5, 8, 11$.
:::

:::key title="AP facts that win marks"
- $a_{m} + a_{n} = a_{p} + a_{q}$ whenever $m + n = p + q$ (indices trade against each other). In particular terms equidistant from the ends sum to $a + \ell$.
- $S_{n}$ is a quadratic in $n$ with zero constant term: $S_{n} = \frac{d}{2}n^{2} + \left(a - \frac{d}{2}\right)n$. Conversely any such quadratic is an AP sum, recovered by $a_{n} = S_{n} - S_{n-1}$.
- Three terms in AP: write $a - d, a, a + d$; four terms: $a - 3d, a - d, a + d, a + 3d$ (common difference $2d$) — symmetric parametrisation kills the linear term.
- If $a, b, c$ in AP then $b$ is the **arithmetic mean** of $a, c$: $A = \frac{a + c}{2}$.
:::

:::warn title="Common traps — AP"
- Inserting $k$ means creates $k + 1$ gaps: $d = \frac{b - a}{k + 1}$, not $\frac{b - a}{k}$.
- $S_{n} = \frac{n}{2}(a + \ell)$ needs $\ell$ to be genuinely the $n$-th term — confirm the term count first ("sum of terms from 5th to 20th" has 16 terms).
- Given $S_{n}$ as a formula, $a_{1} = S_{1}$, not "$S_{n} - S_{n-1}$ at $n = 1$".
:::

:::diagram
{"type": "graph", "xrange": [0, 11], "yrange": [0, 34], "xticks": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "yticks": [0, 10, 20, 30], "xlabel": "n", "ylabel": "term", "curves": [{"expr": "3*x - 1", "from": 1, "to": 10, "color": "#16295C", "label": "AP: aₙ = 2+3(n−1) — a straight line", "labpos": 0.25}], "points": [{"x": 1, "y": 2, "label": "a₁=2"}, {"x": 10, "y": 29, "label": "a₁₀=29"}], "title": "An AP plotted against n is linear: slope = d", "ratio": 0.55}
:::
