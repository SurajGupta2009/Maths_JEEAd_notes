---
id: jee-07
part: jee
title: "Two-Circle Position and Circle Strategy"
---

## Compare centre distance and radii

For centres distance $d$ and radii $r_1,r_2>0$:

| Condition | Real intersection |
|---|---|
| $d>r_1+r_2$ | none; externally separate |
| $d=r_1+r_2$ | one; externally tangent |
| $|r_1-r_2|<d<r_1+r_2$ | two points |
| $d=|r_1-r_2|>0$ | one; internally tangent |
| $0<d<|r_1-r_2|$ | none; one strictly inside the other |
| $d=0$ | concentric: compare radii; identical if radii agree |

The zero-radius point-circle is handled separately by testing whether its point lies on the other circle.

## Efficient order of attack

1. Complete squares and identify centres/radii.
2. For a line, use centre-to-line distance before solving intersections.
3. For a tangent, check the point lies on the circle and use the radius as normal.
4. For a common chord, subtract normalized equations first.
5. For two circles, compare $d$ with $r_1+r_2$ and $|r_1-r_2|$.

:::example title="Two equal circles"
$(x-0)^2+y^2=4$ and $(x-3)^2+y^2=4$ have $d=3$, $r_1+r_2=4$, and $|r_1-r_2|=0$. Hence they meet twice. Subtracting gives radical axis $x=3/2$; substituting yields $y=\pm\sqrt{7}/2$.
:::

:::assume title="JEE boundary"
The official circle bullet includes circle forms, tangent, normal, chord, parametric equations and intersection with a straight line. Radical axes, power and two-circle position are useful direct applications; the official scope is not a promise to include every theorem about circles.
:::
