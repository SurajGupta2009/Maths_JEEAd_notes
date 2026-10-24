---
id: jee-02
part: jee
title: "Substitution — Reverse the Chain Rule"
---

## Look for an inner expression and its derivative

From $(F(g(x)))'=F'(g(x))g'(x)$, we obtain
$$
\int f(g(x))g'(x)\,dx=\int f(u)\,du,
\qquad u=g(x),\quad du=g'(x)dx.
$$
Substitution is not a guess followed by hope: the factor accompanying $dx$ must account for $du$, up to a constant that can be moved outside the integral.

:::diagram
{
  "type": "flow",
  "title": "A substitution audit prevents a missing scale factor",
  "steps": [
    {"title": "Choose the inner u", "detail": "Pick the expression inside a power, exponential or logarithm."},
    {"title": "Compute du", "detail": "Differentiate u and compare du with the remaining factors."},
    {"title": "Integrate in u", "detail": "Use a standard form only after the conversion is complete."},
    {"title": "Return and check", "detail": "Replace u by g(x), restore +C and differentiate."}
  ],
  "caption": "A constant multiplier can be repaired. A missing nonconstant factor usually means that another method or another substitution is needed."
}
:::

:::example title="The derivative factor is already present"
For
$$
I=\int2x(x^2+1)^5\,dx,
$$
put $u=x^2+1$, so $du=2x\,dx$. Then $I=\int u^5du=(x^2+1)^6/6+C$.

Likewise, with $u=x^2+3$,
$$
\int2x(x^2+3)^4\,dx=\frac{(x^2+3)^5}{5}+C.
$$
:::

:::example title="A constant factor of one-half is enough"
For $\int xe^{x^2}dx$, put $u=x^2$, so $du=2x\,dx$ and $x\,dx=du/2$. Hence
$$
\int xe^{x^2}dx=\frac{1}{2}\int e^u du
=\frac{1}{2}e^{x^2}+C.
$$
The same antiderivative is used in the source's definite questions P4 and Q7; their limits and numerical evaluation belong to Chapter 21.
:::

## Linear inner functions have a predictable scale

If $F'=f$ and $a\ne0$, then
$$
\int f(ax+b)\,dx=\frac{1}{a}F(ax+b)+C.
$$
For example,
$$
\int\cos(3x-1)dx=\frac{1}{3}\sin(3x-1)+C,
\qquad
\int(2x+1)^4dx=\frac{(2x+1)^5}{10}+C.
$$

:::warn title="Do not invent the derivative factor"
For $\int x(x^2+1)^5dx$, the missing factor is only a constant $2$, so substitution works with $x\,dx=du/2$. For $\int(x^2+1)^5dx$, the needed factor $2x$ is absent and cannot be created as a constant multiplier.
:::
