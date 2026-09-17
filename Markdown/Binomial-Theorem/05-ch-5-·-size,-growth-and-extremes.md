# Chapter 5 — Ch 5 · Size, Growth and Extremes

*3 sections · 8 questions*

*Chapter 5 of 6*

# Size, Growth and Extremes

When you do not need the exact value — only to know which of two numbers is bigger, how large a sum must be, or which term of an expansion wins — the binomial theorem becomes an *inequality* machine. All of it runs on one fact: every term of $(1+x)^n$ with $x \ge 0$ is non-negative, so *any* handful of terms is a lower bound and a truncated sum is a proof. This chapter also settles the largest-term question, which Chapter 2 set up the ratio for.

### 5.0 What you will be able to do

- Prove Bernoulli's inequality from the truncation principle and use it to compare numbers like $1.01^{80}$ against rational targets.
- Trap the sequence $(1+1/n)^n$ between 2 and 3 using the binomial expansion — and see $e$ appear.
- Find the numerically greatest term of $(a+bx)^n$ at a given $x$ by the ratio walk.
- Compute last digits and remainders of huge powers via $(m \pm c)^n$ — the binomial kills every term carrying enough of the modulus.
- Handle conjugate surds: floors of $(1+\sqrt2)^n$ without a calculator.


### 5.1 Truncation as proof — Bernoulli and friends

> **⛁ First Principles — positivity of terms is a weapon**
>
> If $x \ge 0$, every term $\binom{n}{k}x^k \ge 0$, so for any term-set $S$: $(1+x)^n \ge \sum_{k \in S} \binom{n}{k} x^k$. Drop nothing? Equality. Keep $k \le 1$? **Bernoulli:** $(1+x)^n \ge 1 + nx$. Keep $k \le 2$? A strictly sharper $(1+x)^n \ge 1 + nx + \frac{n(n-1)}{2} x^2$. Inequality questions are decided by choosing which handful of terms is strong enough — and the truncation is *always* legitimate for $x \ge 0$, which is exactly where JEE asks.

The same principle with the alternating series $(1-1/n)^n$ or with $x$ tiny gives *upper* bounds by a second trick — compare consecutive terms: in $(1 + \frac1n)^n = \sum_k \binom{n}{k} n^{-k}$, the $k$-th summand is $\frac{1}{k!} \cdot \frac{n(n-1)\cdots(n-k+1)}{n^k} \le \frac{1}{k!}$, and $k! \ge 2^{k-1}$ for $k \ge 1$. Hence

$$ 2 \;\le\; \left(1 + \frac1n\right)^{n} \;\le\; \sum_{k=0}^{n} \frac{1}{k!} \;\le\; 1 + \sum_{k \ge 0} 2^{-k} = 3, $$

