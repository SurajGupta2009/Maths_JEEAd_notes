---
id: jee-03
part: jee
title: "Variables Separable — Integrate, Then Apply the IVP"
---

## Put each variable on one side

For $y'=f(x)g(y)$, separation on a region where $g(y)\neq0$ gives
$$
\frac{dy}{g(y)}=f(x)\,dx.
$$
Integrate both sides, apply the initial condition, and only then choose a branch. Constant solutions with $g(y)=0$ must be checked separately before dividing.

:::diagram
{
  "type": "flow",
  "title": "A safe separation routine",
  "steps": [
    {"title": "Factor", "detail": "Write the slope as a product of an x-factor and a y-factor."},
    {"title": "Separate", "detail": "Move the nonzero y-factor with dy and the x-factor with dx."},
    {"title": "Integrate", "detail": "Include one combined arbitrary constant."},
    {"title": "Select", "detail": "Use the IVP to fix the constant, branch and maximal interval."}
  ],
  "caption": "If a division assumes y is nonzero, test the zero function or equilibrium separately."
}
:::

:::example title="S3 and Q5: choose the positive square-root branch"
From $y'=x/y$,
$$
y\,dy=x\,dx
\quad\Longrightarrow\quad
y^2=x^2+C.
$$
Since $y(0)=1$, $C=1$. Continuity from the positive initial value selects
$$
y=\sqrt{x^2+1},\qquad {y(1)=\sqrt{2}}.
$$
The negative square root belongs to a different initial condition, not to this IVP. This solution is defined on $(-\infty,\infty)$.
:::

:::example title="S4/Q6 and P3/Q7: exponential separation"
For $y'=y$, $y(0)=1$, separation for $y\neq0$ gives $\ln|y|=x+C$, hence $y=e^x$ and ${y(1)=e}$. The zero function is another solution of the general equation but fails this IVP.

For $y'=2xy$, $y(0)=3$,
$$
\frac{dy}{y}=2x\,dx
\quad\Longrightarrow\quad
y=3e^{x^2},\qquad {y(1)=3e}.
$$
Both IVP solutions remain on the positive branch for all real $x$.
:::

:::example title="P4 and Q8: separate an exponential of a difference"
Since $e^{x-y}=e^xe^{-y}$,
$$
e^y\,dy=e^x\,dx
\quad\Longrightarrow\quad e^y=e^x+C.
$$
The condition $y(0)=0$ gives $1=1+C$, so $C=0$ and ${y=x}$ on $(-\infty,\infty)$. Direct verification is immediate: $y'=1=e^{x-y}$.
:::

:::warn title="The constant belongs after integration, not after branch selection"
Adding a new constant after taking a square root or exponential usually describes a different family. Carry one constant through the algebra and let the initial condition determine it.
:::
