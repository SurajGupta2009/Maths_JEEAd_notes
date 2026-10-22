---
id: jee-04
part: jee
title: "Logarithms in Action — Simplification, Signs, Comparisons"
---

## Simplification patterns that recur in exams

**Nested logs** peel from the inside: $\log_{2}\!(\log_{3} 81) = \log_{2}(4) = 2$. **Mixed-base sums** use change of base: $\log_{4} 8 = \dfrac{\log_{2} 8}{\log_{2} 4} = \dfrac{3}{2}$.

**Power towers of a single base:** $\log_{a}\!\left(a^{a^{x}}\right) = a^{x}$ (one application of $\log_{a}(a^{p}) = p$).

**Sums of logs at fractions:** $\log_{2} 3 + \log_{2} 6 + \log_{2} 24 = \log_{2}(3 \cdot 6 \cdot 24) = \log_{2} 432 = \log_{2}(2^{4} \cdot 27) = 4 + 3\log_{2} 3$.

:::derive title="The digit formula — how many digits does $N$ have?"
A positive integer $N$ has $d$ digits exactly when $10^{d-1} \leq N < 10^{d}$. Taking $\lg$: $d - 1 \leq \lg N < d$, so $d = \lfloor \lg N \rfloor + 1$. Example: $2^{100}$. $\lg(2^{100}) = 100 \lg 2 \approx 30.103$, so $2^{100}$ has $\lfloor 30.103 \rfloor + 1 = 31$ digits ✓ (indeed $2^{100} = 1267650600228229401496703205376$). The formula uses **$\lfloor \cdot \rfloor$, not rounding**, and works for any positive real $N$ ("order of magnitude" version).
:::

## Comparing magnitudes — the three standard moves

1. **Take a log.** $2^{300}$ vs $3^{200}$: compare $300 \lg 2 \approx 90.31$ vs $200 \lg 3 \approx 95.42$ $\Rightarrow 3^{200} > 2^{300}$. Logs are increasing, so $\log$ of two positives preserves their order (use $\ln$ or $\lg$, any base $> 1$).

2. **Raise to a common power.** $a^{b}$ vs $b^{a}$ with $a < b$: compare after raising both to $1/(ab)$: $a^{b} < b^{a} \Leftrightarrow a^{1/a} < b^{1/b} \Leftrightarrow \dfrac{\ln a}{a} < \dfrac{\ln b}{b}$. The function $f(t) = \dfrac{\ln t}{t}$ increases up to $t = e$ and decreases after (calculus confirms; for the toolkit, know the shape: max at $e$).

3. **Squeeze between integers.** For integer estimates, bracket with known powers: $2^{10} = 1024 \approx 10^{3.01}$ is the usual bridge ($1000 \approx 2^{10}$).

:::example title="Worked. Which is larger: $e^{\pi}$ or $\pi^{e}$?"
Take $\ln$ of both (both positive, $\ln$ increasing): $\ln(e^{\pi}) = \pi \approx 3.14159$, while $\ln(\pi^{e}) = e \ln \pi \approx 2.71828 \times 1.14473 \approx 3.11229$. Since $3.14159 > 3.11229$, we get $e^{\pi} > \pi^{e}$. (Consistent with $f(t) = \frac{\ln t}{t}$ decreasing for $t > e$: here $\pi > e$, so $\frac{\ln e}{e} > \frac{\ln \pi}{\pi} \Rightarrow \pi \ln e > e \ln \pi \Rightarrow e^{\pi} > \pi^{e}$ ✓.)
:::

## Sign and size of $\log_{a} x$ — the grid to hold in your head

| | $x > 1$ | $x = 1$ | $0 < x < 1$ |
|---|---|---|---|
| $a > 1$ | $\log_{a} x > 0$ | $0$ | $\log_{a} x < 0$ |
| $0 < a < 1$ | $\log_{a} x < 0$ | $0$ | $\log_{a} x > 0$ |

Absolute value: $|\log_{a} x| = -\log_{a} x$ exactly when $\log_{a} x \leq 0$, i.e. when $x$ and $a$ sit on opposite sides of $1$. So $\log_{a}|x|$ (defined for $x \ne 0$) and $|\log_{a} x|$ (defined for $x > 0$) are **different functions** — check which one a problem asks for.

:::key
**Comparison checklist:** (1) take $\ln$ of both sides if both are positive; (2) convert to a common base or to $e$ via $a^{x} = e^{x \ln a}$; (3) for $a^{b}$ vs $b^{a}$ use $f(t) = \frac{\ln t}{t}$ (max at $t = e$; $2^{4} = 4^{2}$ is the only integer pair with $a \ne b$ and $a^{b} = b^{a}$, namely $(2, 4)$ and $(4, 2)$); (4) remember $\lg 2 \approx 0.301$, $\lg 3 \approx 0.477$, $\ln 2 \approx 0.693$ — three numbers that unlock most numerical estimates.
:::

:::warn title="Common traps — comparison edition"
- Taking $\log$ of an inequality requires **both sides positive**; $\log$ of a negative is undefined, not "negative log".
- $\lg(a + b) \ne \lg a + \lg b$; write $\lg(a+b)$ as it is or factor first.
- $\log_{a} x$ increasing is for $a > 1$ only; with $0 < a < 1$, $\log_{a} x > \log_{a} y \Rightarrow x < y$.
- $2^{300} \approx 10^{90.3}$ means $2^{300}$ is between $10^{90}$ and $10^{91}$ — use floors, not rounding, for digits.
:::
