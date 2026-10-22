---
id: olympiad-02
part: olympiad
title: "Extension — Burnside's Lemma and Pólya Enumeration: Counting Up to Symmetry"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Group-action counting is university/Olympiad material. It exists in this chapter because Part I's "divide by the symmetry" is exactly the special case where every orbit has the same size — and fails precisely when it does not.
:::

:::derive title="Burnside's lemma (double counting in disguise)"
A group $G$ acts on colourings $X$; orbits = essentially-different colourings. Count pairs $(g, x)$ with $gx = x$ two ways: by $g$ it is $\sum_{g} \left|\mathrm{Fix}(g)\right|$; by $x$ it is $\sum_{x} \left|\mathrm{Stab}(x)\right| = \sum_{x} \frac{\left|G\right|}{\left|\mathrm{orbit}(x)\right|}$, which sums to $\left|G\right| \times$ (number of orbits). Hence

$$\#\text{orbits} = \frac{1}{\left|G\right|} \sum_{g \in G} \left|\mathrm{Fix}(g)\right|$$

A colouring is fixed by $g$ iff it is constant on $g$'s cycles: $k^{\#\text{cycles}}$ colourings in $k$ colours.
:::

:::example title="Worked — necklaces and bracelets"
Necklaces of $n$ beads, $k$ colours (rotations only): $N(n, k) = \frac{1}{n}\sum_{d \mid n} \varphi(d)\, k^{n/d}$ (rotations grouped by $\gcd(n, s)$). $N(4, 2) = \frac{1}{4}(16 + 4 + 4) = 6$: RRRR, RRRB, RRBB, RBRB, RBBB, BBBB ✓. Bracelets of 6 beads, 2 colours (full dihedral group of order 12): fixed counts $64 + 2\cdot2 + 2\cdot4 + 8 + 3\cdot16 + 3\cdot8 = 156$, orbits $156/12 = 13$ ✓.
:::

:::warn title="Common traps — Burnside"
- Forgetting the identity element (usually the largest Fix count).
- Grouping rotations wrongly: rotation by $s$ on $n$ beads has $\gcd(n, s)$ cycles, and there are $\varphi(n/d)$ rotations with a given divisor structure — recount small cases by listing (as with $N(4, 2) = 6$).
- Applying "divide by $\left|G\right|$" directly to colourings: that is exactly the non-exact symmetry error Burnside repairs.
:::
