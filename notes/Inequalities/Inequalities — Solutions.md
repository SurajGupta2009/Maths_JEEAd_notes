---
title: "Inequalities — Solutions"
aliases: ["Inequalities Solutions"]
module: "Inequalities"
module_title: "Inequalities"
type: solutions
tags: [inequalities, solutions, olympiad, algebra]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Inequalities — Paper|Paper]] · 📖 [[Inequalities|Complete Notes]]

# Inequalities — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[Inequalities — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Linear and quadratic inequalities

#### **Q1**
**Method: collect $x$ on one side.** $3x-2x>-7-5$, so $x>-12$.
**Answer:** $x>-12$. (Check at $x=-11$: $-28>-29$ ✓.)

#### **Q2**
**Method: roots $2,3$; $a>0$ so negative between them.**
**Answer:** $2<x<3$. (Check at $2.5$: $-0.25<0$ ✓.)

#### **Q3**
**Method: $D=1-4=-3<0$ with $a>0$ — no real roots, so the expression never changes sign and is positive at $x=0$.**
**Answer:** all real $x$. (The minimum is $\frac{4-1}{4}=\frac34>0$ ✓.)

#### **Q4**
**Method: mark roots $1,2,3$; the sign is $+$ on $(1,2)$ and $(3,\infty)$.**
**Answer:** $x\in(1,2)\cup(3,\infty)$. (Check at $1.5$: $(+)(-)(-)=+$ ✓; at $2.5$: $(+)(+)(-)=-$ ✓.)

#### **Q5**
**Method: $\lvert u\rvert\le a\iff-a\le u\le a$.** $-5\le2x-3\le5\Rightarrow-2\le2x\le8$.
**Answer:** $-1\le x\le4$. (Check: $\lvert2(-1)-3\rvert=5$ and $\lvert2(4)-3\rvert=5$, both included ✓.)

---

## B · Rational inequalities

#### **Q6**
**Method: critical points $-2,1$; alternate signs; exclude $x=-2$.**
**Answer:** $x<-2$ or $x>1$. (Check at $-3$: $\frac{-4}{-1}=4>0$ ✓; at $0$: $-\frac12<0$ ✓.)

#### **Q7**
**Method: critical points $-1,0,1$; include $x=0$ (numerator zero), exclude $x=\pm1$ (denominator zero).**
**Answer:** $x\in(-\infty,-1)\cup[0,1)$. (Check at $-\frac12$: $\frac{-1/2}{-3/4}>0$ ✓; at $\frac12$: $<0$ ✓; at $2$: $>0$ ✓.)

#### **Q8**
**Method: numerator roots $\pm2$, denominator root $1$; include $x=\pm2$, exclude $x=1$.**
**Answer:** $x\in[-2,1)\cup[2,\infty)$. (Check at $0$: $\frac{-4}{-1}=4\ge0$ ✓.)

#### **Q9**
**Method: solve first, then count.** $x^2-5x+6<0\Rightarrow2<x<3$, which contains no integer.
**Answer:** $0$ integers.

#### **Q10**
**Method: bring to one side rather than cross-multiplying.** $\frac1{x-1}-\frac1{x+1}=\frac{2}{x^2-1}<0$, so $x^2-1<0$.
**Answer:** $-1<x<1$. (Check at $x=0$: $-1<1$ ✓; at $x=2$: $1<\frac13$ false ✓.)

---

## C · Absolute value

#### **Q11**
**Method: $-3<x-2<3$.**
**Answer:** $-1<x<5$ (open, since the endpoints give equality with $3$).

#### **Q12**
**Method: $\lvert u\rvert\ge a\iff u\le-a$ or $u\ge a$.** $2x+1\le-5$ or $2x+1\ge5$.
**Answer:** $x\le-3$ or $x\ge2$. (Check: $\lvert2(-3)+1\rvert=5$ ✓; $\lvert2(2)+1\rvert=5$ ✓.)

#### **Q13**
**Method: the sum of distances to two fixed points is minimised anywhere between them, where it equals the distance between them.**
**Answer:** least value $\lvert1-3\rvert=2$, attained for every $x\in[1,3]$.

