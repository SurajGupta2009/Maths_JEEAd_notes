---
id: jee-05
part: jee
title: "Mixed Problem Shapes and the Recap Toolkit — Sequences & Series"
---

## The question shapes

:::key title="Shape recognition for Part I problems"
1. **Identify the progression from data:** given $a_{m}, a_{n}$ in an AP, $d = \frac{a_{n} - a_{m}}{n - m}$; in a GP, $r^{n - m} = \frac{a_{n}}{a_{m}}$. Given three terms with a condition, use the symmetric parametrisations ($a - d, a, a + d$ / $\frac{a}{r}, a, ar$).
2. **$S_{n}$ given, $a_{n}$ wanted:** $a_{n} = S_{n} - S_{n - 1}$ ($n \geq 2$), $a_{1} = S_{1}$. Watch for $S_{n}$ formulas whose implied $a_{1}$ disagrees — then the sequence is only eventually an AP.
3. **AP meets GP:** the same three numbers in both progressions force them equal (AM = GM with the middle term common). Terms of an AP exponentiated give a GP, and vice versa via logs.
4. **Sum with polynomial general term:** split into $\sum k, \sum k^{2}, \sum k^{3}$. Polynomial × power: AGP. Rational with AP factors: telescope.
5. **Inequality/extremum:** AM–GM with constant product and attainable equality; or $n^{2}$-type identities for sums of odds.
:::

:::example title="Worked — mixed set"
**AP data:** an AP has $a_{5} = 17$, $a_{9} = 29$: $d = \frac{29 - 17}{9 - 5} = 3$, $a_{1} = 17 - 4 \cdot 3 = 5$, so $a_{n} = 3n + 2$ and $S_{20} = 10(10 + 57) = 670$? — compute carefully: $S_{20} = \frac{20}{2}(2 \cdot 5 + 19 \cdot 3) = 10 \cdot 67 = 670$ ✓.

**Recover terms:** $S_{n} = 3n^{2} + 5n$ gives $a_{n} = S_{n} - S_{n-1} = 6n + 2$ ($n \geq 2$) and $a_{1} = S_{1} = 8 = 6 + 2$ consistent, so it is the AP $8, 14, 20, \ldots$ with $d = 6$ ✓.

**Identify:** is $2, 3, 5, 9, 17, \ldots$ anything? Differences $1, 2, 4, 8$ form a GP — so $a_{n} = 2^{n - 1} + 1$ (each term is one more than a GP term; handle by splitting, sheet Olympiad-02's fixed-point idea in embryo).
:::

:::key title="Recap — the chapter on one card"
AP: $a_{n} = a + (n - 1)d$, $S_{n} = \frac{n}{2}(2a + (n - 1)d) = \frac{n}{2}(a + \ell)$; $2b = a + c$; means divisor $k + 1$. GP: $a_{n} = ar^{n - 1}$, $S_{n} = \frac{a(r^{n} - 1)}{r - 1}$, $S_{\infty} = \frac{a}{1 - r}$ ($\left|r\right| < 1$); $b^{2} = ac$. AM $\geq$ GM for positives, equality iff equal. $\sum k = \frac{n(n + 1)}{2}$, $\sum k^{2} = \frac{n(n + 1)(2n + 1)}{6}$, $\sum k^{3} = \left(\frac{n(n + 1)}{2}\right)^{2}$. AGP: shift-subtract; $\sum kx^{k} = \frac{x}{(1 - x)^{2}}$. Telescope: $\frac{1}{k(k + m)} = \frac{1}{m}\left(\frac{1}{k} - \frac{1}{k + m}\right)$, ends survive.
:::

:::warn title="The chapter checklist (mistakes that cost marks)"
1. Means divisor $k$ instead of $k + 1$. 2. $S_{\infty}$ with $\left|r\right| \geq 1$. 3. Mixed $\frac{r^{n} - 1}{r - 1}$ / $\frac{1 - r^{n}}{1 - r}$ signs. 4. Missing $\frac{1}{m}$ in the telescope split. 5. AGP powers misaligned. 6. AM–GM on negatives or with unattainable equality. 7. Assuming AP/GP without checking both difference and ratio. 8. $S_{n} = \frac{n}{2}(a + \ell)$ with wrong term count. 9. $\sum k^{3}$ without the square. 10. Recurrence/telescoping answer not checked at the first term.
:::

:::intuition title="Forward map"
Harmonic progressions and the full $A \geq G \geq H$ chain, recurrences with characteristic equations, generating functions, telescoping products and Wallis, Stolz–Cesàro: Part II. The through-line of the whole topic: *find the representation in which the sum collapses* — pairing (AP), shifting (GP/AGP), or differencing (telescopes).
:::
