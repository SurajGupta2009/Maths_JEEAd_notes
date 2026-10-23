---
id: jee-90
part: jee
title: "Visual Trigonometry Lab — Unit Circle, Graphs and General Solutions"
---

## Start from coordinates, not a sign mnemonic

On the unit circle, the point at angle $\theta$ is $P=(\cos\theta,\sin\theta)$. The $x$-coordinate gives cosine and the $y$-coordinate gives sine. Hence $\tan\theta=\sin\theta/\cos\theta$ whenever $\cos\theta\ne0$. Quadrant signs follow immediately from the signs of the two coordinates.

:::diagram
{
  "type": "unitcircle",
  "angle_deg": 45,
  "point_label": "P = (cos(theta), sin(theta))",
  "cos_label": "cos(theta)", "sin_label": "sin(theta)", "angle_label": "theta",
  "title": "One point contains all three basic ratios",
  "caption": "At 45 degrees the coordinates are equal and positive. Rotating the point changes signs and may interchange sine and cosine, but the coordinate definition never changes."
}
:::

The radius also proves $\sin^2\theta+\cos^2\theta=1$: it is simply the distance equation $OP=1$. Dividing by $\cos^2\theta$ gives $1+\tan^2\theta=\sec^2\theta$ where cosine is nonzero; dividing by $\sin^2\theta$ gives $1+\cot^2\theta=\csc^2\theta$ where sine is nonzero. The excluded angles belong with the identities.

<!-- pagebreak -->
## Sine and cosine are the same wave shifted

:::diagram
{
  "type": "graph",
  "title": "Read amplitude, period and phase from two curves",
  "xrange": [-6.2832, 6.2832], "yrange": [-1.6, 1.6],
  "xticks": [-6.2832, -3.1416, 0, 3.1416, 6.2832], "xticklabels": ["-2pi", "-pi", "0", "pi", "2pi"], "yticks": [-1, 0, 1],
  "curves": [{"expr": "sin(x)", "label": "sin x", "labpos": 0.80}, {"expr": "cos(x)", "label": "cos x", "labpos": 0.88, "color": "#B8860B"}],
  "points": [{"x": 1.5708, "y": 1, "label": "sine maximum", "dx": 0.25, "dy": 0.25}, {"x": 0, "y": 1, "label": "cosine maximum", "dx": -0.25, "dy": 0.25, "ha": "right"}],
  "caption": "Both curves have amplitude 1 and period 2pi. The cosine curve shifted right by pi/2 becomes the sine curve: cos(x - pi/2) = sin x."
}
:::

For $y=A\sin(Bx+C)+D$ with $A\ne0$ and $B>0$, the midline is $y=D$, amplitude is $|A|$, and period is $2\pi/B$. The horizontal shift is found by writing $Bx+C=B(x+C/B)$, so the shift is $-C/B$, **not** $-C$. Always read the coefficient of $x$ after factoring $B$.

:::example title="Transform before reading the period"
For $y=3\sin(2x-\pi/3)+1$, write $2x-\pi/3=2(x-\pi/6)$. The midline is $y=1$, amplitude $3$, period $\pi$, and the basic sine wave is shifted right by $\pi/6$. Its maximum is $4$ and minimum is $-2$. These values follow from the vertical stretch and shift; no point-by-point plotting is needed.
:::

<!-- pagebreak -->
## Tangent has a different period and breaks at asymptotes

:::diagram
{
  "type": "graph",
  "title": "Why tangent repeats after pi, not 2pi",
  "xrange": [-6.2832, 6.2832], "yrange": [-5, 5],
  "xticks": [-6.2832, -3.1416, 0, 3.1416, 6.2832], "xticklabels": ["-2pi", "-pi", "0", "pi", "2pi"], "yticks": [-4, -2, 0, 2, 4],
  "curves": [{"expr": "tan(x)", "from": -6.1, "to": 6.1, "n": 1600, "clip": 5.2, "label": "tan x", "labpos": 0.60}],
  "vlines": [{"x": -4.7124}, {"x": -1.5708, "label": "cos x = 0", "dx": -0.15, "ha": "right"}, {"x": 1.5708, "label": "cos x = 0", "dx": 0.15, "ha": "left"}, {"x": 4.7124}],
  "points": [{"x": 0, "y": 0, "label": "origin", "dx": 0.25, "dy": -0.65}],
  "caption": "Each branch is increasing on its domain. The dashed vertical lines are excluded inputs, not parts of the graph. Tangent has period pi because sin(x+pi) and cos(x+pi) both change sign."
}
:::

The statement “$\tan x$ is increasing” needs a domain qualification. It increases on every interval $(-\pi/2+k\pi,\pi/2+k\pi)$, but not across an asymptote. For example, $\tan(3\pi/4)=-1$ and $\tan(\pi/4)=1$; comparing values across different branches does not preserve one global increasing order.

### A horizontal line turns a trig equation into angles

To solve $\sin x=1/2$, first find the intersections in one convenient interval. On $[0,2\pi)$ they occur at $x=\pi/6$ and $x=5\pi/6$. Then add $2n\pi$ because sine repeats after $2\pi$.

<!-- pagebreak -->
## Two intersections per period for sin x = 1/2

:::diagram
{
  "type": "graph",
  "title": "Base angles first, periodic copies second",
  "xrange": [-0.2, 6.4832], "yrange": [-1.4, 1.5],
  "xticks": [0, 1.5708, 3.1416, 4.7124, 6.2832], "xticklabels": ["0", "pi/2", "pi", "3pi/2", "2pi"], "yticks": [-1, 0, 0.5, 1],
  "curves": [{"expr": "sin(x)", "from": 0, "to": 6.2832, "label": "y = sin x", "labpos": 0.76}],
  "hlines": [{"y": 0.5, "label": "y = 1/2"}],
  "points": [{"x": 0.5236, "y": 0.5, "label": "pi/6", "dy": 0.25}, {"x": 2.6180, "y": 0.5, "label": "5pi/6", "dx": -0.8, "dy": 0.25}],
  "caption": "The graph gives the two base angles. Periodicity supplies every other intersection; an interval in the question then selects only the required answers."
}
:::

$$
x=2n\pi+\frac{\pi}{6}\quad\text{or}\quad x=2n\pi+\frac{5\pi}{6},\qquad n\in\mathbb{Z}.
$$

:::warn title="A general solution is not yet the requested answer"
If the question asks for $x\in[0,\pi]$, substitute integer values of $n$ or use the graph to retain only $\pi/6$ and $5\pi/6$. If a transformation introduced squaring, tangent division, or a denominator, also substitute into the original equation. “General solution” and “solution in the stated interval” are separate steps.
:::

:::key title="The graph-first equation routine"
Reduce to one trigonometric function, draw one period, draw the required horizontal level, record all intersections in that period, and only then add the correct period. Use $2\pi$ for sine and cosine, and $\pi$ for tangent. Finish with the interval and validity filters.
:::
