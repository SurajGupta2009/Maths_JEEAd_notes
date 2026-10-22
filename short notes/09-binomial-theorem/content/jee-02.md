---
id: jee-02
part: jee
title: "Coefficient Machinery — Multinomials, Counting Terms, Greatest Coefficients"
---

## Beyond two outcomes per bracket

:::key title="Multinomial coefficients"
In $(x_{1} + \cdots + x_{r})^{n}$, the coefficient of $x_{1}^{n_{1}} \cdots x_{r}^{n_{r}}$ ($\sum n_{i} = n$) is $\frac{n!}{n_{1}! \cdots n_{r}!}$: line up the brackets, mark which gave each outcome. Number of raw products for $(a + b + c)^{6}$: $3^{6} = 729$; collected terms (exponent tuples, stars and bars): $\binom{6 + 2}{2} = 28$. Coefficient of $a^{2}b^{2}c^{2}$ in $(a + b + c)^{6}$: $\frac{6!}{2!\,2!\,2!} = 90$.

Coefficient of $x^{3}$ in $(1 + x + x^{2})^{4}$ by census: patterns $\{x^{2}, x, 1, 1\}$ in $\frac{4!}{1!\,1!\,2!} = 12$ ways and $\{x, x, x, 1\}$ in $\frac{4!}{3!\,1!} = 4$ ways: total $16$ (matches $(1 + x + x^{2})^{4} = 1 + 4x + 10x^{2} + 16x^{3} + 19x^{4} + \cdots$ ✓).
:::

:::warn title="Number-of-terms trap"
"Terms in $(1 + x + x^{2})^{n}$" is **not** $\binom{n + 2}{2}$: collecting in the single variable $x$ collapses to powers $x^{0}, \ldots, x^{2n}$ — exactly $2n + 1$ terms. Always ask: collected in which variables?
:::

:::key title="Where coefficients peak"
$\frac{\binom{n}{k + 1}}{\binom{n}{k}} = \frac{n - k}{k + 1}$ passes 1 at $k = \frac{n - 1}{2}$. So row $n$: $n$ even $\Rightarrow$ single peak $\binom{n}{n/2}$; $n$ odd $\Rightarrow$ twin peaks $\binom{n}{(n - 1)/2} = \binom{n}{(n + 1)/2}$ (for $(1 + x)^{13}$: $1716$ at $x^{6}, x^{7}$; for $(1 + x)^{21}$: $352716$ at $k = 10, 11$). Coefficient of $x^{5}$ in $(1 + x)^{12}$ is $\binom{12}{5} = 792$, and of $x^{7}$ also $792$ by symmetry.
:::

:::key title="Substitution engine — coefficient sums without expanding"
For $f(x) = (px + q)^{n}$ expanded: sum of coefficients $= f(1) = (p + q)^{n}$; constant term $= f(0) = q^{n}$; alternating sum $= f(-1)$ splits even/odd powers. Sum of coefficients of $(2x - 1)^{7}$ is $(2 - 1)^{7} = 1$; of $(x - 2y)^{9}$ (set $x = y = 1$): $(-1)^{9} = -1$ — negative answers are legal. Odd-power coefficients of $(1 + x)^{12}$: $\frac{f(1) - f(-1)}{2} = 2^{11} = 2048$.
:::

:::example title="Worked — coefficient extraction across factors"
Coefficient of $x^{8}$ in $(1 + x)^{10}\left(1 + \frac{1}{x}\right)^{12}$: write the second factor as $x^{-12}(1 + x)^{12}$; the product is $x^{-12}(1 + x)^{22}$; need $x^{20}$: $\binom{22}{20} = 231$. Always clear negative powers into an $x^{-m}$ prefactor first.
:::
