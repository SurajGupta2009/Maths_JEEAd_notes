# Source Audit — Chapter 7: Sequences & Series

## Sources

- `notes/Sequences-and-Series/Sequences-and-Series.md` — the repository's
  own module (750 lines, 6 chapters + appendix). **Read in full before
  authoring.** The accompanying Paper/Solutions files are practice sets.
- Official JEE Advanced 2026 syllabus (jeeadv.ac.in PDF), Algebra unit —
  used to set the Part I / Part II boundary: AP, GP, AM, GM, $\sum n$,
  $\sum n^{2}$, $\sum n^{3}$ are in; HP, AGP-as-a-topic, recurrences,
  generating functions, products and Stolz–Cesàro are outside the listed
  lines (AGP/telescoping appear in Part I only as labelled one-step
  derivations of the GP sum).

## Independent verification performed

`scripts/math_checks.py`: **859/859 assertions pass**, covering AP/GP
formulas against direct summation; insertion of means; $S_{n} = 3n^{2} + 5n$
term recovery; the power-sum formulas for $n \le 30$ including $\sum k^{4}$;
AM–GM and $A \geq G \geq H$, $G^{2} = AH$ on 200 random positive pairs;
AGP finite formula vs direct sum ($\frac{57}{16}$ at $n=5$), infinite AGP
values $2$, $4$, $\sum k^{2}2^{-k} = 6$; telescoping families for
$n \le 20$ ($m = 1, 2$, triple product, factorials); HM values;
recurrence $a_{n} = 2^{n} - 1$; repeated-root characteristic example;
Binet for $n \le 13$; $\prod_{2}^{n}(1 - 1/k^{2}) = \frac{n+1}{2n}$;
Wallis finite closed form ($n \le 7$) and limit $\pi/2$ (3000 factors);
$H_{n}/\ln n$ at $10^{2}$–$10^{5}$ decreasing to 1; arctan telescope;
$a_{n+1} = a_{n} + 1/a_{n}$ asymptotics to $n = 2000$.

## Corrections (source defects not reproduced)

- **Source §6.5 remainder claim:** the source says that for
  $a_{n+1} = a_{n} + 1/a_{n}$, the remainder $\sum 1/a_{k}^{2}$ "converges
  to a finite constant". It does not: $1/a_{k}^{2} \approx 1/(2k)$, so the
  sum diverges like $\frac{1}{2}\ln n$ (verified numerically:
  $a_{n}^{2} - 2n$ grows without bound). The conclusion
  $a_{n} \sim \sqrt{2n}$ survives with remainder $O(\log n)$; the sheets
  state this correctly and flag the point.
- **Classification correction:** the source presents HP as a co-equal
  third progression in its core chapters. The official JEE Advanced
  syllabus does not list harmonic progressions; the sheets move HP/HM to
  Part II with an explicit status note (HM itself appears only through
  $A \geq G \geq H$).

## Assumptions and conventions

- $S_{n}$ always means the sum of the first $n$ terms; GP ratio definition
  assumes nonzero terms; AM–GM and the means framework assume positive
  numbers wherever invoked.
- Generating functions are used as formal power series (coefficient
  algebra), not as convergence statements.
- Infinite-sum formulas always carry their convergence condition
  ($|r| < 1$); products require a nonzero limit.
