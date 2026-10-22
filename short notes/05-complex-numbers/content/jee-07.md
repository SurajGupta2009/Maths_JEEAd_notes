---
id: jee-07
part: jee
title: "Equations in z and z̄ — Two Methods, One Discipline"
---

## The exam's native equation type

Real-variable techniques assume the unknown appears "purely"; JEE mixes $z$ and $\bar z$: $2z + i\bar z = 5 + 2i$, or $|z| + z = 1 + i$. Two systematic methods exist; run the second as a check on the first.

:::key title="Method 1 — real and imaginary parts (always works)"
Write $z = a + bi$, $\bar z = a - bi$, expand, equate components. Two real linear equations in $a, b$ — mechanical and bulletproof. Reach for it under pressure.
:::

:::key title="Method 2 — the conjugate trick (fast, linear equations only)"
If the equation is linear in $z$ and $\bar z$ — $\alpha z + \beta \bar z = c$ — conjugate it: $\bar\alpha \bar z + \bar\beta z = \bar c$. Now solve the $2 \times 2$ system in the unknowns $z, \bar z$. Watch the sign: $\bar i = -i$.
:::

:::example title="Worked — $2z + i\bar z = 5 + 2i$ both ways"
Method 1: $2(a + bi) + i(a - bi) = (2a + b) + i(2b + a) = 5 + 2i$, so $2a + b = 5$, $a + 2b = 2$: subtract twice the second from the first: $-3b = 1 \Rightarrow b = -\frac{1}{3}$, $a = \frac{8}{3}$.

Method 2: conjugate: $2\bar z - iz = 5 - 2i$. Multiply by $i$: $2i\bar z + z = i(5 - 2i) = 2 + 5i$. Subtract from the original: $(2z + i\bar z) - (z + 2i\bar z) = z - i\bar z = 3 - 3i$. Add to the original: $3z = 8 - i \Rightarrow z = \frac{8}{3} - \frac{1}{3}i$ ✓ same answer.

Check by substitution (mandatory): $2(\frac{8}{3} - \frac{i}{3}) + i(\frac{8}{3} + \frac{i}{3}) = \frac{16}{3} - \frac{2i}{3} + \frac{8i}{3} - \frac{1}{3} = 5 + 2i$ ✓.
:::

:::app title="The $z + \bar z = 2\operatorname{Re} z$ family — linear in the parts"
Equations like $z + \bar z = 4$, $z - \bar z = 6i$ solve by adding/subtracting: $2\operatorname{Re} z = 4$, $2i\operatorname{Im} z = 6i \Rightarrow z = 2 + 3i$. "$2\bar z - 3z$ is purely imaginary": expand $-a - 5bi$; real part $= 0 \Leftrightarrow a = 0$: the whole imaginary axis (including $0$). "Purely imaginary $\Leftrightarrow z + \bar z = 0$"; "real $\Leftrightarrow z - \bar z = 0$"; "$|z| = r$ with $z = x + iy$": $x^{2} + y^{2} = r^{2}$.
:::

## Quadratics with real coefficients — conjugate roots

If $x^{2} + bx + c = 0$ has real coefficients and discriminant $\Delta = b^{2} - 4c < 0$, the roots are $z_{1,2} = \frac{-b}{2} \pm i\frac{\sqrt{4c - b^{2}}}{2}$ — automatically conjugates. JEE asks for *quantities built from* the roots.

:::key title="Root-distance formulas (no root-finding needed)"
For $x^{2} + bx + c = 0$, $b, c$ real, $\Delta < 0$: with $z_{2} = \bar z_{1}$:

$$|z_{1} - z_{2}| = \sqrt{4c - b^{2}} = \sqrt{|\Delta|},$$

$$|z_{1} - \bar z_{1}| = \sqrt{4c - b^{2}} \ \text{(same number)}$$

$$|z_{1}| = \sqrt{c} \ \text{(when } c > 0\text{)}, \qquad \operatorname{Re} z_{1} = -\frac{b}{2}$$

Worked: $x^{2} - 4x + 13 = 0$: $\Delta = -36$, roots $2 \pm 3i$: $|z_{1} - z_{2}| = |6i| = 6 = \sqrt{36}$ ✓, $|z_{1}| = \sqrt{13}$ ✓. The point of the formulas: never compute the roots themselves when the question is a modulus/distance.
:::

:::derive title="Why conjugate roots — one line"
Complex roots of a real polynomial come in conjugate pairs because conjugating $p(z) = 0$ (legal: conjugation respects sums and products, $\bar 1 = 1$) gives $p(\bar z) = 0$. So $\bar z_{1}$ is a root whenever $z_{1}$ is; for a quadratic the two roots are exactly $\{z_{1}, \bar z_{1}\}$ (distinct when $\Delta \neq 0$). The same argument locks every degree: real polynomials have conjugate-symmetric root sets — Vieta's real coefficients are the algebraic shadow of the reflection symmetry.
:::

:::assume title="Scope and conventions"
- "$z$ and $\bar z$ equations" are solved over $\mathbb{C}$ with $z = a + bi$, $a, b \in \mathbb{R}$; "purely imaginary" includes $0$ unless a problem excludes it explicitly.
- Quadratics in this sheet have **real** coefficients (stated each time); complex coefficients can have non-conjugate root pairs — then only Method 1 applies.
- $|z_{1} - z_{2}| = \sqrt{|\Delta|}$ assumes $|a| = 1$ leading coefficient; for $ax^{2} + bx + c$ scale first.
:::

:::warn title="Common traps — equations"
- Method 2's conjugation step: $\overline{i\bar z} = -iz$, not $i z$. A sign slip here poisons both methods' agreement.
- "Purely imaginary" allows $0$; "imaginary" sometimes means "non-real" in problem text — read the convention in the question.
- $|z_{1} - z_{2}| = \sqrt{|\Delta|}$ needs $\Delta < 0$ and real coefficients; with $\Delta > 0$ the roots are real and $|z_{1} - z_{2}| = \sqrt{\Delta}$ (no conjugates involved).
- Cancelling $z$ or $\bar z$ terms across an equation without checking $z = 0$ cases: $z\bar z = |z|^{2}$ vanishes only at $z = 0$ — test it.
- $|z| + z = 1 + i$-type: modulus equations are **non-linear** — Method 2 fails; split into parts and use $|z| = \sqrt{a^{2} + b^{2}} \geq 0$ as an extra unknown with a consistency condition ($a^{2} + b^{2} = $ the squared equation).
:::
