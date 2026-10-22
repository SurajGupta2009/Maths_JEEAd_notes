---
id: oly-06
part: olympiad
title: "Extension — Gauss–Lucas, Marden, Pompeiu: Structure Theorems"
---

:::assume title="STATUS — olympiad/specialised extension (deeper theory; IOQM/RMO+)"
Three structure theorems about polynomials and equilateral triangles. **Gauss–Lucas** (critical points stay in the convex hull of the roots) is the complex substitute for Rolle's theorem; **Marden** pinpoints the critical points of a cubic as ellipse foci; **Pompeiu** says $PA, PB, PC$ from an equilateral triangle always form a triangle. Each proof here is a few lines of Part I algebra; the theorems themselves are beyond the core JEE syllabus sentence and are labelled accordingly. No claim that any of this "can never appear" in JEE Advanced — the *computational* corollaries (critical points of a cubic; distance-triangle inequalities) are ordinary Part I manipulations.
:::

## Gauss–Lucas — critical points cannot leave the hull

:::key title="Theorem"
Let $p(z) = c\prod_{k=1}^{n}(z - r_{k})$. Then every zero of $p'(z)$ lies in the **convex hull** of $\{r_{1}, \dots, r_{n}\}$.
:::

:::derive title="Proof — the logarithmic derivative is a sum of point charges"
Logarithmic differentiation: $\frac{p'(z)}{p(z)} = \sum_{k=1}^{n} \frac{1}{z - r_{k}}$. If $z$ lies *outside* the hull, a line separates it from all roots: for some real $\theta$, $\operatorname{Re}\left(e^{-i\theta}(z - r_{k})\right) > 0$ for all $k$. Then

$$\operatorname{Re}\left(e^{i\theta}\frac{p'(z)}{p(z)}\right)$$

$$ = \sum_{k=1}^{n} \frac{\operatorname{Re}\left(e^{-i\theta}(z - r_{k})\right)}{|z - r_{k}|^{2}} > 0$$

so $p'(z)/p(z) \neq 0$, hence $p'(z) \neq 0$ — contradiction. ∎

Corollary (Rolle in complex form): all roots real $\Rightarrow$ hull is a segment of the real line $\Rightarrow$ every critical point is real — no intermediate-value argument anywhere.
:::

:::example title="Worked — critical points of $p(z) = z(z - 2)(z - 1 - 2i)$"
Expand: $p(z) = z^{3} + (-3 - 2i)z^{2} + (2 + 4i)z$; $p'(z) = 3z^{2} + (-6 - 4i)z + (2 + 4i)$. Discriminant: $b^{2} - 4ac = (20 + 48i) - (24 + 48i) = -4$, so $\sqrt{\text{disc}} = \pm 2i$:

$$z = \frac{6 + 4i \pm 2i}{6} \in \left\{1 + i, \ 1 + \frac{i}{3}\right\}.$$

Both lie inside the triangle $(0, 2, 1 + 2i)$ (half-plane check: $y \geq 0$, $y \leq 2x$, $y \leq 4 - 2x$ ✓), exactly as Gauss–Lucas demands. Shifting the centroid $1 + \frac{2}{3}i$ to $0$ sends the two points to $\pm \frac{i}{3}$ — symmetric about the centroid, which is Marden's signature.
:::

:::app title="Marden's theorem (quote-level)"
For a cubic whose roots are the vertices of a triangle, the two roots of $p'$ are the **foci of the Steiner inellipse** (the ellipse tangent to the three sides at their midpoints). Gauss–Lucas puts them inside the triangle; Marden identifies them exactly. Test with distances: each side midpoint $m_{k}$ satisfies $|m_{k} - f_{1}| + |m_{k} - f_{2}| = $ the same constant. For an equilateral triangle the foci coincide at the center and $p'$ has a double root there.
:::

## Pompeiu — three distances that always make a triangle

:::key title="Theorem"
$ABC$ equilateral, $P$ any point of the plane: $PA, PB, PC$ are the side lengths of a (possibly degenerate) triangle; degenerate **exactly** when $P$ lies on the circumcircle of $ABC$.
:::

:::derive title="Proof — the equilateral condition cancels $P$"
Take $\omega = e^{2\pi i/3}$ with $A + \omega B + \omega^{2} C = 0$ (CCW, oly-01). Put $u = P - A$, $v = P - B$, $w = P - C$; then

$$u + \omega v + \omega^{2} w = P(1 + \omega + \omega^{2}) - (A + \omega B + \omega^{2} C)$$

$$0$$

Rotate this one identity to read all three triangle inequalities: as it stands, $u = -\omega v - \omega^{2} w \Rightarrow |u| \leq |v| + |w|$; multiplied by $\omega^{2}$: $|v| \leq |u| + |w|$; by $\omega$: $|w| \leq |u| + |v|$. So $PA, PB, PC$ form a triangle. Equality in $|u| \leq |v| + |w|$ needs $\omega v, \omega^{2} w$ parallel with the same sign — precisely $P$ on the arc $BC$ of the circumcircle; by symmetry, on the whole circle. ∎

Concrete: equilateral $1, \omega, \omega^{2}$ (circumcircle $= |z| = 1$): every $P = e^{i\theta}$ makes $PA + PB = PC$ for the largest distance (degenerate), while $|P| = 2$ gives a genuine triangle (e.g. at $\theta = \frac{\pi}{3}$: $1.414 + 2.504 > 3.120$ ✓).
:::

:::app title="Why these theorems are the same trick"
Gauss–Lucas: expand $\frac{p'}{p}$ and take real parts. Pompeiu: expand the $\omega$-relation and take moduli. Ptolemy (oly-02): expand an identity and take moduli. **Expand, then extract a geometric statement from an algebraic equality/inequality** — the complex-bash method in three costumes. When an olympiad problem smells like "points, distances, and a hidden regular polygon", this is the family to try first.
:::

:::warn title="Traps — structure theorems"
- Gauss–Lucas bounds by the convex **hull**, not the circumcircle ("zeros of $p'$ lie in the circle through the roots" is a weaker, half-remembered statement that is sometimes false).
- The hull can be a segment (collinear roots) or the full triangle; boundary cases (critical point *on* the hull edge) are allowed by the theorem.
- Pompeiu degeneracy is *exactly* on the circumcircle — inside the triangle the distance-triangle is strictly non-degenerate (so "$PA, PB, PC$ can never form a triangle" is wrong for interior points).
- Pompeiu needs **equilateral**; for general triangles the three distances need not satisfy any clean inequality beyond the obvious pairwise ones.
- The orientation in $A + \omega B + \omega^{2} C = 0$ is CCW; swapping $B, C$ swaps $\omega \leftrightarrow \omega^{2}$ and the Pompeiu rotation bookkeeping follows suit.
:::
