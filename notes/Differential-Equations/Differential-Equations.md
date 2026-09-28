---
title: "Differential Equations — Complete Notes"
aliases: ["Differential Equations", "Differential-Equations", "ODE"]
module: "Differential-Equations"
type: notes
tags: [differential-equations, module, complete, calculus, ode]
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 📝 [[Differential-Equations — Paper|Olympiad Paper]] · ✅ [[Differential-Equations — Solutions|Solutions]]

# Differential Equations

A **differential equation** (DE) relates a function to its derivatives. Newton's
second law, radioactive decay, population growth, cooling, mixing, circuits and
compound interest are all differential equations — the subject is the language of
*change*, and solving one means recovering the function from the rule that
governs how it changes.

The methods form a ladder: **separable** → **homogeneous** → **linear** →
**exact** → **higher-order linear** → the frontier (Clairaut's equation, singular
solutions, orthogonal trajectories). Each rung needs the one below it.

Everything here rests on [[Integration|antiderivatives and the integration
toolkit]] — every solution is obtained by *integrating*, which is why this module
comes after Integration.

`6 chapters` `worked examples (S) + practice (P)` `SVG + Mermaid diagrams` `41-question Olympiad paper + full solutions`

### ★ How to use these notes

**Read in order, and identify the type before you compute.** Chapter 1 fixes the
vocabulary (order, degree, linearity, initial-value problem) — misclassifying the
type is the single biggest source of wasted time. Chapters 2–5 are the method
ladder; Chapter 6 is higher-order and the Olympiad frontier.

- **Callouts** — `[!abstract]` First Principles = the derivation; `[!tip]` Key
  Idea = the takeaway; `[!warning]` Common Trap = the classic mistake;
  `[!example]` Olympiad Extension = the frontier version.
- **Numeric habit** — check any solution by *substituting it back* into the
  equation, and verify the initial condition. A numerical integrator (RK4) on
  $y'=f(x,y)$ gives an independent check.

### ▣ The roadmap

| Ch | Title | Level |
|---|---|---|
| 1 | Formation, order, degree & terminology | foundations |
| 2 | Variables separable | foundations |
| 3 | Homogeneous equations | machinery |
| 4 | Linear first-order & Bernoulli | machinery |
| 5 | Exact equations & orthogonal trajectories | applications |
| 6 | Higher-order linear & the Olympiad frontier | synthesis |

**Fig 1.1 — a slope field and its solution.** Each short segment has slope
$f(x,y)$; the solution through $(0,1)$ is the curve that is *tangent* to the
field everywhere. For $y'=\frac xy$ the field is $x^2-y^2=C$ — a family of
hyperbolas, and the initial condition picks one.

![Fig 1.1 — slope field and a solution curve](assets/fig-01.svg)

**Fig 1.2 — orthogonal trajectories.** Two families of curves that meet at right
angles everywhere. From $y=cx^2$ (slope $\frac{2y}{x}$) the orthogonal family has
slope $-\frac{x}{2y}$, which integrates to $x^2+2y^2=C$ — a family of ellipses.

![Fig 1.2 — orthogonal trajectories of a parabola family](assets/fig-02.svg)

---

# Chapter 1 — Formation, Order, Degree & Terminology

*Foundations · naming the thing before solving it*

## 1.1 The vocabulary

> [!abstract] First Principles — order and degree
> The **order** of a DE is the order of the highest derivative appearing in it.
> The **degree** is the power of that highest derivative *after* the equation has
> been made rational and integral in the derivatives.

$$\frac{dy}{dx}+2y=e^x \quad\text{(order 1, degree 1)}$$
$$\frac{d^2y}{dx^2}+3\frac{dy}{dx}+2y=0 \quad\text{(order 2, degree 1)}$$
$$\left(\frac{d^2y}{dx^2}\right)^3+\frac{dy}{dx}=0 \quad\text{(order 2, degree 3)}$$

> [!warning] Common Trap — "degree" is not always defined
> In $\sqrt{\frac{d^2y}{dx^2}}+\frac{dy}{dx}=1$ the equation is not polynomial in
> the derivatives, so the **degree is not defined** until you square it. Report
> the order always; the degree only when it exists.

## 1.2 Solution, general solution, particular solution

A **solution** is a function that satisfies the equation on an interval. The
**general solution** contains as many arbitrary constants as the order; a
**particular solution** fixes them, usually from an **initial-value problem**
(IVP).

#### **S1**[JEE Main][solved][verify]Verify that $y=e^{2x}$ solves $\frac{dy}{dx}-2y=0$.

$\frac{dy}{dx}=2e^{2x}$ and $2y=2e^{2x}$, so the difference is $0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute and check.** $y=Ce^{2x}$ is the general solution; $y=e^{2x}$ is the particular solution with $y(0)=1$.

**Answer:** yes, it is a solution.

</details>

#### **P1**[JEE Main][practice][order degree]State the order and degree of $\dfrac{d^3y}{dx^3}+\left(\dfrac{dy}{dx}\right)^4+y=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: highest derivative is third order; it appears to the first power.**

**Answer:** order $3$, degree $1$.

</details>

## 1.3 Forming a DE from a family of curves

> [!tip] Key Idea — differentiate to eliminate the constants
> A family of curves with $n$ parameters yields a DE of order $n$: differentiate
> $n$ times and eliminate the parameters.

#### **S2**[JEE Main][solved][formation]Find the DE of the family $y=cx+c^2$.

$\frac{dy}{dx}=c$, so substituting gives $y=x\frac{dy}{dx}+\left(\frac{dy}{dx}\right)^2$ — a first-order equation.

