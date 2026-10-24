---
id: olympiad-05
part: olympiad
title: "Extension V — Complexification and Ansatz"
---

## One complex exponential integrates sine and cosine together

Using $i^2=-1$ and $e^{ix}=\cos x+i\sin x$,
$$
\int e^{(a+ib)x}dx=\frac{e^{(a+ib)x}}{a+ib}+C,
\qquad a+ib\ne0.
$$
Taking real and imaginary parts gives the general formulas
$$
\int e^{ax}\sin bx\,dx
=\frac{e^{ax}(a\,\sin bx-b\,\cos bx)}{a^2+b^2}+C,
$$
$$
\int e^{ax}\cos bx\,dx
=\frac{e^{ax}(a\,\cos bx+b\,\sin bx)}{a^2+b^2}+C.
$$
At $a=b=1$, the sine formula becomes Q18's $\frac{1}{2}e^x(\sin x-\cos x)$.

## An ansatz gives the same result without complex arithmetic

Try
$$
F=e^{ax}(A\,\sin bx+B\,\cos bx).
$$
Then
$$
F'=e^{ax}\left((aA-bB)\sin bx+(bA+aB)\cos bx\right).
$$
To make $F'=e^{ax}\sin bx$, solve
$$
aA-bB=1,\qquad bA+aB=0,
$$
which gives $A=a/(a^2+b^2)$ and $B=-b/(a^2+b^2)$. The cosine case only changes the right-hand sides of these two linear equations.

:::diagram
{
  "type": "graph",
  "title": "The cyclic antiderivative has slope e^x sin x",
  "xrange": [-2, 2], "yrange": [-1.5, 7.5],
  "xticks": [-2, -1, 0, 1, 2], "yticks": [-1, 0, 2, 4, 6],
  "curves": [
    {"expr": "exp(x)*sin(x)", "from": -2, "to": 2, "color": "#B91C1C"},
    {"expr": "0.5*exp(x)*(sin(x)-cos(x))", "from": -2, "to": 2}
  ],
  "points": [
    {"x": 0, "y": -0.5, "label": "F(0)=-1/2", "dx": 0.15, "dy": -0.35},
    {"x": 1.5707963268, "y": 2.4052386905, "label": "F(pi/2)", "dx": -0.85, "dy": 0.35}
  ],
  "caption": "Red is f=e^x sin x; teal is F=e^x(sin x-cos x)/2. The slope of teal at zero is f(0)=0, while at pi/2 it is f(pi/2)=e^(pi/2), about 4.8105."
}
:::

:::example title="The same ansatz handles a damped cosine"
With $a=-2$ and $b=3$,
$$
\int e^{-2x}\cos3x\,dx
=\frac{e^{-2x}(-2\cos3x+3\sin3x)}{13}+C.
$$
Differentiation restores both exponential damping and the frequency $3$; the denominator is $(-2)^2+3^2=13$.
:::

:::warn title="Do not mix the sine and cosine coefficient rows"
The sine antiderivative has $a\,\sin bx-b\,\cos bx$; the cosine antiderivative has $a\,\cos bx+b\,\sin bx$. A quick differentiation at one general parameter set is safer than relying on visual similarity between the two formulas.
:::
