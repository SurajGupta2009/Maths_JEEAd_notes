---
id: jee-02
part: jee
title: "Argument and Polar Form — Multiplication is Stretch × Rotate"
---

## The argument: the direction half of the data

For $z = a + bi \neq 0$, an **argument** is any $\theta$ with $a = |z|\cos\theta$, $b = |z|\sin\theta$; arguments form the set $\arg z = \{\theta_{0} + 2k\pi : k \in \mathbb{Z}\}$ (multi-valued — angles add only mod $2\pi$). The **principal argument** is the canonical choice

$$\operatorname{Arg} z \in (-\pi, \pi].$$

Note the half-open window: $\operatorname{Arg}(-1) = \pi$, never $-\pi$; $\operatorname{Arg}$ of a fourth-quadrant point is negative. The quadrant of $(a, b)$ fixes the reference angle — that check is the whole skill.

:::key title="The standard Arg table (instant recall)"
$$\operatorname{Arg} 1 = 0, \quad \operatorname{Arg} i = \frac{\pi}{2}, \quad \operatorname{Arg}(-1) = \pi,$$

$$\operatorname{Arg}(-i) = -\frac{\pi}{2}$$

$$\operatorname{Arg}(1 + i) = \frac{\pi}{4}, \quad \operatorname{Arg}(-1 + i) = \frac{3\pi}{4},$$

$$\operatorname{Arg}(1 - i\sqrt{3}) = -\frac{\pi}{3}$$

(Read $\operatorname{Arg}(-1 + i) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$ — quadrant II, *not* $-\frac{\pi}{4}$.)
:::

:::assume title="Conventions for $\arg$ and $\operatorname{Arg}$"
- $\arg z$ (lowercase) = the full set of angles; statements like $\arg(z_{1}z_{2}) = \arg z_{1} + \arg z_{2}$ mean **equality of sets mod $2\pi$**.
- $\operatorname{Arg}$ (capitalised) = the principal value in $(-\pi, \pi]$; it is *not* additive: $\operatorname{Arg}(z_{1}z_{2}) = \operatorname{Arg} z_{1} + \operatorname{Arg} z_{2} - 2\pi\epsilon$ with $\epsilon \in \{-1, 0, 1\}$ chosen to land in the window.
- $z = 0$ has no argument; $\arg \bar z = -\arg z$, $\arg(1/z) = -\arg z$, $\arg(z^{n}) = n \arg z$ (as sets).
:::

## Polar form

Every $z \neq 0$ is uniquely $z = r(\cos\theta + i\sin\theta)$ with $r = |z| > 0$, $\theta \in \arg z$; the principal polar form takes $\theta = \operatorname{Arg} z$. Round trip check: expand $r\cos\theta + i\,r\sin\theta$ to get $a + bi$ back.

:::derive title="Why products add angles — the calculation that seeds the subject"
Let $z_{1} = r_{1}(\cos\theta_{1} + i\sin\theta_{1})$, $z_{2} = r_{2}(\cos\theta_{2} + i\sin\theta_{2})$. Expanding:

$$z_{1}z_{2}$$

$$z_{1}z_{2} = r_{1}r_{2}[(\cos\theta_{1}\cos\theta_{2} - \sin\theta_{1}\sin\theta_{2})$$

$$+ \, i(\cos\theta_{1}\sin\theta_{2} + \sin\theta_{1}\cos\theta_{2})]$$

$$= r_{1}r_{2}\left(\cos(\theta_{1} + \theta_{2}) + i\sin(\theta_{1} + \theta_{2})\right)$$

by the addition formulas from trigonometry. **Multiplication stretches by $r_{1}r_{2}$ and rotates by $\theta_{1} + \theta_{2}$.** Division: divide moduli, subtract arguments. This is "multiplication is rotation" made exact, and it is where $\arg(z_{1}z_{2}) = \arg z_{1} + \arg z_{2}$ comes from.
:::

