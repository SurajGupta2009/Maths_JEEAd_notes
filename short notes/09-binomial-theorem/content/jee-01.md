---
id: jee-01
part: jee
title: "Binomial Theorem — What (a+b)ⁿ Counts, the General Term, Middle Terms"
---

## The theorem is a census of bracket choices

Expanding $(a + b)^{n}$ means picking one letter from each of $n$ brackets. A pick-list is determined by *which $k$ brackets contributed $b$*: $\binom{n}{k}$ lists, each giving $a^{n - k}b^{k}$. Hence, for non-negative integer $n$,

$$(a + b)^{n} = \sum_{k=0}^{n} \binom{n}{k} a^{n - k} b^{k}, \qquad T_{k + 1} = \binom{n}{k} a^{n - k} b^{k}$$

No induction, nothing to memorise: the coefficient **is** a count (chapter 8). Symmetry $\binom{n}{k} = \binom{n}{n - k}$ (choose the $a$-brackets instead) and Pascal's rule (condition on the first bracket) are the same picture. Row $n$ of Pascal's triangle is the census for $(a + b)^{n}$.

:::key title="The general-term machine"
For $\left(\alpha x^{p} + \beta x^{-q}\right)^{n}$ the general term is $\binom{n}{k}\alpha^{n - k}\beta^{k} x^{p(n - k) - qk}$. "Coefficient of $x^{m}$" and "term independent of $x$" are one step: set the exponent $pn - (p + q)k$ equal to the target, solve for $k$; integer in $[0, n]$ $\Rightarrow$ substitute; otherwise **the answer is 0** — "no such term" is a legitimate exam answer.
:::

:::example title="Worked — the machine at three gears"
Coefficient of $x^{4}$ in $(2 + x)^{5}$: $k = 4$: $\binom{5}{4} 2^{1} = 10$ (full row $32 + 80x + 80x^{2} + 40x^{3} + 10x^{4} + x^{5}$ ✓).

Term independent of $x$ in $\left(x - \frac{2}{x^{2}}\right)^{9}$: exponent $9 - 3k = 0$, $k = 3$: $\binom{9}{3}(-2)^{3} = -672$.

Coefficient of $x^{4}$ in $(3 - 2x)^{7}$: $k = 4$: $\binom{7}{4} 3^{3} (-2)^{4} = 35 \cdot 27 \cdot 16 = 15120$ (even $k$, positive ✓).
:::

:::key title="Middle terms and equal coefficients"
$n$ even: one middle term $T_{n/2 + 1}$. $n$ odd: two, at $k = \frac{n - 1}{2}, \frac{n + 1}{2}$. Equal coefficients: $\binom{n}{r} = \binom{n}{s}$ iff $r = s$ or $r + s = n$ — always report both branches: in $(1 + x)^{18}$, coefficients of $x^{2r}$ and $x^{r + 6}$ equal gives $2r = r + 6$ or $2r + r + 6 = 18$, so $r = 6$ or $r = 4$. Consecutive-coefficient ratios: $\frac{\binom{n}{k + 1}}{\binom{n}{k}} = \frac{n - k}{k + 1}$ (three consecutive coefficients $36, 84, 126$ force row $n = 9$: ratios $\frac{7}{3}, \frac{3}{2}$ ✓).
:::

:::warn title="Common traps — general term"
- $T_{k}$ vs $T_{k + 1}$: the 5th term has $k = 4$.
- Buried negatives: rewrite the bracket as $A + B$ with the minus inside $B$, then apply the formula robotically.
- Expanding term-by-term instead of writing $T_{k + 1}$: the census view gives each term in one line.
:::

:::assume title="Standing conventions for this chapter"
Positive integral index $n$ in Part I (official syllabus); general real index is Part II. $\binom{n}{k} = 0$ outside $0 \leq k \leq n$. Coefficients of an expansion are read after collecting like powers — "number of terms" questions must state in which variable(s) collection happens.
:::
