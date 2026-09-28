---
title: "Integration — Olympiad Paper"
aliases: ["Integration Paper", "Integral Calculus Paper"]
module: "Integration"
module_title: "Integration"
type: paper
tags: [integration, paper, olympiad, calculus, integral-calculus]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Integration|Chapter 6]] · 📖 [[Integration|Complete Notes]] · ✅ [[Integration — Solutions|Solutions]] ➡

# Integration — Olympiad Paper

> **34 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Integration — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · Antiderivatives & basic indefinite integrals (Q1–Q4)

#### **Q1**[JEE Main][indefinite]Find $\int x^5\,dx$.

**Answer:** $\dfrac{x^6}{6}+C$

#### **Q2**[JEE Main][indefinite]Find $\int(3x^2+2x+1)\,dx$.

**Answer:** $x^3+x^2+x+C$

#### **Q3**[JEE Main][indefinite]Find $\int e^{2x}\,dx$.

**Answer:** $\dfrac12e^{2x}+C$

#### **Q4**[JEE Adv][indefinite]Find $\int\dfrac{dx}{3x+2}$.

**Answer:** $\dfrac13\ln\lvert3x+2\rvert+C$

---

## B · Substitution (Q5–Q9)

#### **Q5**[JEE Main][substitution]Find $\int2x(x^2+3)^4\,dx$.

**Answer:** $\dfrac{(x^2+3)^5}{5}+C$

#### **Q6**[JEE Main][substitution]Find $\int xe^{x^2}\,dx$.

**Answer:** $\dfrac12e^{x^2}+C$

#### **Q7**[JEE Adv][substitution]Evaluate $\int_0^1 2x\,e^{x^2}\,dx$.

**Answer:** $e-1\approx1.7183$

#### **Q8**[JEE Main][substitution]Find $\int\tan x\,dx$.

**Answer:** $\ln\lvert\sec x\rvert+C$

#### **Q9**[JEE Adv][substitution]Find $\int\sin^3x\cos x\,dx$.

**Answer:** $\dfrac{\sin^4x}{4}+C$

---

## C · Standard forms (Q10–Q13)

#### **Q10**[JEE Main][standard]Evaluate $\int_0^1\dfrac{dx}{1+x^2}$.

**Answer:** $\dfrac{\pi}{4}$

#### **Q11**[JEE Adv][standard]Evaluate $\int_0^1\dfrac{dx}{x^2+2x+2}$.

**Answer:** $\tan^{-1}(2)-\dfrac{\pi}{4}\approx0.3218$

#### **Q12**[JEE Adv][standard]Evaluate $\int_0^1\dfrac{dx}{\sqrt{4-x^2}}$.

**Answer:** $\dfrac{\pi}{6}$

#### **Q13**[JEE Main][standard]Find $\int\dfrac{dx}{x^2+4}$.

**Answer:** $\dfrac12\tan^{-1}\!\dfrac{x}{2}+C$

---

## D · Integration by parts (Q14–Q18)

#### **Q14**[JEE Main][parts]Find $\int xe^x\,dx$.

**Answer:** $e^x(x-1)+C$

#### **Q15**[JEE Main][parts]Find $\int\ln x\,dx$.

**Answer:** $x\ln x-x+C$

#### **Q16**[JEE Adv][parts]Find $\int x^2e^x\,dx$.

**Answer:** $e^x(x^2-2x+2)+C$

#### **Q17**[JEE Adv][parts]Evaluate $\int_0^{\pi}x\sin x\,dx$.

**Answer:** $\pi$

#### **Q18**[JEE Adv][parts]Find $\int e^x\sin x\,dx$.

**Answer:** $\dfrac12e^x(\sin x-\cos x)+C$

---

## E · Partial fractions (Q19–Q21)

#### **Q19**[JEE Main][partial fractions]Find $\int\dfrac{dx}{(x+1)(x+2)}$.

**Answer:** $\ln\left\lvert\dfrac{x+1}{x+2}\right\rvert+C$

#### **Q20**[JEE Adv][partial fractions]Evaluate $\int_0^1\dfrac{dx}{(x+1)(x+2)}$.

**Answer:** $\ln\dfrac43\approx0.2877$

#### **Q21**[JEE Adv][partial fractions]Find $\int\dfrac{dx}{x^2-a^2}$ ($a>0$).

