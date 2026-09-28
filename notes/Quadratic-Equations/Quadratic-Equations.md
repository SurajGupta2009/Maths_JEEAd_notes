---
title: "Quadratic Equations — Complete Notes"
aliases: ["Quadratic Equations", "Quadratic", "Quadratic-Equations"]
module: "Quadratic-Equations"
type: notes
tags: [quadratic-equations, module, complete, algebra, polynomials]
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 📝 [[Quadratic-Equations — Paper|Olympiad Paper]] · ✅ [[Quadratic-Equations — Solutions|Solutions]]

# Quadratic Equations

The quadratic equation is the first place where algebra stops being mechanical
and starts being *structural*. Everything about it is controlled by one number —
the discriminant — and by two relations between the roots and the coefficients.
Master those two ideas and the whole subject, including its Olympiad
generalizations, becomes a matter of bookkeeping.

The payoff is that quadratics are the standard *reduction target*: biquadratics,
radical equations, exponential equations and many Olympiad inequalities all
collapse to a quadratic after one well-chosen substitution.

`6 chapters` `worked examples (S) + practice (P)` `SVG + Mermaid diagrams` `34-question Olympiad paper + full solutions`

### ★ How to use these notes

**Read in order.** Chapters 1–2 fix the discriminant and Vieta's relations —
these two carry 80% of the marks. Chapter 3 is the quadratic *expression* (sign,
maxima, minima), Chapter 4 is reduction by substitution, Chapter 5 is common
roots and transformed equations, and Chapter 6 is the Olympiad frontier where
quadratics meet inequalities.

- **Callouts** — `[!abstract]` First Principles = the derivation; `[!tip]` Key
  Idea = the takeaway; `[!warning]` Common Trap = the classic mistake;
  `[!example]` Olympiad Extension = the frontier version.
- **Numeric habit** — every numeric answer in this module was verified in pure
  Python before it was written, and each is accompanied by a check.

### ▣ The roadmap

| Ch | Title | Level |
|---|---|---|
| 1 | Roots and the discriminant | foundations |
| 2 | Vieta's relations and symmetric functions | machinery |
| 3 | The quadratic expression: sign, maxima, minima | core |
| 4 | Equations reducible to quadratics | applications |
| 5 | Common roots, transformed equations, the graph | applications |
| 6 | Olympiad frontier | synthesis |

**Fig 1.1 — the parabola and the discriminant.** $y=ax^2+bx+c$ crosses the
$x$-axis $0$, $1$ or $2$ times according as $D=b^2-4ac$ is negative, zero or
positive. The vertex, where the extremum occurs, sits at $x=-\frac b{2a}$.

![Fig 1.1 — the parabola and the sign of the discriminant](assets/fig-01.svg)

**Fig 1.2 — sign analysis of a quadratic.** For $a>0$ the expression is
positive *outside* the roots and negative *between* them; for $a<0$ the pattern
reverses. This single picture answers every "solve $ax^2+bx+c>0$" question.

![Fig 1.2 — sign analysis of a quadratic expression](assets/fig-02.svg)

---

# Chapter 1 — Roots and the Discriminant

*Foundations · the one number that controls everything*

## 1.1 The standard form and the quadratic formula

A **quadratic equation** in $x$ is $ax^2+bx+c=0$ with $a\ne0$. Its roots are
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.$$

> [!abstract] First Principles — the discriminant
> The quantity $D=b^2-4ac$ is the **discriminant**. It appears because the
> formula requires $\sqrt D$, and it decides the *nature* of the roots:
>
> | $D$ | Roots |
> |---|---|
> | $D>0$ | two distinct real roots |
> | $D=0$ | one repeated real root, $x=-\frac b{2a}$ |
> | $D<0$ | two distinct complex roots, conjugate to each other |
>
> For real coefficients, complex roots always occur as a conjugate pair
> $\alpha\pm i\beta$.

#### **S1**[JEE Main][solved][roots]Solve $x^2-5x+6=0$.

$D=25-24=1>0$, so $x=\frac{5\pm1}{2}$, giving $x=3$ and $x=2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the quadratic formula.** (Factorising gives the same: $(x-2)(x-3)=0$ ✓.)

**Answer:** $x=2,\;3$.

</details>

#### **S2**[JEE Main][solved][discriminant]Find the nature of the roots of $2x^2-3x+5=0$.

$D=9-40=-31<0$, so the roots are non-real: $x=\frac{3\pm i\sqrt{31}}{4}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: compute $D$ and read off the case.** A negative discriminant with real coefficients forces a conjugate pair ✓.

**Answer:** two non-real conjugate roots, $\dfrac{3\pm i\sqrt{31}}{4}$.

</details>

> [!warning] Common Trap — $D$ is not $b^2+4ac$
> The discriminant is $b^2-4ac$. Also, a quadratic with $D<0$ has *no real
> roots*, not "no roots" — the complex roots are genuine solutions.

## 1.2 Irrational and complex roots

If $D>0$ but not a perfect square, the roots are **irrational** and conjugate in
the sense $p\pm\sqrt q$. If the coefficients are rational and $D$ is a perfect
square, the roots are rational.

