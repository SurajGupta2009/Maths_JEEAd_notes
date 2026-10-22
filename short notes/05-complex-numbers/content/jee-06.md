---
id: jee-06
part: jee
title: "Product Formulas and the Roots-of-Unity Filter"
---

## Products of (1 − ζₖ) — where the number n hides

:::key title="Product formula"
For $\zeta_{k} = e^{2\pi i k/n}$ ($k = 0, \dots, n-1$):

$$\prod_{k=1}^{n-1}\left(1 - \zeta_{k}\right) = n.$$
:::

:::derive title="Proof — factor, then let $x \to 1$"
$x^{n} - 1 = \prod_{k=0}^{n-1}(x - \zeta_{k}) = (x - 1)\prod_{k=1}^{n-1}(x - \zeta_{k})$. Divide by $x - 1$ and take $x \to 1$ (equivalently, differentiate at $x = 1$):

$$\prod_{k=1}^{n-1}(1 - \zeta_{k}) = \lim_{x \to 1}\frac{x^{n} - 1}{x - 1} = n. \ ∎$$

Two checks: $n = 3$: $(1 - \omega)(1 - \omega^{2}) = 3$ ✓ (sheet 05, identity 3). $n = 5$: $\prod_{k=1}^{4}(1 - e^{2\pi i k/5}) = 5$ ✓. The factors come in conjugate pairs, so the product is real and positive — consistent.
:::

:::key title="Trigonometric cousin — the sine product"
$$\prod_{k=1}^{n-1} \sin\frac{\pi k}{n} = \frac{n}{2^{n-1}}$$

Derivation: $|1 - \zeta_{k}| = 2\sin\frac{\pi k}{n}$ (compute: $|1 - e^{2\pi i k/n}| = |e^{\pi i k/n}||e^{-\pi i k/n} - e^{\pi i k/n}| = 2\sin\frac{\pi k}{n}$, positive for $1 \leq k \leq n-1$). Take moduli in the product formula. Check $n = 6$: $\frac{1}{2} \cdot \frac{\sqrt{3}}{2} \cdot 1 \cdot \frac{\sqrt{3}}{2} \cdot \frac{1}{2} = \frac{3}{16}$ and $\frac{6}{2^{5}} = \frac{3}{16}$ ✓. E.g. $\sin\frac{\pi}{5}\sin\frac{2\pi}{5}\sin\frac{3\pi}{5}\sin\frac{4\pi}{5} = \frac{5}{16}$.
:::

## The roots-of-unity filter

**Problem type:** compute $\sum_{k \equiv r \ (\mathrm{mod}\ n)} \binom{N}{k}$ — add only the terms whose index sits in one residue class.

:::key title="The filter (derived on the spot if forgotten)"
For $\zeta = e^{2\pi i/n}$, the average $\frac{1}{n}\sum_{j=0}^{n-1} \zeta^{j(k - r)}$ equals $1$ when $n \mid (k - r)$ and $0$ otherwise (vanishing sum — sheet 05). Hence for $P(x) = \sum_{k} c_{k}x^{k}$:

$$\sum_{k \equiv r \ (\mathrm{mod}\ n)} c_{k} = \frac{1}{n}\sum_{j=0}^{n-1} \zeta^{-rj} P(\zeta^{j})$$

and for $P(x) = (1 + x)^{N}$:

$$\sum_{k \equiv r \ (\mathrm{mod}\ n)} \binom{N}{k}$$

$$ = \frac{1}{n}\sum_{j=0}^{n-1} e^{-2\pi i r j / n}\left(1 + e^{2\pi i j / n}\right)^{N}.$$
:::

:::example title="Worked — $\sum_{k \equiv 0 \ (\mathrm{mod}\ 3)} \binom{9}{k}$"
Filter with $n = 3$, $r = 0$, $\omega = e^{2\pi i/3}$:

$$\frac{1}{3}\left[(1 + 1)^{9} + (1 + \omega)^{9} + (1 + \omega^{2})^{9}\right]$$

$$ = \frac{1}{3}\left[512 + (e^{i\pi/3})^{9} + (e^{-i\pi/3})^{9}\right]$$

$$ = \frac{1}{3}(512 - 1 - 1) = 170.$$

Direct check: $\binom{9}{0} + \binom{9}{3} + \binom{9}{6} + \binom{9}{9} = 1 + 84 + 84 + 1 = 170$ ✓.

Sibling classes: $r = 1$: $\frac{1}{3}\left[512 + \omega^{-1}(-1) + \omega^{-2}(-1)\right] = \frac{1}{3}(512 + 1) = 171$; $r = 2$ likewise $171$. Check: $170 + 171 + 171 = 512 = 2^{9}$ ✓ — the classes partition the power set.
:::

:::app title="When to reach for the filter"
- Any "sum of binomial coefficients where $k \equiv r$ (mod $n$)" — JEE Advanced has asked $\omega$-flavoured versions repeatedly (e.g. sums of $\binom{N}{k}$ over $k \equiv 1\ (\mathrm{mod}\ 3)$).
- Evaluating $(1 + \zeta^{j})^{N}$: convert $1 + \zeta^{j}$ to polar first ($1 + \omega = e^{i\pi/3}$, $1 + \omega^{2} = e^{-i\pi/3}$, $1 + i = \sqrt{2}e^{i\pi/4}$ ...) then De Moivre.
- Alternating sums ($(-1)^{k}\binom{N}{k}$) are the case $n = 2$: $\sum_{k \text{ even}} \binom{N}{k} = \sum_{k \text{ odd}} \binom{N}{k} = 2^{N-1}$ for $N \geq 1$.
:::

:::derive title="Side identity worth owning — $\prod_{k=0}^{n-1}|z - \zeta_{k}| = |z^{n} - 1|$"
Factor $z^{n} - 1 = \prod (z - \zeta_{k})$ and take moduli: one line. At $z = 2$, $n = 5$: $\prod |2 - \zeta_{k}| = |32 - 1| = 31$ — a five-distance product with no trigonometry. At $z = e^{i\theta}$ on the unit circle: $\prod_{k=0}^{n-1} |e^{i\theta} - \zeta_{k}| = |e^{in\theta} - 1| = 2\left|\sin\frac{n\theta}{2}\right|$ — a clean chord product (olympiad sheets use this form).
:::

:::warn title="Common traps — products and filters"
- $\prod_{k=1}^{n-1}(1 - \zeta_{k}) = n$ is a **product of complex numbers**; its modulus interpretation ($|1 - \zeta_{k}| = 2\sin\frac{\pi k}{n}$) is a different statement — keep the two apart.
- Filter setup: the sum must run over $k \equiv r$ (mod $n$) **with the same $n$ as the root of unity**; mixing $n = 3$ filter with a mod-4 condition is the standard misfire.
- $(1 + \omega)^{9} = -1$ requires $1 + \omega = e^{i\pi/3}$ (identity 4) first — expanding $(1 + \omega)^{9}$ by the binomial theorem is a trap door.
- In the sine product, the index runs $1$ to $n - 1$ (not $n$) and $\sin\frac{\pi k}{n} > 0$ throughout — sign care when $n$ is even.
- $\sum_{k \equiv 0 \ (3)} \binom{9}{k} = 170$ counts $k = 0, 3, 6, 9$ — $k = 0$ is included; "positive multiples of 3" is a different (170 − 1) answer. Read the residue class exactly.
:::
