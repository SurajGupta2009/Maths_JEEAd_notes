---
id: jee-01
part: jee
title: "Inverse Trigonometric Functions — Why Branches, the Six Principal Inverses"
---

## The problem: no trig function is one-to-one

A function has an inverse only if it is one-to-one (injective). Every trig function fails globally: $\sin 0 = \sin \pi = 0$, $\tan 0 = \tan \pi = 0$, and so on. Graphically, a horizontal line $y = c$ with $|c| < 1$ crosses $y = \sin x$ infinitely many times. So "$\sin^{-1}$" cannot exist on all of $\mathbb{R}$ until we **cut the domain down to a strip on which sine is one-to-one and takes every value in $[-1,1]$**.

:::intuition title="Inverse = undo: the one question that decides everything"
$y = \sin^{-1}x$ means exactly: "$y$ is the angle (in the chosen strip) whose sine is $x$". So $\sin(\sin^{-1}x) = x$ is *automatic* on the domain of $\sin^{-1}$ — but $\sin^{-1}(\sin y) = y$ only for $y$ inside the chosen strip. **All the difficulty of this chapter lives on that one asymmetry.** The strip is a convention — but once fixed (by the official principal-value ranges below), every formula is determined, and every "simplify" question is a branch-check question.
:::

## The six principal values (memorise the ranges — they are the whole syllabus)

| Function | Domain | Principal range (the branch) |
|---|---|---|
| $\sin^{-1}x$ | $[-1, 1]$ | $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$ |
| $\cos^{-1}x$ | $[-1, 1]$ | $[0, \pi]$ |
| $\tan^{-1}x$ | $\mathbb{R}$ | $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ |
| $\cot^{-1}x$ | $\mathbb{R}$ | $(0, \pi)$ |
| $\sec^{-1}x$ | $|x| \geq 1$ | $[0, \pi] \setminus \{\pi/2\}$ |
| $\csc^{-1}x$ | $|x| \geq 1$ | $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right] \setminus \{0\}$ |

Reading the table correctly: $\sin^{-1}$ is the *inverse of the restriction* $\sin : [-\pi/2, \pi/2] \to [-1,1]$; $\cos^{-1}$ inverts $\cos : [0,\pi] \to [-1,1]$; $\tan^{-1}$ inverts $\tan : (-\pi/2, \pi/2) \to \mathbb{R}$. The half-open endpoints for $\tan^{-1}$ reflect the vertical asymptotes of $\tan$.

:::assume title="Symbols and conventions used everywhere below"
- $\sin^{-1}x$ means the **inverse function** (arcsine), never $\csc x = (\sin x)^{-1}$. Write $\sin^{-1}$ / $\arcsin$ for the inverse; never write $\sin^{-1}x$ for $1/\sin x$.
- All inputs $x$ are real; ranges above are in **radians**. Degree-mode answers convert at the boundary only.
- "$\sin^{-1}(\sin y) = y$"-type claims always silently assume $y$ lies in the principal range of the outer inverse. Part of the answer is *stating* that assumption.
- $\cot^{-1}$ takes range $(0,\pi)$ (the JEE convention); some calculus texts use $(-\pi/2, 0) \cup (0, \pi/2]$ — the value of $\cot^{-1}x + \tan^{-1}x$ then changes. We fix $(0,\pi)$ throughout and note the caveat here once.
:::

## Graphs: domain on the x-axis, branch on the y-axis

:::diagram
{"type": "graph", "xrange": [-1.35, 1.35], "yrange": [-2.1, 2.1], "xticks": [-1, 0, 1], "yticks": [-2, -1, 0, 1, 2], "yticklabels": ["-2", "-1", "0", "1", "2"], "curves": [{"expr": "asin(x)", "from": -1, "to": 1, "color": "#0F766E", "label": "y = sin⁻¹x", "labpos": 0.72}], "hlines": [{"y": 1.5708, "label": "y = π/2 (range bound)"}, {"y": -1.5708, "label": "y = -π/2"}], "points": [{"x": -1, "y": -1.5708, "label": "(-1, -π/2)", "dx": -1.25, "dy": 0.15, "ha": "right"}, {"x": 1, "y": 1.5708, "label": "(1, π/2)", "dx": -1.7, "dy": 0.05, "ha": "right"}], "title": "y = sin⁻¹x : domain [-1, 1] ⊂ x-axis, branch [-π/2, π/2] ⊂ y-axis", "ratio": 0.66}
:::

:::diagram
{"type": "graph", "xrange": [-1.35, 1.35], "yrange": [-0.6, 3.75], "xticks": [-1, 0, 1], "yticks": [0, 1, 2, 3], "yticklabels": ["0", "1", "2", "3"], "curves": [{"expr": "acos(x)", "from": -1, "to": 1, "color": "#B91C1C", "label": "y = cos⁻¹x", "labpos": 0.3}], "points": [{"x": -1, "y": 3.1416, "label": "(-1, π)", "dx": 0.1, "dy": -0.45}, {"x": 1, "y": 0, "label": "(1, 0)", "dx": -1.25, "dy": 0.12, "ha": "right"}], "title": "y = cos⁻¹x : range [0, π] — note cos⁻¹1 = 0, cos⁻¹(-1) = π", "ratio": 0.66}
:::