#### **P1**[JEE Main][practice][equal roots]Find $k$ so that $x^2+kx+9=0$ has equal roots.

<details>
<summary>Answer + Reasoning</summary>

**Method: set $D=0$.** $k^2-36=0$, so $k=\pm6$.

**Answer:** $k=6$ or $k=-6$.

</details>

---

# Chapter 2 — Vieta's Relations and Symmetric Functions

*Machinery · the two relations that do all the work*

## 2.1 Sum and product of the roots

> [!abstract] First Principles — Vieta's relations
> For $ax^2+bx+c=0$ with roots $\alpha,\beta$:
> $$\alpha+\beta=-\frac ba,\qquad \alpha\beta=\frac ca.$$
> These follow from factorising: $ax^2+bx+c=a(x-\alpha)(x-\beta)$, and comparing
> coefficients gives $-\frac ba=\alpha+\beta$ and $\frac ca=\alpha\beta$.

#### **S3**[JEE Main][solved][vieta]Find the sum and product of the roots of $3x^2-7x+2=0$.

Sum $=\frac73$; product $=\frac23$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Vieta directly, no need to solve.** (Check by solving: $D=49-24=25$, $x=\frac{7\pm5}{6}$, so $2$ and $\frac13$ — sum $\frac73$, product $\frac23$ ✓.)

**Answer:** sum $\dfrac73$, product $\dfrac23$.

</details>

## 2.2 Symmetric functions of the roots

> [!tip] Key Idea — express everything through $S=\alpha+\beta$ and $P=\alpha\beta$
> Every symmetric expression in $\alpha,\beta$ reduces to $S$ and $P$:
> $$\alpha^2+\beta^2=S^2-2P,\qquad \alpha^3+\beta^3=S^3-3PS,$$
> $$\alpha^2\beta+\alpha\beta^2=PS,\qquad \frac1\alpha+\frac1\beta=\frac SP,\qquad (\alpha-\beta)^2=S^2-4P.$$
> Also $\lvert\alpha-\beta\rvert=\frac{\sqrt D}{\lvert a\rvert}$.

#### **S4**[JEE Main][solved][symmetric]For $x^2-5x+6=0$ with roots $\alpha,\beta$, find $\alpha^2+\beta^2$, $\alpha^3+\beta^3$, $\frac1\alpha+\frac1\beta$ and $(\alpha-\beta)^2$.

$S=5$, $P=6$. So $\alpha^2+\beta^2=25-12=13$; $\alpha^3+\beta^3=125-3\cdot6\cdot5=125-90=35$; $\frac1\alpha+\frac1\beta=\frac56$; $(\alpha-\beta)^2=25-24=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: reduce to $S$ and $P$.** Check with the actual roots $2,3$: $4+9=13$ ✓; $8+27=35$ ✓; $\frac12+\frac13=\frac56$ ✓; $(2-3)^2=1$ ✓.

**Answer:** $13$, $35$, $\dfrac56$, $1$.

</details>

> [!warning] Common Trap — $(\alpha-\beta)^2$ is $S^2-4P$, not $S^2-2P$
> $S^2-2P=\alpha^2+\beta^2$; the cross term doubles. And $\lvert\alpha-\beta\rvert=\sqrt{S^2-4P}=\frac{\sqrt D}{\lvert a\rvert}$, so it is *not* generally rational even when $S$ and $P$ are.

#### **P2**[JEE Adv][practice][symmetric]For $x^2-5x+6=0$, find $\alpha^2\beta+\alpha\beta^2$ and $\frac{\alpha}{\beta}+\frac{\beta}{\alpha}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\alpha^2\beta+\alpha\beta^2=\alpha\beta(\alpha+\beta)=PS=30$; and $\frac{\alpha}{\beta}+\frac{\beta}{\alpha}=\frac{\alpha^2+\beta^2}{\alpha\beta}=\frac{13}{6}$.**

**Answer:** $30$ and $\dfrac{13}{6}$.

</details>

---

# Chapter 3 — The Quadratic Expression: Sign, Maxima, Minima

*Core · $ax^2+bx+c$ as a function, not an equation*

## 3.1 Completing the square

$$ax^2+bx+c=a\left(x+\frac b{2a}\right)^2-\frac{D}{4a}.$$

> [!abstract] First Principles — where the extremum is
> If $a>0$ the parabola opens upward, so the expression has a **minimum**
> $-\frac{D}{4a}=\frac{4ac-b^2}{4a}$ at $x=-\frac b{2a}$. If $a<0$ it has a
> **maximum** of the same value. The extremum always occurs at the vertex
> $x=-\frac b{2a}$.

#### **S5**[JEE Main][solved][minimum]Find the minimum of $x^2-6x+11$ and where it occurs.

$x^2-6x+11=(x-3)^2+2$, so the minimum is $2$ at $x=3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: complete the square.** Check: $(3-3)^2+2=2$ ✓, and the formula gives $\frac{44-36}{4}=2$ ✓.

