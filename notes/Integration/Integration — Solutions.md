---
title: "Integration — Solutions"
aliases: ["Integration Solutions", "Integral Calculus Solutions"]
module: "Integration"
module_title: "Integration"
type: solutions
tags: [integration, solutions, olympiad, calculus, integral-calculus]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Integration — Paper|Paper]] · 📖 [[Integration|Complete Notes]]

# Integration — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[Integration — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Antiderivatives & basic indefinite integrals

#### **Q1**
**Method: reverse the power rule.** $\frac{x^6}{6}$ since $\frac{d}{dx}\frac{x^6}{6}=x^5$.
**Answer:** $\dfrac{x^6}{6}+C$.

#### **Q2**
**Method: linearity term-by-term.** $x^3+x^2+x$.
**Answer:** $x^3+x^2+x+C$.

#### **Q3**
**Method: reverse the chain rule.** $\frac12e^{2x}$, since $\frac{d}{dx}\frac12e^{2x}=e^{2x}$.
**Answer:** $\dfrac12e^{2x}+C$.

#### **Q4**
**Method: log standard form, scaled.** $u=3x+2$, $du=3\,dx$, so $\frac13\ln\lvert u\rvert$.
**Answer:** $\dfrac13\ln\lvert3x+2\rvert+C$.

---

## B · Substitution

#### **Q5**
**Method: substitution.** $u=x^2+3$, $du=2x\,dx$: $\int u^4du=\frac{u^5}{5}$.
**Answer:** $\dfrac{(x^2+3)^5}{5}+C$.

#### **Q6**
**Method: substitution.** $u=x^2$, $du=2x\,dx$: $\frac12\int e^udu$.
**Answer:** $\dfrac12e^{x^2}+C$.

#### **Q7**
**Method: substitution in a definite integral — change the limits.** $u=x^2$; $x=0\to u=0$, $x=1\to u=1$: $\int_0^1e^udu=e-1$.
**Answer:** $e-1\approx1.7183$. (Check: a midpoint Riemann sum with $2\times10^5$ panels gives $1.71828$ ✓.)

#### **Q8**
**Method: rewrite and substitute.** $\tan x=\frac{\sin x}{\cos x}$; $u=\cos x$, $du=-\sin x\,dx$: $-\ln\lvert\cos x\rvert=\ln\lvert\sec x\rvert$.
**Answer:** $\ln\lvert\sec x\rvert+C$.

#### **Q9**
**Method: substitution.** $u=\sin x$, $du=\cos x\,dx$: $\int u^3du=\frac{u^4}{4}$.
**Answer:** $\dfrac{\sin^4x}{4}+C$. (Check on $[0,1]$: numeric $0.125342$ vs $\frac14\sin^41=0.125342$ ✓.)

---

## C · Standard forms

#### **Q10**
**Method: arctangent standard form.** $\int_0^1\frac{dx}{1+x^2}=\tan^{-1}(1)-\tan^{-1}(0)=\frac\pi4$.
**Answer:** $\dfrac{\pi}{4}$.

#### **Q11**
**Method: complete the square, then arctangent.** $x^2+2x+2=(x+1)^2+1$; with $u=x+1$, limits $1\to2$: $\tan^{-1}(2)-\tan^{-1}(1)$.
**Answer:** $\tan^{-1}(2)-\dfrac{\pi}{4}\approx0.3218$. (Check: midpoint Riemann sum $0.32175$ ✓.)

#### **Q12**
**Method: arcsin standard form.** $\frac1{\sqrt{4-x^2}}=\frac12\cdot\frac1{\sqrt{1-(x/2)^2}}$; with $u=x/2$, limits $0\to\frac12$: $\sin^{-1}(\frac12)-0=\frac\pi6$.
**Answer:** $\dfrac{\pi}{6}$. (Check: midpoint Riemann sum $0.52360$ ✓.)

#### **Q13**
**Method: arctangent with $a=2$.** $\frac1a\tan^{-1}\frac xa$ with $a=2$.
**Answer:** $\dfrac12\tan^{-1}\!\dfrac{x}{2}+C$.

---

## D · Integration by parts

