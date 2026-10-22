---
id: jee-02
part: jee
title: "sin⁻¹(sin x) and Companions — Reading Angles Off the Branch"
---

## The one skill: reduce the angle into the principal branch

For every "inverse of a trig" the question is: *which angle in the principal range has the same trig value as $x$?* The answer is never "$x$ itself" unless $x$ already lies in the branch. The reliable method is a **two-step reduction** (shown for $\sin^{-1}(\sin x)$; the others are identical in spirit):

:::key title="Reduction algorithm for $f^{-1}(f\,x)$ — reduce, then read the branch"
1. **Reduce mod the period** of $f$: replace $x$ by $t = x - 2k\pi$ (sine/cosine) or $t = x - k\pi$ (tangent/cotangent), with $k \in \mathbb{Z}$ chosen so that $t$ falls in one full period.
2. **Read the branch**: find the unique angle $y$ in the principal range with $f(y) = f(t)$; that $y$ is the answer.
:::

### sin⁻¹(sin x) in closed piecewise form

Reduce $x$ to $t \in [-\pi/2, 3\pi/2)$ by subtracting $2\pi k$. Then the closed piecewise read is just two cases:

$$\sin^{-1}(\sin t) = t \quad \text{for } t \in [-\pi/2, \pi/2]$$

$$\sin^{-1}(\sin t) = \pi - t \quad \text{for } t \in (\pi/2, 3\pi/2)$$

Why $\pi - t$: for $t \in (\pi/2, 3\pi/2)$, the angle $\pi - t \in (-\pi/2, \pi/2)$ and $\sin(\pi - t) = \sin t$ — it is the mirror angle on the branch, produced by the symmetry of the sine wave about $t = \pi/2$.

:::example title="Worked — $\sin^{-1}\left(\sin\dfrac{7\pi}{6}\right)$ and $\sin^{-1}\left(\sin\dfrac{5\pi}{4}\right)$"
$\frac{7\pi}{6} = \pi + \frac{\pi}{6}$ is in $(\pi/2, 3\pi/2)$: answer $= \pi - \frac{7\pi}{6} = -\frac{\pi}{6}$. Check: $\sin\frac{7\pi}{6} = -\frac{1}{2} = \sin(-\frac{\pi}{6})$ ✓, and $-\frac{\pi}{6}$ is on the branch ✓.

$\frac{5\pi}{4} \in (\pi/2, 3\pi/2)$: answer $= \pi - \frac{5\pi}{4} = -\frac{\pi}{4}$. Check: $\sin\frac{5\pi}{4} = -\frac{\sqrt{2}}{2} = \sin(-\frac{\pi}{4})$ ✓.

For $\sin^{-1}\left(\sin\frac{9\pi}{5}\right)$: first reduce — $\frac{9\pi}{5} - 2\pi = -\frac{\pi}{5} \in [-\pi/2, \pi/2]$, so the answer is $-\frac{\pi}{5}$. **Reduce first, read second** — skipping the reduction is how wrong signs appear.
:::

### cos⁻¹(cos x)

Reduce to $t \in [0, 2\pi)$; then $\cos^{-1}(\cos t) = t$ for $t \in [0, \pi]$ and $= 2\pi - t$ for $t \in (\pi, 2\pi)$ (mirror about $t = 0$ on the circle: $2\pi - t \in (0,\pi)$ has the same cosine). E.g. $\cos^{-1}(\cos\frac{7\pi}{4}) = 2\pi - \frac{7\pi}{4} = \frac{\pi}{4}$.

### tan⁻¹(tan x)

Reduce to $t \in (-\pi/2, \pi/2)$ by subtracting $\pi k$ (period $\pi$, not $2\pi$!): $\tan^{-1}(\tan x) = x - \pi k$ with the unique $k \in \mathbb{Z}$ landing the result in $(-\pi/2, \pi/2)$. E.g. $\tan^{-1}\left(\tan\frac{3\pi}{4}\right) = \frac{3\pi}{4} - \pi = -\frac{\pi}{4}$; $\tan^{-1}(\tan 5) = 5 - 2\pi$ (since $5 - 2\pi \approx -1.28 \in (-\pi/2,\pi/2)$). Same for $\cot^{-1}(\cot x)$ with output forced into $(0,\pi)$.

:::diagram
{"type": "graph", "xrange": [-6.8, 6.8], "yrange": [-2.3, 2.3], "xticks": [-6.2832, -4.7124, -3.1416, -1.5708, 0, 1.5708, 3.1416, 4.7124, 6.2832], "xticklabels": ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "3π/2", "2π"], "yticks": [-2, -1, 0, 1, 2], "curves": [{"expr": "asin(sin(x))", "from": -6.8, "to": 6.8, "n": 1200, "color": "#0F766E", "clip": 2.2, "label": "y = sin⁻¹(sin x)", "labpos": 0.05}], "hlines": [{"y": 1.5708, "label": "π/2"}, {"y": -1.5708, "label": "-π/2"}], "title": "sin⁻¹(sin x) : a sawtooth oscillating INSIDE the branch [-π/2, π/2]", "ratio": 0.52}
:::

