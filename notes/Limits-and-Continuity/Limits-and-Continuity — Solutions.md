---
title: "Limits and Continuity — Olympiad Paper Solutions"
aliases: ["Limits and Continuity Solutions", "Limits Solutions"]
module: "Limits-and-Continuity"
module_title: "Limits and Continuity"
type: solutions
tags: [limits-and-continuity, solutions, olympiad, calculus]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Limits-and-Continuity — Paper|Paper]] · 📖 [[Limits-and-Continuity|Complete Notes]]

# Limits and Continuity — Solutions & Marking Guide

> Full solutions to all 32 questions, same Q-ids as the [[Limits-and-Continuity — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · The meaning of a limit

#### **Q1**
**Method: direct substitution (linear).** $5x-3$ is continuous everywhere, so substitute $x=2$: $5(2)-3 = 7$.
**Answer:** $7$. ✓

#### **Q2**
**Method: cancel the common factor.** $\frac{x^2-3x}{x} = x - 3$ for $x\ne0 \to -3$.
**Answer:** $-3$. (Check: at $x=10^{-6}$, value $\approx -3$ ✓.)

#### **Q3**
**Method: rationalise.** $\frac{\sqrt x-2}{x-4}\cdot\frac{\sqrt x+2}{\sqrt x+2} = \frac{x-4}{(x-4)(\sqrt x+2)} = \frac1{\sqrt x+2} \to \frac1{2+2}=\frac14$.
**Answer:** $\frac14$. ✓

#### **Q4**
**Method: sequential criterion (two sequences).** $x_n=\frac1{n\pi}\to0$ gives $\sin(1/x_n)=\sin(n\pi)=0$; $y_n=\frac1{\pi/2+2n\pi}\to0$ gives $\sin(1/y_n)=1$. Different limits along different paths ⇒ the limit does not exist.
**Answer:** does not exist.

---

## B · Standard limits

#### **Q5**
**Method: reduce to $\sin u/u$.** $\frac{\sin5x}{3x}=\frac53\cdot\frac{\sin5x}{5x}\to \frac53$.
**Answer:** $\frac53$. ✓

#### **Q6**
**Method: $(e^u-1)/u\to1$ with $u=3x$.** $=3\cdot\frac{e^{3x}-1}{3x}\to3$.
**Answer:** $3$. ✓

#### **Q7**
**Method: $\tan x/x\to1$.** $\frac{\tan2x}{x}=2\cdot\frac{\tan2x}{2x}\to2$.
**Answer:** $2$. ✓

#### **Q8**
**Method: half-angle.** $1-\cos x = 2\sin^2(x/2)$, so $\frac{\cos x-1}{\sin^2 x} = -\frac{2\sin^2(x/2)}{\sin^2 x} \to -2\cdot\frac{(x/2)^2}{x^2}=-\frac12$.
**Answer:** $-\frac12$. (Check via cancellation-free form: $-0.5000001$ ✓.)

#### **Q9**
**Method: factor.** $1-\cos2x = 2\sin^2 x$, so $\frac{1-\cos2x}{x\sin x}=\frac{2\sin^2 x}{x\sin x}=\frac{2\sin x}{x}\to2$.
**Answer:** $2$. ✓

#### **Q10**
**Method: the $e$-limit.** $\big(1+\frac3x\big)^x = \big[\big(1+\frac3x\big)^{x/3}\big]^3 \to e^{3}$.
**Answer:** $e^{3}\approx 20.0855$. ✓

#### **Q11**
**Method: rewrite base.** $2^x = e^{x\ln2}$, so $\frac{2^x-1}{x} = \ln2\cdot\frac{e^{x\ln2}-1}{x\ln2}\to\ln2$.
**Answer:** $\ln2\approx0.6931$. ✓

---

## C · Squeeze & L'Hôpital

#### **Q12**
**Method: squeeze.** $-|x|\le x\sin(1/x)\le|x|$ and $|x|\to0$, so the limit is $0$.
**Answer:** $0$. ✓

#### **Q13**
**Method: squeeze.** $-x^2\le x^2\cos(1/x)\le x^2\to0$.
**Answer:** $0$. ✓

#### **Q14**
**Method: L'Hôpital three times (or series).** $\frac{x-\tan x}{x^3}$ is $0/0$: $\frac{1-\sec^2 x}{3x^2}$ (still $0/0$) $\to\frac{-2\sec^2 x\tan x}{6x}=\frac{-\sec^2 x}{3}\cdot\frac{\tan x}{x}\to-\frac13$. (Equivalently $\tan x = x+\frac{x^3}{3}+O(x^5)$.)
**Answer:** $-\frac13$. (Check via $(x\cos x-\sin x)/(x^3\cos x)$: $-0.3333335$ ✓.)

#### **Q15**
**Method: L'Hôpital ($0/0$).** $\frac{1/(1+x)}{1}=\frac1{1+x}\to1$.
**Answer:** $1$. ✓

#### **Q16**
**Method: L'Hôpital ($\infty/\infty$).** $\frac{1/x}{1}=\frac1x\to0$.
**Answer:** $0$. ✓

---

## D · Continuity & discontinuities

#### **Q17**
**Method: factor and compare limit vs value.** $\frac{(x-2)(x+2)}{x-2}=x+2$ for $x\ne2$, so the limit is $4$; $f(2)$ is undefined. The hole is patchable ⇒ removable.
**Answer:** removable (limit $4$).

#### **Q18**
**Method: two one-sided limits.** $\lim_{x\to1^-}|x-1|=0=\lim_{x\to1^+}=|1-1|=g(1)$.
**Answer:** continuous at $1$.

#### **Q19**
**Method: match one-sided limits.** Continuity at $1$ needs the left value to equal the right limit: $f(1)=1^2=1$ and $\lim_{x\to1^+}(cx+2)=c+2$. Set $1=c+2\Rightarrow c=-1$.
**Answer:** $c=-1$.

#### **Q20**
**Method: zeros of the denominator.** $x^2-1=(x-1)(x+1)$, neither factor cancels; $f\to\pm\infty$ at both.
**Answer:** $x=\pm1$ (infinite discontinuities).

#### **Q21**
**Method: one-sided values.** $\lim_{x\to n^-}\lfloor x\rfloor=n-1$, $\lim_{x\to n^+}=n$; unequal finite one-sided limits ⇒ jump.
**Answer:** jump discontinuity.

---

## E · Intermediate Value Theorem

#### **Q22**
**Method: sign change + Bolzano.** $f(0)=-1$, $f(1)=1$, $f$ continuous ⇒ a root in $(0,1)$.
**Answer:** root exists in $(0,1)$.

#### **Q23**
**Method: IVT on $g=f-x$.** $g(0)=f(0)\ge0$, $g(1)=f(1)-1\le0$, $g$ continuous ⇒ $g(c)=0$ for some $c$, i.e. $f(c)=c$.
**Answer:** a fixed point exists.

#### **Q24**
**Method: IVT on the antipodal difference.** Parametrise the circle by $\theta\in[0,2\pi)$; set $g(\theta)=T(\theta)-T(\theta+\pi)$. Then $g(\theta+\pi)=-g(\theta)$, so $g$ changes sign on $[0,\pi]$; continuity gives $g(\theta_0)=0$, i.e. antipodal points of equal temperature.
**Answer:** such a pair exists.

#### **Q25**
**Method: IVT on $g(x)=f(x)-f(x+\frac12)$ on $[0,\frac12]$.** $g(0)=f(0)-f(\frac12)$, $g(\frac12)=f(\frac12)-f(1)=f(\frac12)-f(0)=-g(0)$; a sign change ⇒ $g(c)=0$.
**Answer:** such a $c$ exists.

---

## F · Differentiability & asymptotes

#### **Q26**
**Method: definition.** $\frac{\frac1{x+h}-\frac1x}{h}=\frac{x-(x+h)}{xh(x+h)}=\frac{-1}{x(x+h)}\to-\frac1{x^2}$.
**Answer:** $f'(x)=-\frac1{x^2}$.

#### **Q27**
**Method: divide by the top power.** $\frac{3+1/x^2}{1-2/x^2}\to3$ as $x\to\infty$.
**Answer:** $y=3$.

#### **Q28**
**Method: factor the denominator.** $x^2-x-6=(x-3)(x+2)$, so $f=\frac{x+2}{(x-3)(x+2)}=\frac1{x-3}$ for $x\ne-2$. The $x+2$ cancels (a hole at $-2$); only $x=3$ makes the simplified form blow up.
**Answer:** vertical asymptote $x=3$ only.

---

## G · Olympiad techniques

#### **Q29**
**Method: Stolz–Cesàro (or exact sum).** $a_n=\frac{n(n+1)}2$, $b_n=n^2$; $\frac{a_{n+1}-a_n}{b_{n+1}-b_n}=\frac{n+1}{(n+1)^2-n^2}=\frac{n+1}{2n+1}\to\frac12$. (Directly: $\frac{n(n+1)}{2n^2}\to\frac12$.)
**Answer:** $\frac12$. ✓

#### **Q30**
**Method: Riemann sum.** $\frac1n\sum_{k=1}^n (k/n)^2 \to \int_0^1 x^2\,dx=\frac13$.
**Answer:** $\frac13$. (Check: at $n=2\times10^5$, $0.33334$ ✓.)

#### **Q31**
**Method: monotone bounded + fixed point (Newton for $\sqrt2$).** $a_n\ge\sqrt2$ (AM–GM) and $a_{n+1}\le a_n$, so $a_n$ decreases to $L$ with $L=\frac12(L+2/L)$, i.e. $L^2=2$, $L=\sqrt2>0$.
**Answer:** $\sqrt2\approx1.41421$. (Check: 60 iterations from $2$ give $1.41421356$ ✓.)

---

## H · Synthesis & stretch

#### **Q32**
**Method: expand the exponent.** $\big(1+\frac1n\big)^n=\exp\!\big(n\ln(1+\tfrac1n)\big)$ and $n\ln(1+\tfrac1n)=1-\frac1{2n}+O(n^{-2})$, so $\big(1+\frac1n\big)^n = e\cdot e^{-1/(2n)+O(n^{-2})}=e\Big(1-\frac1{2n}+O(n^{-2})\Big)$. Hence $n\big[\big(1+\frac1n\big)^n-e\big]\to-\frac e2$.
**Answer:** $-\frac e2\approx-1.35914$. (Check: $-1.35902,-1.35913$ at $n=10^4,10^5$, converging to $-1.35914$ ✓.)
