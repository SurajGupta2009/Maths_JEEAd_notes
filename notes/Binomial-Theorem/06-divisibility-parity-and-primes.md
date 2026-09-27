---
title: "Chapter 6 — Divisibility, Parity and Primes"
aliases:
  - Divisibility, Parity and Primes
  - Ch 6 — Divisibility, Parity and Primes
module: "Binomial-Theorem"
module_title: "Binomial Theorem"
chapter: 6
level: synthesis
tags:
  - binomial-theorem
  - chapter
  - synthesis
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Binomial-Theorem|Binomial Theorem]] · ⬅ [[05-size-growth-and-extremes|Chapter 5]] · [[Binomial-Theorem — Paper|Olympiad Paper]] ➡ · 📝 [[Binomial-Theorem — Paper|Olympiad Paper]] · ✅ [[Binomial-Theorem — Solutions|Solutions]]

# Chapter 6 — Divisibility, Parity and Primes

*4 sections · 10 questions*

*Chapter 6 of 6*

# Divisibility, Parity and Primes

The binomial coefficient $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ hides prime factorisations inside a division — Chapter 5 already used the case $p \mid \binom{p}{k}$, the single most recycled lemma in olympiad number theory. This chapter makes the whole machinery explicit: primality forcing, Legendre's valuation formula, Kummer's carry-count, Lucas' theorem, and the parity fractal of Pascal's triangle. The prize at the end — Wolstenholme's congruence $\binom{2p}{p} \equiv 2 \pmod{p^3}$ — is a genuine research-adjacent result you can fully prove with only what is here.

### 6.0 What you will be able to do

- Prove $p \mid \binom{p}{k}$ for prime $p$ in one line, and watch it produce Fermat's little theorem, $(a+b)^p \equiv a^p + b^p$, and parity fractals.
- Count exact powers of a prime in a factorial (Legendre) and in a binomial coefficient — trailing zeros become arithmetic, not folklore.
- State and use Kummer's theorem: $v_p\binom{n}{k}$ = number of carries when adding $k + (n-k)$ in base $p$.
- Reduce any binomial coefficient mod $p$ with Lucas' theorem, and count odd entries of any row as $2^{s_2(n)}$.
- Filter sums by residue class with cube roots of unity — the roots-of-unity filter, the sharpest tool in the row-sum armoury.


### 6.1 Prime rows and the Freshman's Dream

> [!abstract] First Principles — why the prime rows are special
>
> $\binom{p}{k} = \frac{p\,(p-1) \cdots (p-k+1)}{k!}$: the numerator carries one factor $p$, and the denominator $k!$ is coprime to $p$ — every factor $1 \le j \le k \le p-1$ avoids it. Since $\binom pk$ is a whole number and $p \cdot \big[(p-1)\cdots(p-k+1)\big] = \binom pk \cdot k!$ exhibits $p$ dividing a product in which the second factor cannot absorb it, $p \mid \binom pk$ for $0 \lt k \lt p$. Setting $a = b = 1$: $2^p = \sum_k \binom pk \equiv 2 \pmod p$ — Fermat for base 2. Setting general $a, b$: the **Freshman's Dream** $(a+b)^p \equiv a^p + b^p \pmod p$, which iterating gives $a^p \equiv a$.

And the converse carries real content: if $\binom{n}{k}$ is divisible by some fixed prime for *all* interior $k$, then $n$ must be a power of that prime. (Row $n = 8$: all of $8, 28, 56, 70, 56, 28, 8$ are even, and $8 = 2^3$. Row 6 fails for 2 at $\binom62 = 15$, and 6 is not a prime power.)

> [!warning] Common Trap — primality of the row index is not cosmetic
>
> The Freshman's Dream fails the moment the exponent is composite: $(a+b)^4$ has middle term $6a^2b^2$, and $6 \not\equiv 0 \pmod 4$ — nor is $6$ divisible by every prime power at stake. "All middle terms vanish" works mod $p$ for prime $p$ only; for composite exponents the valuation question goes through Kummer/Lucas, not through optimism. When a solution says "all middle terms vanish mod $p$", the word $p$ must name a prime, and $0 \lt k \lt n$ must be the interior range of *this* $n$.

