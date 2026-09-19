# Chapter 3 — Three Identity Engines

*4 sections · 12 questions*

*Chapter 3 of 6*

# Three Identity Engines

"Prove $\sum_k k\binom{n}{k} = n2^{n-1}$" looks like a different problem from "evaluate $\sum_k \frac{1}{k+1}\binom{n}{k}$". They are the same problem wearing different hats, and this module gives you only three engines to run them all: **substitute**, **differentiate/integrate** the master polynomial $(1+x)^n$, and **extract coefficients / count twice** (Vandermonde and its family). Memorised identities decay; engines do not.

### 3.0 What you will be able to do

- Derive, not recall: $\sum \binom{n}{k} = 2^n$, $\sum k\binom{n}{k} = n2^{n-1}$, $\sum k(k-1)\binom{n}{k} = n(n-1)2^{n-2}$, and the divided-by-$(k{+}1)$ integral twin.
- Prove Vandermonde's convolution $\sum_k \binom{r}{k}\binom{s}{n-k} = \binom{r+s}{n}$ by two independent engines, then specialise it to $\sum_k \binom{n}{k}^2 = \binom{2n}{n}$.
- Run the hockey-stick identity from Pascal's rule, telescoping style.
- Choose signs wisely: $x = -1$ and alternating sums are the same engine with the brake on.


### 3.1 Engine 1 — substitution, and Engine 2 — calculus

Everything runs on one identity, the master polynomial:

$$ f(x) = (1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k. $$

**Engine 1 (substitute).** $f(1)$: row sum $= 2^n$. $f(-1)$: alternating sum $= 0$ (splitting rows into even/odd halves). $f(2) = 3^n$: "weighted row sum" $\sum \binom{n}{k} 2^k = 3^n$ — the census for choosing from brackets $(1 + 2)$. Every evaluation point is a different weighting of the same census.

**Engine 2 (differentiate, then substitute).** Multiply-by-$k$ is a derivative's fingerprint: 
$$ x f'(x) = \sum_k k \binom{n}{k} x^k \;\Rightarrow\; \sum_k k \binom{n}{k} = n\cdot 2^{n-1}, \qquad
    (x f')'(1) = \sum_k k(k-1)\binom{n}{k} = n(n-1) 2^{n-2}. $$


Divide-by-$(k+1)$ is an *integral's* fingerprint: 
$$ \sum_{k=0}^n \frac{\binom{n}{k}}{k+1} = \int_0^1 (1+x)^n\, dx = \frac{2^{n+1} - 1}{n+1}, $$


and putting the alternating series inside the same integral gives the razor-thin variant $\sum_k \frac{(-1)^k}{k+1}\binom{n}{k} = \int_0^1 (1-x)^n dx = \frac{1}{n+1}$. Note what just happened: two "completely different" sums, one line apart in the statement, differ by exactly one engine setting.

> **⛁ First Principles — why "multiply by k" must be a derivative**
>
> For a monomial, $\frac{d}{dx} x^k = k x^{k-1}$, so $x\frac{d}{dx} x^k = kx^k$: the operator $x \frac{d}{dx}$ stamps the exponent onto the front of every term *simultaneously*. That is the whole trick — any $\sum (\text{polynomial in } k)\binom{n}{k}$ is a fixed combination of $f, xf', (xf')',\dots$ evaluated at a point. $k^2$ needs both: $\sum k^2 \binom{n}{k} = \sum k(k{-}1)\binom{n}{k} + \sum k\binom{n}{k} = n(n{+}1) 2^{n-2}$.

> **⚠ Common Trap — evaluating the derivative at the wrong point**
>
> $\sum k\binom{n}{k}$ means $x f'(x)$ at $x=1$, i.e. $n(1+1)^{n-1} \cdot 1$. Students differentiate to $n(1+x)^{n-1}$ and substitute $x=1$ forgetting the outer $x$ (which is 1 here — but at $x = 2$, $\sum k \binom nk 2^k = n \cdot 2 \cdot 3^{n-1}$, and the missing $x$ is now a factor-2 error). Write the operator, *then* evaluate.


### 3.2 Worked examples

#### **S6**[JEE Adv][solved][calculus engine]Evaluate [formula] .

Evaluate $\displaystyle\sum_{k=0}^{6} k(k-1)\binom{6}{k}$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: second derivative of the master polynomial.** $(1+x)^6$ twice differentiated: $30(1+x)^4 = \sum_k k(k-1)\binom{6}{k} x^{k-2}$. Put $x = 1$: $30 \cdot 16 = 480$.


Answer: **Answer: $480$**


**Small-case check:** at $n = 3$: $0 + 0 + 2\cdot 3 + 6\cdot 1 = 12 = 3\cdot 2 \cdot 2^{1}$ ✓ — matches $n(n-1)2^{n-2}$.

</details>

#### **S7**[JEE Adv][solved][peak + sum]State the greatest coefficient of [formula] , then prove it: no calculator.

State the greatest coefficient of $(1+x)^{21}$, then prove it: no calculator.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: consecutive-term ratio.** $\binom{21}{k+1}/\binom{21}{k} = \frac{21-k}{k+1} \ge 1 \iff k \le 10$. So the row climbs to $k = 10$ and the ratio at $k=10$ equals $\frac{11}{11} = 1$: entries $k=10,11$ tie, then fall. Peaks: $\binom{21}{10} = \binom{21}{11}$.


Value: $\binom{21}{10} = \frac{21\cdot20\cdots 12}{10!}$. Cancel 20·15·12 against $10!$'s factors and compute: $\binom{21}{10} =$ **Answer: $352716$**.


**Check:** row sum $2^{21} = 2097152$; ten symmetric pairs around a central tie of $2 \times 352716 \approx 7.05 \times 10^5$ is under half the total — consistent with a peaked distribution ✓.

</details>

#### **S8**[Olympiad][solved][coefficient extraction]Evaluate [formula] and name the general identity it instantiates.

Evaluate $\displaystyle\sum_{k=0}^{6} \binom{6}{k}\binom{6}{6-k}$ and name the general identity it instantiates.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: read it as one coefficient.** In $(1+x)^6 (1+x)^6 = (1+x)^{12}$, the $x^6$ coefficient is $\sum_k \binom{6}{k}\binom{6}{6-k}$ on the left and $\binom{12}{6}$ on the right. So the sum is $\binom{12}{6} = 924$.


General form — **Vandermonde's convolution**: $\sum_k \binom{r}{k}\binom{s}{n-k} = \binom{r+s}{n}$, obtained identically from $(1+x)^r (1+x)^s = (1+x)^{r+s}$ at the $x^n$ slot. The combinatorial census: choose $n$ people from $r$ men $+ s$ women, grouping by $k$ men.


Answer: **Answer: $924 = \binom{12}{6}$**


**Check with the special case $\sum \binom{n}{k}^2 = \binom{2n}{n}$** at $n=2$: $1 + 4 + 1 = 6 = \binom42$ ✓.

</details>


### 3.3 Engine 3 — coefficients, telescoping, and the family album

Engine 3 (used at S8) is the most olympiad-flavoured: *an identity between sums of binomial coefficients is one coefficient of one product of two binomial expansions*. Keep $(1+x)^A (1-x)^B (1+x^2)^C = (1+x)^{n}$-style factorisations in mind; choosing $A,B,C$ is the whole game.

#### The two-line album (derive each from an engine; never memorise raw)

- $\sum_k \binom{n}{k} = 2^n$, $\sum_k (-1)^k \binom{n}{k} = 0$ — substitution.
- $\sum_k k \binom{n}{k} = n 2^{n-1}$, $\sum_k k^2 \binom{n}{k} = n(n+1) 2^{n-2}$ — calculus.
- $\sum_k \frac{\binom{n}{k}}{k+1} = \frac{2^{n+1}-1}{n+1}$, $\sum_k \frac{(-1)^k \binom{n}{k}}{k+1} = \frac{1}{n+1}$ — integral engine.
- $\sum_k \binom{n}{k}^2 = \binom{2n}{n}$, $\sum_k (-1)^k \binom{n}{k}^2 = \begin{cases} 0, & n \text{ odd}\\ (-1)^{n/2} \binom{n}{n/2}, & n \text{ even} \end{cases}$ — coefficient engine (the second one from the $x^n$ slot of $(1-x^2)^n$).
- **Hockey stick:** $\sum_{i=r}^{m} \binom{i}{r} = \binom{m+1}{r+1}$ — telescoping of Pascal's rule $\binom{i}{r} = \binom{i+1}{r+1} - \binom{i}{r+1}$.

> **💡 Key Idea — the $x^n$ slot is a bank vault**
>
> Any question of the shape "sum over $k$ of a *product* of binomial coefficients" is asking for one coefficient of a product of expansions. Squares are the diagonal case ($r = s = n$, $n$th slot), and the alternating square sum is the same vault with $(1-x)^n (1+x)^n = (1-x^2)^n$ — a polynomial with only even powers, which is *why* it vanishes for odd $n$. Structure, not memory.

> **★ Olympiad Extension — finite differences annihilate polynomials**
>
> The operator $\Delta P(x) = P(x+1) - P(x)$ drops degree by one, so the $n$-th difference of a degree-$n$ polynomial is constant and equals $n!$·(leading coefficient). Unwinding $\Delta^n$ by the binomial theorem: 
> $$ \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} P(x+k) = n!\,[x^n]\,P. $$
>  For $P(x) = x^n$: $\sum_k (-1)^k \binom{n}{k}(x + k)^n = (-1)^n n!$ — a number independent of $x$. (Paper Q37 asks you to prove exactly this; the binomial theorem supplies the telescoping in one line.)


#### Practice set — engines

#### **P17**[JEE Main][practice][substitution]Evaluate [formula] .

Evaluate $\sum_{k=0}^{10} 2^k \binom{10}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: read $f(2)$.** The sum is $(1+2)^{10} = 3^{10}$.


