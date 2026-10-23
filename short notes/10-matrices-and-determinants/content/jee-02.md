---
id: jee-02
part: jee
title: Determinants — Cofactors & Rules
---

## The determinant measures signed area / volume

For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, $\det A=ad-bc$. The columns span a parallelogram; $|\det A|$ is its area scale, while the sign records orientation. In dimension $n$, determinant is the signed volume scale.

For a $3\times3$ matrix expand along a row/column: delete row $i$, column $j$ to get minor $M_{ij}$; cofactor $C_{ij}=(-1)^{i+j}M_{ij}$. Then $\det A=\sum_j a_{ij}C_{ij}$. The checkerboard signs begin $+,-,+$.

$$\det\begin{pmatrix}1&2&3\\4&5&6\\7&8&10\end{pmatrix}=1(50-48)-2(40-42)$$

$$+3(32-35)=-3.$$

:::derive title="Why the cofactor signs alternate"
In the permutation formula, exchanging two columns reverses orientation. Deleting row $i$ and column $j$ leaves the same smaller determinant; the parity of the row/column moves contributes $(-1)^{i+j}$.
:::

## Row operations: distinguish the three

1. Swap two rows: determinant changes sign.
2. Multiply a row by $c$: determinant multiplies by $c$.
3. Add $c$ times one row to another: determinant unchanged.

Same rules hold for columns. Thus if rows are equal/proportional, determinant is zero; a common row factor can be pulled out. Triangular determinant is product of diagonal entries.

:::warn title="Scaling the whole matrix"
For an $n\times n$ matrix, $\det(cA)=c^n\det A$ because each of the $n$ rows scales. It is not merely $c\det A$ unless $n=1$.
:::

## Structural identities

$$\det(A^T)=\det A,\qquad \det(AB)=\det A\det B$$

$$\det(A^{-1})=\frac{1}{\det A}.$$
The inverse identity assumes $\det A\ne0$. $A$ is singular iff $\det A=0$; geometrically its columns collapse into a lower-dimensional space.

:::example title="Parameter test"
$A=\begin{pmatrix}k&1\\2&k\end{pmatrix}$ is invertible iff $k^2-2\ne0$, i.e. $k\ne\pm\sqrt{2}$. At either excluded value the columns are dependent and the homogeneous system has a nonzero solution.
:::

:::key title="Fast evaluation"
Before expanding, look for a sparse row/column; repeated/proportional rows; row additions that create zeros; triangular form. Keep track of swaps and row scalings explicitly.
:::
