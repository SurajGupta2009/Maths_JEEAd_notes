---
id: olympiad-01
part: olympiad
title: "Coaxal Families and Radical Centre"
---

## A normalized pencil of circles

Write $S_i=x^2+y^2+D_ix+E_iy+F_i$ for $i=1,2$, normalizing each circle to the same $x^2+y^2$ coefficient. Then
$$S_\lambda=(1-\lambda)S_1+\lambda S_2=0$$
is a family of circles. Every member has the same radical axis $S_1-S_2=0$, and if the original circles intersect in two real points, every member passes through both. If they do not meet in real points, the radical axis is still an equal-power line but is not a real common chord.

:::example title="A pencil through two fixed points"
The family $x^2+y^2+\lambda(x-y)-2=0$ passes through $(1,1)$ and $(-1,-1)$ for every real $\lambda$. Subtracting two members gives $(\lambda_1-\lambda_2)(x-y)=0$, so their radical axis is $x-y=0$.
:::

## Radical centre, when finite

For three circles, solve two radical-axis equations. If the axes are nonparallel, their intersection is the unique finite radical centre, and equal-power transitivity makes powers to all three circles equal. If axes are parallel or coincide, do not force a finite point.

:::warn title="Concentric degeneracy from the source"
For $x^2+y^2=1$ and $x^2+y^2=4$, equal powers would require $-1=-4$, impossible: these concentric unequal circles have no finite radical axis. A third circle cannot create a finite point equidistant in power from both. Replace one circle with a nonconcentric one before asking for a radical centre.
:::
