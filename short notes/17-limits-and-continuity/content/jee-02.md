---
id: jee-02
part: jee
title: "Algebraic Limits — Laws, Factoring and Rationalising"
---

## Limit laws work after existence is known

If $f(x)\to L$ and $g(x)\to M$ with finite $L,M$, then sums, differences, products and constant multiples pass through the limit. If $M\ne0$, then
$$
\frac{f(x)}{g(x)}\to\frac{L}{M}.
$$
For a product, the proof uses
$$
|fg-LM|\leq |f||g-M|+|M||f-L|.
$$
A convergent $f$ is locally bounded, so both terms can be made small. The quotient law requires the denominator's limit to be nonzero; it says nothing about a $0/0$ expression.

## Factor out the cause of 0/0

Substitution gives $0/0$ only when both numerator and denominator vanish. Factor their common zero, cancel on a punctured neighbourhood, and then use the limit laws.

:::example title="A cubic and quadratic sharing a zero"
For $x\ne1$,
$$
\frac{x^3-1}{x^2-1}
=\frac{(x-1)(x^2+x+1)}{(x-1)(x+1)}
=\frac{x^2+x+1}{x+1}.
$$
Hence the limit as $x\to1$ is $3/2$. More generally, for integer $n\geq1$,
$$
\frac{x^n-1}{x-1}=x^{n-1}+x^{n-2}+\cdots+x+1\longrightarrow n.
$$
The right-hand sum has exactly $n$ terms, each tending to $1$.
:::

:::diagram
{
  "type": "graph",
  "title": "The hole at (2,4) does not stop the limit",
  "xrange": [0, 4], "yrange": [1, 7],
  "curves": [
    {"expr": "x+2", "from": 0, "to": 1.97, "label": "y = x+2, x != 2", "labpos": 0.50, "label_dy": 0.35},
    {"expr": "x+2", "from": 2.03, "to": 4}
  ],
  "points": [{"x": 2, "y": 4, "label": "open hole (2,4)", "face": "white", "color": "#B91C1C", "dx": 0.18, "dy": 0.25}],
  "caption": "The original quotient (x^2-4)/(x-2) is undefined at 2 but equals x+2 everywhere nearby. Both one-sided approaches point to height 4."
}
:::

## Conjugates turn radical 0/0 into ordinary algebra

:::example title="Rationalise, cancel, then substitute"
For $x\ne0$,
$$
\frac{\sqrt{1+x}-1}{x}
=\frac{(1+x)-1}{x(\sqrt{1+x}+1)}
=\frac{1}{\sqrt{1+x}+1}
\longrightarrow\frac{1}{2}.
$$
Similarly, as $x\to4$,
$$
\frac{\sqrt{x}-2}{x-4}
=\frac{1}{\sqrt{x}+2}\longrightarrow\frac{1}{4}.
$$
The conjugate removes the radical from the numerator without changing the expression on the permitted domain.
:::

:::example title="A direct calculation is enough when no form is indeterminate"
For $\lim_{x\to2}(5x-3)$, ordinary arithmetic gives $7$. For $\lim_{x\to0}(x^2-3x)/x$, cancel $x$ on $x\ne0$ to obtain $x-3\to-3$. L'Hôpital's rule is unnecessary in both cases.
:::

:::key title="Preserve the punctured-domain statement"
Write “for $x\ne a$” beside a cancellation. The simplified formula determines the limit, but it does not restore a value or change the original function's domain. This distinction becomes the definition of a removable discontinuity later.
:::
