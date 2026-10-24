---
id: olympiad-05
part: olympiad
title: "Feynman Differentiation under the Integral Sign"
---

## Differentiate a parameter, then recover the constant

Under suitable local domination and convergence hypotheses,
$$
I(a)=\int f(x,a)dx
\quad\Longrightarrow\quad
I'(a)=\int\frac{\partial f}{\partial a}(x,a)dx.
$$
After evaluating the simpler derivative, integrate in $a$ and use one known value to determine the constant.

:::example title="S14/Q28 and P14/Q29: differentiate a power integral"
For $a>-1$,
$$
F(a)=\int_0^1x^a dx=\frac{1}{a+1}.
$$
Differentiating once and twice gives
$$
\int_0^1x^a\ln x\,dx=-\frac{1}{(a+1)^2},
\qquad
\int_0^1x^a(\ln x)^2dx=\frac{2}{(a+1)^3}.
$$
At $a=1$, the first identity gives S14/Q28 $=-1/4$. At $a=0$, the second gives P14/Q29 $=2$. These agree with the by-parts evaluations in Lesson 8.
:::

## Q45: a logarithmic quotient represented by a parameter integral

For $a>-1$, define
$$
I(a)=\int_0^1\frac{x^a-1}{\ln x}dx.
$$
At $x=1$, the expression has continuous limiting value $a$; convergence at $0$ follows from the $x^a$ scale and the logarithmic denominator. Differentiation gives
$$
I'(a)=\int_0^1x^a dx=\frac{1}{a+1}.
$$
Since $I(0)=0$,
$$
I(a)=\int_0^a\frac{dt}{1+t}=\ln(1+a).
$$
Thus Q45, with $a=3$, equals $\ln4=2\ln2$.

The two anchors are consistent: $I(0)=0=\ln1$, and $I'(a)=1/(1+a)$ is exactly the derivative of $\ln(1+a)$. For $-1<a<0$, the oriented parameter integral and the logarithm are both negative, providing an additional sign check.

## Q45's source representation needs a corrected lower limit

For $x>0$, $x\ne1$,
$$
\int_0^a x^t dt=\left[\frac{x^t}{\ln x}\right]_0^a
=\frac{x^a-1}{\ln x}.
$$
If the lower limit were $1$ as printed in the source, the value would instead be $(x^a-x)/\ln x$. Thus the intended representation requires lower limit $0$; the final Q45 answer $\ln4$ remains correct.


:::diagram
{
  "type": "flow",
  "title": "Feynman differentiation is a four-step method with hypotheses",
  "steps": [
    {"title": "Introduce a parameter", "detail": "Choose a family containing the target and one easy value."},
    {"title": "Justify differentiation", "detail": "Use local integrable domination and convergence at every endpoint."},
    {"title": "Evaluate I'(a)", "detail": "The parameter derivative should remove a difficult factor."},
    {"title": "Integrate and anchor", "detail": "Recover I(a) using a known value such as I(0) or the limit at infinity."}
  ],
  "caption": "For Q45, the anchor is I(0)=0. For the power derivatives, differentiation gives the answer directly without an integration constant."
}
:::

:::warn title="Differentiation under the integral sign needs its own hypotheses"
Convergence of the original integral alone is not sufficient. Use local integrable domination for the parameter derivative, check improper endpoints, and anchor the integrated result with a known value.
:::
