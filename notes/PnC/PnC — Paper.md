---
title: "PnC — Olympiad Paper"
aliases:
  - PnC Paper
module: "PnC"
module_title: "PnC"
type: paper
tags:
  - pnc
  - paper
  - olympiad
  - assessment
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[06-olympiad-theory|Chapter 6]] · 📖 [[PnC|PnC]] · ✅ [[PnC — Solutions|Solutions]] ➡

# Olympiad Paper · 40 questions

*Assessment · The Whole Course*

# The PnC Olympiad Paper

40 questions covering every concept of the six chapters, from arrangement mechanics to Burnside, partitions and synthesis proofs. Questions 1–38 are the core paper (sections A–G); 39–40 are stretch. Suggested time: 4–5 hours. No calculator needed; "exact number" questions expect a fully reduced integer.

`A · Arrangements (8)` `B · Stars & Bars (4)` `C · Binomial / Double Counting (5)` `D · Inclusion–Exclusion (5)` `E · Pigeonhole (6)` `F · Lattice Paths (4)` `G · Synthesis (6)` `+2 stretch`

### Supplementary notes

**Instructions.** Each question is tagged with the concepts it uses and a difficulty: [Hard] [Olympiad]. Answer questions as numbered. For "prove" questions, a clean argument with every step justified earns full marks — a claim with no proof earns none. The answer key is at the bottom (collapsed); *full solutions with reasoning* are in [the solutions file](#solutions).


### A Arrangements

#### **Q1**[gaps & repeats][Hard]How many arrangements of the letters of the word [formula] have no two vowels …

How many arrangements of the letters of the word $\text{PERMUTATION}$ have no two vowels adjacent?

#### **Q2**[onto · IE][Hard]Let [formula] be onto . How many such [formula] satisfy [formula] ?

Let $f : [5] \to [3]$ be *onto*. How many such $f$ satisfy $f(1) \ne f(2)$?

#### **Q3**[gaps][Moderate]Four men and four women are to be arranged in a row. How many arrangements hav…

Four men and four women are to be arranged in a row. How many arrangements have no two women adjacent?

#### **Q4**[circular · gaps][Hard]Twelve people, among them [formula] , sit around a round table. How many seati…

Twelve people, among them $A, B, C$, sit around a round table. How many seatings have $A, B, C$ *pairwise* non-adjacent?

#### **Q5**[derangements · IE][Hard]Six distinct letters are posted into six correctly addressed envelopes. In how…

Six distinct letters are posted into six correctly addressed envelopes. In how many arrangements is *no* letter in its own envelope, and letter $A$ is *not* in envelope $B$?

#### **Q6**[choice · order][Moderate]From a group of 12 people, a committee of 5 is formed and a chairman is chosen…

From a group of 12 people, a committee of 5 is formed and a chairman is chosen from among the 5 committee members. In how many ways can this be done?

#### **Q7**[couples][Moderate]From 8 married couples, 4 people are to be chosen for a dinner, no two from th…

From 8 married couples, 4 people are to be chosen for a dinner, no two from the same couple. How many choices are possible?

#### **Q8**[alternating · slots][Hard]Five men and five women are arranged in a row, alternating by gender. If man […

Five men and five women are arranged in a row, alternating by gender. If man $A$ and woman $B$ must be adjacent, how many arrangements are possible?


### B Stars & Bars

#### **Q9**[bounded IE][Hard]Find the number of solutions in positive integers of [formula] with [formula] …

Find the number of solutions in positive integers of $x + y + z + w = 20$ with $x, y, z, w \le 8$.

#### **Q10**[bounded IE][Hard]Find the number of solutions in non-negative integers of [formula] with [formu…

Find the number of solutions in non-negative integers of $x_1 + x_2 + x_3 = 15$ with $x_1, x_2, x_3 \le 6$.

#### **Q11**[digits · stars][Moderate]How many 4-digit positive integers have digit sum [formula] ?

How many 4-digit positive integers have digit sum $9$?

#### **Q12**[GF · Fibonacci][Olympiad]Let [formula] be the number of compositions of [formula] into odd parts ( [for…

Let $a_n$ be the number of compositions of $n$ into *odd* parts ($n \ge 1$). Prove that $a_n = F_n$, where $F_1 = F_2 = 1$, $F_{n} = F_{n-1} + F_{n-2}$. (Hint: the generating function $\frac{1 - x^2}{1 - x - x^2}$ and the Fibonacci GF.)


### C Binomial Coefficients & Double Counting

#### **Q13**[bounded GF][Hard]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^{10}$ in $(1 + x + x^2 + x^3 + x^4)^5$.

#### **Q14**[Vandermonde][Olympiad]Prove that for all [formula] : [formula] (Both a generating-function proof and…

Prove that for all $n \ge 1$: 
$$ \sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^2 = (-1)^n \binom{2n}{n}. $$
 (Both a generating-function proof and a double-counting interpretation are welcome.)

#### **Q15**[Vandermonde][Hard]Prove that [formula] .

Prove that $\displaystyle\sum_{k} \binom{n}{k}\binom{n}{k+1} = \binom{2n}{n+1}$.

#### **Q16**[Vandermonde][Hard]Prove that [formula] , and interpret it as a committee problem with two pools …

Prove that $\displaystyle\sum_{k} \binom{n}{k}\binom{n+1}{k+1} = \binom{2n+1}{n}$, and interpret it as a committee problem with two pools of people.

#### **Q17**[symmetry · GF][Olympiad](a) Let [formula] be odd , [formula] . Prove that exactly [formula] of the [fo…

(a) Let $k$ be *odd*, $1 \le k \le 2n-1$. Prove that exactly $\frac{1}{2}\binom{2n}{k}$ of the $k$-subsets of $[2n] = \{1, \dots, 2n\}$ have *odd* sum of elements. (Hint: cyclically shift a subset by $1$ modulo $2n$.) (b) What is the exact count when $k$ is *even*? Express it using $\binom{2n}{k}$ and $\binom{n}{k/2}$, and verify your formula for $n = 3, k = 2$.


### D Inclusion–Exclusion & Rooks

#### **Q18**[rook · derangement][Hard]In how many ways can 5 non-attacking rooks be placed on a [formula] board so t…

In how many ways can 5 non-attacking rooks be placed on a $5 \times 5$ board so that none stands on the main diagonal? (Compute with the rook polynomial of the forbidden board, and note the relation to derangements.)

#### **Q19**[repeats · IE][Hard]How many arrangements of the letters of [formula] have no two [formula] 's adj…

How many arrangements of the letters of $\text{AABBC}$ have no two $A$'s adjacent?

#### **Q20**[bounded IE][Hard]Find the number of solutions in positive integers of [formula] with each [form…

Find the number of solutions in positive integers of $x_1 + x_2 + x_3 + x_4 + x_5 = 30$ with each $x_i \le 7$.

#### **Q21**[partial IE][Hard]How many permutations [formula] of [formula] satisfy [formula] ?

How many permutations $\sigma$ of $[5]$ satisfy $\sigma(1) \ne 2,\ \sigma(2) \ne 1,\ \sigma(3) \ne 3$?

#### **Q22**[rook][Hard]In how many ways can 3 non-attacking rooks be placed on a [formula] board, non…

In how many ways can 3 non-attacking rooks be placed on a $4 \times 4$ board, none on the main diagonal? (Remark: compare the answer with Q18 — same number, different story. Why is that *not* a coincidence waiting to be exploited?)


### E Pigeonhole & Extremal

#### **Q23**[residues][Hard]Given any [formula] integers, prove that some non-empty subset of them has sum…

Given any $2n + 1$ integers, prove that some non-empty subset of them has sum divisible by $2n + 1$. (In fact, show a *consecutive block* in the given order suffices.)

#### **Q24**[Ramsey R(3,3)][Olympiad]Prove that [formula] : (a) every red/blue coloring of the edges of [formula] c…

Prove that $R(3,3) = 6$: (a) every red/blue coloring of the edges of $K_6$ contains a monochromatic triangle (argue from one vertex: its 5 incident edges, a pigeonhole step, then look at the triangle on the three same-colored neighbors); (b) a red/blue coloring of $K_5$ with *no* monochromatic triangle exists — construct one and verify it. (Comment: the lower bound can also be obtained by the probabilistic method; explain why the first-moment estimate $\mathbb{E} = \binom{5}{3}/4$ does *not* prove (b).)

#### **Q25**[van der Waerden][Olympiad]Prove that every red/blue coloring of [formula] contains a monochromatic 3-ter…

Prove that every red/blue coloring of $\{1, 2, \dots, 9\}$ contains a monochromatic 3-term arithmetic progression $(x, y, z)$ with $x + y = 2z$, and that 9 is best possible: give a coloring of $\{1, \dots, 8\}$ with none. (This is $W(2,3) = 9$; the case analysis is in Ch 5, §5.2 — you may cite it for the upper bound and must supply the extremal coloring yourself.)

#### **Q26**[geometry PH][Hard]Given any 5 points in a unit square, prove that two of them are at distance at…

Given any 5 points in a unit square, prove that two of them are at distance at most $\frac{\sqrt 2}{2}$ of each other.

#### **Q27**[residue pairs][Hard]Let [formula] be odd. Prove that among any [formula] integers there are two wh…

Let $n$ be odd. Prove that among any $\frac{n+3}{2}$ integers there are two whose sum is divisible by $n$. Explain why the argument needs the parity of $n$.

#### **Q28**[construction][Hard]Prove that there exist 100 consecutive composite positive integers. (Generaliz…

Prove that there exist 100 consecutive composite positive integers. (Generalize: for every $m \ge 1$, how long can a block of consecutive composites be guaranteed to be? Use factorial, not primality testing.)


### F Lattice Paths & Catalan

#### **Q29**[reflection][Olympiad]Prove, using the reflection principle as a bijection (state and prove the bije…

Prove, using the reflection principle as a bijection (state and prove the bijection), that the number of monotone lattice paths from $(0,0)$ to $(n,n)$ that never go strictly above the diagonal $y = x$ is $C_n = \binom{2n}{n} - \binom{2n}{n+1} = \frac{1}{n+1}\binom{2n}{n}$.

#### **Q30**[Dvoretzky–Motzkin][Olympiad]For [formula] , prove that the number of monotone paths from [formula] to [for…

For $a \ge b \ge 0$, prove that the number of monotone paths from $(0,0)$ to $(a,b)$ that never go strictly above the diagonal is $\frac{a-b+1}{a+1}\binom{a+b}{b}$, and check that it specializes to the Catalan number at $a = b = n$.

#### **Q31**[ballot][Hard]In an election, candidate A receives 5 votes and candidate B receives 3. In ho…

In an election, candidate A receives 5 votes and candidate B receives 3. In how many orders of counting is A strictly ahead of B after every vote that is cast (from the first vote onward)?

#### **Q32**[paths · reflection][Hard](a) How many monotone paths from [formula] to [formula] stay strictly below th…

(a) How many monotone paths from $(0,0)$ to $(5,5)$ stay *strictly below* the diagonal $y = x$ at every interior point? (Equivalently: first step $R$, last step $U$, and $y &lt; x$ in between.) (b) How many monotone paths from $(0,0)$ to $(4,4)$ pass through the point $(1,3)$? How many *avoid* it?


### G Synthesis — the whole course

#### **Q33**[Burnside · dihedral][Olympiad]The vertices of a regular hexagon are colored with 2 colors. Count the colorin…

The vertices of a regular hexagon are colored with 2 colors. Count the colorings up to the full symmetry group of the hexagon (rotations and reflections), showing the $\mathrm{Fix}(g)$ count for each of the 12 symmetries.

#### **Q34**[partitions][Hard](a) Compute [formula] (the number of integer partitions of 10) — enumerate, or…

(a) Compute $p(10)$ (the number of integer partitions of 10) — enumerate, or verify with Euler's pentagonal recurrence from the known values $p(0), \dots, p(9)$. (b) Prove Euler's theorem: the number of partitions of $n$ into *distinct* parts equals the number of partitions of $n$ into *odd* parts. Then compute both for $n = 10$ and confirm they agree.

#### **Q35**[GF · Fibonacci][Hard]Let [formula] be the number of subsets of [formula] that contain no two consec…

Let $b_n$ be the number of subsets of $[n]$ that contain no two consecutive integers. Show that $b_n = F_{n+2}$ (with $F_1 = F_2 = 1$), both by a recurrence argument and by finding the generating function $B(x)$ and recognizing it.

#### **Q36**[Stirling][Hard](a) Compute [formula] (Stirling numbers of the second kind) using both the rec…

(a) Compute $S(6,3)$ (Stirling numbers of the second kind) using both the recurrence $S(n,k) = k\,S(n-1,k) + S(n-1,k-1)$ and the closed form $\frac{1}{k!}\sum_j (-1)^j \binom{k}{j}(k-j)^n$. (b) Six people are divided into 3 unlabeled pairs for a doubles tournament. How many divisions? (Explain why this is *not* $S(6,3)$.)

#### **Q37**[linearity · parity][Olympiad]How many [formula] [formula] - [formula] matrices have all row sums even and a…

How many $n \times n$ $0$-$1$ matrices have all row sums even *and* all column sums even? (Hint: how many entries are free? Prove the corner is forced consistently.)

#### **Q38**[involution · parity][Olympiad]Prove that exactly [formula] of the permutations of [formula] (for [formula] )…

Prove that exactly $\frac{n!}{2}$ of the permutations of $[n]$ (for $n \ge 2$) have an *even* number of cycles in their disjoint-cycle decomposition. (Hint: left-composition by the fixed involution $(1\;2)$ is a fixed-point-free pairing that toggles the parity of the cycle count. Why does it toggle it? Use the sign of a permutation.)


### + Stretch

#### **Q39**[Burnside · 3D][Olympiad]The 8 vertices of a cube are colored with 2 colors. Count the colorings up to …

The 8 vertices of a cube are colored with 2 colors. Count the colorings up to *rotation* of the cube (the 24-element rotation group). Classify the 24 rotations by their cycle structure on the vertices, compute each $\mathrm{Fix}(g)$, and finish with Burnside.

#### **Q40**[Erdős–Szekeres][Olympiad]Prove the Erdős–Szekeres theorem: every sequence of [formula] distinct real nu…

Prove the Erdős–Szekeres theorem: every sequence of $(r-1)(s-1) + 1$ distinct real numbers contains an increasing subsequence of length $r$ or a decreasing one of length $s$ (use the $(I_i, D_i)$ label argument). Deduce: any 101 distinct real numbers contain a monotone subsequence of length 11. Give an example of 100 distinct reals with *no* monotone subsequence of length 11, and verify it.


### ✎ Answer Key

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ans | 907,200 | 114 | 2,880 | 20,321,280 | 212 | 3,960 | 1,120 | 10,368 |  |
| Q | 9 | 10 | 11 | 13 | 18 | 19 | 20 | 21 | 22 |
| ans | 315 | 10 | 165 | 381 | 44 | 18 | 126 | 64 | 44 |
| Q | 31 | 32a | 32b | 33 | 34a | 34b | 36a | 36b | 39 |
| ans | 14 | 14 | 54 | 13 | 42 | 10 | 90 | 15 | 23 |
