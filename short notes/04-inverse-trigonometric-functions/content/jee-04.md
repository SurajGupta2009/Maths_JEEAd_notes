---
id: jee-04
part: jee
title: "sin⁻¹ and cos⁻¹ Addition Formulas + the Simplification Toolkit"
---

## sin⁻¹x ± sin⁻¹y — derived, not recited

Let $A = \sin^{-1}x$, $B = \sin^{-1}y$, so $A, B \in [-\pi/2, \pi/2]$ and $A + B \in [-\pi, \pi]$. Take the sine of the sum: $\sin(A+B) = x\sqrt{1 - y^{2}} + y\sqrt{1 - x^{2}} =: \sigma$ (the square roots are non-negative precisely because of the branches). Then $A + B = \sin^{-1}\sigma$ **if** $A + B \in [-\pi/2, \pi/2]$, else the mirror-angle correction applies. The branch test reduces to the sign of

$$\cos(A+B) = \sqrt{1 - x^{2}}\sqrt{1 - y^{2}} - xy$$

which is $\geq 0$ exactly when $xy \leq 0$ or $x^{2} + y^{2} \leq 1$.

:::key title="The sum formulas, with the branch conditions"
$$\sin^{-1}x + \sin^{-1}y = \sin^{-1}(x\sqrt{1-y^{2}} + y\sqrt{1-x^{2}})$$

$$\text{if } xy \leq 0 \text{ or } x^{2} + y^{2} \leq 1$$

$$\sin^{-1}x + \sin^{-1}y = \pi - \sin^{-1}(x\sqrt{1-y^{2}} + y\sqrt{1-x^{2}})$$

$$\text{if } x > 0,\ y > 0,\ x^{2} + y^{2} > 1$$

$$\sin^{-1}x + \sin^{-1}y$$

$$-\pi - \sin^{-1}(x\sqrt{1-y^{2}} + y\sqrt{1-x^{2}})$$

$$\text{if } x < 0,\ y < 0,\ x^{2} + y^{2} > 1$$

**Difference:** $\sin^{-1}x - \sin^{-1}y = \sin^{-1}x + \sin^{-1}(-y)$ — run the same table with $y \mapsto -y$. All statements assume $|x|, |y| \leq 1$.
:::

:::example title="Worked — $\sin^{-1}\frac{3}{5} + \sin^{-1}\frac{8}{17}$: which case?"
$x = \frac{3}{5}, y = \frac{8}{17}$: $xy > 0$ and $x^{2} + y^{2} = \frac{9}{25} + \frac{64}{289} \approx 0.36 + 0.22 = 0.58 < 1$ → **first case**, no correction. Compute $\sigma = \frac{3}{5}\cdot\frac{15}{17} + \frac{8}{17}\cdot\frac{4}{5} = \frac{45}{85} + \frac{32}{85} = \frac{77}{85}$. So the sum equals $\sin^{-1}\frac{77}{85}$.

Cross-check numerically: $\sin^{-1}0.6 \approx 0.6435$, $\sin^{-1}(8/17) \approx 0.4899$, sum $\approx 1.1334$; $\sin^{-1}(77/85) \approx 1.1334$ ✓.

Now the *other* regime: $\sin^{-1}\frac{4}{5} + \sin^{-1}\frac{12}{13}$: $x^{2}+y^{2} = 0.64 + 0.852 > 1$, both positive $\to$ second case. $\sigma = \frac{4}{5}\cdot\frac{5}{13} + \frac{12}{13}\cdot\frac{3}{5} = \frac{20 + 36}{65} = \frac{56}{65}$. So the sum equals $\pi - \sin^{-1}\frac{56}{65}$. Numerically the two sides agree: $\sin^{-1}0.8 + \sin^{-1}(12/13) \approx 0.9273 + 1.1760 = 2.1033$, and $\pi - \sin^{-1}(56/65) \approx 3.1416 - 1.0383 = 2.1033$ ✓. Without the correction you would quote $\sin^{-1}\frac{56}{65} \approx 1.0383$ — not the sum.
:::

## cos⁻¹x ± cos⁻¹y

Same machinery with $A, B \in [0, \pi]$: $\cos(A \pm B) = xy \mp \sqrt{1 - x^{2}}\sqrt{1 - y^{2}}$, and the sum $A + B \in [0, 2\pi]$ needs one $\pi$-type correction when $A + B > \pi$ (i.e. when $x + y < 0$). The clean exam form:

$$\cos^{-1}x + \cos^{-1}y = \cos^{-1}(xy - \sqrt{1-x^{2}}\sqrt{1-y^{2}})$$

$$\text{if } x + y \geq 0$$

$$\cos^{-1}x + \cos^{-1}y$$

