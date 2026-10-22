---
id: jee-05
part: jee
title: "Equations Reducible to Quadratics — One Substitution Away, Then Verify"
---

## The standard substitutions

:::key title="Recognise the shape, name the substitution"
- $ax^{4} + bx^{2} + c = 0$ (biquadratic): $t = x^{2}$, keep only $t \geq 0$.
- $a\left(x^{2} + \frac{1}{x^{2}}\right) + b\left(x + \frac{1}{x}\right) + c = 0$: $t = x + \frac{1}{x}$, using $x^{2} + \frac{1}{x^{2}} = t^{2} - 2$. Note $\left|t\right| \geq 2$ for real $x \neq 0$ — reject $\left|t\right| < 2$.
- $a^{2x} + b\,a^{x} + c = 0$ (and $\sin$, $\log$ analogues): $t = a^{x} > 0$ — require $t > 0$.
- $(x + a)(x + b)(x + c)(x + d) = k$ with $a + d = b + c$: pair outer with outer so both products share the same $x^{2} + (\text{common})x$ part; set $t$ to that shared part.
- Radical equations: isolate the radical, square, solve — then **verify every candidate in the original equation**.
- Anything of the form $g(x)^{2} + b\,g(x) + c = 0$: $t = g(x)$, with the range of $g$ as the admissibility filter.
:::

:::example title="Worked — the four canonical types"
**Biquadratic:** $x^{4} - 5x^{2} + 4 = 0$: $t = x^{2}$ gives $t = 1, 4$, so $x = \pm 1, \pm 2$.

**Exponential:** $2^{2x} - 5 \cdot 2^{x} + 4 = 0$: $t = 2^{x} > 0$ gives $t = 1, 4$ (both admissible), so $x = 0, 2$.

**Reciprocal:** $x^{2} + \frac{1}{x^{2}} = 7$: with $t = x + \frac{1}{x}$, $t^{2} - 2 = 7$, $t = \pm 3$; then $x = \frac{3 \pm \sqrt{5}}{2}$ or $x = \frac{-3 \pm \sqrt{5}}{2}$.

**Radical:** $\sqrt{x + 3} = x - 3$: squaring gives $x^{2} - 7x + 6 = 0$, candidates $x = 1, 6$. Check: $x = 1$ gives $2 = -2$ ✗ (also the RHS is negative while a square root never is — rejectable *before* squaring); $x = 6$ gives $3 = 3$ ✓. Answer: $x = 6$ only.
:::

:::warn title="Common traps — reducible equations"
- Squaring is not reversible: extraneous roots are the rule, not the exception. Verification is part of the method.
- Dividing by an expression that can vanish loses roots: $(x + 1)^{2} = 4(x + 1)$ divided by $x + 1$ loses $x = -1$; the substitution $t = x + 1$ gives $t = 0, 4$, i.e. $x = -1, 3$.
- Admissibility forgotten: $t = x^{2} < 0$ or $t = 2^{x} \leq 0$ or $\left|x + \frac{1}{x}\right| < 2$ candidates must be discarded even though the quadratic "gave" them.
- For $\sqrt{A} = B$, record $B \geq 0$ and $A \geq 0$ first — often half the candidates die instantly.
:::

:::app title="Why quadratics are the reduction target"
Biquadratics, radical, exponential, logarithmic and many trigonometric equations all collapse to a quadratic after one well-chosen substitution. The exam skill is not solving the quadratic — it is (1) spotting the repeated block $g(x)$, (2) writing its admissible range, (3) filtering. Marks are lost at steps 2–3, almost never at step 1.
:::
