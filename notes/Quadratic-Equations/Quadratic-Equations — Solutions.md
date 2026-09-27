---
title: "Quadratic Equations — Solutions"
aliases: ["Quadratic Equations Solutions"]
module: "Quadratic-Equations"
module_title: "Quadratic Equations"
type: solutions
tags: [quadratic-equations, solutions, olympiad, algebra, polynomials]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Quadratic-Equations — Paper|Paper]] · 📖 [[Quadratic-Equations|Complete Notes]]

# Quadratic Equations — Solutions

> Full solutions to all 34 questions, same Q-ids as the
> [[Quadratic-Equations — Paper|paper]]. Every solution: **method first →
> derivation → a check.** Every numeric answer was verified in pure Python
> (stdlib only) before this file was written.

---

## A · Roots and the discriminant

#### **Q1**
**Method: the quadratic formula.** $D=25-24=1$, so $x=\frac{5\pm1}{2}$.
**Answer:** $x=2,\;3$. (Factorising: $(x-2)(x-3)=0$ ✓.)

#### **Q2**
**Method: compute $D=b^2-4ac$ and read off the case.** $D=(-3)^2-4(2)(5)=9-40=-31<0$.
**Answer:** no real roots; two non-real conjugate roots $\frac{3\pm i\sqrt{31}}{4}$.

#### **Q3**
**Method: Vieta directly.** Sum $=-\frac ba=-\frac{-7}{3}=\frac73$; product $=\frac ca=\frac23$.
**Answer:** sum $\dfrac73$, product $\dfrac23$. (Check by solving: $D=49-24=25$, $x=\frac{7\pm5}{6}$, so $2$ and $\frac13$ ✓.)

#### **Q4**
**Method: $D=0$ means a repeated root.** $D=16-16=0$.
**Answer:** equal roots, $x=-\frac b{2a}=2$ (double).

#### **Q5**
**Method: set $D=0$.** $k^2-4(1)(9)=k^2-36=0$.
**Answer:** $k=\pm6$.

---

## B · Vieta and symmetric functions

Here $S=\alpha+\beta=5$ and $P=\alpha\beta=6$.

#### **Q6**
**Method: $\alpha^2+\beta^2=S^2-2P$.** $25-12=13$.
**Answer:** $13$. (Check with roots $2,3$: $4+9=13$ ✓.)

#### **Q7**
**Method: $\alpha^3+\beta^3=S^3-3PS$.** $125-3(6)(5)=125-90=35$.
**Answer:** $35$. (Check: $8+27=35$ ✓.)

#### **Q8**
**Method: $\frac1\alpha+\frac1\beta=\frac SP$.** $\frac56$.
**Answer:** $\dfrac56$. (Check: $\frac12+\frac13=\frac56$ ✓.)

#### **Q9**
**Method: $\alpha^2\beta+\alpha\beta^2=\alpha\beta(\alpha+\beta)=PS$.** $6\cdot5=30$.
**Answer:** $30$. (Check: $4\cdot3+2\cdot9=30$ ✓.)

#### **Q10**
**Method: $(\alpha-\beta)^2=S^2-4P$; then take the root.** $25-24=1$.
**Answer:** $(\alpha-\beta)^2=1$ and $\lvert\alpha-\beta\rvert=1$. (Cross-check: $\frac{\sqrt D}{\lvert a\rvert}=\frac11=1$ ✓.)

---

## C · The quadratic expression

#### **Q11**
**Method: complete the square.** $x^2-6x+11=(x-3)^2+2$.
**Answer:** minimum $2$ at $x=3$. (Formula check: $\frac{4ac-b^2}{4a}=\frac{44-36}{4}=2$ ✓.)

#### **Q12**
**Method: factor out $-1$, then complete the square.** $-x^2+4x-1=-(x-2)^2+3$.
**Answer:** maximum $3$ at $x=2$.

#### **Q13**
**Method: substitute $x=0$.** $0-0-6=-6<0$.
**Answer:** negative.

#### **Q14**
**Method: roots are $2$ and $3$; since the leading coefficient is positive the expression is negative between the roots.**
**Answer:** $2<x<3$. (Check at $x=2.5$: $6.25-12.5+6=-0.25<0$ ✓.)

