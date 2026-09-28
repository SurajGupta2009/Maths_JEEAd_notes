---
title: "Binomial Theorem — Olympiad Paper"
aliases:
  - Binomial-Theorem Paper
module: "Binomial-Theorem"
module_title: "Binomial Theorem"
type: paper
tags:
  - binomial-theorem
  - paper
  - olympiad
  - assessment
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[06-divisibility-parity-and-primes|Chapter 6]] · 📖 [[Binomial-Theorem|Binomial Theorem]] · ✅ [[Binomial-Theorem — Solutions|Solutions]] ➡

# Olympiad Paper · 48 questions

*Final assessment · whole module*

# Olympiad & JEE Advanced Paper — Binomial Theorem

48 questions in nine sections (A–I), JEE Main → JEE Advanced → Olympiad. Each section maps onto a chapter's signature move: A · counting roots, B · coefficient machinery, C · identity engines, D · infinite expansions, E · size and extremes, F · divisibility, G · Lucas/Kummer/parity, H · synthesis and stretch, I · roots-of-unity filter, Catalan numbers and the Stirling frontier. **Do it cold, on paper.** Suggested time: 4 h. Short-form answers are given; full worked solutions are in [the companion file](#solutions).

### Supplementary notes

**Instructions.** Each question is tagged with difficulty. "Prove" questions earn marks only for a complete argument — a claim without proof earns none. Numeric answers are expected fully reduced unless stated otherwise.


### A · Binomial from Counting (Q1–Q5)

#### **Q1**[JEE Main]Find the coefficient of $x^6$ in $(1-2x)^9$.

Find the coefficient of $x^6$ in $(1-2x)^9$.


Answer: $5376$ (i.e. $\binom96 (−2)^6 = 84 \cdot 64$)

#### **Q2**[JEE Main]Find the sum of the coefficients of $(3x^2 - 2x + 1)^5$.

Find the sum of the coefficients of $(3x^2 - 2x + 1)^5$.


Answer: $(3-2+1)^5 = 32$

#### **Q3**[JEE Main]How many distinct terms remain after collecting like terms in $(a+b+c)^{10}$?

How many distinct terms remain after collecting like terms in $(a+b+c)^{10}$?


Answer: $\binom{12}{2} = 66$

#### **Q4**[JEE Adv]In the expansion of $(1+x)^{13}$, the coefficients of $x^r$ and $x^{r+3}$ are equal. Find…

In the expansion of $(1+x)^{13}$, the coefficients of $x^r$ and $x^{r+3}$ are equal. Find $r$, and the common value.


Answer: $r = 5$; both coefficients $= \binom{13}{5} = 1287$

#### **Q5**[JEE Adv]Prove $\sum_{k=0}^n \binom{n}{k} = 2^n$ by an explicit bijection between the two counted…

Prove $\sum_{k=0}^n \binom{n}{k} = 2^n$ by an explicit bijection between the two counted sets — no algebraic substitution permitted.


Answer: subsets of $[n]$ grouped by size vs. in/out decisions


### B · Coefficient Machinery (Q6–Q11)

#### **Q6**[JEE Main]Find the coefficient of $x^5$ in $(1+x)^{10} + (1+x)^{11}$, and rewrite it using only…

Find the coefficient of $x^5$ in $(1+x)^{10} + (1+x)^{11}$, and rewrite it using only row-10 entries plus one identity's name.


Answer: $\binom{10}{5} + \binom{11}{5} = 252 + 462 = 714$; via Pascal's rule the same number is $\binom{10}{4} + 2\binom{10}{5}$

#### **Q7**[JEE Adv]Find the coefficient of $x^{-2}$ in $\left(x^2 + \dfrac{1}{x^3}\right)^9$.

Find the coefficient of $x^{-2}$ in $\left(x^2 + \dfrac{1}{x^3}\right)^9$.


Answer: $126$ (from $18 - 5k = -2 \Rightarrow k = 4$, $\binom94$)

#### **Q8**[JEE Adv]Find the coefficient of $x^4$ in $(1+x+x^2)^5$.

Find the coefficient of $x^4$ in $(1+x+x^2)^5$.


Answer: $45$

#### **Q9**[JEE Adv]The sum of the coefficients of $(1+2x)^n$ is $6561$. Find $n$.

The sum of the coefficients of $(1+2x)^n$ is $6561$. Find $n$.


Answer: $3^n = 6561 = 3^8$, so $n = 8$

#### **Q10**[JEE Adv]In $(1+x)^n$ the binomial coefficients of the 4th and 8th terms are equal. Find $n$ and the…

