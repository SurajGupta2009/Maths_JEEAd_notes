# Chapter 4 — Binomial Coefficients & Identities

*6 sections · 13 questions*

*Chapter 4 · Coefficients Count*

# Binomial Theorem & Double Counting

The binomial theorem is a counting statement wearing algebra's clothes. This chapter proves it by counting, turns double counting into a proof machine, builds the complete identity toolkit, and ends with coefficient extraction — the bridge to generating functions.

`theorem by counting` `double counting` `identity toolkit` `negative binomial` `coefficient extraction`

### 4.1 The binomial theorem, proved by counting

**Theorem.** For a non-negative integer $n$,

$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$$

> **⛁ First Principles — the proof is one sentence**
>
> $(x+y)^n$ is a product of $n$ identical factors. To produce the term $x^{n-k}y^k$ in the expansion, exactly $k$ of the $n$ factors must contribute their $y$, and the other $n-k$ their $x$. The choice of *which $k$ factors* is the whole data: $\binom{n}{k}$ choices, each contributing the same monomial $x^{n-k}y^k$. Coefficients add. That's the proof — no induction needed (induction is just a different bookkeeping of the same split).
>
>
> Notice the deeper statement this proof actually makes: **a binomial coefficient is the number of ways to take a specific term from a specific product.** From now on, "coefficient of $x^m$ in $F(x)$" and "number of objects of size $m$" are interchangeable languages. That is the entire philosophy of generating functions (Chapter 6).

| Substitution | Identity | Counting meaning |
| --- | --- | --- |
| $x = y = 1$ | $\sum_k \binom{n}{k} = 2^n$ | all subsets of $[n]$, by size |
| $x = 1, y = -1$ | $\sum_k (-1)^k \binom{n}{k} = 0$ | even-sized vs odd-sized subsets equal (involution, Ch. 1) |
| $x = y = 1$, differentiate in $x$ | $\sum k\binom{n}{k} = n2^{n-1}$ | (element, subset) pairs |
| $x = 1, y = t$ | $(1+t)^n = \sum \binom{n}{k}t^k$ | the counting engine itself |


### 4.2 Double counting — the method, systematized

From Chapter 1: count a pair-set $\Omega$ two ways. The complete recipe:

- **Invent $\Omega$:** a set of pairs (or triples, or "flags on a figure") whose definition contains the objects of both sides of the target identity.
- **Count by coordinate 1** → one side.
- **Count by coordinate 2** → the other side.
- **Set equal.** No algebra was "used" — the identity is a tautology about one set.

#### Worked — Vandermonde's identity (the flagship)

**Theorem (Vandermonde).** $\displaystyle\sum_{k} \binom{r}{k}\binom{s}{m-k} = \binom{r+s}{m}$, where the sum runs over all $k$ for which the binomials are defined.

> **⛁ First Principles — the committee story**
>
> Let $A, B$ be disjoint sets, $|A| = r$, $|B| = s$. Count the $m$-subsets of $A \cup B$. **Directly:** $\binom{r+s}{m}$. **By the part from $A$:** an $m$-subset contains exactly $k$ elements of $A$ for some $k$: choose those ($\binom{r}{k}$) and the remaining $m-k$ from $B$ ($\binom{s}{m-k}$). The cases are disjoint and exhaustive, so sum over $k$. Identity proved. $\square$
>
>
> Everything downstream is a parameter choice: $r = s = n, m = n$ gives $\sum \binom{n}{k}^2 = \binom{2n}{n}$; $s = 1$ gives Pascal; $r = n, s = n, m = n+1$ gives $\sum \binom{n}{k}\binom{n}{k-1} = \binom{2n}{n+1}$. One proof, a family of identities.


#### Worked — a genuinely new shape: $\sum_k \binom{k}{m}\binom{n-k}{r-m} = \binom{n+1}{r+1}$

**Proof.** Let $U = \{0, 1, \dots, n\}$ (size $n+1$). Count the $(r+1)$-subsets of $U$, and inside each subset look at its $(m+1)$-**smallest** element, call it $k$. Then: $m$ elements are chosen from $\{0, \dots, k-1\}$: $\binom{k}{m}$ ways; $r-m$ elements from $\{k+1, \dots, n\}$: $\binom{n-k}{r-m}$ ways. Sum over possible $k$: $\sum_k \binom{k}{m}\binom{n-k}{r-m}$. But the total is $\binom{n+1}{r+1}$. $\square$

The pattern to steal: **"split by a distinguished element's *position*"** (here: the $(m+1)$-smallest member). It is the same engine as the hockey-stick identity (split by the maximum element) — one idea, two costumes.


