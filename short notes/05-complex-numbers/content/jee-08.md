---
id: jee-08
part: jee
title: "Loci I — Modulus Conditions: Circles, Bisectors, Apollonius, Regions"
---

## Reading loci off the page

$|z - z_{0}| = r$ **is** the circle of center $z_{0}$ and radius $r$; the exam skill is recognising circle conditions in disguise.

:::key title="The locus dictionary (modulus side)"
$$|z - z_{0}| = r \ \text{circle}; \qquad |z - z_{0}| < r \ \text{open disk}$$

$$|z - a| = |z - b| \ \text{perpendicular bisector of } ab;$$

$$\operatorname{Re} z = c \ \text{vertical line};$$

$$\operatorname{Im} z = d \ \text{horizontal line}$$

$$|z - a| = k|z - b| \ (k \neq 1) \ \text{circle (Apollonius)};$$

$$|z - a| + |z - b| = 2a_{0} \ \text{ellipse (if } 2a_{0} > |a - b|)$$

$$|z - a| + |z - b| = |a - b| \ \text{the segment } ab \ \text{itself};$$

$$< |a - b| \ \text{empty set}$$
:::

:::derive title="Apollonius circle — derived once, used forever"
$|z - a| = k|z - b|$, square: $|z|^{2} - z\bar a - \bar z a + |a|^{2} = k^{2}(|z|^{2} - z \bar b - \bar z b + |b|^{2})$. Collect (with $k \neq 1$): $(1 - k^{2})|z|^{2} - z(\bar a - k^{2}\bar b) - \bar z(a - k^{2}b) + |a|^{2} - k^{2}|b|^{2} = 0$ — divide by $(1 - k^{2})$ and complete the square: a circle. **Special case $k = 1$: the circle degenerates to the perpendicular bisector** (the $|z|^{2}$ terms cancel). The limit case is not a formality: exam problems love $k = 1$ hidden as "equidistant from".
:::

:::example title="Worked — the disguised circle $|z|^{2} = z + \bar z$"
Write $z = x + iy$: $x^{2} + y^{2} = 2x \Leftrightarrow (x - 1)^{2} + y^{2} = 1$: circle of center $1$, radius $1$, through the origin. Then $\max|z|$ on it $= |1| + 1 = 2$ (farthest point: extend the ray $0 \to$ center by the radius) and $\min|z| = 0$ (the origin is on it).

$(z + 1)(\bar z + 1) = |z|^{2} + z + \bar z + 1$-style expansions are the same move: expand, collect $z + \bar z = 2\operatorname{Re} z$, $z - \bar z = 2i\operatorname{Im} z$, $z \bar z = |z|^{2}$, then complete the square.

**"Purely imaginary" loci:** $\frac{z + 1}{z - 1}$ purely imaginary $\Leftrightarrow$ the fraction plus its conjugate is $0$: numerator $(z + 1)(\bar z - 1) + (\bar z + 1)(z - 1) = 2|z|^{2} - 2 = 0$: the unit circle minus $z = 1$ (undefined there). Geometry confirms: $\arg\frac{z+1}{z-1} = \pm 90^{\circ}$ is Thales' circle on diameter $[-1, 1]$ — the unit circle.
:::

:::diagram
{"type": "graph", "xrange": [-3.2, 3.2], "yrange": [-2.6, 2.8], "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-2, -1, 0, 1, 2], "xlabel": "Re", "ylabel": "Im", "curves": [{"expr": "sqrt(1 - (x-1)*(x-1))", "from": 0, "to": 2, "color": "#0F766E", "label": "|z|² = z + z̄  →  |z-1| = 1", "labpos": 0.12}, {"expr": "-sqrt(1 - (x-1)*(x-1))", "from": 0, "to": 2, "color": "#0F766E"}, {"expr": "sqrt(9 - x*x)", "from": -3, "to": 3, "color": "#B91C1C", "ls": "--", "label": "|z| = 3: min gap at closest point", "labpos": 0.3}, {"expr": "-sqrt(9 - x*x)", "from": -3, "to": 3, "color": "#B91C1C", "ls": "--"}], "points": [{"x": 1, "y": 0, "label": "center 1", "color": "#16295C"}, {"x": 2, "y": 0, "label": "max |z| = 2", "color": "#B8860B", "dy": 0.3}, {"x": 0, "y": 0, "label": "0 (on the circle)", "color": "#B8860B", "dx": -1.5, "dy": -0.65, "ha": "right"}], "title": "Disguised circle |z|² = z + z̄ : center 1, radius 1 — range of |z| on it is [0, 2]", "ratio": 0.66}
:::

## Ranges of |z| over regions

Method: $|z|$ is the distance from $0$; over a closed region the extreme distances are attained on the boundary (draw it, read them off). For open regions the range is open accordingly.

:::example title="Worked — $|z + 2| \leq 3$ and the open-disk variant"
$|z + 2| \leq 3$: closed disk center $-2$, radius $3$. It contains $0$ ($|0 + 2| = 2 \leq 3$): $\min|z| = 0$; farthest point from $0$ is $-2 - 3 = -5$: $\max|z| = 5$. Range $[0, 5]$. (Triangle-inequality check: $|z| \leq |z + 2| + 2 \leq 5$, equality at $z = -5$ ✓.)

$\operatorname{Re} z > 0$ and $|z - 1| < 1$: the open disk touches $0$ (its leftmost point) and lies in $\operatorname{Re} z \geq 0$; the constraint removes just $0$. Distances from $0$ inside: $(0, 2)$ — open at both ends (the disk is open; its rightmost point $2$ is excluded). Range $(0, 2)$.
:::

:::app title="Protocol for every locus problem"
1. Translate the condition into $|z - a|$-language (expand $z \bar z$, $z + \bar z$).
2. Identify the curve (circle / bisector / ellipse / line) **and its degenerate cases** ($k = 1$; ellipse constant $\leq$ focal distance).
3. Fix endpoints/exclusions (fractions: exclude poles; arcs: exclude endpoints).
4. If a max/min is asked: draw the region, mark $0$ (or the target point), read nearest/farthest boundary points — then confirm with the triangle inequality and its equality condition.
:::

:::warn title="Common traps — modulus loci"
- Center: $|z - a| = r$ has center at $a$; $|z + a| = r$ at $-a$.
- Degenerate cases first: $|z - 1| + |z + 1| = 2$ is the **segment** $[-1, 1]$, not an ellipse; $= 1$ is the empty set; $|z - a| = |z - b|$ is a line, not a circle.
- Open vs closed: $|z| < 1$ excludes the boundary — range answers must respect it ($(0, 2)$, not $[0, 2]$).
- In "purely imaginary" fraction problems, always exclude the pole ($z = 1$ above) — substituting it back gives $\frac{2}{0}$.
- $\max|z|$ on a circle is center-distance $+$ radius; $\min|z|$ is $|$center-distance $-$ radius$|$ — not the radius alone.
:::
