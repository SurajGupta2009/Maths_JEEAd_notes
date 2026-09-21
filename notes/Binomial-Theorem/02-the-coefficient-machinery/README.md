# Chapter 2 — The Coefficient Machinery

*5 sections · 11 questions*

*Chapter 2 of 6*

# The Coefficient Machinery

Chapter 1 said every term of the expansion is a record of bracket choices. This chapter turns that into a machine: one formula for the general term $T_{k+1}$ solves — in a single line — "coefficient of $x^m$", "term independent of $x$", "middle term", "which coefficients are equal". Then we upgrade the machine to multinomials, where the bracket census counts *three or four* outcomes per bracket.

### 2.0 What you will be able to do

- Write the general term of $(\alpha x^p + \beta x^{-q})^n$ and read off any power of $x$ by solving one linear equation in $k$.
- Handle "term independent of $x$" and "ratio of consecutive coefficients" questions, the two JEE Advanced staples.
- Use multinomial coefficients $\frac{n!}{a!\,b!\,c!\cdots}$ to attack $(1+x+x^2)^n$-type problems where the pure binomial machine stalls.
- Locate the largest coefficient of $(1+x)^n$ and of full expansions $(a+bx)^n$.


### 2.1 The general term — one line that ends most questions

From the census: the term formed by taking $b$ from exactly $k$ brackets is the *collective* of all such pick-lists:

$$ T_{k+1} \;=\; \binom{n}{k}\, a^{\,n-k}\, b^{k}
      \qquad (k = 0, 1, \dots, n;\ \text{the } (k{+}1)\text{-th term}). $$

Apply it to a mixed-power bracket like $\left(\alpha x^p + \beta x^{-q}\right)^n$: the general term is $\binom{n}{k} \alpha^{n-k}\beta^k\, x^{\,p(n-k)-qk}$. "Coefficient of $x^m$" and "constant term" both become the same mechanical step —

> **💡 Key Idea — solve for k once, then everything follows**
>
> Set the exponent equal to the target: $pn - (p+q)k = m$. If $k$ comes out an integer in $[0,n]$, substitute it into the coefficient part. If it does not, **the answer is 0** — "no such term" is a legitimate, frequent exam answer, and stating it confidently is a skill.

> **⚠ Common Trap — T_k vs T_{k+1}, and buried negatives**
>
> Two classic mark-losers: (i) the "5th term" is $k=4$, not $k=5$; (ii) writing the term of $\left(2x - \tfrac{3}{x^2}\right)^6$ without $(-3)^k$ — keep the sign inside the power you raise. Rule: rewrite every bracket as $A + B$ with $B$ *including* its minus sign, then apply $T_{k+1}$ robotically.

#### Middle terms

For $n$ even, one middle term: $T_{n/2 + 1} = \binom{n}{n/2} a^{n/2} b^{n/2}$. For $n$ odd, two: $T_{(n+1)/2}$ and $T_{(n+3)/2}$, with $k = \tfrac{n-1}{2}, \tfrac{n+1}{2}$ — mirror images by $\binom{n}{k} = \binom{n}{n-k}$. (JEE Main asks for these verbatim; know them cold.)


#### Consecutive coefficients and equal coefficients

If three consecutive *binomial* coefficients of row $n$ are known, divide neighbours: $\binom{n}{k+1}/\binom{n}{k} = \frac{n-k}{k+1}$ — a rational equation for $(n,k)$. Likewise $\binom{n}{r} = \binom{n}{s}$ iff $r = s$ or $r + s = n$: always report both branches.



### 2.2 Worked examples — the machine, three gears

#### **S3**[JEE Main][solved][general term]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^4$ in $(2+x)^6$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: $T_{k+1}$ with the constant carried along.** General term: $\binom{6}{k} 2^{6-k} x^k$. Target $x^4 \Rightarrow k = 4$: coefficient $= \binom{6}{4} 2^{2} = 15 \cdot 4 = 60$.


Answer: **Answer: $60$**


**Check by symmetry of work:** the $x^2$ coefficient is $\binom{6}{2} 2^4 = 240$; the ratio $60/240 = \tfrac14$ equals $\frac{\binom64}{\binom62}\cdot\frac14$ as the general-term formula predicts ✓.

</details>

#### **S4**[JEE Adv][solved][constant term]Find the term independent of [formula] in [formula] .

Find the term independent of $x$ in $\left(x - \dfrac{2}{x^2}\right)^9$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: exponent equation.** $T_{k+1} = \binom{9}{k} x^{9-k} (-2)^k x^{-2k}
        = \binom{9}{k}(-2)^k x^{9-3k}$. Kill the power: $9 - 3k = 0 \Rightarrow k = 3$. Coefficient: $\binom{9}{3}(-2)^3 = 84 \cdot (-8) = -672$.


Answer: **Answer: $-672$**


