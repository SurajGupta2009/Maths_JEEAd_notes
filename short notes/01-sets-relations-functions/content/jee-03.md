---
id: jee-03
part: jee
title: "Cartesian Products & Relations — Definitions, Types, Counting"
---

## Cartesian product of sets

An **ordered pair** $(a,b)$ remembers order: $(a,b) = (c,d) \Leftrightarrow a = c \text{ and } b = d$ (this is the working convention; the formal set-theoretic build $(a,b) := \{\{a\},\{a,b\}\}$ is a background fact, not an exam tool).

:::key
$A \times B = \{(a,b) : a \in A,\ b \in B\}$. Then $n(A \times B) = n(A) \cdot n(B)$ — product rule: choose the first coordinate ($n(A)$ ways) then the second ($n(B)$ ways), independently. $A \times B = \varnothing \Leftrightarrow A = \varnothing$ or $B = \varnothing$. $A \times B \ne B \times A$ in general (they are equal only in trivial cases such as $A = B$ or one empty).
:::

Distributive-style facts (all set identities carry over with $\times$):

- $A \times (B \cup C) = (A \times B) \cup (A \times C)$ and $A \times (B \cap C) = (A \times B) \cap (A \times C)$.
- $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$ — intersect **coordinate-wise**.
- $A \times (B \setminus C) = (A \times B) \setminus (A \times C)$.
- $A \times B \subseteq C \times D \Leftrightarrow (A \subseteq C \text{ and } B \subseteq D)$ when all four are non-empty.

:::warn
- $(A \times B) \times C \ne A \times (B \times C)$ as sets: the elements are $((a,b),c)$ vs $(a,(b,c))$. Only the *elements* are in natural bijection. JEE counts pairs, so keep parentheses as written.
- $A \times B$ is a **set of pairs**, not a number: $|A \times B|$ is the number; $A \times B$ itself contains points such as $(1,4)$.
- $A \times A$ is the plane grid of a set with itself; $n(A \times A) = n(A)^2$, which is why an $n$-element set has $n^2$ ordered pairs — memorise this number, you will use it constantly.
:::

## Relations

A **relation** $R$ from $A$ to $B$ is any subset $R \subseteq A \times B$. If $B = A$ we say "$R$ is a relation on $A$". For $(a,b) \in R$ we often write $a\,R\,b$.

- **Domain** $= \{a \in A : \exists b,\ (a,b) \in R\}$ (first coordinates that actually appear).
- **Range** $= \{b \in B : \exists a,\ (a,b) \in R\}$.
- **Codomain** $= B$, fixed by declaration — range is a subset of the codomain, not necessarily equal to it.

Representations: roster form $R = \{(1,1),(1,2),(2,3),(3,3)\}$; rule form $\{(x,y) : y = x^2\}$; arrow diagrams; the $0$-$1$ matrix ($m_{ij} = 1$ iff $(a_i, b_j) \in R$); graphs for relations on $\mathbb{R}$.

:::diagram
{
  "type": "mapping",
  "A": ["1", "2", "3"],
  "B": ["1", "2", "3"],
  "arrows": [["1", "1"], ["1", "2"], ["2", "3"], ["3", "3"]],
  "Aname": "A (domain side)",
  "Bname": "B (codomain side)",
  "title": "R = {(1,1),(1,2),(2,3),(3,3)}: a general relation — 1 sends two arrows, so R is not a function"
}
:::

## Three properties of relations on a set $A$

- **Reflexive:** $a\,R\,a$ for **every** $a \in A$. One missing diagonal pair kills it.
- **Symmetric:** $a\,R\,b \Rightarrow b\,R\,a$ for all $a,b$.
- **Transitive:** $a\,R\,b$ and $b\,R\,c \Rightarrow a\,R\,c$.

Standard test cases on $\mathbb{Z}^+$ or $\mathbb{R}$: "$\leq$" is reflexive + transitive, **not** symmetric. "$\ne$" is symmetric, **not** reflexive, **not** transitive ($1 \ne 2$, $2 \ne 1$ but $1 \ne 1$ is false — the transitive conclusion fails). "divides" on $\mathbb{Z}^+$: reflexive + transitive, not symmetric ($2 \mid 4$ but $4 \nmid 2$). Parallelism of lines in a plane (with every line parallel to itself) is an equivalence relation.

:::derive title="How many relations exist?"
A relation on $A$ is any subset of $A \times A$, and $n(A \times A) = n^2$ for $n = n(A)$. Each of the $n^2$ pairs is independently in or out of $R$: total relations $= 2^{n^2}$. Reflexive relations must contain all $n$ diagonal pairs $(a,a)$ and are free on the other $n^2 - n$ pairs: $2^{n^{2}-n}$. Small case $n = 2$, $A = \{1,2\}$: 4 pairs, $2^4 = 16$ relations; reflexive ones must contain $(1,1),(2,2)$ and are choices on $(1,2),(2,1)$: $2^2 = 4$ — list them: $\{(1,1),(2,2)\}$, plus each of $(1,2)$ and/or $(2,1)$.
:::

:::example
**Worked.** $A = \{1,2,3\}$, $B = \{4,5\}$. Then $A \times B$ has $6$ pairs, so there are $2^{6} = 64$ relations from $A$ to $B$. Let $R = \{(x,y) \in A \times B : y - x \geq 3\}$. Check all six pairs: $(1,4): 4-1 = 3\ \geq 3$ ✓; $(1,5): 4 \geq 3$ ✓; $(2,4): 2 \geq 3$ ✗; $(2,5): 3 \geq 3$ ✓; $(3,4): 1 \geq 3$ ✗; $(3,5): 2 \geq 3$ ✗. So $R = \{(1,4),(1,5),(2,5)\}$, domain $= \{1,2\}$, range $= \{4,5\}$, codomain $= \{4,5\}$. **Check:** the boundary $y - x = 3$ is included ($\geq$, not $>$), which is what makes $(1,4)$ and $(2,5)$ members — boundary conditions decide membership more often than bulk algebra.
:::
