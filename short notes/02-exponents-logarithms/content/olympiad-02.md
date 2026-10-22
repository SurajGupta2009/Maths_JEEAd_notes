---
id: oly-02
part: olympiad
title: "Olympiad Extensions — Growth Hierarchy, Digits, Legendre's Formula"
---

## Status of this sheet

Order-of-magnitude estimates and Legendre's formula are **classic IOQM/RMO number theory** built from the Part I toolkit (logs, floors, geometric progressions). The hierarchy statements below are *comparisons between standard functions*, models derivable from supplied information — not additional theory claimed as a syllabus item.

## The growth hierarchy (state it as ordering, use it as a tool)

For fixed $a > 1$, $b > 1$, $c > 1$, $k \in \mathbb{N}$, as $x \to \infty$:

$$\log_{c} x \ \ll\ x \ \ll\ x^{k} \ \ll\ a^{x} \ \ll\ b^{b^{x}}.$$

**Use in estimates:** to compare $n^{\log n}$-shaped quantities, take $\log$ once or twice until everything is polynomial. Example: which is larger for huge $n$ — $100^{n}$ or $n^{100}$? Take $\ln$: $n \ln 100$ vs $100 \ln n$; divide by $n$: $\ln 100 \approx 4.605$ vs $\frac{100 \ln n}{n} \to 0$. So $100^{n}$ wins for large $n$: at $n = 100$ the two are **equal**, for $n > 100$ the exponential $100^{n}$ is larger, for $e < n < 100$ the power $n^{100}$ is larger (crossover where $\frac{\ln n}{n} = \frac{\ln 100}{100} = 0.046$).

:::key
**Digit-counting engine.** $d(N) = \lfloor \lg N \rfloor + 1$ for integers $N \geq 1$. Sums of digits in base $b$: $N = \sum d_i b^{i}$ with $0 \leq d_i < b$; the digit-sum $s_{b}(N) = \sum d_i$ satisfies $N - s_{b}(N)$ is divisible by $b - 1$ (casting out $b-1$'s). This pair ($\lfloor \log \rfloor$, digit sum) is exactly what Legendre's formula packages.
:::

## Legendre's formula — the exponent of a prime in $n!$

For prime $p$: $ v_{p}(n!) = \sum_{k=1}^{\infty} \left\lfloor \dfrac{n}{p^{k}} \right\rfloor = \dfrac{n - s_{p}(n)}{p - 1}$, where $s_{p}(n)$ is the digit sum of $n$ in base $p$ (finitely many non-zero terms: stop when $p^{k} > n$).

:::derive title="Derivation — count multiples, then clean up with digits"
Among $1, 2, \ldots, n$, exactly $\lfloor n/p \rfloor$ are divisible by $p$; among those, $\lfloor n/p^{2} \rfloor$ contribute a **second** factor $p$; and so on — each integer $m$ contributes $v_{p}(m)$ factors, so the total is $\sum_{k \geq 1} \lfloor n/p^{k} \rfloor$ ✓ (count each $m$ once per power of $p$ dividing it). For the closed form, write $n = s_{p}(n) + (p-1)\sum_{k \geq 1} \lfloor n/p^{k} \rfloor$ (base-$p$ identity: $\lfloor n/p^{k} \rfloor = \sum_{j>k} d_j p^{j-k-1}$), rearranged to the formula.
:::

:::example title="Worked. $v_{2}(100!)$ and $v_{5}(100!)$"
$v_{2}(100!) = 50 + 25 + 12 + 6 + 3 + 1 = 97$. Via digits: $100 = (1100100)_{2}$, $s_{2} = 3$, $\frac{100 - 3}{1} = 97$ ✓. $v_{5}(100!) = 20 + 4 = 24$; digits: $100 = (400)_{5}$, $s_{5} = 4$, $\frac{100 - 4}{4} = 24$ ✓. Consequence: $100!$ ends in exactly $24$ zeros (the power of $10 = 2 \cdot 5$ is the smaller of $v_{2}, v_{5}$).
:::

## Series estimates with logs and floors

**Truncation errors:** $ \sum_{k=1}^{n} \frac{1}{k}$ grows like $\ln n$ (harmonic estimate: $\ln(n+1) \leq H_{n} \leq 1 + \ln n$ — provable by comparing the sum with $\int \frac{dx}{x}$, a standard derived model). The telescoping estimate $\frac{1}{k+1} \leq \ln\!\left(1 + \frac{1}{k}\right) \leq \frac{1}{k}$ (from $\frac{1}{1+t} \leq \ln(1+t)$-style log bounds at $t = 1/k$) is the workhorse behind it.

:::example title="Worked. Bound $H_{100} = 1 + \frac{1}{2} + \cdots + \frac{1}{100}$"
$\ln 101 \approx 4.615 \leq H_{100} \leq 1 + \ln 100 \approx 5.605$; the true value is $\approx 5.187$ ✓ inside the bracket. Use such brackets to decide sign/size questions without computing sums.
:::

:::warn title="Traps on this sheet"
- $\lfloor n/p \rfloor + \lfloor n/p^{2} \rfloor + \cdots$ is **not** a geometric series — do not sum it as one; each term is a floor.
- Trailing zeros of $n!$ are $v_{5}(n!)$ (5s are rarer than 2s), not $v_{2}(n!)$.
- $\log$ estimates compare growth rates; a bound valid "for large $n$" must not be quoted for a specific small $n$ without checking (e.g. $n^{100} > 100^{n}$ fails for $n = 2$).
- Digit sums $s_{p}$ depend on the base; $s_{2}(100) = 3$ counts **ones in binary**, not decimal digits.
:::

## Assumptions & conventions

$p$ prime; $v_{p}(m)$ = exact exponent of $p$ in $m$; floors are real floors; harmonic estimates quoted as standard derived bounds (checked numerically above); hierarchy statements are eventual comparisons (there is always a crossover point).
