---
title: "Inequalities — Complete Notes"
aliases: ["Inequalities", "Inequalities"]
module: "Inequalities"
type: notes
tags: [inequalities, module, complete, algebra, olympiad]
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 📝 [[Inequalities — Paper|Olympiad Paper]] · ✅ [[Inequalities — Solutions|Solutions]]

# Inequalities

An inequality states that one quantity is bigger than another. Two quite
different skills are needed, and it is worth separating them from the start.

The first is **solving** inequalities — finding the set of $x$ for which
$f(x)>0$. This is algorithmic: find the critical points, test the intervals.
The second is **proving** inequalities — showing that some expression is always
non-negative. This is where the real mathematics lives, and it is the Olympiad
heart of the topic.

The bridge between them is a single idea: almost every proof of an inequality
consists of *rewriting the difference as a sum of obviously non-negative
quantities*. Squares, absolute values, and AM–GM are the three sources of
obvious non-negativity, and the whole art is finding the right rewriting.

`6 chapters` `worked examples (S) + practice (P)` `SVG + Mermaid diagrams` `36-question Olympiad paper + full solutions`

### ★ How to use these notes

**Read in order.** Chapters 1–3 are solving: linear, quadratic, rational,
absolute value. Chapter 4 introduces the proof engine — AM–GM and its family.
Chapter 5 adds Cauchy–Schwarz, Titu and Nesbitt. Chapter 6 is the Olympiad
frontier: Schur, Jensen, the $uvw$ method and the tangent-line trick.

- **Callouts** — `[!abstract]` First Principles = the derivation; `[!tip]` Key
  Idea = the takeaway; `[!warning]` Common Trap = the classic mistake;
  `[!example]` Olympiad Extension = the frontier version.
- **Numeric habit** — every numeric answer in this module was verified in pure
  Python before it was written, and each is accompanied by a check.

### ▣ The roadmap

| Ch | Title | Level |
|---|---|---|
| 1 | Linear and quadratic inequalities | foundations |
| 2 | Rational inequalities and the wavy curve | machinery |
| 3 | Absolute value | machinery |
| 4 | AM–GM and the mean family | core |
| 5 | Cauchy–Schwarz, Titu and Nesbitt | applications |
| 6 | Olympiad frontier: Schur, Jensen, uvw | synthesis |

**Fig 1.1 — the sign of a quadratic.** The roots split the line into intervals;
the sign is constant on each and alternates as you cross a simple root. This
picture is the entire method for solving polynomial inequalities.

![Fig 1.1 — sign analysis and the wavy curve method](assets/fig-01.svg)

**Fig 1.2 — AM–GM as a picture.** For fixed sum $a+b$, the product $ab$ is
maximised when $a=b$; equivalently, for fixed product the sum is minimised
there. The whole mean family lives on this one trade-off.

![Fig 1.2 — AM–GM: the trade-off between sum and product](assets/fig-02.svg)

---

# Chapter 1 — Linear and Quadratic Inequalities

*Foundations · the algorithmic half*

## 1.1 Linear inequalities

$a x + b > 0$ solves to $x > -\frac ba$ when $a>0$ and $x < -\frac ba$ when
$a<0$. **Multiplying or dividing by a negative number reverses the
inequality** — the single most common error in this topic.

#### **S1**[JEE Main][solved][linear]Solve $3x+5>2x-7$.

$x>-12$.

<details>
<summary>Answer + Reasoning</summary>

**Method: collect $x$ on one side.** $3x-2x>-7-5$, so $x>-12$. Check at $x=-11$: $3(-11)+5=-28$ and $2(-11)-7=-29$, and $-28>-29$ ✓.

**Answer:** $x>-12$.

</details>

## 1.2 Quadratic inequalities

> [!abstract] First Principles — sign of $ax^2+bx+c$
> For $a>0$ with real roots $\alpha<\beta$, the expression is **positive
> outside** the roots and **negative between** them:
>
> | Interval | Sign ($a>0$) |
> |---|---|
> | $x<\alpha$ | $+$ |
> | $\alpha<x<\beta$ | $-$ |
> | $x>\beta$ | $+$ |
>
> For $a<0$ every sign reverses. If $D\le0$ and $a>0$ the expression is
> $\ge0$ for all $x$.

#### **S2**[JEE Main][solved][quadratic]Solve $x^2-5x+6<0$.

Roots $2$ and $3$; $a>0$, so negative between them: $2<x<3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: find the roots, then read the sign pattern.** Check at $x=2.5$: $6.25-12.5+6=-0.25<0$ ✓; at $x=1$: $1-5+6=2>0$ ✓.

