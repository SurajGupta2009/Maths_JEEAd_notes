---
id: jee-07
part: jee
title: "Exact Equations and Potential Functions"
---

## Find one function whose total differential vanishes

The differential form $M(x,y)dx+N(x,y)dy=0$ is exact when there is a potential $F$ with
$$
F_x=M,\qquad F_y=N.
$$
On a suitable simply connected region, the standard cross-check is $M_y=N_x$. Then every solution satisfies $F(x,y)=C$. Exactness is a property of the chosen differential form, not merely of the slope expression after division.

:::diagram
{
  "type": "flow",
  "title": "Potential reconstruction without guessing the missing terms",
  "steps": [
    {"title": "Test", "detail": "Compute the y-partial of M and the x-partial of N."},
    {"title": "Integrate M", "detail": "Integrate with respect to x and add an unknown h(y)."},
    {"title": "Match N", "detail": "Differentiate in y and compare with N to determine h-prime."},
    {"title": "Set constant", "detail": "Write F = C and use the initial point to determine C."}
  ],
  "caption": "The integration term after integrating M with respect to x is h(y), not simply a numerical constant."
}
:::

:::example title="S9 and Q17: an elliptic level curve"
For $(2x+y)dx+(x+2y)dy=0$,
$$
M_y=1=N_x.
$$
Integrating $M$ in $x$ gives $F=x^2+xy+h(y)$. Then $F_y=x+h'(y)=x+2y$, so $h=y^2$. Hence
$$
x^2+xy+y^2=C.
$$
At $(0,1)$, $C=1$. The explicit branch through that point is
$$
y=\frac{-x+\sqrt{4-3x^2}}{2},
\qquad -\frac{2}{\sqrt{3}}<x<\frac{2}{\sqrt{3}}.
$$
The endpoints make $x+2y=0$, so the graph cannot be continued as a finite-slope function $y(x)$ through them.
:::

:::example title="P7 and Q18: retain the x-squared-y term"
For $(3x^2+2xy)dx+(x^2+2y)dy=0$,
$$
M_y=2x=N_x.
$$
Integrate $M$:
$$
F=x^3+x^2y+h(y).
$$
Comparison of $F_y=x^2+h'(y)$ with $N=x^2+2y$ gives $h=y^2$. Since the initial point is $(0,1)$, the solution is
$$
x^3+x^2y+y^2=1.
$$
This implicit answer is complete and often cleaner than introducing a quartic square root.
:::

## Verification in differential form

Differentiate $F(x,y)=C$ implicitly:
$$
F_x+F_y\frac{dy}{dx}=0.
$$
Where $F_y\neq0$, this gives $y'=-M/N$. Where $F_y=0$, use the original differential form or a local parametrization rather than dividing blindly.

:::warn title="M sub-y must equal N sub-x, not M sub-x"
The mixed-partial test compares the derivative of the dx coefficient with respect to y against the derivative of the dy coefficient with respect to x.
:::
