---
id: jee-02
part: jee
title: "One-Sided Derivatives and Piecewise Differentiability"
---

## Two one-sided slopes must both exist and agree

At a junction $a$, define
$$
f'_-(a)=\lim_{h\to0^-}\frac{f(a+h)-f(a)}{h},
\qquad
f'_+(a)=\lim_{h\to0^+}\frac{f(a+h)-f(a)}{h}.
$$
The two-sided derivative exists exactly when these are equal. On a domain with only one side, the corresponding one-sided derivative is the appropriate notion.

For $|x-2|$ at $2$, the left derivative is $-1$ and the right derivative is $1$, so the continuous corner is not differentiable. For $x|x|$ at $0$,
$$
\frac{h|h|}{h}=|h|\longrightarrow0
$$
from either side, so the derivative exists and equals $0$.

:::diagram
{
  "type": "graph",
  "title": "A corner and a smooth flat join are different",
  "xrange": [-1.6, 1.6], "yrange": [-2.8, 2.8],
  "curves": [
    {"expr": "abs(x)", "label": "|x|: unequal slopes", "labpos": 0.18, "label_dx": -0.25, "label_dy": 0.30, "color": "#B8860B"},
    {"expr": "x*abs(x)", "label": "x|x|: derivative 0", "labpos": 0.78, "label_dx": -0.20, "label_dy": -1.35}
  ],
  "hlines": [{"y": 0}],
  "points": [{"x": 0, "y": 0, "label": "O", "dx": 0.12, "dy": 0.22}],
  "caption": "Both functions are continuous at 0. The V-shaped graph has left/right slopes -1 and 1; the curved graph has difference quotient |h|, so both sides have slope 0. The red dashed line is its horizontal tangent."
}
:::

## Match values before matching derivative formulas

For
$$
f(x)=x^2\quad(x\leq1),\qquad f(x)=ax+b\quad(x>1),
$$
differentiability first requires continuity:
$$
1=a+b.
$$
The left derivative at $1$ is $2$, while the right derivative is $a$. Therefore
$$
a=2,\qquad b=-1.
$$
With these parameters the right formula is $2x-1$, exactly the tangent to $x^2$ at $1$.

:::example title="A smooth junction needs two independent equations"
Checking only $a=2$ matches slopes but leaves $1=2+b$, so continuity would fail unless $b=-1$. Checking only $a+b=1$ matches values but does not control the slopes. Both conditions are necessary.
:::

## An infinite difference quotient is not a finite derivative

For $f(x)=x^{1/3}$ at $0$,
$$
\frac{f(h)-f(0)}{h}=h^{-2/3},
$$
which is unbounded as $h\to0$. The graph has a vertical tangent in a geometric sense, but $f'(0)$ does not exist as a finite real number.

:::warn title="Do not differentiate each branch only away from the junction"
Branch formulas tell you the one-sided derivatives only after the function value is known and continuous. Preserve the domain of each formula, then compare left limit, right limit, value, left derivative and right derivative explicitly.
:::