— the sequence is pinched, monotone (shown by the same term-by-term comparison for two different $n$'s), and its limit is what we call $e$. Everything in this paragraph is standard JEE Advanced fodder ("prove $(1+1/n)^n \lt 3$") and Olympiad warm-up.

> **⚠ Common Trap — Bernoulli is one-sided by design**
>
> $(1+x)^n \ge 1+nx$ also holds for $-1 \le x \lt 0$ (induction — the binomial-sum argument above does *not* cover it, since odd terms flip sign), but fails badly for $x \lt -1$ with even $n$ in the other direction. When a problem says "for all $x \gt -1$", switch to the induction proof and say so; the truncation proof is for $x \ge 0$ only.

#### Worked example — the ratio walk to the greatest term

#### **S12**[JEE Adv][solved][term ratio]Find the numerically greatest term in the expansion of [formula] at [formula] …

Find the numerically greatest term in the expansion of $(2+3x)^8$ at $x = 1$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: walk the ratio until it crosses 1.** The terms are $t_k = \binom{8}{k} 2^{8-k} 3^k$ and 
$$ \frac{t_{k+1}}{t_k} = \frac{8-k}{k+1} \cdot \frac{3}{2}. $$
 The ratio is $\ge 1$ while $3(8-k) \ge 2(k+1)$, i.e. $k \le 4.4$. So $t_0 \lt t_1 \lt \cdots \lt t_5$ (the steps $k = 0, \dots, 4$ all ascend), and from $k = 5$ on it descends — e.g. $t_6 = t_5 \cdot \frac{9}{12} \lt t_5$. The peak is $t_5$, the 6th term: $T_6 = \binom{8}{5} 2^{3} 3^{5} = 56 \cdot 8 \cdot 243$.


Answer: **Answer: $T_6 = 108864$**


**Check:** neighbours $t_4 = \binom84 2^4 3^4 = 70 \cdot 16 \cdot 81 = 90720$ and $t_6 = \binom86 2^2 3^6 = 28 \cdot 4 \cdot 729 = 81648$ — both below ✓.

</details>



### 5.2 Remainders, last digits — the binomial as a sieve

Ask for the last digit of $7^{20}$: write $7^{20} = (7^2)^{10} = 49^{10} = (50-1)^{10}$. The binomial census is instant: every term with $j \ge 1$ carries a factor $\binom{10}{j} 50^j (-1)^{10-j}$, the $j = 1$ term being $-500 \equiv 0 \pmod{100}$ and higher $j$ a fortiori. The only survivor mod 10 — even mod 100 — is $(-1)^{10} = 1$: last digit **1**.

> **💡 Key Idea — expand around the modulus, then truncate with impunity**
>
> To compute $A^n \bmod m$: write $A = m' \pm c$ with $m' \equiv 0 \pmod m$, expand $(m' \pm c)^n$, and *all but the last few terms vanish mod $m$*. Truncating a modular binomial sum is not an approximation — it is an equality in residue classes. For $6^{999} + 1 \pmod 5$: $6^{999} = (5+1)^{999} \equiv 1 \pmod 5$, so the answer is 2.

#### Conjugates: floors of surd powers without decimals

The trick every contest coach hands out: for $\alpha = 1+\sqrt2$, the sum 
$$ \alpha^n + \bar\alpha^{\,n} = (1+\sqrt2)^n + (1-\sqrt2)^n = 2 \sum_{j} \binom{n}{2j} 2^{j} \in \mathbb Z $$


— the odd $\sqrt2$ powers cancel *by the binomial theorem itself*, leaving twice an integer combination. Since $|1 - \sqrt2| \lt 1$, the second term is a small dust of sign $(-1)^n$. For odd $n$ it is negative, so $\alpha^n = (\text{integer}) + \text{tiny}$: $\lfloor (1+\sqrt2)^3 \rfloor = 14$, because $\alpha^3 + \bar\alpha^3 = 2(1 + 3\cdot 2) = 14$ exactly and $\alpha^3 = 14 - \bar\alpha^3 \gt 14$ by less than 1.

> **★ Olympiad Extension — the integer-part theorem, and why parity matters**
>
> Track the argument above for $n = 2m+1$: $\lfloor (1+\sqrt2)^{2m+1} \rfloor$ equals the integer $S_{2m+1}$, and $S_{2m+1} = 2(\text{something})$ is **even** — so "the integer part of $(1+\sqrt2)^{\text{odd}}$ is even" is a one-line consequence. For even exponents the dust adds instead, and the floor becomes $S_{2m} - 1$: **odd**. Both facts, from one conjugate pairing. (Paper Q38.)


#### Practice set — size and sieve

#### **P34**[JEE Main][practice][truncation]Prove [formula] for all [formula] , and deduce [formula] .

Prove $2^n \ge 1 + n + \binom{n}{2}$ for all $n \ge 2$, and deduce $2^{10} \ge 56$.

<details>
<summary>Answer + Reasoning</summary>

**Method: truncate $(1+1)^n$.** All terms are non-negative, so keeping $k \in \{0,1,2\}$ bounds it below. At $n=10$: $1 + 10 + 45 = 56$; truth is 1024 — bounds are cheap, keep the terms you can afford.


Answer: **proved; $56 \le 1024$** ✓ (loose but valid — exactly what a proof question wants).

</details>

#### **P35**[JEE Adv][practice][trapping e]Prove [formula] for every integer [formula] .

Prove $2 \le \left(1 + \frac1n\right)^n \lt 3$ for every integer $n \ge 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand and dominate termwise.** The $k$-th summand of $\left(1+\frac1n\right)^n$ equals $\frac{n(n-1)\cdots(n-k+1)}{k!\, n^k} \le \frac{1}{k!} \le \frac{1}{2^{k-1}}$ for $k \ge 1$. Summing: $\left(1+\frac1n\right)^n \le 1 + \sum_{k \ge 1} 2^{1-k} = 1 + 2 = 3$. For $n \ge 2$ the $k=2$ summand is $\frac{n-1}{2n} \lt \frac12$, making the total strictly less than 3; $n = 1$ reads $2 \lt 3$ by hand. Lower bound: keep $k \in \{0,1\}$: $1 + n \cdot \frac1n = 2$.


Answer: **proved: pinched in $[2, 3)$**. (Numerical feel: $n = 1000$ gives $2.7169\ldots$ ✓.)

</details>

#### **P36**[JEE Adv][practice][term ratio]Find the greatest term in the expansion of [formula] at [formula] .

Find the greatest term in the expansion of $(3+2x)^{10}$ at $x = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: ratio walk.** $\frac{t_{k+1}}{t_k} = \frac{10-k}{k+1}\cdot\frac23 \ge 1
        \iff 2(10-k) \ge 3(k+1) \iff k \le 3.4$. Terms climb until $k = 4$: greatest term is $T_5 = \binom{10}{4} 3^6 2^4 = 210 \cdot 729 \cdot 16$.


Answer: **$T_5 = 2449440$**. (Neighbour check: $t_3 = \binom{10}{3}3^7 2^3 = 120 \cdot 2187 \cdot 8 = 2099520 \lt T_5$ ✓.)

</details>

#### **P37**[JEE Main][practice][modular sieve]Find the remainder when [formula] is divided by 5.

Find the remainder when $7^{100}$ is divided by 5.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand $7^{100} = (5+2)^{100}$.** Everything with a factor of 5 dies mod 5, leaving $2^{100} = (2^4)^{25} = 16^{25} \equiv 1^{25} = 1$.


Answer: **1**. (Small check: $7^4 = 2401 \equiv 1 \pmod 5$ ✓ and $100 \mid 4 \cdot 25$.)

</details>

#### **P38**[JEE Main][practice][modular sieve]Find the last digit of [formula] .

Find the last digit of $7^{20}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: last digit $= \bmod 10$.** $7^{20} = 49^{10} = (50-1)^{10}$: every term carrying $50^j$, $j \ge 1$, is a multiple of 10 — the $j=1$ term is $\binom{10}{1} 50 (-1)^9 = -500 \equiv 0$ and higher $j$ even more so. The only survivor is $(-1)^{10} = 1$.


Answer: **1**. (Cycle check: $7, 9, 3, 1$ repeats mod 10 and $20 \equiv 0 \pmod 4$ ✓.)

</details>

#### **P39**[JEE Adv][practice][conjugates]Find [formula] without evaluating any square root.

Find $\lfloor (1+\sqrt2)^3 \rfloor$ without evaluating any square root.

<details>
<summary>Answer + Reasoning</summary>

**Method: conjugate sum.** $S = (1+\sqrt2)^3 + (1-\sqrt2)^3 = 2(1 + 3\cdot 2) = 14$ (odd surd terms cancel by the binomial theorem). Since $-1 \lt 1-\sqrt2 \lt 0$, its cube is in $(-1, 0)$, so $(1+\sqrt2)^3 = 14 - (1-\sqrt2)^3 \in (14, 15)$.


Answer: **$\lfloor \cdot \rfloor = 14$**. (Expanding directly: $7 + 5\sqrt2 \approx 14.071$ ✓.)

</details>

#### **P40**[Olympiad][practice][truncation + growth]Prove [formula] for all integers [formula] .

Prove $2^n \gt n^2$ for all integers $n \ge 5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: keep four fat terms of $(1+1)^n$.** For $n \ge 7$ the indices $2, 3, n-2, n-3$ are four distinct slots, so 
$$ 2^n = \sum_k \binom nk \;\ge\; \binom n2 + \binom n3 + \binom{n}{n-2} + \binom{n}{n-3} \;=\; 2\left[\binom n2 + \binom n3\right] = \frac{n(n-1)(n+1)}{3}, $$
 and $\frac{n(n^2-1)}{3} \gt n^2 \iff n^2 - 1 \gt 3n$, true for $n \ge 4$. The small cases $n = 5, 6$ are direct: $32 \gt 25$, $64 \gt 36$. QED. *(Induction is the one-line alternative: $2^{n+1} = 2\cdot 2^n \gt 2n^2 \ge (n+1)^2$ once $n \ge 3$.)*


Answer: **proved**. (The truncation proof is the one the examiner wants — the ratio $(n{+}1)^2/n^2 = (1 + 1/n)^2 \le 1.44 \lt 2$ is why the LHS wins in the long run ✓.)

</details>




---

