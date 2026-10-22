---
id: jee-03
part: jee
title: "De Moivre and Euler — Powers, Roots, and Where Trig Identities Come From"
---

## De Moivre's theorem

:::key title="Statement (for integer $n \geq 1$, extended to all $n \in \mathbb{Z}$)"
$$\left(\cos\theta + i\sin\theta\right)^{n} = \cos n\theta + i\sin n\theta$$

$$\left(r(\cos\theta + i\sin\theta)\right)^{n} = r^{n}(\cos n\theta + i\sin n\theta).$$
:::

:::derive title="Proof — one induction step"
$n = 1$ is trivial. If it holds for $n$, multiply by $(\cos\theta + i\sin\theta)$ and use the angle-addition calculation of sheet 02: $(\cos n\theta + i\sin n\theta)(\cos\theta + i\sin\theta) = \cos(n+1)\theta + i\sin(n+1)\theta$. ∎

Negative $n$: $(\cos\theta + i\sin\theta)^{-1} = \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta)$ (conjugate flips the angle), so $z^{-m} = (z^{-1})^{m}$ extends the theorem to all integers. **Integer exponents only** — rational powers are multi-valued and go through the $n$-th-root machinery of sheet 04, never through "De Moivre with fractions".
:::

:::example title="Worked — $(1 + i)^{10}$ and $(\sqrt{3} + i)^{4}$"
$1 + i = \sqrt{2}\,e^{i\pi/4}$ (Euler form, below), so $(1 + i)^{10} = 2^{5} e^{i 10\pi/4} = 32 e^{i5\pi/2} = 32 e^{i\pi/2} = 32i$ — the only real work is reducing $5\pi/2 \equiv \frac{\pi}{2}$ (mod $2\pi$).

$(\sqrt{3} + i)^{4}$: $r = 2$, $\theta = \frac{\pi}{6}$: $2^{4}(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}) = 16(-\frac{1}{2} + i\frac{\sqrt{3}}{2}) = -8 + 8\sqrt{3}\,i$. Brute-force check by squaring twice gives the same — De Moivre halves the work at each step.

Pattern bank: $(1 + i)^{2} = 2i$, $(1 + i)^{4} = -4$, $(1 + i)^{8} = 16$ — the direction cycles with period 8 ($n \cdot 45^{\circ}$).
:::

:::derive title="Triple angles in ten seconds — the trig payoff"
Set $n = 3$ and expand $(\cos\theta + i\sin\theta)^{3} = \cos^{3}\theta + 3i\cos^{2}\theta\sin\theta - 3\cos\theta\sin^{2}\theta - i\sin^{3}\theta$. Equate real and imaginary parts (componentwise equality):

$$\cos 3\theta = 4\cos^{3}\theta - 3\cos\theta,$$

$$\sin 3\theta = 3\sin\theta - 4\sin^{3}\theta.$$

Every "hard" multiple-angle identity is a De Moivre expansion you can redo in seconds — do not memorise these; derive them.
:::

## Euler form

Define $e^{i\theta} := \cos\theta + i\sin\theta$ (for real $\theta$). Then $z = re^{i\theta}$, $z^{n} = r^{n}e^{in\theta}$, roots are $R^{1/n} e^{i(\phi + 2k\pi)/n}$, and the notation is *exact* (expanding the exponential series at $i\theta$ groups into $\cos\theta + i\sin\theta$ term by term). The famous checkpoint: $e^{i\pi} + 1 = 0$.

:::key title="The Euler-form move table"
Powers: $(re^{i\theta})^{n} = r^{n}e^{in\theta}$ (multiply the angle). Products: multiply moduli, add angles. Quotients: divide moduli, subtract angles.

**The workhorse pair** (for $z = re^{i\theta}$, and for $|z| = 1$ where $\bar z = 1/z$):

$$z + \bar z = 2r\cos\theta, \qquad z - \bar z = 2ir\sin\theta,$$

$$e^{i\theta} + e^{-i\theta} = 2\cos\theta$$

$$e^{i\theta} - e^{-i\theta} = 2i\sin\theta, \qquad \cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2},$$

$$\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$
:::

:::app title="Why $z^{n} + z^{-n}$ is a polynomial in $2\cos\theta$"
For $z = e^{i\theta}$: $z^{n} + z^{-n} = 2\cos n\theta$ — real, always. E.g. $z^{3} + z^{-3} = 2\cos 3\theta = 8\cos^{3}\theta - 6\cos\theta$. This bridge (complex ↔ trig) is how olympiad trig-product identities and JEE "express $\cos 3\theta$ in terms of $\cos\theta$" questions are the same question. Also: three unit vectors $120^{\circ}$ apart sum to zero — $e^{i\theta}(1 + \omega + \omega^{2}) = 0$ — the geometric seed of sheet 05.
:::

:::assume title="Scope note on $e^{i\theta}$"
$e^{i\theta}$ is *defined* as $\cos\theta + i\sin\theta$ here; the full complex exponential $e^{z}$ for arbitrary complex $z$ (series, log) is a calculus-topic treated later in the series. Everything on this sheet uses only the definition plus the algebra of sheets 01–02. The notation is used because it compresses De Moivre to one line; the content never depends on it.
:::

:::warn title="Common traps — De Moivre and Euler"
- **Integer exponents only**: $(\cos\theta + i\sin\theta)^{1/2} \neq \cos\frac{\theta}{2} + i\sin\frac{\theta}{2}$ as a statement about *all* square roots — the right side is one of the two roots (the principal one), the other is its negative. Rational powers go through sheet 04.
- Reducing the angle: $(1 + i)^{10} = 32i$ requires $10\pi/4 \equiv \pi/2$ (mod $2\pi$); forgetting the reduction gives phantom directions.
- $e^{i\theta} = 1 \Leftrightarrow \theta \equiv 0$ (mod $2\pi$); $e^{i\theta}$ has modulus $1$ for real $\theta$, so $|e^{i\theta}| = 1$ never gives magnitude information.
- Equating real/imaginary parts to extract $\cos n\theta$ needs the powers of $\sin^{2} = 1 - \cos^{2}$ converted consistently — a messy sign here is not a "deep" error, it is bookkeeping.
- $\bar z = 1/z$ is valid **only** when $|z| = 1$; $z + 1/z = 2\cos\theta$ likewise.
:::
