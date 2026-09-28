---
title: "Matrices & Determinants — Solutions"
aliases: ["Matrices and Determinants Solutions"]
module: "Matrices-and-Determinants"
module_title: "Matrices & Determinants"
type: solutions
tags: [matrices-and-determinants, solutions, olympiad, linear-algebra]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Matrices-and-Determinants — Paper|Paper]] · 📖 [[Matrices-and-Determinants|Complete Notes]]

# Matrices & Determinants — Solutions

> Full solutions to all 34 questions, same Q-ids as the
> [[Matrices-and-Determinants — Paper|paper]]. Every solution: **method first →
> derivation → a check.** Every numeric answer was verified in pure Python
> (stdlib only) before this file was written.

---

## A · Matrix operations

#### **Q1**
**Method: componentwise addition.** $\begin{pmatrix}1+5&2+6\\3+7&4+8\end{pmatrix}$.
**Answer:** $\begin{pmatrix}6&8\\10&12\end{pmatrix}$.

#### **Q2**
**Method: row times column.** $(1,1)$ entry: $1\cdot5+2\cdot7=19$; $(1,2)$: $1\cdot6+2\cdot8=22$; $(2,1)$: $3\cdot5+4\cdot7=43$; $(2,2)$: $3\cdot6+4\cdot8=50$.
**Answer:** $AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}$.

#### **Q3**
**Method: the same computation with the factors swapped.** $(1,1)$ entry: $5\cdot1+6\cdot3=23$; $(1,2)$: $5\cdot2+6\cdot4=34$; $(2,1)$: $7\cdot1+8\cdot3=31$; $(2,2)$: $7\cdot2+8\cdot4=46$.
**Answer:** $BA=\begin{pmatrix}23&34\\31&46\end{pmatrix}$, and $AB\ne BA$ — matrix multiplication is not commutative.

#### **Q4**
**Method: interchange rows and columns.**
**Answer:** $\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}$.

#### **Q5**
**Method: sum the diagonal entries.** $1+4$.
**Answer:** $\operatorname{tr}A=5$.

---

## B · Determinants

#### **Q6**
**Method: $ad-bc$.** $3\cdot2-1\cdot5$.
**Answer:** $1$.

#### **Q7**
**Method: cofactor expansion along the first row.** $1(50-48)-2(40-42)+3(32-35)=2+4-9$.
**Answer:** $-3$. (Check along the third column: $3(-3)+6(6)+10(-3)=-9+36-30=-3$ ✓.)

#### **Q8**
**Method: a diagonal matrix's determinant is the product of its diagonal entries.** $2\cdot3\cdot4$.
**Answer:** $24$.

#### **Q9**
**Method: Vandermonde with $x_1=2,x_2=5,x_3=9$; the determinant is $(x_2-x_1)(x_3-x_1)(x_3-x_2)$.** $3\cdot7\cdot4$.
**Answer:** $84$. (Direct expansion gives $84$ ✓.)

#### **Q10**
**Method: $C_{12}=(-1)^{1+2}M_{12}$ where $M_{12}=\det\begin{pmatrix}4&6\\7&10\end{pmatrix}=40-42=-2$.** $C_{12}=-1\cdot(-2)$.
**Answer:** $2$.

---

## C · Adjoint and inverse

#### **Q11**
**Method: for a $2\times2$ matrix, $\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.**
**Answer:** $\operatorname{adj}A=\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$.

#### **Q12**
**Method: $A^{-1}=\frac1{\det A}\operatorname{adj}A$ with $\det A=-2$.**
$$A^{-1}=-\frac12\begin{pmatrix}4&-2\\-3&1\end{pmatrix}=\begin{pmatrix}-2&1\\\frac32&-\frac12\end{pmatrix}.$$
**Answer:** $\begin{pmatrix}-2&1\\\frac32&-\frac12\end{pmatrix}$. (Check: $AA^{-1}=I$ ✓; $\det(A^{-1})=-\frac12=\frac1{\det A}$ ✓.)

#### **Q13**
**Method: cofactors, transpose, divide by the determinant.** $\det A=4$ and the cofactor matrix transposes to $\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix}$.
**Answer:** $A^{-1}=\frac14\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix}$. (Check: $A\cdot\operatorname{adj}A=4I$, so $A\cdot A^{-1}=I$ ✓.)

#### **Q14**
**Method: $\det\begin{pmatrix}2&1\\1&1\end{pmatrix}=1$ and $\operatorname{adj}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$.**
**Answer:** $A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$. (Check: $AA^{-1}=I$ ✓.)

#### **Q15**
**Method: $\det(A^{-1})=\frac1{\det A}$.** $\det A=-2$.
**Answer:** $-\dfrac12$. (Check: $\det\begin{pmatrix}-2&1\\3/2&-1/2\end{pmatrix}=1-\frac32=-\frac12$ ✓.)

---

## D · Systems of linear equations

#### **Q16**
**Method: Cramer's rule.** $\det A=-3$, $\det A_1=-6$, $\det A_2=-3$.
**Answer:** $x=\frac{-6}{-3}=2$, $y=\frac{-3}{-3}=1$. (Check: $2(2)+1=5$ and $2-1=1$ ✓.)

#### **Q17**
**Method: $X=A^{-1}B$.** $\det A=-5$, $A^{-1}=-\frac15\begin{pmatrix}-1&-2\\-1&3\end{pmatrix}$, so $X=\begin{pmatrix}2\\3\end{pmatrix}$.
**Answer:** $x=2$, $y=3$. (Check: $3(2)+2(3)=12$ and $2-3=-1$ ✓.)