In $(1+x)^n$ the binomial coefficients of the 4th and 8th terms are equal. Find $n$ and the greatest binomial coefficient of that row.


Answer: $n = 10$; greatest coefficient $\binom{10}{5} = 252$

#### **Q11**[Olympiad]Prove that the central coefficient of $(1+x)^{2n}$ satisfies…

Prove that the central coefficient of $(1+x)^{2n}$ satisfies $\dbinom{2n}{n} \gt \dfrac{4^n}{2n+1}$, and evaluate it at $n = 6$ against the bound.


Answer: $924 \gt \tfrac{4096}{13} \approx 315.1$


### C · The Identity Toolkit (Q12–Q16)

#### **Q12**[JEE Main]Evaluate $\displaystyle\sum_{k=0}^{6} \frac{\binom{6}{k}}{k+1}$ exactly.

Evaluate $\displaystyle\sum_{k=0}^{6} \frac{\binom{6}{k}}{k+1}$ exactly.


Answer: $\dfrac{2^7 - 1}{7} = \dfrac{127}{7}$

#### **Q13**[JEE Main]Evaluate $\displaystyle\sum_{k=0}^{4} k\binom{4}{k} 2^{-k}$.

Evaluate $\displaystyle\sum_{k=0}^{4} k\binom{4}{k} 2^{-k}$.


