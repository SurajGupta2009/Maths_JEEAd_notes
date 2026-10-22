---
id: oly-01
part: olympiad
title: "Extension — Piecewise Masters: f(x) = sin⁻¹(sin x) + cos⁻¹(cos x) and Siblings"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Beyond the core syllabus sentence (principal values), the *analysis of composite inverse-trig functions* — piecewise closed forms, parity/period, graph shapes, extrema on intervals — is standard olympiad and coaching-extension material. Every model here is **derivable from Part I** (branch reads + addition formulas): no new theory is assumed, only sustained bookkeeping. Nothing here "can never appear" in JEE Advanced; it is simply less typical than the Part I types.
:::

## The full closed form of f(x) = sin⁻¹(sin x) + cos⁻¹(cos x)

Both pieces are sheet-02 reads. Reduce $x$ to $t \in [0, 2\pi)$ first (both components have period $2\pi$, so $f$ has period $2\pi$). On $[0, 2\pi)$:

$$\sin^{-1}(\sin t) = t \ (0 \leq t \leq \frac{\pi}{2}), \qquad = \pi - t \ (\frac{\pi}{2} < t < \frac{3\pi}{2}),$$

$$= t - 2\pi \ (\frac{3\pi}{2} \leq t < 2\pi)$$

$$\cos^{-1}(\cos t) = t \ (0 \leq t \leq \pi), \qquad = 2\pi - t \ (\pi < t < 2\pi)$$

Adding on each sub-interval of $[0, 2\pi)$ — leg by leg (the composition of two affine pieces is affine, so only endpoints need checking):

- $t \in [0, \frac{\pi}{2}]$: $t + t = 2t$ (rises $0 \to \pi$).
- $t \in [\frac{\pi}{2}, \pi]$: $(\pi - t) + t = \pi$ (the plateau).
- $t \in [\pi, \frac{3\pi}{2}]$: $(\pi - t) + (2\pi - t) = 3\pi - 2t$ (falls $\pi \to 0$).
- $t \in [\frac{3\pi}{2}, 2\pi)$: $(t - 2\pi) + (2\pi - t) = 0$ (the floor).

$$f(t) = 2t \ \text{on } [0, \frac{\pi}{2}], \qquad f(t) = \pi \ \text{on } [\frac{\pi}{2}, \pi]$$

$$f(t) = 3\pi - 2t \ \text{on } [\pi, \frac{3\pi}{2}], \qquad f(t) = 0 \ \text{on } [\frac{3\pi}{2}, 2\pi)$$

Range on $\mathbb{R}$: $f$ takes every value in $[0, \pi]$ (max $\pi$ on the plateau, min $0$). **Neither odd nor even**; $f(x + 2\pi) = f(x)$.

:::derive title="The bookkeeping lesson — always split at the branch knots"
The knots of $\sin^{-1}(\sin x)$ are $x = \frac{\pi}{2} + k\pi$ (where the sawtooth turns); those of $\cos^{-1}(\cos x)$ are $x = k\pi$. A sum's piecewise form splits at the **union** of knots. On each open piece both components are linear ($\pm x + \text{const}$), so $f$ is affine there: the whole problem reduces to assembling slopes. Slopes of $\sin^{-1}(\sin x)$ alternate $+1, -1$; of $\cos^{-1}(\cos x)$: $+1, -1$; sums have slopes in $\{-2, 0, 2\}$ — the flat middle leg above is the $+1 + (-1)$ collision.
:::

:::diagram
{"type": "graph", "xrange": [-6.8, 6.8], "yrange": [-0.7, 4.0], "xticks": [-6.2832, -4.7124, -3.1416, -1.5708, 0, 1.5708, 3.1416, 4.7124, 6.2832], "xticklabels": ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "3π/2", "2π"], "yticks": [0, 1, 2, 3], "yticklabels": ["0", "1", "2", "3"], "curves": [{"expr": "asin(sin(x)) + acos(cos(x))", "from": -6.8, "to": 6.8, "n": 1400, "color": "#0F766E", "clip": 4.0, "label": "f = sin⁻¹(sinx)+cos⁻¹(cosx)", "labpos": 0.12}], "hlines": [{"y": 3.1416, "label": "y = π (max)"}], "title": "f(x): plateau π on [π/2, π], zero on [3π/2, 2π), period 2π — range [0, π]", "ratio": 0.5}
:::

