---
id: jee-06
part: jee
title: "Locus — Translate the Condition, Then Verify"
---

## A locus is a set of points satisfying one condition

Let the moving point be $P=(x,y)$. Write the geometric condition using distances, slopes or projections; simplify to an equation; then check that every point of the resulting equation satisfies the original condition. Squaring can introduce false branches, so the final check matters.

:::example title="Equidistant from two fixed points"
For $A=(0,0)$ and $B=(4,0)$, $PA=PB$ gives $x^2+y^2=(x-4)^2+y^2$, hence $x=2$. This is the perpendicular bisector of $AB$, not a circle.
:::

## Constant distance from one point

$PA=r$ becomes $(x-a)^2+(y-b)^2=r^2$: a circle centred at $A=(a,b)$. The special case $r=0$ is the single point $A$; $r<0$ has no solutions because distance is nonnegative.

## Constant ratio of distances: Apollonius

For distinct fixed points $A=(x_1,y_1)$ and $B=(x_2,y_2)$, let $PA/PB=k\geq0$. Squaring gives
$$(x-x_1)^2+(y-y_1)^2=k^2\left((x-x_2)^2+(y-y_2)^2\right).$$
If $k=1$, equal quadratic terms cancel and the locus is the perpendicular bisector. If $k\ne1$, it is a circle with centre
$$\left(\frac{x_1-k^2x_2}{1-k^2},\frac{y_1-k^2y_2}{1-k^2}\right),$$
and radius $\dfrac{k\,AB}{|1-k^2|}$. At $k=0$, interpret the zero-radius circle as the point $A$.

:::derive title="The centre and radius are not guessed"
After expansion, the coefficient of $x^2+y^2$ is $1-k^2$ and the linear terms are $2(k^2x_2-x_1)x+2(k^2y_2-y_1)y$. Divide by $1-k^2$ and complete squares. For $A=(0,0),B=(d,0)$ the centre is $\left(k^2d/(k^2-1),0\right)$; substituting it gives radius $kd/|k^2-1|$.
:::

:::example title="Ratio 2 on a 4-unit baseline"
For $A=(0,0)$, $B=(4,0)$ and $PA/PB=2$, $x^2+y^2=4((x-4)^2+y^2)$, so $(x-16/3)^2+y^2=64/9$. Check $P=(16/3,8/3)$: $PA/PB=2$.
:::

:::warn title="Locus checklist"
Preserve nonnegative distance conditions when squaring; handle $k=1$ separately before dividing by $1-k^2$; distinguish a perpendicular bisector (line) from a ratio circle; and test a point in the final equation against the original condition.
:::
