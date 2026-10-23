---
id: jee-05
part: jee
title: "Power, Tangent Length and Chord of Contact"
---

## Power records inside, on, or outside

For circle centre $C=(h,k)$ and radius $r$, define
$$\operatorname{Pow}(P)=|P-C|^2-r^2.$$
It is negative inside, zero on, and positive outside. In the general equation $x^2+y^2+2gx+2fy+c=0$, the power at $(x_0,y_0)$ is the left-hand side evaluated there.

:::derive title="Tangent length from a right triangle"
If $P$ is outside and $T$ is a tangent point, $CT\perp PT$. Therefore
$$PT^2=PC^2-CT^2=PC^2-r^2=\operatorname{Pow}(P).$$
So each tangent from $P$ has length $\sqrt{\operatorname{Pow}(P)}$.
:::

:::example title="Tangent length is not centre distance"
From $P=(5,5)$ to $x^2+y^2=9$, power is $25+25-9=41$. Each tangent has length $\sqrt{41}$, whereas $PC=\sqrt{50}$.
:::

## Chord of contact / polar of an external point

For a circle centred at the origin, $x^2+y^2=r^2$, the two tangent points from $P=(p,q)$ lie on the line
$$px+qy=r^2.$$
This line is the **chord of contact**. Its intersection with the circle gives the two contact points. For a translated circle, first use coordinates relative to its centre: $(P-C)\cdot(X-C)=r^2$.

:::example title="Find both contacts by one line and one circle"
From $P=(5,0)$ to $x^2+y^2=9$, the chord of contact is $5x=9$, so $x=9/5$. Then $y^2=9-81/25=144/25$, giving contacts $(9/5,\pm12/5)$. The tangent length is $\sqrt{25-9}=4$.
:::

:::warn title="The polar formula needs the same circle centre"
For a circle not centred at the origin, replace $P$ and $X$ by their vectors from the centre. Forgetting this translation shifts the chord of contact.
:::
