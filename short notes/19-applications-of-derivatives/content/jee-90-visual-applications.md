---
id: jee-90-visual-applications
part: jee
title: "Visual Lab — Six Derivative Applications"
---

This lab separates the geometric and numerical ideas that can be hidden by a formula. Every diagram is generated from an editable mathematical expression; the companion checks test its anchors independently.

## Lab 1 — A ladder's dimensions satisfy a circle constraint

:::diagram
{
  "type": "graph",
  "title": "The physical 5-12-13 ladder state gives a Pythagorean constraint",
  "xrange": [-0.5, 14], "yrange": [-0.5, 14],
  "xticks": [0, 5, 10], "yticks": [0, 5, 10, 12],
  "xlabel": "horizontal distance", "ylabel": "height",
  "rays": [
    {"x": [0, 5], "y": [12, 0], "label": "13 m", "color": "#B91C1C"},
    {"x": [0, 0], "y": [0, 12], "label": "wall", "color": "#5B6B84"},
    {"x": [0, 5], "y": [0, 0], "label": "floor", "color": "#5B6B84"}
  ],
  "points": [
    {"x": 0, "y": 12, "label": "top: height 12", "dx": 0.35, "dy": 0.25},
    {"x": 5, "y": 0, "label": "foot: distance 5", "dx": 0.35, "dy": 1.0}
  ],
  "caption": "In this physical diagram the foot distance is x=5 and the top height is y=12, so the ladder length is sqrt(x^2+y^2)=13. Differentiate x^2+y^2=169 to obtain the time rates."
}
:::

The equation $x^2+y^2=169$ is a **position constraint**, not a graph of position against time. The drawing uses physical wall/floor coordinates; $x$ and $y$ are the two distances. Time enters only after differentiating the constraint, which prevents confusing the geometric slope with the requested time rate.

<!-- pagebreak -->
## Lab 2 — Angle between curves is angle between tangents

:::diagram
{
  "type": "graph",
  "title": "Two curves and their tangents at the common point (1,1)",
  "xrange": [0.1, 1.75], "yrange": [-0.3, 2.9],
  "xticks": [0, 0.5, 1, 1.5], "yticks": [0, 1, 2],
  "curves": [
    {"expr": "x**2", "from": 0.1, "to": 1.65},
    {"expr": "x**3", "from": 0.1, "to": 1.4, "color": "#0F766E", "ls": "--"},
    {"expr": "2*x-1", "from": 0.25, "to": 1.75, "color": "#B91C1C"},
    {"expr": "3*x-2", "from": 0.35, "to": 1.55, "color": "#5B6B84"}
  ],
  "points": [{"x": 1, "y": 1, "label": "(1,1)", "dx": 0.1, "dy": -0.45}],
  "caption": "The teal solid parabola and dashed cubic have tangent slopes 2 and 3 at (1,1). The red and slate tangent lines make an acute angle arctan(1/7), about 8.13 degrees."
}
:::

To reproduce the angle, use $\tan\theta=|(3-2)/(1+6)|=1/7$. The tangent lines—not the secants and not the angle between radius vectors—carry the local directions of the curves.

<!-- pagebreak -->
## Lab 3 — Linear approximation has a visible error under magnification

:::diagram
{
  "type": "graph",
  "title": "A zoom near sqrt(25.4) separates the curve from its tangent",
  "xrange": [25.39, 25.41], "yrange": [5.03965, 5.04008],
  "xticks": [25.39, 25.4, 25.41],
  "yticks": [5.0398, 5.0399, 5.04, 5.04008],
  "yticklabels": ["5.03980", "5.03990", "5.04000", "5.04008"],
  "xlabel": "", "ylabel": "",
  "curves": [
    {"expr": "sqrt(x)", "from": 25.39, "to": 25.41},
    {"expr": "5+(x-25)/10", "from": 25.39, "to": 25.41, "color": "#B91C1C"}
  ],
  "points": [
    {"x": 25.4, "y": 5.0398412677, "label": "actual", "dx": -0.0085, "dy": -0.00007},
    {"x": 25.4, "y": 5.04, "label": "estimate", "dx": 0.0015, "dy": 0.000025}
  ],
  "caption": "The red tangent at x=25 gives the estimate 5.04; the teal square-root curve gives 5.0398412677.... The vertical gap is about 0.0001587, invisible at ordinary graph scale."
}
:::

