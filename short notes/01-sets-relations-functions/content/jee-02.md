---
id: jee-02
part: jee
title: "Operations on Sets — Union, Intersection, Difference, De Morgan"
---

## The five operations

Fix a universal set $U$; all complements are relative to $U$.

- **Union:** $A \cup B = \{x : x \in A \text{ or } x \in B\}$ — "or" is inclusive: $A \cap B$ is counted in.
- **Intersection:** $A \cap B = \{x : x \in A \text{ and } x \in B\}$. Disjoint means $A \cap B = \varnothing$.
- **Difference:** $A \setminus B = \{x : x \in A \text{ and } x \notin B\} = A \cap B'$ — "in $A$, but not in $B$".
- **Complement:** $A' = U \setminus A = \{x \in U : x \notin A\}$. Without $U$ there is no complement — always fix $U$ first.
- **Symmetric difference:** $A \,\Delta\, B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$ — elements in **exactly one** of the two.

:::diagram
{
  "type": "venn2",
  "shade": ["AxB_sym"],
  "title": "Shaded: A Δ B, the elements belonging to exactly one set",
  "labels": {"A Δ B": "Aonly"},
  "A": "A", "B": "B",
  "universe": "All sets are understood inside a fixed universe U"
}
:::

## The algebraic laws (all provable by element-chasing)

:::key
Commutative: $A \cup B = B \cup A$, $A \cap B = B \cap A$, $A \,\Delta\, B = B \,\Delta\, A$. Associative: $(A \cup B) \cup C = A \cup (B \cup C)$ (same for $\cap$, $\Delta$). Distributive: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ and $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$. Idempotent: $A \cup A = A = A \cap A$. Complement: $A \cup A' = U$, $A \cap A' = \varnothing$, $(A')' = A$. Absorption: $A \cup (A \cap B) = A$, $A \cap (A \cup B) = A$. Difference: $A \setminus B = A \cap B'$, $A \setminus A = \varnothing$.
:::

:::derive title="De Morgan's laws"
$(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$. Chase elements: $x \in (A \cup B)'$ means "$x \notin A \cup B$", i.e. "$x \notin A$ **and** $x \notin B$" (negation flips "or" to "and"), i.e. $x \in A'$ and $x \in B'$, i.e. $x \in A' \cap B'$. Swapping $\cup, \cap$ and negating again gives the second law. The same argument with $n$ sets gives: complement of a union is the intersection of complements, and vice versa — "keep the elements outside **all** of them" $= \bigcap A_i'$, "outside at least one" $= \bigcup A_i'$.
:::

:::intuition
Read the operations as filters on a Venn diagram. $\cup$ = at least one condition true. $\cap$ = all conditions true. $\setminus$ = first true, second false. $\Delta$ = odd number of memberships. Every identity becomes "the shaded region is the same picture on both sides" — a genuine proof method once you say which region each element lands in.
:::

## Counting with a Venn diagram

:::derive title="Inclusion–exclusion"
Partition $A \cup B$ into the three disjoint pieces $A \setminus B$, $A \cap B$, $B \setminus A$. Then $n(A \cup B) = n(A) + n(B) - n(A \cap B)$, because adding $n(A) + n(B)$ counts the overlap twice. For three sets (same idea, seven disjoint regions):
$$n(A \cup B \cup C) = \sum n(A) - \sum n(A \cap B) + n(A \cap B \cap C)$$
where $\sum n(A)$ sums the three singletons and $\sum n(A \cap B)$ the three pairwise intersections.
:::

:::diagram
{
  "type": "venn3",
  "title": "Seven disjoint regions; n(A∪B∪C) = sum of all seven counts",
  "labels": {"Aonly": "a", "Bonly": "b", "Conly": "c", "ABn": "d", "ACn": "e", "BCn": "f", "ABCn": "g"}
}
:::

:::example
**Standard application.** Of 60 students, 25 play cricket, 20 football, 15 both. How many play neither? $n(C \cup F) = 25 + 20 - 15 = 30$, so $n((C \cup F)') = 60 - 30 = 30$ students play neither. **Check:** the 15 who play both are inside both counts; subtracting once leaves each student counted exactly once. Boundary habit: "neither" is a *complement*, so the total 60 must be the universe.
:::

:::warn
- A complement is meaningless without a stated universe — "the set of students not playing cricket" lives inside the class, not inside all humans.
- $A \setminus B = \varnothing$ means $A \subseteq B$, **not** $A = B$.
- $(A \setminus B) \cup B = A \cup B$ in general, not $A$. The reverse difference $B \setminus A$ is a different animal.
- $\Delta$ is not associative with $\cup$ mixing: parentheses matter when three operations combine.
- $n(A \cup B) = n(A) + n(B)$ holds **only** when $A \cap B = \varnothing$. Using it without checking disjointness is the classic counting error.
:::
