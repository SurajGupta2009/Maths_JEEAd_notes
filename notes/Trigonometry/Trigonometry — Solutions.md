---
title: "Trigonometry — Solutions"
aliases: ["Trigonometry Solutions"]
module: "Trigonometry"
module_title: "Trigonometry"
type: solutions
tags: [trigonometry, solutions, olympiad, algebra, geometry]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Trigonometry — Paper|Paper]] · 📖 [[Trigonometry|Complete Notes]]

# Trigonometry — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[Trigonometry — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Ratios and identities

#### **Q1**
**Method: substitute the standard values.** $\sin30^\circ=\frac12$, $\cos30^\circ=\frac{\sqrt3}{2}$, so $\frac14+\frac34=1$.
**Answer:** $1$ ✓.

#### **Q2**
**Method: standard value.** In the $45^\circ$-$45^\circ$-$90^\circ$ triangle, opposite $=$ adjacent.
**Answer:** $\tan45^\circ=1$.

#### **Q3**
**Method: allied-angle rule.** $\sin135^\circ=\sin(180^\circ-45^\circ)=\sin45^\circ$.
**Answer:** $\dfrac{\sqrt2}{2}\approx0.7071$.

#### **Q4**
**Method: compound-angle formula.** $\sin75^\circ=\sin(45^\circ+30^\circ)=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}+\frac{\sqrt2}{2}\cdot\frac12=\frac{\sqrt6+\sqrt2}{4}$.
**Answer:** $\dfrac{\sqrt6+\sqrt2}{4}\approx0.9659$.

#### **Q5**
**Method: allied-angle rule.** $\cos225^\circ=\cos(180^\circ+45^\circ)=-\cos45^\circ$.
**Answer:** $-\dfrac{\sqrt2}{2}\approx-0.7071$.

---

## B · Compound angles

#### **Q6**
**Method: $\tan(A+B)=\frac{\tan A+\tan B}{1-\tan A\tan B}$.**
$$\frac{1+\sqrt3}{1-\sqrt3}=\frac{(1+\sqrt3)^2}{(1-\sqrt3)(1+\sqrt3)}=\frac{4+2\sqrt3}{-2}=-(2+\sqrt3).$$
**Answer:** $-(2+\sqrt3)\approx-3.7321$.

#### **Q7**
**Method: $\cos(A-B)=\cos A\cos B+\sin A\sin B$ — note the plus sign.** $\frac12\cdot\frac{\sqrt3}{2}+\frac{\sqrt3}{2}\cdot\frac12=\frac{\sqrt3}{2}$.
**Answer:** $\dfrac{\sqrt3}{2}=\cos30^\circ$ ✓.

#### **Q8**
**Method: find the missing cosines by Pythagoras, then apply $\sin(A+B)$.** $\cos A=\sqrt{1-\frac9{25}}=\frac45$ and $\sin B=\sqrt{1-\frac{25}{169}}=\frac{12}{13}$. So
$$\sin(A+B)=\frac35\cdot\frac5{13}+\frac45\cdot\frac{12}{13}=\frac{15+48}{65}=\frac{63}{65}.$$
**Answer:** $\dfrac{63}{65}\approx0.9692$.

#### **Q9**
**Method: the three forms of $\cos2A$, and $\sin2A=2\sin A\cos A$.** With $\cos A=\frac35$, $\sin A=\frac45$:
$$\cos2A=2\cdot\frac9{25}-1=\frac{18-25}{25}=-\frac7{25},\qquad \sin2A=2\cdot\frac45\cdot\frac35=\frac{24}{25}.$$
**Answer:** $\cos2A=-\dfrac7{25}$, $\sin2A=\dfrac{24}{25}$. (Check: $(-7/25)^2+(24/25)^2=\frac{49+576}{625}=1$ ✓.)

#### **Q10**
**Method: $\tan(A-B)=\frac{\tan A-\tan B}{1+\tan A\tan B}$.**
$$\frac{\frac12-\frac13}{1+\frac12\cdot\frac13}=\frac{\frac16}{\frac76}=\frac17.$$
**Answer:** $\dfrac17\approx0.1429$.

---

## C · Multiple and submultiple angles

#### **Q11**
**Method: substitute $A=30^\circ$ into $\sin3A=3\sin A-4\sin^3A$.** $3\cdot\frac12-4\cdot\frac18=\frac32-\frac12=1$.
**Answer:** $1=\sin90^\circ$ ✓.

