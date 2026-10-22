---
id: olympiad-03
part: olympiad
title: "Extension — Telescoping Products, Wallis, Stolz–Cesàro, and Asymptotics"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Multi-factor telescopes, infinite products, discrete l'Hôpital and growth-rate answers are Olympiad/analysis-flavoured extensions of the Part I summation engines.
:::

## Products telescope too

:::derive title="The product ∏(1 − 1/k²)"
Since $\log \prod a_{k} = \sum \log a_{k}$, products collapse by the same cancellation as sums. The unlocking identity is the difference of squares: $1 - \frac{1}{k^{2}} = \frac{k - 1}{k} \cdot \frac{k + 1}{k}$. Hence

$$\prod_{k=2}^{n}\left(1 - \frac{1}{k^{2}}\right) = \prod_{k=2}^{n}\frac{k - 1}{k} \cdot \prod_{k=2}^{n}\frac{k + 1}{k} = \frac{1}{n} \cdot \frac{n + 1}{2} = \frac{n + 1}{2n} \to \frac{1}{2}$$

Check at $n = 4$: $\frac{3}{4} \cdot \frac{8}{9} \cdot \frac{15}{16} = \frac{5}{8} = \frac{4 + 1}{2 \cdot 4}$ ✓. The same split in $\prod \frac{4k^{2}}{4k^{2} - 1} = \prod \frac{2k}{2k - 1} \cdot \frac{2k}{2k + 1}$ gives the finite closed form $\frac{2^{4n}(n!)^{4}}{(2n + 1)\left((2n)!\right)^{2}}$, whose limit is **Wallis's product** $\frac{\pi}{2}$.
:::

## Stolz–Cesàro: l'Hôpital for sequences

:::key title="The discrete l'Hôpital"
If $b_{n}$ is strictly increasing and unbounded, then $\lim \frac{a_{n}}{b_{n}} = \lim \frac{a_{n + 1} - a_{n}}{b_{n + 1} - b_{n}}$ whenever the latter limit exists. No differentiability needed.

Worked: $\lim \frac{H_{n}}{\ln n}$ with $H_{n} = \sum_{1}^{n} \frac{1}{k}$: the difference ratio is $\frac{1/(n + 1)}{\ln(1 + 1/n)} \to 1$, so $\frac{H_{n}}{\ln n} \to 1$. Numerically $1.1264, 1.0836, 1.0627, 1.0501$ at $n = 10^{2}, \ldots, 10^{5}$ — approaching 1 slowly, at rate $\sim \frac{\gamma}{\ln n}$ with $\gamma$ Euler's constant.
:::

## Asymptotics: when the honest answer is a growth rate

:::example title="Worked — aₙ₊₁ = aₙ + 1/aₙ grows like √(2n)"
$a_{1} = 1$, $a_{n + 1} = a_{n} + \frac{1}{a_{n}}$. Square: $a_{n + 1}^{2} = a_{n}^{2} + 2 + \frac{1}{a_{n}^{2}}$, telescoping to $a_{n}^{2} = 2(n - 1) + \sum_{k=1}^{n-1} \frac{1}{a_{k}^{2}} + 1$. Since $a_{k}^{2} \approx 2k$, the terms $\frac{1}{a_{k}^{2}} \approx \frac{1}{2k}$, so the sum grows only like $\frac{1}{2}\ln n$; hence $a_{n}^{2} = 2n + O(\log n)$ and $a_{n} \sim \sqrt{2n}$. (Note: the remainder sum does **not** converge to a constant — it diverges logarithmically; the growth-rate conclusion is unaffected.) Numerics: $a_{10} = 4.5699$ vs $\sqrt{20} = 4.4721$, ratio $\to 1$ ✓. The method: **transform until it telescopes, then estimate the remainder.**
:::

:::warn title="Common traps — advanced summation"
- Infinite product "cancellation" without checking convergence to a **nonzero** limit.
- Stolz–Cesàro applied with non-monotone denominator, or in the converse direction (the difference-limit may fail while the ratio-limit exists).
- Asymptotic claims stated as equalities: $a_{n} \sim \sqrt{2n}$ means ratio $\to 1$, not $a_{n} = \sqrt{2n} + o(1)$.
- Telescoping arctan-type sums (e.g. $\sum \arctan \frac{1}{k^{2} + k + 1} = \frac{\pi}{4} - \arctan \frac{1}{n + 1}$) need branch care: each difference must land in the principal range (chapter 4 of this series).
:::
