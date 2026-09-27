---
title: "Chapter 5 — Advanced Methods"
aliases:
  - Advanced Methods
  - Ch 5 — Advanced Methods
module: "PnC"
module_title: "PnC"
chapter: 5
level: frontier
tags:
  - pnc
  - chapter
  - frontier
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[PnC|PnC]] · ⬅ [[04-binomial-coefficients-and-identities|Chapter 4]] · [[06-olympiad-theory|Chapter 6]] ➡ · 📝 [[PnC — Paper|Olympiad Paper]] · ✅ [[PnC — Solutions|Solutions]]

# Chapter 5 — Advanced Methods

*4 sections · 15 questions*

*Chapter 5 · JEE Advanced Weapons*

# Inclusion–Exclusion, Pigeonhole & Recurrences

The three engines behind nearly every "at least one", "no two", "must exist" problem. Inclusion–exclusion is bookkeeping for overlaps; the pigeonhole principle is the existence engine; recurrences turn "count size n" into "count smaller sizes".

`inclusion–exclusion` `rook polynomials` `pigeonhole` `van der Waerden (taste)` `recurrence methods` `Fibonacci everywhere`

### 5.1 Inclusion–Exclusion (IE)

#### Two sets — the Venn diagram logic

**Fig 5.1 — Two sets: add, subtract the double-counted intersection.**

![Fig 5.1 — Two sets: add, subtract the double-counted intersection.](assets/fig-07.svg)


#### The general principle

**Theorem.** For sets $A_1, \dots, A_n$ (inside a universe $X$),

$$\left|\bigcup_{i=1}^{n} A_i\right|
      = \sum_i |A_i| - \sum_{i&lt;j}|A_i\cap A_j|
      + \sum_{i&lt;j&lt;\ell}|A_i\cap A_j\cap A_\ell| - \cdots + (-1)^{n+1}\left|\bigcap_i A_i\right|$$ and therefore $$\left|X \setminus \bigcup_i A_i\right|
      = \sum_{S \subseteq [n]} (-1)^{|S|}\left|\bigcap_{i\in S} A_i\right|,
      \quad \text{with }\bigcap_{i\in\varnothing} A_i = X.$$

> [!abstract] First Principles — the proof counts how many times one element is seen
>
> Track a single element $x \in X$ that lies in exactly $t$ of the sets (say $A_1, \dots, A_t$). How many times does the alternating sum "see" $x$? Once for each non-empty $S \subseteq \{1, \dots, t\}$, with sign $(-1)^{|S|+1}$ on the union side. The number of such sightings is 
> $$ \sum_{j=1}^{t} (-1)^{j+1}\binom{t}{j} \;=\; -\sum_{j=0}^{t}(-1)^j\binom{t}{j} + 1 \;=\; 1, $$
>  using $\sum_{j=0}^{t}(-1)^j\binom{t}{j} = 0$ for $t \ge 1$ (the $x = 1, y = -1$ binomial identity, Ch. 4). So **every element in the union is counted exactly once**, whatever $t\ge 1$; every element outside the union is counted 0 times. The formula is forced. $\square$
>
>
> This proof reveals the whole philosophy: *IE is the unique linear combination of intersection counts that gives each element of the union weight exactly 1.* The same bookkeeping, applied to "avoid all $A_i$", gives the complement formula. Every application below is this one proof with a concrete definition of the events $A_i$.

#### **S1**[JEE Adv][solved][IE · divisibility]How many integers from 1 to 1000 are divisible by 2, 3, or 5 ?

How many integers from 1 to 1000 are divisible by **2, 3, or 5**?

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


Events $A_2 =$ divisible by 2, etc. $|A_2| = 500, |A_3| = 333, |A_5| = 200$; $|A_2\cap A_3| = 166, |A_2\cap A_5| = 100, |A_3\cap A_5| = 66$; $|A_2\cap A_3\cap A_5| = 33$. (Each count is $\lfloor 1000/m \rfloor$ for the lcm $m$.) IE: $500 + 333 + 200 - 166 - 100 - 66 + 33 =$ **Answer: 734**


