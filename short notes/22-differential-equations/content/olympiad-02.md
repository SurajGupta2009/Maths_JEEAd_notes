---
id: olympiad-02
part: olympiad
title: "Extension II — Clairaut Equations and Singular Envelopes"
---

## Differentiation splits into straight lines and an envelope

A Clairaut equation has the form
$$
y=xy'+f(y').
$$
Set $p=y'$ and differentiate:
$$
p=p+\left(x+f'(p)\right)\frac{dp}{dx}
\quad\Longrightarrow\quad
\left(x+f'(p)\right)p'=0.
$$
The branch $p'=0$ gives $p=C$ and the general straight-line family $y=Cx+f(C)$. The other branch, $x+f'(p)=0$, gives a parametric singular solution; equivalently, eliminate $C$ using $F=y-Cx-f(C)=0$ and $F_C=0$.

:::diagram
{
  "type": "flow",
  "title": "Clairaut's two branches answer two different questions",
  "steps": [
    {"title": "General family", "detail": "Take p = C to obtain all straight-line members y = Cx + f(C)."},
    {"title": "Envelope condition", "detail": "Differentiate the line equation with respect to C and set the result to zero."},
    {"title": "Eliminate C", "detail": "Combine the line and envelope equations to obtain x and y."},
    {"title": "Verify", "detail": "Substitute the envelope into the original equation and check tangency."}
  ],
  "caption": "A singular solution need not belong to the general family for any finite value of its arbitrary constant."
}
:::

:::example title="S15 and Q32: a downward envelope"
For $y=xp+p^2$, the general family is
$$
y=Cx+C^2.
$$
The other branch is $x+2p=0$, so $p=-x/2$ and
$$
y=x\left(-\frac{x}{2}\right)+\left(-\frac{x}{2}\right)^2
=-\frac{x^2}{4}.
$$
Thus the singular solution is $y=-x^2/4$. For a fixed C, its tangent line touches this parabola at $(-2C,-C^2)$, as shown in Visual Lab 6.
:::

:::example title="P11 and Q33: reversing the sign reverses the envelope"
For $y=xp-p^2$, the line family is $y=Cx-C^2$. The envelope conditions are
$$
y=Cx-C^2,\qquad x-2C=0.
$$
Therefore $C=x/2$ and
$$
y=\frac{x^2}{2}-\frac{x^2}{4}=\frac{x^2}{4}.
$$
Direct verification gives $p=x/2$ and $xp-p^2=x^2/4=y$.
:::

## Why the extra solution is not contradictory

Differentiating the original equation is reversible only with care: the factorized equation permits both $p'=0$ and $x+f'(p)=0$. Reporting only the first branch discards the second. The word singular describes the envelope's relation to the general family, not a blow-up or discontinuity.

:::warn title="Envelope algebra still needs a solution check"
The envelope conditions are necessary for the standard smooth family construction. Substitution into the original differential equation confirms that the resulting curve is genuinely a solution.
:::
