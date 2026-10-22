---
id: jee-01
part: jee
title: "Quadratic Equations — Roots, the Discriminant, and the One Number That Decides Everything"
---

## Why one number controls the whole subject

A **quadratic equation** is $ax^{2} + bx + c = 0$ with $a \neq 0$ (if $a = 0$ it is linear, and every formula below collapses). Coefficients are real unless stated otherwise. The equation asks: where does the parabola $y = ax^{2} + bx + c$ meet the $x$-axis? Everything — nature of roots, sign of the expression, location of roots — is bookkeeping built on one quantity.

:::derive title="Completing the square forces the formula and the discriminant"
Divide by $a$ and complete the square:

$$x^{2} + \frac{b}{a}x = -\frac{c}{a} \quad \Rightarrow \quad \left(x + \frac{b}{2a}\right)^{2} = \frac{b^{2} - 4ac}{4a^{2}}$$

The left side is a square, so a real solution exists iff the right side is $\geq 0$, i.e. iff $D = b^{2} - 4ac \geq 0$. Taking roots gives the **quadratic formula**

$$x = \frac{-b \pm \sqrt{D}}{2a}, \qquad D = b^{2} - 4ac$$

$D$ is called the **discriminant** because it discriminates between the cases. Note it is $b^{2} - 4ac$, never $b^{2} + 4ac$.
:::

:::key title="The three cases — memorise with the picture"
- $D > 0$: two **distinct real** roots; the parabola crosses the axis twice.
- $D = 0$: one **repeated** real root $x = -\frac{b}{2a}$; the parabola touches the axis at its vertex.
- $D < 0$: **no real roots**, but two complex roots, always a conjugate pair $\alpha \pm i\beta$ (real coefficients force this: conjugating the equation changes nothing, so $\bar{\alpha}$ is a root whenever $\alpha$ is).

Saying "$D < 0$ means no roots" is wrong — it means no *real* roots.
:::

:::diagram
{"type": "graph", "xrange": [-4.2, 4.2], "yrange": [-3.2, 5.2], "xticks": [-3, -1, 0, 1, 2, 3], "yticks": [-2, 0, 2, 4], "xlabel": "x", "ylabel": "y", "hlines": [{"y": 0, "color": "#94A3B8"}], "curves": [{"expr": "x*x - 3*x + 2", "color": "#16295C", "label": "D>0: crosses twice (roots 1, 2)", "labpos": 0.72}, {"expr": "x*x - 2*x + 1", "color": "#0F766E", "label": "D=0: touches at x=1", "labpos": 0.9}, {"expr": "x*x - 2*x + 3", "color": "#B91C1C", "label": "D<0: never meets axis", "labpos": 0.55}], "points": [{"x": 1, "y": 0, "label": "1"}, {"x": 2, "y": 0, "label": "2"}], "title": "One parabola family, three discriminant cases", "ratio": 0.62}
:::

:::example title="Worked — reading the case off D"
$x^{2} - 5x + 6 = 0$: $D = 25 - 24 = 1 > 0$, so $x = \frac{5 \pm 1}{2}$, giving $x = 2, 3$.

$2x^{2} - 3x + 5 = 0$: $D = 9 - 40 = -31 < 0$, so $x = \frac{3 \pm i\sqrt{31}}{4}$ — non-real conjugates.

Equal roots: $x^{2} + kx + 9 = 0$ needs $D = k^{2} - 36 = 0$, so $k = \pm 6$ (both signs — a classic one-mark loss).
:::

## Rational, irrational, and conjugate root pairs

:::key title="What the coefficients force the roots to look like"
- Rational coefficients and $D$ a perfect square (of a rational) $\Leftrightarrow$ both roots **rational**.
- $D > 0$ but not a perfect square: roots are irrational **conjugates** $p \pm \sqrt{q}$ with $p, q$ rational.
- Real coefficients, $D < 0$: complex conjugates $\alpha \pm i\beta$.
- One root known of conjugate type forces the other: if $2 + \sqrt{3}$ is a root of a rational-coefficient quadratic, $2 - \sqrt{3}$ is the other root. Product $= 4 - 3 = 1$, sum $= 4$, so the equation is $x^{2} - 4x + 1 = 0$.
:::

:::warn title="Common traps — foundations"
- $D = b^{2} - 4ac$: the minus sign, and the $4$.
- "Equal roots" means $D = 0$ **and** the equation is genuinely quadratic ($a \neq 0$). If $a$ contains the parameter, check the degenerate case separately.
- If coefficients depend on a parameter, $D \geq 0$ alone does not guarantee two real roots when the equation can degenerate to linear.
- A repeated root is still a root of multiplicity two — it counts twice in Vieta's relations.
:::

:::assume title="Standing conventions for this chapter"
$a, b, c \in \mathbb{R}$, $a \neq 0$; roots denoted $\alpha, \beta$; $S = \alpha + \beta$, $P = \alpha\beta$; "roots" means complex roots counted with multiplicity unless "real roots" is said. All root-location conditions in sheet 04 assume real coefficients.
:::
