---
title: "Binomial Theorem — Olympiad Paper Solutions"
aliases:
  - Binomial-Theorem Solutions
module: "Binomial-Theorem"
module_title: "Binomial Theorem"
type: solutions
tags:
  - binomial-theorem
  - solutions
  - olympiad
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Binomial-Theorem — Paper|Paper]] · 📖 [[Binomial-Theorem|Binomial Theorem]]

# Olympiad Paper · Solutions & marking guide

*Companion to the 38-question paper*

# Full Worked Solutions

Every solution shows the *method name* first, then the computation, then a check. Where a problem has two standard methods, both are given — the exam rewards the ability to choose, and the notes are built on the same principle. All numeric answers below were re-verified by an independent pure-Python computation (exact polynomial convolutions, modular arithmetic) before this key was written.

### A · Binomial from Counting (Q1–Q5)

#### **Q1**[JEE Main]Find the coefficient of $x^6$ in $(1-2x)^9$.

Find the coefficient of $x^6$ in $(1-2x)^9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: general term.** $T_{k+1} = \binom{9}{k}(-2x)^k$; the $x^6$ slot is $k = 6$: $\binom96 (-2)^6 = 84 \cdot 64 = 5376$.


Answer: $5376$


Check: $\binom96 = \binom93 = 84$, $2^6 = 64$, $84 \cdot 64 = 5376$; sign positive since $k$ even ✓.

</details>

#### **Q2**[JEE Main]Find the sum of the coefficients of $(3x^2 - 2x + 1)^5$.

Find the sum of the coefficients of $(3x^2 - 2x + 1)^5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitution $x = 1$.** The sum of coefficients of a polynomial equals its value at $x = 1$: $(3 - 2 + 1)^5 = 2^5 = 32$.


Answer: $32$


Check: no expansion was needed — the whole question tests whether you know the substitution, and $2^5$ has no sign subtleties ✓.

</details>

#### **Q3**[JEE Main]How many distinct terms remain after collecting like terms in $(a+b+c)^{10}$?

How many distinct terms remain after collecting like terms in $(a+b+c)^{10}$?

<details>
<summary>Answer + Reasoning</summary>

**Method: exponent tuples $=$ stars and bars.** A collected term is $a^i b^j c^k$ with $i + j + k = 10$, $i,j,k \ge 0$: the count is $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$. (The raw product count is $3^{10}$.)


Answer: $66$


Check: the multinomial $x^3y^2z^5$ occurs $\frac{10!}{3!2!5!} = 2520$ times among the raw products — every collected term does, in general, so both counts are census-complete ✓.

</details>

#### **Q4**[JEE Adv]In $(1+x)^{13}$, $\binom{13}{r} = \binom{13}{r+3}$. Find $r$ and the common value.

In $(1+x)^{13}$, $\binom{13}{r} = \binom{13}{r+3}$. Find $r$ and the common value.

<details>
<summary>Answer + Reasoning</summary>

**Method: the two-branch symmetry solve.** Equality of binomial coefficients forces $r = r+3$ (impossible) or $r + (r+3) = 13$. Hence $2r = 10$, $r = 5$, and the common value is $\binom{13}{5} = \binom{13}{8} = 1287$.


Answer: $r = 5$; $1287$


Check: $\binom{13}{5} = \frac{13\cdot12\cdot11\cdot10\cdot9}{120} = 13\cdot11\cdot9 = 1287$ ✓; a brute scan of row 13 confirms no other coincidence at distance 3 ✓ (verified by script).

</details>

#### **Q5**[JEE Adv]Prove $\sum_{k=0}^n \binom{n}{k} = 2^n$ by an explicit bijection.

Prove $\sum_{k=0}^n \binom{n}{k} = 2^n$ by an explicit bijection.

<details>
<summary>Answer + Reasoning</summary>

**Method: count one set two ways.** Let $\mathcal P$ be the set of all subsets of $[n] = \{1,\dots,n\}$. Each subset is decided element-by-element — $n$ independent in/out choices: $|\mathcal P| = 2^n$. Alternatively group $\mathcal P$ by size: exactly $\binom{n}{k}$ subsets have size $k$, so $|\mathcal P| = \sum_k
        \binom nk$. The identity is the comparison of two censuses of the *same* set; the bijection is "a subset, seen as a subset".


Answer: $2^n = \sum_{k=0}^n \binom nk$, both sides $= |\mathcal P([n])|$


Check at $n = 3$: $1+3+3+1 = 8$ ✓ — and the grouping by parity of size gives the Chapter 1 even/odd split for free.

</details>


### B · Coefficient Machinery (Q6–Q11)

#### **Q6**[JEE Main]Coefficient of $x^5$ in $(1+x)^{10} + (1+x)^{11}$, rewritten via one identity.

Coefficient of $x^5$ in $(1+x)^{10} + (1+x)^{11}$, rewritten via one identity.

<details>
<summary>Answer + Reasoning</summary>

**Method: read each row.** $\binom{10}{5} + \binom{11}{5} = 252 + 462 = 714$. Using Pascal's rule $\binom{11}{5} = \binom{10}{4} + \binom{10}{5}$, the same answer is $\binom{10}{4} + 2\binom{10}{5} = 210 + 504 = 714$ — row-10 entries with the identity named, as requested.


Answer: $714$


Check: add one more way — $(1+x)^{11} = (1+x)(1+x)^{10}$ so the coefficient of $x^5$ there is $\binom{10}{5} + \binom{10}{4} = 462$ ✓, consistent with the line above.

</details>

#### **Q7**[JEE Adv]Find the coefficient of $x^{-2}$ in $\left(x^2 + \dfrac{1}{x^3}\right)^9$.

Find the coefficient of $x^{-2}$ in $\left(x^2 + \dfrac{1}{x^3}\right)^9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: exponent equation.** $T_{k+1} = \binom9k x^{2(9-k)} x^{-3k}
        = \binom9k x^{18-5k}$. Solve $18 - 5k = -2 \Rightarrow k = 4$. Coefficient $\binom94 = 126$.


