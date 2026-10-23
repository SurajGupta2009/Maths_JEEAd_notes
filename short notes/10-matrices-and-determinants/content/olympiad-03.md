---
id: olympiad-03
part: olympiad
title: Trace, Rank–Nullity, Block Structure
---

## Trace: cyclic, not commutative

For square matrices $A,B$ of the same order, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ since both equal $\sum_{i,j}a_{ij}b_{ji}$. This does **not** say $AB=BA$. More generally $\operatorname{tr}(ABC)=\operatorname{tr}(BCA)$ when dimensions permit cyclic products.

## Rank–nullity

For linear map $A:\mathbb{R}^n\to\mathbb{R}^m$, $\operatorname{rank}A+\operatorname{nullity}A=n$. Row reduction exposes pivot variables and free variables; the null space is the solution space of $Ax=0$.

:::example title="Dimension count"
If a $3\times4$ matrix has rank 2, then nullity is $4-2=2$: the homogeneous system has a two-dimensional family of solutions.
:::

## Block determinants

For square diagonal blocks $A,D$:
$$\det\begin{pmatrix}A&B\\0&D\end{pmatrix}=\det A\det D.$$
If $A$ is invertible (and block sizes compatible), Schur complement gives
$$\det\begin{pmatrix}A&B\\C&D\end{pmatrix}=\det A\det(D-CA^{-1}B).$$

:::intuition title="Eliminate the lower-left block"
Multiply on the left by the block triangular matrix $\begin{pmatrix}I&0\\-CA^{-1}&I\end{pmatrix}$, whose determinant is 1. The product has lower-left block zero and lower-right block $D-CA^{-1}B$.
:::

:::example title="Schur complement in one calculation"
Let $A=I_2$, $B=(1,2)^T$, $C=(3,4)$, $D=(10)$. Then the Schur complement is $10-(3,4)(1,2)^T=10-11=-1$, so the block determinant is $-1$. Directly, $\det\begin{pmatrix}1&0&1\\0&1&2\\3&4&10\end{pmatrix}=-1$.
:::

## Boundary reminder

Eigenvalues, Cayley–Hamilton, rank–nullity, Hadamard, Vandermonde and Schur complements are useful Olympiad extensions; they are not being represented as explicit JEE syllabus requirements. Matrix algebra can still arise inside a JEE question when supplied or derivable.