#### **Q14**
**Method: let $t=\lvert x\rvert\ge0$.** $t^2-3t+2=0\Rightarrow t=1$ or $t=2$, both admissible.
**Answer:** $x=\pm1,\;\pm2$. (Check: $1-3+2=0$ and $4-6+2=0$ ✓.)

#### **Q15**
**Method: peel from the outside.** $\lvert x-1\rvert-2=\pm3$, so $\lvert x-1\rvert=5$ (the value $-1$ is impossible).
**Answer:** $x=6$ or $x=-4$. (Check: $\lvert\lvert6-1\rvert-2\rvert=\lvert5-2\rvert=3$ ✓.)

---

## D · AM–GM and the mean family

#### **Q16**
**Method: AM–GM on $x$ and $\frac1x$.** $x+\frac1x\ge2\sqrt{x\cdot\frac1x}=2$, equality at $x=1$.
**Answer:** least value $2$ at $x=1$.

#### **Q17**
**Method: AM–GM on $x^2$ and $\frac1{x^2}$.** $\ge2\sqrt{x^2\cdot\frac1{x^2}}=2$, equality at $x^2=\frac1{x^2}$, i.e. $x=1$.
**Answer:** least value $2$ at $x=1$.

#### **Q18**
**Method: compare the arithmetic and geometric means.** $\frac{1+2+3}{3}=2$ and $\sqrt[3]{1\cdot2\cdot3}=\sqrt[3]{6}\approx1.8171$.
**Answer:** $2\ge1.8171$, so AM–GM holds ✓.

#### **Q19**
**Method: $ab\le\left(\frac{a+b}{2}\right)^2$.** $\le\left(\frac{10}{2}\right)^2=25$.
**Answer:** maximum $25$ at $a=b=5$.

#### **Q20**
**Method: $a+b\ge2\sqrt{ab}$.** $\ge2\sqrt9=6$.
**Answer:** minimum $6$ at $a=b=3$.

---

## E · Cauchy–Schwarz, Titu and Nesbitt

#### **Q21**
**Method: Cauchy–Schwarz on $\left(\frac a{\sqrt b},\frac c{\sqrt d}\right)$ and $(\sqrt b,\sqrt d)$.**
$$\left(\frac{a^2}{b}+\frac{c^2}{d}\right)(b+d)\ge\left(\frac a{\sqrt b}\sqrt b+\frac c{\sqrt d}\sqrt d\right)^2=(a+c)^2,$$
and dividing by $b+d>0$ gives the claim.
**Answer:** proved; equality when $\frac ab=\frac cd$. (Numeric check with $a=1,c=2,b=3,d=4$: LHS $=\frac43\approx1.3333$, RHS $=\frac97\approx1.2857$ ✓.)

#### **Q22**
**Method: substitute $x=b+c$, $y=c+a$, $z=a+b$, then pair the reciprocals.**
$$\sum_{\rm cyc}\frac{a}{b+c}=\frac12\left[\left(\frac yx+\frac xy\right)+\left(\frac zx+\frac xz\right)+\left(\frac zy+\frac yz\right)-3\right]\ge\frac12(2+2+2-3)=\frac32.$$
**Answer:** proved, equality at $a=b=c$. (Numeric check for $(1,2,3)$: $\frac{47}{30}\approx1.5667\ge1.5$ ✓.)

#### **Q23**
**Method: expand and pair each term with its reciprocal.**
$$(a+b+c)\left(\frac1a+\frac1b+\frac1c\right)=3+\left(\frac ab+\frac ba\right)+\left(\frac bc+\frac cb\right)+\left(\frac ca+\frac ac\right)\ge3+2+2+2=9.$$
**Answer:** proved, equality at $a=b=c$. (Numeric check for $(1,2,3)$: $11\ge9$ ✓.)

#### **Q24**
**Method: evaluate both sides; the difference is the Cauchy defect $(ad-bc)^2$.**
$(1+4)(9+16)=125$ and $(3+8)^2=121$; the difference is $(1\cdot4-2\cdot3)^2=4$, and $125-121=4$ ✓.
**Answer:** $125\ge121$.

