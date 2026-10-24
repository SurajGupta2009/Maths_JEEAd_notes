---
id: jee-03
part: jee
title: "Definite Substitution — Change the Limits"
---

## Either transform the limits or return to x before evaluating

When $u=g(x)$ is used in a definite integral, the endpoints become $g(a)$ and $g(b)$:
$$
\int_a^b f(g(x))g'(x)dx=\int_{g(a)}^{g(b)}f(u)du.
$$
The substitution must be valid on the integration interval; monotonicity is a convenient sufficient condition but is not the only possible justification.

:::diagram
{
  "type": "flow",
  "title": "A definite substitution changes the whole problem",
  "steps": [
    {"title": "Choose u", "detail": "Identify the inner expression and compute du completely."},
    {"title": "Convert endpoints", "detail": "Replace x=a,b by u=g(a),g(b), including their order."},
    {"title": "Integrate in u", "detail": "Evaluate the new definite integral without returning to x."},
    {"title": "Check interval", "detail": "Confirm no singular point was crossed and verify numerically if useful."}
  ],
  "caption": "Alternatively, find an x-antiderivative and use the original endpoints. Do not mix u-limits with an x-antiderivative."
}
:::

:::example title="P4 and Q7: an exponential substitution"
For $u=x^2$, $du=2x\,dx$, and $x=0,1$ become $u=0,1$:
$$
\int_0^1 2xe^{x^2}dx=\int_0^1e^u du=e-1.
$$
The numerical value is $1.718281828\ldots$.
:::

:::example title="P5 and Q11: complete the square and translate both endpoints"
Since $x^2+2x+2=(x+1)^2+1$, put $u=x+1$. The limits $0,1$ become $1,2$:
$$
\int_0^1\frac{dx}{x^2+2x+2}
=\int_1^2\frac{du}{u^2+1}
=\tan^{-1}(2)-\frac{\pi}{4}.
$$
This is approximately $0.3217505544$.
:::

## Two standard-form evaluations

For Q10 and Q12,
$$
\int_0^1\frac{dx}{1+x^2}=\tan^{-1}(1)-\tan^{-1}(0)=\frac{\pi}{4},
$$
$$
\int_0^1\frac{dx}{\sqrt{4-x^2}}
=\left[\sin^{-1}\frac{x}{2}\right]_0^1=\frac{\pi}{6}.
$$
The second integrand is continuous on $[0,1]$, so no improper endpoint issue arises.

:::warn title="Reversed u-limits carry a sign"
If $g(a)>g(b)$, keep that order. Reversing the new limits changes the sign. Also, an antiderivative cannot be used across an interior singularity of the original integrand.
:::
