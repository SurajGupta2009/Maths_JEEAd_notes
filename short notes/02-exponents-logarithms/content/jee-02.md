---
id: jee-02
part: jee
title: "The Exponential Function $a^{x}$ — Shape, Monotonicity, $e$"
---

## $a^{x}$ as a function $\mathbb{R} \to (0, \infty)$

Fix $a > 0$. Then $f(x) = a^{x}$ has **domain $\mathbb{R}$**, **range $(0, \infty)$**, and satisfies the **exponential law**

$$f(x+y) = f(x) f(y), \qquad f(0) = 1, \qquad f(-x) = \dfrac{1}{f(x)}.$$

(Any *continuous* function with $f(x+y) = f(x)f(y)$ and $f(1) = a > 0$ must be $a^{x}$ — the law plus continuity pins the whole function down. Discontinuous counter-examples exist but need set-theoretic constructions beyond this syllabus; exam functions are continuous.)

- $a > 1$: strictly **increasing**, $a^{x} \to \infty$ as $x \to \infty$, $a^{x} \to 0^{+}$ as $x \to -\infty$.
- $0 < a < 1$: strictly **decreasing**, $a^{x} \to 0^{+}$ as $x \to \infty$, $a^{x} \to \infty$ as $x \to -\infty$.
- $a = 1$: the constant $1$ — which is why log bases exclude $1$.

Every curve $y = a^{x}$ passes through $(0, 1)$ and lies **above the $x$-axis**; the $x$-axis is a horizontal asymptote.

:::diagram
{"type": "graph", "ratio": 0.58, "xrange": [-3, 3], "yrange": [-0.6, 9], "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [0, 2, 4, 6, 8], "title": "The exponential family (all pass through (0, 1), asymptote y = 0)", "hlines": [{"y": 0, "label": "asymptote y = 0"}], "curves": [{"expr": "2**x", "color": "#0F766E", "label": "y = 2^x (up)", "labpos": 0.86}, {"expr": "exp(x)", "color": "#16295C", "label": "y = e^x", "labpos": 0.80}, {"expr": "0.5**x", "color": "#B91C1C", "label": "y = (1/2)^x (down)", "labpos": 0.10}], "points": [{"x": 0, "y": 1, "label": "(0, 1)", "color": "#B8860B", "dx": 0.45, "dy": 0.95}]}
:::

## The number $e$ and the natural exponential

$e = 2.718281828459045\ldots$ is the unique base for which the curve $y = e^{x}$ has slope $1$ at $x = 0$ (the fact that will make $e^{x}$ the natural exponential in calculus). Facts used constantly:

$$e \approx 2.71828, \qquad \ln e = 1, \qquad e^{x+y} = e^{x}e^{y}$$

$$(e^{x})^{r} = e^{rx}$$

Notation: $\lg x = \log_{10} x$ (common log), $\ln x = \log_{e} x$ (natural log), and $a^{x} = e^{x \ln a}$ for every $a > 0$ — this identity converts any exponential base into $e$ and is the workhorse of comparisons.

:::key
**Monotonicity is the whole game.** For $a > 1$: $a^{f(x)} > a^{g(x)} \Leftrightarrow f(x) > g(x)$. For $0 < a < 1$ the inequality **flips**: $a^{f(x)} > a^{g(x)} \Leftrightarrow f(x) < g(x)$. Same rule for log inequalities in the next sheets.
:::

:::derive title="Why $a^{x}$ is increasing when $a > 1$ (algebraic proof)"
Let $x < y$, so $y - x > 0$. Then $a^{y} = a^{x} \cdot a^{y-x}$. For $a > 1$ and $h > 0$ we have $a^{h} > 1$ (the $q$-th root of a number $> 1$ is $> 1$, and rationals are dense / continuity), so $a^{y} > a^{x}$. For $0 < a < 1$, $a^{h} < 1$ and the inequality reverses. This is the entire content of "exp preserves inequalities" — one multiplication by a factor $>1$ or $<1$.
:::

## Standard applications

**1. Exponential equations by substitution.** $4^{x} - 3 \cdot 2^{x} + 2 = 0$: put $t = 2^{x} > 0$, get $t^{2} - 3t + 2 = 0$, so $t \in \{1, 2\}$, i.e. $x \in \{0, 1\}$. Always keep the constraint $t > 0$ in the quadratic stage.

**2. Growth comparisons.** To compare $2^{300}$ and $3^{200}$, take $\lg$: $300 \lg 2 \approx 90.31$ and $200 \lg 3 \approx 95.42$, so $3^{200} > 2^{300}$. Taking a log of a positive comparison never changes its direction.

**3. Mixed systems.** Solve $e^{2x} - 3e^{x} + 2 = 0$ by $t = e^{x}$: $t = 1, 2$, so $x = 0$ or $x = \ln 2$.

:::example title="Worked. Solve $2^{2x} - 5 \cdot 2^{x} + 4 = 0$"
$t = 2^{x} > 0$: $t^{2} - 5t + 4 = 0 \Rightarrow t = 1$ or $t = 4$ (both $> 0$ ✓). So $2^{x} = 1 \Rightarrow x = 0$; $2^{x} = 4 \Rightarrow x = 2$. Check $x = 0$: $1 - 5 + 4 = 0$ ✓; $x = 2$: $16 - 20 + 4 = 0$ ✓. Answer: $x \in \{0, 2\}$.
:::

:::warn title="Common traps — exponential edition"
- $(a^{x})^{2} = a^{2x}$ ✓ for $a > 0$; but $a^{x} = a^{y} \Rightarrow x = y$ only when $a \ne 1$.
- Substituting $t = a^{x}$ **throws away** the range condition $t > 0$: a quadratic giving $t = -2$ contributes nothing.
- $2^{x} = -4$ has **no real solution** (range of $2^{x}$ is $(0,\infty)$) — say so instead of writing $x = 2i$.
- $a^{x} > 0$ always: $a^{x} \geq 0$ or $a^{x} > c$ for $c < 0$ is automatically true for all $x$.
:::
