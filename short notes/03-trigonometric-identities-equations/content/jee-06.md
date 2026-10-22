---
id: jee-06
part: jee
title: "Trigonometric Equations I — Principal and General Solutions"
---

## The idea: one circle, infinitely many angles

A trig equation's solutions repeat every period. The **principal solution** lies in $[0, 2\pi)$ (for $\sin, \cos$) or $[0, \pi)$ (for $\tan$); the **general solution** packages all copies:

| Equation | General solution | Why |
|---|---|---|
| $\sin\theta = \sin\alpha$ | $\theta = n\pi + (-1)^{n} \alpha$, $n \in \mathbb{Z}$ | $\sin$ is $\alpha$ at $\alpha$ and $\pi - \alpha$ per period $2\pi$ |
| $\cos\theta = \cos\alpha$ | $\theta = 2n\pi \pm \alpha$ | $\cos$ is $\alpha$ at $\pm\alpha$ per period $2\pi$ |
| $\tan\theta = \tan\alpha$ | $\theta = n\pi + \alpha$ | $\tan$ has period $\pi$ |

:::derive title="Why $(-1)^{n}$ appears in the sine solution"
Inside $[0, 2\pi)$ the solutions of $\sin\theta = \sin\alpha$ are $\alpha$ and $\pi - \alpha$ (two symmetric points on the horizontal line $y = \sin\alpha$). Adding $2\pi$-copies: $\alpha + 2n\pi$ and $\pi - \alpha + 2n\pi = (2n+1)\pi - \alpha$. The single formula $n\pi + (-1)^{n}\alpha$ interleaves both families: even $n$ gives $2k\pi + \alpha$, odd $n$ gives $(2k+1)\pi - \alpha$ ✓. For cosine the two solutions $\pm \alpha$ are symmetric about $0$, giving $2n\pi \pm \alpha$. For tangent the period is $\pi$ and there is one solution per period.
:::

:::diagram
{"type": "graph", "ratio": 0.52, "xrange": [-1, 13.5], "yrange": [-1.5, 1.9], "xticks": [0, 1.5708, 3.1416, 4.7124, 6.2832, 7.854, 9.4248], "xticklabels": ["0", "$\\pi/2$", "$\\pi$", "$3\\pi/2$", "$2\\pi$", "$5\\pi/2$", "$3\\pi$"], "yticks": [-1, 0, 1], "title": "sin x = 1/2: two solutions per period — x = nπ + (−1)^n π/6", "hlines": [{"y": 0.5, "label": "y = 1/2"}], "curves": [{"expr": "sin(x)", "color": "#0F766E", "label": "y = sin x", "labpos": 0.35}], "points": [{"x": 0.5236, "y": 0.5, "label": "π/6", "color": "#B91C1C", "dx": -0.15, "dy": 0.3}, {"x": 2.618, "y": 0.5, "label": "5π/6", "color": "#B91C1C", "dx": -0.35, "dy": 0.3}, {"x": 6.8068, "y": 0.5, "label": "13π/6", "color": "#B91C1C", "dx": -0.75, "dy": 0.3}, {"x": 8.9012, "y": 0.5, "label": "17π/6", "color": "#B91C1C", "dx": 0.18, "dy": 0.3}]}
:::

## The discipline of solving

1. **Reduce** to one function where possible ($\sin^{2}$-type: use Pythagorean or power reduction).
2. **Find principal solutions** on one period (draw the circle or the wave).
3. **Write the general form** using the table (substitute the $\alpha$ you found).
4. **Intersect with any requested interval** by ranging over integer $n$.
5. **Check** solutions in the original equation if any step squared, divided, or used a derived identity.

:::example title="Worked. Solve $\sin x = \frac{1}{2}$ generally; count solutions in $[0, 2\pi)$"
Principal: $x = \frac{\pi}{6}, \frac{5\pi}{6}$. General: $x = n\pi + (-1)^{n} \frac{\pi}{6}$ ✓ (check $n = 2$: $2\pi + \frac{\pi}{6} = \frac{13\pi}{6}$, $\sin = \frac{1}{2}$ ✓; $n = 3$: $3\pi - \frac{\pi}{6} = \frac{17\pi}{6}$ ✓). In $[0, 2\pi)$: exactly **2** solutions.
:::

:::example title="Worked. Solve $\cos x = \frac{1}{2}$ and $\tan x = 1$ generally"
$\cos x = \cos\frac{\pi}{3} \Rightarrow x = 2n\pi \pm \frac{\pi}{3}$. $\tan x = \tan\frac{\pi}{4} \Rightarrow x = n\pi + \frac{\pi}{4}$. Checks: $\cos(\pm\frac{\pi}{3} + 2\pi) = \frac{1}{2}$ ✓; $\tan(\frac{\pi}{4} + \pi) = \tan\frac{5\pi}{4} = 1$ ✓.
:::

:::warn title="Common traps — general solutions"
- Forgetting $(-1)^{n}$: $\theta = n\pi + \alpha$ is the **tangent** form; for sine it drops half the solutions ($\sin(\pi + \alpha) = -\sin\alpha \ne \sin\alpha$).
- $\cos x = c$ with $|c| > 1$: **no solution**; $|c| = 1$: $x = 2n\pi$ (or $2n\pi + \pi$); state this before "solving".
- Mixing units inside one formula: $x = n\pi + (-1)^{n} 30^{\circ}$ is illegal — either all radians ($x = n\pi + (-1)^{n} \frac{\pi}{6}$) or all degrees ($x = n \cdot 180^{\circ} + (-1)^{n} 30^{\circ}$).
- $\tan x$ general solution adds $\pi$, not $2\pi$; period of $\tan, \cot$ is $\pi$.
- Squared equations ($\sin^{2} x = \frac{1}{4}$) give $\sin x = \pm \frac{1}{2}$ — four principal solutions per $2\pi$; do not drop the $\pm$.
:::
