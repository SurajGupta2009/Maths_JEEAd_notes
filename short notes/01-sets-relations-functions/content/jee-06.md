---
id: jee-06
part: jee
title: "Special Functions & Graph Transformations — |x|, sgn, [x], {x}"
---

## The standard library (know the graphs cold)

- **Absolute value:** $|x| = x$ for $x \geq 0$, $-x$ for $x < 0$. Always $\geq 0$; $|x| = \sqrt{x^{2}}$; triangle inequality $|a + b| \leq |a| + |b|$ with equality iff $a, b$ have the same sign (or one is 0).
- **Signum:** $\operatorname{sgn}(x) = 1$ ($x > 0$), $0$ ($x = 0$), $-1$ ($x < 0$). So $x = |x| \operatorname{sgn}(x)$ for all $x$.
- **Greatest integer (floor):** $[x] = \lfloor x \rfloor$ = greatest integer $\leq x$. Fundamental sandwich: $[x] \leq x < [x] + 1$, equivalently $x = [x] + \{x\}$ with **fractional part** $\{x\} = x - [x] \in [0,1)$.
- **Exponential / logarithm:** $e^{x} : \mathbb{R} \to (0,\infty)$ strictly increasing; $\ln x : (0,\infty) \to \mathbb{R}$ its inverse. $e^{\ln x} = x$ ($x > 0$), $\ln e^{x} = x$ (all $x$).

:::diagram
{
  "type": "graph",
  "title": "Floor function y = [x]: right-continuous jumps at every integer (open circle = value excluded, closed = included)",
  "xrange": [-3.4, 3.4],
  "yrange": [-3.4, 3.4],
  "xticks": [-3, -2, -1, 0, 1, 2, 3],
  "yticks": [-3, -2, -1, 0, 1, 2, 3],
  "curves": [
    {"expr": "floor(x)", "from": -3.4, "to": -2, "color": "#0F766E", "n": 50, "labpos": 0.5},
    {"expr": "floor(x)", "from": -2, "to": -1, "color": "#0F766E", "n": 50},
    {"expr": "floor(x)", "from": -1, "to": 0, "color": "#0F766E", "n": 50},
    {"expr": "floor(x)", "from": 0, "to": 1, "color": "#0F766E", "n": 50},
    {"expr": "floor(x)", "from": 1, "to": 2, "color": "#0F766E", "n": 50},
    {"expr": "floor(x)", "from": 2, "to": 3, "color": "#0F766E", "n": 50}
  ],
  "points": [
    {"x": -2, "y": -3, "label": "jump at every integer k", "dx": 0.15, "dy": -0.85, "ha": "left", "color": "#B91C1C"},
    {"x": 1, "y": 1, "label": "closed at (k, k)", "color": "#0F766E"},
    {"x": 1, "y": 0, "label": "open at (k, k-1)", "color": "#B8860B"}
  ],
  "annotations": []
}
:::

:::warn
- $\sqrt{x^{2}} = |x|$, never $x$: $\sqrt{(-3)^{2}} = 3$, not $-3$.
- $[x]$ jumps by 1 at integers: $[0.999] = 0$ but $[1] = 1$. Draw open/closed dots explicitly — $[x]$ is **right-continuous**: value at the jump equals the right limit.
- $[x] + [-x] = 0$ if $x \in \mathbb{Z}$, else $-1$. $\{x\} + \{-x\} = 0$ if $x \in \mathbb{Z}$, else $1$.
- $e^{x} > 0$ always: "$e^{x} = -2$" has no solution. $\ln x$ of a negative argument is undefined in $\mathbb{R}$.
- $|x| = x$ iff $x \geq 0$ (equality includes 0 — boundary!).
:::

## Graph transformations (one picture, many curves)

:::key
From $y = f(x)$: $f(x) + c$ shifts **up** $c$; $f(x + c)$ shifts **left** $c$ (mind the sign); $a f(x)$ scales vertically; $f(ax)$ scales horizontally by $1/|a|$ and reflects if $a < 0$; $|f(x)|$ reflects every negative lobe **upward** (creates cusps at old zeros); $f(|x|)$ keeps $x \geq 0$ and mirrors it into $x < 0$ (even function); $\{f(x)\}$ wraps each value into $[0,1)$ (sawtooth along the curve); $1/f(x)$ turns zeros into vertical asymptotes and bounds into horizontal ones.
:::

:::diagram
{
  "type": "graph",
  "title": "y = |x^2 - 3x + 2| (solid) from y = x^2 - 3x + 2 (dashed): roots at 1, 2 become cusps",
  "xrange": [-1.2, 4.2],
  "yrange": [-1.5, 5.5],
  "xticks": [-1, 0, 1, 2, 3, 4],
  "yticks": [-1, 0, 1, 2, 3, 4, 5],
  "curves": [
    {"expr": "x*x - 3*x + 2", "color": "#B8860B", "lw": 2.2, "ls": "--", "label": "x^2-3x+2", "labpos": 0.12},
    {"expr": "abs(x*x - 3*x + 2)", "color": "#0F766E", "lw": 3.2, "label": "|x^2-3x+2|", "labpos": 0.93}
  ],
  "points": [
    {"x": 1, "y": 0, "label": "(1, 0) cusp", "color": "#B91C1C", "dx": -1.35, "dy": 0.3, "ha": "right"},
    {"x": 2, "y": 0, "label": "(2, 0) cusp", "color": "#B91C1C", "dx": 0.15, "dy": 0.3},
    {"x": 1.5, "y": 0.75, "label": "vertex (1.5, 0.75)", "color": "#16295C", "dx": -0.2, "dy": -1.15, "ha": "center"},
    {"x": 0, "y": 2, "label": "(0, 2)", "color": "#16295C", "dx": 0.18, "dy": 0.25}
  ]
}
:::

:::example
**Worked.** Sketch $y = \{x\} = x - [x]$: straight segments of slope 1 from each integer up to, but not including, the next integer height 1; value 0 exactly at integers (closed dots at $(k,0)$, open dots at $(k,1)$). Range $[0,1)$ — half-open, every time. Then $\{3.7\} = 0.7$, $\{-1.2\} = 0.8$ (because $[-1.2] = -2$). **Check:** $\{x\} \in [0,1)$ for negatives too — the floor of a negative number is the integer to its **left**, not "the integer part" of the digits.
:::

:::app
**Standard application.** Solve $|x - 1| + |x - 3| = 4$ by breaking at the knots $x = 1, 3$: on $x < 1$: $(1-x) + (3-x) = 4 \Rightarrow x = 0$ ✓; on $1 \leq x < 3$: $(x-1)+(3-x) = 2 \ne 4$; on $x \geq 3$: $(x-1)+(x-3)=4 \Rightarrow x = 4$ ✓. Solution set $\{0, 4\}$. **Check boundaries:** $x = 1$ gives $0+2 = 2$; $x = 3$ gives $2+0 = 2$ — knots must be tested separately, they belong to exactly one case each.
:::
