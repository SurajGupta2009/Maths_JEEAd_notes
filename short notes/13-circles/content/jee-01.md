---
id: jee-01
part: jee
title: "Circle — Definition, Forms, Reality Check"
---

## Definition: fixed distance from a centre

A circle with centre $C=(h,k)$ and radius $r\geq0$ is the locus
$$(x-h)^2+(y-k)^2=r^2.$$
For $r>0$ this is a proper circle; $r=0$ is the single point $C$.

:::derive title="Complete squares in the general equation"
For $x^2+y^2+2gx+2fy+c=0$, group the coordinate terms:
$$(x+g)^2+(y+f)^2=g^2+f^2-c.$$
Thus the centre is $(-g,-f)$ and $r^2=g^2+f^2-c$. The equal coefficients of $x^2,y^2$, with no $xy$ term, are essential for a circle in orthogonal Cartesian axes.
:::

## Three cases—do not call every equation a circle

- $g^2+f^2-c>0$: a real circle of positive radius.
- $g^2+f^2-c=0$: a point-circle (one real point).
- $g^2+f^2-c<0$: no real points.

:::example title="Centre, radius, then check"
$x^2+y^2-2x-4y-4=0$ gives $g=-1,f=-2,c=-4$, centre $(1,2)$ and $r^2=1+4+4=9$, so $r=3$. Check $(1,5)$: it is distance $3$ from $(1,2)$ and satisfies the equation.
:::

:::warn title="Radius is the nonnegative square root"
If a formula yields $r^2<0$, it is not a real circle. If $r^2=0$, do not describe it as a circle with positive circumference. A negative value cannot be repaired by dropping a sign.
:::
