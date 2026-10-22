---
id: oly-01
part: olympiad
title: "Extension — The Rotation Engine: Equilateral Condition, Tests, Area, Circumcenter"
---

:::assume title="STATUS — olympiad/geometry-via-complex extension (IOQM/RMO core weapon)"
Encoding a figure's vertices as complex numbers and proving theorems by algebra is standard olympiad technique (and an occasional JEE Advanced strand). Everything here is derived from Part I (rotation $= \times e^{i\theta}$, $\omega$-identities). The equilateral condition appears in JEE-Advanced-flavoured problems regularly; Ptolemy/Napoleon/van Aubel (next sheets) are classical olympiad theorems. No claim that these "can never appear" in JEE — they are simply at the harder, technique-heavy end.
:::

## The engine: rotation is multiplication

:::key title="Rotation by $\theta$ about $A$"
$$X' = A + e^{i\theta}(X - A)$$

One line: $X - A$ is the vector $A \to X$; multiplying by $e^{i\theta}$ keeps its length and adds $\theta$ to its direction; adding $A$ re-anchors. Quarter turns: $\times i$; half turn: $\times(-1)$; $60^{\circ}$: $\times e^{i\pi/3} = \times(1 + \omega)$ (identity 4 of sheet 05) — and $e^{-i\pi/3} = -\omega = \overline{1 + \omega}$.
:::

:::key title="Equilateral-triangle condition (orientation-sensitive)"
$(a, b, c)$ is equilateral **counterclockwise** $\Leftrightarrow$

$$a + \omega b + \omega^{2} c = 0$$

(clockwise ordering gives $a + \omega^{2} b + \omega c = 0$). Both directions are one-line proofs below; the condition is the single most-used complex-geometry fact in olympiads.
:::

:::derive title="Proof both directions"
($\Rightarrow$) CCW equilateral: $c - a = e^{i\pi/3}(b - a) = (1 + \omega)(b - a)$ (rotate side $ab$ by $+60^{\circ}$). Solve: $c = -\omega a + (1 + \omega)b$. Substitute: $a + \omega b + \omega^{2}c = a + \omega b - \omega^{3} a + (\omega^{2} + \omega^{3})b = a + \omega b - a - \omega b = 0$ using $\omega^{3} = 1$, $\omega^{2} + 1 = -\omega$. ∎

($\Leftarrow$) From $a + \omega b + \omega^{2}c = 0$: $c = -\omega a - \omega^{2} b$ (using $\omega^{-2} = \omega$), so $c - a = -(1 + \omega)a - \omega^{2}b = (1 + \omega)(b - a)$ (expand and use $1 + \omega + \omega^{2} = 0$). Hence $|c - a| = |b - a|$ with a $60^{\circ}$ turn: equilateral, CCW. ∎

Check on $a = 0$, $b = 1$, $c = e^{i\pi/3}$: $\omega + \omega^{2}(1 + \omega) = \omega + \omega^{2} + \omega^{3} = 0$ ✓.
:::

:::app title="Standard tests (translation dictionary)"
Collinear $z_{1}, z_{2}, z_{3}$: $\frac{z_{1} - z_{2}}{z_{1} - z_{3}} \in \mathbb{R}$ (the ratio of two side-vectors is real). Perpendicular at $z_{1}$: that ratio is purely imaginary ($\in i\mathbb{R}$). Equal lengths: $|z_{1} - z_{2}| = |z_{3} - z_{4}|$. Section formula: point dividing $z_{1}z_{2}$ in ratio $m : n$ is $\frac{n z_{1} + m z_{2}}{m + n}$. Angle $\theta$ at $z$ between $a, b$: $\arg\frac{b - z}{a - z} = \pm\theta$ — the sheet-09 arc language. Concyclic: cross-ratio $\frac{(z_{1} - z_{3})(z_{2} - z_{4})}{(z_{1} - z_{4})(z_{2} - z_{3})} \in \mathbb{R}$ (olympiad-level; use only when needed).
:::

:::key title="Area and circumcenter — two more one-liners"
$$\text{Area}(\triangle z_{1}z_{2}z_{3})$$

$$ = \frac{1}{2}\left|\operatorname{Im}\left((z_{2} - z_{1})\overline{(z_{3} - z_{1})}\right)\right|$$

Reason: $(z_{2} - z_{1})\overline{(z_{3} - z_{1})}$ is the cross product of the two sides in complex clothing — modulus $|$product of lengths$|$, argument $=$ signed angle between them; its imaginary part is the signed twice-area. Shoelace is this formula in coordinates.

**Cumcenter $u$**: solve $|u - a|^{2} = |u - b|^{2} = |u - c|^{2}$: expanding, $u(\bar b - \bar a) + \bar u(b - a) = |b|^{2} - |a|^{2}$ — one linear equation in $u, \bar u$ per pair; two of them, $2 \times 2$ solve. No perpendicular bisectors drawn.
:::

:::example title="Worked — area of $\triangle(1, 3i, -2 + 2i)$; circumcenter of $(1, i, -1)$"
$z_{2} - z_{1} = -1 + 3i$, $z_{3} - z_{1} = -3 + 2i$: $(z_{2} - z_{1})\overline{(z_{3} - z_{1})} = (-1 + 3i)(-3 - 2i) = 3 + 2i - 9i + 6 = 9 - 7i$. Area $= \frac{1}{2}|{-7}| = \frac{7}{2}$. (Shoelace check: $\frac{1}{2}|1 \cdot (3 - 2) + 0 + (-2)(0 - 3)| = \frac{1}{2} \cdot 7$ ✓.)

Circumcenter of $1, i, -1$: all on $|z| = 1$, so $u = 0$ (uniqueness of the circumcenter of a non-degenerate triangle). The linear solve confirms: $u(-i - 1) + \bar u(i - 1) = |i|^{2} - |1|^{2} = 0$, satisfied by $u = 0$ ✓.
:::

:::warn title="Traps — rotation toolkit"
- Orientation: $a + \omega b + \omega^{2}c = 0$ is **CCW-only**; a problem's clockwise labelling needs $\omega \leftrightarrow \omega^{2}$. If ordering is unstated, check both or phrase conclusions orientation-free.
- $\frac{z_{1} - z_{2}}{z_{1} - z_{3}} \in \mathbb{R}$ excludes $z_{1} = z_{3}$ (division) — degenerate configurations need separate handling.
- Area formula has a $\frac{1}{2}$ and an absolute value; the *signed* imaginary part tracks orientation.
- Circumcenter $2 \times 2$ solve fails when $a = b$ (degenerate); assume distinct vertices.
- $e^{i\pi/3} = 1 + \omega$ and $e^{-i\pi/3} = -\omega$ — mixing these up reverses every rotation in sight.
:::
