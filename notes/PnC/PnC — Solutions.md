---
title: "PnC — Olympiad Paper Solutions"
aliases:
  - PnC Solutions
module: "PnC"
module_title: "PnC"
type: solutions
tags:
  - pnc
  - solutions
  - olympiad
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[PnC — Paper|Paper]] · 📖 [[PnC|PnC]]

# Olympiad Paper · Solutions & marking guide

*Assessment · Answer Book*

# Full Solutions — The PnC Olympiad Paper

All 50 solutions with the reasoning written out: the bijection, the inclusion–exclusion table, the generating function, or the case analysis — the thing that earns the marks. Answers verified by direct enumeration wherever a computer can be trusted more than a hand.

`A · Q1–Q8` `B · Q9–Q12` `C · Q13–Q17` `D · Q18–Q22` `E · Q23–Q28` `F · Q29–Q32` `G · Q33–Q38` `+ Q39–Q40` `H · Q41–Q46` `I · Q47–Q50`

### A Arrangements

#### **Q1**[gaps & repeats]



<details>
<summary>Answer + Reasoning</summary>

Solution


$\text{PERMUTATION}$: 11 letters — vowels $E,U,A,I,O$ (5, distinct), consonants $P,R,M,T,T,N$ (6, with $T$ twice). No two vowels adjacent ⟺ place the consonants first, then seat the vowels in distinct gaps.


Consonants: $\frac{6!}{2!} = 360$. They create 7 gaps ($\_C\_C\_C\_C\_C\_C\_$); choose 5 for the vowels: $\binom{7}{5} = 21$; arrange the 5 distinct vowels: $5! = 120$.


$360 \times 21 \times 120 =$ **Answer: 907,200**


Verified by direct enumeration over all distinct consonant orders and vowel placements.

</details>

#### **Q2**[onto · IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


Onto $f : [5] \to [3]$: $3!\,S(5,3) = 6 \times 25 = 150$ (Ch 4, S3: onto functions are block-partitions with labeled blocks; $S(5,3) = 25$).


Bad: $f(1) = f(2)$. Merge $\{1,2\}$ into one element: onto maps from a 4-element set to $[3]$: $3!\,S(4,3) = 6 \times 6 = 36$.


$150 - 36 =$ **Answer: 114** (brute-force checked: 114 of the $3^5 = 243$ maps).

</details>

#### **Q3**[gaps]



<details>
<summary>Answer + Reasoning</summary>

Solution


Men first: $4! = 24$. Five gaps, choose 4 for the women: $\binom{5}{4} = 5$; arrange the women: $4! = 24$.


$24 \times 5 \times 24 =$ **Answer: 2,880**

</details>

#### **Q4**[circular · gaps]



<details>
<summary>Answer + Reasoning</summary>

Solution


Seat the other 9 people around the table: $(9-1)! = 8! = 40{,}320$. They create 9 gaps; choose 3 for $A,B,C$: $\binom{9}{3} = 84$; arrange them: $3! = 6$. One per gap forces pairwise non-adjacency (a circular version of the gap method — Ch 2, Fig 2.1).


$40{,}320 \times 84 \times 6 =$ **Answer: 20,321,280**


**Sanity check on a small model (enumeration-verified):** $n = 6$ people, 2 special, round table, special pairwise non-adjacent: gap method $(6-2-1)!\binom{4}{2}2! = 6 \times 6 \times 2 = 72$; complement method $5! - 2 \cdot 4! = 120 - 48 = 72$ (all circular arrangements minus "special pair adjacent": glue them into one block — 5 objects in a circle, $4!$, times the 2 orders of the pair). Both roads agree.

</details>

#### **Q5**[derangements · IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


All derangements of 6: $D_6 = \sum_{j=0}^{6} (-1)^j \binom{6}{j}(6-j)!
        = 720 - 720 + 360 - 120 + 30 - 6 + 1 = 265$.


Subtract those with letter $A$ in envelope $B$: fix $\sigma(1) = 2$. The remaining letters $\{2,3,4,5,6\}$ go to envelopes $\{1,3,4,5,6\}$, with letters $3,4,5,6$ forbidden from their own envelopes (letter 2 has no forbidden envelope — envelope 2 is taken). IE over the 4 forbidden positions: 
$$ \sum_{j=0}^{4} (-1)^j \binom{4}{j} (5-j)! = 120 - 4\cdot 24 + 6\cdot 6 - 4\cdot 2 + 1 = 53. $$



$265 - 53 =$ **Answer: 212** (verified by direct enumeration of the 265 derangements).

</details>

#### **Q6**[choice · order]



<details>
<summary>Answer + Reasoning</summary>

Solution


Choose the committee: $\binom{12}{5} = 792$; choose the chairman from its 5 members: 5.


$792 \times 5 =$ **Answer: 3,960** (equivalently, chairman first: $12 \times \binom{11}{4} = 12 \times 330$).

</details>

#### **Q7**[couples]



<details>
<summary>Answer + Reasoning</summary>

Solution


Choose which 4 of the 8 couples are represented: $\binom{8}{4} = 70$; from each chosen couple, pick one of the 2: $2^4 = 16$.


$70 \times 16 =$ **Answer: 1,120**

</details>

#### **Q8**[alternating · slots]



<details>
<summary>Answer + Reasoning</summary>

Solution


Two alternating patterns (M-W-…-M or W-M-…-W); by symmetry count one and double. Men in positions $0, 2, 4, 6, 8$ (0-indexed row of 10), women in $1,3,5,7,9$.


Place man $A$ first — his slot determines the allowed slots for $B$: $A$ at 0: only slot 1 (1 choice); $A$ at 2: slots 1, 3; $A$ at 4: slots 3, 5; $A$ at 6: slots 5, 7; $A$ at 8: slots 7 and 9 — *two* choices, since position 8 is adjacent to both 7 and 9 (the classic trap is treating both ends as degree 1). Total over $A$'s slots: $1 + 2 + 2 + 2 + 2 = 9$. For each, the other 4 men: $4!$, the other 4 women: $4!$.


$2 \times 9 \times 4! \times 4! = 2 \times 9 \times 576 =$ **Answer: 10,368** (verified by exhaustive enumeration of all $2 \cdot 5! \cdot 5! = 28{,}800$ alternating arrangements).

</details>


### B Stars & Bars

#### **Q9**[bounded IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


Positive solutions of $x+y+z+w = 20$: $\binom{19}{3} = 969$. Subtract solutions with some variable $\ge 9$: set $x = 9 + x'$ ($x' \ge 0$): $x' + y + z + w = 11$ with $y,z,w \ge 1$: $\binom{11-1}{3} = \binom{10}{3} = 165$; four variables: $4 \times 165 = 660$. Add back two variables $\ge 9$: $x' + y' + z + w = 2$ with $z, w \ge 1$: forces $z = w = 1$, $x' = y' = 0$: 1 way per pair: $\binom{4}{2} \times 1 = 6$. Three variables $\ge 9$ would need sum $\ge 27$: 0.


$969 - 660 + 6 =$ **Answer: 315** (brute-force checked over all 4-tuples in $[1,8]$.)


The bounded engine in compact form (Ch 4): $\sum_{j} (-1)^j \binom{4}{j}\binom{16 - 8j + 3}{3}$ after the substitution $x_i = 1 + y_i$ (sum 16, cap 7): $969 - 4\binom{11}{3} + 6\binom{3}{3} = 315$.

</details>

#### **Q10**[bounded IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


Non-negative solutions of $x_1 + x_2 + x_3 = 15$: $\binom{17}{2} = 136$. Subtract some $x_i \ge 7$: $x_i' + x_j + x_k = 8$: $\binom{10}{2} = 45$ each: $3 \times 45 = 135$. Add back two $\ge 7$: $x_i' + x_j' + x_k = 1$: $\binom{3}{2} = 3$ each: $3 \times 3 = 9$.


$136 - 135 + 9 =$ **Answer: 10** (verified by enumeration; the 10 solutions are the 3-permutations of $(7,7,1), (7,6,2), (7,5,3), (6,6,3), (6,5,4)$).

</details>

#### **Q11**[digits · stars]



<details>
<summary>Answer + Reasoning</summary>

Solution


