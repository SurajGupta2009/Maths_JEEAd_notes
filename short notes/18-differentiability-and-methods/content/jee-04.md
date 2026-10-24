---
id: jee-04
part: jee
title: "The Chain Rule and Standard Functions"
---

## Differentiate the outer function, then multiply by the inner rate

If $g$ is differentiable at $x$ and $f$ is differentiable at $u=g(x)$, then
$$
\frac{d}{dx}f(g(x))=f'(g(x))g'(x).
$$
A proof that also covers repeated zero inner increments writes $k=g(x+h)-g(x)$ and
$$
f(u+k)-f(u)=(f'(u)+\varepsilon(k))k,
\qquad \varepsilon(k)\to0\text{ as }k\to0.
$$
Since $k/h\to g'(x)$, division by $h$ and passage to the limit give the chain rule without assuming $k\ne0$ at every step.

## Standard derivatives supply the outer rates

$$
(\sin x)'=\cos x,\qquad(\cos x)'=-\sin x,
\qquad(e^x)'=e^x,\qquad(\ln x)'=\frac{1}{x}\quad(x>0).
$$
For example, the sine formula follows by expanding $\sin(x+h)$ and using $\sin h/h\to1$ and $(\cos h-1)/h\to0$. The logarithm formula follows from $\ln(1+h/x)\sim h/x$.

:::example title="Name the outer and inner functions explicitly"
$$
\frac{d}{dx}\sin(3x^2)=6x\cos(3x^2),
\qquad
\frac{d}{dx}e^{x^2}=2xe^{x^2},
$$
and
$$
\frac{d}{dx}\cos(x^3)=-3x^2\sin(x^3).
$$
Where $\sin x>0$,
$$
\frac{d}{dx}\ln(\sin x)=\frac{\cos x}{\sin x}=\cot x.
$$
The derivative $\cot x$ is not claimed at zeros of $\sin x$, where the original logarithm is undefined.
:::

:::diagram
{
  "type": "flow",
  "title": "A reliable chain-rule workflow",
  "steps": [
    {"title": "Write the composition", "detail": "Identify outer f(u) and inner u=g(x)."},
    {"title": "Differentiate each layer", "detail": "Compute f'(u) and g'(x) separately."},
    {"title": "Substitute and multiply", "detail": "Form f'(g(x)) times g'(x)."},
    {"title": "Check domain and scale", "detail": "Retain restrictions; test one numerical slope."}
  ],
  "caption": "The outer derivative keeps the inner input unchanged. Only after evaluating that outer rate do you multiply by the inner derivative."
}
:::

:::warn title="Do not multiply by a missing inner derivative"
The derivative of $\sin(3x)$ is $3\cos(3x)$, not $\cos(3x)$. Conversely, the derivative of $\sin x$ has no extra factor. A useful check at $0$ is that $\sin(3h)/(3h)\to1$, so the slope of $\sin(3x)$ at $0$ is $3$.
:::