**Answer:** $\dfrac1{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert+C$

---

## F · Definite integrals & the Fundamental Theorem (Q22–Q26)

#### **Q22**[JEE Main][FTC]Differentiate $A(x)=\int_0^x t^3\,dt$.

**Answer:** $x^3$

#### **Q23**[JEE Main][definite]Evaluate $\int_0^1x^3\,dx$.

**Answer:** $\dfrac14$

#### **Q24**[JEE Adv][definite]Evaluate $\int_0^{\pi/2}\sin^2x\,dx$.

**Answer:** $\dfrac{\pi}{4}$

#### **Q25**[JEE Adv][definite]Evaluate $\int_{-1}^{1}x^3\,dx$.

**Answer:** $0$

#### **Q26**[Olympiad][King]Evaluate $\int_0^{\pi/2}\dfrac{dx}{1+\tan x}$.

**Answer:** $\dfrac{\pi}{4}$

---

## G · Improper integrals & Olympiad techniques (Q27–Q34)

#### **Q27**[JEE Adv][improper]Evaluate $\int_0^\infty e^{-x}\,dx$.

**Answer:** $1$

#### **Q28**[Olympiad][Feynman]Evaluate $\int_0^1x\ln x\,dx$.

**Answer:** $-\dfrac14$

#### **Q29**[Olympiad][log integral]Evaluate $\int_0^1(\ln x)^2\,dx$.

**Answer:** $2$

#### **Q30**[Olympiad][Wallis]Evaluate $\int_0^{\pi/2}\sin^6x\,dx$.

**Answer:** $\dfrac{5\pi}{32}\approx0.4909$

#### **Q31**[Olympiad][substitution]Evaluate $\int_0^\infty\dfrac{\ln x}{1+x^2}\,dx$.

**Answer:** $0$

#### **Q32**[Olympiad][Gaussian]Evaluate $\displaystyle\int_0^{\infty}e^{-x^{2}}\,dx$.

**Answer:** $\dfrac{\sqrt\pi}{2}\approx0.886227$

#### **Q33**[JEE Adv][Gaussian]Evaluate $\displaystyle\int_{-\infty}^{\infty}e^{-2x^{2}}\,dx$.

**Answer:** $\sqrt{\dfrac\pi2}\approx1.253314$

#### **Q34**[Olympiad][Frullani]Evaluate $\displaystyle\int_0^{\infty}\frac{e^{-x}-e^{-2x}}{x}\,dx$.

**Answer:** $\ln2\approx0.693147$

---

## H · Frontier synthesis (Q35–Q46)

#### **Q35**[Olympiad][t-substitution]Evaluate $\int_0^{\pi/2}\dfrac{dx}{2+\cos x}$.

**Answer:** $\dfrac{\pi}{3\sqrt3}\approx0.6046$

#### **Q36**[Olympiad][King]Evaluate $\int_0^{\pi/2}\dfrac{\sin^2x}{\sin^2x+\cos^2x}\,dx$.

**Answer:** $\dfrac{\pi}{4}$

#### **Q37**[Olympiad][Dirichlet]Evaluate $\int_0^\infty\dfrac{\sin x}{x}\,dx$.

**Answer:** $\dfrac{\pi}{2}$

#### **Q38**[Olympiad][Frullani]Evaluate $\displaystyle\int_0^{\infty}\frac{e^{-3x}-e^{-5x}}{x}\,dx$.

**Answer:** $\ln\dfrac53\approx0.510826$

#### **Q39**[Olympiad][Beta]Evaluate $B\big(\frac12,\frac12\big)$.

**Answer:** $\pi$ (substitute $t=\sin^{2}\theta$, giving $\int_0^{\pi/2}2\,d\theta$)

#### **Q40**[Olympiad][Beta]Evaluate $\displaystyle\int_0^{\pi/2}\sqrt{\sin x\cos x}\,dx$.

**Answer:** $\dfrac1{\sqrt2}\cdot\dfrac{\sqrt\pi}{2}\dfrac{\Gamma(3/4)}{\Gamma(5/4)}\approx0.8472$

#### **Q41**[Olympiad][Gamma]Use the duplication formula with $z=\frac14$ to evaluate $\Gamma\big(\frac14\big)\Gamma\big(\frac34\big)$.

**Answer:** $2^{1/2}\sqrt\pi\,\Gamma(\frac12)=\pi\sqrt2\approx4.442883$

#### **Q42**[Olympiad][Gamma]State Euler's reflection formula for $\Gamma$.

**Answer:** $\Gamma(z)\Gamma(1-z)=\dfrac{\pi}{\sin\pi z}$

#### **Q43**[Olympiad][Gamma]Use the Beta function to evaluate $\displaystyle\int_0^{\pi/2}\sin^{6}x\,dx$.

**Answer:** $\frac12 B(\frac72,\frac12)=\dfrac{\sqrt\pi}{2}\dfrac{\Gamma(7/2)}{\Gamma(4)}=\dfrac{5\pi}{32}$

#### **Q44**[Olympiad][Gamma]State Legendre's duplication formula for $\Gamma$.

**Answer:** $\Gamma(z)\Gamma\big(z+\frac12\big)=2^{1-2z}\sqrt\pi\,\Gamma(2z)$

#### **Q45**[Olympiad][Feynman]Evaluate $\displaystyle\int_0^1\frac{x^{3}-1}{\ln x}\,dx$ by differentiating $\int_0^1x^{a}\,dx$ with respect to $a$.

**Answer:** $\displaystyle\int_0^1\frac{x^{a}-1}{\ln x}\,dx=\ln(a+1)$, so with $a=3$ the value is $\ln4=2\ln2\approx1.386294$

#### **Q46**[Olympiad][Gaussian]State the general Gaussian integral $\displaystyle\int_{-\infty}^{\infty}e^{-ax^{2}+bx}\,dx$ for $a>0$.

**Answer:** $\sqrt{\dfrac\pi a}\,e^{b^{2}/4a}$

---

> [!note] Exam technique notes
> - Match the tool to the integrand: $g'(x)$ as a factor → substitute; a product
>   with an algebraic factor → by parts (LIATE); a rational function → partial
>   fractions.
> - For a *definite* integral, always change the limits when you substitute.
> - Reach for King's property or an even/odd symmetry before grinding out
>   algebra — symmetry is almost always the intended shortcut.
> - Check any answer by differentiating it.
> - If no elementary antiderivative exists, try squaring the integral and
>   changing to polar coordinates.
> - A difference of two scaled copies of one function divided by $x$ is a
>   Frullani integral: $\big(f(0)-f(\infty)\big)\ln\frac ba$.
> - A power of $\sin$ or $\cos$ over $[0,\frac\pi2]$ is a Beta function in
>   disguise — convert first, then use $\Gamma$.
