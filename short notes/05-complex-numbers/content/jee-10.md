---
id: jee-10
part: jee
title: "Optimization — Triangle Inequality with Equality Conditions, Chords, Regions"
---

## The three results, in increasing power

:::key title="(A) Triangle inequality with equality condition"
$$|z - a| \geq \left||z| - |a|\right|, \qquad |z - a| \leq |z| + |a|$$

Equality on the left iff $z, a$ point the **same direction** (one is a non-negative real multiple of the other); on the right iff **opposite directions**. For constrained $z$ this gives min/max in one line.
:::

:::key title="(B) Extremes of $|z - a|$ on the unit circle (and any circle)"
If $|z| = r$ and $a \neq 0$:

$$\min |z - a| = \left||a| - r\right|\quad\text{ at } z = r\frac{a}{|a|}$$

$$\max |z - a| = |a| + r\quad\text{ at } z = -r\frac{a}{|a|}$$

Geometric reading: nearest/farthest points of a circle to an exterior point lie on the line through the center and the point. For a circle $|z - z_{0}| = r$: replace $|z|$-distance by $|$distance from $z_{0}|$ — same formulas with $a \mapsto a - z_{0}$.
:::

:::key title="(C) Chord distance between unit points"
If $|z| = |w| = 1$:

$$|z - w|^{2} = (z - w)(\bar z - \bar w) = 2 - z\bar w - \bar z w$$

$$2 - 2\operatorname{Re}(z \bar w)$$

so $|z - w| = 2\left|\sin\frac{\varphi}{2}\right|$ where $\varphi = \arg(w/z)$ is the angle between them. In particular $|z - w| = \sqrt{2}$ iff $z \bar w = \pm i$ (quarter-turn apart); $|z - w| = 1$ iff $60^{\circ}$ apart ($z \bar w = e^{\pm i\pi/3}$).
:::

:::diagram
{"type": "graph", "xrange": [-2.2, 3.4], "yrange": [-3.2, 1.8], "xticks": [-2, -1, 0, 1, 2, 3], "yticks": [-3, -2, -1, 0, 1], "xlabel": "Re", "ylabel": "Im", "curves": [{"expr": "sqrt(1 - x*x)", "from": -1, "to": 1, "color": "#0F766E", "label": "|z| = 1", "labpos": 0.12}, {"expr": "-sqrt(1 - x*x)", "from": -1, "to": 1, "color": "#0F766E"}], "rays": [{"x": [0, 1], "y": [0, -2], "label": "a = 1-2i, |a| = √5", "color": "#B8860B"}, {"x": [0.4472, 1], "y": [-0.8944, -2], "label": "gap = √5 - 1", "color": "#B91C1C"}], "points": [{"x": 0.4472, "y": -0.8944, "label": "z = a/|a| (nearest)", "color": "#16295C", "dy": -0.55}, {"x": 1, "y": -2, "label": "a", "color": "#B8860B"}], "title": "min |z - a| on |z| = 1 : attained where the ray 0 → a exits the circle — gap √5 - 1", "ratio": 0.72}
:::

:::example title="Worked — the standard three questions"
1. $|z| = 1$: $\min |z - (3 + 4i)| = 5 - 1 = 4$ at $z = \frac{3 + 4i}{5}$; $\max = 6$ at $z = -\frac{3 + 4i}{5}$.
2. $|z| = 1$: range of $\left|z + \frac{1}{z} + 2i\right|$: on the circle $\frac{1}{z} = \bar z$, so $z + \frac{1}{z} = 2\cos\theta$ (real) and the expression $= 2\cos\theta + 2i$: modulus $2\sqrt{\cos^{2}\theta + 1} \in [2, 2\sqrt{2}]$. Min at $z = \pm i$, max at $z = \pm 1$.
3. $|z| = |w| = 1$, $z \bar w = i$: $|z - w|^{2} = 2 - 2\operatorname{Re}(i) = 2$: $|z - w| = \sqrt{2}$ ✓ (quarter-turn chord).
:::

:::derive title="Parallelogram-type minimisations — $|z - a|^{2} + |z - b|^{2}$"
Expand $|z - a|^{2} + |z - b|^{2} = 2|z - m|^{2} + \frac{1}{2}|a - b|^{2}$ with $m = \frac{a + b}{2}$ (complete the square in $z$; or read Leibniz's centroid identity of the olympiad sheets with $n = 2$). So the unconstrained min is at the midpoint; under a constraint like $|z| = 1$ the problem becomes "min $|z - m|$" = case (B) applied to $m$. Every "$\min(|z - a|^{2} + |z - b|^{2})$ subject to..." question is this two-step.
:::

:::app title="Region questions — draw, then read distances"
Range of $|z|$ (or $|z - a|$) for $z$ in a region: nearest/farthest points are on the boundary — circle arcs give center $\pm$ radius; half-plane constraints clip candidates; **vertices and tangency points win**. Always: (i) draw to scale, (ii) list candidate points (nearest/farthest on each boundary piece), (iii) evaluate, (iv) state open/closed as given. For *complex* objectives like $|z + \frac{1}{z}|$ substitute $z = e^{i\theta}$ first (unit circle only!) and reduce to a real-variable range.
:::

:::warn title="Common traps — optimisation"
- Equality conditions, not just the inequality: $\min |z - a|$ on $|z| = r$ is $||a| - r|$ **attained at** $z = r\,a/|a|$ — forgetting the attaining $z$ loses half the marks.
- $\min |z - a| + |z - b|$ unconstrained is $|a - b|$ (segment), not via circles; with $|z| = r$ it becomes an ellipse problem — check degeneracy first.
- $|z + \frac{1}{z}|$ simplifies only on $|z| = 1$ (where $\frac{1}{z} = \bar z$); off the circle it is not $2|\cos\theta|$.
- Chord formula $|z - w| = 2|\sin\frac{\varphi}{2}|$ needs **both** on the unit circle; for general radii use $|z - w|$ directly or scale first.
- Region ranges respect openness: open disk + strict inequalities $\Rightarrow$ open range endpoints.
:::