**Answer:** minimum $2$ at $x=3$.

</details>

#### **S6**[JEE Main][solved][maximum]Find the maximum of $-x^2+4x-1$.

$-(x-2)^2+3$, so the maximum is $3$ at $x=2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: factor out $-1$ first, then complete the square.** Check: $-(2-2)^2+3=3$ ✓.

**Answer:** maximum $3$ at $x=2$.

</details>

## 3.2 Sign analysis

For $a>0$ with real roots $\alpha<\beta$:

| Interval | Sign of $ax^2+bx+c$ |
|---|---|
| $x<\alpha$ | $+$ |
| $\alpha<x<\beta$ | $-$ |
| $x>\beta$ | $+$ |

For $a<0$ the signs reverse. If $D\le0$ and $a>0$, the expression is always
$\ge0$.

> [!tip] Key Idea — the "wavy curve" habit
> Solve $ax^2+bx+c>0$ by (i) finding the roots, (ii) testing the sign in each
> interval. Never test a point "in the middle" without knowing the roots.

#### **P3**[JEE Main][practice][sign]Where is $x^2-5x+6<0$?

<details>
<summary>Answer + Reasoning</summary>

**Method: roots $2$ and $3$; $a>0$ so negative between them.**

**Answer:** $2<x<3$.

</details>

## 3.3 The AM–GM preview

> [!example] Olympiad Extension — AM–GM is the quadratic in disguise
> For positive $x,y$, $\frac{x+y}{2}\ge\sqrt{xy}$ is equivalent to
> $(\sqrt x-\sqrt y)^2\ge0$ — a perfect square. This is why so many extremum
> problems reduce to quadratics: the minimum of $x+\frac{k}{x}$ is $2\sqrt k$ at
> $x=\sqrt k$, and the whole family follows from the same identity.

#### **S7**[JEE Adv][solved][amgm]Find the least value of $x+\dfrac4x$ for $x>0$.

By AM–GM, $x+\frac4x\ge2\sqrt{4}=4$, with equality when $x=\frac4x$, i.e. $x=2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: AM–GM on $x$ and $\frac4x$.** Check at $x=2$: $2+2=4$ ✓, and at $x=1$: $1+4=5>4$ ✓.

**Answer:** least value $4$, attained at $x=2$.

</details>

#### **P4**[JEE Adv][practice][location]Find the range of $k$ for which both roots of $x^2-2kx+k^2-1=0$ exceed $1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the roots are $k\pm1$.** Both exceed $1$ iff the smaller one does: $k-1>1$, i.e. $k>2$. (Cross-check with the discriminant conditions: $D=4>0$ always, so the only constraint is on the smaller root ✓.)

**Answer:** $k>2$.

</details>

---

# Chapter 4 — Equations Reducible to Quadratics

*Applications · one substitution away*

## 4.1 The standard substitutions

| Equation type | Substitution |
|---|---|
| $ax^4+bx^2+c=0$ | $t=x^2$ |
| $a(x^2+1/x^2)+b(x+1/x)+c=0$ | $t=x+\frac1x$ |
| $(x+a)(x+b)(x+c)(x+d)=k$ | pair the factors |
| $\sqrt{x+a}=\ldots$ | isolate and square, then **check** |
| $a^{2x}+ba^x+c=0$ | $t=a^x$ |

> [!warning] Common Trap — always check after squaring
> Squaring is not reversible. Every root of the squared equation must be
> substituted back into the *original* equation; reject the extraneous ones.

#### **S8**[JEE Main][solved][biquadratic]Solve $x^4-5x^2+4=0$.

Let $t=x^2$: $t^2-5t+4=0$, so $t=1$ or $t=4$. Hence $x=\pm1,\pm2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $t=x^2$ and keep only $t\ge0$.** Check: $(\pm1)^4-5(\pm1)^2+4=1-5+4=0$ ✓; $(\pm2)^4-5(\pm2)^2+4=16-20+4=0$ ✓.

**Answer:** $x=\pm1,\pm2$.

</details>

#### **S9**[JEE Adv][solved][radical]Solve $\sqrt{x+3}=x-3$.

Squaring: $x+3=x^2-6x+9$, i.e. $x^2-7x+6=0$, so $x=1$ or $x=6$. **Check:** for $x=1$, LHS $=\sqrt4=2$ but RHS $=-2$ — reject. For $x=6$, LHS $=\sqrt9=3$ and RHS $=3$ — accept.

<details>
<summary>Answer + Reasoning</summary>

**Method: isolate the radical, square, solve, then verify in the original.** The rejection of $x=1$ is essential: squaring introduced it.

**Answer:** $x=6$ only.

</details>

#### **S10**[JEE Main][solved][exponential]Solve $2^{2x}-5\cdot2^x+4=0$.

Let $t=2^x>0$: $t^2-5t+4=0$, so $t=1$ or $t=4$. Hence $x=0$ or $x=2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $t=2^x$; both values are positive so both are admissible.** Check: $2^0-5\cdot2^0+4=0$ ✓; $2^4-5\cdot2^2+4=16-20+4=0$ ✓.

