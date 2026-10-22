---
id: oly-02
part: olympiad
title: "Olympiad Extensions — Products of Sines & Cosines from Roots of Unity"
---

## Status of this sheet

Products like $\prod \sin\frac{k\pi}{n}$ are **classic RMO/INMO algebra** obtained by combining Part I identities with complex numbers (chapter 5 of the main sequence supplies $z = r e^{i\theta}$ and $|z|$; only elementary modulus facts are used). Classification: beyond the syllabus sentence, but every step is derivable from supplied identities and the definition of $|1 - e^{i\theta}|$.

## The two flagship products

$$\prod_{k=1}^{n-1} \sin\dfrac{k\pi}{n} = \dfrac{n}{2^{n-1}}$$

$$\prod_{k=1}^{n} \cos\dfrac{k\pi}{2n+1} = \dfrac{1}{2^{n}}$$

:::derive title="Derivation — factor $z^{n} - 1$ at the roots of unity, set $z = 1$, take moduli"
The $n$ roots of $z^{n} = 1$ are $e^{2\pi i k/n}$, $k = 0, \ldots, n-1$. So $z^{n} - 1 = (z - 1) \prod_{k=1}^{n-1} (z - e^{2\pi i k /n})$. Cancel $z - 1$ ($\frac{z^{n} - 1}{z - 1} = 1 + z + \cdots + z^{n-1}$) and set $z = 1$: $n = \prod_{k=1}^{n-1} (1 - e^{2\pi i k/n})$. Now $|1 - e^{i\theta}| = 2 \left|\sin\frac{\theta}{2}\right|$ (chord of a unit-circle arc; expand $|1 - \cos\theta - i \sin\theta|$). Taking moduli: $n = \prod 2 \sin\frac{k\pi}{n} = 2^{n-1} \prod \sin\frac{k\pi}{n}$ (each $\sin\frac{k\pi}{n} > 0$ for $1 \leq k \leq n-1$) ✓. The cosine product comes from the same factorisation at $z = -1$.
:::

:::example title="Worked. $\prod_{k=1}^{6} \sin\frac{k\pi}{7}$ and $\cos\frac{\pi}{7} \cos\frac{2\pi}{7} \cos\frac{3\pi}{7}$"
$n = 7$: product $= \frac{7}{2^{6}} = \frac{7}{64} = 0.109375$ ✓ (direct: $0.43388 \times 0.78183 \times 0.97493 \times 0.97493 \times 0.78183 \times 0.43388 = 0.109375$). Cosine product with $2n + 1 = 7$ ($n = 3$): $\frac{1}{2^{3}} = \frac{1}{8}$ ✓ (direct: $0.90097 \times 0.62349 \times 0.22252 = 0.125$).
:::

## The pattern to internalise

**A product of trig values at rational multiples of $\pi$ is a roots-of-unity problem in disguise.** Second tool: when the angles come from a polynomial whose roots are $\tan$-values or the values themselves, **Vieta** hands you sums/products for free (see the $\tan 20^{\circ} \tan 40^{\circ} \tan 80^{\circ} = \sqrt{3}$ model of Part I sheet 8 — same idea with $\tan 3\theta$).

:::example title="Worked. Sine product for $n = 5$: $\sin 36^{\circ} \sin 72^{\circ}$?"
$\prod_{k=1}^{4} \sin\frac{k\pi}{5} = \frac{5}{16}$. Pair $\sin\frac{\pi}{5} = \sin 36^{\circ}$, $\sin\frac{2\pi}{5} = \sin 72^{\circ}$, $\sin\frac{3\pi}{5} = \sin 72^{\circ}$, $\sin\frac{4\pi}{5} = \sin 36^{\circ}$: product $= (\sin 36^{\circ} \sin 72^{\circ})^{2} = \frac{5}{16}$, so $\sin 36^{\circ} \sin 72^{\circ} = \frac{\sqrt{5}}{4} \approx 0.5590$ ✓ (direct: $0.58779 \times 0.95106 = 0.55902$).
:::

:::warn title="Traps on this sheet"
- $\prod_{k=1}^{n-1}$ vs $\prod_{k=1}^{n}$: the sine product has $n - 1$ factors (the $k = 0$ factor would be $\sin 0 = 0$); count factors before quoting.
- $|1 - e^{i\theta}| = 2|\sin\frac{\theta}{2}|$ — drop the absolute values only after checking positivity (done via $0 < \frac{k\pi}{n} < \pi$).
- The cosine product $\prod_{k=1}^{n} \cos\frac{k\pi}{2n+1} = 2^{-n}$ has $n$ factors and denominator $2n + 1$ — a different index bookkeeping from the sine product.
- Claims here need complex arithmetic: state $e^{i\theta} = \cos\theta + i\sin\theta$ and $|z|$ facts explicitly in a solution write-up (assumptions below).
:::

## Assumptions & conventions

Complex numbers used: $e^{i\theta} = \cos\theta + i\sin\theta$, $|z w| = |z||w|$, $|1 - e^{i\theta}| = 2|\sin\frac{\theta}{2}|$ (proved above in modulus form). All products finite; $n \geq 2$ integer; positivity of $\sin\frac{k\pi}{n}$ for $1 \leq k \leq n - 1$ used to drop absolute values.
