---
id: jee-08
part: jee
title: "Integration by Parts — Cyclic and Algebraic Products"
---

## A product with sine may need only one application

For the antiderivative used in Q17,
$$
\int x\sin x\,dx=-x\cos x+\int\cos x\,dx
=-x\cos x+\sin x+C.
$$
Its definite evaluation on $[0,\pi]$ is a Chapter 21 application of the Fundamental Theorem.

## Exponential-trigonometric products can return to the original integral

:::example title="Solve for the cyclic integral instead of abandoning it"
Let $I=\int e^x\sin x\,dx$ and $J=\int e^x\cos x\,dx$. By parts,
$$
I=e^x\sin x-J,
\qquad
J=e^x\cos x+I.
$$
Substitute the second equation into the first:
$$
I=e^x\sin x-e^x\cos x-I.
$$
Thus P7 and Q18 have the antiderivative
$$
\int e^x\sin x\,dx
=\frac{1}{2}e^x(\sin x-\cos x)+C.
$$
Differentiation gives
$$
\frac{1}{2}e^x(\sin x-\cos x)+\frac{1}{2}e^x(\cos x+\sin x)=e^x\sin x.
$$
:::

:::diagram
{
  "type": "flow",
  "title": "A cyclic by-parts calculation ends with algebra",
  "steps": [
    {"title": "Name I", "detail": "Write the original exponential-trigonometric integral as I."},
    {"title": "Apply parts twice", "detail": "Keep the signs so the second step returns to I, not a lookalike."},
    {"title": "Collect the I terms", "detail": "Move every copy of I to one side and divide by its coefficient."},
    {"title": "Differentiate", "detail": "Confirm both the exponential factor and the trigonometric coefficients."}
  ],
  "caption": "For e^x sin x, the calculation gives 2I=e^x(sin x-cos x). The factor 1/2 comes from collecting the returned integral."
}
:::

## An algebraic factor can hide a substitution after parts

:::example title="Combine by parts with a logarithmic substitution"
For $I=\int x\tan^{-1}x\,dx$, choose $u=\tan^{-1}x$ and $dv=x\,dx$:
$$
I=\frac{x^2}{2}\tan^{-1}x-\frac{1}{2}\int\frac{x^2}{1+x^2}dx.
$$
Since $x^2/(1+x^2)=1-1/(1+x^2)$,
$$
I=\frac{x^2}{2}\tan^{-1}x-\frac{x}{2}
+\frac{1}{2}\tan^{-1}x+C
=\frac{x^2+1}{2}\tan^{-1}x-\frac{x}{2}+C.
$$
:::

:::warn title="The returned integral must have exactly the same sign and coefficient"
If two applications produce $I=\text{terms}-I$, then $2I=\text{terms}$. Writing $I=\text{terms}$ at that stage loses the essential factor $1/2$. If the result is $I=I$, no information has been gained; change the arrangement.
:::
