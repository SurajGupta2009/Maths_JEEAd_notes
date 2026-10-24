---
id: jee-07
part: jee
title: "Integration by Parts — Polynomial, Logarithm and Inverse"
---

## Integrate the product rule instead of guessing a product rule

From $(uv)'=u'v+uv'$, we obtain
$$
\int u\,dv=uv-\int v\,du.
$$
A successful choice makes $\int v\,du$ simpler than $\int u\,dv$. LIATE is a useful default: choose $u$ from Logarithm, Inverse trigonometric, Algebraic, Trigonometric, Exponential, in that order.

:::diagram
{
  "type": "flow",
  "title": "By parts transfers difficulty from u to du",
  "steps": [
    {"title": "Choose u and dv", "detail": "Use LIATE as a guide, while checking that dv is easy to integrate."},
    {"title": "Compute du and v", "detail": "Differentiate u and integrate dv without adding a second constant."},
    {"title": "Form uv minus integral", "detail": "Keep the minus sign and all factors in the remaining integral."},
    {"title": "Finish and verify", "detail": "Repeat if useful, add +C once, then differentiate the answer."}
  ],
  "caption": "The method succeeds when du is simpler or the remaining integral has a known recurrence. Reversing a good choice often makes the problem harder."
}
:::

:::example title="One application removes the polynomial factor"
For S6 and Q14, choose $u=x$ and $dv=e^xdx$. Then $du=dx$ and $v=e^x$:
$$
\int xe^xdx=xe^x-\int e^xdx=e^x(x-1)+C.
$$
:::

:::example title="A lone logarithm still has a product structure"
For S7 and Q15 on $x>0$, take $u=\ln x$ and $dv=dx$:
$$
\int\ln x\,dx=x\ln x-\int x\cdot\frac{1}{x}\,dx
=x\ln x-x+C.
$$
:::

## Repeated parts can be organised as a polynomial recurrence

For P6 and Q16,
$$
\int x^2e^xdx=x^2e^x-2\int xe^xdx
=x^2e^x-2e^x(x-1)+C.
$$
Therefore
$$
\int x^2e^xdx=e^x(x^2-2x+2)+C.
$$
Differentiation gives $e^x(x^2-2x+2)+e^x(2x-2)=x^2e^x$.

:::example title="Inverse trigonometric functions also benefit from dv=dx"
$$
\int\tan^{-1}x\,dx
=x\tan^{-1}x-\int\frac{x}{1+x^2}dx
=x\tan^{-1}x-\frac{1}{2}\ln(1+x^2)+C.
$$
:::

:::warn title="Do not add independent constants at every by-parts step"
A constant chosen for $v$ can be absorbed into the remaining calculation. Write one final $+C$ for the complete antiderivative, and check that no intermediate constant has changed the intended recurrence.
:::
