---
id: jee-01
part: jee
title: "Antiderivatives, Constants and the Standard Library"
---

## Integration reverses differentiation on an interval

A function $F$ is an antiderivative of $f$ on an interval $I$ when $F'=f$ there. We write
$$
\int f(x)\,dx=F(x)+C.
$$
If $F_1'=F_2'=f$ on $I$, then $(F_1-F_2)'=0$. The Mean Value Theorem therefore gives $F_1-F_2=C$: all antiderivatives on that interval form one vertical family.

The differential $dx$ identifies the variable. Thus $\int 2x\,dx=x^2+C$, whereas $\int 2x\,dt=2xt+C$ when $x$ is independent of $t$.

:::example title="Reverse the power, exponential and trigonometric rules"
Linearity allows term-by-term integration:
$$
\int x^3\,dx=\frac{x^4}{4}+C,\qquad
\int x^5\,dx=\frac{x^6}{6}+C,
$$
$$
\int(3x^2+2x+1)\,dx=x^3+x^2+x+C,
\qquad
\int(3x^2+2x)\,dx=x^3+x^2+C.
$$
Reverse the chain rule and include the inner scale:
$$
\int e^{2x}\,dx=\frac{1}{2}e^{2x}+C,\qquad
\int e^{3x}\,dx=\frac{1}{3}e^{3x}+C,
$$
$$
\int\sin(2x)\,dx=-\frac{1}{2}\cos(2x)+C.
$$
Every answer can be checked immediately by differentiating it.
:::

:::diagram
{
  "type": "table",
  "title": "The basic antiderivative library comes from derivatives",
  "columns": ["Integrand", "Antiderivative", "Condition"],
  "rows": [
    ["x^n", "x^(n+1)/(n+1)", "n is not -1"],
    ["1 / x", "ln|x|", "x is nonzero"],
    ["e^x", "e^x", "all real x"],
    ["sin x", "-cos x", "all real x"],
    ["cos x", "sin x", "all real x"],
    ["sec^2 x", "tan x", "cos x is nonzero"],
    ["csc^2 x", "-cot x", "sin x is nonzero"],
    ["sec x tan x", "sec x", "cos x is nonzero"]
  ],
  "col_widths": [0.25, 0.40, 0.35],
  "caption": "The exceptional power n=-1 produces a logarithm. Trigonometric formulas retain the domains on which their derivatives exist."
}
:::

## An initial value selects one member of the family

:::example title="Use the condition after finding the general antiderivative"
Suppose $F'(x)=3x^2+2x+1$ and $F(0)=5$. Integration gives
$$
F(x)=x^3+x^2+x+C.
$$
Now $F(0)=C=5$, so the required function is
$$
F(x)=x^3+x^2+x+5.
$$
The initial condition does not change the derivative; it fixes the vertical shift.
:::

:::warn title="One constant per connected interval"
On $(0,\infty)$, $\int x^{-1}dx=\ln x+C$; on $(-\infty,0)$, it is $\ln(-x)+C$. The compact formula $\ln|x|+C$ works on either interval separately. A single constant need not describe both branches simultaneously.
:::