#### **Q12**
**Method: substitute $A=30^\circ$ into $\cos3A=4\cos^3A-3\cos A$.** $4\cdot\frac{3\sqrt3}{8}-3\cdot\frac{\sqrt3}{2}=\frac{3\sqrt3}{2}-\frac{3\sqrt3}{2}=0$.
**Answer:** $0=\cos90^\circ$ ✓.

#### **Q13**
**Method: substitute $A=30^\circ$ into $\tan2A=\frac{2\tan A}{1-\tan^2A}$.** $\frac{2/\sqrt3}{1-1/3}=\frac{2/\sqrt3}{2/3}=\frac3{\sqrt3}=\sqrt3$.
**Answer:** $\sqrt3=\tan60^\circ$ ✓.

#### **Q14**
**Method: the half-angle formula, positive root since $30^\circ$ is in quadrant I.** $\sqrt{\frac{1-\frac12}{2}}=\sqrt{\frac14}=\frac12$.
**Answer:** $\dfrac12=\sin30^\circ$ ✓.

#### **Q15**
**Method: $1+\cos A=2\cos^2\frac A2$.** LHS $=1+\frac12=\frac32$; RHS $=2\cdot\frac34=\frac32$.
**Answer:** $\frac32=\frac32$ ✓.

---

## D · Transformation formulae and sums

#### **Q16**
**Method: $\sin C+\sin D=2\sin\frac{C+D}{2}\cos\frac{C-D}{2}$.** $\frac{C+D}{2}=45^\circ$, $\frac{C-D}{2}=30^\circ$:
$$2\sin45^\circ\cos30^\circ=2\cdot\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}=\frac{\sqrt6}{2}.$$
**Answer:** $\dfrac{\sqrt6}{2}\approx1.2247$.

#### **Q17**
**Method: $\cos C-\cos D=-2\sin\frac{C+D}{2}\sin\frac{C-D}{2}$.**
$$-2\sin45^\circ\sin30^\circ=-2\cdot\frac{\sqrt2}{2}\cdot\frac12=-\frac{\sqrt2}{2}.$$
**Answer:** $-\dfrac{\sqrt2}{2}\approx-0.7071$.

#### **Q18**
**Method: $2\sin A\cos B=\sin(A+B)+\sin(A-B)$.** $=\sin75^\circ+\sin15^\circ$.
**Answer:** $\sin75^\circ+\sin15^\circ$. (Check: $2\cdot0.7071\cdot0.8660=1.2247$ and $0.9659+0.2588=1.2247$ ✓.)

#### **Q19**
**Method: $\sin A\cos B=\frac12\big(\sin(A+B)+\sin(A-B)\big)$.**
$$\sin50^\circ\cos20^\circ=\frac12(\sin70^\circ+\sin30^\circ).$$
**Answer:** $\frac12(\sin70^\circ+\sin30^\circ)\approx0.7198$. (Check directly: $0.7660\cdot0.9397=0.7198$ ✓.)

#### **Q20**
**Method: multiply by $2\sin\frac\theta2$ and telescope.** Since
$2\sin\frac\theta2\sin k\theta=\cos\left(k-\frac12\right)\theta-\cos\left(k+\frac12\right)\theta$, the sum becomes $\cos\frac\theta2-\cos\left(n+\frac12\right)\theta=2\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}$. Dividing by $2\sin\frac\theta2$ gives the result.
**Answer:** $\dfrac{\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac\theta2}$.

---

## E · Trigonometric equations

#### **Q21**
**Method: $\sin\theta=\sin\alpha\Rightarrow\theta=n\pi+(-1)^n\alpha$ with $\alpha=30^\circ=\frac\pi6$.**
**Answer:** $x=n\pi+(-1)^n\dfrac\pi6$. (Check: $n=1$ gives $\frac{5\pi}6$ and $\sin\frac{5\pi}6=\frac12$ ✓.)

#### **Q22**
**Method: $\cos\theta=\cos\alpha\Rightarrow\theta=2n\pi\pm\alpha$ with $\alpha=\frac\pi3$.**
**Answer:** $x=2n\pi\pm\dfrac\pi3$.

