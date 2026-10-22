---
id: jee-11
part: jee
title: "Recap Toolkit — The Whole Chapter on One Sheet"
---

## The one-page register

:::key title="Algebra (sheet 01)"
$z = a + bi$; $\bar z = a - bi$; $z + \bar z = 2\operatorname{Re} z$, $z - \bar z = 2i\operatorname{Im} z$; $|z|^{2} = z \bar z$; $\frac{z}{w} = \frac{z \bar w}{|w|^{2}}$; $zw = 0 \Rightarrow z = 0$ or $w = 0$; $i^{n}$ cycles with period 4. Conjugation: $\overline{z + w} = \bar z + \bar w$, $\overline{zw} = \bar z \bar w$, $\bar{\bar z} = z$.
:::

:::key title="Plane and polar (sheets 02–03)"
$|z - w|$ = distance; midpoint $\frac{z_{1} + z_{2}}{2}$; triangle inequality $|z + w| \leq |z| + |w|$ and reverse, with same-direction/opposite-direction equality conditions; parallelogram law $|z + w|^{2} + |z - w|^{2} = 2|z|^{2} + 2|w|^{2}$.

$\operatorname{Arg} z \in (-\pi, \pi]$; $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$; products multiply moduli and **add** arguments; $\times i$ = quarter-turn CCW; $z + \bar z = 2r\cos\theta$, $z - \bar z = 2ir\sin\theta$; $|z| = 1 \Rightarrow \bar z = 1/z$.

De Moivre: $(\cos\theta + i\sin\theta)^{n} = \cos n\theta + i\sin n\theta$ ($n \in \mathbb{Z}$); triple angles from $n = 3$; $e^{i\pi} + 1 = 0$.
:::

:::key title="Roots and roots of unity (sheets 04–06)"
$n$-th roots of $w$: $R^{1/n} e^{i(\phi + 2k\pi)/n}$, $k = 0, \dots, n - 1$ — regular $n$-gon; square-root formula $\pm(\sqrt{\frac{r + a}{2}} + i\operatorname{sgn}(b)\sqrt{\frac{r - a}{2}})$.

$\omega = e^{2\pi i/3}$: $1 + \omega + \omega^{2} = 0$, $\bar\omega = \omega^{2}$, $(1 - \omega)(1 - \omega^{2}) = 3$, $1 + \omega = e^{i\pi/3}$, $1 - \omega = \sqrt{3}e^{-i\pi/6}$.

Vanishing sum: $\sum_{k=0}^{n-1} \zeta^{mk} = n$ if $n \mid m$, else $0$. Products: $\prod_{k=1}^{n-1}(1 - \zeta_{k}) = n$, $\prod_{k=1}^{n-1} \sin\frac{\pi k}{n} = \frac{n}{2^{n-1}}$, $\prod_{k=0}^{n-1} |z - \zeta_{k}| = |z^{n} - 1|$. Filter: $\sum_{k \equiv r \ (\mathrm{mod}\ n)} \binom{N}{k} = \frac{1}{n}\sum_{j} e^{-2\pi i r j/n}(1 + e^{2\pi i j/n})^{N}$.
:::

:::key title="Equations, loci, optimisation (sheets 07–10)"
Linear in $z, \bar z$: real/imag parts, or conjugate + $2 \times 2$. Real quadratics, $\Delta < 0$: $|z_{1} - z_{2}| = \sqrt{|\Delta|}$, roots conjugate.

Loci: circle $|z - z_{0}| = r$; bisector $|z - a| = |z - b|$; Apollonius $|z - a| = k|z - b|$; ellipse $|z - A| + |z - B| = 2a_{0}$ (max height $b_{0} = \sqrt{a_{0}^{2} - c^{2}}$); arc: $\arg\frac{z - a}{z - b} = \theta$, $R = \frac{|a - b|}{2\sin|\theta|}$, center on bisector at distance $\frac{|a - b|}{2}\cot|\theta|$, endpoints excluded.

Optimisation: $\min_{|z| = r} |z - a| = ||a| - r|$ at $z = r\,a/|a|$; $\max = |a| + r$; chord $|z - w| = 2|\sin\frac{\varphi}{2}|$ for unit points; $|z - a|^{2} + |z - b|^{2} = 2|z - m|^{2} + \frac{1}{2}|a - b|^{2}$.
:::

## Strategy card — the order that avoids every trap

:::app title="Five steps for any complex-number problem"
1. **Translate**: what is the algebraic shape ($z \bar z$, $|z - a|$, $\arg$) and the geometric shape (distance / rotation / locus)?
2. **Choose the language**: compute in algebra, see structure in geometry; solve in whichever is transparent, verify in the other when possible.
3. **Check degenerate cases**: $k = 1$ Apollonius, ellipse constant $\leq$ focal distance, $z = 0$, $w = 0$, $|z| = 1$ vs not.
4. **Track the branch/window**: $\operatorname{Arg} \in (-\pi, \pi]$; principal square root; equality conditions of the triangle inequality.
5. **Verify numerically**: plug the answer back ($z = \frac{8}{3} - \frac{i}{3}$ style) or compute both sides — one number check kills most silent errors.
:::

## Where this toolkit reappears

- **Trigonometry (ch 3)**: De Moivre re-derives multiple angles; $\prod \sin\frac{\pi k}{n}$ matches the olympiad sine products; $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$ is the bridge.
- **Quadratic equations / sequences (ch 6–7)**: conjugate-root symmetry, Vieta, geometric series on the unit circle.
- **Coordinate geometry & vectors (ch 12–16)**: rotation formula $X' = A + e^{i\theta}(X - A)$ is the vector rotation; Ptolemy and distance identities become coordinate proofs.
- **Calculus (ch 17–21)**: $\tan^{-1}x = \arg(1 + xi)$-style links; limits of $(\cos\frac{\theta}{n} + i\sin\frac{\theta}{n})^{n}$ foreshadow $e^{i\theta}$.
- **Olympiad Part II of this chapter**: geometry-by-complex-bash, Gauss sums, Gauss–Lucas, Pompeiu.

:::warn title="Final trap sweep"
1. $-2i^{2} = +2$; $\operatorname{Im}(3 + 4i) = 4$.
2. $\operatorname{Arg}(-1) = \pi$; fourth-quadrant arguments negative; Arg is not additive.
3. "Find the cube roots" = all three; $\sqrt{z}\sqrt{w} \neq \sqrt{zw}$.
4. $(1 + \omega)(1 + \omega^{2}) = 1$; $\sum_{k=0}^{2023}\omega^{k} = 1 + \omega$.
5. $|z - a| = r$ center at $a$; degenerate locus cases checked first; endpoints excluded on arcs.
6. Equality conditions stated; region ranges respect open/closed.
7. $\bar z = 1/z$ only on $|z| = 1$; $z + \frac{1}{z} = 2\cos\theta$ only there.
:::