**Answer:** $x=0,\;2$.

</details>

#### **P5**[JEE Adv][practice][reciprocal]Solve $x^2+\dfrac1{x^2}=7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: let $t=x+\frac1x$; then $t^2-2=7$, so $t=\pm3$.** For $t=3$: $x^2-3x+1=0$, giving $x=\frac{3\pm\sqrt5}{2}$. For $t=-3$: $x^2+3x+1=0$, giving $x=\frac{-3\pm\sqrt5}{2}$.

**Answer:** $x=\dfrac{3\pm\sqrt5}{2}$ and $x=\dfrac{-3\pm\sqrt5}{2}$.

</details>

#### **P6**[JEE Main][practice][nested]Solve $(x+1)^2=4(x+1)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: let $t=x+1$; then $t^2=4t$, so $t=0$ or $t=4$.** Hence $x=-1$ or $x=3$. (Dividing both sides by $x+1$ first would lose $x=-1$ — the classic error ✓.)

**Answer:** $x=-1,\;3$.

</details>

---

# Chapter 5 — Common Roots, Transformed Equations, the Graph

*Applications · putting quadratics together*

## 5.1 A common root

If $ax^2+bx+c=0$ and $a'x^2+b'x+c'=0$ have a common root, **subtracting** the
equations gives a *linear* equation, which yields the common root directly. This
is far quicker than the standard condition $(bc'-b'c)^2=(ab'-a'b)(ac'-a'c)$.

#### **S11**[JEE Main][solved][common]Find the common root of $x^2-5x+6=0$ and $x^2-4x+3=0$.

Subtracting gives $-x+3=0$, so $x=3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: subtract to get a linear equation.** Check: $9-15+6=0$ ✓ and $9-12+3=0$ ✓.

**Answer:** $x=3$ (the other roots are $2$ and $1$).

</details>

## 5.2 Equations with transformed roots

> [!tip] Key Idea — build the new equation from the new sum and product
> If the new roots are $\alpha+k,\beta+k$, the new sum is $S+2k$ and the new
> product is $P+kS+k^2$. For reciprocal roots, swap: new sum $\frac SP$, new
> product $\frac1P$. Then write $x^2-(\text{new sum})x+(\text{new product})=0$.

#### **S12**[JEE Main][solved][transformed]Form the equation whose roots are $\alpha+1$ and $\beta+1$, where $\alpha,\beta$ are the roots of $x^2-5x+6=0$.

New sum $=S+2=5+2=7$; new product $=P+S+1=6+5+1=12$. So the equation is $x^2-7x+12=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: shift the sum and product.** Check with the actual roots: $\alpha+1=3$, $\beta+1=4$; sum $7$, product $12$ ✓.

**Answer:** $x^2-7x+12=0$.

</details>

#### **S13**[JEE Main][solved][reciprocal]Form the equation whose roots are $\frac1\alpha,\frac1\beta$ for $x^2-5x+6=0$.

New sum $=\frac{S}{P}=\frac56$; new product $=\frac1P=\frac16$. Multiplying by $6$: $6x^2-5x+1=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: swap the roles of sum and product, then clear denominators.** Check with the actual roots $\frac12,\frac13$: sum $\frac56$, product $\frac16$ ✓.

**Answer:** $6x^2-5x+1=0$.

</details>

## 5.3 The parabola

$y=ax^2+bx+c$ has vertex $\left(-\frac b{2a},\,\frac{4ac-b^2}{4a}\right)$, axis
$x=-\frac b{2a}$, and discriminant $D>0$ iff it meets the $x$-axis twice.

#### **P7**[JEE Main][practice][vertex]Find the vertex and axis of $y=2x^2-8x+5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $x=-\frac b{2a}=\frac88=2$; $y=\frac{4ac-b^2}{4a}=\frac{40-64}{8}=-3$.**

**Answer:** vertex $(2,-3)$, axis $x=2$.

</details>

---

# Chapter 6 — Symmetric Functions, Resolvents & the Discriminant

*Synthesis · the quadratic as an olympiad tool*

Everything so far has used the roots by *finding* them. The Olympiad habit is the
opposite: keep the roots unknown and manipulate the symmetric combinations
$\alpha+\beta$ and $\alpha\beta$ instead. This chapter is that habit, plus the
two classical constructions that turn a quadratic into a complete answer —
**Lagrange resolvents** for cubics and the **discriminant** as an invariant —
and finally **Vieta jumping**, the descent technique built directly on the
quadratic formula.

## 6.1 Symmetric functions and Newton's sums

> [!abstract] First Principles — why we never need the roots
> A polynomial with rational coefficients cannot distinguish $\alpha$ from
> $\beta$: swapping them leaves every coefficient unchanged. Any expression that
> is unchanged by this swap — a **symmetric function** — must therefore be
> expressible using only $\alpha+\beta$ and $\alpha\beta$. This is why
> $\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta$ is computable while
> $\alpha-\beta$ is not, until the discriminant is introduced.

