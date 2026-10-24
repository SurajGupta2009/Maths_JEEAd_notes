---
id: jee-03
part: jee
title: "Logarithmic Substitution and Trigonometric Integrals"
---

## A numerator equal to the denominator's derivative gives a logarithm

Where $g(x)\ne0$,
$$
\int\frac{g'(x)}{g(x)}\,dx=\ln|g(x)|+C.
$$
The absolute value is essential on negative branches. With $u=3x+2$,
$$
\int\frac{dx}{3x+2}=\frac{1}{3}\ln|3x+2|+C.
$$
Similarly,
$$
\int\frac{2x+2}{x^2+2x+2}dx=\ln(x^2+2x+2)+C,
$$
where the quadratic is always positive, so absolute-value signs are optional.

:::example title="Tangent and cotangent are logarithmic substitutions"
Since $\tan x=\sin x/\cos x$, put $u=\cos x$ on an interval where $\cos x\ne0$:
$$
\int\tan x\,dx=-\int\frac{du}{u}
=-\ln|\cos x|+C=\ln|\sec x|+C.
$$
In the same way,
$$
\int\cot x\,dx=\ln|\sin x|+C.
$$
:::

:::diagram
{
  "type": "table",
  "title": "Four standard trigonometric logs and their domains",
  "columns": ["Integral", "Antiderivative", "Valid away from"],
  "rows": [
    ["tan x", "ln|sec x|", "zeros of cos x"],
    ["cot x", "ln|sin x|", "zeros of sin x"],
    ["sec x", "ln|sec x + tan x|", "zeros of cos x"],
    ["csc x", "ln|csc x - cot x|", "zeros of sin x"]
  ],
  "col_widths": [0.20, 0.47, 0.33],
  "caption": "Each formula is proved by differentiation on one connected interval. Constants can change when a different interval is chosen."
}
:::

## Secant and cosecant use a multiplier that creates $u'/u$

For secant, let $u=\sec x+\tan x$. Then
$$
\frac{du}{dx}=\sec x\tan x+\sec^2x
=\sec x(\sec x+\tan x)=\sec x\,u.
$$
Therefore $u'/u=\sec x$, giving the table's formula. For cosecant, $u=\csc x-\cot x$ satisfies $u'=\csc x\,u$.

:::example title="Check a scaled quotient rather than memorising its coefficient"
$$
\int\frac{6x}{3x^2+5}dx
=\ln(3x^2+5)+C,
$$
because the numerator is exactly the derivative of the denominator. In contrast,
$$
\int\frac{x}{3x^2+5}dx
=\frac{1}{6}\ln(3x^2+5)+C.
$$
:::

:::warn title="A logarithm does not remove a singularity"
The formulas above are valid only between consecutive excluded points. Never integrate through a zero of the original denominator as though $\ln|g(x)|$ made the integrand finite there.
:::