#### **Q18**
**Method: compare the ranks.** $\det A=\det\begin{pmatrix}1&1\\2&2\end{pmatrix}=0$, while replacing a column by $B$ gives $\det\begin{pmatrix}2&1\\5&2\end{pmatrix}=-1\ne0$. So $\rho(A)=1\ne2=\rho[A\,|\,B]$.
**Answer:** inconsistent — no solution. (Geometrically the two lines are parallel and distinct ✓.)

#### **Q19**
**Method: a homogeneous system has a non-trivial solution iff $\det A=0$.** $\lambda^2-1=0$.
**Answer:** $\lambda=\pm1$.

#### **Q20**
**Method: compute both sides.** $\det A=-2$, $\det B=-2$, product $4$; and $\det(AB)=19\cdot50-22\cdot43=950-946=4$.
**Answer:** verified, both sides $=4$.

---

## E · Rank and elementary operations

#### **Q21**
**Method: row-reduce.** $R_3\leftarrow R_3-2R_2+R_1$ produces a zero third row; the first two rows are independent.
**Answer:** rank $2$. (Consistency: $\det=0$ rules out rank $3$, and the minor $\det\begin{pmatrix}1&2\\4&5\end{pmatrix}=-3\ne0$ confirms rank $\ge2$ ✓.)

#### **Q22**
**Method: the second row is twice the first.**
**Answer:** rank $1$.

#### **Q23**
**Method: row-reduce.** $R_2\leftarrow R_2-2R_1$ gives a zero row; the remaining two rows are independent.
**Answer:** rank $2$.

#### **Q24**
**Method: the identity has no zero rows in echelon form.**
**Answer:** rank $2$.

#### **Q25**
**Method: $\det(kA)=k^n\det A$ with $n=2$.** $\det A=-2$, so the prediction is $9\cdot(-2)=-18$. Directly, $3A=\begin{pmatrix}3&6\\9&12\end{pmatrix}$ and $\det(3A)=36-54=-18$.
**Answer:** verified, both sides $-18$.

---

## F · Special matrices

#### **Q26**
**Method: check $AA^{\mathsf T}=I$.** $\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.
**Answer:** verified orthogonal (a rotation through $90^\circ$, $\det=1$ ✓).

#### **Q27**
**Method: square it.** $\begin{pmatrix}1&1\\0&0\end{pmatrix}^2=\begin{pmatrix}1&1\\0&0\end{pmatrix}$.
**Answer:** verified idempotent.

#### **Q28**
**Method: square it.** $\begin{pmatrix}0&1\\1&0\end{pmatrix}^2=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.
**Answer:** verified involutory.

#### **Q29**
**Method: halve the sum and the difference with the transpose.** $A+A^{\mathsf T}=\begin{pmatrix}2&5\\5&8\end{pmatrix}$ and $A-A^{\mathsf T}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$.
**Answer:** $A=\begin{pmatrix}1&\frac52\\\frac52&4\end{pmatrix}+\begin{pmatrix}0&-\frac12\\\frac12&0\end{pmatrix}$, symmetric plus skew-symmetric ✓.

---

## G · Olympiad frontier

#### **Q30**
**Method: form the characteristic polynomial and substitute $A$.** $\operatorname{tr}A=5$, $\det A=-2$, so $p(\lambda)=\lambda^2-5\lambda-2$. With $A^2=\begin{pmatrix}7&10\\15&22\end{pmatrix}$:
$$A^2-5A-2I=\begin{pmatrix}7&10\\15&22\end{pmatrix}-\begin{pmatrix}5&10\\15&20\end{pmatrix}-\begin{pmatrix}2&0\\0&2\end{pmatrix}=0.$$
**Answer:** verified, $A^2-5A-2I=0$.

#### **Q31**
**Method: multiply the characteristic relation by $A$.** From $A^2=5A+2I$:
$$A^3=5A^2+2A=5(5A+2I)+2A=27A+10I.$$
**Answer:** $A^3=27A+10I$. (Check directly: $A^3=A^2A=\begin{pmatrix}37&54\\81&118\end{pmatrix}$ and $27A+10I=\begin{pmatrix}37&54\\81&118\end{pmatrix}$ ✓.)

#### **Q32**
**Method: split into two $2\times2$ blocks.** $\det\begin{pmatrix}2&0\\0&3\end{pmatrix}\det\begin{pmatrix}4&0\\0&5\end{pmatrix}=6\cdot20$.
**Answer:** $120$. (Directly $2\cdot3\cdot4\cdot5=120$ ✓.)

#### **Q33**
**Method: track the image of the unit square.** The columns of $A$ are the images of the basis vectors, so the unit square maps to the parallelogram they span, whose area is $\lvert a_{11}a_{22}-a_{12}a_{21}\rvert=\lvert\det A\rvert$. Linearity makes every area scale by the same factor.
**Answer:** $\lvert\det A\rvert$ — the area of the image of the unit square.

#### **Q34**
**Method: expand the determinant directly.**
$$\det\begin{pmatrix}1+k&2\\3&4+k\end{pmatrix}=(1+k)(4+k)-6=k^2+5k+4-6=k^2+5k-2.$$
**Answer:** $k^2+5k-2$. (Check at $k=3$: $9+15-2=22$, and directly $\det\begin{pmatrix}4&2\\3&7\end{pmatrix}=28-6=22$ ✓.)
