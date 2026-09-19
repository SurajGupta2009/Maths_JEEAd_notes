# Chapter 4 — Beyond Non-Negative Integer Powers

*4 sections · 11 questions*

*Chapter 4 of 6*

# Beyond Non-Negative Integer Powers

The census of brackets died at negative exponents — you cannot choose from $-2$ brackets. But look at the coefficients $\binom{n}{k}$ as the *polynomial* $\frac{n(n-1)\cdots(n-k+1)}{k!}$ in the top entry, and the formula keeps making sense for every $n$, including negatives and halves. The price: the expansion no longer terminates, and a validity condition $(|x| \lt 1)$ is welded to every line. This chapter is where "approximation" problems live, and where JEE quietly checks whether you read the fine print.

### 4.0 What you will be able to do

- Define $\binom{r}{k}$ for any real $r$, and state Euler's theorem: $(1+x)^r = \sum_k \binom{r}{k}x^k$ converges exactly for $|x| \lt 1$.
- Run the three canonical negative series $(1-x)^{-1}, (1-x)^{-2}, (1-x)^{-1/2}$ from memory — and *derive* each in one line when asked.
- Choose which bracket to factor out so that the validity condition holds (expand in ascending vs descending powers — the classic JEE Advanced validity trap).
- Approximate $\sqrt{1.04}$, $\sqrt[3]{1.03}$ with an explicit error budget instead of vibes.


### 4.1 The generalised coefficient, and why it must be this one

For integer $n$, $\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}$ — a falling product of $k$ factors over $k!$. Nothing in that *expression* needs $n$ to be a positive integer, so we adopt it as the definition for all real $r$:

$$ \binom{r}{k} := \frac{r\,(r-1)\cdots(r-k+1)}{k!}, \qquad \binom{r}{0} := 1. $$

Why *this* extension and not another? Because the three engines of Chapter 3 survive it. Differentiate $(1+x)^r$: $\frac{d}{dx}(1+x)^r = r(1+x)^{r-1}$, which is exactly the statement that the series satisfies the recursion its coefficients should have — the same calculation that proved every identity in §3.1. The extension is forced, not chosen.

Two families to own completely:

- **Negative integers:** 
$$ \binom{-n}{k} = (-1)^k \binom{n+k-1}{k} \;\Rightarrow\; (1-x)^{-n} = \sum_{k\ge0} \binom{n+k-1}{k} x^k, \quad |x| \lt 1. $$
 The signs are absorbed by writing $(-x)$: the coefficients of $(1-x)^{-n}$ are all *positive* — a stars-and-bars count ("multisets"), the mirror image of the finite census.
- **Halves:** 
$$ (1+x)^{1/2} = 1 + \tfrac{x}{2} - \tfrac{x^2}{8} + \tfrac{x^3}{16} - \cdots, \qquad
      (1-x)^{-1/2} = \sum_{k\ge0} \frac{\binom{2k}{k}}{4^k} x^k, \quad |x| \lt 1, $$


the second one being the central-binomial generating function — keep it sighted, it is how "coefficient of $x^5$ in $(1-x)^{-1/2}$" becomes a one-liner $\big(\frac{\binom{10}{5}}{4^5} = \frac{63}{256}\big)$.

> **⚠ Common Trap — the expansion you write must be the one that converges**
>
> "Expand $(3+2x)^{-2}$ in ascending powers of $x$." Factor the *constant*: $(3+2x)^{-2} = \frac{1}{9}\left(1 + \frac{2x}{3}\right)^{-2}$, valid for $\left|\frac{2x}{3}\right| \lt 1$, i.e. $|x| \lt \frac32$. Had the question said *descending* powers of $x$, you must factor $2x$ instead — $\frac{1}{4x^2}\left(1 + \frac{3}{2x}\right)^{-2}$, valid for $|x| \gt \frac32$. Wrong factorisation $=$ a divergent series written as if it were an answer $=$ zero marks.

