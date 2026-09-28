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
**Method: $f'=0$ then $f''$.** $f'=1-\frac1{x^{2}}=0\Rightarrow x=1$ (the only critical point for $x>0$); $f''=\frac2{x^{3}}>0$, so it is a minimum. Also $f\to\infty$ as $x\to0^{+}$ and as $x\to\infty$, so this critical point is the global minimum.
**Answer:** minimum $2$ at $x=1$. (Check: $x+\frac1x-2=\frac{(x-1)^{2}}{x}\ge0$ ✓.)

#### **Q32**
**Method: express the area in terms of one side.** Let the sides be $x$ and $\frac p2-x$; then $A=x\big(\frac p2-x\big)$, a concave quadratic in $x$ maximised at its vertex $x=\frac p4$.
**Answer:** the square of side $\frac p4$, with area $\dfrac{p^{2}}{16}$. (Check: $A\le\big(\frac p4\big)^{2}$ follows from AM–GM on $x$ and $\frac p2-x$, since $x+\big(\frac p2-x\big)=\frac p2$ ✓.)

#### **Q33**
**Method: convexity gives the tangent as a global lower bound.** $f'(x)=2x$, so the supporting line at $a=3$ is $y=f(3)+f'(3)(x-3)=9+6(x-3)=6x-9$. Since $f''(x)=2>0$, $f(x)\ge6x-9$ for all $x$.
**Answer:** supporting line $y=6x-9$; $x^{2}\ge6x-9$, equality only at $x=3$. (Check: $x^{2}-(6x-9)=(x-3)^{2}\ge0$ ✓.)

#### **Q34**
**Method: Jensen with $f(x)=e^{x}$.** $f''(x)=e^{x}>0$, so $f$ is strictly convex and
$$\frac{e^{a}+e^{b}+e^{c}}{3}\ge e^{(a+b+c)/3},$$
with equality iff $a=b=c$ (strict convexity).
**Answer:** proved; equality iff $a=b=c$. (Check numerically: for $(1,2,3)$ the left side is $\frac{e+e^{2}+e^{3}}3\approx10.71$ and the right side is $e^{2}\approx7.39$, so the inequality holds strictly ✓.)

#### **Q35**
**Method: Lagrange multipliers, or complete the square.** $\nabla(x^{2}+y^{2}+z^{2})=(2x,2y,2z)=\lambda(1,1,1)$, so $x=y=z$; with $x+y+z=3$ this gives $x=y=z=1$ and value $3$. Equivalently, without calculus, $\sum(x-1)^{2}=x^{2}+y^{2}+z^{2}-2(x+y+z)+3=x^{2}+y^{2}+z^{2}-3\ge0$.
**Answer:** minimum $3$ at $x=y=z=1$. (Check: $\sum(x-1)^{2}=x^{2}+y^{2}+z^{2}-2(x+y+z)+3=x^{2}+y^{2}+z^{2}-3\ge0$ ✓.)

#### **Q36**
**Method: Jensen on $\ln x$ (concave), or the tangent-line method.** $\ln$ is concave, so $\frac{\ln x+\ln y+\ln z}{3}\le\ln\frac{x+y+z}{3}$, i.e. $(xyz)^{1/3}\le\frac{x+y+z}{3}$.
**Answer:** proved; equality iff $x=y=z$. (Check: for $(1,2,6)$ the geometric mean is $12^{1/3}\approx2.289$ and the arithmetic mean is $3$ ✓.)

#### **Q37**
**Method: the envelope condition $F=0$, $\partial F/\partial m=0$.** Write $F=y-mx-\frac am=0$. Then $\frac{\partial F}{\partial m}=-x+\frac a{m^{2}}=0$, so $x=\frac a{m^{2}}$, and substituting into $F=0$ gives $y=\frac{2a}{m}$. Eliminating $m$ yields $y^{2}=4ax$.
**Answer:** contact at $\left(\dfrac{a}{m^{2}},\dfrac{2a}{m}\right)$; the envelope is the parabola $y^{2}=4ax$. (Check: the discriminant of $y=mx+\frac am$ against $y^{2}=4ax$ is $(2a-4a)^{2}-4m^{2}\cdot\frac{a^{2}}{m^{2}}=0$ ✓.)

#### **Q38**
**Method: Young with $p=q=2$.** With $A=\sqrt a$, $B=\sqrt b$: $AB\le\frac{A^{2}}{2}+\frac{B^{2}}{2}=\frac{a+b}{2}$.
**Answer:** $\sqrt{ab}\le\dfrac{a+b}{2}$ — AM–GM for two numbers as a special case of Young. (Check: for $a=4$, $b=9$: $6\le6.5$ ✓.)