#### **Q25**
**Method: evaluate both sides.** $(1+2+3)^2=36$ and $3(1\cdot2+2\cdot3+3\cdot1)=3\cdot11=33$.
**Answer:** $36\ge33$ ✓.

---

## F · Olympiad frontier

#### **Q26**
**Method: evaluate $a(a-b)(a-c)+b(b-c)(b-a)+c(c-a)(c-b)$ directly.** For $(1,2,3)$: $1(-1)(-2)+2(-1)(1)+3(2)(1)=2-2+6=6$. For $(3,4,5)$: $3(-1)(-2)+4(-1)(1)+5(2)(1)=6-4+10=12$.
**Answer:** $6$ and $12$ — both $\ge0$, consistent with Schur ✓.

#### **Q27**
**Method: AM–GM on three numbers, then cube.** $\frac{a+b+c}{3}\ge\sqrt[3]{abc}$, so $a+b+c\ge3\sqrt[3]{abc}$ and cubing gives $(a+b+c)^3\ge27abc$.
**Answer:** proved, equality at $a=b=c$. (Numeric check for $(1,2,3)$: $6^3=216\ge27\cdot6=162$ ✓.)

#### **Q28**
**Method: double both sides and complete the squares.**
$$2(a^2+b^2+c^2-ab-bc-ca)=(a-b)^2+(b-c)^2+(c-a)^2\ge0.$$
**Answer:** proved, equality iff $a=b=c$. (Numeric check for $(1,2,3)$: $14\ge11$ ✓.)

#### **Q29**
**Method: apply Q23 and use $a+b+c=1$.**
$$(a+b+c)\left(\frac1a+\frac1b+\frac1c\right)\ge9\implies\frac1a+\frac1b+\frac1c\ge9.$$
**Answer:** proved, equality at $a=b=c=\frac13$. (Check: $3+3+3=9$ ✓.)

#### **Q30**
**Method: $-\ln x$ is convex on $x>0$, so Jensen gives $-\ln\left(\frac{\sum x_i}{n}\right)\le\frac{\sum(-\ln x_i)}{n}$.** Exponentiating both sides yields
$$\frac{\sum x_i}{n}\ge\left(\prod x_i\right)^{1/n},$$
which is AM–GM.
**Answer:** AM–GM is Jensen applied to the convex function $-\ln x$.

#### **Q31**
**Method: substitute $t=\sqrt{x^2+1}\ge1$.** Then $x^2+2=t^2+1$, so the expression is $\frac{t^2+1}{t}=t+\frac1t\ge2$ by AM–GM, with equality at $t=1$, i.e. $x=0$. Since $t+\frac1t$ is increasing for $t\ge1$, the minimum on the admissible range is attained at $t=1$.
**Answer:** least value $2$ at $x=0$. (Check at $x=1$: $\frac3{\sqrt2}\approx2.1213>2$ ✓.)

---

## G · Applications and mixed

#### **Q32**
**Method: AM–GM on three numbers.** $a+b+c\ge3\sqrt[3]{abc}=3\sqrt[3]{1}=3$.
**Answer:** proved, equality at $a=b=c=1$. (Numeric check for $(2,\frac12,1)$: $3.5\ge3$ ✓.)

#### **Q33**
**Method: solve first, then count.** $\lvert x-2\rvert<3\Rightarrow-1<x<5$, whose integers are $0,1,2,3,4$.
**Answer:** $5$ integers.

#### **Q34**
**Method: find the interval for $x$, then the range of $x+\frac1x$ on it.** $x^2-3x+2\le0\Rightarrow(x-1)(x-2)\le0\Rightarrow1\le x\le2$. On $[1,2]$ the function $x+\frac1x$ has derivative $1-\frac1{x^2}\ge0$, so it is increasing; hence the range is $[f(1),f(2)]=\left[2,\frac52\right]$.
**Answer:** $\left[2,\dfrac52\right]$. (Check: the minimum $2$ is attained at $x=1$ and the maximum $\frac52$ at $x=2$; a fine scan of $[1,2]$ confirms both ✓.)
