---
id: jee-02
part: jee
title: "Signs by Quadrant, Allied Angles, Standard Values"
---

## Signs — read them off the coordinates

Since $P = (\cos\theta, \sin\theta)$: sine carries the $y$-sign, cosine the $x$-sign, tangent their ratio.

| Quadrant | $\sin$ / $\csc$ | $\cos$ / $\sec$ | $\tan$ / $\cot$ |
|---|---|---|---|
| I $(0, \frac{\pi}{2})$ | $+$ | $+$ | $+$ |
| II $(\frac{\pi}{2}, \pi)$ | $+$ | $-$ | $-$ |
| III $(\pi, \frac{3\pi}{2})$ | $-$ | $-$ | $+$ |
| IV $(\frac{3\pi}{2}, 2\pi)$ | $-$ | $+$ | $-$ |

Mnemonic ("**A**ll **S**tudent**s T**ake **C**alculus"): I all positive, II only sine/csc, III only tan/cot, IV only cos/sec.

## Allied angles — symmetry about the axes

Reflections of $P = (\cos\theta, \sin\theta)$ in the axes give, for example:

$$\sin(\pi - \theta) = \sin\theta, \quad \cos(\pi - \theta) = -\cos\theta$$

$$\sin(\pi + \theta) = -\sin\theta, \quad \cos(\pi + \theta) = -\cos\theta$$

$$\sin\!\left(\frac{\pi}{2} - \theta\right) = \cos\theta, \quad \cos\!\left(\frac{\pi}{2} - \theta\right) = \sin\theta$$

$$\sin(-\theta) = -\sin\theta, \quad \cos(-\theta) = \cos\theta.$$

:::derive title="Why odd multiples of $\frac{\pi}{2}$ swap $\sin$ and $\cos$"
Adding $\frac{\pi}{2}$ rotates $P$ by a quarter turn: $(x, y) \mapsto (-y, x)$. So $\cos(\theta + \frac{\pi}{2}) = -\sin\theta$ and $\sin(\theta + \frac{\pi}{2}) = \cos\theta$ — the coordinates **swap with a sign**. Adding $\pi$ sends $(x, y) \mapsto (-x, -y)$: both signs flip, no swap. So: **odd multiples of $\frac{\pi}{2}$ swap sine and cosine (with quadrant signs); even multiples only change signs.** This one rotation picture generates the entire allied-angle table.
:::

:::diagram
{"type": "unitcircle", "angle_deg": 145, "title": "Allied angle π − θ in QII: sine survives (y unchanged), cosine flips sign", "point_label": "P'(cos(π−θ), sin(π−θ)) = (−cos θ, sin θ)", "angle_label": "π−θ"}
:::

## Standard values (memorise the first octant; extend by symmetry)

| $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|---|---|---|---|---|---|
| $\sin$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| $\cos$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\tan$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | undef. |

Extend with allied angles: $\sin\frac{2\pi}{3} = \sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$; $\cos\frac{3\pi}{4} = -\cos\frac{\pi}{4} = -\frac{\sqrt{2}}{2}$; $\tan\frac{5\pi}{3} = -\tan\frac{\pi}{3} = -\sqrt{3}$. Special values $\sin\frac{\pi}{10} = \sin 18^{\circ} = \frac{\sqrt{5}-1}{4}$ and $\cos 36^{\circ} = \frac{\sqrt{5}+1}{4}$ are derived in Part II.

**Periodicity:** $\sin, \cos$ have period $2\pi$; $\tan, \cot$ have period $\pi$ (because $\tan(\theta + \pi) = \tan\theta$; the sine/cosine pair flips sign together and the ratio forgets). So $\sin(\theta + 2k\pi) = \sin\theta$, $\tan(\theta + k\pi) = \tan\theta$.

:::example title="Worked. Evaluate $\sin 135^{\circ}$, $\cos 225^{\circ}$, $\tan\frac{7\pi}{6}$"
$\sin 135^{\circ} = \sin(180^{\circ} - 45^{\circ}) = \sin 45^{\circ} = \frac{\sqrt{2}}{2}$ ✓. $\cos 225^{\circ} = \cos(180^{\circ} + 45^{\circ}) = -\cos 45^{\circ} = -\frac{\sqrt{2}}{2}$ ✓. $\tan\frac{7\pi}{6} = \tan\!\left(\pi + \frac{\pi}{6}\right) = \tan\frac{\pi}{6} = \frac{\sqrt{3}}{3}$ (QIII: tan positive) ✓.
:::

:::warn title="Common traps — signs and values"
- $\cos(\pi - \theta) = -\cos\theta$ **not** $\cos\theta$; the cosine sign flips in QII, the sine does not.
- $\sin^{-1}$ notation trap again: $\sin(\pi - \theta)$ is an allied angle, not an inverse function.
- $\tan\frac{\pi}{2}$ is **undefined** (not $\infty$ as a number); "approaches $+\infty$ from the left" is a limit statement.
- Degree/radian mixing: $135^{\circ} = \frac{3\pi}{4}$ rad — write the conversion before computing.
:::
