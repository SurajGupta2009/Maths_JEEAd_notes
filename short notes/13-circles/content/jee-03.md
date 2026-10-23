---
id: jee-03
part: jee
title: "A Line Meets a Circle — Chords and Position"
---

## Centre-to-line distance classifies the intersection

Let a circle have centre $C=(h,k)$, radius $r$, and let the line be $ax+by+c=0$. The distance from $C$ to the line is
$$d=\frac{|ah+bk+c|}{\sqrt{a^2+b^2}}.$$

- $d<r$: two intersection points (a secant).
- $d=r$: one repeated intersection (a tangent).
- $d>r$: no real intersection.

:::derive title="Why the chord length is twice a right-triangle leg"
The perpendicular from the centre bisects a chord. If its length is $\ell$, the right triangle has hypotenuse $r$ and one leg $d$, hence $(\ell/2)^2=r^2-d^2$ and
$$\ell=2\sqrt{r^2-d^2}.$$
This is real precisely in the secant/tangent cases $d\leq r$.
:::

:::example title="A secant, not merely a line equation"
The line $x+y=5$ is at distance $5/\sqrt{2}$ from the centre $(0,0)$ of $x^2+y^2=25$. Since this is less than $5$, it cuts a chord of length $2\sqrt{25-25/2}=5\sqrt{2}$.
:::

:::diagram
{"type":"graph","xrange":[-6,6],"yrange":[-6,6],"curves":[{"expr":"sqrt(25-x**2)","from":-5,"to":5,"label":"circle","color":"#0F766E"},{"expr":"-sqrt(25-x**2)","from":-5,"to":5,"color":"#0F766E"},{"expr":"5-x","from":-1,"to":6,"label":"secant x+y=5","color":"#B91C1C"}],"points":[{"x":0,"y":5,"label":"A"},{"x":5,"y":0,"label":"B"}],"title":"Centre-to-line distance sets the chord length"}
:::

## Solve the intersection only after classifying it

Parametrize the line by $P(t)=P_0+t(-b,a)$, where $P_0$ is any point on it. Substitute in $(x-h)^2+(y-k)^2=r^2$: a quadratic in $t$ results. Its discriminant is positive, zero or negative exactly when $d<r$, $d=r$ or $d>r$.

:::warn title="Tangency is a repeated root"
A tangent line meets the circle in one geometric point but gives a double root after substitution. Do not infer “no intersection” from a zero discriminant.
:::