#### Worked examples

#### **S13**[JEE Main][solved][modular sieve]Find the remainder when [formula] is divided by 5.

Find the remainder when $6^{999} + 1$ is divided by 5.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: expand around the modulus.** $6^{999} = (5+1)^{999}
        = \sum_k \binom{999}{k} 5^k$. Every term with $k \ge 1$ is a multiple of 5; the survivor is $1$. So $6^{999} + 1 \equiv 2 \pmod 5$.


Answer: **Answer: $2$**


**Check:** $6^2 = 36 \equiv 1$, so $6^{998} \equiv 1$ and $6^{999} \equiv 6 \equiv 1$ ✓.

</details>

#### **S14**[JEE Adv][solved][Legendre]How many trailing zeros does [formula] end in? State and prove the general for…

How many trailing zeros does $50!$ end in? State and prove the general formula you are using.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: count prime factors.** A trailing zero is a factor 10 = 2·5, and factorials are 2-rich — fives are the bottleneck. Legendre: 
$$ v_5(n!) = \left\lfloor \frac n5 \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \cdots, $$
 because $\lfloor n/5 \rfloor$ counts the multiples of 5 once each, and the extra floor counts a second copy for multiples of 25, and so on. At $n = 50$: $10 + 2 = 12$.


Answer: **Answer: $12$**


**Check:** the multiples of 25 below 50 are 25, 50 — exactly the two numbers needing a second five ✓.

</details>

#### **S15**[Olympiad][solved][Lucas, carefully]Compute [formula] by Lucas' theorem, then [formula] , and explain why the two …

Compute $\binom{10}{3} \pmod 7$ by Lucas' theorem, then $\pmod 2$, and explain why the two answers feel contradictory but are not.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: digitwise reduction.** Base 7: $10 = (1,3)_7$, $3 = (0,3)_7$; Lucas says $\binom{10}{3} \equiv \binom10 \binom33 = 1 \pmod 7$ — and indeed $\binom{10}{3} = 120 = 7\cdot 17 + 1$ ✓. Base 2: $10 = (1,0,1,0)_2$, $3 = (1,1)_2$ — the second bit has $k_1 = 1 \gt n_1 = 0$, so $\binom{10}{3} \equiv 0 \pmod 2$.


Both are true: $120 \equiv 1 \pmod 7$ and $120 \equiv 0 \pmod 2$. The trap is in the middle step: Lucas' digitwise product can hit a $\binom{n_i}{k_i}$ with $k_i \gt n_i$, which is defined as $0$ — and one such zero annihilates the whole product. Check digits *before* trusting the answer.


Answer: **Answer: $\binom{10}{3} \equiv 1 \pmod 7, \quad 0 \pmod 2$**


**Check mod 2 by Pascal:** row 10 mod 2 is $1,0,1,0,0,0,0,0,1,0,1$ — the odd slots are $k \in \{0,2,8,10\}$, the subsets of the 1-bits of $10 = 1010_2$ — and position 3 is 0 ✓.

</details>



### 6.2 Kummer's theorem — the carries are the valuation

Legendre counts prime factors of a factorial; subtracting gives the binomial case. Kummer's theorem packages the subtraction into a picture:

$$ v_p \binom{n}{k} \;=\; \text{(number of carries when adding } k + (n-k) \text{ in base } p). $$

