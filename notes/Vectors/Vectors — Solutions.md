---
title: "Vectors — Solutions"
aliases: ["Vectors Solutions", "Vector Algebra Solutions"]
module: "Vectors"
module_title: "Vectors"
type: solutions
tags: [vectors, solutions, olympiad, geometry, linear-algebra]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Vectors — Paper|Paper]] · 📖 [[Vectors|Complete Notes]]

# Vectors — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[Vectors — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Vector algebra

#### **Q1**
**Method: Pythagoras in 3D, then normalise.** $\lvert\mathbf a\rvert=\sqrt{1+4+9}=\sqrt{14}$; $\hat{\mathbf a}=\mathbf a/\sqrt{14}$.
**Answer:** $\sqrt{14}\approx3.7417$; $\hat{\mathbf a}=\big(\tfrac1{\sqrt{14}},\tfrac2{\sqrt{14}},\tfrac3{\sqrt{14}}\big)$. (Check: $1/14+4/14+9/14=1$ ✓.)

#### **Q2**
**Method: componentwise dot product.** $1\cdot4+2\cdot5+3\cdot6=4+10+18=32$.
**Answer:** $32$.

#### **Q3**
**Method: the $3\times3$ determinant.** $(2\cdot6-3\cdot5,\;3\cdot4-1\cdot6,\;1\cdot5-2\cdot4)=(-3,6,-3)$; length $\sqrt{9+36+9}=\sqrt{54}=3\sqrt6$.
**Answer:** $(-3,6,-3)$; $3\sqrt6\approx7.3485$. (Check: $(-3,6,-3)\cdot(1,2,3)=0$ and $(-3,6,-3)\cdot(4,5,6)=0$ ✓.)

#### **Q4**
**Method: $\cos\theta=\frac{\mathbf a\cdot\mathbf b}{\lvert\mathbf a\rvert\lvert\mathbf b\rvert}$.** $\frac{32}{\sqrt{14}\sqrt{77}}=\frac{32}{\sqrt{1078}}$.
**Answer:** $\theta\approx12.93^\circ$.

#### **Q5**
**Method: section formula $\frac{n\mathbf a+m\mathbf b}{m+n}$.** $\frac{3(1,0,0)+2(4,5,6)}{5}=\frac{(11,10,12)}{5}$.
**Answer:** $\left(\dfrac{11}{5},2,\dfrac{12}{5}\right)$.

---

## B · The two products

#### **Q6**
**Method: dot product zero ⟺ perpendicular.** $1\cdot2+2(-2)+2\cdot1=2-4+2=0$.
**Answer:** perpendicular.

#### **Q7**
**Method: Lagrange's identity, evaluated both sides.** LHS $=\lvert(-3,6,-3)\rvert^2+32^2=54+1024=1078$; RHS $=14\cdot77=1078$.
**Answer:** verified, both sides $1078$.

#### **Q8**
**Method: scalar triple product.** $(4,5,6)\times(-1,0,2)=(5\cdot2-6\cdot0,\;6(-1)-4\cdot2,\;4\cdot0-5(-1))=(10,-14,5)$. Then $(1,2,3)\cdot(10,-14,5)=10-28+15=-3$.
**Answer:** $-3$.

#### **Q9**
**Method: $\lvert\mathbf a\times\mathbf a\rvert=\lvert\mathbf a\rvert^2\sin0=0$.** Equivalently, the determinant has two identical rows.
**Answer:** $\mathbf 0$ — a vector cannot be perpendicular to itself (unless zero).

#### **Q10**
**Method: $\mathbf a\times\mathbf b$ is perpendicular to both factors by definition.** So its dot product with $\mathbf a$ vanishes.
**Answer:** $0$.

---

## C · Geometry of points

#### **Q11**
**Method: $\lvert\mathbf b-\mathbf a\rvert$.** $(4,6,9)-(1,2,3)=(3,4,6)$; $\sqrt{9+16+36}=\sqrt{61}$.
**Answer:** $\sqrt{61}\approx7.8102$.

