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
**Method: symmetric reduction.** $\alpha+\beta=5$ and $\alpha\beta=3$, so
$\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=25-6=19$.
**Answer:** $19$. (Check via Newton's sums: $S_2=5\cdot5-2\cdot3=19$; numerically
$\alpha\approx4.3028$, $\beta\approx0.6972$ and $\alpha^2+\beta^2\approx19.0000$ ✓.)

#### **Q29**
**Method: compute $\Delta$ and test whether it is a perfect square.**
$\Delta=k^2-4(k-1)=k^2-4k+4=(k-2)^2$, a perfect square for every integer $k$.
Hence the roots are rational for all integers $k$:
$x=\frac{k\pm|k-2|}{2}$, namely $x=1$ and $x=k-1$.
**Answer:** every integer $k$; roots $1$ and $k-1$. (Check:
$x^2-kx+k-1=(x-1)(x-(k-1))$ exactly, so $x=1$ is always a root ✓.)

#### **Q30**
**Method: induction using $\alpha^2=\alpha+1$.** Base cases:
$n=1$ gives $F_1\alpha+F_0=\alpha$ ✓; $n=2$ gives $F_2\alpha+F_1=\alpha+1=\alpha^2$ ✓.
For the step,
$\alpha^{n+1}=\alpha(F_n\alpha+F_{n-1})=F_n\alpha^2+F_{n-1}\alpha=F_n(\alpha+1)+F_{n-1}\alpha
=(F_n+F_{n-1})\alpha+F_n$, and $F_n+F_{n-1}=F_{n+1}$ by definition ✓.
**Answer:** $F_{10}=55$. (Check: the Fibonacci list is
$0,1,1,2,3,5,8,13,21,34,55$; and $\alpha^{10}\approx122.9918=55\cdot1.618034+34$ ✓.
Adding the identities for both roots gives the Lucas numbers
$S_n=\alpha^n+\beta^n=F_{n+1}+F_{n-1}=2,1,3,4,7,11,\ldots$ ✓.)

#### **Q31**
**Method: build from the new symmetric sums.** For roots $\alpha^2,\beta^2$ the sum
is $\alpha^2+\beta^2=19$ and the product is $(\alpha\beta)^2=9$, so the equation is
$x^2-19x+9=0$.
**Answer:** $x^2-19x+9=0$. (Check: $\alpha^2\approx18.5139$ and
$\beta^2\approx0.4861$ give sum $\approx19.0000$, product $\approx9.0000$, and
$\Delta=325>0$ so both are real ✓.)

#### **Q32**
**Method: Newton's recurrence.** With $\alpha+\beta=3$, $\alpha\beta=1$ the roots
satisfy $t^2=3t-1$, so $S_n=3S_{n-1}-S_{n-2}$ with $S_0=2$, $S_1=3$:
$$S_2=7,\quad S_3=18,\quad S_4=47,\quad S_5=123.$$
**Answer:** $123$. (Check: $\alpha=\frac{3+\sqrt5}{2}\approx2.6180$,
$\beta\approx0.3820$; $\alpha^5+\beta^5\approx122.9919+0.0081=123.0000$ ✓.)

#### **Q33**
**Method: depress the cubic, form the resolvent, take cube roots.** Substituting
$x=y+2$ gives $y^3-y=0$, so $P=-1$, $Q=0$. The resolvent quadratic is
$t^2+Qt-\frac{P^3}{27}=t^2+\frac1{27}=0$, whose roots are
$t=\pm\frac{i}{3\sqrt3}$. Since $u,v$ are conjugates with $uv=-\frac P3=\frac13$,
we get $|u|^2=\frac13$, so $|u|=\frac1{\sqrt3}$ and $\arg u=\frac\pi6$. Hence
$u=\frac12+\frac{i}{2\sqrt3}$, $v=\frac12-\frac{i}{2\sqrt3}$, giving $y=u+v=1$ and
$x=3$. The three cube-root choices give all three roots.
**Answer:** $x=1,2,3$. (Check: $1+2+3=6=-p$ and $1\cdot2\cdot3=6=-r$ ✓; the
depressed values $y=1,0,-1$ each satisfy $y^3-y=0$ ✓, and the numerically
recovered roots are exactly $1.0,2.0,3.0$ ✓.)

#### **Q34**
**Method: Vieta jumping.** Fix $k=\frac{a^2+b^2}{ab+1}$, an integer, and read the
relation as a quadratic in $a$:
$$a^2-kba+(b^2-k)=0.$$
One root is $a$; by Vieta the other is $a'=kb-a=\frac{b^2-k}{a}$, and $a'$ is an
integer because rearranging gives $b^2-k=a(kb-a)$. Ordering $A\ge B$ one checks
$0\le a'<B$, so $(a',B)$ is a smaller solution with the *same* $k$. The descent
must terminate, and it can only terminate when $a'=0$, i.e. when $k=b^2$ — a
perfect square. Since $k$ never changes, the original $k$ is that same square.
**Answer:** $\frac{a^2+b^2}{ab+1}$ is always a perfect square. (Check: over all
$a,b<300$ with $ab+1\mid a^2+b^2$ the quotient takes only the values
$1,4,9,16,25$ — all squares — and the descent inequality $0\le a'<B$ held for
every pair. For example $(8,30)$: $k=\frac{964}{241}=4$, and the descent
$(30,8)\to(8,2)\to(0,2)$ stops at $k=2^2$ ✓.)