For $f(x)=\sqrt{x}$, $f''(x)=-1/(4x^{3/2})<0$. Concavity explains why the tangent estimate is above the actual value. The next-order term is approximately $f''(25)(0.4)^2/2=-0.00016$, matching the displayed error.

<!-- pagebreak -->
## Lab 4 — Three monotone branches give exactly three roots

:::diagram
{
  "type": "graph",
  "title": "Each monotone branch of the cubic crosses the x-axis once",
  "xrange": [-2.5, 2.5], "yrange": [-3, 3],
  "curves": [{"expr": "x**3-3*x", "from": -2.15, "to": 2.15}],
  "vlines": [{"x": -1}, {"x": 1}],
  "points": [
    {"x": -1.7320508076, "y": 0, "label": "-sqrt(3)", "dx": -0.65, "dy": 0.55},
    {"x": 0, "y": 0, "label": "0", "dx": 0.12, "dy": 0.25},
    {"x": 1.7320508076, "y": 0, "label": "sqrt(3)", "dx": 0.25, "dy": 0.25}
  ],
  "caption": "The red dashed lines x=-1 and x=1 separate three strictly monotone branches. The signs at the turning values 2 and -2, together with the end behaviour, give one crossing per branch."
}
:::

The graph illustrates the proof but does not replace it. The algebraic argument uses IVT for existence and strict monotonicity for uniqueness, then verifies the roots $-\sqrt{3},0,\sqrt{3}$ exactly.

<!-- pagebreak -->
## Lab 5 — Absolute extrema include both endpoints

:::diagram
{
  "type": "graph",
  "title": "On [0,2], the cubic's maximum occurs at the right endpoint",
  "xrange": [-0.25, 2.25], "yrange": [-2.8, 2.8],
  "curves": [{"expr": "x**3-3*x", "from": 0, "to": 2}],
  "bands": [{"a": 0, "b": 2, "label": "feasible interval"}],
  "points": [
    {"x": 0, "y": 0, "label": "f(0)=0", "dx": 0.12, "dy": 0.2},
    {"x": 1, "y": -2, "label": "minimum -2", "dx": 0.15, "dy": -0.15},
    {"x": 2, "y": 2, "label": "maximum 2", "dx": -0.85, "dy": 0.2}
  ],
  "caption": "For f(x)=x^3-3x on [0,2], the candidate values are f(0)=0, f(1)=-2 and f(2)=2. Comparing values—not slopes—selects the absolute extrema."
}
:::

The local maximum at $x=-1$ is outside this interval and must not enter the candidate list. Conversely, the endpoint $x=2$ must enter even though the derivative there is not zero.

<!-- pagebreak -->
## Lab 6 — The corrected window optimum is feasible

:::diagram
{
  "type": "graph",
  "title": "The window area vertex lies before the zero-height endpoint",
  "xrange": [0, 2], "yrange": [0, 7.8],
  "xticks": [0, 0.5, 1, 1.5, 2],
  "xlabel": "radius r", "ylabel": "area A",
  "curves": [{"expr": "10*x-(2+pi/2)*x**2", "from": 0, "to": 1.9449226482}],
  "points": [
    {"x": 0, "y": 0, "label": "degenerate", "dx": 0.05, "dy": 0.25},
    {"x": 1.4002478838, "y": 7.0012394189, "label": "feasible maximum", "dx": -0.55, "dy": 0.35},
    {"x": 1.9449226482, "y": 5.9418891336, "label": ""}
  ],
  "annotations": [
    {"text": "h=0 endpoint", "x": 1.9449226482, "y": 5.9418891336, "tx": 1.05, "ty": 4.9}
  ],
  "caption": "The feasible interval ends at r_max=10/(2+pi), about 1.9449, where h=0 and the semicircle area is 5.9419. The vertex r*=10/(4+pi), about 1.4002, gives the larger value A_max=50/(4+pi), about 7.0012."
}
:::

At $r=r_*$, the perimeter relation gives $h=r_*>0$. At $r=r_{\max}$, the height is zero and the window degenerates to a semicircle. The completed-square identity in the verification script independently proves that the interior vertex gives the global maximum.
