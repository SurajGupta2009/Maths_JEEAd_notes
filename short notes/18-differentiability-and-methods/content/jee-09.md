---
id: jee-09
part: jee
title: "Higher Derivatives and Method Selection"
---

## Iterate derivatives and look for a cycle

Second and higher derivatives are defined by repeated differentiation:
$$
f''=(f')',\qquad f^{(n+1)}=(f^{(n)})'.
$$
The trigonometric cycle
$$
\sin x\to\cos x\to-\sin x\to-\cos x\to\sin x
$$
has period $4$. Hence $(\sin x)^{(4)}=\sin x$ and $(\sin x)''|_{x=\pi/2}=-1$. Also
$$
\frac{d^n}{dx^n}e^{ax}=a^ne^{ax},
$$
so the third derivative of $e^{2x}$ at $0$ is $8$.

## A normal uses the negative reciprocal of a nonzero tangent slope

At a point with $f'(a)=m\ne0$, the normal slope is $-1/m$. For $y=x^3$ at $(1,1)$, the tangent slope is $3$, so the normal is
$$
y-1=-\frac{1}{3}(x-1).
$$
Horizontal and vertical tangent cases are handled geometrically in Chapter 19 rather than by forcing the reciprocal formula.

:::diagram
{
  "type": "table",
  "title": "Match the expression to the smallest sufficient method",
  "columns": ["Expression or question", "Method", "Final check"],
  "rows": [
    ["Definition at a point", "Difference quotient", "finite two-sided limit"],
    ["Absolute or piecewise join", "One-sided derivatives", "value and slopes agree"],
    ["Sum, product or quotient", "Derivative algebra", "denominator and power domain"],
    ["Nested expression", "Chain rule", "multiply every inner rate"],
    ["Inverse trigonometric form", "Inverse rule or simplify", "principal branch interval"],
    ["Relation F(x,y)=0", "Implicit differentiation", "point lies on relation"],
    ["Variable power or product", "Logarithmic differentiation", "positive base; multiply by y"],
    ["x(t), y(t)", "Parametric ratios", "dx/dt nonzero; divide again for y''"],
    ["nth derivative of product", "Leibniz extension", "keep only surviving orders"]
  ],
  "col_widths": [0.34, 0.32, 0.34],
  "caption": "A correct rule applied to the wrong domain is still an incorrect answer. Check the expression, the point and the requested derivative order."
}
:::

## Verify a computed derivative with a finite difference

For small nonzero $h$,
$$
\frac{f(x+h)-f(x)}{h}
$$
should approach the claimed $f'(x)$. This is a numerical diagnostic, not a replacement for the exact simplification. For example, at $x=1$ the derivative of $x^x$ is $1$, and its forward difference quotients approach $1$ from above.

:::key title="Final differentiation self-check"
Did I prove existence at a junction before using branch formulas? Did every inner derivative appear? Are inverse-trigonometric and logarithmic domains stated? For parametric second derivatives, did I divide by $dx/dt$ twice in the correct places? For a normal, is the tangent slope nonzero? Can one exact value and one finite difference independently confirm the result?
:::
