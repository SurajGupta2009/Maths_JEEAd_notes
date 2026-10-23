---
id: olympiad-01
part: olympiad
title: "Euler Line — Three Centres, One Ratio"
---

## The vector identities

For a non-equilateral triangle with circumcentre $O$, centroid $G$ and orthocentre $H$, use vectors measured from any origin. Since $H=A+B+C-2O$ and $G=(A+B+C)/3$,
$$G-O=\frac{1}{3}(H-O).$$
Thus $O,G,H$ are collinear and $OG:GH=1:2$ (unless the triangle is equilateral, where $O=G=H$ and the line has no unique direction).

:::derive title="Why the orthocentre vector works"
Translate the origin to $O$, so $|A|=|B|=|C|=R$ and $H=A+B+C$. Then $H-A=B+C$. Its dot product with $C-B$ is $|C|^2-|B|^2=0$, so $AH\perp BC$; cyclically, all three altitudes pass through $H$.
:::

## Add the nine-point centre

The nine-point centre is $N=(O+H)/2$. Along the Euler line the parameter positions from $O$ to $H$ are $0,1/3,1/2,1$, so
$$O,G,N,H\quad\text{and}\quad OG:GN:NH=2:1:3.$$
This is a length ratio, not the ratio of the four position coordinates.

:::example title="A 3–4–5 right triangle"
For $A=(0,0),B=(4,0),C=(0,3)$, $O=(2,3/2)$ and $H=A$. Then $G=(4/3,1)$, $N=(1,3/4)$, and the ordered distances along $OH$ are in ratio $2:1:3$.
:::

:::warn title="Equilateral exception"
In an equilateral triangle, all four classical centres coincide. Any statement that the Euler line has a direction or that the centres are distinct needs a non-equilateral hypothesis.
:::
