---
id: olympiad-02
part: olympiad
title: Determinant Geometry — Bounds and Updates
---

## Hadamard's volume bound

For columns $c_1,\ldots,c_n$ of $A$, $|\det A|\leq\prod_j\|c_j\|$. Volume cannot exceed the rectangular box with those edge lengths; equality holds exactly when nonzero columns are pairwise orthogonal (zero-column case gives both sides zero).

:::derive title="Two-dimensional identity"
For columns $(a,c)^T,(b,d)^T$, $(ad-bc)^2=(a^2+c^2)(b^2+d^2)-(ab+cd)^2$. Thus $|ad-bc|$ is at most the product of their lengths; equality iff dot product is zero.
:::

## Rank-one determinant lemma

For invertible $A$ and compatible column vectors $u,v$:
$$\det(A+uv^T)=\det A\left(1+v^TA^{-1}u\right).$$
A high-dimensional determinant update reduces to one scalar. Equivalent core identity: $\det(I+XY)=\det(I+YX)$ for compatible rectangular $X,Y$.

:::example title="Check one update"
$A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $u=(1,2)^T$, $v=(3,4)^T$. Directly $\det(A+uv^T)=-6$; the lemma gives $(-2)(1+2)=-6$.
:::

## Vandermonde determinant

$$\det\begin{pmatrix}1&x_1&x_1^2\\1&x_2&x_2^2\\1&x_3&x_3^2\end{pmatrix}=(x_2-x_1)(x_3-x_1)(x_3-x_2).$$
It vanishes iff two nodes coincide, exactly when quadratic interpolation loses uniqueness. General form: $\prod_{i<j}(x_j-x_i)$.

:::warn title="State the needed hypotheses"
The matrix determinant lemma uses $A^{-1}$, so $A$ must be invertible. The Vandermonde product depends on the stated column order $1,x,x^2$ and row order $x_1,x_2,x_3$; reordering nodes changes sign accordingly.
:::
