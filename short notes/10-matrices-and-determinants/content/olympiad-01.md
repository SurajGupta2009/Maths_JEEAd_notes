---
id: olympiad-01
part: olympiad
title: Cayley–Hamilton — Reduce Every Power
---

## Characteristic polynomial

For square $A$, define $p(\lambda)=\det(\lambda I-A)$. Eigenvalues are roots because $(A-\lambda I)v=0$ has a nonzero vector exactly when determinant vanishes. For $2\times2$:
$$p(\lambda)=\lambda^2-(\operatorname{tr}A)\lambda+\det A.$$

:::key title="Cayley–Hamilton theorem"
Every square matrix satisfies its characteristic polynomial: $p(A)=0$. For order 2, $A^2-(\operatorname{tr}A)A+(\det A)I=0$. Therefore every higher power reduces to a linear combination of $I$ and $A$.
:::

:::example title="Power reduction"
For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, trace $5$, determinant $-2$, so $A^2-5A-2I=0$. Then $A^2=5A+2I$ and $A^3=27A+10I$.
:::

## Eigenvalue invariants and similarity

$B=P^{-1}AP$ is a change of basis (similarity), when $P$ invertible. Then $\det(\lambda I-B)=\det(\lambda I-A)$; hence trace and determinant, and the eigenvalue multiset, are unchanged. Distinct eigenvalues imply diagonalizability over a field containing all eigenvalues (for real matrices, at least over $\mathbb{C}$); repeated eigenvalues alone do not.

:::warn title="Avoid an invalid substitution"
Cayley–Hamilton lets us reduce powers of one fixed square matrix. It does not permit replacing a scalar variable by a matrix in an unrelated identity unless products commute and the polynomial identity applies.
:::
