---
id: jee-11
part: jee
title: "Model Audits — Ellipse and Rectangle-with-Semicircle"
---

## Parametrise the constraint before differentiating

For a rectangle inscribed in $x^2/a^2+y^2/b^2=1$, let the first-quadrant corner be $(a\cos t,b\sin t)$ with $0\leq t\leq\pi/2$. The full area is
$$
A(t)=4ab\sin t\cos t=2ab\sin2t.
$$
The maximum is $2ab$ at $t=\pi/4$, with corner $(a/\sqrt{2},b/\sqrt{2})$. Equivalently, with corner $(x,y)$,
$$
A=4bx\sqrt{1-\frac{x^2}{a^2}},
$$
and $A^2$ can be maximised as a quadratic in $x^2$.

:::example title="The classic window model has a feasible optimum"
A rectangle of height $h$ and width $2r$ is topped by a semicircle of radius $r$. Its perimeter is
$$
2h+2r+\pi r=10,
$$
so $h=5-r(1+\pi/2)$ and feasibility requires $h\geq0$, hence
$$
0\leq r\leq\frac{10}{2+\pi}.
$$
Its area, including the semicircle, is
$$
A=2rh+\frac{1}{2}\pi r^2
=10r-\left(2+\frac{\pi}{2}\right)r^2.
$$
Therefore
$$
A'(r)=10-(4+\pi)r,
\qquad r_*=\frac{10}{4+\pi}.
$$
At this point $h=5-r_*(1+\pi/2)=r_*$, so the optimum is feasible. Since $A''=-(4+\pi)<0$ and the endpoint areas are smaller,
$$
A_{\max}=\frac{50}{4+\pi},\qquad h=r=\frac{10}{4+\pi}.
$$
:::

:::diagram
{
  "type": "table",
  "title": "Three optimisation models, each with its domain retained",
  "columns": ["Model", "Feasible reduction", "Verified optimum"],
  "rows": [
    ["Open box", "0<=x<=6", "x=2, V=128"],
    ["Ellipse rectangle", "x=a cos t, y=b sin t", "A_max=2ab"],
    ["Classic window", "0<=r<=10/(2+pi)", "r=h=10/(4+pi)"]
  ],
  "col_widths": [0.25, 0.39, 0.36],
  "caption": "The window calculation uses the semicircle arc in the perimeter and its area in the objective. It does not cancel the semicircle's area term."
}
:::

## Audit the source algebra, not only the numerical answer

A tempting incorrect step is to claim that the rectangular area $2rh$ and semicircle area $\pi r^2/2$ cancel. They do not. After substituting the perimeter relation, the correct coefficient of $r^2$ is $-(2+\pi/2)$, and the resulting vertex satisfies the height constraint.

:::warn title="A defect is corrected by returning to the model"
The canonical source's assertion that this window optimum is infeasible is wrong. Recompute both the reduced objective and the feasible interval; the independent check in this chapter also verifies the optimum by a completed square.
:::