:::example title="Worked — convert $-\sqrt{3} + i$ and $1 - i\sqrt{3}$, with checks"
$-\sqrt{3} + i$: $r = 2$, quadrant II, reference $\tan^{-1}\frac{1}{\sqrt{3}} = \frac{\pi}{6}$, so $\theta = \frac{5\pi}{6}$:

$$-\sqrt{3} + i = 2\left(\cos\frac{5\pi}{6} + i\sin\frac{5\pi}{6}\right).$$

Back: $2\cos\frac{5\pi}{6} = -\sqrt{3}$ ✓, $2\sin\frac{5\pi}{6} = 1$ ✓.

$1 - i\sqrt{3}$: $r = 2$, quadrant IV, $\operatorname{Arg} = -\frac{\pi}{3}$ — the same magnitude as $\frac{\pi}{3}$ but **negative**: $1 - i\sqrt{3} = 2(\cos(-\frac{\pi}{3}) + i\sin(-\frac{\pi}{3}))$.

$\frac{1}{1 + i} = \frac{1 - i}{2} = \frac{1}{\sqrt{2}}(\cos(-\frac{\pi}{4}) + i\sin(-\frac{\pi}{4}))$ — check via the rules: $|1/(1+i)| = 1/\sqrt{2}$ ✓, $\arg = -\arg(1 + i) = -\frac{\pi}{4}$ ✓. Both languages agree; use one to check the other.
:::

:::key title="Multiplication by $i$ and by $e^{i\theta}$ — the rotation reflex"
$i(a + bi) = -b + ai$: the point $(a, b) \mapsto (-b, a)$ — length preserved ($a^{2} + b^{2}$ unchanged; $|iz| = |i||z| = |z|$), dot product $(a,b)\cdot(-b,a) = 0$, orientation $(1,0) \mapsto (0,1)$: a $90^{\circ}$ counterclockwise turn. So $\times i$ = quarter-turn CCW, $\times(-1)$ = half-turn, $\times(-i)$ = quarter-turn clockwise, $\times\, re^{i\theta}$ = stretch $r$ + rotate $\theta$.
:::

:::app title="Where this pays off — the two-language method"
Translate the problem into whichever language makes it visible, solve, translate back. "Solve $iz = \bar z$": algebra $z = a + bi$, $iz = -b + ai = a - bi = \bar z \Rightarrow a = -b$: the line $y = -x$. Geometry: rotating $z$ by $90^{\circ}$ gives its mirror — the line at $-45^{\circ}$. Same answer, two sentences; if they disagree, one of them is wrong — that is the check.
:::

:::warn title="Common traps — argument and polar"
- Principal window is $(-\pi, \pi]$: $\operatorname{Arg}(-1) = \pi$; $\operatorname{Arg}(-i) = -\frac{\pi}{2}$; fourth-quadrant arguments are negative.
- "$\arg z = \theta$" statements are mod $2\pi$; when a problem asks for *the* argument it usually means $\operatorname{Arg}$ — state which you are giving.
- $\operatorname{Arg}$ is not additive across products; $\arg$ (the set) is. Using principal values in De Moivre without reducing mod $2\pi$ is the classic wrong-answer machine.
- $z = r(\cos\theta + i\sin\theta)$ with $r > 0$; writing $r < 0$ just shifts $\theta$ by $\pi$ — keep $r$ positive and $\theta$ absorbing the sign.
- $\operatorname{Arg}(z_{1}/z_{2}) \neq \operatorname{Arg} z_{1} - \operatorname{Arg} z_{2}$ blindly: $z_{1} = 1, z_{2} = -1$ gives $\operatorname{Arg}(-1) = \pi$ while the naive difference $0 - \pi = -\pi$ sits outside the window. The correct statement: $\operatorname{Arg}(z_{1}/z_{2}) \equiv \operatorname{Arg} z_{1} - \operatorname{Arg} z_{2} (\text{mod } 2\pi)$, then **reduce into $(-\pi, \pi]$**.
:::
