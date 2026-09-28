---
title: "Differential Equations — Olympiad Paper"
aliases: ["Differential Equations Paper", "ODE Paper"]
module: "Differential-Equations"
module_title: "Differential Equations"
type: paper
tags: [differential-equations, paper, olympiad, calculus, ode]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Differential-Equations|Chapter 6]] · 📖 [[Differential-Equations|Complete Notes]] · ✅ [[Differential-Equations — Solutions|Solutions]] ➡

# Differential Equations — Olympiad Paper

> **34 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Differential-Equations — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · Formation, order, degree & verification (Q1–Q4)

#### **Q1**[JEE Main][order degree]State the order and degree of $\dfrac{d^3y}{dx^3}+\left(\dfrac{dy}{dx}\right)^4+y=0$.

**Answer:** order $3$, degree $1$

#### **Q2**[JEE Main][verification]Verify that $y=e^{2x}$ solves $\dfrac{dy}{dx}-2y=0$.

**Answer:** yes — $\frac{dy}{dx}=2e^{2x}=2y$

#### **Q3**[JEE Main][formation]Form the DE of the family $y=cx+c^2$.

**Answer:** $y=xy'+(y')^2$

#### **Q4**[JEE Adv][formation]Form the DE of the circles $(x-a)^2+y^2=a^2$.

**Answer:** $x^2-y^2=2xy\dfrac{dy}{dx}$

---

## B · Variables separable (Q5–Q8)

#### **Q5**[JEE Main][separable]Solve $\dfrac{dy}{dx}=\dfrac xy$ with $y(0)=1$; find $y(1)$.

**Answer:** $y=\sqrt{x^2+1}$, so $y(1)=\sqrt2\approx1.4142$

#### **Q6**[JEE Main][separable]Solve $\dfrac{dy}{dx}=y$ with $y(0)=1$; find $y(1)$.

**Answer:** $y=e^x$, so $y(1)=e\approx2.7183$

#### **Q7**[JEE Main][separable]Solve $\dfrac{dy}{dx}=2xy$ with $y(0)=3$; find $y(1)$.

**Answer:** $y=3e^{x^2}$, so $y(1)=3e\approx8.1548$

#### **Q8**[JEE Adv][separable]Solve $\dfrac{dy}{dx}=e^{x-y}$ with $y(0)=0$.

**Answer:** $y=x$

---

## C · Homogeneous equations (Q9–Q11)

#### **Q9**[JEE Main][homogeneous]Solve $\dfrac{dy}{dx}=\dfrac{x+y}{x}$ with $y(1)=0$; find $y(e)$.

**Answer:** $y=x\ln x$, so $y(e)=e\approx2.7183$

#### **Q10**[JEE Adv][homogeneous]Solve $\dfrac{dy}{dx}=\dfrac yx+\left(\dfrac yx\right)^2$ with $y(1)=1$; find $y(2)$.

**Answer:** $y=\dfrac{x}{1-\ln x}$, so $y(2)=\dfrac2{1-\ln2}\approx6.5178$

#### **Q11**[JEE Adv][homogeneous]Solve $\dfrac{dy}{dx}=\dfrac{x^2+y^2}{xy}$ with $y(1)=1$; find $y(e)$.

**Answer:** $y=x\sqrt{2\ln x+1}$, so $y(e)=e\sqrt3\approx4.7082$

---

## D · Linear first-order & Bernoulli (Q12–Q16)

#### **Q12**[JEE Main][linear]Solve $\dfrac{dy}{dx}+y=e^x$ with $y(0)=0$; find $y(1)$.

**Answer:** $y=\sinh x$, so $y(1)=\sinh1\approx1.1752$

#### **Q13**[JEE Main][linear]Solve $\dfrac{dy}{dx}+2y=4x$ with $y(0)=1$; find $y(1)$.

**Answer:** $y=2x-1+2e^{-2x}$, so $y(1)=1+\dfrac2{e^2}\approx1.2707$

#### **Q14**[JEE Adv][linear]Solve $\dfrac{dy}{dx}+\dfrac yx=x$ with $y(1)=0$; find $y(2)$.

