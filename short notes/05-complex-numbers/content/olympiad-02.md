---
id: oly-02
part: olympiad
title: "Extension — Ptolemy from One Identity; Distance Theorems by Expansion"
---

:::assume title="STATUS — olympiad extension (classical geometry ↔ algebra)"
Ptolemy's theorem/inequality and distance theorems (British Flag and friends) are proved here as pure algebra in $\mathbb{C}$. The identity behind Ptolemy is a 30-second expansion usable in any exam; the equality-condition analysis is olympiad-grade. The JEE-visible content: the identity, the inequality, and the distance expansions — all derivable from Part I.
:::

## The Ptolemy identity — no geometry anywhere

:::key title="Identity (valid for ALL four complex numbers $a, b, c, d$)"
$$(a - c)(b - d) = (a - b)(c - d) + (b - c)(a - d)$$

Verify yourself: RHS $= (ac - ad - bc + bd) + (ab - bd - ca + cd) = ab - ad - bc + cd = (a - c)(b - d)$ ✓. (Expansion only — no circle, no ordering, nothing.)
:::

:::derive title="Ptolemy's inequality and theorem — one modulus step each"
Take moduli and use the triangle inequality:

$$|a - c|\,|b - d|$$

$$|(a - b)(c - d) + (b - c)(a - d)|$$

$$\leq |a - b|\,|c - d| + |b - c|\,|a - d|$$

— the product of the diagonals is at most the sum of products of opposite sides, for **any** four points. Equality holds iff $(a - b)(c - d)$ and $(b - c)(a - d)$ point the same direction, i.e. $\frac{(b - c)(a - d)}{(a - b)(c - d)} \in \mathbb{R}_{>0}$; taking arguments this says the angles the chord $bd$ subtends at $a$ and at $c$ are **supplementary** — the points are concyclic in the order $a, b, c, d$ (inscribed-angle theorem, oly-01's collinearity language). That is Ptolemy's *theorem*: for a cyclic quadrilateral, equality — the diagonal-product formula from school geometry. ∎

**Unit-square check** ($a = 1, b = i, c = -1, d = -i$): diagonals $2 \times 2 = 4$; sides $\sqrt{2}$: $\sqrt{2}\cdot\sqrt{2} + \sqrt{2}\cdot\sqrt{2} = 4$ ✓.
:::

:::app title="How to use Ptolemy in an olympiad"
1. Encode the four points; write the identity (or just take the cyclic special case if cyclicity is given).
2. For length-product equalities/inequalities ($PA \cdot QC + \ldots$), match to the four factors.
3. Collinearity-ish corollaries: if one "vertex" collapses onto a side, Ptolemy degenerates to the triangle inequality $|a - b| \leq |a - c| + |c - b|$ — recognise the degeneration instead of re-deriving.
4. The converse direction (equality $\Rightarrow$ cyclic) is available when a problem says "prove $ABCD$ cyclic" via lengths.
:::

## Distance theorems as expansions — the British Flag

:::key title="British Flag theorem (rectangle form)"
For a rectangle $A, B, C, D$ (diagonal pairs $A, C$ and $B, D$) and **any** point $e$ in the plane:

$$|e - A|^{2} + |e - C|^{2} = |e - B|^{2} + |e - D|^{2}$$
:::

:::derive title="Proof — expand $|z - a|^{2} = |z|^{2} - z \bar a - \bar z a + |a|^{2}$ and collect"
Take the square with vertices $0, 1, 1 + i, i$; the statement is $|e|^{2} + |e - (1 + i)|^{2} = |e - 1|^{2} + |e - i|^{2}$. Expand each:

$$|e - (1 + i)|^{2} = |e|^{2} - e(1 - i) - \bar e(1 + i) + 2,$$

$$|e - 1|^{2} = |e|^{2} - e - \bar e + 1,$$

$$|e - i|^{2} = |e|^{2} + ie - i\bar e + 1$$

LHS $= 2|e|^{2} - e + ie - \bar e - i\bar e + 2$; RHS $= 2|e|^{2} - e + ie - \bar e - i\bar e + 2$ — identical term for term. ∎ (For a general rectangle with vertices $0, w, w + v, v$ the same expansion cancels because the vertex constants pair up: $0 + (w + v) = w + v$.)

The pattern worth internalising: **$|z - a|^{2}$ is a quadratic in $z, \bar z$ with clean coefficients** — every rectangle/square distance theorem is "expand and collect".
:::

:::example title="Worked — the same expansion proves the parallelogram law and the Leibniz $n = 2$ case"
$|z + w|^{2} + |z - w|^{2}$: expand $= (|z|^{2} + |w|^{2} + z \bar w + \bar z w) + (|z|^{2} + |w|^{2} - z \bar w - \bar z w) = 2|z|^{2} + 2|w|^{2}$ ✓ (sheet 01). And $|z - a|^{2} + |z - b|^{2} = 2|z - m|^{2} + \frac{1}{2}|a - b|^{2}$ with $m = \frac{a + b}{2}$: expand both sides, compare (or complete the square). Three "theorems", one algebraic habit.
:::

:::warn title="Traps — Ptolemy and expansions"
- The identity is unconditional; the **theorem** (equality) needs cyclic order — never claim $|a - c||b - d| = \ldots$ for a generic quadrilateral.
- Ptolemy's factors pair as (diagonal, diagonal) vs (opposite side, opposite side) — the ordering $a, b, c, d$ around the circle is part of the statement.
- British Flag is for **rectangles** (points in the plane, any point $e$ — inside or outside); for general quadrilaterals it fails.
- When expanding $|z - a|^{2}$, note $\overline{(z - a)} = \bar z - \bar a$ — conjugating the constant correctly is the usual slip.
- Degenerate Ptolemy (a point on a side) gives the triangle inequality — good consistency check, not a new theorem.
:::
