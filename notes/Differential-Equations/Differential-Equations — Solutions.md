---
title: "Differential Equations — Solutions"
aliases: ["Differential Equations Solutions", "ODE Solutions"]
module: "Differential-Equations"
module_title: "Differential Equations"
type: solutions
tags: [differential-equations, solutions, olympiad, calculus, ode]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Differential-Equations — Paper|Paper]] · 📖 [[Differential-Equations|Complete Notes]]

# Differential Equations — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[Differential-Equations — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written — most by an
> independent RK4 numerical integration of $y'=f(x,y)$.

---

## A · Formation, order, degree & verification

#### **Q1**
**Method: highest derivative, then its power.** The highest derivative is $\frac{d^3y}{dx^3}$, so the order is $3$; it appears to the first power (the fourth power belongs to $y'$, a lower derivative), so the degree is $1$.
**Answer:** order $3$, degree $1$.

#### **Q2**
**Method: substitute.** $\frac{dy}{dx}=2e^{2x}$ and $2y=2e^{2x}$, so $\frac{dy}{dx}-2y=0$.
**Answer:** yes — it is a solution. (In fact $y=Ce^{2x}$ is the general solution.)

#### **Q3**
**Method: one parameter ⇒ differentiate once and eliminate $c$.** $\frac{dy}{dx}=c$, so $y=x\cdot\frac{dy}{dx}+\left(\frac{dy}{dx}\right)^2$.
**Answer:** $y=xy'+(y')^2$.

#### **Q4**
**Method: expand, differentiate, eliminate $a$.** $(x-a)^2+y^2=a^2\Rightarrow x^2+y^2=2ax$, so $a=\frac{x^2+y^2}{2x}$. Differentiating $x^2+y^2=2ax$ implicitly: $2x+2yy'=2a$, and substituting $a=\frac{x^2+y^2}{2x}$ gives $x+yy'=\frac{x^2+y^2}{2x}$, i.e. $2x^2+2xyy'=x^2+y^2$.
**Answer:** $x^2-y^2=2xy\dfrac{dy}{dx}$.

---

## B · Variables separable

