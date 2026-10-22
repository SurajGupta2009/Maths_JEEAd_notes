---
id: jee-06
part: jee
title: "Common Roots and Transformed Equations — Putting Quadratics Together"
---

## A common root

:::key title="Subtract first, condition later"
If $ax^{2} + bx + c = 0$ and $a'x^{2} + b'x + c' = 0$ share a root $\alpha$, subtracting kills the $x^{2}$ term (after scaling to equalise leading coefficients): the common root satisfies a **linear** equation, and is usually immediate. The textbook condition

$$(bc' - b'c)^{2} = (ab' - a'b)(ac' - a'c)$$

is the same statement after elimination — correct but slow; reach for it only when subtraction degenerates (identical or proportional equations, which share *both* roots: coefficients proportional, $\frac{a}{a'} = \frac{b}{b'} = \frac{c}{c'}$).
:::

:::example title="Worked — common roots"
$x^{2} - 5x + 6 = 0$ and $x^{2} - 4x + 3 = 0$: subtract, $-x + 3 = 0$, so the common root is $x = 3$ (check: $9 - 15 + 6 = 0$ ✓, $9 - 12 + 3 = 0$ ✓).

If $x^{2} + ax + b = 0$ and $x^{2} + bx + a = 0$ ($a \neq b$) share a root: subtracting gives $(a - b)(x - 1) = 0$, so the common root is $1$ and substituting gives $a + b + 1 = 0$.
:::

## Transformed roots

:::key title="Build from new S and new P — or substitute and skip the algebra"
- Roots $\alpha + k, \beta + k$: new sum $S + 2k$, new product $P + kS + k^{2}$. Equivalent shortcut: replace $x$ by $x - k$ in the original equation.
- Roots $\frac{1}{\alpha}, \frac{1}{\beta}$ ($P \neq 0$): new sum $\frac{S}{P}$, new product $\frac{1}{P}$. Shortcut: reverse the coefficients — $cx^{2} + bx + a = 0$.
- Roots $k\alpha, k\beta$: sum $kS$, product $k^{2}P$. Shortcut: replace $x$ by $\frac{x}{k}$ and clear.
- Roots $\alpha^{2}, \beta^{2}$: sum $S^{2} - 2P$, product $P^{2}$.
- Roots $\alpha^{3}, \beta^{3}$: sum $S^{3} - 3PS$, product $P^{3}$.
:::

:::example title="Worked — transformations"
From $x^{2} - 5x + 6 = 0$ ($S = 5$, $P = 6$): roots $\alpha + 1, \beta + 1$ give sum $7$, product $6 + 5 + 1 = 12$, equation $x^{2} - 7x + 12 = 0$ (actual roots $3, 4$ ✓). Reciprocals give sum $\frac{5}{6}$, product $\frac{1}{6}$, equation $6x^{2} - 5x + 1 = 0$ (actual $\frac{1}{2}, \frac{1}{3}$ ✓).
:::

:::warn title="Common traps — common and transformed roots"
- The squared-roots equation has product $P^{2}$, not $P$.
- Reciprocal transformation silently assumes neither root is $0$; if $c = 0$ the "reciprocal equation" drops degree.
- Common-root condition memorised with the factors in the wrong pairing — derive by elimination if unsure, or just subtract.
- Two quadratics can share both roots without being identical: proportional coefficients are enough.
:::

:::app title="The graph view (what the algebra is saying)"
$y = ax^{2} + bx + c$: vertex $\left(-\frac{b}{2a}, \frac{4ac - b^{2}}{4a}\right)$, axis $x = -\frac{b}{2a}$, meets the axis iff $D \geq 0$, opens up iff $a > 0$. Shifting roots by $k$ translates the graph; reversing coefficients reflects the root set by $r \mapsto \frac{1}{r}$. Every transformation above is a picture before it is a formula.
:::
