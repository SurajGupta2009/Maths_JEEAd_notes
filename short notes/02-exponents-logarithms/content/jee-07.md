---
id: jee-07
part: jee
title: "Chapter Recap — Exponents & Logarithms Toolkit"
---

## The whole toolkit on one sheet

**Exponents ($a > 0$ convention).** $a^{r}a^{s} = a^{r+s}$; $(a^{r})^{s} = a^{rs}$ (needs $a > 0$); $(ab)^{r} = a^{r}b^{r}$ (needs $a,b > 0$); $a^{-r} = 1/a^{r}$; $a^{0} = 1$ (empty product, incl. $0^{0} = 1$ as convention). Rational $p/q$ in lowest terms; negative base only with odd $q$. $\sqrt{x^{2}} = |x|$.

**Exponential function.** Domain $\mathbb{R}$, range $(0, \infty)$, through $(0, 1)$, asymptote $y = 0$; $a > 1$ increasing, $0 < a < 1$ decreasing; $f(x+y) = f(x)f(y)$; $a^{x} = e^{x \ln a}$.

**Logarithm.** $\log_{a} y = x \Leftrightarrow a^{x} = y$; domain $y > 0$, base $a > 0$, $a \ne 1$; laws $\log MN = \log M + \log N$, $\log(M/N) = \log M - \log N$, $\log M^{p} = p \log M$ (with $M > 0$; repair $\log x^{2} = 2 \log|x|$); change of base $\log_{a} b = \frac{\ln b}{\ln a}$; chain $\log_{a} b \cdot \log_{b} c = \log_{a} c$; inverses $a^{\log_{a} x} = x$ ($x > 0$), $\log_{a}(a^{x}) = x$.

**Signs and monotonicity.** $\log_{a} x > 0 \Leftrightarrow (x-1)(a-1) > 0$; $\log_{a}$ increasing for $a > 1$, decreasing for $0 < a < 1$ (flip inequalities); $\lg 2 \approx 0.301$, $\lg 3 \approx 0.477$, $\ln 2 \approx 0.693$, $e \approx 2.718$.

**Equations.** Types: common base ($f = g$), quadratic in $a^{x}$ ($t = a^{x} > 0$), collapse-logs-then-exponentiate (domain first!), $x^{\log x}$ (take logs). Always: domain, solve, verify in the original.

**Applications.** Digits $d = \lfloor \lg N \rfloor + 1$; compare magnitudes by $\ln$; $a^{b}$ vs $b^{a}$ via $\frac{\ln t}{t}$ (max at $e$); growth $N_0 a^{t}$ / $N_0 e^{kt}$, doubling $t = \ln 2 / k$; growth hierarchy log $\ll$ power $\ll$ exponential.

:::key
**Five questions to ask any exponent/log problem.** (1) What is the domain (bases $> 0$, arguments $> 0$, bases $\ne 1$)? (2) Which single monotone function can I bring everything under? (3) Is the base $> 1$ or $< 1$ (inequality direction)? (4) After solving, which candidates survive the original equation? (5) Are units/bases mixed ($\lg$ vs $\ln$, degrees vs real exponents)?
:::

:::assume
Conventions fixed for the whole chapter: $a^{x}$ real-valued for $a > 0$ (negative bases only through integer exponents or odd roots); $0^{0} = 1$ as empty-product convention; $\lg = \log_{10}$, $\ln = \log_{e}$; all logs real, so arguments positive; "log" with no base means a formula holds for every legal base.
:::

:::app
**Where this toolkit reappears.** Domain/monotonicity discipline powers calculus limits ($1^{\infty}$ forms via $\ln$), analysis of $f(t) = \frac{\ln t}{t}$, and counting estimates (digits, digits of $n!$, order of magnitude) in later chapters and in Olympiad number theory (Legendre's formula — see Part II). The habit "convert $a^{x}$ to $e^{x \ln a}$" is the bridge to differential calculus.
:::

:::warn title="Final trap sweep"
- $\log_{a}(M + N)$ has **no** expansion; $(\log M)^{p} \ne \log M^{p}$.
- $(a^{r})^{s} = a^{rs}$ and $(ab)^{r} = a^{r}b^{r}$ silently need $a, b > 0$.
- Inequality flips when the base is in $(0, 1)$.
- Ghost roots from squaring / collapsing logs: verify in the original.
- $2^{x} = c$ has a real solution only for $c > 0$; then $x = \log_{2} c$ uniquely.
:::
