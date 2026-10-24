---
id: olympiad-03
part: olympiad
title: "The Gaussian Integral, Scaling and Its Cosine Transform"
---

## S16/Q32: polar coordinates square a one-dimensional integral

Let
$$
I=\int_0^\infty e^{-x^2}dx.
$$
The exponential tail proves convergence, and $I>0$. Therefore
$$
I^2=\int_0^\infty\int_0^\infty e^{-(x^2+y^2)}dx\,dy.
$$
On the first quadrant, polar coordinates give $x^2+y^2=r^2$ and Jacobian $r$:
$$
I^2=\int_0^{\pi/2}\int_0^\infty e^{-r^2}r\,dr\,d\theta
=\frac{\pi}{2}\cdot\frac{1}{2}=\frac{\pi}{4}.
$$
Thus
$$
\int_0^\infty e^{-x^2}dx=\frac{\sqrt{\pi}}{2},
\qquad
\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}.
$$

## P16/Q33 and Q46: scale, shift and complete the square

For $a>0$, $u=\sqrt{a}x$ gives
$$
\int_{-\infty}^{\infty}e^{-ax^2}dx
=\frac{1}{\sqrt{a}}\int_{-\infty}^{\infty}e^{-u^2}du
=\sqrt{\frac{\pi}{a}}.
$$
P16/Q33 is the case $a=2$, with value $\sqrt{\pi/2}$.

For Q46, also complete the square:
$$
-ax^2+bx=-a\left(x-\frac{b}{2a}\right)^2+\frac{b^2}{4a}.
$$
Translation does not change a full-line integral, so
$$
\int_{-\infty}^{\infty}e^{-ax^2+bx}dx
=e^{b^2/(4a)}\sqrt{\frac{\pi}{a}},\qquad a>0.
$$
The exponential factor comes from the completed-square constant; the factor $\sqrt{\pi/a}$ comes from scaling.

## Additional extension: differentiate a cosine parameter

Define
$$
J(a)=\int_0^\infty e^{-x^2}\cos(2ax)dx.
$$
Differentiation under the integral is justified by the integrable dominating function $2xe^{-x^2}$. Hence
$$
J'(a)=-\int_0^\infty2xe^{-x^2}\sin(2ax)dx.
$$
Integration by parts with $d(e^{-x^2})=-2xe^{-x^2}dx$ gives
$$
J'(a)=-2aJ(a),\qquad J(0)=\frac{\sqrt{\pi}}{2}.
$$
Solving yields $J(a)=J(0)e^{-a^2}$. In particular, $J(1)=\sqrt{\pi}/(2e)$, and the full-line cosine transform is $\sqrt{\pi}e^{-a^2}$.

:::diagram
{
  "type": "table",
  "title": "The Gaussian and its transform are positive, exact and checkable",
  "columns": ["Integral", "Method", "Value"],
  "rows": [
    ["S16 / Q32 half-line", "square and use polar coordinates", "sqrt(pi)/2"],
    ["P16 / Q33 with a=2", "scale x by sqrt(a)", "sqrt(pi/2)"],
    ["Q46 with linear term", "complete square, translate and scale", "sqrt(pi/a) exp(b^2/(4a))"],
    ["additional cosine transform", "differentiate then integrate by parts", "sqrt(pi) exp(-a^2)/2"]
  ],
  "col_widths": [0.30, 0.42, 0.28],
  "caption": "The three canonical Gaussian results all follow from the same half-line value. The cosine transform is an additional parameter-differentiation extension."
}
:::

:::warn title="The Jacobian and scaling factors are essential"
Replacing $dx\,dy$ by $dr\,d\theta$ without $r$ would give the wrong polar value. Likewise, $u=\sqrt{a}x$ contributes $1/\sqrt{a}$. Also, $I^2=\pi/4$ determines $|I|$; positivity selects $I=\sqrt{\pi}/2$.
:::
