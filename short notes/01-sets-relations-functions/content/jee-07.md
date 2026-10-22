---
id: jee-07
part: jee
title: "One-one, Onto, Even / Odd, Periodic — the Classification Sheet"
---

## Injective, surjective, bijective

- **One-one (injective):** $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$. Test: horizontal line test on the graph; or solve $f(x_1) = f(x_2)$ and cancel. Strictly monotone (increasing or decreasing) on an interval $\Rightarrow$ one-one there.
- **Onto (surjective):** range $=$ codomain. "Into" just means not onto. To prove onto: for arbitrary $y$ in the codomain, exhibit $x$ with $f(x) = y$ and check $x$ lies in the domain.
- **Bijection:** both. Exactly then does the inverse function $f^{-1}$ exist (see the composition & inverse sheet).

:::diagram
{
  "type": "graph",
  "title": "Horizontal line test: y = x^2 is not one-one on R (line y = 4 crosses twice) but y = x^3 is",
  "xrange": [-2.6, 2.6],
  "yrange": [-5, 5],
  "xticks": [-2, -1, 0, 1, 2],
  "yticks": [-4, -2, 0, 2, 4],
  "curves": [
    {"expr": "x*x", "color": "#B8860B", "lw": 2.6, "label": "y = x^2"},
    {"expr": "x*x*x/2", "color": "#0F766E", "lw": 2.6, "label": "y = x^3/2"}
  ],
  "hlines": [{"y": 4, "label": "y = 4: two hits on x^2, one hit on x^3/2"}],
  "points": [
    {"x": -2, "y": 4, "label": "(-2, 4)", "color": "#B91C1C", "dy": 0.4, "dx": -1.35},
    {"x": 2, "y": 4, "label": "(2, 4)", "color": "#B91C1C", "dy": 0.4, "dx": 0.15}
  ]
}
:::

:::derive title="How many functions A to B?"
Each of the $n(A)$ inputs independently chooses one of the $n(B)$ outputs — product rule: $|B|^{|A|}$ functions. Among them: **injections** $= n(B)(n(B)-1)\cdots(n(B)-n(A)+1) = P(n(B), n(A))$ if $n(A) \leq n(B)$, else $0$ (pigeonhole: more inputs than outputs forces a collision). **Bijections** $= n(A)!$ when $n(A) = n(B)$. **Surjections:** if $n(A) < n(B)$ none exist; otherwise count by cases for tiny sets — $f : \{1,2,3\} \to \{a,b\}$ has $2^3 = 8$ functions total, exactly $2$ constant, so $8 - 2 = 6$ onto (each value must appear, i.e. not all three go to one side). The general inclusion–exclusion formula is Part II material; this case analysis is fully syllabus-level.
:::

:::key
Small-case table for $|A| = 3, |B| = 2$: total functions $= 8$; one-one $= 0$; onto $= 6$; constant $= 2$. For $|A| = 2, |B| = 3$: total $= 9$; one-one $= 3 \cdot 2 = 6$; onto $= 0$; constant $= 3$. Memorise the *shape* of the table, not just the numbers — the constraints ($n(A) \leq n(B)$ for injective, $n(A) \geq n(B)$ for surjective) are what get tested.
:::

## Even and odd functions

Requires a domain **symmetric about 0** (if $x$ is allowed so is $-x$). Then $f$ is **even** if $f(-x) = f(x)$ (graph symmetric about the $y$-axis), **odd** if $f(-x) = -f(x)$ (graph symmetric about the origin; rotation by $180^\circ$).

:::derive title="Every function splits into even + odd parts"
$f(x) = g(x) + h(x)$ where $g(x) = \frac{f(x) + f(-x)}{2}$ (even part) and $h(x) = \frac{f(x) - f(-x)}{2}$ (odd part). Check: $g(-x) = \frac{f(-x)+f(x)}{2} = g(x)$; $h(-x) = \frac{f(-x)-f(x)}{2} = -h(x)$. The split is unique. Consequences worth knowing: an odd $f$ with $0$ in its domain has $f(0) = 0$; even $\pm$ even $=$ even, odd $\pm$ odd $=$ odd; even $\times$ odd $=$ odd; $f \cdot f$ is even whenever $f$ is odd or even.
:::

:::warn
- $f(x) = x^{2}$ on $[0,1]$ is **neither** even nor odd — the domain is not symmetric. Check the domain before the formula.
- $f(x) = x + 1$ is neither (sum of odd $x$ and even $1$ — sums of mixed parity are usually neither).
- $f(0) = 0$ is *necessary* for odd functions defined at 0, not sufficient ($f(x) = x^3 + x$ odd ✓, $f(x) = x^2$ has $f(0)=0$ but is even).
:::

## Periodic functions

$f$ is **periodic** with period $T > 0$ if $f(x + T) = f(x)$ for all $x$ (domain must allow $x + T$). The least such $T$ is the **fundamental period** ("the period" in exam language).

:::key
Periods: $\sin x, \cos x$: $2\pi$; $\tan x$: $\pi$; $\sin(ax + b), \cos(ax+b)$: $\frac{2\pi}{|a|}$; $\tan(ax+b)$: $\frac{\pi}{|a|}$; $|\sin x|$, $\sin^{2}x$, $\cos^{2}x$: $\pi$ (taking absolute value or squaring merges the two halves); $\lfloor x \rfloor, \{x\}$: $1$; a constant function satisfies $f(x+T)=f(x)$ for every $T$ — it is periodic but has **no** fundamental period.
:::

:::example
**Worked.** Period of $f(x) = \sin\left(\frac{x}{2}\right) + \cos(3x)$. First term: $\frac{2\pi}{1/2} = 4\pi$. Second: $\frac{2\pi}{3}$. Candidate period $= \operatorname{lcm}(4\pi, \frac{2\pi}{3}) = 4\pi$ (need $T = k \cdot 4\pi = m \cdot \frac{2\pi}{3}$; least positive is $4\pi$). **Check:** $f(x + 4\pi) = \sin(\frac{x}{2} + 2\pi) + \cos(3x + 12\pi) = f(x)$ ✓. Trap: lcms only exist for *commensurable* periods ($T_1/T_2 \in \mathbb{Q}$); $\sin x + \sin(\pi x)$ is periodic only in trivial senses — never assume a combined period exists.
:::

:::app
**Standard application.** $f(x) = \sin^{2}\left(\frac{x}{2}\right)$: use $\sin^{2}\theta = \frac{1 - \cos 2\theta}{2} = \frac{1 - \cos x}{2}$, whose period is $2\pi$ — while naive reading suggests $\frac{2\pi}{1/2}=4\pi$ for $\sin(x/2)$ then squaring halves it to $2\pi$. Reduce with identities first, then read off the period; the two-stage guess $4\pi$ is wrong.
:::
