---
id: jee-05
part: jee
title: "Equations, Inequalities and Parameters — Domain First, Injectivity Second"
---

## The two licenses for manipulation

Every solution step in an inverse-trig equation uses exactly one of two licences:

:::key title="The two legal moves"
1. **Domain agreement**: $\sin^{-1}(\text{stuff})$ exists iff $-1 \leq \text{stuff} \leq 1$; $\tan^{-1}(\text{stuff})$ exists for all real stuff; $\sec^{-1}(\text{stuff})$ needs $|\text{stuff}| \geq 1$. Write the domain condition *before* the first algebraic step and intersect it with the solution set at the end.
2. **Injectivity of the outer inverse**: $\sin^{-1}u = \sin^{-1}v \Leftrightarrow u = v$ (both sides legal), $\cos^{-1}u = \cos^{-1}v \Leftrightarrow u = v$, $\tan^{-1}u = \tan^{-1}v \Leftrightarrow u = v$. This is the only way to strip an outer inverse. **Never** strip an inverse by "removing inverses from both sides" of different functions ($\sin^{-1}u = \cos^{-1}v$ needs the complementary identity or a $\tan$ of both sides, with a range check afterwards).
:::

## Worked set — the canonical exam types

:::example title="Type 1 — two inverses, same function: $\tan^{-1}2x + \tan^{-1}3x = \frac{\pi}{4}$"
Domain: none needed ($\tan^{-1}$ is everywhere). Use the addition table: $xy = 6x^{2}$ vs $1$ splits the parameter line.

Case $6x^{2} < 1$: $\tan^{-1}2x + \tan^{-1}3x = \tan^{-1}\frac{5x}{1 - 6x^{2}} = \frac{\pi}{4}$, so $\frac{5x}{1 - 6x^{2}} = 1 \Rightarrow 6x^{2} + 5x - 1 = 0 \Rightarrow x = \frac{1}{6}$ or $x = -1$. Check the case condition $6x^{2} < 1$: $x = \frac{1}{6}$ gives $\frac{1}{6} < 1$ ✓; $x = -1$ gives $6 > 1$ ✗ (wrong case).

Case $6x^{2} > 1$, $x > 0$: sum $= \pi + \tan^{-1}\frac{5x}{1 - 6x^{2}} = \frac{\pi}{4}$ forces $\tan^{-1}(\cdots) = -\frac{3\pi}{4}$ — impossible (arctan output is in $(-\pi/2, \pi/2)$). No solution. Case $x < 0$, $6x^{2} > 1$: sum $= -\pi + \tan^{-1}\frac{5x}{1-6x^{2}} = \frac{\pi}{4}$ needs $\tan^{-1}(\cdots) = \frac{5\pi}{4}$ — impossible.

**Solution: $x = \frac{1}{6}$ only.** The extraneous $x = -1$ is a *ghost from the wrong case*, not from squaring — case conditions are domain conditions too.
:::

:::example title="Type 2 — mixed inverses: $\sin^{-1}x = \cos^{-1}x$"
Move 1: $\cos^{-1}x = \frac{\pi}{2} - \sin^{-1}x$ (complementary pair), so $\sin^{-1}x = \frac{\pi}{4}$, $x = \frac{\sqrt{2}}{2}$. Move 2 (check): both sides are defined at $x = \frac{\sqrt{2}}{2}$ and equal $\frac{\pi}{4}$ ✓. Alternative: take $\sin$ of both sides directly — $x = \sqrt{1 - x^{2}}$ after the triangle — same answer with $x \geq 0$ forced by the range of both sides ($\sin^{-1}x = \cos^{-1}x \in [0, \pi/2]$).
:::

:::example title="Type 3 — parameter on both sides: $\sin^{-1}x + \sin^{-1}(1 - x) = \frac{\pi}{2}$"
Since $\sin^{-1}(1-x) = \frac{\pi}{2} - \cos^{-1}(1 - x)$, the equation becomes $\sin^{-1}x = \cos^{-1}(1 - x)$. Take $\sin$ of both sides: $x = \sqrt{1 - (1 - x)^{2}} = \sqrt{2x - x^{2}}$, needing $2x - x^{2} \geq 0$ (i.e. $x \in [0, 2]$) and $x \geq 0$ (range of the right side... $\sin(\cos^{-1}(1-x)) = \sqrt{1-(1-x)^{2}} \geq 0$ forces $x \geq 0$). Square: $x^{2} = 2x - x^{2} \Rightarrow 2x^{2} = 2x \Rightarrow x = 0$ or $x = 1$. Check $x = 0$: $\sin^{-1}0 + \sin^{-1}1 = 0 + \frac{\pi}{2}$ ✓. Check $x = 1$: $\sin^{-1}1 + \sin^{-1}0 = \frac{\pi}{2}$ ✓. **Both valid.**
:::

