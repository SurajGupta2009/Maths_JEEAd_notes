---
id: jee-05
part: jee
title: "Linear First-Order Equations — Integrating Factors"
---

## Multiply first, then recognize a product derivative

For
$$
y'+P(x)y=Q(x),
$$
choose an integrating factor $\mu=e^{\int P(x)dx}$. Then $\mu'=P\mu$, so
$$
(\mu y)'=\mu Q,
\qquad
y=\frac{1}{\mu}\left(\int\mu Q\,dx+C\right).
$$
Work on an interval where $P$ and $Q$ are continuous. The same $\mu$ works up to a nonzero constant multiple.

:::diagram
{
  "type": "flow",
  "title": "The integrating-factor method is product rule in reverse",
  "steps": [
    {"title": "Standardize", "detail": "Make the coefficient of y-prime equal to one."},
    {"title": "Compute mu", "detail": "Integrate P(x), then exponentiate; no constant is needed in mu."},
    {"title": "Multiply", "detail": "Collapse the left side to the derivative of mu times y."},
    {"title": "Integrate", "detail": "Solve for y, apply the IVP and retain the coefficient domain."}
  ],
  "caption": "Dividing by mu at the end is essential; stopping at mu y leaves the unknown still wrapped."
}
:::

:::example title="S6 and Q12: exponential forcing"
For $y'+y=e^x$, $\mu=e^x$ and
$$
(e^xy)'=e^{2x}
\quad\Longrightarrow\quad
y=\frac{1}{2}e^x+Ce^{-x}.
$$
Since $y(0)=0$, $C=-1/2$. Thus
$$
y=\frac{e^x-e^{-x}}{2}=\sinh x,
\qquad y(1)=\sinh1.
$$
:::

:::example title="S7/Q13 and Q16: polynomial and matching exponential forcing"
For $y'+2y=4x$, $\mu=e^{2x}$. Integration, or the trial $ax+b$, gives
$$
y=2x-1+Ce^{-2x}.
$$
The condition $y(0)=1$ gives $C=2$, so $y(1)=1+2e^{-2}$.

For $y'+2y=e^{-x}$, try $Ae^{-x}$: $(-A+2A)e^{-x}=e^{-x}$, so $A=1$. Hence $y=e^{-x}+Ce^{-2x}$. Since $y(0)=1$, $C=0$ and the IVP solution is simply $y=e^{-x}$ on $(-\infty,\infty)$.
:::

:::example title="P6 and Q14: keep x positive"
For $y'+y/x=x$, the initial point $x=1$ selects $x>0$. Here $\mu=x$ and
$$
(xy)'=x^2
\quad\Longrightarrow\quad
xy=\frac{x^3}{3}+C.
$$
Since $y(1)=0$, $C=-1/3$. Therefore
$$
y=\frac{x^2}{3}-\frac{1}{3x},
\qquad y(2)=\frac{7}{6},
$$
with maximal IVP interval $(0,\infty)$.
:::

:::warn title="Standard form comes before the integrating factor"
If the equation is $a(x)y'+b(x)y=r(x)$, divide by $a(x)$ first on an interval where it does not vanish. Using $b/a$ incorrectly is the most common integrating-factor error.
:::
