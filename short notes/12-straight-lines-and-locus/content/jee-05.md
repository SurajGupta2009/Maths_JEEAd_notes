---
id: jee-05
part: jee
title: "Triangle Centres in Coordinates"
---

## Centroid $G$: average the vertices

For $A,B,C$ with position pairs $(x_i,y_i)$,
$$G=\left(\frac{x_1+x_2+x_3}{3},\frac{y_1+y_2+y_3}{3}\right).$$
It lies on all three medians and divides each median vertex-to-midpoint in ratio $2:1$.

## Circumcentre $O$: equidistant from the vertices

Set $OA^2=OB^2$ and $OA^2=OC^2$. The squared terms in the unknown coordinates cancel, leaving two linear equations: the perpendicular bisectors. Their intersection is $O$; $R=OA$ is the circumradius.

:::example title="The 3–4–5 right triangle"
Take $A=(0,0), B=(4,0), C=(0,3)$. The perpendicular bisector of $AB$ is $x=2$ and of $AC$ is $y=3/2$, so $O=(2,3/2)$ and $R=5/2$. The hypotenuse midpoint confirms the same centre.
:::

## Orthocentre $H$: intersect the altitudes

An altitude through $A$ is perpendicular to $BC$, hence has direction normal to $BC$. Intersect two altitudes to find $H$. A useful vector identity (coordinates measured from any common origin) is
$$H=A+B+C-2O.$$
Indeed, $(H-A)=(B-O)+(C-O)$, whose dot product with $C-B$ is $|C-O|^2-|B-O|^2=0$; cyclically the other altitudes follow.

For the right triangle above, $H=A=(0,0)$: the legs themselves are altitudes.

## Incentre $I$: side-length weighted average

Let $a=|BC|$, $b=|CA|$, $c=|AB|$. The coordinate formula is
$$I=\left(\frac{ax_1+bx_2+cx_3}{a+b+c},\frac{ay_1+by_2+cy_3}{a+b+c}\right).$$
The weights come from the three subtriangle areas: if the common perpendicular distance is $r$, then $[IBC]=ar/2$, $[ICA]=br/2$, $[IAB]=cr/2$, while $[ABC]=(a+b+c)r/2$. The signed-area coordinates of a point are weighted by these opposite subtriangle areas, giving the formula. Thus its perpendicular distances from the sides are equal; their common value is the inradius.

:::example title="Centers of the 3–4–5 right triangle"
For $A=(0,0),B=(4,0),C=(0,3)$, side lengths opposite $A,B,C$ are $5,3,4$. Thus $G=(4/3,1)$, $O=(2,3/2)$, $H=(0,0)$, and $I=(1,1)$. Check $I$ is one unit from each leg; its distance to $3x+4y=12$ is $|3+4-12|/5=1$.
:::

:::diagram
{"type":"graph","xrange":[-1,5],"yrange":[-1,4],"curves":[{"expr":"0*x","from":0,"to":4,"color":"#16295C"},{"expr":"3-0.75*x","from":0,"to":4,"label":"BC","color":"#0F766E"}],"vlines":[{"x":0,"label":"AC"}],"points":[{"x":0,"y":0,"label":"A"},{"x":4,"y":0,"label":"B"},{"x":0,"y":3,"label":"C"},{"x":2,"y":1.5,"label":"O","color":"#B8860B"},{"x":1,"y":1,"label":"I","color":"#B91C1C","dx":-0.55},{"x":1.3333,"y":1,"label":"G","color":"#16295C","dx":0.25}],"title":"Right triangle: centroid, circumcentre, incentre"}
:::

:::key title="Use the geometric definition to choose the equations"
Centroid: medians or coordinate average. Circumcentre: equal squared distances. Orthocentre: perpendicular altitudes (or the proved vector identity). Incentre: equal perpendicular distances / side-length weights.
:::
