---
id: jee-04
part: jee
title: "Definite By Parts, Partial Fractions and Half-Angle"
---

## The Chapter 20 toolkit becomes an endpoint calculation

The definite method is unchanged: prepare, integrate and then subtract endpoint values. Keep any interval restriction visible until the final evaluation.

:::example title="Q17: by parts on a trigonometric interval"
$$
\int_0^\pi x\sin x\,dx
=\left[-x\cos x+\sin x\right]_0^\pi
=(\pi+0)-(0+0)=\pi.
$$
Although $x\sin x\geq0$ on $[0,\pi]$, this value is also the geometric area under that arch.
:::

:::example title="Q20: partial fractions with logarithmic endpoint values"
Using the Chapter 20 decomposition,
$$
\int_0^1\frac{dx}{(x+1)(x+2)}
=\left[\ln\left|\frac{x+1}{x+2}\right|\right]_0^1
=\ln\frac{2}{3}-\ln\frac{1}{2}=\ln\frac{4}{3}.
$$
The interval $[0,1]$ avoids both poles $-2$ and $-1$.
:::

## The half-angle substitution needs valid new limits

:::example title="S13 and Q35: the complete definite calculation"
For $t=\tan(x/2)$ on $[0,\pi/2]$,
$$
\cos x=\frac{1-t^2}{1+t^2},\qquad dx=\frac{2dt}{1+t^2},
$$
and the limits become $0\to0$ and $\pi/2\to1$. Hence
$$
\int_0^{\pi/2}\frac{dx}{2+\cos x}
=\int_0^1\frac{2}{3+t^2}dt
=\frac{2}{\sqrt{3}}\left[\tan^{-1}\frac{t}{\sqrt{3}}\right]_0^1.
$$
Since $\tan^{-1}(1/\sqrt{3})=\pi/6$,
$$
I=\frac{\pi}{3\sqrt{3}}\approx0.6045997881.
$$
:::

:::diagram
{
  "type": "table",
  "title": "Three definite techniques, three independent endpoint checks",
  "columns": ["Question", "Antiderivative or transformed form", "Value"],
  "rows": [
    ["Q17", "-x cos x + sin x", "pi"],
    ["Q20", "ln|(x+1)/(x+2)|", "ln(4/3)"],
    ["Q35", "2 arctan(t/sqrt(3))/sqrt(3)", "pi/(3 sqrt(3))"]
  ],
  "col_widths": [0.15, 0.57, 0.28],
  "caption": "The technique is selected from the integrand. The definite value is then forced by endpoints or transformed limits, not by memorising a numerical answer."
}
:::

:::warn title="An antiderivative on a branch is enough only if the whole interval stays on that branch"
The half-angle calculation uses $0\leq x\leq\pi/2$, safely inside $(-\pi,\pi)$. A larger interval reaching an odd multiple of $\pi$ would require branch and convergence analysis first.
:::
