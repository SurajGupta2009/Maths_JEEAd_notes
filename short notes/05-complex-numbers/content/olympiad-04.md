---
id: oly-04
part: olympiad
title: "Extension — Centroid Sums, Unit-Circle Configurations, w = z + 1/z"
---

:::assume title="STATUS — olympiad extension (synthesis problems)"
Three advanced-but-derivable strands: the Leibniz centroid distance formula (uses only $|z - a|^{2}$ expansions), unit-circle configurations where $|z_{k}| = 1$ forces a shape (uses $\bar z = 1/z$), and the map $w = z + \frac{1}{z}$ (Joukowski) collapsing circles to segments. All appear in IOQM/RMO and in coaching "advanced complex numbers" sets; all are derivable from Part I.
:::

## Leibniz — distance sums are minimised at the centroid

:::key title="Centroid identity (points $v_{1}, \dots, v_{n}$, centroid $c = \frac{1}{n}\sum v_{k}$, any $p$)"
$$\sum_{k=1}^{n} |p - v_{k}|^{2} = n\,|p - c|^{2} + \sum_{k=1}^{n} |v_{k} - c|^{2}$$
:::

:::derive title="Proof — expand $p - v_{k} = (p - c) - (v_{k} - c)$"
$$\sum |p - v_{k}|^{2}$$

$$ = \sum |(p - c) - (v_{k} - c)|^{2}$$

$$ = n|p - c|^{2} + \sum |v_{k} - c|^{2} - 2\operatorname{Re}\left((p - c)\overline{\sum(v_{k} - c)}\right)$$

and $\sum (v_{k} - c) = \sum v_{k} - nc = 0$ kills the cross term. ∎ Reading: the second term is the fixed "inertia" of the configuration; the first is minimised at $p = c$ — **the centroid is the point of minimum total squared distance**. Corollary for a regular $n$-gon of circumradius $R$ centered at $0$ with $|p| = 1$: sum $= n \cdot 1 + nR^{2}$ — e.g. hexagon $R = 2$, $|P| = 1$: $6 + 24 = 30$ (independent of the direction of $P$).
:::

## Unit-circle configurations — z̄ = 1/z is the entry ticket

:::app title="Four unit numbers summing to zero form a rectangle"
If $|z_{k}| = 1$ and $z_{1} + z_{2} + z_{3} + z_{4} = 0$: conjugate the sum and use $\bar z_{k} = 1/z_{k}$:

$$\frac{1}{z_{1}} + \frac{1}{z_{2}}$$

$$ = -\left(\frac{1}{z_{3}} + \frac{1}{z_{4}}\right) \Rightarrow (z_{1} + z_{2})\left(\frac{1}{z_{1}z_{2}} - \frac{1}{z_{3}z_{4}}\right)$$

$$ = 0$$

(using $z_{3} + z_{4} = -(z_{1} + z_{2})$). Either $z_{1} + z_{2} = 0$ (antipodal pairs $\Rightarrow \{\pm a, \pm b\}$: a cyclic parallelogram = rectangle), or $z_{1}z_{2} = z_{3}z_{4}$, which makes $\{z_{3}, z_{4}\} = \{-z_{1}, -z_{2}\}$ (same shape: $t^{2} + st + p = 0$ has roots $-1 \times$ those of $t^{2} - st + p = 0$). Square exactly when adjacent vertices are $90^{\circ}$ apart ($z_{2} = \pm i z_{1}$). ∎
:::

:::app title="Three unit numbers summing to zero are $120^{\circ}$ apart"
$|z_{1} + z_{2}| = |z_{3}| = 1 \Rightarrow 1 = 2 + 2\operatorname{Re}(z_{1}\bar z_{2}) \Rightarrow \operatorname{Re}(z_{1} \bar z_{2}) = -\frac{1}{2} \Rightarrow$ mutual angles $120^{\circ}$: an equilateral triangle centered at $0$; the six points $\{\pm z_{k}\}$ step by $60^{\circ}$: a **regular hexagon**. (Check: antipodes land exactly halfway between the $120^{\circ}$-spaced points.)
:::

:::key title="Product identity — distances to the $n$-th roots"
$$\prod_{k=0}^{n-1} |z - \zeta_{k}| = |z^{n} - 1|$$

(factor $z^{n} - 1 = \prod (z - \zeta_{k})$, take moduli). E.g. vertices of the regular pentagon on $|z| = 1$, distances from $z = 2$: $\prod |2 - \zeta_{k}| = |32 - 1| = 31$. On the circle itself ($z = e^{i\theta}$): $\prod_{k} |e^{i\theta} - \zeta_{k}| = 2\left|\sin\frac{n\theta}{2}\right|$.
:::

## Joukowski — w = z + 1/z collapses circles to segments

On $|z| = 1$: $\frac{1}{z} = \bar z$, so $w = z + \bar z = 2\cos\theta \in [-2, 2]$: the unit circle maps **two-to-one** onto the real segment $[-2, 2]$ (once each at $\pm 1$). Affine images: $w = z + \frac{1}{z} + i$ maps the circle to the segment $[-2 + i, 2 + i]$ — translate the segment by $i$. Off the circle: $|z| = r \neq 1$ gives the ellipse $\frac{u^{2}}{(r + 1/r)^{2}} + \frac{v^{2}}{(r - 1/r)^{2}} = 1$ in $w = u + iv$ (derive: $w = re^{i\theta} + r^{-1}e^{-i\theta} = (r + r^{-1})\cos\theta + i(r - r^{-1})\sin\theta$) — circles become ellipses, degenerating to the segment at $r = 1$.

:::example title="Worked — locus of $w = z + \frac{1}{z} + i$ as $|z| = 1$"
$w = 2\cos\theta + i$: the horizontal segment from $-2 + i$ to $2 + i$, traced twice (endpoints once). Every point attained ($\cos\theta = \frac{\operatorname{Re} w}{2}$). For range-type JEE questions ("find the range of $|z + \frac{1}{z} + 2i|$ on $|z| = 1$") the same reduction is sheet-10 method: $2\cos\theta + 2i \Rightarrow [2, 2\sqrt{2}]$ ✓ consistent.
:::

:::warn title="Traps — synthesis"
- $\bar z = 1/z$ requires $|z| = 1$; conjugating a relation to introduce $1/z$ is illegal off the circle.
- Rectangle conclusion from four-unit-sum-zero assumes all four on the unit circle; drop that and the statement dies ($z_{k}$ arbitrary with zero sum says nothing).
- Joukowski collapse is **two-to-one** ($z$ and $1/z$ map to the same $w$); locus answers list the image set, not parametrisations.
- The product identity's index runs $0$ to $n - 1$ (includes $z = 1$'s factor $|z - 1|$); the $\prod(1 - \zeta_{k}) = n$ formula of sheet 06 is its $z = 1$ cousin **excluding** $\zeta_{0}$ — keep the two consistent (at $z = 1$: $|z^{n} - 1| = 0$; the nonzero cousin excludes $k = 0$).
- Leibniz needs the **centroid**; using the circumcenter instead gives the wrong "minimum" statement (the circumcenter minimises max distance, a different problem).
:::
