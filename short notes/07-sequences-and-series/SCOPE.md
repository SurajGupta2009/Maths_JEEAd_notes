# Scope — Chapter 7: Sequences & Series

Official basis: JEE (Advanced) 2026 syllabus, Algebra — "arithmetic and
geometric progressions, arithmetic and geometric means, sums of finite
arithmetic and geometric progressions, terms of geometric progression and
the sum … sum of the first $n$ terms … $\sum n$, $\sum n^{2}$, $\sum n^{3}$"
(AP, GP, AM, GM and the three power sums). Classification below is
concept-by-concept; nothing is claimed to "never appear in JEE" — Part II
items are *added theory* beyond the syllabus lines, while AGP/telescoping
are *derivations from* syllabus results and are marked as such.

## In Part I (JEE core) — 5 sheets

- AP: definition, $a_{n} = a + (n-1)d$, $S_{n} = \frac{n}{2}(2a + (n-1)d)
  = \frac{n}{2}(a + \ell)$ (derived by pairing), index identities
  $a_{m} + a_{n} = a_{p} + a_{q}$ for $m + n = p + q$, arithmetic means with
  the $k+1$ divisor, symmetric parametrisations, $S_{n}$-as-quadratic and
  $a_{n} = S_{n} - S_{n-1}$ recovery.
- GP: definition, $a_{n} = ar^{n-1}$, $S_{n} = \frac{a(r^{n}-1)}{r-1}$
  derived by shift-and-subtract, $S_{\infty} = \frac{a}{1-r}$ for
  $|r| < 1$ only, geometric means, $b^{2} = ac$, log-bridge to AP.
- AM–GM (two and $n$ terms, positives, equality iff all equal) with the
  attainability-of-equality warning; power sums $\sum k$, $\sum k^{2}$,
  $\sum k^{3}$ derived from $(k+1)^{m+1} - k^{m+1}$ telescoping; sums of
  odds $= n^{2}$; polynomial-term sums by splitting.
- Derivable applications (labelled): AGP shift-and-subtract
  ($\sum kx^{k} = \frac{x}{(1-x)^{2}}$, $\sum k^{2}x^{k}$), method of
  differences ($\frac{1}{k(k+m)}$ split, $m \geq 2$ survival counts,
  factorial telescopes).
- Problem shapes: recovering $d$/$r$ from two terms, AP↔GP interactions,
  recognition of non-obvious sequences ($2^{n-1} + 1$), recap card,
  ten-mistake checklist.

## In Part II (Olympiad extensions) — 3 sheets

- Harmonic progressions via reciprocals, harmonic mean, $A \geq G \geq H$
  and $G^{2} = AH$; average-speed application. **Not** an official JEE
  Advanced topic — included as extension, flagged on the sheet.
- Recurrences: fixed-point shift for $a_{n} = pa_{n-1} + q$; characteristic
  equation (distinct and repeated roots); generating functions as formal
  power series; Fibonacci $F(x) = \frac{x}{1-x-x^{2}}$ to Binet.
- Infinite products ($\prod (1 - 1/k^{2}) = \frac{n+1}{2n} \to \frac12$,
  Wallis finite form $\to \frac{\pi}{2}$); Stolz–Cesàro with
  $H_{n}/\ln n \to 1$; asymptotics by squaring-and-telescoping; arctan
  telescope (cross-reference to chapter 4's branch discipline).

## Out of scope

- Convergence theory beyond the GP/AGP conditions stated (analysis of
  series is not a JEE Advanced topic).
- HP sum formulas: none exist in elementary closed form; not invented.
- Binomial/series expansions (chapter 9).
