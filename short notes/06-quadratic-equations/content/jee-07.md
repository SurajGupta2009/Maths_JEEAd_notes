---
id: jee-07
part: jee
title: "Parameter Problems and the Recap Toolkit — The JEE Question Shapes"
---

## The five shapes every parameter problem takes

:::key title="Shape recognition"
1. **Nature prescribed** ("real/distinct/equal/non-real roots"): write $D$ and solve the inequality — plus the $a \neq 0$ degeneracy check.
2. **Condition between roots** ("one root is double the other", "roots differ by 2", "reciprocals of each other"): Vieta plus the extra relation. Reciprocals condition: $P = 1$, i.e. $c = a$. One root double: roots $t, 2t$, so $S = 3t$, $P = 2t^{2}$, eliminate: $9P = 2S^{2}$ (for the monic-scaled $S, P$).
3. **Sign prescribed** ("both positive", "opposite signs"): sheet 04, Vieta form: $D \geq 0$, signs of $S$ and $P$.
4. **Location prescribed:** sheet 04 toolkit, three ingredients.
5. **Range/extremum asked:** vertex (sheet 03), or write $y = \frac{\text{quadratic}}{\text{quadratic}}$, cross-multiply to a quadratic in $x$ and demand $D \geq 0$ — the **discriminant method** for ranges.
:::

:::example title="Worked — discriminant method for a range"
Range of $y = \frac{x^{2} - 3x + 4}{x^{2} + 3x + 4}$ ($x \in \mathbb{R}$; denominator $> 0$ always since its $D = 9 - 16 < 0$). Cross-multiply: $(y - 1)x^{2} + 3(y + 1)x + 4(y - 1) = 0$. Real $x$ exists iff $D = 9(y + 1)^{2} - 16(y - 1)^{2} \geq 0$, i.e. $-7y^{2} + 50y - 7 \geq 0$, i.e. $(7y - 1)(y - 7) \leq 0$, so $\frac{1}{7} \leq y \leq 7$. (The case $y = 1$ separately gives $x = 0$, consistent.) Equality endpoints are attained, so the range is the closed interval.
:::

:::key title="Recap — the chapter on one card"
Formula $x = \frac{-b \pm \sqrt{D}}{2a}$; $D$ cases; $S = -\frac{b}{a}$, $P = \frac{c}{a}$; $\alpha^{2} + \beta^{2} = S^{2} - 2P$; $\alpha^{3} + \beta^{3} = S^{3} - 3PS$; $(\alpha - \beta)^{2} = S^{2} - 4P = \frac{D}{a^{2}}$; vertex $\left(-\frac{b}{2a}, \frac{4ac - b^{2}}{4a}\right)$; sign: $a$'s sign outside, opposite between; always $\geq 0$ iff $a > 0, D \leq 0$; location = $D$ + $af(k)$ + vertex; reducible = substitute, filter by range, verify; common root = subtract; transformed = new $S$, new $P$.
:::

:::warn title="The ten mistakes that cost the marks (chapter checklist)"
1. $D = b^{2} + 4ac$ sign slip. 2. "$D < 0 \Rightarrow$ no roots." 3. $(\alpha - \beta)^{2} = S^{2} - 2P$. 4. Vertex value called max when $a > 0$. 5. Sign pattern ignoring sign of $a$. 6. Location: dropping one of $D$, $af(k)$, vertex. 7. Parameter in $a$: degenerate linear case unchecked. 8. Squared-roots product written $P$ not $P^{2}$. 9. No verification after squaring. 10. Dividing away a vanishing factor and losing a root.
:::

:::intuition title="Forward map — where quadratics reappear"
Vieta is the seed of symmetric polynomials (Part II here, and Newton's identities); the vertex is the seed of optimisation and of the discriminant range method used again in conic ranges; roots-of-unity filters, quadratic residues and Vieta jumping all begin with "read this symmetric condition as a quadratic in one variable".
:::
