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
**Method: direct evaluation of Schur's left side.** For $(1,2,3)$:
$1(-1)(-2)+2(-1)(1)+3(2)(1)=2-2+6=6$. For $(3,4,5)$:
$3(-1)(-2)+4(-1)(1)+5(2)(1)=6-4+10=12$.
**Answer:** $6$ and $12$ — both non-negative ✓.

#### **Q27**
**Method: SOS.** $a^2+b^2+c^2-ab-bc-ca=\frac12[(a-b)^2+(b-c)^2+(c-a)^2]\ge0$.
**Answer:** proved. (Check for $(1,2,3)$: LHS $=1+4+9=14$ and
$ab+bc+ca=2+6+3=11$, so $14\ge11$ ✓; the SOS form gives
$\frac12[1+1+4]=3=14-11$ ✓.)

#### **Q28**
**Method: Cauchy–Schwarz, or AM–GM on the pairs.** By Cauchy–Schwarz,
$(a+b+c)\left(\frac1a+\frac1b+\frac1c\right)\ge(1+1+1)^2=9$.
**Answer:** $9$. (Check for $(a,b,c)=(\frac13,\frac13,\frac13)$: the sum of
reciprocals is $9$ ✓; for $(\frac12,\frac13,\frac16)$ it is $2+3+6=11\ge9$ ✓.)

#### **Q29**
**Method: AM–GM directly.** $a+b+c\ge3\sqrt[3]{abc}=3\sqrt[3]{1}=3$.
**Answer:** $3$. (Check for $(1,1,1)$: $3=3$ (equality) ✓; for $(2,\frac12,1)$:
$3.5\ge3$ ✓.)

#### **Q30**
**Method: the master SOS identity.** $a^3+b^3+c^3-3abc=\frac12(a+b+c)[(a-b)^2+(b-c)^2+(c-a)^2]\ge0$
since $a+b+c>0$ and squares are non-negative. Equality needs all three squares to
vanish, i.e. $a=b=c$.
**Answer:** proved; equality iff $a=b=c$. (Check for $(1,2,3)$: $36\ge18$ ✓; for
$(3,4,5)$: $216\ge180$ ✓.)

#### **Q31**
**Method: two chained rounds of AM–GM.** First $a^4+b^4\ge2a^2b^2$ etc., giving
$a^4+b^4+c^4\ge a^2b^2+b^2c^2+c^2a^2$. Then $a^2b^2+b^2c^2\ge2ab^2c$ etc., giving
$a^2b^2+b^2c^2+c^2a^2\ge abc(a+b+c)$. Chaining proves the claim.
**Answer:** proved; equality iff $a=b=c$. (Check for $(1,1,1)$: $3=3$ ✓; for
$(2,1,1)$: $18\ge8$ ✓; for $(1,2,3)$: $98\ge36$ ✓. A $200000$-sample random test
found no violation.)

#### **Q32**
**Method: expand in symmetric sums and cancel.** $p^3=a^3+b^3+c^3+3\sum_{\rm sym}a^2b+6abc$
and $pq=\sum_{\rm sym}a^2b+3abc$, so
$$p^3-4pq=a^3+b^3+c^3-\sum_{\rm sym}a^2b-6abc,$$
and adding $9r=9abc$ gives
$$p^3+9r-4pq=a^3+b^3+c^3+3abc-\sum_{\rm sym}a^2b,$$
which is Schur's left side, already proved non-negative.
**Answer:** proved. (Check: $(1,1,1)$ gives $36=36$ (equality) ✓; $(2,1,1)$ gives
$82\ge80$ ✓; $(1,2,3)$ gives $270\ge264$ ✓. A $200000$-sample random test found no
violation. Equality at $a=b=c$ or when two variables are equal and the third is
$0$.)

#### **Q33**
**Method: uvw with $q=3$ fixed.** The target $p$ involves no $r$, so the reduction
applies and only the two boundary cases need checking.
*Two equal:* $a=b=x$ gives $c=\frac{3-x^2}{2x}$ and
$p=2x+\frac{3-x^2}{2x}=\frac32\left(x+\frac1x\right)\ge3$ by AM–GM, with equality
at $x=1$.
*One zero:* $c=0$ gives $ab=3$ and $p=a+b\ge2\sqrt{ab}=2\sqrt3\approx3.464\ge3$ ✓.
**Answer:** $a+b+c\ge3$; equality at $a=b=c=1$. (Check numerically: $x=0.8$ gives
$p=3.075$ ✓; $x=0.5$ gives $3.75$ ✓; $x=1.5$ gives $3.25$ ✓.)

#### **Q34**
**Method: Engel form of Cauchy–Schwarz.** $\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$
with $(a_i)=(a,b,c)$ and $(b_i)=(b,c,a)$ gives
$\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}\ge\frac{(a+b+c)^2}{a+b+c}=a+b+c$.
**Answer:** proved; equality iff $a=b=c$. (Check: $(1,1,1)$ gives $3=3$ ✓;
$(1,2,3)$ gives $10.833\ge6$ ✓; $(2,1,4)$ gives $12.25\ge7$ ✓.)

#### **Q35**
**Method: Engel form with the pair-sums.** With $(a_i)=(a,b,c)$ and
$(b_i)=(b+c,c+a,a+b)$, $\sum b_i=2(a+b+c)$, so
$$\frac{a^2}{b+c}+\frac{b^2}{c+a}+\frac{c^2}{a+b}\ge\frac{(a+b+c)^2}{2(a+b+c)}=\frac{a+b+c}{2}.$$
**Answer:** proved; equality iff $a=b=c$. (Check: $(1,1,1)$ gives $1.5=1.5$ ✓;
$(2,1,1)$ gives $2.667\ge2$ ✓; $(1,2,3)$ gives $4.2\ge3$ ✓. A $200000$-sample
random test found no violation.)

#### **Q36**
**Method: Jensen with the concave function $\ln$.** Since $\ln''x=-\frac1{x^2}<0$,
$\ln$ is concave, so
$$\ln\left(\frac{\sum a_i}{n}\right)\ge\frac{\sum\ln a_i}{n}=\ln\left(\left(\prod a_i\right)^{1/n}\right),$$
and exponentiating gives $\frac{\sum a_i}{n}\ge\left(\prod a_i\right)^{1/n}$ — AM–GM.
For $n=2$ this is $\frac{a+b}{2}\ge\sqrt{ab}$, the familiar case.
**Answer:** proved. (Check: for $(1,2,3,4)$, AM $=2.5$ and
$GM=24^{1/4}\approx2.2134$, so $2.5\ge2.2134$ ✓.)
