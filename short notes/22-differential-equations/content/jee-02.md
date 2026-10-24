---
id: jee-02
part: jee
title: "Formation — Eliminate Every Arbitrary Constant"
---

## Differentiate enough times, then eliminate

A family with $n$ independent arbitrary constants usually requires $n$ differentiations and leads to an equation of order $n$. The goal is not merely to differentiate: every arbitrary constant must be eliminated. The resulting differential equation can have additional solutions, so formation gives a necessary equation for the family, not always an identical solution set.

:::diagram
{
  "type": "flow",
  "title": "From a family of curves to a differential equation",
  "steps": [
    {"title": "Count", "detail": "Count independent arbitrary constants in the given family."},
    {"title": "Differentiate", "detail": "Differentiate with respect to x, treating y as y(x)."},
    {"title": "Eliminate", "detail": "Remove every constant using the original and derived relations."},
    {"title": "Audit", "detail": "Note divisions, excluded points and any extra solution branches."}
  ],
  "caption": "One constant normally means first order; two independent constants normally mean second order."
}
:::

:::example title="S2 and Q3: the family y = cx + c squared"
For $y=cx+c^2$, write $p=y'$. Differentiation gives $p=c$. Substitution in the original family yields
$$
{y=xy'+(y')^2}.
$$
This is a Clairaut equation. Its singular solution $y=-x^2/4$ is not one of the original straight lines; Extension II explains why the differential equation has that extra branch.
:::

:::example title="P2 and Q4: circles through the origin"
The circles $(x-a)^2+y^2=a^2$ satisfy
$$
x^2+y^2=2ax.
$$
Implicit differentiation gives $2x+2yy'=2a$. Eliminating $a$ on intervals where $x\neq0$ gives
$$
2x+2yy'=\frac{x^2+y^2}{x}
\quad\Longrightarrow\quad
{2xyy'=y^2-x^2}.
$$
The final polynomial form is the required formation result. At the origin it carries no slope information, so do not infer a unique tangent there.
:::

:::example title="Q41: two constants demand a second-order equation"
For $y=c_1e^x+c_2e^{-x}$,
$$
y'=c_1e^x-c_2e^{-x},
\qquad
y''=c_1e^x+c_2e^{-x}=y.
$$
Thus the required equation is ${y''-y=0}$. Conversely, its characteristic roots are $1$ and $-1$, so the displayed family is its full real general solution.
:::

:::warn title="Do not differentiate without using the original relation"
Differentiation alone leaves the constants in place. Always return to the family equation and eliminate them; otherwise the order may look right while the formation task remains unfinished.
:::
