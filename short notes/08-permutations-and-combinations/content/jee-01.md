---
id: jee-01
part: jee
title: "Permutations & Combinations — The Two Rules, the Complement, and What Counting Means"
---

## Counting is matching, construction is multiplication

To count a set $X$ means to find $\left|X\right|$. Two master moves solve almost everything: **(A) construct** each object by a sequence of choices (multiply), **(B) match up** $X$ bijectively with a set already counted (inherit its size). Every formula in this chapter is one of these, packaged.

:::key title="Product rule and sum rule (with their exact hypotheses)"
**Product rule:** a task in successive steps, step $i$ offering $n_{i}$ choices *regardless of earlier choices*, has $n_{1}n_{2}\cdots n_{k}$ outcomes. The independence clause is the hypothesis: "5 choices then 4 choices" for choosing 2 people from 5 counts **ordered** pairs (20), because $\{A, B\}$ is built twice.

**Sum rule:** if $X$ is split into disjoint, exhaustive cases, $\left|X\right|$ is the sum of the case counts. Cases must be *every case counted once, every object in some case*.
:::

:::key title="Complement: negatives are rigid, positives are flexible"
"At least one" / "no" / "not all" $\Rightarrow$ count the complement and subtract from the total. Committees of 5 from 12 men and 8 women with at least one woman: $\binom{20}{5} - \binom{12}{5} = 15504 - 792 = 14712$, instead of five direct cases. Strings of length 4 over $\{0, 1, 2, 3, 4\}$ containing a 0: $5^{4} - 4^{4} = 625 - 256 = 369$.
:::

:::example title="Worked — cases where steps interact"
4-digit numbers with distinct digits divisible by 5: split on the units digit (the thousands digit's options depend on it). Units 0: $9 \cdot 8 \cdot 7 = 504$. Units 5: $8 \cdot 8 \cdot 7 = 448$. Total $952$. Splitting is the cure when independence fails in exactly one place.
:::

:::intuition title="Bijections you already own"
Subsets of an $n$-set $\leftrightarrow$ binary strings of length $n$ (in/out per element): $2^{n}$ subsets. Increasing functions $f$ with $f(1) < f(2) < f(3)$ into $\{1, \ldots, 5\}$ $\leftrightarrow$ 3-subsets: $\binom{5}{3} = 10$. Pairs $A \subseteq B$ of subsets: each element has 3 states (in neither, in $B$ only, in both): $3^{n}$. Monotone/ordered-with-condition almost always means: find the unordered object it encodes.
:::

:::warn title="The three sins of counting (check every answer against them)"
1. **Overcounting:** one object built by two choice paths. 2. **Undercounting:** cases not exhaustive. 3. **Broken independence:** multiplying counts that are not fixed per step. Cure for all three: verify a small case by listing. Also ask: objects labelled or unlabelled? order matters or not? is the answer a plausible size (never more than the total pool)?
:::

:::assume title="Standing conventions"
$n, r$ are non-negative integers with $0 \leq r \leq n$ unless stated; $\binom{n}{r} = 0$ if $r < 0$ or $r > n$ (a useful convention in sums); $0! = 1$ (exactly one empty arrangement). "Arrangements" are ordered; "selections/committees" are unordered.
:::