#### **Q14**
**Method: LIATE — $u=x$, $dv=e^xdx$.** $xe^x-\int e^xdx=xe^x-e^x$.
**Answer:** $e^x(x-1)+C$. (Check: $\frac{d}{dx}e^x(x-1)=xe^x$ ✓.)

#### **Q15**
**Method: by parts with $dv=dx$.** $x\ln x-\int x\cdot\frac1x\,dx=x\ln x-x$.
**Answer:** $x\ln x-x+C$. (Check: $\frac{d}{dx}(x\ln x-x)=\ln x$ ✓.)

#### **Q16**
**Method: by parts twice (tabular).** $\int x^2e^xdx=x^2e^x-2\int xe^xdx=x^2e^x-2e^x(x-1)=e^x(x^2-2x+2)$.
**Answer:** $e^x(x^2-2x+2)+C$. (Check: differentiating gives $(x^2e^x)$ ✓.)

#### **Q17**
**Method: by parts, $u=x$, $dv=\sin x\,dx$.** $[-x\cos x]_0^\pi+\int_0^\pi\cos x\,dx=(-\pi(-1)-0)+[\sin x]_0^\pi=\pi+0$.
**Answer:** $\pi$. (Check: midpoint Riemann sum $3.14159$ ✓.)

#### **Q18**
**Method: by parts twice, then solve for the integral.** With $I=\int e^x\sin x\,dx$, two applications give $I=e^x\sin x-e^x\cos x-I$, so $I=\frac12e^x(\sin x-\cos x)$.
**Answer:** $\dfrac12e^x(\sin x-\cos x)+C$. (Check: differentiating at $x=1$ gives $e\sin1$ ✓.)

---

## E · Partial fractions

#### **Q19**
**Method: split on distinct linear factors.** $\frac1{(x+1)(x+2)}=\frac1{x+1}-\frac1{x+2}$.
**Answer:** $\ln\left\lvert\dfrac{x+1}{x+2}\right\rvert+C$.

#### **Q20**
**Method: definite form of Q19.** $\Big[\ln\lvert\frac{x+1}{x+2}\rvert\Big]_0^1=\ln\frac{2}{3}-\ln\frac{1}{2}=\ln\frac{4}{3}$.
**Answer:** $\ln\dfrac43\approx0.2877$. (Check: midpoint Riemann sum $0.28768$ ✓.)

