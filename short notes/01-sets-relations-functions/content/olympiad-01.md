---
id: oly-01
part: olympiad
title: "Counting Relations & Functions — Rigorous Catalogue"
---

## Status of this sheet

Part I derived total, reflexive, symmetric and reflexive+symmetric counts with direct pair analysis. This sheet completes the catalogue (antisymmetric, equivalence/Bell, surjections by inclusion–exclusion) and shows the small-case listings an IOQM/RMO solution must carry. All counts are **models built from the Part I supply list** (product rule, complements, inclusion–exclusion on sets) — the *technique* is exam-derivable even where the topic is listed as an extension.

## The catalogue for $|A| = n$

:::key
On an $n$-element set: relations $= 2^{n^{2}}$; reflexive $= 2^{n^{2}-n}$; symmetric $= 2^{n(n+1)/2}$; antisymmetric $= 2^{n} \cdot 3^{n(n-1)/2}$; reflexive+symmetric $= 2^{n(n-1)/2}$; reflexive+transitive $=$ number of "preorder with fixed diagonal" (no simple closed form — casework); equivalence relations $= B_n$ (Bell): $1, 2, 5, 15, 52$ for $n = 1..5$. Functions $A \to B$ with $|B| = m$: $m^{n}$; injective: $\frac{m!}{(m-n)!}$ if $n \leq m$ else $0$; surjective: $n! \, S(n,m)$ with $S$ the Stirling number $= \sum_{i=0}^{m} (-1)^{i}\binom{m}{i}(m-i)^{n}$.
:::

:::derive title="Surjections by inclusion-exclusion"
$f : A \to B$ surjective iff no element of $B$ is missed. Let $U$ = all $m^{n}$ functions and $E_b$ = functions missing the value $b$. We want $|U \setminus \bigcup_{b} E_b|$. Now $|E_b| = (m-1)^{n}$ (values chosen from the rest), $|E_{b} \cap E_{c}| = (m-2)^{n}$, and so on, so inclusion–exclusion gives $\sum_{i=0}^{m} (-1)^{i}\binom{m}{i}(m-i)^{n}$. Small case $n = 3, m = 2$: $2^{3} - 2 \cdot 1^{3} = 6$ ✓ matches the 6 onto functions $\{1,2,3\} \to \{a,b\}$ found by cases in Part I. Sanity: $m > n$ gives 0 (e.g. $n=2, m=3$: $9 - 3\cdot4 + 3\cdot1 = 0$).
:::

:::example
**Worked.** Onto functions $\{1,2,3,4\} \to \{a,b,c\}$: $3^{4} - \binom{3}{1}2^{4} + \binom{3}{2}1^{4} - \binom{3}{3}0^{4} = 81 - 48 + 3 = 36$. Cross-check with Stirling: $S(4,3) = 6$ (partitions of 4 elements into 3 blocks: one block of 2 and two singletons, $\binom{4}{2} = 6$), then order the blocks onto $a,b,c$: $6 \cdot 3! = 36$ ✓. Two independent methods agreeing is the standard olympiad "check" line.
:::

## Bell numbers by listings (do this in solutions)

For $A = \{1,2,3,4\}$, $B_4 = 15$ partitions: $1$ block ($1$ way), $2$ blocks: choose the block containing 1 ($S(4,2) = 7$), $3$ blocks ($S(4,3) = 6$), $4$ singletons ($1$). Total $1 + 7 + 6 + 1 = 15$ ✓. General recurrence (extension): $B_{n+1} = \sum_{k=0}^{n}\binom{n}{k}B_{k}$ — element $n+1$ joins a block after $k$ others are already placed... more cleanly: $B_{n+1} = \sum_{k=0}^{n} \binom{n}{k} B_{n-k}$: choose which elements share the block of $n+1$.

:::diagram
{
  "type": "blocks",
  "title": "The 5 equivalence relations on {1,2,3} as partitions (Bell B_3 = 5)",
  "groups": [
    {"label": "1 block", "members": ["{1,2,3}"]},
    {"label": "2 blocks", "members": ["{1}|{2,3}", "{2}|{1,3}", "{3}|{1,2}"]},
    {"label": "3 blocks", "members": ["{1}|{2}|{3}"]}
  ]
}
:::

:::warn
- **Labelled vs unlabelled.** $\{\{1,2\},\{3,4\}\}$ and $\{\{1,3\},\{2,4\}\}$ are different partitions of a labelled set; counting unlabeled block *shapes* is a different (smaller) problem. State which one you count.
- Antisymmetric count $2^{n}3^{n(n-1)/2}$: each off-diagonal unordered pair $\{a,b\}$ allows exactly 3 states — neither direction, only $a \to b$, only $b \to a$ — never 4 (both directions are banned).
- Inclusion–exclusion signs alternate. Boundary convention: a function on an empty domain is unique (the empty function), so $m^{0} = 1$ for every $m$, including $0^{0} = 1$ — state the convention whenever $n = 0$ appears.
- Surjections need $n \geq m$; injections need $n \leq m$. A formula that spits out a nonzero answer violating these is being used wrong.
:::

:::assume
Counts assume **finite** sets and labelled elements throughout. $S(n,m)$ here means Stirling numbers of the second kind (onto functions divided by $m!$); the notation is Part II vocabulary, but every *numerical* claim above is checkable by listing for $n, m \leq 4$ — an olympiad write-up should always include one such listing.
:::
