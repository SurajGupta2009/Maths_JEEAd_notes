# Scope — Chapter 8: Permutations & Combinations

Official basis: JEE (Advanced) 2026 syllabus, Algebra — "permutations and
combinations".

## In Part I (JEE core) — 7 sheets

- Counting foundations: product rule (with the fixed-count-per-step
  hypothesis), sum rule (disjoint + exhaustive), complement principle,
  bijections (subsets ↔ binary strings, monotone functions ↔ subsets,
  $A \subseteq B$ pairs $= 3^{n}$), the three sins of counting.
- Permutations: $P(n,r) = \frac{n!}{(n-r)!}$ from labelled roles, factorial
  and $0! = 1$, arrangements with identical objects
  $\frac{n!}{n_{1}! \cdots n_{k}!}$ via label–count–divide and the
  exact-symmetry condition.
- Circular permutations $(n-1)!$ (two proofs), necklaces of distinct
  beads, adjacency complements; bundle, gap ($m!\binom{m+1}{k}k!$) and
  fixed-relative-order ($\frac{n!}{k!}$) methods, composed restrictions.
- Combinations $\binom{n}{r}$ (exact division by $r!$), complementation
  symmetry, Pascal's identity and hockey-stick (each proved by one split),
  restricted selections including multi-group case tables.
- Stars and bars $\binom{n+k-1}{k-1}$ / $\binom{n-1}{k-1}$, multisets,
  compositions ($2^{n-1}$ total), lower-bound shifts, upper bounds via
  complement/IE.
- Inclusion–exclusion (proved by tracking one element), derangements
  ($D_{n} = n!\sum \frac{(-1)^{k}}{k!}$, recurrence, nearest integer to
  $n!/e$, rencontres numbers), onto functions, all-suits counting.
- Pigeonhole (odd-part and geometry box constructions, sharpness),
  recurrence counting by last-step decomposition (tilings, staircases),
  recap card and pre-submission checklist.

## In Part II (Olympiad extensions) — 3 sheets

- Lattice paths $\binom{a+b}{b}$, reflection principle, Catalan numbers
  $\frac{1}{n+1}\binom{2n}{n}$ with the first-return convolution, ballot
  theorem $\frac{p-q}{p+q}\binom{p+q}{q}$.
- Burnside's lemma (proved by double counting) and Pólya-style
  enumeration: necklaces $N(n,k) = \frac{1}{n}\sum_{d \mid n}\varphi(d)k^{n/d}$,
  bracelets.
- Integer partitions: generating function, Euler distinct = odd,
  conjugation duality, pentagonal recurrence; Stirling numbers of the
  second kind (recurrence and IE closed form), Bell numbers; Sperner's
  theorem (LYM), Erdős–Ko–Rado (statement, star extremal, $n \geq 2k$
  hypothesis).

## Out of scope

- The source module's deeper frontier (Frankl–Wilson, Bollobás set-pairs,
  cycle lemma in full, van der Waerden, probabilistic method) is noted in
  SOURCE-AUDIT but not sheeted; rook-polynomial theory is only signposted
  from derangements.
- Probability built on these counts is chapter 11.