> **★ Olympiad Extension — the radius is not pedantry**
>
> $\sum_k \binom{r}{k} x^k$ has radius of convergence 1 for every $r \notin \{0,1,2,\dots\}$ (ratio test: consecutive coefficients behave like $1 - \frac{r+1}{k+1} \to 1$... the failure of termination is exactly the failure of finiteness). At the boundary $x = \pm 1$ the answer is delicate and beautiful: the series converges at $x=-1$ iff $r \gt 0$ and at $x = 1$ iff $r \gt -1$ — Abel's theorem then lets the boundary values be taken as limits, which is what justifies $\sum_k \frac{\binom{2k}{k}}{4^k} x^k \to (1-x)^{-1/2}$ as $x \to 1^{-}$. JEE tests the $|x| \lt 1$ part; analsis tests the rest — one chapter away.


### 4.2 Worked examples

#### **S9**[JEE Main][solved][negative exponent]Find the coefficient of [formula] in [formula] , in full: derive the general c…

Find the coefficient of $x^2$ in $(1-x)^{-3}$, in full: derive the general coefficient first.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: generalised binomial coefficient.** $\binom{-3}{k} = \frac{(-3)(-4)\cdots(-3-k+1)}{k!} = (-1)^k \frac{(k+2)!}{2\,k!} =
        (-1)^k \binom{k+2}{2}$. With $x^k$: signs $(-1)^k(-x)^k$... cleaner to use the derived family: $(1-x)^{-3} = \sum_{k\ge0} \binom{k+2}{2} x^k$. At $k=2$: $\binom{4}{2} = 6$.


Answer: **Answer: $6$**


**Check:** $(1-x)^{-3} = \frac{d^2/dx^2}{2!}\,(1-x)^{-1}$ — differentiating $\sum x^k$ twice gives $\sum (k{+}2)(k{+}1) x^k / 2$, the same $\binom{k+2}{2}$ ✓.

</details>

#### **S10**[JEE Adv][solved][factor + validity]Find the first two terms in the expansion of [formula] in ascending powers of …

Find the first two terms in the expansion of $(4+3x)^{-1/2}$ in ascending powers of $x$, and the values of $x$ for which the expansion is valid.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: factor the 4, then one series.** $(4+3x)^{-1/2} = \frac12 \left(1 + \frac{3x}{4}\right)^{-1/2}$. Using $(1+u)^{-1/2} = 1 - \frac{u}{2} + \cdots$: 
$$ \frac12 \left( 1 - \frac{3x}{8} + \cdots \right) = \frac12 - \frac{3x}{16} + \cdots $$
 Validity: $\left|\frac{3x}{4}\right| \lt 1 \iff |x| \lt \frac43$.


Answer: **Answer: $\dfrac12 - \dfrac{3x}{16} + \cdots,\ \ |x| \lt \dfrac43$**


**Check:** at $x = 0$ both sides are $1/2$ ✓; the ratio of corrections at $x = 0.1$ is $-0.01875 / 0.5 = -3.75\%$, matching $\frac12\cdot(-\frac12)\cdot 0.075$ — first-order consistency ✓.

</details>

#### **S11**[JEE Adv][solved][approximation]Use the binomial series to estimate [formula] correct to two decimal places, a…

Use the binomial series to estimate $\sqrt[3]{26}$ correct to two decimal places, and justify the accuracy.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: anchor at the nearest perfect cube.** $26 = 27(1 - \frac{1}{27})$, so $\sqrt[3]{26} = 3\left(1 - \frac{1}{27}\right)^{1/3}$. With $u = -\frac{1}{27}$ and $(1+u)^{1/3} = 1 + \frac{u}{3} - \frac{u^2}{9} + \cdots$: 
$$ 3\left( 1 - \frac{1}{81} - \frac{1}{6561} \right) = 3 \times 0.987502 = 2.96250. $$



Answer: **Answer: $\approx 2.96$** (true value $2.96250\ldots$).