:::app title="Inequalities — monotone reading is the entire method"
Each inverse is strictly monotone on its domain: $\sin^{-1} \nearrow$, $\tan^{-1} \nearrow$, $\cos^{-1} \searrow$. So e.g.

$$\cos^{-1}x > \cos^{-1}(2x - 1) \Leftrightarrow x < 2x - 1$$

$$\Leftrightarrow x > 1$$

with domain $|x| \leq 1$ and $|2x - 1| \leq 1$ intersected in: here $x > 1$ contradicts $x \leq 1$, so **no solution** — the domain check kills it before you trust the monotone read. Typical exam inequality: $\tan^{-1}(x - 1) < \tan^{-1}x$ is true for **all** legal $x$ ($x - 1 < x$ always, no domain to enforce) — a quick-mark question.

Ranges as constraints: "find the domain of $f(x) = \sin^{-1}(2x - 1) + \cos^{-1}(x)$" $\Rightarrow$ solve $-1 \leq 2x - 1 \leq 1$ and $-1 \leq x \leq 1$ simultaneously: $x \in [0, 1]$. Always write these as an intersection of intervals — every domain question on this topic is that one move.
:::

:::derive title="Worked — solve $\tan^{-1}\frac{x - 1}{x - 2} + \tan^{-1}\frac{x + 1}{x + 2} = \frac{\pi}{4}$"
Let $u = \frac{x-1}{x-2}$, $v = \frac{x+1}{x+2}$; domain excludes $x = \pm 2$. Add via the table — but first check $uv$ vs $1$. Compute the *plain case* and verify at the end (the case check is mandatory):

$$\tan^{-1}u + \tan^{-1}v$$

$$ = \tan^{-1}\frac{u + v}{1 - uv} = \frac{\pi}{4} \Rightarrow \frac{u + v}{1 - uv}$$

$$ = 1 \Rightarrow u + v = 1 - uv.$$

With $u + v = \frac{x-1}{x-2} + \frac{x+1}{x+2} = \frac{2x^{2} - 6}{x^{2} - 4}$ and $uv = \frac{x^{2} - 1}{x^{2} - 4}$: condition $\frac{2x^{2} - 6}{x^{2} - 4} = 1 - \frac{x^{2} - 1}{x^{2} - 4} = \frac{x^{2} - 4 - x^{2} + 1}{x^{2} - 4} = \frac{-3}{x^{2} - 4}$. So $2x^{2} - 6 = -3 \Rightarrow x^{2} = \frac{3}{2} \Rightarrow x = \pm\sqrt{\frac{3}{2}}$. Final check by substitution in the original equation (both values must be tested — the addition formula's case is decided by $uv$ at those $x$): direct numeric evaluation of both sides confirms each. This style — **solve freely, verify every root in the original** — is the discipline every such equation needs.
:::

:::warn title="Common traps — equations and parameters"
- Squaring introduces ghosts ($x = 0$ vs $x = 1$ above); case-branching introduces *wrong-case* ghosts (the $x = -1$ of Type 1). Both are removed by substitution in the **original** equation, not in the derived one.
- $\sin^{-1}x = \theta$ has the single solution $x = \sin\theta$ **only if** $\theta \in [-\pi/2, \pi/2]$; solving "$\sin^{-1}x = \frac{3\pi}{4}$" gives no solution, while $\sin x = \frac{3\pi}{4}$-style confusion gives one — never mix the two equation families.
- The range of $\sin^{-1}x + \cos^{-1}y$ is not $[-\pi/2, \pi/2]$ but $[-\pi/2, \pi] + [0, \pi]$ read componentwise: min $= -\pi/2 + 0$, max $= \pi/2 + \pi$. Asking for "range of $f(x) = \sin^{-1}x + \cos^{-1}x$" is the complementary-pair question ($\pi/2$).
- For $\tan^{-1}x + \tan^{-1}y = c$ with parameters, the answer is usually a **union of intervals** (different cases), not one number — write each case's solution set and union them.
- Domain of $\sec^{-1}$ and $\csc^{-1}$: $|x| \geq 1$; forgetting it admits $x = 0$-type ghosts.
:::