**Answer:** $y=\dfrac{x^2}{3}-\dfrac1{3x}$, so $y(2)=\dfrac76\approx1.1667$

#### **Q15**[Olympiad][Bernoulli]Solve $\dfrac{dy}{dx}+y=xy^2$ with $y(0)=1$; find $y(1)$.

**Answer:** $y=\dfrac1{x+1}$, so $y(1)=\dfrac12$

#### **Q16**[JEE Adv][linear]Solve $\dfrac{dy}{dx}+2y=e^{-x}$ with $y(0)=1$.

**Answer:** $y=e^{-x}$

---

## E · Exact equations & orthogonal trajectories (Q17–Q20)

#### **Q17**[JEE Adv][exact]Solve $(2x+y)\,dx+(x+2y)\,dy=0$ with $y(0)=1$.

**Answer:** $x^2+xy+y^2=1$

#### **Q18**[JEE Adv][exact]Solve $(3x^2+2xy)\,dx+(x^2+2y)\,dy=0$ with $y(0)=1$.

**Answer:** $x^3+x^2y+y^2=1$

#### **Q19**[JEE Adv][orthogonal]Find the orthogonal trajectories of $y=cx^2$.

**Answer:** $x^2+2y^2=C$

#### **Q20**[JEE Adv][orthogonal]Find the orthogonal trajectories of $x^2+y^2=c$.

**Answer:** $y=Cx$

---

## F · Second-order linear (Q21–Q25)

#### **Q21**[JEE Main][second order]Solve $y''+y=0$ with $y(0)=0$, $y'(0)=1$.

**Answer:** $y=\sin x$

#### **Q22**[JEE Adv][second order]Solve $y''-3y'+2y=0$ with $y(0)=0$, $y'(0)=1$; find $y(1)$.

**Answer:** $y=e^{2x}-e^x$, so $y(1)=e^2-e\approx4.6708$

#### **Q23**[JEE Adv][second order]Solve $y''+4y'+4y=0$ with $y(0)=1$, $y'(0)=0$; find $y(1)$.

**Answer:** $y=(1+2x)e^{-2x}$, so $y(1)=3e^{-2}\approx0.4060$

#### **Q24**[JEE Adv][Cauchy–Euler]Solve $x^2y''+xy'-y=0$ with $y(1)=0$, $y'(1)=1$; find $y(2)$.

**Answer:** $y=\dfrac12\Big(x-\dfrac1x\Big)$, so $y(2)=\dfrac34$

#### **Q25**[JEE Adv][Cauchy–Euler]Solve $x^2y''-2xy'+2y=0$ with $y(1)=1$, $y'(1)=2$; find $y(3)$.

**Answer:** $y=x^2$, so $y(3)=9$

---

## G · Applications & higher-order structure (Q26–Q31)

#### **Q26**[JEE Main][cooling]A body at $100^\circ$C cools in a $20^\circ$C room; after $10$ min it reads $60^\circ$C. Find the temperature after $20$ min.

**Answer:** $40^\circ$C

#### **Q27**[JEE Main][growth]A population of $1000$ grows at $10\%$ per year. Find $P(10)$.

**Answer:** $1000e\approx2718.28$

#### **Q28**[JEE Adv][linear]Solve $\dfrac{dy}{dx}+y=\sin x$ with $y(0)=0$; find $y\!\left(\dfrac\pi2\right)$.

**Answer:** $y=\dfrac{\sin x-\cos x}{2}+\dfrac{e^{-x}}{2}$, so $y\!\left(\dfrac\pi2\right)=\dfrac{1+e^{-\pi/2}}{2}\approx0.6039$

#### **Q29**[JEE Adv][damping]Solve $y''+2y'+5y=0$ with $y(0)=0$, $y'(0)=2$; state the damping regime and find $y(1)$.

**Answer:** $y=e^{-x}\sin 2x$, under-damped ($\zeta=\frac{1}{\sqrt5}<1$); $y(1)\approx0.334512$