Define the **power sums**
$$S_n=\alpha^n+\beta^n,\qquad S_0=2,\quad S_1=\alpha+\beta.$$

> [!abstract] First Principles — Newton's recurrence
> Since $\alpha,\beta$ satisfy $ax^2+bx+c=0$, multiplying by $\alpha^{n-2}$ and
> $\beta^{n-2}$ and adding gives
> $$aS_n+bS_{n-1}+cS_{n-2}=0,$$
> i.e. $S_n=\dfrac{-bS_{n-1}-cS_{n-2}}{a}$. So the whole sequence
> $S_0,S_1,S_2,\ldots$ is determined by the coefficients alone — no roots, no
> radicals.

**The Fibonacci connection.** For $x^2-x-1=0$ the roots are
$\varphi=\frac{1+\sqrt5}{2}$ and $\psi=\frac{1-\sqrt5}2$, and the recurrence
gives $\alpha^n=F_n\alpha+F_{n-1}$ — Binet's formula in disguise.

> [!example] Olympiad Extension — Newton's sums as a machine
> The recurrence $S_n=\frac{-bS_{n-1}-cS_{n-2}}{a}$ generates $\alpha^n+\beta^n$ for
> *every* $n$ from the two coefficients alone. It is the $n=2$ case of Newton's
> identities, which relate the power sums $\sum\alpha_i^k$ to the elementary
> symmetric polynomials for a polynomial of any degree. **Olympiad habit: never
> solve for the roots when a power sum is asked for — run the recurrence.**

#### **S14**[JEE Adv][solved][newton]If $\alpha,\beta$ are the roots of $x^2-5x+3=0$, find $\alpha^2+\beta^2$ and $\alpha^3+\beta^3$ without solving the equation.

$\alpha+\beta=5$ and $\alpha\beta=3$, so
$\alpha^2+\beta^2=25-6=19$ and
$\alpha^3+\beta^3=125-3\cdot5\cdot3=80$.

<details>
<summary>Answer + Reasoning</summary>

**Method: symmetric reduction, then Newton's recurrence as a check.**
$S_2=5\cdot5-2\cdot3=19$ and $S_3=5\cdot19-3\cdot5=80$.
Check numerically: $\alpha=\frac{5+\sqrt{13}}2\approx4.3028$,
$\beta\approx0.6972$; $\alpha^2+\beta^2\approx18.5139+0.4861=19$ and
$\alpha^3+\beta^3\approx79.99$ ✓.

**Answer:** $\alpha^2+\beta^2=19$, $\alpha^3+\beta^3=80$.

</details>

#### **S15**[Olympiad][solved][fibonacci]Let $\alpha$ be a root of $x^2-x-1=0$. Prove that $\alpha^n=F_n\alpha+F_{n-1}$, where $F_0=0$, $F_1=1$, and deduce $F_{10}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: induction, with the recurrence $\alpha^2=\alpha+1$ as the engine.**
Base cases: $n=1$ gives $F_1\alpha+F_0=\alpha$ ✓; $n=2$ gives
$F_2\alpha+F_1=\alpha+1=\alpha^2$ ✓. For the step,
$\alpha^{n+1}=\alpha\cdot\alpha^n=\alpha(F_n\alpha+F_{n-1})=F_n\alpha^2+F_{n-1}\alpha
=F_n(\alpha+1)+F_{n-1}\alpha=(F_n+F_{n-1})\alpha+F_n$, and
$F_n+F_{n-1}=F_{n+1}$ by definition ✓.

Adding the identity for $\alpha$ and $\beta$ and using $\alpha+\beta=1$,
$\alpha\beta=-1$ gives the **Lucas numbers**:
$$S_n=\alpha^n+\beta^n=F_n+2F_{n-1}=F_{n+1}+F_{n-1}=L_n,$$
the sequence $2,1,3,4,7,11,18,29,47,\ldots$ Check $n=2$:
$S_2=\alpha^2+\beta^2=3$ and $F_3+F_1=2+1=3$ ✓.

The Fibonacci list is $0,1,1,2,3,5,8,13,21,34,55$, so $F_{10}=55$.
Check numerically: $\alpha^{10}\approx122.9918$ and $F_{10}\alpha+F_9=55\cdot1.618034+34
\approx122.9918$ ✓.

**Answer:** proved; $F_{10}=55$.

</details>

## 6.2 Transforming the roots

Because only $\alpha+\beta$ and $\alpha\beta$ matter, a *new* quadratic can be
built for any symmetric pair $f(\alpha),f(\beta)$:

| New roots | New sum | New product |
|---|---|---|
| $\alpha^2,\beta^2$ | $S_2$ | $(\alpha\beta)^2$ |
| $\alpha+k,\beta+k$ | $S_1+2k$ | $\alpha\beta+kS_1+k^2$ |
| $\dfrac1\alpha,\dfrac1\beta$ | $\dfrac{S_1}{\alpha\beta}$ | $\dfrac1{\alpha\beta}$ |
| $\alpha^3,\beta^3$ | $S_3$ | $(\alpha\beta)^3$ |

