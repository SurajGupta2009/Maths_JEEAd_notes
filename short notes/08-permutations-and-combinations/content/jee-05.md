---
id: jee-05
part: jee
title: "Stars and Bars, Compositions, Multisets, and Bounded Distributions"
---

## Identical objects into distinct boxes

:::derive title="The stars-and-bars bijection"
Distributing $n$ **identical** balls into $k$ **distinct** boxes is the same data as a count tuple $(x_{1}, \ldots, x_{k})$, $x_{i} \geq 0$, $\sum x_{i} = n$ — and the same as a word of $n$ stars and $k - 1$ bars (stars for box 1, bar, stars for box 2, …). Choosing the bar positions among $n + k - 1$ symbols:

$$\binom{n + k - 1}{k - 1} \quad \text{(empty boxes allowed)}$$

$$\binom{n - 1}{k - 1} \quad \text{(every box} \geq 1\text{)}$$

The positive case: pre-place one ball in each box, distribute the remaining $n - k$ freely. Non-negative solutions of $x + y + z = 15$: $\binom{17}{2} = 136$; positive: $\binom{14}{2} = 91$ (difference $45 = 42 + 3$: exactly one zero $3 \cdot 14$, exactly two zeros $3$ ✓).
:::

:::key title="The same formula in four costumes"
- **Multisets:** choosing 12 fruits from 5 varieties (counts only): $\binom{12 + 5 - 1}{4} = \binom{16}{4} = 1820$.
- **Compositions:** ordered sums of $n$ into $k$ positive parts: $\binom{n - 1}{k - 1}$ (separators in the $n - 1$ gaps between unit blocks); any number of parts: $2^{n - 1}$. Ordered sums of 10 into parts $\geq 2$: shift $b_{i} = a_{i} - 1$, sum over the number of parts $k = 1..5$: $1 + 7 + 15 + 10 + 1 = 34$ (the $k = 1$ term is the single-part sum $[10]$ itself — easy to drop).
- **Non-negative solutions with lower bounds:** shift each variable down to 0 first.
- **Upper bounds:** complement/inclusion–exclusion: $x_{1} + x_{2} + x_{3} + x_{4} = 20$, $x_{1} \leq 5$: total $\binom{23}{3} = 1771$ minus ($x_{1} \geq 6$, shift) $\binom{17}{3} = 680$ gives $1091$.
:::

:::warn title="Common traps — stars and bars"
- Identical vs distinct balls: distinct balls into boxes is $k^{n}$ (functions), a completely different count. Read which objects are identical.
- Applying $\binom{n + k - 1}{k - 1}$ to *ordered compositions with positive parts* (that is $\binom{n - 1}{k - 1}$).
- Upper-bound problems with two violated bounds need genuine inclusion–exclusion, not one subtraction.
- Balls identical + boxes identical (partitions) has **no closed form** — Part II; do not invent one.
:::