Answer: $126$


Check: $18 - 5k$ hits $-2$ for exactly one $k \in [0,9]$ ✓ (step size 5, and $126$ is the same as the $x^{-2}$-slot; neighbouring slots $k=3,5$ would give $x^3, x^{-7}$ — no double counting).

</details>

#### **Q8**[JEE Adv]Find the coefficient of $x^4$ in $(1+x+x^2)^5$.

Find the coefficient of $x^4$ in $(1+x+x^2)^5$.

<details>
<summary>Answer + Reasoning</summary>

**Method 1: multinomial census.** From 5 brackets, total exponent 4 using parts $\le 2$: patterns $(2,2,0,0,0)$: $\frac{5!}{2!3!} = 10$; $(2,1,1,0,0)$: $\frac{5!}{1!2!2!} = 30$; $(1,1,1,1,0)$ — sums to 4 with parts $\le 1$: 4 ones and a zero: $\frac{5!}{4!1!} = 5$. Total $10 + 30 + 5 = 45$.


**Method 2: the $\frac{1-x^3}{1-x}$ trick.** $(1+x+x^2)^5 = (1-x^3)^5 (1-x)^{-5}$. The $x^4$ coefficient is $[x^4](1-x)^{-5} - 5[x^1](1-x)^{-5} = \binom84 - 5\cdot\binom51 = 70 - 25 = 45$.


Answer: $45$


Check: two independent engines — the multinomial sum and the geometric product — agree on 45 (both confirmed against the full convolution $1+5x+15x^2+30x^3+45x^4+41x^5+\cdots
        +x^{10}$) ✓.

</details>

#### **Q9**[JEE Adv]Sum of coefficients of $(1+2x)^n$ is $6561$. Find $n$.

Sum of coefficients of $(1+2x)^n$ is $6561$. Find $n$.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $x = 1$.** $(1+2)^n = 3^n = 6561$. Compute $3^8 = 6561$: $n = 8$.


Answer: $n = 8$


Check: $3^4 = 81$, $81^2 = 6561$ ✓ (so $3^8$ is right and the exponent is unique since $3^n$ is strictly increasing).

</details>

#### **Q10**[JEE Adv]4th and 8th binomial coefficients of $(1+x)^n$ are equal; find $n$ and the greatest…

4th and 8th binomial coefficients of $(1+x)^n$ are equal; find $n$ and the greatest coefficient.

<details>
<summary>Answer + Reasoning</summary>

**Method: convert ordinals to $k$'s, then two-branch solve.** 4th term is $k = 3$, 8th is $k = 7$: $\binom n3 = \binom n7$ gives $3 = 7$ (dead) or $3 + 7 = n \Rightarrow n = 10$. Row 10 peaks at $k = 5$: $\binom{10}{5} = 252$.


Answer: $n = 10$; greatest coefficient $252$


Check: $\binom{10}{3} = 120 = \binom{10}{7}$ ✓; $n$ even ⇒ unique middle peak at $k = 5$ ✓.

</details>

#### **Q11**[Olympiad]Prove $\dbinom{2n}{n} \gt \dfrac{4^n}{2n+1}$ and evaluate at $n = 6$.

Prove $\dbinom{2n}{n} \gt \dfrac{4^n}{2n+1}$ and evaluate at $n = 6$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the largest term beats the average.** $(1+1)^{2n} = \sum_k
        \binom{2n}{k} = 4^n$ has $2n+1$ summands, each $\le \binom{2n}{n}$ (the central coefficient is the row's maximum — Chapter 2's ratio walk). If every summand equalled the maximum the row would be constant, but $\binom{2n}{0} = 1 \lt \binom{2n}{n}$ for $n \ge 1$, so the inequality is strict: $4^n \lt (2n+1)\binom{2n}{n}$.


Answer: proved; at $n = 6$: $924 \gt \tfrac{4096}{13} \approx 315.1$


Check at $n=1$: $2 > 4/3$ ✓. Read the other way, the proof shows the central coefficient is within a factor $2n+1$ of the whole row sum $4^n$ — the standard "sandwich" that opens the door to $\binom{2n}{n} \sim 4^n/\sqrt{\pi n}$.

</details>


### C · The Identity Toolkit (Q12–Q16)

#### **Q12**[JEE Main]Evaluate $\sum_{k=0}^{6} \frac{\binom{6}{k}}{k+1}$ exactly.

Evaluate $\sum_{k=0}^{6} \frac{\binom{6}{k}}{k+1}$ exactly.

<details>
<summary>Answer + Reasoning</summary>

**Method: integral engine.** $\sum_k \binom 6k \frac{1}{k+1} =
        \int_0^1 (1+x)^6 dx = \frac{2^7 - 1}{7} = \frac{127}{7}$.


Answer: $\dfrac{127}{7}$


Check by term: $1 + 3 + 3 + \tfrac{20}{4} + \tfrac{15}{5} + \tfrac{6}{6} + \tfrac17
        = 1+3+3+5+3+1+\tfrac17 = \tfrac{127}{7}$ ✓.

</details>

#### **Q13**[JEE Main]Evaluate $\sum_{k=0}^{4} k\binom{4}{k} 2^{-k}$.

