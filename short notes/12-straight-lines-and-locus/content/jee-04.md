---
id: jee-04
part: jee
title: "Pencils, Concurrency and Angle Bisectors"
---

## Every line through a fixed intersection

Let $L_1=0$ and $L_2=0$ be distinct, nonparallel lines meeting at $P$. Every line through $P$ can be written
$$\lambda L_1+\mu L_2=0,\qquad (\lambda,\mu)\ne(0,0).$$
Using both coefficients is essential: $L_1+tL_2=0$ alone misses $L_2=0$ for finite $t$.

:::example title="A pencil through a known point"
For $L_1=x+y-2=0$ and $L_2=x-y=0$, the intersection is $(1,1)$. Every line through it is $\lambda(x+y-2)+\mu(x-y)=0$. Choosing $(\lambda,\mu)=(1,0)$ or $(0,1)$ recovers the two original lines.
:::

## Concurrency test for three lines

For three lines $a_ix+b_iy+c_i=0$, the determinant
$$\Delta=\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}$$
vanishes exactly when their coefficient rows are linearly dependent. This means the lines have a common finite point **or** are parallel (including coincident degeneracies). To assert finite concurrency, also check that at least two distinct direction vectors are not parallel.

:::example title="Check, then locate"
$x+y-2=0$, $x-y=0$, $2x-3=0$ meet at $(1,1)$: the first two give that point, and the third also holds there. Solving two lines and checking the third is the safest concrete test.
:::

## Angle bisectors compare signed distances

For two intersecting lines $L_i=a_ix+b_iy+c_i=0$, their bisectors satisfy
$$\frac{L_1}{\sqrt{a_1^2+b_1^2}}=\pm\frac{L_2}{\sqrt{a_2^2+b_2^2}}.$$
The two signed normalized expressions are signed distances; equal absolute distances define the two bisectors. The $+$ and $-$ choices select the two angle regions.

:::derive title="Why normalization is compulsory"
The distance from $(x,y)$ to $L_i=0$ is $|L_i|/\sqrt{a_i^2+b_i^2}$. Equidistance means these magnitudes agree, which factors into the two signed equations above. Without the denominators, coefficients change the scale and the resulting lines are generally not bisectors.
:::

:::warn title="Three distinct ideas"
A line through the intersection of two lines is a pencil; concurrency asks whether several lines share a point; angle bisectors require distance normalization. Do not substitute one test for another.
:::
