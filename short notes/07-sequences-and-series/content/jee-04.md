---
id: jee-04
part: jee
title: "Arithmetico-Geometric Sums and Telescoping — The Two Summation Engines (Derivable Applications)"
---

:::assume title="STATUS — core technique, extension label"
The official syllabus names AP, GP, AM/GM and $\sum k, \sum k^{2}, \sum k^{3}$. AGP sums and the method of differences are **not separate syllabus lines** — they are one-step derivations from the GP sum formula, and JEE Advanced asks them exactly in that derivable form. Master the derivations, not just the results.
:::

## Engine 1: shift-and-subtract (AGP)

An **arithmetico-geometric progression** has terms $(a + kd)r^{k}$: an AP factor times a GP factor.

:::derive title="The AGP sum"
Let $S = \sum_{k=0}^{n-1} (a + kd)r^{k}$. Form $S - rS$: the AP factor's constancy turns the difference into a plain GP plus one leftover term, giving (for $r \neq 1$) a closed form; letting $n \to \infty$ with $\left|r\right| < 1$,

$$\sum_{k=0}^{\infty} (a + kd)r^{k} = \frac{a}{1 - r} + \frac{dr}{(1 - r)^{2}}$$

Most used case: $\sum_{k=1}^{\infty} k x^{k} = \frac{x}{(1 - x)^{2}}$ ($\left|x\right| < 1$). Applying shift-subtract twice: $\sum k^{2} x^{k} = \frac{x(1 + x)}{(1 - x)^{3}}$.
:::

:::example title="Worked — AGP"
$\sum_{k=1}^{\infty} \frac{k}{2^{k}} = \frac{1/2}{(1 - 1/2)^{2}} = 2$. Finite check: $1 + 2x + 3x^{2} + 4x^{3} + 5x^{4}$ at $x = \frac{1}{2}$ is $1 + 1 + \frac{3}{4} + \frac{1}{2} + \frac{5}{16} = \frac{57}{16}$, matching the finite formula $\frac{1 - (n + 1)x^{n} + nx^{n + 1}}{(1 - x)^{2}}$ at $n = 5$, and approaching the infinite value $4$ ✓.

**Align the powers before subtracting** — mis-indexing by one term is the standard AGP error.
:::

## Engine 2: the method of differences (telescoping)

:::key title="Telescoping: find f with term = f(k) − f(k+1)"
If the general term equals $f(k) - f(k + 1)$, then $\sum_{k=1}^{n} = f(1) - f(n + 1)$: only the ends survive. The standard split, from partial fractions:

$$\frac{1}{k(k + m)} = \frac{1}{m}\left(\frac{1}{k} - \frac{1}{k + m}\right)$$

With $m = 1$: $\sum_{1}^{n} \frac{1}{k(k + 1)} = \frac{n}{n + 1}$. With $m = 2$ the first **two** and last **two** terms survive: $\sum_{k=1}^{5} \frac{1}{k(k + 2)} = \frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{6} - \frac{1}{7}\right) = \frac{25}{42}$.
:::

:::example title="Worked — recognising telescopes in disguise"
- $\sum k \cdot k! = (n + 1)! - 1$, since $k \cdot k! = (k + 1)! - k!$.
- $\sum \frac{k}{(k + 1)!} = 1 - \frac{1}{(n + 1)!}$, since $\frac{k}{(k+1)!} = \frac{1}{k!} - \frac{1}{(k + 1)!}$.
- $\sum_{k=1}^{n} \frac{1}{k(k + 1)(k + 2)} = \frac{n(n + 3)}{4(n + 1)(n + 2)}$ via $\frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left(\frac{1}{k(k+1)} - \frac{1}{(k+1)(k+2)}\right)$ — a difference of differences.
:::

:::warn title="Common traps — summation engines"
- Forgetting the $\frac{1}{m}$ factor in the split.
- Infinite AGP/telescoping sums quoted without the convergence condition ($\left|r\right| < 1$; for telescopes, $f(n + 1)$ must have a limit).
- With $m \geq 2$, cancelling as if only one term survives at each end.
- Shift-and-subtract with misaligned powers (write both sums out in full, aligned by power of $r$).
:::
