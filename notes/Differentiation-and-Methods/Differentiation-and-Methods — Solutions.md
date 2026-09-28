---
title: "Differentiation and Method of Differentiation — Solutions"
aliases: ["Differentiation Solutions", "Methods of Differentiation Solutions"]
module: "Differentiation-and-Methods"
module_title: "Differentiation and Method of Differentiation"
type: solutions
tags: [differentiation-and-methods, solutions, olympiad, calculus]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Differentiation-and-Methods — Paper|Paper]] · 📖 [[Differentiation-and-Methods|Complete Notes]]

# Differentiation and Method of Differentiation — Solutions

> Full solutions to all 38 questions, same Q-ids as the [[Differentiation-and-Methods — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · From the definition & differentiability

#### **Q1**
**Method: power rule / definition.** $(x^3)'=3x^2$, so $f'(2)=3\cdot4=12$.
**Answer:** $12$. (Check: finite difference $\frac{2.000001^3-8}{10^{-6}}\approx12$ ✓.)

#### **Q2**
**Method: difference quotient.** $\frac{\frac1{x+h}-\frac1x}{h}=\frac{-1}{x(x+h)}\to-\frac1{x^2}$.
**Answer:** $-\dfrac1{x^{2}}$.

#### **Q3**
**Method: one-sided derivatives.** $\frac{|h|}{h}=+1$ (right), $-1$ (left); unequal.
**Answer:** not differentiable at $0$.

#### **Q4**
**Method: one-sided derivatives.** $x|x|=x^2$ ($x>0$), $-x^2$ ($x<0$); both one-sided derivatives are $0$.
**Answer:** differentiable, $f'(0)=0$.

---

## B · Rules: product, quotient, power

#### **Q5**
**Method: product rule.** $(xe^x)'=e^x+xe^x=e^x(1+x)$; at $x=0$, $=1$.
**Answer:** $1$. (Check: finite difference $\approx1.0000005$ ✓.)

#### **Q6**
**Method: quotient rule.** $\frac{1\cdot(1+x^2)-x\cdot2x}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2}$.
**Answer:** $\dfrac{1-x^2}{(1+x^2)^2}$.

#### **Q7**
**Method: product rule.** $(x^3\sin x)'=3x^2\sin x+x^3\cos x$; at $x=\pi/2$, $\sin=1,\cos=0$, so $=3(\pi/2)^2=\frac{3\pi^2}{4}$.
**Answer:** $\dfrac{3\pi^2}{4}\approx7.4022$. (Check: finite difference ✓.)

#### **Q8**
**Method: power rule.** $(x^{1/2})'=\frac12 x^{-1/2}=\frac1{2\sqrt x}$.
**Answer:** $\dfrac1{2\sqrt x}$.

#### **Q9**
**Method: quotient rule.** $\frac{2x(x+1)-x^2}{(x+1)^2}=\frac{x^2+2x}{(x+1)^2}$.
**Answer:** $\dfrac{x^2+2x}{(x+1)^2}$.

#### **Q10**
**Method: power rule term-by-term.** $12x^3-2$.
**Answer:** $12x^3-2$.

---

## C · Chain rule & standard functions

#### **Q11**
**Method: chain rule.** $\cos(3x)\cdot3=3\cos(3x)$; at $0$, $=3$.
**Answer:** $3$.

#### **Q12**
**Method: chain rule.** $e^{x^2}\cdot2x$.
**Answer:** $2x\,e^{x^{2}}$. (At $x=1$: $2e\approx5.4366$ ✓.)

#### **Q13**
**Method: chain rule.** $\frac1{\sin x}\cos x=\cot x$.
**Answer:** $\cot x$.

#### **Q14**
**Method: chain rule.** $-\sin(x^3)\cdot3x^2=-3x^2\sin(x^3)$.
**Answer:** $-3x^{2}\sin(x^{3})$.

#### **Q15**
**Method: standard inverse-trig derivative.** $\frac1{1+x^2}$ at $x=1$ is $\frac12$.
**Answer:** $\dfrac12$.

#### **Q16**
**Method: chain rule on arcsin.** $\frac1{\sqrt{1-(2x)^2}}\cdot2=\frac2{\sqrt{1-4x^2}}$.
**Answer:** $\dfrac{2}{\sqrt{1-4x^{2}}}$.

---

## D · Implicit, logarithmic, parametric

#### **Q17**
**Method: implicit.** $2x+2y\,y'=0\Rightarrow y'=-x/y$; at $(3,4)$, $=-\frac34$.
**Answer:** $-\dfrac34$.

#### **Q18**
**Method: logarithmic.** $\ln f=x\ln x\Rightarrow f'/f=\ln x+1\Rightarrow f'=x^x(1+\ln x)$; at $x=1$, $=1\cdot1=1$.
**Answer:** $f'(1)=1$. (Check: finite difference of $x^x$ at $1$ gives $\approx1.0000003$ ✓.)

#### **Q19**
**Method: parametric.** $\frac{dy/dt}{dx/dt}=\frac{3t^2}{2t}=\frac{3t}{2}$; at $t=1$, $=\frac32$.
**Answer:** $\dfrac32$.

#### **Q20**
**Method: parametric.** $\frac{dy/dt}{dx/dt}=\frac{b\cos t}{-a\sin t}=-\frac ba\cot t$.
**Answer:** $-\dfrac{b}{a}\cot t$.

#### **Q21**
**Method: second parametric derivative.** $\frac{dy}{dx}=\frac{3t}{2}$; $\frac{d^2y}{dx^2}=\frac{(3/2)}{2t}=\frac{3}{4t}$; at $t=1$, $=\frac34$.
**Answer:** $\dfrac34$.

---

## E · Higher-order & nth derivatives

#### **Q22**
**Method: iterate.** $(\sin x)''=-\sin x$; at $\pi/2$, $=-1$.
**Answer:** $-1$.

#### **Q23**
**Method: pattern.** $(e^{2x})^{(n)}=2^ne^{2x}$; for $n=3$ at $0$, $2^3=8$.
**Answer:** $8$.

#### **Q24**
**Method: Leibniz with $f=x^2$, $g=e^x$.** Only $k=n,n-1,n-2$ survive: $e^x\big(x^2+2nx+n(n-1)\big)$.
**Answer:** $e^{x}\big(x^{2}+2nx+n(n-1)\big)$. (Check $n=1$: $e^x(x^2+2x)$; direct product rule gives $(x^2+2x)e^x$ ✓.)

#### **Q25**
**Method: pattern.** $(1-x)^{-1}\to(1-x)^{-2}\to2(1-x)^{-3}\to\cdots\to n!(1-x)^{-(n+1)}$.
**Answer:** $\dfrac{n!}{(1-x)^{\,n+1}}$.

---

## F · Tangents, normals & piecewise differentiability

#### **Q26**
**Method: point + slope.** $y'=2x=2$ at $x=1$; through $(1,1)$: $y-1=2(x-1)$, i.e. $y=2x-1$.
**Answer:** $y=2x-1$.

#### **Q27**
**Method: normal slope $=-1/y'$.** $y'=3x^2=3$ at $x=1$; normal slope $-\frac13$; through $(1,1)$: $y-1=-\frac13(x-1)$.
**Answer:** $y-1=-\tfrac13(x-1)$.

#### **Q28**
**Method: match value and derivative.** Continuity: $1=a+b$. Derivative: left $2x|_{1}=2$, right $a$; so $a=2$, then $b=-1$.
**Answer:** $a=2,\ b=-1$.

---

## G · Rolle, MVT & functional equations

#### **Q29**
**Method: the Mean Value Theorem.** $f'(x)=2x$ and
$\frac{f(3)-f(1)}{3-1}=\frac{9-1}{2}=4$, so $2c=4$ and $c=2\in(1,3)$ ✓.
**Answer:** $c=2$.

#### **Q30**
**Method: Rolle's theorem needs $f(a)=f(b)$.** Here $f(-1)=0=f(1)$, so there is
$c\in(-1,1)$ with $f'(c)=0$. Since $f'(x)=3x^2-1$, we get
$c=\pm\frac1{\sqrt3}$, both inside $(-1,1)$ ✓.
**Answer:** $f'\big(\pm\tfrac1{\sqrt3}\big)=0$.

#### **Q31**
**Method: differentiate with respect to $y$ at $y=0$.** $f'(x+y)=f(x)f'(y)$, so
at $y=0$: $f'(x)=f(x)f'(0)=2f(x)$. This ODE has solution $f(x)=Ce^{2x}$, and
$f(0)=f(0)^2$ with $f\not\equiv0$ gives $f(0)=1$, so $C=1$.
**Answer:** $f(x)=e^{2x}$. (Check: $e^{2(x+y)}=e^{2x}e^{2y}$ ✓ and
$(e^{2x})'(0)=2$ ✓.)

#### **Q32**
**Method: Leibniz with $f=x^2$.** Only $f^{(0)}=x^2$, $f^{(1)}=2x$ and
$f^{(2)}=2$ survive, so
$$\frac{d^n}{dx^n}(x^2e^x)=e^x\left[x^2+2nx+n(n-1)\right].$$
**Answer:** $e^x\big[x^2+2nx+n(n-1)\big]$. (Check at $x=1.3$: $n=1$ gives
$15.7413$ ✓, $n=2$ gives $32.6200$ ✓, $n=3$ gives $56.8374$ ✓.)

#### **Q33**
**Method: complex exponentials.** $e^x\cos x=\Re\,e^{(1+i)x}$ and
$1+i=\sqrt2\,e^{i\pi/4}$, so $(1+i)^n=2^{n/2}e^{in\pi/4}$ and
$$\frac{d^n}{dx^n}(e^x\cos x)=2^{n/2}e^x\cos\!\left(x+\frac{n\pi}{4}\right).$$
**Answer:** $2^{n/2}e^x\cos\!\big(x+\frac{n\pi}{4}\big)$. (Check at $x=0.7$:
$n=1$ gives $0.2429$ ✓, $n=2$ gives $-2.5946$ ✓, $n=3$ gives $-5.6750$ ✓,
$n=4$ gives $-6.1608$ ✓.)

#### **Q34**
**Method: induction.** $\frac{d}{dx}(1-x)^{-1}=(1-x)^{-2}$, and if
$\frac{d^n}{dx^n}(1-x)^{-1}=n!(1-x)^{-(n+1)}$ then differentiating gives
$(n+1)!(1-x)^{-(n+2)}$ ✓.
**Answer:** $\dfrac{n!}{(1-x)^{n+1}}$. (Check at $x=0.4$: $n=1$ gives
$2.7778$ ✓, $n=2$ gives $9.2593$ ✓, $n=4$ gives $308.6420$ ✓.)

#### **Q35**
**Method: differentiate with respect to $y$ at $y=0$.** $f'(x+y)=f'(y)$, so at
$y=0$: $f'(x)=f'(0)=3$, a constant. Hence $f(x)=3x+C$, and $f(0)=0$ (from
$f(0)=f(0)+f(0)$) gives $C=0$.
**Answer:** $f(x)=3x$; differentiability is needed because without it there exist
additive functions that are nowhere continuous (constructed using a Hamel basis),
for which the conclusion fails.

#### **Q36**
**Method: the difference quotient, then the explicit formula.** At $0$:
$\frac{f(h)-f(0)}{h}=h\sin\frac1h\to0$ since $\lvert\sin\frac1h\rvert\le1$, so
$f'(0)=0$ ✓. For $x\ne0$ the product and chain rules give
$f'(x)=2x\sin\frac1x-\cos\frac1x$, and
$f'\big(\frac1{k\pi}\big)=-\cos(k\pi)=(-1)^{k+1}$, which alternates between $1$
and $-1$ as $k\to\infty$ ✓.
**Answer:** $f'(0)=0$ exists, but $f'$ oscillates and is discontinuous at $0$.

#### **Q37**
**Method: study $g(x)=e^x-1-x$.** $g'(x)=e^x-1$, which is negative for $x<0$ and
positive for $x>0$, so $g$ decreases then increases and attains its minimum at
$x=0$, where $g(0)=0$. Hence $g(x)\ge0$ everywhere, with equality only at $x=0$.
**Answer:** proved; equality only at $x=0$. (Check numerically: $x=-1$ gives
$0.3679\ge0$ ✓, $x=2$ gives $6.389\ge2$ ✓, $x=0$ gives equality ✓.)

#### **Q38**
**Method: study $h(x)=\ln x-x+1$.** $h'(x)=\frac1x-1$, positive for $0<x<1$ and
negative for $x>1$, so $h$ attains its maximum at $x=1$, where $h(1)=0$. Hence
$h(x)\le0$, i.e. $\ln x\le x-1$, with equality only at $x=1$.
**Answer:** proved; equality only at $x=1$. (Check numerically: $x=0.3$ gives
$-1.204\le-0.7$ ✓, $x=2.5$ gives $0.916\le1.5$ ✓, $x=1$ gives equality ✓.)
