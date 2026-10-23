---
id: jee-90
part: jee
title: "Visual Inverse-Trigonometry Lab — Branches, Graphs and Safe Identities"
---

## The range is the branch rule

An inverse trigonometric value is an **angle in a specified principal range**. The range is therefore as important as the formula. Always write the branch before simplifying a composition or squaring an equation.

:::diagram
{
  "type": "table",
  "title": "Principal branches at a glance",
  "columns": ["Function", "Domain", "Principal range"],
  "rows": [
    ["sin^-1 x", "[-1, 1]", "[-pi/2, pi/2]"],
    ["cos^-1 x", "[-1, 1]", "[0, pi]"],
    ["tan^-1 x", "R", "(-pi/2, pi/2)"],
    ["cot^-1 x", "R", "(0, pi)"],
    ["sec^-1 x", "(-inf, -1] U [1, inf)", "[0, pi] minus {pi/2}"],
    ["cosec^-1 x", "(-inf, -1] U [1, inf)", "[-pi/2, pi/2] minus {0}"]
  ],
  "caption": "Use the repository convention consistently. The branch selects exactly one angle from the infinitely many angles having the requested trigonometric value."
}
:::

The identities $\sin^{-1}x+\cos^{-1}x=\pi/2$ on $[-1,1]$ and $\tan^{-1}x+\cot^{-1}x=\pi/2$ for the stated cotangent convention are useful checks: their graphs are reflections in a horizontal midline, not unrelated curves.

<!-- pagebreak -->
## Arcsine returns an angle, not a general solution

For $y=\sin^{-1}x$, the input $x$ is a sine value and the output $y$ lies in $[-\pi/2,\pi/2]$. Thus $\sin(\sin^{-1}x)=x$ on $[-1,1]$, but $\sin^{-1}(\sin\theta)$ need not equal $\theta$.

:::diagram
{
  "type": "graph",
  "title": "Arcsine is increasing on its entire domain",
  "xrange": [-1.25, 1.25], "yrange": [-1.8, 1.8], "xticks": [-1, 0, 1], "yticks": [-1.5708, 0, 1.5708], "yticklabels": ["-pi/2", "0", "pi/2"],
  "curves": [{"expr": "asin(x)", "from": -1, "to": 1, "label": "y = arcsin x", "labpos": 0.72}],
  "points": [{"x": -1, "y": -1.5708, "label": "(-1, -pi/2)", "dx": 0.1, "dy": 0.15}, {"x": 1, "y": 1.5708, "label": "(1, pi/2)", "dx": -1.05, "dy": -0.45}],
  "caption": "Every input between -1 and 1 has exactly one output in the principal range. The steep endpoints reflect cos(y) = 0 there, not extra branches."
}
:::

:::example title="Read the outer range"
To evaluate $\sin^{-1}(\sin(3\pi/4))$, first compute $\sin(3\pi/4)=1/\sqrt{2}$. The principal angle in $[-\pi/2,\pi/2]$ having that sine is $\pi/4$, not $3\pi/4$. The outer function's range, not the original angle, makes the final decision.
:::

<!-- pagebreak -->
## Arctangent has horizontal asymptotes

For every real $x$, $\tan^{-1}x\in(-\pi/2,\pi/2)$. It is strictly increasing, odd, and approaches $\pm\pi/2$ as $x\to\pm\infty$. The asymptotes are limits, so the values $\pm\pi/2$ are never outputs.

:::diagram
{
  "type": "graph",
  "title": "Arctangent compresses every real input into a bounded angle",
  "xrange": [-8, 8], "yrange": [-2, 2], "xticks": [-8, -4, 0, 4, 8], "yticks": [-1.5708, 0, 1.5708], "yticklabels": ["-pi/2", "0", "pi/2"],
  "curves": [{"expr": "atan(x)", "label": "y = arctan x", "labpos": 0.78}],
  "hlines": [{"y": 1.5708, "label": "pi/2"}, {"y": -1.5708, "label": "-pi/2"}],
  "points": [{"x": 1, "y": 0.7854, "label": "(1, pi/4)", "dx": 0.25}, {"x": -1, "y": -0.7854, "label": "(-1, -pi/4)", "dx": 0.25, "dy": -0.45}],
  "caption": "Oddness appears as rotational symmetry about the origin. The horizontal asymptotes explain why arctan addition formulas must watch whether their sum crosses a branch boundary."
}
:::