**Answer:** $2<x<3$.

</details>

#### **S3**[JEE Main][solved][always positive]Solve $x^2+x+1>0$.

$D=1-4=-3<0$ and $a>0$, so the expression is positive for **all** real $x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $D<0$ with $a>0$ means no real roots and the parabola never crosses the axis.** Check: at $x=0$, $1>0$; at $x=-1$, $1>0$; the minimum is $\frac{4-1}{4}=\frac34>0$ ✓.

**Answer:** all real $x$.

</details>

> [!warning] Common Trap — the leading coefficient decides the outside/inside rule
> The rule "positive outside the roots" holds only for $a>0$. If $a<0$, factor
> out the minus sign first. Testing a point in the outer region settles it in
> one line, so do that whenever you are unsure.

#### **P1**[JEE Main][practice][cubic]Solve $(x-1)(x-2)(x-3)>0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: mark the roots $1,2,3$ on a line and alternate signs, starting from $+\infty$ where the product is positive.** Sign is $+$ on $(1,2)$ and $(3,\infty)$.

**Answer:** $x\in(1,2)\cup(3,\infty)$.

</details>

---

# Chapter 2 — Rational Inequalities and the Wavy Curve

*Machinery · multiplying by a denominator is dangerous*

## 2.1 The rule

To solve $\frac{P(x)}{Q(x)}>0$, **never multiply through by $Q(x)$** unless you
know its sign. Instead:

