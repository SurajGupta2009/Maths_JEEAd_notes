---
id: jee-04
part: jee
title: "Combinations — nCr, Pascal, Hockey-Stick, and Restricted Selections"
---

## Unordered selections

:::derive title="Why dividing by r! is exact here"
Every $r$-subset generates exactly $r!$ orderings, and every ordering comes from one subset: the ordered selections $P(n, r)$ split into equal fibres of size $r!$. So

$$\binom{n}{r} = \frac{n!}{r!\,(n - r)!}, \qquad \binom{n}{r} = \binom{n}{n - r}$$

The symmetry is complementation: choosing what to keep = choosing what to discard. First question of every problem: do the objects come with positions/labels (permutations) or not (combinations)? Mixed problems do both, in that order.
:::

:::key title="Pascal and hockey-stick (proofs are one split each)"
**Pascal:** $\binom{n}{r} = \binom{n - 1}{r} + \binom{n - 1}{r - 1}$ — split $r$-subsets by whether a fixed element is in (then choose $r - 1$ more) or out (choose all $r$ from the rest).

**Hockey-stick:** $\sum_{i=r}^{n} \binom{i}{r} = \binom{n + 1}{r + 1}$ — count $(r + 1)$-subsets of $\{1, \ldots, n + 1\}$ by their largest element $i + 1$: the rest is an $r$-subset of $\{1, \ldots, i\}$. E.g. $\binom{1}{1} + \binom{2}{1} + \binom{3}{1} + \binom{4}{1} = 10 = \binom{5}{2}$ (which is also $1 + 2 + 3 + 4$).
:::

:::example title="Worked — restricted selections"
At least one of 4 special books among 5 chosen from 20: $\binom{20}{5} - \binom{16}{5} = 15504 - 4368 = 11136$ (complement again).

Team of 11 from 7 batsmen, 5 bowlers, 3 all-rounders, at least 3 batsmen and at least 2 bowlers: enumerate by all-rounders $a = 0..3$ and sum products $\binom{7}{b}\binom{5}{w}\binom{3}{a}$ over valid $(b, w)$: $12 + 198 + 660 + 490 = 1360$. The template: one free variable plus bounds makes a finite table — check boundary triples twice, and **do not drop the $\binom{3}{a}$ factor** for the enumerated group (the classic table error: rows for $a = 1, 2$ are each 3 times their unweighted subsums).
:::

:::diagram
{"type": "blocks", "title": "Pascal's triangle — row n of (a+b)ⁿ, each entry the sum of the two above", "groups": [{"label": "n=0", "members": [1]}, {"label": "n=1", "members": [1, 1]}, {"label": "n=2", "members": [1, 2, 1]}, {"label": "n=3", "members": [1, 3, 3, 1]}, {"label": "n=4", "members": [1, 4, 6, 4, 1]}, {"label": "n=5", "members": [1, 5, 10, 10, 5, 1]}]}
:::

:::warn title="Common traps — combinations"
- $\binom{n}{r}$ computed for "arrange the chosen few" problems (or vice versa): decide order first.
- Case splits on "at least" that double-count overlaps — use complement or inclusion–exclusion (sheet 06).
- Boundary triples dropped in group-selection tables (the $(7, 3)$-type corner cases).
- Choosing from groups: multiply the independent group choices, then sum over the valid compositions — not the reverse.
:::