For $\tan^{-1}a+\tan^{-1}b$, the naive formula $\tan^{-1}((a+b)/(1-ab))$ can differ from the actual sum by $\pi$. Compute the quadrant of the sum from the two principal angles before choosing the branch.

<!-- pagebreak -->
## Composition with sine creates a sawtooth

The graph of $y=\sin^{-1}(\sin x)$ repeats the branch correction in every interval. Near $x=0$, $y=x$; near $x=\pi$, $y=\pi-x$. It is not the unrestricted line $y=x$.

:::diagram
{
  "type": "graph",
  "title": "Branch selection folds the line y = x into a sawtooth",
  "xrange": [-6.4, 6.4], "yrange": [-2, 2], "xticks": [-6.2832, -3.1416, 0, 3.1416, 6.2832], "xticklabels": ["-2pi", "-pi", "0", "pi", "2pi"], "yticks": [-1.5708, 0, 1.5708], "yticklabels": ["-pi/2", "0", "pi/2"],
  "curves": [{"expr": "asin(sin(x))", "n": 1600, "label": "arcsin(sin x)", "labpos": 0.66}],
  "hlines": [{"y": 1.5708, "label": "upper branch bound"}, {"y": -1.5708, "label": "lower branch bound"}],
  "caption": "Each straight segment has slope +1 or -1. At odd multiples of pi/2 the nearest principal angle changes, producing the corners."
}
:::

A reliable algebraic method is to choose an angle $\phi\in[-\pi/2,\pi/2]$ with $\sin\phi=\sin x$. On $[-\pi/2+2k\pi,\pi/2+2k\pi]$, use $\phi=x-2k\pi$; on the complementary intervals use the reflected angle.

<!-- pagebreak -->
## A safe identity workflow

:::diagram
{
  "type": "flow",
  "title": "Branch before formula, verification after formula",
  "steps": [
    {"title": "Write domains and principal ranges", "detail": "Check inverse inputs and identify the interval in which every output angle must lie."},
    {"title": "Reduce the inner trigonometric value", "detail": "Use identities to obtain a sine, cosine or tangent value without losing sign information."},
    {"title": "Select the angle in the required branch", "detail": "Use a unit circle or graph; do not simply cancel a function with its inverse."},
    {"title": "Check a boundary and a numerical value", "detail": "Test endpoints and one interior input to catch a missing pi correction or an invalid formal identity."}
  ],
  "caption": "This routine handles compositions, addition identities, equations and extrema without memorising a separate trick for every branch case."
}
:::

:::example title="A boundary-aware equation"
For $2\sin^{-1}x=\pi/2$, the inverse input first requires $-1\leq x\leq1$. Dividing gives $\sin^{-1}x=\pi/4$, whose unique solution is $x=1/\sqrt{2}$. Substitution returns $\pi/2$. By contrast, squaring an equation involving two inverse angles can introduce candidates whose angle sum lies outside the possible principal range.
:::

:::key title="The one-line branch test"
After obtaining an answer, ask: **is this angle in the range of the outer inverse function?** If not, the algebraic expression may be equivalent up to a period, but it is not yet the requested principal value.
:::


<!-- pagebreak -->
## Worked synthesis: choose the angle before using the identity

Let $\alpha=\sin^{-1}(3/5)$. By the principal range, $\alpha\in(0,\pi/2)$, so $\cos\alpha=4/5$ is positive. Therefore
$$
\sin(2\alpha)=2\sin\alpha\cos\alpha=2\cdot\frac{3}{5}\cdot\frac{4}{5}=\frac{24}{25}.
$$
The sign of the cosine follows from the branch, not merely from the Pythagorean identity.

:::example title="An arctangent sum may need a pi correction"
Consider $S=\tan^{-1}1+\tan^{-1}2$. Both summands are positive, and $\tan^{-1}2>\pi/4$, so $\pi/2<S<\pi$. The addition formula gives $\tan S=(1+2)/(1-2)=-3$. In quadrant II, the required angle is therefore $S=\pi-\tan^{-1}3$, not the negative principal value $-\tan^{-1}3$.
:::

:::warn title="Equal tangents do not imply equal angles without a range"
The expressions $S$ and $-\tan^{-1}3$ have the same tangent but lie in different intervals. Periodic identities supply candidates; the principal ranges and the located quadrant select the answer.
:::

:::key title="Final branch audit"
Write the interval for every inverse angle before adding, doubling or applying another function. After simplifying, check both the numerical value and the interval of the result.
:::