#### Worked — $\sum k^2 \binom{n}{k} = n(n+1)2^{n-2}$

**Proof (by pairs of marked elements).** Let $\Omega = \{(i, j, S) : i, j \in S
    \subseteq [n]\}$ — a subset with *two distinguished (ordered) elements*. **By $S$:** a $k$-subset contributes $k^2$ ordered pairs → $\sum k^2\binom{n}{k}$. **By $(i,j)$:** $i = j$: $n$ choices, then $S$ any of the $2^{n-1}$ subsets containing $i$ → $n\cdot 2^{n-1}$; $i \ne j$: $n(n-1)$ ordered pairs, then $S$ any of the $2^{n-2}$ subsets containing both → $n(n-1)2^{n-2}$. Total $n\cdot 2^{n-1} + n(n-1)2^{n-2} = n(n+1)2^{n-2}$. $\square$

Same as differentiating twice (the $k(k-1)$ term plus the $k$ term) — but the counting proof shows *what is being counted*, and that knowledge is what lets you invent the next identity.



### 4.3 The identity toolkit

All proven by the methods above (committees, marking, involution). Memorize the *proof pattern*, not the list.

| Identity | Pattern |
| --- | --- |
| $\displaystyle\sum_k \binom{n}{k} = 2^n$ | subsets by size |
| $\displaystyle\sum_k (-1)^k \binom{n}{k} = 0$ | toggle involution / $x=1, y=-1$ |
| $\displaystyle\sum_{k\ \mathrm{even}} \binom{n}{k} = 2^{n-1}\ (n\ge 1)$ | even/odd sizes equal |
| $\displaystyle\sum k\binom{n}{k} = n2^{n-1}$ | mark one element |
| $\displaystyle\sum k(k-1)\binom{n}{k} = n(n-1)2^{n-2}$ | mark two (ordered) |
| $\displaystyle\sum \binom{n}{k}^2 = \binom{2n}{n}$ | Vandermonde $r=s=n$ |
| $\displaystyle\sum_k \binom{n}{k}\binom{n}{k+1} = \binom{2n}{n+1}$ | Vandermonde $m = n+1$ |
| $\displaystyle\sum_{i=r}^{n}\binom{i}{r} = \binom{n+1}{r+1}$ | split by maximum (hockey stick, Ch. 3) |
| $\displaystyle\sum_k \binom{n}{k}\binom{n+1}{k+1} = \binom{2n+1}{n}$ | Vandermonde $r = n, s = n+1, m = n$ |
| $\displaystyle\sum_k \binom{n}{k}\frac{1}{k+1} = \frac{2^{n+1}-1}{n+1}$ | integration (below) |
| $\displaystyle\binom{n}{r} = \frac{n}{r}\binom{n-1}{r-1}$ | committee + chair: $\binom{n}{r}r = n\binom{n-1}{r-1}$ |

#### The integration trick (for "1/(k+1)" identities)

Since $\int_0^1 (1+x)^n dx = \frac{2^{n+1}-1}{n+1}$ and $\int_0^1 x^k dx = \frac{1}{k+1}$, integrating $\sum \binom{n}{k}x^k = (1+x)^n$ from 0 to 1 gives $\sum_k \binom{n}{k}\dfrac{1}{k+1} = \dfrac{2^{n+1}-1}{n+1}$. Counting meaning: $\binom{n}{k}\frac{1}{k+1} = \frac{1}{k+1}\binom{n+1}{k+1}\cdot\frac{k+1}{n+1}$… the cleanest form: $\dfrac{1}{k+1}\binom{n}{k} = \dfrac{1}{n+1}\binom{n+1}{k+1}$ (catalan-shaped!). So the identity is a scaled even-split of $\sum\binom{n+1}{k+1} = 2^{n+1}-1$.

#### **S1**[JEE Adv][solved][three proofs of one identity]Prove [formula] in three different ways.

Prove $\displaystyle\sum_{k=0}^{n} k\binom{n}{k} = n\,2^{n-1}$ in three different ways.

<details>
<summary>Answer + Reasoning</summary>

Solution


**(i) Double counting.** $\Omega = \{(i,S): i \in S \subseteq [n]\}$: by $i$: $n\cdot 2^{n-1}$; by $S$: $\sum k\binom{n}{k}$. ✓ (Ch. 1/4.2.)


**(ii) Calculus.** $(1+x)^n = \sum \binom{n}{k}x^k$; differentiate: $n(1+x)^{n-1} = \sum k\binom{n}{k}x^{k-1}$; set $x = 1$. ✓


