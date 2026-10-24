---
id: olympiad-04
part: olympiad
title: "Extension IV — Non-Elementary Antiderivatives"
---

## Some antiderivatives require new named functions

An elementary function is built from algebraic, exponential, logarithmic, trigonometric and inverse-trigonometric operations. Liouville's theory shows that several innocent-looking integrands have no antiderivative within that class.

This does **not** say that no antiderivative exists. It says that we must enlarge the function library.

:::diagram
{
  "type": "table",
  "title": "Special functions can be introduced by derivative and normalisation",
  "columns": ["Integrand", "Named antiderivative", "Defining derivative"],
  "rows": [
    ["exp(-x^2)", "(sqrt(pi)/2) erf(x)", "erf'(x)=2 exp(-x^2)/sqrt(pi)"],
    ["sin x / x", "Si(x)", "Si'(x)=sin x/x"],
    ["1 / ln x", "li(x)", "li'(x)=1/ln x"],
    ["exp(x) / x", "Ei(x)", "Ei'(x)=exp(x)/x"]
  ],
  "col_widths": [0.25, 0.34, 0.41],
  "caption": "Together with erf(0)=0 and Si(0)=0, the first two derivatives determine smooth special functions. The logarithmic and exponential integrals require domain branches around their singularities."
}
:::

For example,
$$
\int e^{-x^2}dx=\frac{\sqrt{\pi}}{2}\,\mathrm{erf}(x)+C,
\qquad
\mathrm{erf}'(x)=\frac{2}{\sqrt{\pi}}e^{-x^2}.
$$
Similarly, after assigning the continuous value $1$ to $\sin x/x$ at $x=0$,
$$
\int\frac{\sin x}{x}dx=\mathrm{Si}(x)+C,
\qquad \mathrm{Si}(0)=0.
$$
These statements are verified by the same principle as every other antiderivative: differentiate the named function.

## The frontier is about representation, not computational failure

The source's Gaussian S16/Q32/Q46 and Dirichlet Q37 questions concern **definite** values. Chapter 21 will show that some of those values are exact even though no elementary antiderivative is available. A definite symmetry or double-integral method can succeed where an elementary formula for $F(x)$ does not exist.

:::warn title="Never write 'the integral does not exist' merely because the usual methods fail"
The precise statement is “there is no elementary antiderivative.” Numerical approximation, a special function, a convergent series or an exact definite-integral technique may still be available. Conversely, quoting a special-function name without its derivative and domain is not a verification.
:::
