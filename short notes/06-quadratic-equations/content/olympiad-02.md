---
id: olympiad-02
part: olympiad
title: "Extension — The Discriminant as an Invariant, Rational Roots, and Solving Cubics by Quadratics"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
The discriminant as $a^{2}(\alpha - \beta)^{2}$, rational-root criteria, and the resolvent solution of the cubic are classical extension material beyond the official quadratic-equations syllabus line.
:::

:::key title="What the discriminant actually measures"
$$\Delta = b^{2} - 4ac = a^{2}(\alpha - \beta)^{2}$$

The factor $a^{2} > 0$ is pure scale: the **sign** of $\Delta$ is the sign of $(\alpha - \beta)^{2}$ — positive (distinct real), zero (coincident), negative (non-real conjugates, where $\alpha - \beta$ is purely imaginary). The **value** measures root separation. One number, complete information.
:::

:::key title="Rational roots are a perfect-square question"
For rational $a, b, c$: roots rational $\Leftrightarrow$ $\Delta$ is the square of a rational. Worked: $x^{2} - kx + (k - 1) = 0$ has $\Delta = k^{2} - 4k + 4 = (k - 2)^{2}$, a perfect square for **every** integer $k$; roots $x = \frac{k \pm |k - 2|}{2} = 1, k - 1$ (indeed $x^{2} - kx + k - 1 = (x - 1)(x - k + 1)$ ✓).
:::

:::derive title="Lagrange's resolvent — a cubic solved by one quadratic"
For $x^{3} + px^{2} + qx + r = 0$, the shift $x = y - \frac{p}{3}$ kills the square term: depressed cubic $y^{3} + Py + Q = 0$. Set $y = u + v$; then $y^{3} = u^{3} + v^{3} + 3uv\,y$, so matching needs $3uv = -P$ and $u^{3} + v^{3} = -Q$. Hence $u^{3}v^{3} = -\frac{P^{3}}{27}$, and $u^{3}, v^{3}$ are the roots of the **resolvent quadratic**

$$t^{2} + Qt - \frac{P^{3}}{27} = 0$$

Solve it, take cube roots *chosen with $uv = -\frac{P}{3}$* (the pairing constraint is essential — arbitrary cube roots give wrong $y$), and $y = u + v$. Worked: $x^{3} - 6x^{2} + 11x - 6 = 0$: $x = y + 2$ gives $y^{3} - y = 0$; resolvent $t^{2} + \frac{1}{27} = 0$; the three admissible $(u, v)$ pairings give $y = 1, 0, -1$, so $x = 1, 2, 3$ ✓ (sum $6 = -p$, product $6 = -r$ ✓).
:::

:::intuition title="Why the ladder stops at degree 4"
Quadratic $\to$ cubic (resolvent quadratic) $\to$ quartic (resolvent cubic): each degree is solved by the previous. At degree 5 the ladder provably ends — the general quintic is not solvable by radicals (Abel–Ruffini), and the explanation of *why* is Galois theory. The resolvent is the last rung reachable by pure algebra.
:::

:::warn title="Common traps — resolvents and discriminants"
- Taking cube roots of $u^{3}, v^{3}$ independently: the three choices must satisfy $uv = -\frac{P}{3}$.
- "Rational coefficients" hypothesis dropped: $\Delta$ a perfect square decides rationality only over $\mathbb{Q}$.
- $\Delta = a^{2}(\alpha-\beta)^{2}$, not $(\alpha - \beta)^{2}$ — the $a^{2}$ matters for exact values.
:::
