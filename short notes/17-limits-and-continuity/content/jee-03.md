---
id: jee-03
part: jee
title: "Squeeze and Trigonometric Limits"
---

## Two known bounds can force an unknown limit

If $g(x)\leq f(x)\leq h(x)$ near $a$, and $g,h$ both tend to $L$, then $f(x)\to L$. For an output tolerance $\varepsilon$, eventually both outer functions lie in $(L-\varepsilon,L+\varepsilon)$, leaving no other place for $f$.

:::example title="Bounded oscillation multiplied by a vanishing factor"
For $x\ne0$,
$$
-x^2\leq x^2\sin\frac{1}{x}\leq x^2.
$$
Both bounds tend to $0$, so $x^2\sin(1/x)\to0$. Likewise,
$$
\left|x\sin\frac{1}{x}\right|\leq|x|\longrightarrow0.
$$
The oscillating factor has no limit by itself, but its boundedness is enough for the squeeze.
:::

## The fundamental trigonometric limit comes from areas

For $0<x<\pi/2$, comparing triangle and sector areas gives
$$
\frac{1}{2}\sin x<\frac{1}{2}x<\frac{1}{2}\tan x.
$$
Rearranging,
$$
\cos x<\frac{\sin x}{x}<1.
$$
Since $\cos x\to1$, the squeeze gives $\sin x/x\to1$ from the right. The quotient is even, so the left limit is also $1$.

:::warn title="Radians and matching arguments are essential"
The area proof and the standard trigonometric limits use radians. A formula $\sin u/u\to1$ requires the **same** $u$ above and below, with $u\to0$ and $u\ne0$. Do not replace $\sin5x$ by $5x$ and then forget the factor $5$.
:::

:::diagram
{
  "type": "graph",
  "title": "sin(x)/x is squeezed between cos(x) and 1",
  "xrange": [0, 1.5], "yrange": [0.45, 1.12],
  "xticks": [0, 0.5, 1, 1.5], "yticks": [0.5, 0.75, 1],
  "curves": [
    {"expr": "cos(x)", "from": 0.02, "to": 1.5, "label": "cos(x)", "labpos": 0.78, "label_dy": -0.05, "color": "#B8860B"},
    {"expr": "sin(x)/x", "from": 0.02, "to": 1.5, "label": "sin(x)/x", "labpos": 0.62, "label_dy": 0.05},
    {"expr": "1+0*x", "from": 0, "to": 1.5, "label": "1", "labpos": 0.86, "label_dy": 0.04, "color": "#5B6B84"}
  ],
  "caption": "On 0 < x < pi/2, the middle curve approaches 1 because both outer values approach 1. Evenness supplies the left-hand conclusion."
}
:::

The same standard limit yields
$$
\lim_{x\to0}\frac{\tan x}{x}=1,
\qquad
\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac{1}{2}.
$$
For the second, use $1-\cos x=2\sin^2(x/2)$ or multiply by $1+\cos x$. Consequently,
$$
\frac{\cos x-1}{\sin^2x}=-\frac{1}{1+\cos x}\longrightarrow-\frac{1}{2}.
$$

:::example title="Match the small argument with its denominator"
$$
\frac{\sin5x}{3x}=\frac{5}{3}\cdot\frac{\sin5x}{5x}\longrightarrow\frac{5}{3}.
$$
Also $1-\cos2x=2\sin^2x$, so
$$
\frac{1-\cos2x}{x\sin x}=2\cdot\frac{\sin x}{x}\longrightarrow2.
$$
:::

:::example title="A third-power trigonometric limit without series"
For $x\ne0$,
$$
\frac{\tan x-\sin x}{x^3}
=\frac{1}{\cos x}\cdot\frac{\sin x}{x}\cdot\frac{1-\cos x}{x^2}
\longrightarrow1\cdot1\cdot\frac{1}{2}=\frac{1}{2}.
$$
Each factor has a separately justified finite limit.
:::
