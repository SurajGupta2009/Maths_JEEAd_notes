---
id: jee-01
part: jee
title: "Sets — Language, Representation, Subsets"
---

## What a set is (and what it is not)

A **set** is a *well-defined collection of distinct objects*. Well-defined means membership is decidable: for any candidate $x$, the statement $x \in A$ is either true or false, never a matter of taste. The objects are called **elements** (or members). Distinct means a set lists each element once: $\{1, 1, 2\}$ *means* $\{1, 2\}$.

**Notation.** Capital letters ($A, B, U$) name sets, small letters ($x, y, a$) name elements. $x \in A$ reads "$x$ is an element of $A$"; $x \notin A$ is its negation. The **cardinality** $n(A)$ (also written $|A|$) is the number of elements; it may be finite or infinite.

### Three ways to write a set

- **Roster (listing):** $A = \{1, 2, 3\}$ — order and repetition do not matter.
- **Set-builder:** $B = \{x : x \text{ is an even prime}\} = \{2\}$. Read $\{x : P(x)\}$ as "the set of all $x$ such that $P(x)$ holds".
- **Interval (only for subsets of $\mathbb{R}$, order matters):** $(a,b)$ open, $[a,b]$ closed, $[a,b)$ or $(a,b]$ half-open, and rays $[a,\infty)$, $(-\infty, b)$. Infinity is never an element: always round brackets at $\pm\infty$.

:::assume
Braces $\{\}$ always describe a set. $\in$ links an **element** to a set; $\subseteq$ links a **set** to a set. $1 \in \{1,2\}$ but $\{1\} \subseteq \{1,2\}$. Never mix the two levels: "$1 \subseteq \{1,2\}$" is a type error, not a false inequality. All sets in a discussion are assumed to live inside a fixed **universal set** $U$ once complements appear.
:::

## Kinds of sets

- **Empty (null) set** $\varnothing$: the set with no elements. There is exactly **one** empty set (uniqueness: any two sets with no elements are equal by definition of equality). $n(\varnothing)=0$.
- **Singleton** $\{a\}$: one element. Note $\{a\} \ne a$ — the set and its element are different kinds of objects.
- **Finite / infinite:** $n(A)$ is a natural number vs not. $n(\mathbb{N})$ is infinite (countably so; no JEE counting applies).
- **Equal sets:** $A = B \Leftrightarrow$ every element of $A$ is in $B$ and vice versa. The standard proof is **double inclusion**: prove $A \subseteq B$ and $B \subseteq A$ separately.
- **Equivalent sets:** same cardinality only. $\{1,2\}$ and $\{3,4\}$ are equivalent but not equal. Do not say "equivalent" when you mean "equal".

## Subsets and the power set

$A \subseteq B$ iff every element of $A$ is an element of $B$. We write $A \subset B$ (or $A \subsetneq B$) when $A \subseteq B$ with $A \ne B$ (**proper** subset). Vacuous truth: $\varnothing \subseteq A$ for every $A$ — there is no element of $\varnothing$ that could fail the test.

:::derive title="Why $|\mathcal{P}(A)| = 2^{n}$"
Build a subset $S \subseteq A$ by deciding, for each of the $n$ elements of $A$ in turn, "in $S$" or "not in $S$". That is $2$ choices per element, independently, so $2 \times 2 \times \cdots \times 2 = 2^{n}$ subsets. Small case $A = \{1,2\}$: the four decisions list $\varnothing, \{1\}, \{2\}, \{1,2\}$. Same reasoning: subsets with exactly $k$ elements number $\binom{n}{k}$, so $\sum_{k=0}^{n}\binom{n}{k} = 2^{n}$ (choosing each element is a subset of some size $k$).
:::

:::key
The **power set** $\mathcal{P}(A)$ is the set of all subsets of $A$. Then $|\mathcal{P}(A)| = 2^{n(A)}$ and, for finite $A$: number of subsets $= 2^{n}$, number of proper subsets $= 2^{n} - 1$, number of non-empty subsets $= 2^{n} - 1$, number of non-empty proper subsets $= 2^{n} - 2$. Also $A \in \mathcal{P}(A)$ (as an element) and $A \subseteq A$ (as a subset) — two different statements, both true.
:::

:::diagram
{
  "type": "numberline",
  "range": [-7, 7],
  "title": "Interval conventions on the real line (filled dot = included)",
  "xlabel": "real line x",
  "items": [
    {"kind": "interval", "a": -5, "b": -2, "closed_a": true, "closed_b": false, "label": "[a, b) : a included, b excluded", "y": 0.35, "color": "#0F766E"},
    {"kind": "interval", "a": 0, "b": 3.5, "closed_a": true, "closed_b": true, "label": "[c, d] both included", "y": 0.75, "color": "#16295C"},
    {"kind": "points", "xs": [5.5], "label": "singleton {5.5}", "y": 0.35, "color": "#B8860B"}
  ]
}
:::

## The four confusions that cost marks

:::warn
1. **$\varnothing$ vs $\{0\}$ vs $\{\varnothing\}$.** $\varnothing$ has 0 elements. $\{0\}$ has one element (the number 0). $\{\varnothing\}$ has one element (the empty set). So $n(\{\varnothing\}) = 1$, and $\varnothing \in \{\varnothing\}$ is true while $\varnothing \in \{0\}$ is false. The set $\{\varnothing, \{0\}\}$ has exactly two elements.
2. **$\in$ vs $\subseteq$.** $\varnothing \subseteq \{0\}$ is true (subset), $\varnothing \in \{0\}$ is false (not an element). $0 \in \{0\}$ true, $\{0\} \in \{0\}$ false.
3. **Equal vs equivalent.** $\{1,2\}$ and $\{2,1\}$ are equal; $\{1,2\}$ and $\{3,4\}$ are only equivalent.
4. **Two empty sets in one problem** (e.g. $A \cap B = \varnothing$ vs $A \setminus B = \varnothing$) mean different things: the first says $A, B$ are disjoint, the second says $A \subseteq B$.
:::

:::example
**Worked.** $A = \{x \in \mathbb{Z} : |x| \leq 2\}$ and $B = \{x \in \mathbb{Z} : 1 \leq x \leq 3\}$. Then $A = \{-2,-1,0,1,2\}$, $B = \{1,2,3\}$, $A \cap B = \{1,2\}$, $A \cup B = \{-2,-1,0,1,2,3\}$, $n(A \cup B) = 7$. **Check:** the two listed sets share exactly $1,2$, and every integer appearing in either list appears once in the union. Notice $|x| \leq 2$ includes $x = -2$ — boundary cases always flip signs when absolute values appear.
:::
