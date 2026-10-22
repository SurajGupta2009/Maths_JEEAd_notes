# Source Audit — Chapter 8: Permutations & Combinations

## Sources

- `notes/PnC/PnC.md` — the repository's own module (2513 lines, 6 chapters
  + appendix). **Read before authoring** (theory sections in full; the
  50-question Olympiad paper and solutions were not used as sheet content).
- Official JEE Advanced 2026 syllabus (jeeadv.ac.in PDF), Algebra unit —
  for the Part I / Part II boundary.

## Independent verification performed

`scripts/math_checks.py`: **297/297 assertions pass**, including brute-force
enumeration checks: 4-digit distinct-digit multiples of 5 (952 by listing);
DAAR adjacency (6 of 12 by listing); pairwise non-adjacent arrangements of
6 people (144 by listing all 720 permutations); $x+y+z=15$ (136 by listing);
derangements $D_{5} = 44$ by listing; onto functions $5 \to 3$ (150 by
listing); Dyck paths for $n \le 7$ by enumeration; necklace classes
$N(4,2) = 6$ by listing rotation classes; partitions $p(n)$, $n \le 10$,
and distinct = odd at $n = 10$ by enumeration; plus all closed-form values
(cricket team, bounded stars-and-bars, hockey-stick/Pascal sweeps,
Stirling/Bell tables, Catalan/ballot values, Burnside counts).

## Corrections (source defects not reproduced)

- **Cricket-team count (source S2, Chapter 3):** the source's table sums
  $\binom{7}{b}\binom{5}{w}$ over the valid $(b,w)$ for each number $a$ of
  all-rounders but omits the factor $\binom{3}{a}$. Its stated total 788 is
  wrong; the correct count is $12 + 198 + 660 + 490 = \mathbf{1360}$
  (brute-force confirmed). The sheets use 1360 and explicitly warn against
  dropping the enumerated group's factor.
- **Compositions of 10 into parts $\geq 2$ (source S5, Chapter 3):** the
  source sums over $k = 2..5$ parts and misses the one-part composition
  $[10]$. Correct total: $1 + 7 + 15 + 10 + 1 = \mathbf{34}$ (confirmed by
  direct enumeration and by DP). The sheets use 34.

## Assumptions and conventions

- $\binom{n}{r} = 0$ for $r \notin [0, n]$ inside sums; $0! = 1$.
- Necklace division by 2 (distinct beads) relies on no ring being
  flip-fixed; with identical beads Burnside's lemma is required — stated
  on the sheets.
- Derangement $D_{n}$ = nearest integer to $n!/e$ uses $n \geq 1$.