:::diagram
{"type": "graph", "xrange": [-5.2, 5.2], "yrange": [-2.3, 2.3], "xticks": [-4, -2, 0, 2, 4], "yticks": [-2, -1, 0, 1, 2], "curves": [{"expr": "atan(x)", "from": -5.2, "to": 5.2, "color": "#16295C", "label": "y = tan⁻¹x", "labpos": 0.62}], "hlines": [{"y": 1.5708, "label": "y = π/2 (asymptote, never reached)"}, {"y": -1.5708, "label": "y = -π/2"}], "title": "y = tan⁻¹x : range (-π/2, π/2) is OPEN — the asymptotes are not values", "ratio": 0.6}
:::

Three graph-reading habits: (i) the **branch bounds are horizontal lines on the $y$-axis** — they constrain the *output*; (ii) endpoints may be attained ($\sin^{-1}$, $\cos^{-1}$) or not ($\tan^{-1}$); (iii) $\sin^{-1}$ and $\tan^{-1}$ are **odd** functions ($\sin^{-1}(-x) = -\sin^{-1}x$, $\tan^{-1}(-x) = -\tan^{-1}x$), visible as origin-symmetry; $\cos^{-1}$ is **neither** — its graph is not symmetric.

## The three complementary-pair identities (state + prove)

:::key title="Complementary sums — valid on the stated domains"
$$\sin^{-1}x + \cos^{-1}x = \frac{\pi}{2}, \qquad |x| \leq 1$$

$$\tan^{-1}x + \cot^{-1}x = \frac{\pi}{2}, \qquad x \in \mathbb{R}$$

$$\sec^{-1}x + \csc^{-1}x = \frac{\pi}{2}, \qquad |x| \geq 1$$
:::

:::derive title="Proof of the first — the template for all three"
Let $\theta = \sin^{-1}x$, so $\theta \in [-\pi/2, \pi/2]$ and $\sin\theta = x$. Then $\cos(\pi/2 - \theta) = \sin\theta = x$, and $\pi/2 - \theta \in [0, \pi]$ — which is exactly the principal range of $\cos^{-1}$. Hence $\cos^{-1}x = \pi/2 - \theta = \pi/2 - \sin^{-1}x$. ∎

The second: $\cot(\pi/2 - \theta) = \tan\theta$, and the range bookkeeping ($\pi/2 - \tan^{-1}x \in (0,\pi)$) is identical. Same for the third. **The mechanism is always: co-function identity + range verification.** The range check is not decoration — it is what makes the inverse *principal*.
:::

## Standard values (the x-values worth instant recall)

| $x$ | $\sin^{-1}x$ | $x$ | $\cos^{-1}x$ | $x$ | $\tan^{-1}x$ |
|---|---|---|---|---|---|
| $0$ | $0$ | $0$ | $\pi/2$ | $0$ | $0$ |
| $1/2$ | $\pi/6$ | $1/2$ | $\pi/3$ | $1/\sqrt{3}$ | $\pi/6$ |
| $1/\sqrt{2}$ | $\pi/4$ | $1/\sqrt{2}$ | $\pi/4$ | $1$ | $\pi/4$ |
| $\sqrt{3}/2$ | $\pi/3$ | $\sqrt{3}/2$ | $\pi/6$ | $\sqrt{3}$ | $\pi/3$ |
| $1$ | $\pi/2$ | $1$ | $0$ | — | $\to \pi/2$ |
| $-1/2$ | $-\pi/6$ | $-1/2$ | $2\pi/3$ | $-1$ | $-\pi/4$ |
| $-1$ | $-\pi/2$ | $-1$ | $\pi$ | — | $\to -\pi/2$ |

Note the systematic pattern: $\sin^{-1}$ and $\cos^{-1}$ of the same $x$ always sum to $\pi/2$; $\tan^{-1}$ of the reciprocal of $\sqrt{3}$-values is the complementary angle. Negative inputs: $\sin^{-1}$ and $\tan^{-1}$ give negative outputs (odd functions); $\cos^{-1}(-x) = \pi - \cos^{-1}x$ (output stays in $[0,\pi]$).

:::warn title="Common traps — foundations"
- $\sin^{-1}(\sin\theta) = \theta$ is **false** for e.g. $\theta = \frac{3\pi}{4}$: the left side is $\pi/4$. Trap of the entire chapter.
- $\sin(\sin^{-1}x) = x$ holds for all $x \in [-1,1]$; $\sin^{-1}(\sin x) = x$ holds only for $x \in [-\pi/2, \pi/2]$.
- Domain before value: $\sin^{-1}2$ is **undefined** in $\mathbb{R}$, not "$\pi/2$". $\cos^{-1}(1.01)$ does not exist.
- $\tan^{-1}x$ never equals $\pm\pi/2$; writing $\tan^{-1}x = \pi/2$ "as $x \to \infty$" is a limit, not a value.
- $(\sin x)^{-1} = \csc x \neq \sin^{-1}x$. The notation is genuinely ambiguous in print; our convention is stated in the ASSUMPTIONS box and used without exception.
- $\cos^{-1}x$ is not an odd function: $\cos^{-1}(-1/2) = 2\pi/3 \neq -\pi/3$.
:::
