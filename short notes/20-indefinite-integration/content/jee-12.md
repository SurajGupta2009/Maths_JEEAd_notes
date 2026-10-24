---
id: jee-12
part: jee
title: "Method Selection, Equivalent Answers and Final Verification"
---

## Diagnose the structure before calculating

The fastest method is usually the one exposed by preparation. Do not begin with a favourite technique and force the integrand to fit it.

:::diagram
{
  "type": "table",
  "title": "A compact method-selection map",
  "columns": ["Visible structure", "First method", "Decisive check"],
  "rows": [
    ["polynomial or basic library", "reverse derivative", "power and scale"],
    ["f(g(x)) g'(x)", "u=g(x)", "du is complete"],
    ["g'(x)/g(x)", "log substitution", "g is nonzero"],
    ["sum or difference of squares", "standard form", "complete square first"],
    ["polynomial times e^x or trig", "by parts", "du gets simpler"],
    ["log or inverse trig factor", "by parts with dv=dx", "new integral is easier"],
    ["rational function", "division and partial fractions", "factor multiplicities"],
    ["rational sin and cos", "half-angle substitution", "branch and dx factor"]
  ],
  "col_widths": [0.33, 0.34, 0.33],
  "caption": "Preparation can move an integrand from one row to another. If a calculation grows without creating a standard form, stop and reassess the structure."
}
:::

## Three short choices show the difference

:::example title="Substitution, parts and preparation are not interchangeable"
For $\int xe^{x^2}dx$, the factor $x$ helps create $du=2x\,dx$:
$$
\int xe^{x^2}dx=\frac{1}{2}e^{x^2}+C.
$$
For $\int xe^x dx$, there is no inner $x^2$; by parts gives
$$
\int xe^x dx=e^x(x-1)+C.
$$
For $\int(x^{1/2}+x^{-1/2})dx$, no advanced method is needed:
$$
\int(x^{1/2}+x^{-1/2})dx=\frac{2}{3}x^{3/2}+2x^{1/2}+C.
$$
:::

## Verification is a mathematical step, not a courtesy

A complete check has four parts:

1. Differentiate the proposed antiderivative and simplify to the **original** integrand.
2. Confirm the inner scale, signs and partial-fraction coefficients.
3. State an interval on which both integrand and antiderivative are defined.
4. If two answers look different, test whether their difference is constant on that interval.

For example, the three answers to $\int\sin x\cos x\,dx$ in `jee-04.md` differ by $0$, $-1/2$ or $-1/4$ when written relative to $\frac{1}{2}\sin^2x$. Their equality up to $C$ is therefore proved, not inferred from similar graphs.

:::warn title="A value check at one point is not enough"
Two different functions can agree at one point. Differentiation checks the whole relationship at once. Conversely, if $G'=f$ but the domain has been ignored, the calculation is still incomplete: singularities and disconnected branches remain part of the answer.
:::
