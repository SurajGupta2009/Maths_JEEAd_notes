---
id: jee-05
part: jee
title: "Inverse-Trigonometric Standard Forms"
---

## Recognise a sum of squares or a square-root difference

For $a>0$, direct differentiation gives
$$
\int\frac{dx}{x^2+a^2}
=\frac{1}{a}\tan^{-1}\frac{x}{a}+C,
\qquad
\int\frac{dx}{\sqrt{a^2-x^2}}
=\sin^{-1}\frac{x}{a}+C,
$$
the second on $-a<x<a$. Thus
$$
\int\frac{dx}{x^2+4}=\frac{1}{2}\tan^{-1}\frac{x}{2}+C,
\qquad
\int\frac{dx}{\sqrt{4-x^2}}=\sin^{-1}\frac{x}{2}+C.
$$
The source's definite Q10–Q12 use these same antiderivatives before their limits are applied in Chapter 21.

:::example title="Complete the square before using arctangent"
For S5,
$$
x^2+2x+2=(x+1)^2+1.
$$
With $u=x+1$ and $du=dx$,
$$
\int\frac{dx}{x^2+2x+2}
=\int\frac{du}{u^2+1}
=\tan^{-1}(x+1)+C.
$$
:::

:::diagram
{
  "type": "graph",
  "title": "Arctangent has derivative 1/(1+x^2)",
  "xrange": [-3, 3], "yrange": [-1.5, 1.5],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-1, 0, 1],
  "curves": [
    {"expr": "1/(1+x**2)", "from": -3, "to": 3, "color": "#B91C1C"},
    {"expr": "arctan(x)", "from": -3, "to": 3}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "F(0)=0", "dx": 0.15, "dy": 0.18},
    {"x": 1, "y": 0.7853981634, "label": "F(1)=pi/4", "dx": 0.18, "dy": 0.18}
  ],
  "caption": "The teal curve is F(x)=arctan(x); the red curve is f(x)=1/(1+x^2). The slope of F at x=0 is 1 and at x=1 is 1/2: red gives height, teal gives the antiderivative."
}
:::

## Scaling must be handled before quoting the formula

:::example title="Extract the coefficient of x squared"
$$
\int\frac{dx}{4x^2+9}
=\frac{1}{4}\int\frac{dx}{x^2+9/4}
=\frac{1}{6}\tan^{-1}\frac{2x}{3}+C.
$$
Differentiating the last expression returns $1/(4x^2+9)$, including the factor $1/6$.
:::

:::warn title="Inverse notation is not reciprocal notation"
Here $\tan^{-1}u$ and $\sin^{-1}u$ mean $\arctan u$ and $\arcsin u$, not $1/\tan u$ or $1/\sin u$. Also, the arcsin formula requires $a>0$ and $|x|<a$; it is not valid at an arbitrary complex or outside-domain input.
:::