## Sibling composites worth owning

- $g(x) = \sin^{-1}(\sin x)$ alone: odd, $2\pi$-periodic, range $[-\pi/2, \pi/2]$.
- $h(x) = \cos^{-1}(\cos x)$: even, $2\pi$-periodic, range $[0, \pi]$ — note $h(x) = |x|$ on $[-\pi, \pi]$, the "triangle wave".
- $p(x) = \tan^{-1}(\tan x)$: odd, $\pi$-periodic (undefined at odd multiples of $\pi/2$), range $(-\pi/2, \pi/2)$ — the sawtooth of sheet 02.
- $q(x) = \sin^{-1}(\sin x) + \cos^{-1}(\sin x)$: collapses to $\frac{\pi}{2}$ **everywhere** (complementary pair with the *same* argument $\sin x$ — a one-liner that looks like work).
- $r(x) = \tan^{-1}(\sin x)$: odd, $2\pi$-periodic, range $[-\frac{\pi}{4}, \frac{\pi}{4}]$ (bound $\sin x \in [-1,1]$ through the increasing $\tan^{-1}$). Extrema-type questions ("range of $\tan^{-1}(\sin x) + \tan^{-1}(\cos x)$") are solved by monotone-plus-derivative-free bounding: $\sin x + \cos x$-style collapse.

:::app title="Extrema method for $u(x) = \tan^{-1}(\sin x) + \tan^{-1}(\cos x)$"
Add via the table: $\tan^{-1}u + \tan^{-1}v = \tan^{-1}\frac{u + v}{1 - uv}$ when $uv < 1$ — here $uv = \sin x \cos x \leq \frac{1}{2} < 1$ ✓ always. So

$$u(x) = \tan^{-1}\left(\frac{\sin x + \cos x}{1 - \sin x \cos x}\right)$$

a monotone transform of $s = \sin x + \cos x \in [-\sqrt{2}, \sqrt{2}]$ with $\sin x \cos x = \frac{s^{2} - 1}{2}$. Write $u = \tan^{-1}\frac{s}{1 - \frac{s^{2} - 1}{2}} = \tan^{-1}\frac{2s}{3 - s^{2}}$. On $s \in [-\sqrt{2}, \sqrt{2}]$ the fraction $\frac{2s}{3 - s^{2}}$ is odd-increasing in $s$ (denominator $3 - s^{2} \in [1, 3]$ stays positive), so max at $s = \sqrt{2}$: $\frac{2\sqrt{2}}{1} = 2\sqrt{2}$, i.e. $\max u = \tan^{-1}(2\sqrt{2})$ and $\min u = -\tan^{-1}(2\sqrt{2})$; range $\left[-\tan^{-1}2\sqrt{2},\ \tan^{-1}2\sqrt{2}\right]$. Every step used only Part I: the addition formula's condition, the range of $\sin x + \cos x$, monotonicity of $\tan^{-1}$.
:::

:::warn title="Traps specific to piecewise work"
- Splitting at the wrong knots (only one component's) creates false affine pieces with wrong slopes.
- Period: $\sin^{-1}(\sin x) + \cos^{-1}(\cos x)$ has period $2\pi$; $\tan^{-1}(\tan x)$ has $\pi$ — sums take the LCM ($2\pi$ here).
- Endpoints of branch windows ($x = \frac{\pi}{2}$ etc.) are continuous for these composites but *not* differentiable — extrema questions may land on a knot; evaluate both one-sided values (they agree here).
- In "$q(x)$ collapses to $\pi/2$" the argument of both inverses must be identical; $\sin^{-1}(\sin x) + \cos^{-1}(\cos x) \neq \frac{\pi}{2}$ (that is $f$ above!).
:::
