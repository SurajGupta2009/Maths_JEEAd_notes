---
id: jee-06
part: jee
title: "Radical Axis — Equal Power, Common Chord"
---

## Subtract normalized circle equations

Write $S_i=x^2+y^2+D_ix+E_iy+F_i$ for $i=1,2$; the corresponding circles are $S_i=0$. Their power functions are $S_1(x,y)$ and $S_2(x,y)$. Equal power means $S_1-S_2=0$; the quadratic terms cancel, leaving a line (unless the circles are concentric or identical).

:::derive title="Why the line is perpendicular to the centres"
The centre difference is parallel to $(D_1-D_2,E_1-E_2)$, the normal vector of $S_1-S_2=0$. Thus the radical axis is perpendicular to the line of centres. When the real circles intersect, its points are exactly their common chord.
:::

:::example title="Subtract, then test equal powers"
For $x^2+y^2=9$ and $x^2+y^2-4x+6y-3=0$, subtract to get $2x-3y-3=0$. At $(0,-1)$ both power values equal $-8$, checking the line's equal-power meaning.
:::

## Three circles and the radical centre

The radical axes of three circles are the pairwise equal-power lines. If the circles are not identical and the axes are not parallel, solve two axes to get their common point; equality of the third pair follows by subtraction. Degenerate cases need care: concentric unequal circles have no finite equal-power locus, identical circles have equal power everywhere, and parallel axes need not meet in a finite radical centre.

:::warn title="A radical axis need not be a real common chord"
Two nonconcentric circles can be disjoint or nested. Their equal-power line still exists, but it contains real points only as a locus of equal powers—not points on both circles. Call it a common chord only when the circles actually intersect.
:::