#### **Q5**
**Method: separate and integrate.** $y\,dy=x\,dx\Rightarrow y^2=x^2+C$; $y(0)=1\Rightarrow C=1$, so $y=\sqrt{x^2+1}$ (positive branch).
**Answer:** $y(1)=\sqrt2\approx1.4142$. (Check: RK4 on $y'=x/y$ gives $1.41421$ ✓.)

#### **Q6**
**Method: separate.** $\frac{dy}{y}=dx\Rightarrow\ln y=x+C$; $y(0)=1\Rightarrow C=0$.
**Answer:** $y=e^x$; $y(1)=e\approx2.7183$. (Check: RK4 gives $2.71828$ ✓.)

#### **Q7**
**Method: separate.** $\frac{dy}{y}=2x\,dx\Rightarrow\ln y=x^2+C$; $y(0)=3\Rightarrow C=\ln3$.
**Answer:** $y=3e^{x^2}$; $y(1)=3e\approx8.1548$. (Check: RK4 gives $8.15485$ ✓.)

#### **Q8**
**Method: separate ($e^{x-y}=e^xe^{-y}$).** $e^y\,dy=e^xdx\Rightarrow e^y=e^x+C$; $y(0)=0\Rightarrow1=1+C$, $C=0$.
**Answer:** $e^y=e^x$, i.e. $y=x$. (Check: $y'=1$ and $e^{x-y}=e^0=1$ ✓.)

---

## C · Homogeneous equations

#### **Q9**
**Method: $y=vx$.** $v+xv'=1+v\Rightarrow xv'=1\Rightarrow v=\ln x+C$; $v(1)=0\Rightarrow C=0$, so $y=x\ln x$.
**Answer:** $y(e)=e\approx2.7183$. (Check: RK4 gives $2.71828$ ✓.)

#### **Q10**
**Method: $y=vx$.** $v+xv'=v+v^2\Rightarrow\frac{dv}{v^2}=\frac{dx}{x}\Rightarrow-\frac1v=\ln x+C$; $v(1)=1\Rightarrow C=-1$, so $v=\frac1{1-\ln x}$.
**Answer:** $y=\dfrac{x}{1-\ln x}$; $y(2)=\dfrac2{1-\ln2}\approx6.5178$. (Check: RK4 gives $6.51778$ ✓. Note the solution blows up as $x\to e$.)

#### **Q11**
**Method: $y=vx$.** $v+xv'=\frac1v+v\Rightarrow xv'=\frac1v\Rightarrow v\,dv=\frac{dx}{x}\Rightarrow\frac{v^2}{2}=\ln x+C$; $v(1)=1\Rightarrow C=\frac12$, so $v=\sqrt{2\ln x+1}$.
**Answer:** $y=x\sqrt{2\ln x+1}$; $y(e)=e\sqrt3\approx4.7082$. (Check: RK4 gives $4.70820$ ✓.)

---

## D · Linear first-order & Bernoulli

#### **Q12**
**Method: integrating factor $\mu=e^{\int1\,dx}=e^x$.** $\frac{d}{dx}(e^xy)=e^{2x}\Rightarrow e^xy=\frac12e^{2x}+C$; $y(0)=0\Rightarrow C=-\frac12$.
**Answer:** $y=\frac12(e^x-e^{-x})=\sinh x$; $y(1)=\sinh1\approx1.1752$. (Check: RK4 gives $1.17520$ ✓.)

#### **Q13**
**Method: $\mu=e^{2x}$, then by parts on $\int4xe^{2x}dx$.** $e^{2x}y=2xe^{2x}-e^{2x}+C$; $y(0)=1\Rightarrow C=2$.
**Answer:** $y=2x-1+2e^{-2x}$; $y(1)=1+\dfrac2{e^2}\approx1.2707$. (Check: RK4 gives $1.27067$ ✓.)

#### **Q14**
**Method: $P=\frac1x$, $\mu=e^{\ln x}=x$.** $\frac{d}{dx}(xy)=x^2\Rightarrow xy=\frac{x^3}{3}+C$; $y(1)=0\Rightarrow C=-\frac13$.
**Answer:** $y=\dfrac{x^2}{3}-\dfrac1{3x}$; $y(2)=\dfrac43-\dfrac16=\dfrac76\approx1.1667$. (Check: RK4 gives $1.16667$ ✓.)

#### **Q15**
**Method: Bernoulli with $n=2$ — substitute $u=y^{-1}$.** Dividing by $y^2$: $y^{-2}y'+y^{-1}=x$; with $u=y^{-1}$, $u'=-y^{-2}y'$, so $-u'+u=x$, i.e. $u'-u=-x$. With $\mu=e^{-x}$: $(ue^{-x})'=-xe^{-x}\Rightarrow ue^{-x}=e^{-x}(x+1)+C$; $u(0)=1\Rightarrow C=0$.
**Answer:** $u=x+1$, so $y=\dfrac1{x+1}$ and $y(1)=\dfrac12$. (Check: RK4 gives $0.5$ ✓; and $y'+y=x/(x+1)^2=xy^2$ ✓.)

#### **Q16**
**Method: $\mu=e^{2x}$.** $\frac{d}{dx}(e^{2x}y)=e^{x}\Rightarrow e^{2x}y=e^x+C$; $y(0)=1\Rightarrow1=1+C$, $C=0$.
**Answer:** $y=e^{-x}$. (Check: RK4 gives $e^{-1}=0.36788$ at $x=1$ ✓.)

---

## E · Exact equations & orthogonal trajectories

#### **Q17**
**Method: check exactness, then find the potential.** $\frac{\partial M}{\partial y}=1=\frac{\partial N}{\partial x}$, so exact. $F_x=2x+y\Rightarrow F=x^2+xy+\phi(y)$; $F_y=x+\phi'(y)=x+2y\Rightarrow\phi=y^2$. Hence $F=x^2+xy+y^2=C$; $y(0)=1\Rightarrow C=1$.
**Answer:** $x^2+xy+y^2=1$. (At $x=1$: $y=0$ or $y=-1$.)

#### **Q18**
**Method: exactness, then integrate.** $\frac{\partial M}{\partial y}=2x=\frac{\partial N}{\partial x}$, so exact. $F_x=3x^2+2xy\Rightarrow F=x^3+x^2y+\phi(y)$; $F_y=x^2+\phi'(y)=x^2+2y\Rightarrow\phi=y^2$. With $y(0)=1$: $C=1$.
**Answer:** $x^3+x^2y+y^2=1$.

#### **Q19**
**Method: orthogonal slope $-\frac1{y'}$.** From $y=cx^2$, $\frac{dy}{dx}=2cx=\frac{2y}{x}$, so the orthogonal slope is $-\frac{x}{2y}$. Then $2y\,dy=-x\,dx\Rightarrow y^2=-\frac{x^2}{2}+C$.
**Answer:** $x^2+2y^2=C$. (Check: slopes $\frac{2y}{x}$ and $-\frac{x}{2y}$ multiply to $-1$ ✓.)

#### **Q20**
**Method: orthogonal slope.** Circle slope $-\frac xy$; orthogonal slope $\frac yx$; separate: $\frac{dy}{y}=\frac{dx}{x}\Rightarrow\ln\lvert y\rvert=\ln\lvert x\rvert+C$.
**Answer:** $y=Cx$ — straight lines through the origin. (Check: $(-\frac xy)(\frac yx)=-1$ ✓.)

---

## F · Second-order linear

#### **Q21**
**Method: characteristic roots $r=\pm i$.** $y=A\cos x+B\sin x$; $y(0)=0\Rightarrow A=0$; $y'(0)=B=1$.
**Answer:** $y=\sin x$. (Check: RK4 system gives $1.00000$ at $x=\pi/2$ ✓.)

#### **Q22**
**Method: $r^2-3r+2=(r-1)(r-2)$.** $y=Ae^x+Be^{2x}$; $A+B=0$ and $A+2B=1\Rightarrow B=1$, $A=-1$.
**Answer:** $y=e^{2x}-e^x$; $y(1)=e^2-e\approx4.6708$. (Check: RK4 system gives $4.67077$ ✓.)

#### **Q23**
**Method: repeated root $r=-2$, so $y=(A+Bx)e^{-2x}$.** $y(0)=1\Rightarrow A=1$; $y'(0)=B-2A=0\Rightarrow B=2$.
**Answer:** $y=(1+2x)e^{-2x}$; $y(1)=3e^{-2}\approx0.4060$. (Check: RK4 system gives $0.40601$ ✓.)

#### **Q24**
**Method: Cauchy–Euler, try $y=x^r$.** $r(r-1)+r-1=r^2-1=0\Rightarrow r=\pm1$; $y=Ax+\frac Bx$; $A+B=0$, $A-B=1\Rightarrow A=\frac12$, $B=-\frac12$.
**Answer:** $y=\dfrac12\Big(x-\dfrac1x\Big)$; $y(2)=\dfrac34$. (Check: RK4 system gives $0.75000$ ✓.)

#### **Q25**
**Method: Cauchy–Euler.** $r(r-1)-2r+2=r^2-3r+2=0\Rightarrow r=1,2$; $y=Ax+Bx^2$; $A+B=1$, $A+2B=2\Rightarrow B=1$, $A=0$.
**Answer:** $y=x^2$; $y(3)=9$. (Check: RK4 system gives $9.00000$ ✓.)

---

## G · Applications

#### **Q26**
**Method: Newton's cooling, separable.** $T-20=(100-20)e^{-kt}=80e^{-kt}$. From $T(10)=60$: $40=80e^{-10k}$, so $e^{-10k}=\frac12$ and $e^{-20k}=\frac14$. Hence $T(20)=20+80\cdot\frac14=40$.
**Answer:** $40^\circ$C. (Check: with $k=\frac{\ln2}{10}$, $20+80e^{-2\ln2}=40$ ✓.)

#### **Q27**
**Method: exponential growth, separable.** $\frac{dP}{P}=0.1\,dt\Rightarrow P=1000e^{0.1t}$.
**Answer:** $P(10)=1000e\approx2718.28$.

#### **Q28**
**Method: integrating factor $\mu=e^x$, then $\int e^x\sin x\,dx$ by parts.** $\frac{d}{dx}(e^xy)=e^x\sin x\Rightarrow e^xy=\frac12e^x(\sin x-\cos x)+C$; $y(0)=0\Rightarrow0=\frac12(-1)+C$, $C=\frac12$.
**Answer:** $y=\dfrac{\sin x-\cos x}{2}+\dfrac{e^{-x}}{2}$; $y\!\left(\dfrac\pi2\right)=\dfrac{1+e^{-\pi/2}}{2}\approx0.6039$. (Check: RK4 gives $0.60394$ ✓.)

---

## H · Olympiad frontier

#### **Q29**
**Method: differentiate a Clairaut equation and split into two branches.** With $p=y'$, $y=xp+p^2$. Differentiating: $p=p+xp'+2pp'$, so $(x+2p)p'=0$.
- **Branch $p'=0$:** $p=c$ constant, giving the family of lines $y=cx+c^2$.
- **Branch $x+2p=0$:** $p=-\frac x2$, substituting back: $y=-\frac{x^2}{2}+\frac{x^2}{4}=-\frac{x^2}{4}$.
**Answer:** general solution $y=cx+c^2$; singular solution $y=-\dfrac{x^2}{4}$. (Check: at $x=2$, $y=-1$, $p=-1$, and $xp+p^2=2(-1)+1=-1=y$ ✓ — verified at $x=1,2,-3$.)

#### **Q30**
**Method: as Q29.** $p=y'$, differentiate $y=xp-p^2$: $(x-2p)p'=0$. Lines $y=cx-c^2$; envelope from $x-2p=0$, $p=\frac x2$: $y=\frac{x^2}{2}-\frac{x^2}{4}=\frac{x^2}{4}$.
**Answer:** $y=\dfrac{x^2}{4}$. (Check: at $x=2$, $y=1$, $p=1$, and $xp-p^2=2-1=1=y$ ✓.)

#### **Q31**
**Method: reduce the order by treating $p=y'$ as a function of $y$.** $y''=p\frac{dp}{dy}$, so $p\frac{dp}{dy}=\frac{p^2}{y}$, giving $\frac{dp}{p}=\frac{dy}{y}$ (for $p\ne0$), so $\ln p=\ln y+C$ and $p=Cy$. From $p(0)=y'(0)=1$ and $y(0)=1$: $C=1$. Then $y'=y$ with $y(0)=1$ gives $y=e^x$.
**Answer:** $y=e^x$. (Check: RK4 on the system $y'=u$, $u'=u^2/y$ gives $2.71828$ at $x=1$ ✓.)

#### **Q32**
**Method: characteristic roots $r=\pm1$.** $y=Ae^x+Be^{-x}$; $A+B=1$ and $A-B=0\Rightarrow A=B=\frac12$, so $y=\cosh x$.
**Answer:** $y=\cosh x$; $y(1)=\cosh1\approx1.5431$. (Check: RK4 system gives $1.54308$ ✓.)

#### **Q33**
**Method: two arbitrary constants ⇒ a second-order DE; differentiate twice and eliminate.** $y=c_1e^x+c_2e^{-x}$, $y'=c_1e^x-c_2e^{-x}$, $y''=c_1e^x+c_2e^{-x}=y$.
**Answer:** $y''-y=0$.

#### **Q34**
**Method: as Q33.** $y=ae^{2x}+be^{-2x}$, $y''=4ae^{2x}+4be^{-2x}=4y$.
**Answer:** $y''-4y=0$. (Check: for $(a,b,x)=(1,2,0.5),(3,-1,1),(-2,5,2)$, $y''-4y=0$ exactly ✓.)
