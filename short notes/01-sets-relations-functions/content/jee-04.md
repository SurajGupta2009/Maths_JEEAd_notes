---
id: jee-04
part: jee
title: "Equivalence Relations & Partitions — with JEE-style Counting"
---

## Equivalence relation

A relation $R$ on $A$ is an **equivalence relation** if it is reflexive, symmetric **and** transitive. The model example is congruence: for fixed $n \geq 2$, define $x\,R\,y \Leftrightarrow n \mid (x - y)$ ("$x \equiv y \ (\mathrm{mod}\ n)$").

:::derive title="Congruence mod n is an equivalence relation on Z"
Reflexive: $x - x = 0$ and $n \mid 0$. Symmetric: if $n \mid (x-y)$ then $x - y = nk$, so $y - x = n(-k)$ and $n \mid (y-x)$. Transitive: $n \mid (x-y)$ and $n \mid (y-z)$ give $x-y = nk$, $y-z = nl$, so $x-z = n(k+l)$. Each step is one divisibility fact — nothing clever, which is exactly why this template reappears in exams.
:::

## Equivalence classes and partitions

For $a \in A$ the **class** $[a] = \{x \in A : x\,R\,a\}$. Fundamental facts: $a \in [a]$ (reflexivity); $[a] = [b] \Leftrightarrow a\,R\,b$; distinct classes are disjoint; the classes cover $A$. So the classes form a **partition** of $A$: a family of non-empty, pairwise disjoint blocks whose union is $A$.

:::key
Equivalence relations on $A$ and partitions of $A$ are the same data in two languages. $a\,R\,b \Leftrightarrow$ "$a$ and $b$ are in the same block". Counting either one gives the **Bell numbers**: $B_1 = 1$, $B_2 = 2$, $B_3 = 5$, $B_4 = 15$, $B_5 = 52$ — the number of equivalence relations on an $n$-element set. For $A = \{1,2,3\}$ the five partitions are: $\{\{1,2,3\}\}$; $\{\{1\},\{2,3\}\}$, $\{\{2\},\{1,3\}\}$, $\{\{3\},\{1,2\}\}$; $\{\{1\},\{2\},\{3\}\}$.
:::

:::diagram
{
  "type": "blocks",
  "title": "Partition induced by congruence mod 3 on {1,...,6}: three classes, one block each",
  "groups": [
    {"label": "[0]", "members": ["3", "6"]},
    {"label": "[1]", "members": ["1", "4"]},
    {"label": "[2]", "members": ["2", "5"]}
  ]
}
:::

:::example
**Worked.** On $\mathbb{Z}$ let $x\,R\,y \Leftrightarrow x + y$ is even. Symmetric is immediate ($x+y = y+x$); reflexive: $x + x = 2x$ even; transitive: if $x+y$ and $y+z$ are even, then $(x+y) - (y+z) = x - z$ is even and $x + z = (x - z) + 2z$ is even. Classes: even numbers $[0] = \{\dots,-2,0,2,\dots\}$ and odds $[1] = \{\dots,-1,1,3,\dots\}$. **Check:** $[2] = [0]$ since $2 + 0$ is even — classes are named by any member, not only by the smallest. Note this $R$ is the same equivalence as $x \equiv y \ (\mathrm{mod}\ 2)$.
:::

## The traps that generate exam questions

:::warn
1. **Symmetric + transitive does not imply reflexive.** On $A = \{1,2,3\}$ the relation $R = \{(1,1),(1,2),(2,1),(2,2)\}$ is symmetric and transitive but not reflexive ($3 \notin$ any pair with itself).
2. **The empty relation on a non-empty $A$** is symmetric and transitive (vacuously) but not reflexive. The **universal relation** $A \times A$ is an equivalence relation (one big block). The **identity relation** $\{(a,a) : a \in A\}$ is also one (all singleton blocks).
3. **To prove "equivalence"** check the three axioms separately on arbitrary elements; a single counterexample kills any axiom. Many partial proofs assume transitivity "by symmetry" — never valid.
4. **Class names:** $[1] = [4]$ under mod 3; the partition blocks are *sets of elements*, the labels are cosmetic.
:::

## How JEE counts these (derivable with the syllabus)

:::derive title="Reflexive and symmetric relations on an n-set"
Reflexive + symmetric: the $n$ diagonal pairs are forced in; off-diagonal, $(a,b)$ and $(b,a)$ must be chosen *together* — in or out as a pair. There are $\frac{n(n-1)}{2}$ such unordered pairs, so the count is $2^{n(n-1)/2}$. Small case $n = 3$: $2^{3} = 8$ relations — forced $\{(1,1),(2,2),(3,3)\}$ plus any subset of $\{(1,2),(2,1)\}, \{(1,3),(3,1)\}, \{(2,3),(3,2)\}$, listed as $2^3 = 8$ choices. Similarly: reflexive alone $= 2^{n^2-n}$, symmetric alone $= 2^{n(n+1)/2}$ (diagonal free + pairs together), antisymmetric $= 2^{n} \cdot 3^{n(n-1)/2}$ (diagonal free; each off-diagonal pair: neither, only $(a,b)$, or only $(b,a)$).
:::

:::app
**Standard application.** Number of relations on $\{1,2,3\}$ that are reflexive and symmetric $= 2^{3} = 8$; that are equivalence relations $= B_3 = 5$; that are reflexive $= 2^{6} = 64$. The examiner tests whether you separate the three axioms' constraints — diagonal forced, pairs coupled, or fully free.
:::
