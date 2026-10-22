---
id: jee-03
part: jee
title: "Circular Permutations and Restriction Methods — Bundle, Gap, Relative Order"
---

## Around a table

:::key title="Circular permutations: (n − 1)!"
$n$ distinct people around a round table, seatings identified up to rotation: $(n - 1)!$. Two proofs: anchor one person as reference and arrange the rest linearly; or divide $n!$ by the $n$ rotations (every orbit has size exactly $n$ for distinct people). If flips are also identified (necklaces of **distinct** beads, $n \geq 3$): $\frac{(n - 1)!}{2}$.

Two specified people adjacent (round table): bundle, $2(n - 2)!$; not adjacent: $(n - 1)! - 2(n - 2)! = (n - 3)(n - 2)!$. For 10 people with A, B non-adjacent: $9! - 2 \cdot 8! = 362880 - 80640 = 282240$.
:::

## The three restriction methods (linear arrangements)

:::key title="Bundle, gap, relative order — pick by the wording"
- **"Together/consecutive":** bundle the $k$ objects into one super-object ($k!$ internal orders if distinct), arrange the $n - k + 1$ objects.
- **"No two adjacent":** gap method. Arrange the $m$ ordinary objects ($m!$), creating $m + 1$ gaps; place the $k$ special objects into **distinct** gaps: $\binom{m + 1}{k}$ choices and $k!$ orders: total $m! \binom{m + 1}{k} k!$. Six people with A, B, C pairwise non-adjacent: $3! \cdot \binom{4}{3} \cdot 3! = 144$.
- **"Fixed relative order" (A before B before C, not necessarily adjacent):** among all $n!$ orders the $k$ specified objects show each of their $k!$ relative orders equally often: answer $\frac{n!}{k!}$. "A before B" alone: $\frac{n!}{2}$.
:::

:::example title="Worked — composing methods"
Six people P, Q, R, S, T, U in a row; P, Q together and R not at an end. Bundle PQ: $2 \cdot 5! = 240$ arrangements of the 5 objects. Subtract R at an end: 2 ends, then $4!$ arrangements of the rest, bundle order 2: $2 \cdot 4! \cdot 2 = 96$. Answer $240 - 96 = 144$. Order of operations: bundle first, then apply the positional restriction to the shrunken list.

Alternation: 5 men and 5 women alternating in a row: 2 patterns $\times 5! \cdot 5! = 28800$.
:::

:::warn title="Common traps — restrictions"
- Gap method requires the ordinary objects arranged **first**, and needs $k \leq m + 1$ to be possible at all.
- "Not adjacent" for a *specified pair* is bundle-and-subtract; "no two of a set adjacent" is the gap method. Swapping them is the classic error.
- Circular "not adjacent" via linear gap method: wrong geometry — use total minus bundled.
- Necklace division by 2 needs distinct beads (or Burnside); identical beads break exactness.
:::
