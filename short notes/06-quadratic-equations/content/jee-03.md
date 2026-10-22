---
id: jee-03
part: jee
title: "The Quadratic Expression — Sign, Vertex, Range, and When It Never Changes Sign"
---

## The expression as a function

:::derive title="Completed-square form reads off everything"
$$ax^{2} + bx + c = a\left(x + \frac{b}{2a}\right)^{2} - \frac{D}{4a}$$

The square term is $\geq 0$, so the extremum sits at the **vertex** $x_{v} = -\frac{b}{2a}$ and equals $-\frac{D}{4a} = \frac{4ac - b^{2}}{4a}$: a **minimum** if $a > 0$, a **maximum** if $a < 0$. The axis of symmetry is $x = -\frac{b}{2a}$.
:::

:::example title="Worked — vertex without calculus"
$x^{2} - 6x + 11 = (x - 3)^{2} + 2$: minimum $2$ at $x = 3$. $-x^{2} + 4x - 1 = -(x - 2)^{2} + 3$: maximum $3$ at $x = 2$. For $y = 2x^{2} - 8x + 5$: $x_{v} = \frac{8}{4} = 2$, $y_{v} = \frac{40 - 64}{8} = -3$; vertex $(2, -3)$, axis $x = 2$.
:::

:::key title="Sign analysis — the picture that solves every inequality"
With real roots $\alpha < \beta$: for $a > 0$ the expression is **positive outside** $[\alpha, \beta]$ and **negative between** them ("outside positive, inside negative" for an upward parabola). For $a < 0$ all signs reverse. If $D < 0$ the sign never changes: it is the sign of $a$ everywhere. Solve $ax^{2} + bx + c > 0$ by roots-then-intervals, never by testing a random middle point. $x^{2} - 5x + 6 < 0 \Leftrightarrow 2 < x < 3$.
:::

:::diagram
{"type": "graph", "xrange": [-1.2, 6.2], "yrange": [-2.6, 6.5], "xticks": [0, 1, 2, 3, 4, 5, 6], "yticks": [-2, 0, 2, 4, 6], "xlabel": "x", "ylabel": "y", "hlines": [{"y": 0, "color": "#94A3B8"}], "vlines": [{"x": 2.5, "color": "#94A3B8", "ls": "--"}], "curves": [{"expr": "x*x - 5*x + 6", "color": "#16295C", "label": "y = x²−5x+6 (a>0)", "labpos": 0.97}], "points": [{"x": 2, "y": 0, "label": "α=2"}, {"x": 3, "y": 0, "label": "β=3"}, {"x": 2.5, "y": -0.25, "label": "vertex x=5/2 (min −1/4)", "dy": -0.85}], "annotations": [{"x": 0.4, "y": 3.4, "text": "+ outside"}, {"x": 2.15, "y": -1.9, "text": "− between"}, {"x": 4.6, "y": 3.4, "text": "+ outside"}], "title": "Sign of a quadratic: + outside the roots, − between (a>0)", "ratio": 0.6}
:::

:::key title="Never-negative / always-positive conditions"
$ax^{2} + bx + c \geq 0$ for **all** real $x$ $\Leftrightarrow$ $a > 0$ **and** $D \leq 0$. Similarly $\leq 0$ for all $x$ $\Leftrightarrow$ $a < 0$ and $D \leq 0$. Both conditions are needed: $D \leq 0$ with $a < 0$ gives an always-*negative* expression. This pair is the standard engine for parameter ranges and later powers the discriminant method for ranges of rational functions.

**Range on all of $\mathbb{R}$:** $a > 0$: $\left[\frac{4ac-b^{2}}{4a}, \infty\right)$; $a < 0$: $\left(-\infty, \frac{4ac-b^{2}}{4a}\right]$. On a restricted interval, check whether the vertex lies inside; if not, the extremum is at an endpoint.
:::

:::warn title="Common traps — the expression"
- Calling $\frac{4ac-b^{2}}{4a}$ a maximum when $a > 0$ — it is a minimum; the sign of $a$ decides.
- Sign pattern quoted without the sign of $a$.
- "Always positive" written with $D < 0$ but strict/non-strict mixed up: $> 0$ for all $x$ needs $a > 0, D < 0$; $\geq 0$ allows $D = 0$ (touching zero at one point).
- On interval range problems, using the vertex value when the vertex is outside the interval.
:::

:::intuition title="AM–GM is this sheet in disguise"
For $x > 0$, $x + \frac{k}{x} \geq 2\sqrt{k}$ is $(\sqrt{x} - \frac{\sqrt{k}}{\sqrt{x}})^{2} \geq 0$ — a perfect square, i.e. a $D = 0$ quadratic. Least value of $x + \frac{4}{x}$ is $4$ at $x = 2$. Most "quadratic-flavoured" extrema are a vertex or a square in hiding.
:::