#### **Q12**
**Method: half the cross product.** $(3,0,0)\times(0,4,0)=(0,0,12)$; $\frac12\cdot12=6$.
**Answer:** $6$.

#### **Q13**
**Method: average the position vectors.** $\frac{(1,0,0)+(4,5,6)+(7,8,9)}{3}=\frac{(12,13,15)}{3}$.
**Answer:** $\left(4,\dfrac{13}{3},5\right)$.

#### **Q14**
**Method: scalar triple product.** $\big[(1,0,0)\,(0,2,0)\,(0,0,3)\big]=\det\operatorname{diag}(1,2,3)=6$.
**Answer:** $6$.

#### **Q15**
**Method: the tetrahedron is $\frac16$ of the parallelepiped.**
**Answer:** $1$.

---

## D · Straight lines

#### **Q16**
**Method: $\mathbf r=\mathbf a+t\mathbf b$.** At $t=2$: $(1,2,3)+2(2,-1,4)=(1,2,3)+(4,-2,8)=(5,0,11)$.
**Answer:** $\dfrac{x-1}{2}=\dfrac{y-2}{-1}=\dfrac{z-3}{4}$; point $(5,0,11)$.

#### **Q17**
**Method: angle between directions.** $\frac{(1,2,2)\cdot(2,1,-1)}{3\cdot\sqrt6}=\frac{2}{3\sqrt6}$.
**Answer:** $\theta\approx74.21^\circ$.

#### **Q18**
**Method: $\lvert(\mathbf p-\mathbf a)\times\mathbf b\rvert/\lvert\mathbf b\rvert$ with $\mathbf a=\mathbf 0$, $\mathbf b=(2,-1,2)$.** $(1,2,3)\times(2,-1,2)=(7,4,-5)$; $\sqrt{90}/3=\sqrt{10}$.
**Answer:** $\sqrt{10}\approx3.1623$.

#### **Q19**
**Method: the skew-line formula.** $\mathbf b=(1,2,2)$, $\mathbf d=(2,-1,2)$, $\mathbf c-\mathbf a=(1,0,0)$; $\mathbf b\times\mathbf d=(6,2,-5)$, so numerator $\lvert(1,0,0)\cdot(6,2,-5)\rvert=6$ and denominator $\sqrt{36+4+25}=\sqrt{65}$.
**Answer:** $\dfrac{6}{\sqrt{65}}\approx0.7442$.

#### **Q20**
**Method: parallel lines — the distance is the point–line distance from any point on one line to the other.** Take $\mathbf a=(0,0,0)$ on the first line and $\mathbf p=(4,5,6)$ on the second:
$$\mathbf p-\mathbf a=(4,5,6),\qquad (\mathbf p-\mathbf a)\times\mathbf d=(4,5,6)\times(2,-1,2)=(16,4,-14).$$
So
$$d=\frac{\lvert(16,4,-14)\rvert}{3}=\frac{\sqrt{256+16+196}}{3}=\frac{\sqrt{468}}{3}=\frac{6\sqrt{13}}{3}=2\sqrt{13}.$$
**Answer:** $2\sqrt{13}\approx7.2111$. (Check by projection: $\lvert\mathbf p-\mathbf a\rvert\sin\theta=\sqrt{77}\cdot0.82178=7.2111$ ✓.)

#### **Q21**
**Method: divide the direction ratios by their magnitude.** $\lvert(2,-1,2)\rvert=3$.
**Answer:** $\left(\dfrac23,-\dfrac13,\dfrac23\right)$. (Check: $\frac49+\frac19+\frac49=1$ ✓.)

---

## E · The plane

#### **Q22**
**Method: $\mathbf r\cdot\mathbf n=\mathbf a\cdot\mathbf n$.** $(2,-3,4)\cdot(1,2,3)=2-6+12=8$.
**Answer:** $2x-3y+4z=8$.

#### **Q23**
**Method: point–plane distance.** $\frac{\lvert2-3+4-5\rvert}{\sqrt{4+9+16}}=\frac{2}{\sqrt{29}}$.
**Answer:** $\dfrac{2}{\sqrt{29}}\approx0.3714$.

