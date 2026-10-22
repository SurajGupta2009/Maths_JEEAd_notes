---
id: oly-01
part: olympiad
title: "Olympiad Extensions — the Weierstrass Substitution"
---

## Status of this sheet

The substitution $t = \tan\frac{A}{2}$ (Weierstrass) is **standard RMO/INMO technique** and a bridge to integral calculus; every model below is derivable from Part I identities. Nothing here "can never appear in JEE" — historically JEE-style papers have used it in disguised form; the classification is only that it exceeds the syllabus sentence "Trigonometric functions, general solution, identities".

## The substitution and what it buys

Put $t = \tan\dfrac{A}{2}$. Then (for $A \ne \pi + 2k\pi$):

$$\sin A = \dfrac{2t}{1 + t^{2}}, \qquad \cos A = \dfrac{1 - t^{2}}{1 + t^{2}}, \qquad \tan A = \dfrac{2t}{1 - t^{2}}.$$

:::derive title="Derivation — divide the double-angle forms by $\cos^{2} \frac{A}{2}$"
$\sin A = 2 \sin\frac{A}{2} \cos\frac{A}{2} = \frac{2 \tan\frac{A}{2}}{\sec^{2}\frac{A}{2}} = \frac{2t}{1 + t^{2}}$ (using $\sec^{2} = 1 + \tan^{2}$). Similarly $\cos A = \cos^{2}\frac{A}{2} - \sin^{2}\frac{A}{2} = \frac{1 - t^{2}}{1 + t^{2}}$ after dividing by $\cos^{2}\frac{A}{2}$. Tangent: ratio of the two ✓. The point: **any rational expression in $\sin A, \cos A$ becomes a rational function of $t$** — trig equations become polynomial equations; trig integrals $\int R(\sin x, \cos x)\, dx$ become rational integrals (calculus toolkit).
:::

:::example title="Worked. Solve $\sin x + \cos x = 1$ for $0 \leq x < 2\pi$ with $t = \tan\frac{x}{2}$"
$\frac{2t}{1 + t^{2}} + \frac{1 - t^{2}}{1 + t^{2}} = 1 \Rightarrow 2t + 1 - t^{2} = 1 + t^{2} \Rightarrow 2t^{2} - 2t = 0 \Rightarrow t = 0$ or $t = 1$. $t = 0 \Rightarrow x = 0$; $t = 1 \Rightarrow \frac{x}{2} = \frac{\pi}{4} \Rightarrow x = \frac{\pi}{2}$. The excluded point $x = \pi$ (where $\cos\frac{x}{2} = 0$) gives $\sin\pi + \cos\pi = -1 \ne 1$ ✓ nothing lost. Answer: $x \in \{0, \frac{\pi}{2}\}$ ✓.
:::

:::warn title="The blind spot — $A = \pi$ (mod $2\pi$)"
$t = \tan\frac{A}{2}$ is undefined when $\frac{A}{2} = \frac{\pi}{2} + k\pi$, i.e. $A = \pi + 2k\pi$. Every solution there is invisible to the substitution — **always test $A = \pi + 2k\pi$ in the original equation** and add it if it works. For $A \in (-\pi, \pi)$ the map $A \mapsto t$ is a bijection onto $\mathbb{R}$ (this is the clean domain window for the substitution).
:::

:::key
**When to use it.** (1) Equations rational in $\sin, \cos$ that resist factorisation; (2) proving identities by clearing denominators in $t$; (3) converting geometry (slope $= \tan\frac{\theta}{2}$) into algebra; (4) (forward reference) any integral $\int R(\sin x, \cos x) dx$. Counter-indication: when half-angle or product-to-sum is quicker — do the cheap tool first.
:::

## Worked models

:::example title="Worked. Solve $\sin x + \cos x = 1$ over all reals"
General solutions from the two families: $x = 2n\pi$ (from $t = 0$) and $x = \frac{\pi}{2} + 2n\pi$ (from $t = 1$), $n \in \mathbb{Z}$; the blind-spot test $x = \pi + 2n\pi$ fails. Combined: $x = 2n\pi$ or $x = \frac{\pi}{2} + 2n\pi$ ✓ (leave as the two families).
:::

:::example title="Worked. Express $\frac{1 - \cos x}{\sin x}$ in $t$"
$\frac{1 - \cos x}{\sin x} = \frac{1 - \frac{1 - t^{2}}{1 + t^{2}}}{\frac{2t}{1 + t^{2}}} = \frac{\frac{2t^{2}}{1 + t^{2}}}{\frac{2t}{1 + t^{2}}} = t = \tan\frac{x}{2}$ ✓ — consistent with the half-angle identity of Part I. Any rational $R(\sin x, \cos x)$ now reduces by $t$-clearing denominators; $1 + t^{2} \ne 0$ is automatic for real $t$.
:::

## Assumptions & conventions

$A$ real with $A \ne \pi + 2k\pi$ under the substitution; the blind spot is checked separately in every problem; rational expressions in $\sin, \cos$ mean ratios of polynomials; all conversions verified back in the original equation.
