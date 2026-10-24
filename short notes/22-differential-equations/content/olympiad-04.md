---
id: olympiad-04
part: olympiad
title: "Extension IV — Lagrange's Equation and Q38"
---

## Differentiate with x regarded as a function of p

A Lagrange equation has the form $y=xf(p)+g(p)$, where $p=y'$. On a branch that can be parametrized by $p$, differentiation with respect to $p$ gives
$$
p\frac{dx}{dp}=f(p)\frac{dx}{dp}+\left(xf'(p)+g'(p)\right).
$$
Away from $p=f(p)$, this is linear in $x(p)$. Constant-$p$ solutions excluded by that division must be recovered separately.

:::example title="S19 and Q38: the corrected differentiation"
For
$$
y=xp^2+1,
$$
differentiate with respect to $p$:
$$
p\frac{dx}{dp}=p^2\frac{dx}{dp}+2xp.
$$
Thus, away from $p=0$ for the derivation,
$$
(1-p)\frac{dx}{dp}=2x
\quad\Longrightarrow\quad
\frac{dx}{x}=\frac{2\,dp}{1-p}.
$$
Integration gives
$$
x=\frac{C}{(1-p)^2},
\qquad
y=1+\frac{Cp^2}{(1-p)^2},
$$
with $C\neq0$ and p restricted to an interval not crossing $1$. Direct parametric differentiation confirms $dy/dx=p$ and the original relation; the displayed family is also valid at an isolated parameter value $p=0$.
:::

## Restore the constant-p solutions

If $p=k$ is constant, then $y=kx+b$. Substitution into $y=xp^2+1$ forces $k=k^2$ and $b=1$. Hence the two additional solutions are
$$
y=1,\qquad y=x+1.
$$
Neither is obtained from the displayed parametric family by a finite nonzero C. These restore the branches omitted by the source's erroneous differentiation and incomplete final list.

:::diagram
{
  "type": "graph",
  "title": "Q38 with C=1: two parametric branches and two constant-p lines",
  "xrange": [-0.4, 4.2], "yrange": [-0.2, 10.5],
  "xticks": [0, 1, 2, 3, 4], "yticks": [0, 1, 2, 4, 6, 8, 10],
  "curves": [
    {"expr": "x+2-2*sqrt(x)", "from": 0.04, "to": 4, "color": "#16295C", "lw": 2.8},
    {"expr": "x+2+2*sqrt(x)", "from": 0.04, "to": 4, "color": "#0F766E", "lw": 2.8},
    {"expr": "1+0*x", "from": -0.4, "to": 4.2, "color": "#B91C1C", "lw": 2.1, "ls": "--"},
    {"expr": "x+1", "from": -0.4, "to": 4.2, "color": "#B91C1C", "lw": 2.1, "ls": "--"}
  ],
  "points": [{"x": 1, "y": 1, "label": "p=0", "dx": 0.15, "dy": 0.2}],
  "caption": "For C=1, eliminating p gives y=x+2 plus/minus 2 sqrt(x) on x>0. The red dashed lines y=1 and y=x+1 are separate solutions; the lower navy branch touches y=1 at (1,1)."
}
:::

:::warn title="The source equation p = 2xp + xp^2 p-prime is not differentiation of y = xp^2 + 1"
The product rule first gives p = p^2 + 2xp(dp/dx). Equivalently, the p-parametric calculation above avoids that error and keeps the linear equation in x(p) transparent.
:::
