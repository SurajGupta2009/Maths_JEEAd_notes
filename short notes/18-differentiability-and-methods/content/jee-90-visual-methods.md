---
id: jee-90-visual-methods
part: jee
title: "Visual Differentiation Methods Lab"
---

## Secant slopes reveal the derivative of a reciprocal

For $f(x)=1/x$ at $P=(1,1)$, the derivative is $-1$. The secants using $h=1$ and $h=1/2$ have slopes
$$
\frac{1/2-1}{2-1}=-\frac{1}{2},
\qquad
\frac{2/3-1}{1/2}=-\frac{2}{3}.
$$
They approach the tangent slope $-1$ as $h\to0$.

:::diagram
{
  "type": "graph",
  "title": "Two reciprocal secants approach the tangent of slope -1",
  "xrange": [0.35, 2.6], "yrange": [-0.6, 2.2],
  "curves": [
    {"expr": "1/x", "from": 0.4, "to": 2.4, "label": "y=1/x", "labpos": 0.82, "label_dy": 0.15},
    {"expr": "1.5-0.5*x", "from": 0.7, "to": 2.3, "label": "h=1: slope -1/2", "labpos": 0.05, "label_dx": -0.25, "label_dy": 0.55, "color": "#B8860B"},
    {"expr": "5/3-(2/3)*x", "from": 0.7, "to": 2.0, "label": "h=1/2: slope -2/3", "labpos": 0.75, "label_dx": 0.10, "label_dy": 0.35, "color": "#5B6B84"},
    {"expr": "2-x", "from": 0.45, "to": 2.4, "label": "tangent: slope -1", "labpos": 0.68, "label_dx": -0.55, "label_dy": -0.18, "color": "#B91C1C"}
  ],
  "points": [
    {"x": 1, "y": 1, "label": "P(1,1)", "dx": -0.55, "dy": -0.35},
    {"x": 2, "y": 0.5, "label": "Q(2,1/2)", "dx": 0.10, "dy": -0.28},
    {"x": 1.5, "y": 0.6666666667, "face": "white", "color": "#B91C1C"}
  ],
  "caption": "The secant slopes -1/2 and -2/3 are finite-difference approximations. The tangent y=2-x has the exact derivative slope -1 at P."
}
:::

**Visual check:** the tangent and both secants pass through $P$. Their slopes are ordered $-1/2>-2/3>-1$, consistent with the convex reciprocal graph on $x>0$.

<!-- pagebreak -->
## A differentiable piecewise join matches value and slope

For $x^2$ on the left and $ax+b$ on the right of $1$, the requirements are
$$
a+b=1,\qquad a=2.
$$
Thus $a=2$, $b=-1$, and the right branch is the tangent line $2x-1$.

:::diagram
{
  "type": "graph",
  "title": "The line 2x-1 joins x^2 without a corner",
  "xrange": [-0.5, 2.6], "yrange": [-1, 4.2],
  "curves": [
    {"expr": "x**2", "from": -0.5, "to": 1, "label": "left: x^2", "labpos": 0.35, "label_dy": 0.20},
    {"expr": "2*x-1", "from": 1, "to": 2.4, "label": "right: 2x-1", "labpos": 0.55, "label_dx": -0.70, "label_dy": 0.25},
    {"expr": "2*x-1", "from": 0.1, "to": 1, "label": "shared tangent", "labpos": 0.20, "label_dx": -0.25, "label_dy": -0.35, "color": "#B91C1C", "ls": "--"}
  ],
  "points": [{"x": 1, "y": 1, "label": "(1,1): value 1, slope 2", "dx": 0.15, "dy": -0.55}],
  "caption": "The function value is continuous and both one-sided derivatives equal 2. Merely drawing a connected graph would not be enough; the common tangent certifies the slope match."
}
:::

**Visual check:** at $1$, $x^2=1$ and $2x-1=1$. Their derivatives are $2x|_{x=1}=2$ and $2$, so both differentiability conditions hold exactly.

<!-- pagebreak -->
## Chain rule scales the slope at the origin

Near $0$, $\sin x\approx x$ while $\sin(3x)\approx3x$. The same small-angle limit therefore gives tangent slopes $1$ and $3$ at the origin.

:::diagram
{
  "type": "graph",
  "title": "The inner factor 3 triples the initial slope",
  "xrange": [-1.4, 1.4], "yrange": [-1.5, 1.5],
  "curves": [
    {"expr": "sin(x)", "label": "sin(x)", "labpos": 0.75, "label_dy": 0.15, "color": "#5B6B84"},
    {"expr": "sin(3*x)", "label": "sin(3x)", "labpos": 0.16, "label_dy": 0.20},
    {"expr": "x", "from": -0.7, "to": 0.7, "label": "y=x", "labpos": 0.95, "label_dy": -0.25, "color": "#B8860B", "ls": "--"},
    {"expr": "3*x", "from": -0.4, "to": 0.4, "label": "y=3x", "labpos": 0.85, "label_dx": -1.0, "label_dy": 0.45, "color": "#B91C1C", "ls": "--"}
  ],
  "points": [{"x": 0, "y": 0, "label": "common origin", "dx": 0.15, "dy": -0.35}],
  "caption": "Both sine curves pass through the origin, but sin(3x) oscillates three times as fast. Its local tangent is y=3x, illustrating the chain-rule factor 3."
}
:::

