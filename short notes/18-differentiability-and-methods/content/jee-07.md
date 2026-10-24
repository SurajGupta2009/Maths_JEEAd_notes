---
id: jee-07
part: jee
title: "Logarithmic Differentiation"
---

## Turn products, quotients and variable powers into sums

If $y>0$ and $y$ is differentiable, then $(\ln y)'=y'/y$. Thus logarithmic differentiation is the chain rule applied before multiplying back by $y$. It is ideal for $u(x)^{v(x)}$ and long products.

For a variable power with $u(x)>0$,
$$
y=u^v
\quad\Longrightarrow\quad
\ln y=v\ln u
\quad\Longrightarrow\quad
\frac{y'}{y}=v'\ln u+v\frac{u'}{u}.
$$

:::example title="Differentiate x^x without treating either x as constant"
For $x>0$ and $y=x^x$,
$$
\ln y=x\ln x
\quad\Longrightarrow\quad
\frac{y'}{y}=\ln x+1.
$$
Therefore
$$
y'=x^x(1+\ln x),\qquad y'(1)=1.
$$
Neither the constant-base power rule nor the constant-exponent rule applies to $x^x$ by itself.
:::

:::example title="Logarithms compress a product and a radical denominator"
For an interval on which
$$
y=\frac{x^2\sin x}{\sqrt{1+x}}
$$
is positive, logarithmic differentiation gives
$$
\frac{y'}{y}=\frac{2}{x}+\cot x-\frac{1}{2(1+x)}.
$$
Multiply by the original $y$ at the end. On intervals where a nonzero product changes sign, use $\ln|y|$ and track each factor's domain instead of assuming positivity.
:::

## The same idea proves the real-power rule

For $x>0$ and fixed real $r$, write $y=x^r=e^{r\ln x}$. Then
$$
y'=e^{r\ln x}\frac{r}{x}=rx^{r-1}.
$$
At other points, use the domain of the particular real power rather than extending this proof blindly.

:::diagram
{
  "type": "flow",
  "title": "Logarithmic differentiation preserves a four-step chain",
  "steps": [
    {"title": "Check the log domain", "detail": "Use positive bases; use ln|y| for nonzero products."},
    {"title": "Take logarithms", "detail": "Convert powers, products and quotients to sums."},
    {"title": "Differentiate both sides", "detail": "The left side becomes y'/y."},
    {"title": "Multiply back by y", "detail": "Use the original formula and test one value."}
  ],
  "caption": "Dropping the final factor y is the most common algebraic slip. The computed quantity before that step is the relative rate y'/y."
}
:::

:::warn title="Real variable powers need a positive base"
The proof of $(u^v)'=u^v(v'\ln u+vu'/u)$ requires $u>0$ near the point. A negative or zero base needs a separate definition and cannot be substituted into $\ln u$.
:::
