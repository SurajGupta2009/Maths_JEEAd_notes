---
id: jee-09
part: jee
title: "Inversion and Absolute versus Conditional Convergence"
---

## Establish convergence before using a symmetry argument

For P15 and Q31, let
$$
I=\int_0^\infty\frac{\ln x}{1+x^2}dx.
$$
Near $0$, $|\ln x|$ is integrable; near $\infty$, $|\ln x|/(1+x^2)=O(\ln x/x^2)$ is integrable. Thus the integral converges absolutely on both ends.

Now put $x=1/u$. Then $dx=-du/u^2$, $\ln x=-\ln u$, and the endpoints interchange. After simplifying,
$$
I=\int_\infty^0\frac{\ln u}{1+u^2}du=-I.
$$
Therefore $2I=0$ and $I=0$. The inversion is legitimate because convergence was checked first.

:::diagram
{
  "type": "flow",
  "title": "An improper symmetry argument has a convergence gate",
  "steps": [
    {"title": "Check both ends", "detail": "Use endpoint estimates or comparison before manipulating the integral."},
    {"title": "Substitute carefully", "detail": "Track dx, signs and the reversed infinite limits."},
    {"title": "Combine the forms", "detail": "Use I=-I or another relation only after convergence is known."},
    {"title": "Classify", "detail": "Distinguish absolute, conditional and principal-value convergence."}
  ],
  "caption": "For ln(x)/(1+x^2), inversion gives I=-I. The conclusion I=0 uses the fact that I is a finite number."
}
:::

## Three different meanings must not be confused

An integral $\int_I f$ converges **absolutely** when $\int_I|f|$ is finite. It converges **conditionally** when it converges but the absolute integral diverges. The Dirichlet integral in Extension VII is conditionally convergent.

A symmetric limit can define a Cauchy principal value without making the ordinary integral convergent. For example,
$$
\int_{-R}^{R}\frac{x}{1+x^2}dx=0
$$
by oddness, yet
$$
\int_0^R\frac{x}{1+x^2}dx=\frac{1}{2}\ln(1+R^2)\to\infty.
$$
The two-sided improper integral therefore diverges even though its symmetric principal value is zero.

:::warn title="I=-I is useful only for a finite I"
If $I$ were infinite or undefined, subtracting it from itself would be meaningless. Convergence is not a technical footnote; it is what permits the algebraic step.
:::
