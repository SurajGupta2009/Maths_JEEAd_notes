---
id: jee-06
part: jee
title: "Standard Applications — Inequalities, Digits, Growth, Parameters"
---

## Log and exponent inequalities

Solve like equations, then respect the monotonicity direction. Worked: $\lg(x-1) < 1$. Domain $x > 1$; $\lg$ is increasing ($10 > 1$), so $x - 1 < 10^{1} = 10$; combine: $1 < x < 11$.

With a base $< 1$ the inequality flips: $\log_{1/2}(x-1) < 1 \Rightarrow x - 1 > (1/2)^{1} = \frac{1}{2}$ (flip!) $\Rightarrow x > \frac{3}{2}$.

**Exponential inequalities** follow the same rule: $2^{x^{2}-1} \geq 2^{3x} \Rightarrow x^{2} - 1 \geq 3x$ (base $2 > 1$) $\Rightarrow x^{2} - 3x - 1 \geq 0 \Rightarrow x \leq \frac{3-\sqrt{13}}{2}$ or $x \geq \frac{3+\sqrt{13}}{2}$.

:::key
**Inequality protocol:** (1) write the domain first (logs: argument $> 0$); (2) bring to one monotone function and read off the argument inequality (flip if base $< 1$); (3) intersect with the domain; (4) for $| \log |$ or mixed signs, split cases before step 2. Parametric problems: solve for $x$ with the parameter as a constant, then discuss the parameter ranges where the solution set changes (usually at the boundary points where a log argument hits $0/1$ or a base equals $1$).
:::

## Number-of-digits and order-of-magnitude models

$d(N) = \lfloor \lg N \rfloor + 1$ (see sheet 4). Variants: how many integers $n \leq N$ satisfy something? take logs; how many powers $2^{k}$ lie in $[a, b]$? count $k$ with $\lg a \leq k \lg 2 < \lg b$.

:::example title="Worked. How many digits does $3^{50}$ have? First two digits estimate."
$\lg(3^{50}) = 50 \lg 3 \approx 23.856$. So $d = \lfloor 23.856 \rfloor + 1 = 24$ digits. For the leading digits: $10^{0.856} \approx 7.18$, so $3^{50} \approx 7.18 \times 10^{23}$ — leading digit $7$. (Check: $3^{50} = 717897987691852588770249$ ✓ 24 digits, starts with 7 ✓.)
:::

## Growth models (the syllabus-fit applied framing)

Populations, compound interest, and radioactive decay all use $N(t) = N_{0} a^{t}$ or $N_{0} e^{kt}$: with a *fixed* percentage growth per period the multiplier is constant and the index is time. Doubling time for $e^{kt}$: $k t = \ln 2$, so $t = \ln 2 / k$ (with $\ln 2 \approx 0.693$). Half-life is the same with $-\ln 2$. These are **models built from the supplied function $a^{x}$** — the exam task is always to translate words into $a^{x}$ or $\log$, then solve with the toolkit above.

**Comparison of growth classes (use as ordering, not as calculus):** as $x \to \infty$ (any fixed bases $a > 1$, $b > 1$, $c > 1$): $\log_{c} x \ll x^{1/n}$ (for every $n$) $\ll a^{x}$. "Slowest to fastest: log, then root/power, then exponential." This is why compound growth overtakes polynomial growth eventually, and why taking logs linearises exponential comparisons.

:::derive title="Solving $a^{x} = b^{x + c}$ — the canonical parameter problem"
Take $\ln$: $x \ln a = (x + c) \ln b \Rightarrow x(\ln a - \ln b) = c \ln b \Rightarrow x = \dfrac{c \ln b}{\ln a - \ln b} = \dfrac{c}{\log_{b} a - 1}$, provided $a \ne b$ (if $a = b$: either no solution ($c \ne 0$) or all $x$ ($c = 0$)). Every "two-exponential crossing" problem is this shape after factoring.
:::

:::warn title="Common traps — applications edition"
- Word problems smuggle in domains: "$\log$ of the population" assumes the population is positive; "after $t$ years" may mean $t \in \mathbb{N}$ vs $t \geq 0$ real.
- Doubling/half-life formulas use **natural** logs; mixing $\lg$ and $\ln$ in one computation is a classic arithmetic error.
- $\lfloor \lg N \rfloor + 1$ counts digits of the **integer part** of $N$; for non-integers state the convention used.
- Growth "per cent per year" compounds: $1.06^{t}$, not $1 + 0.06 t$ (that linear model is a different, weaker statement).
:::
