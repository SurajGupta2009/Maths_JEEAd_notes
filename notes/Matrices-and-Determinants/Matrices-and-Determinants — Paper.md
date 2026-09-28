---
title: "Matrices & Determinants — Olympiad Paper"
aliases: ["Matrices and Determinants Paper"]
module: "Matrices-and-Determinants"
module_title: "Matrices & Determinants"
type: paper
tags: [matrices-and-determinants, paper, olympiad, linear-algebra]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Matrices-and-Determinants|Chapter 6]] · 📖 [[Matrices-and-Determinants|Complete Notes]] · ✅ [[Matrices-and-Determinants — Solutions|Solutions]] ➡

# Matrices & Determinants — Olympiad Paper

> **34 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Matrices-and-Determinants — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · Matrix operations (Q1–Q5)

#### **Q1**[JEE Main][operations]Compute $A+B$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$.

**Answer:** $\begin{pmatrix}6&8\\10&12\end{pmatrix}$

#### **Q2**[JEE Main][multiply]Compute $AB$ for the same $A$ and $B$.

**Answer:** $\begin{pmatrix}19&22\\43&50\end{pmatrix}$

#### **Q3**[JEE Main][multiply]Compute $BA$ for the same $A$ and $B$, and comment.

**Answer:** $\begin{pmatrix}23&34\\31&46\end{pmatrix}$ — different from $AB$

#### **Q4**[JEE Main][transpose]Find the transpose of $\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}$.

**Answer:** $\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}$

#### **Q5**[JEE Main][trace]Find $\operatorname{tr}A$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $5$

---

## B · Determinants (Q6–Q10)

#### **Q6**[JEE Main][det2]Evaluate $\det\begin{pmatrix}3&1\\5&2\end{pmatrix}$.

**Answer:** $1$

#### **Q7**[JEE Main][det3]Evaluate $\det\begin{pmatrix}1&2&3\\4&5&6\\7&8&10\end{pmatrix}$.

**Answer:** $-3$

#### **Q8**[JEE Main][det3]Evaluate $\det\begin{pmatrix}2&0&0\\0&3&0\\0&0&4\end{pmatrix}$.

**Answer:** $24$

#### **Q9**[Olympiad][vandermonde]Evaluate $\det\begin{pmatrix}1&1&1\\2&5&9\\4&25&81\end{pmatrix}$.

**Answer:** $84$

#### **Q10**[JEE Main][cofactor]Find the cofactor of the element in position $(1,2)$ of $\begin{pmatrix}1&2&3\\4&5&6\\7&8&10\end{pmatrix}$.

**Answer:** $2$

---

## C · Adjoint and inverse (Q11–Q15)

#### **Q11**[JEE Main][adjoint]Find $\operatorname{adj}A$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$

#### **Q12**[JEE Main][inverse]Find $A^{-1}$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $\begin{pmatrix}-2&1\\\frac32&-\frac12\end{pmatrix}$

#### **Q13**[JEE Adv][inverse]Find $A^{-1}$ for $A=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$.

**Answer:** $\frac14\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix}$

#### **Q14**[JEE Main][inverse]Find $A^{-1}$ for $A=\begin{pmatrix}2&1\\1&1\end{pmatrix}$.

**Answer:** $\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$

#### **Q15**[JEE Main][det properties]Find $\det(A^{-1})$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $-\dfrac12$

---

## D · Systems of linear equations (Q16–Q20)

#### **Q16**[JEE Main][cramer]Solve $2x+y=5$, $x-y=1$ by Cramer's rule.

**Answer:** $x=2$, $y=1$

#### **Q17**[JEE Main][matrix method]Solve $3x+2y=12$, $x-y=-1$ by the matrix method.

**Answer:** $x=2$, $y=3$

#### **Q18**[JEE Main][consistency]Test the consistency of $x+y=2$, $2x+2y=5$.

**Answer:** inconsistent ($\rho(A)=1$, $\rho[A|B]=2$)

#### **Q19**[JEE Main][homogeneous]For what $\lambda$ does $\begin{pmatrix}\lambda&1\\1&\lambda\end{pmatrix}X=0$ have a non-trivial solution?

**Answer:** $\lambda=\pm1$

#### **Q20**[JEE Adv][det properties]Verify $\det(AB)=\det A\det B$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$.

