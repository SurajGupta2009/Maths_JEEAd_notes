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

> **38 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.** → JEE Advanced → Olympiad.**
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

## G · Rolle, MVT and functional equations (Q29–Q31)

#### **Q29**[JEE Main][MVT]$f(x)=x^2$ on $[1,3]$. Find $c$ with $f'(c)=\dfrac{f(3)-f(1)}{3-1}$.

**Answer:** $c=2$

#### **Q30**[JEE Adv][MVT]State Rolle's theorem and verify it for $f(x)=x^3-x$ on $[-1,1]$.

**Answer:** $f'(\pm\tfrac1{\sqrt3})=0$

#### **Q31**[Olympiad][functional]$f$ is differentiable, $f(x+y)=f(x)f(y)$ for all real $x,y$, and $f'(0)=2$. Find $f$.

**Answer:** $f(x)=e^{2x}$

---

## H · Olympiad frontier (Q32–Q38)

#### **Q32**[Olympiad][leibniz]Find $\dfrac{d^n}{dx^n}\big(x^2e^x\big)$ in closed form.

**Answer:** $e^x\big[x^2+2nx+n(n-1)\big]$

#### **Q33**[Olympiad][leibniz]Find $\dfrac{d^n}{dx^n}\big(e^x\cos x\big)$ in closed form.

**Answer:** $2^{n/2}e^x\cos\!\big(x+\frac{n\pi}{4}\big)$

#### **Q34**[Olympiad][nth derivative]Find the $n^{\rm th}$ derivative of $\dfrac1{1-x}$.

**Answer:** $\dfrac{n!}{(1-x)^{n+1}}$

#### **Q35**[Olympiad][functional]$f$ is differentiable and $f(x+y)=f(x)+f(y)$ for all real $x,y$, with $f'(0)=3$. Find $f$, and explain why differentiability is needed.

**Answer:** $f(x)=3x$; without regularity there are wild discontinuous solutions

#### **Q36**[Olympiad][darboux]Let $f(x)=x^2\sin\frac1x$ for $x\ne0$ and $f(0)=0$. Show that $f$ is differentiable at $0$ but that $f'$ is not continuous at $0$.

**Answer:** $f'(0)=0$, but $f'\big(\frac1{k\pi}\big)=(-1)^{k+1}$ oscillates

#### **Q37**[Olympiad][inequality]Using calculus, prove $e^x\ge1+x$ for all real $x$, and state when equality holds.

**Answer:** proved; equality only at $x=0$

#### **Q38**[Olympiad][inequality]Using calculus, prove $\ln x\le x-1$ for $x>0$, and state when equality holds.

**Answer:** proved; equality only at $x=1$

---

> [!note] Exam technique notes
> - **Leibniz before brute force.** For the $n^{\rm th}$ derivative of a product,
>   only the derivatives of each factor that survive matter — most terms vanish.
> - **Complex exponentials kill trig.** $e^{ax}\cos bx=\Re\,e^{(a+ib)x}$ turns an
>   $n^{\rm th}$ derivative into one multiplication.
> - **Differentiate a functional equation at the coincidence point** ($y=0$ or
>   $y=1$) to extract an ODE, then solve it.
> - **Check the regularity hypothesis** in every functional-equation problem —
>   without it the conclusion can fail spectacularly.
> - **For a derivative inequality, study $g=f-h$:** show $g'\ge0$ (or $g$ has a
>   minimum) and read the equality case off the critical point.
