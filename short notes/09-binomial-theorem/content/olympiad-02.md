---
id: olympiad-02
part: olympiad
title: "Extension — Divisibility, Prime Rows, Lucas, and Finite Differences"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Modular properties of binomial coefficients (Lucas, Kummer, prime rows) are Olympiad number theory built on the Part I census.
:::

:::key title="Prime rows and the Freshman's dream"
For prime $p$ and $0 < k < p$: $p \mid \binom{p}{k}$ (the numerator carries $p$, the denominator cannot cancel it). Hence in characteristic $p$,

$$(a + b)^{p} \equiv a^{p} + b^{p} \ (	ext{mod } p)$$

and iterating, $(a + b)^{p^{m}} \equiv a^{p^{m}} + b^{p^{m}} \ (	ext{mod } p)$. Row $p$ of Pascal's triangle mod $p$ is $1, 0, 0, \ldots, 0, 1$ — brute-force verified for all primes $\leq 47$ in math_checks.
:::

:::key title="Lucas's theorem (statement and use)"
Write $n, k$ in base $p$: $n = \sum n_{i} p^{i}$, $k = \sum k_{i} p^{i}$. Then $\binom{n}{k} \equiv \prod_{i} \binom{n_{i}}{k_{i}} \ (	ext{mod } p)$ (with $\binom{n_{i}}{k_{i}} = 0$ if $k_{i} > n_{i}$). Consequence: $\binom{n}{k}$ is **odd** iff every binary digit of $k$ is $\leq$ that of $n$ ($k$ is a submask of $n$) — so row $n$ contains exactly $2^{(\text{number of 1 bits in } n)}$ odd entries. Kummer (statement): the exponent of $p$ in $\binom{n}{k}$ equals the number of carries when adding $k$ and $n - k$ in base $p$.
:::

:::key title="Finite differences annihilate polynomials"
The $n$-th forward difference of a degree-$n$ polynomial is the constant $n! \times$ (leading coefficient): $\sum_{k=0}^{n} (-1)^{n - k}\binom{n}{k} P(x + k) = n! \times [\text{leading coeff}]$. For $P(x) = x^{n}$: $\sum_{k} (-1)^{k}\binom{n}{k}(x + k)^{n} = (-1)^{n} n!$, independent of $x$ — a pure binomial-theorem telescoping, checked numerically in math_checks.
:::

:::warn title="Common traps — modular binomials"
- $(a + b)^{p} \equiv a^{p} + b^{p}$ is modulo $p$ (or in characteristic $p$) — never an integer equality.
- Lucas needs base-$p$ digits of **both** $n$ and $k$ aligned; a single digit $k_{i} > n_{i}$ kills the coefficient mod $p$.
- $\binom{p}{k}$ divisible by $p$ requires $0 < k < p$ strictly; endpoints are 1.
:::