The "why" to internalize: an integer divisible by exactly two of them (say 2 and 3) is added in $|A_2|, |A_3|$ (twice) and removed in $|A_2 \cap A_3|$ (once) → net 1 ✓. Divisible by all three: added 3 times, removed 3 times, added once → net 1 ✓. *Run this trace on every IE answer — it catches sign errors instantly.*

</details>

#### **S2**[JEE Main][solved][IE · derangements]Permutations of [formula] with [formula] , [formula] , [formula] (positions 4,…

Permutations of $[6]$ with $\sigma(1)\ne 1$, $\sigma(2)\ne 2$, $\sigma(3)\ne 3$ (positions 4, 5, 6 unrestricted).

<details>
<summary>Answer + Reasoning</summary>

Solution


IE on the three forbidden events $E_i = \{\sigma(i) = i\}$: $6! - 3\cdot 5! + 3\cdot 4! - 3\cdot 3! = 720 - 360 + 72 - 18 =$ **Answer: 414**


Partial derangements: "fix exactly which positions are forbidden, derange those" generalizes to $\sum_k (-1)^k \binom{n}{k}(n-k)!$ with $n$ replaced by the forbidden count — the same engine as Ch. 2's derangements.

</details>


#### Rook polynomials — IE for "forbidden positions"

Suppose we want permutations of $[n]$ that avoid a set $B$ of forbidden board positions (position $i$ may not send to value $j$ for $(i,j) \in B$). Let $r_k$ = number of ways to place $k$ non-attacking rooks on the forbidden squares $B$ (attacking = sharing a row or column). Then

$$\#\{\sigma : (\sigma(i), i) \notin B\} = \sum_{k=0}^{n} (-1)^k\, r_k\, (n-k)!$$

> [!abstract] First Principles — why this is plain IE in disguise
>
> Event $E_{(i,j)}$ = "rook lands on forbidden square $(i,j)$". The number of permutations containing a *specified* set of $k$ forbidden squares (in distinct rows and columns — otherwise 0) is $(n-k)!$. IE over the forbidden squares groups by "how many of them occur", and the number of $k$-sets of forbidden squares in distinct rows/columns is exactly the rook number $r_k$. Done. Derangements = $B$ is the diagonal: $r_k = \binom{n}{k}$, recovering $D_n = \sum (-1)^k\binom{n}{k}(n-k)!$. The rook formalism matters when $B$ is a *weird board* (L-shapes, staircases) where $r_k$ is easy but the events are not "symmetric".

#### **S3**[Olympiad][solved][rook board]Count the permutations [formula] of [formula] with [formula] , [formula] , [fo…

Count the permutations $\sigma$ of $[4]$ with $\sigma(1)\ne 2$, $\sigma(2)\ne 1$, $\sigma(3)\ne 4$, $\sigma(4)\ne 3$.

<details>
<summary>Answer + Reasoning</summary>

Solution


Forbidden board: 4 squares — two disjoint "anti-diagonal pairs". Rook numbers: $r_0 = 1$; $r_1 = 4$; $r_2 = \binom42 = 6$ (any two of the 4 squares are in distinct rows and columns — check: rows 1,2,3,4 and columns 2,1,4,3, all distinct ✓); $r_3 = 4$; $r_4 = 1$ (all 4 use distinct rows/columns ✓). Answer: $4! - 4\cdot 3! + 6\cdot 2! - 4\cdot 1! + 1\cdot 0! = 24 - 24 + 12 - 4 + 1 =$ **Answer: 9**

</details>

> [!tip] Key Idea — the universal IE recipe
>
> - Define the **bad events** $A_i$ ("property $i$ occurs").
> - Compute $|\bigcap_{i\in S} A_i|$ for a generic $S$ of size $k$ — usually $\binom{n}{k} \times$ (something free).
> - Write $\sum_k (-1)^k \binom{n}{k} \times (\text{something free})$.
>
>
> Everything you've seen so far — derangements, bounded stars-and-bars (Ch. 4), "all suits present" (Ch. 3), "at least one 0" (Ch. 1) — is this recipe with a different $A_i$.



