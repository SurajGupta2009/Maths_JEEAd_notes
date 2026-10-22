---
id: jee-04
part: jee
title: "n-th Roots — Exactly n, Regular Polygons; the Square-Root Formula"
---

## Solving zⁿ = w

Write $w = R(\cos\phi + i\sin\phi)$ ($R > 0$) and $z = r(\cos\theta + i\sin\theta)$ ($r > 0$). De Moivre splits the equation into two real conditions: $r^{n} = R$ and $n\theta \equiv \phi$ (mod $2\pi$).

:::key title="The $n$-th roots of $w \neq 0$ — count and geometry"
$$z_{k} = R^{1/n}\left(\cos\frac{\phi + 2k\pi}{n} + i\sin\frac{\phi + 2k\pi}{n}\right),$$

$$k = 0, 1, \dots, n - 1.$$

Exactly $n$ distinct roots: $r = R^{1/n}$ is unique, and $\theta = \frac{\phi + 2k\pi}{n}$ repeats mod $2\pi$ with period exactly $n$ in $k$. They lie on the circle $|z| = R^{1/n}$ at equal angular steps $\frac{2\pi}{n}$: **the vertices of a regular $n$-gon**. Consecutive roots differ by the factor $e^{2\pi i/n}$.
:::

:::diagram
{"type": "graph", "xrange": [-2.6, 2.6], "yrange": [-2.3, 2.5], "xticks": [-2, -1, 0, 1, 2], "yticks": [-2, -1, 0, 1, 2], "xlabel": "Re", "ylabel": "Im", "curves": [{"expr": "sqrt(3.737 - x*x)", "from": -1.933, "to": 1.933, "color": "#C8D4E6", "ls": "--"}, {"expr": "-sqrt(3.737 - x*x)", "from": -1.933, "to": 1.933, "color": "#C8D4E6", "ls": "--"}], "points": [{"x": 1.933, "y": 0, "label": "z₀", "color": "#16295C", "dx": 0.12, "dy": 0.15}, {"x": 0.5973, "y": 1.8376, "label": "z₁", "color": "#0F766E"}, {"x": -1.5636, "y": 1.1361, "label": "z₂", "color": "#0F766E"}, {"x": -1.5636, "y": -1.1361, "label": "z₃", "color": "#0F766E"}, {"x": 0.5973, "y": -1.8376, "label": "z₄", "color": "#0F766E"}], "title": "The five 5th roots of 27 on |z| = 27^{1/5} ≈ 1.933, steps of 72° — a regular pentagon", "ratio": 0.72}
:::

:::example title="Worked — cube roots of $8$ and fourth roots of $16$"
Cube roots of $8$: $R = 8, \phi = 0$: $z_{k} = 2(\cos\frac{2k\pi}{3} + i\sin\frac{2k\pi}{3})$, $k = 0,1,2$:

$$z_{0} = 2, \qquad z_{1} = -1 + i\sqrt{3}, \qquad z_{2} = -1 - i\sqrt{3}.$$

Check $z_{1}^{3}$: $-1 + i\sqrt{3} = 2e^{2\pi i/3}$, cube $= 8 e^{2\pi i} = 8$ ✓.

Fourth roots of $16$: $r = 2$, angles $\frac{k\pi}{2}$: $\{2, 2i, -2, -2i\}$ — the square inscribed in $|z| = 2$.

Cube roots of $-27$: $R = 27$, $\phi = \pi$: $\{-3,\ \frac{3}{2} \pm i\frac{3\sqrt{3}}{2}\}$ — equilateral triangle centered at $0$; Vieta on $t^{3} + 27 = 0$ immediately gives $z_{1} + z_{2} + z_{3} = 0$ and $z_{1}z_{2} + z_{2}z_{3} + z_{3}z_{1} = 0$ — the geometry *explains* Vieta here.
:::

## Square roots of an arbitrary complex number — the explicit formula

:::key title="Formula (derived, not guessed)"
For $w = a + bi$, $r = |w| = \sqrt{a^{2} + b^{2}}$: the two square roots of $w$ are

$$\pm\left(\sqrt{\frac{r + a}{2}} + i\operatorname{sgn}(b)\sqrt{\frac{r - a}{2}}\right) \qquad (b \neq 0)$$

with the sign of the imaginary part tied to the sign of $b$ (for $b = 0$: $\sqrt{a}$ or $i\sqrt{-a}$ by the sign of $a$).
:::

:::derive title="Derivation — match parts"
Seek $\sqrt{a + bi} = x + iy$ with $x, y \in \mathbb{R}$. Squaring: $(x + iy)^{2} = x^{2} - y^{2} + 2xyi = a + bi$, so $x^{2} - y^{2} = a$, $2xy = b$. Also $|x + iy|^{2} = x^{2} + y^{2} = |w| = r$. Add and subtract:

$$x^{2} = \frac{r + a}{2}, \qquad y^{2} = \frac{r - a}{2}$$

(both $\geq 0$ since $|a| \leq r$), and $xy = \frac{b}{2}$ forces $x, y$ to share the sign of $b$ (with $x > 0$ by convention). ∎

Worked: $\sqrt{3 + 4i}$: $r = 5$: $x^{2} = 4$, $y^{2} = 1$, $b > 0$: roots $\pm(2 + i)$ ✓ ($(2 + i)^{2} = 3 + 4i$). $\sqrt{-3 + 4i}$: $r = 5$: $x^{2} = 1$, $y^{2} = 4$: roots $\pm(1 + 2i)$ ✓. $\sqrt{4i}$: $r = 4$, $a = 0$: $x^{2} = y^{2} = 2$, $b > 0$: $\pm(\sqrt{2} + i\sqrt{2})$ ✓ ($( \sqrt{2} + i\sqrt{2})^{2} = 2(1 + i)^{2} = 4i$).
:::

:::warn title="Common traps — roots"
- **"Find the cube roots"** means all $n$ of them: "the cube root of 8" as a complete answer is $\{2, -1 \pm i\sqrt{3}\}$.
- $\sqrt{w}$ written bare usually means the **principal** root (arg in $(-\frac{\pi}{2}, \frac{\pi}{2}]$); "find the square roots" means both.
- **Never distribute roots over products for complex numbers**: $\sqrt{(-1)^{2}} = 1$ but $(\sqrt{-1})^{2} = -1$; $\sqrt{z}\sqrt{w} \neq \sqrt{zw}$ in general. Solve $z^{n} = w$ from scratch instead.
- The sign in the square-root formula is $\operatorname{sgn}(b)$ on the imaginary part (and $x > 0$) — mixing it up gives a root of $\bar w$ instead of $w$.
- Roots of $0$: only $z = 0$ (the formula and the count assume $w \neq 0$).
- Rational exponents $w^{p/q}$: reduce $p/q$ to lowest terms, then read as "$q$-th roots raised to $p$" — exactly the parity discipline of chapter 2's rational exponents.
:::
