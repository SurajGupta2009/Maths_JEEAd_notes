---
id: jee-04
part: jee
title: "Location of Roots — Pinning Roots into Intervals Without Solving"
---

## The three ingredients

Let $f(x) = ax^{2} + bx + c$, $a \neq 0$, roots $\alpha \leq \beta$ real. Every location condition is assembled from three ingredients only:

:::key title="The location toolkit"
1. **Reality:** $D \geq 0$.
2. **Vertex position:** $x_{v} = -\frac{b}{2a}$ relative to the interval (the axis must sit where the roots are claimed to be).
3. **Endpoint sign:** $a \cdot f(k)$ at endpoints. The product $a f(k) > 0$ means $k$ lies *outside* $[\alpha, \beta]$ (same sign region as far away); $a f(k) < 0$ means $k$ lies *strictly between* the roots; $f(k) = 0$ means $k$ **is** a root.

Multiply by $a$ to kill case-splitting on the sign of $a$: always work with $a f(k)$.
:::

:::key title="The standard configurations (learn as pictures, not formulas)"
- **Both roots $> k$:** $D \geq 0$, $a f(k) > 0$, $x_{v} > k$.
- **Both roots $< k$:** $D \geq 0$, $a f(k) > 0$, $x_{v} < k$.
- **$k$ between the roots** ($\alpha < k < \beta$): $a f(k) < 0$ alone (this forces $D > 0$ automatically).
- **Both roots in $(k_{1}, k_{2})$:** $D \geq 0$, $a f(k_{1}) > 0$, $a f(k_{2}) > 0$, $k_{1} < x_{v} < k_{2}$.
- **Exactly one root in $(k_{1}, k_{2})$:** $f(k_{1}) f(k_{2}) < 0$ (then $D > 0$ is automatic), plus separately check endpoint roots $f(k_{i}) = 0$.
- **Roots of opposite signs:** $a f(0) = ac < 0$ alone (i.e. $P = \frac{c}{a} < 0$); again $D > 0$ is automatic.
- **Both roots positive:** $D \geq 0$, $S > 0$, $P > 0$. Both negative: $D \geq 0$, $S < 0$, $P > 0$. (This is the $k = 0$ case of the first two bullets — Vieta form.)
:::

:::diagram
{"type": "graph", "xrange": [-0.6, 7.4], "yrange": [-3.4, 6.4], "xticks": [0, 1, 2, 3, 4, 5, 6, 7], "yticks": [-2, 0, 2, 4, 6], "xlabel": "x", "ylabel": "y", "hlines": [{"y": 0, "color": "#94A3B8"}], "vlines": [{"x": 1, "color": "#B91C1C", "ls": "--"}, {"x": 5, "color": "#B91C1C", "ls": "--"}], "curves": [{"expr": "0.55*(x - 2)*(x - 4)", "color": "#16295C", "label": "both roots in (1, 5): f(1)>0, f(5)>0, vertex 3 inside, D>0", "labpos": 0.9}], "points": [{"x": 2, "y": 0, "label": "α=2"}, {"x": 4, "y": 0, "label": "β=4"}, {"x": 1, "y": 1.65, "label": "f(1)>0", "dy": 0.5}, {"x": 5, "y": 1.65, "label": "f(5)>0", "dy": 0.5}], "title": "Root location: endpoint signs + vertex position + D≥0", "ratio": 0.6}
:::

:::example title="Worked — both roots exceed 1"
Both roots of $x^{2} - 2kx + k^{2} - 1 = 0$ exceed 1. $D = 4 > 0$ always; the roots are $k \pm 1$, so the smaller exceeds 1 iff $k - 1 > 1$, i.e. $k > 2$. Toolkit cross-check: $x_{v} = k > 1$ and $a f(1) = k^{2} - 2k = k(k - 2) > 0$ give $k > 2$ or $k < 0$; intersecting with $k > 1$ leaves $k > 2$ ✓. Solving directly was cleaner here only because the roots are explicit — use the toolkit when they are not.
:::

:::example title="Worked — exactly one root in (0, 2)"
$f(x) = x^{2} - 3x + k$ has exactly one root in $(0, 2)$: $f(0)f(2) = k(k - 2) < 0$ gives $0 < k < 2$; endpoints must be checked individually: $k = 0$ gives roots $0, 3$ — none inside, excluded; $k = 2$ gives roots $1, 2$ — the root $1$ **is** inside, so $k = 2$ is included. Answer $0 < k \leq 2$, with the endpoint discussion stated — losing it (in particular, mechanically excluding both endpoints) is the standard half-mark.
:::

:::warn title="Common traps — location"
- Forgetting any one of the three ingredients: $D \geq 0$ and $af(k) > 0$ without the vertex condition also admits both roots on the *other* side of $k$.
- Using $f(k) > 0$ instead of $a f(k) > 0$ when $a$ may be negative or contains a parameter.
- Adding $D > 0$ redundantly (and then mishandling equality) when $af(k) < 0$ already forces distinct real roots.
- Strict vs non-strict: "in $(k_{1}, k_{2})$" excludes endpoint roots; "in $[k_{1}, k_{2}]$" requires checking $f(k_{i}) = 0$ cases separately.
- When the leading coefficient contains the parameter, the degenerate linear case must be tested on its own.
:::

:::assume title="Assumptions behind the toolkit"
Real coefficients and real roots throughout; "root in interval" claims are meaningless for non-real roots. If $a$ depends on the parameter, first confirm the equation stays quadratic on the claimed parameter range.
:::
