# Scope — Chapter 9: Binomial Theorem

Official basis: JEE (Advanced) 2026 syllabus, Algebra — "binomial theorem
for a positive integral index". The general (real) index is explicitly
**not** in the official line and is placed in Part II.

## In Part I (JEE core) — 4 sheets

- The theorem $(a+b)^{n} = \sum \binom{n}{k}a^{n-k}b^{k}$ proved by the
  bracket-choice census; $T_{k+1}$; the exponent equation
  $pn - (p+q)k = m$ for coefficients and constant terms in
  $(\alpha x^{p} + \beta x^{-q})^{n}$, including "no such term" answers.
- Middle terms (one/two by parity), equal-coefficient conditions
  ($r = s$ or $r + s = n$), consecutive-coefficient ratios
  $\frac{n-k}{k+1}$ and recovering $n$ from three consecutive coefficients.
- Multinomial coefficients $\frac{n!}{n_{1}! \cdots n_{r}!}$, raw products
  $r^{n}$ vs collected terms $\binom{n+r-1}{r-1}$, and the single-variable
  collection trap ($2n+1$ terms in $(1+x+x^{2})^{n}$).
- Greatest binomial coefficients (peak at $\frac{n-1}{2}$, twin peaks for
  odd $n$) and numerically greatest terms of $(a+bx)^{n}$ via the ratio
  walk; substitution engine for coefficient sums ($f(1)$, $f(0)$, $f(-1)$,
  even/odd splits).
- Identity engines: $xf'(x)$ calculus sums ($\sum k\binom{n}{k}$,
  $\sum k(k-1)\binom{n}{k}$, $\sum k^{2}\binom{n}{k}$), integral sums
  $\sum \frac{\binom{n}{k}}{k+1} = \frac{2^{n+1}-1}{n+1}$, Vandermonde and
  specialisations ($\sum \binom{n}{k}^{2} = \binom{2n}{n}$, alternating
  squares), hockey-stick.
- Truncation inequalities: Bernoulli (with the $x > -1$ caveat),
  $2 \leq (1+1/n)^{n} \leq 3$; remainders and last digits by expanding
  around the modulus; conjugate-surd integer parts
  $(1+\sqrt{2})^{n} + (1-\sqrt{2})^{n} \in \mathbb{Z}$.

## In Part II (Olympiad extensions) — 2 sheets

- Generalised $\binom{r}{k}$ for real $r$; Euler's series with validity
  $|x| < 1$; the families $(1-x)^{-n}$ and $(1-x)^{-1/2}$; factoring
  discipline (ascending vs descending powers); approximations with
  explicit error budgets; summing series by recognition.
- Divisibility: $p \mid \binom{p}{k}$ for $0 < k < p$, Freshman's dream
  mod $p$, Lucas's theorem and the odd-entries count $2^{\text{popcount}(n)}$,
  Kummer's theorem (statement), finite differences annihilating
  polynomials.

## Out of scope

- Full convergence/boundary theory of the general series (Abel-type
  endpoint results) — flagged, not sheeted.
- Wolstenholme and deeper $p$-adic results from the source's Chapter 6.