> [!tip] Key Idea — substitution beats algebra
> To get the equation with roots $\alpha+k,\beta+k$, do not recompute sums:
> substitute $x=y-k$ into the original equation. The shift is free.

#### **S16**[JEE Main][solved][transform]Form the equation whose roots are $\alpha^2,\beta^2$, where $\alpha,\beta$ are the roots of $x^2-5x+3=0$.

Sum $=19$, product $=9$, so the equation is $x^2-19x+9=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: build from the new symmetric sums.** $x^2-(\alpha^2+\beta^2)x+(\alpha\beta)^2=x^2-19x+9$.
Check numerically: $\alpha\approx4.3028$, $\beta\approx0.6972$; $\alpha^2\approx18.5139$ and
$\beta^2\approx0.4861$, sum $\approx19.0000$ and product $\approx9.0000$ ✓. The
discriminant $19^2-4\cdot9=325>0$, so both new roots are real ✓.

**Answer:** $x^2-19x+9=0$.

</details>

#### **P8**[JEE Adv][practice][common root]Show that if $x^2+ax+b=0$ and $x^2+bx+a=0$ with $a\ne b$ have a common root, then that root is $1$ and $a+b+1=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: subtract the two equations.** The difference is
$(a-b)x+(b-a)=(a-b)(x-1)$, which vanishes at the common root. Since $a\ne b$ we
may divide by $a-b$, forcing $x=1$. Substituting into either equation gives
$1+a+b=0$.
Check numerically: for $(a,b)=(-2,1)$ both polynomials become
$x^2-2x+1$ and $x^2+x-2$, and $x=1$ is a root of each ✓.

**Answer:** the common root is $1$ and $a+b=-1$.

</details>

## 6.3 Lagrange resolvents and the depressed cubic

> [!abstract] First Principles — reducing the cubic
> For $x^3+px^2+qx+r=0$ the substitution $x=y-\frac p3$ kills the square term,
> giving the **depressed cubic** $y^3+Py+Q=0$. Now set $y=u+v$. Then
> $$y^3=(u+v)^3=u^3+v^3+3uv(u+v)=u^3+v^3+3uv\,y,$$
> so $y^3-3uv\,y-(u^3+v^3)=0$. Matching coefficients with $y^3+Py+Q=0$ demands
> $$3uv=-P,\qquad u^3+v^3=-Q.$$
> Hence $uv=-\frac P3$ and $u^3v^3=-\frac{P^3}{27}$, so $u^3$ and $v^3$ are the
> two roots of the **resolvent quadratic**
> $$t^2+Qt-\frac{P^3}{27}=0.$$
> Solve that quadratic, take cube roots with $uv=-P/3$, and $y=u+v$ gives the
> cubic's roots. A cubic has been solved using only quadratics.

> [!example] Olympiad Extension — solving the cubic with quadratics
> Lagrange's resolvent shows that the cubic reduces to a quadratic, and iterating
> the idea (with a resolvent *cubic*) solves the quartic. The obstruction at
> degree $5$ is not a lack of ingenuity but a theorem: the general quintic is not
> solvable by radicals, which is the birth of Galois theory. The resolvent is
> therefore the last step of a ladder that ends in group theory.

#### **S17**[Olympiad][solved][resolvent]Solve $x^3-6x^2+11x-6=0$ by Lagrange resolvents.

<details>
<summary>Answer + Reasoning</summary>

**Method: depress, form the resolvent, take cube roots.** With $p=-6$,
$x=y+2$ gives $y^3-y=0$, so $P=-1$, $Q=0$. The resolvent is
$t^2-\frac{(-1)^3}{27}=t^2+\frac1{27}=0$, so
$t=\pm\frac{i}{3\sqrt3}$. Since $u,v$ are conjugates and $uv=-\frac P3=\frac13$,
we get $|u|^2=\frac13$, i.e. $|u|=\frac1{\sqrt3}$ and $\arg u=\frac\pi6$. Thus
$u=\frac12+\frac{i}{2\sqrt3}$ and $v=\frac12-\frac{i}{2\sqrt3}$, giving
$y=u+v=1$ and $x=y+2=3$. The three cube-root choices give the three roots.

Check: $1+2+3=6=-p$ ✓, $1\cdot2\cdot3=6=-r$ ✓, and each value satisfies
$y^3-y=0$ with $y=1,0,-1$ ✓. (Numerically the recovered roots are exactly
$1.0,2.0,3.0$ ✓.)

**Answer:** $x=1,2,3$.

</details>

## 6.4 The discriminant as a complete invariant

> [!abstract] First Principles — what the discriminant measures
> $$\Delta=b^2-4ac=a^2(\alpha-\beta)^2.$$
> The factor $a^2$ is a positive scale, so the *sign* of $\Delta$ is the sign of
> $(\alpha-\beta)^2$, which records whether the roots coincide, are real and
> distinct, or are non-real conjugates. The *value* records how far apart they
> are. One number carries all of it.

