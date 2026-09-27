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

> Full solutions to all 32 questions, same Q-ids as the [[Differentiation-and-Methods — Paper|paper]].
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
**Method: Rolle.** $f(-2)=f(2)=0$, $f$ smooth; $f'=2x=0\Rightarrow c=0\in(-2,2)$.
**Answer:** $c=0$.

#### **Q30**
**Method: MVT.** Secant slope $\frac{9-1}{2}=4$; $f'=2x=4\Rightarrow c=2\in(1,3)$.
**Answer:** $c=2$.

#### **Q31**
**Method: differentiate the FE.** $f'(x+y)=f(x)f'(y)$; set $y=0$: $f'(x)=f(x)f'(0)=2f(x)$. With $f(0)=1$, solve $f'=2f\Rightarrow f=Ce^{2x}=e^{2x}$.
**Answer:** $f(x)=e^{2x}$.

---

## H · Synthesis & stretch

#### **Q32**
**Method: complex form.** $e^x\cos x=\operatorname{Re}\big(e^{(1+i)x}\big)$; the $n$th derivative is $\operatorname{Re}\big((1+i)^n e^{(1+i)x}\big)$. Since $1+i=\sqrt2\,e^{i\pi/4}$, $(1+i)^n=2^{n/2}e^{in\pi/4}$, giving $2^{n/2}e^x\cos\!\big(x+\frac{n\pi}{4}\big)$.
**Answer:** $2^{n/2}e^{x}\cos\!\Big(x+\dfrac{n\pi}{4}\Big)$. (Check $n=1$: $\sqrt2\,e^x\cos(x+\pi/4)=e^x(\cos x-\sin x)=(e^x\cos x)'$ ✓.)
