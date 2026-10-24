---
id: olympiad-04
part: olympiad
title: "Frullani Integrals and the Sine-Difference Correction"
---

## Scaling two copies of the same function

Suppose $f$ is continuous with finite limiting values $f(0)$ and $f(\infty)$. For $a,b>0$, Frullani's formula is
$$
\int_0^\infty\frac{f(ax)-f(bx)}{x}dx
=(f(0)-f(\infty))\ln\frac{b}{a}.
$$
Indeed, after $u=ax$ and $u=bx$ in the two pieces of a finite cutoff integral,
$$
\int_\varepsilon^R\frac{f(ax)-f(bx)}{x}dx
=\int_{a\varepsilon}^{b\varepsilon}\frac{f(u)}{u}du
-\int_{aR}^{bR}\frac{f(u)}{u}du.
$$
The endpoint limiting values produce the stated logarithm.

:::example title="S17/Q34 and P17/Q38: exponential Frullani integrals"
For $f(t)=e^{-t}$, $f(0)=1$ and $f(\infty)=0$. Therefore
$$
\int_0^\infty\frac{e^{-x}-e^{-2x}}{x}dx=\ln2,
$$
and
$$
\int_0^\infty\frac{e^{-3x}-e^{-5x}}{x}dx=\ln\frac{5}{3}
\approx0.5108256238.
$$
More generally, for $x>0$, $\ln x=\int_0^\infty(e^{-t}-e^{-xt})/t\,dt$.
:::

## Additional conditional example: a cosine difference

For $a,b>0$, $\cos(ax)$ has no limit at infinity, so the basic finite-$f(\infty)$ statement does not directly apply. Introduce $\delta>0$ and use
$$
\frac{\cos(ax)-\cos(bx)}{x}=\int_a^b\sin(tx)dt.
$$
Fubini's theorem for the damped integral gives
$$
I_\delta=\int_a^b\frac{t}{\delta^2+t^2}dt
=\frac{1}{2}\ln\frac{\delta^2+b^2}{\delta^2+a^2}.
$$
Dirichlet convergence and Abel continuity as $\delta\to0^+$ then give
$$
\int_0^\infty\frac{\cos(ax)-\cos(bx)}{x}dx=\ln\frac{b}{a}.
$$

## Source-warning correction: the sine difference converges to zero

For the additional sine-difference example,
$$
\frac{\sin(ax)-\sin(bx)}{x}=-\int_a^b\cos(tx)dt.
$$
With the same damping,
$$
I_\delta=-\int_a^b\frac{\delta}{\delta^2+t^2}dt
=-\left[\tan^{-1}\frac{t}{\delta}\right]_a^b\longrightarrow0.
$$
Dirichlet's test proves convergence of the original improper integral, and Abel continuity identifies its value as $0$. The source's claim that this difference diverges merely because sine has no limiting value at infinity is incorrect.

:::diagram
{
  "type": "graph",
  "title": "A cosine Frullani integrand with a1 and b2",
  "xrange": [0, 12], "yrange": [-0.55, 1.35],
  "xticks": [0, 2, 4, 6, 8, 10, 12], "yticks": [-0.5, 0, 0.5, 1],
  "fills": [
    {"from": 0.05, "to": 4, "y1": 0, "y2": "(cos(x)-cos(2*x))/x", "color": "#F6C445", "alpha": 0.25}
  ],
  "curves": [
    {"expr": "(cos(x)-cos(2*x))/x", "from": 0.05, "to": 12}
  ],
  "caption": "For a=1 and b=2, the full conditional integral is ln(2). The shaded finite window is illustrative; convergence and the exact value come from the damped calculation, not the plot."
}
:::

:::warn title="No f(infinity) does not automatically mean divergence"
The finite-limit Frullani theorem has hypotheses, but failure of one shortcut does not settle convergence. The exponential source questions satisfy the hypotheses directly; oscillatory differences require a separate convergence argument and can converge conditionally.
:::
