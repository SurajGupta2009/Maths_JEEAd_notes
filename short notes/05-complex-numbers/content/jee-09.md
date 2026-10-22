---
id: jee-09
part: jee
title: "Loci II — Argument Conditions: Arcs of Circles; the Ellipse Case"
---

## The inscribed-angle condition arg((z − a)/(z − b)) = θ

$\arg\frac{z - a}{z - b}$ is the directed angle from the ray $z \to b$ to the ray $z \to a$ (mod $2\pi$). Fixing it at $\theta$ with $0 < |\theta| < \pi$ says: **the chord $ab$ subtends the constant angle $\theta$ at $z$** — by the inscribed-angle theorem, the locus is an **arc of a circle through $a$ and $b$** (two arcs qualify; the sign/orientation of $\theta$ selects one).

:::key title="Construction (memorise the two formulas)"
For chord $ab$ and angle $\theta$ with $0 < |\theta| < \pi$:

$$R = \frac{|a - b|}{2\sin|\theta|},$$

$$\text{center on the perpendicular bisector of } ab$$

$$\text{ at distance } \frac{|a - b|}{2}\cot|\theta| \text{ from the midpoint}$$

on the side that makes the inscribed angle $|\theta|$; the locus is the arc **opposite the center** (the major arc when $|\theta| < \frac{\pi}{2}$), excluding $a$ and $b$ themselves (the fraction is $0$ or undefined there).

Ray version: $\arg(z - a) = \theta$ is the **ray** from $a$ at angle $\theta$ (excluding $a$).
:::

:::example title="Worked — $\arg\frac{z - 1}{z + 1} = \frac{\pi}{4}$"
$a = 1$, $b = -1$: chord length $2$: $R = \frac{2}{2\sin(\pi/4)} = \sqrt{2}$; midpoint $0$; center on the imaginary axis at distance $\cot\frac{\pi}{4} = 1$: center $C = i$ (the side is decided by testing a point). Test the top of the circle $z = i(1 + \sqrt{2})$: $\arg(z - 1) = \pi - \frac{3\pi}{8} = \frac{5\pi}{8}$, $\arg(z + 1) = \frac{3\pi}{8}$, difference $\frac{\pi}{4}$ ✓ — so the locus is the **upper arc** of $x^{2} + (y - 1)^{2} = 2$ ($y > 0$), endpoints $\pm 1$ excluded.

(Needed value: $\tan\frac{3\pi}{8} = \sqrt{2} + 1$, the half-angle tangent of $45^{\circ}$ — worth knowing.)
:::

:::diagram
{"type": "graph", "xrange": [-2.6, 2.6], "yrange": [-1.6, 3.4], "xticks": [-2, -1, 0, 1, 2], "yticks": [-1, 0, 1, 2, 3], "xlabel": "Re", "ylabel": "Im", "curves": [{"expr": "1 + sqrt(2 - x*x)", "from": -1.4142, "to": 1.4142, "color": "#0F766E", "lw": 3.2, "label": "locus: upper arc, arg((z-1)/(z+1)) = π/4", "labpos": 0.5}, {"expr": "1 - sqrt(2 - x*x)", "from": -1.4142, "to": 1.4142, "color": "#B91C1C", "ls": "--", "label": "rest of the circle |z-i| = √2 (not in locus)", "labpos": 0.55}], "points": [{"x": 1, "y": 0, "label": "a = 1 (excluded)", "color": "#16295C"}, {"x": -1, "y": 0, "label": "b = -1 (excluded)", "color": "#16295C"}, {"x": 0, "y": 1, "label": "C = i", "color": "#B8860B", "dx": -1.2, "dy": -0.25, "ha": "right"}, {"x": 0, "y": 2.4142, "label": "test point i(1+√2)", "color": "#B8860B"}], "title": "arg((z-1)/(z+1)) = π/4 : arc of |z - i| = √2 above the chord [-1, 1], endpoints excluded", "ratio": 0.7}
:::

## Ellipses — |z − A| + |z − B| = 2a₀

Sum of distances to two fixed points constant $2a_{0}$: an **ellipse** with foci $A, B$ when $2a_{0} > |A - B|$; semi-major $a_{0}$, semi-minor $b_{0} = \sqrt{a_{0}^{2} - c^{2}}$ with $2c = |A - B|$. The **maximum of $|\operatorname{Im} z|$ is $b_{0}$** (top of the minor axis) when the foci are real.

:::example title="Worked — $|z - 1| + |z + 1| = 6$: max of $\operatorname{Im} z$"
Foci $\pm 1$: $2c = 2$, $c = 1$; $2a_{0} = 6$, $a_{0} = 3$; $b_{0} = \sqrt{9 - 1} = 2\sqrt{2}$. Max $\operatorname{Im} z = 2\sqrt{2}$ at $z = \pm i 2\sqrt{2}$: check $|i2\sqrt{2} - 1| = \sqrt{1 + 8} = 3$, same for $+1$, sum $6$ ✓.

**Check the constant first:** $|z - 1| + |z + 1| = 2$ is the segment $[-1, 1]$ ($2a_{0} = 2c$: degenerate); $= 1$ is empty. The inequality $2a_{0} > 2c$ must be verified before any ellipse work.
:::

:::app title="Argument vs modulus — the two-branch decision tree"
Condition is a **modulus** of a linear fraction $= k$? Apollonius circle. **Modulus sum** $=$ const? ellipse (or segment/empty). **Argument** of a fraction $=$ const? arc of circle. **Arg of a linear term** $=$ const? ray. **Real/imaginary part** $=$ const? line. Mixed conditions ($|z - a| = r$ *and* $\arg z = \theta$)? Intersections — usually 0, 1 or 2 points: draw the circle and the ray, count.
:::

:::warn title="Common traps — argument loci"
- Endpoints $a, b$ are **never** on the locus (the fraction is $0$ or $\infty$ there) — exclude them explicitly.
- The arc selection: test one point (as in the worked example) or track the sign of $\theta$; the other arc gives $\arg = -\theta$ or $\pi - \theta$-type values.
- $\arg w = \theta$ fixes $w$ to one **ray**; $\arg w \in (\theta_{1}, \theta_{2})$ is a sector; $\arg(w) = \theta$ or $\theta + \pi$ is a *line* through the origin in the $w$-plane — read the shape from the allowed set of values.
- Ellipse formula $b_{0} = \sqrt{a_{0}^{2} - c^{2}}$ needs $a_{0} \geq c$; foci on the real axis is assumed for "$\max \operatorname{Im} z = b_{0}$" — for general foci rotate accordingly (or work with $|z|$-distances).
- $\arg\frac{z - a}{z - b}$ at $z$ on the *major* arc vs *minor* arc: the two arcs see the chord under supplementary angles $\theta$ and $\pi - \theta$; only one matches the given directed value.
:::
