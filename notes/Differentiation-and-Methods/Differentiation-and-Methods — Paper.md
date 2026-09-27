---
title: "Differentiation and Method of Differentiation — Olympiad Paper"
aliases: ["Differentiation Paper", "Methods of Differentiation Paper"]
module: "Differentiation-and-Methods"
module_title: "Differentiation and Method of Differentiation"
type: paper
tags: [differentiation-and-methods, paper, olympiad, calculus, assessment]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Differentiation-and-Methods|Chapter 6]] · 📖 [[Differentiation-and-Methods|Complete Notes]] · ✅ [[Differentiation-and-Methods — Solutions|Solutions]] ➡

# Differentiation and Method of Differentiation — Olympiad Paper

> **32 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Differentiation-and-Methods — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · From the definition & differentiability (Q1–Q4)

#### **Q1**[JEE Main][definition]$f(x)=x^3$. Find $f'(2)$.

**Answer:** $12$

#### **Q2**[JEE Main][definition]From the definition, differentiate $f(x)=\dfrac1x$.

**Answer:** $f'(x)=-\dfrac1{x^{2}}$

#### **Q3**[JEE Adv][differentiability]Is $f(x)=|x|$ differentiable at $0$? Justify.

**Answer:** No — left derivative $-1$, right derivative $+1$.

#### **Q4**[JEE Adv][differentiability]Test differentiability of $f(x)=x|x|$ at $0$.

**Answer:** Differentiable, $f'(0)=0$.

---

## B · Rules: product, quotient, power (Q5–Q10)

#### **Q5**[JEE Main][product]$\dfrac{d}{dx}\big(xe^{x}\big)$ at $x=0$.

**Answer:** $1$

#### **Q6**[JEE Main][quotient]Differentiate $f(x)=\dfrac{x}{1+x^2}$.

**Answer:** $\dfrac{1-x^2}{(1+x^2)^2}$

#### **Q7**[JEE Adv][product]$\dfrac{d}{dx}\big(x^3\sin x\big)$ at $x=\dfrac{\pi}{2}$.

**Answer:** $\dfrac{3\pi^2}{4}$

#### **Q8**[JEE Main][power]Differentiate $f(x)=\sqrt{x}$.

**Answer:** $\dfrac1{2\sqrt x}$

#### **Q9**[JEE Adv][quotient]Differentiate $f(x)=\dfrac{x^2}{x+1}$.

**Answer:** $\dfrac{x^2+2x}{(x+1)^2}$

#### **Q10**[JEE Main][power]Differentiate $f(x)=3x^4-2x+5$.

**Answer:** $12x^3-2$

---

## C · Chain rule & standard functions (Q11–Q16)

#### **Q11**[JEE Main][chain]$\dfrac{d}{dx}\sin(3x)$ at $x=0$.

**Answer:** $3$

#### **Q12**[JEE Main][chain]Differentiate $f(x)=e^{x^2}$.

**Answer:** $2x\,e^{x^{2}}$

#### **Q13**[JEE Adv][chain]Differentiate $f(x)=\ln(\sin x)$.

**Answer:** $\cot x$

#### **Q14**[JEE Adv][chain]Differentiate $f(x)=\cos(x^3)$.

**Answer:** $-3x^{2}\sin(x^{3})$

#### **Q15**[JEE Adv][inverse trig]$\dfrac{d}{dx}\arctan x$ at $x=1$.

**Answer:** $\dfrac12$

#### **Q16**[JEE Adv][inverse trig]Differentiate $f(x)=\arcsin(2x)$.

**Answer:** $\dfrac{2}{\sqrt{1-4x^{2}}}$

---

## D · Implicit, logarithmic, parametric (Q17–Q21)

#### **Q17**[JEE Main][implicit]For $x^2+y^2=25$, find $\dfrac{dy}{dx}$ at $(3,4)$.

**Answer:** $-\dfrac34$

#### **Q18**[JEE Main][logarithmic]Differentiate $f(x)=x^{x}$; give $f'(1)$.

**Answer:** $f'(1)=1$

#### **Q19**[JEE Main][parametric]$x=t^2+1$, $y=t^3$. Find $\dfrac{dy}{dx}$ at $t=1$.

**Answer:** $\dfrac32$

#### **Q20**[JEE Adv][parametric]For $x=a\cos t$, $y=b\sin t$, find $\dfrac{dy}{dx}$.

**Answer:** $-\dfrac{b}{a}\cot t$

#### **Q21**[JEE Adv][parametric]For $x=t^2$, $y=t^3$, find $\dfrac{d^2y}{dx^2}$ at $t=1$.

**Answer:** $\dfrac34$

---

## E · Higher-order & nth derivatives (Q22–Q25)

#### **Q22**[JEE Main][higher-order]$\dfrac{d^2}{dx^2}(\sin x)$ at $x=\dfrac{\pi}{2}$.

**Answer:** $-1$

#### **Q23**[JEE Adv][nth]Find $\dfrac{d^3}{dx^3}e^{2x}$ at $x=0$.

**Answer:** $8$

#### **Q24**[Olympiad][Leibniz]Find the $n$th derivative of $x^2e^{x}$.

**Answer:** $e^{x}\big(x^{2}+2nx+n(n-1)\big)$

#### **Q25**[Olympiad][nth]Find the $n$th derivative of $\dfrac1{1-x}$.

**Answer:** $\dfrac{n!}{(1-x)^{\,n+1}}$

---

## F · Tangents, normals & piecewise differentiability (Q26–Q28)

#### **Q26**[JEE Main][tangent]Tangent to $y=x^2$ at $x=1$.

**Answer:** $y=2x-1$

#### **Q27**[JEE Main][normal]Normal to $y=x^3$ at $x=1$.

**Answer:** $y-1=-\tfrac13(x-1)$

#### **Q28**[JEE Adv][piecewise]Find $a,b$ so that $f(x)=\begin{cases}x^2,&x\le1\\ ax+b,&x>1\end{cases}$ is differentiable at $1$.

**Answer:** $a=2,\ b=-1$

---

## G · Rolle, MVT & functional equations (Q29–Q31)

#### **Q29**[JEE Main][Rolle]$f(x)=x^2-4$ on $[-2,2]$. Find $c$ with $f'(c)=0$.

**Answer:** $c=0$

#### **Q30**[JEE Adv][MVT]$f(x)=x^2$ on $[1,3]$. Find $c$ with $f'(c)=\dfrac{f(3)-f(1)}{3-1}$.

**Answer:** $c=2$

#### **Q31**[Olympiad][functional]$f$ differentiable, $f(x+y)=f(x)f(y)$, $f'(0)=2$. Find $f$.

**Answer:** $f(x)=e^{2x}$

---

## H · Synthesis & stretch (Q32)

#### **Q32**[Olympiad][stretch]Find $\dfrac{d^{n}}{dx^{n}}\big(e^{x}\cos x\big)$.

**Answer:** $2^{n/2}\,e^{x}\cos\!\Big(x+\dfrac{n\pi}{4}\Big)$

---

> [!note] Exam technique notes
> - Match the method to the shape: $u^v$ → logarithmic; two parametric equations → $\frac{dy/dt}{dx/dt}$; $F(x,y)=0$ → implicit.
> - For an $n$th derivative, compute the first few and read the pattern, or reach for Leibniz.
> - To prove an inequality, differentiate a difference and read the sign.
