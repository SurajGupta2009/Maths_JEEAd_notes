---
id: olympiad-03
part: olympiad
title: "Extension III — Existence, Uniqueness and Delayed Solutions"
---

## Continuity and Lipschitz continuity have different jobs

For $y'=f(x,y)$, $y(x_0)=y_0$, local continuity of $f$ gives a local existence theorem. Picard–Lindelöf adds a Lipschitz condition in $y$ near the initial point and then guarantees local uniqueness. A continuous partial derivative $f_y$ on a nearby closed rectangle is a common sufficient way to obtain that Lipschitz condition.

Failure of a sufficient uniqueness hypothesis does not itself prove non-uniqueness. The examples below prove non-uniqueness by constructing distinct solutions explicitly.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "What the standard local statements do and do not assert",
  "columns": ["Hypothesis", "Conclusion", "Caution"],
  "col_widths": [0.34, 0.28, 0.38],
  "rows": [
    ["f continuous", "Local existence", "No uniqueness asserted"],
    ["f continuous + y-Lipschitz", "Local uniqueness", "Theorem is local"],
    ["f_y unbounded", "Lipschitz test fails", "Not a non-uniqueness proof"],
    ["Two solutions verified", "Non-uniqueness", "Check joining derivatives"]
  ],
  "caption": "The examples use real-valued differential equations and check both one-sided derivatives where a formula changes."
}
:::

:::example title="S18 and Q36: sqrt(y) permits arbitrary waiting times"
One solution of $y'=\sqrt{y}$, $y(0)=0$ is $y=0$ for all $x$. Another is zero for $x\leq0$ and $x^2/4$ for $x>0$. For the latter,
$$
y'=\frac{x}{2}=\sqrt{\frac{x^2}{4}}=\sqrt{y}
$$
when $x>0$, and both one-sided derivatives at $0$ are $0$. More generally, for any $a\geq0$, take zero for $x\leq a$ and $(x-a)^2/4$ for $x>a$. All satisfy the same IVP.

Since $f_y=1/(2\sqrt{y})$ is unbounded as $y\to0^+$, the required Lipschitz condition near zero is absent.
:::

:::example title="P14 and Q37: a cube-root equation with departure at x = 1"
Define $y=0$ for $x\leq1$ and
$$
y=\left(\frac{2(x-1)}{3}\right)^{3/2}\qquad x>1.
$$
On the departing branch, put $u=2(x-1)/3$. Then
$$
y=u^{3/2},\qquad y'=u^{1/2},\qquad y^{1/3}=u^{1/2},
$$
so $y'=y^{1/3}$. At $x=1$, both one-sided derivatives are $0$, and the initial condition $y(0)=0$ holds. Here $f_y=y^{-2/3}/3$ is unbounded near $0$, again defeating the Lipschitz hypothesis.
:::

:::warn title="Real powers and joining points require domain care"
For Q36, sqrt(y) requires y nonnegative. For Q37, the displayed nonnegative departing branch uses a real cube root. In both examples the derivative at the waiting-time endpoint must be checked, not assumed from the formulas on either side.
:::