#### **Q15**
**Method: AM–GM on $x$ and $\frac4x$.** $x+\frac4x\ge2\sqrt{x\cdot\frac4x}=2\sqrt4=4$, with equality when $x=\frac4x$, i.e. $x=2$.
**Answer:** least value $4$ at $x=2$. (Check: $2+2=4$ ✓.)

---

## D · Equations reducible to quadratics

#### **Q16**
**Method: substitute $t=x^2$.** $t^2-5t+4=0\Rightarrow t=1$ or $t=4$; both are $\ge0$.
**Answer:** $x=\pm1,\;\pm2$. (Check: $1-5+4=0$ and $16-20+4=0$ ✓.)

#### **Q17**
**Method: substitute $t=x+1$ (do not divide by $x+1$).** $t^2=4t\Rightarrow t=0$ or $t=4$.
**Answer:** $x=-1,\;3$. (Check: $0=0$ ✓ and $16=16$ ✓.)

#### **Q18**
**Method: square, solve, then verify in the original.** $x+3=(x-3)^2\Rightarrow x^2-7x+6=0\Rightarrow x=1$ or $x=6$. Verify: at $x=1$, LHS $=2$, RHS $=-2$ — reject; at $x=6$, LHS $=3$, RHS $=3$ — accept.
**Answer:** $x=6$ only.

#### **Q19**
**Method: substitute $t=x+\frac1x$, using $x^2+\frac1{x^2}=t^2-2$.** $t^2-2=7\Rightarrow t=\pm3$. For $t=3$: $x^2-3x+1=0\Rightarrow x=\frac{3\pm\sqrt5}{2}$. For $t=-3$: $x^2+3x+1=0\Rightarrow x=\frac{-3\pm\sqrt5}{2}$.
**Answer:** $x=\dfrac{3\pm\sqrt5}{2}$ and $x=\dfrac{-3\pm\sqrt5}{2}$. (Check at $x=\frac{3+\sqrt5}{2}\approx2.618$: $x^2+\frac1{x^2}=7$ ✓.)

#### **Q20**
**Method: substitute $t=2^x>0$.** $t^2-5t+4=0\Rightarrow t=1$ or $t=4$; both positive.
**Answer:** $x=0,\;2$. (Check: $1-5+4=0$ and $16-20+4=0$ ✓.)

---

## E · Common roots and transformed equations

#### **Q21**
**Method: subtract the two equations to get a linear equation.** $(x^2-5x+6)-(x^2-4x+3)=-x+3=0\Rightarrow x=3$.
**Answer:** $x=3$. (Check: $9-15+6=0$ and $9-12+3=0$ ✓.)

#### **Q22**
**Method: subtract to get $(p-r)x+(q-s)=0$, so a common root must be $x=\frac{s-q}{p-r}$; substituting this into either quadratic and clearing denominators gives the condition.** Equivalently the standard result is
$$(p-r)^2=(q-s)(r-p).$$
**Answer:** $(p-r)^2=(q-s)(r-p)$ (when $p\ne r$; if $p=r$ the quadratics are identical up to a constant).

#### **Q23**
**Method: build the equation from the sum and product.** Sum $=4$; product $=(2+\sqrt3)(2-\sqrt3)=4-3=1$.
**Answer:** $x^2-4x+1=0$. (Check: the roots of this are $2\pm\sqrt3$ ✓.)

#### **Q24**
**Method: reciprocal roots swap the roles of sum and product.** New sum $=\frac SP=\frac56$; new product $=\frac1P=\frac16$.
**Answer:** $6x^2-5x+1=0$. (Check: the roots of this are $\frac13,\frac12$ ✓.)

#### **Q25**
**Method: shift the sum and product by $1$.** New sum $=S+2=7$; new product $=P+S+1=6+5+1=12$.
**Answer:** $x^2-7x+12=0$. (Check with the actual shifted roots $3,4$: sum $7$, product $12$ ✓.)

---

## F · The parabola and location of roots

#### **Q26**
**Method: $x=-\frac b{2a}$ and $y=\frac{4ac-b^2}{4a}$.** $x=\frac88=2$; $y=\frac{40-64}{8}=-3$.
**Answer:** vertex $(2,-3)$, axis $x=2$. (Check: $2(4)-16+5=-3$ ✓.)

