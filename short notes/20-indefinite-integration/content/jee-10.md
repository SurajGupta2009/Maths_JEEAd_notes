---
id: jee-10
part: jee
title: "Partial Fractions — Quadratics and the P8 Correction"
---

## Split the numerator into derivative plus constant

Let $D=x^2+px+q$ be irreducible, so $D>0$ after completing the square. For a numerator $Ax+B$, write
$$
Ax+B=\alpha(2x+p)+\beta,
\qquad \alpha=\frac{A}{2},\quad \beta=B-\frac{Ap}{2}.
$$
Then
$$
\int\frac{Ax+B}{D}dx
=\alpha\ln D+\beta\int\frac{dx}{D}+C.
$$
The remaining integral becomes arctangent after completing the square.

:::diagram
{
  "type": "table",
  "title": "Match the decomposition to the real denominator factor",
  "columns": ["Factor", "Required term", "Integrated shape"],
  "rows": [
    ["x-a", "A/(x-a)", "logarithm"],
    ["(x-a)^k", "terms through power k", "log and reciprocal powers"],
    ["irreducible quadratic", "(Ax+B)/quadratic", "log plus arctangent"],
    ["improper rational", "polynomial division first", "polynomial plus proper part"]
  ],
  "col_widths": [0.27, 0.40, 0.33],
  "caption": "The numerator over an irreducible quadratic must be linear. Splitting it into alpha D' + beta determines exactly when the logarithm term stands alone."
}
:::

:::example title="P8 correction: the remainder beta is zero"
For
$$
I=\int\frac{x+1}{x^2+2x+2}dx,
$$
the denominator's derivative is $2x+2=2(x+1)$. Thus
$$
x+1=\frac{1}{2}(2x+2)+0,
$$
so the complete answer is
$$
I=\frac{1}{2}\ln(x^2+2x+2)+C.
$$
The source adds $\frac{1}{2}\tan^{-1}(x+1)$. That extra term is incorrect: its derivative is
$$
\frac{1}{2}\cdot\frac{1}{(x+1)^2+1}=\frac{1}{2(x^2+2x+2)}\ne0.
$$
Differentiating the corrected answer returns exactly $(x+1)/(x^2+2x+2)$.
:::

:::example title="A nonzero remainder produces both standard shapes"
For $D=x^2+2x+5=(x+1)^2+4$,
$$
3x+5=\frac{3}{2}(2x+2)+2.
$$
Therefore
$$
\int\frac{3x+5}{x^2+2x+5}dx
=\frac{3}{2}\ln(x^2+2x+5)+2\int\frac{dx}{(x+1)^2+4}.
$$
The last integral is $\frac{1}{2}\tan^{-1}((x+1)/2)$, hence
$$
I=\frac{3}{2}\ln(x^2+2x+5)
+\tan^{-1}\frac{x+1}{2}+C.
$$
:::

:::warn title="Check the coefficient split before integrating either piece"
A quick derivative check of the proposed identity $Ax+B=\alpha D'+\beta$ catches a missing remainder immediately. The logarithm and arctangent terms are not interchangeable decorations; their coefficients are forced by that identity.
:::
