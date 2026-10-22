---
id: oly-03
part: olympiad
title: "Extension — Van Aubel and Napoleon: Squares and Equilaterals on the Sides"
---

:::assume title="STATUS — olympiad extension (classical theorems, JEE-adjacent technique)"
Van Aubel (squares on the sides of a quadrilateral) and Napoleon (equilateral triangles on the sides of a triangle) are olympiad staples proved here by the $\omega$-machinery of Part I. The *technique* (center formulas + the equilateral condition) is exactly the JEE-Advanced "geometry via complex numbers" strand; the theorems themselves sit at the IOQM/RMO end. Derivable from Part I + oly-01; nothing assumed beyond them.
:::

## Outward-square centers

:::key title="Center formula (counterclockwise quadrilateral, outward square on side $pq$)"
$$m_{pq} = \frac{p + q}{2} - \frac{i}{2}(q - p) = \frac{(1 + i)p + (1 - i)q}{2}$$

Reason: the center of any square on base $pq$ is the midpoint $\pm$ the half-side rotated by $90^{\circ}$; for a CCW quadrilateral the interior lies to the left of $p \to q$, so the outward direction is $-i(q - p)$'s side. (Check on side $0 \to 1$: center $\frac{1 - i}{2}$ — below the real axis ✓.)
:::

:::derive title="Van Aubel — opposite centers are equal and perpendicular"
For CCW $a, b, c, d$ with outward centers $m_{ab}, m_{bc}, m_{cd}, m_{da}$:

$$2(m_{bc} - m_{da})$$

$$\left((1 + i)b + (1 - i)c\right) - \left((1 + i)d + (1 - i)a\right)$$

$$2(m_{cd} - m_{ab})$$

$$\left((1 + i)c + (1 - i)d\right) - \left((1 + i)a + (1 - i)b\right)$$

Multiply the second by $i$ and collect: $i \cdot 2(m_{cd} - m_{ab}) = -2(m_{bc} - m_{da})$, i.e.

$$m_{bc} - m_{da} = -i\,(m_{cd} - m_{ab}).$$

One equation, two facts: $\times(-i)$ is a $90^{\circ}$ rotation preserving length — the segments are **equal and perpendicular**. ∎ (Numeric check on $0, 1, 1.5 + 1.2i, 0.3 + 0.9i$: both segments $\approx 2.1645$ long, ratio pure imaginary ✓.)
:::

## Napoleon's Theorem — equilaterals erected on the sides

:::key title="Outward-equilateral center (CCW triangle $a, b, c$, third vertex via $-60^{\circ}$ turn)"
Third vertex of the outward equilateral on $a \to b$: $a + e^{-i\pi/3}(b - a) = a - \omega(b - a)$. Its center:

$$m_{ab} = \frac{a + b + (a - \omega(b - a))}{3} = \frac{(2 + \omega)a + (1 - \omega)b}{3}$$

using $e^{-i\pi/3} = -\omega$ and $1 - \omega^{2} = 2 + \omega$.
:::

:::derive title="Napoleon — the centers form an equilateral triangle"
By oly-01's condition, suffices to show $m_{ab} + \omega m_{bc} + \omega^{2}m_{ca} = 0$. Compute $3 \times$ the left side and collect the $a$-coefficient:

$$(2 + \omega) + \omega^{2}(1 - \omega) = 2 + \omega + \omega^{2} - \omega^{3} = 1 + \omega + \omega^{2}$$

$$0$$

and identically for $b$ and $c$ (each coefficient collapses to $1 + \omega + \omega^{2} = 0$). Hence $m_{ab} + \omega m_{bc} + \omega^{2}m_{ca} = 0$: the outer Napoleon triangle is equilateral. ∎

Numeric check on $(0,0), (4,0), (1,3)$: centers $(2, -1.1547)$, $(3.366, 2.366)$, $(-0.366, 1.789)$; all three mutual distances $\sqrt{14.261}$ ✓.
:::

:::app title="Technique takeaway — center formulas are linears in the vertices"
Any "centers of figures erected on the sides" problem is: (i) write each center as an affine combination of its two base vertices (fixed complex coefficients depending only on the shape erected); (ii) form the target combination; (iii) the vertex coefficients must vanish (or match) — this *is* the theorem. Works for squares (van Aubel), equilaterals (Napoleon), similar triangles, and regular $n$-gons. The coefficients come from the rotation factors $e^{i\theta}$ of oly-01.
:::

:::warn title="Traps — outward constructions"
- Outward vs inward: the sign in $\frac{p + q}{2} \pm \frac{i}{2}(q - p)$ flips the construction; "outward" is fixed by the polygon's orientation (CCW assumed throughout these sheets). Inward squares give a companion theorem (segments still equal/perpendicular) — same proof, sign flip.
- $\omega = e^{2\pi i/3}$ in the equilateral condition, but the $60^{\circ}$ turn of a side is $e^{\pm i\pi/3}$: $e^{-i\pi/3} = -\omega$, $e^{i\pi/3} = 1 + \omega$ — do not conflate the $\omega$ of the condition with the rotation factor.
- Van Aubel is for **any** quadrilateral (convex or not, with outward defined by consistent orientation); Napoleon for any triangle.
- "Centers" are centroids (of the square/equilateral), not vertices or circumcenters — the coefficients above are centroid-specific ($\frac{1}{3}$ for triangles, $\frac{1}{2} + \frac{i}{2}$-type for squares).
:::