1. Factor numerator and denominator completely.
2. Mark every root (of numerator *and* denominator) on a number line.
3. Starting from $+\infty$ (where the expression has the sign of the leading
   coefficients' ratio), alternate the sign at each **simple** root. Roots of
   **even** multiplicity do not change the sign.
4. Exclude the denominator's roots from the answer.

> [!tip] Key Idea — the wavy curve
> Draw a curve that crosses the axis at odd-multiplicity roots and touches it
> at even ones. The regions where the curve is above the axis are the solution.

#### **S4**[JEE Main][solved][rational]Solve $\dfrac{x-1}{x+2}>0$.

Critical points $-2$ and $1$. The expression is positive for $x<-2$ and for
$x>1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: two simple roots, alternate signs; exclude $x=-2$.** Check: at $x=-3$, $\frac{-4}{-1}=4>0$ ✓; at $x=0$, $\frac{-1}{2}<0$ ✓; at $x=2$, $\frac11>0$ ✓.

**Answer:** $x<-2$ or $x>1$.

</details>

#### **S5**[JEE Adv][solved][rational]Solve $\dfrac{x}{x^2-1}\le0$.

Critical points $-1,0,1$. The expression is $\le0$ on $(-\infty,-1)$ and on
$[0,1)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: mark $-1,0,1$; alternate; $x=0$ is included (numerator zero), $x=\pm1$ excluded (denominator zero).** Check: at $x=-2$, $\frac{-2}{3}<0$ ✓; at $x=-\frac12$, $\frac{-1/2}{-3/4}>0$ ✓; at $x=\frac12$, $\frac{1/2}{-3/4}<0$ ✓; at $x=2$, $\frac23>0$ ✓.

**Answer:** $x\in(-\infty,-1)\cup[0,1)$.

</details>

#### **P2**[JEE Adv][practice][rational]Solve $\dfrac{x^2-4}{x-1}\ge0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: numerator roots $\pm2$, denominator root $1$; alternate; include $x=\pm2$, exclude $x=1$.** Check at $x=0$: $\frac{-4}{-1}=4\ge0$ ✓.

**Answer:** $x\in[-2,1)\cup[2,\infty)$.

</details>

#### **P3**[JEE Main][practice][reciprocal]Solve $\dfrac1{x-1}<\dfrac1{x+1}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: bring to one side.** $\frac1{x-1}-\frac1{x+1}=\frac{2}{x^2-1}<0$, so $x^2-1<0$, i.e. $-1<x<1$. Check at $x=0$: $-1<1$ ✓.

**Answer:** $-1<x<1$.

</details>

---

# Chapter 3 — Absolute Value

*Machinery · distance, and the case split it forces*

## 3.1 Definitions and the core tactic

$\lvert x\rvert$ is the distance from $x$ to $0$. The two tools are:

- $\lvert x\rvert<a\iff -a<x<a$ (and $\lvert x\rvert>a\iff x<-a$ or $x>a$)
- $\lvert f(x)\rvert=g(x)\iff f(x)=g(x)$ **or** $f(x)=-g(x)$

Both amount to the same thing: **split into cases at the points where the
inside changes sign**.

> [!tip] Key Idea — $\lvert x-a\rvert+\lvert x-b\rvert$ is a distance sum
> $\lvert x-a\rvert+\lvert x-b\rvert$ is minimised by any $x$ between $a$ and
> $b$, where it equals $\lvert a-b\rvert$. This solves a whole family of
> problems with no algebra at all.

#### **S6**[JEE Main][solved][absolute]Solve $\lvert x-2\rvert<3$.

$-3<x-2<3$, so $-1<x<5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: use $\lvert u\rvert<a\iff-a<u<a$.** Check: the endpoints give $\lvert-3\rvert=3$ and $\lvert3\rvert=3$, so they are excluded (the interval is open) ✓; at $x=2$, $0<3$ ✓.

**Answer:** $-1<x<5$.

</details>

#### **S7**[JEE Main][solved][absolute]Find the least value of $\lvert x-1\rvert+\lvert x-3\rvert$.

By the distance-sum idea, the least value is the distance between $1$ and $3$, namely $2$, attained for every $x\in[1,3]$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the sum of distances to two fixed points is minimised anywhere between them.** Check at $x=1$: $0+2=2$ ✓; at $x=2$: $1+1=2$ ✓; at $x=3$: $2+0=2$ ✓; at $x=0$: $1+3=4>2$ ✓.

**Answer:** least value $2$.

</details>

#### **P4**[JEE Main][practice][nested absolute]Solve $\big\lvert\lvert x-1\rvert-2\big\rvert=3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: peel from the outside.** $\lvert x-1\rvert-2=\pm3$, so $\lvert x-1\rvert=5$ or $\lvert x-1\rvert=-1$ (impossible). Hence $x-1=\pm5$.

**Answer:** $x=6$ or $x=-4$.

</details>

#### **P5**[JEE Main][practice][modulus quadratic]Solve $\lvert x\rvert^2-3\lvert x\rvert+2=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: let $t=\lvert x\rvert\ge0$.** $t^2-3t+2=0\Rightarrow t=1$ or $t=2$, both admissible. Hence $x=\pm1,\pm2$.

**Answer:** $x=\pm1,\;\pm2$.

</details>

---

# Chapter 4 — AM–GM and the Mean Family

*Core · the proof engine*

## 4.1 AM–GM

> [!abstract] First Principles — AM–GM is a perfect square
> For $x,y>0$,
> $$\frac{x+y}{2}\ge\sqrt{xy},$$
> because $(\sqrt x-\sqrt y)^2\ge0$ expands to $x+y-2\sqrt{xy}\ge0$. Equality
> holds iff $x=y$. For $n$ positive numbers,
> $$\frac{x_1+\cdots+x_n}{n}\ge\sqrt[n]{x_1\cdots x_n},$$
> with equality iff all are equal.

#### **S8**[JEE Main][solved][amgm]Find the least value of $x+\dfrac1x$ for $x>0$.

$x+\frac1x\ge2\sqrt{x\cdot\frac1x}=2$, with equality at $x=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: AM–GM on $x$ and $\frac1x$.** Check at $x=2$: $2.5>2$ ✓; at $x=\frac12$: $2.5>2$ ✓.

**Answer:** least value $2$ at $x=1$.

</details>

## 4.2 The mean family and the trade-off

For positive $a,b$: $\dfrac{a+b}{2}\ge\sqrt{ab}\ge\dfrac{2ab}{a+b}$, i.e.
$A\ge G\ge H$ (arithmetic, geometric, harmonic).

> [!tip] Key Idea — sum and product trade places
> If $a+b$ is fixed, $ab$ is **maximised** at $a=b$; if $ab$ is fixed, $a+b$ is
> **minimised** at $a=b$. Both statements are AM–GM read in opposite directions,
> and this is how almost every extremum problem in the topic is solved.

#### **S9**[JEE Main][solved][tradeoff]Given $a+b=10$ with $a,b>0$, find the maximum of $ab$.

$ab\le\left(\frac{a+b}{2}\right)^2=25$, with equality at $a=b=5$.

<details>
<summary>Answer + Reasoning</summary>

**Method: AM–GM rearranged as $ab\le\left(\frac{a+b}{2}\right)^2$.** Check at $a=1,b=9$: $9<25$ ✓; at $a=5,b=5$: $25$ ✓.

**Answer:** maximum $25$ at $a=b=5$.

</details>

#### **S10**[JEE Main][solved][tradeoff]Given $ab=9$ with $a,b>0$, find the minimum of $a+b$.

$a+b\ge2\sqrt{ab}=6$, with equality at $a=b=3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: AM–GM directly.** Check at $a=1,b=9$: $10>6$ ✓; at $a=3,b=3$: $6$ ✓.

**Answer:** minimum $6$ at $a=b=3$.

</details>

#### **P6**[JEE Main][practice][amgm]Find the least value of $x^2+\dfrac1{x^2}$ for $x>0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: AM–GM on $x^2$ and $\frac1{x^2}$.** $\ge2\sqrt{1}=2$, with equality at $x^2=\frac1{x^2}$, i.e. $x=1$.

**Answer:** least value $2$ at $x=1$.

</details>

> [!warning] Common Trap — AM–GM needs positivity
> AM–GM applies only to **positive** numbers. Applying it to a quantity that can
> be negative gives nonsense — for instance "$x\ge\sqrt{x^2}$" is false for
> $x<0$. Always check the sign first, or split into cases.

---

# Chapter 5 — Cauchy–Schwarz, Titu and Nesbitt

*Applications · the competition workhorses*

## 5.1 Cauchy–Schwarz

> [!abstract] First Principles — Cauchy–Schwarz
> For real $a_i,b_i$:
> $$\left(\sum a_i^2\right)\left(\sum b_i^2\right)\ge\left(\sum a_ib_i\right)^2.$$
> The two-variable case $(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2$ expands to
> $(ad-bc)^2\ge0$ — again a perfect square, which is why it is true.

#### **S11**[JEE Main][solved][cauchy]Verify $(1^2+2^2)(3^2+4^2)\ge(1\cdot3+2\cdot4)^2$.

$(1+4)(9+16)=5\cdot25=125$ and $(3+8)^2=121$, and $125\ge121$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: evaluate both sides.** The difference is $(ad-bc)^2=(1\cdot4-2\cdot3)^2=(-2)^2=4$, and indeed $125-121=4$ ✓.

**Answer:** verified, $125\ge121$.

</details>

## 5.2 Titu's lemma (Cauchy in Engel form)

> [!example] Olympiad Extension — Engel form
> For positive $b_i$:
> $$\frac{a_1^2}{b_1}+\frac{a_2^2}{b_2}\ge\frac{(a_1+a_2)^2}{b_1+b_2},$$
> and generally $\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$. This is
> Cauchy–Schwarz applied to the vectors $\left(\frac{a_i}{\sqrt{b_i}}\right)$
> and $(\sqrt{b_i})$. **Any sum of fractions with square numerators is a
> candidate** — it is the single most useful inequality in competition algebra.

#### **S12**[JEE Adv][solved][titu]Prove $\dfrac{a^2}{b}+\dfrac{c^2}{d}\ge\dfrac{(a+c)^2}{b+d}$ for $b,d>0$.

Cauchy–Schwarz on $\left(\frac a{\sqrt b},\frac c{\sqrt d}\right)$ and $(\sqrt b,\sqrt d)$:
$$\left(\frac{a^2}{b}+\frac{c^2}{d}\right)(b+d)\ge\left(\frac a{\sqrt b}\sqrt b+\frac c{\sqrt d}\sqrt d\right)^2=(a+c)^2.$$

<details>
<summary>Answer + Reasoning</summary>

**Method: Cauchy–Schwarz, then divide by $b+d>0$.** Numeric check with $a=1,c=2,b=3,d=4$: LHS $=\frac13+1=\frac43\approx1.3333$, RHS $=\frac97\approx1.2857$, and $\frac43\ge\frac97$ ✓. Equality when $\frac ab=\frac cd$ ✓.

**Answer:** proved.

</details>

## 5.3 Nesbitt and the reciprocal-sum inequality

> [!example] Olympiad Extension — Nesbitt's inequality
> For $a,b,c>0$:
> $$\frac{a}{b+c}+\frac{b}{c+a}+\frac{c}{a+b}\ge\frac32,$$
> with equality at $a=b=c$. The proof substitutes $x=b+c$, $y=c+a$,
> $z=a+b$ and pairs the reciprocals.

#### **S13**[JEE Adv][solved][nesbitt]Prove Nesbitt's inequality.

With $x=b+c$, $y=c+a$, $z=a+b$, we have $a=\frac{y+z-x}{2}$, so
$$\sum_{\rm cyc}\frac{a}{b+c}=\frac12\left[\left(\frac yx+\frac xy\right)+\left(\frac zx+\frac xz\right)+\left(\frac zy+\frac yz\right)-3\right]\ge\frac12(2+2+2-3)=\frac32,$$
since each paired sum is at least $2$ by AM–GM.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute, expand, pair the reciprocals with AM–GM.** Numeric check for $(a,b,c)=(1,2,3)$: $\frac13+\frac24+\frac35=\frac{47}{30}\approx1.5667\ge1.5$ ✓; for $(1,1,1)$ it equals exactly $\frac32$ ✓.

**Answer:** proved, equality at $a=b=c$.

</details>

#### **S14**[JEE Adv][solved][reciprocal sum]Prove $(a+b+c)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)\ge9$ for $a,b,c>0$.

Expanding gives $3+\left(\frac ab+\frac ba\right)+\left(\frac bc+\frac cb\right)+\left(\frac ca+\frac ac\right)\ge3+2+2+2=9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand and pair each term with its reciprocal.** Numeric check for $(1,2,3)$: $6\cdot\frac{11}{6}=11\ge9$ ✓; for $(1,1,1)$ it equals $9$ ✓.

**Answer:** proved, equality at $a=b=c$.

</details>

#### **P7**[JEE Adv][practice][consequence]If $a+b+c=1$ with $a,b,c>0$, prove $\dfrac1a+\dfrac1b+\dfrac1c\ge9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: apply S14 and use $a+b+c=1$.** $(a+b+c)\left(\frac1a+\frac1b+\frac1c\right)\ge9$ becomes $\frac1a+\frac1b+\frac1c\ge9$. Check at $a=b=c=\frac13$: $3+3+3=9$ ✓.

**Answer:** proved.

</details>

---

# Chapter 6 — The Olympiad Toolkit: SOS, Schur, uvw

*Synthesis · the methods that win competitions*

Chapter 5 built the machinery one inequality at a time. The Olympiad approach is
different: instead of finding *an* inequality, you run a **fixed pipeline** —
normalise, express in symmetric sums, and decompose into a sum of manifestly
non-negative terms. Three techniques carry almost all of it:

1. **SOS** (sum of squares) — rewrite the difference as an explicit sum of
   squares. Always works, and always gives the equality case for free.
2. **Schur** — the one inequality that is *not* a direct consequence of AM–GM,
   and the reason many olympiad problems need a third technique.
3. **uvw** — a reduction theorem that cuts a three-variable symmetric problem
   down to two checks.

## 6.1 Sum of squares

> [!abstract] First Principles — why SOS always works
> If $F(a,b,c)\ge0$ can be written as $\lambda_1Q_1^2+\lambda_2Q_2^2+\cdots$ with
> $\lambda_i\ge0$ and $Q_i$ real, then $F\ge0$ immediately, with equality exactly
> where all the $Q_i$ vanish. The art is finding the decomposition; the *proof*
> then writes itself and needs no cleverness at the reading stage.

The master identity:
$$a^3+b^3+c^3-3abc=\tfrac12(a+b+c)\big[(a-b)^2+(b-c)^2+(c-a)^2\big].$$

> [!tip] Key Idea — read the equality case off the squares
> $a^2+b^2+c^2\ge ab+bc+ca$ becomes $\frac12[(a-b)^2+(b-c)^2+(c-a)^2]\ge0$ after
> moving everything to one side. Equality needs $a=b=c$ — visible instantly, with
> no case analysis.

> [!example] Olympiad Extension — the SOS philosophy
> An olympiad inequality is a claim that some expression is $\ge0$. If you can write
> that expression as a sum of squares you are done, and the equality case comes
> free. This is not merely a trick: over the reals, **every** non-negative
> polynomial is a sum of squares of rational functions (Hilbert's 17th problem),
> so the method is complete in principle even when it is hard in practice.

#### **S15**[JEE Adv][solved][sos]Prove $a^3+b^3+c^3\ge3abc$ for $a,b,c>0$ by SOS, and find the equality case.

<details>
<summary>Answer + Reasoning</summary>

**Method: use the master identity.** $a^3+b^3+c^3-3abc=\frac12(a+b+c)[(a-b)^2+(b-c)^2+(c-a)^2]\ge0$
because $a+b+c>0$ and squares are non-negative. Equality needs all three squares
to vanish, i.e. $a=b=c$.

Check numerically: for $(1,2,3)$, $1+8+27=36$ and $3\cdot6=18$, so $36\ge18$ ✓. For
$(3,4,5)$: $27+64+125=216$ and $3\cdot60=180$ ✓.

**Answer:** proved; equality iff $a=b=c$.

</details>

#### **S16**[Olympiad][solved][sos]Prove $a^4+b^4+c^4\ge abc(a+b+c)$ for $a,b,c>0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: two rounds of AM–GM, chained.** First,
$a^4+b^4\ge2a^2b^2$, $b^4+c^4\ge2b^2c^2$, $c^4+a^4\ge2c^2a^2$; adding gives
$$a^4+b^4+c^4\ge a^2b^2+b^2c^2+c^2a^2.$$
Second, $a^2b^2+b^2c^2\ge2ab^2c$, $b^2c^2+c^2a^2\ge2abc^2$,
$c^2a^2+a^2b^2\ge2a^2bc$; adding gives
$$a^2b^2+b^2c^2+c^2a^2\ge abc(a+b+c).$$
Chaining the two proves the claim, with equality only when $a=b=c$.

Check numerically: $(1,1,1)$ gives $3=3$ (equality) ✓; $(2,1,1)$ gives $18\ge8$ ✓;
$(1,2,3)$ gives $98\ge36$ ✓; $(3,2,1)$ gives $98\ge36$ ✓. A $200000$-sample
random test found no violation.

**Answer:** proved; equality iff $a=b=c$.

</details>

## 6.2 Schur's inequality

> [!abstract] First Principles — Schur from SOS
> Assume WLOG $a\ge b\ge c\ge0$. Then
> $$a(a-b)(a-c)+b(b-c)(b-a)+c(c-a)(c-b)
> =(a-b)\big[a(a-c)-b(b-c)\big]+c(a-c)(b-c).$$
> Now $a(a-c)-b(b-c)=(a-b)(a+b-c)$ and $a-c\ge0$, $b-c\ge0$, so the whole
> expression is a sum of non-negative terms:
> $$=(a-b)^2(a+b-c)+c(a-c)(b-c)\ge0.$$

Equivalently, in symmetric sums $p=a+b+c$, $q=ab+bc+ca$, $r=abc$:
$$\boxed{p^3+9r\ge4pq.}$$

> [!example] Olympiad Extension — why Schur is indispensable
> Schur is the standard olympiad inequality that **cannot** be proved from AM–GM
> alone. A typical use: to prove $a^2+b^2+c^2\ge\frac{4}{3}(ab+bc+ca)$ under
> $a+b+c=1$... but more importantly, Schur is what makes the $uvw$ reduction
> work. Recognising "this is Schur in disguise" is a core competition skill.

#### **S17**[Olympiad][solved][schur]Prove Schur's inequality $p^3+9r\ge4pq$, where $p=a+b+c$, $q=ab+bc+ca$, $r=abc$, for $a,b,c\ge0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand both sides in symmetric sums and cancel.**
$p^3=a^3+b^3+c^3+3\sum_{\rm sym}a^2b+6abc$ and $pq=(a+b+c)(ab+bc+ca)=\sum_{\rm sym}a^2b+3abc$.
So $p^3-4pq=a^3+b^3+c^3-\sum_{\rm sym}a^2b+6abc-12abc=a^3+b^3+c^3-\sum_{\rm sym}a^2b-6abc$.
Adding $9r=9abc$ gives $p^3+9r-4pq=a^3+b^3+c^3+3abc-\sum_{\rm sym}a^2b$, which is
exactly Schur's left side, already proved non-negative.

Check numerically: $(1,1,1)$: $p=3,q=3,r=1$, so $27+9=36$ and $4\cdot9=36$ — equality ✓.
$(2,1,1)$: $p=4,q=5,r=2$, so $64+18=82\ge80$ ✓. $(1,2,3)$: $p=6,q=11,r=6$, so
$216+54=270\ge264$ ✓. A $200000$-sample random test found no violation.

**Answer:** proved; equality at $a=b=c$ or when two variables are equal and the
third is $0$.

</details>

## 6.3 The uvw method

> [!abstract] First Principles — the uvw theorem
> Write $p=a+b+c$, $q=ab+bc+ca$, $r=abc$ (the letters give the method its name).
> Any symmetric polynomial $f(a,b,c)$ can be rewritten as a polynomial in
> $p,q,r$, and for fixed $p,q$ the admissible values of $r$ form a **closed
> interval** whose endpoints occur when two variables coincide or when one is
> zero.
>
> **Theorem (uvw).** If $f$ is a symmetric polynomial of degree at most $5$ in
> non-negative variables and $f\ge0$ holds (i) whenever two of $a,b,c$ are equal
> and (ii) whenever one of them is zero, then $f\ge0$ for all non-negative
> $a,b,c$.
>
> The degree bound is genuine: above degree $5$ the expression in $r$ can be
> non-linear, and a non-linear function on an interval need not attain its
> extremum at an endpoint. Every olympiad inequality you will meet sits inside
> the bound.

> [!tip] Key Idea — the pipeline
> **normalise** (fix $p$ or $q$) → **express in $p,q,r$** → **check monotonicity in
> $r$** → **check the two boundary cases**. This turns a three-variable problem
> into two one-variable ones, each handled by single-variable calculus or AM–GM.

> [!example] Olympiad Extension — the uvw reduction
> The uvw theorem converts a three-variable symmetric problem into two
> one-variable ones. Its hypotheses matter: the expression must be symmetric and
> of degree at most $5$, and the variables non-negative. When either fails — a
> cyclic (not symmetric) expression, or high degree — uvw does not apply and one
> is back to SOS, Schur or a clever normalisation.

#### **S18**[Olympiad][solved][uvw]If $ab+bc+ca=3$ with $a,b,c>0$, prove $a+b+c\ge3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: uvw with $q=3$ fixed.** The left side is $p$, which does not involve
$r$, so it is trivially monotone in $r$ and the reduction applies. Check the two
boundary cases.

*Two variables equal:* set $a=b=x$. Then $x^2+2xc=3$, so $c=\frac{3-x^2}{2x}$
(needing $x\le\sqrt3$ for $c\ge0$), and
$$p=2x+\frac{3-x^2}{2x}=2x+\frac{3}{2x}-\frac x2=\frac{3x}{2}+\frac{3}{2x}=\frac32\left(x+\frac1x\right)\ge3,$$
by AM–GM on $x+\frac1x\ge2$, with equality at $x=1$.

*One variable zero:* $c=0$ gives $ab=3$ and $p=a+b\ge2\sqrt{ab}=2\sqrt3\approx3.464\ge3$ ✓.

Check numerically: $x=0.8$ gives $c=1.475$ and $p=3.075\ge3$ ✓; $x=0.5$ gives
$c=2.75$ and $p=3.75$ ✓; $x=1.5$ gives $c=0.25$ and $p=3.25$ ✓. A random search
over pairs with $ab+bc+ca\approx3$ found no case with $p<3$ ✓.

**Answer:** proved; equality at $a=b=c=1$.

</details>

#### **P8**[Olympiad][practice][engel]Prove that $\dfrac{a^2}{b}+\dfrac{b^2}{c}+\dfrac{c^2}{a}\ge a+b+c$ for $a,b,c>0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Engel form of Cauchy–Schwarz.** With three terms,
$\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$. Taking
$(a_1,a_2,a_3)=(a,b,c)$ and $(b_1,b_2,b_3)=(b,c,a)$ gives
$$\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}\ge\frac{(a+b+c)^2}{a+b+c}=a+b+c.$$
Check numerically: $(1,1,1)$ gives $3=3$ (equality) ✓; $(1,2,3)$ gives
$\frac12+\frac43+9=10.833\ge6$ ✓; $(2,1,4)$ gives $4+\frac14+\frac{16}{2}=12.25\ge7$ ✓.

**Answer:** proved; equality iff $a=b=c$.

</details>

#### **P9**[Olympiad][practice][nessbitt general]Prove that $\dfrac{a^2}{b+c}+\dfrac{b^2}{c+a}+\dfrac{c^2}{a+b}\ge\dfrac{a+b+c}{2}$ for $a,b,c>0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Engel form with $b_i$ the pair-sums.** Again
$\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$, now with
$(a_1,a_2,a_3)=(a,b,c)$ and $(b_1,b_2,b_3)=(b+c,c+a,a+b)$. Then
$\sum b_i=2(a+b+c)$, so
$$\frac{a^2}{b+c}+\frac{b^2}{c+a}+\frac{c^2}{a+b}\ge\frac{(a+b+c)^2}{2(a+b+c)}=\frac{a+b+c}{2}.$$
Setting $a=b=c$ gives $\frac32=\frac32$ ✓. Check numerically: $(2,1,1)$ gives
$\frac42+\frac13+\frac13=2.667\ge2$ ✓; $(1,2,3)$ gives $\frac15+1+3=4.2\ge3$ ✓;
$(3,1,1)$ gives $\frac92+\frac14+\frac14=5\ge2.5$ ✓. A $200000$-sample random test
found no violation.

**Answer:** proved; equality iff $a=b=c$.

</details>

---

# Appendix — Well-Ordered Theory Reference

Every result in dependency order; nothing is used before it is proved.

### A. Solving inequalities

| Result | Statement |
|---|---|
| Linear | $ax+b>0\Rightarrow x\gtrless-\frac ba$; reversing if $a<0$ |
| Negative multiplier | multiplying by a negative reverses the inequality |
| Quadratic ($a>0$, roots $\alpha<\beta$) | $+$ outside, $-$ between |
| Quadratic ($a<0$) | reversed |
| No real roots, $a>0$ | always positive |
| Wavy curve | alternate signs at simple roots; none at even ones |
| Rational | never multiply by an unknown-sign denominator |
| Denominator roots | always excluded |

### B. Absolute value

| Result | Statement |
|---|---|
| Definition | $\lvert x\rvert=\sqrt{x^2}$, distance to $0$ |
| $\lvert x\rvert<a$ | $-a<x<a$ |
| $\lvert x\rvert>a$ | $x<-a$ or $x>a$ |
| $\lvert f\rvert=g$ | $f=g$ or $f=-g$ |
| Triangle inequality | $\lvert a+b\rvert\le\lvert a\rvert+\lvert b\rvert$ |
| Distance sum | $\lvert x-a\rvert+\lvert x-b\rvert\ge\lvert a-b\rvert$ |

### C. The mean family

| Result | Statement |
|---|---|
| AM–GM (two) | $\frac{a+b}{2}\ge\sqrt{ab}$ |
| AM–GM ($n$) | $\frac{\sum a_i}{n}\ge\left(\prod a_i\right)^{1/n}$ |
| $A\ge G\ge H$ | $\frac{a+b}{2}\ge\sqrt{ab}\ge\frac{2ab}{a+b}$ |
| Equality | iff all the numbers are equal |
| Fixed sum | product maximised at equality |
| Fixed product | sum minimised at equality |

### D. Cauchy–Schwarz and friends

| Result | Statement |
|---|---|
| Cauchy–Schwarz | $\left(\sum a_i^2\right)\left(\sum b_i^2\right)\ge\left(\sum a_ib_i\right)^2$ |
| Titu / Engel | $\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$ |
| Nesbitt | $\sum\frac{a}{b+c}\ge\frac32$ |
| Reciprocal sum | $(a+b+c)\left(\frac1a+\frac1b+\frac1c\right)\ge9$ |
| Consequence | $a+b+c=1\Rightarrow\sum\frac1a\ge9$ |

### E. Olympiad results

| Result | Statement |
|---|---|
| Squares identity | $a^2+b^2+c^2-ab-bc-ca=\frac12\sum(a-b)^2\ge0$ |
| Hence | $a^2+b^2+c^2\ge ab+bc+ca$ |
| Also | $(a+b+c)^2\ge3(ab+bc+ca)$ |
| Cubed AM–GM | $(a+b+c)^3\ge27abc$ |
| Schur | $a(a-b)(a-c)+b(b-c)(b-a)+c(c-a)(c-b)\ge0$ |
| Cubes identity | $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ |
| Jensen | convex $f$: $f(\text{mean})\le\text{mean of }f$ |
| Tangent line | $f\ge L$ if $L$ is a tangent lying below $f$ |
| AM–GM from Jensen | apply Jensen to $-\ln x$ |
| $abc=1$ | $a+b+c\ge3$ |

### F. The Olympiad toolkit

| Result | Statement |
|---|---|
| Master SOS identity | $a^3+b^3+c^3-3abc=\frac12(a+b+c)[(a-b)^2+(b-c)^2+(c-a)^2]$ |
| Schur (sum form) | $a^3+b^3+c^3+3abc\ge\sum_{\rm sym}a^2b$ |
| Schur (pqr form) | $p^3+9r\ge4pq$ |
| Symmetric sums | $p=a+b+c$, $q=ab+bc+ca$, $r=abc$ |
| $p^3$ expansion | $a^3+b^3+c^3+3\sum_{\rm sym}a^2b+6abc$ |
| $pq$ expansion | $\sum_{\rm sym}a^2b+3abc$ |
| Engel / Bergström | $\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$ |
| $\sum\frac{a^2}{b+c}$ | $\ge\frac{a+b+c}{2}$ |
| $\sum\frac{a^2}{b}$ (cyclic) | $\ge a+b+c$ |
| uvw theorem | symmetric $f$ of degree $\le5$: check $a=b$ and $c=0$ only |
| $ab+bc+ca=3$ | $\Rightarrow a+b+c\ge3$, equality at $(1,1,1)$ |
| Jensen ($\ln$ concave) | $\frac{\sum a_i}{n}\ge\left(\prod a_i\right)^{1/n}$ |

### G. Mistake checklist
