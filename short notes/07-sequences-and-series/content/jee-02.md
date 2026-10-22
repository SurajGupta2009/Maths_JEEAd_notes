---
id: jee-02
part: jee
title: "Geometric Progressions — Multiply by the Same Amount, and the Infinite Sum"
---

## Definitions and the shift-and-subtract proof

A **geometric progression (GP)** has constant ratio $\frac{a_{n+1}}{a_{n}} = r$ (terms assumed nonzero for the ratio definition). Hence $a_{n} = ar^{n - 1}$.

:::derive title="The GP sum — the trick the whole chapter reuses"
Write $S_{n} = a + ar + \cdots + ar^{n - 1}$ and $rS_{n} = ar + \cdots + ar^{n}$. Subtract: everything telescopes except the ends, $(1 - r)S_{n} = a(1 - r^{n})$, so for $r \neq 1$

$$S_{n} = \frac{a(r^{n} - 1)}{r - 1} = \frac{a(1 - r^{n})}{1 - r}$$

(both forms identical; pick the one avoiding negatives). If $\left|r\right| < 1$ then $r^{n} \to 0$ and

$$S_{\infty} = \frac{a}{1 - r} \qquad \left(\left|r\right| < 1 \text{ only}\right)$$
:::

:::example title="Worked — GP basics"
GP $3, 6, 12, \ldots$: $a_{10} = 3 \cdot 2^{9} = 1536$; $S_{10} = 3(2^{10} - 1) = 3069$. Infinite: $1 + \frac{1}{2} + \frac{1}{4} + \cdots = \frac{1}{1 - 1/2} = 2$ (partial sum after 10 terms $1.9980$ ✓).

**Means:** insert 3 geometric means between 1 and 81: $r = \left(\frac{81}{1}\right)^{1/4} = 3$, means $3, 9, 27$. Geometric mean of $2, 8, 32$ is $(2 \cdot 8 \cdot 32)^{1/3} = 8$.
:::

:::key title="GP facts that win marks"
- $a_{m}a_{n} = a_{p}a_{q}$ whenever $m + n = p + q$; terms equidistant from the ends have constant product $a \cdot \ell$.
- Three terms in GP: $\frac{a}{r}, a, ar$; four terms: $\frac{a}{r^{3}}, \frac{a}{r}, ar, ar^{3}$.
- Every term (except possibly signs) satisfies $a_{n}^{2} = a_{n-1}a_{n+1}$: $a, b, c$ in GP iff $b^{2} = ac$.
- If each term of a GP is multiplied by a constant, raised to a power, or reciprocated, the result is still a GP (ratio $r$, $r^{k}$, $\frac{1}{r}$ respectively). Products/quotients of two GPs are GPs.
- A GP with $r > 0$ has all terms of one sign; $r < 0$ alternates. Log of a positive GP is an AP — the bridge between the two progressions.
:::

:::key title="The geometric mean and AM–GM (two positive numbers)"
$G = \sqrt{ab}$ is defined by $a, G, b$ in GP. For $a, b > 0$: $\frac{a + b}{2} \geq \sqrt{ab}$, equality iff $a = b$ — because it rearranges to $(\sqrt{a} - \sqrt{b})^{2} \geq 0$. AM–GM is examined in depth on sheet 03.
:::

:::warn title="Common traps — GP"
- $S_{\infty}$ used when $\left|r\right| \geq 1$: the partial sums do not converge; there is no finite sum. At $r = 1$, $S_{n} = na$; at $r = -1$ the sums oscillate.
- Sign chaos from mixing $\frac{a(r^{n} - 1)}{r - 1}$ and $\frac{a(1 - r^{n})}{1 - r}$ mid-line.
- Inserting $k$ geometric means: the exponent is $\frac{1}{k + 1}$, and for even roots with negative $\frac{b}{a}$ there may be no real $r$.
- $a_{n} = ar^{n-1}$: the exponent is $n - 1$, not $n$.
:::

:::diagram
{"type": "graph", "xrange": [0, 8.4], "yrange": [0, 7.4], "xticks": [0, 1, 2, 3, 4, 5, 6, 7, 8], "yticks": [0, 2, 4, 6], "xlabel": "n", "ylabel": "partial sum", "curves": [{"expr": "2 - 2*(0.5)**x", "from": 0, "to": 8, "color": "#16295C", "label": "Sₙ of 1 + 1/2 + 1/4 + ⋯ → 2", "labpos": 0.4}, {"expr": "0*x + 2", "from": 0, "to": 8, "color": "#B91C1C", "ls": "--", "label": "S∞ = a/(1−r) = 2", "labpos": 0.85}], "points": [{"x": 1, "y": 1, "label": "S₁=1"}, {"x": 3, "y": 1.75, "label": "S₃=1.75"}], "title": "Infinite GP: partial sums approach a/(1−r) when |r|<1", "ratio": 0.55}
:::
