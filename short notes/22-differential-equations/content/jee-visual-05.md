---
id: jee-visual-05
part: jee
title: "Visual Lab 5 — One IVP, Infinitely Many Departures"
---

## The zero solution can wait before peeling away

:::diagram
{
  "type": "graph",
  "title": "Three solutions of y-prime = sqrt(y), y(0)=0",
  "xrange": [-1, 4], "yrange": [-0.18, 3.2],
  "xticks": [-1, 0, 1, 2, 3, 4], "yticks": [0, 1, 2, 3],
  "slope_fields": [{"expr": "sqrt(y)", "xrange": [-1, 4], "yrange": [0, 3], "nx": 16, "ny": 10, "length": 0.14}],
  "curves": [
    {"expr": "0*x", "from": -1, "to": 4, "color": "#0F766E", "lw": 3.2},
    {"expr": "x**2/4", "from": 0, "to": 3.45, "color": "#16295C", "lw": 2.8},
    {"expr": "(x-1)**2/4", "from": 1, "to": 4, "color": "#B91C1C", "lw": 2.8, "ls": "--"}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "same IVP", "dx": 0.12, "dy": 0.14},
    {"x": 1, "y": 0, "label": "delayed departure", "dx": 0.12, "dy": 0.14}
  ],
  "caption": "Teal is the zero solution; navy departs at 0; red remains zero until x=1 and then follows (x-1)^2/4. Replacing 1 by any nonnegative delay gives another solution."
}
:::

## Differentiability includes the joining point

For delay $a\geq0$, the departing formula is $y=(x-a)^2/4$ for $x>a$ and $y=0$ for $x\leq a$. On the right,
$$
y'=\frac{x-a}{2}=\sqrt{y}.
$$
At $x=a$, both one-sided derivatives are $0$, and the right-hand side is also $0$. Hence the joined function solves the IVP on the whole real line.

:::example title="Why the uniqueness theorem does not object"
For $f(y)=\sqrt{y}$ and $y>0$,
$$
f_y=\frac{1}{2\sqrt{y}},
$$
which is unbounded as $y\to0^+$. Therefore $f$ is not Lipschitz on a neighbourhood of $y=0$. Continuity still permits existence; the missing Lipschitz hypothesis removes the uniqueness guarantee. The negative plotting margin is only visual space: real $\sqrt{y}$ requires $y\geq0$.
:::
