---
title: "Applications of Derivatives — Solutions"
aliases: ["Applications of Derivatives Solutions", "AOD Solutions"]
module: "Applications-of-Derivatives"
module_title: "Applications of Derivatives"
type: solutions
tags: [applications-of-derivatives, solutions, olympiad, calculus, optimisation]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Applications-of-Derivatives — Paper|Paper]] · 📖 [[Applications-of-Derivatives|Complete Notes]]

# Applications of Derivatives — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[Applications-of-Derivatives — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Rates of change & related rates

#### **Q1**
**Method: chain rule in time.** $A=\pi r^2\Rightarrow\dot A=2\pi r\,\dot r=2\pi r(2)=4\pi r$; at $r=5$: $20\pi$.
**Answer:** $20\pi\ \text{cm}^2/\text{s}\approx62.83$. (Check: finite difference of $\pi r^2$ at $r=5$ with $\dot r=2$ ✓.)

#### **Q2**
**Method: chain rule in time.** $V=s^3\Rightarrow\dot V=3s^2\dot s=3(100)(3)=900$.
**Answer:** $900\ \text{cm}^3/\text{min}$.

#### **Q3**
**Method: related rates, differentiate the relation first.** $x^2+y^2=169\Rightarrow2x\dot x+2y\dot y=0\Rightarrow\dot y=-\frac{x}{y}\dot x$. When $x=5$, $y=\sqrt{169-25}=12$, $\dot x=0.5$: $\dot y=-\frac{5}{12}(0.5)=-\frac{5}{24}$.
**Answer:** $-\dfrac{5}{24}\ \text{m/s}\approx-0.2083$ (descending).

#### **Q4**
**Method: chain rule in time.** $V=\frac43\pi r^3\Rightarrow\dot V=4\pi r^2\dot r\Rightarrow\dot r=\dfrac{100}{4\pi(100)}=\dfrac1{4\pi}$.
**Answer:** $\dfrac1{4\pi}\ \text{cm/s}\approx0.0796$.

---

## B · Tangents, normals & lengths

#### **Q5**
**Method: point + slope.** $f(2)=8-6=2$, $f'(2)=12-3=9$; $y-2=9(x-2)$.
**Answer:** $y=9x-16$.

#### **Q6**
**Method: normal slope $=-1/f'$.** $f(1)=1$, $f'(1)=2$; normal slope $-\frac12$: $y-1=-\frac12(x-1)$, i.e. $x+2y=3$.
**Answer:** $x+2y=3$.

#### **Q7**
**Method: angle between curves.** Slopes at $(1,1)$: $2x=2$ and $3x^2=3$. $\tan\theta=\left|\frac{2-3}{1+2\cdot3}\right|=\frac17$.
**Answer:** $\theta=\tan^{-1}\!\frac17\approx8.13^\circ$.

#### **Q8**
**Method: subtangent $|y/m|$, subnormal $|my|$.** At $x=1$: $y=1$, $m=3$.
**Answer:** subtangent $\frac13$, subnormal $3$.

#### **Q9**
**Method: tangent parallel to chord $\Rightarrow$ equal slopes.** Chord slope $\frac{9-1}{3-1}=4$; $f'=2x=4\Rightarrow x=2$, $y=4$.
**Answer:** $(2,4)$.

---

## C · Differentials & approximation

#### **Q10**
**Method: $f(x+\Delta x)\approx f(x)+f'(x)\Delta x$.** $f=\sqrt x$, $x=25$, $\Delta x=0.4$, $f'=\frac1{2\sqrt x}=\frac1{10}$: $5+\frac1{10}(0.4)=5.04$.
**Answer:** $5.04$ (true $\sqrt{25.4}=5.039841\ldots$).

#### **Q11**
**Method: differentials.** $f=x^{10}$, $x=1$, $\Delta x=0.01$, $f'=10x^9=10$: $1+10(0.01)=1.1$.
**Answer:** $1.1$ (true $1.104622\ldots$).

#### **Q12**
**Method: differentials.** $f=\ln x$, $x=1$, $\Delta x=0.02$, $f'=\frac1x=1$: $0+1(0.02)=0.02$.
**Answer:** $0.02$ (true $\ln1.02=0.019803\ldots$).

---

## D · Monotonicity

