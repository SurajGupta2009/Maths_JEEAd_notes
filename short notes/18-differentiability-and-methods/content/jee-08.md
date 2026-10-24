---
id: jee-08
part: jee
title: "Parametric Differentiation"
---

## Divide rates with respect to the same parameter

If $x=x(t)$, $y=y(t)$ and $dx/dt\ne0$, then
$$
\frac{dy}{dx}=\frac{dy/dt}{dx/dt}.
$$
For a second derivative, differentiate the **first derivative with respect to t**, then divide by $dx/dt$ again:
$$
\frac{d^2y}{dx^2}
=\frac{\dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)}{dx/dt}.
$$
It is generally wrong to compute $y''(t)/x''(t)$.

:::example title="A cubic parameter gives both derivatives exactly"
For $x=t^2$, $y=t^3$ and $t\ne0$,
$$
\frac{dy}{dx}=\frac{3t^2}{2t}=\frac{3t}{2}.
$$
Thus the slope at $t=2$ is $3$, and
$$
\frac{d^2y}{dx^2}=\frac{3/2}{2t}=\frac{3}{4t},
$$
whose value at $t=1$ is $3/4$.
:::

:::example title="An ellipse parameter retains a trigonometric slope"
For $x=a\cos t$, $y=b\sin t$ with $a,b\ne0$ and $\sin t\ne0$,
$$
\frac{dy}{dx}=\frac{b\cos t}{-a\sin t}=-\frac{b}{a}\cot t.
$$
At parameter values where $dx/dt=0$, investigate a vertical tangent or another parametrization instead of cancelling $0/0$.
:::

:::diagram
{
  "type": "flow",
  "title": "Parametric derivatives alternate between t and x",
  "steps": [
    {"title": "Compute parameter rates", "detail": "Find dx/dt and dy/dt; note where dx/dt=0."},
    {"title": "Form the first slope", "detail": "Divide dy/dt by dx/dt on the valid interval."},
    {"title": "Differentiate that slope in t", "detail": "For second order, apply d/dt to dy/dx."},
    {"title": "Divide by dx/dt again", "detail": "This final division converts the t-rate back to x."}
  ],
  "caption": "The derivative dy/dx is a function of the parameter. A second x-derivative therefore needs one more parameter derivative and one more division by dx/dt."
}
:::

:::warn title="A zero parameter rate needs a separate limiting analysis"
At $t=0$ for $x=t^2$, $y=t^3$, the displayed ratio is $0/0$. The simplified slope $3t/2$ still has limit $0$, but this is a conclusion from taking a limit, not from substituting into the original quotient.
:::
