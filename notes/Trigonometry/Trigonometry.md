---
title: "Trigonometry — Complete Notes"
aliases: ["Trigonometry", "Trig", "Trigonometry"]
module: "Trigonometry"
type: notes
tags: [trigonometry, module, complete, algebra, geometry]
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 📝 [[Trigonometry — Paper|Olympiad Paper]] · ✅ [[Trigonometry — Solutions|Solutions]]

# Trigonometry

Trigonometry is the study of the six ratios built from a right-angled triangle,
and then of the *periodic functions* they become when the angle is allowed to
grow without bound. Two ideas run through the whole subject.

The first is that **everything reduces to sine and cosine** — $\tan=\sin/\cos$,
$\sec=1/\cos$, and every identity in the subject is ultimately a statement about
$\sin$ and $\cos$. The second is the **unit circle**: it converts "angle" into
"arc length" and makes the general solution of a trigonometric equation
completely mechanical.

The payoff is broad. Trigonometry is the language of periodic phenomena, of
vectors and rotations, and — through the sine and cosine rules — of every
triangle that is not right-angled.

`6 chapters` `worked examples (S) + practice (P)` `SVG + Mermaid diagrams` `34-question Olympiad paper + full solutions`

### ★ How to use these notes

**Read in order.** Chapters 1–2 fix the identities and the compound-angle
formulae — these are the tools everything else is built from. Chapter 3 is the
multiple-angle family, Chapter 4 is the transformation formulae (product ↔ sum),
Chapter 5 is trigonometric *equations*, and Chapter 6 is triangles plus the
Olympiad frontier.

- **Callouts** — `[!abstract]` First Principles = the derivation; `[!tip]` Key
  Idea = the takeaway; `[!warning]` Common Trap = the classic mistake;
  `[!example]` Olympiad Extension = the frontier version.
- **Numeric habit** — every numeric answer in this module was verified in pure
  Python before it was written, and each is accompanied by a check.

### ▣ The roadmap

| Ch | Title | Level |
|---|---|---|
| 1 | Ratios, identities and signs | foundations |
| 2 | Compound angles | machinery |
| 3 | Multiple and submultiple angles | machinery |
| 4 | Transformation formulae and sums | applications |
| 5 | Trigonometric equations | core |
| 6 | Properties of triangles & the Olympiad frontier | synthesis |

**Fig 1.1 — the unit circle and the signs.** The coordinates of a point on the
unit circle are $(\cos\theta,\sin\theta)$. The sign of each ratio is fixed by
the quadrant, and the four allied-angle rules follow by symmetry about the axes.

![Fig 1.1 — the unit circle, quadrants and signs](assets/fig-01.svg)

**Fig 1.2 — the general solution on the circle.** $\sin\theta=\frac12$ has two
solutions in $[0,2\pi)$ — and then repeats every $2\pi$. The unit circle turns
"find all solutions" into "read the two angles and add $2n\pi$".

![Fig 1.2 — reading the general solution off the unit circle](assets/fig-02.svg)

---

# Chapter 1 — Ratios, Identities and Signs

*Foundations · six numbers and how they hang together*

## 1.1 The six ratios

For a right-angled triangle with angle $\theta$, opposite $O$, adjacent $A$,
hypotenuse $H$:
$$\sin\theta=\frac OH,\quad\cos\theta=\frac AH,\quad\tan\theta=\frac OA,$$
$$\csc\theta=\frac HO,\quad\sec\theta=\frac HA,\quad\cot\theta=\frac AO.$$

> [!abstract] First Principles — the unit circle generalises everything
> On the unit circle, a point at angle $\theta$ from the positive $x$-axis has
> coordinates $(\cos\theta,\sin\theta)$. This defines $\sin$ and $\cos$ for *all*
> real $\theta$ (not just acute angles), makes them periodic with period $2\pi$,
> and gives the fundamental identity
> $$\sin^2\theta+\cos^2\theta=1$$
> immediately, as the equation of the unit circle.

## 1.2 The identities

> [!tip] Key Idea — two families, and everything follows
> **Pythagorean:** $\sin^2\theta+\cos^2\theta=1$, $1+\tan^2\theta=\sec^2\theta$,
> $1+\cot^2\theta=\csc^2\theta$.
> **Reciprocal:** $\sin\theta\csc\theta=1$, $\cos\theta\sec\theta=1$,
> $\tan\theta\cot\theta=1$, and $\tan\theta=\frac{\sin\theta}{\cos\theta}$.

#### **S1**[JEE Main][solved][identity]Verify $\sin^2 30^\circ+\cos^2 30^\circ=1$.

$\left(\frac12\right)^2+\left(\frac{\sqrt3}{2}\right)^2=\frac14+\frac34=1$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute the standard values.** The identity holds for every angle, not just $30^\circ$ ✓.

**Answer:** verified, $=1$.

</details>

## 1.3 Signs and allied angles

| Quadrant | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|
| I ($0$–$90^\circ$) | $+$ | $+$ | $+$ |
| II | $+$ | $-$ | $-$ |
| III | $-$ | $-$ | $+$ |
| IV | $-$ | $+$ | $-$ |