#### **Q13**
**Method: sign chart of $f'$.** $f'=3x^2-3=3(x-1)(x+1)>0$ for $|x|>1$.
**Answer:** $(-\infty,-1)\cup(1,\infty)$.

#### **Q14**
**Method: sign chart.** $f'=6x^2-18x+12=6(x-1)(x-2)>0$ outside $[1,2]$.
**Answer:** $(-\infty,1)\cup(2,\infty)$.

#### **Q15**
**Method: monotonicity + IVT.** $f'=3(x^2-1)$: increasing on $(-\infty,-1)$, decreasing on $(-1,1)$, increasing on $(1,\infty)$. Values $f(-2)=-1$, $f(-1)=3$, $f(1)=-1$, $f(2)=3$ — one sign change on each interval.
**Answer:** $3$ real roots. (Confirmed by a sign scan over $[-2,2]$ at step $10^{-3}$.)

#### **Q16**
**Method: $f'=0$ then classify.** $f'=1-\frac1x=0\Rightarrow x=1$; $f''=\frac1{x^2}>0$, a minimum; $f(1)=1-0=1$.
**Answer:** $1$.

---

## E · Maxima & minima

#### **Q17**
**Method: first derivative test.** $f'=3x^2-12x+9=3(x-1)(x-3)$; $+\to-$ at $x=1$; $f(1)=1-6+9+2=6$.
**Answer:** $6$.

#### **Q18**
**Method: first derivative test.** $f'=3(x^2-1)$: $+\to-$ at $x=-1$ (max $f(-1)=2$); $-\to+$ at $x=1$ (min $f(1)=-2$).
**Answer:** local max $2$ at $x=-1$; local min $-2$ at $x=1$.

#### **Q19**
**Method: second derivative test.** $f'=4x(x^2-2)$: $0,\pm\sqrt2$. $f''=12x^2-8$: $f''(0)=-8<0$ (max, $f(0)=0$); $f''(\pm\sqrt2)=24-8=16>0$ (min, $f=\pm4$).
**Answer:** local max $0$ at $x=0$; local minima $-4$ at $x=\pm\sqrt2$.

#### **Q20**
**Method: endpoints + critical points.** $f(-2)=-2$, $f(2)=2$, $f(-1)=2$, $f(1)=-2$.
**Answer:** max $2$ (at $x=-1,2$); min $-2$ (at $x=-2,1$).

#### **Q21**
**Method: $f'=0$ + verify.** $f'=1-\frac1{x^2}=0\Rightarrow x=1$ ($x>0$); $f''=\frac2{x^3}>0$; $f(1)=2$.
**Answer:** $2$.

#### **Q22**
**Method: closed-interval method.** Candidates: endpoints $\frac12$ ($f=\frac52$) and $4$ ($f=\frac{17}{4}$), plus $f'=0\Rightarrow x=1$ ($f=2$).
**Answer:** min $2$ at $x=1$; max $\dfrac{17}{4}$ at $x=4$.

---

## F · Convexity, inflection & sketching

#### **Q23**
**Method: $f''=0$ + sign change.** $f''=6x$, zero at $0$, negative then positive; $f(0)=0$.
**Answer:** $(0,0)$.

#### **Q24**
**Method: sign of $f''$.** $f''=6x-6=6(x-1)>0$ for $x>1$.
**Answer:** $(1,\infty)$.

#### **Q25**
**Method: count zeros of $f'$ with a sign change.** $f'=4x^3-8x=4x(x^2-2)$ has three distinct real zeros, each a sign change.
**Answer:** $3$.

#### **Q26**
**Method: $f''=0$ + sign change.** $f''=12x^2-8=0\Rightarrow x=\pm\frac1{\sqrt3}$, and $f''$ changes sign at both. $f\!\left(\pm\frac1{\sqrt3}\right)=\frac19-\frac43=-\frac{11}9$.
**Answer:** $\left(\pm\dfrac1{\sqrt3},-\dfrac{11}{9}\right)$.

---

## G · Optimisation

#### **Q27**
**Method: one variable.** $P=x(20-x)$, $P'=20-2x=0\Rightarrow x=10$; $P''=-2<0$.
**Answer:** $10$ and $10$; product $100$.

#### **Q28**
**Method: constraint → one variable, then endpoints.** $V=x(12-2x)^2$ on $0\le x\le6$; $V'=(12-2x)(12-6x)=0\Rightarrow x=2$ (the other root $x=6$ is an endpoint giving $V=0$). $V(2)=2\cdot64=128$.
**Answer:** $x=2$, max volume $128$.

