---
id: jee-01
part: jee
title: "Complex Numbers — Arithmetic, Conjugate, Modulus, the Two Languages"
---

## Why i exists, and what it forces

The quadratic $x^{2} + x + 1 = 0$ has discriminant $-3$: the reals are not enough. Adjoin one symbol $i$ with the single property $i^{2} = -1$; a **complex number** is $z = a + bi$ with $a, b \in \mathbb{R}$. Here $a = \operatorname{Re} z$ and $b = \operatorname{Im} z$ — the imaginary part is $b$, **not** $bi$.

:::derive title="The product rule is forced, not chosen"
Expand with distributivity and reduce $i^{2} = -1$:

$$(a + bi)(c + di) = ac + adi + bci + bdi^{2}$$

$$(ac - bd) + (ad + bc)i.$$

No convention to memorise: every rule of the subject is "expand, then replace $i^{2}$ by $-1$". Equality is componentwise: $a + bi = c + di \Leftrightarrow a = c$ and $b = d$; a complex number is zero iff both parts are.
:::

:::key title="The conjugate, the division trick, and why $\mathbb{C}$ is a field"
$\bar z = a - bi$. Then $z + \bar z = 2\operatorname{Re} z$, $z - \bar z = 2i\operatorname{Im} z$, $z\bar z = a^{2} + b^{2} = |z|^{2} \geq 0$, $= 0$ iff $z = 0$.

**Division:** for $w \neq 0$, multiply by $\bar w/\bar w$: $\frac{z}{w} = \frac{z \bar w}{|w|^{2}}$; in particular $\frac{1}{a + bi} = \frac{a - bi}{a^{2} + b^{2}}$. The conjugate exists to *kill the imaginary denominator*.

**No zero divisors:** if $w \neq 0$ and $zw = 0$, multiply by $\bar w$: $z|w|^{2} = 0 \Rightarrow z = 0$. Hence $\mathbb{C}$ is a field — factoring, Vieta, the quadratic formula all run unchanged. (And every complex number has a square root — sheet 04 — so *every* quadratic splits.)
:::

:::example title="Worked arithmetic — where the sign flips"
$(3 + 2i)(5 - i) = 15 - 3i + 10i - 2i^{2} = 17 + 7i$ — the step $-2i^{2} = +2$ is the single most common slip.

$\frac{1 + 2i}{3 - i} = \frac{(1 + 2i)(3 + i)}{(3 - i)(3 + i)} = \frac{3 + i + 6i + 2i^{2}}{9 + 1} = \frac{1 + 7i}{10}$.

$\left(\frac{1 + i}{1 - i}\right)^{3}$: first $\frac{1 + i}{1 - i} = \frac{(1 + i)^{2}}{(1 - i)(1 + i)} = \frac{2i}{2} = i$; then $i^{3} = -i$. **Reduce the base before the exponent.**

Cycle of $i$: $i^{n} = i^{r}$ with $r \in \{0,1,2,3\}$ the remainder of $n$ on division by 4 — $(1 + i)^{40} = ((1 + i)^{2})^{20} = (2i)^{20} = 2^{20}i^{20} = 2^{20}$.
:::

## The plane: complex numbers are vectors

Plot $z = a + bi$ as $(a, b)$. Addition is **vector addition**; the modulus $|z| = \sqrt{a^{2} + b^{2}}$ is the distance from the origin; $|z - w|$ is the distance between points; $\frac{z_{1} + z_{2}}{2}$ is the midpoint.

:::diagram
{"type": "graph", "xrange": [-5.2, 5.2], "yrange": [-3.6, 4.4], "xticks": [-4, -2, 0, 2, 4], "yticks": [-2, 0, 2, 4], "xlabel": "Re", "ylabel": "Im", "curves": [{"expr": "sqrt(16 - x*x)", "from": -4, "to": 4, "color": "#C8D4E6", "ls": "--", "label": "|z| = 4", "labpos": 0.06}, {"expr": "-sqrt(16 - x*x)", "from": -4, "to": 4, "color": "#C8D4E6", "ls": "--"}], "rays": [{"x": [0, 3], "y": [0, 4], "label": "z = 3+4i, |z| = 5", "color": "#16295C"}, {"x": [0, 1], "y": [0, -2], "label": "w = 1-2i, |w| = √5", "color": "#B8860B"}, {"x": [1, 3], "y": [-2, 4], "label": "z - w = 2+6i", "color": "#B91C1C"}], "points": [{"x": 3, "y": 4, "label": "z", "color": "#16295C"}, {"x": 3, "y": -4, "label": "z̄ (reflection in real axis)", "color": "#16295C", "dy": -0.75}, {"x": 1, "y": -2, "label": "w", "color": "#B8860B"}, {"x": 4, "y": 2, "label": "z+w = 4+2i", "color": "#0F766E"}], "title": "The Argand plane: |z| is a distance, z - w is the vector w → z, z̄ is the mirror", "ratio": 0.72}
:::

:::key title="Triangle and reverse triangle inequalities — with equality conditions"
$$|z + w| \leq |z| + |w|, \qquad \left||z| - |w|\right| \leq |z - w|$$

Geometric proof: the points $0, z, z+w$ form a (possibly degenerate) triangle; a side never exceeds the sum of the other two. **Equality** in the first iff $z, w$ point the same way (one is a non-negative real multiple of the other) or one is $0$; in the second, iff they point opposite ways. These equality conditions are the engine of every minimisation in sheet 10.
:::

:::key title="Parallelogram law (the hidden JEE workhorse)"
$$|z + w|^{2} + |z - w|^{2} = 2|z|^{2} + 2|w|^{2}$$

Proof: $|z \pm w|^{2} = (z \pm w)(\bar z \pm \bar w) = |z|^{2} + |w|^{2} \pm (z \bar w + \bar z w)$; add and the cross terms cancel. Geometry: sum of squared diagonals = sum of squared sides. Recognise it inside "minimise $|z|^{2} + |z - 2|^{2}$"-style targets and stop computing.
:::

:::warn title="Common traps — foundations"
- $-2i^{2} = +2$. Re-derive any forgotten rule by expanding and reducing $i^{2} = -1$.
- $\operatorname{Im}(3 + 4i) = 4$, not $4i$.
- $\frac{z_{1}}{z_{2}} = 1$ means $z_{1} = z_{2}$; $\left|\frac{z_{1}}{z_{2}}\right| = 1$ means only *equal moduli*.
- $|z - a| = r$ has center at $a$ — the minus points **to** the center.
- $\overline{z_{1} z_{2}} = \bar z_{1} \bar z_{2}$, $\overline{z_{1} + z_{2}} = \bar z_{1} + \bar z_{2}$, $\bar{\bar z} = z$ — you may conjugate whole equations (used in sheet 07).
- $|z|^{2} = z \bar z \neq z^{2}$ unless $z$ is real.
:::
