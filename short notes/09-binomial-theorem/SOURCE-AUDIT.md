# Source Audit — Chapter 9: Binomial Theorem

## Sources

- `notes/Binomial-Theorem/Binomial-Theorem.md` — the repository's own
  module (1734 lines, 6 chapters + appendix). **Read before authoring**
  (theory chapters in full; the Olympiad paper/solutions were not used as
  sheet content).
- Official JEE Advanced 2026 syllabus (jeeadv.ac.in PDF), Algebra unit:
  binomial theorem for a **positive integral index**. This is why the
  general series is Part II here, even though the source module treats it
  as a core chapter — a classification correction relative to the source.

## Independent verification performed

`scripts/math_checks.py`: **1231/1231 assertions pass**, covering the
general-term examples; multinomial coefficients and collected-term counts
(by explicit polynomial multiplication, incl. $(1+x+x^{2})^{4}$);
all identity-engine formulas swept for $n \le 14$ (row sums, alternating
sums, $k$-, $k(k-1)$-, $k^{2}$-weighted sums, $\frac{1}{k+1}$ sums in both
signs, sums of squares, alternating squares, hockey-stick for all $r$);
Vandermonde at several $(r, s, m)$; greatest-term example with neighbours;
Bernoulli randomised sweep; $2 \leq (1+1/n)^{n} \leq 3$ for $n < 60$;
last-digit and modular claims via Python modular exponentiation;
conjugate-surd floors for $n \le 9$; general-series coefficients
($\binom{-3}{k}$, $(1-x)^{-1/2}$ central-binomial form, $(1+3x)^{-2}$),
numeric series sums ($\sum (k+1)0.9^{k} = 100$,
$\sum \binom{2k}{k}8^{-k} = \sqrt{2}$), approximation anchors
($\sqrt[3]{26}$, $\sqrt{1.02}$); prime divisibility of $\binom{p}{k}$ for
all primes $\leq 47$; Lucas's theorem against direct computation (200
random cases) and the odd-entries/submask criterion; finite differences
$\sum (-1)^{k}\binom{n}{k}(x+k)^{n} = (-1)^{n}n!$.

## Corrections (source defects not reproduced)

- **Classification:** the source presents the negative/fractional-index
  series as a core chapter. The official syllabus restricts the binomial
  theorem to positive integral index, so the sheets place the general
  series in Part II with a status box (the mathematics is unchanged).
- No numeric errors were found in the Binomial source's worked answers
  that are sheeted here; every sheeted value was recomputed independently
  (see above). Two errors found in the *companion P&C source* during the
  same pass are recorded in chapter 8's SOURCE-AUDIT (they affect
  concepts shared between the chapters).

## Assumptions and conventions

- Part I: non-negative integral index only; $\binom{n}{k} = 0$ outside
  $0 \leq k \leq n$.
- General series always quoted with $|x| < 1$; endpoint convergence is
  flagged as delicate and never silently used.
- "Greatest term" means greatest absolute value at the given $x$.
