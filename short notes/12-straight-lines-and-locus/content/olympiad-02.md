---
id: olympiad-02
part: olympiad
title: "Nine-Point Circle: Coordinates"
---

## The nine points

For triangle $ABC$, the side midpoints, the three altitude feet, and the midpoints of $AH,BH,CH$ lie on one circle. Its centre is $N=(O+H)/2$ and its radius is $R/2$, where $O,H$ and $R$ are the circumcentre, orthocentre and circumradius.

:::derive title="A coordinate proof for three of the nine points"
Put the midpoint of $BC$ at the origin and take $BC$ as the $x$-axis. Write $B=(-s,0)$, $C=(s,0)$, circumcentre $O=(0,q)$, and $A=(u,v)$. Then $R^2=s^2+q^2=u^2+(v-q)^2$. The orthocentre vector identity gives $H=(u,v-2q)$ and hence $N=(O+H)/2=(u/2,(v-q)/2)$. The midpoint of $BC$ is $(0,0)$, the foot from $A$ to $BC$ is $(u,0)$, and the midpoint of $AH$ is $(u,v-q)$. Each differs from $N$ by a vector with squared length $[u^2+(v-q)^2]/4=R^2/4$. Cycling the labels proves the same for the other six points.
:::

:::example title="Check all nine points in a non-right triangle"
For $A=(0,0),B=(4,0),C=(1,3)$, $O=(2,1)$, $H=(1,1)$, so $N=(3/2,1)$ and $R=\sqrt{5}$. The three side midpoints are $(2,0),(5/2,3/2),(1/2,3/2)$; the altitude feet are $(2,2),(2/5,6/5),(1,0)$; the midpoints of $AH,BH,CH$ are $(1/2,1/2),(5/2,1/2),(1,2)$. Each is at distance $\sqrt{5}/2$ from $N$.
:::

:::warn title="A midpoint check alone is not the nine-point proof"
The side-midpoint calculation does not automatically cover the altitude feet. The coordinate derivation above checks the side-midpoint, one altitude-foot and one midpoint-of-altitude cases, then cycles the labels. A few numerical examples alone would not establish the theorem for every triangle.
:::
