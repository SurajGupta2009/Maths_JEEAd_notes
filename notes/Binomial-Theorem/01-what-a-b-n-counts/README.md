# Chapter 1 — What (a+b)^n Counts

*5 sections · 10 questions*

*Chapter 1 of 6*

# What (a+b)^n Counts

Before any formula, one picture: expanding $(a+b)^n$ means choosing from $n$ separate brackets, and every product that survives is a record of those choices. Once you see $\binom{n}{k}$ as "*the number of ways to pick which $k$ brackets contributed $b$*" — not as a symbol to memorise — symmetry, Pascal's triangle and the identity $\sum_k \binom{n}{k} = 2^n$ all appear for free. This chapter builds that counting foundation; every later chapter (coefficients, identities, series, divisibility) is the same idea wearing a different hat.

### 1.0 What you will be able to do

This chapter is the load-bearing wall of the whole module. By the end you will never "expand a binomial" mechanically again.

- Expand $(a+b)^n$ by the bracket-choice argument and say *why* the coefficient of $a^{\,n-k}b^k$ is $\binom{n}{k}$.
- Read Pascal's triangle as a counting table (small cases of the theorem), and prove every pattern in it by conditioning on one element.
- Prove $\sum_k \binom{n}{k} = 2^n$ by a bijection, and derive the even/odd split of a row without any new work.
- Use substitution ($x = 1, -1, \tfrac12$) to extract coefficient sums from $(px+q)^n$ — the JEE's favourite three-second question.


### 1.1 The expansion as a decision tree

Take $n = 3$. Expanding $(a+b)^3 = (a+b)(a+b)(a+b)$ by the distributive law means picking *one letter from each bracket* and multiplying your three picks. There are $2 \times 2 \times 2 = 8$ pick-lists, and each produces a string like $aab$. Collecting like strings is just sorting these lists by how many $b$'s they contain:


$$ (a+b)^3 = \underbrace{aaa}_{\text{0 picks of }b} + \underbrace{(aab + aba + baa)}_{1\text{ pick}} + \underbrace{(abb + bab + bba)}_{2\text{ picks}} + \underbrace{bbb}_{3\text{ picks}}. $$


> **⛁ First Principles — why the number $3$ is really $\binom{3}{2}$**
>
> There are $\binom{n}{k}$ pick-lists with exactly $k$ copies of $b$: a list is fully described by saying *which $k$ of the $n$ brackets* contributed their $b$, and any such set of positions gives a valid, distinct list. So the coefficient of $a^{\,n-k}b^k$ — the number of strings $a^{\,n-k}b^k$ produced — is exactly $\binom{n}{k}$. Nothing was proved by induction and nothing needs memorising: the binomial theorem is a census of pick-lists.

$$ (a+b)^n \;=\; \sum_{k=0}^{n} \binom{n}{k} a^{\,n-k} b^{k},
      \qquad \binom{n}{k} = \frac{n!}{k!\,(n-k)!} $$

The number $\binom{n}{k}$ is called a **binomial coefficient**; the rows of these numbers are Pascal's triangle. Row $n$ of Pascal's triangle *is* the census for $(a+b)^n$.

#### Two consequences you may never re-prove but must be able to prove on demand

**Symmetry.** Choosing which $k$ brackets give $b$ is the same decision as choosing which $n-k$ brackets give $a$: $\binom{n}{k} = \binom{n}{n-k}$. Row $n$ reads the same forwards and backwards.

**Pascal's rule.** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$. Condition on the *first* bracket: if bracket 1 contributed $b$, the remaining $k-1$ $b$'s are chosen from the last $n-1$ brackets; if it contributed $a$, you still need all $k$ from those. Two disjoint cases, one row of the triangle built from the row above.

> **⚠ Common Trap — "expanding" as multiplying out blindly**
>
> Students who expand $(2x-5)^7$ term-by-term from the distributive law run out of time and make sign errors. The census view gives every term directly: the $k$-th term is $\binom{7}{k}(2x)^{7-k}(-5)^k$, one line each. *Always* write the general term; never brute-force.



### 1.2 Worked examples — the census at work

#### **S1**[JEE Main][solved][general term]Find the coefficient of [formula] in [formula] , and say which row of Pascal's…

Find the coefficient of $x^4$ in $(2+x)^5$, and say which row of Pascal's triangle is hiding in it.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** census of pick-lists. A term choosing $k$ copies of $x$ (and $5-k$ copies of $2$) looks like $\binom{5}{k} 2^{\,5-k} x^{k}$. For $x^4$: $k=4$, giving $\binom{5}{4} 2^{1} = 5 \cdot 2 = 10$.


