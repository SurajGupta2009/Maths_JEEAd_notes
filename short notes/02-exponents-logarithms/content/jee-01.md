---
id: jee-01
part: jee
title: "Exponents — Laws, Domains, Conventions"
---

## What $a^{x}$ means (and when it exists)

An **exponent** $a^{x}$ answers "multiply $a$ by itself $x$ times" only when $x$ is a positive integer. Every other exponent is an *extension* built to keep the laws below true:

- $a^{0} = 1$ (empty product) for every $a \ne 0$.
- $a^{-p} = \dfrac{1}{a^{p}}$ for $p > 0$.
- $a^{p/q} = (\sqrt[q]{a})^{p} = (a^{1/q})^{p}$ for $p \in \mathbb{Z}$, $q \in \mathbb{N}$, $q \geq 1$, $\gcd(p,q)=1$.

**Base convention (the single most important assumption of the chapter):** for *real* exponents $x$ that are not integers, $a^{x}$ is defined for **$a > 0$** only. With $a > 0$, $a^{x}$ exists for every real $x$ and is positive.

:::assume
Throughout this chapter a base written $a$, $b$, $c$ under a real exponent is assumed **positive**. If the base can be negative, only *integer* exponents are safe, and rational exponents need the parity rule below. Logarithm bases further satisfy $a \ne 1$. When a problem writes $a^{x}$ with no comment, $a > 0$ is part of the data.
:::

### Rational exponents and parity

For $a > 0$: $a^{p/q}$ is the **unique positive** $q$-th root raised to $p$. For $a < 0$ the real $q$-th root exists **iff $q$ is odd**. So $(-8)^{1/3} = -2$ is legal, while $(-8)^{1/2}$ is not real.

$(-8)^{2/3} = ((-8)^{1/3})^{2} = (-2)^{2} = 4$ — reduce $p/q$ to lowest terms **first**, then take the odd root.

## The laws of indices (and their hidden hypotheses)

For $a, b > 0$ and $r, s \in \mathbb{R}$:

$$a^{r} a^{s} = a^{r+s}, \qquad \dfrac{a^{r}}{a^{s}} = a^{r-s}, \qquad (a^{r})^{s} = a^{rs},$$

$$(ab)^{r} = a^{r} b^{r}, \qquad \left(\dfrac{a}{b}\right)^{r} = \dfrac{a^{r}}{b^{r}}, \qquad a^{-r} = \dfrac{1}{a^{r}}.$$

:::derive title="Why $(ab)^{r} = a^{r}b^{r}$ needs $a, b > 0$"
For integer $r$ the identity holds for all reals $a, b$ (just expand). For $r = 1/2$ it fails on negatives: $( (-1)(-1) )^{1/2} = 1^{1/2} = 1$, but $(-1)^{1/2} \cdot (-1)^{1/2}$ is not real. The clean repair: restrict to $a, b > 0$, where every factor $a^{r}$ is a well-defined positive number. That is exactly the convention above.
:::

:::warn title="Common trap — $(a^{r})^{s} = a^{rs}$ is false on negatives"
$((-2)^{2})^{1/2} = 4^{1/2} = 2$, but $(-2)^{2 \cdot 1/2} = (-2)^{1} = -2$. The rule $(a^{r})^{s} = a^{rs}$ is valid for **$a > 0$** (or when $r, s$ are both integers). Mixing "even power" and "half power" on a negative base is the classic JEE trap. Two safe forms: $(a^{2})^{1/2} = |a|$ for all real $a$; $a^{1/2}$ only for $a \geq 0$.
:::

### The absolute-value repairs

$$\sqrt{x^{2}} = |x| \ \ \text{for all real } x; \qquad \left(x^{1/2}\right)^{2} = x \ \ \text{for } x \geq 0$$

$$\sqrt[n]{x^{n}} = |x| \ \text{if } n \text{ even}; \quad x \ \text{if } n \text{ odd}$$

:::key
Three repairs worth memorising: (1) $\sqrt{x^{2}} = |x|$, never $x$; (2) reduce $p/q$ to lowest terms before evaluating a negative base; (3) $(a^{r})^{s} = a^{rs}$ and $(ab)^{r} = a^{r}b^{r}$ are stated here for $a, b > 0$ — that is the standing convention.
:::

## Solving exponent equations on the level of indices

If $a > 0$, $a \ne 1$, then $a^{f(x)} = a^{g(x)} \Leftrightarrow f(x) = g(x)$ — the exponential function is **injective** (one-to-one). If $a = 1$, both sides are $1$ and the equation is empty of information; if $a = 0$ or the base can vary, handle cases.

:::example title="Worked. Solve $x^{2/3} = 8$ over $\mathbb{R}$"
Raise both sides to the power $3/2$ *with care*. Write $x^{2/3} = (x^{1/3})^{2} = 8$, so $x^{1/3} = \pm 2\sqrt{2}$ and $x = \pm (2\sqrt{2})^{3} = \pm 16\sqrt{2}$. Both are valid (the exponent $2/3$ has odd denominator, so $(-16\sqrt{2})^{2/3} = ((-16\sqrt{2})^{1/3})^{2} = ( -2\sqrt{2})^{2} = 8$ ✓). Answer: $x = \pm 16\sqrt{2}$.
:::

:::warn title="Common trap — squaring and simplifying add or drop roots"
$x^{2} = 4 \Rightarrow x = \pm 2$, not $x = 2$. But $x^{1/2} = 2 \Rightarrow x = 4$ **only** (the left side forces $x \geq 0$ and is already non-negative; squaring here does not add roots). Before any manipulation, write the **domain** of the equation; after, check every candidate in the original equation.
:::
