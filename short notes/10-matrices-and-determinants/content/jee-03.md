---
id: jee-03
part: jee
title: Adjoint & Inverse — The Reversible Case
---

## Cofactors assemble the adjoint

For square $A$, $C_{ij}=(-1)^{i+j}M_{ij}$ and $\operatorname{adj}A=(C_{ij})^T$: **transpose the cofactor matrix**. Cofactor expansion gives
$$A\operatorname{adj}A=\operatorname{adj}A A=(\det A)I.$$
Off-diagonal entries cancel in pairs; diagonal entries are cofactor expansions of $\det A$.

:::key title="Inverse criterion and formula"
$A^{-1}$ exists exactly when $\det A\ne0$. Then $A^{-1}=\dfrac{\operatorname{adj}A}{\det A}$. If determinant vanishes, no inverse: the adjoint formula is not a workaround.
:::

For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, $\operatorname{adj}A=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ and
$$A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix},\quad ad-bc\ne0.$$

:::example title="Compute and verify"
For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, determinant $-2$, adjoint $\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$, hence $A^{-1}=\begin{pmatrix}-2&1\\3/2&-1/2\end{pmatrix}$. Check by multiplication: $AA^{-1}=I$.
:::

## Useful inverse laws (only when defined)

$(AB)^{-1}=B^{-1}A^{-1}$, $(A^T)^{-1}=(A^{-1})^T$, $(A^{-1})^{-1}=A$. Also $\det(A^{-1})=1/\det A$. To solve $AX=B$, multiply **on the left**: $X=A^{-1}B$; preserve order.

:::warn title="Adjoint versus cofactor matrix"
The adjoint is the transpose of the cofactor matrix. A symmetric matrix can hide this distinction because its cofactor matrix may also be symmetric; verify the definition instead of relying on that coincidence.
:::

## A practical 3×3 calculation

For $A=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$, cofactors give $\det A=4$ and $\operatorname{adj}A=\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix}$. Therefore $A^{-1}=\frac{1}{4}\operatorname{adj}A$; the quick check is $A\operatorname{adj}A=4I$.
