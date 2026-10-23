---
id: jee-90
part: jee
title: "Visual Function Lab — Domain, Range, Graph Tests and Inverses"
---

## Read a graph in three passes

A graph is not decoration: it is the set of ordered pairs $(x,f(x))$. Read it in this order. **First**, project the curve onto the $x$-axis to obtain the domain. **Second**, project it onto the $y$-axis to obtain the range. **Third**, use vertical and horizontal lines to ask whether an input is repeated and whether an output has more than one input.

:::diagram
{
  "type": "graph",
  "title": "One curve, three kinds of information",
  "xrange": [-2, 4], "yrange": [-3, 6],
  "curves": [{"expr": "x**2-2*x-1", "label": "y = f(x)", "labpos": 0.84}],
  "hlines": [{"y": -2, "label": "minimum output"}, {"y": 1, "label": "a horizontal test line"}],
  "points": [{"x": 1, "y": -2, "label": "vertex (1, -2)", "dx": 0.2}, {"x": 0, "y": -1, "label": "(0, -1)", "dx": -1.0}],
  "caption": "The vertex fixes the minimum output. The horizontal line y = 1 meets the curve twice, so this unrestricted quadratic is not one-one."
}
:::

For $f(x)=x^2-2x-1=(x-1)^2-2$, the domain is $\mathbb{R}$ and the range is $[-2,\infty)$. A vertical line meeting a relation more than once would violate the function condition. A horizontal line meeting a function more than once shows failure of injectivity; these are different tests answering different questions.

:::warn title="Do not confuse the two line tests"
The vertical-line test asks, “Is this relation a function?” The horizontal-line test asks, “Is this function one-one?” Neither test decides onto until a codomain is specified. For example, $x^2:\mathbb{R}\to\mathbb{R}$ is not onto, but $x^2:\mathbb{R}\to[0,\infty)$ is onto.
:::

<!-- pagebreak -->
## A domain-and-range example drawn before algebra

Consider $g(x)=\sqrt{4-x^2}$. The square root first requires $4-x^2\geq0$, so $-2\leq x\leq2$. On that domain, $0\leq4-x^2\leq4$; taking the nonnegative square root gives $0\leq g(x)\leq2$. Both endpoints are attained: $g(\pm2)=0$ and $g(0)=2$.

:::diagram
{
  "type": "graph",
  "title": "The upper semicircle explains both domain and range",
  "xrange": [-2.4, 2.4], "yrange": [-0.5, 2.6], "xticks": [-2, -1, 0, 1, 2], "yticks": [0, 1, 2],
  "curves": [{"expr": "sqrt(4-x**2)", "from": -2, "to": 2, "label": "y = sqrt(4 - x^2)", "labpos": 0.52, "label_dy": 0.18}],
  "points": [{"x": -2, "y": 0, "label": "(-2, 0)", "dy": 0.2}, {"x": 2, "y": 0, "label": "(2, 0)", "dx": -0.9, "dy": 0.2}, {"x": 0, "y": 2, "label": "(0, 2)", "dx": 0.15}],
  "caption": "The curve exists only between x = -2 and x = 2. Its height runs continuously from 0 to 2, with every intermediate value attained."
}
:::

The algebraic calculation and the picture should agree. Squaring $y=\sqrt{4-x^2}$ gives $x^2+y^2=4$, but the original equation also says $y\geq0$. Therefore the graph is only the **upper** semicircle, not the whole circle. This extra sign condition is exactly the information lost by squaring.

### One-one becomes visible after restriction

On $[0,\infty)$, the function $f(x)=x^2$ is strictly increasing and hence one-one. Its inverse is $f^{-1}(x)=\sqrt{x}$. Reflecting the point $(a,b)$ in $y=x$ gives $(b,a)$, so the graphs of a function and its inverse are mirror images in that line.

<!-- pagebreak -->
## Inverse graphs interchange the coordinates

