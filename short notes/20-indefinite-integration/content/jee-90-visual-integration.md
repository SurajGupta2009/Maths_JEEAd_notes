---
id: jee-90-visual-integration
part: jee
title: "Visual Lab — Six Ways to See an Antiderivative"
---

An antiderivative is not merely an algebraic string. These six sheets display vertical families, domains, slopes, equivalent forms and substitution branches. Every curve is generated from an editable expression and independently differentiated in the verification suite.

## Lab 1 — The constant moves a curve without changing its slopes

:::diagram
{
  "type": "graph",
  "title": "Three antiderivatives of 2x have parallel tangents at x=1",
  "xrange": [-2.4, 2.4], "yrange": [-3.5, 5],
  "xticks": [-2, -1, 0, 1, 2], "yticks": [-3, -1, 1, 3, 5],
  "curves": [
    {"expr": "x**2-2", "from": -2.2, "to": 2.2},
    {"expr": "x**2", "from": -2.2, "to": 2.2, "color": "#B8860B", "ls": "--"},
    {"expr": "x**2+2", "from": -2.2, "to": 2.2, "color": "#5B6B84", "ls": ":"}
  ],
  "rays": [
    {"x": [0.4, 1.6], "y": [-2.2, 0.2], "color": "#B91C1C"},
    {"x": [0.4, 1.6], "y": [-0.2, 2.2], "color": "#B91C1C"},
    {"x": [0.4, 1.6], "y": [1.8, 4.2], "color": "#B91C1C"}
  ],
  "points": [
    {"x": 1, "y": -1, "label": ""},
    {"x": 1, "y": 1, "label": ""},
    {"x": 1, "y": 3, "label": "all slopes are 2", "dx": 0.2, "dy": 0.25}
  ],
  "caption": "The curves x^2-2, x^2 and x^2+2 differ only by vertical shifts. Their red tangent segments at x=1 are parallel because each derivative is 2x=2."
}
:::

If $F'=f$, then $(F+C)'=f$. Conversely, on one interval, any two antiderivatives have zero derivative for their difference and therefore differ by a constant. An initial condition selects exactly one of these vertical translates.

<!-- pagebreak -->
## Lab 2 — Logarithm branches and their slopes

:::diagram
{
  "type": "graph",
  "title": "ln|x| differentiates to 1/x on both sides of zero",
  "xrange": [-3, 3], "yrange": [-3, 3],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-3, -2, -1, 0, 1, 2, 3],
  "curves": [
    {"expr": "1/x", "from": -3, "to": -0.5, "color": "#B91C1C"},
    {"expr": "1/x", "from": 0.5, "to": 3, "color": "#B91C1C"},
    {"expr": "log(abs(x))", "from": -3, "to": -0.35},
    {"expr": "log(abs(x))", "from": 0.35, "to": 3}
  ],
  "rays": [
    {"x": [-2.6, -1.4], "y": [0.9931471806, 0.3931471806], "color": "#B8860B"},
    {"x": [1.4, 2.6], "y": [0.3931471806, 0.9931471806], "color": "#B8860B"}
  ],
  "points": [
    {"x": -2, "y": 0.6931471806, "label": "slope -1/2", "dx": -1.25, "dy": 0.35},
    {"x": 2, "y": 0.6931471806, "label": "slope 1/2", "dx": 0.15, "dy": -0.55}
  ],
  "caption": "Red branches are f(x)=1/x; teal branches are F(x)=ln|x|. The gold tangent slopes at x=-2 and x=2 are -1/2 and 1/2. No curve crosses the excluded line x=0."
}
:::

For $x<0$, $\ln|x|=\ln(-x)$, whose derivative is $(-1)/(-x)=1/x$. The absolute value therefore handles both signs. The two disconnected branches may carry different constants even though the shorthand writes one $C$.

<!-- pagebreak -->
## Lab 3 — By parts produces a function whose slope is ln x

:::diagram
{
  "type": "graph",
  "title": "The antiderivative x ln x - x has tangent slope ln x",
  "xrange": [0.15, 3.2], "yrange": [-2.5, 2.2],
  "xticks": [0.5, 1, 1.5, 2, 2.5, 3], "yticks": [-2, -1, 0, 1, 2],
  "curves": [
    {"expr": "log(x)", "from": 0.15, "to": 3.2, "color": "#B91C1C"},
    {"expr": "x*log(x)-x", "from": 0.15, "to": 3.2}
  ],
  "rays": [
    {"x": [0.5, 1.5], "y": [-1, -1], "color": "#B8860B"},
    {"x": [2.2, 3.1], "y": [-0.5182818285, 0.3817181715], "color": "#B8860B"}
  ],
  "points": [
    {"x": 1, "y": -1, "label": "F(1)=-1", "dx": 0.15, "dy": -0.35},
    {"x": 2.7182818285, "y": 0, "label": "F(e)=0", "dx": -0.65, "dy": 0.30}
  ],
  "caption": "Red is f(x)=ln x and teal is F(x)=x ln x-x. The gold tangent at x=1 is horizontal because ln 1=0; at x=e its slope is 1 because ln e=1."
}
:::

