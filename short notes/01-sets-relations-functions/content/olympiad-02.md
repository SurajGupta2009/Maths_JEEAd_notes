---
id: oly-02
part: olympiad
title: "Functional Equations — Cauchy, Pexider, Involutions"
---

## Status of this sheet

The equations below are **additional theory** (classic RMO/INMO and AIME-adjacent material). Nothing here contradicts the syllabus: every *model* shown is solvable with the Part I supply list plus one extra idea, stated openly. Do not claim such an equation "can never appear in JEE" — exam papers have historically leaked olympiad-flavoured models; what is *not* promised is any theorem beyond the statements given here.

## The Cauchy equation $f(x+y) = f(x) + f(y)$ on $\mathbb{R}$

:::derive title="Rational linearity"
$f(0) = f(0+0) = f(0)+f(0) \Rightarrow f(0) = 0$. Induction: $f(nx) = n f(x)$ for $n \in \mathbb{N}$; then $0 = f(0) = f(x + (-x)) = f(x) + f(-x) \Rightarrow f(-x) = -f(x)$, so $f(nx) = nf(x)$ for all integers $n$. For $p/q$ with $q \geq 1$: $f(p) = f\left(q \cdot \frac{p}{q}\right) = q f\left(\frac{p}{q}\right) \Rightarrow f\left(\frac{p}{q}\right) = \frac{p}{q} f(1)$. Hence $f(r) = cr$ for every rational $r$, where $c = f(1)$.
:::

:::key
**Regular upgrade.** If $f$ is additionally monotone on any interval, or continuous at a point, or bounded above/below on any interval, then $f(x) = c x$ for all real $x$ (rational-linearity plus density of $\mathbb{Q}$ and the squeeze). Without *some* regularity, non-linear solutions exist (via a Hamel basis; they are non-measurable and cannot be written down explicitly) — so: **never write $f(x) = cx$ as "the" solution unless the problem grants a regularity condition.** Many exam models quietly assume continuity; state it.
:::

:::example
**Worked models.**
1. $f(x+y) = f(x) + f(y)$ for all $x, y \in \mathbb{Q}$, $f(1) = 2$: then $f(7/3) = \frac{7}{3} \cdot 2 = \frac{14}{3}$ — no regularity needed, because the domain is $\mathbb{Q}$ itself (rational linearity already complete).
2. $f : \mathbb{R} \to \mathbb{R}$ continuous, $f(x+y) = f(x) + f(y)$, $f(2) = 6$: $c = f(1) = 3$, so $f(x) = 3x$ for every real $x$. **Check:** $f(x + y) = 3(x+y) = 3x + 3y$ ✓.
3. $f : \mathbb{R} \to \mathbb{R}$ with $f(x+y) = f(x) + f(y)$ and $f(x) \geq 0$ for all $x > 0$ (bounded below on $(0,\infty)$): the regularity condition is what upgrades $f(r) = cr$ to $f(x) = cx$; then $f(x) \geq 0$ for $x > 0$ forces $c \geq 0$.
:::

## The multiplicative cousins

:::key
$f(x+y) = f(x)f(y)$: either $f \equiv 0$, or $f(0) = 1$ and $f$ never vanishes; with continuity $f(x) = a^{x}$, $a = f(1) > 0$. $f(xy) = f(x) + f(y)$ on $(0,\infty)$: with continuity $f(x) = c \ln x$ (set $g(t) = f(e^{t})$ and Cauchy reduces). $f(xy) = f(x)f(y)$ on $(0,\infty)$: $f(x) = x^{c}$ or $f \equiv 0, 1$ specials. **Pexider:** $f(x+y) = g(x) + h(y)$ for all $x,y$ implies all three are affine with $f = g + h + \text{const}$ relationships — plug $y = 0$ to express $g, h$ through one function and fall back to Cauchy. **Jensen:** $f\left(\frac{x+y}{2}\right) = \frac{f(x)+f(y)}{2}$ with continuity $\Rightarrow f(x) = cx + d$.
:::

:::derive title="f(x+y)=f(x)f(y) quickly"
Put $y = 0$: $f(x) = f(x)f(0)$, so either $f \equiv 0$ or $f(0) = 1$. If $f(x_{0}) = 0$ for some $x_0$, then $f(x) = f((x - x_{0}) + x_{0}) = f(x - x_{0})f(x_{0}) = 0$ for all $x$: $f \equiv 0$. So a non-zero solution never vanishes; if it takes both signs it still can't cross 0 (continuous image of connected set), hence a positive solution has $f(x) = e^{g(x)}$ with $g$ additive, and continuity finishes $g(x) = x \ln a$.
:::

## Involutions $f(f(x)) = x$

$f \circ f = \operatorname{id}$ means $f$ is its own inverse: $f$ is bijective and $f^{-1} = f$. Solutions of $f(f(x)) = x$ split into **fixed points** ($f(x) = x$) and **2-cycles** ($f(x) = y \ne x$, $f(y) = x$).

:::derive title="Increasing involution fixes everything"
Suppose $f$ is strictly increasing and $f(f(x)) = x$. If $f(x_{0}) > x_{0}$ then applying the increasing $f$ gives $f(f(x_{0})) > f(x_{0}) > x_{0}$, i.e. $x_{0} > f(x_{0})$ — contradiction. Similarly $f(x_{0}) < x_{0}$ contradicts. So $f(x) = x$ for all $x$: every increasing involution is the identity on its domain. A decreasing involution (e.g. $f(x) = a - x$, $f(x) = 1/x$ on $\mathbb{R}^{+}$) instead swaps pairs around fixed points.
:::

:::example
**Worked.** Find all continuous $f : \mathbb{R} \to \mathbb{R}$ with $f(f(x)) = x$ and $f$ decreasing. Any $x$ with $f(x) = x$ is a fixed point; $g(x) = f(x) - x$ is decreasing ($f$ dec, $-x$ dec... sum of two decreasing is decreasing) hence $g$ has at most one zero — at most one fixed point. Example $f(x) = a - x$ has exactly one ($x = a/2$). The general decreasing-continuous involution picture: one fixed point (if $g$ changes sign) and the rest of the line paired off in 2-cycles symmetric about it. **Check:** $f(x) = 1/x$ on $(0,\infty)$: decreasing, $f(f(x)) = x$ ✓, fixed point $x = 1$ ✓.
:::

:::warn
- Cauchy with domain $\mathbb{Q}$: rational linearity is the *complete* answer. Cauchy with domain $\mathbb{R}$: rational linearity + "regularity" is required; state the condition.
- $f(x) = x^{2}$ is even, $f(x) = x^{3}$ odd, but $f(x) = x^{2} + x^{3}$ is neither — decomposition (Part I) is the safe tool.
- In $f(f(x)) = x$ problems, plugging $x = f(t)$ is the standard trick: $f(f(f(t))) = f(t)$, i.e. $f^{3} = f$; combined with $f^{2} = \operatorname{id}$ this just re-proves bijectivity — write the injection/surjection argument once, cleanly.
- Periodic + additive: $f(x+T) = f(x)$ with additivity forces $f(T) = f(0) = 0$, and with continuity that collapses $f \equiv 0$ (since $f(r) = cr$ and $cT = 0$). Without continuity a wild additive $T$-periodic solution can still exist on a Hamel basis — so again: state the regularity condition before claiming collapse. The point stands: **imposing two strong structures usually collapses the family to trivial members, but "usually" needs a hypothesis.**
:::
