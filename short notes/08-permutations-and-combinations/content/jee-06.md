---
id: jee-06
part: jee
title: "Inclusion–Exclusion and Derangements — Counting 'None of the Bad Things'"
---

## The principle

:::derive title="Inclusion–exclusion, proved by tracking one element"
For bad events $A_{1}, \ldots, A_{n}$ in a universe $X$:

$$\left|X \setminus \bigcup A_{i}\right| = \sum_{S \subseteq \{1..n\}} (-1)^{\left|S\right|} \left|\bigcap_{i \in S} A_{i}\right|$$

Proof: an element lying in exactly $t \geq 1$ of the sets is counted $\sum_{j=0}^{t} (-1)^{j}\binom{t}{j} = (1 - 1)^{t} = 0$ times; an element in none is counted once. **Universal recipe:** define bad events; compute the intersection size for a generic set of $k$ specified events (usually $\binom{n}{k} \times$ something free); write the alternating sum.

Integers 1–1000 divisible by 2, 3 or 5: $500 + 333 + 200 - 166 - 100 - 66 + 33 = 734$ (so divisible by none: $266$).
:::

:::key title="Derangements: the flagship application"
$D_{n}$ = permutations of $\{1..n\}$ with **no** fixed point. With $A_{i}$ = "$i$ is fixed", a specified set of $k$ fixed points leaves $(n - k)!$ free permutations:

$$D_{n} = \sum_{k=0}^{n} (-1)^{k} \binom{n}{k} (n - k)! = n! \sum_{k=0}^{n} \frac{(-1)^{k}}{k!}$$

$D_{0} = 1, D_{1} = 0, D_{2} = 1, D_{3} = 2, D_{4} = 9, D_{5} = 44, D_{6} = 265$. Also $D_{n} = (n - 1)(D_{n - 1} + D_{n - 2})$ (where does element 1 go? then whether its partner swaps back), and $D_{n}$ is the **nearest integer to $n!/e$** since the tail beyond $n$ is $< \frac{1}{n + 1} < \frac{1}{2}$.

Exactly $k$ fixed points: $\binom{n}{k} D_{n - k}$ (for $n = 5$, exactly two correct letters: $\binom{5}{2} \cdot 2 = 20$; check: $44 + 20 + 45 + 10 + 0 + 1 = 120 = 5!$ ✓).
:::

:::example title="Worked — onto functions (IE in disguise)"
Onto functions from a 5-set to a 3-set: total $3^{5}$ minus those missing a value: $3^{5} - \binom{3}{1} 2^{5} + \binom{3}{2} 1^{5} = 243 - 96 + 3 = 150$. Hands of 6 cards containing all four suits: $\binom{52}{6} - 4\binom{39}{6} + 6\binom{26}{6} - 4\binom{13}{6} = 8682544$.
:::

:::warn title="Common traps — inclusion–exclusion"
- Sign alternation starting wrong: the empty intersection (whole universe) carries $+$.
- Intersection sizes computed for *exactly* $k$ events instead of *at least these* $k$ (IE wants the latter).
- Bounded stars-and-bars terms with negative top: $\binom{m}{k - 1}$ for a negative-sum equation is **0** — terminate the sum, never evaluate.
- Derangement problems with only *some* positions forbidden: restrict the event set (then it is partial derangement / rook theory, Part II flavour).
:::
