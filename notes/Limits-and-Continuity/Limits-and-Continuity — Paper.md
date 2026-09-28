---
title: "Limits and Continuity — Olympiad Paper"
aliases: ["Limits and Continuity Paper", "Limits Paper"]
module: "Limits-and-Continuity"
module_title: "Limits and Continuity"
type: paper
tags: [limits-and-continuity, paper, olympiad, calculus, assessment]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Limits-and-Continuity|Chapter 6]] · 📖 [[Limits-and-Continuity|Complete Notes]] · ✅ [[Limits-and-Continuity — Solutions|Solutions]] ➡

# Limits and Continuity — Olympiad Paper

> **39 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.** → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Limits-and-Continuity — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · The meaning of a limit (Q1–Q4)

#### **Q1**[JEE Main][direct]$\displaystyle\lim_{x\to 2}(5x-3)$

**Answer:** $7$

#### **Q2**[JEE Main][0/0]$\displaystyle\lim_{x\to 0}\frac{x^2-3x}{x}$

**Answer:** $-3$

#### **Q3**[JEE Main][rationalise]$\displaystyle\lim_{x\to 4}\frac{\sqrt{x}-2}{x-4}$

**Answer:** $\dfrac14$

#### **Q4**[JEE Adv][existence]Does $\displaystyle\lim_{x\to 0}\sin\frac1x$ exist? Justify.

**Answer:** No — along $x_n=\frac1{n\pi}$ the value is $0$, along $x_n=\frac1{\pi/2+2n\pi}$ it is $1$ (sequential criterion).

---

## B · Standard limits (Q5–Q11)

#### **Q5**[JEE Main][trig]$\displaystyle\lim_{x\to 0}\frac{\sin 5x}{3x}$

**Answer:** $\dfrac53$

#### **Q6**[JEE Main][exponential]$\displaystyle\lim_{x\to 0}\frac{e^{3x}-1}{x}$

**Answer:** $3$

#### **Q7**[JEE Main][trig]$\displaystyle\lim_{x\to 0}\frac{\tan 2x}{x}$

**Answer:** $2$

#### **Q8**[JEE Adv][trig]$\displaystyle\lim_{x\to 0}\frac{\cos x - 1}{\sin^2 x}$

**Answer:** $-\dfrac12$

#### **Q9**[JEE Adv][trig]$\displaystyle\lim_{x\to 0}\frac{1-\cos 2x}{x\sin x}$

**Answer:** $2$

#### **Q10**[JEE Adv][e-limit]$\displaystyle\lim_{x\to\infty}\Big(1+\frac3x\Big)^{x}$

**Answer:** $e^{3}$

#### **Q11**[JEE Adv][exponential]$\displaystyle\lim_{x\to 0}\frac{2^{x}-1}{x}$

**Answer:** $\ln 2$

---

## C · Squeeze & L'Hôpital (Q12–Q16)

#### **Q12**[JEE Main][squeeze]$\displaystyle\lim_{x\to 0} x\sin\frac1x$

**Answer:** $0$

#### **Q13**[JEE Main][squeeze]$\displaystyle\lim_{x\to 0} x^{2}\cos\frac1x$

**Answer:** $0$

#### **Q14**[JEE Adv][L'Hôpital]$\displaystyle\lim_{x\to 0}\frac{x-\tan x}{x^{3}}$

**Answer:** $-\dfrac13$

#### **Q15**[JEE Adv][L'Hôpital]$\displaystyle\lim_{x\to 0}\frac{\ln(1+x)}{x}$

**Answer:** $1$

#### **Q16**[JEE Adv][L'Hôpital]$\displaystyle\lim_{x\to\infty}\frac{\ln x}{x}$

**Answer:** $0$

---

## D · Continuity & discontinuities (Q17–Q21)

#### **Q17**[JEE Main][classify]Classify the discontinuity of $f(x)=\dfrac{x^2-4}{x-2}$ at $x=2$.

**Answer:** removable (limit $=4$, value undefined)

#### **Q18**[JEE Main][continuity]Is $g(x)=|x-1|$ continuous at $x=1$?

**Answer:** Yes (both sides $\to 0 = g(1)$)

#### **Q19**[JEE Adv][piecewise]Find $c$ so that $f(x)=\begin{cases}x^2,&x\le 1\\ cx+2,&x>1\end{cases}$ is continuous at $1$.

**Answer:** $c=-1$

#### **Q20**[JEE Adv][poles]Points of discontinuity of $h(x)=\dfrac{1}{x^2-1}$.

**Answer:** $x=1$ and $x=-1$ (infinite)

#### **Q21**[JEE Adv][jump]Classify the discontinuity of $\lfloor x\rfloor$ at an integer $n$.

**Answer:** jump (left $=n-1$, right $=n$)

---

## E · Intermediate Value Theorem (Q22–Q25)

#### **Q22**[JEE Main][IVT]Show $x^{5}+x-1=0$ has a root in $(0,1)$.

**Answer:** $f(0)=-1<0$, $f(1)=1>0$; continuous ⇒ a root exists.

#### **Q23**[JEE Adv][fixed point]Show any continuous $f:[0,1]\to[0,1]$ has a fixed point.