#### **Q30**[JEE Adv][damping]Classify and solve $y''+3y'+2y=0$ with $y(0)=0$, $y'(0)=1$.

**Answer:** over-damped ($r=-1,-2$); $y=e^{-x}-e^{-2x}$, so $y(1)\approx0.232544$

#### **Q31**[JEE Adv][reduction of order]Solve $yy''=(y')^{2}$ with $y(0)=1$, $y'(0)=1$.

**Answer:** $y=e^{x}$ (set $p=y'$ as a function of $y$, so $y''=p\frac{dp}{dy}$)

---

## H · Olympiad frontier (Q32–Q41)

#### **Q32**[Olympiad][Clairaut]Solve $y=xy'+(y')^{2}$ and find its singular solution.

**Answer:** general $y=cx+c^{2}$; singular solution $y=-\dfrac{x^{2}}{4}$

#### **Q33**[Olympiad][Clairaut]Find the singular solution of $y=xy'-(y')^{2}$.

**Answer:** general $y=cx-c^{2}$; singular solution $y=\dfrac{x^{2}}{4}$

#### **Q34**[Olympiad][reduction of order]Given that $y=\sin x$ solves $y''+y=0$, find a second independent solution and the general solution.

**Answer:** $y_{2}=-\cos x$ (Wronskian $-1$); general solution $y=A\sin x+B\cos x$

#### **Q35**[Olympiad][reduction of order]Given that $y=x$ solves $x^{2}y''-2xy'+2y=0$, find the general solution.

**Answer:** $y=Ax+Bx^{2}$

#### **Q36**[Olympiad][non-uniqueness]Exhibit two distinct solutions of $y'=y^{1/2}$ with $y(0)=0$, and explain why Picard–Lindelöf does not force uniqueness here.

**Answer:** $y=0$ and $y=\dfrac{x^{2}}{4}$ ($x\ge0$); $\frac{\partial f}{\partial y}=\frac{1}{2\sqrt y}\to\infty$ as $y\to0^{+}$, so $f$ is not Lipschitz at the initial point

#### **Q37**[Olympiad][non-uniqueness]Show that $y'=y^{1/3}$, $y(0)=0$, has a solution equal to $0$ for $x\le1$ and positive for $x>1$.

**Answer:** $y=\begin{cases}0,&x\le1\\[2pt]\big(\frac{2(x-1)}{3}\big)^{3/2},&x>1\end{cases}$

#### **Q38**[Olympiad][Lagrange]Solve $y=x(y')^{2}+1$.

**Answer:** parametric in $p=y'$: $x=\dfrac{C}{(1-p)^{2}},\ y=1+\dfrac{Cp^{2}}{(1-p)^{2}}$

#### **Q39**[Olympiad][Riccati]Solve $y'=y^{2}-y$, given that $y=0$ is a solution.

**Answer:** $y=\dfrac{1}{1+Ce^{x}}$ (substitute $y=\frac1u$)

#### **Q40**[Olympiad][Riccati]Solve $y'=x\big(y^{2}-1\big)$, given that $y=1$ is a solution.

**Answer:** $y=1+\dfrac{1}{Ce^{-x^{2}}-\frac12}$

#### **Q41**[Olympiad][formation]Form the differential equation whose general solution is $y=c_{1}e^{x}+c_{2}e^{-x}$.

**Answer:** $y''-y=0$

---

> [!note] Exam technique notes
> - Identify the type first: separable? homogeneous? linear? exact? — in that order.
> - For a linear first-order DE, write $y'+P(x)y=Q(x)$ in standard form *before*
>   computing the integrating factor.
> - If $x$ is absent from a second-order equation, set $p=y'$ and use
>   $y''=p\frac{dp}{dy}$ — this is the single most useful reduction available.
> - In a Clairaut equation, always look for **both** the family of lines and the
>   singular (envelope) solution.
> - For a Riccati equation, hunt for one particular solution first; without it
>   there is no general closed form.
> - Before invoking uniqueness, check that $\partial f/\partial y$ is finite at
>   the initial point.
> - Check every solution by substituting it back, and verify the initial condition.
