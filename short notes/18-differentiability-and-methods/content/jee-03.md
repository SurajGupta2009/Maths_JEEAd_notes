---
id: jee-03
part: jee
title: "The Algebra of Derivatives"
---

## Linearity and the product rule come from the definition

Limit laws give $(af+bg)'=af'+bg'$. For a product, add and subtract $f(x+h)g(x)$:
$$
\frac{f(x+h)g(x+h)-f(x)g(x)}{h}
=\frac{f(x+h)-f(x)}{h} g(x)
+f(x+h)\frac{g(x+h)-g(x)}{h}.
$$
Taking $h\to0$ proves
$$
(fg)'=f'g+fg'.
$$
The second term uses continuity of $f$, which follows from its differentiability.

:::example title="Products with exact evaluations"
For $x^2\sin x$,
$$
(x^2\sin x)'=2x\sin x+x^2\cos x.
$$
For $x^3\sin x$, the derivative is $3x^2\sin x+x^3\cos x$, so at $\pi/2$ it is $3\pi^2/4$. Also $(xe^x)'=e^x(1+x)$, whose value at $0$ is $1$.
:::

## Quotient and power rules need their domains

For $g(x)\ne0$,
$$
\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}.
$$
The power rule $(x^n)'=nx^{n-1}$ follows for positive integers by the binomial difference quotient or induction. Logarithmic differentiation later supplies the real-power version on the appropriate domain.

:::example title="Two quotient calculations"
$$
\left(\frac{x}{1+x^2}\right)'
=\frac{1-x^2}{(1+x^2)^2},
\qquad
\left(\frac{x^2}{x+1}\right)'
=\frac{x^2+2x}{(x+1)^2}\quad(x\ne-1).
$$
For $x>0$,
$$
\left(x^5-3x^{1/2}+7\right)'
=5x^4-\frac{3}{2\sqrt{x}}.
$$
:::

:::diagram
{
  "type": "table",
  "title": "Choose the algebra rule and retain its hypothesis",
  "columns": ["Expression", "Derivative rule", "Essential condition"],
  "rows": [
    ["a f + b g", "a f' + b g'", "both derivatives exist"],
    ["f g", "f'g + fg'", "both derivatives exist"],
    ["f / g", "(f'g - fg')/g^2", "g(x) is nonzero"],
    ["x^n", "n x^(n-1)", "use the valid power domain"],
    ["1 / x", "-1/x^2", "x is nonzero"]
  ],
  "col_widths": [0.24, 0.38, 0.38],
  "caption": "The quotient rule is not (f'/g'). Differentiate the numerator and denominator in the correct order and square the original denominator."
}
:::

:::warn title="Simplification can expose a domain restriction"
Although
$$
\frac{x^2}{x+1}=x-1+\frac{1}{x+1}\qquad(x\ne-1),
$$
differentiating the simplified form still gives a derivative only on the original domain. Algebraic cancellation or division never restores the excluded point.
:::
