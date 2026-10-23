---
id: jee-04
part: jee
title: Linear Systems — Cramer & Consistency
---

## Encode equations as $AX=B$

For $n$ linear equations in $n$ unknowns, coefficient matrix $A$, unknown vector $X$, constants $B$. If $\det A\ne0$, there is exactly one solution, $X=A^{-1}B$.

### Cramer's rule

Replace column $i$ of $A$ by $B$ to form $A_i$. Then $x_i=\det A_i/\det A$. This requires square $A$ and nonzero determinant.

:::example title="Two equations"
$2x+y=5$, $x-y=1$. Here $A=\begin{pmatrix}2&1\\1&-1\end{pmatrix}$ and $\det A=-3$. Replacing columns gives determinants $-6,-3$, hence $(x,y)=(2,1)$. Substitute back to check both equations.
:::

:::example title="Three unknowns"
For $x+y+z=6$, $2x-y+z=3$, $x+2y-z=2$, coefficient determinant is $7$. Replacing columns by $(6,3,2)^T$ gives determinants $7,14,21$, so $(x,y,z)=(1,2,3)$. Direct substitution checks all three equations.
:::

:::warn title="Cramer's rule does not settle singular cases"
If $\det A=0$, do not divide. The system may have no solution or infinitely many; compare the equations/ranks or row-reduce the augmented matrix.
:::

## Homogeneous systems

$AX=0$ always has $X=0$. A nonzero solution exists iff $A$ is singular (for square $A$), since $AX=0$ has a nontrivial null vector exactly when columns are dependent.

:::example title="Parameter condition"
$\begin{pmatrix}\lambda&1\\1&\lambda\end{pmatrix}X=0$ has nonzero solutions iff $\lambda^2-1=0$, so $\lambda=\pm1$. For other real $\lambda$, only $X=0$.
:::

## General consistency and rank

For $m$ equations, $n$ unknowns, compare coefficient rank $r(A)$ and augmented rank $r([A|B])$:

- unequal ranks: no solution;
- equal rank $r=n$: unique solution;
- equal rank $r<n$: infinitely many solutions (over $\mathbb{R}$).

The last case has $n-r$ free parameters. Rank is the number of pivots after row reduction, equivalently the largest order of a nonzero minor.

:::derive title="Why ranks decide consistency"
Row operations preserve the equation solution set. An echelon system has one pivot equation per pivot; a row $[0\;\cdots\;0\mid c]$, $c\ne0$, is a contradiction. Without contradiction, each non-pivot variable is free.
:::

:::key title="Syllabus boundary"
JEE matrix methods: determinants up to order 3, adjoint/inverse, and Cramer's rule for 2- or 3-variable systems. Rank language is a useful explanatory lens; do not let it replace the required determinant conditions.
:::