Expanding the whole row as a sanity check: $(2+x)^5 = 32 + 80x + 80x^2 + 40x^3 + 10x^4 + x^5$. The coefficient of $x^4$ is **Answer: $10$**, and the raw binomial coefficients $1,5,10,10,5,1$ are row 5 of Pascal's triangle.


**Small-case check:** the powers of 2 explain the inflation: $1\cdot 2^1 = 2 \ne 10$ is the coefficient *of $x^4$ in $(1+x)^5$* being 5, times $2^{5-4} = 2$ from the four untouched brackets — consistent. ✓

</details>

#### **S2**[JEE Adv][solved][substitution]Split row 8 of Pascal's triangle into even-position and odd-position entries. …

Split row 8 of Pascal's triangle into even-position and odd-position entries. Prove they are equal, for every row $n \ge 1$, not just row 8.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: evaluate the polynomial at two points.** Let $f(x) = (1+x)^8 = \sum_k \binom{8}{k} x^k$. At $x = 1$: total $= 2^8 = 256$. At $x = -1$: $\sum_k \binom{8}{k}(-1)^k = 0$, i.e. the even-position sum equals the odd-position sum. Adding the two equations, each part is $2^8/2 = 2^7 = 128$.


The argument used nothing special about $8$: for any $n \ge 1$, 
$$ \sum_{k \text{ even}} \binom{n}{k} \;=\; \sum_{k \text{ odd}} \binom{n}{k} \;=\; 2^{\,n-1}. $$



Both halves $=$ **Answer: $2^{7} = 128$**.


**Check row 8 by hand:** $1,8,28,56,70,56,28,8,1$; evens $1+28+70+28+1 = 128$, odds $8+56+56+8 = 128$. ✓

</details>


### 1.3 The $2^n$ identity, proved twice

Set $a = b = 1$ in the theorem: $\sum_{k=0}^n \binom{n}{k} = 2^n$. That one line is a whole subject — a sum of counts equaling a total count — and the JEE keeps testing whether you know *why*.

> **💡 Key Idea — a sum of binomial coefficients is always a counting story**
>
> $\sum_k \binom{n}{k}$ counts subsets of an $n$-set two ways: grouped by size (left side) and element-by-element, "in or out" (right side $= 2^n$). Any identity of binomial coefficients is *the same set counted twice*. Keep this in your pocket for Chapters 3 and 6.

#### Engine 1 — substitution. Coefficient sums without expanding

If $(px+q)^n = c_0 + c_1 x + \dots + c_n x^n$, then:

- putting $x = 1$: $\;c_0 + c_1 + \cdots + c_n = (p+q)^n$ — the **sum of all coefficients**;
- putting $x = 0$: $\;c_0 = q^n$ — the **constant term**;
- putting $x = -1$: the alternating sum, which splits even/odd positions.

No expansion ever. This is why "sum of coefficients of $(2x-1)^7$" is a 10-second question for a prepared student and a 5-minute one for everyone else.


#### Engine 2 — the bijection (and why it beats algebra)

Map each subset $S \subseteq \{1,\dots,n\}$ to the pair $(|S|, S)$: grouping all $2^n$ subsets by size gives exactly the row sum $\sum_k \binom{n}{k}$. The same idea, with "size" replaced by "size mod 2", gives the even/odd split of S2 — a proof by *involution*: toggling element 1 pairs up all subsets into in/out pairs, so half have even size.

> **★ Olympiad Extension — counting twice is a proof technique, not a trick**
>
> Almost every olympiad combinatorics identity $\sum_k (\text{something})\binom{n}{k} = (\text{something else})$ is resolved by naming the set on both sides: LHS counts it with a statistic recorded, RHS counts it directly. E.g. $\sum_k k\binom{n}{k} = n2^{n-1}$ counts "a committee from $n$ people with a chosen chair": choose chair first ($n$), decide each other member ($2^{n-1}$). Chapter 3 makes this a full machinery.



### 1.4 Practice set — counting roots

#### **P1**[JEE Main][practice][decision tree]How many separate products appear when [formula] is expanded by the distributi…

How many separate products appear when $(a+b+c)^6$ is expanded by the distributive law *before* collecting like terms? How many distinct terms survive after collecting?

<details>
<summary>Answer + Reasoning</summary>

**Method: the pick-list census, three-way.** Each of the 6 brackets offers 3 choices, so there are $3^6 = 729$ raw products. After collecting, a term is determined by $(i,j,k)$, the number of brackets contributing $a,b,c$, with $i+j+k = 6$: by stars-and-bars there are $\binom{6+2}{2} = 28$.


Answer: **$3^6 = 729$ products, $28$ collected terms**. (Check: for two variables the same logic gives $2^n$ products and $n+1$ terms — matches the binomial case ✓.)

</details>

#### **P2**[JEE Main][practice][substitution]Find the sum of the coefficients of [formula] without expanding.