The product-rule calculation $\int\ln x\,dx=x\ln x-\int1\,dx$ is visible in the slopes. Notice that the red curve gives the **slope** of the teal curve, not its height. This distinction is the geometric meaning of $F'=f$.

<!-- pagebreak -->
## Lab 4 — Partial fractions make a logarithm increase

:::diagram
{
  "type": "graph",
  "title": "A positive partial-fraction integrand makes its antiderivative increase",
  "xrange": [-0.9, 3], "yrange": [-3, 2.5],
  "xticks": [0, 1, 2, 3], "yticks": [-3, -2, -1, 0, 1, 2],
  "curves": [
    {"expr": "1/((x+1)*(x+2))", "from": -0.9, "to": 3, "clip": 3, "color": "#B91C1C"},
    {"expr": "log(abs((x+1)/(x+2)))", "from": -0.9, "to": 3}
  ],
  "rays": [
    {"x": [-0.4, 0.6], "y": [-0.8931471806, -0.3931471806], "color": "#B8860B"},
    {"x": [0.4, 1.8], "y": [-0.5054651081, -0.2721317748], "color": "#B8860B"}
  ],
  "points": [
    {"x": 0, "y": -0.6931471806, "label": "F(0)=ln(1/2)", "dx": 0.15, "dy": -0.45},
    {"x": 1, "y": -0.4054651081, "label": "F(1)=ln(2/3)", "dx": 0.15, "dy": 0.25}
  ],
  "caption": "On x>-1, red is f=1/((x+1)(x+2)) and teal is F=ln|(x+1)/(x+2)|. Gold tangent slopes are f(0)=1/2 and f(1)=1/6, so F increases with decreasing slope."
}
:::

The decomposition $f=1/(x+1)-1/(x+2)$ explains why the antiderivative is a difference of logarithms. The graph uses only the interval $x>-1$; the excluded points $-2$ and $-1$ divide the full domain into separate branches.

<!-- pagebreak -->
## Lab 5 — Equivalent answers are vertical translates

:::diagram
{
  "type": "graph",
  "title": "Three correct antiderivatives of sin x cos x have the same shape",
  "xrange": [-3.3, 3.3], "yrange": [-0.65, 0.65],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-0.5, -0.25, 0, 0.25, 0.5],
  "curves": [
    {"expr": "0.5*sin(x)**2", "from": -3.2, "to": 3.2},
    {"expr": "-0.5*cos(x)**2", "from": -3.2, "to": 3.2, "color": "#B8860B", "ls": "--"},
    {"expr": "-0.25*cos(2*x)", "from": -3.2, "to": 3.2, "color": "#5B6B84", "ls": ":"}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "A", "dx": 0.12, "dy": 0.08},
    {"x": 0, "y": -0.25, "label": "C", "dx": 0.12, "dy": -0.02},
    {"x": 0, "y": -0.5, "label": "B", "dx": 0.12, "dy": -0.03}
  ],
  "caption": "A=sin^2(x)/2, B=-cos^2(x)/2 and C=-cos(2x)/4. Their vertical differences are A-B=1/2 and A-C=1/4, so all three derivatives equal sin x cos x."
}
:::

The curves are not approximations of one another: their vertical separations are exactly constant. This is why an answer can look different from a textbook answer and still be completely correct. Differentiate first; then compare constants if necessary.

<!-- pagebreak -->
## Lab 6 — Half-angle antiderivatives have branches

:::diagram
{
  "type": "graph",
  "title": "The half-angle formula differentiates to 1/(2+cos x) on (-pi,pi)",
  "xrange": [-3, 3], "yrange": [-1.1, 1.1],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-1, -0.5, 0, 0.5, 1],
  "curves": [
    {"expr": "1/(2+cos(x))", "from": -3, "to": 3, "color": "#B91C1C"},
    {"expr": "(2/sqrt(3))*arctan(tan(x/2)/sqrt(3))", "from": -3, "to": 3}
  ],
  "rays": [
    {"x": [-1, 1], "y": [-0.3333333333, 0.3333333333], "color": "#B8860B"}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "F(0)=0", "dx": 0.15, "dy": 0.15},
    {"x": 1.5707963268, "y": 0.6045997884, "label": "F(pi/2)", "dx": 0.15, "dy": 0.15}
  ],
  "caption": "Red is f=1/(2+cos x); teal is the half-angle antiderivative F. The gold tangent at zero has slope f(0)=1/3. At pi/2 the slope of F is f(pi/2)=1/2, not the displayed height."
}
:::

On $-\pi<x<\pi$, $t=\tan(x/2)$ is continuous and strictly increasing, and differentiating the plotted $F$ returns the positive red integrand. At $x=\pm\pi$, the substitution itself fails. A continuous antiderivative on a larger interval must be constructed branch by branch with matching constants.