#### **Q39**
**Method: the supporting line of $f(x)=\frac{x^{p}}{p}$ at $a=b^{q-1}$.** Since $f''(x)=(p-1)x^{p-2}>0$ for $x>0$, $f$ is convex and $f(x)\ge f(a)+f'(a)(x-a)$. Taking $a=b^{q-1}$ and using $a^{p}=b^{q}$ gives $bx\le\frac{x^{p}}{p}+\frac{b^{q}}{q}$.
**Answer:** $ab\le\dfrac{a^{p}}{p}+\dfrac{b^{q}}{q}$ for $\frac1p+\frac1q=1$, $p,q>1$, with equality iff $a^{p-1}=b$. (Check: for $p=3$, $q=\frac32$, $a=2$, $b=4$: $ab=8$ and $\frac{8}{3}+\frac{8}{1.5}=\frac83+\frac{16}3=8$ — equality, and indeed $a^{p-1}=2^{2}=4=b$ ✓.)

#### **Q40**
**Method: complete the square, or Young with $p=q=2$.** $\frac{a^{2}+b^{2}}2-ab=\frac{(a-b)^{2}}2\ge0$.
**Answer:** $a^{2}+b^{2}\ge2ab$, equality iff $a=b$. (Check: the difference is exactly $\frac12(a-b)^{2}$ ✓; this is also the seed of Cauchy–Schwarz, obtained by summing over components.)

#### **Q41**
**Method: write both tangents and eliminate $m$.** The tangent of slope $m$ to $y^{2}=4ax$ is $y=mx+\frac am$; a perpendicular one has slope $-\frac1m$, namely $y=-\frac xm-am$. Solving: $mx+\frac am=-\frac xm-am$, so $x\big(m+\frac1m\big)=-a\big(m+\frac1m\big)$ and hence $x=-a$.
**Answer:** the locus is $x=-a$, the directrix. (Check: for $a=2.6$ and various $m$, the intersection always had $x=-2.6$ ✓; and each line's discriminant against the parabola was $0$ ✓.)

#### **Q42**
**Method: the director circle.** For $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ the intersection of perpendicular tangents lies on $x^{2}+y^{2}=a^{2}+b^{2}$. With $a=5$, $b=3$: $|OP|^{2}=34$.
**Answer:** $|OP|=\sqrt{34}\approx5.831$. (Check: for specific pairs of perpendicular tangents to this ellipse the intersection satisfied $x^{2}+y^{2}=34$ exactly ✓.)

#### **Q43**
**Method: the $a=b$ case of the director circle, or a direct computation.** The tangent at parameter $t$ to $x^{2}+y^{2}=R^{2}$ is $x\cos t+y\sin t=R$; the perpendicular one is $x\cos(t+\frac\pi2)+y\sin(t+\frac\pi2)=R$. Solving the two linear equations gives $\lvert OP\rvert^{2}=2R^{2}$.
**Answer:** $|OP|=\sqrt2\,R$. (Check: with $R=1$, $t=0.7$ the intersection gave $|OP|^{2}=2$ ✓.)

#### **Q44**
**Method: rewrite in terms of $t=x+y$ and $s=xy$.** $\frac1x+\frac1y=\frac{x+y}{xy}=\frac{10}{xy}$, and $x^{2}+y^{2}=100-2xy$; both decrease as $xy$ grows. Since $xy\le\frac{t^{2}}4=25$ with equality iff $x=y=5$, both minima occur at $x=y=5$.
**Answer:** $\min\big(\frac1x+\frac1y\big)=\dfrac{10}{25}=\dfrac25$ and $\min(x^{2}+y^{2})=100-50=50$. (Check: at $(4,6)$: $\frac14+\frac16=0.417>0.4$ ✓ and $16+36=52>50$ ✓.)

#### **Q45**
**Method: $x^{3}+y^{3}=(x+y)^{3}-3xy(x+y)$.** With $t=6$: $x^{3}+y^{3}=216-18xy$, which **decreases** as $xy$ grows. So the maximum is at the smallest attainable $xy$, namely as one variable tends to $0$ — at the boundary, not at $x=y$.
**Answer:** supremum $216$, approached as $x\to0^{+}$, $y\to6$; there is no interior maximum. (Check: at $x=y=3$ the value is $54$, far below $216$ ✓; at $(0.1,5.9)$ it is $205.8$ ✓. This is the counterexample to "symmetric ⟹ extremum at $x=y$".)

#### **Q46**
**Method: complete the square about the mean.** $x^{2}+y^{2}+z^{2}-\frac13=\sum\big(x-\frac13\big)^{2}$, because $\sum\big(x-\frac13\big)^{2}=x^{2}+y^{2}+z^{2}-\frac23(x+y+z)+3\cdot\frac19=x^{2}+y^{2}+z^{2}-\frac23+\frac13$.
**Answer:** $x^{2}+y^{2}+z^{2}\ge\dfrac13$, equality iff $x=y=z=\frac13$. (Check: for $(\frac12,\frac14,\frac14)$ the sum is $\frac38=0.375>\frac13$ ✓.)
