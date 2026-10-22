---
id: jee-05
part: jee
title: "Transformation Formulae — Products ↔ Sums"
---

## The four product-to-sum formulae

Add/subtract the compound sine and cosine expansions:

$$2 \sin A \cos B = \sin(A+B) + \sin(A-B)$$

$$2 \cos A \sin B = \sin(A+B) - \sin(A-B)$$

$$2 \cos A \cos B = \cos(A+B) + \cos(A-B)$$

$$2 \sin A \sin B = \cos(A-B) - \cos(A+B)$$

:::derive title="Derivation — one addition, one subtraction"
$\sin(A+B) = \sin A \cos B + \cos A \sin B$ and $\sin(A-B) = \sin A \cos B - \cos A \sin B$. Add: $2 \sin A \cos B = \sin(A+B) + \sin(A-B)$. Subtract: $2 \cos A \sin B = \sin(A+B) - \sin(A-B)$. Same game with the cosine pair. **The RHS argument pair is always $(A+B, A-B)$** — one formula in each direction, nothing new to memorise.
:::

## Sum-to-product (set $C = A + B$, $D = A - B$, so $A = \frac{C+D}{2}$, $B = \frac{C-D}{2}$)

$$\sin C + \sin D = 2 \sin\dfrac{C+D}{2} \cos\dfrac{C-D}{2}$$

$$\sin C - \sin D = 2 \cos\dfrac{C+D}{2} \sin\dfrac{C-D}{2}$$

$$\cos C + \cos D = 2 \cos\dfrac{C+D}{2} \cos\dfrac{C-D}{2}$$

$$\cos C - \cos D = -2 \sin\dfrac{C+D}{2} \sin\dfrac{C-D}{2}$$

Note the **minus sign** in the last one (the only formula with it).

:::key
**What these are for.** (1) Turn products of sines/cosines into sums (then factor); (2) turn sums into products (then solve each factor $= 0$ — the backbone of equation sheet 7); (3) telescope sums whose arguments are in arithmetic progression (Part II series); (4) evaluate exact values: $\sin 75^{\circ} + \sin 15^{\circ} = 2 \sin 45^{\circ} \cos 30^{\circ} = 2 \cdot \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{6}}{2} \approx 1.2247$ ✓ matches direct addition $0.9659 + 0.2588$.
:::

:::example title="Worked. Simplify $\cos 3x \cos x + \cos 5x \cos x$-type products; evaluate $\cos 75^{\circ} - \cos 15^{\circ}$"
Product-to-sum: $\cos 3x \cos x = \frac{1}{2}[\cos 4x + \cos 2x]$; so the sum $= \frac{1}{2}[\cos 4x + \cos 2x + \cos 6x + \cos 4x] = \frac{1}{2}[\cos 2x + 2 \cos 4x + \cos 6x]$. For the exact value: $\cos 75^{\circ} - \cos 15^{\circ} = -2 \sin 45^{\circ} \sin 30^{\circ} = -\frac{\sqrt{2}}{2} \approx -0.7071$ ✓ (direct: $0.2588 - 0.9659$).
:::

:::example title="Worked. Factor $\sin x + \sin 3x + \sin 5x$"
Pair first and last? Pairwise sum-to-product: $\sin x + \sin 5x = 2 \sin 3x \cos 2x$, so the expression $= 2 \sin 3x \cos 2x + \sin 3x = \sin 3x (2 \cos 2x + 1)$. Factored form ready for solving $\sin 3x (2 \cos 2x + 1) = 0$ (sheet 7's method). Check at $x = 30^{\circ}$: $\sin 30^{\circ} + \sin 90^{\circ} + \sin 150^{\circ} = 0.5 + 1 + 0.5 = 2$; RHS: $\sin 90^{\circ}(2 \cos 60^{\circ} + 1) = 1 \cdot (1 + 1) = 2$ ✓.
:::

:::warn title="Common traps — transformations"
- $2 \sin A \sin B = \cos(A-B) - \cos(A+B)$: the **order** of $A-B$, $A+B$ matters (sign).
- $\cos C - \cos D = -2 \sin\frac{C+D}{2} \sin\frac{C-D}{2}$ — the leading minus.
- Mixed arguments: $2 \sin A \cos B$ vs $2 \cos A \sin B$ are different formulas; match the pattern before applying.
- Keep the $\frac{C \pm D}{2}$ halving straight: $\sin C + \sin D$ uses $\sin\frac{C+D}{2}\cos\frac{C-D}{2}$ (sine of the average, cosine of the half-difference).
:::
