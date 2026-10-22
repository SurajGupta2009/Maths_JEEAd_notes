---
id: olympiad-03
part: olympiad
title: "Extension — Vieta Jumping: Descent Built on the Quadratic Formula (IMO 1988/6)"
---

:::assume title="STATUS — olympiad/specialised extension (IMO-level)"
Vieta jumping is a number-theoretic descent technique, far beyond the JEE syllabus. It is included because its engine is exactly Part I material: Vieta's relations plus root-flipping.
:::

:::key title="The move, isolated"
Given a symmetric condition on positive integers $(a, b)$ with a fixed integer quotient $k$: read the condition as a **quadratic in one variable**. One root is $a$; Vieta hands you the other root $a' = (\text{sum of roots}) - a = \frac{\text{product}}{a}$, automatically an integer with the same $k$. If $0 \leq a' < b \leq a$, the pair $(b, a')$ is a *smaller* solution with the same $k$ — descend until forced to stop; the terminal configuration reveals what $k$ must be.
:::

:::derive title="IMO 1988 Problem 6 — the famous application"
Claim: if $a, b$ are positive integers with $ab + 1 \mid a^{2} + b^{2}$, then $k = \frac{a^{2} + b^{2}}{ab + 1}$ is a perfect square. Fix such a $k$ and view $a^{2} - kba + (b^{2} - k) = 0$ as a quadratic in $a$. The other root is $a' = kb - a = \frac{b^{2} - k}{a}$: an integer since $a \mid b^{2} - k$ (rearrange the equation: $b^{2} - k = a(kb - a)$). Ordering $A \geq B$, one checks $0 \leq a' < B$, so descent strictly shrinks the pair while $k$ never changes. It can only halt at $a' = 0$, where the equation gives $k = B^{2}$ — a perfect square, and the same $k$ as the original pair. ∎
:::

:::example title="Worked — tracing the descent"
$(a, b) = (8, 30)$: $k = \frac{64 + 900}{241} = 4$. Order $A = 30 \geq B = 8$: other root $a' = 4 \cdot 8 - 30 = 2$, pair $(8, 2)$ (check $\frac{64 + 4}{17} = 4$ ✓). Reorder $A = 8, B = 2$: $a' = 4 \cdot 2 - 8 = 0$; halt with $k = 2^{2} = 4$ ✓. Brute force over $1 \leq a, b < 300$: every admissible quotient is a perfect square ($1, 4, 9, 16, 25, 36, \ldots$) — no exceptions.
:::

:::app title="The k = 9 chain (building solutions up)"
Descent runs from any solution down to $(0, 3)$ for $k = 9$; reversing ($ (a, b) \mapsto (b, kb - a)$) builds all solutions upward: $(0, 3) \to (3, 27) \to (27, 240) \to (240, 2133) \to \cdots$ Checks: $\frac{9 + 729}{82} = 9$ ✓; $\frac{729 + 57600}{6481} = 9$ ✓. So with $a, b \leq 500$: $(3, 27), (27, 3), (27, 240), (240, 27)$.
:::

:::warn title="Common traps — Vieta jumping"
- Forgetting $k$ is *invariant* under the flip — that invariance is the entire proof.
- Assuming $a'$ is a non-negative integer without proof: integrality comes from Vieta (product/sum of roots), non-negativity from $a' = \frac{B^{2} - k}{A}$ plus the ordering argument; both need care in a written solution.
- Descending without a well-ordering: the descent terminates because positive integers cannot decrease forever — state it.
:::
