---
id: olympiad-03
part: olympiad
title: "Extension III — Parameter Differentiation"
---

## A parameter can manufacture a logarithm

For $x>0$ and $a\ne-1$, start with
$$
H(a,x)=\int x^a dx=\frac{x^{a+1}}{a+1}+C.
$$
Holding $x$ fixed and differentiating with respect to $a$ brings down $\ln x$:
$$
\frac{\partial H}{\partial a}
=\int x^a\ln x\,dx
=\frac{x^{a+1}((a+1)\ln x-1)}{(a+1)^2}+C.
$$
At $a=0$ this reproduces $\int\ln x\,dx=x\ln x-x$. At $a=1$ it gives
$$
\int x\ln x\,dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}+C,
$$
which is the antiderivative used in the source's S14 and Q28.

:::diagram
{
  "type": "table",
  "title": "Parameter differentiation creates a logarithmic hierarchy",
  "columns": ["Starting object", "Operation in a", "New integrand"],
  "rows": [
    ["x^(a+1)/(a+1)", "first derivative", "x^a ln x"],
    ["x^(a+1)/(a+1)", "second derivative", "x^a (ln x)^2"],
    ["a=0 after first", "specialise", "ln x"],
    ["a=1 after first", "specialise", "x ln x"]
  ],
  "col_widths": [0.38, 0.30, 0.32],
  "caption": "Differentiate first with a general, then substitute the parameter value. Setting a=0 before differentiating would erase the parameter being used."
}
:::

## A second differentiation gives squared logarithms

Differentiating once more,
$$
\int x^a(\ln x)^2dx
=x^{a+1}\left(\frac{(\ln x)^2}{a+1}
-\frac{2\ln x}{(a+1)^2}
+\frac{2}{(a+1)^3}\right)+C.
$$
At $a=0$,
$$
\int(\ln x)^2dx=x(\ln x)^2-2x\ln x+2x+C,
$$
in agreement with the reduction formula $J_2$ in Extension II. This is the indefinite form behind P14 and Q29; their endpoint limits belong to Chapter 21.

:::example title="Cross-check two methods at a=2"
Parameter differentiation gives
$$
\int x^2\ln x\,dx
=x^3\left(\frac{\ln x}{3}-\frac{1}{9}\right)+C.
$$
Direct by parts with $u=\ln x$ and $dv=x^2dx$ gives exactly the same expression. Their agreement checks both the parameter derivative and the by-parts coefficient.
:::

:::warn title="State the domain and the order of operations"
Here $x>0$ makes $x^a=e^{a\ln x}$ unambiguous. Differentiate with respect to $a$ while $x$ is fixed, and only then specialise $a$. The method generates an antiderivative; any later definite limit requires its own convergence check.
:::