**Answer:** apply IVT to $g=f(x)-x$: $g(0)\ge0$, $g(1)\le0$.

#### **Q24**[JEE Adv][IVT]Prove some two antipodal points on a circle have equal temperature (temperature continuous on the circle).

**Answer:** $g(\theta)=T(\theta)-T(\theta+\pi)$; $g(0)=-g(\pi)$ ⇒ IVT gives $g=0$.

#### **Q25**[Olympiad][IVT]Continuous $f$ on $[0,1]$ with $f(0)=f(1)$. Show $\exists c\in[0,\tfrac12]$ with $f(c)=f(c+\tfrac12)$.

**Answer:** $g(x)=f(x)-f(x+\tfrac12)$; $g(0)=-g(\tfrac12)$ ⇒ IVT.

---

## F · Differentiability & asymptotes (Q26–Q28)

#### **Q26**[JEE Main][definition]From the definition, differentiate $f(x)=\dfrac1x$.

**Answer:** $f'(x)=-\dfrac1{x^{2}}$

#### **Q27**[JEE Main][asymptote]Horizontal asymptote of $f(x)=\dfrac{3x^2+1}{x^2-2}$.

**Answer:** $y=3$

#### **Q28**[JEE Adv][asymptote]Vertical asymptotes of $f(x)=\dfrac{x+2}{x^2-x-6}$.

**Answer:** $x=3$ only (the factor $x+2$ cancels — a hole at $x=-2$, not an asymptote)

---

## G · Olympiad techniques (Q29–Q31)

#### **Q29**[JEE Adv][Stolz]$\displaystyle\lim_{n\to\infty}\frac{1+2+\cdots+n}{n^{2}}$

**Answer:** $\dfrac12$

#### **Q30**[Olympiad][Riemann]$\displaystyle\lim_{n\to\infty}\frac1n\sum_{k=1}^{n}\Big(\frac{k}{n}\Big)^{2}$

**Answer:** $\dfrac13$

#### **Q31**[Olympiad][recursion]$a_1=2$, $a_{n+1}=\dfrac12\Big(a_n+\dfrac{2}{a_n}\Big)$. Find $\lim a_n$.

**Answer:** $\sqrt2$

---

## H · Olympiad frontier (Q32–Q39)

#### **Q32**[Olympiad][stretch]$\displaystyle\lim_{n\to\infty} n\Big[\Big(1+\frac1n\Big)^{n}-e\Big]$

**Answer:** $-\dfrac e2$

#### **Q33**[Olympiad][riemann]Evaluate $\displaystyle\lim_{n\to\infty}\frac{1^3+2^3+\cdots+n^3}{n^{4}}$ by recognising a Riemann sum.

**Answer:** $\dfrac14$

#### **Q34**[Olympiad][riemann]Evaluate $\displaystyle\lim_{n\to\infty}\frac1n\sum_{k=1}^{n}\sqrt{\frac{k}{n}}$ as an integral.

**Answer:** $\displaystyle\int_0^1\sqrt{x}\,dx=\dfrac23$

#### **Q35**[Olympiad][squeeze]$\displaystyle\lim_{n\to\infty}\Big(1+\frac1{n^2}\Big)\Big(1+\frac2{n^2}\Big)\cdots\Big(1+\frac{n}{n^2}\Big)$

**Answer:** $\sqrt e\approx1.648721$

#### **Q36**[Olympiad][recursion]$a_1=1$, $a_{n+1}=\sqrt{2+a_n}$. Find $\lim a_n$.

**Answer:** $2$

#### **Q37**[Olympiad][ivt]$f$ continuous on $[0,1]$ with $f(0)=f(1)$. Prove there is $c\in[0,\tfrac12]$ with $f(c)=f\big(c+\tfrac12\big)$.

**Answer:** proved by $g(x)=f(x)-f(x+\frac12)$, $g(\frac12)=-g(0)$, IVT

#### **Q38**[Olympiad][continuity]A function $f$ satisfies $f\!\big(\tfrac{x+y}{2}\big)=\tfrac{f(x)+f(y)}{2}$ for all $x,y$ and is continuous at one point. Prove $f$ is linear.

**Answer:** $f(x)=ax+b$

#### **Q39**[Olympiad][stretch]Evaluate $\displaystyle\lim_{n\to\infty}\frac1n\sum_{k=1}^{n}\frac{1}{1+k/n}$ as an integral.

**Answer:** $\ln2$

---

> [!note] Exam technique notes
> - **Look for the Riemann-sum shape** $\frac1n\sum g(\frac kn)$ before doing any
>   algebra; it converts the limit into $\int_0^1g$.
> - **For a recursion, prove monotone + bounded first**, then solve the
>   fixed-point equation $L=f(L)$ and discard the extraneous root.
> - **For a product limit, take logarithms** and squeeze with
>   $x-\frac{x^2}2\le\ln(1+x)\le x$.
> - **For an existence claim, build an auxiliary function whose sign change is
>   forced**, then apply the IVT.
> - **A convergence rate question asks for the second-order term** — expand to the
>   next order, do not just take the limit.
