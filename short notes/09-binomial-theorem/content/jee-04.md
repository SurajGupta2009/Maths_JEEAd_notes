---
id: jee-04
part: jee
title: "Greatest Terms, Truncation Inequalities, and the Binomial as a Sieve"
---

## The ratio walk to the greatest term

:::key title="Greatest term of (a + bx)ⁿ at a given x"
For terms $t_{k} = \binom{n}{k} a^{n - k} (bx)^{k}$, walk the ratio $\frac{t_{k + 1}}{t_{k}} = \frac{n - k}{k + 1} \cdot \left|\frac{bx}{a}\right|$ until it crosses 1. Greatest term of $(2 + 3x)^{8}$ at $x = 1$: ratio $\frac{8 - k}{k + 1} \cdot \frac{3}{2} \geq 1$ iff $k \leq 4.4$, so terms rise through $t_{5}$ and fall after: $T_{6} = \binom{8}{5} 2^{3} 3^{5} = 108864$ (neighbours $90720$, $81648$ ✓). Use absolute values: "numerically greatest" means largest $\left|t_{k}\right|$.
:::

:::key title="Truncation: positivity turns expansions into inequalities"
For $x \geq 0$ every term of $(1 + x)^{n}$ is non-negative, so any partial sum is a lower bound. Keeping $k \leq 1$: **Bernoulli** $(1 + x)^{n} \geq 1 + nx$; keeping $k \leq 2$ sharpens it by $\frac{n(n - 1)}{2}x^{2}$. Bernoulli in fact holds for all $x > -1$ (induction proof — the truncation argument alone covers only $x \geq 0$ since odd terms flip sign).

The same term comparison traps $\left(1 + \frac{1}{n}\right)^{n}$: its $k$-th term is $\frac{1}{k!}\prod\left(1 - \frac{j}{n}\right) \leq \frac{1}{k!} \leq \frac{1}{2^{k - 1}}$, giving $2 \leq \left(1 + \frac{1}{n}\right)^{n} \leq 3$ — $e$ appears as the pinched limit.
:::

:::key title="Remainders and last digits: expand around the modulus"
To compute $A^{n}$ modulo $m$: write $A$ as (multiple of $m$) $\pm$ small residue and expand — all terms carrying the multiple vanish mod $m$ except the last few. Last digit of $7^{20} = 49^{10} = (50 - 1)^{10}$: every term except $(-1)^{10}$ carries a factor 50 (the $j = 1$ term is $-500 \equiv 0$ mod 100), so last digit $1$. Similarly $6^{999} + 1 \equiv 1 + 1 = 2 \ (	ext{mod } 5)$ since $6 \equiv 1 \ (	ext{mod } 5)$.
:::

:::key title="Conjugate surds: integer parts without decimals"
$(1 + \sqrt{2})^{n} + (1 - \sqrt{2})^{n} = 2\sum_{j} \binom{n}{2j} 2^{j}$ is an integer (odd $\sqrt{2}$ powers cancel by the binomial theorem itself), and $\left|1 - \sqrt{2}\right| < 1$ leaves only dust. For odd $n$ the dust is negative, so the integer part of $(1 + \sqrt{2})^{n}$ is that integer: $(1 + \sqrt{2})^{3}$ has conjugate sum $2(1 + 6) = 14$, and integer part $14$ (even, for every odd exponent). For even $n$ the dust is positive and the integer part is the conjugate sum minus 1 (odd).
:::

:::warn title="Common traps — size questions"
- Truncation claimed for negative $x$ without the induction form of Bernoulli.
- Ratio walk without absolute values when terms alternate in sign.
- Modular truncation treated as approximation: it is exact in residue classes — but every dropped term must genuinely carry the modulus factor.
:::
