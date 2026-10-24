---
id: olympiad-01
part: olympiad
title: "Extension I — Sequential Criteria and Nonexistence"
---

## Heine's criterion turns function limits into sequence limits

For a function defined near $a$,
$$
\lim_{x\to a}f(x)=L
$$
holds exactly when **every** sequence $x_n\to a$ with $x_n\ne a$ satisfies $f(x_n)\to L$. To prove nonexistence, two sequences with different output limits are enough. To prove existence, checking only a favourite sequence is not enough; the statement must cover every approach.

:::example title="Two sequences disprove the limit of sin(1/x)"
Take
$$
x_n=\frac{1}{n\pi},
\qquad
y_n=\frac{1}{\pi/2+2n\pi}.
$$
Both tend to $0$ from the right, but
$$
\sin\frac{1}{x_n}=\sin(n\pi)=0,
\qquad
\sin\frac{1}{y_n}=1.
$$
Thus $\sin(1/x)$ has no limit as $x\to0$. The oscillation is not a failure of algebra; it is verified nonexistence.
:::

:::diagram
{
  "type": "graph",
  "title": "Two marked sequences approach x=0 but keep different heights",
  "xrange": [0, 0.36], "yrange": [-1.3, 1.3],
  "xticks": [0, 0.1, 0.2, 0.3], "yticks": [-1, 0, 1],
  "curves": [{"expr": "sin(1/x)", "from": 0.012, "to": 0.36, "n": 4000}],
  "hlines": [{"y": 0}, {"y": 1}],
  "points": [
    {"x": 0.3183098862, "y": 0, "label": "zero sequence", "dx": -0.06, "dy": -0.25},
    {"x": 0.1591549431, "y": 0}, {"x": 0.1061032954, "y": 0}, {"x": 0.0795774715, "y": 0}, {"x": 0.0636619772, "y": 0},
    {"x": 0.1273239545, "y": 1, "label": "unit sequence", "dx": 0.015, "dy": 0.15, "color": "#B91C1C"},
    {"x": 0.0707355303, "y": 1, "color": "#B91C1C"}, {"x": 0.0489707517, "y": 1, "color": "#B91C1C"}, {"x": 0.0374482219, "y": 1, "color": "#B91C1C"}
  ],
  "caption": "The zero-height points use x_n=1/(n pi); the unit-height points use y_n=1/(pi/2+2n pi). Their inputs all approach 0."
}
:::

## Dense sets can make every approach fail

Define $D(x)=1$ for rational $x$ and $D(x)=0$ for irrational $x$. At any real $a$, rationals and irrationals are both dense, so there are sequences $q_n\to a$ and $r_n\to a$ with
$$
D(q_n)=1,\qquad D(r_n)=0.
$$
Therefore the Dirichlet function has no limit at any point. This is stronger than having a single jump or removable discontinuity.

## A substitution can certify every sequence at once

For $x\ne0$, put $u=1/x^2$. Whenever $x_n\to0$ with $x_n\ne0$, we have $u_n=1/x_n^2\to\infty$, and hence
$$
e^{-1/x_n^2}=e^{-u_n}\longrightarrow0.
$$
Heine's criterion now proves the two-sided limit $e^{-1/x^2}\to0$. Assigning the value $0$ at $x=0$ therefore makes this function continuous there.

:::key title="Existence and nonexistence need different amounts of evidence"
One sequence can never prove a full function limit. One pair of sequences can disprove it. For a positive proof, use an estimate valid on a whole punctured neighbourhood or a substitution valid for every admissible sequence.
:::