Answer: **$59049$**. (Census check: choices from ten brackets of $1$ or $2x$ at $x=1$: $3^{10}$ ✓.)

</details>

#### **P18**[JEE Main][practice][calculus engine]Evaluate [formula] .

Evaluate $\sum_{k=0}^{10} k \binom{10}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $xf'$ at $x=1$.** $\sum k \binom{10}{k} = 10 \cdot 2^{9} = 5120$.


Answer: **5120**. (Committee-with-chair count gives the same number by design ✓.)

</details>

#### **P19**[JEE Adv][practice][calculus engine]Evaluate [formula] .

Evaluate $\sum_{k=0}^{8} k^2 \binom{8}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: split $k^2 = k(k-1) + k$.** $8 \cdot 9 \cdot 2^{6} = 72 \cdot 64 = 4608$, from $n(n{+}1)2^{n-2}$.


Answer: **4608**. (Small case $n=2$: $0 + 2 + 4 = 6 = 2\cdot3\cdot2^0$ ✓.)

</details>

#### **P20**[JEE Adv][practice][hockey stick]Evaluate [formula] .

Evaluate $\binom{4}{4} + \binom{5}{4} + \binom{6}{4} + \binom{7}{4}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: telescope Pascal's rule.** Hockey stick: the sum is $\binom{8}{5} = 56$.


Answer: **56**. (Direct: $1 + 5 + 15 + 35 = 56$ ✓ — hockey stick earns its keep at larger $m$.)

</details>

#### **P21**[JEE Adv][practice][Vandermonde]Evaluate [formula] .

Evaluate $\sum_{k=0}^{4} \binom{7}{k}\binom{5}{4-k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the $x^4$ slot of $(1+x)^7(1+x)^5$.** Answer $\binom{12}{4} = 495$.


Answer: **495**. (Story: pick a 4-person committee from 7 + 5 people, grouped by how many come from the 7 ✓.)

</details>

#### **P22**[JEE Adv][practice][integral engine]Evaluate [formula] exactly.

Evaluate $\displaystyle\sum_{k=0}^{4} \frac{\binom{4}{k}}{k+1}$ exactly.

<details>
<summary>Answer + Reasoning</summary>

**Method: integrate the master polynomial.** $\int_0^1 (1+x)^4 dx = \frac{31}{5}$, since the integral expands termwise to $\sum \binom{4}{k}\frac{1}{k+1}$.


Answer: **$\frac{31}{5}$**. (Direct: $1 + 2 + 2 + 1 + \frac15 = \frac{31}{5}$ ✓.)

</details>

#### **P23**[Olympiad][practice][coefficient engine]Evaluate [formula] .

Evaluate $\sum_{k=0}^{10} (-1)^k \binom{10}{k}^2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the $x^{10}$ slot of $(1-x^2)^{10}$.** Expand $(1-x)^{10}(1+x)^{10}$; the $x^{10}$ coefficient is the sum on the left, and on the right $10 = 2\cdot 5$ gives $(-1)^5 \binom{10}{5} = -252$.


Answer: **$-252$**. (Odd $n$ would give 0 because $(1-x^2)^n$ has only even powers but odd slot — here $n$ is even, so the vault pays $(-1)^{n/2}\binom{n}{n/2}$ ✓.)

</details>

#### **P24**[Olympiad][practice][count twice]Prove [formula] twice: once by coefficient extraction, once by a counting stor…

Prove $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$ twice: once by coefficient extraction, once by a counting story with no polynomials at all.

<details>
<summary>Answer + Reasoning</summary>

**Method 1:** $x^n$ slot of $(1+x)^n(1+x)^n = (1+x)^{2n}$, using $\binom{n}{n-k} = \binom{n}{k}$ to convert the convolution to a square-sum. **Method 2:** choose $n$ from $2n$ people seated as $n$ pairs — no; cleaner: $2n$ people split into two halves of $n$; a committee of size $n$ with $k$ from the first half: $\binom{n}{k}$ ways for the first half and $\binom{n}{n-k} = \binom{n}{k}$ for the second. Group over $k$. Both engines agree: at $n = 8$, $\binom{16}{8} = 12870$.


Answer: **proved; $12870$ at $n=8$**. (Both proofs are the same vault with different locks — that redundancy is the point ✓.)

</details>

#### **P25**[Olympiad][practice][integral engine]Prove [formula] .

Prove $\displaystyle\sum_{k=0}^{n} \frac{(-1)^k}{k+1}\binom{n}{k} = \frac{1}{n+1}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: integrate $(1-x)^n$, term by term, from 0 to 1.** $\int_0^1 (1-x)^n dx = \frac{1}{n+1}$; expanding $(1-x)^n$ and integrating each monomial produces exactly the left side. One line, done. (This is Catalan's first step: the Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$ is the ratio of the two identities P24 and P25 wearing matching outfits.)


Answer: **proved**. (Numerical at $n=8$: $1 - 4 + \frac{28}{3} - \frac{56}{4} + 14 - \frac{56}{6} + \frac{28}{7} - 1 + \frac19$... the script-checked value is $\frac19$ ✓.)

</details>




---