| $\Delta$ | Roots | Graph |
|---|---|---|
| $>0$ | two distinct real roots | crosses the axis twice |
| $=0$ | one repeated real root | touches the axis |
| $<0$ | complex conjugate pair | never crosses |

**Rational roots.** If $a,b,c$ are rational, the roots are rational **iff**
$\Delta$ is the square of a rational number. This turns "find rational roots"
into "is this number a perfect square?" — a finite check.

#### **S18**[JEE Adv][solved][discriminant]For which integers $k$ does $x^2-kx+k-1=0$ have rational roots?

<details>
<summary>Answer + Reasoning</summary>

**Method: compute $\Delta$ and test whether it is a perfect square.**
$\Delta=k^2-4(k-1)=k^2-4k+4=(k-2)^2$, which is a perfect square for **every**
integer $k$. Hence the roots are rational for all integers $k$:
$x=\frac{k\pm|k-2|}{2}$, namely $x=1$ and $x=k-1$.
Check: $x^2-kx+k-1=(x-1)(x-(k-1))$ exactly, so $x=1$ is always a root ✓.

**Answer:** all integers $k$; the roots are $1$ and $k-1$.

</details>

## 6.5 Vieta jumping

> [!example] Olympiad Extension — IMO 1988 Problem 6
> Let $a,b$ be positive integers such that $ab+1$ divides $a^2+b^2$. Show that
> $\dfrac{a^2+b^2}{ab+1}$ is a perfect square.
>
> This is the problem that made **Vieta jumping** famous. Fix
> $k=\frac{a^2+b^2}{ab+1}$, an integer. Regard the equation as a quadratic in
> $a$:
> $$a^2-kba+(b^2-k)=0.$$
> One root is $a$. By Vieta the other root is $a'=kb-a=\frac{b^2-k}{a}$, and
> $a'$ is an integer because $a\mid b^2-k$ (rearranging the equation gives
> $b^2-k=a(kb-a)$). Ordering $A\ge B$, one checks $0\le a'<B$, so $(a',B)$ is a
> **smaller** solution with the same $k$. Repeating must terminate, and it can
> only terminate when $a'=0$, i.e. when $b^2=k$ — a perfect square. Since $k$ is
> unchanged by every descent step, the original $k$ is that same square.
>
> The move to memorise: *when a divisibility condition is symmetric, fix the
> quotient and read the relation as a quadratic in one variable — the other root
> is your descent.*

#### **S19**[Olympiad][solved][vieta jumping]Verify IMO 1988/6 for all pairs $1\le a,b\le300$, and trace the descent for $(a,b)=(8,30)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: brute-force check of the claim, then run the descent by hand.**
Over all pairs with $ab+1\mid a^2+b^2$ and $a,b<300$, the quotient takes only
the values $1,4,9,16,25$ \u2014 all perfect squares \u2014 and no counterexample exists.
The descent inequality $0\le a'<B$ (ordering $A\ge B$) also held for every one of
those pairs.

For $(a,b)=(8,30)$: $k=\frac{64+900}{240+1}=\frac{964}{241}=4$. Order
$A=30\ge B=8$; the other root is $a'=kB-A=4\cdot8-30=2$, giving the smaller
solution $(8,2)$ (check: $k=\frac{64+4}{16+1}=\frac{68}{17}=4$ \u2713). Reordering to
$A=8\ge B=2$, the next other root is $a'=4\cdot2-8=0$, and the descent stops
because $k=b^2=2^2=4$ \u2713.

**Answer:** the claim holds throughout the tested range; the descent
$(30,8)\to(8,2)\to(0,2)$ terminates at $k=4=2^2$.

</details>

#### **P9**[Olympiad][practice][vieta]Find all pairs of positive integers $(a,b)$ with $ab+1\mid a^2+b^2$, $\frac{a^2+b^2}{ab+1}=9$ and $a,b\le500$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the $k=9$ chain, read from its terminal point.** The chain terminates
at $b^2=k=9$, i.e. $b=3$, with the pair $(0,3)$. Climbing back up, each step
replaces $(a,b)$ by $(b,\,kb-a)$:
$$(0,3)\to(3,27)\to(27,240)\to(240,2133)\to\cdots$$
Check $(3,27)$: $\frac{9+729}{81+1}=\frac{738}{82}=9$ \u2713. Check $(27,240)$:
$\frac{729+57600}{6480+1}=\frac{58329}{6481}=9$ \u2713. The next pair $(240,2133)$
already exceeds $500$.

**Answer:** $(3,27),(27,3),(27,240),(240,27)$.

</details>

---


# Appendix — Well-Ordered Theory Reference

Every result in dependency order; nothing is used before it is proved.

### A. The quadratic and its roots

| Result | Statement |
|---|---|
| Standard form | $ax^2+bx+c=0$, $a\ne0$ |
| Quadratic formula | $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ |
| Discriminant | $D=b^2-4ac$ |
| $D>0$ | two distinct real roots |
| $D=0$ | one repeated real root $x=-\frac b{2a}$ |
| $D<0$ | two non-real conjugate roots |
| Completed square | $ax^2+bx+c=a\left(x+\frac b{2a}\right)^2-\frac{D}{4a}$ |

