---
id: oly-01
part: olympiad
title: "Olympiad Extensions — $x^{y} = y^{x}$, Multi-Base Logs, Towers"
---

## Status of this sheet

The equation $x^{y} = y^{x}$ and multi-base logarithmic systems are **standard IOQM/RMO algebra** and appear in specialised exam questions; everything below is derived from the Part I toolkit (monotonicity, change of base, $\frac{\ln t}{t}$) with no new theory assumed. Nothing here "can never appear in JEE" — the classification is only that these models go beyond the current syllabus sentence "Logarithms and their properties".

## $x^{y} = y^{x}$ — the complete positive solution set

For $x, y > 0$: if $x = y$ everything works. If $x \ne y$, take $\ln$: $y \ln x = x \ln y$, i.e. $\dfrac{\ln x}{x} = \dfrac{\ln y}{y}$. So $x, y$ are two distinct points where $f(t) = \frac{\ln t}{t}$ takes the **same value** — and $f$ increases on $(1, e]$, decreases on $[e, \infty)$, so any level is cut at most twice.

:::derive title="Parametrisation of all unequal solutions"
Put $y = tx$ with $t > 0$, $t \ne 1$. Then $x^{tx} = (tx)^{x} \Rightarrow x^{t} = tx \Rightarrow x^{t-1} = t \Rightarrow x = t^{1/(t-1)}$, $y = t^{t/(t-1)}$. Writing $t = 1 + \dfrac{1}{n}$ gives the classic family $x = \left(1 + \dfrac{1}{n}\right)^{n}$, $y = \left(1 + \dfrac{1}{n}\right)^{n+1}$ for $n > 0$ ($n \in \mathbb{Q}^{+}$ or $\mathbb{N}$). Check $n = 1$: $(x, y) = (2, 4)$: $2^{4} = 4^{2} = 16$ ✓. Integer solutions with $x \ne y$: exactly $(2, 4)$ and $(4, 2)$.
:::

:::example title="Worked. Real solutions with $x < y$, $xy = 8$, $x^{y} = y^{x}$?"
$\frac{\ln x}{x} = \frac{\ln y}{y}$ with $y = 8/x$: solve $\frac{\ln x}{x} = \frac{\ln(8/x)}{8/x}$ numerically/graphically by monotonicity arguments; or use the parametrisation: $\frac{y}{x} = t = 1 + \frac{1}{n}$, $xy = 8$ fixes $n$. From $y = tx$ and $xy = 8$: $t x^{2} = 8$. With $x = t^{1/(t-1)}$ this becomes $t^{1 + \frac{2}{t-1}} = 8 \Rightarrow t^{\frac{t+1}{t-1}} = 8$. Trial $t = 4$: $4^{5/3} \approx 10.08 \ne 8$; $t = 2$: $2^{3} = 8$ ✓. So $t = 2$, $x = 2$, $y = 4$. Answer: $(x, y) = (2, 4)$ (and the symmetric pair if order is free).
:::

## Multi-base logarithmic systems

**The three moves:** (1) reciprocity $\log_{a} b \cdot \log_{b} a = 1$; (2) chain $\log_{a} b \cdot \log_{b} c = \log_{a} c$; (3) change every base to $\ln$ (or to a common base $c$) and clear denominators.

:::example title="Worked. Solve $\log_{2} x = \log_{x} 4$"
Domain $x > 0$, $x \ne 1$. Reciprocity: $\log_{x} 4 = \dfrac{\ln 4}{\ln x} = \dfrac{2 \ln 2}{\ln x}$; also $\log_{2} x = \dfrac{\ln x}{\ln 2}$. Set $u = \ln x$: $\dfrac{u}{\ln 2} = \dfrac{2 \ln 2}{u} \Rightarrow u^{2} = 2(\ln 2)^{2} \Rightarrow u = \pm \ln 2 \cdot \sqrt{2}$. So $x = 2^{\sqrt{2}}$ or $x = 2^{-\sqrt{2}}$. Check both are $> 0$ and $\ne 1$ ✓. Answer: $x \in \{2^{\sqrt{2}},\ 2^{-\sqrt{2}}\}$.
:::

**Towers obey a convention:** $a^{b^{c}} = a^{(b^{c})}$ — exponentiation is **right-associative**; $(a^{b})^{c} = a^{bc} \ne a^{b^{c}}$ in general. Nested logs peel from the inside: $\log_{2}\!(\log_{3}(\log_{4} 256)) = \log_{2}\!(\log_{3} 4) = \log_{2}\!\left(\dfrac{\ln 4}{\ln 3}\right)$ — leave as exact expressions; never invent a "log of log" law.

:::warn title="Traps on this sheet"
- $x^{y} = y^{x}$ over **integers** vs **reals** give different answer sets; the parametrisation covers reals; integers need $t = 1 + 1/n$ with $t$ rational $\Rightarrow n = 1$ only among integers (for $x < y$ positive integers: $\{2, 4\}$).
- $\log_{a} b = \log_{a} c \Rightarrow b = c$ **needs the same base**; $\log_{2} x = \log_{3} x \Rightarrow x = 1$ only.
- Solving $\log_{x}(\cdot)$ adds base conditions $x > 0$, $x \ne 1$ on top of argument positivity.
- $f(t) = \frac{\ln t}{t}$ is **not** monotone on $(0, \infty)$ — it turns at $t = e$; two solutions for $f(t) = c \in (0, 1/e)$ sit on opposite sides of $e$.
:::

## Assumptions & conventions

All variables positive reals unless stated; integer solutions are a separate reading of the same equations; $\frac{\ln t}{t}$ analysis uses its stated monotonicity shape (derivable later by calculus; here taken as the known shape of the standard curve, with the level-curve picture as the geometric model).
