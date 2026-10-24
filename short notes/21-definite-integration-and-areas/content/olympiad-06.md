---
id: olympiad-06
part: olympiad
title: "Q37 — The Dirichlet Integral, Conditional but Exact"
---

## First evaluate the damped parameter family

For $t>0$, define
$$
J(t)=\int_0^\infty e^{-tx}\frac{\sin x}{x}dx,
$$
with continuous value $1$ for $\sin x/x$ at $x=0$. Local domination permits differentiation:
$$
J'(t)=-\int_0^\infty e^{-tx}\sin x\,dx=-\frac{1}{1+t^2}.
$$
Since $J(t)\to0$ as $t\to\infty$,
$$
J(t)=\int_t^\infty\frac{ds}{1+s^2}
=\frac{\pi}{2}-\tan^{-1}t.
$$
This proves the damped formula without setting $t=0$ prematurely.

## Convergence comes from oscillation and a decreasing envelope

The expression $\sin x/x$ has continuous extension $1$ at $x=0$, so only infinity is improper. For $1<R<S$, integration by parts gives
$$
\int_R^S\frac{\sin x}{x}dx
=\left[-\frac{\cos x}{x}\right]_R^S-\int_R^S\frac{\cos x}{x^2}dx.
$$
The boundary terms are $O(1/R)$ and the remaining absolute integral is at most $\int_R^\infty x^{-2}dx=1/R$. Thus the finite integrals have a limit.

The convergence is not absolute. On each interval $[n\pi+\pi/6,n\pi+5\pi/6]$, $|\sin x|\geq1/2$, so the contribution to $\int|\sin x|/x\,dx$ is at least a constant multiple of $1/(n+1)$. The harmonic series diverges.

## Abel continuity supplies the exact value

For $\delta>0$, the calculation above gives
$$
I(\delta)=\int_0^\infty e^{-\delta x}\frac{\sin x}{x}dx
=\frac{\pi}{2}-\tan^{-1}\delta.
$$
Because the undamped improper integral converges, Abel continuity gives Q37:
$$
\int_0^\infty\frac{\sin x}{x}dx
=\lim_{\delta\to0^+}I(\delta)=\frac{\pi}{2}.
$$
This is the missing justification for inserting a convergence factor and then removing it.

:::diagram
{
  "type": "graph",
  "title": "Alternating Dirichlet arches have a finite signed sum",
  "xrange": [0, 20], "yrange": [-0.32, 1.10],
  "xticks": [0, 3.1415926536, 6.2831853072, 9.4247779608, 12.5663706144, 15.7079632679, 18.8495559215],
  "yticks": [-0.2, 0, 0.5, 1],
  "fills": [
    {"from": 0.001, "to": 3.1415926536, "y1": 0, "y2": "sin(x)/x", "color": "#F6C445", "alpha": 0.28},
    {"from": 3.1415926536, "to": 6.2831853072, "y1": 0, "y2": "sin(x)/x", "color": "#B91C1C", "alpha": 0.14},
    {"from": 6.2831853072, "to": 9.4247779608, "y1": 0, "y2": "sin(x)/x", "color": "#F6C445", "alpha": 0.20},
    {"from": 9.4247779608, "to": 12.5663706144, "y1": 0, "y2": "sin(x)/x", "color": "#B91C1C", "alpha": 0.12}
  ],
  "curves": [{"expr": "sin(x)/x", "from": 0.001, "to": 20}],
  "points": [{"x": 0, "y": 1, "label": "continuous value 1", "dx": 0.5, "dy": -0.16}],
  "caption": "Alternating arches make the improper integral converge conditionally to pi/2. Their absolute areas do not have a finite sum, and the graph cannot by itself establish the exact limit."
}
:::

:::warn title="Conditional convergence is not absolute convergence"
The exact value $\pi/2$ concerns the ordered improper integral $\lim_{R\to\infty}\int_0^R\sin x/x\,dx$. It does not assert that $\int_0^\infty|\sin x/x|dx$ is finite, and it does not permit arbitrary rearrangement of positive and negative area.
:::