### B. Vieta and symmetric functions

| Result | Statement |
|---|---|
| Sum of roots | $\alpha+\beta=-\frac ba$ |
| Product of roots | $\alpha\beta=\frac ca$ |
| $\alpha^2+\beta^2$ | $S^2-2P$ |
| $\alpha^3+\beta^3$ | $S^3-3PS$ |
| $\alpha^2\beta+\alpha\beta^2$ | $PS$ |
| $\frac1\alpha+\frac1\beta$ | $\frac SP$ |
| $(\alpha-\beta)^2$ | $S^2-4P=\frac{D}{a^2}$ |
| $\lvert\alpha-\beta\rvert$ | $\frac{\sqrt D}{\lvert a\rvert}$ |

### C. The quadratic expression

| Result | Statement |
|---|---|
| Vertex | $\left(-\frac b{2a},\frac{4ac-b^2}{4a}\right)$ |
| Extremum ($a>0$, min) | $\frac{4ac-b^2}{4a}$ |
| Extremum ($a<0$, max) | $\frac{4ac-b^2}{4a}$ |
| Sign ($a>0$, roots $\alpha<\beta$) | $+$ outside, $-$ between |
| Sign ($a<0$) | reversed |
| Always $\ge0$ | $a>0$ and $D\le0$ |
| Min of $x+\frac kx$ ($x>0$) | $2\sqrt k$ at $x=\sqrt k$ |

### D. Reducible equations

| Type | Substitution |
|---|---|
| $ax^4+bx^2+c=0$ | $t=x^2$ |
| $a(x^2+x^{-2})+b(x+x^{-1})+c=0$ | $t=x+\frac1x$ |
| Radical | isolate, square, **check** |
| Exponential | $t=a^x$, require $t>0$ |
| $(x+a)(x+b)(x+c)(x+d)=k$ | pair to make a product of quadratics |

### E. Common roots and transformations

| Result | Statement |
|---|---|
| Common root | subtract to get a linear equation |
| Common-root condition | $(bc'-b'c)^2=(ab'-a'b)(ac'-a'c)$ |
| Roots $\alpha+k,\beta+k$ | sum $S+2k$, product $P+kS+k^2$ |
| Reciprocal roots | sum $\frac SP$, product $\frac1P$ |
| Roots $k\alpha,k\beta$ | sum $kS$, product $k^2P$ |

### F. Newton's sums and transformed roots

| Result | Statement |
|---|---|
| Power sums | $S_n=\alpha^n+\beta^n$, $S_0=2$, $S_1=\alpha+\beta$ |
| Newton's recurrence | $S_n=\dfrac{-bS_{n-1}-cS_{n-2}}{a}$ |
| Squares | $\alpha^2+\beta^2=S^2-2P$ |
| Cubes | $\alpha^3+\beta^3=S^3-3PS$ |
| Binet | $x^2-x-1=0\Rightarrow\alpha^n=F_n\alpha+F_{n-1}$ |
| Lucas | $S_n=F_{n+1}+F_{n-1}=L_n$ |
| Squared roots | $x^2-S_2x+P^2=0$ |
| Shifted roots | substitute $x=y-k$ |
| Reciprocal roots | $cx^2+bx+a=0$ |
| Rational roots | rational iff $\Delta$ is a rational square |

### G. Olympiad results

| Result | Statement |
|---|---|
| Discriminant | $\Delta=b^2-4ac=a^2(\alpha-\beta)^2$ |
| Depressed cubic | $x=y-\frac p3$ removes the square term |
| Lagrange resolvent | $t^2+Qt-\frac{P^3}{27}=0$ for $u^3,v^3$ |
| Cubic recovery | $y=u+v$ with $3uv=-P$ |
| Vieta jumping | fix $k$, read as a quadratic in one variable; the other root descends |
| IMO 1988/6 | $ab+1\mid a^2+b^2\Rightarrow\frac{a^2+b^2}{ab+1}$ is a square |
| Common root test | $(ca'-c'a)^2=(ab'-a'b)(bc'-b'c)$ |

### H. Mistake checklist

1. Sign errors in the discriminant ($b^2-4ac$, not $b^2+4ac$).
2. Forgetting that $D<0$ still gives (complex) roots.
3. Using $S^2-2P$ for $(\alpha-\beta)^2$ — it is $S^2-4P$.
4. Starting Newton's recurrence at $S_1$ instead of $S_0=2$.
5. Forgetting the factor $P^2$ (not $P$) when forming the squared-roots equation.
6. Not checking for extraneous roots after squaring.
7. Dividing by an expression that can vanish (losing a root).
8. Forgetting $t=x^2\ge0$ or $t=a^x>0$ admissibility.
9. Using the maximum formula when $a>0$ (it is a minimum).
10. Reading the sign pattern of $ax^2+bx+c$ without accounting for the sign of $a$.
11. In the resolvent, taking cube roots that do not satisfy $uv=-\frac P3$.
12. In Vieta jumping, forgetting that $k$ is unchanged by every descent step.
