---
id: jee-06
part: jee
title: "Implicit Differentiation"
---

## Differentiate the relation, treating y as a function of x

If a local branch satisfies $F(x,y)=0$, differentiate both sides with respect to $x$. Every $y$-term uses the chain rule. When $F_y\ne0$,
$$
F_x+F_y\frac{dy}{dx}=0
\quad\Longrightarrow\quad
\frac{dy}{dx}=-\frac{F_x}{F_y}.
$$
The point must first satisfy the original relation; the derivative formula alone does not prove that a branch exists.

:::example title="A circle gives the slope without solving for y"
For $x^2+y^2=25$,
$$
2x+2y\frac{dy}{dx}=0
\quad\Longrightarrow\quad
\frac{dy}{dx}=-\frac{x}{y}\qquad(y\ne0).
$$
At $(3,4)$, the slope is $-3/4$. The tangent is
$$
y-4=-\frac{3}{4}(x-3).
$$
The radius has slope $4/3$, so the radius and tangent slopes multiply to $-1$.
:::

:::diagram
{
  "type": "graph",
  "title": "The implicit tangent is perpendicular to the radius",
  "xrange": [-6, 6], "yrange": [-6, 7],
  "curves": [
    {"expr": "sqrt(25-x**2)", "from": -5, "to": 5, "label": "upper branch", "labpos": 0.23, "label_dy": 0.25},
    {"expr": "-sqrt(25-x**2)", "from": -5, "to": 5, "label": "lower branch", "labpos": 0.72, "label_dy": -0.35},
    {"expr": "-(3/4)*x+25/4", "from": 0.4, "to": 5.5, "label": "tangent: slope -3/4", "labpos": 0.15, "label_dx": -0.3, "label_dy": 0.65, "color": "#B91C1C"}
  ],
  "rays": [{"x": [0, 3], "y": [0, 4], "color": "#B8860B"}],
  "points": [{"x": 3, "y": 4, "label": "(3,4)", "dx": 0.18, "dy": 0.20}, {"x": 0, "y": 0, "label": "O", "dx": 0.15, "dy": 0.20}],
  "caption": "The tangent uses only the local branch through (3,4). Its slope -3/4 is perpendicular to the radius slope 4/3."
}
:::

:::example title="Solve for the derivative only after collecting its coefficient"
For $y^3+xy=2$ at $(1,1)$,
$$
3y^2y'+y+xy'=0.
$$
Thus $(3y^2+x)y'=-y$, and substitution of the point gives
$$
y'=-\frac{1}{4}.
$$
The relation checks first: $1^3+1\cdot1=2$.
:::

:::warn title="The derivative formula can be undefined at a valid point"
At $(5,0)$ on the circle, $-x/y$ is undefined and the tangent is vertical. This does not contradict the relation; it means the local branch cannot be written as a differentiable function $y(x)$ there. Use $x$ as a function of $y$ or a parameter instead.
:::