#### **Q29**
**Method: symmetric reduction (or Lagrange).** Fix $y+z=s$, so $yz\le\frac{s^2}4$ with equality at $y=z$; then $xyz\le x\frac{(1-x)^2}4$, maximised at $x=\frac13$. Lagrange gives the same: $yz=xz=xy\Rightarrow x=y=z=\frac13$.
**Answer:** $\dfrac1{27}$ at $x=y=z=\dfrac13$.

#### **Q30**
**Method: parametrise the ellipse.** Vertices $(\pm a\cos\theta,\pm b\sin\theta)$, area $4ab\sin\theta\cos\theta=2ab\sin2\theta\le2ab$, equality when $\sin2\theta=1$.
**Answer:** $2ab$.

---

## H · Olympiad frontier

#### **Q31**
**Method: Jensen.** $f(x)=e^x$ is convex since $f''=e^x>0$. With weights $\frac13,\frac13,\frac13$ summing to $1$:
$$\frac{e^a+e^b+e^c}{3}\ge e^{(a+b+c)/3},$$
with equality iff $a=b=c$ (strict convexity).
**Answer:** Jensen with $f(x)=e^x$; equality iff $a=b=c$. (Check $(a,b,c)=(1,2,3)$: LHS $14.154$, RHS $e^2=7.389$ ✓.)

#### **Q32**
**Method: Lagrange multipliers, or complete the square.** Lagrange: $\nabla(x^2+y^2+z^2)=\lambda\nabla(x+y+z)$ gives $2x=2y=2z=\lambda$, so $x=y=z$; with $x+y+z=3$, $x=y=z=1$ and the value is $3$.
Algebraically: $x^2+y^2+z^2-\frac{(x+y+z)^2}{3}=\frac13\big[(x-y)^2+(y-z)^2+(z-x)^2\big]\ge0$, so $x^2+y^2+z^2\ge\frac{9}{3}=3$.
**Answer:** $3$ at $x=y=z=1$. (Check: the feasible perturbation $(1.2,0.9,0.9)$ has the same sum but value $1.44+0.81+0.81=3.06>3$ ✓.)

#### **Q33**
**Method: fix the partial sum, reduce to one variable (the AM–GM proof).** Fix $y+z=s$. Then $yz$ is maximised at $y=z=\frac{s}{2}$, since $\frac{d}{dy}[y(s-y)]=s-2y=0$. So $xyz\le x\frac{s^2}{4}$ with $x+s=3$ fixed... more precisely write $t=x+y+z$; then
$$\frac{x+y+z}{3}\ge\sqrt[3]{xyz}$$
because for fixed sum the product is largest when the variables are equal. Justification: with $z=t-x-y$, $xyz=x y(t-x-y)$; $\partial/\partial y$ and $\partial/\partial x$ both vanish only at $x=y=z=\frac t3$, and the boundary (some variable $\to0$) gives product $0$, so the interior critical point is the global maximum.
**Answer:** $\dfrac{x+y+z}{3}\ge\sqrt[3]{xyz}$, equality iff $x=y=z$. (Check $(x,y,z)=(1,2,3)$: mean $2$ vs $\sqrt[3]{6}=1.817$ ✓.)

#### **Q34**
**Method: substitute and show the discriminant vanishes.** Substituting $y=mx+\frac am$ into $y^2=4ax$ gives
$$m^2x^2-2ax+\frac{a^2}{m^2}=0,$$
whose discriminant is $(-2a)^2-4m^2\cdot\frac{a^2}{m^2}=4a^2-4a^2=0$ — exactly one root, so the line is tangent. The root is $x=\dfrac{2a}{2m^2}=\dfrac{a}{m^2}$, and then $y=m\cdot\frac{a}{m^2}+\frac am=\dfrac{2a}{m}$. Eliminating $m$ via $m^2=\frac ax$ gives $y^2=4ax$, the envelope.
**Answer:** contact at $\left(\dfrac{a}{m^2},\dfrac{2a}{m}\right)$; the envelope is $y^2=4ax$. (Verified: for $a=2$ and $m\in\{0.25,0.5,1,2,4\}$ the discriminant is exactly $0$ and $y^2=4ax$ at each contact point ✓.)