:::diagram
{
  "type": "graph",
  "title": "Inverse graphs interchange the coordinates",
  "xrange": [-0.25, 2.25], "yrange": [-0.25, 2.25], "xticks": [0, 1, 2], "yticks": [0, 1, 2],
  "curves": [
    {"expr": "x**2", "from": 0, "to": 1.45, "label": "y = x^2", "labpos": 0.93, "label_ha": "right", "label_dx": -0.08},
    {"expr": "sqrt(x)", "from": 0, "to": 2.1, "label": "y = sqrt(x)", "labpos": 0.88, "label_ha": "right", "label_dx": -0.08, "label_dy": -0.30, "color": "#B8860B"},
    {"expr": "x", "from": 0, "to": 2.1, "label": "y = x", "ls": "--", "color": "#5B6B84"}
  ],
  "points": [{"x": 1, "y": 1, "label": "(1, 1) is fixed", "dx": 0.12, "dy": -0.38}],
  "caption": "The restriction x >= 0 is essential. Without it, x^2 is not one-one and no single inverse function exists on the whole real line."
}
:::

To find an inverse algebraically, write $y=f(x)$, solve for $x$ in terms of $y$, and then interchange the variable names. Carry the branch restriction through every step. Finally check both $f(f^{-1}(x))=x$ on the codomain of $f$ and $f^{-1}(f(x))=x$ on the domain of $f$.

### Composition: check the inner output first

For $(g\circ f)(x)=g(f(x))$, the number $x$ must belong to the domain of $f$, **and** $f(x)$ must belong to the domain of $g$. The second condition is easy to forget because the final simplified formula may appear to accept more inputs.

<!-- pagebreak -->
## A reusable composition check

:::diagram
{
  "type": "flow",
  "title": "Domain conditions travel through the composition",
  "steps": [
    {"title": "Start with the inner function", "detail": "Require x in Domain(f), then calculate the intermediate output f(x)."},
    {"title": "Admit that output into the outer function", "detail": "Impose f(x) in Domain(g); simplify these conditions together."},
    {"title": "Only now simplify the formula", "detail": "The simplified expression does not restore inputs removed by either earlier condition."},
    {"title": "Verify with a boundary input", "detail": "Test an included endpoint and a rejected candidate in the original composition."}
  ],
  "caption": "Domain conditions travel from left to right through the composition; they are not recovered by looking only at the final expression."
}
:::

:::example title="Two orders, two different domains"
Let $f(x)=\sqrt{x}$ and $g(x)=1-x$. Then $(g\circ f)(x)=1-\sqrt{x}$, with domain $[0,\infty)$. In the other order, $(f\circ g)(x)=\sqrt{1-x}$, with domain $(-\infty,1]$. At $x=4$, the first composition gives $-1$, while the second is undefined because $g(4)=-3$ cannot enter $f$. The formulas and domains both show why composition is generally not commutative.
:::

:::key title="The visual revision routine"
For any graph, mark the domain on the $x$-axis and the range on the $y$-axis. Draw a vertical line for the function test and a horizontal line for the one-one test. For an inverse, draw $y=x$ and check reflection. For a composition, write the intermediate output explicitly. These four drawings prevent most avoidable function errors.
:::


<!-- pagebreak -->
## Worked synthesis: composition, range and inversion

Let $h(x)=\sqrt{1-x^2}$ with the declared domain $[-1,1]$. The inner square accepts every real $x$, but the outer square root requires $1-x^2\geq0$, which is exactly the declared domain. Keeping both conditions visible prevents an apparently larger domain from appearing after simplification.

:::example title="Compute the range from the inner output"
On $[-1,1]$, the inner quantity $u=x^2$ ranges over $[0,1]$. As $u$ increases, $\sqrt{1-u}$ decreases from $1$ to $0$. Therefore the range is $[0,1]$, with both endpoints attained: $h(0)=1$ and $h(1)=0$.
:::

:::example title="Restrict first, then invert"
The formula $x^2$ is not one-one on $[-1,1]$, so the initial squaring step does not have an unrestricted inverse. On $[0,1]$, however, $h$ is strictly decreasing and $h(h(x))=\sqrt{1-(1-x^2)}=\sqrt{x^2}=x$. Thus $h$ is its own inverse on $[0,1]$. The absolute-value step uses $x\geq0$; it is not optional.
:::

:::key title="One example, three checks"
Domain comes from the outer function's requirement, range follows the inner output interval, and inversion requires a one-one restriction. Algebraic symmetry alone supplies none of these three hypotheses.
:::
