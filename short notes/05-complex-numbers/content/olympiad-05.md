---
id: oly-05
part: olympiad
title: "Extension — The Quadratic Gauss Sum: Squaring, Filtering, Phase Mod 4"
---

:::assume title="STATUS — olympiad extension (deeper number theory; IOQM/RMO+)"
The quadratic Gauss sum $G(n) = \sum_{k=0}^{n-1} \zeta^{k^{2}}$ is classical olympiad/number-theory material (the analytic heart of quadratic reciprocity). Its **evaluation mechanism** — square, re-index, let the vanishing sum filter — uses nothing but Part I sheets 05–06. The full reciprocity connection is quoted as context, not required. This is specialised extension material, not core JEE; nothing prevents an exam from asking the small cases ($n = 3, 4, 5$) computationally.
:::

## The object and its closed form

For $\zeta = e^{2\pi i/n}$ define $G(n) = \sum_{k=0}^{n-1} \zeta^{k^{2}}$ (the exponent is $k^{2}$ — this is why the vanishing-sum filter does not kill it outright).

:::key title="Closed form (phase locked to $n$ mod 4)"
$$G(n) = \sqrt{n} \ \text{ if } n \equiv 1\ (4); \qquad = i\sqrt{n} \ \text{ if } n \equiv 3\ (4)$$

$$G(n) = (1 + i)\sqrt{n} \ \text{ if } n \equiv 0\ (4); \qquad = 0 \ \text{ if } n \equiv 2\ (4)$$
:::

## Mechanism 1: square, then re-index

:::derive title="$|G(n)|^{2}$ — the double sum the filter can collapse"
Each term has modulus $1$, so $|G(n)|^{2} = \sum_{k, l} \zeta^{k^{2} - l^{2}}$. Put $k = l + h$: $k^{2} - l^{2} = 2lh + h^{2}$, and

$$|G(n)|^{2} = \sum_{h=0}^{n-1} \zeta^{h^{2}} \sum_{l=0}^{n-1} \zeta^{2lh}$$

- $n$ odd: $n \mid 2h \Rightarrow n \mid h$: only $h = 0$ survives: $|G(n)|^{2} = n$.
- $n = 2m$: $n \mid 2h \Leftrightarrow m \mid h$: $h = 0$ and $h = m$ survive; $\zeta^{m^{2}} = e^{\pi i m} = (-1)^{m}$, so $|G(n)|^{2} = n(1 + (-1)^{m})$: $0$ for $m$ odd ($n \equiv 2 \ (\mathrm{mod}\ 4)$), $2n$ for $m$ even ($n \equiv 0 \ (\mathrm{mod}\ 4)$).

Squaring is the whole trick: it turns a 1-dimensional sum into a 2-dimensional one the filter collapses. ∎
:::

## Mechanism 2: the phase, case by case

Since $k^{2} \equiv (n - k)^{2}$ (mod $n$), terms pair: $G(n) = 1 + 2\sum_{k=1}^{(n-1)/2} \zeta^{k^{2}}$ for odd $n$.

:::example title="Small cases, computed exactly"
$G(3) = 1 + 2\omega = 1 + 2(-\frac{1}{2} + i\frac{\sqrt{3}}{2}) = i\sqrt{3}$ ✓ ($n = 3 \equiv 3$: phase $i$).

$G(5) = 1 + 2(\zeta + \zeta^{4}) = 1 + 4\cos\frac{2\pi}{5} = 1 + (\sqrt{5} - 1) = \sqrt{5}$ ✓ ($n \equiv 1$: phase $1$), using $\cos\frac{2\pi}{5} = \frac{\sqrt{5} - 1}{4}$.

$G(7) = 1 + 2(\zeta + \zeta^{2} + \zeta^{4}) = i\sqrt{7}$ ✓ ($n = 7 \equiv 3$); the exponent residues $k^{2} \ (\mathrm{mod}\ 7)$ run $0, 1, 4, 2, 2, 4, 1$.

$G(8)$: residues $k^{2} \ (\mathrm{mod}\ 8)$ are $0, 1, 4$ with $4$ twice and $1$ four times: $G(8) = 2(1 + \zeta^{4}) + 4\zeta = 4 \cdot \frac{1 + i}{\sqrt{2}} = (1 + i)\sqrt{8}$ ✓ ($n \equiv 0$).

$G(2)$: here $\zeta = e^{2\pi i/2} = -1$ and $k = 0, 1$ give $\zeta^{0} + \zeta^{1} = 1 + (-1) = 0$ ✓ (vanishes, as the mod-4 rule predicts). Likewise $G(6) = G(10) = 0$.
:::

:::app title="How to use this in a problem"
1. **Vanishing case first**: if $n \equiv 2\ (\mathrm{mod}\ 4)$, the answer is $0$ before any arithmetic.
2. Odd $n$: pair $k$ with $n - k$, evaluate the half-sum in trig ($\cos\frac{2\pi k}{n}$ values) when $n$ is small; or quote the phase rule with the modulus $\sqrt{n}$.
3. The Legendre-symbol form $G(p) = \sum_{k=0}^{p-1} \left(\frac{k}{p}\right) \zeta^{k}$ for odd primes $p$ is the same number; $G(p) = \sqrt{p}$ or $i\sqrt{p}$ by $p \ (\mathrm{mod}\ 4)$ is quadratic reciprocity's analytic core — quote as context.
4. Verification habit: compute $|G(n)|^{2}$ numerically (should be $n$, $0$, or $2n$ per the table) — one number confirms the phase branch.
:::

:::warn title="Traps — Gauss sums"
- $n \equiv 2 (\mathrm{mod}\ 4)$: the sum is exactly $0$ — not "small"; the two surviving filter contributions cancel ($1$ and $(-1)^{m}$ with $m$ odd).
- The phase: $n \equiv 1$: real positive; $n \equiv 3$: purely imaginary positive; $n \equiv 0$: $(1 + i)\sqrt{n}$ (argument $\frac{\pi}{4}$) — mixing up $n \ (\mathrm{mod}\ 4)$ with $n \ (\mathrm{mod}\ 3)$ because "odd/even" feels like enough is the standard slip.
- The exponent is $k^{2}$ **mod $n$** inside $\zeta^{k^{2}}$ only implicitly: $\zeta^{k^{2}} = \zeta^{k^{2} \ (\mathrm{mod}\ n)}$ — when pairing residues, reduce mod $n$ first.
- $G(2) = 0$ uses $\zeta = e^{2\pi i/2} = -1$; reading $\zeta$ as $i = e^{2\pi i/4}$ (the $n = 4$ root) gives the wrong sum $1 + i$. $\zeta$ is always $e^{2\pi i/n}$ for the $n$ of the problem.
- $\zeta$ depends on $n$; every line must use the same $n$ throughout.
:::