Digits $d_1 d_2 d_3 d_4$, $d_1 \ge 1$, sum 9. Set $d_1' = d_1 - 1$: $d_1' + d_2 + d_3 + d_4 = 8$, all non-negative: $\binom{11}{3} = 165$. No upper bound binds: $d_1 = 9$ (giving 9000) is allowed, and $d_i \ge 10$ is impossible when the total is 9.


**Answer: 165** (brute-force checked over all 4-digit numbers.)

</details>

#### **Q12**[GF · Fibonacci]



<details>
<summary>Answer + Reasoning</summary>

Proof


**Step 1 (the GF).** A composition into odd parts is a *sequence* of odd pieces, each of weight $x^1, x^3, x^5, \dots$: 
$$ A(x) = \frac{1}{1 - (x + x^3 + x^5 + \cdots)}
        = \frac{1}{1 - \frac{x}{1-x^2}} = \frac{1 - x^2}{1 - x - x^2}. $$
 **Step 2 (the Fibonacci GF).** With $F_1 = F_2 = 1$, 
$$ \sum_{n \ge 0} F_{n+1} x^n = \frac{1}{1 - x - x^2} $$
 (check: $(1 - x - x^2)(1 + x + 2x^2 + 3x^3 + \cdots) = 1 + 0x + 0x^2 + \cdots$, since $F_{n+1} - F_n - F_{n-1} = 0$ for $n \ge 2$).


**Step 3 (match coefficients).** $A(x) = (1 - x^2)\sum_{n \ge 0} F_{n+1}x^n$, so $a_0 = 1$, $a_1 = 1$, and for $n \ge 2$: $a_n = F_{n+1} - F_{n-1} = F_n$ (by the recurrence $F_{n+1} = F_n + F_{n-1}$).


$a_n = F_n$ for all $n \ge 1$. Values: $1, 1, 2, 3, 5, 8, 13, 21$ for $n = 1, \dots, 8$ (matches direct enumeration, e.g. $a_4 = 3$: $1+1+1+1, 1+3, 3+1$).

</details>


### C Binomial Coefficients & Double Counting

#### **Q13**[bounded GF]



<details>
<summary>Answer + Reasoning</summary>

Solution


$[x^{10}](1 + x + \cdots + x^4)^5$ counts non-negative solutions of $x_1 + \cdots + x_5 = 10$ with each $x_i \le 4$ (bounded engine, Ch 4): 
$$ \binom{14}{4} - 5\binom{9}{4} + \binom{5}{2}\binom{4}{4} - 0
        = 1001 - 630 + 10 = 381. $$
 (Terms: unrestricted; one variable $\ge 5$; two variables $\ge 5$; three would need $\ge 15 > 10$.)


**Answer: 381** (checked by polynomial multiplication.)

</details>

#### **Q14**[Vandermonde]



<details>
<summary>Answer + Reasoning</summary>

Proof


Using $\binom{2n}{k} = \binom{2n}{2n-k}$, the sum is a Vandermonde convolution: 
$$ \sum_{k} (-1)^k \binom{2n}{k}\binom{2n}{2n-k}
        = [x^{2n}]\, (1 - x)^{2n}(1 + x)^{2n}
        = [x^{2n}]\, (1 - x^2)^{2n} = (-1)^n \binom{2n}{n}, $$
 since $(1 - x^2)^{2n} = \sum_j \binom{2n}{j}(-x^2)^j$ has its $x^{2n}$ term at $j = n$. $\square$


**Double-counting face:** $[x^{2n}](1 - x^2)^{2n}$ counts choices of exactly $n$ of the $2n$ factors to contribute their $-x^2$ term — $\binom{2n}{n}$ choices, each contributing $(-1)^n$. Small case $n = 1$: $1 - 4 + 1 = -2 = -\binom{2}{1}$ ✓.

</details>

#### **Q15**[Vandermonde]



<details>
<summary>Answer + Reasoning</summary>

Proof


$\binom{n}{k+1} = \binom{n}{n-k-1}$, so 
$$ \sum_k \binom{n}{k}\binom{n}{k+1}
        = \sum_k \binom{n}{k}\binom{n}{(n-1)-k}
        = \binom{2n}{n-1} = \binom{2n}{n+1}. $$
 $\square$


**Committee reading:** a committee of $n - 1$ chosen from group A ($n$ people) and group B ($n$ people): pick $k$ from A and $n - 1 - k$ from B: $\binom{n}{k}\binom{n}{n-1-k}$. Sum over $k$: total committees $\binom{2n}{n-1}$.

</details>

#### **Q16**[Vandermonde]



<details>
<summary>Answer + Reasoning</summary>

Proof


$\binom{n+1}{k+1} = \binom{n+1}{n-k}$, so 
$$ \sum_k \binom{n}{k}\binom{n+1}{k+1}
        = \sum_k \binom{n}{k}\binom{n+1}{n-k}
        = \binom{2n+1}{n}. $$
 $\square$


