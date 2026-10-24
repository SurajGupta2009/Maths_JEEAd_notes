---
id: jee-90-visual-methods
part: jee
title: "Visual Limits and Continuity Lab"
---

## A hole can have a limit without having the right value

Consider $(x^2-1)/(x-1)$ for $x\ne1$, and separately assign the value $f(1)=3$. Away from $1$, the quotient equals $x+1$, so both approaches point to $2$. The assigned value $3$ sits above the limiting height.

:::diagram
{
  "type": "graph",
  "title": "The limit is 2, but the assigned value is 3",
  "xrange": [-0.5, 2.5], "yrange": [0, 4.2],
  "curves": [
    {"expr": "x+1", "from": -0.5, "to": 0.97, "label": "x+1 away from 1", "labpos": 0.30, "label_dy": 0.25},
    {"expr": "x+1", "from": 1.03, "to": 2.5}
  ],
  "points": [
    {"x": 1, "y": 2, "label": "open limiting point (1,2)", "face": "white", "color": "#B91C1C", "dx": 0.15, "dy": -0.45},
    {"x": 1, "y": 3, "label": "assigned value f(1)=3", "dx": -1.35, "dy": 0.25}
  ],
  "caption": "The open point controls the limit; the closed point controls continuity. Redefining the closed point at (1,2) would remove the discontinuity."
}
:::

**Visual check:** at $x=1.001$, the original quotient is $2.001$ exactly. The approach is toward $2$, regardless of the separately assigned value.

:::key title="Second read: three different objects"
The original domain excludes $1$, the two-sided limit is $2$, and the declared value is $3$. Keeping those three claims separate prevents both algebra and continuity errors.
:::

<!-- pagebreak -->
## Squeeze makes oscillation irrelevant

For $x\ne0$, the graph of $x^2\sin(1/x)$ oscillates increasingly often near $0$. Nevertheless its absolute value never exceeds $x^2$, so it is trapped between the two smooth parabolas $-x^2$ and $x^2$.

:::diagram
{
  "type": "graph",
  "title": "The oscillating curve is trapped between -x^2 and x^2",
  "xrange": [-0.45, 0.45], "yrange": [-0.22, 0.22],
  "xticks": [-0.4, -0.2, 0, 0.2, 0.4], "yticks": [-0.2, 0, 0.2],
  "curves": [
    {"expr": "x**2", "label": "x^2", "labpos": 0.88, "label_dy": -0.025, "color": "#B8860B"},
    {"expr": "-x**2", "label": "-x^2", "labpos": 0.88, "label_dy": 0.025, "color": "#B8860B"},
    {"expr": "x**2*sin(1/x)", "from": -0.45, "to": -0.003, "n": 1600, "color": "#0F766E"},
    {"expr": "x**2*sin(1/x)", "from": 0.003, "to": 0.45, "n": 1600}
  ],
  "points": [{"x": 0.3183098862, "y": 0, "label": "zero at x=1/pi", "dx": 0.03, "dy": 0.07}],
  "caption": "Frequency does not defeat the squeeze: both smooth bounds have height 0 at the origin, so the middle graph is forced to the same limit."
}
:::

**Visual check:** at $x=2/(5\pi)$, $\sin(1/x)=1$, so the middle curve touches $x^2$. At $x=1/\pi$, it touches zero. Both observations agree with $-x^2\leq f(x)\leq x^2$.

<!-- pagebreak -->
## A standard trigonometric limit has a visible target

The quotient $\sin(5x)/(3x)$ is undefined at $0$. Away from $0$, it equals $(5/3)\sin(5x)/(5x)$, so the limiting height is $5/3$.

:::diagram
{
  "type": "graph",
  "title": "The removable gap has height 5/3",
  "xrange": [-1.4, 1.4], "yrange": [-0.5, 2.2],
  "curves": [
    {"expr": "sin(5*x)/(3*x)", "from": -1.4, "to": -0.01, "n": 1000, "color": "#0F766E"},
    {"expr": "sin(5*x)/(3*x)", "from": 0.01, "to": 1.4, "n": 1000}
  ],
  "hlines": [{"y": 1.6666666667, "label": "y = 5/3"}],
  "points": [{"x": 0, "y": 1.6666666667, "label": "open at (0,5/3)", "face": "white", "color": "#B91C1C", "dx": 0.12, "dy": 0.28}],
  "caption": "Oscillations away from zero do not change the local target. Matching 5x in the sine and denominator produces the factor 5/3 exactly."
}
:::

**Visual check:** at $x=0.1$, the value is $\sin(0.5)/0.3\approx1.598085$, already near $1.666667$. The graph and the standard-limit calculation identify the same hole.

<!-- pagebreak -->
## A base approaching 1 can still have a nontrivial limit

