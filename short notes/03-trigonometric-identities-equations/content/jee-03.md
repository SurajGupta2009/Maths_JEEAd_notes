---
id: jee-03
part: jee
title: "Compound Angles — the Four Formulae and How to Own Them"
---

## The formulae

$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B,$$

$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B,$$

$$\tan(A \pm B) = \dfrac{\tan A \pm \tan B}{1 \mp \tan A \tan B}.$$

Sign reading: **sine keeps the sign of $\pm$; cosine flips it** ($\cos(A - B)$ has a $+$). Tangent's denominator flips like cosine's.

:::derive title="Derivation of $\cos(A - B)$ from the unit circle (the root of all four)"
Points $P = (\cos A, \sin A)$, $Q = (\cos B, \sin B)$ on the unit circle. The chord $|PQ|^{2} = 2 - 2\cos(A - B)$ (law of cosines in $\triangle POQ$ with angle $A - B$ at the centre; or expand $(\cos A - \cos B)^{2} + (\sin A - \sin B)^{2}$ directly). Expanding: $|PQ|^{2} = 2 - 2(\cos A \cos B + \sin A \sin B)$. Comparing: $\cos(A - B) = \cos A \cos B + \sin A \sin B$ ✓. Replace $B \to -B$ (cos even, sin odd) for $\cos(A + B)$; use $\sin x = \cos(\frac{\pi}{2} - x)$ to get both sine formulae; divide sine by cosine for tangent. All four identities rest on one distance computation.
:::

## Standard applications

**Evaluate non-standard angles.** $\sin 75^{\circ} = \sin(45^{\circ} + 30^{\circ}) = \frac{\sqrt{2}}{2}\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\frac{1}{2} = \frac{\sqrt{6} + \sqrt{2}}{4} \approx 0.9659$ ✓. $\tan 105^{\circ} = \tan(60^{\circ} + 45^{\circ}) = \frac{\sqrt{3} + 1}{1 - \sqrt{3}} = -(2 + \sqrt{3}) \approx -3.732$ ✓ (rationalise the denominator).

**Given one ratio and a quadrant, find the rest, then expand.** If $\sin A = \frac{3}{5}$, $A$ acute, then $\cos A = \frac{4}{5}$; if $\cos B = \frac{5}{13}$, $B$ acute, then $\sin B = \frac{12}{13}$, and $\sin(A + B) = \frac{3}{5}\frac{5}{13} + \frac{4}{5}\frac{12}{13} = \frac{63}{65}$ ✓.

**The linear form (preview of equations sheet 7).** $a \sin x + b \cos x = \sqrt{a^{2} + b^{2}} \sin(x + \varphi)$ where $\cos\varphi = \frac{a}{\sqrt{a^{2}+b^{2}}}$, $\sin\varphi = \frac{b}{\sqrt{a^{2}+b^{2}}}$ (so $\tan\varphi = b/a$ with the quadrant fixed by the two signs). Consequence (range): $|a \sin x + b \cos x| \leq \sqrt{a^{2} + b^{2}}$ — equality at $x + \varphi = \pm\frac{\pi}{2}$.

:::key
**Pattern ownership.** Every compound-angle exercise is one of four moves: (1) expand and collect like terms; (2) factor a collected expression back into a product of sines/cosines (using the formulae *in reverse*); (3) plug special angles $15^{\circ}, 75^{\circ}, 105^{\circ}$ etc.; (4) given $\sin A$ + quadrant data, rebuild $\cos A, \tan A$ with **Pythagoras plus a sign read from the quadrant**, then expand. Doing (4) with a wrong sign is the most common exam loss.
:::

:::example title="Worked. Prove $\cos(A - B) - \cos(A + B) = 2 \sin A \sin B$ and evaluate $\cos 75^{\circ} - \cos 15^{\circ}$"
Expand both: $\cos(A-B) - \cos(A+B) = (\cos A \cos B + \sin A \sin B) - (\cos A \cos B - \sin A \sin B) = 2 \sin A \sin B$ ✓. With $A = 75^{\circ}, B = 15^{\circ}$: sum-to-product gives $-2 \sin 45^{\circ} \sin 30^{\circ} = -2 \cdot \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = -\frac{\sqrt{2}}{2} \approx -0.7071$ ✓ (matches direct: $0.2588 - 0.9659$).
:::

:::warn title="Common traps — compound angles"
- $\cos(A - B) = \cos A \cos B \mathbf{+} \sin A \sin B$ — the plus sign. #1 exam error in this chapter.
- $\tan(A + B)$ denominator is $1 - \tan A \tan B$; numerator keeps $+$. Mixing these gives $\tan 45^{\circ} \ne 1$ instantly.
- Formulae need the angles in a **common unit**: convert $A = 20^{\circ}$, $B = \frac{\pi}{6}$ before expanding.
- $\sin(A + B) \ne \sin A + \sin B$; $\cos 2A \ne 2 \cos A$ — the formulae are products, not linear.
- Finding $\cos A$ from $\sin A = \frac{3}{5}$ gives $\pm \frac{4}{5}$; the quadrant decides. Acute $\Rightarrow +$. State the quadrant assumption if given.
:::
