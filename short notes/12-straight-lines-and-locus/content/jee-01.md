---
id: jee-01
part: jee
title: "Coordinates — Displacement, Section, Translation"
---

## A point is a pair of signed coordinates

A point $P=(x,y)$ is reached by moving $x$ units horizontally and $y$ vertically from the origin. Coordinate differences, not absolute positions, measure displacement.

:::derive title="Distance and midpoint from the right triangle"
For $A(x_1,y_1)$ and $B(x_2,y_2)$, the horizontal and vertical legs have lengths $|x_2-x_1|$ and $|y_2-y_1|$. Pythagoras gives
$$AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.$$
The midpoint has half of each displacement: $M=((x_1+x_2)/2,(y_1+y_2)/2)$.
:::

:::example title="Read displacement before calculating"
From $A=(-2,1)$ to $B=(4,9)$ the displacement is $(6,8)$, so $AB=\sqrt{6^2+8^2}=10$. The midpoint is $(1,5)$.
:::

## Section formula: keep the ratio orientation explicit

If $P$ divides $AB$ internally in the ratio $AP:PB=m:n$, then
$$P=\left(\frac{nx_1+mx_2}{m+n},\frac{ny_1+my_2}{m+n}\right).$$
The coefficient of $A$ is the *opposite* ratio-part $n$. This is a weighted average: for $m=n$, it is the midpoint. For external division with $AP:PB=m:n$, use $P=\left((mx_2-nx_1)/(m-n),(my_2-ny_1)/(m-n)\right)$ with $m\ne n$; verify which endpoint lies between the other two. If $m=n$, no finite point divides externally in that ratio.

:::example title="A ratio check catches reversed weights"
If $A=(1,2)$, $B=(6,7)$ and $AP:PB=2:3$, then $P=(3,4)$: it lies two-fifths of the way from $A$ to $B$. Substitution verifies $AP:PB=2:3$.
:::

:::warn title="Section-formula trap"
Never memorize the numerator without the ratio convention. A point dividing $AB$ in $2:3$ must be closer to $A$, so its coordinates must be weighted more heavily toward $A$.
:::

## Shift the origin, not the geometry

Let the new origin $O'$ have old coordinates $(h,k)$, with axes kept parallel. If a point has new coordinates $(X,Y)$ and old coordinates $(x,y)$, then
$$(x,y)=(X+h,Y+k),\qquad (X,Y)=(x-h,y-k).$$

:::derive title="Translation rule for equations"
To rewrite an old equation in the new coordinates, substitute $x=X+h$ and $y=Y+k$, then simplify. Example: the old line $2x-y+1=0$ viewed from $O'=(1,-2)$ becomes $2(X+1)-(Y-2)+1=0$, i.e. $2X-Y+5=0$. Translation changes constants and point coordinates, not lengths, angles, or slopes.
:::

## Centroid is the average of the vertices

For triangle vertices $A(x_1,y_1),B(x_2,y_2),C(x_3,y_3)$,
$$G=\left(\frac{x_1+x_2+x_3}{3},\frac{y_1+y_2+y_3}{3}\right).$$
The two medians meet at this point; it divides each median in the ratio $2:1$ measured from the vertex.

The signed double-area of triangle $ABC$ is
$$x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2).$$
Its absolute value divided by $2$ is the area; it vanishes exactly for collinear vertices. This determinant identity is a useful derived coordinate test, not a separate line-syllabus bullet.

:::key title="Coordinate habits"
Write displacement as $(x_2-x_1,y_2-y_1)$; check an internal section point lies between its endpoints; for a shifted origin substitute old coordinates $x=X+h,y=Y+k$; and average coordinates for the centroid.
:::
