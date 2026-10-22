---
id: jee-05
part: jee
title: "Roots of Unity — The ω Toolkit and Vanishing Sums"
---

## The cube roots of unity

$z^{3} = 1$ has solutions $1, \omega = e^{2\pi i/3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}, \omega^{2} = e^{4\pi i/3} = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$. **By universal convention $\omega$ denotes a non-real cube root of unity**: $\omega^{3} = 1$, $\omega \neq 1$.

:::key title="The five $\omega$-identities (each with its one-line proof)"
1. $1 + \omega + \omega^{2} = 0$ — since $\omega \neq 1$ is a root of $x^{3} - 1 = (x - 1)(x^{2} + x + 1)$.
2. $\bar\omega = \omega^{2}$ — conjugate reflects in the real axis; $\omega, \omega^{2}$ sit at $\pm 120^{\circ}$.
3. $(1 - \omega)(1 - \omega^{2}) = 3$ — expand: $1 - (\omega + \omega^{2}) + \omega^{3} = 1 + 1 + 1 = 3$.
4. $1 + \omega = e^{i\pi/3}$ — compute: $\frac{1}{2} + i\frac{\sqrt{3}}{2}$: modulus $1$, argument $60^{\circ}$; also $1 + \omega = -\omega^{2}$.
5. $1 - \omega = \sqrt{3}\,e^{-i\pi/6}$ — so $|1 - \omega| = \sqrt{3}$ (the side of the triangle) and $\arg(1 - \omega) = -30^{\circ}$.

Drill: $\omega + \omega^{2} = -1$, $\omega\omega^{2} = \omega^{3} = 1$, $\omega^{3k} = 1$.
:::

:::derive title="Why the triangle geometry keeps reappearing"
$1, \omega, \omega^{2}$ are equally spaced on the unit circle: an equilateral triangle. Identity 3 says the *squared side length* is $3$; identity 4 says $1 + \omega$ is the vertex reached by rotating $1$ by $60^{\circ}$. Every $\omega$-computation in an exam is either "expand and use $1 + \omega + \omega^{2} = 0$, $\omega^{3} = 1$" or "read the geometry". Try both when stuck — they must agree.
:::

:::example title="Worked — $(1 + \omega)(1 + \omega^{2})$, and the sign trap"
Algebra: $1 + (\omega + \omega^{2}) + \omega^{3} = 1 - 1 + 1 = 1$. Geometry: $(e^{i\pi/3})(e^{-i\pi/3}) = 1$ ✓. The classic wrong answer is $2$ — produced by treating $\omega + \omega^{2}$ as $+1$. If you get $2$, the sign drill above has slipped.

Also: $\sum_{k=0}^{2023} \omega^{k}$: $2024 = 3 \cdot 674 + 2$ terms; each block of three sums to $0$, leaving $\omega^{2022} + \omega^{2023} = 1 + \omega = -\omega^{2}$.

$(\omega + \omega^{2})^{3} + 3(\omega + \omega^{2}) + 1 = (-1)^{3} + 3(-1) + 1 = -3$.
:::

## The n-th roots of unity and the vanishing sum

The $n$-th roots are $\zeta_{k} = e^{2\pi i k/n}$, $k = 0, \dots, n-1$ — a regular $n$-gon on $|z| = 1$; write $\zeta = e^{2\pi i/n}$.

:::key title="Vanishing-sum identity — the engine of every sum-of-roots problem"
For integers $m, n$ with $n \geq 1$:

$$\sum_{k=0}^{n-1} \zeta^{mk} = n \ \text{ if } n \text{ divides } m, \qquad = 0 \ \text{ otherwise.}$$

Proof: geometric series with ratio $\zeta^{m}$: if $n \nmid m$ then $\zeta^{m} \neq 1$ and the sum is $\frac{(\zeta^{m})^{n} - 1}{\zeta^{m} - 1} = \frac{(\zeta^{n})^{m} - 1}{\zeta^{m} - 1} = 0$; if $n \mid m$ every term is $1$. ∎

Read geometrically: the vertices of a regular $n$-gon centered at $0$ sum to zero. Corollaries: $\sum_{k=0}^{n-1} \zeta^{k} = 0$ for $n > 1$; the sixth-roots sum $\sum_{k=0}^{5} e^{i\pi k/3} = 0$; a geometric progression of unit steps around the circle always closes.
:::

:::app title="Standard applications — the two reflexes"
1. **Sums of powers**: $\sum_{k=0}^{N} \omega^{k}$-type: reduce the number of terms mod $3$ (or mod $n$), leftover terms only.
2. **Vieta on $x^{n} - 1$**: the coefficient of $x^{n-1}$ is $0$, so $\zeta_{0} + \cdots + \zeta_{n-1} = 0$ — the vanishing sum again. For $t^{3} + 27 = 0$ (cube roots of $-27$): sum $= 0$, pairwise sum $= 0$ — see sheet 04. Whenever roots sit on a regular polygon, Vieta's zero coefficients are the polygon's symmetry in disguise.
:::

:::assume title="Conventions"
$\omega$ = a **non-real** cube root of unity ($\omega = e^{2\pi i/3}$ or $e^{4\pi i/3}$ — the two are $\omega$ and $\omega^{2}$, and "$\omega$ is a non-real cube root" statements must hold for either choice). $\zeta = e^{2\pi i/n}$ for general $n$. "The $n$-th roots of unity" always means the full set of $n$. All sums in this sheet are finite; no convergence questions arise.
:::

:::warn title="Common traps — roots of unity"
- $(1 + \omega)(1 + \omega^{2}) = 1$, not $2$. ($\omega + \omega^{2} = -1$.)
- $\omega^{3} = 1$ does **not** let you "cancel cubes" inside sums like $\omega^{2} + \omega + 1$ — that sum is $0$ by identity 1, not by cancellation.
- $\sum_{k=0}^{n-1} \zeta^{mk} = 0$ needs $n \nmid m$; e.g. $\sum_{k=0}^{5} e^{i\pi k/3}$ is $0$ because the terms are the six sixth-roots of unity — the exponent step is $\pi/3 = 2\pi/6$ ✓ — but $\sum_{k=0}^{5} e^{i\pi k/6}$ is **not** $0$ (that is twelve steps' worth compressed into six terms: a geometric series with ratio $e^{i\pi/6}$, sum $\frac{1 - e^{i\pi}}{1 - e^{i\pi/6}} = \frac{2}{1 - e^{i\pi/6}} \neq 0$).
- $\bar\omega = \omega^{2}$ is special to cube roots ($\omega^{2} = \omega^{-1} = \bar\omega$ needs $|\omega| = 1$ ✓ but the exponent identity is $n = 3$ specific).
- Using $\omega$ as if it were real: $\omega^{2} \neq \omega$; $\omega^{2} = \bar\omega$ is complex, and $|\omega| = 1$ means $\omega\bar\omega = 1$.
:::