$$2\pi - \cos^{-1}(xy - \sqrt{1-x^{2}}\sqrt{1-y^{2}})$$

$$\text{if } x + y < 0$$

$$\cos^{-1}x - \cos^{-1}y = \cos^{-1}(xy + \sqrt{1-x^{2}}\sqrt{1-y^{2}})$$

$$\text{if } x \leq y$$

and $= -\cos^{-1}(xy + \sqrt{1-x^{2}}\sqrt{1-y^{2}})$ if $x > y$ (the difference is negative then). Also worth memorising as a one-liner: $\cos^{-1}x - \sin^{-1}y = \cos^{-1}\left(x\sqrt{1 - y^{2}} + y\sqrt{1 - x^{2}}\right)$ for $x, y \geq 0$... the safest habit: **derive the needed formula on the spot from $\cos(A \pm B)$ or $\sin(A \pm B)$ plus a branch check**, and use the table only as a time-saver you have already verified once.

:::assume title="Assumptions packed into the four formulas above"
$|x|, |y| \leq 1$ throughout; the un-specified square roots $\sqrt{1 - x^{2}}, \sqrt{1 - y^{2}}$ always mean the **non-negative** root; all angles in radians; outputs of $\sin^{-1}$ in $[-\pi/2, \pi/2]$ and of $\cos^{-1}$ in $[0,\pi]$ without exception. When a problem statement gives angles outside these windows, the problem is a sheet-02 reduction problem first.
:::

## The simplification toolkit — patterns that actually appear

:::app title="Five standard simplification patterns"
1. **Sum of two arctans** → sheet 03 table (check $xy$ vs $1$). Classic: $\tan^{-1}1 + \tan^{-1}2 + \tan^{-1}3 = \frac{\pi}{4} + \frac{3\pi}{4} = \pi$.
2. **Pair a sine-inverse with a cosine-inverse of the same argument**: $\sin^{-1}x + \cos^{-1}x = \frac{\pi}{2}$ collapses the pair instantly — scan for it before computing anything.
3. **Square-root absorption**: $\tan^{-1}\left(\frac{\sqrt{1 + x^{2}} - 1}{x}\right)$ for $x > 0$ recognises the half-angle: with $x = \tan\theta$ this is $\tan^{-1}\frac{1 - \cos\theta}{\sin\theta} = \frac{\theta}{2} = \frac{1}{2}\tan^{-1}x$. Setting $x = \tan\theta$ (or $x = \sin\theta$, $x = \cos\theta$) to expose a compound angle is the standard move.
4. **Convert to one inverse**: $\sin^{-1}x = \tan^{-1}\frac{x}{\sqrt{1 - x^{2}}}$, $\cos^{-1}x = \tan^{-1}\frac{\sqrt{1 - x^{2}}}{x}$ (branch-checked), then use the arctan table.
5. **Monotone reading for equations**: each inverse is strictly monotone on its domain ($\sin^{-1}$, $\tan^{-1}$ increasing; $\cos^{-1}$ decreasing), so $f^{-1}(\text{stuff}) = c$ may be replaced by "$\text{stuff} = f(c)$" — injectivity of the *outer* function is what licenses the step.
:::

:::warn title="Common traps — addition formulas"
- $\sin^{-1}x + \sin^{-1}y = \sin^{-1}(x\sqrt{1-y^{2}} + y\sqrt{1-x^{2}})$ is **conditional**. Test the regime first: at $x = y = \frac{3}{5}$ one has $x^{2}+y^{2} = 0.72 < 1$ so the plain case applies ($2\sin^{-1}\frac{3}{5} = \sin^{-1}\frac{24}{25} \approx 1.287$ ✓); at $x = y = \frac{4}{5}$ one has $x^{2}+y^{2} = 1.28 > 1$ and the $\pi -$ case applies ($2\sin^{-1}\frac{4}{5} = \pi - \sin^{-1}\frac{24}{25} \approx 1.854$ ✓). Same $\sigma = \frac{24}{25}$, different answers — the regime is the whole content of the formula.
- $\cos^{-1}x + \cos^{-1}y$ output can exceed $\pi$ (up to $2\pi$) — it is **not** a principal value unless corrected.
- Dropping square-root signs: $\sqrt{1 - x^{2}} \geq 0$ always in these formulas; writing $\cos(\sin^{-1}x) = \pm\sqrt{1 - x^{2}}$ shows the branch was never read.
- $\sin^{-1}x + \cos^{-1}y = \frac{\pi}{2}$ is only valid for $x = y$ (same argument!).
- Applying the difference formula for $\cos^{-1}x - \cos^{-1}y$ without the $x \leq y$ condition flips the sign of the answer.
:::