**Error budget:** the dropped third-order term has magnitude $3 \cdot \frac{|\tfrac13(-\tfrac23)(-\tfrac53)|}{6} |u|^3 \lt 3 \cdot 0.1 \cdot (0.038)^3 \lt 10^{-4}$ — cannot move the second decimal ✓.

</details>


### 4.3 Summing infinite series by recognition

The reverse engine: a numerical series that looks hopeless is often a binomial series at a lucky $x$. The pattern to hunt: coefficients that *are* $\binom{n+k-1}{k}$, $\binom{2k}{k}$, or polynomial multiples like $k+1$ — each is a known series evaluated at some rational $x$.


$$ \sum_{k=0}^{\infty} (k+1)\, t^k = \frac{1}{(1-t)^2}, \qquad
    \sum_{k=0}^{\infty} \binom{n+k-1}{k} t^k = \frac{1}{(1-t)^n}, \qquad |t| \lt 1, $$


so e.g. $1 + 2(0.9) + 3(0.9)^2 + \cdots = \frac{1}{0.01} = 100$. A JEE Main classic, done in one line once the recognition reflex exists.

> **💡 Key Idea — approximation = one series value at tiny |x|**
>
> $\sqrt{1.04}$ is $(1+x)^{1/2}$ at $x = 0.04$: keep two terms for a rough value, three for exam-grade accuracy, four for 5 decimal places — then *bound the first dropped term* to certify the digits. Alternating-ish series with decreasing terms end on the first omitted term; say so in one sentence and the question is bulletproof.

> **⚠ Common Trap — (2+x)⁶ vs (1+2x)⁶ thinking they are the same series**
>
> Factor before expanding: $(2+x)^6$ in ascending powers needs the constant pulled out; $(1+\frac{x}{2})^6 \cdot 2^6$ — and for the *infinite* version $(2+x)^{-3}$, the validity is $|\frac{x}{2}| \lt 1$, i.e. $|x| \lt 2$, not $|x| \lt 1$. The number inside the radius is the ratio, never 1 by default.

#### Practice set — infinite expansions

#### **P26**[JEE Main][practice][negative exponent]Find the coefficient of [formula] in [formula] , deriving the general coeffici…

Find the coefficient of $x^4$ in $(1-x)^{-2}$, deriving the general coefficient from $\binom{-2}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: generalised coefficient.** $\binom{-2}{k} = (-1)^k (k+1)$, so $(1-x)^{-2} = \sum_k (k+1) x^k$ and the slot $k = 4$ reads $5$.


Answer: **$5$**. (Check: this is the derivative of the geometric series $\sum x^k = (1-x)^{-1}$ — differentiating multiplies term $k$ by $k$ and shifts, giving $k+1$ ✓.)

</details>

#### **P27**[JEE Main][practice][negative exponent]Find the coefficient of [formula] in [formula] , and state for which [formula]…

Find the coefficient of $x^6$ in $(1+3x)^{-2}$, and state for which $x$ your series is valid.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute into the owned family.** $(1+u)^{-2} = \sum_k (-1)^k (k+1) u^k$ with $u = 3x$: the $x^6$ coefficient is $(-1)^6 \cdot 7 \cdot 3^6 = 5103$. Validity: $|3x| \lt 1$, i.e. $|x| \lt \tfrac13$.


Answer: **$5103,\ |x| \lt \tfrac13$**. (Magnitude sanity: $3^6 = 729$, times 7 ✓.)

</details>

#### **P28**[JEE Adv][practice][factor + validity]Expand [formula] in ascending powers of [formula] up to and including the line…

Expand $(3+2x)^{-2}$ in ascending powers of $x$ up to and including the linear term; state the validity condition.

<details>
<summary>Answer + Reasoning</summary>

**Method: factor the constant first.** $(3+2x)^{-2} = \frac19\left(1 + \frac{2x}{3}\right)^{-2}
        = \frac19 \left( 1 - 2\cdot\frac{2x}{3} + \cdots \right) = \frac19 - \frac{4x}{27} + \cdots$, valid for $|x| \lt \tfrac32$.


