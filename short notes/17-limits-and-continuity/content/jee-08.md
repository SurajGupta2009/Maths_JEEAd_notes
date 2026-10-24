---
id: jee-08
part: jee
title: "The Intermediate Value Theorem and Roots"
---

## Continuity prevents an interval from being skipped

If $f$ is continuous on $[a,b]$ and $N$ lies between $f(a)$ and $f(b)$, then some $c\in[a,b]$ satisfies $f(c)=N$. In particular, **Bolzano's root theorem** says
$$
f(a)f(b)<0\quad\Longrightarrow\quad f(c)=0\text{ for some }c\in(a,b).
$$
The proof can be organized by bisection: repeatedly keep a half-interval whose endpoints straddle the target. Nested intervals locate a point where continuity forces the target value.

:::example title="A sign change proves a root, and monotonicity makes it unique"
For $f(x)=x^3+x-1$,
$$
f(0)=-1<0,\qquad f(1)=1>0.
$$
Thus a root lies in $(0,1)$. Moreover, $x^3$ and $x$ are strictly increasing on $[0,1]$, so their sum is strictly increasing and the root there is unique. Numerically it is approximately $0.6823278038$.

For a first bisection step,
$$
f\left(\frac{1}{2}\right)=-\frac{3}{8}<0,
\qquad
f\left(\frac{3}{4}\right)=\frac{11}{64}>0,
$$
so the root lies in $(1/2,3/4)$.
:::

:::diagram
{
  "type": "graph",
  "title": "A continuous curve cannot avoid the zero level",
  "xrange": [-0.05, 1.05], "yrange": [-1.2, 1.2],
  "xticks": [0, 0.5, 0.682328, 1], "xticklabels": ["0", "1/2", "c", "1"],
  "yticks": [-1, 0, 1],
  "curves": [{"expr": "x**3+x-1", "from": 0, "to": 1, "label": "f(x)=x^3+x-1", "labpos": 0.60, "label_dx": -0.35, "label_dy": 0.15}],
  "hlines": [{"y": 0, "label": "N = 0"}],
  "points": [
    {"x": 0, "y": -1, "label": "f(0)=-1", "dx": 0.05, "dy": -0.18},
    {"x": 1, "y": 1, "label": "f(1)=1", "dx": -0.45, "dy": 0.12},
    {"x": 0.6823278038, "y": 0, "label": "root ~0.682328", "dx": -0.20, "dy": 0.15, "color": "#B91C1C"}
  ],
  "caption": "Opposite endpoint signs force at least one crossing. On this interval strict increase also rules out a second crossing."
}
:::

## Build an auxiliary function for existence questions

The equation $\cos x=x$ becomes $g(x)=\cos x-x=0$. Since
$$
g(0)=1>0,\qquad g\left(\frac{\pi}{2}\right)=-\frac{\pi}{2}<0,
$$
a solution lies in $(0,\pi/2)$; its approximate value is $0.7390851332$.

The same construction proves a fixed-point theorem. If $f:[0,1]\to[0,1]$ is continuous, put $g(x)=f(x)-x$. Then
$$
g(0)=f(0)\geq0,\qquad g(1)=f(1)-1\leq0.
$$
If either endpoint is zero, that endpoint is fixed; otherwise IVT gives an interior zero of $g$. Hence some $c$ satisfies $f(c)=c$.

:::warn title="IVT gives existence under continuity, not a converse"
A sign change does not say how many roots exist unless monotonicity or another argument is added. Conversely, equal endpoint signs do not prove there is no root: $x^2$ has equal positive values at $-1$ and $1$ but has a root at $0$. IVT can also fail without continuity.
:::
