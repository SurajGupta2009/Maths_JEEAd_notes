---
id: jee-05
part: jee
title: Special Matrices — Symmetry, Orthogonality, Structure
---

## Symmetric and skew-symmetric

Real square $A$ is symmetric when $A^T=A$; skew-symmetric when $A^T=-A$. In the latter, $a_{ii}=-a_{ii}$, so every diagonal entry is zero. Every real square matrix splits uniquely:
$$A=S+K,\quad S=\frac{A+A^T}{2},\quad K=\frac{A-A^T}{2}.$$

:::example title="Split a 2×2 matrix"
For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $S=\begin{pmatrix}1&5/2\\5/2&4\end{pmatrix}$ and $K=\begin{pmatrix}0&-1/2\\1/2&0\end{pmatrix}$. Check $S^T=S$, $K^T=-K$, and $S+K=A$.
:::

## Orthogonal matrices preserve length

Real square $Q$ is orthogonal if $Q^TQ=QQ^T=I$. Thus $Q^{-1}=Q^T$ and columns (also rows) are orthonormal. For every vector $x$, $\|Qx\|^2=x^TQ^TQx=\|x\|^2$: rotations/reflections preserve lengths and angles. Taking determinants: $(\det Q)^2=1$, so $\det Q=\pm1$.

$$Q=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$$
is a rotation; check orthogonality using $\cos^2\theta+\sin^2\theta=1$.

:::warn title="Transpose is not inverse in general"
$A^T=A^{-1}$ only for orthogonal $A$. Symmetry $A^T=A$ alone does not imply orthogonality or invertibility.
:::

## Three algebraic families

Idempotent: $P^2=P$ (projection; eigenvalue intuition only in extension). Involutory: $R^2=I$, hence $R^{-1}=R$. Nilpotent: $N^k=0$ for some positive integer $k$; nilpotent matrices are singular when positive-dimensional.

:::example title="A projection"
$P=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ has $P^2=P$. Acting on $(x,y)^T$, it maps to $(x+y,0)^T$; applying it again changes nothing.
:::

:::key title="Test the definition"
To classify a given matrix, compute the defining product: $A^T$, $A^2$, or $AA^T$. A visual pattern is not a proof.
:::