> [!abstract] First Principles — the allied-angle rules
> These follow from symmetry about the axes:
> $$\sin(90^\circ-\theta)=\cos\theta,\quad \cos(90^\circ-\theta)=\sin\theta,$$
> $$\sin(90^\circ+\theta)=\cos\theta,\quad \cos(90^\circ+\theta)=-\sin\theta,$$
> $$\sin(180^\circ-\theta)=\sin\theta,\quad \cos(180^\circ-\theta)=-\cos\theta,$$
> $$\sin(180^\circ+\theta)=-\sin\theta,\quad \cos(180^\circ+\theta)=-\cos\theta,$$
> $$\sin(270^\circ-\theta)=-\cos\theta,\quad \sin(270^\circ+\theta)=-\cos\theta.$$
> **Odd multiples of $90^\circ$ swap sine and cosine; even multiples change only signs.**

#### **S2**[JEE Main][solved][allied]Evaluate $\sin135^\circ$ and $\cos225^\circ$.

$\sin135^\circ=\sin(180^\circ-45^\circ)=\sin45^\circ=\frac{\sqrt2}{2}$; $\cos225^\circ=\cos(180^\circ+45^\circ)=-\cos45^\circ=-\frac{\sqrt2}{2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: allied-angle rules.** Check numerically: $\sin135^\circ\approx0.7071$ and $\cos225^\circ\approx-0.7071$ ✓.

**Answer:** $\dfrac{\sqrt2}{2}$ and $-\dfrac{\sqrt2}{2}$.

</details>

#### **P1**[JEE Main][practice][standard values]Evaluate $\sin75^\circ$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\sin75^\circ=\sin(45^\circ+30^\circ)$.** $\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}+\frac{\sqrt2}{2}\cdot\frac12=\frac{\sqrt6+\sqrt2}{4}$.

**Answer:** $\dfrac{\sqrt6+\sqrt2}{4}\approx0.9659$.

</details>

---

# Chapter 2 — Compound Angles

*Machinery · the four formulae that generate everything*

## 2.1 The formulae

> [!abstract] First Principles — the addition formulae
> $$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B,$$
> $$\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B,$$
> $$\tan(A\pm B)=\frac{\tan A\pm\tan B}{1\mp\tan A\tan B}.$$
> The sine formula keeps the sign; the cosine formula *flips* it. The tangent
> formula is just the sine formula divided by the cosine formula.

#### **S3**[JEE Main][solved][compound]Evaluate $\tan(45^\circ+60^\circ)$.

$\dfrac{1+\sqrt3}{1-\sqrt3}=\dfrac{(1+\sqrt3)^2}{1-3}=-\dfrac{4+2\sqrt3}{2}=-(2+\sqrt3)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the tangent addition formula.** Check: $\tan105^\circ\approx-3.7321$ and $-(2+\sqrt3)\approx-3.7321$ ✓.

**Answer:** $-(2+\sqrt3)\approx-3.7321$.

</details>

> [!warning] Common Trap — the sign flip in $\cos(A-B)$
> $\cos(A-B)=\cos A\cos B+\sin A\sin B$ — the **plus** sign, unlike the sine
> formula. Getting this wrong is the most common error in the chapter.

#### **S4**[JEE Main][solved][compound]Verify $\cos(60^\circ-30^\circ)=\cos30^\circ$ using the formula.

$\cos60^\circ\cos30^\circ+\sin60^\circ\sin30^\circ=\frac12\cdot\frac{\sqrt3}{2}+\frac{\sqrt3}{2}\cdot\frac12=\frac{\sqrt3}{2}=\cos30^\circ$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: the cosine subtraction formula, with the plus sign between the products.** ✓

**Answer:** verified, $\dfrac{\sqrt3}{2}$.

</details>

#### **P2**[JEE Main][practice][compound]If $\sin A=\frac35$ and $\cos B=\frac5{13}$ with $A,B$ acute, find $\sin(A+B)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: find the missing cosines by Pythagoras, then apply the formula.** $\cos A=\frac45$, $\sin B=\frac{12}{13}$. So $\sin(A+B)=\frac35\cdot\frac5{13}+\frac45\cdot\frac{12}{13}=\frac{15}{65}+\frac{48}{65}=\frac{63}{65}$.

**Answer:** $\dfrac{63}{65}$.

</details>

---

# Chapter 3 — Multiple and Submultiple Angles

*Machinery · setting $A=B$ and $B=A/2$*

## 3.1 Double angles

> [!abstract] First Principles — put $A=B$ in the compound formulae
> $$\sin2A=2\sin A\cos A,$$
> $$\cos2A=\cos^2A-\sin^2A=2\cos^2A-1=1-2\sin^2A,$$
> $$\tan2A=\frac{2\tan A}{1-\tan^2A}.$$
> The three forms of $\cos2A$ are not redundant: each is the natural one for a
> different substitution.

#### **S5**[JEE Main][solved][double]Verify $\sin60^\circ=2\sin30^\circ\cos30^\circ$.

$2\cdot\frac12\cdot\frac{\sqrt3}{2}=\frac{\sqrt3}{2}=\sin60^\circ$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $A=30^\circ$ into $\sin2A=2\sin A\cos A$.** ✓

**Answer:** verified.

</details>

#### **S6**[JEE Main][solved][double]Verify $\tan60^\circ=\dfrac{2\tan30^\circ}{1-\tan^2 30^\circ}$.

$\dfrac{2/\sqrt3}{1-1/3}=\dfrac{2/\sqrt3}{2/3}=\dfrac{3}{\sqrt3}=\sqrt3=\tan60^\circ$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $A=30^\circ$.** Note the denominator $1-\tan^2A$ vanishes when $A=45^\circ$, which is exactly why $\tan90^\circ$ is undefined ✓.

**Answer:** verified, $=\sqrt3$.

</details>

## 3.2 Triple angles and half angles

> [!tip] Key Idea — derive, don't memorise
> $\sin3A=3\sin A-4\sin^3A$ and $\cos3A=4\cos^3A-3\cos A$ both come from
> expanding $\sin(2A+A)$ and $\cos(2A+A)$. Re-deriving them takes ten seconds
> and cannot be forgotten.

The **half-angle** formulae come from the double-angle forms solved for
$\sin\frac A2$ and $\cos\frac A2$:
$$\sin\frac A2=\pm\sqrt{\frac{1-\cos A}{2}},\qquad\cos\frac A2=\pm\sqrt{\frac{1+\cos A}{2}},$$
$$\tan\frac A2=\frac{1-\cos A}{\sin A}=\frac{\sin A}{1+\cos A}=\pm\sqrt{\frac{1-\cos A}{1+\cos A}}.$$

#### **S7**[JEE Main][solved][triple]Verify $\sin90^\circ=3\sin30^\circ-4\sin^3 30^\circ$.

$3\cdot\frac12-4\cdot\frac18=\frac32-\frac12=1=\sin90^\circ$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute $A=30^\circ$ into $\sin3A=3\sin A-4\sin^3A$.** ✓

**Answer:** verified, $=1$.

</details>

#### **S8**[JEE Main][solved][half angle]Verify $\sin30^\circ=\sqrt{\dfrac{1-\cos60^\circ}{2}}$.

$\sqrt{\frac{1-\frac12}{2}}=\sqrt{\frac14}=\frac12=\sin30^\circ$ ✓.

<details>
<summary>Answer + Reasoning</summary>

**Method: the half-angle formula with $A=60^\circ$, taking the positive root since $30^\circ$ is in the first quadrant.** ✓

**Answer:** verified.

</details>

> [!warning] Common Trap — the half-angle sign is not optional
> The $\pm$ must be resolved from the quadrant of $\frac A2$. For $A=60^\circ$,
> $\frac A2=30^\circ$ is in quadrant I, so the root is positive; for
> $A=420^\circ$, $\frac A2=210^\circ$ is in quadrant III and the root is
> negative.

#### **P3**[JEE Main][practice][double angle]If $\cos A=\frac35$ with $A$ acute, find $\cos2A$ and $\sin2A$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\cos2A=2\cos^2A-1$; $\sin A=\frac45$ so $\sin2A=2\sin A\cos A$.** $\cos2A=2\cdot\frac9{25}-1=-\frac7{25}$; $\sin2A=2\cdot\frac45\cdot\frac35=\frac{24}{25}$.

**Answer:** $\cos2A=-\dfrac7{25}$, $\sin2A=\dfrac{24}{25}$.

</details>

---

# Chapter 4 — Transformation Formulae and Sums

*Applications · product ↔ sum, and what it buys*

## 4.1 The four formulae

> [!abstract] First Principles — add and subtract the compound formulae
> Adding and subtracting $\sin(A+B)$ and $\sin(A-B)$ cancels one product:
> $$2\sin A\cos B=\sin(A+B)+\sin(A-B),$$
> $$2\cos A\sin B=\sin(A+B)-\sin(A-B),$$
> $$2\cos A\cos B=\cos(A+B)+\cos(A-B),$$
> $$2\sin A\sin B=\cos(A-B)-\cos(A+B).$$
> Reversing these (with $C=A+B$, $D=A-B$) gives the **sum-to-product** forms.

#### **S9**[JEE Main][solved][sum to product]Evaluate $\sin75^\circ+\sin15^\circ$.

$2\sin45^\circ\cos30^\circ=2\cdot\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}=\frac{\sqrt6}{2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\sin C+\sin D=2\sin\frac{C+D}{2}\cos\frac{C-D}{2}$.** Check directly: $0.9659+0.2588=1.2247$ and $\frac{\sqrt6}{2}\approx1.2247$ ✓.

**Answer:** $\dfrac{\sqrt6}{2}\approx1.2247$.

</details>

#### **S10**[JEE Main][solved][difference of cosines]Evaluate $\cos75^\circ-\cos15^\circ$.

$-2\sin45^\circ\sin30^\circ=-2\cdot\frac{\sqrt2}{2}\cdot\frac12=-\frac{\sqrt2}{2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\cos C-\cos D=-2\sin\frac{C+D}{2}\sin\frac{C-D}{2}$.** Check directly: $0.2588-0.9659=-0.7071$ and $-\frac{\sqrt2}{2}\approx-0.7071$ ✓.

**Answer:** $-\dfrac{\sqrt2}{2}\approx-0.7071$.

</details>

> [!tip] Key Idea — what transformation formulae are *for*
> They turn **products** of sines and cosines into **sums**, and a sum of terms
> with arguments in arithmetic progression **telescopes**. That is how the closed
> forms $\sum_{k=1}^n\sin k\theta=\frac{\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac{\theta}{2}}$ and its cosine analogue are proved.

#### **S11**[Olympiad][solved][series]Find $\displaystyle\sum_{k=1}^{n}\sin(k\theta)$.

Multiply by $2\sin\frac\theta2$ and use $2\sin\frac\theta2\sin k\theta=\cos\left(k-\frac12\right)\theta-\cos\left(k+\frac12\right)\theta$; the sum telescopes to $\cos\frac\theta2-\cos\left(n+\frac12\right)\theta$, so
$$\sum_{k=1}^{n}\sin(k\theta)=\frac{\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac\theta2}.$$

<details>
<summary>Answer + Reasoning</summary>

**Method: the $2\sin\frac\theta2$ multiplier trick, then telescope.** Numeric check for $n=90$, $\theta=1^\circ$: the direct sum and the closed form agree to $10^{-6}$ ✓.

**Answer:** $\dfrac{\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac\theta2}$.

</details>

#### **P4**[JEE Adv][practice][product to sum]Express $2\sin45^\circ\cos30^\circ$ as a sum, and verify.

<details>
<summary>Answer + Reasoning</summary>

**Method: $2\sin A\cos B=\sin(A+B)+\sin(A-B)$.** $=\sin75^\circ+\sin15^\circ$. Check: $2\cdot0.7071\cdot0.8660=1.2247$ and $0.9659+0.2588=1.2247$ ✓.

**Answer:** $\sin75^\circ+\sin15^\circ$.

</details>

---

# Chapter 5 — Trigonometric Equations

*Core · all solutions, not just one*

## 5.1 Principal and general solutions

> [!abstract] First Principles — read the solutions off the unit circle
> Because sine and cosine are periodic with period $2\pi$, every equation has
> infinitely many solutions. The **principal solution** lies in $[0,2\pi)$; the
> **general solution** adds $2n\pi$ (or $n\pi$ for tangent, whose period is $\pi$).
>
> | Equation | General solution |
> |---|---|
> | $\sin\theta=\sin\alpha$ | $\theta=n\pi+(-1)^n\alpha$ |
> | $\cos\theta=\cos\alpha$ | $\theta=2n\pi\pm\alpha$ |
> | $\tan\theta=\tan\alpha$ | $\theta=n\pi+\alpha$ |

#### **S12**[JEE Main][solved][general]Solve $\sin x=\frac12$ generally.

$\sin x=\sin30^\circ$, so $x=n\pi+(-1)^n\cdot30^\circ$. In degrees: $x=n180^\circ+(-1)^n30^\circ$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\sin\theta=\sin\alpha\Rightarrow\theta=n\pi+(-1)^n\alpha$.** Check: $n=0$ gives $30^\circ$ ✓; $n=1$ gives $180^\circ-30^\circ=150^\circ$ ✓; $n=2$ gives $360^\circ+30^\circ=390^\circ$, and $\sin390^\circ=\frac12$ ✓.

**Answer:** $x=n\pi+(-1)^n\dfrac\pi6$.

</details>

#### **S13**[JEE Main][solved][general]Solve $\tan x=1$ generally, and $\cos x=\frac12$ generally.

$\tan x=\tan45^\circ\Rightarrow x=n\pi+\frac\pi4$. $\cos x=\cos60^\circ\Rightarrow x=2n\pi\pm\frac\pi3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the two remaining standard forms.** Check $\tan(225^\circ)=1$ ✓ and $\cos(300^\circ)=\frac12$ ✓.

**Answer:** $x=n\pi+\dfrac\pi4$; $x=2n\pi\pm\dfrac\pi3$.

</details>

## 5.2 Methods

> [!tip] Key Idea — always factorise
> Convert the equation to $\prod(\text{factor})=0$ and solve each factor with
> the standard forms. The two commonest conversions are
> $\sin x-\sin y=2\cos\frac{x+y}{2}\sin\frac{x-y}{2}$ and
> $a\sin x+b\cos x=\sqrt{a^2+b^2}\sin(x+\varphi)$ with
> $\tan\varphi=\frac ba$.

#### **S14**[JEE Adv][solved][factorise]Solve $\sin2x=\cos x$.

$2\sin x\cos x=\cos x$, so $\cos x(2\sin x-1)=0$. Hence $\cos x=0$ or $\sin x=\frac12$, giving $x=\frac\pi2+n\pi$ or $x=n\pi+(-1)^n\frac\pi6$.

<details>
<summary>Answer + Reasoning</summary>

**Method: bring everything to one side and factor out $\cos x$ — do not divide by it.** In $[0,2\pi)$ the four solutions are $\frac\pi6,\frac\pi2,\frac{5\pi}6,\frac{3\pi}2$ ✓ (all four satisfy $\sin2x=\cos x$).

**Answer:** $x=\dfrac\pi2+n\pi$ or $x=n\pi+(-1)^n\dfrac\pi6$.

</details>

> [!warning] Common Trap — never divide by a trigonometric factor
> Dividing $\sin2x=\cos x$ by $\cos x$ loses the solutions where $\cos x=0$.
> Always factorise instead; the lost solutions are exactly the ones that appear
> in the "easy" case.

#### **P5**[JEE Main][practice][count]How many solutions does $\sin x=\frac12$ have in $[0,2\pi)$?

<details>
<summary>Answer + Reasoning</summary>

**Method: the unit circle cuts the horizontal line $y=\frac12$ twice in one revolution.** They are $\frac\pi6$ and $\frac{5\pi}6$.

**Answer:** $2$.

</details>

---

# Chapter 6 — The Olympiad Identities

*Synthesis · where angles stop being independent*

Everything up to now treats $A$ and $B$ as independent. The Olympiad content
begins the moment they are **linked** — most often by $A+B+C=180^\circ$ in a
triangle, or by $n\theta$ being a multiple of $2\pi$. Those constraints collapse
whole families of expressions into exact values, and the two tools that do the
collapsing are the **$A+B+C=\pi$ identities** and the **roots-of-unity**
argument behind products of sines.

## 6.1 The $A+B+C=\pi$ family

> [!abstract] First Principles — one constraint, many identities
> If $A+B+C=\pi$ then $C=\pi-(A+B)$, and every function of $C$ can be rewritten
> using $A+B$: $\sin C=\sin(A+B)$, $\cos C=-\cos(A+B)$,
> $\tan C=-\tan(A+B)$. Substituting the addition formulae and simplifying gives
> the whole family at once.

| Identity | Statement |
|---|---|
| Cosines squared | $\cos^2A+\cos^2B+\cos^2C+2\cos A\cos B\cos C=1$ |
| Sines squared | $\sin^2A+\sin^2B+\sin^2C=2+2\cos A\cos B\cos C$ |
| Sines | $\sin A+\sin B+\sin C=4\cos\frac A2\cos\frac B2\cos\frac C2$ |
| Double angles | $\sin2A+\sin2B+\sin2C=4\sin A\sin B\sin C$ |
| Tangents | $\tan A+\tan B+\tan C=\tan A\tan B\tan C$ |
| Half-angle tangents | $\tan\frac A2\tan\frac B2+\tan\frac B2\tan\frac C2+\tan\frac C2\tan\frac A2=1$ |

> [!tip] Key Idea — the tangent identity is the most useful
> $\tan A+\tan B+\tan C=\tan A\tan B\tan C$ holds for $A+B+C=\pi$ and is the
> standard way to break a symmetric expression involving tangents. It fails
> exactly when one angle is $90^\circ$, which is the degenerate case to watch for.

#### **S15**[JEE Adv][solved][triangle identity]If $A+B+C=180^\circ$, prove $\sin2A+\sin2B+\sin2C=4\sin A\sin B\sin C$.

<details>
<summary>Answer + Reasoning</summary>

**Method: sum-to-product, then use $C=\pi-(A+B)$.**
$\sin2A+\sin2B=2\sin(A+B)\cos(A-B)$, and $\sin2C=\sin(2\pi-2(A+B))=-\sin2(A+B)$.
So the left side is
$$2\sin(A+B)\cos(A-B)-2\sin(A+B)\cos(A+B)=2\sin(A+B)\big[\cos(A-B)-\cos(A+B)\big].$$
Since $\cos(A-B)-\cos(A+B)=2\sin A\sin B$ and $\sin(A+B)=\sin C$, this becomes
$4\sin A\sin B\sin C$ ✓.

Check numerically for $(60^\circ,60^\circ,60^\circ)$: LHS $=3\sin120^\circ=2.5981$
and RHS $=4(\frac{\sqrt3}{2})^3=2.5981$ ✓. For $(30^\circ,60^\circ,90^\circ)$: both
give $1.7321$ ✓.

**Answer:** proved.

</details>

#### **S16**[JEE Adv][solved][triangle identity]If $A+B+C=180^\unicode{00b0}$, prove $\tan A+\tan B+\tan C=\tan A\tan B\tan C$, and use it to find $\tan20^\circ\tan40^\circ\tan80^\circ$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the tangent addition formula.** $\tan(A+B)=\frac{\tan A+\tan B}{1-\tan A\tan B}$,
and $\tan(A+B)=\tan(\pi-C)=-\tan C$. Cross-multiplying gives
$\tan A+\tan B=-\tan C(1-\tan A\tan B)$, i.e.
$\tan A+\tan B+\tan C=\tan A\tan B\tan C$ ✓.

For the product, use $\tan3\theta=\frac{3t-t^3}{1-3t^2}$ with $t=\tan\theta$.
At $\theta=20^\circ$, $\tan60^\circ=\sqrt3$, so $t=\tan20^\circ$ satisfies
$$t^3-3\sqrt3\,t^2-3t+\sqrt3=0.$$
The three roots are $\tan20^\circ$, $\tan80^\circ$ and $\tan140^\circ=-\tan40^\circ$
(adding $60^\circ$ and $120^\circ$ leaves $\tan3\theta$ unchanged). Their product is
the negative of the constant term, $-\sqrt3$, so
$\tan20^\circ\cdot\tan80^\circ\cdot(-\tan40^\circ)=-\sqrt3$.

Check numerically: $\tan20^\circ\tan40^\circ\tan80^\circ
=0.36397\times0.83910\times5.67128=1.7321=\sqrt3$ ✓. Also the root sum is
$0.36397+5.67128-0.83910=5.19615=3\sqrt3$ ✓.

**Answer:** proved; $\tan20^\circ\tan40^\circ\tan80^\circ=\sqrt3$.

</details>

## 6.2 The Weierstrass (half-angle) substitution

> [!abstract] First Principles — rationalising trigonometry
> Put $t=\tan\frac A2$. Then
> $$\sin A=\frac{2t}{1+t^2},\qquad \cos A=\frac{1-t^2}{1+t^2},\qquad \tan A=\frac{2t}{1-t^2}.$$
> These follow from $\sin A=2\sin\frac A2\cos\frac A2$ after dividing by
> $\cos^2\frac A2$. The point is that **any** rational expression in sines and
> cosines becomes a rational expression in $t$ — so trig equations reduce to
> polynomial equations, and calculus on trig functions becomes calculus on
> rational functions.

> [!warning] Common Trap — the substitution is not onto
> $t=\tan\frac A2$ is undefined when $A=\pi$ (mod $2\pi$). Any solution with
> $\cos\frac A2=0$ is lost and must be checked separately. For $A\in(-\pi,\pi)$
> the map is a bijection onto $\mathbb R$.

> [!example] Olympiad Extension — rationalising everything
> The substitution $t=\tan\frac A2$ converts *any* rational expression in
> $\sin A,\cos A$ into a rational expression in $t$. This is why it is the standard
> first move for trig equations, and also why every integral of the form
> $\int R(\sin x,\cos x)\,dx$ becomes an integral of a rational function. Its one
> blind spot is $A=\pi$, where $\cos\frac A2=0$ — always check that case
> separately.

#### **S17**[JEE Adv][solved][weierstrass]Solve $\sin x+\cos x=1$ for $0\le x<2\pi$ using $t=\tan\frac x2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute and solve the resulting quadratic.**
$\frac{2t}{1+t^2}+\frac{1-t^2}{1+t^2}=1$, so $2t+1-t^2=1+t^2$, giving
$2t^2-2t=0$, i.e. $t=0$ or $t=1$.
$t=0$ gives $x=0$; $t=1$ gives $\frac x2=45^\circ$, so $x=90^\circ$.
Check: at $x=0$, $\sin0+\cos0=1$ ✓; at $x=90^\circ$, $1+0=1$ ✓. The excluded case
$x=\pi$ gives $\sin\pi+\cos\pi=-1\ne1$, so nothing was lost ✓.

**Answer:** $x=0$ and $x=\dfrac\pi2$.

</details>

## 6.3 Products of sines and cosines from roots of unity

> [!abstract] First Principles — the $n^{\rm th}$ roots of unity
> The $n$ roots of $z^n=1$ are $e^{2\pi ik/n}$, $k=0,\ldots,n-1$. Factoring,
> $$z^n-1=(z-1)\prod_{k=1}^{n-1}\left(z-e^{2\pi ik/n}\right),$$
> and dividing by $z-1$ and setting $z=1$ gives
> $$n=\prod_{k=1}^{n-1}\left(1-e^{2\pi ik/n}\right).$$
> Now $\lvert1-e^{i\theta}\rvert=2\left\lvert\sin\frac\theta2\right\rvert$, so taking
> moduli yields the sine product; a variant with $z=-1$ gives the cosine product.

$$\boxed{\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=\frac{n}{2^{n-1}}}
\qquad
\boxed{\prod_{k=1}^{n}\cos\frac{k\pi}{2n+1}=\frac1{2^n}}$$

> [!example] Olympiad Extension — products from roots of unity
> The identity $\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=\frac{n}{2^{n-1}}$ looks like
> it needs $n-1$ separate trig evaluations. It needs none: factor $z^n-1$ over the
> complex roots of unity, set $z=1$, and take moduli. The same trick gives the
> cosine product $\prod_{k=1}^{n}\cos\frac{k\pi}{2n+1}=\frac1{2^n}$ by working at
> $z=-1$ instead. **The pattern to memorise: a product of trig values at rational
> multiples of $\pi$ is a roots-of-unity problem in disguise.**

#### **S18**[Olympiad][solved][sine product]Prove $\displaystyle\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=\frac{n}{2^{n-1}}$, and evaluate the product for $n=7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: roots of unity, then take moduli.** From the factorisation above,
$n=\prod_{k=1}^{n-1}(1-e^{2\pi ik/n})$. Since
$\lvert1-e^{2\pi ik/n}\rvert=2\sin\frac{k\pi}{n}$ (positive for $1\le k\le n-1$),
$$n=2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}.$$
Check for $n=7$: the product is
$\sin\frac\pi7\sin\frac{2\pi}7\sin\frac{3\pi}7\sin\frac{4\pi}7\sin\frac{5\pi}7\sin\frac{6\pi}7
=0.43388\times0.78183\times0.97493\times0.97493\times0.78183\times0.43388
=0.109375$, and $\frac7{2^6}=\frac7{64}=0.109375$ ✓.

**Answer:** $\dfrac{n}{2^{n-1}}$; for $n=7$ it is $\dfrac7{64}$.

</details>

#### **S19**[Olympiad][solved][cosine product]Evaluate $\cos\dfrac\pi7\cos\dfrac{2\pi}7\cos\dfrac{3\pi}7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the cosine product with $2n+1=7$, so $n=3$.**
$\prod_{k=1}^{3}\cos\frac{k\pi}{7}=\frac1{2^3}=\frac18$.
Check numerically: $0.90097\times0.62349\times0.22252=0.125$ ✓.

**Answer:** $\dfrac18$.

</details>

## 6.4 Sums of cotangent and cosecant squares

> [!abstract] First Principles — where the sums come from
> The numbers $\tan\frac{k\pi}{n}$, $k=1,\ldots,n-1$, are the non-zero roots of a
> polynomial obtained by writing $\tan(n\theta)$ in terms of $t=\tan\theta$.
> Expanding $\tan(n\theta)=\frac{\Im(1+it)^n}{\Re(1+it)^n}$ and setting the
> numerator to zero gives a polynomial in $t$ whose roots are exactly those
> tangents. Reading off $\sum t_k^2$ from the coefficients gives
> $$\sum_{k=1}^{n-1}\cot^2\frac{k\pi}{n}=\frac{(n-1)(n-2)}{3},\qquad
> \sum_{k=1}^{n-1}\csc^2\frac{k\pi}{n}=\frac{n^2-1}{3},$$
> using $\csc^2=1+\cot^2$.

> [!example] Olympiad Extension — sums from polynomial roots
> The numbers $t_k=\tan\frac{k\pi}{n}$, $k=1,\ldots,n-1$, are the non-zero roots of
> a polynomial obtained by clearing denominators in $\tan(n\theta)$. Once that
> polynomial is written down, Vieta's formulae hand you $\sum t_k^2$ for free — and
> $\cot^2\frac{k\pi}{n}=\frac1{t_k^2}$ turns it into the cotangent sum. **Whenever a
> sum runs over trig values at equally spaced angles, look for the polynomial whose
> roots they are.**

#### **P6**[Olympiad][practice][cot sum]Verify $\displaystyle\sum_{k=1}^{n-1}\cot^2\frac{k\pi}{n}=\frac{(n-1)(n-2)}{3}$ for $n=3,4,5,6,7$.

<details>
<summary>Answer + Reasoning</summary>

**Method: direct evaluation.** For $n=3$: $\cot^260^\circ+\cot^2120^\circ=\frac13+\frac13=\frac23$,
and $\frac{2\cdot1}{3}=\frac23$ ✓. For $n=4$: $1+0+1=2=\frac{3\cdot2}{3}$ ✓. For
$n=5$: the sum is $4=\frac{4\cdot3}{3}$ ✓. For $n=6$: $6.6667=\frac{5\cdot4}{3}$ ✓.
For $n=7$: $10=\frac{6\cdot5}{3}$ ✓.

**Answer:** the identity holds for all tested $n$.

</details>

#### **P7**[Olympiad][practice][csc sum]Verify $\displaystyle\sum_{k=1}^{n-1}\csc^2\frac{k\pi}{n}=\frac{n^2-1}{3}$ for $n=3,4,5,6$.

<details>
<summary>Answer + Reasoning</summary>

**Method: use $\csc^2=1+\cot^2$ and the cotangent sum.** There are $n-1$ terms,
so $\sum\csc^2=(n-1)+\frac{(n-1)(n-2)}{3}=\frac{(n-1)(n+1)}{3}=\frac{n^2-1}{3}$.
Check for $n=3$: $\csc^260^\circ+\csc^2120^\circ=\frac43+\frac43=\frac83$, and
$\frac{9-1}{3}=\frac83$ ✓. For $n=4$: $2+1+2=5=\frac{15}{3}$ ✓. For $n=5$: $8=\frac{24}{3}$ ✓.
For $n=6$: $11.6667=\frac{35}{3}$ ✓.

**Answer:** the identity holds for all tested $n$.

</details>

---

# Appendix — Well-Ordered Theory Reference

Every result in dependency order; nothing is used before it is proved.

### A. Ratios and identities

| Result | Statement |
|---|---|
| Definitions | $\sin=\frac OH$, $\cos=\frac AH$, $\tan=\frac OA$ |
| Reciprocal | $\sin\csc=1$, $\cos\sec=1$, $\tan\cot=1$ |
| Quotient | $\tan=\frac{\sin}{\cos}$, $\cot=\frac{\cos}{\sin}$ |
| Pythagorean | $\sin^2+\cos^2=1$, $1+\tan^2=\sec^2$, $1+\cot^2=\csc^2$ |
| Periods | $\sin,\cos:2\pi$; $\tan,\cot:\pi$ |
| Signs | $\sin,+$ in I–II; $\cos,+$ in I, IV; $\tan,+$ in I, III |

### B. Compound angles

| Result | Statement |
|---|---|
| Sine | $\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$ |
| Cosine | $\cos(A\mp B)=\cos A\cos B\mp\sin A\sin B$ |
| Tangent | $\tan(A\pm B)=\frac{\tan A\pm\tan B}{1\mp\tan A\tan B}$ |
| Special | $\sin75^\circ=\frac{\sqrt6+\sqrt2}{4}$, $\tan105^\circ=-(2+\sqrt3)$ |

### C. Multiple and half angles

| Result | Statement |
|---|---|
| Double | $\sin2A=2\sin A\cos A$ |
| Double | $\cos2A=\cos^2A-\sin^2A=2\cos^2A-1=1-2\sin^2A$ |
| Double | $\tan2A=\frac{2\tan A}{1-\tan^2A}$ |
| Triple | $\sin3A=3\sin A-4\sin^3A$ |
| Triple | $\cos3A=4\cos^3A-3\cos A$ |
| Half | $\sin\frac A2=\pm\sqrt{\frac{1-\cos A}{2}}$ |
| Half | $\cos\frac A2=\pm\sqrt{\frac{1+\cos A}{2}}$ |
| Half | $\tan\frac A2=\frac{1-\cos A}{\sin A}=\frac{\sin A}{1+\cos A}$ |

### D. Transformation formulae

| Result | Statement |
|---|---|
| Product → sum | $2\sin A\cos B=\sin(A+B)+\sin(A-B)$ |
| Product → sum | $2\cos A\sin B=\sin(A+B)-\sin(A-B)$ |
| Product → sum | $2\cos A\cos B=\cos(A+B)+\cos(A-B)$ |
| Product → sum | $2\sin A\sin B=\cos(A-B)-\cos(A+B)$ |
| Sum → product | $\sin C+\sin D=2\sin\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| Sum → product | $\cos C+\cos D=2\cos\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| Sum → product | $\cos C-\cos D=-2\sin\frac{C+D}{2}\sin\frac{C-D}{2}$ |
| Series | $\sum_{k=1}^n\sin k\theta=\frac{\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac\theta2}$ |

### E. Trigonometric equations

| Equation | General solution |
|---|---|
| $\sin\theta=\sin\alpha$ | $\theta=n\pi+(-1)^n\alpha$ |
| $\cos\theta=\cos\alpha$ | $\theta=2n\pi\pm\alpha$ |
| $\tan\theta=\tan\alpha$ | $\theta=n\pi+\alpha$ |
| $a\sin x+b\cos x$ | $\sqrt{a^2+b^2}\sin(x+\varphi)$, $\tan\varphi=\frac ba$ |

### F. Triangles

| Result | Statement |
|---|---|
| Sine rule | $\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R$ |
| Cosine rule | $a^2=b^2+c^2-2bc\cos A$ |
| Area | $\Delta=\frac12bc\sin A$ |
| Inradius | $\Delta=rs$, so $r=\frac\Delta s$ |
| Half-angle | $\tan\frac A2=\frac r{s-a}$ |
| Right triangle | hypotenuse $=2R$ |
| Special values | $\sin18^\circ=\frac{\sqrt5-1}{4}$, $\cos36^\circ=\frac{\sqrt5+1}{4}$ |

### G. The $A+B+C=\pi$ identities

| Result | Statement |
|---|---|
| Cosines squared | $\cos^2A+\cos^2B+\cos^2C+2\cos A\cos B\cos C=1$ |
| Sines squared | $\sin^2A+\sin^2B+\sin^2C=2+2\cos A\cos B\cos C$ |
| Sines | $\sin A+\sin B+\sin C=4\cos\frac A2\cos\frac B2\cos\frac C2$ |
| Double angles | $\sin2A+\sin2B+\sin2C=4\sin A\sin B\sin C$ |
| Tangents | $\tan A+\tan B+\tan C=\tan A\tan B\tan C$ |
| Half-angle tangents | $\sum_{\rm cyc}\tan\frac A2\tan\frac B2=1$ |

### H. Olympiad products and sums

| Result | Statement |
|---|---|
| Weierstrass | $t=\tan\frac A2$: $\sin A=\frac{2t}{1+t^2}$, $\cos A=\frac{1-t^2}{1+t^2}$ |
| Sine product | $\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=\frac{n}{2^{n-1}}$ |
| Cosine product | $\prod_{k=1}^{n}\cos\frac{k\pi}{2n+1}=\frac1{2^n}$ |
| $\cos\frac\pi7\cos\frac{2\pi}7\cos\frac{3\pi}7$ | $\frac18$ |
| Cotangent squares | $\sum_{k=1}^{n-1}\cot^2\frac{k\pi}{n}=\frac{(n-1)(n-2)}{3}$ |
| Cosecant squares | $\sum_{k=1}^{n-1}\csc^2\frac{k\pi}{n}=\frac{n^2-1}{3}$ |
| $\tan20^\circ\tan40^\circ\tan80^\circ$ | $\sqrt3$ (cubic $t^3-3\sqrt3t^2-3t+\sqrt3=0$) |
| Sine sum | $\sum_{k=1}^{n}\sin k\theta=\frac{\sin(n\theta/2)\sin((n+1)\theta/2)}{\sin(\theta/2)}$ |

### I. Mistake checklist

1. The sign flip in $\cos(A-B)$ (it is $\cos A\cos B+\sin A\sin B$).
2. Resolving the half-angle $\pm$ without checking the quadrant of $\frac A2$.
3. Dividing an equation by a trigonometric factor that can vanish.
4. Forgetting the $(-1)^n$ in the general solution of $\sin\theta=\sin\alpha$.
5. Using period $\pi$ for sine or cosine (they are $2\pi$).
6. Mixing degrees and radians inside one computation.
7. Applying the sine rule to a *right* angle without care ($\sin90^\circ=1$).
8. Forgetting that $\tan90^\circ$ is undefined because $1-\tan^245^\circ=0$.
9. Writing $\sum\sin k\theta$ with the wrong $\frac{n+1}{2}$.
10. Using the cosine rule where the sine rule suffices (and vice versa).
