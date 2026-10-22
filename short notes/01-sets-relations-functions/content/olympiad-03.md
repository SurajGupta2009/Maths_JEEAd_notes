---
id: oly-03
part: olympiad
title: "Floor Toolkit & Fixed-Point Counting — Hermite, Equations, Involution Sets"
---

## Status of this sheet

The greatest-integer function is **in the official syllabus** (listed under special functions); Hermite's identity and the fixed-point decomposition are extra theory. Every worked model below is solved with syllabus tools only — so treat the identities as accelerators, and the models as fair game.

## Hermite's identity

:::derive title="Sum of n shifted floors"
For real $x$ and positive integer $n$:
$$\sum_{k=0}^{n-1} \left\lfloor x + \frac{k}{n} \right\rfloor = \lfloor n x \rfloor$$
Write $x = m + \theta$ with $m = \lfloor x \rfloor$, $\theta \in [0,1)$. Then $\lfloor x + \frac{k}{n}\rfloor = m + \lfloor \theta + \frac{k}{n}\rfloor$, so the left side is $nm + \sum_{k}\lfloor \theta + \frac{k}{n} \rfloor$. Now $\lfloor \theta + \frac{k}{n} \rfloor = 1$ exactly when $\frac{k}{n} \geq 1 - \theta$, i.e. $k \geq n(1-\theta)$; the number of $k \in \{0,\dots,n-1\}$ with $k \geq n(1-\theta)$ is $\lfloor n\theta \rfloor$ (boundary $n(1-\theta)$ an integer counts $k$ from that value up). So the sum $= nm + \lfloor n\theta \rfloor = \lfloor nm + n\theta \rfloor = \lfloor nx \rfloor$ ✓.
:::

:::example
**Worked checks.** $n = 3$, $x = 1.7$: $\lfloor 1.7\rfloor + \lfloor 1.7 + 0.33\rfloor + \lfloor 1.7 + 0.67\rfloor = 1 + 2 + 2 = 5 = \lfloor 5.1\rfloor$ ✓. $x = 2$ exactly: $2 + 2 + 2 = 6 = \lfloor 6 \rfloor$ ✓. **Check boundary:** when $n\theta$ is an integer the threshold $k \geq n(1-\theta)$ is attained (included) — $\lfloor \cdot \rfloor$ inequality is $\geq$ on both sides of the threshold count.
:::

## Floor identities and equations

:::key
$[x] \leq x < [x]+1$; $[x] + [y] \leq [x+y] \leq [x]+[y]+1$; $[x] + [-x] = 0$ if $x \in \mathbb{Z}$ else $-1$; $\{x\} + \{-x\} = 0$ or $1$ with the same split; number of integers in $(a, b]$ is $[b] - [a]$; $[x] = c \Leftrightarrow x \in [c, c+1)$; $[x] < c \Leftrightarrow x < c$ (for integer $c$); $[x] \geq c \Leftrightarrow x \geq c$ (integer $c$).
:::

:::app
**Model (fully syllabus-level).** Solve $\lfloor x^{2} \rfloor = 2$ over the reals. Sandwich: $2 \leq x^{2} < 3$. Left half: $x^{2} \geq 2 \Rightarrow |x| \geq \sqrt{2}$; right half: $x^{2} < 3 \Rightarrow |x| < \sqrt{3}$. Solution set $= \{x : \sqrt{2} \leq |x| < \sqrt{3}\} = [-\sqrt{3}, -\sqrt{2}] \cup [\sqrt{2}, \sqrt{3})$ — **closed** at $\pm\sqrt{2}$ ($x^{2} = 2$ gives $\lfloor 2 \rfloor = 2$ ✓) and **open** at $\pm\sqrt{3}$ ($x^{2} = 3$ would give $\lfloor 3 \rfloor = 3$ ✗). The answer is a set of reals, not a number. Integer version: $x \in \mathbb{Z}$ needs $x^{2} \in [2,3)$, but squares of integers are $0, 1, 4, \ldots$ — **no solutions**. **Check:** the two phrasings ("all real $x$" vs "all integer $x$") have completely different answers; the quantifier is part of the question.
:::

## Fixed points and involutions (counting flavour)

$f(x) = x$ is a **fixed point**; $f(f(x)) = x$ is an **involution equation** whose solution set decomposes into fixed points of $f$ plus 2-cycles $\{x, f(x)\}$ with $f(x) \ne x$.

:::key
If $f$ is strictly increasing and $f(f(x)) = x$ on an interval, then $f(x) = x$ everywhere on it (Part II sheet 02 proof). If $f$ is strictly decreasing and continuous, $g(x) = f(x) - x$ is strictly decreasing, so $f$ has **at most one** fixed point; each non-fixed $x$ pairs with $f(x)$ in a 2-cycle. Counting solutions of $f(f(x)) = x$ for a concrete monotone $f$ therefore reduces to: find fixed points (solve $f(x)=x$), then account for the symmetric 2-cycles.
:::

:::example
**Worked.** $f(x) = 3 - x$ on $\mathbb{R}$: decreasing, $f(f(x)) = 3-(3-x) = x$ ✓ for **every** $x$ — the entire line solves the involution equation, yet only $x = 3/2$ is a fixed point. Moral: "solutions of $f(f(x))=x$" and "fixed points of $f$" are different sets; the question wording decides which is asked. With $f(x) = \frac{1}{x}$ on $(0,\infty)$: $f(f(x)) = x$ everywhere; fixed point $x = 1$ only. **Check:** $f(2) = 1/2$, $f(1/2) = 2$ — a 2-cycle, as predicted by the decreasing-case analysis.
:::

:::warn
- $\lfloor x \rfloor$ of a negative number: $\lfloor -1.2 \rfloor = -2$, not $-1$ (greatest integer **less or equal**). Truncation toward zero is a different function.
- In floor equations, the answer set's endpoints are decided by strict vs non-strict inequalities — write the sandwich first, then convert to interval notation, then test both endpoints.
- $\lfloor x^{2} \rfloor = 2$ vs $\lfloor x \rfloor^{2} = 2$: the second means $\lfloor x \rfloor = \pm\sqrt{2}$, impossible for integer $\lfloor x \rfloor$ — no solutions. Composition order matters even inside floor equations.
- Never square an inequality $\sqrt{2} \leq |x| < \sqrt{3}$ without tracking that $|x|$ is already non-negative — squaring is safe on $[0,\infty)$ but flips nothing here; for $x < 0$ reflect by $|x|$.
:::

:::assume
All floor statements are for real $x$; $n$ is a positive integer in Hermite; fixed-point claims assume the stated monotonicity/continuity on an interval. 2-cycles are unordered pairs $\{x, y\}$ with $y = f(x) \ne x$; when "count solutions" is asked on a finite set, count elements $x$, not cycles.
:::
