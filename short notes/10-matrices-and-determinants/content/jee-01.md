---
id: jee-01
part: jee
title: Matrix Language — Shapes, Operations, Transpose
---

## A matrix is a linear machine

An $m\times n$ matrix $A=(a_{ij})$ has $m$ rows and $n$ columns; its entry $a_{ij}$ is in row $i$, column $j$. Multiplication by a column vector combines rows with coordinates:
$$A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\quad x=\begin{pmatrix}u\\v\end{pmatrix},\quad Ax=\begin{pmatrix}u+2v\\3u+4v\end{pmatrix}.$$

:::intuition title="Rows act; columns record"
The row $i$ of $A$ computes the $i$th output as a dot product. The columns are the outputs of the coordinate basis vectors: $Ae_j$ is column $j$.
:::

## Shape check before multiplying

$A_{m\times n}B_{n\times p}$ exists and has shape $m\times p$; its entry $(i,j)$ is $\sum_{k=1}^{n}a_{ik}b_{kj}$. Inner dimensions must agree. Addition needs identical shapes. Matrix multiplication is associative and distributive, generally **not commutative**.

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}5&6\\7&8\end{pmatrix}=\begin{pmatrix}19&22\\43&50\end{pmatrix}\ne\begin{pmatrix}23&34\\31&46\end{pmatrix}.$$

:::warn title="Order and zero traps"
$AB$ defined does not imply $BA$ is defined. $AB=0$ does not force $A=0$ or $B=0$; singular matrices can annihilate nonzero vectors. Never cancel a matrix factor unless invertibility is established.
:::

## Identity, powers and transpose

$I_nA=A=AI_m$ when dimensions fit. $A^0=I$ for square $A$; powers require a square matrix. $(AB)^T=B^TA^T$ (reverse order), $(A+B)^T=A^T+B^T$.

:::example title="Quick transpose check"
If $A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}$, then $A^T=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}$, now $3\times2$. Transposing swaps row/column labels, not the entries' signs.
:::

## Named structures

Square: $n\times n$. Diagonal: off-diagonal entries zero. Scalar: $\lambda I$. Symmetric: $A^T=A$; skew-symmetric: $A^T=-A$, hence diagonal entries are zero over real numbers. For any real square $A$:
$$A=\frac{A+A^T}{2}+\frac{A-A^T}{2}$$
is the unique symmetric + skew-symmetric decomposition.

:::key title="Transpose identities"
$(A^T)^T=A$; $(AB)^T=B^TA^T$; $(A^{-1})^T=(A^T)^{-1}$ when inverse exists. The last follows by transposing $AA^{-1}=I$.
:::