### 5.2 The Pigeonhole Principle

**Fig 5.2 — If $n+1$ objects enter $n$ boxes, one box holds $\ge 2$. The average is $>1$, so some box beats the average.**

![Fig 5.2 — If $n+1$ objects enter $n$ boxes, one box holds $\ge 2$. The average is $>1$, so some box beats the average.](assets/fig-08.svg)

> [!abstract] First Principles — two forms, one averaging argument
>
> **Weak form.** $n+1$ objects, $n$ boxes $\Rightarrow$ some box has $\ge 2$. Proof: if every box had $\le 1$, total $\le n &lt; n+1$. Contradiction.
>
>
> **Strong form.** Objects distributed into boxes with capacities $m_1, \dots, m_n$: if total $> \sum m_i$, some box exceeds its capacity. (Same contradiction: total $\le \sum m_i$.)
>
>
> The *reasoning* behind every application: **build the boxes deliberately**. The theorem is trivial; the art is choosing a function $\text{object} \to \text{box}$ (a "pigeonhole map") such that (a) the number of boxes is smaller than the number of objects, and (b) "two objects in the same box" implies the conclusion you need. Standard box constructions: residues mod $m$; the *odd part* of an integer; months/quarters for dates; grid subsquares for geometry; initial segments for sequences.

#### Classic applications — each teaches one box construction

#### **S4**[JEE Adv][solved][pigeonhole · odd part]Prove: from any [formula] integers chosen from [formula] , two exist such that…

Prove: from any $n+1$ integers chosen from $\{1, 2, \dots, 2n\}$, two exist such that **one divides the other**.

<details>
<summary>Answer + Reasoning</summary>

Proof (the odd-part construction)


Write each chosen integer uniquely as $2^a \cdot m$ with $m$ *odd*. The odd part $m$ lies in $\{1, 3, 5, \dots, 2n-1\}$ — exactly $n$ possible values (the boxes). We chose $n+1$ integers (the pigeons), so two, say $x = 2^a m$ and $y = 2^b m$, share the same odd part. If $a &lt; b$ then $x \mid y$ (indeed $y/x = 2^{b-a}$ is an integer). Done. $\square$


Note the box map: $x \mapsto$ odd part of $x$. "Same box ⇒ one divides the other" is exactly what the odd-part factorization guarantees. *Refinement & sharpness:* the same argument shows any 11 integers from $\{1,\dots,20\}$ contain such a pair (only 10 odd parts $\le 20$ exist) — and 11 is best possible: $\{11,12,\dots,20\}$ is a 10-element subset with *no* dividing pair, since twice any element of it already exceeds 20.

</details>

#### **S5**[Olympiad][solved][pigeonhole · geometry]Given 5 points in a unit square, prove that two are within distance [formula] …

Given **5 points** in a unit square, prove that two are within distance $\le \dfrac{\sqrt2}{2}$.

<details>
<summary>Answer + Reasoning</summary>

Proof


Split the square into 4 equal subsquares of side $1/2$ (the boxes). By the pigeonhole principle (5 points, 4 boxes), some subsquare contains at least 2 points. Two points in a $1/2 \times 1/2$ square are at distance at most its diagonal, $\frac{\sqrt{1/2}}{1} = \frac{\sqrt2}{2}$. Done. $\square$


General shape: $2n+1$ points in a unit square $\Rightarrow$ 2 within distance $\le \sqrt2/2$. And the bound is sharp: the 4 corner points of the subsquares (plus center)… the extremal configuration is the 4 subsquare centers (mutual distance $\sqrt2/2$).

</details>

