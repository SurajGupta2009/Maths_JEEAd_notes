---
id: jee-02
part: jee
title: Addition Rule, Counting, Conditional Probability
---

## Overlap correction

For events $A,B$, disjointly split their union to obtain
$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$
For disjoint events the intersection is zero; for mutually exclusive events with positive probabilities, they cannot be independent.

:::example title="Heart or king"
In a 52-card deck, 13 hearts and 4 kings overlap at the king of hearts: $P(H\cup K)=(13+4-1)/52=4/13$.
:::

## Counting under a probability model

When all selections are equally likely, count using permutations if order matters, combinations if not, then divide. For a committee of size $r$ from $N$, total outcomes $\binom{N}{r}$. “At least one” often uses a complement count.

:::example title="Committee has a woman"
Choose 3 from 5 men and 4 women. Probability at least one woman is $1-\binom{5}{3}/\binom{9}{3}=37/42$. The event and total use the same uniformly selected committee model.
:::

## Conditional probability shrinks the space

For $P(B)>0$:
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}.$$
Multiplication rule: $P(A\cap B)=P(A\mid B)P(B)$. Order matters: $P(A\mid B)$ generally differs from $P(B\mid A)$.

:::example title="Even die, then six"
Given an even result, the reduced space is {2,4,6}. Exactly one outcome is 6, so $P(6\mid even)=1/3$.
:::

:::warn title="Without replacement"
The second draw's probability changes after the first. Use conditional probability; do not multiply the original marginal probabilities as if independent.
:::
