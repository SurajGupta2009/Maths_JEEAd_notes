---
id: olympiad-03
part: olympiad
title: "Extension — Partitions, Stirling Numbers, and Extremal Set Families"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Integer partitions, Stirling/Bell numbers and extremal combinatorics (Sperner, Erdős–Ko–Rado) are Olympiad territory beyond the JEE P&C lines.
:::

:::key title="Integer partitions: no closed form, one generating function"
$p(n)$ counts partitions of $n$ (order ignored): $1, 2, 3, 5, 7, 11, 15, 22, 30, 42$ for $n = 1..10$. There is no stars-and-bars model; the count lives in

$$\sum_{n \geq 0} p(n) x^{n} = \prod_{k \geq 1} \frac{1}{1 - x^{k}}$$

**Euler:** partitions into **distinct** parts = partitions into **odd** parts, since $\prod (1 + x^{k}) = \prod \frac{1 - x^{2k}}{1 - x^{k}} = \prod_{m\ \mathrm{odd}} \frac{1}{1 - x^{m}}$ (for $n = 10$: 10 of each, listed in math_checks by enumeration). Conjugation of Young diagrams: partitions into at most $k$ parts $\leftrightarrow$ partitions with largest part $\leq k$. Euler's pentagonal theorem gives $p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) + \cdots$ (check $p(10) = 30 + 22 - 7 - 3 = 42$ ✓).
:::

:::key title="Stirling numbers of the second kind and Bell numbers"
$S(n, k)$ = partitions of an $n$-set into $k$ nonempty **unlabelled** blocks: recurrence ("where does element $n$ go?") $S(n, k) = k S(n - 1, k) + S(n - 1, k - 1)$; closed form by IE $S(n, k) = \frac{1}{k!}\sum_{j} (-1)^{j}\binom{k}{j}(k - j)^{n}$, because $k! S(n, k)$ counts onto functions. $S(6, 3) = 3 \cdot 25 + 15 = 90 = \frac{729 - 192 + 3}{6}$ ✓. Bell numbers $B_{n} = \sum_{k} S(n, k)$: $1, 1, 2, 5, 15, 52, 203$. Dividing 6 people into 3 unlabelled pairs: $\frac{6!}{(2!)^{3} 3!} = 15$.
:::

:::key title="Extremal families: Sperner and Erdős–Ko–Rado"
**Sperner:** an antichain of subsets of an $n$-set (no one containing another) has at most $\binom{n}{\lfloor n/2 \rfloor}$ members — the middle layer is extremal (LYM proof: a random maximal chain meets an antichain at most once, and hits a $k$-set with probability $1/\binom{n}{k}$).

**Erdős–Ko–Rado:** for $n \geq 2k$, an intersecting family of $k$-subsets of an $n$-set has at most $\binom{n - 1}{k - 1}$ members; the star (all sets through one fixed point) attains it. Hypothesis essential: for $n < 2k$ every two $k$-sets meet and the whole $\binom{n}{k}$ is intersecting.
:::

:::warn title="Common traps — advanced counting"
- Confusing partitions (no formula) with compositions ($\binom{n - 1}{k - 1}$): "order ignored" changes the universe, not just the count.
- $S(n, k)$ vs onto functions: the factor $k!$ is the labelling of blocks.
- Quoting EKR/Sperner without their hypotheses ($n \geq 2k$; antichain, not intersecting).
:::