Find the sum of the coefficients of $(2x-1)^7$ without expanding.

<details>
<summary>Answer + Reasoning</summary>

**Method: evaluate at $x=1$.** The sum of coefficients of any polynomial $f$ is $f(1)$ — here $f(1) = (2-1)^7 = 1$.


Answer: **$1$**. (Check: the constant term is $f(0) = (-1)^7 = -1$; the remaining coefficients sum to $2$, consistent with the alternating binomial balance ✓.)

</details>

#### **P3**[JEE Main][practice][substitution]Find the sum of the coefficients of [formula] .

Find the sum of the coefficients of $(x-2y)^9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: two variables — evaluate at $x=y=1$.** Sum of all coefficients of a polynomial in $x,y$ is its value at $(1,1)$: $(1-2)^9 = (-1)^9 = -1$.


Answer: **$-1$**. (A negative answer is legal and a good sign you did not silently take absolute values: odd power of a negative flips the sign ✓.)

</details>

#### **P4**[JEE Adv][practice][even/odd split]Find the sum of the coefficients of the odd powers of [formula] in [formula] .

Find the sum of the coefficients of the odd powers of $x$ in $(1+x)^{12}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: half-sum.** $S_{\text{odd}} = \tfrac{f(1) - f(-1)}{2} =
        \tfrac{2^{12} - 0}{2} = 2^{11}$.


Answer: **$2048$**. (Check: even powers also sum to 2048 and $2048+2048 = 2^{12}$ = total ✓.)

</details>

#### **P5**[JEE Adv][practice][symmetry]In the expansion of [formula] , the coefficients of [formula] and [formula] ar…

In the expansion of $(1+x)^{18}$, the coefficients of $x^{2r}$ and $x^{r+6}$ are equal. Find all valid $r$.

<details>
<summary>Answer + Reasoning</summary>

**Method: solve the symmetry equation.** $\binom{18}{2r} = \binom{18}{r+6}$ holds iff $2r = r+6$ (same slot) or $2r + (r+6) = 18$ (mirror slots). So $r = 6$ or $3r = 12 \Rightarrow r = 4$. Both give admissible indices $0 \le k \le 18$.


Answer: **$r \in \{4, 6\}$** — and notice $r=6$ is the trivial solution (the two terms are literally the same coefficient), which exam keys love to hide. (Check $r=4$: $\binom{18}{8} = \binom{18}{10}$ ✓ by symmetry.)

</details>

#### **P6**[JEE Adv][practice][conditioning]Prove Pascal's rule [formula] by conditioning on membership of one fixed eleme…

Prove Pascal's rule $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ by conditioning on membership of one fixed element, and verify it numerically at $(n,k) = (8,3)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: split the census.** Count $k$-subsets of $\{1,\dots,n\}$ by whether they contain the element $n$. Without $n$: all $k$ from the first $n-1$: $\binom{n-1}{k}$. With $n$: remaining $k-1$ from $n-1$: $\binom{n-1}{k-1}$. Disjoint, exhaustive — proved.


Answer: **$\binom{8}{3} = 56 = 21 + 35 = \binom{7}{2} + \binom{7}{3}$**. (The numerical split 21 + 35 is visible in the triangle itself ✓.)

</details>

#### **P7**[Olympiad][practice][bijection]Prove [formula] by exhibiting an explicit bijection between the set it counts …

Prove $\sum_{k=0}^n \binom{n}{k} = 2^n$ by exhibiting an explicit bijection between the set it counts on each side. (No algebraic manipulation allowed.)

<details>
<summary>Answer + Reasoning</summary>

**Method: the subset bijection.** RHS: all subsets of $[n]$, each of the $n$ elements independently in/out — $2^n$ lists. LHS: the same subsets, grouped by size; there are $\binom{n}{k}$ of size $k$. The identity-map "a subset is a subset" is the bijection; the two counts agree.


Answer: **proved — one set, two censuses**. (Sanity at $n=3$: $1+3+3+1 = 8$ ✓.)

</details>

#### **P8**[JEE Main][practice][general term]Find the 5th term in the expansion of [formula] , and state the largest binomi…

Find the 5th term in the expansion of $(1+x)^8$, and state the largest binomial coefficient of that row.

<details>
<summary>Answer + Reasoning</summary>

**Method: index carefully.** The 5th term is $k=4$ (terms start at $k=0$): $T_5 = \binom{8}{4} = 70$, i.e. $70x^4$. For $n$ even the middle $k = n/2$ is the unique peak, so 70 is also the largest coefficient of row 8.


Answer: **$T_5 = 70x^4$; largest coefficient $70$**. (Row 8: $1,8,28,56,70,56,\dots$ — the bump is exactly at position 4 ✓.)

</details>



---

