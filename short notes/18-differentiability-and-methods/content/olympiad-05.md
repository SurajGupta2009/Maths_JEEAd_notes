---
id: olympiad-05
part: olympiad
title: "Extension V — Rolle, Mean Value and Derivative Inequalities"
---

## Rolle's theorem turns equal endpoints into a stationary point

If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$ and $f(a)=f(b)$, then there is $c\in(a,b)$ with $f'(c)=0$. Continuity on the closed interval gives an extreme value. If every extreme occurs only at endpoints, equal endpoint values force $f$ to be constant; otherwise an interior extreme has zero derivative.

:::example title="Two Rolle points for x^3-x on [-1,1]"
Here $f(-1)=f(1)=0$ and
$$
f'(x)=3x^2-1.
$$
Thus $f'(c)=0$ exactly at $c=\pm1/\sqrt{3}$, both inside $(-1,1)$.
:::

## The mean value theorem tilts the same picture

Under the same continuity and differentiability hypotheses, but without equal endpoints,
$$
\frac{f(b)-f(a)}{b-a}=f'(c)
$$
for some $c\in(a,b)$. To prove this, apply Rolle's theorem to
$$
g(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a),
$$
which has $g(a)=g(b)=0$. For $f(x)=x^2$ on $[1,3]$, the secant slope is $4$, so $2c=4$ and $c=2$.

## MVT can prove global inequalities without optimization

For $a\ne b$, MVT gives $c$ between $a$ and $b$ such that
$$
\sin a-\sin b=(a-b)\cos c.
$$
Hence $|\sin a-\sin b|\leq|a-b|$. Taking $a=x\geq0$ and $b=0$ also gives $\sin x\leq|\sin x|\leq x$.

Similarly, for $x\ne0$, MVT gives $c$ between $0$ and $x$ with $e^x-1=xe^c$. If $x>0$, then $e^c>1$; if $x<0$, then $e^c<1$ and multiplication by the negative $x$ reverses the inequality. In both cases $e^x-1>x$, while equality occurs at $x=0$. Thus $e^x\geq1+x$ for every real $x$, with equality only at $0$.

For $x>1$, applying MVT to $\ln x$ on $[1,x]$ gives $c\in(1,x)$ with
$$
\ln x=\frac{x-1}{c}<x-1.
$$
For $0<x<1$, there is $c\in(x,1)$ such that $\ln x=(x-1)/c<x-1$; the negative numerator and $0<c<1$ preserve the stated strict inequality. At $x=1$, equality holds. Hence
$$
\ln x\leq x-1\qquad(x>0).
$$

:::diagram
{
  "type": "graph",
  "title": "The logarithm lies below its tangent upper bound x-1",
  "xrange": [0.15, 3], "yrange": [-2.6, 2.2],
  "curves": [
    {"expr": "log(x)", "from": 0.15, "to": 3, "label": "ln(x)", "labpos": 0.65, "label_dy": -0.30},
    {"expr": "x-1", "from": 0.15, "to": 3, "label": "x-1", "labpos": 0.65, "label_dy": 0.20, "color": "#B91C1C"}
  ],
  "points": [{"x": 1, "y": 0}],
  "annotations": [{"text": "equality at x=1", "x": 1, "y": 0, "tx": 0.35, "ty": 0.8}],
  "caption": "The two graphs meet at (1,0) and agree in slope there. MVT proves the full inequality; the figure is an independent geometric check, not the proof."
}
:::

:::warn title="This extension is a bridge, not Chapter 19"
Rolle and MVT are included because the source introduces them beside derivatives. Systematic monotonicity, extrema, optimization and advanced tangent-normal applications belong to Chapter 19 — Applications of Derivatives.
:::
