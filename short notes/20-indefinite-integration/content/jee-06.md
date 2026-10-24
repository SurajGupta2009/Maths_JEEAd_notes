---
id: jee-06
part: jee
title: "Difference-of-Squares and Radical Standard Forms"
---

## Logarithms and inverse trigonometry come from the denominator's shape

For $a>0$, on an interval avoiding singularities,
$$
\int\frac{dx}{x^2-a^2}
=\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|+C,
$$
$$
\int\frac{dx}{a^2-x^2}
=\frac{1}{2a}\ln\left|\frac{a+x}{a-x}\right|+C.
$$
The first is Q21. Its partial-fraction derivation is
$$
\frac{1}{x^2-a^2}
=\frac{1}{2a}\left(\frac{1}{x-a}-\frac{1}{x+a}\right).
$$

:::diagram
{
  "type": "table",
  "title": "Three radical denominators have logarithmic antiderivatives",
  "columns": ["Integrand", "Antiderivative", "Domain interval"],
  "rows": [
    ["1/sqrt(x^2+a^2)", "ln(x+sqrt(x^2+a^2))", "all real x"],
    ["1/sqrt(x^2-a^2)", "ln|x+sqrt(x^2-a^2)|", "x>a or x<-a"],
    ["1/sqrt(a^2-x^2)", "arcsin(x/a)", "-a<x<a"]
  ],
  "col_widths": [0.29, 0.46, 0.25],
  "caption": "The first two formulas can be checked by differentiating the radical and simplifying. On a disconnected domain, treat each interval separately."
}
:::

## A radical in the numerator may need a trigonometric substitution

For $-a<x<a$, put $x=a\sin\theta$ with $-\pi/2<\theta<\pi/2$. Then $dx=a\cos\theta\,d\theta$ and $\sqrt{a^2-x^2}=a\cos\theta$, so
$$
\int\sqrt{a^2-x^2}\,dx
=a^2\int\cos^2\theta\,d\theta
=\frac{a^2}{2}(\theta+\sin\theta\cos\theta)+C.
$$
Returning to $x$ gives
$$
\int\sqrt{a^2-x^2}\,dx
=\frac{x}{2}\sqrt{a^2-x^2}
+\frac{a^2}{2}\sin^{-1}\frac{x}{a}+C.
$$

:::diagram
{
  "type": "graph",
  "title": "The semicircle is the derivative of its antiderivative",
  "xrange": [-2.2, 2.2], "yrange": [-3.5, 3.5],
  "xticks": [-2, -1, 0, 1, 2], "yticks": [-3, -2, -1, 0, 1, 2, 3],
  "curves": [
    {"expr": "sqrt(4-x**2)", "from": -2, "to": 2, "color": "#B91C1C"},
    {"expr": "x/2*sqrt(4-x**2)+2*arcsin(x/2)", "from": -2, "to": 2}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "F(0)=0", "dx": 0.12, "dy": 0.22},
    {"x": 1, "y": 1.913222954, "label": "F(1)", "dx": 0.15, "dy": 0.20}
  ],
  "caption": "The red semicircle is f(x)=sqrt(4-x^2); the teal curve is F=x sqrt(4-x^2)/2+2 arcsin(x/2). Differentiating the plotted F returns the red height."
}
:::

:::warn title="Do not confuse the two difference-of-squares orders"
The answers for $1/(x^2-a^2)$ and $1/(a^2-x^2)$ differ by more than a casually moved sign. Their logarithmic ratios are different. Differentiation is faster and safer than trying to memorise the numerator order without a check.
:::
