---
id: jee-02
part: jee
title: "Vieta's Relations and Symmetric Functions — Never Solve for the Roots"
---

## The two relations that do all the work

:::derive title="Vieta from factorising"
If $\alpha, \beta$ are the roots, then $ax^{2} + bx + c = a(x - \alpha)(x - \beta) = a\left(x^{2} - (\alpha + \beta)x + \alpha\beta\right)$. Comparing coefficients:

$$S = \alpha + \beta = -\frac{b}{a}, \qquad P = \alpha\beta = \frac{c}{a}$$

Watch the signs: sum carries the minus, product does not. The derivation also shows why Vieta survives in $\mathbb{C}$: factorisation needs no reality.
:::

:::key title="The symmetric-function toolkit (all from S and P)"
$$\alpha^{2} + \beta^{2} = S^{2} - 2P, \qquad \alpha^{3} + \beta^{3} = S^{3} - 3PS$$

$$\alpha^{2}\beta + \alpha\beta^{2} = PS, \qquad \frac{1}{\alpha} + \frac{1}{\beta} = \frac{S}{P} \quad (P \neq 0)$$

$$(\alpha - \beta)^{2} = S^{2} - 4P = \frac{D}{a^{2}}, \qquad \left|\alpha - \beta\right| = \frac{\sqrt{D}}{\left|a\right|} \ (D \geq 0)$$

$$\frac{\alpha}{\beta} + \frac{\beta}{\alpha} = \frac{S^{2} - 2P}{P}, \qquad \alpha^{2} - \beta^{2} = (\alpha - \beta)S$$

Deep reason: swapping $\alpha \leftrightarrow \beta$ changes no coefficient, so any *symmetric* expression must be expressible through $S, P$ alone. $\alpha - \beta$ is **not** symmetric — that is exactly why the discriminant has to be brought in for it.
:::

:::example title="Worked — everything from S and P, roots never found"
For $x^{2} - 5x + 6 = 0$: $S = 5$, $P = 6$. Then $\alpha^{2} + \beta^{2} = 25 - 12 = 13$; $\alpha^{3} + \beta^{3} = 125 - 90 = 35$; $\frac{1}{\alpha} + \frac{1}{\beta} = \frac{5}{6}$; $(\alpha - \beta)^{2} = 25 - 24 = 1$; $\alpha^{2}\beta + \alpha\beta^{2} = 30$; $\frac{\alpha}{\beta} + \frac{\beta}{\alpha} = \frac{13}{6}$. (Roots are $2, 3$ — check: $4 + 9 = 13$, $8 + 27 = 35$ ✓.)

For $3x^{2} - 7x + 2 = 0$: $S = \frac{7}{3}$, $P = \frac{2}{3}$ directly — solving ($x = 2, \frac{1}{3}$) is wasted effort.
:::

:::warn title="Common traps — Vieta"
- $(\alpha - \beta)^{2} = S^{2} - 4P$, not $S^{2} - 2P$ (that is $\alpha^{2} + \beta^{2}$). The cross-term doubles.
- $\left|\alpha - \beta\right| = \sqrt{S^{2} - 4P}$ needs $D \geq 0$ to be a real distance; over $\mathbb{C}$ only $(\alpha - \beta)^{2}$ is meaningful.
- Reciprocal identities need $P \neq 0$, i.e. $c \neq 0$: a zero root has no reciprocal.
- $\alpha - \beta$ has a sign ambiguity; problems asking for it usually want $\left|\alpha - \beta\right|$ or $(\alpha - \beta)^{2}$.
:::

## Forming an equation from its roots

:::key title="The reverse direction"
Roots $r_{1}, r_{2}$ $\Rightarrow$ equation $x^{2} - (r_{1} + r_{2})x + r_{1}r_{2} = 0$ (monic form; multiply out to clear fractions). This is the whole of "form the equation whose roots are …": compute the **new sum** and **new product**, never the roots themselves.

Roots $\alpha^{2}, \beta^{2}$ for $x^{2} - 5x + 3 = 0$ ($S = 5, P = 3$): new sum $= S^{2} - 2P = 19$, new product $= P^{2} = 9$, so $x^{2} - 19x + 9 = 0$. Note product $P^{2}$, not $P$ — checklist item.
:::

:::app title="Where this is used everywhere else"
Condition problems ("roots in ratio $m:n$", "one root is the square of the other", "roots differ by $k$") are all Vieta plus one extra equation. E.g. roots differing by 1 for $x^{2} - 5x + 6$: $(\alpha-\beta)^{2} = S^{2} - 4P = 1$ gives the difference without solving. Ratio $m : n$: set roots $m t, n t$, then $S = (m+n)t$ and $P = mn\,t^{2}$, so $P(m+n)^{2} = mn\,S^{2}$ — eliminate $t$ immediately.
:::
