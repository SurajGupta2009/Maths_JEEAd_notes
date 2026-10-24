---
id: olympiad-07
part: olympiad
title: "Additional Special Values and Logarithmic Trigonometry"
---

## Two rational tails can be evaluated without numerical approximation

For the first additional rational tail, partial fractions give
$$
\frac{1}{(x^2+1)(x^2+4)}
=\frac{1}{3}\left(\frac{1}{x^2+1}-\frac{1}{x^2+4}\right).
$$
Therefore
$$
\int_0^\infty\frac{dx}{(x^2+1)(x^2+4)}
=\frac{1}{3}\left(\frac{\pi}{2}-\frac{\pi}{4}\right)
=\frac{\pi}{12}.
$$

For the additional quartic tail, let $I=\int_0^\infty dx/(1+x^4)$. Inversion $x\mapsto1/x$ gives $I=\int_0^\infty x^2dx/(1+x^4)$. Hence
$$
2I=\int_0^\infty\frac{1+x^2}{1+x^4}dx.
$$
Divide by $x^2$ and put $u=x-1/x$, so $du=(1+1/x^2)dx$ and $u$ runs from $-\infty$ to $\infty$:
$$
2I=\int_{-\infty}^\infty\frac{du}{u^2+2}=\frac{\pi}{\sqrt{2}},
\qquad I=\frac{\pi}{2\sqrt{2}}.
$$

:::diagram
{
  "type": "graph",
  "title": "Two positive rational tails with exact areas",
  "xrange": [0, 5], "yrange": [0, 1.10],
  "xticks": [0, 1, 2, 3, 4, 5], "yticks": [0, 0.25, 0.5, 0.75, 1],
  "fills": [
    {"from": 0, "to": 5, "y1": 0, "y2": "1/(1+x**4)", "color": "#F6C445", "alpha": 0.25},
    {"from": 0, "to": 5, "y1": 0, "y2": "1/((x**2+1)*(x**2+4))", "color": "#0F6B5C", "alpha": 0.16}
  ],
  "curves": [
    {"expr": "1/(1+x**4)", "from": 0, "to": 5},
    {"expr": "1/((x**2+1)*(x**2+4))", "from": 0, "to": 5, "color": "#B91C1C"}
  ],
  "caption": "The teal curve 1/(1+x^4) has full tail area pi/(2 sqrt(2)); the red curve has full tail area pi/12. Only [0,5] is plotted, while the proofs include the remaining tails."
}
:::

## Log-sine uses reflection and a doubling substitution

For the additional log-sine integral, set
$$
I=\int_0^{\pi/2}\ln\sin x\,dx.
$$
The endpoint singularities are integrable. Reflection gives $I=\int_0^{\pi/2}\ln\cos x\,dx$, so
$$
2I=\int_0^{\pi/2}\ln(\sin x\cos x)dx
=\int_0^{\pi/2}\ln\sin(2x)dx-\frac{\pi}{2}\ln2.
$$
With $u=2x$ and symmetry on $[0,\pi]$,
$$
\int_0^{\pi/2}\ln\sin(2x)dx
=\frac{1}{2}\int_0^\pi\ln\sin u\,du=I.
$$
Thus $2I=I-(\pi/2)\ln2$, and
$$
\int_0^{\pi/2}\ln\sin x\,dx=-\frac{\pi}{2}\ln2.
$$
A log-tangent consequence follows immediately:
$$
\int_0^{\pi/2}\ln\tan x\,dx
=\int_0^{\pi/2}\ln\sin x\,dx-\int_0^{\pi/2}\ln\cos x\,dx=0.
$$

:::warn title="Logarithmic identities require positive inputs inside each interval"
Use $\ln(\sin x\cos x)$ on $(0,\pi/2)$, where both factors are positive, and interpret endpoints through limits. The identity $\ln(ab)=\ln a+\ln b$ is not applied at an endpoint where either logarithm is undefined.
:::