For $x>0$, the base $1+3/x$ tends to $1$ while the exponent $x$ tends to infinity. The logarithm resolves the competition:
$$
\ln\!\left(1+\frac{3}{x}\right)^x
=3\frac{\ln(1+3/x)}{3/x}\longrightarrow3.
$$
Therefore $(1+3/x)^x\to e^3$.

:::diagram
{
  "type": "graph",
  "title": "The growing exponent pulls the expression toward e^3",
  "xrange": [0, 40], "yrange": [0, 23],
  "xticks": [0, 10, 20, 30, 40], "yticks": [0, 5, 10, 15, 20.0855],
  "yticklabels": ["0", "5", "10", "15", "e^3"],
  "curves": [{"expr": "exp(x*log(1+3/x))", "from": 1, "to": 40}],
  "hlines": [{"y": 20.085536923, "label": "y = e^3"}],
  "points": [{"x": 10, "y": 13.785849184, "label": "x=10", "dx": 0.8, "dy": -1.2}, {"x": 30, "y": 17.449402268, "label": "x=30", "dx": 1.0, "dy": -1.4}],
  "caption": "The horizontal asymptote is e^3, not 1. The product of the small base increment 3/x and the large exponent x remains 3."
}
:::

**Visual check:** $1.3^{10}\approx13.78585$ and $1.1^{30}\approx17.44940$ lie below $e^3\approx20.08554$, consistent with the graph's approach from below.

<!-- pagebreak -->
## Continuity needs the left, right and value to meet

Use the three-piece formula from the mixed-strategy lesson with $a=b=2$. The left formula is $\sin(2x)/x$, the right formula is $(e^{2x}-1)/x$, and the value at $0$ is $2$.

:::diagram
{
  "type": "graph",
  "title": "Two different formulas can join continuously",
  "xrange": [-1.5, 1.5], "yrange": [-0.2, 7],
  "curves": [
    {"expr": "sin(2*x)/x", "from": -1.5, "to": -0.01, "label": "left: sin(2x)/x", "labpos": 0.20, "label_dy": 0.4},
    {"expr": "(exp(2*x)-1)/x", "from": 0.01, "to": 1.5, "clip": 7, "label": "right: (e^(2x)-1)/x", "labpos": 0.55, "label_dx": -0.55, "label_dy": 0.4, "color": "#B8860B"}
  ],
  "hlines": [{"y": 2}],
  "points": [{"x": 0, "y": 2, "label": "value 2", "dx": 0.15, "dy": 0.35}],
  "caption": "The left limit, right limit and assigned value all equal 2. The formulas need not be the same on the two sides for continuity to hold."
}
:::

**Visual check:** the left standard limit is $2$, the right standard limit is $2$, and the plotted point is exactly at their common height. If $b$ were changed, only that point would move and continuity would fail.

<!-- pagebreak -->
## IVT turns opposite endpoint heights into a crossing

For $g(x)=\cos x-x$ on $[0,\pi/2]$,
$$
g(0)=1,\qquad g\left(\frac{\pi}{2}\right)=-\frac{\pi}{2}.
$$
The continuous graph therefore crosses zero at least once. Its crossing is the Dottie number, approximately $0.7390851332$.

:::diagram
{
  "type": "graph",
  "title": "The continuous difference cos(x)-x must cross zero",
  "xrange": [0, 1.65], "yrange": [-1.8, 1.2],
  "xticks": [0, 0.7390851332, 1.5707963268], "xticklabels": ["0", "c", "pi/2"],
  "yticks": [-1.5707963, 0, 1], "yticklabels": ["-pi/2", "0", "1"],
  "curves": [{"expr": "cos(x)-x", "from": 0, "to": 1.5707963268, "label": "g(x)=cos(x)-x", "labpos": 0.25, "label_dy": 0.25}],
  "hlines": [{"y": 0, "label": "zero level"}],
  "points": [
    {"x": 0, "y": 1, "label": "positive", "dx": 0.05, "dy": -0.3},
    {"x": 0.7390851332, "y": 0, "label": "c ~0.739085", "dx": 0.10, "dy": 0.25, "color": "#B91C1C"},
    {"x": 1.5707963268, "y": -1.5707963268, "label": "negative", "dx": -0.50, "dy": 0.15}
  ],
  "caption": "Continuity supplies the crossing. The IVT statement alone does not supply its decimal value or prove uniqueness."
}
:::

:::key title="Read every graph with a mathematical question"
An open point asks for a limit; a closed point asks for continuity. Outer curves ask for a squeeze; an asymptote asks about growth; a sign change asks for IVT. The picture organizes the calculation, while exact substitution and the theorem hypotheses certify it.
:::
