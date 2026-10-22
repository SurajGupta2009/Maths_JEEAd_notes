---
id: jee-02
part: jee
title: "Permutations — nPr, Factorials, and Arrangements with Identical Objects"
---

## Ordered selections

:::derive title="nPr from filling labelled roles"
Fill $r$ labelled positions from $n$ distinct objects: $n$ options, then $n - 1$, …, then $n - r + 1$ (each count fixed regardless of history). Hence

$$P(n, r) = \frac{n!}{(n - r)!}, \qquad P(n, n) = n!$$

Equivalently $P(n, r)$ counts injective functions from an $r$-set to an $n$-set; $n!$ counts bijections of an $n$-set. $0! = 1$ is forced: there is exactly one empty arrangement.
:::

:::key title="Identical objects: label, count, divide by the symmetry"
Arrangements of a multiset with $n_{1}, \ldots, n_{k}$ copies of $k$ types ($n = \sum n_{i}$):

$$\frac{n!}{n_{1}!\, n_{2}! \cdots n_{k}!}$$

Proof: temporarily label all copies ($n!$ words); each unlabelled word is hit exactly $n_{1}! \cdots n_{k}!$ times (permute labels within each type). Division is legal **iff every fibre has the same size** — the exact-symmetry condition; where it fails (necklaces with identical beads), Part II's Burnside lemma is the fix.

Words from COMBINATORICS (C, O, I twice each, 13 letters): $\frac{13!}{2!\,2!\,2!} = 778377600$. MATHEMATICS: $\frac{11!}{2!\,2!\,2!} = 4989600$.
:::

:::example title="Worked — bundles inside identical-letter words"
Words from DAAR with the two A's adjacent: bundle AA into one super-object; arrange $\{D, AA, R\}$: $3! = 6$ (the identical A's give the bundle one internal order). Words: DAAR, AADR, ADAR, ADRA, ARDA, RADA ✓.
:::

:::warn title="Common traps — permutations"
- Dividing by symmetry when the symmetry is not exact (some arrangements fixed by the swap).
- "Choose first, then second" silently counting ordered pairs for an unordered question — off by $r!$.
- Bundles: internal orders multiply only if the bundled objects are distinct; identical objects contribute 1.
- $P(n, r)$ with $r > n$ is 0, not a formula to evaluate.
:::