> [!example] Olympiad Extension — van der Waerden's theorem, first case
>
> **Van der Waerden $W(r, k)$:** the least $N$ such that every $r$-coloring of $\{1, \dots, N\}$ contains a *monochromatic $k$-term arithmetic progression*. $W(2, 3) = 9$: any red/blue coloring of $[9]$ has a monochromatic $\{a, a+d, a+2d\}$. (It is a theorem that $W(r,k)$ is finite for *all* $r, k$ — one of the founding results of Ramsey theory; the proof of finiteness is deep, but the small cases are excellent pigeonhole practice.)
>
>
> **Proof that $W(2,3) \le 9$.** Suppose a coloring avoids a monochromatic 3-AP. WLOG $1 = R$. *(i) If $3 = R$:* then $2 = B$ (else $1,2,3$); $5 = B$ (else $1,3,5$). If $7 = R$: $4 = B$ (from $1,4,7$), $6 = R$ (from $2,4,6$), $9 = B$ (from $3,6,9$), $8 = B$ (from $6,7,8$) — but then $2,5,8$ are all $B$, contradiction. So $7 = B$ — but then $3,5,7$ are all $B$, contradiction. Hence $3 = B$. *(ii) If $5 = B$:* $4 = R$ (from $3,4,5$), $7 = B$ (from $1,4,7$), $9 = R$ (from $5,7,9$), $6 = R$ (from $5,6,7$), $8 = B$ (from $4,6,8$), $2 = B$ (from $2,5,8$) — but then $2,5,8$ are all $B$, contradiction. Hence $5 = R$. *(iii) Now $1 = R, 3 = B, 5 = R$:* $9 = B$ (from $1,5,9$). If $7 = R$: $4 = B$ (from $1,4,7$), $6 = B$ (from $5,6,7$), $2 = R$ (from $2,4,6$), $8 = B$ (from $2,5,8$) — but $4,6,8$ are all $B$, contradiction. If $7 = B$: $8 = R$ (from $7,8,9$), $2 = B$ (from $2,5,8$). If $4 = R$: $6 = B$ (from $4,6,8$) — but $3,6,9$ all $B$, contradiction. If $4 = B$: $6 = R$ (from $2,4,6$) — but $2,3,4$ all $B$, contradiction. All branches die; no such coloring exists. Hence $W(2,3) \le 9$. And $W(2,3) > 8$: the coloring $R, B, B, R, R, B, B, R$ of $[8]$ has no monochromatic 3-AP (check the list $(1,2,3),(2,3,4),\dots,(6,7,8),(1,3,5),\dots,(2,5,8),(1,4,7)$ — none monochromatic). So $W(2,3) = 9$. $\square$
>
>
> This case-split style — "assume the opposite, follow the forced colors until a clash" — is the standard method for small Ramsey-type statements.



### 5.3 Recurrence methods — counting by structure

> [!abstract] First Principles — the last-step decomposition
>
> Many families of objects of "size $n$" decompose **uniquely** by their last building block: a tiling ends with a vertical domino or two horizontal ones; a binary string ends in 0 or in …10; a composition ends with a part of size $1, 2, 3$. If "ending with block $b_i$" leaves a smaller instance of the *same problem* (of size $n - |b_i|$) and the cases are disjoint and exhaustive, then 
> $$ a_n = a_{n - |b_1|} + a_{n - |b_2|} + \cdots, $$
>  with base cases from the smallest sizes. The method is the sum rule applied *recursively*. Its two failure modes: (a) the last-block cases overlap or miss configurations (→ introduce auxiliary "state" sequences, below); (b) the recurrence is right but you can't solve it (→ generating functions, Chapter 6, or just compute the needed $n$).

#### Worked — domino tilings of a $2 \times n$ board

**Fig 5.3 — The last-step decomposition: $2\times n$ domino tilings satisfy $a_n = a_{n-1} + a_{n-2}$, so $a_n = F_{n+1}$. For $n = 10$: $F_{11} = 89$.**