*Why it is true:* Legendre says $v_p(n!) = \frac{n - s_p(n)}{p-1}$ where $s_p$ is the base-$p$ digit sum (each floor in the sum removes a digit's worth). Then $v_p \binom{n}{k} = \frac{s_p(k) + s_p(n-k) - s_p(n)}{p-1}$. Carrying in base $p$ destroys exactly $p - 1$ units of digit sum per carry — so the count of carries is the valuation. One formula, two stories: floors on one side, carries on the other.

Worked instance: $v_2 \binom{20}{10}$. $10 = 1010_2$; adding $1010 + 1010$ in binary produces carries out of bit 1 and bit 3 — two carries — so $v_2 = 2$, i.e. the highest power of 2 dividing $\binom{20}{10}$ is $4$. (Check: $\binom{20}{10} = 184756 = 4 \times 46189$, and 46189 is odd ✓.)

> [!example] Olympiad Extension — Lucas' theorem and Sierpiński's gasket
>
> Write $n = \sum n_i p^i$, $k = \sum k_i p^i$ in base $p$. Then 
> $$ \binom{n}{k} \equiv \prod_i \binom{n_i}{k_i} \pmod p $$
>
>
>
> Proof in two moves: Freshman's Dream gives $(1+x)^{p^i} \equiv 1 + x^{p^i}$, hence $(1+x)^n = \prod_i (1+x)^{n_i p^i} \equiv \prod_i (1 + x^{p^i})^{n_i}$; the coefficient of $x^k$ picks the digitwise product. $\binom nk$ is *odd* iff no carries occur when forming $k + (n-k) = n$, i.e. iff every 1-bit of $k$ sits inside a 1-bit of $n$ ($k \mathbin{\&} \lnot n = 0$). Consequences: row $n$ has exactly $2^{s_2(n)}$ odd entries — row 2024 has $2^7 = 128$ — and the odd entries of rows $0..2^m-1$ draw Sierpiński's triangle. The parity of Pascal's triangle is a fractal, and Lucas is its generator.

#### The roots-of-unity filter — summing over residue classes

To sum $\binom{n}{k}$ only over $k \equiv r \pmod m$: average $f(\omega^j \zeta)$ with a weight $\zeta^{-jr}$, where $\zeta = e^{2\pi i/m}$. The $m$-th-root orthogonality kills every exponent not congruent to $r$. For $m = 3$, $n = 12$: the even/odd trick of Chapter 1 upgrades to


$$ \sum_{k \equiv 0 (3)} \binom{12}{k} = \frac{(1+1)^{12} + (1+\omega)^{12} + (1+\omega^2)^{12}}{3}
    = \frac{4096 + \omega^{24} + \bar\omega^{24}}{3} = \frac{4098}{3} = 1366, $$


using $1 + \omega = -\omega^2$. The two other classes come out 1365 each — and they must, since $1366 + 1365 + 1365 = 4096$ exactly.



### 6.3 Wolstenholme — the frontier, within reach

Everything so far is a run-up to this theorem: for prime $p \ge 5$, $\binom{2p}{p} \equiv 2 \pmod{p^3}$.

> [!abstract] First Principles — proof sketch
>
> Start from Chapter 3's coefficient engine: Vandermonde gives $\binom{2p}{p} = \sum_{k=0}^{p} \binom pk^2 = 2 + \sum_{k=1}^{p-1} \binom pk^2$ (the two endpoints are $1$ each). For interior $k$, $\binom pk = \frac pk \binom{p-1}{k-1}$, and every factor of $(p-1)(p-2)\cdots(p-k+1)$ is $-j$ mod $p$, so $\binom{p-1}{k-1}^2 \equiv 1 \pmod p$. Hence $\binom pk^2 \equiv p^2/k^2 \pmod{p^3}$ and 
> $$ \binom{2p}{p} \equiv 2 + p^2 \sum_{k=1}^{p-1} k^{-2} \pmod{p^3}. $$
>  The remaining sum dies by two moves: $k^{-2} \equiv k^{p-3} \pmod p$ (Fermat), and $\sum_{k=1}^{p-1} k^{m} \equiv 0 \pmod p$ whenever $p-1 \nmid m$ — multiply the sum by $g^{m}$ for a primitive root $g$, which permutes the nonzero residues, forcing $(g^m - 1) S \equiv 0$. For $p \ge 5$, $m = p-3$ satisfies $0 \lt m \lt p-1$, so the sum is $0$ mod $p$, the correction term is $0$ mod $p^3$. QED — four ideas, no technology beyond this module. ($p=3$ is where $m = 0 \equiv p-1$ and the argument breaks — which is exactly why $p \ge 5$ is in the statement.)

The verified instance (and the one you may be asked to check): $p = 5$: $\binom{10}{5} = 252 = 2 + 2\cdot 125 \equiv 2 \pmod{125}$. $p = 7$: $\binom{14}{7} = 3432 = 2 + 10 \cdot 343 \equiv 2 \pmod{343}$. The modulus $p^3$ — not $p^2$ — is the sharp part of the statement.

> [!tip] Key Idea — prime divisibility questions live in the factorials, not the formula
>
> Whenever a problem asks "what power of $p$ divides $\binom{n}{k}$", do not touch the factorial quotient directly: translate immediately — floors of $n/p^i$ (Legendre), carries in base $p$ (Kummer), digits (Lucas). The three views agree by design and disagree only in which one cracks the given problem. For $\binom{2p}{p}$ mod $p^3$ even $p^1$ is obvious and $p^3$ is Wolstenholme; Kummer tells you $v_p\binom{2p}{p} = 1$, i.e. $p \,\|\, \binom{2p}{p}$ — one carry, since $p + p = 2p$ carries exactly once in base $p$ — so the congruence $\equiv 2 \pmod{p^3}$ is *not* about divisibility at all: it is a statement that $\binom{2p}{p} - 2$ is the divisible one. Read congruences slowly.

#### Practice set — divisibility and primes

#### **P41**[JEE Main][practice][prime rows]Prove that for prime [formula] , [formula] for [formula] , and deduce [formula…

Prove that for prime $p$, $p \mid \binom{p}{k}$ for $0 \lt k \lt p$, and deduce $2^7 \equiv 2 \pmod 7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the coprime-denominator argument.** $\binom{p}{k} k! = p (p-1) \cdots (p-k+1)$: $p$ divides the RHS; no factor of $k!$ is divisible by $p$; so $p \mid \binom pk$. Then $2^7 = \sum_k \binom 7k = 1 + 7 + 21 + 35 + 35 + 21 + 7 + 1$: all six interior terms die mod 7, leaving $1 + 1 = 2$.


Answer: **proved; $2^7 = 128 = 7 \cdot 18 + 2$** ✓.

</details>

#### **P42**[JEE Adv][practice][Lucas parity]How many entries of row 20 of Pascal's triangle are odd?

How many entries of row 20 of Pascal's triangle are odd?

<details>
<summary>Answer + Reasoning</summary>

**Method: odd $=$ no carries $= 2^{s_2(n)}$.** $20 = 10100_2$ has two 1-bits, so exactly $2^2 = 4$ subsets of bits give odd $\binom{20}{k}$: the rows $k \in \{0, 4, 16, 20\}$.


Answer: **4**. (Direct: $\binom{20}{4} = 4845$ odd ✓, and $\binom{20}{1} = 20$ even ✓.)

</details>

#### **P43**[JEE Adv][practice][Lucas]Compute [formula] with Lucas' theorem.

Compute $\binom{10}{3} \pmod 7$ with Lucas' theorem.

<details>
<summary>Answer + Reasoning</summary>

**Method: base-7 digits.** $10 = (1,3)_7$, $3 = (0,3)_7$: $\binom{10}{3} \equiv \binom10 \binom33 = 1 \pmod 7$.


Answer: **1**. (Verify by hand: $120 = 119 + 1$ ✓. Compare with the mod-2 digit check of S15: same theorem, different base, different verdict — that is the point.)

</details>

#### **P44**[JEE Adv][practice][Legendre]How many zeros does [formula] end with?

How many zeros does $100!$ end with?

<details>
<summary>Answer + Reasoning</summary>

**Method: count fives.** $v_5(100!) = 20 + 4 = 24$.


Answer: **24**. (The 4 is for 25, 50, 75, 100 — one extra five each ✓.)

</details>

#### **P45**[Olympiad][practice][root-of-unity filter]Compute [formula] .

Compute $\sum_{k \equiv 1 \,(3)} \binom{12}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: filter with $\omega$.** The roots-of-unity filter is $\sum_{k \equiv r\,(3)} \binom{12}{k} = \frac13 \sum_{j=0}^{2} \omega^{-jr}(1+\omega^j)^{12}$. For $r = 1$: the $j = 0$ term is $2^{12} = 4096$; the $j = 1$ term is $\omega^{-1}(1+\omega)^{12} = \omega^{2}(-\omega^2)^{12} = \omega^2$, since $(-\omega^2)^{12} = \omega^{24} = 1$; the $j = 2$ term is its conjugate $\omega$. And $\omega^2 + \omega = -1$, so the value is $\frac{4096 - 1}{3} = 1365$.


Answer: **1365**. (Check against §6.2: classes 0, 1, 2 of row 12 are $1366 + 1365 + 1365 = 4096 = 2^{12}$ ✓ exactly.)

</details>

#### **P46**[Olympiad][practice][Freshman converse]Prove: if a prime [formula] divides every interior entry of row [formula] of P…

Prove: if a prime $p$ divides every interior entry of row $n$ of Pascal's triangle, then $n$ is a power of $p$.

<details>
<summary>Answer + Reasoning</summary>

**Method: one valuation formula, two directions.** Legendre's floors collect into the digit identity $v_p(n!) = \frac{n - s_p(n)}{p-1}$ (each multiple of $p^i$ contributes one to $\lfloor n/p^i\rfloor$; summing over $i$ unwinds the base-$p$ expansion), so 
$$ v_p\binom{n}{k} = \frac{s_p(k) + s_p(n-k) - s_p(n)}{p-1} \;\ge\; 0, $$
 with equality exactly when no carry occurs in $k + (n-k)$. *($\Leftarrow$)* If $n = p^e$ and $0 \lt k \lt n$: some digit of $k$ below position $e$ is positive, and cancelling it against $n-k$ forces a carry out of that column — so every interior entry has $v_p \ge 1$. *($\Rightarrow$)* Contrapositive: if $n = p^e q$ with $q \gt 1$ and $p \nmid q$, test $k = p^e$. Then $s_p(k) = 1$; $n - k = (q-1)p^e$ and the last digit of $q$ is at least $1$, so $s_p(q-1) = s_p(q) - 1 = s_p(n) - 1$. Total: $v_p\binom{n}{p^e} = \frac{1 + s_p(n) - 1 - s_p(n)}{p-1} = 0$ — a non-zero interior entry not divisible by $p$. Exactly the failure the hypothesis forbids.


Answer: **proved — powers of $p$ are precisely the rows whose interior is uniformly divisible by $p$**. (Check: row $9 = 3^2$ has interior gcd $3$ ✓; row $12 = 3\cdot 4$ predicts the test $k = 3$: $\binom{12}{3} = 220$, $3 \nmid 220$ ✓; row 6: $\binom62 = 15$ is odd, so $n = 6$ fails for 2 — not a prime power ✓.)

</details>

#### **P47**[Olympiad][practice][Wolstenholme check]Verify Wolstenholme's congruence [formula] for [formula] and [formula] , and s…

Verify Wolstenholme's congruence $\binom{2p}{p} \equiv 2 \pmod{p^3}$ for $p = 5$ and $p = 7$, and show it fails (as a statement about the exact exponent) for $p = 3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: compute.** $p=5$: $\binom{10}{5} = 252 = 2 + 2 \cdot 125$ ✓. $p=7$: $\binom{14}{7} = 3432 = 2 + 10\cdot 343$ ✓. $p=3$: $\binom63 = 20$, $20 - 2 = 18$: divisible by 9 but not 27 — the prime-$\ge 5$ hypothesis is exactly what makes the third power work.


Answer: **$252 \equiv 3432 \equiv 2$ mod $p^3$; $p=3$ is the boundary case**. (The failure at $p=3$ is a legitimate exam answer too: congruence statements deserve their hypotheses checked at the small end ✓.)

</details>




---
