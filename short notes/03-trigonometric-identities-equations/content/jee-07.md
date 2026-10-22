---
id: jee-07
part: jee
title: "Trigonometric Equations II — Factorise, Combine, Filter"
---

## Method 1 — factorise, never divide

Bring everything to one side and factor. Solve each factor with the master forms.

:::example title="Worked. Solve $\sin 2x = \cos x$"
$2 \sin x \cos x = \cos x \Rightarrow \cos x (2 \sin x - 1) = 0 \Rightarrow \cos x = 0$ **or** $\sin x = \frac{1}{2}$. So $x = \frac{\pi}{2} + n\pi$ or $x = n\pi + (-1)^{n} \frac{\pi}{6}$. In $[0, 2\pi)$: $\frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}, \frac{3\pi}{2}$ — four solutions ✓ (each verifies in $\sin 2x = \cos x$). **Dividing by $\cos x$ would have destroyed the $\frac{\pi}{2}, \frac{3\pi}{2}$ family** — the classic trap.
:::

:::warn title="Golden rule — never divide by a trig expression"
$\cos x$ vanishes somewhere, so cancelling it loses solutions. Multiply out, bring over, factor. Same for $\sin x$, $\tan x$, and for any substitution step — check what it excludes.
:::

## Method 2 — the harmonic form $a \sin x + b \cos x = c$

Write $a \sin x + b \cos x = R \sin(x + \varphi)$ with $R = \sqrt{a^{2} + b^{2}}$ and $\tan\varphi = b/a$ (quadrant of $\varphi$ fixed by signs of $a, b$). Then $\sin(x + \varphi) = c/R$, which needs $|c| \leq R$ — the **compatibility test** (no solution if $|c| > R$; one per period if $|c| = R$; two per period if $|c| < R$).

:::derive title="Worked. Solve $\sqrt{3} \sin x + \cos x = 1$"
$R = \sqrt{3 + 1} = 2$; $\tan\varphi = \frac{1}{\sqrt{3}}$, $\cos\varphi = \frac{\sqrt{3}}{2}$, $\sin\varphi = \frac{1}{2} \Rightarrow \varphi = \frac{\pi}{6}$. So $2 \sin(x + \frac{\pi}{6}) = 1 \Rightarrow \sin(x + \frac{\pi}{6}) = \frac{1}{2} \Rightarrow x + \frac{\pi}{6} = n\pi + (-1)^{n} \frac{\pi}{6}$. Even $n = 2k$: $x = 2k\pi$; odd $n = 2k+1$: $x = 2k\pi + \frac{2\pi}{3}$. In $[0, 2\pi)$: $x = 0, \frac{2\pi}{3}$ ✓ (check $x = 0$: $0 + 1 = 1$ ✓; $x = \frac{2\pi}{3}$: $\sqrt{3} \cdot \frac{\sqrt{3}}{2} - \frac{1}{2} = 1$ ✓).
:::

## Method 3 — polynomial in one ratio

$2 \cos^{2} x + 3 \sin x = 0 \Rightarrow 2(1 - \sin^{2} x) + 3 \sin x = 0 \Rightarrow 2 \sin^{2} x - 3 \sin x - 2 = 0 \Rightarrow (2 \sin x + 1)(\sin x - 2) = 0$. Only $\sin x = -\frac{1}{2}$ is admissible ($\sin x = 2$ is impossible — range!) $\Rightarrow x = \frac{7\pi}{6}, \frac{11\pi}{6}$ per period. **Always clip roots of the polynomial to $[-1, 1]$** for $\sin/\cos$.

## Method 4 — squaring (last resort) and filtering

$\sin x + \cos x = 1$: square $\Rightarrow 1 + \sin 2x = 1 \Rightarrow \sin 2x = 0 \Rightarrow x = \frac{n\pi}{2}$. Squaring **added** roots: check each in the original: $x = 0$ ✓, $x = \frac{\pi}{2}$ ✓, $x = \pi$ gives $-1 \ne 1$ ✗, $x = \frac{3\pi}{2}$ gives $-1 \ne 1$ ✗. Final: $x = 2n\pi$ or $x = \frac{\pi}{2} + 2n\pi$. (Better: rewrite as $\sqrt{2} \sin(x + \frac{\pi}{4}) = 1$ — Method 2 avoids ghosts entirely.)

:::diagram
{"type": "numberline", "xrange": [-0.5, 7], "xticks": [0, 1.5708, 3.1416, 4.7124, 6.2832], "xticklabels": ["0", "$\\pi/2$", "$\\pi$", "$3\\pi/2$", "$2\\pi$"], "title": "Interval filtering: solutions of √3 sin x + cos x = 1 in [0, 2π) — the general form must be ranged over n", "marks": [{"kind": "points", "pts": [0, 2.0944], "label": "x = 0, 2π/3 ✓ (in [0, 2π))", "color": "#B91C1C"}, {"kind": "interval", "a": 0, "b": 6.2832, "label": "requested interval [0, 2π)", "color": "#0F766E"}]}
:::

:::key
**Method chooser.** (1) Can I factor? Factor (Method 1). (2) Is it $a \sin x + b \cos x$? Harmonic form (Method 2 — it also tests solvability). (3) Is it quadratic in one ratio? Substitute and clip to range (Method 3). (4) Absolute values? Split cases per interval of the inside expression. (5) Only if desperate: square, then filter (Method 4).
:::

:::warn title="Traps — equations II"
- $\sin 2x = \cos x$-type: convert to one angle multiple only after moving everything to one side.
- Polynomial in $\sin x$: reject $|\sin x| > 1$ roots **before** writing answers.
- Squaring: every step after it is suspect; verify all candidates in the original.
- Counting problems ("how many roots in $[a, b]$?"): draw the wave, count crossings — then convert the general solution with the right integer range for $n$.
- $\tan x = \tan y \Rightarrow x = y + n\pi$ only; it is **not** $x = y + 2n\pi$.
:::
