---
id: oly-02
part: olympiad
title: "Extension — Telescoping Arctan Series and Sums"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO standard)"
Telescoping sums of $\tan^{-1}$-terms are a staple of IOQM/RMO arithmetic. The engine is Part I's difference formula; the *skill* is recognising which $\frac{a - b}{1 + ab}$ is hiding inside the term. Sums are treated exactly (finite forms and the convergent infinite limits); no calculus beyond "$\tan^{-1}n \to \frac{\pi}{2}$ as $n \to \infty$" is used (that limit is the graph of $\tan^{-1}$ from Part I).
:::

## The one identity every such sum hides

:::key title="Difference identity (the telescoping workhorse)"
For $ab > -1$:

$$\tan^{-1}a - \tan^{-1}b = \tan^{-1}\left(\frac{a - b}{1 + ab}\right)$$

So any term $\tan^{-1}\frac{c}{d}$ is telescoping material the moment $c = a - b$ and $d = 1 + ab$ for an *integer-valued* sequence $a_k, b_k$ (usually $b_k = a_{k+1}$ or $a_k = k + \text{const}$). With $a = k + 1$, $b = k$: $\frac{a - b}{1 + ab} = \frac{1}{1 + k + k^{2}}$; with $a = k + 1$, $b = k - 1$: $\frac{2}{k^{2}}$. Those two shapes cover most published problems.
:::

:::derive title="Series 1 — $\sum_{k=1}^{n} \tan^{-1}\frac{1}{1 + k + k^{2}} = \tan^{-1}(n+1) - \frac{\pi}{4}$"
Each term: $\frac{1}{1 + k(k+1)} = \frac{(k+1) - k}{1 + k(k+1)} = \tan^{-1}(k+1) - \tan^{-1}k$ (valid: $k(k+1) > -1$ ✓). The sum telescopes:

$$\sum_{k=1}^{n}[\tan^{-1}(k+1) - \tan^{-1}k]$$

$$\tan^{-1}(n+1) - \tan^{-1}1 = \tan^{-1}(n+1) - \frac{\pi}{4}.$$

Checks: $n = 1$: LHS $= \tan^{-1}\frac{1}{3} \approx 0.3217$; RHS $= \tan^{-1}2 - \frac{\pi}{4} \approx 1.1071 - 0.7854 = 0.3217$ ✓. As $n \to \infty$: sum $\to \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4}$.
:::

:::derive title="Series 2 — $\sum_{k=1}^{n} \tan^{-1}\frac{2}{k^{2}} = \tan^{-1}(n+1) + \tan^{-1}n - \frac{\pi}{4}$"
Here $\frac{2}{k^{2}} = \frac{(k+1) - (k-1)}{1 + (k+1)(k-1)}$, so $\tan^{-1}\frac{2}{k^{2}} = \tan^{-1}(k+1) - \tan^{-1}(k-1)$ (valid since $(k+1)(k-1) = k^{2} - 1 > -1$). This is a **two-step** telescope (stride 2):

$$\sum_{k=1}^{n}[\tan^{-1}(k+1) - \tan^{-1}(k-1)]$$

$$[\tan^{-1}(n+1) + \tan^{-1}n] - [\tan^{-1}0 + \tan^{-1}1]$$

$$= \tan^{-1}(n+1) + \tan^{-1}n - \frac{\pi}{4}.$$

Checks: $n = 1$: LHS $= \tan^{-1}2 \approx 1.1071$; RHS $= \tan^{-1}2 + \tan^{-1}1 - \frac{\pi}{4} = 1.1071$ ✓. Infinite limit: $\frac{\pi}{2} + \frac{\pi}{2} - \frac{\pi}{4} = \frac{3\pi}{4}$ — the classic "$\sum_{k=1}^{\infty} \tan^{-1}\frac{2}{k^{2}} = \frac{3\pi}{4}$".
:::

## Worked variants — the same engine, different residues

:::example title="Variant A — $\sum_{k=1}^{n} \tan^{-1}\frac{2k}{k^{4} + k^{2} + 2}$ (the denominator is the tell)"
Spot $a = k^{2} + k + 1$, $b = k^{2} - k + 1$: then $a - b = 2k$ ✓ and, from $(k^{2}+1)^{2} - k^{2} = k^{4} + k^{2} + 1$,

$$1 + ab = 1 + (k^{2} + k + 1)(k^{2} - k + 1)$$

$$= k^{4} + k^{2} + 2$$

exactly the given denominator. Each term is $\tan^{-1}(k^{2} + k + 1) - \tan^{-1}(k^{2} - k + 1)$, and $k^{2} - k + 1 = (k-1)^{2} + (k-1) + 1 = u_{k-1}$ with $u_{k} = k^{2} + k + 1$ — the sum telescopes along $u_k$:

$$\sum_{k=1}^{n} \tan^{-1}\frac{2k}{k^{4} + k^{2} + 2}$$

$$ = \tan^{-1}(n^{2} + n + 1) - \tan^{-1}1$$

$$ = \tan^{-1}(n^{2} + n + 1) - \frac{\pi}{4}.$$

Numeric verification (also in `math_checks.py`): $n = 1$: $\tan^{-1}\frac{2}{4} = 0.46365 = \tan^{-1}3 - \frac{\pi}{4}$ ✓. $n = 2$: $\tan^{-1}0.5 + \tan^{-1}\frac{2}{11} = 0.64350 = \tan^{-1}7 - \frac{\pi}{4}$ ✓.
:::

:::app title="Strategy card for arctan series"
1. Force the term into the shape $\tan^{-1}\frac{a - b}{1 + ab}$ by **matching the denominator to $1 + ab$** with small integer $a_k, b_k$.
2. Ensure $a_k b_k > -1$ on the range (automatic for positive sequences).
3. Telescoping: write out the first two and last two terms before cancelling; stride-2 series lose half their terms to the boundary.
4. Infinite sums: take $n \to \infty$ in the *closed form*, using $\tan^{-1}n \to \frac{\pi}{2}$; never sum "infinitely many small arctans" by estimation.
5. Verify $n = 1$ and $n = 2$ numerically before trusting the closed form.
:::

:::warn title="Traps — series"
- Stride-2 telescopes drop the parity of surviving boundary terms; write $n$ even and $n = 5$ by hand and compare.
- $\tan^{-1}\frac{2}{k^{2}}$ at $k = 1$: $\tan^{-1}2$; the split $\tan^{-1}2 - \tan^{-1}0$ is legal ($0 \cdot 2 = 0 > -1$ ✓) — but at $ab = -1$ the difference formula is void: e.g. $a = 1, b = -1$ gives $\tan^{-1}1 - \tan^{-1}(-1) = \frac{\pi}{2}$ while $\frac{a - b}{1 + ab} = \frac{2}{0}$ explodes — the boundary case is real, not a formality.
- Sign of the residue: $\tan^{-1}\frac{1}{1 + k + k^{2}}$ telescopes as $\tan^{-1}(k+1) - \tan^{-1}k$ (positive), not $k - (k+1)$.
:::