![Fig 5.3 — The last-step decomposition: $2\times n$ domino tilings satisfy $a_n = a_{n-1} + a_{n-2}$, so $a_n = F_{n+1}$. For $n = 10$: $F_{11} = 89$.](assets/fig-09.svg)


| Object counted by $a_n$ | Last block | Recurrence |
| --- | --- | --- |
| $2\times n$ domino tilings | vertical (1) / two horizontal (2) | $a_n = a_{n-1} + a_{n-2}$, $a_0=1,a_1=1$ → $F_{n+1}$ |
| binary strings of length $n$, no consecutive 1s | ends in 0 / ends in 10 | $a_n = a_{n-1} + a_{n-2}$ → $F_{n+2}$ |
| subsets of $[n]$ with no two consecutive | $n \notin S$ / $n \in S$ (then $n{-}1\notin S$) | $a_n = a_{n-1} + a_{n-2}$ → $F_{n+2}$ |
| compositions of $n$ with parts in $\{1,2,3\}$ | last part 1 / 2 / 3 | $a_n = a_{n-1}+a_{n-2}+a_{n-3}$ (tribonacci) |
| compositions of $n$ into odd parts | GF: $(1-x^2)/(1-x-x^2)$ (§4.4) | $a_n = F_n$ (Ch. 6/§4.4) |
| $3\times n$ domino tilings ($n$ even) | needs auxiliary state | $a_n = 4a_{n-2} - a_{n-4}$ |

#### Fibonacci inside Pascal's triangle — the "same recurrence" proof technique

**Identity:** $\displaystyle\sum_{k\ge 0} \binom{n-k}{k} = F_{n+1}$ (the $k$-th superdiagonal sum).

> [!abstract] First Principles — verify the recurrence, match the initials
>
> Let $D_n = \sum_k \binom{n-k}{k}$. By Pascal's identity on the *top* index, $\binom{n-k}{k} = \binom{n-k-1}{k} + \binom{n-k-1}{k-1}$; shifting the second sum ($k\mapsto k+1$): $D_n = D_{n-1} + D_{n-2}$. The Fibonacci numbers satisfy the same recurrence, and $D_0 = 1 = F_1, D_1 = 1 = F_2$. Same recurrence + same initials ⇒ $D_n = F_{n+1}$. This "match recurrence and base cases" technique is how you prove *any* closed form for a recursively defined sequence — and it connects Pascal's triangle to tiling counts without a bijection (though one exists: tilings of a $1\times n$ board, vertical tile ↔ part 1, horizontal pair ↔ part 2… i.e. compositions into $\{1,2\}$).

#### **S6**[JEE Adv][solved][recurrence]In how many ways can 6 people sit in a row so that no two of A, B, C sit toget…

In how many ways can 6 people sit in a row so that no two of A, B, C sit together? (i.e. A, B, C pairwise non-adjacent — the gap method, Ch. 2, now framed as a decomposition).

<details>
<summary>Answer + Reasoning</summary>

Solution


Gap method: arrange the other 3 people: $3! = 6$; choose 3 of the 4 gaps: $\binom43 = 4$; order A, B, C: $3! = 6$. Total $6 \cdot 4 \cdot 6 =$ **Answer: 144**

</details>

#### **S7**[JEE Main][solved][recurrence]A stair has 10 steps. Each move is 1 or 2 steps. How many ways to climb? (Ch. …

