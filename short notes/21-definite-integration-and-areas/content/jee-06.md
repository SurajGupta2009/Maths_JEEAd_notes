---
id: jee-06
part: jee
title: "King's Property and Reflection Symmetry"
---

## Reflect the dummy variable across the interval

The substitution $x\mapsto a+b-x$ reverses orientation twice and gives
$$
\int_a^b f(x)dx=\int_a^b f(a+b-x)dx.
$$
On $[0,a]$, this is King's property
$$
\int_0^a f(x)dx=\int_0^a f(a-x)dx.
$$
It is most powerful when the original and reflected integrands can be added into something simpler.

:::diagram
{
  "type": "flow",
  "title": "King's property is a reflection followed by a useful combination",
  "steps": [
    {"title": "Name I", "detail": "Write the definite integral and its exact interval."},
    {"title": "Reflect x", "detail": "Replace x by a+b-x; the interval remains the same."},
    {"title": "Add the forms", "detail": "Look for a constant, simpler numerator or paired identity."},
    {"title": "Solve for I", "detail": "Divide by the coefficient and check any removable endpoints."}
  ],
  "caption": "Reflection does not assert f(x)=f(a+b-x). It asserts equality of the two integrals after substitution, even when the functions differ pointwise."
}
:::

:::example title="P10 and Q24: sine and cosine exchange places"
Let $I=\int_0^{\pi/2}\sin^2x\,dx$. Reflection gives $I=\int_0^{\pi/2}\cos^2x\,dx$. Adding,
$$
2I=\int_0^{\pi/2}(\sin^2x+\cos^2x)dx=\frac{\pi}{2},
$$
so $I=\pi/4$.
:::

:::example title="S12 and Q26: add two reciprocal forms"
For
$$
I=\int_0^{\pi/2}\frac{dx}{1+\tan x},
$$
reflection gives $I=\int_0^{\pi/2}dx/(1+\cot x)$. For $u>0$,
$$
\frac{1}{1+u}+\frac{1}{1+1/u}=\frac{1}{1+u}+\frac{u}{1+u}=1.
$$
Therefore $2I=\pi/2$ and $I=\pi/4$. At the endpoint $\pi/2$, the original expression is assigned its continuous limiting value $0$.
:::

## Q36: the final answer is right, but the printed prose is not

For Q36,
$$
\frac{\sin^2x}{\sin^2x+\cos^2x}=\sin^2x,
$$
not $1/2$. Hence
$$
\int_0^{\pi/2}\frac{\sin^2x}{\sin^2x+\cos^2x}dx
=\int_0^{\pi/2}\sin^2x\,dx=\frac{\pi}{4}.
$$
The source solution's final value is correct; its phrase “the integrand is $1/2$” is corrected here.

:::warn title="Reflection does not remove an interior singularity"
King's property preserves the interval and any singularities within it. If the integrand is improper, establish convergence and interpret the reflection through limits before adding the two forms.
:::
