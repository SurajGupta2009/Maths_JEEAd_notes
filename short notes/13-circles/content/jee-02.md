---
id: jee-02
part: jee
title: "Determine a Circle and Parametrize It"
---

## Three independent conditions determine a circle

A general circle has equation $x^2+y^2+Dx+Ey+F=0$ with three unknown coefficients. Substituting three noncollinear points gives a linear system for $D,E,F$. If the points are collinear, no proper circle passes through all three.

:::example title="Through the origin and two unit intercepts"
Through $(0,0),(1,0),(0,1)$: the origin gives $F=0$, then $1+D=0$ and $1+E=0$. The circle is $x^2+y^2-x-y=0$, centre $(1/2,1/2)$, radius $1/\sqrt{2}$.
:::

## Diameter endpoints give a dot-product equation

For diameter endpoints $A=(x_1,y_1)$ and $B=(x_2,y_2)$, a point $P=(x,y)$ lies on the circle exactly when $\angle APB=90^\circ$ (Thales' theorem). Therefore
$$(P-A)\cdot(P-B)=0,$$
or explicitly
$$(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0.$$
The centre is the midpoint of $AB$ and the radius is $AB/2$.

:::example title="Diameter through two points"
For $A=(1,2)$, $B=(5,8)$, $(x-1)(x-5)+(y-2)(y-8)=0$, i.e. $(x-3)^2+(y-5)^2=13$. Both endpoints satisfy the diameter equation.
:::

## Parametric equations

For centre $(h,k)$ and radius $r$,
$$x=h+r\cos t,\qquad y=k+r\sin t,\qquad 0\leq t<2\pi.$$
The angle parameter traces every point once except the equivalent endpoint at $2\pi$.

A rational parameter is
$$x=h+r\frac{1-u^2}{1+u^2},\qquad y=k+r\frac{2u}{1+u^2},\qquad u\in\mathbb{R}.$$
It traces the circle except $(h-r,k)$; that missing point is the limit $|u|\to\infty$. Include it separately when a problem asks for every point.

:::warn title="Parameter is not arc length"
In the trigonometric parametrization, $t$ is the polar angle about the centre. In the rational form, $u=\tan(t/2)$ and the omitted point comes from the half-angle coordinate's pole.
:::
