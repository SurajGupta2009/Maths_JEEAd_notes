---
id: jee-09
part: jee
title: "Partial Fractions — Division and Linear Factors"
---

## First make the rational function proper

A rational function is proper when the numerator has smaller degree than the denominator. If not, divide first:
$$
\frac{x^2+1}{x+1}=x-1+\frac{2}{x+1}.
$$
Therefore
$$
\int\frac{x^2+1}{x+1}dx
=\frac{x^2}{2}-x+2\ln|x+1|+C.
$$
Only then factor the denominator and decompose the proper remainder.

:::diagram
{
  "type": "flow",
  "title": "A rational function has a reliable preparation order",
  "steps": [
    {"title": "Divide if improper", "detail": "Separate the polynomial part before assigning partial-fraction coefficients."},
    {"title": "Factor the denominator", "detail": "Use real linear and irreducible quadratic factors with their multiplicities."},
    {"title": "Write every term", "detail": "Include all powers of repeated factors and linear numerators over quadratics."},
    {"title": "Solve and integrate", "detail": "Match coefficients, integrate each standard piece and differentiate the total."}
  ],
  "caption": "Most partial-fraction errors occur before integration: no prior division, an omitted repeated power or an incomplete numerator over a quadratic."
}
:::

## Distinct linear factors produce logarithms

:::example title="S8 and Q19: decompose before integrating"
Since
$$
\frac{1}{(x+1)(x+2)}=\frac{1}{x+1}-\frac{1}{x+2},
$$
we obtain
$$
\int\frac{dx}{(x+1)(x+2)}
=\ln|x+1|-\ln|x+2|+C
=\ln\left|\frac{x+1}{x+2}\right|+C.
$$
The definite Q20 applies limits to this antiderivative in Chapter 21; no singularity may lie inside the interval used.
:::

## A repeated linear factor needs every power up to its multiplicity

For a factor $(x-a)^k$, include
$$
\frac{A_1}{x-a}+\frac{A_2}{(x-a)^2}+\cdots+\frac{A_k}{(x-a)^k}.
$$

:::example title="Repeated factor: one logarithm and one reciprocal power"
Write
$$
\frac{2x+3}{(x+1)^2}=\frac{A}{x+1}+\frac{B}{(x+1)^2}.
$$
Then $2x+3=A(x+1)+B$, so $A=2$ and $B=1$. Hence
$$
\int\frac{2x+3}{(x+1)^2}dx
=2\ln|x+1|-\frac{1}{x+1}+C.
$$
:::

:::warn title="A single A/(x-a) is incomplete for a repeated factor"
Omitting $(x-a)^{-2},\ldots,(x-a)^{-k}$ usually makes the coefficient equations impossible—or, worse, produces an answer that matches at one point but has the wrong derivative. Differentiate the complete result on an allowed interval.
:::
