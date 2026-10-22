---
id: jee-05
part: jee
title: "Exponential & Logarithmic Equations — Methods with Domain Checks"
---

## The four structural types

**Type 1 — common base.** $a^{f(x)} = a^{g(x)}$ with $a > 0$, $a \ne 1$ $\Rightarrow f(x) = g(x)$. If the bases differ but are related ($4^{x} = 8^{x-1}$), convert: $2^{2x} = 2^{3x-3} \Rightarrow x = 3$.

**Type 2 — quadratic in an exponential.** $a^{2x} + B a^{x} + C = 0$: substitute $t = a^{x} > 0$, solve, then reject $t \leq 0$ and take $x = \log_{a} t$.

**Type 3 — logarithmic equation to exponential.** Isolate a single log, then rewrite: $\log_{2}(x-3) = 4 \Rightarrow x - 3 = 2^{4} \Rightarrow x = 19$. If logs remain, use laws to **collapse** to one log first: $\log_{2}(x-3) + \log_{2}(x+1) = 3 \Rightarrow \log_{2}\!((x-3)(x+1)) = 3$.

**Type 4 — $x$ in base and argument.** $x^{\log_{2} x} = 16$-type: take $\log_{2}$: $(\log_{2} x)^{2} = 4 \Rightarrow \log_{2} x = \pm 2 \Rightarrow x = 4$ or $x = \frac{1}{4}$. Both check out (a power $x^{y}$ with $x > 0$ is always legal).

:::diagram
{"type": "numberline", "xrange": [-1, 6], "xticks": [-1, 0, 1, 2, 3, 4, 5, 6], "title": "Domain checks turn 'solutions' into verified roots — worked example 2: only x = 2 + 2√3 survives", "marks": [{"kind": "interval", "a": 3, "b": 6, "label": "domain x > 3", "color": "#0F766E"}, {"kind": "points", "pts": [4.464], "label": "x = 1 + 2√3 ✓", "color": "#B91C1C"}, {"kind": "points", "pts": [-2.464], "label": "1 − 2√3 ✗ (outside)", "color": "#5B6B84", "offrange": true}]}
:::

## The domain-first discipline

Every log equation has an **implicit domain**: each $\log(\cdot)$ needs its argument $> 0$; every $a^{x}$ is fine on $\mathbb{R}$ for $a > 0$; $x^{p/q}$ needs the parity care of sheet 1. Solve **first** on the domain, then verify — or solve freely and **filter at the end**. Either way the final answer must be checked in the *original* equation, because squaring, exponentiating, and multiplying by logs can create ghosts.

:::derive title="Worked 1. $2^{2x} - 5 \cdot 2^{x} + 4 = 0$ (type 2)"
$t = 2^{x}$, $t > 0$: $t^{2} - 5t + 4 = 0 \Rightarrow t = 1, 4$, both admissible. $2^{x} = 1 \Rightarrow x = 0$; $2^{x} = 4 \Rightarrow x = 2$. Substitute back: $x = 0$ gives $1 - 5 + 4 = 0$ ✓; $x = 2$ gives $16 - 20 + 4 = 0$ ✓. Answer $\{0, 2\}$.
:::

:::derive title="Worked 2. $\log_{2}(x-3) + \log_{2}(x+1) = 3$ (type 3)"
Domain: $x > 3$ **and** $x > -1$, so $x > 3$. Collapse: $\log_{2}\!((x-3)(x+1)) = 3 \Rightarrow (x-3)(x+1) = 8 \Rightarrow x^{2} - 2x - 11 = 0 \Rightarrow x = 1 \pm 2\sqrt{3}$. Only $1 + 2\sqrt{3} \approx 4.464$ lies in $x > 3$; $1 - 2\sqrt{3} < 0$ is a ghost created by the algebra (it would make the original logs undefined). Answer: $x = 1 + 2\sqrt{3}$.
:::

:::example title="Worked 3. $x^{\lg x} = 10^{4}$ (type 4)"
Take $\lg$ of both sides (both positive): $(\lg x)(\lg x) = 4 \Rightarrow (\lg x)^{2} = 4 \Rightarrow \lg x = \pm 2 \Rightarrow x = 100$ or $x = 10^{-2} = 0.01$. Check: $100^{\lg 100} = 100^{2} = 10^{4}$ ✓; $(0.01)^{\lg 0.01} = (10^{-2})^{-2} = 10^{4}$ ✓. Both answers valid.
:::

:::warn title="Common traps — equations edition"
- **Collapsing logs** $\log A + \log B = \log(AB)$ requires $A, B > 0$ — the domain shrinks, it does not grow.
- Squaring both sides (e.g. when clearing $\sqrt{\cdot}$ or $|\cdot|$) creates ghost roots — verify each one.
- $\log_{a} f = \log_{a} g \Rightarrow f = g$ **plus** $f, g > 0$; never cancel logs before writing the domain.
- Exponentiating $e^{A} = e^{B}$ is reversible for all real $A, B$; but $A^{2} = B^{2} \Rightarrow A = \pm B$ — do not "cancel squares".
- If a base depends on $x$ ($x^{\log x}$, $\log_{x} 2$), add the conditions $x > 0$, $x \ne 1$ (base rule) on top of argument rules.
:::