**Visual check:** for small $h$, $\sin(3h)/h=3\sin(3h)/(3h)\to3$. This agrees with $(\sin3x)'=3\cos3x$ at $0$.

<!-- pagebreak -->
## Implicit and parametric methods agree on an ellipse

For $x^2/4+y^2=1$,
$$
\frac{x}{2}+2yy'=0
\quad\Longrightarrow\quad
y'=-\frac{x}{4y}.
$$
With $x=2\cos t$, $y=\sin t$, the parametric slope is $-(1/2)\cot t$. At $t=\pi/4$, the point is $(\sqrt{2},1/\sqrt{2})$ and both methods give slope $-1/2$.

:::diagram
{
  "type": "graph",
  "title": "Two differentiation methods produce the same ellipse tangent",
  "xrange": [-2.5, 3], "yrange": [-1.8, 2],
  "curves": [
    {"expr": "sqrt(1-x**2/4)", "from": -2, "to": 2, "label": "upper ellipse", "labpos": 0.18, "label_dy": 0.15},
    {"expr": "-sqrt(1-x**2/4)", "from": -2, "to": 2, "label": "lower ellipse", "labpos": 0.70, "label_dy": -0.18},
    {"expr": "-0.5*x+sqrt(2)", "from": 0, "to": 2.8, "label": "tangent: slope -1/2", "labpos": 0.65, "label_dx": -1.25, "label_dy": 0.18, "color": "#B91C1C"}
  ],
  "points": [{"x": 1.4142135624, "y": 0.7071067812, "label": "(sqrt(2),1/sqrt(2))", "dx": 0.15, "dy": 0.15}],
  "caption": "The tangent is y=-x/2+sqrt(2). Implicit differentiation uses the relation; parametric differentiation uses t=pi/4. Their agreement is an independent check."
}
:::

**Visual check:** substituting the tangent point gives $x^2/4+y^2=1/2+1/2=1$. The tangent slope satisfies $-x/(4y)=-1/2=-(1/2)\cot(\pi/4)$.

<!-- pagebreak -->
## Logarithmic differentiation finds the tangent to x^x

For $x>0$, $y=x^x$ gives $\ln y=x\ln x$ and
$$
y'=x^x(1+\ln x).
$$
At $(1,1)$ the slope is $1$, so the tangent is $y=x$.

:::diagram
{
  "type": "graph",
  "title": "The tangent to x^x at (1,1) is y=x",
  "xrange": [0, 2.1], "yrange": [0, 4.5],
  "curves": [
    {"expr": "exp(x*log(x))", "from": 0.1, "to": 2, "label": "y=x^x", "labpos": 0.72, "label_dx": -0.50, "label_dy": 0.25},
    {"expr": "x", "from": 0.1, "to": 2, "label": "tangent y=x", "labpos": 0.45, "label_dx": -0.25, "label_dy": -0.75, "color": "#B91C1C"}
  ],
  "points": [{"x": 1, "y": 1, "label": "(1,1), slope 1", "dx": 0.25, "dy": -0.45}],
  "caption": "Taking logarithms differentiates both occurrences of x at once. The original curve and the line y=x share the point and first derivative at 1."
}
:::

**Visual check:** $1^1=1$ and $1^1(1+\ln1)=1$. Forward difference quotients at $1$ approach the same slope from above.

<!-- pagebreak -->
## A second parametric derivative needs one more division

For $x=t^2$, $y=t^3$,
$$
\frac{dy}{dx}=\frac{3t}{2},
\qquad
\frac{d^2y}{dx^2}=\frac{3}{4t}\qquad(t\ne0).
$$
At $t=1$, these are $3/2$ and $3/4$. At $t=2$, the point is $(4,8)$ and the tangent slope is $3$.

:::diagram
{
  "type": "graph",
  "title": "The semicubical parabola has slope 3 at t=2",
  "xrange": [-0.5, 5], "yrange": [-9, 10],
  "curves": [
    {"expr": "x**(3/2)", "from": 0, "to": 4.5, "label": "upper", "labpos": 0.45, "label_dx": -1.3, "label_dy": 1.0},
    {"expr": "-x**(3/2)", "from": 0, "to": 4.5, "label": "lower", "labpos": 0.65, "label_dx": 0.2, "label_dy": -0.8},
    {"expr": "3*x-4", "from": 2, "to": 4.5, "label": "tangent: slope 3", "labpos": 0.60, "label_dx": -2.0, "label_dy": 1.0, "color": "#B91C1C"}
  ],
  "points": [{"x": 4, "y": 8, "label": "t=2", "dx": 0.15, "dy": 0.25}, {"x": 1, "y": 1, "label": "t=1", "dx": 0.20, "dy": -0.65}],
  "caption": "The curve is y^2=x^3 with two branches. The tangent at t=2 is y=3x-4. The second derivative 3/(4t) is not y''(t)/x''(t)."
}
:::

:::key title="Read each figure as a derivative equation"
A secant shows a finite difference; a tangent shows its limit. A smooth join requires matching values and slopes. Inner scaling changes local rates. Implicit and parametric methods must agree on the same point. Every logarithmic or parametric calculation should end by multiplying or dividing by the factor required by the chain rule.
:::
