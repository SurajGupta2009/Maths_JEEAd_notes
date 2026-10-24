---
id: jee-06
part: jee
title: "L'Hôpital's Rule and Indeterminate Forms"
---

## Differentiate only a genuine 0/0 or ∞/∞ quotient

Under the standard differentiability and nonzero-denominator-derivative hypotheses, if $f/g$ has form $0/0$ or $\infty/\infty$ and
$$
\lim_{x\to a}\frac{f'(x)}{g'(x)}
$$
exists finitely or as a signed infinity, then $f/g$ has the same limit. The rule also applies to one-sided limits and limits at infinity. If the derivative ratio still has an indeterminate form, check the hypotheses again before applying the rule another time.

:::example title="Two applications, then a standard limit"
For
$$
\lim_{x\to0}\frac{x-\sin x}{x^3},
$$
the form is $0/0$. Differentiating numerator and denominator gives
$$
\frac{1-\cos x}{3x^2},
$$
still $0/0$. A second application gives
$$
\frac{\sin x}{6x}\longrightarrow\frac{1}{6}.
$$
The repeated differentiation is on numerator and denominator separately; this is not the quotient rule.
:::

:::example title="A negative third-power tangent limit"
For $(x-\tan x)/x^3$, two L'Hôpital steps lead to
$$
\frac{-2\sec^2x\tan x}{6x}
=-\frac{\sec^2x}{3}\cdot\frac{\tan x}{x}
\longrightarrow-\frac{1}{3}.
$$
The last step uses a standard limit rather than another unnecessary differentiation.
:::

## Other indeterminate forms must first become quotients

- For $0\cdot\infty$, write $fg=f/(1/g)$ or $g/(1/f)$.
- For $\infty-\infty$, combine fractions or rationalize.
- For $0^0$, $\infty^0$ and $1^\infty$, take logarithms and evaluate the resulting product.

:::example title="A 0·∞ form and an ∞−∞ form"
As $x\to0^+$,
$$
x\ln x=\frac{\ln x}{1/x}
\quad\Longrightarrow\quad
\frac{1/x}{-1/x^2}=-x\longrightarrow0.
$$
As $x\to\infty$,
$$
\sqrt{x^2+x}-x
=\frac{x}{\sqrt{x^2+x}+x}
=\frac{1}{\sqrt{1+1/x}+1}\longrightarrow\frac{1}{2}.
$$
:::

:::diagram
{
  "type": "flow",
  "title": "Transform the form before choosing the rule",
  "steps": [
    {"title": "Substitute and classify", "detail": "Classify the form before calculating."},
    {"title": "Preserve the domain", "detail": "Check one-sided limits, bases and denominators."},
    {"title": "Transform if necessary", "detail": "Factor, invert, combine or take a logarithm."},
    {"title": "Verify the result", "detail": "Recheck hypotheses; finish with an exact check."}
  ],
  "caption": "L'Hopital is one tool inside a domain-aware strategy, not a substitute for classifying the expression."
}
:::

:::warn title="Not every zero in the numerator is 0/0"
For $\sin x/(x^2+1)$ as $x\to0$, the form is $0/1$, so the limit is simply $0$. For $1/x$ as $x\to0$, the form is $1/0$, not an invitation to differentiate; the two-sided behaviour is unbounded with opposite signs.
:::
