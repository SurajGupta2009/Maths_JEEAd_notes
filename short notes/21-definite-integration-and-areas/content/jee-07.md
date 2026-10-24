---
id: jee-07
part: jee
title: "Improper Integrals I — Infinite Intervals"
---

## An infinite upper limit is always a limit of finite integrals

By definition,
$$
\int_a^\infty f(x)dx=\lim_{R\to\infty}\int_a^R f(x)dx,
$$
when that limit is finite. The symbol $\infty$ is not an endpoint at which an antiderivative can simply be evaluated without a limit.

:::example title="P12 and Q27: an exponential tail has finite area"
$$
\int_0^R e^{-x}dx=1-e^{-R}.
$$
As $R\to\infty$, $e^{-R}\to0$, so
$$
\int_0^\infty e^{-x}dx=1.
$$
The visual lab separates the finite part on $[0,2]$ from the remaining tail of size $e^{-2}$.
:::

## The p-integrals give a fundamental comparison scale

For $p\ne1$,
$$
\int_1^R x^{-p}dx=\frac{R^{1-p}-1}{1-p}.
$$
Consequently, for $p>1$,
$$
\int_1^\infty\frac{dx}{x^p}=\frac{1}{p-1}.
$$
For $p\leq1$, the integral diverges. At $p=1$, the finite value is $\ln R$, which diverges. The antiderivative formula and the limit must agree.

:::diagram
{
  "type": "table",
  "title": "Infinite-interval convergence is decided by the tail",
  "columns": ["Integrand or test", "Conclusion", "Reason"],
  "rows": [
    ["1/x^p, p>1", "converges to 1/(p-1)", "negative exponent of R vanishes"],
    ["1/x", "diverges", "ln R grows without bound"],
    ["1/x^p, p<1", "diverges", "positive power of R grows"],
    ["exp(-x)", "converges to 1", "exp(-R) vanishes"],
    ["0<=f<=g", "convergence of g forces f", "comparison for nonnegative tails"]
  ],
  "col_widths": [0.28, 0.34, 0.38],
  "caption": "Comparison tests require the stated sign and a common tail interval. A finite graph on a large finite window is not itself a proof of convergence."
}
:::

:::example title="Comparison can precede an exact evaluation"
For $x\geq1$, $0<1/(1+x^2)\leq1/x^2$. Convergence follows by comparison, and FTC gives the exact value
$$
\int_1^\infty\frac{dx}{1+x^2}
=\lim_{R\to\infty}(\tan^{-1}R-\tan^{-1}1)
=\frac{\pi}{4}.
$$
:::

:::warn title="A finite value at every R does not imply a finite limit"
The number $\ln R$ is finite for each finite $R$, yet grows without bound. Always take the final limit. Also, signed cancellation over expanding intervals does not prove absolute convergence.
:::
