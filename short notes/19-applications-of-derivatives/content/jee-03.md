---
id: jee-03
part: jee
title: "Tangent Lengths, Differentials and Approximation"
---

## Derive lengths from the x-axis intersections

At $P=(x_0,y_0)$, suppose $m=f'(x_0)\ne0$ and $y_0\ne0$. The tangent meets the $x$-axis at $T=(x_0-y_0/m,0)$, while the normal meets it at $N=(x_0+my_0,0)$. Horizontal projections give the subtangent and subnormal; the Pythagorean theorem gives the segment lengths.

:::diagram
{
  "type": "table",
  "title": "Tangent and normal lengths come from the same two intersections",
  "columns": ["Quantity", "Formula", "Geometric meaning"],
  "rows": [
    ["Subtangent", "|y0/m|", "horizontal projection"],
    ["Tangent segment", "|y0| sqrt(1+m^2)/|m|", "P to tangent intercept"],
    ["Subnormal", "|m y0|", "horizontal projection"],
    ["Normal segment", "|y0| sqrt(1+m^2)", "P to normal intercept"]
  ],
  "col_widths": [0.24, 0.43, 0.33],
  "caption": "These formulas concern segments to the x-axis and require the stated nonzero cases. Horizontal or vertical lines are handled directly."
}
:::

For $y=x^3$ at $(1,1)$, $m=3$. Hence the subtangent is $1/3$, the subnormal is $3$, the tangent segment is $\sqrt{10}/3$, and the normal segment is $\sqrt{10}$.

## A differential is the tangent-line increment

For small $\Delta x$,
$$
f(x+\Delta x)\approx f(x)+f'(x)\Delta x.
$$
This is a local approximation, not an exact identity. A useful check is to compare with a direct numerical evaluation and, when possible, estimate the error using the next derivative.

:::example title="Three standard linear approximations"
For $f(x)=\sqrt{x}$ at $x=25$, $f'(25)=1/10$, so
$$
\sqrt{25.4}\approx5+\frac{1}{10}(0.4)=5.04.
$$
The direct value is $5.039841\ldots$, so the approximation overestimates by about $1.59\times10^{-4}$.

For $f(x)=x^{10}$ at $x=1$,
$$
(1.01)^{10}\approx1+10(0.01)=1.1,
$$
compared with $1.104622\ldots$. For $f(x)=\ln x$ at $x=1$,
$$
\ln(1.02)\approx0+1(0.02)=0.02,
$$
compared with $0.019803\ldots$.
:::

:::warn title="A small step does not make the linear answer exact"
The approximation omits higher-order terms. In the square-root example, the curve is concave, so its tangent lies above the graph and the estimate is slightly too large.
:::