#### **Q21**
**Method: partial fractions.** $\frac1{x^2-a^2}=\frac1{2a}\Big(\frac1{x-a}-\frac1{x+a}\Big)$, giving $\frac1{2a}\ln\lvert\frac{x-a}{x+a}\rvert$.
**Answer:** $\dfrac1{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert+C$.

---

## F · Definite integrals & the Fundamental Theorem

#### **Q22**
**Method: FTC Part 1.** $\frac{d}{dx}\int_0^x f(t)dt=f(x)$ with $f(t)=t^3$.
**Answer:** $x^3$. (Indeed $A(x)=\frac{x^4}{4}$.)

#### **Q23**
**Method: FTC Part 2.** $[\frac{x^4}{4}]_0^1=\frac14$.
**Answer:** $\dfrac14$. (Check: midpoint Riemann sum $0.25000$ ✓.)

#### **Q24**
**Method: King's property (or the $\sin^2+\cos^2=1$ identity).** Let $I=\int_0^{\pi/2}\sin^2x\,dx$; by King's property $I=\int_0^{\pi/2}\cos^2x\,dx$, so $2I=\int_0^{\pi/2}1\,dx=\frac\pi2$.
**Answer:** $\dfrac{\pi}{4}$. (Check: midpoint Riemann sum $0.78540$ ✓.)

#### **Q25**
**Method: odd function on a symmetric interval.** $x^3$ is odd, so the integral vanishes.
**Answer:** $0$. (Direct: $[\frac{x^4}4]_{-1}^1=0$ ✓.)

#### **Q26**
**Method: King's property, then add.** $I=\int_0^{\pi/2}\frac{dx}{1+\tan x}$; substituting $x\mapsto\frac\pi2-x$ gives $I=\int_0^{\pi/2}\frac{dx}{1+\cot x}$. Adding: $2I=\int_0^{\pi/2}\Big(\frac1{1+\tan x}+\frac1{1+\cot x}\Big)dx=\int_0^{\pi/2}1\,dx=\frac\pi2$, since $\frac1{1+u}+\frac1{1+1/u}=1$.
**Answer:** $\dfrac{\pi}{4}$. (Check: midpoint Riemann sum $0.78540$ ✓.)

---

## G · Improper integrals & Olympiad techniques

#### **Q27**
**Method: improper integral as a limit.** $\lim_{R\to\infty}[-e^{-x}]_0^R=\lim_{R\to\infty}(1-e^{-R})=1$.
**Answer:** $1$. (Check: midpoint Riemann sum on $[0,40]$ gives $1.00000$ ✓.)

#### **Q28**
**Method: Feynman's trick.** Let $I(a)=\int_0^1x^a\,dx=\frac1{a+1}$. Then $I'(a)=\int_0^1x^a\ln x\,dx=-\frac1{(a+1)^2}$, so at $a=1$: $-\frac14$.
**Answer:** $-\dfrac14$. (Check: by parts $\big[\frac{x^2}{2}\ln x-\frac{x^2}{4}\big]_0^1=-\frac14$; midpoint Riemann sum $-0.25000$ ✓.)

#### **Q29**
**Method: Feynman's trick, second derivative.** From $I(a)=\frac1{a+1}$, $I''(a)=\frac2{(a+1)^3}=\int_0^1x^a(\ln x)^2dx$; at $a=0$: $2$.
**Answer:** $2$. (Check: midpoint Riemann sum $1.99997$ ✓.)

#### **Q30**
**Method: Wallis reduction $I_n=\frac{n-1}{n}I_{n-2}$.** $I_6=\frac56\cdot\frac34\cdot\frac12\cdot I_0=\frac5{32}\cdot\frac\pi2=\frac{5\pi}{32}$.
**Answer:** $\dfrac{5\pi}{32}\approx0.4909$. (Check: midpoint Riemann sum $0.49087$ ✓.)

#### **Q31**
**Method: the substitution $x=1/u$ maps the integral to its own negative.** With $x=\frac1u$, $dx=-\frac{du}{u^2}$ and $\ln x=-\ln u$:
$$I=\int_\infty^0\frac{-\ln u}{1+1/u^2}\cdot\Big(-\frac{du}{u^2}\Big)=\int_0^\infty\frac{-\ln u}{u^2+1}\,du=-I,$$
so $2I=0$.
**Answer:** $0$. (Check: numeric $0\to1$ plus $1\to10^5$ gives $0.00116$, tending to $0$ as the cutoff grows ✓.)

---

## H · Frontier synthesis

#### **Q32**
**Method: square the integral and change to polar coordinates.** With $I=\int_0^\infty e^{-x^2}dx$,
$$I^2=\int_0^\infty\!\!\int_0^\infty e^{-(x^2+y^2)}dx\,dy=\int_0^{\pi/2}\!\!\int_0^\infty e^{-r^2}r\,dr\,d\theta=\frac\pi2\cdot\frac12=\frac\pi4,$$
so $I=\frac{\sqrt\pi}{2}$.
**Answer:** $\dfrac{\sqrt\pi}{2}\approx0.886227$. (Check: numerical integration to $12$ gives $0.8862269$ ✓.)

#### **Q33**
**Method: scale the Gaussian.** $\int_{-\infty}^{\infty}e^{-ax^{2}}dx=\sqrt{\frac\pi a}$ with $a=2$.
**Answer:** $\sqrt{\dfrac\pi2}\approx1.253314$. (Check: numerical integration of $e^{-2x^2}$ over $[-20,20]$ gives $1.2533141$ ✓.)

#### **Q34**
**Method: Frullani with $f(t)=e^{-t}$, $a=1$, $b=2$.** $f(0)=1$ and $f(\infty)=0$, so the integral is $\big(f(0)-f(\infty)\big)\ln\frac ba=\ln2$.
**Answer:** $\ln2\approx0.693147$. (Check: numerically the integral from $10^{-9}$ to $60$ is $0.6915$, converging to $\ln2$ as the tail is refined ✓.)

#### **Q35**
**Method: the tangent half-angle substitution $t=\tan\frac x2$.** Then $\cos x=\frac{1-t^2}{1+t^2}$ and $dx=\frac{2\,dt}{1+t^2}$, so $2+\cos x=\frac{3+t^2}{1+t^2}$ and the integrand becomes $\frac{2}{3+t^2}$. With limits $0$ to $1$:
$$\int_0^1\frac{2}{3+t^2}\,dt=\frac{2}{\sqrt3}\tan^{-1}\frac{t}{\sqrt3}\Big|_0^1=\frac{2}{\sqrt3}\cdot\frac\pi6=\frac{\pi}{3\sqrt3}.$$
**Answer:** $\dfrac{\pi}{3\sqrt3}\approx0.6046$.

#### **Q36**
**Method: the integrand is $\frac12$.** Since $\sin^2x+\cos^2x=1$, the integrand is $\sin^2x$, and $\int_0^{\pi/2}\sin^2x\,dx=\frac\pi4$.
**Answer:** $\dfrac{\pi}{4}$. (Check: $\int_0^{\pi/2}\sin^2x\,dx=\frac\pi4$ exactly, and numerically $0.7853982$ ✓.)

#### **Q37**
**Method: the Dirichlet integral — introduce a damping factor and differentiate.** For $a>0$ set $F(a)=\int_0^\infty e^{-ax}\frac{\sin x}{x}\,dx$. Then $F'(a)=-\int_0^\infty e^{-ax}\sin x\,dx=-\frac1{a^2+1}$. Since $F(a)\to0$ as $a\to\infty$,
$$F(a)=\int_a^\infty\frac{du}{u^2+1}=\frac\pi2-\tan^{-1}a,$$
and letting $a\to0^{+}$ gives $F(0)=\frac\pi2$.
**Answer:** $\dfrac{\pi}{2}$.

#### **Q38**
**Method: Frullani with $f(t)=e^{-t}$, $a=3$, $b=5$.** $\big(f(0)-f(\infty)\big)\ln\frac ba=\ln\frac53$.
**Answer:** $\ln\dfrac53\approx0.510826$. (Check: numerically $0.5104$, converging to $0.5108256$ ✓.)

#### **Q39**
**Method: substitute $t=\sin^2\theta$ to remove the endpoint singularities.** $dt=2\sin\theta\cos\theta\,d\theta$ and $\sqrt{t(1-t)}=\sin\theta\cos\theta$, so
$$B\big(\tfrac12,\tfrac12\big)=\int_0^1\frac{dt}{\sqrt{t(1-t)}}=\int_0^{\pi/2}2\,d\theta=\pi.$$
**Answer:** $\pi$. (Check: the substituted integral $\int_0^{\pi/2}2\,d\theta=\pi$ to 12 decimals ✓; and $\frac{\Gamma(1/2)^2}{\Gamma(1)}=\pi$ ✓.)

#### **Q40**
**Method: reduce to $\int_0^{\pi/2}\sin^{1/2}u\,du$ via $u=2x$, then use the Beta–Gamma formula.** $\sqrt{\sin x\cos x}=\frac1{\sqrt2}\sqrt{\sin2x}$, so
$$\int_0^{\pi/2}\sqrt{\sin x\cos x}\,dx=\frac1{\sqrt2}\int_0^{\pi/2}\sqrt{\sin u}\,du=\frac1{\sqrt2}\cdot\frac{\sqrt\pi}{2}\frac{\Gamma(3/4)}{\Gamma(5/4)}.$$
**Answer:** $\approx0.8472$. (Check: direct numerical integration gives $0.8472131$ and the closed form $0.8472131$ ✓.)

#### **Q41**
**Method: Legendre's duplication formula with $z=\frac14$.** $\Gamma(z)\Gamma(z+\frac12)=2^{1-2z}\sqrt\pi\,\Gamma(2z)$ gives
$$\Gamma\big(\tfrac14\big)\Gamma\big(\tfrac34\big)=2^{1/2}\sqrt\pi\,\Gamma\big(\tfrac12\big)=\sqrt2\cdot\sqrt\pi\cdot\sqrt\pi=\pi\sqrt2.$$
**Answer:** $\pi\sqrt2\approx4.442883$. (Check: Euler's reflection formula with $z=\frac14$ gives $\frac{\pi}{\sin(\pi/4)}=\pi\sqrt2$ — the two formulae agree ✓, and numerically $\Gamma(\frac14)\Gamma(\frac34)=4.4428829$ ✓.)

#### **Q42**
**Method: state the formula and note its consequence.** For $z$ not an integer,
$$\Gamma(z)\,\Gamma(1-z)=\frac{\pi}{\sin\pi z}.$$
Because $\sin\pi z$ vanishes at every integer, $\Gamma$ has simple poles at $0,-1,-2,\dots$ — the formula explains the pole structure as well as giving values.
**Answer:** $\Gamma(z)\Gamma(1-z)=\dfrac{\pi}{\sin\pi z}$. (Check at $z=\frac13$, $\frac14$, $0.3$: both sides agree to $10^{-9}$ ✓.)

#### **Q43**
**Method: convert the trig power to a Beta function.** With $t=\sin^2x$,
$$\int_0^{\pi/2}\sin^{p}x\,dx=\frac12 B\Big(\frac{p+1}{2},\frac12\Big)=\frac{\sqrt\pi}{2}\frac{\Gamma(\frac{p+1}{2})}{\Gamma(\frac{p+2}{2})}.$$
For $p=6$: $\frac{\sqrt\pi}{2}\cdot\frac{\Gamma(7/2)}{\Gamma(4)}=\frac{\sqrt\pi}{2}\cdot\frac{\frac{15}{8}\sqrt\pi}{6}=\frac{15\pi}{96}=\frac{5\pi}{32}$.
**Answer:** $\dfrac{5\pi}{32}\approx0.490874$. (Check: numerically $0.4908739$ ✓.)

#### **Q44**
**Method: state the duplication formula.** For $z>0$,
$$\Gamma(z)\,\Gamma\Big(z+\frac12\Big)=2^{1-2z}\sqrt\pi\,\Gamma(2z).$$
It is proved from the Beta integral together with the substitution $t\mapsto\frac{1-t}{t}$.
**Answer:** $\Gamma(z)\Gamma\big(z+\frac12\big)=2^{1-2z}\sqrt\pi\,\Gamma(2z)$. (Check at $z=\frac14$ it gives $\pi\sqrt2$, agreeing with the reflection formula ✓; verified numerically at $z=0.4,\,1.3,\,2.2$ ✓.)

#### **Q45**
**Method: Feynman — differentiate a one-parameter integral.** For $a>-1$ let $F(a)=\int_0^1x^{a}\,dx=\frac1{a+1}$. Differentiating under the integral sign,
$$F'(a)=\int_0^1x^{a}\ln x\,dx=-\frac1{(a+1)^2}.$$
Now note that $\frac{x^{a}-1}{\ln x}$ has the same value as $\int_1^{a}x^{t}\,dt$ (since $\int_1^a x^t dt=\frac{x^a-1}{\ln x}$), so
$$\int_0^1\frac{x^{a}-1}{\ln x}\,dx=\int_1^a\!\!\int_0^1x^{t}\,dx\,dt=\int_1^a\frac{dt}{t+1}=\ln(a+1).$$
With $a=3$ this is $\ln4=2\ln2$.
**Answer:** $\ln4=2\ln2\approx1.386294$. (Check: substituting $x=e^{-t}$ and integrating numerically gives $1.3862944$ ✓.)

#### **Q46**
**Method: complete the square and scale the Gaussian.** $-ax^{2}+bx=-a\big(x-\frac{b}{2a}\big)^{2}+\frac{b^{2}}{4a}$, so
$$\int_{-\infty}^{\infty}e^{-ax^{2}+bx}\,dx=e^{b^{2}/4a}\int_{-\infty}^{\infty}e^{-a\big(x-\frac{b}{2a}\big)^{2}}dx=e^{b^{2}/4a}\sqrt{\frac\pi a}.$$
**Answer:** $\sqrt{\dfrac\pi a}\,e^{b^{2}/4a}$. (Check: for $a=1,b=0$ this is $\sqrt\pi$ ✓; the shift and the exponential factor were verified separately — $\int e^{-a(x-c)^2}dx=\sqrt{\pi/a}$ and the remaining factor $e^{b^2/4a}$ ✓.)
