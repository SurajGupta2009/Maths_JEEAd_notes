---
id: jee-03
part: jee
title: "Logarithms — Definition, Laws, Derivations"
---

## The definition (memorise the *equivalence*)

For $a > 0$, $a \ne 1$ and $y > 0$:

$$\log_{a} y = x \quad \Longleftrightarrow \quad a^{x} = y.$$

Read it both ways: $\log_{a} y$ is the **exponent** to which $a$ must be raised to get $y$. Immediate consequences (all just the definition in disguise):

$$\log_{a} 1 = 0, \qquad \log_{a} a = 1, \qquad \log_{a} \dfrac{1}{a} = -1$$

$$\log_{a} a^{p} = p \ \ (\forall p \in \mathbb{R})$$

$$a^{\log_{a} y} = y \ \ (y > 0)$$

**Domain discipline:** $\log_{a} y$ requires $y > 0$ **and** $a > 0$, $a \ne 1$. $\log_{a} 0$ and $\log_{a}(\text{negative})$ are undefined in $\mathbb{R}$; $\log_{1} y$ and $\log_{-2} y$ are meaningless (no unique inverse of $1^{x}$ or of $(-2)^{x}$).

## The three laws (each comes from a law of indices)

For $M, N > 0$, $a > 0$, $a \ne 1$, $p \in \mathbb{R}$:

$$\log_{a}(MN) = \log_{a} M + \log_{a} N$$

$$\log_{a}\!\left(\dfrac{M}{N}\right) = \log_{a} M - \log_{a} N$$

$$\log_{a}\!\left(M^{p}\right) = p \log_{a} M.$$

:::derive title="Derivation — set $M = a^{m}$, $N = a^{n}$"
Then $MN = a^{m+n}$, so by definition $\log_{a}(MN) = m + n = \log_{a} M + \log_{a} N$. The quotient law is the same with $N \mapsto 1/N$. For the power law, $M^{p} = (a^{m})^{p} = a^{pm}$ (here $M > 0$ makes $(a^{m})^{p} = a^{mp}$ legitimate), so $\log_{a}(M^{p}) = pm$. Every log law is an index law in disguise — that is why the domain restrictions above are non-negotiable.
:::

:::warn title="Common traps — there is no law for sums or products of logs"
- $\log_{a}(M + N)$ **does not expand**. There is no formula. Expand $\log(MN)$ or $\log(M/N)$ only.
- $\log_{a} M \cdot \log_{a} N$ is not the log of anything.
- $(\log_{a} M)^{p} \ne \log_{a}(M^{p})$ in general: $p \log_{a} M = \log_{a}(M^{p})$, but $(\log_{a} M)^{p}$ is just a power of a number.
- $\log_{a}(x^{2}) = 2 \log_{a} x$ is **wrong for $x < 0$** — correct form: $\log_{a}(x^{2}) = 2 \log_{a}|x|$ for $x \ne 0$.
- $\log_{a} a^{p} = p$ holds for all real $p$; $a^{\log_{a} x} = x$ holds only for $x > 0$.
:::

## Change of base, chain rule, reciprocity

For $a, b, c > 0$, $a, b \ne 1$:

$$\log_{a} b = \dfrac{\log_{c} b}{\log_{c} a} = \dfrac{\ln b}{\ln a} = \dfrac{\lg b}{\lg a}$$

$$\log_{a} b \cdot \log_{b} a = 1, \qquad \log_{a} b \cdot \log_{b} c = \log_{a} c.$$

:::derive title="Derivation — put $x = \log_{a} b$, so $a^{x} = b$"
Take $\log_{c}$ of both sides: $x \log_{c} a = \log_{c} b$, hence $x = \frac{\log_{c} b}{\log_{c} a}$. Setting $c = b$ gives $\log_{a} b = 1/\log_{b} a$ (the reciprocity $\log_{a} b \cdot \log_{b} a = 1$); chaining two such fractions gives $\log_{a} b \cdot \log_{b} c = \frac{\ln b}{\ln a} \cdot \frac{\ln c}{\ln b} = \frac{\ln c}{\ln a} = \log_{a} c$.
:::

## The sign rule and log inequalities

For $a > 0$, $a \ne 1$, $x > 0$:

$$\log_{a} x > 0 \ \Leftrightarrow\ (x-1)(a-1) > 0$$

(equivalently: $x$ and $a$ lie on the same side of $1$)

So $\log_{2} 5 > 0$, $\log_{1/2} 5 < 0$, $\log_{2} 0.3 < 0$. Monotonicity: $\log_{a} x$ is **increasing** for $a > 1$, **decreasing** for $0 < a < 1$ — so $\log_{a} M > \log_{a} N \Rightarrow M > N$ for $a > 1$ but $\Rightarrow M < N$ for $0 < a < 1$.

:::diagram
{"type": "graph", "ratio": 0.62, "xrange": [-1.2, 9], "yrange": [-3.2, 3.2], "xticks": [0, 1, 2, 4, 8], "yticks": [-3, -2, -1, 0, 1, 2, 3], "title": "Log curves (all pass (1, 0)), vertical asymptote x = 0, reflection in y = x", "vlines": [{"x": 0, "label": "asymptote x = 0"}], "curves": [{"expr": "log(x)/log(2)", "color": "#0F766E", "label": "y = log2 x", "labpos": 0.78}, {"expr": "log(x)/log(0.5)", "color": "#B91C1C", "label": "y = log(1/2) x", "labpos": 0.44}, {"expr": "log(x)", "color": "#16295C", "label": "y = ln x", "labpos": 0.9}, {"expr": "x", "color": "#B8860B", "ls": "--", "lw": 2.0, "label": "y = x (mirror)", "labpos": 0.37}], "points": [{"x": 1, "y": 0, "label": "(1, 0)", "color": "#B8860B", "dx": -1.35, "dy": -0.85}, {"x": 2, "y": 1, "label": "(a, 1) for base a", "color": "#B8860B", "dx": 0.35, "dy": -0.85}]}
:::

:::key
The graph of $y = \log_{a} x$ is the reflection of $y = a^{x}$ in the line $y = x$ (inverse functions). Both pass $(1, 0)$ / $(0, 1)$ respectively; log has **vertical** asymptote $x = 0$, exp has **horizontal** asymptote $y = 0$; range of log = domain of exp = $\mathbb{R}$, domain of log = range of exp = $(0, \infty)$.
:::

:::example title="Worked. Simplify $\log_{2} 6 - \log_{2} 3 + \log_{2} 16$"
$= \log_{2}\!\left(\dfrac{6}{3} \cdot 16\right) = \log_{2} 32 = 5$. Check: $2^{5} = 32 = 2 \cdot 16$ ✓.
:::