#### **Q23**
**Method: $\tan\theta=\tan\alpha\Rightarrow\theta=n\pi+\alpha$ with $\alpha=\frac\pi4$.**
**Answer:** $x=n\pi+\dfrac\pi4$.

#### **Q24**
**Method: the unit circle meets the horizontal line $y=\frac12$ twice per revolution**, at $\frac\pi6$ and $\frac{5\pi}6$.
**Answer:** $2$.

#### **Q25**
**Method: bring to one side and factorise — do not divide by $\cos x$.**
$$\sin2x=\cos x\Rightarrow2\sin x\cos x-\cos x=0\Rightarrow\cos x(2\sin x-1)=0.$$
So $\cos x=0\Rightarrow x=\frac\pi2+n\pi$, or $\sin x=\frac12\Rightarrow x=n\pi+(-1)^n\frac\pi6$.
**Answer:** $x=\dfrac\pi2+n\pi$ or $x=n\pi+(-1)^n\dfrac\pi6$. In $[0,2\pi)$ these are $\frac\pi6,\frac\pi2,\frac{5\pi}6,\frac{3\pi}2$ — four solutions, all verified ✓.

---

## F · Properties of triangles

#### **Q26**
**Method: cosine rule for $c$, sine rule for $R$, $\frac12ab\sin C$ for the area.**
$$c=\sqrt{3^2+4^2-2\cdot3\cdot4\cos90^\circ}=5,$$
$$2R=\frac c{\sin C}=\frac51=5\Rightarrow R=2.5,\qquad \Delta=\frac12\cdot3\cdot4\cdot1=6.$$
**Answer:** $c=5$, $R=2.5$, area $6$. (Consistency: for a right triangle the hypotenuse is a diameter, so $R=\frac c2=2.5$ ✓.)

#### **Q27**
**Method: $\tan\frac A2=\frac r{s-a}$ with $r=\frac\Delta s$.** $s=\frac{3+4+5}{2}=6$ and $r=\frac66=1$, so
$$\tan\frac A2=\frac1{6-3}=\frac13.$$
**Answer:** $\dfrac13$. (Check directly: $A\approx36.87^\circ$, so $\tan18.43^\circ\approx0.3333$ ✓.)

#### **Q28**
**Method: cosine rule $a^2=b^2+c^2-2bc\cos A$.**
$$a^2=4^2+3^2-2\cdot4\cdot3\cdot\cos90^\circ=16+9-0=25,$$
so $a=5$.
**Answer:** $a^2=25$, $a=5$ ✓.

#### **Q29**
**Method: $\Delta=\frac12bc\sin A$.**
$$\Delta=\frac12\cdot5\cdot7\cdot\sin60^\circ=\frac{35}{2}\cdot\frac{\sqrt3}{2}=\frac{35\sqrt3}{4}.$$
**Answer:** $\dfrac{35\sqrt3}{4}\approx15.1554$.

#### **Q30**
**Method: scale the ratio, then use the right-triangle circumradius.** $3k+4k+5k=36\Rightarrow k=3$, so the sides are $9,12,15$. Since $9^2+12^2=225=15^2$ the triangle is right-angled with hypotenuse $15=2R$.
**Answer:** $R=7.5$.

---

## G · Olympiad frontier

#### **Q31**
**Method: use $2\theta+3\theta=90^\circ$ at $\theta=18^\circ$.** Then
$\sin2\theta=\cos3\theta$, so with $s=\sin\theta$ and $c=\cos\theta$:
$$2sc=4c^3-3c.$$
Dividing by the non-zero $c$ and using $c^2=1-s^2$:
$$2s=4(1-s^2)-3=1-4s^2,$$
so $4s^2+2s-1=0$, giving $s=\frac{-1+\sqrt5}{4}$ (the positive root). Then
$\cos36^\circ=1-2s^2=1-2\cdot\frac{3-\sqrt5}{8}=\frac{1+\sqrt5}{4}$.
**Answer:** both verified. (Check: $4s^2+2s-1=0$ exactly for $s=\frac{\sqrt5-1}{4}$ ✓,
$\frac{\sqrt5-1}{4}=0.30902=\sin18^\circ$ ✓ and
$\frac{1+\sqrt5}{4}=0.80902=\cos36^\circ$ ✓.)