**Answer:** both sides $=4$

---

## E · Rank and elementary operations (Q21–Q25)

#### **Q21**[JEE Main][rank]Find the rank of $\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}$.

**Answer:** $2$

#### **Q22**[JEE Main][rank]Find the rank of $\begin{pmatrix}1&2\\2&4\end{pmatrix}$.

**Answer:** $1$

#### **Q23**[JEE Adv][rank]Find the rank of $\begin{pmatrix}1&2&3&4\\2&4&6&8\\1&0&1&0\end{pmatrix}$.

**Answer:** $2$

#### **Q24**[JEE Main][rank]Find the rank of the $2\times2$ identity matrix.

**Answer:** $2$

#### **Q25**[JEE Main][det properties]Verify $\det(kA)=k^n\det A$ for $k=3$, $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $\det(3A)=-18=9\cdot(-2)$

---

## F · Special matrices (Q26–Q29)

#### **Q26**[JEE Main][orthogonal]Verify that $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ is orthogonal.

**Answer:** verified, $AA^{\mathsf T}=I$

#### **Q27**[JEE Main][idempotent]Verify that $\begin{pmatrix}1&1\\0&0\end{pmatrix}$ is idempotent.

**Answer:** verified, $A^2=A$

#### **Q28**[JEE Main][involutory]Verify that $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is involutory.

**Answer:** verified, $A^2=I$

#### **Q29**[JEE Main][decomposition]Decompose $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ into symmetric plus skew-symmetric parts.

**Answer:** $\begin{pmatrix}1&\frac52\\\frac52&4\end{pmatrix}+\begin{pmatrix}0&-\frac12\\\frac12&0\end{pmatrix}$

---

## G · Olympiad frontier (Q30–Q36)

#### **Q30**[Olympiad][eigenvalues]Find the eigenvalues of $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, and verify that their sum and product are the trace and the determinant.

**Answer:** $\dfrac{5\pm\sqrt{33}}2\approx5.3723,\,-0.3723$; sum $5=\operatorname{tr}A$, product $-2=\det A$

#### **Q31**[Olympiad][cayley hamilton]Verify Cayley–Hamilton for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $A^2-5A-2I=0$

#### **Q32**[Olympiad][power]Use Cayley–Hamilton to express $A^3$ as $\alpha A+\beta I$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

**Answer:** $A^3=27A+10I$

#### **Q33**[Olympiad][hadamard]Verify Hadamard's inequality $\lvert\det A\rvert\le\prod_j\lVert A_{\cdot j}\rVert$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and $B=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$.

**Answer:** $A$: $2\le\sqrt{200}\approx14.1421$; $B$: $4\le\sqrt{150}\approx12.2474$

#### **Q34**[Olympiad][det lemma]Verify the matrix determinant lemma $\det(A+uv^{\rm T})=\det(A)(1+v^{\rm T}A^{-1}u)$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $u=\binom12$, $v=\binom34$.

**Answer:** both sides equal $-6$

#### **Q35**[Olympiad][trace]Verify that $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and $B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$, and note whether $AB=BA$.

**Answer:** both traces are $69$, but $AB\ne BA$

#### **Q36**[Olympiad][vandermonde]Evaluate the Vandermonde determinant $\det\begin{pmatrix}1&1&1\\2&5&9\\4&25&81\end{pmatrix}$ and verify it against $\prod_{i<j}(x_j-x_i)$.

**Answer:** $84$

---

> [!note] Exam technique notes
> - **Compute $\operatorname{tr}$ and $\det$ first.** They are the two invariants
>   that generate the whole characteristic polynomial, and they are the cheapest
>   things to compute.
> - **Cayley–Hamilton turns powers into linear combinations.** To get $A^n$,
>   reduce modulo $p(A)$ rather than multiplying $n$ times.
> - **For a determinant bound, think geometry.** Hadamard is the statement that a
>   parallelepiped's volume is at most the product of its edge lengths.
> - **A rank-one update changes $\det$ by a scalar factor** — the matrix
>   determinant lemma. Recognising $uv^{\rm T}$ structure saves a full
>   recomputation.
> - **Check invariance claims by change of basis:** similar matrices share
>   characteristic polynomial, trace and determinant, but not the matrix itself.