**Check:** had we asked for $x^3$ instead ($k=2$): $\binom92 \cdot 4 = 144$ — smaller magnitude and positive, exactly as the sign structure demands ✓.

</details>

#### **S5**[JEE Adv][solved][multinomial]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^3$ in $(1+x+x^2)^4$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: multinomial census.** Four brackets, each offering $1, x, x^2$. To total $x^3$ the picks are either $\{x^2, x, 1, 1\}$ — arrange in $\frac{4!}{1!1!2!} = 12$ ways — or $\{x, x, x, 1\}$ — $\frac{4!}{3!1!} = 4$ ways. Total $12 + 4 = 16$.


Answer: **Answer: $16$**


**Check by full expansion:** $(1+x+x^2)^4 = 1 + 4x + 10x^2 + 16x^3 + 19x^4 + 16x^5 + \cdots + x^8$ — the $x^3$ slot reads 16 ✓ (and the row is symmetric, as $x^2(1/x + 1 + x)^4$ forces).

</details>


### 2.3 Multinomial coefficients and counting terms

The $r$-bracket-outcome generalisation: in $(x_1 + \cdots + x_r)^n$, the number of raw products with outcome-counts $(n_1, \dots, n_r)$ is

$$ (x_1 + \cdots + x_r)^n = \sum_{n_1 + \cdots + n_r = n} \frac{n!}{n_1!\, n_2! \cdots n_r!}\; x_1^{n_1} \cdots x_r^{n_r}. $$

Read the coefficient as: line up the $n$ brackets in a row, mark which $n_1$ gave $x_1$, which $n_2$ gave $x_2$, … — $\binom{n}{n_1}\binom{n-n_1}{n_2}\cdots = \frac{n!}{\prod n_i!}$.

#### How many terms survive collecting?

For $(x_1+\cdots+x_r)^n$ in independent variables, a collected term is determined by its exponent tuple, so the count is the number of solutions of $n_1 + \cdots + n_r = n$:


$$ \binom{n + r - 1}{r - 1}. \qquad\text{(With each variable required to appear: } \binom{n-1}{r-1}.\text{)} $$


> **⚠ Common Trap — "number of terms" of a collected expression with a twist**
>
> "Terms in the expansion of $(1+x+x^2)^n$" is NOT $\binom{n+2}{2}$: collecting powers of a *single* variable collapses everything into $x^0,\dots,x^{2n}$ — at most $2n+1$ terms, and all of them do occur here. Always ask: collected in which variable(s)?

> **★ Olympiad Extension — the multinomial as a pigeonhole engine**
>
> The multinomial coefficient $\frac{n!}{n_1!\cdots n_r!}$ counts the arrangements of a multiset. Olympiad problems disguise this: "the coefficient of $x^{a}y^{b}$ in $(x+y+z)^n$" is exactly the number of length-$n$ words over $\{x,y,z\}$ with $a$ x's and $b$ y's. Whenever a problem counts objects described by *how many of each kind*, a multinomial coefficient is the right shape of answer.



### 2.4 Where the coefficients peak

The coefficients of row $n$ rise then fall. Dividing consecutive terms, $\binom{n}{k+1}/\binom{n}{k} = \frac{n-k}{k+1}$, the ratio passes through 1 exactly when $k = \frac{n-1}{2}$. So:

- $n$ even: single peak $\binom{n}{n/2}$;
- $n$ odd: two equal peaks $\binom{n}{(n-1)/2} = \binom{n}{(n+1)/2}$.

For a *full* expansion $(a+bx)^n$ (weights $a, b$ matter now) the same ratio test on $t_k = \binom{n}{k} a^{n-k} b^k x^k$ decides "greatest *term* at a point": $t_{k+1} \ge t_k \iff (n-k)\,|bx| \ge (k+1)\,|a|$. Sum all such inequalities once and you have the whole distribution's shape.

#### Practice set — the machinery

#### **P9**[JEE Main][practice][general term]Find the coefficient of [formula] in [formula] , and of [formula] .

Find the coefficient of $x^5$ in $(1+x)^{12}$, and of $x^7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: read the row.** $\binom{12}{5} = 792$; $\binom{12}{7} = \binom{12}{5} = 792$ by symmetry.


Answer: **792 for both**. (Check: $\binom{12}{5} = \frac{12\cdot11\cdot10\cdot9\cdot8}{120} = 792$ ✓.)

</details>

#### **P10**[JEE Main][practice][general term]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^4$ in $(3-2x)^7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: carry the weights.** $T_{k+1} = \binom{7}{k} 3^{7-k}(-2x)^k$; $k = 4$: $\binom{7}{4} 3^3 (-2)^4 = 35 \cdot 27 \cdot 16 = 15120$.


Answer: **$15120$**. (Even $k$ ⇒ positive — sign check ✓.)

</details>

#### **P11**[JEE Adv][practice][constant term]Find the term independent of [formula] in [formula] .

Find the term independent of $x$ in $\left(2x - \dfrac{3}{x^2}\right)^6$.