**Committee reading:** a committee of $n$ from group A ($n$ people) and group B ($n + 1$ people): $k$ from A forces $n - k$ from B: $\binom{n}{k}\binom{n+1}{n-k} = \binom{n}{k}\binom{n+1}{k+1}$. Total: $\binom{2n+1}{n}$. (Note the two pools are deliberately unequal — that's what makes the $k+1$ appear.)

</details>

#### **Q17**[symmetry · GF]



<details>
<summary>Answer + Reasoning</summary>

Solution


**(a) $k$ odd.** Let the cyclic group $C_{2n}$ act on $k$-subsets by $A \mapsto A + 1 \pmod{2n}$ (each element $+1$, with $2n$ wrapping to $1$). If $t \in \{0,1\}$ elements wrap, the sum changes by $(k - t)(+1) + t(1 - 2n) = k - 2nt \equiv k \equiv 1 \pmod 2$ — an *odd* change, since $2n$ is even: **every single step flips the parity of the sum.** Take any orbit of size $d$: walking around it flips parity $d$ times and returns to the start, so $d$ is even, and exactly $d/2$ of the orbit's subsets have odd sum. Summing over orbits: $\#\{\text{odd-sum } k\text{-subsets}\} =
        \frac{1}{2}\binom{2n}{k}$.


**(b) $k$ even.** Let $D = \sum_{S, |S|=k} (-1)^{\sum S}$ (even-sum minus odd-sum). Then 
$$ D = [x^k]\, \prod_{i=1}^{2n} (1 + (-1)^i x)
        = [x^k]\, (1 - x)^n (1 + x)^n = [x^k]\, (1 - x^2)^n
        = (-1)^{k/2}\binom{n}{k/2}. $$
 With $E + O = \binom{2n}{k}$ and $E - O = D$: $\#O = \frac{1}{2}\left(\binom{2n}{k} + (-1)^{k/2+1}\binom{n}{k/2}\right)$.


**Verification $n = 3, k = 2$:** the 2-subsets of $\{1,\dots,6\}$ with odd sum are exactly the odd-even pairs: $3 \times 3 = 9$; formula: $\frac{1}{2}(15 + (-1)^{2}\binom{3}{1}) = \frac{15 + 3}{2} = 9$ ✓. (For even $k$ the parity does *not* flip under the cyclic shift — the shift changes the sum by an even amount — which is exactly why the count escapes $\frac{1}{2}$ by the $\frac{1}{2}(-1)^{k/2+1}\binom{n}{k/2}$ correction.)

</details>


### D Inclusion–Exclusion & Rooks

#### **Q18**[rook · derangement]



<details>
<summary>Answer + Reasoning</summary>

Solution


Forbidden board: the main diagonal. Its rook numbers: $r_j = \binom{5}{j}$ (choose $j$ diagonal squares; rooks on distinct diagonal squares are automatically non-attacking, so 1 way). Rook method (Ch 5, S3): 
$$ \sum_{j=0}^{5} (-1)^j r_j (5 - j)!
        = \sum_{j=0}^{5} (-1)^j \binom{5}{j}(5-j)!
        = 120 - 120 + 60 - 20 + 5 - 1 = 44. $$



**Answer: 44** — this is exactly the derangement number $D_5$.


**Why they agree:** a placement of 5 non-attacking rooks on a $5 \times 5$ board is a permutation matrix — row $i$ has its rook in column $\sigma(i)$. "None on the diagonal" is $\sigma(i) \ne i$ for all $i$: a derangement of $[5]$. The rook computation and $D_5 = \sum (-1)^j \binom{5}{j}(5-j)!$ are the same formula with the same combinatorial content.

</details>

#### **Q19**[repeats · IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


$\text{AABBC}$: 5 letters, total arrangements $\frac{5!}{2!\,2!} = 30$.


**Complement (block method):** arrangements with adjacent A's: glue $\text{AA}$ into one block: arrange $(\text{AA}), B, B, C$: $\frac{4!}{2!} = 12$. Answer: $30 - 12 = 18$.


**Direct (gaps):** choose 2 of the 5 positions for the A's, non-adjacent: $\binom{5}{2} - 4 = 6$; arrange $B,B,C$ in the rest: $\frac{3!}{2!} = 3$: $6 \times 3 = 18$.


**Answer: 18** (both methods agree; verified by enumeration of the 30 distinct words.)

</details>

#### **Q20**[bounded IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


Substitute $y_i = 7 - x_i$ (reflected, so the cap becomes a floor): $y_1 + \cdots + y_5 = 35 - 30 = 5$, $0 \le y_i \le 6$. The cap never binds ($5 \le 6$): unrestricted non-negative solutions: $\binom{9}{4} = 126$.


**Answer: 126**


**IE cross-check (without the reflection):** $\binom{29}{4} - 5\binom{22}{4} + 10\binom{15}{4} - 10\binom{8}{4}$ $= 23{,}751 - 36{,}575 + 13{,}650 - 700 = 126$ ✓. (The reflection turns a 4-term IE with huge numbers into one binomial — use it whenever the cap is close to the average: here average $6 &lt; 7$, so the complement is tiny.)

</details>

#### **Q21**[partial IE]



<details>
<summary>Answer + Reasoning</summary>

Solution


IE over the three bad events $\sigma(1) = 2$, $\sigma(2) = 1$, $\sigma(3) = 3$: 
$$ 120 - 3 \times 4! + 3 \times 3! - 2! = 120 - 72 + 18 - 2 = 64. $$
 (Single events: $4!$ each. Pairs: pin two positions, $3!$ each. Triple: $2!$.)


**Answer: 64** (enumeration-checked.)

</details>

#### **Q22**[rook]



<details>
<summary>Answer + Reasoning</summary>

Solution


3 non-attacking rooks on $4 \times 4$, avoiding the diagonal. Choose $j$ rooks to land on the $j$ chosen diagonal squares, then place the remaining $3 - j$ on the remaining $(4-j) \times (4-j)$ board freely: 
$$ \sum_{j=0}^{3} (-1)^j \binom{4}{j} \binom{4-j}{3-j}^2 (3-j)!
        = 96 - 4 \times 9 \times 2 + 6 \times 4 \times 1 - 4 \times 1
        = 96 - 72 + 24 - 4 = 44. $$



**Answer: 44** (enumeration-checked.)


**On the "coincidence" with Q18:** both are IE sums, but with different summands — Q18 is $\sum (-1)^j \binom{5}{j}(5-j)!$ (a derangement), Q22 is $\sum (-1)^j \binom{4}{j}\binom{4-j}{3-j}^2(3-j)!$ (a restricted placement). Equal values here, no reason in general: 5 rooks on $5 \times 5$ avoiding the diagonal is $44$, but 4 rooks on $4 \times 4$ avoiding the diagonal is $D_4 = 9$, and 3 rooks on $3 \times 3$ is $D_3 = 2$. When two different IE sums agree, look for a reason — and when they *don't* agree in nearby cases, you've found the coincidence. (This question is designed to train exactly that reflex.)

</details>


### E Pigeonhole & Extremal

#### **Q23**[residues]



<details>
<summary>Answer + Reasoning</summary>

Proof


Write the integers as $a_1, \dots, a_{2n+1}$ and form the partial sums $s_k = a_1 + \cdots + a_k$ for $k = 1, \dots, 2n+1$. **Case 1:** some $s_k \equiv 0 \pmod{2n+1}$: the block $a_1, \dots, a_k$ has the required sum. **Case 2:** no $s_k \equiv 0$. Then the $2n+1$ residues of the $s_k$'s live in $\{1, 2, \dots, 2n\}$ — only $2n$ boxes. By the pigeonhole principle, $s_i \equiv s_j \pmod{2n+1}$ for some $i &lt; j$; the consecutive block $a_{i+1}, \dots, a_j$ has sum $s_j - s_i \equiv 0$. $\square$

</details>

#### **Q24**[Ramsey R(3,3)]



<details>
<summary>Answer + Reasoning</summary>

Proof


**(a) $R(3,3) \le 6$.** In any red/blue coloring of $K_6$, take a vertex $v$. Its 5 incident edges: by PHP, at least 3 are the same color — say red — to vertices $x, y, z$. If any of $xy, yz, zx$ is red, we have a red triangle with $v$; if all three are blue, then $xyz$ is a blue triangle. Either way, a monochromatic triangle exists. $\square$


**(b) $R(3,3) > 5$.** Color the edges of the 5-cycle $012340$ red and the other five edges (the chords) blue. The red graph is a 5-cycle — triangle-free. The blue graph is the *complement* of a 5-cycle, which is again a 5-cycle (the star polygon $024130$) — also triangle-free. So no monochromatic triangle: $R(3,3) > 5$. Combined with (a): $R(3,3) = 6$.


**(c) Why the probabilistic method doesn't prove (b).** Coloring $K_5$ at random, $\mathbb{E}[\text{mono triangles}] = \binom{5}{3} \cdot 2 \cdot 2^{-3}
        = 10/4 = 2.5$. The first-moment method concludes "some coloring has 0" only when the expectation is $&lt; 1$ — here it is $2.5 > 1$, so the method proves nothing (a mean of 2.5 is perfectly compatible with the minimum being 0). The lower bound genuinely needs the construction. (The method does work for larger parameters — e.g. $\binom{6}{4}/2^5 = 15/32 &lt; 1$ gives $R(4,4) \ge 7$; Ch 6, §6.6.)


Brute-force confirmation: exactly 12 of the $2^{10}$ colorings of $K_5$ are triangle-free in both colors (the 5-cycle construction and its symmetries), and 0 of the $2^{15}$ colorings of $K_6$.

</details>

#### **Q25**[van der Waerden]



<details>
<summary>Answer + Reasoning</summary>

Proof


**Upper bound (citing Ch 5, §5.2):** the full case analysis shows every red/blue coloring of $\{1, \dots, 9\}$ has a monochromatic 3-term arithmetic progression: WLOG $1$ is red; the subcases (3 red vs 3 blue, then the forced dominoes of AP-closures) each force a monochromatic $(x, x+d, x+2d)$ inside 9. Hence $W(2,3) \le 9$.


**Sharpness.** Color $\{1, \dots, 8\}$ as $R\, B\, B\, R\, R\, B\, B\, R$ (positions $1,4,5,8$ red; $2,3,6,7$ blue).


| color | set | check |
| --- | --- | --- |
| red | $\{1,4,5,8\}$ | APs with all 3 terms in $[8]$: d=1: none; d=2: $(4,6,8)$ needs $6\notin$ red, $(1,3,5)$ needs 3, $(3,5,7)$ needs 3,7; d=3: $(1,4,7)$ needs 7, $(2,5,8)$ needs 2 — none |
| blue | $\{2,3,6,7\}$ | d=1: $(2,3,4)$ needs 4, $(6,7,8)$ needs 8; d=2: $(2,4,6)$ needs 4, $(3,5,7)$ needs 5; d=3: $(2,5,8)$ needs 5,8 — none |


So no monochromatic 3-AP on $[8]$: $W(2,3) \ge 9$. Hence $W(2,3) = 9$. $\square$

</details>

#### **Q26**[geometry PH]



<details>
<summary>Answer + Reasoning</summary>

Proof


Cut the unit square into 4 squares of side $\frac12$ (the two midlines). Five points into four squares: two points $P, Q$ share a small square. Their distance is at most the small square's diagonal: 
$$ |PQ| \le \sqrt{\left(\tfrac12\right)^2 + \left(\tfrac12\right)^2} = \frac{\sqrt 2}{2}. $$
 $\square$


**Sharpness of the constant:** take the 4 corners and the center of the square. Corner-corner distances are $1$ or $\sqrt2$ (all $> \frac{\sqrt2}{2}$); every corner-center distance is exactly $\sqrt{\frac14 + \frac14} = \frac{\sqrt2}{2}$. So this 5-point configuration has *every* pair at distance $\ge \frac{\sqrt2}{2}$: the guarantee "some pair is within $\frac{\sqrt2}{2}$" is tight — no smaller constant would work for all configurations.

</details>

#### **Q27**[residue pairs]



<details>
<summary>Answer + Reasoning</summary>

Proof


Reduce the $\frac{n+3}{2}$ integers modulo $n$. Since $n$ is odd, the non-zero residues split into $\frac{n-1}{2}$ *pairs* $\{r, n-r\}$ (no residue is its own negative except 0, because $2x \equiv 0 \pmod n$ with $n \mid 2x$ and $\gcd(2, n) = 1$ forces $n \mid x$). Make the boxes $\{0\}$ and the $\frac{n-1}{2}$ pairs: $\frac{n+1}{2}$ boxes. With $\frac{n+3}{2}$ integers (one more than the boxes), two integers land in the same box: either both $\equiv 0$ (sum $\equiv 0$) or $\equiv r, n-r$ (sum $\equiv 0$). $\square$


**Where the oddness enters:** the box count $\frac{n+1}{2}$ uses that 0 is the *only* self-inverse residue. If $n$ were even, $n/2$ would be self-inverse ($2 \cdot n/2 = n \equiv 0$) and would form an extra box — the count becomes $\frac{n}{2} + 1$ and the pigeonhole threshold $\frac{n}{2} + 2$. The argument survives even $n$ in this modified form, but the clean $\frac{n+3}{2}$ bound stated here is the odd-$n$ one.

</details>

#### **Q28**[construction]



<details>
<summary>Answer + Reasoning</summary>

Proof


Consider the 100 consecutive integers 
$$ (101)! + 2,\ (101)! + 3,\ \dots,\ (101)! + 101. $$
 For $2 \le j \le 101$: $j \mid (101)!$ (since $j \le 101$), so $j \mid (101)! + j$. Also $1 &lt; j &lt; (101)! + j$ (the number is larger than its divisor $j$ and $j > 1$): hence $(101)! + j$ is composite. Ten hundred… one hundred consecutive composites, constructed without testing a single number for primality. $\square$


**Generalization:** for every $m \ge 1$, the $m$ consecutive integers $(m+1)! + 2, \dots, (m+1)! + (m+1)$ are all composite — so arbitrarily long blocks of consecutive composites exist. (The factorial trick gives existence; the actual gaps between primes grow much faster, but this proof needs nothing about prime distribution.)

</details>


### F Lattice Paths & Catalan

#### **Q29**[reflection]



<details>
<summary>Answer + Reasoning</summary>

Proof (the bijection, stated and proved)


**Bijection.** Let $\mathcal{B}$ be the set of "bad" paths $(0,0) \to (n,n)$ that at some point reach the line $y = x + 1$ (i.e. go strictly above the diagonal). A bad path has a *first* point $P$ on $y = x + 1$; reflect the portion of the path up to and including $P$ in the line $y = x + 1$ (map $(u, v) \mapsto (v-1, u+1)$ — the involution fixing exactly that line). The image starts at $(-1, 1)$ (the mirror of $(0,0)$), ends at $(n, n)$, and is a monotone path. **Inverse:** any path from $(-1,1)$ to $(n,n)$ must meet $y = x + 1$ — it starts with $y - x = 2$ (above the line) and ends with $y - x = 0$ (below it), and steps change $y - x$ by at most 1 — so it has a first-crossing point; reflect that prefix. The two operations undo each other, so $|\mathcal{B}|$ equals the number of paths $(-1,1) \to (n,n)$: those use $n+1$ R-steps and $n-1$ U-steps: $\binom{2n}{n-1} = \binom{2n}{n+1}$.


Good paths = total paths minus bad paths: 
$$ \binom{2n}{n} - \binom{2n}{n+1}
        = \binom{2n}{n}\left(1 - \frac{n}{n+1}\right)
        = \frac{1}{n+1}\binom{2n}{n} = C_n. $$
 $\square$


Check: $n = 3$: $\binom{6}{3} - \binom{6}{4} = 20 - 15 = 5 = C_3$ — the five Dyck paths $RRRUUU, RRURUU, RRUURU, RURRUU, RURURU$, which you can enumerate in ten seconds to build intuition for what the bijection is saving you from.

</details>

#### **Q30**[Dvoretzky–Motzkin]



<details>
<summary>Answer + Reasoning</summary>

Proof


Identical reflection argument with general target: bad paths $(0,0) \to (a,b)$ (reaching $y = x + 1$) biject to paths $(-1,1) \to (a,b)$: those use $a+1$ R-steps and $b-1$ U-steps: $\binom{a+b}{b-1}$ of them. Hence 
$$ \binom{a+b}{b} - \binom{a+b}{b-1}
        = \binom{a+b}{b}\left(1 - \frac{b}{a+1}\right)
        = \frac{a-b+1}{a+1}\binom{a+b}{b}. $$
 $\square$


**Catalan check:** $a = b = n$: $\frac{1}{n+1}\binom{2n}{n}$ ✓. **Sanity:** $a = 5, b = 3$: $\frac{3}{6}\binom{8}{3} = 28$; total $\binom{8}{3} = 56$, bad $\binom{8}{2} = 28$ — exactly half, as the formula says.

</details>

#### **Q31**[ballot]



<details>
<summary>Answer + Reasoning</summary>

Solution


A = R-step, B = U-step; "A strictly ahead after every vote" = the path $(0,0) \to (5,3)$ has $x &gt; y$ at every prefix. First step is R, so this equals paths $(1,0) \to (5,3)$ that never touch $y = x$: total minus bad, where bad paths (first touch of $y = x$) reflect to paths $(0,1) \to (5,3)$: 
$$ \binom{7}{3} - \binom{7}{2} = 35 - 21 = 14. $$
 Equivalently, the ballot formula: $\frac{5-3}{5+3}\binom{8}{3} = \frac{1}{4} \cdot 56
        = 14$.


**Answer: 14**

</details>

#### **Q32**[paths · reflection]



<details>
<summary>Answer + Reasoning</summary>

Solution


**(a)** "Strictly below at every interior point" forces first step R (to $(1,0)$) and last step U (from $(5,4)$); in between, $y &lt; x$. Shift coordinates: $(x', y') = (x - 1, y)$. The path becomes a path $(0,0) \to (4,4)$, and $y &lt; x = x' + 1$ becomes $y' \le x'$: *exactly* a Dyck path of size 4. Count: $C_4 = \binom{8}{4} - \binom{8}{5} = 70 - 56 = 14$.


(a) **Answer: 14** (equivalently $\binom{2n-2}{n-1} - \binom{2n-2}{n-2}$ at $n = 5$.)


**(b)** Through $(1,3)$: $\binom{4}{1}\binom{4}{3} = 4 \times 4 = 16$. Total $(4,4)$ paths: $\binom{8}{4} = 70$. Avoiding: $70 - 16 = 54$.


(b) through: 16; avoiding: **Answer: 54**.

</details>


### G Synthesis

#### **Q33**[Burnside · dihedral]



<details>
<summary>Answer + Reasoning</summary>

Solution


Burnside: orbits $= \frac{1}{|G|}\sum_g |\mathrm{Fix}(g)|$, $|G| = 12$. A coloring is fixed by $g$ iff it is constant on each cycle of $g$: $|\mathrm{Fix}(g)| = 2^{\#\text{cycles}}$.


| symmetry | count | cycle structure on 6 vertices | $\|\mathrm{Fix}(g)\|$ | contribution |
| --- | --- | --- | --- | --- |
| identity | 1 | $1^6$ | 64 | 64 |
| rotations $60^\circ, 300^\circ$ | 2 | $6$ | 2 | 4 |
| rotations $120^\circ, 240^\circ$ | 2 | $3^2$ | 4 | 8 |
| rotation $180^\circ$ | 1 | $2^3$ | 8 | 8 |
| refl. through opposite vertices | 3 | $1^2 2^2$ | 16 | 48 |
| refl. through opposite edges | 3 | $2^3$ | 8 | 24 |


Sum: $64 + 4 + 8 + 8 + 48 + 24 = 156$. Orbits: $156 / 12$.


**Answer: 13** (cross-checked with the bracelet formula $\frac{1}{2n}\left(\sum_{d\mid n}\varphi(d)2^{n/d} + \frac{n}{2}(2^{n/2+1} + 2^{n/2})\right)
        = \frac{84 + 72}{12} = 13$, and by direct orbit enumeration.)

</details>

#### **Q34**[partitions]



<details>
<summary>Answer + Reasoning</summary>

Solution


**(a)** Euler's pentagonal recurrence (Ch 6, §6.4): $p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + \cdots$. With $p(0), \dots, p(9) = 1, 1, 2, 3, 5, 7, 11, 15, 22, 30$: 
$$ p(10) = p(9) + p(8) - p(5) - p(3) = 30 + 22 - 7 - 3 = 42 $$
 (terms $p(10-12), p(10-15)$ vanish). Direct enumeration of the 42 partitions confirms. $p(10) =$ **Answer: 42**


**(b) Euler: distinct = odd.** GF for distinct parts: $\prod_{k \ge 1}(1 + x^k)$ (each size 0 or 1 times). GF for odd parts: $\prod_{m\ \mathrm{odd}}(1 - x^m)^{-1}$ (any number of parts of each odd size). But 
$$ \prod_{k\ge 1}(1 + x^k)
        = \prod_{k\ge 1}\frac{1 - x^{2k}}{1 - x^k}
        = \frac{1}{\prod_{k\ge 1}(1 - x^k)} \cdot \prod_{k\ge 1}(1 - x^{2k})
        = \frac{1}{\prod_{m\ \mathrm{odd}}(1 - x^m)}, $$
 since $\prod_k (1 - x^k) = \prod_{m\ \mathrm{odd}}(1 - x^m)\cdot\prod_k (1 - x^{2k})$. The generating functions are identical: the counts agree for every $n$. $\square$


For $n = 10$: distinct: $10; 9{+}1; 8{+}2; 7{+}3; 7{+}2{+}1; 6{+}4; 6{+}3{+}1;
        5{+}4{+}1; 5{+}3{+}2; 4{+}3{+}2{+}1$ → **10**. Odd: $9{+}1; 7{+}3; 7{+}1^3; 5{+}5; 5{+}3{+}1^2; 5{+}1^5; 3^3{+}1; 3^2{+}1^4; 3{+}1^7; 1^{10}$ → **10** ✓. Both: **Answer: 10**

</details>

#### **Q35**[GF · Fibonacci]



<details>
<summary>Answer + Reasoning</summary>

Solution


**Recurrence.** Split by whether $n \in S$: subsets not containing $n$: $b_{n-1}$; subsets containing $n$: then $n-1 \notin S$, and the rest is a no-consecutive subset of $[n-2]$: $b_{n-2}$. Disjoint and exhaustive: $b_n = b_{n-1} + b_{n-2}$, with $b_0 = 1$ (empty set), $b_1 = 2$ ($\emptyset,
        \{1\}$). So $b_n = F_{n+2}$: $b_0 = F_2 = 1$, $b_1 = F_3 = 2$, and both sides obey the same recurrence. ✓


**GF.** $B(x) = \sum_{n\ge 0} b_n x^n$. For $n \ge 2$ the recurrence gives $b_n - b_{n-1} - b_{n-2} = 0$, so multiplying by $1 - x - x^2$ kills every coefficient from $x^2$ up; only the low terms survive: 
$$ (1 - x - x^2)B(x) = b_0 + (b_1 - b_0)x = 1 + x. $$
 Hence $B(x) = \frac{1 + x}{1 - x - x^2}$. And by Q12's Fibonacci GF ($\sum F_{n+1}x^n = \frac{1}{1-x-x^2}$): 
$$ \sum_{n \ge 0} F_{n+2} x^n = (1+x)\sum_{n\ge 0} F_{n+1} x^n = \frac{1+x}{1-x-x^2}
        = B(x) $$
 — so $b_n = F_{n+2}$ from the generating function as well. ✓


$b_n = F_{n+2}$; values $1, 2, 3, 5, 8, 13, 21, 34$ for $n = 0, \dots, 7$ (e.g. $n = 4$: $\emptyset, \{1\}, \{2\}, \{3\}, \{4\},
        \{1,3\}, \{1,4\}, \{2,4\}$ → 8 ✓).

</details>

#### **Q36**[Stirling]



<details>
<summary>Answer + Reasoning</summary>

Solution


**(a) Recurrence:** $S(6,3) = 3S(5,3) + S(5,2) = 3 \times 25 + 15 = 90$. **Closed form:** $\frac{1}{3!}\left(\binom{3}{0}3^6 - \binom{3}{1}2^6 + \binom{3}{2}1^6\right)
        = \frac{729 - 192 + 3}{6} = 90$. Agreement ✓. **Answer: 90**


**(b)** Pairs: label the pairs 1,2,3: choose the partner structure — first count labeled: $6!$ arrangements into 3 labeled slots of size 2, divided by $2!^3$ for within-pair order: $\frac{6!}{8} = 90$; divide by $3!$ for pair order: $\frac{90}{6} = 15$.


**Answer: 15**


**Why not $S(6,3)$:** $S(6,3)$ counts partitions of 6 people into 3 unlabeled nonempty blocks of *any* sizes — e.g. $\{\{1,2,3\}, \{4,5\}, \{6\}\}$ (a 3-2-1 split) is counted by $S(6,3)$ but is not a pairing. Pairings are exactly the 2-2-2 splits. The decomposition checks out: 2-2-2: $\frac{6!}{2!^3 3!} = 15$; 3-2-1: $\binom{6}{3}\binom{3}{2} = 20 \times 3 = 60$ (blocks of distinct sizes, so no overcount); 4-1-1: $\binom{6}{4} = 15$. And $15 + 60 + 15 = 90 = S(6,3)$ ✓ — the pairing count is precisely the first of the three summands.

</details>

#### **Q37**[linearity · parity]



<details>
<summary>Answer + Reasoning</summary>

Solution


The entries $x_{ij}$ with $i &lt; n, j &lt; n$ (the top-left $(n-1) \times
        (n-1)$ block) are **free**: $2^{(n-1)^2}$ choices. Everything else is then forced: for $i &lt; n$, $x_{i,n}$ must make row $i$ even: $x_{i,n} \equiv \sum_{j &lt; n} x_{ij} \pmod 2$ — unique. For $j &lt; n$, $x_{n,j}$ is forced by column $j$. The corner $x_{nn}$ is forced by the last row and also by the last column — we must check these agree:


Last row: $x_{nn} \equiv \sum_{j&lt;n} x_{nj} \equiv \sum_{j&lt;n}\sum_{i&lt;n} x_{ij}
        \pmod 2$ (using the column formulas). Last column: $x_{nn} \equiv \sum_{i&lt;n} x_{in}
        \equiv \sum_{i&lt;n}\sum_{j&lt;n} x_{ij} \pmod 2$ (using the row formulas). Same double sum: the two prescriptions coincide, so the corner is consistently determined. Every free block gives exactly one valid matrix, and every valid matrix arises this way.


**Answer: $2^{(n-1)^2}$** (checked: $n = 2$: 2 — the zero matrix and the all-ones matrix; $n = 3$: 16, enumeration-confirmed.)

</details>

#### **Q38**[involution · parity]



<details>
<summary>Answer + Reasoning</summary>

Proof


Define $\varphi : S_n \to S_n$ by $\varphi(\sigma) = (1\;2)\circ\sigma$. **Fixed-point-free:** $\varphi(\sigma) = \sigma$ would give $(1\;2) = \mathrm{id}$ — impossible, so $\varphi$ is a fixed-point-free involution (its own inverse), pairing $S_n$ into $n!/2$ pairs.


**Parity toggles.** Write $\varphi(\sigma) = \sigma \circ \tau$ where $\tau = \sigma^{-1}(1\;2)\sigma$ — a transposition (conjugates of transpositions are transpositions). Right-multiplying a permutation by a transposition $(a\;b)$ changes its cycle count by exactly 1: if $a, b$ lie in the *same* cycle of $\sigma$, that cycle splits into two ($+1$); if in *different* cycles, they merge ($-1$). Hence $c(\varphi(\sigma)) \equiv c(\sigma) + 1 \pmod 2$: every pair $\{\sigma,\ \varphi(\sigma)\}$ contains one permutation with an even number of cycles and one with an odd.


Therefore $\#\{\text{even-cycle permutations}\} = \frac{n!}{2}$. $\square$


**One-line alternative (signs):** $\mathrm{sign}(\sigma) = (-1)^{n - c(\sigma)}$, so "even number of cycles" $\Leftrightarrow$ $\mathrm{sign}(\sigma) = (-1)^n$. The map $\varphi(\sigma) = (1\;2)\sigma$ flips the sign ($\mathrm{sign}((1\;2)\sigma) = -\mathrm{sign}(\sigma)$) and is fixed-point-free, so exactly half of $S_n$ has sign $(-1)^n$: again $\frac{n!}{2}$. Check $n = 4$: 12 of 24 have an even number of cycles (cycle types $1^4, 2^2, 3\cdot1$: $1 + 3 + 8 = 12 = 24/2$ ✓).

</details>


### + Stretch

#### **Q39**[Burnside · 3D]



<details>
<summary>Answer + Reasoning</summary>

Solution


The rotation group of the cube has 24 elements. With the cube as $(\pm1, \pm1, \pm1)$, the rotations are the $3 \times 3$ signed permutation matrices with determinant $+1$. Their cycle structures on the 8 vertices:


| rotation | count | cycle structure on vertices | $\|\mathrm{Fix}\|$ | contribution |
| --- | --- | --- | --- | --- |
| identity | 1 | $1^8$ | 256 | 256 |
| $90^\circ/270^\circ$ about face axes | 6 | $4^2$ | 4 | 24 |
| $180^\circ$ about face axes | 3 | $2^4$ | 16 | 48 |
| $120^\circ/240^\circ$ about body diagonals | 8 | $1^2 3^2$ | 16 | 128 |
| $180^\circ$ about mid-edge axes | 6 | $2^4$ | 16 | 96 |


Face axis: line through centers of opposite faces — 3 axes × $\{90^\circ, 180^\circ, 270^\circ\}$. Body diagonal: through opposite vertices — 4 axes × $\{120^\circ, 240^\circ\}$ (the 2 diagonal vertices are fixed; the other 6 form two 3-cycles). Mid-edge axis: through midpoints of opposite edges — 6 axes × $180^\circ$ (all 8 vertices paired).


Sum: $256 + 24 + 48 + 128 + 96 = 552$. Orbits: $552 / 24$.


**Answer: 23** (verified by brute-force orbit enumeration over all 256 colorings and all 24 rotations — a genuinely 3D check of the table.)

</details>

#### **Q40**[Erdős–Szekeres]



<details>
<summary>Answer + Reasoning</summary>

Proof


**Labels.** Given $a_1, \dots, a_m$ distinct, $m = (r-1)(s-1) + 1$. For each $i$, let $I_i$ = length of the longest *increasing* subsequence **starting at $a_i$**, and $D_i$ = same for *decreasing*. **Key claim: no two terms carry the same pair $(I, D)$.** Suppose $i &lt; j$ and $(I_i, D_i) = (I_j, D_j)$. If $a_i &lt; a_j$: prefix $a_i$ to the increasing subsequence starting at $a_j$: $I_i \ge I_j + 1$, contradiction. If $a_i &gt; a_j$: $D_i \ge D_j + 1$, contradiction. (Distinctness rules out equality.)


**Pigeonhole.** The $m$ pairs $(I_i, D_i)$ are distinct. If every $I_i \le r - 1$ and every $D_i \le s - 1$, the pairs live in a set of size at most $(r-1)(s-1) = m - 1$ — impossible. Hence some $I_i \ge r$ (an increasing subsequence of length $r$) or some $D_j \ge s$ (a decreasing one of length $s$). $\square$


**Corollary.** $r = s = 11$: $10 \times 10 + 1 = 101$ distinct reals contain a monotone subsequence of length 11.


**Sharpness — 100 reals with no monotone subsequence of length 11.** Ten decreasing blocks of 10, each block larger than the previous: 
$$ \underbrace{10, 9, \dots, 1}_{B_1}\ \ \underbrace{20, 19, \dots, 11}_{B_2}\ \ \cdots\ \
        \underbrace{100, 99, \dots, 91}_{B_{10}}. $$
 *Increasing* subsequence: each block is decreasing, so at most one term per block: length $\le 10$. *Decreasing* subsequence: a term of block $B_{i+1}$ is larger than every term of $B_i$, so a decreasing subsequence can never pass from $B_{i+1}$ back to $B_i$: it lies inside a single block: length $\le 10$. Hence no monotone subsequence of length 11 exists — matching the theorem's bound $(11-1)(11-1) = 100$ exactly. $\square$


The example is tight exactly at the theorem's threshold: it has $(11-1)(11-1) = 100$ terms — one short of the $(r-1)(s-1)+1 = 101$ that force a monotone subsequence of length 11 — and no such subsequence exists in it.

</details>


### H Intersecting & Restricted Families

#### **Q41**[Erdős–Ko–Rado]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) A $4$-subset of $[8]$ containing $1$ is determined by the other $3$ elements, chosen from the remaining $7$: $\binom{7}{3} = 35$. Any two of them share the element $1$, so the star $\{A : |A| = 4,\ 1 \in A\}$ is intersecting.

(b) **Erdős–Ko–Rado.** If $\mathcal F$ is an intersecting family of $k$-subsets of $[n]$ with $n \ge 2k$, then $|\mathcal F| \le \binom{n-1}{k-1}$. For $n = 8$, $k = 4$: $\binom{7}{3} = 35$.

(c) The $70$ four-subsets of $[8]$ form a graph in which two vertices are adjacent when the sets meet; an intersecting family is exactly a clique. The maximum clique was computed by branch and bound and equals $35$, so the bound is attained and cannot be improved.

(d) The hypothesis $n \ge 2k$ is essential. When $n < 2k$, *every* two $k$-sets meet (two $k$-subsets can be disjoint only inside a set of size at least $2k$), so the whole $\binom{n}{k}$ family is intersecting and the theorem is vacuous. Check at $n = 7$, $k = 4$: $4 + 4 = 8 > 7$, so all $35 = \binom{7}{4}$ four-subsets of $[7]$ are pairwise intersecting — while the EKR formula would have predicted the smaller $\binom{6}{3} = 20$.


**Answer: 35**

</details>

#### **Q42**[Hilton–Milner]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) **Hilton–Milner.** The largest intersecting $k$-uniform family on $[n]$ whose total intersection is empty (no element lies in every member) has size
$$\binom{n-1}{k-1} - \binom{n-k-1}{k-1} + 1$$
as long as $n > 2k$. For $n = 7$, $k = 3$: $\binom{6}{2} - \binom{3}{2} + 1 = 15 - 3 + 1 = 13$.

(b) Fix $S = \{2,3,4\}$ and an element $1 \notin S$, and take
$$\mathcal H = \{A : |A| = 3,\ 1 \in A,\ A \cap S \ne \varnothing\} \cup \{S\}.$$
The first part has $\binom{6}{2} - \binom{3}{2} = 12$ members (all triples through $1$, minus the three using only $\{5,6,7\}$), and adding $S$ gives $13$. It is intersecting: two members both containing $1$ meet; a member containing $1$ meets $S$ by construction; $S$ meets itself. Its total intersection is empty: $1 \notin S$, and for each $x \in S$ the triple $\{1\} \cup (S \setminus \{x\}) \cup \{5\}$ is a member missing $x$. A direct maximum-clique computation over the $\binom{7}{3} = 35$ triples, restricted to families with empty total intersection, returns $13$.

(c) $n = 6$, $k = 3$: $\binom{5}{2} - \binom{2}{2} + 1 = 10 - 1 + 1 = 10$. $n = 8$, $k = 3$: $\binom{7}{2} - \binom{4}{2} + 1 = 21 - 6 + 1 = 16$. Both confirmed by the same clique computation (maxima $10$ and $16$).


**Answer: 13** (and $10$, $16$ for the two smaller/larger cases)

</details>

#### **Q43**[Katona circle]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) Arrange the $n$ points on a circle and call $k$ consecutive points an *interval*. There are exactly $n$ cyclic intervals of length $k$. **Claim: an intersecting family contains at most $k$ of them.**

*Proof.* Suppose $k+1$ of them were pairwise intersecting, with starts $s_1 < s_2 < \cdots < s_{k+1}$ taken as integers in $[0,n)$. Because $n \ge 2k$, two length-$k$ intervals are disjoint exactly when the clockwise distance between their starts lies in $[k,\,n-k]$; so pairwise intersection forces every difference $s_b - s_a$ ($a<b$) into $\{1,\dots,k-1\}\cup\{n-k+1,\dots,n-1\}$.

Fix $I_1$, the interval starting at $s_1$. Every other interval meets $I_1$, so its start lies in the window $[s_1-k+1,\,s_1+k-1]$ (width $2k-1 \le n-1$, so no wraparound ambiguity). Such an interval contains $s_1$ if its start is $\le s_1$, and contains $s_1+k-1$ if its start is $\ge s_1+1$. Let $U$ be the set of offsets $u\in\{1,\dots,k-1\}$ of intervals starting at $s_1-u$ and $V$ the set of offsets $v\in\{1,\dots,k-1\}$ of intervals starting at $s_1+v$; together with $I_1$ itself (offset $0$) these account for all $k+1$ intervals, so $|U|+|V| = k$.

An interval with offset $u$ is $[s_1-u,\,s_1-u+k-1]$ and one with offset $v$ is $[s_1+v,\,s_1+v+k-1]$; they meet iff $s_1+v \le s_1-u+k-1$, i.e. iff $u+v\le k-1$. This must hold for every $u\in U$, $v\in V$, so $\max U+\max V\le k-1$. As $U$ and $V$ are sets of distinct positive integers, $|U|\le\max U$ and $|V|\le\max V$, giving $|U|+|V|\le k-1$ — contradicting $|U|+|V|=k$.

The remaining possibility is that $U$ or $V$ is empty, so that all $k+1$ intervals pass through the single point $s_1$ (or $s_1+k-1$). But exactly $k$ cyclic intervals of length $k$ pass through any given point, so that is impossible too. Hence at most $k$. $\square$

(b) The twelve intervals $\{i, i+1, i+2, i+3\}$ (mod $12$) on a circle of $12$ points: the largest pairwise-intersecting subfamily has size $4$, attained for instance by $\{0,1,2,3\}$, $\{1,2,3,4\}$, $\{2,3,4,5\}$, $\{3,4,5,6\}$, which all contain the point $3$. (No five are pairwise intersecting, by (a) and by direct computation.)

(c) $(n,k) = (8,3)$: the eight intervals of length $3$ admit a pairwise-intersecting subfamily of size $3$, e.g. $\{0,1,2\},\{1,2,3\},\{2,3,4\}$. $(n,k) = (10,4)$: size $4$, e.g. $\{0,1,2,3\},\{1,2,3,4\},\{2,3,4,5\},\{3,4,5,6\}$. Both match the general bound $k$ exactly.


**Answer: 4** (at most $k$ in general; $3$ and $4$ for the two checks)

</details>

#### **Q44**[Frankl–Wilson]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) **Frankl–Wilson (uniform version).** Let $\mathcal F$ be a $k$-uniform family on $[n]$ and $L$ a set of $s$ non-negative integers with $k \notin L$, such that $|A \cap B| \in L$ for all *distinct* $A, B \in \mathcal F$. Then $|\mathcal F| \le \binom{n}{s}$. Here $n = 8$, $k = 3$, $L = \{1,2\}$, so $s = 2$ and $k = 3 \notin L$: the bound is $\binom{8}{2} = 28$.

(b) The compatibility graph on the $\binom{8}{3} = 56$ triples joins two triples when their intersection has size $1$ or $2$; a valid family is a clique. Its maximum clique is $21$, comfortably inside the bound of $28$.

(c) The theorem depends only on $s = |L|$, never on which sizes are allowed. Replacing $L$ by $\{0,2\}$ leaves $s = 2$, so the bound is again $\binom{8}{2} = 28$ — yet the actual maximum drops to $8$. The permitted sizes $1,2$ are far more permissive than $0,2$, but the *number* of permitted sizes is what the linear-algebra proof counts: the vectors $\big(\binom{|A \cap T|}{j}\big)$ live in a space of dimension $\binom{n}{s}$, and independence caps the family at $\binom{n}{s}$ whatever $L$ is.


**Answer: 28** (the bound); the true maximum is $21$

</details>

#### **Q45**[odd town]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) To each $A \in \mathcal F$ attach its incidence vector $v_A \in \mathbb F_2^{\,n}$. For $A \ne B$ the inner product is $\langle v_A, v_B\rangle = |A \cap B| \bmod 2 = 0$, and for $A = A$ it is $\langle v_A, v_A\rangle = |A| \bmod 2 = 1$ because $|A|$ is odd. So the Gram matrix $G = (\langle v_A, v_B\rangle)$ is the identity matrix of size $|\mathcal F|$. If $\sum_A \lambda_A v_A = 0$ with $\lambda \in \mathbb F_2^{|\mathcal F|}$, taking inner products with $v_B$ gives $\lambda_B = 0$ for every $B$. The $v_A$ are linearly independent in an $n$-dimensional space, so $|\mathcal F| \le n$.

(b) The $n$ singletons $\{1\}, \dots, \{n\}$: each has odd size, and two distinct singletons meet in $0$ elements, which is even. So $|\mathcal F| = n$ is attained.

(c) Exhaustive search over all $2^n$ subsets (max clique in the graph joining two odd subsets when their intersection is even) gives maxima $4, 5, 6$ for $n = 4, 5, 6$ — exactly $n$ in each case.


**Answer: n** (attained by the singletons; verified $4, 5, 6$)

</details>

#### **Q46**[even town]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) If $A, B$ are both even and $|A \cap B|$ is even, then $|A \mathbin{\Delta} B| = |A| + |B| - 2|A \cap B|$ is even, and $|(A \mathbin{\Delta} B) \cap C| = |(A \cap C) \mathbin{\Delta} (B \cap C)|$ is even too. So $\mathcal F$ is closed under symmetric difference and is a subspace of $\mathbb F_2^{\,n}$ — necessarily a subspace of the even-weight hyperplane. Moreover every $v_A$ is orthogonal to every $v_B$ including itself, so $\mathcal F \subseteq \mathcal F^\perp$ and $\dim \mathcal F \le n - \dim \mathcal F$, i.e. $\dim \mathcal F \le \lfloor n/2 \rfloor$. Hence $|\mathcal F| = 2^{\dim \mathcal F} \le 2^{\lfloor n/2 \rfloor}$.

(b) Pair the coordinates as $(1,2), (3,4), \dots$ and take every union of complete pairs. For $n = 6$: $\varnothing, \{1,2\}, \{3,4\}, \{5,6\}, \{1,2,3,4\}, \{1,2,5,6\}, \{3,4,5,6\}, \{1,2,3,4,5,6\}$ — $8 = 2^3$ sets. For $n = 5$ the same construction on the pairs $(1,2),(3,4)$ gives $4 = 2^2$ sets.

(c) Exhaustive search over the even subsets gives maxima $2, 4, 4, 8$ for $n = 3, 4, 5, 6$, matching $2^{\lfloor n/2 \rfloor}$ throughout.


**Answer: $2^{\lfloor n/2 \rfloor}$** (attained by unions of coordinate pairs; verified $2, 4, 4, 8$)

</details>

### I Bollobás & Set-Pairs

#### **Q47**[Bollobás]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) **Bollobás's set-pairs inequality.** Let $(A_i, B_i)$, $i = 1, \dots, m$, satisfy $A_i \cap B_i = \varnothing$ and $A_i \cap B_j \ne \varnothing$ for $i \ne j$. Then $\sum_{i=1}^m \binom{|A_i| + |B_i|}{|A_i|}^{-1} \le 1$.

*Proof.* Take a uniformly random permutation of the ground set and read it left to right. For a pair with $a_i = |A_i|$, $b_i = |B_i|$, consider the event $E_i$ = "every element of $A_i$ precedes every element of $B_i$". Among the $a_i + b_i$ elements of $A_i \cup B_i$ all relative orders are equally likely, and exactly the $\binom{a_i+b_i}{a_i}$ orders in which the $a_i$ positions of $A_i$ come first satisfy $E_i$; hence $\Pr[E_i] = \binom{a_i+b_i}{a_i}^{-1}$.

The events are pairwise disjoint. Suppose $E_i$ and $E_j$ both occur with $i \ne j$. The hypothesis supplies $x \in A_i \cap B_j$ and $y \in A_j \cap B_i$. From $E_i$, every element of $A_i$ precedes every element of $B_i$, so $x$ precedes $y$. From $E_j$, every element of $A_j$ precedes every element of $B_j$, so $y$ precedes $x$. A strict linear order cannot satisfy both $x \prec y$ and $y \prec x$. So $\sum_i \Pr[E_i] = \Pr[\bigcup E_i] \le 1$. $\square$

(b) Random families were generated subject to the crossing condition (each pair's own intersection empty, every cross-intersection non-empty), the condition was re-checked, and the sum evaluated. Over $1393$ valid families the largest value was $1.000000000000$ — never above the bound.

(c) Take $A_1 = \{1\}$, $B_1 = \{2\}$, $A_2 = \{2\}$, $B_2 = \{1\}$. Then $A_1 \cap B_1 = A_2 \cap B_2 = \varnothing$ and $A_1 \cap B_2 = A_2 \cap B_1 = \{1\} \ne \varnothing$ (equivalently $\{2\}$), so the hypothesis holds and the sum is $\binom{2}{1}^{-1} + \binom{2}{1}^{-1} = \tfrac12 + \tfrac12 = 1$ exactly.


**Answer: $\le 1$** — attained by $A_1=\{1\},B_1=\{2\},A_2=\{2\},B_2=\{1\}$

</details>

#### **Q48**[Bollobás corollary]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) If $|A_i| \ge a$ and $|B_i| \ge b$ for all $i$, then every summand is at least $\binom{a+b}{a}^{-1}$, because $\binom{x+y}{x}$ is increasing in each argument on the relevant range. Bollobás gives $m \binom{a+b}{a}^{-1} \le \sum_i \binom{a_i+b_i}{a_i}^{-1} \le 1$, hence $m \le \binom{a+b}{a}$. The bound depends only on the two *minimum* sizes.

(b) For $a = b = 1$ the corollary gives $m \le \binom{2}{1} = 2$. Attained by $A_1 = \{1\}$, $B_1 = \{2\}$, $A_2 = \{2\}$, $B_2 = \{1\}$: both own-intersections are empty and both cross-intersections are non-empty, and the sum is exactly $1$.

(c) With $|A_i| = |B_i| = 1$ write $A_i = \{x_i\}$, $B_i = \{y_i\}$ with $x_i \ne y_i$. The crossing condition forces $x_i = y_j$ for every $i \ne j$. If $m \ge 3$, fixing $i$ gives $y_j = x_i$ for all $j \ne i$, so all the $x$'s and $y$'s coincide with one value, contradicting $x_i \ne y_i$. Hence $m \le 2$, confirmed by exhaustive search over all candidate pairs for ground sets of size $3, 4, 5$: the maximum is $2$ in every case.


**Answer: $m \le \binom{a+b}{a}$**; for $a = b = 1$ this is $m \le 2$, and it is tight

</details>

#### **Q49**[Bollobás sharp]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) All pairs $(A, B)$ with $A, B$ disjoint $2$-subsets of $[5]$ were enumerated ($30$ of them), and the largest subfamily in which every $A$ meets every other pair's $B$ was found by maximum clique. The answer is $6$, meeting the corollary's bound $\binom{2+2}{2} = 6$ exactly.

(b) An extremal family of six, using only the ground set $\{1,2,3,4\}$:

| $i$ | $A_i$ | $B_i$ |
| --- | --- | --- |
| 1 | $\{1,2\}$ | $\{3,4\}$ |
| 2 | $\{1,3\}$ | $\{2,4\}$ |
| 3 | $\{1,4\}$ | $\{2,3\}$ |
| 4 | $\{2,3\}$ | $\{1,4\}$ |
| 5 | $\{2,4\}$ | $\{1,3\}$ |
| 6 | $\{3,4\}$ | $\{1,2\}$ |

These are the six ordered ways to split $\{1,2,3,4\}$ into two pairs. Each $B_i$ is the complement of $A_i$, so $A_i \cap B_i = \varnothing$; and for $i \ne j$ the sets $A_i$ and $B_j$ are two distinct $2$-subsets of a $4$-set that are not complementary, so they meet. Both conditions hold. The sum is $6 \cdot \binom{4}{2}^{-1} = 6/6 = 1$ — Bollobás is *tight* here as well.

(c) The cyclic-interval construction with $n = 6$, $a = b = 3$ gives $m = 6$ pairs with sum $6/\binom{6}{3} = 6/20 = 0.3$, far from $1$. The corollary's bound $\binom{6}{3} = 20$ is a cap on the *count*, not on the sum, and this construction is nowhere near saturating it: tightness needs the $A_i$ and $B_i$ to be as small as the hypothesis allows, which the $a = b = 2$ family above achieves but the $a = b = 3$ one does not.


**Answer: 6** $= \binom{4}{2}$, with the sum exactly $1$

</details>

#### **Q50**[synthesis]



<details>
<summary>Answer + Reasoning</summary>

Solution


(a) Frankl–Wilson with $n = 9$, $k = 3$, $L = \{0,2\}$: $s = |L| = 2$ and $k = 3 \notin L$, so $|\mathcal F| \le \binom{9}{2} = 36$. The true maximum, found by maximum clique over the $\binom{9}{3} = 84$ triples, is $8$ — the theorem's bound is a long way from sharp here, which is typical: Frankl–Wilson is a universal cap, not a formula for the extremal family.

(b) With $L = \{1\}$ every two members meet in exactly one point. Now $s = 1$, so $|\mathcal G| \le \binom{9}{1} = 9$, and the actual maximum is $7$ (again by maximum clique). Note how much stronger the bound becomes as $s$ shrinks — the same machinery, one fewer permitted intersection size, a bound $4$ times smaller.

(c) On the ground set $\{1,2,3,4\}$ arranged on a circle, take $a = 1$, $b = 3$: $A_i = \{i\}$ and $B_i$ = the three consecutive points immediately before $i$. The four pairs satisfy $A_i \cap B_i = \varnothing$ and $A_i \cap B_j \ne \varnothing$ for $i \ne j$, and the sum is
$$4 \cdot \binom{1+3}{1}^{-1} = \frac{4}{4} = 1.$$
In general the cyclic construction with $n = a + b$ points gives $n$ valid pairs and sum $n \big/ \binom{n}{a}$, which equals $1$ precisely when $n = \binom{n}{a}$ — e.g. $n = 4, a = 1, b = 3$ and $n = 5, a = 1, b = 4$. What makes it tight is that the pairs are *consecutive* on the circle: each $A_i$ sits in the unique gap of $B_i$, and every other $B_j$ wraps around to meet it.


**Answer: (a) $36$; (b) $9$; (c) sum $= 1$**

</details>


### ◈ Marking guide (suggested)

| band | questions | weight |
| --- | --- | --- |
| Mechanics (execute a known method cleanly) | Q3, Q6, Q7, Q9, Q10, Q11, Q13, Q19, Q20, Q21, Q26, Q28, Q31, Q32 | 1 mark each |
| Hard (method + a twist: bounded IE, rooks, parity, gaps in circles) | Q1, Q2, Q4, Q5, Q8, Q15, Q16, Q18, Q22, Q23, Q27, Q33, Q34, Q35, Q36 | 2 marks each |
| Olympiad (full bijections / proofs: reflection, Burnside 3D, cycle parity, Ramsey, W(2,3), ES) | Q12, Q14, Q17, Q24, Q25, Q29, Q30, Q37, Q38, Q39, Q40 | 3–4 marks each |
| Frontier (extremal set theory: EKR, Hilton–Milner, Katona, Frankl–Wilson, odd/even town, Bollobás) | Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50 | 3–4 marks each |

Total: $14 + 15\cdot 2 + 11\cdot 3.5 + 10\cdot 3.5 \approx 113$ "marks" over 50 questions — a realistic full-length attempt covers $\sim 60\%$ with strong time management; the stretch questions are worth starting only after G is done, and the frontier sections H–I after that.