#### **Q24**
**Method: angle between the normals.** $\frac{(1,2,2)\cdot(2,1,-1)}{3\sqrt6}=\frac{2}{3\sqrt6}$.
**Answer:** $\approx74.21^\circ$.

#### **Q25**
**Method: $\sin\theta=\frac{\lvert\mathbf b\cdot\mathbf n\rvert}{\lvert\mathbf b\rvert\lvert\mathbf n\rvert}$.** $\frac{\lvert3-2+4\rvert}{\sqrt{14}\cdot3}=\frac5{3\sqrt{14}}$.
**Answer:** $\theta\approx26.4^\circ$.

#### **Q26**
**Method: a line is parallel to a plane iff its direction is perpendicular to the plane's normal.** $(2,-1,2)\cdot(1,2,2)=2-2+4=4\ne0$.
**Answer:** not parallel.

#### **Q27**
**Method: the intercept form $\frac xa+\frac yb+\frac zc=1$ has normal $(\frac1a,\frac1b,\frac1c)$.** With $(a,b,c)=(2,3,6)$: $(\frac12,\frac13,\frac16)$, proportional to $(3,2,1)$.
**Answer:** $(3,2,1)$.

---

## F · Scalar triple & volumes

#### **Q28**
**Method: form the three edge vectors from $(1,2,3)$ and take the triple product.** Edges $(3,3,3)$, $(-2,-2,-1)$, $(1,-3,1)$; the triple product is non-zero.
**Answer:** not coplanar.

#### **Q29**
**Method: the triple product of three proportional vectors is zero.** All three are multiples of $(1,1,1)$.
**Answer:** coplanar.

#### **Q30**
**Method: $\frac16$ of the triple product of the edge vectors from one vertex.** Taking $\mathbf a=(1,1,1)$, the edges are $(0,-1,-1)$, $(-1,1,-1)$, $(-1,-1,2)$, and
$$\begin{vmatrix}0&-1&-1\\-1&1&-1\\-1&-1&2\end{vmatrix}=0(2-1)+1(-2-1)-1(1+1)=-5,$$
so the volume is $\frac{|-5|}{6}=\frac56$.
**Answer:** $\dfrac56\approx0.8333$. (Check: recomputing from each of the four vertices gives $\pm5$ every time ✓.)

---

## G · Applications

#### **Q31**
**Method: work $=\mathbf F\cdot\mathbf s$.** $(3,4,5)\cdot(1,0,2)=3+0+10=13$.
**Answer:** $13$.

#### **Q32**
**Method: torque magnitude $=\lvert\mathbf r\times\mathbf F\rvert$.** $(1,0,0)\times(0,3,4)=(0\cdot4-0\cdot3,\;0\cdot0-1\cdot4,\;1\cdot3-0\cdot0)=(0,-4,3)$; length $5$.
**Answer:** $5$.

---

## H · Olympiad frontier

#### **Q33**
**Method: compute each term and add.** With $\mathbf a=(7,8,9)$, $\mathbf b=(1,2,3)$, $\mathbf c=(4,5,6)$: the three cross products sum to $(0,0,0)$ exactly.
**Answer:** verified, the sum is $\mathbf 0$.

#### **Q34**
**Method: place $A$ at the origin, with $\mathbf b,\mathbf c$ the position vectors of $B,C$.** The midpoint of $BC$ is $\frac{\mathbf b+\mathbf c}{2}$, so the median from $A$ is the set $\left\{t\cdot\frac{\mathbf b+\mathbf c}{2}\right\}$. The point $\frac{\mathbf b+\mathbf c}{3}$ lies on it at $t=\frac23$, i.e. it divides the median from $A$ in the ratio $2:1$. By the symmetry of the expression $\frac{\mathbf b+\mathbf c}{3}$ (which is also $\frac{\mathbf c+\mathbf a}{3}$ and $\frac{\mathbf a+\mathbf b}{3}$ under relabelling), the same point lies on all three medians.
**Answer:** concurrent at $\frac{\mathbf b+\mathbf c}{3}$, dividing each median $2:1$.