#### **Q32**
**Method: sum-to-product, then use $C=\pi-(A+B)$.**
$\sin2A+\sin2B=2\sin(A+B)\cos(A-B)$ and
$\sin2C=\sin(2\pi-2(A+B))=-\sin2(A+B)$, so the left side is
$$2\sin(A+B)\big[\cos(A-B)-\cos(A+B)\big]=2\sin(A+B)\cdot2\sin A\sin B=4\sin A\sin B\sin C,$$
using $\sin(A+B)=\sin C$ and $\cos(A-B)-\cos(A+B)=2\sin A\sin B$.
**Answer:** proved. (Check for $(60^\circ,60^\circ,60^\circ)$: LHS
$=3\sin120^\circ=2.5981$ and RHS $=4(\frac{\sqrt3}{2})^3=2.5981$ ✓.)

#### **Q33**
**Method: replace $\sin^2$ by $1-\cos^2$ and use the cosine identity.**
$\sin^2A+\sin^2B+\sin^2C=3-(\cos^2A+\cos^2B+\cos^2C)$. From the companion
identity $\cos^2A+\cos^2B+\cos^2C=1-2\cos A\cos B\cos C$, this becomes
$3-1+2\cos A\cos B\cos C=2+2\cos A\cos B\cos C$ ✓.
**Answer:** proved. (Check for $(60^\circ,60^\circ,60^\circ)$: LHS $=3\cdot\frac34=2.25$
and RHS $=2+2\cdot\frac18=2.25$ ✓. For $(30^\circ,60^\circ,90^\circ)$: both give
$2$ ✓.)

#### **Q34**
**Method: $\tan3\theta$ is unchanged by $\theta\mapsto\theta+60^\circ$.**
With $t=\tan\theta$, $\tan3\theta=\frac{3t-t^3}{1-3t^2}$. At $\theta=20^\circ$,
$\tan3\theta=\tan60^\circ=\sqrt3$, so $t=\tan20^\circ$ satisfies
$$t^3-3\sqrt3\,t^2-3t+\sqrt3=0.$$
Adding $60^\circ$ and $120^\circ$ to $\theta$ leaves $\tan3\theta$ unchanged, so
the three roots are $\tan20^\circ$, $\tan80^\circ$ and $\tan140^\circ=-\tan40^\circ$.
Their product is the negative of the constant term, $-\sqrt3$, hence
$\tan20^\circ\tan80^\circ(-\tan40^\circ)=-\sqrt3$.
**Answer:** $\sqrt3$. (Check numerically:
$0.36397\times0.83910\times5.67128=1.7321=\sqrt3$ ✓, and the root sum
$0.36397+5.67128-0.83910=5.19615=3\sqrt3$ ✓.)

#### **Q35**
**Method: roots of unity, then take moduli.** Factoring
$z^n-1=(z-1)\prod_{k=1}^{n-1}(z-e^{2\pi ik/n})$, dividing by $z-1$ and setting
$z=1$ gives $n=\prod_{k=1}^{n-1}(1-e^{2\pi ik/n})$. Since
$\lvert1-e^{2\pi ik/n}\rvert=2\sin\frac{k\pi}{n}$ for $1\le k\le n-1$, taking
moduli yields $n=2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}$.
**Answer:** $\dfrac{n}{2^{n-1}}$; for $n=7$ it is $\dfrac7{64}$. (Check for $n=7$:
the product is $0.43388\times0.78183\times0.97493\times0.97493\times0.78183\times0.43388
=0.109375=\frac7{64}$ ✓. For $n=3$: $(\frac{\sqrt3}{2})^2=\frac34=\frac3{2^2}$ ✓.)

#### **Q36**
**Method: the sine-sum formula
$\sum_{k=1}^{n}\sin k\theta=\frac{\sin(n\theta/2)\sin((n+1)\theta/2)}{\sin(\theta/2)}$.**
With $n=90$ and $\theta=1^\circ$, $n\theta/2=45^\circ$ and
$(n+1)\theta/2=45.5^\circ$, so
$$\sum_{k=1}^{90}\sin k^\circ=\frac{\sin45^\circ\sin45.5^\circ}{\sin0.5^\circ}.$$
**Answer:** $\dfrac{\sin45^\circ\sin45.5^\circ}{\sin0.5^\circ}\approx57.7943$. (Check
numerically: $\frac{0.70711\times0.71325}{0.0087265}=57.7943$ ✓, and a direct sum
of the $90$ terms gives $57.7943$ ✓.)