A stair has 10 steps. Each move is 1 or 2 steps. How many ways to climb? (Ch. 1's P6 with a part-3 removed.)

<details>
<summary>Answer + Reasoning</summary>

Solution


$a_n = a_{n-1} + a_{n-2}$, $a_0 = 1, a_1 = 1$: $1,1,2,3,5,8,13,21,34,55,89$. $a_{10} =$ **Answer: 89** (it is $F_{11}$).

</details>



### 5.4 Practice set

#### **P1**[JEE Main][practice][IE]How many integers from 1 to 100 are divisible by 2 or 3?

How many integers from 1 to 100 are divisible by 2 or 3?

<details>
<summary>Answer + Reasoning</summary>

$50 + 33 - 16 =$ **67**.

</details>

#### **P2**[JEE Adv][practice][pigeonhole (generalization)]Prove: from any 101 integers chosen from [formula] , two exist with one dividi…

Prove: from any 101 integers chosen from $\{1, \dots, 200\}$, two exist with one dividing the other.

<details>
<summary>Answer + Reasoning</summary>

Odd-part construction with $n = 100$: 101 integers, 100 odd parts $\le 200$ → two share an odd part → divisibility. (This is exactly S4 with $n = 100$; stating it as a general $n$ is the lesson: *prove the general form, not the instance.*)

</details>

#### **P3**[JEE Main][practice][complement + IE]How many integers from 1 to 1000 are divisible by none of 2, 3, 5?

How many integers from 1 to 1000 are divisible by **none** of 2, 3, 5?

<details>
<summary>Answer + Reasoning</summary>

$1000 - 734 =$ **266** (from S1).

</details>

#### **P4**[JEE Main][practice][recurrence]Domino tilings of a [formula] board.

Domino tilings of a $2 \times 5$ board.

<details>
<summary>Answer + Reasoning</summary>

$F_6 =$ **8**.

</details>

#### **P5**[JEE Adv][practice][recurrence + state]Binary strings of length 6 that start with 1 and have no consecutive 1s.

Binary strings of length 6 that **start with 1** and have no consecutive 1s.

<details>
<summary>Answer + Reasoning</summary>

Start with 1 ⇒ second symbol 0 ⇒ remaining 4 symbols: any no-consecutive-1s string of length 4: $F_6 = 8$. Answer **8**.

</details>

#### **P6**[Olympiad][practice][same-recurrence proof]Prove [formula] (define [formula] ).

Prove $\displaystyle\sum_{k\ge 0}\binom{n-k}{k} = F_{n+1}$ (define $F_1 = F_2 = 1$).

<details>
<summary>Answer + Reasoning</summary>

Shown in §5.3: $D_n = D_{n-1} + D_{n-2}$ by Pascal, $D_0 = D_1 = 1 = F_1, F_2$. Bonus bijection: the summand $\binom{n-k}{k}$ counts tilings of a $1\times n$ board with exactly $k$ horizontal dominoes… (check: a tiling with $k$ horizontals uses $k+2k = 3k$ cells? no — $k$ horizontals cover $2k$ cells, and $n - 2k$ verticals cover $n - 2k$, total $n$ ✓, and the number of such tilings is $\binom{n-k}{k}$ (choose positions of the $k$ horizontals among the $n-k$ tiles). So the sum is "all tilings" $= F_{n+1}$ — the identity has a *direct* tiling reading too.)

</details>

#### **P7**[Olympiad][practice][van der Waerden W(2,3)]Prove: any red/blue coloring of [formula] contains a monochromatic 3-term arit…

Prove: any red/blue coloring of $\{1,\dots,9\}$ contains a monochromatic 3-term arithmetic progression, and the statement fails for $\{1,\dots,8\}$.

<details>
<summary>Answer + Reasoning</summary>

The upper bound is the full case analysis of §5.2 (follow it line by line — each branch is forced, not guessed). For the lower bound, exhibit the coloring $R\, B\, B\, R\, R\, B\, B\, R$ of $[8]$ and check the 15 three-term progressions of $[8]$: six of gap 1, four of gap 2, three of gap 3, two of gap 4 — none monochromatic (each contains both colors by direct inspection). Hence $W(2,3) = 9$.

</details>

#### **P8**[JEE Adv][practice][IE + bounded]Non-negative solutions of [formula] with [formula] .

Non-negative solutions of $x + y + z = 20$ with $x \le 7$.

<details>
<summary>Answer + Reasoning</summary>

$\binom{22}{2} - \binom{14}{2} = 231 - 91 =$ **140** (total minus $x \ge 8$, shifted to a non-negative equation of sum 12 in 3 variables).

</details>



---