<details>
<summary>Answer + Reasoning</summary>

**Method: one parameter $\Rightarrow$ one differentiation.** $c$ disappears.

**Answer:** $y=xy'+(y')^2$ (Clairaut's form).

</details>

#### **P2**[JEE Main][practice][formation]Find the DE of all circles through the origin with centre on the $x$-axis: $(x-a)^2+y^2=a^2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: one parameter $a$; differentiate once.** Expanding: $x^2+y^2=2ax$, so $a=\frac{x^2+y^2}{2x}$; differentiating and substituting gives $x^2-y^2-2xy\frac{dy}{dx}=0$.

**Answer:** $x^2-y^2=2xy\dfrac{dy}{dx}$.

</details>

---

# Chapter 2 — Variables Separable

*Foundations · the first and easiest method*

## 2.1 The method

> [!abstract] First Principles — separation
> If the equation can be written $g(y)\,dy=f(x)\,dx$, integrate both sides:
> $$\int g(y)\,dy=\int f(x)\,dx+C.$$
> This is exactly the substitution rule run backwards — the equation is
> *separable* when $y'$ factors as a function of $x$ times a function of $y$.

#### **S3**[JEE Main][solved][separable]Solve $\dfrac{dy}{dx}=\dfrac xy$ with $y(0)=1$.

$y\,dy=x\,dx\Rightarrow\frac{y^2}{2}=\frac{x^2}{2}+C$. With $y(0)=1$: $C=\frac12$, so $y^2=x^2+1$ and (positive branch) $y=\sqrt{x^2+1}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: separate and integrate.** Check: $\frac{dy}{dx}=\frac{x}{\sqrt{x^2+1}}=\frac xy$ ✓.

**Answer:** $y=\sqrt{x^2+1}$; $y(1)=\sqrt2\approx1.4142$.

</details>

#### **S4**[JEE Main][solved][separable]Solve $\dfrac{dy}{dx}=y$ with $y(0)=1$.

$\frac{dy}{y}=dx\Rightarrow\ln\lvert y\rvert=x+C$; $y(0)=1\Rightarrow C=0$, so $y=e^x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: separate.** This is the defining property of the exponential: the function equal to its own rate of change.

**Answer:** $y=e^x$.

</details>

#### **P3**[JEE Main][practice][separable]Solve $\dfrac{dy}{dx}=2xy$ with $y(0)=3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: separate.** $\ln\lvert y\rvert=x^2+C$; $y(0)=3\Rightarrow C=\ln3$.

**Answer:** $y=3e^{x^2}$; $y(1)=3e\approx8.1548$.

</details>

#### **P4**[JEE Adv][practice][separable]Solve $\dfrac{dy}{dx}=e^{x-y}$ with $y(0)=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: separate ($e^{x-y}=e^xe^{-y}$).** $e^y\,dy=e^xdx\Rightarrow e^y=e^x+C$; $y(0)=0\Rightarrow1=1+C$, $C=0$.

**Answer:** $e^y=e^x$, i.e. $y=x$.

</details>

```mermaid
flowchart LR
    A["y′ = f(x)·g(y)"] --> B["Separate: dy/g(y) = f(x) dx"]
    B --> C["Integrate both sides (+C)"]
    C --> D["Apply the initial condition"]
    D --> E["Solve for y if possible"]
```

---

# Chapter 3 — Homogeneous Equations

*Machinery · the substitution $y=vx$*

## 3.1 What homogeneous means

> [!abstract] First Principles — homogeneous function
> $M(x,y)$ is **homogeneous of degree $n$** if
> $M(tx,ty)=t^nM(x,y)$. A DE $\frac{dy}{dx}=\frac{M(x,y)}{N(x,y)}$ with $M,N$
> homogeneous of the *same* degree is a **homogeneous DE**, and the substitution
> $y=vx$ makes it separable.

#### **S5**[JEE Main][solved][homogeneous]Solve $\dfrac{dy}{dx}=\dfrac{x+y}{x}$ with $y(1)=0$.

Put $y=vx$, so $\frac{dy}{dx}=v+x\frac{dv}{dx}$: $v+xv'=1+v\Rightarrow xv'=1\Rightarrow v=\ln x+C$. With $v(1)=0$: $C=0$, so $v=\ln x$ and $y=x\ln x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y=vx$ reduces it to a separable equation.** Check: $\frac{dy}{dx}=\ln x+1$ and $\frac{x+y}{x}=\frac{x+x\ln x}{x}=1+\ln x$ ✓.

**Answer:** $y=x\ln x$; $y(e)=e\approx2.7183$.

</details>

#### **P5**[JEE Adv][practice][homogeneous]Solve $\dfrac{dy}{dx}=\dfrac yx+\left(\dfrac yx\right)^2$ with $y(1)=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y=vx$.** $v+xv'=v+v^2\Rightarrow\frac{dv}{v^2}=\frac{dx}{x}\Rightarrow-\frac1v=\ln x+C$; $v(1)=1\Rightarrow C=-1$, so $v=\frac1{1-\ln x}$.

**Answer:** $y=\dfrac{x}{1-\ln x}$; $y(2)=\dfrac2{1-\ln2}\approx6.5178$ (blows up as $x\to e$).

</details>

---

# Chapter 4 — Linear First-Order & Bernoulli

*Machinery · the integrating factor*

## 4.1 The integrating factor

> [!abstract] First Principles — why the integrating factor works
> A **linear first-order** DE has the form $\frac{dy}{dx}+P(x)y=Q(x)$. Multiply
> by the **integrating factor** $\mu=e^{\int P\,dx}$; then
> $\frac{d}{dx}(\mu y)=\mu Q$, because $\mu'=\mu P$. Integrate:
> $$y=\frac{1}{\mu}\int\mu Q\,dx.$$
> The factor is chosen so the left side becomes an exact derivative.

#### **S6**[JEE Main][solved][linear]Solve $\dfrac{dy}{dx}+y=e^x$ with $y(0)=0$.

$P=1$, so $\mu=e^x$: $\frac{d}{dx}(e^xy)=e^{2x}$, hence $e^xy=\frac12e^{2x}+C$. With $y(0)=0$: $C=-\frac12$, so $y=\frac12(e^x-e^{-x})=\sinh x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: integrating factor.** Check: $y'+y=\frac12(e^x+e^{-x})+\frac12(e^x-e^{-x})=e^x$ ✓.

**Answer:** $y=\sinh x$; $y(1)=\sinh1\approx1.1752$.

</details>

#### **S7**[JEE Main][solved][linear]Solve $\dfrac{dy}{dx}+2y=4x$ with $y(0)=1$.

$\mu=e^{2x}$: $\frac{d}{dx}(e^{2x}y)=4xe^{2x}$, so $e^{2x}y=2xe^{2x}-e^{2x}+C$. With $y(0)=1$: $C=2$, so $y=2x-1+2e^{-2x}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: integrating factor + by parts on the right.** Check at $x=0$: $y=0-1+2=1$ ✓; $y'+2y=(2-4e^{-2x})+(4x-2+4e^{-2x})=4x$ ✓.

**Answer:** $y=2x-1+2e^{-2x}$; $y(1)=1+\dfrac2{e^2}\approx1.2707$.

</details>

#### **P6**[JEE Adv][practice][linear]Solve $\dfrac{dy}{dx}+\dfrac yx=x$ with $y(1)=0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $P=\frac1x$, $\mu=e^{\ln x}=x$.** $\frac{d}{dx}(xy)=x^2$, so $xy=\frac{x^3}{3}+C$; $y(1)=0\Rightarrow C=-\frac13$.

**Answer:** $y=\dfrac{x^2}{3}-\dfrac1{3x}$.

</details>

## 4.2 Bernoulli's equation

> [!abstract] First Principles — Bernoulli
> $\frac{dy}{dx}+P(x)y=Q(x)y^n$ with $n\ne0,1$. Divide by $y^n$ and substitute
> $u=y^{1-n}$; the result is **linear** in $u$, so the integrating factor applies.

#### **S8**[Olympiad][solved][Bernoulli]Solve $\dfrac{dy}{dx}+y=xy^2$ with $y(0)=1$.

Divide by $y^2$: $y^{-2}y'+y^{-1}=x$. Put $u=y^{-1}$, so $u'=-y^{-2}y'$ and the equation becomes $-u'+u=x$, i.e. $u'-u=-x$. With $\mu=e^{-x}$: $(ue^{-x})'=-xe^{-x}$, so $ue^{-x}=e^{-x}(x+1)+C$, i.e. $u=x+1+Ce^x$. From $u(0)=1$: $C=0$, so $u=x+1$ and $y=\frac1{x+1}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Bernoulli substitution $u=y^{-1}$.** Check: $y'+y=-1/(x+1)^2+1/(x+1)=x/(x+1)^2=xy^2$ ✓.

**Answer:** $y=\dfrac1{x+1}$; $y(1)=\dfrac12$.

</details>

---

# Chapter 5 — Exact Equations & Orthogonal Trajectories

*Applications · potentials, and curves meeting at right angles*

## 5.1 Exact equations

> [!abstract] First Principles — exactness
> $M(x,y)\,dx+N(x,y)\,dy=0$ is **exact** if $\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$ — then there is a **potential** $F$ with
> $F_x=M$, $F_y=N$, and the solutions are the level curves $F(x,y)=C$.

#### **S9**[JEE Adv][solved][exact]Solve $(2x+y)\,dx+(x+2y)\,dy=0$ with $y(0)=1$.

$\frac{\partial M}{\partial y}=1=\frac{\partial N}{\partial x}$, so it is exact. Integrate $F_x=2x+y$ in $x$: $F=x^2+xy+\phi(y)$; then $F_y=x+\phi'(y)=x+2y$, so $\phi'=2y$ and $\phi=y^2$. Thus $x^2+xy+y^2=C$; with $y(0)=1$, $C=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: find the potential by partial integration.** Check: $dF=(2x+y)dx+(x+2y)dy$ ✓.

**Answer:** $x^2+xy+y^2=1$; at $x=1$, $y=0$ or $y=-1$.

</details>

#### **P7**[JEE Adv][practice][exact]Solve $(3x^2+2xy)\,dx+(x^2+2y)\,dy=0$ with $y(0)=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: exactness check $\partial M/\partial y=2x=\partial N/\partial x$, then integrate.** $F=x^3+x^2y+y^2=C$; $y(0)=1\Rightarrow C=1$.

**Answer:** $x^3+x^2y+y^2=1$.

</details>

## 5.2 Orthogonal trajectories

> [!tip] Key Idea — negate and invert the slope
> The orthogonal trajectory of a family has slope $-\dfrac1{y'}$ at every point.
> Solve that new first-order DE to get the second family.

#### **S10**[JEE Adv][solved][orthogonal]Find the orthogonal trajectories of $y=cx^2$.

$\frac{dy}{dx}=2cx=\frac{2y}{x}$, so the orthogonal slope is $-\frac{x}{2y}$. Then $2y\,dy=-x\,dx\Rightarrow y^2=-\frac{x^2}{2}+C$, i.e. $x^2+2y^2=C$.

<details>
<summary>Answer + Reasoning</summary>

**Method: replace the slope by its negative reciprocal and separate.** Check the orthogonality: parabola slope $\frac{2y}{x}$, ellipse slope $-\frac{x}{2y}$, product $-1$ ✓.

**Answer:** $x^2+2y^2=C$ (a family of ellipses).

</details>

#### **P8**[JEE Adv][practice][orthogonal]Find the orthogonal trajectories of the concentric circles $x^2+y^2=c$.

<details>
<summary>Answer + Reasoning</summary>

**Method: circle slope $-\frac xy$; orthogonal slope $\frac yx$; separate.** $\frac{dy}{y}=\frac{dx}{x}\Rightarrow\ln\lvert y\rvert=\ln\lvert x\rvert+C$.

**Answer:** $y=Cx$ — the straight lines through the origin.

</details>

---

# Chapter 6 — Higher-Order Linear & the Olympiad Frontier

*Synthesis · second-order equations and the frontier*

## 6.1 Second-order linear with constant coefficients

> [!abstract] First Principles — the characteristic equation
> For $ay''+by'+cy=0$ try $y=e^{rx}$: substitution gives $ar^2+br+c=0$, the
> **characteristic equation**. Distinct real roots $r_1,r_2\Rightarrow y=Ae^{r_1x}+Be^{r_2x}$; a repeated root $r\Rightarrow y=(A+Bx)e^{rx}$; complex roots
> $\alpha\pm i\beta\Rightarrow y=e^{\alpha x}(A\cos\beta x+B\sin\beta x)$.

#### **S11**[JEE Main][solved][second order]Solve $y''-3y'+2y=0$ with $y(0)=0$, $y'(0)=1$.

$r^2-3r+2=(r-1)(r-2)$, so $y=Ae^x+Be^{2x}$. Then $A+B=0$ and $A+2B=1$, giving $A=-1$, $B=1$: $y=e^{2x}-e^x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: characteristic roots + the two initial conditions.** Check: $y(0)=1-1=0$ ✓; $y'(0)=2-1=1$ ✓.

**Answer:** $y=e^{2x}-e^x$; $y(1)=e^2-e\approx4.6708$.

</details>

#### **S12**[JEE Adv][solved][second order]Solve $y''+4y'+4y=0$ with $y(0)=1$, $y'(0)=0$.

$r^2+4r+4=(r+2)^2$, a repeated root: $y=(A+Bx)e^{-2x}$. From $y(0)=1$, $A=1$; $y'=(B-2A-2Bx)e^{-2x}$, so $y'(0)=B-2=0$ and $B=2$: $y=(1+2x)e^{-2x}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: repeated root ⇒ the $xe^{rx}$ companion.** Check: $y(0)=1$ ✓; $y'(0)=0$ ✓.

**Answer:** $y=(1+2x)e^{-2x}$; $y(1)=3e^{-2}\approx0.4060$.

</details>

#### **S13**[JEE Adv][solved][Cauchy–Euler]Solve $x^2y''+xy'-y=0$ with $y(1)=0$, $y'(1)=1$.

Try $y=x^r$: $r(r-1)+r-1=r^2-1=0$, so $r=\pm1$ and $y=Ax+\frac Bx$. From $y(1)=0$: $A+B=0$; $y'=A-\frac B{x^2}$, so $y'(1)=A-B=1$. Hence $A=\frac12$, $B=-\frac12$: $y=\frac12\big(x-\frac1x\big)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Cauchy–Euler (equidimensional) — powers of $x$ replace exponentials.** Check: $y'=\frac12(1+x^{-2})$, $y''=x^{-3}$; $x^2y''+xy'-y=1+\frac x2(1+x^{-2})-\frac12(x-x^{-1})=0$ ✓.

**Answer:** $y=\dfrac12\Big(x-\dfrac1x\Big)$; $y(2)=\dfrac34$.

</details>

#### **P9**[JEE Main][practice][second order]Solve $y''+y=0$ with $y(0)=0$, $y'(0)=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $r^2+1=0\Rightarrow r=\pm i$, so $y=A\cos x+B\sin x$; $y(0)=0\Rightarrow A=0$, $y'(0)=B=1$.**

**Answer:** $y=\sin x$; $y(\pi/2)=1$.

</details>

## 6.2 Applications: growth, decay and cooling

> [!abstract] First Principles — Newton's law of cooling
> $\frac{dT}{dt}=-k(T-T_a)$ where $T_a$ is the ambient temperature. This is
> separable *and* linear: $T-T_a=(T_0-T_a)e^{-kt}$.

#### **S14**[JEE Main][solved][cooling]A body at $100^\circ$C cools in a $20^\circ$C room; after $10$ min it is $60^\circ$C. Find its temperature after $20$ min.

$T-20=80e^{-kt}$. From $T(10)=60$: $40=80e^{-10k}$, so $e^{-10k}=\frac12$ and $k=\frac{\ln2}{10}$. Then $T(20)-20=80e^{-20k}=80\cdot\frac14=20$, giving $T(20)=40$.

<details>
<summary>Answer + Reasoning</summary>

**Method: separable; use the middle reading to find $k$.** Check: $e^{-10k}=1/2$ means $e^{-20k}=1/4$ ✓.

**Answer:** $40^\circ$C.

</details>

#### **P10**[JEE Main][practice][growth]A population of $1000$ grows at $10\%$ per year. Find $P(10)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\frac{dP}{dt}=0.1P$ separable.** $P=1000e^{0.1t}$.

**Answer:** $P(10)=1000e\approx2718.28$.

</details>

## 6.3 The frontier: Clairaut and singular solutions

> [!example] Olympiad Extension — Clairaut's equation
> $y=xp+f(p)$ with $p=\frac{dy}{dx}$ has a **family of straight lines**
> $y=cx+f(c)$ *and* a **singular solution** which is their envelope. Differentiate
> with respect to $x$: $p=p+xp'+f'(p)p'$, so $\big(x+f'(p)\big)p'=0$. The branch
> $p'=0$ (i.e. $p=c$ constant) gives the lines; the branch $x+f'(p)=0$ gives the
> envelope, found by eliminating $p$.

#### **S15**[Olympiad][solved][Clairaut]Solve $y=xy'+(y')^2$, and find its singular solution.

Differentiating: $(x+2y')y''=0$. The branch $y''=0$ gives $y'=c$, so $y=cx+c^2$ — a family of lines. The branch $x+2c=0$ gives $c=-\frac x2$, and substituting into the family: $y=-\frac{x^2}{2}+\frac{x^2}{4}=-\frac{x^2}{4}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: differentiate and split into two branches.** Check the envelope: at $x=2$, $y=-1$, $y'=-1$, and $xy'+(y')^2=2(-1)+1=-1=y$ ✓.

**Answer:** general $y=cx+c^2$; singular solution $y=-\dfrac{x^2}{4}$.

</details>

#### **P11**[Olympiad][practice][singular]Find the singular solution of $y=xy'-(y')^2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: as S15.** Differentiating: $(x-2y')y''=0$. Lines $y=cx-c^2$; envelope from $x-2c=0$, $c=\frac x2$: $y=\frac{x^2}{2}-\frac{x^2}{4}=\frac{x^2}{4}$.

**Answer:** $y=\dfrac{x^2}{4}$.

</details>

#### **P12**[Olympiad][practice][reduction of order]Solve $x^2y''-2xy'+2y=0$ given $y(1)=1$, $y'(1)=2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: Cauchy–Euler, $y=x^r$.** $r(r-1)-2r+2=r^2-3r+2=0\Rightarrow r=1,2$, so $y=Ax+Bx^2$; $y(1)=A+B=1$, $y'(1)=A+2B=2\Rightarrow B=1$, $A=0$.

**Answer:** $y=x^2$.

</details>

---

*Synthesis · higher-order structure, existence theory, and the nonlinear frontier*

## 6.4 Reduction of order: equations free of $x$

> [!abstract] First Principles — the substitution $p=p(y)$
> If $x$ does not appear explicitly, the equation has the form $y''=f(y,y')$.
> Treat $p=y'$ as a function of $y$ and use the chain rule:
> $$y''=\frac{dp}{dx}=\frac{dp}{dy}\cdot\frac{dy}{dx}=p\,\frac{dp}{dy}.$$
> A second-order equation collapses to a **first-order** one in $p$ and $y$ — one
> integration down. The constant that appears is genuinely new, and a second
> integration later the general solution carries its two constants, as it must.

#### **S16**[JEE Adv][solved][reduction of order]Solve $yy''=(y')^2$ with $y(0)=1$, $y'(0)=1$.

Put $p=y'$ and regard $p$ as a function of $y$: $y''=p\frac{dp}{dy}$, so
$yp\frac{dp}{dy}=p^2$. For $p\neq0$ this is $\frac{dp}{p}=\frac{dy}{y}$, giving
$\ln p=\ln y+\ln C$, i.e. $p=Cy$. From $y(0)=1$ and $y'(0)=p=1$ we get $C=1$, so
$y'=y$, hence $y=Ae^{x}$ and $y(0)=1$ gives $A=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the $p(y)$ substitution; note the discarded branch $p=0$ before dividing.** Check: for $y=e^{x}$, $y''=e^{x}=y$ and $yy''=e^{2x}=(y')^{2}$ ✓; $y(0)=1$, $y'(0)=1$ ✓. The branch $p=0$ gives $y$ constant, which cannot satisfy $y'(0)=1$, so nothing is lost.

**Answer:** $y=e^{x}$; $y(1)=e\approx2.718282$.

</details>

> [!example] Olympiad Extension — one known solution generates the whole family
> For a homogeneous linear equation $y''+P(x)y'+Q(x)y=0$, a **single** known
> solution $y_{1}$ determines a second one:
> $$y_{2}=y_{1}\int\frac{e^{-\int P\,dx}}{y_{1}^{2}}\,dx.$$
> So the general solution is recovered from one solution alone. The proof is a
> substitution: put $y=y_{1}v$, and $v$ satisfies
> $y_{1}v''+(2y_{1}'+Py_{1})v'=0$ — first-order in $v'$, with integrating factor
> $y_{1}^{2}e^{\int P\,dx}$. This is why finding *one* solution of a homogeneous
> linear equation is as good as finding them all.

#### **S17**[JEE Adv][solved][reduction of order]Given that $y=\sin x$ solves $y''+y=0$, find a second independent solution and the general solution.

Here $P(x)=0$, so $y_{2}=\sin x\int\frac{1}{\sin^{2}x}\,dx=\sin x\,(-\cot x)=-\cos x$. Independence is confirmed by the Wronskian: $W=\sin x\cdot(-\sin x)-\cos x\cdot\cos x=-1\neq0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the reduction-of-order formula with $P=0$.** Check: $(-\cos x)''+(-\cos x)=\cos x-\cos x=0$ ✓; $W=-1\neq0$ ✓.

**Answer:** general solution $y=A\sin x+B\cos x$ (any independent pair does — $-\cos x$ may be replaced by $\cos x$).

</details>

#### **P13**[JEE Adv][practice][reduction of order]Given that $y=x$ solves $x^{2}y''-2xy'+2y=0$, find the general solution.

<details>
<summary>Answer + Reasoning</summary>

**Method: divide by $x^{2}$ first to read off $P=-\frac2x$.** Then $e^{-\int P\,dx}=e^{2\ln x}=x^{2}$, so $y_{2}=x\int\frac{x^{2}}{x^{2}}\,dx=x\int1\,dx=x^{2}$.

**Answer:** $y=Ax+Bx^{2}$. (Check: $x^{2}(2)-2x(2x)+2x^{2}=0$ ✓.)

</details>

## 6.5 Existence and uniqueness: where the theorem stops

> [!abstract] First Principles — Picard–Lindelöf
> If $f(x,y)$ and $\frac{\partial f}{\partial y}$ are continuous near
> $(x_{0},y_{0})$, then $y'=f(x,y)$, $y(x_{0})=y_{0}$ has exactly **one**
> solution through that point. The hypothesis on $\partial f/\partial y$ is a
> *Lipschitz* condition: the slope may not grow faster than linearly in $y$.
> It is this — not the continuity of $f$ — that forces uniqueness.

> [!example] Olympiad Extension — $y'=y^{1/2}$ has a continuum of solutions
> With $y(0)=0$, the equation $y'=y^{1/2}$ has at least two solutions:
> $$y=0\qquad\text{and}\qquad y=\frac{x^{2}}{4}\quad(x\ge0).$$
> Both pass through the origin. The reason is that $y\mapsto y^{1/2}$ has
> **infinite slope at $0$**, so the Lipschitz condition fails exactly at the
> initial point. More is true: for **any** $a\ge0$,
> $$y=\begin{cases}0,&x\le a\\[2pt]\dfrac{(x-a)^{2}}{4},&x>a\end{cases}$$
> is also a solution — the curve may sit at $0$ as long as it likes and then
> peel away. Uniqueness is not a property of equations; it is a **theorem with
> hypotheses**, and dropping them yields infinitely many solutions.

#### **S18**[Olympiad][solved][non-uniqueness]Exhibit two distinct solutions of $y'=y^{1/2}$ with $y(0)=0$, and explain why the uniqueness theorem does not apply.

$y=0$ clearly works. For $y=\frac{x^{2}}{4}$ we have $y'=\frac{x}{2}$ and
$y^{1/2}=\frac{|x|}{2}$, which equals $\frac x2$ for $x\ge0$; so it solves the
equation on $x\ge0$ and satisfies $y(0)=0$. Two different curves pass through
$(0,0)$, so the initial value problem is not uniquely solvable.

<details>
<summary>Answer + Reasoning</summary>

**Method: check both candidates directly, then audit the hypotheses.** $\frac{\partial f}{\partial y}=\frac{1}{2\sqrt y}\to\infty$ as $y\to0^{+}$, so $f$ is not Lipschitz near $y=0$ and Picard–Lindelöf gives no conclusion.

**Answer:** $y=0$ and $y=\dfrac{x^{2}}{4}$ ($x\ge0$) — infinitely many in total. Related: $y'=y^{1/3}$, $y(0)=0$ has solutions $y=0$ and $y=\big(\frac{2x}{3}\big)^{3/2}$ ($x\ge0$).

</details>

#### **P14**[Olympiad][practice][non-uniqueness]Show that $y'=y^{1/3}$, $y(0)=0$, has a solution that is $0$ for $x\le1$ and positive for $x>1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: shift the standard solution so that it starts at $x=1$.** Take $y=\big(\frac{2(x-1)}{3}\big)^{3/2}$ for $x>1$: then $y'=\big(\frac{2(x-1)}{3}\big)^{1/2}$ and $y^{1/3}=\big(\frac{2(x-1)}{3}\big)^{1/2}$ ✓, with $y(1)=0$.

**Answer:** $y=\begin{cases}0,&x\le1\\[2pt]\big(\dfrac{2(x-1)}{3}\big)^{3/2},&x>1\end{cases}$

</details>

## 6.6 Lagrange and Riccati: the nonlinear frontier

> [!abstract] First Principles — Lagrange's equation
> An equation of the form $y=xf(y')+g(y')$ is not linear in $y$, but
> differentiating once makes it linear — in the *other* variable. With $p=y'$:
> $$p=f(p)+\big(xf'(p)+g'(p)\big)\frac{dp}{dx},$$
> and rearranging gives a **linear** equation for $x$ as a function of $p$:
> $$\frac{dx}{dp}-\frac{xf'(p)}{p-f(p)}=\frac{g'(p)}{p-f(p)}.$$
> Solve it with an integrating factor; the answer then comes out parametrically
> in $p$.

#### **S19**[Olympiad][solved][Lagrange]Solve $y=x(y')^{2}+1$.

With $p=y'$ the equation is $y=xp^{2}+1$, so $f(p)=p^{2}$ and $g(p)=1$ with
$g'(p)=0$. Differentiating: $p=2xp+xp^{2}p'$, so
$p(1-2x)=xp^{2}\frac{dp}{dx}$. Solving for $\frac{dx}{dp}$ rather than
$\frac{dp}{dx}$ gives $\frac{dx}{dp}=\frac{2x}{1-p}$, i.e.
$\frac{dx}{dp}-\frac{2x}{1-p}=0$ — linear and homogeneous. Hence
$\frac{dx}{x}=\frac{2\,dp}{1-p}$, so $\ln x=-2\ln(1-p)+C$ and
$x=\frac{C}{(1-p)^{2}}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: differentiate, then read the equation as linear in $x(p)$ — not in $p(x)$.** Substituting back gives $y=xp^{2}+1=1+\dfrac{Cp^{2}}{(1-p)^{2}}$.

**Answer:** $x=\dfrac{C}{(1-p)^{2}},\qquad y=1+\dfrac{Cp^{2}}{(1-p)^{2}}$ (parametric, $p$ the parameter). Check: from the parametric form, $\dfrac{dy}{dx}=\dfrac{dy/dp}{dx/dp}=\dfrac{2Cp(1-p)^{-2}+2Cp^{2}(1-p)^{-3}}{2C(1-p)^{-3}}=p$ exactly, so $y=xp^{2}+1$ holds ✓ (verified at $p=0,\,0.2,\,0.5,\,-0.3,\,0.9$).

</details>

> [!example] Olympiad Extension — Riccati: linear once you know one solution
> $$y'=q_{0}(x)+q_{1}(x)y+q_{2}(x)y^{2}$$
> has **no general quadrature**: no formula built from integrals and elementary
> functions solves it for arbitrary $q_{0},q_{1},q_{2}$. But if one particular
> solution $y_{1}$ is known, the substitution $y=y_{1}+\frac1u$ turns it into a
> **linear** equation for $u$. Riccati is exactly what sits between the linear
> case ($q_{2}=0$) and the separable case ($q_{0}=q_{1}=0$) — and that is
> precisely why it resists a closed form in general.

#### **S20**[Olympiad][solved][Riccati]Solve $y'=y^{2}-y$, given that $y=0$ is a solution.

Put $y=0+\frac1u$, so $y'=-\frac{u'}{u^{2}}$. Then
$-\frac{u'}{u^{2}}=\frac1{u^{2}}-\frac1u$, so $-u'=1-u$, i.e. $u'-u=-1$. This is
linear with integrating factor $e^{-x}$: $\frac{d}{dx}(ue^{-x})=-e^{-x}$, so
$ue^{-x}=e^{-x}+C$ and $u=1+Ce^{x}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the Riccati substitution $y=y_{1}+\frac1u$ reduces the equation to a linear DE.** Hence $y=\dfrac{1}{1+Ce^{x}}$.

**Answer:** $y=\dfrac{1}{1+Ce^{x}}$. Check: $y'=\dfrac{-Ce^{x}}{(1+Ce^{x})^{2}}$ and $y^{2}-y=\dfrac{1-(Ce^{x}+1)}{(1+Ce^{x})^{2}}=\dfrac{-Ce^{x}}{(1+Ce^{x})^{2}}$ ✓; also $y\to0$ as $C\to\infty$, recovering the given particular solution ✓. Cross-checked by RK4 at $x=1.3$ from $x_{0}=0.3$ for $C=1$ and $C=3$ ✓.

</details>

#### **P15**[Olympiad][practice][Riccati]Solve $y'=x\big(y^{2}-1\big)$, given that $y=1$ is a solution.

<details>
<summary>Answer + Reasoning</summary>

**Method: as S20, but the integrating factor is now a Gaussian.** With $y=1+\frac1u$: $-\frac{u'}{u^{2}}=x\big(2/u+1/u^{2}\big)$, so $-u'=2xu+x$, i.e. $u'+2xu=-x$. The integrating factor is $e^{x^{2}}$, giving $\frac{d}{dx}(ue^{x^{2}})=-xe^{x^{2}}$, so $ue^{x^{2}}=-\frac12 e^{x^{2}}+C$ and $u=Ce^{-x^{2}}-\frac12$.

**Answer:** $y=1+\dfrac{1}{Ce^{-x^{2}}-\frac12}$. Check: with $u=Ce^{-x^{2}}-\frac12$, $u'=-2Cxe^{-x^{2}}$ and $2xu+x=2xCe^{-x^{2}}$, so $u'+2xu=-x$ ✓; substituting back gives $x(y^{2}-1)=y'$ exactly at $x=0.6$ for $C=1,\,2,\,-0.7$ ✓.

</details>

## 6.7 Damping: the three regimes

> [!abstract] First Principles — the damped oscillator
> $y''+2\zeta\omega\,y'+\omega^{2}y=0$ has characteristic roots
> $r=-\zeta\omega\pm\omega\sqrt{\zeta^{2}-1}$. The sign of the discriminant
> splits the behaviour into three regimes, and the transition at $\zeta=1$ is
> where the two real roots merge into one — which is exactly why the critically
> damped solution needs the $xe^{rx}$ companion term.

#### **S21**[JEE Adv][solved][damping]Solve $y''+2y'+5y=0$ with $y(0)=0$, $y'(0)=2$, and describe the behaviour.

$r^{2}+2r+5=0$ gives $r=-1\pm2i$, so $y=e^{-x}(A\cos2x+B\sin2x)$. From $y(0)=0$, $A=0$; then $y=Be^{-x}\sin2x$ and $y'(0)=2B=2$, so $B=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: complex roots with a negative real part — under-damped oscillation with a decaying envelope.** Check: $y'=e^{-x}(2\cos2x-\sin2x)$, so $y'(0)=2$ ✓; substituting $y=e^{-x}\sin2x$ into $y''+2y'+5y$ gives $0$ ✓.

**Answer:** $y=e^{-x}\sin 2x$; $y(1)\approx0.334512$. The oscillation has period $\pi$ and the envelope $e^{-x}$ halves every $\ln2\approx0.693$ units — this is **under-damped** ($\zeta=\frac{1}{\sqrt5}<1$).

</details>

#### **P16**[JEE Adv][practice][damping]Classify and solve $y''+3y'+2y=0$ with $y(0)=0$, $y'(0)=1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $r^{2}+3r+2=(r+1)(r+2)$ — two distinct negative real roots, so the motion is over-damped and non-oscillatory. $y=Ae^{-x}+Be^{-2x}$; $A+B=0$ and $-A-2B=1$, so $A=1$, $B=-1$.

**Answer:** $y=e^{-x}-e^{-2x}$; $y(1)\approx0.232544$. Both terms decay, so the response returns to $0$ without crossing it — the hallmark of over-damping.

</details>

# Appendix — Well-Ordered Theory Reference

Every result in dependency order; nothing is used before it is proved.

### A. Terminology

| Result | Statement |
|---|---|
| Order | order of the highest derivative present |
| Degree | power of that derivative, when the equation is polynomial in derivatives |
| General solution | contains as many arbitrary constants as the order |
| IVP | a DE plus enough initial conditions to fix the constants |

### B. First-order methods

| Method | Form | Key step |
|---|---|---|
| Separable | $y'=f(x)g(y)$ | $\int\frac{dy}{g(y)}=\int f(x)dx$ |
| Homogeneous | $\frac{M}{N}$, $M,N$ same degree | $y=vx$ ⇒ separable |
| Linear | $y'+P(x)y=Q(x)$ | integrating factor $\mu=e^{\int P\,dx}$ |
| Bernoulli | $y'+Py=Qy^n$ | $u=y^{1-n}$ ⇒ linear |
| Exact | $Mdx+Ndy=0$, $M_y=N_x$ | find $F$ with $F_x=M$, $F_y=N$ |
| Orthogonal trajectories | slope $-\frac1{y'}$ | solve the new first-order DE |

### C. Higher-order linear

| Result | Statement |
|---|---|
| Characteristic equation | $ar^2+br+c=0$ for $ay''+by'+cy=0$ |
| Distinct real roots | $y=Ae^{r_1x}+Be^{r_2x}$ |
| Repeated root | $y=(A+Bx)e^{rx}$ |
| Complex roots $\alpha\pm i\beta$ | $y=e^{\alpha x}(A\cos\beta x+B\sin\beta x)$ |
| Cauchy–Euler | try $y=x^r$ in $ax^2y''+bxy'+cy=0$ |
| No explicit $x$: $y''=f(y,y')$ | set $p=y'$, then $y''=p\frac{dp}{dy}$ | first-order in $p(y)$ |
| One known solution $y_1$ | $y_2=y_1\int\frac{e^{-\int P\,dx}}{y_1^2}\,dx$ | generates the second |
| Damped oscillator | $y''+2\zeta\omega y'+\omega^2y=0$ | $\zeta<1$ oscillates, $\zeta=1$ critical, $\zeta>1$ overdamped |
| Newton's cooling | $T-T_a=(T_0-T_a)e^{-kt}$ |
| Exponential growth | $P=P_0e^{kt}$ |

### D. Frontier

| Result | Statement |
|---|---|
| Clairaut $y=xp+f(p)$ | lines $y=cx+f(c)$ **plus** the singular envelope |
| Envelope | differentiate the family w.r.t. the parameter and eliminate it |
| Singular solution | satisfies the DE but is not a member of the general family |
| Lagrange $y=xf(y')+g(y')$ | differentiate ⇒ **linear** in $x(p)$; answer parametric in $p$ |
| Riccati $y'=q_0+q_1y+q_2y^2$ | no general quadrature; one known solution ⇒ linear in $u$ via $y=y_1+\frac1u$ |
| Picard–Lindelöf | $f$, $\partial f/\partial y$ continuous ⇒ **unique** solution |
| Lipschitz failure | $y'=y^{1/2}$, $y(0)=0$ has infinitely many solutions |

### E. Mistake checklist

1. Misclassifying the type — check separability, homogeneity, linearity *in that order* before starting.
2. Forgetting the arbitrary constant (or applying the initial condition too early).
3. Sign errors in the integrating factor $\mu=e^{\int P\,dx}$ (the integral, not its negative).
4. Applying the Bernoulli substitution when $n=0$ or $n=1$ — those are already linear.
5. Forgetting that an exact equation needs $M_y=N_x$ checked *before* searching for $F$.
6. Using $\ln y$ instead of $\ln\lvert y\rvert$ when the solution may be negative.
7. Forgetting the $Bxe^{rx}$ companion term for a repeated characteristic root.
8. Reporting only the family of lines from a Clairaut equation and missing the singular solution.
9. Dividing by $p=y'$ in a reduction of order without checking the branch $p=0$.
10. Applying Picard–Lindelöf when $\partial f/\partial y$ blows up at the initial point — uniqueness is not automatic.
11. Solving a Lagrange or Riccati equation for $\frac{dp}{dx}$ instead of inverting to get a **linear** equation.
12. Forgetting that a critically damped oscillator ($\zeta=1$) needs the $xe^{rx}$ term, not two distinct exponentials.