**(iii) Term manipulation.** $k\binom{n}{k} = n\binom{n-1}{k-1}$ (mark the chosen element, then it's "chosen element + subset of the rest" — choose the element first). Sum: $n\sum_{k\ge 1}\binom{n-1}{k-1} = n\sum_{j\ge 0}\binom{n-1}{j} = n2^{n-1}$. ✓


**Why three proofs?** Each proof suggests different generalizations: (i) → pairs of marks; (ii) → higher moments; (iii) → shifting identities. The Olympiad habit is: *never stop at one proof when the problem invites more.*

</details>

#### **S2**[JEE Adv][solved][coefficient extraction]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^8$ in $(1+x)^{10}\left(1+\dfrac{1}{x}\right)^{12}$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


Rewrite: $\left(1+\frac{1}{x}\right)^{12} = x^{-12}(1+x)^{12}$, so the product is $x^{-12}(1+x)^{22}$. Coefficient of $x^8$ = coefficient of $x^{20}$ in $(1+x)^{22}$ $= \binom{22}{20} =$ **Answer: 231**


The move "pull out $x^{-12}$ and reindex" is used constantly in coefficient problems — always write negative powers as $x^{-m}$ times a polynomial first.

</details>

#### **S3**[Olympiad][solved][onto functions (IE preview)]How many onto functions [formula] are there?

How many **onto** functions $f: \{1,2,3,4,5\} \to \{1,2,3\}$ are there?

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


Total functions: $3^5 = 243$. Subtract those missing at least one value, by IE on the three "value $i$ is missing" events: $3^5 - \binom31 2^5 + \binom32 1^5 - \binom33 0^5 = 243 - 96 + 3 =$ **Answer: 150**


In general, onto $[n]\to[k]$ counts are $k!\,S(n,k)$ where $S(n,k)$ (Stirling numbers of the second kind, Chapter 6) partition $[n]$ into $k$ nonempty unlabeled blocks. The IE formula $\sum_{j=0}^k (-1)^j\binom{k}{j}(k-j)^n$ *is* the definition of $k!S(n,k)$ — the two notations are the same number seen from probability vs combinatorics.

</details>

#### **S4**[JEE Adv][solved][numeric application]Compute [formula] .

Compute $\displaystyle\sum_{k=0}^{10} \binom{10}{k}^2$.

<details>
<summary>Answer + Reasoning</summary>

Solution


Vandermonde with $r = s = n = 10, m = 10$: $\binom{20}{10} =$ **Answer: 184,756**. (JEE pattern: sums of $\binom{n}{k}^2$, $\binom{n}{k}\binom{n}{n-k}$, $\binom{2n}{2k}$ all resolve to a single central binomial coefficient.)

</details>



### 4.4 Beyond positive exponents — the negative binomial

The counting story works for *any* integer (even negative) exponent, if we allow infinite series. For $|x| &lt; 1$:

$$(1 - x)^{-(r+1)} = \sum_{n=0}^{\infty} \binom{n+r}{r} x^n$$

> **⛁ First Principles — why stars and bars produces this series**
>
> Recall (Ch. 3): the number of non-negative solutions of $y_1 + \cdots + y_{r+1} = n$ is $\binom{n+r}{r}$. Now look at the product $(1 + x + x^2 + \cdots)^{r+1}$: the coefficient of $x^n$ counts exactly the ways to choose exponents $e_1, \dots, e_{r+1} \ge 0$ with $e_1 + \cdots + e_{r+1} = n$ — the same solutions! But each factor is $\frac{1}{1-x}$, so 
> $$ \frac{1}{(1-x)^{r+1}} = \sum_{n\ge 0} \binom{n+r}{r} x^n. $$
>  The formal algebra (generalized binomial theorem) and the counting agree — they *must*, because both sides are the same stars-and-bars count. This is the first time a **generating function** has done real counting work; Chapter 6 makes it systematic.

> **🏛 Olympiad Extension — the "any number of parts" corollaries**
>
> $(1-x)^{-2} = \sum (n+1)x^n$: the coefficient $n+1$ is the number of 2-part compositions of $n$ — check: $\binom{n+1}{1}$ ✓. $(1-x)^{-3} = \sum \binom{n+2}{2}x^n$: 3-part compositions. The pattern: **compositions with parts from a set $S$ have GF $\frac{1}{1 - (x^{s_1} + x^{s_2} + \cdots)}$**. Example: parts from $\{1,2\}$: $\frac{1}{1 - x - x^2} = \sum F_{n+1}x^n$ — *Fibonacci as a counting sequence*, which Chapter 5 proves combinatorially too.


### 4.5 Coefficients under bounds — the dice engine

The most frequent JEE Advanced shape: "how many ways can $k$ dice sum to $n$?", or equivalently "non-negative solutions of $x_1 + \cdots + x_k = m$ with $x_i \le b$". The universal method:

$$[x^m]\,(1 + x + \cdots + x^b)^k
      \;=\; \sum_{j \ge 0} (-1)^j \binom{k}{j}\binom{m - j(b+1) + k - 1}{k - 1}$$

> **⛁ First Principles — inclusion–exclusion inside a coefficient**
>
> $(1 + \cdots + x^b)^k = \left(\frac{1-x^{b+1}}{1-x}\right)^k = (1-x^{b+1})^k (1-x)^{-k}$. Expand $(1-x^{b+1})^k = \sum_j (-1)^j \binom{k}{j} x^{j(b+1)}$. The term with a given $j$ contributes $\binom{k}{j}(-1)^j$ times the coefficient of $x^{m - j(b+1)}$ in $(1-x)^{-k}$, which is $\binom{m - j(b+1) + k - 1}{k-1}$ (negative binomial, §4.4 — or: non-negative solutions of a $(k)$-variable equation). Sum over $j$. The formula is just IE on the events "$x_i \ge b+1$", packaged as a coefficient. **Every bounded-composition problem in JEE Advanced is this one formula with $b$ specialized** (dice: $b = 5$ after shifting, bounded stars-and-bars: arbitrary $b$).

#### **S5**[JEE Adv][solved][dice / bounded]In how many outcomes do 3 dice sum to 10 ?

In how many outcomes do **3 dice** sum to **10**?

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


Each die: $1$ to $6$ → shift: $x_i \in \{0,\dots,5\}$, $\sum x_i = 7$. By the engine: $[x^7](1+x+\cdots+x^5)^3 = \binom{9}{2} - 3\binom{3}{2} = 27$; compute term by term: $j = 0$: $\binom{7+3-1}{2} = \binom92 = 36$; $j = 1$: $-3\binom{7-6+2}{2} = -3\binom32 = -9$; $j \ge 2$: $7 - 12 &lt; 0$, no terms. Answer $36 - 9 =$ **Answer: 27**


Sanity check: 3 dice, 216 outcomes, sum 10 has 27 — matches the known dice-distribution table (11: 25, 10: 27, 9: 25). The "small case by table" habit again.

</details>

> **⚠ Common Trap — when the binomial is "negative"**
>
> In the engine, a term $\binom{m - j(b+1) + k - 1}{k-1}$ with $m - j(b+1) &lt; 0$ is **zero** (no solutions to a negative-sum equation) — the sum terminates on its own. Never evaluate $\binom{-3}{2}$ algebraically; set the term to 0. This is the #1 arithmetic disaster in bounded-coefficient problems.


### 4.6 Practice set

#### **P1**[JEE Adv][practice][coefficient enumeration]Coefficient of [formula] in [formula] .

Coefficient of $x^5$ in $(1+x)^3 (1+x^2)^4 (1+x^3)^2$.

<details>
<summary>Answer + Reasoning</summary>

Write $x^{a + 2b + 3c}$, $0\le a\le 3, 0\le b\le 4, 0\le c\le 2$, $a+2b+3c = 5$, weight $\binom3a\binom4b\binom2c$. $c=0$: $a+2b = 5$: $(a,b) = (1,2), (3,1)$: $3\cdot 6 + 1\cdot 4 = 22$. $c=1$: $a+2b = 2$: $(0,1), (2,0)$: $2\cdot(4 + 3) = 14$. $c=2$: $a+2b = -1$: none. Total **36**.

</details>

#### **P2**[JEE Adv][practice][proof]Prove [formula] .

Prove $\displaystyle\sum k(k-1)\binom{n}{k} = n(n-1)2^{n-2}$.

<details>
<summary>Answer + Reasoning</summary>

$k(k-1)\binom{n}{k} = n(n-1)\binom{n-2}{k-2}$ (mark two elements, ordered: choose them first). Sum over $k\ge 2$: $n(n-1)\sum_{j\ge 0}\binom{n-2}{j} = n(n-1)2^{n-2}$. ✓ (Or: differentiate twice and set $x = 1$.)

</details>

#### **P3**[Olympiad][practice][bounded engine]Coefficient of [formula] in [formula] .

Coefficient of $x^{15}$ in $(1 + x + x^2)^{10}$.

<details>
<summary>Answer + Reasoning</summary>

$(1+x+x^2)^{10} = (1-x^3)^{10}(1-x)^{-10}$. Terms $j = 0..4$ (for $j \ge 5$, $15 - 3j &lt; 0$): $j=0: \binom{24}{9} = 1{,}307{,}504$; $j=1: -10\binom{21}{9} = -10\cdot 293{,}930 = -2{,}939{,}300$; $j=2: +45\binom{18}{9} = 45\cdot 48{,}620 = 2{,}187{,}900$; $j=3: -120\binom{15}{9} = -120\cdot 5{,}005 = -600{,}600$; $j=4: +210\binom{12}{9} = 210\cdot 220 = 46{,}200$; $j=5: -252\binom{9}{9} = -252$. Sum: $1{,}307{,}504 - 2{,}939{,}300 + 2{,}187{,}900 - 600{,}600 + 46{,}200 - 252 =$ **1,452**.

</details>

#### **P4**[JEE Main][practice][parity split]Sum of the coefficients of the odd powers of [formula] in [formula] .

Sum of the coefficients of the **odd powers** of $x$ in $(1+x)^{100}$.

<details>
<summary>Answer + Reasoning</summary>

$\frac{(1+1)^{100} - (1-1)^{100}}{2} =$ **$2^{99}$**. (General trick: even/odd splits use $F(1)$ and $F(-1)$.)

</details>

#### **P5**[JEE Adv][practice][coefficient]Coefficient of [formula] in [formula] .

Coefficient of $x^9$ in $(1+x)^4(1+x^2)^4(1+x^3)^4$.

<details>
<summary>Answer + Reasoning</summary>

Need $[x^9]$ of $\left(\sum_a \binom4a x^a\right)\left(\sum_b \binom4b x^{2b}\right)
        \left(\sum_c \binom4c x^{3c}\right)$: solutions of $a+2b+3c = 9$ with $0\le a,b,c\le 4$, weight $\binom4a\binom4b\binom4c$:


| $c$ | $(a,b)$ valid | contribution |
| --- | --- | --- |
| 0 | $(1,4), (3,3)$ | $4 + 16 = 20$ |
| 1 | $(4,1), (2,2), (0,3)$ | $16 + 144 + 16 = 176$ |
| 2 | $(3,0), (1,1)$ | $24 + 96 = 120$ |
| 3 | $(0,0)$ | $4$ |


Total: $20 + 176 + 120 + 4 =$ **320**.

</details>

#### **P6**[JEE Adv][practice][parity proof]Prove that for [formula] , [formula] .

Prove that for $n \ge 1$, $\displaystyle\sum_{k\ \mathrm{even}} \binom{n}{k} = 2^{n-1}$.

<details>
<summary>Answer + Reasoning</summary>

$(1+1)^n = 2^n$ (all subsets) and $(1-1)^n = 0$ (even minus odd). Subtract: twice the even sum $= 2^n$ → even sum $= 2^{n-1}$. ✓ (Counting version: the toggle involution of Ch. 1 matches even/odd subsets.)

</details>

#### **P7**[JEE Adv][practice][coefficient]Coefficient of [formula] in [formula] .

Coefficient of $x^8$ in $(1+x)^6(1+x^2)^6$.

<details>
<summary>Answer + Reasoning</summary>

$\sum_{j} \binom6j\binom6{8-2j}$ over $8 - 2j \in [0,6]$: $j = 1: 6\cdot 1 = 6$; $j = 2: 15\cdot 15 = 225$; $j = 3: 20\cdot 15 = 300$; $j = 4: 15\cdot 1 = 15$. Total $6 + 225 + 300 + 15 =$ **546**.

</details>

#### **P8**[Olympiad][practice][roots-of-unity filter]If [formula] , find [formula] (sum over [formula] ).

If $(1+x)^{20} = \sum_{r=0}^{20} \binom{20}{r} x^r$, find $\displaystyle\sum_{4\mid r} \binom{20}{r}$ (sum over $r \equiv 0 \pmod 4$).

<details>
<summary>Answer + Reasoning</summary>

Roots-of-unity filter: $\sum_{4\mid r} \binom{20}{r}
        = \frac14\sum_{j=0}^{3} (1 + i^j)^{20}$, where $i^2 = -1$: $(1+1)^{20} = 2^{20}$; $(1+i^2)^{20} = 0^{20} = 0$; $(1+i)^{20} = (2i)^{10} = 2^{10}i^{10} = -1024$; $(1-i)^{20} = -1024$. Sum: $\frac{1}{4}(1{,}048{,}576 - 2048) =$ **261,632**. (The filter $\frac{1}{m}\sum_{j=0}^{m-1} \zeta^{-rj}$ extracts the $r \equiv 0 \pmod m$ terms — a standard Olympiad tool; here $\zeta = i$.)

</details>



---