<details>
<summary>Answer + Reasoning</summary>

**Method: exponent equation.** $T_{k+1} = \binom{6}{k} 2^{6-k}(-3)^k x^{6-3k}$; $6 - 3k = 0 \Rightarrow k = 2$: $\binom62 \cdot 2^4 \cdot 9 = 15 \cdot 16 \cdot 9 = 2160$.


Answer: **$2160$**. (Check $k=2$ is the only solution in $[0,6]$ ✓.)

</details>

#### **P12**[JEE Adv][practice][ratio of coefficients]Three consecutive binomial coefficients in the expansion of [formula] are [for…

Three consecutive binomial coefficients in the expansion of $(1+x)^n$ are $36, 84, 126$. Find $n$.

<details>
<summary>Answer + Reasoning</summary>

**Method: consecutive ratios.** $\frac{\binom{n}{k+1}}{\binom{n}{k}} = \frac{84}{36} = \frac73$ and $\frac{126}{84} = \frac32$. From the second: $3(n-k-1) = 2(k+2)$. Trial on small rows of the triangle lands on $\binom{9}{2} = 36, \binom{9}{3} = 84, \binom{9}{4} = 126$ — consistent with the first ratio too: $\frac{9-2}{3} = \frac73$ ✓.


Answer: **$n = 9$**. (No other row works since ratios $\frac{n-k}{k+1}$ strictly decrease as $k$ grows ✓.)

</details>

#### **P13**[JEE Adv][practice][peak location]Find the greatest binomial coefficient in the expansion of [formula] . Which p…

Find the greatest binomial coefficient in the expansion of $(1+x)^{13}$. Which powers of $x$ carry it, and why two?

<details>
<summary>Answer + Reasoning</summary>

**Method: parity rule.** $n = 13$ odd ⇒ two equal middle peaks $k = 6, 7$: $\binom{13}{6} = \binom{13}{7} = 1716$. The ratio $\frac{13-k}{k+1}$ passes through exactly $1$ at $k = 6$, so the row climbs $1 \to 6$ and falls $7 \to 13$, with the top two steps tied by symmetry $\binom{13}{6} = \binom{13}{7}$.


Answer: **$1716$** (at $x^6$ and $x^7$). (Check: $\binom{13}{5} = 1287 < 1716$ ✓.)

</details>

#### **P14**[JEE Adv][practice][multinomial]Find the coefficient of [formula] in [formula] — using the multinomial census,…

Find the coefficient of $x^3$ in $(1+x+x^2)^4$ — using the multinomial census, not by squaring the square.

<details>
<summary>Answer + Reasoning</summary>

**Method: count picks.** Exponent-3 patterns from four brackets: $x^2 \cdot x \cdot 1 \cdot 1$: $\frac{4!}{1!1!2!} = 12$; $x\cdot x \cdot x \cdot 1$: $\frac{4!}{3!1!} = 4$. (No other composition of 3 into parts at most 2 fits 4 slots with each slot at most 2; the $x^2\cdot x$ patterns exhaust it.) Total 16.


Answer: **16**. (Same number S5 reached — two independent routes agreeing ✓.)

</details>

#### **P15**[JEE Main][practice][constant term]Find the constant term of [formula] .

Find the constant term of $\left(x^2 + \dfrac{1}{x}\right)^9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: exponent equation.** $T_{k+1} = \binom9k x^{18-3k}$; $18 - 3k = 0 \Rightarrow k = 6$: coefficient $\binom{9}{6} = \binom{9}{3} = 84$.


Answer: **$84$**. (Weights are 1 so the raw binomial coefficient answers directly ✓.)

</details>

#### **P16**[Olympiad][practice][multinomial census]Find the coefficient of [formula] in [formula] , and again in [formula] . Why …

Find the coefficient of $a^2b^2c^2$ in $(a+b+c)^6$, and again in $(a+b+c+d)^6$. Why is the second reading subtler than it looks?

<details>
<summary>Answer + Reasoning</summary>

**Method: multinomial coefficient.** Pick-lists with counts $(2,2,2)$ from 6 brackets: $\frac{6!}{2!2!2!} = \frac{720}{8} = 90$. In the four-bracket census the exponent tuple $(2,2,2,0)$ is allowed and counts $\frac{6!}{2!2!2!0!} = 90$ too — the "$d^0$-for-all-remaining" decision is made exactly once, and $0! = 1$ is why nothing changes. The subtlety: in $(a+b+c+d)^6$ the monomial $a^2b^2c^2$ also receives no help from anywhere else (no bracket produces $d$ then cancels), so 90 really is the full answer.


Answer: **$90$ in both readings (with the $0!$ remembered)**. (Check: sum of all coefficients of $(a{+}b{+}c)^6$ at $a{=}b{=}c{=}1$ is $3^6 = 729$, and $90$ sits as the middle term of a 28-term row — plausible magnitude ✓.)

</details>




---

