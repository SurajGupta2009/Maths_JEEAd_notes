---
id: oly-03
part: olympiad
title: "Olympiad Extensions — Trig Series (Telescoping) and Square Sums"
---

## Status of this sheet

The telescoping series $\sum \sin k\theta$ and the sums $\sum \cot^{2}$, $\sum \csc^{2}$ are **standard olympiad algebra**; all derive from Part I transformation formulae and the roots-of-Vieta technique of sheet 2. Models are derivable from supplied information; classified as extensions because they sit beyond the current syllabus sentence.

## Sums with arguments in arithmetic progression (telescoping)

**The trick:** multiply by $2 \sin\frac{\theta}{2}$ and watch the product-to-sum formula telescope.

$$\sum_{k=1}^{n} \sin k\theta = \dfrac{\sin\frac{n\theta}{2} \, \sin\frac{(n+1)\theta}{2}}{\sin\frac{\theta}{2}}$$

$$\sum_{k=1}^{n} \cos k\theta = \dfrac{\sin\frac{n\theta}{2} \, \cos\frac{(n+1)\theta}{2}}{\sin\frac{\theta}{2}}$$

:::derive title="Derivation — the $2 \sin\frac{\theta}{2}$ multiplier"
$2 \sin\frac{\theta}{2} \sin k\theta = \cos\left(k - \frac{1}{2}\right)\theta - \cos\left(k + \frac{1}{2}\right)\theta$. Summing over $k = 1 \ldots n$ telescopes to $\cos\frac{\theta}{2} - \cos\left(n + \frac{1}{2}\right)\theta$. Then apply $\cos C - \cos D = -2 \sin\frac{C+D}{2} \sin\frac{C-D}{2}$ with $C = \frac{\theta}{2}$, $D = (n + \frac{1}{2})\theta$: $= 2 \sin\frac{(n+1)\theta}{2} \sin\frac{n\theta}{2}$. Divide by $2 \sin\frac{\theta}{2}$ ✓. (Valid for $\sin\frac{\theta}{2} \ne 0$, i.e. $\theta \notin 2\pi \mathbb{Z}$; the excluded cases are computed directly as sums of $0/1$.)
:::

:::example title="Worked check. $n = 3$, $\theta = \frac{\pi}{6}$"
Direct: $\sin 30^{\circ} + \sin 60^{\circ} + \sin 90^{\circ} = 0.5 + 0.86603 + 1 = 2.36603$. Formula: $\frac{\sin 45^{\circ} \sin 60^{\circ}}{\sin 15^{\circ}} = \frac{0.70711 \times 0.86603}{0.25882} = 2.36603$ ✓.
:::

## Sums of squares at rational multiples of $\pi$ (roots + Vieta)

The numbers $t_{k} = \tan\frac{k\pi}{n}$, $k = 1, \ldots, n-1$, are the non-zero roots of a polynomial obtained from $\tan(n\theta)$ in terms of $t = \tan\theta$ (write $\tan n\theta = \frac{\Im(1 + it)^{n}}{\Re(1 + it)^{n}}$ and set the numerator to $0$). Vieta then gives sums of powers.

$$\sum_{k=1}^{n-1} \cot^{2}\dfrac{k\pi}{n} = \dfrac{(n-1)(n-2)}{3}, \qquad \sum_{k=1}^{n-1} \csc^{2}\dfrac{k\pi}{n} = \dfrac{n^{2} - 1}{3}.$$

:::derive title="Derivation sketch — cotangents as roots of the complementary polynomial"
$\cot^{2} \frac{k\pi}{n} = \frac{1}{t_{k}^{2}}$, and the symmetric identity $\sum \frac{1}{t_{k}^{2}} = \left(\sum \frac{1}{t_{k}}\right)^{2} - 2 \sum_{j < k} \frac{1}{t_{j} t_{k}}$ turns Vieta's data for the $t_{k}$ into the closed form $\frac{(n-1)(n-2)}{3}$. Then $\csc^{2} = 1 + \cot^{2}$ adds $(n - 1)$ terms of $1$: $\sum \csc^{2} = (n-1) + \frac{(n-1)(n-2)}{3} = \frac{(n-1)(n+1)}{3} = \frac{n^{2} - 1}{3}$ ✓.
:::

:::example title="Worked checks. $n = 3, 4, 5$"
$\cot^{2}$: $n = 3$: $\cot^{2} 60^{\circ} + \cot^{2} 120^{\circ} = \frac{1}{3} + \frac{1}{3} = \frac{2}{3} = \frac{2 \cdot 1}{3}$ ✓. $n = 4$: $1 + 0 + 1 = 2 = \frac{3 \cdot 2}{3}$ ✓. $n = 5$: $4 = \frac{4 \cdot 3}{3}$ ✓. $\csc^{2}$: $n = 3$: $\frac{4}{3} + \frac{4}{3} = \frac{8}{3} = \frac{9 - 1}{3}$ ✓; $n = 4$: $2 + 1 + 2 = 5 = \frac{15}{3}$ ✓; $n = 5$: $8 = \frac{24}{3}$ ✓.
:::

:::key
**Whenever a sum runs over trig values at equally spaced angles:** (1) look for a telescoping multiplier ($2 \sin\frac{\theta}{2}$ for AP-argument sums); (2) look for the polynomial whose roots they are (Vieta for square/power sums); (3) pair symmetric terms ($k \leftrightarrow n - k$) to halve the work; (4) validate a small case numerically before the proof.
:::

:::warn title="Traps on this sheet"
- The telescoping formulas divide by $\sin\frac{\theta}{2}$: state $\theta \notin 2\pi\mathbb{Z}$ (or handle those cases directly).
- $\sum \sin k\theta$ closed form: the numerator is $\sin\frac{n\theta}{2} \cdot \sin\frac{(n+1)\theta}{2}$ — order $(n+1)$ vs $n$ swapped between the two factors vs the cosine version (which has $\cos\frac{(n+1)\theta}{2}$).
- $\cot^{2}\frac{k\pi}{n}$ has a term at $k = \frac{n}{2}$ (when $n$ even) equal to $0$ — include it (it is $\cot^{2}\frac{\pi}{2} = 0$).
- $\tan n\theta$'s polynomial in $t = \tan\theta$ has **degree $n$** in the tangent-angle formula bookkeeping; only the roots $t_{k}$ with $\tan$ defined count.
:::

## Assumptions & conventions

$n \geq 2$ integer; $\theta$ real with $\sin\frac{\theta}{2} \ne 0$ in series formulas; Vieta applied to real polynomials; numeric checks above computed in radians (converted to degrees for readability).