#### **Q27**
**Method: solve explicitly — the roots are $k\pm1$.** Both exceed $1$ iff the smaller one does: $k-1>1\Rightarrow k>2$. (The discriminant is $4>0$ always, so no extra condition is needed ✓.)
**Answer:** $k>2$.

---

## G · Olympiad inequalities

#### **Q28**
**Method: substitute $x=b+c$, $y=c+a$, $z=a+b$, so that $a=\frac{y+z-x}{2}$, and pair the reciprocals with AM–GM.**
$$\sum_{\rm cyc}\frac{a}{b+c}=\frac12\left[\left(\frac yx+\frac xy\right)+\left(\frac zx+\frac xz\right)+\left(\frac zy+\frac yz\right)-3\right]\ge\frac12(2+2+2-3)=\frac32.$$
**Answer:** proved, with equality at $a=b=c$. (Numeric check for $(1,2,3)$: $\frac13+\frac24+\frac35=\frac{47}{30}\approx1.5667\ge1.5$ ✓.)

#### **Q29**
**Method: AM–GM on $x$ and $\frac1x$.** $x+\frac1x\ge2\sqrt{x\cdot\frac1x}=2$, with equality at $x=1$.
**Answer:** least value $2$ at $x=1$.

#### **Q30**
**Method: expand and pair each term with its reciprocal.**
$$(a+b+c)\left(\frac1a+\frac1b+\frac1c\right)=3+\left(\frac ab+\frac ba\right)+\left(\frac bc+\frac cb\right)+\left(\frac ca+\frac ac\right)\ge3+2+2+2=9.$$
**Answer:** proved, with equality at $a=b=c$. (Numeric check for $(1,2,3)$: $6\cdot\frac{11}{6}=11\ge9$ ✓.)

#### **Q31**
**Method: Cauchy–Schwarz on $\left(\frac a{\sqrt b},\frac c{\sqrt d}\right)$ and $(\sqrt b,\sqrt d)$.**
$$\left(\frac{a^2}{b}+\frac{c^2}{d}\right)(b+d)\ge\left(\frac a{\sqrt b}\sqrt b+\frac c{\sqrt d}\sqrt d\right)^2=(a+c)^2.$$
**Answer:** proved; equality when $\frac ab=\frac cd$. (Numeric check for $a=1,c=2,b=3,d=4$: LHS $=\frac13+1=\frac43\approx1.3333$, RHS $=\frac97\approx1.2857$ ✓.)

---

## H · Olympiad frontier

#### **Q32**
**Method: expand the proposed factorisation.**
$$(a+b+c)(a^2+b^2+c^2-ab-bc-ca)=a^3+b^3+c^3-3abc.$$
Setting $a+b+c=0$ makes the left side vanish, so $a^3+b^3+c^3-3abc=0$.
**Answer:** $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$; and if $a+b+c=0$ then $a^3+b^3+c^3=3abc$. (Numeric check: for $(1,1,-2)$, $-6=3(1)(1)(-2)=-6$ ✓.)

#### **Q33**
**Method: evaluate $a(a-b)(a-c)+b(b-c)(b-a)+c(c-a)(c-b)$ directly.** For $(1,2,3)$: $1(-1)(-2)+2(-1)(1)+3(2)(1)=2-2+6=6$. For $(3,4,5)$: $3(-1)(-2)+4(-1)(1)+5(2)(1)=6-4+10=12$.
**Answer:** $6$ and $12$ — both non-negative, consistent with Schur ✓.

#### **Q34**
**Method: rational-root theorem, then reduce to a quadratic.** Candidates are $\pm1,\pm2,\pm3,\pm6$; $x=1$ gives $1-6+11-6=0$, so $(x-1)$ is a factor. Dividing gives $x^2-5x+6=(x-2)(x-3)$.
**Answer:** $x=1,\;2,\;3$. (Check: $1-6+11-6=0$, $8-24+22-6=0$, $27-54+33-6=0$ ✓; and the roots sum to $6$ with pairwise products summing to $11$ and product $6$ ✓.)