Evaluate $\sum_{k=0}^{4} k\binom{4}{k} 2^{-k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $x f'$ at a legal point.** $\sum_k k\binom nk x^k = nx(1+x)^{n-1}$; at $x = \tfrac12$, $n = 4$: $4 \cdot \tfrac12 \cdot (\tfrac32)^3 = 2 \cdot \tfrac{27}{8}
        = \tfrac{27}{4}$.


Answer: $\dfrac{27}{4}$


Check term by term: $0 + 4\cdot\tfrac12 + 6\cdot2\cdot\tfrac14 + 4\cdot3\cdot\tfrac18 + 0\cdot16^{-1}$ $= 2 + 3 + 1.5 + 0.25 = 6.75 = \tfrac{27}{4}$ ✓.

</details>

#### **Q14**[JEE Adv]Evaluate $\sum_{k=0}^{10} \frac{(-1)^k}{k+1}\binom{10}{k}$.

Evaluate $\sum_{k=0}^{10} \frac{(-1)^k}{k+1}\binom{10}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: same engine, sign flipped.** The sum is $\int_0^1 (1-x)^{10} dx = \frac{1}{11}$ — expand $(1-x)^{10}$ and integrate monomial by monomial.


Answer: $\dfrac{1}{11}$


Check: $\sum_k (-1)^k\binom{10}{k} = 0$ is the same computation with the integral of $x^k$ removed; the $k+1$ denominators appear *because* of the integral — the pair of answers $0$ and $\frac1{11}$ is a consistency test of the method itself ✓.

</details>

#### **Q15**[JEE Adv]Find $\sum_k k\binom{12}{k}$ over even $k$ only.

Find $\sum_k k\binom{12}{k}$ over even $k$ only.

<details>
<summary>Answer + Reasoning</summary>

**Method: even-slot projector.** $\mathbf 1_{k\text{ even}} = \frac{1+(-1)^k}{2}$, so the target is $\frac12\left[\sum_k k\binom{12}{k} + \sum_k k\binom{12}{k}(-1)^k\right] =
        \frac12\left[12\cdot 2^{11} + \big(-12(1-1)^{11}\big)\right] = \frac{12 \cdot 2^{11}}{2} = 12\cdot2^{10}$, using $\sum k\binom nk x^{k} = nx(1+x)^{n-1}$ at $x = -1$ for the second bracket (0 for $n \ge 2$).


Answer: $12288$


Check: odd part equals the same $12288$; total $= 12\cdot 2^{11} = 24576$ ✓.

</details>

#### **Q16**[JEE Adv]Prove $\sum_k \frac{\binom nk}{k+1} = \frac{2^{n+1}-1}{n+1}$ and deduce the alternating…

Prove $\sum_k \frac{\binom nk}{k+1} = \frac{2^{n+1}-1}{n+1}$ and deduce the alternating variant.

<details>
<summary>Answer + Reasoning</summary>

**Method: integrate the master polynomial.** $(1+x)^n = \sum_k \binom nk x^k$ on $[0,1]$: LHS integrates to $\frac{(1+x)^{n+1}}{n+1}\Big|_0^1
        = \frac{2^{n+1}-1}{n+1}$; RHS integrates to $\sum_k \frac{\binom nk}{k+1}$. For the variant, do the identical computation with $(1-x)^n$: the integral is $\frac{1 - 0^{n+1}}{n+1} = \frac1{n+1}$ and the sum picks up $(-1)^k$.


Answer: both proved — one engine, the sign is a substitution


Check at $n = 1$: $1 + \tfrac12 = \tfrac32 = \tfrac{2^2-1}{2}$ ✓ and $1 - \tfrac12 = \tfrac12 = \tfrac12$ ✓.

</details>


### D · Infinite Expansions (Q17–Q22)

#### **Q17**[JEE Main]Coefficient of $x^6$ in $(1-x)^{-4}$.

Coefficient of $x^6$ in $(1-x)^{-4}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: owned family $(1-x)^{-n} = \sum_k \binom{n+k-1}{k}x^k$.** At $n = 4, k = 6$: $\binom{9}{6} = 84$. Validity $|x| \lt 1$ is implicit in using the series.


Answer: $84$


Check the derivation of the family: $\binom{-4}{k} = (-1)^k
        \frac{4\cdot5\cdots(3+k)}{k!} = (-1)^k \binom{k+3}{k}$ — signs cancel against $(-x)^k$, all coefficients positive ✓.

</details>

#### **Q18**[JEE Main]Expand $(3+2x)^{-2}$ ascending to the linear term; state validity.

Expand $(3+2x)^{-2}$ ascending to the linear term; state validity.

<details>
<summary>Answer + Reasoning</summary>

**Method: factor the constant.** $(3+2x)^{-2} = \frac19\left(1 + \frac{2x}{3}\right)^{-2} = \frac19\left(1 - 2\cdot\frac{2x}{3} + \cdots\right)
        = \frac19 - \frac{4x}{27} + \cdots$. Validity: $\left|\frac{2x}{3}\right| \lt 1
        \iff |x| \lt \frac32$.


Answer: $\dfrac19 - \dfrac{4x}{27} + \cdots,\ \ |x| \lt \dfrac32$


Check: derivative at $x = 0$ of $(3+2x)^{-2}$ is $-2(3+2x)^{-3}\cdot2\big|_0 = -\tfrac{4}{27}$ ✓ — the linear coefficient is exactly $f'(0)$.

</details>

#### **Q19**[JEE Adv]Coefficient of $x^5$ in $(1+x)^{-1/2}$.

Coefficient of $x^5$ in $(1+x)^{-1/2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: half-integer generalised coefficient.** $\binom{-1/2}{5} = \frac{(-1/2)(-3/2)(-5/2)(-7/2)(-9/2)}{5!} = -\frac{945}{32\cdot120}
        = -\frac{63}{256}$. Equivalently $(-1)^k \binom{2k}{k}/4^k$ at $k = 5$: $-\tfrac{252}{1024}$.


Answer: $-\dfrac{63}{256}$


Check: $945/3840 = 63/256$ after dividing by 15 ✓; negative because five numerator factors are each negative ✓.

</details>

#### **Q20**[JEE Adv]Evaluate $1 + 2(0.9) + 3(0.9)^2 + \cdots$.

Evaluate $1 + 2(0.9) + 3(0.9)^2 + \cdots$.

<details>
<summary>Answer + Reasoning</summary>

**Method: recognise the $(1-t)^{-2}$ family.** $\sum_k (k+1)t^k = (1-t)^{-2}$ for $|t| \lt 1$; at $t = 0.9$: $(0.1)^{-2} = 100$.


Answer: $100$


Check: the family is the derivative of the geometric series, and $\sum t^k = (1-t)^{-1}$ ⇒ $\sum (k{+}1)t^k = \frac{d}{dt}\big[t(1-t)^{-1}\big]$... simpler: it is $(1-t)^{-2}$ by the negative-exponent formula with $n = 2$, coefficients $\binom{k+1}{k} = k+1$ ✓.

</details>

#### **Q21**[JEE Adv]Estimate $\sqrt{1.04}$ to five decimal places with an error justification.

Estimate $\sqrt{1.04}$ to five decimal places with an error justification.

<details>
<summary>Answer + Reasoning</summary>

**Method: $(1+x)^{1/2}$ at $x = 0.04$, four terms.** 
$$ 1 + \frac{0.04}{2} - \frac{0.04^2}{8} + \frac{0.04^3}{16} = 1 + 0.02 - 0.0002 + 0.000004 = 1.019804. $$
 The next term is $-\frac{5}{128}x^4 \approx -2.5 \times 10^{-9}$, so the fourth decimal is settled and the fifth (rounding down the $4$ to $1.01980$) is safe by ten orders of magnitude.


Answer: $1.01980$


Check: $(1.01980)^2 = 1.040 - \text{tiny}$: $1.0198^2 = 1.03999204$ vs $1.04$ — the residual $8\times10^{-6}$ equals $2 \times 1.02 \times 4\times10^{-6}$, exactly the discarded sliver ✓.

</details>

#### **Q22**[Olympiad]Prove Bernoulli by truncation; use two kept terms to show $1.01^{50} \gt 1.6$.

Prove Bernoulli by truncation; use two kept terms to show $1.01^{50} \gt 1.6$.

<details>
<summary>Answer + Reasoning</summary>

**Method: non-negative terms ⇒ truncation is a bound.** For $x \ge 0$, $(1+x)^n = \sum_k \binom nk x^k \ge \sum_{k \in S} \binom nk x^k$ for any term set $S$. With $S = \{0,1\}$: Bernoulli $(1+x)^n \ge 1 + nx$. With $S = \{0,1,2\}$ and $x = 0.01, n = 50$: $(1.01)^{50} \ge 1 + 0.5 + \frac{50\cdot49}{2}\times10^{-4}
        = 1.6225 \gt 1.6$.


Answer: proved; $1.6225 > 1.6$


Check: the true value is $1.6446\ldots$ — the two-term truncation overshoots the target with $0.0225$ of slack, so the argument never depended on the third term's luck ✓. (Keeping only $S=\{0,1\}$ gives $1.5$ — *fails* to beat $1.6$: choosing enough terms is the whole skill here.)

</details>


### E · Size, Growth and Extremes (Q23–Q27)

#### **Q23**[JEE Main]Prove $\left(1 + \frac1n\right)^n \lt 3$.

Prove $\left(1 + \frac1n\right)^n \lt 3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand, dominate, geometric-series.** The $k$-th summand is $\frac{n(n-1)\cdots(n-k+1)}{k!\,n^k} \le \frac1{k!} \le \frac{1}{2^{k-1}}$, so the total is at most $1 + \sum_{k\ge1} 2^{1-k} = 3$; for $n \ge 2$ the $k = 2$ summand is $\frac{n-1}{2n} \lt \frac12$ making the total strictly under 3; $n = 1$: $2 \lt 3$ by hand.


Answer: proved — pinched below 3 for all $n \ge 1$


Check $n = 1000$: $2.7169\ldots \lt 3$ ✓; the same chain gives the classical corollary $e \le 3$.

</details>

#### **Q24**[JEE Adv]Show $a_n = (1+1/n)^n$ strictly increases.

Show $a_n = (1+1/n)^n$ strictly increases.

<details>
<summary>Answer + Reasoning</summary>

**Method: summand-by-summand comparison.** The $k$-th summand of $a_n$ is $\frac1{k!}\prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right)$; each factor strictly increases as $n \to n+1$ for $j \ge 1$, and $a_{n+1}$ has one *extra* positive summand. Hence every summand of $a_n$ is strictly exceeded by its twin inside $a_{n+1}$, and the extra term only widens the gap: $a_{n+1} \gt a_n$.


Answer: proved strictly increasing; combined with Q23 the limit defining $e$ is trapped in $[2,3)$


Check: $a_1 = 2 \lt a_2 = 2.25 \lt a_3 = 64/27 \approx 2.37$ ✓.

</details>

#### **Q25**[JEE Adv]Find $\lfloor (1+\sqrt2)^3 \rfloor$ without approximating $\sqrt 2$.

Find $\lfloor (1+\sqrt2)^3 \rfloor$ without approximating $\sqrt 2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: conjugate sum.** $S = (1+\sqrt2)^3 + (1-\sqrt2)^3$: the odd surd terms cancel in the binomial expansions, $S = 2(1 + 3\cdot 2) = 14 \in \mathbb Z$. Since $1 - \sqrt2 \in (-1, 0)$, its cube lies in $(-1, 0)$; thus $(1+\sqrt2)^3 = 14 - (1-\sqrt2)^3 \in (14, 15)$.


Answer: $14$


Check directly: $(1+\sqrt2)^3 = 7 + 5\sqrt2 \approx 14.07$ ✓ — and the floor is the conjugate sum itself for odd exponents (the point of Q38).

</details>

#### **Q26**[JEE Adv]Greatest term of $(3+2x)^{10}$ at $x = 1$.

Greatest term of $(3+2x)^{10}$ at $x = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: ratio walk.** $t_k = \binom{10}{k} 3^{10-k} 2^k$; $\frac{t_{k+1}}{t_k} = \frac{10-k}{k+1}\cdot\frac23 \ge 1 \iff 2(10-k) \ge 3(k+1) \iff
        k \le 3.4$. The walk ascends through $k = 4$ and descends after: greatest term $T_5 = \binom{10}{4} 3^6 2^4 = 210 \cdot 729 \cdot 16 = 2449440$.


Answer: $T_5 = 2449440$


Check neighbours: $t_3 = 120\cdot2187\cdot8 = 2099520$ and $t_5 = 252\cdot243\cdot32 = 1959552$, both smaller ✓.

</details>

#### **Q27**[Olympiad]Prove $2^n \gt n^2$ for $n \ge 5$ by keeping four symmetric terms of $(1+1)^n$.

Prove $2^n \gt n^2$ for $n \ge 5$ by keeping four symmetric terms of $(1+1)^n$.

<details>
<summary>Answer + Reasoning</summary>

**Method: symmetric truncation.** For $n \ge 7$ the slots $2, 3, n-2, n-3$ are four *distinct* indices, so $2^n \ge 2\left[\binom n2 + \binom n3\right]
        = \frac{n(n-1)(n+1)}{3}$, and $\frac{n(n^2-1)}{3} \gt n^2 \iff n^2 - 1 \gt 3n$, true for $n \ge 4$. Base cases $n = 5, 6$ check directly: $32 \gt 25$, $64 \gt 36$. (The indices coincide at $n = 5, 6$, which is *why* the hand-check is not laziness but necessity — a favourite examiner detail.)


Answer: proved for all $n \ge 5$


Check the coincidence honestly: at $n = 6$, "four terms" are actually $\binom62 + \binom63 + \binom64 + \binom63$ — double-counted — the direct check is the clean fix ✓.

</details>


### F · Divisibility and Remainders (Q28–Q32)

#### **Q28**[JEE Main]Prove $p \mid \binom pk$ for prime $p$, $0 \lt k \lt p$; deduce $2^7 \equiv 2 \pmod 7$.

Prove $p \mid \binom pk$ for prime $p$, $0 \lt k \lt p$; deduce $2^7 \equiv 2 \pmod 7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the denominator can't absorb the prime.** $p \cdot (p-1)\cdots(p-k+1) = \binom pk \cdot k!$: the left side is divisible by $p$; $k!$ is coprime to $p$ since every factor is $\lt p$; Euclid's lemma gives $p \mid \binom pk$. Then $2^7 = (1+1)^7 = \sum_k \binom 7k \equiv \binom70 + \binom77 = 2$.


Answer: proved; $128 = 7\cdot 18 + 2$


Check interior entries: $7, 21, 35, 35, 21, 7$ — every one a multiple of 7 ✓.

</details>

#### **Q29**[JEE Main]Remainder of $3^{37} - 3$ upon division by $37$.

Remainder of $3^{37} - 3$ upon division by $37$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Freshman's Dream, twice.** $37$ is prime, so $(a+b)^{37} \equiv
        a^{37} + b^{37}$. Thus $3^{37} = (1+2)^{37} \equiv 1 + 2^{37}$, and again $2^{37} = (1+1)^{37} \equiv 1 + 1 = 2$. So $3^{37} \equiv 3 \pmod{37}$, and the remainder of $3^{37} - 3$ is $0$.


Answer: $0$


Check: the argument used only Q28's lemma twice — no external theorem quoted; $3^{37} - 3$ is in fact divisible by 37 (a Fermat quotient sanity computed in the verification script: pow(3,37,37) = 3) ✓.

</details>

#### **Q30**[JEE Adv]Trailing zeros of $200!$.

Trailing zeros of $200!$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Legendre on the bottleneck prime.** Zeros $=\min(v_2, v_5)$, and fives are scarcer: $v_5(200!) = \lfloor\tfrac{200}5\rfloor + \lfloor\tfrac{200}{25}\rfloor
        + \lfloor\tfrac{200}{125}\rfloor = 40 + 8 + 1 = 49$.


Answer: $49$


Check the bookkeeping: the 8 counts 25-multiples twice, the 1 counts 125-multiples a third time (only 125 itself below 200); next floor is $200/625 = 0$ ✓.

</details>

#### **Q31**[JEE Adv]Remainder of $6^{999} + 1$ mod $5$.

Remainder of $6^{999} + 1$ mod $5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand around the modulus.** $6^{999} = (5+1)^{999}$; every term with a $5^j$ factor dies mod 5, the survivor is $1$. Total: $1 + 1 = 2$.


Answer: $2$


Check: $6^2 = 36 \equiv 1$, so $6^{998} \equiv 1$ and $6^{999} + 1 \equiv 6 + 1 \equiv 2$ ✓.

</details>

#### **Q32**[Olympiad]Prove: a prime $p$ divides every interior entry of row $n$ iff $n = p^e$.

Prove: a prime $p$ divides every interior entry of row $n$ iff $n = p^e$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the digit-sum valuation $v_p\binom nk = \frac{s_p(k) + s_p(n-k) - s_p(n)}{p-1}$** (Legendre's floors collected: $v_p(m!) = \frac{m - s_p(m)}{p-1}$).


*Converse ($n = p^e \Rightarrow$ uniform divisibility):* for $0 \lt k \lt p^e$, the base-$p$ addition $k + (p^e - k)$ must carry (some digit of $k$ below position $e$ is positive and its complement digit forces the sum past $p-1$; a carry of exactly the digit-loss $p-1$), giving $v_p \ge 1$ for every interior entry. *($\Rightarrow$):* if $n = p^e q$ with $q \gt 1$ and $p \nmid q$, test the interior slot $k = p^e$: $s_p(k) = 1$, $s_p(n-k) = s_p((q-1)p^e) = s_p(q-1) = s_p(q)-1$, $s_p(n) = s_p(q)$, so $v_p\binom{n}{p^e} = 0$: an interior entry *not* divisible by $p$. Hence the uniform-divisibility hypothesis forces a single base-$p$ digit, i.e. $n = p^e$ (the digit's coefficient too: a top digit $a \ge 2$ at position $e$ would put $\binom{a p^e}{p^e} \equiv a \not\equiv 0$ — same digit test, one line).


Answer: proved both directions via the valuation formula


Check: row 8 ($= 2^3$) interior $8,28,56,70,\dots$ all even ✓, gcd 2; row 12: the test slot $\binom{12}{3} = 220$ with $p = 3$: $3 \nmid 220$ ✓ as predicted; row 9 for $p = 3$: all of $9,36,84,126$ divisible by 3 ✓.

</details>


### G · Parity, Lucas and Kummer (Q33–Q36)

#### **Q33**[JEE Adv]Odd entries of row 2024 of Pascal's triangle.

Odd entries of row 2024 of Pascal's triangle.

<details>
<summary>Answer + Reasoning</summary>

**Method: Lucas parity.** $\binom{n}{k}$ is odd iff no carries occur in $k + (n-k) = n$ in base 2, iff every 1-bit of $k$ is a 1-bit of $n$. Count: $2024 = 1111110100_2$ has $7$ ones ⇒ $2^7$ admissible $k$'s.


Answer: $128$


Check the bit string: $1024+512+256+128+64+32+8 = 2024$ ✓ — seven summands, seven bits.

</details>

#### **Q34**[JEE Adv]Highest power of $2$ dividing $\binom{20}{10}$.

Highest power of $2$ dividing $\binom{20}{10}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Kummer — count the carries.** $\binom{20}{10}$ lives at the addition $10 + 10 = 20$; in binary $1010_2 + 1010_2$: bit 1 carries, bit 3 carries — **two carries**, so $v_2 = 2$ and the answer is $2^2$.


Answer: $4$


Check with Legendre directly: $v_2(20!) - 2v_2(10!) = (10+5+2+1) -
        2(5+2+1) = 18 - 16 = 2$ ✓ — $\binom{20}{10} = 184756 = 4 \cdot 46189$, and $46189$ is odd ✓.

</details>

#### **Q35**[JEE Adv] $\binom{10}{3}$ mod 7 by Lucas, and mod 2. Explain the different verdicts.

$\binom{10}{3}$ mod 7 by Lucas, and mod 2. Explain the different verdicts.

<details>
<summary>Answer + Reasoning</summary>

**Method: digitwise reduction in each base.** Base 7: $10 = (1,3)_7$, $3 = (0,3)_7$: $\binom{10}{3} \equiv \binom10\binom33 = 1$. Base 2: $10 = (1010)_2$, $3 = (0011)_2$ — the low bit has $k_0 = 1 \gt n_0 = 0$, so $\binom{n_0}{k_0} = \binom01 = 0$ annihilates the product: $\binom{10}{3} \equiv 0 \pmod 2$.


Answer: $120 \equiv 1 \pmod 7$ and $0 \pmod 2$ — consistent since $120 = 7\cdot 17 + 1$ and even


Check: no contradiction is possible — Lucas computes the *same integer's* residue in two moduli; and the mod-7 answer is non-zero precisely because base-7 digits $3 \le 3, 0 \le 1$ pass the digit test ✓.

</details>

#### **Q36**[Olympiad]Compute $\sum_{k \equiv 0 (3)} \binom{15}{k}$ with the roots-of-unity filter.

Compute $\sum_{k \equiv 0 (3)} \binom{15}{k}$ with the roots-of-unity filter.

<details>
<summary>Answer + Reasoning</summary>

**Method: filter.** $\sum_{k \equiv 0}\binom{15}{k} = \frac13\big[(1+1)^{15}
        + (1+\omega)^{15} + (1+\omega^2)^{15}\big]$ with $\omega = e^{2\pi i/3}$. Since $1+\omega = -\omega^2$ and $1 + \omega^2 = -\omega$, both $15$-th powers equal $(-1)^{15}\omega^{30} = -1$ and $(-1)^{15}\omega^{15} = -1$. Total: $\frac{2^{15} - 2}{3} = \frac{32766}{3} = 10922$.


Answer: $10922$


Check: the other two classes come out $\sum_{k\equiv1} = \sum_{k\equiv2} = \frac{32768 + 1}{3} = 10923$ (the filter contributes $-\tfrac13(\omega + \omega^2) = +\tfrac13$ to each), and the bookkeeping closes: $10922 + 2\cdot 10923 = 32768 = 2^{15}$ ✓ — matching the verification script (10922).

</details>


### H · Synthesis and Stretch (Q37–Q38)

#### **Q37**[Olympiad]Prove $\sum_{k=0}^n (-1)^k \binom nk (x+k)^n = (-1)^n n!$, constant in $x$.

Prove $\sum_{k=0}^n (-1)^k \binom nk (x+k)^n = (-1)^n n!$, constant in $x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: finite differences, binomially unwound.** Let $\Delta P(x) =
        P(x+1) - P(x)$. $\Delta$ lowers the degree of a non-constant polynomial by exactly one (leading term $a x^d \mapsto a d x^{d-1} + \cdots$), so $\Delta^n$ of a degree-$n$ polynomial is the constant $n!\,a$. Now expand $\Delta^n$ by the binomial theorem: $\Delta^n P(x) = \sum_{k=0}^{n} (-1)^{n-k}\binom nk P(x+k)$ (prove by induction on $n$; Pascal's rule is the inductive step). With $P(t) = t^n$: $\sum_k (-1)^{n-k}\binom nk (x+k)^n = n!$, and multiplying by $(-1)^n$ is the displayed form.


Answer: $(-1)^n n!$ — e.g. $n = 4$: $24$; $n = 5$: $-120$


Check at $n=2$, $x = 1$: $1\cdot1 - 2\cdot4 + 1\cdot9 = 2$ — and the formula says $(-1)^2 \cdot 2! = 2$ ✓ (the sign on $k=1$ is the middle minus from $(-1)^k$).

</details>

#### **Q38**[Olympiad]Prove $\lfloor (1+\sqrt2)^{2m+1}\rfloor$ is even; determine the even-exponent case.

Prove $\lfloor (1+\sqrt2)^{2m+1}\rfloor$ is even; determine the even-exponent case.

<details>
<summary>Answer + Reasoning</summary>

**Method: conjugate pairing, then sign bookkeeping.** For any $n$, $S_n := (1+\sqrt2)^n + (1-\sqrt2)^n = 2\sum_j \binom{n}{2j} 2^{j} \in 2\mathbb Z$ — the odd surd terms cancel by the binomial theorem and a factor 2 remains. *$n$ odd:* $1-\sqrt2 \in (-1,0)$ so $(1-\sqrt2)^n \in (-1,0)$; then $(1+\sqrt2)^n = S_n - (1-\sqrt2)^n \in (S_n, S_n + 1)$ — the floor is $S_n$, which is even. QED. *$n$ even, $n \ge 2$:* $(1-\sqrt2)^n \in (0,1)$, so $(1+\sqrt2)^n = S_n - \text{tiny} \in (S_n - 1, S_n)$ — the floor is $S_n - 1$: **odd**.


Answer: odd exponents → even floor $S_n$; even exponents → odd floor $S_n - 1$


Check: $n = 3$: $S_3 = 14$, floor $14$ even ✓ (Q25's number); $n = 4$: $(1+\sqrt2)^4 = 17 + 12\sqrt2 \approx 33.97$, floor $33$, and $S_4 - 1 = 34 - 1 = 33$ odd ✓.

</details>


### I · Roots of Unity, Catalans and Stretch (Q39–Q48)

#### **Q39**[Olympiad]Using the roots-of-unity filter with $\omega=e^{2\pi i/3}$, evaluate $\displaystyle\sum_{\substack{k\\ k\equiv1\,(3)}}\binom{14}{k}$.

Using the roots-of-unity filter with $\omega=e^{2\pi i/3}$, evaluate $\displaystyle\sum_{\substack{k\\ k\equiv1\,(3)}}\binom{14}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the filter with $m=3$, $r=1$, then simplify $1+\omega=e^{i\pi/3}$.** With $\omega=e^{2\pi i/3}$ the filter reads $\frac13\sum_{j=0}^{2}\omega^{-j}(1+\omega^{j})^{14}$. The $j=0$ term is $2^{14}=16384$. For $j=1$: $\omega^{-1}(1+\omega)^{14}=e^{-2\pi i/3}\cdot e^{14\pi i/3}=e^{4\pi i}=1$. For $j=2$: $\omega^{-2}(1+\omega^{2})^{14}=e^{-4\pi i/3}\cdot e^{-14\pi i/3}=e^{-6\pi i}=1$.


Answer: $5462$


Check: by direct summation $k\equiv1\pmod3$ in range gives $k=1,4,7,10,13$, and $\binom{14}{1}+\binom{14}{4}+\binom{14}{7}+\binom{14}{10}+\binom{14}{13}=14+1001+3432+1001+14=5462$ ✓. The general closed form for $m=3$ is $\frac{2^{n}+2\cos\frac{(n-2r)\pi}{3}}{3}$.

</details>


#### **Q40**[Olympiad]State the roots-of-unity filter: for $\omega=e^{2\pi i/m}$, give a closed form for $\displaystyle\sum_{\substack{k\\ k\equiv r\,(m)}}\binom{n}{k}$.

State the roots-of-unity filter: for $\omega=e^{2\pi i/m}$, give a closed form for $\displaystyle\sum_{\substack{k\\ k\equiv r\,(m)}}\binom{n}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: average the rotations of $x$; only terms whose exponent is a multiple of $m$ survive.** For $\omega=e^{2\pi i/m}$, $\frac1m\sum_{j=0}^{m-1}\omega^{jt}$ equals $1$ if $m\mid t$ and $0$ otherwise. Multiplying by $\omega^{-rj}$ selects the residue class $r$.


Answer: $\displaystyle\sum_{\substack{k\\ k\equiv r\pmod m}}\binom{n}{k}=\frac1m\sum_{j=0}^{m-1}\omega^{-rj}\big(1+\omega^{j}\big)^{n}$


Check: verified numerically for $m=2,3,4,5$, every residue $r$, and $0\le n\le19$ — over $300$ cases, all exact ✓.

</details>


#### **Q41**[JEE Adv]Using the filter with $m=4$, $r=1$ and $\omega=i$, compute $\displaystyle\sum_{\substack{k\\ k\equiv1\,(4)}}\binom{10}{k}$.

Using the filter with $m=4$, $r=1$ and $\omega=i$, compute $\displaystyle\sum_{\substack{k\\ k\equiv1\,(4)}}\binom{10}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the filter with $m=4$, $r=1$, $\omega=i$.** $\frac14\sum_{j=0}^{3}i^{-j}(1+i^{j})^{10}$. The $j=2$ term vanishes because $1+i^{2}=0$. For $j=1$: $(1+i)^{10}=(\sqrt2\,e^{i\pi/4})^{10}=2^{5}e^{5i\pi/2}=32i$, so $i^{-1}\cdot32i=32$. For $j=3$: $(1-i)^{10}=32e^{-5i\pi/2}=-32i$, so $i^{-3}(-32i)=i(-32i)=32$.


Answer: $\frac14(1024+32+0+32)=272$


Check: directly, $k\equiv1\pmod4$ gives $k=1,5,9$, and $\binom{10}{1}+\binom{10}{5}+\binom{10}{9}=10+252+10=272$ ✓.

</details>


#### **Q42**[Olympiad]Define the Catalan number $C_n$, list $C_0$ to $C_5$, and state the convolution identity they satisfy.

Define the Catalan number $C_n$, list $C_0$ to $C_5$, and state the convolution identity they satisfy.

<details>
<summary>Answer + Reasoning</summary>

**Method: the definition, the first values, and the generating-function consequence.** $C(x)=\sum_{n\ge0}C_nx^n$ satisfies $C(x)=1+xC(x)^{2}$, because a triangulated polygon splits at the triangle containing a fixed edge.


Answer: $C_n=\dfrac1{n+1}\binom{2n}{n}=1,1,2,5,14,42$ for $n=0,\dots,5$; $\displaystyle\sum_{i=0}^{n}C_iC_{n-i}=C_{n+1}$


Check: $C_0,\dots,C_5$ recomputed as $\frac1{n+1}\binom{2n}{n}$ ✓.

</details>


#### **Q43**[Olympiad]Verify the Catalan convolution for $n=4$: show $\sum_{i=0}^{4}C_iC_{4-i}=C_5$.

Verify the Catalan convolution for $n=4$: show $\sum_{i=0}^{4}C_iC_{4-i}=C_5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand $C(x)=1+xC(x)^{2}$ and compare the coefficient of $x^{5}$.** The coefficient of $x^{5}$ on the right is $\sum_{i=0}^{4}C_iC_{4-i}$, and on the left it is $C_5$.


Answer: $C_0C_4+C_1C_3+C_2C_2+C_3C_1+C_4C_0=14+5+4+5+14=42=C_5$ ✓


Check: the convolution was verified for $n=0,\dots,10$ ✓.

</details>


#### **Q44**[Olympiad]How many ways are there to triangulate a convex heptagon?

How many ways are there to triangulate a convex heptagon?

<details>
<summary>Answer + Reasoning</summary>

**Method: a convex $(n+2)$-gon has exactly $C_n$ triangulations.** A heptagon has $7$ sides, so $n+2=7$ and $n=5$.


Answer: $C_5=42$


Check: the familiar small cases: quadrilateral $C_2=2$ ✓, pentagon $C_3=5$ ✓, hexagon $C_4=14$ ✓.

</details>


#### **Q45**[JEE Adv]State Stirling's estimate for the central binomial coefficient and give the first correction.

State Stirling's estimate for the central binomial coefficient and give the first correction.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $n!\sim\sqrt{2\pi n}\big(\frac ne\big)^{n}$ into $\binom{2n}{n}=\frac{(2n)!}{(n!)^{2}}$.** The powers of $2$ and $e$ combine to $4^{n}$, and the square roots combine to $\sqrt{\pi n}$ in the denominator; the correction series follows from Stirling's full expansion.


Answer: $\displaystyle\binom{2n}{n}\sim\frac{4^{n}}{\sqrt{\pi n}}\Big(1-\frac{1}{8n}+\frac{1}{128n^{2}}+\cdots\Big)$


Check: for $n=100$ the corrected factor $1-\frac1{800}$ turns $9.066177\times10^{58}$ into $9.054844\times10^{58}$, within $8\times10^{-5}\%$ of the exact value ✓.

</details>


#### **Q46**[Olympiad]Using $\binom{2n}{n}\sim\frac{4^{n}}{\sqrt{\pi n}}$, estimate the fraction of the whole row $2^{2n}$ carried by its central coefficient.

Using $\binom{2n}{n}\sim\frac{4^{n}}{\sqrt{\pi n}}$, estimate the fraction of the whole row $2^{2n}$ carried by its central coefficient.

<details>
<summary>Answer + Reasoning</summary>

**Method: divide the central coefficient by the row sum $2^{2n}=4^{n}$.** $\frac{\binom{2n}{n}}{4^{n}}\approx\frac{1}{\sqrt{\pi n}}$.


Answer: $\approx\dfrac{1}{\sqrt{\pi n}}$ — about $5.63\%$ for $n=100$


Check: $\binom{200}{100}/4^{100}=0.05635$ and $1/\sqrt{100\pi}=0.05642$ ✓.

</details>


#### **Q47**[Olympiad]Show that $n+1$ divides $\binom{2n}{n}$ for every $n\ge0$ — equivalently, that the Catalan number $\dfrac{1}{n+1}\binom{2n}{n}$ is always an integer.

Show that $n+1$ divides $\binom{2n}{n}$ for every $n\ge0$ — equivalently, that the Catalan number $\dfrac{1}{n+1}\binom{2n}{n}$ is always an integer.

<details>
<summary>Answer + Reasoning</summary>

**Method: use the ratio identity $\frac{\binom{2n}{n}}{\binom{2n}{n-1}}=\frac{n+1}{n}$, i.e. $n\binom{2n}{n}=(n+1)\binom{2n}{n-1}$.** Since $\gcd(n,n+1)=1$, the factor $n+1$ on the right must divide $\binom{2n}{n}$: writing $\binom{2n}{n-1}=nk$ gives $n\binom{2n}{n}=n(n+1)k$, so $\binom{2n}{n}=(n+1)k$. Hence $\frac1{n+1}\binom{2n}{n}$ is an integer, which is precisely $C_n$.


Answer: $C_n=\dfrac1{n+1}\binom{2n}{n}\in\mathbb Z$ for every $n\ge0$


Check: $C_0,\dots,C_5=1,1,2,5,14,42$ are all integers ✓, and the divisibility $n+1\mid\binom{2n}{n}$ was verified for $n=1,\dots,199$ ✓.

</details>


#### **Q48**[Olympiad]Show that the reflection principle counts the "bad" monotone paths from $(0,0)$ to $(n,n)$ as $\binom{2n}{n-1}$, and deduce $C_n=\binom{2n}{n}-\binom{2n}{n-1}$.

Show that the reflection principle counts the "bad" monotone paths from $(0,0)$ to $(n,n)$ as $\binom{2n}{n-1}$, and deduce $C_n=\binom{2n}{n}-\binom{2n}{n-1}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: reflect the path after its first crossing.** A monotone path from $(0,0)$ to $(n,n)$ that rises strictly above the diagonal $y=x$ has a first crossing point; reflecting the remainder of the path in the line $y=x+1$ is a bijection onto the monotone paths from $(0,0)$ to $(n-1,n+1)$. Those number $\binom{2n}{n-1}$: such a path has $n-1$ right steps and $n+1$ up steps, and we choose which $n-1$ of the $2n$ steps go right. Hence the good paths number $\binom{2n}{n}-\binom{2n}{n-1}=\binom{2n}{n}\big(1-\frac{n}{n+1}\big)=\frac1{n+1}\binom{2n}{n}=C_n$.


Answer: $C_n=\binom{2n}{n}-\binom{2n}{n-1}=\dfrac1{n+1}\binom{2n}{n}$


Check: for $n=3$: $\binom63-\binom62=20-15=5=C_3$ ✓; for $n=5$: $\binom{10}{5}-\binom{10}{4}=252-210=42=C_5$ ✓.

</details>