Answer: **$\frac19 - \frac{4x}{27} + \cdots,\ \ |x| \lt \frac32$**. (Check at $x = 0$: LHS $= 1/9$ ✓.)

</details>

#### **P29**[JEE Adv][practice][negative exponent]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^2$ in $(1+2x)^{-3}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: owned family, then substitute.** $(1+u)^{-3} = \sum_k (-1)^k \binom{k+2}{2} u^k$; $u = 2x$, $k = 2$: $\binom{4}{2} \cdot 4 = 24$.


Answer: **24**. (Signs: $k$ even ⇒ positive ✓; validity would be $|x| \lt \tfrac12$.)

</details>

#### **P30**[JEE Adv][practice][recognition]Evaluate [formula] .

Evaluate $1 + 2(0.9) + 3(0.9)^2 + 4(0.9)^3 + \cdots$.

<details>
<summary>Answer + Reasoning</summary>

**Method: recognise $(1-t)^{-2}$.** $\sum_k (k+1) t^k = (1-t)^{-2}$ at $t = 0.9$: $= (0.1)^{-2} = 100$.


Answer: **100**. (Converges since $|t| \lt 1$; partial sum of the first 22 terms already exceeds 99 — the tail carries $0.9^{22}$-sized dust ✓.)

</details>

#### **P31**[JEE Adv][practice][approximation]Estimate [formula] correct to five decimal places using four terms, and justif…

Estimate $\sqrt{1.02}$ correct to five decimal places using four terms, and justify the accuracy.

<details>
<summary>Answer + Reasoning</summary>

**Method: $(1+x)^{1/2}$ at $x = 0.02$.** $1 + 0.01 - \frac{0.0004}{8} + \frac{8\times 10^{-6}}{16} = 1 + 0.01 - 0.00005 + 0.0000005$, i.e. $1.0099505$. First dropped term $= \frac{5}{128}x^4 \lt 10^{-8}$.


Answer: **$1.00995$**. (True value $1.0099505\ldots$ — five decimals certified ✓.)

</details>

#### **P32**[JEE Adv][practice][central binomial]Find the coefficient of [formula] in [formula] .

Find the coefficient of $x^5$ in $(1-x)^{-1/2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: owned family.** $(1-x)^{-1/2} = \sum_k \frac{\binom{2k}{k}}{4^k} x^k$; at $k = 5$: $\frac{\binom{10}{5}}{4^5} = \frac{252}{1024} = \frac{63}{256}$.


Answer: **$\frac{63}{256}$**. (Check the sign story: all coefficients of $(1-x)^{-1/2}$ are positive ✓ — and $\frac{63}{256} \approx 0.246$, consistent with a slowly decaying central-binomial tail.)

</details>

#### **P33**[Olympiad][practice][coefficient engine]Prove [formula] .

Prove $\displaystyle\sum_{k=0}^{\infty} \frac{\binom{2k}{k}}{8^k} = \sqrt{2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the generating function at a legal point.** From P32's family, $\sum_k \binom{2k}{k} t^k = (1-4t)^{-1/2}$ (radius $|t| \lt \tfrac14$). Put $t = \tfrac18$ — inside the radius — giving $(1 - \tfrac12)^{-1/2} = \sqrt 2$.


Answer: **proved: $\sqrt2$**. (Numerically: $1 + 0.25 + 0.09375 + 0.0390625 + 0.0170898 + \cdots$ — the running sums march toward $1.41421\ldots = \sqrt2$ ✓. The general rule: any series whose $k$-th coefficient is $\binom{2k}{k} r^k$ is the $(1-4x)$-family evaluated at $x = r$, and it converges exactly when $|r| \lt \tfrac14$. At the boundary $r = \tfrac14$ the sum $\sum_k \binom{2k}{k} 4^{-k}$ diverges (its terms are $\sim 1/\sqrt{\pi k}$) — the radius is not decoration.

</details>




---

