---
title: "Inequalities — Olympiad Paper"
aliases: ["Inequalities Paper"]
module: "Inequalities"
module_title: "Inequalities"
type: paper
tags: [inequalities, paper, olympiad, algebra]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Inequalities|Chapter 6]] · 📖 [[Inequalities|Complete Notes]] · ✅ [[Inequalities — Solutions|Solutions]] ➡

# Inequalities — Olympiad Paper

> **34 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Inequalities — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · Linear and quadratic inequalities (Q1–Q5)

#### **Q1**[JEE Main][linear]Solve $3x+5>2x-7$.

**Answer:** $x>-12$

#### **Q2**[JEE Main][quadratic]Solve $x^2-5x+6<0$.

**Answer:** $2<x<3$

#### **Q3**[JEE Main][always positive]Solve $x^2+x+1>0$.

**Answer:** all real $x$ ($D=-3<0$, $a>0$)

#### **Q4**[JEE Main][cubic]Solve $(x-1)(x-2)(x-3)>0$.

**Answer:** $x\in(1,2)\cup(3,\infty)$

#### **Q5**[JEE Main][absolute]Solve $\lvert2x-3\rvert\le5$.

**Answer:** $-1\le x\le4$

---

## B · Rational inequalities (Q6–Q10)

#### **Q6**[JEE Main][rational]Solve $\dfrac{x-1}{x+2}>0$.

**Answer:** $x<-2$ or $x>1$

#### **Q7**[JEE Adv][rational]Solve $\dfrac{x}{x^2-1}\le0$.

**Answer:** $x\in(-\infty,-1)\cup[0,1)$

#### **Q8**[JEE Adv][rational]Solve $\dfrac{x^2-4}{x-1}\ge0$.

**Answer:** $x\in[-2,1)\cup[2,\infty)$

#### **Q9**[JEE Main][integers]How many integers satisfy $x^2-5x+6<0$?

**Answer:** none — no integer lies strictly between $2$ and $3$

#### **Q10**[JEE Main][reciprocal]Solve $\dfrac1{x-1}<\dfrac1{x+1}$.

**Answer:** $-1<x<1$

---

## C · Absolute value (Q11–Q15)

#### **Q11**[JEE Main][absolute]Solve $\lvert x-2\rvert<3$.

**Answer:** $-1<x<5$

#### **Q12**[JEE Main][absolute]Solve $\lvert2x+1\rvert\ge5$.

**Answer:** $x\le-3$ or $x\ge2$

#### **Q13**[JEE Main][distance sum]Find the least value of $\lvert x-1\rvert+\lvert x-3\rvert$.

**Answer:** $2$, attained for all $x\in[1,3]$

#### **Q14**[JEE Main][modulus quadratic]Solve $\lvert x\rvert^2-3\lvert x\rvert+2=0$.

**Answer:** $x=\pm1,\;\pm2$

#### **Q15**[JEE Main][nested absolute]Solve $\big\lvert\lvert x-1\rvert-2\big\rvert=3$.

**Answer:** $x=6$ or $x=-4$

---

## D · AM–GM and the mean family (Q16–Q20)

#### **Q16**[JEE Main][amgm]Find the least value of $x+\dfrac1x$ for $x>0$.

**Answer:** $2$ at $x=1$

#### **Q17**[JEE Main][amgm]Find the least value of $x^2+\dfrac1{x^2}$ for $x>0$.

**Answer:** $2$ at $x=1$

#### **Q18**[JEE Main][amgm]Verify AM–GM for $1,2,3$.

**Answer:** $\frac{1+2+3}{3}=2\ge\sqrt[3]{6}\approx1.8171$

#### **Q19**[JEE Main][tradeoff]Given $a+b=10$ with $a,b>0$, find the maximum of $ab$.

**Answer:** $25$ at $a=b=5$

#### **Q20**[JEE Main][tradeoff]Given $ab=9$ with $a,b>0$, find the minimum of $a+b$.

**Answer:** $6$ at $a=b=3$

---

## E · Cauchy–Schwarz, Titu and Nesbitt (Q21–Q25)

#### **Q21**[Olympiad][titu]Prove $\dfrac{a^2}{b}+\dfrac{c^2}{d}\ge\dfrac{(a+c)^2}{b+d}$ for $b,d>0$.

**Answer:** proved by Cauchy–Schwarz; equality when $\dfrac ab=\dfrac cd$

#### **Q22**[JEE Adv][nesbitt]Prove $\dfrac{a}{b+c}+\dfrac{b}{c+a}+\dfrac{c}{a+b}\ge\dfrac32$ for $a,b,c>0$.

**Answer:** proved; equality at $a=b=c$

#### **Q23**[JEE Adv][reciprocal sum]Prove $(a+b+c)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)\ge9$ for $a,b,c>0$.

**Answer:** proved; equality at $a=b=c$

#### **Q24**[JEE Main][cauchy]Verify $(1^2+2^2)(3^2+4^2)\ge(1\cdot3+2\cdot4)^2$.

**Answer:** $125\ge121$ (difference $=(ad-bc)^2=4$)

#### **Q25**[JEE Main][squares]Verify $(a+b+c)^2\ge3(ab+bc+ca)$ for $(a,b,c)=(1,2,3)$.

**Answer:** $36\ge33$

---

## F · Olympiad frontier (Q26–Q31)

#### **Q26**[JEE Adv][schur]Verify Schur's inequality $a(a-b)(a-c)+b(b-c)(b-a)+c(c-a)(c-b)\ge0$ for $(1,2,3)$ and $(3,4,5)$.

**Answer:** $6$ and $12$ — both non-negative

#### **Q27**[Olympiad][cubes]Prove $(a+b+c)^3\ge27abc$ for $a,b,c>0$.

**Answer:** proved (AM–GM cubed); equality at $a=b=c$

#### **Q28**[JEE Main][squares identity]Prove $a^2+b^2+c^2\ge ab+bc+ca$.

**Answer:** difference is $\frac12\sum(a-b)^2\ge0$

#### **Q29**[JEE Adv][constraint]If $a+b+c=1$ with $a,b,c>0$, prove $\dfrac1a+\dfrac1b+\dfrac1c\ge9$.

**Answer:** proved; equality at $a=b=c=\frac13$

#### **Q30**[Olympiad][jensen]Show that AM–GM is a special case of Jensen's inequality.

**Answer:** apply Jensen to the convex function $-\ln x$, then exponentiate

#### **Q31**[Olympiad][substitution]Find the least value of $\dfrac{x^2+2}{\sqrt{x^2+1}}$ for real $x$.

**Answer:** $2$ at $x=0$

---

## G · Applications and mixed (Q32–Q34)

#### **Q32**[JEE Adv][constraint]If $abc=1$ with $a,b,c>0$, prove $a+b+c\ge3$.

**Answer:** proved by AM–GM; equality at $a=b=c=1$

#### **Q33**[JEE Main][integers]Find the number of integers satisfying $\lvert x-2\rvert<3$.

**Answer:** $5$ — namely $x=0,1,2,3,4$

#### **Q34**[JEE Adv][mixed]If $x$ is real and $x^2-3x+2\le0$, find the range of $x+\dfrac1x$.

**Answer:** $\left[2,\dfrac52\right]$

---

> [!note] Exam technique notes
> - **Solving:** find the critical points, then test one point per interval. Never
>   multiply by an expression whose sign you do not know.
> - **Proving:** try to write the difference as a sum of squares. If that fails,
>   try AM–GM; if the variables are ordered, try Schur.
> - Always state the **equality case** — it usually identifies the extremum and
>   is half the marks.
> - Check positivity before quoting any mean inequality.
