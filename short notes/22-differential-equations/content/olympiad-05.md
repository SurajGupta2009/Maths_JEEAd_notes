---
id: olympiad-05
part: olympiad
title: "Extension V — Riccati Equations from a Known Solution"
---

## One particular solution linearizes the remaining family

For
$$
y'=q_0(x)+q_1(x)y+q_2(x)y^2,
$$
suppose $y_1$ is a known particular solution. On a branch with $y\neq y_1$, put $y=y_1+1/u$. Subtracting the equation satisfied by $y_1$ yields
$$
u'+\left(q_1+2q_2y_1\right)u=-q_2.
$$
This linear equation supplies the non-$y_1$ branches. The known solution itself must still be listed separately unless a finite constant happens to reproduce it.

:::example title="S20 and Q39: y = 0 is not recovered by finite C"
Here $y'=y^2-y$ and $y_1=0$. Put $y=1/u$:
$$
-\frac{u'}{u^2}=\frac{1}{u^2}-\frac{1}{u}
\quad\Longrightarrow\quad u'-u=-1.
$$
With integrating factor $e^{-x}$, $u=1+Ce^x$, so
$$
y=\frac{1}{1+Ce^x}.
$$
For $C<0$, the denominator vanishes at $x=\ln(-1/C)$, so each solution interval must stay on one side of that pole. For $C\geq0$, the formula is defined on $(-\infty,\infty)$. The separate equilibrium $y=0$ is not attained for any finite C; $C=0$ instead gives the other equilibrium $y=1$.
:::

:::diagram
{
  "type": "graph",
  "title": "Q39: positive-C branches connect the two equilibria",
  "xrange": [-4, 4], "yrange": [-0.12, 1.16],
  "xticks": [-4, -3, -2, -1, 0, 1, 2, 3, 4], "yticks": [0, 0.25, 0.5, 0.75, 1],
  "curves": [
    {"expr": "1/(1+exp(x))", "from": -4, "to": 4, "color": "#16295C", "lw": 2.8},
    {"expr": "1/(1+3*exp(x))", "from": -4, "to": 4, "color": "#0F766E", "lw": 2.8},
    {"expr": "0*x", "from": -4, "to": 4, "color": "#B91C1C", "lw": 1.8, "ls": "--"},
    {"expr": "1+0*x", "from": -4, "to": 4, "color": "#B91C1C", "lw": 1.8, "ls": "--"}
  ],
  "points": [{"x": 0, "y": 0.5, "label": "C=1", "dx": 0.15, "dy": 0.08}, {"x": 0, "y": 0.25, "label": "C=3", "dx": 0.15, "dy": -0.15}],
  "caption": "For C>0, 1/(1+C exp(x)) decreases from 1 toward 0. The limiting equilibria are genuine separate solutions; approaching one as C grows is not the same as attaining it for finite C."
}
:::

:::example title="P15 and Q40: a Gaussian integrating factor and another omitted equilibrium"
For $y'=x(y^2-1)$ with $y_1=1$, put $y=1+1/u$. Then
$$
u'+2xu=-x,
\qquad
(ue^{x^2})'=-xe^{x^2}.
$$
Therefore
$$
u=Ce^{-x^2}-\frac{1}{2},
\qquad
y=1+\frac{1}{Ce^{-x^2}-1/2}.
$$
The separate solution $y=1$ is not obtained for finite C. The other equilibrium is $y=-1$, obtained with $C=0$. Every branch must avoid zeros of $Ce^{-x^2}-1/2$; when $C>0$ and $2C\geq1$, these occur at $x=\pm\sqrt{\ln(2C)}$, with the two signs coinciding when $C=1/2$.
:::

:::warn title="Taking C to infinity is a limit, not a member of the finite-C family"
The source uses a large-C limit to motivate the omitted Riccati solutions. The corrected general answer lists those equilibria explicitly and states intervals away from denominator zeros.
:::