Answer: $\dfrac{27}{4}$ (from $xf'(x)$ at $x = \tfrac12$)

#### **Q14**[JEE Adv]Evaluate $\displaystyle\sum_{k=0}^{10} \frac{(-1)^k}{k+1}\binom{10}{k}$.

Evaluate $\displaystyle\sum_{k=0}^{10} \frac{(-1)^k}{k+1}\binom{10}{k}$.


Answer: $\dfrac{1}{11}$ (integrate $(1-x)^{10}$ on $[0,1]$)

#### **Q15**[JEE Adv]Find $\displaystyle\sum_{k} k\binom{12}{k}$, the sum over even $k$ only.

Find $\displaystyle\sum_{k} k\binom{12}{k}$, the sum over even $k$ only.


Answer: $12 \cdot 2^{10} = 12288$ (the full sum $n2^{n-1}$ splits in half because $\sum k\binom nk(-1)^k = 0$)

#### **Q16**[JEE Adv]Prove $\displaystyle\sum_{k=0}^{n} \frac{\binom{n}{k}}{k+1} = \frac{2^{n+1}-1}{n+1}$ by…

Prove $\displaystyle\sum_{k=0}^{n} \frac{\binom{n}{k}}{k+1} = \frac{2^{n+1}-1}{n+1}$ by integrating the master polynomial, and deduce $\sum_k \frac{(-1)^k}{k+1}\binom{n}{k} = \frac{1}{n+1}$.


Answer: $\int_0^1 (1+x)^n$ and $\int_0^1 (1-x)^n$ — one engine, two settings


### D · Infinite Expansions (Q17–Q22)

#### **Q17**[JEE Main]Find the coefficient of $x^6$ in $(1-x)^{-4}$.

Find the coefficient of $x^6$ in $(1-x)^{-4}$.


Answer: $\binom{4+6-1}{6} = \binom96 = 84$

#### **Q18**[JEE Main]Expand $(3+2x)^{-2}$ in ascending powers of $x$ up to the linear term, and state the…

Expand $(3+2x)^{-2}$ in ascending powers of $x$ up to the linear term, and state the validity condition.


Answer: $\dfrac19 - \dfrac{4x}{27} + \cdots,\ \ |x| \lt \dfrac32$

#### **Q19**[JEE Adv]Find the coefficient of $x^5$ in $(1+x)^{-1/2}$.

Find the coefficient of $x^5$ in $(1+x)^{-1/2}$.


Answer: $-\dfrac{63}{256}$

#### **Q20**[JEE Adv]Evaluate $1 + 2(0.9) + 3(0.9)^2 + 4(0.9)^3 + \cdots$ exactly.

Evaluate $1 + 2(0.9) + 3(0.9)^2 + 4(0.9)^3 + \cdots$ exactly.


Answer: $(1 - 0.9)^{-2} = 100$

#### **Q21**[JEE Adv]Use the first four terms of $(1+x)^{1/2}$ to estimate $\sqrt{1.04}$ correct to five decimal…

Use the first four terms of $(1+x)^{1/2}$ to estimate $\sqrt{1.04}$ correct to five decimal places, justifying the error.


Answer: $1.01980$ (four-term value $1.019804$; first dropped term $< 10^{-6}$)

#### **Q22**[Olympiad]Prove Bernoulli's inequality $(1+x)^n \ge 1 + nx$ for $x \ge 0$, $n \in \mathbb N$, by…

Prove Bernoulli's inequality $(1+x)^n \ge 1 + nx$ for $x \ge 0$, $n \in \mathbb N$, by truncating the binomial expansion, and use two kept terms to show $1.01^{50} \gt 1.6$.


Answer: bound $1 + 0.5 + 0.1225 = 1.6225 \gt 1.6$


### E · Size, Growth and Extremes (Q23–Q27)

#### **Q23**[JEE Main]Prove that $\left(1 + \frac{1}{n}\right)^n \lt 3$ for every integer $n \ge 1$.

Prove that $\left(1 + \frac{1}{n}\right)^n \lt 3$ for every integer $n \ge 1$.


Answer: expand, dominate the $k$-th summand by $2^{1-k}$, geometric series

#### **Q24**[JEE Adv]Show that $a_n = \left(1 + \frac1n\right)^n$ is strictly increasing in $n$.

Show that $a_n = \left(1 + \frac1n\right)^n$ is strictly increasing in $n$.


Answer: termwise comparison of the two expansions via $\frac{n-j}{n} \lt \frac{n+1-j}{n+1}$

#### **Q25**[JEE Adv]Find $\left\lfloor (1+\sqrt2)^3 \right\rfloor$ without approximating $\sqrt 2$.

Find $\left\lfloor (1+\sqrt2)^3 \right\rfloor$ without approximating $\sqrt 2$.


Answer: $14$ (conjugate sum $= 14$ exactly; dust $\in (0,1)$)

#### **Q26**[JEE Adv]Find the numerically greatest term in the expansion of $(3+2x)^{10}$ at $x = 1$.

Find the numerically greatest term in the expansion of $(3+2x)^{10}$ at $x = 1$.


Answer: $T_5 = \binom{10}{4} 3^6 2^4 = 2449440$

#### **Q27**[Olympiad]Prove $2^n \gt n^2$ for all integers $n \ge 5$, keeping four symmetric terms of $(1+1)^n$…

Prove $2^n \gt n^2$ for all integers $n \ge 5$, keeping four symmetric terms of $(1+1)^n$ (and checking the small cases honestly).


Answer: $\frac{n(n^2-1)}{3} \gt n^2 \iff n^2 - 1 \gt 3n$ for $n \ge 7$; $n = 5, 6$ by hand


### F · Divisibility and Remainders (Q28–Q32)

#### **Q28**[JEE Main]Prove that for prime $p$ and $0 \lt k \lt p$, $p \mid \binom{p}{k}$; deduce…

Prove that for prime $p$ and $0 \lt k \lt p$, $p \mid \binom{p}{k}$; deduce $2^7 \equiv 2 \pmod 7$.


Answer: coprime-denominator argument; $128 = 7\cdot18 + 2$

#### **Q29**[JEE Main]Find the remainder when $3^{37} - 3$ is divided by $37$.

Find the remainder when $3^{37} - 3$ is divided by $37$.


Answer: $0$ — Freshman's Dream twice: $3^{37} = (1+2)^{37} \equiv 1 + 2^{37}$ and $2^{37} = (1+1)^{37} \equiv 2$

#### **Q30**[JEE Adv]How many trailing zeros does $200!$ have?

How many trailing zeros does $200!$ have?


Answer: $40 + 8 + 1 = 49$

#### **Q31**[JEE Adv]Find the remainder when $6^{999} + 1$ is divided by $5$.

Find the remainder when $6^{999} + 1$ is divided by $5$.


Answer: $2$

#### **Q32**[Olympiad]Prove: if a prime $p$ divides every interior entry of row $n$ of Pascal's triangle, then…

Prove: if a prime $p$ divides every interior entry of row $n$ of Pascal's triangle, then $n = p^e$ for some $e \ge 1$. (Converse too.)


Answer: valuation formula $v_p\binom nk = \frac{s_p(k)+s_p(n-k)-s_p(n)}{p-1}$; test $k = p^e$


### G · Parity, Lucas and Kummer (Q33–Q36)

#### **Q33**[JEE Adv]How many entries of row $2024$ of Pascal's triangle are odd?

How many entries of row $2024$ of Pascal's triangle are odd?


Answer: $2^{7} = 128$ ($2024 = 1111110100_2$)

#### **Q34**[JEE Adv]Find the highest power of $2$ dividing $\binom{20}{10}$.

Find the highest power of $2$ dividing $\binom{20}{10}$.


Answer: $2^2 = 4$ (two carries in $1010_2 + 1010_2$)

#### **Q35**[JEE Adv]Compute $\binom{10}{3} \pmod 7$ by Lucas' theorem, and then $\pmod 2$. Why do the digit…

Compute $\binom{10}{3} \pmod 7$ by Lucas' theorem, and then $\pmod 2$. Why do the digit tests give different verdicts, and why is that consistent?


Answer: $120 \equiv 1 \pmod 7$, $120 \equiv 0 \pmod 2$

#### **Q36**[Olympiad]Using the roots-of-unity filter with $\omega = e^{2\pi i/3}$, compute…

Using the roots-of-unity filter with $\omega = e^{2\pi i/3}$, compute $\displaystyle\sum_{k \equiv 0\,(3)} \binom{15}{k}$.


Answer: $\dfrac{2^{15} + 2\,\mathrm{Re}\,(1+\omega)^{15}}{3} = \dfrac{32768 - 2}{3} = 10922$


### H · Synthesis and Stretch (Q37–Q38)

#### **Q37**[Olympiad]Prove that for every real $x$ and integer $n \ge 1$,

Prove that for every real $x$ and integer $n \ge 1$, 
$$ \sum_{k=0}^{n} (-1)^k \binom{n}{k} (x+k)^n \;=\; (-1)^n\, n!, $$
 i.e. the sum is constant in $x$. (Hint: finite differences drop degree; the $n$-th difference of $t^n$ is $n!$.)


Answer: $(-1)^n n!$ — e.g. $n = 4$: $24$; $n = 5$: $-120$

#### **Q38**[Olympiad]Prove that for every $m \ge 0$, the integer part…

Prove that for every $m \ge 0$, the integer part $\left\lfloor (1+\sqrt2)^{2m+1} \right\rfloor$ is **even** — and determine its parity for even exponents.


Answer: odd exponents → even floor ($= S_{2m+1}$); even exponents $2m \ge 2$ → odd floor ($= S_{2m} - 1$)


### I · Roots of Unity, Catalans and Stretch (Q39–Q48)

#### **Q39**[Olympiad]Using the roots-of-unity filter with $\omega=e^{2\pi i/3}$, evaluate $\displaystyle\sum_{\substack{k\\ k\equiv1\,(3)}}\binom{14}{k}$.

Using the roots-of-unity filter with $\omega=e^{2\pi i/3}$, evaluate $\displaystyle\sum_{\substack{k\\ k\equiv1\,(3)}}\binom{14}{k}$.


Answer: $\dfrac{2^{14}+2\cos\big(\tfrac{(14-2)\pi}{3}\big)}{3}=\dfrac{16384+2}{3}=5462$ (the $r=1$ shift replaces $\tfrac{n\pi}{3}$ by $\tfrac{(n-2)\pi}{3}$; here $\cos4\pi=1$)

#### **Q40**[Olympiad]State the roots-of-unity filter: for $\omega=e^{2\pi i/m}$, give a closed form for $\displaystyle\sum_{\substack{k\\ k\equiv r\,(m)}}\binom{n}{k}$.

State the roots-of-unity filter: for $\omega=e^{2\pi i/m}$, give a closed form for $\displaystyle\sum_{\substack{k\\ k\equiv r\,(m)}}\binom{n}{k}$.


Answer: $\dfrac1m\displaystyle\sum_{j=0}^{m-1}\omega^{-rj}(1+\omega^{j})^{n}$

#### **Q41**[JEE Adv]Using the filter with $m=4$, $r=1$ and $\omega=i$, compute $\displaystyle\sum_{\substack{k\\ k\equiv1\,(4)}}\binom{10}{k}$.

Using the filter with $m=4$, $r=1$ and $\omega=i$, compute $\displaystyle\sum_{\substack{k\\ k\equiv1\,(4)}}\binom{10}{k}$.


Answer: $\binom{10}{1}+\binom{10}{5}+\binom{10}{9}=10+252+10=272$

#### **Q42**[Olympiad]Define the Catalan number $C_n$, list $C_0$ to $C_5$, and state the convolution identity they satisfy.

Define the Catalan number $C_n$, list $C_0$ to $C_5$, and state the convolution identity they satisfy.


Answer: $C_n=\dfrac1{n+1}\binom{2n}{n}=1,1,2,5,14,42$; $\displaystyle\sum_{i=0}^{n}C_iC_{n-i}=C_{n+1}$

#### **Q43**[Olympiad]Verify the Catalan convolution for $n=4$: show $\sum_{i=0}^{4}C_iC_{4-i}=C_5$.

Verify the Catalan convolution for $n=4$: show $\sum_{i=0}^{4}C_iC_{4-i}=C_5$.


Answer: $C_0C_4+C_1C_3+C_2C_2+C_3C_1+C_4C_0=14+5+4+5+14=42=C_5$

#### **Q44**[Olympiad]How many ways are there to triangulate a convex heptagon?

How many ways are there to triangulate a convex heptagon?


Answer: $42$ — a convex $(n+2)$-gon has $C_n$ triangulations, and $7=5+2$ so $n=5$

#### **Q45**[JEE Adv]State Stirling's estimate for the central binomial coefficient and give the first correction.

State Stirling's estimate for the central binomial coefficient and give the first correction.


Answer: $\binom{2n}{n}\sim\dfrac{4^{n}}{\sqrt{\pi n}}\Big(1-\dfrac{1}{8n}+\dfrac{1}{128n^{2}}+\cdots\Big)$

#### **Q46**[Olympiad]Using $\binom{2n}{n}\sim\frac{4^{n}}{\sqrt{\pi n}}$, estimate the fraction of the whole row $2^{2n}$ carried by its central coefficient.

Using $\binom{2n}{n}\sim\frac{4^{n}}{\sqrt{\pi n}}$, estimate the fraction of the whole row $2^{2n}$ carried by its central coefficient.


Answer: $\dfrac{\binom{2n}{n}}{2^{2n}}\approx\dfrac{1}{\sqrt{\pi n}}$ (about $5.6\%$ for $n=100$)

#### **Q47**[Olympiad]Show that $n+1$ divides $\binom{2n}{n}$ for every $n\ge0$ — equivalently, that the Catalan number $\dfrac{1}{n+1}\binom{2n}{n}$ is always an integer.

Show that $n+1$ divides $\binom{2n}{n}$ for every $n\ge0$ — equivalently, that the Catalan number $\dfrac{1}{n+1}\binom{2n}{n}$ is always an integer.


Answer: $\dfrac{\binom{2n}{n}}{\binom{2n}{n-1}}=\dfrac{n+1}{n}$, i.e. $n\binom{2n}{n}=(n+1)\binom{2n}{n-1}$; since $\gcd(n,n+1)=1$ it follows that $n+1\mid\binom{2n}{n}$

#### **Q48**[Olympiad]Show that the reflection principle counts the "bad" monotone paths from $(0,0)$ to $(n,n)$ as $\binom{2n}{n-1}$, and deduce $C_n=\binom{2n}{n}-\binom{2n}{n-1}$.

Show that the reflection principle counts the "bad" monotone paths from $(0,0)$ to $(n,n)$ as $\binom{2n}{n-1}$, and deduce $C_n=\binom{2n}{n}-\binom{2n}{n-1}$.


Answer: reflecting after the first crossing bijects bad paths with paths from $(0,0)$ to $(n-1,n+1)$, of which there are $\binom{2n}{n-1}$; hence $C_n=\binom{2n}{n}\big(1-\frac{n}{n+1}\big)=\frac1{n+1}\binom{2n}{n}$


### 📝 Exam technique notes

> **📝 Exam technique notes**
>
> - **Proof questions (Q5, Q11, Q16, Q22–Q24, Q27, Q28, Q32, Q36–Q38, Q47, Q48):** write the chain of implications, not just the claim — "all middle terms vanish mod $p$" must come with *why the denominator cannot cancel*.
> - **Validity ranges (Q18, Q21):** the answer is a pair — series *and* $|x|$-condition. A series outside its radius is not a wrong number, it is not a number.
> - **Approximation questions:** state the first dropped term's size in one sentence; that sentence is the difference between "estimate" and "certified digit".
> - **Lucas-type questions (Q33–Q36):** check the digit condition $k_i \le n_i$ *before* multiplying products; a single violating digit sends the whole residue to $0$, and that is an answer, not an error.
- **Roots-of-unity filter (Q39–Q41):** write $\frac1m\sum_{j}\omega^{-rj}(1+\omega^j)^n$ first, then simplify each $1+\omega^j$ to a polar form — the answer must come out an integer, and a non-integer means a phase slipped.
- **Catalan questions (Q42–Q44):** name the bijection you are using (triangulation, bracketing, lattice path); the same integer $C_n$ arrives from three different counts and they must agree.
- **Stirling estimates (Q45, Q46):** quote $\frac{4^n}{\sqrt{\pi n}}$ and state the size of the first dropped term, $\frac1{8n}$; an unqualified estimate is not an answer.
> - **Greatest-term questions (Q26):** report the term *number* ($T_5$, i.e. $k = 4$) and its value; the ratio walk must be shown, not just the peak.
