---
id: jee-04
part: jee
title: "Tangent and Normal at a Point"
---

## Tangent: perpendicular to the radius

For $(x-h)^2+(y-k)^2=r^2$ and a point $T=(x_1,y_1)$ on the circle, the tangent is
$$(x_1-h)(x-h)+(y_1-k)(y-k)=r^2.$$
The normal is the line through $T$ and the centre $(h,k)$.

:::derive title="The tangent equation is a dot-product condition"
The radius vector $T-C$ is normal to the tangent. Thus $X$ is on the tangent exactly when $(T-C)\cdot(X-T)=0$. Rearranging gives $(T-C)\cdot(X-C)=|T-C|^2=r^2$.
:::

For $x^2+y^2+2gx+2fy+c=0$, the same tangent is
$$xx_1+yy_1+g(x+x_1)+f(y+y_1)+c=0.$$
This formula assumes $T$ lies on the circle; the “$T=0$” replacement is a mnemonic, not a substitute for checking incidence.

:::example title="Unit-free tangent check"
For $x^2+y^2=25$ at $T=(3,4)$, the tangent is $3x+4y=25$. It contains $T$, and its normal vector $(3,4)$ is the radius direction.
:::

:::diagram
{"type":"graph","xrange":[-6,7],"yrange":[-6,7],"curves":[{"expr":"sqrt(25-x**2)","from":-5,"to":5,"label":"x²+y²=25","color":"#0F766E"},{"expr":"-sqrt(25-x**2)","from":-5,"to":5,"color":"#0F766E"},{"expr":"(25-3*x)/4","from":-3,"to":7,"label":"3x+4y=25","color":"#B91C1C"}],"points":[{"x":0,"y":0,"label":"C"},{"x":3,"y":4,"label":"T"}],"title":"The radius is normal to the tangent"}
:::

:::warn title="A tangent is attached to a point on the circle"
If a proposed point is not on the circle, the at-point tangent formula does not apply. From an external point there are generally two tangents; derive them as lines through that point with discriminant zero or use the polar/chord-of-contact equation.
:::