:::diagram
{"type": "graph", "xrange": [-6.8, 6.8], "yrange": [-2.3, 2.3], "xticks": [-6.2832, -4.7124, -3.1416, -1.5708, 0, 1.5708, 3.1416, 4.7124, 6.2832], "xticklabels": ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "3π/2", "2π"], "yticks": [-2, -1, 0, 1, 2], "curves": [{"expr": "atan(tan(x))", "from": -6.8, "to": 6.8, "n": 1200, "color": "#B91C1C", "clip": 2.2, "label": "y = tan⁻¹(tan x)", "labpos": 0.03}], "vlines": [{"x": -4.7124, "label": "x = -3π/2"}, {"x": -1.5708, "label": "-π/2"}, {"x": 1.5708, "label": "π/2"}, {"x": 4.7124, "label": "3π/2"}], "title": "tan⁻¹(tan x) : period π, jumps at odd multiples of π/2 (undefined there)", "ratio": 0.52}
:::

## The reverse compositions: trig of an inverse

$\sin(\tan^{-1}x)$, $\tan(\cos^{-1}x)$ and friends never need formulas — draw the **reference right triangle**:

:::app title="The triangle method — every trig-of-inverse in one picture"
Given $\theta = \tan^{-1}x$: $\theta$ is the acute-or-negative angle with $\tan\theta = x = \frac{x}{1}$. Draw a right triangle with opposite $= x$, adjacent $= 1$, hypotenuse $= \sqrt{1 + x^{2}}$ (the sign of $x$ fixes the quadrant; the triangle gives magnitudes). Read off:

$$\sin(\tan^{-1}x) = \frac{x}{\sqrt{1 + x^{2}}}, \qquad \cos(\tan^{-1}x) = \frac{1}{\sqrt{1 + x^{2}}}$$

valid for all real $x$ (both sides odd/even as they must be). Likewise with $\theta = \sin^{-1}x$: opposite $= x$, hypotenuse $= 1$, adjacent $= \sqrt{1 - x^{2}}$ (non-negative because $\theta \in [-\pi/2,\pi/2]$, where $\cos\theta \geq 0$):

$$\cos(\sin^{-1}x) = \sqrt{1 - x^{2}},$$

$$\tan(\sin^{-1}x) = \frac{x}{\sqrt{1 - x^{2}}}, \quad |x| < 1$$

For $\theta = \cos^{-1}x$ ($\theta \in [0,\pi]$): adjacent $= x$, hypotenuse $= 1$, opposite $= \sqrt{1 - x^{2}}$ (again $\sin\theta \geq 0$ on the branch):

$$\sin(\cos^{-1}x) = \sqrt{1 - x^{2}},$$

$$\tan(\cos^{-1}x) = \frac{\sqrt{1 - x^{2}}}{x}, \quad x \neq 0$$
:::

The **sign of the square root** is decided by the branch, not by taste: $\sqrt{1 - x^{2}}$ appears with a $+$ because both $\cos(\sin^{-1}x)$ and $\sin(\cos^{-1}x)$ are non-negative on their branches. If you ever need $\cos(\sin^{-1}x)$ for an angle outside a branch — you don't, that's the point of branches.

:::derive title="Worked — simplify $\tan\left(\sin^{-1}x\right)$ for $x \in (-1,1)$ and evaluate $\sin\left(\cos^{-1}\frac{3}{5} + \sin^{-1}\frac{5}{13}\right)$"
First part: from the triangle, $\frac{x}{\sqrt{1 - x^{2}}}$.

Second: let $A = \cos^{-1}\frac{3}{5} \in [0,\pi]$, $B = \sin^{-1}\frac{5}{13} \in [-\pi/2,\pi/2]$. Then $\sin A = \frac{4}{5}$ (positive on the branch!), $\cos B = \frac{12}{13}$ (positive on the branch!). So

$$\sin(A + B)$$

$$ = \sin A \cos B + \cos A \sin B$$

$$ = \frac{4}{5}\cdot\frac{12}{13} + \frac{3}{5}\cdot\frac{5}{13}$$

$$ = \frac{48 + 15}{65} = \frac{63}{65}.$$

The trap: $\sin A = \pm 4/5$ in general; the branch of $\cos^{-1}$ forces $+$.
:::

:::warn title="Common traps — branch reading"
- $\sin^{-1}\left(\sin\frac{3\pi}{4}\right) = \frac{\pi}{4}$, **not** $\frac{3\pi}{4}$ — $\frac{3\pi}{4}$ is outside $[-\pi/2, \pi/2]$.
- $\tan^{-1}(\tan x)$ has period $\pi$ and is undefined at $x = \frac{\pi}{2} + k\pi$; $\sin^{-1}(\sin x)$ has period $2\pi$.
- $\cos(\sin^{-1}x) = +\sqrt{1 - x^{2}}$ always (branch $\Rightarrow$ cosine $\geq 0$); never $\pm$.
- $\tan(\cos^{-1}x)$ is positive for $x > 0$ and negative for $x < 0$ — the triangle gives magnitudes, the branch gives signs.
- Reducing *before* reading: $\sin^{-1}\left(\sin\frac{9\pi}{5}\right) = -\frac{\pi}{5}$ requires subtracting $2\pi$ first; treating $\frac{9\pi}{5}$ as "in $(\pi/2, 3\pi/2)$" is wrong because the two-case read assumes the reduction already happened.
:::
