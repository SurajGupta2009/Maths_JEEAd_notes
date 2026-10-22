---
id: jee-07
part: jee
title: "Pigeonhole, Recurrence Counting, and the Chapter Recap"
---

## Existence by averaging

:::key title="Pigeonhole principle (the art is the boxes)"
$n + 1$ objects in $n$ boxes $\Rightarrow$ some box has $\geq 2$. The theorem is trivial; every application is the choice of the box map so that "same box" gives the conclusion.

**Odd-part box:** from any $n + 1$ integers in $\{1, \ldots, 2n\}$, two share the same odd part in $x = 2^{a} \cdot m$ ($m$ odd) — only $n$ odd parts exist — so one divides the other. Sharp: $\{n + 1, \ldots, 2n\}$ has no such pair.

**Geometry box:** 5 points in a unit square: quarter it into 4 subsquares; two points share one, at distance $\leq \frac{\sqrt{2}}{2}$ (its diagonal).
:::

## Counting by last-step decomposition

:::key title="Recurrences: split by the last block"
If objects of size $n$ end with one of a few block types, leaving a smaller instance of the same problem, the counts satisfy a recurrence. $2 \times n$ domino tilings: ends vertical ($a_{n - 1}$) or two horizontal ($a_{n - 2}$): $a_{n} = a_{n - 1} + a_{n - 2}$, $a_{0} = a_{1} = 1$, so $a_{n} = F_{n + 1}$ (tilings of $2 \times 10$: $89$). Binary strings with no consecutive 1s and subsets with no two consecutive give the same recurrence ($F_{n + 2}$). Staircase with steps 1–2: $a_{10} = 89$; steps 1–3: tribonacci. Guard the base cases — a correct recurrence with wrong seeds is a wrong answer.
:::

:::key title="Recap — the chapter on one card"
Product/sum/complement; bijection = same count. $P(n, r) = \frac{n!}{(n - r)!}$; identical objects $\frac{n!}{\prod n_{i}!}$; circular $(n - 1)!$ (necklace $\frac{(n - 1)!}{2}$ distinct beads). Bundle / gap $m!\binom{m + 1}{k}k!$ / relative order $\frac{n!}{k!}$. $\binom{n}{r} = \frac{n!}{r!(n - r)!}$; Pascal; hockey-stick. Stars and bars $\binom{n + k - 1}{k - 1}$ / positive $\binom{n - 1}{k - 1}$; compositions $2^{n - 1}$. IE alternating sum; $D_{n} = n!\sum \frac{(-1)^{k}}{k!} \approx n!/e$; onto $= \sum (-1)^{j}\binom{k}{j}(k - j)^{n}$. Pigeonhole: design the boxes. Recurrence: split by last block, mind the seeds.
:::

:::warn title="Pre-submission checklist"
Order matters? Labels? Identical objects — is my division by symmetry exact (equal fibres)? Cases disjoint and exhaustive? Did "at least" get complemented? Bounds handled by shift/IE, with negative-top terms set to 0? Small case listed by hand? Answer size sane against the total pool?
:::

:::intuition title="Forward map"
Binomial identities are this chapter counted twice (chapter 9); lattice paths and Catalan, Burnside–Pólya, partitions and Stirling numbers, intersecting families: Part II here. The through-line never changes: *construct, split, or match up*.
:::
