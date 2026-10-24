---
id: olympiad-01
part: olympiad
title: "Wallis Reduction and the Wallis Product"
---

## A recurrence converts powers into two base cases

For $n\geq0$, define
$$
I_n=\int_0^{\pi/2}\sin^nx\,dx.
$$
For $n\geq2$, integration by parts gives
$$
I_n=(n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2x\,dx
=(n-1)(I_{n-2}-I_n),
$$
so
$$
I_n=\frac{n-1}{n}I_{n-2},\qquad I_0=\frac{\pi}{2},\qquad I_1=1.
$$
Consequently,
$$
I_{2m}=\frac{(2m-1)!!}{(2m)!!}\frac{\pi}{2},
\qquad
I_{2m+1}=\frac{(2m)!!}{(2m+1)!!}.
$$

:::example title="An odd-power check, followed by S15 and Q30"
For the additional odd-power check $\sin^5x$,
$$
I_5=\frac{4}{5} I_3=\frac{4}{5}\cdot\frac{2}{3} I_1=\frac{8}{15}.
$$
For S15 and Q30, the requested power is $\sin^6x$:
$$
I_6=\frac{5}{6}\cdot\frac{3}{4}\cdot\frac{1}{2}\cdot\frac{\pi}{2}
=\frac{5\pi}{32}.
$$
:::

:::diagram
{
  "type": "table",
  "title": "Wallis reduction separates even and odd powers",
  "columns": ["Power or index", "Reduction route", "Exact value"],
  "rows": [
    ["n=0", "base integral of 1", "pi/2"],
    ["n=1", "base integral of sin x", "1"],
    ["n=5", "(4/5)(2/3) I1", "8/15"],
    ["n=6", "(5/6)(3/4)(1/2) I0", "5 pi/32"],
    ["even 2m", "double-factorial form times pi/2", "decreasing in m"],
    ["odd 2m+1", "double-factorial form", "decreasing in m"]
  ],
  "col_widths": [0.20, 0.48, 0.32],
  "caption": "The recurrence is exact for every n>=2. It also supplies the ratios needed to prove the infinite Wallis product rather than merely quoting it."
}
:::

## The infinite product follows by squeezing adjacent integrals

On $[0,\pi/2]$, $0\leq\sin x\leq1$, hence
$$
I_{2m+1}\leq I_{2m}\leq I_{2m-1}.
$$
The recurrence gives $I_{2m-1}/I_{2m+1}=(2m+1)/(2m)\to1$, so $I_{2m}/I_{2m+1}\to1$. Substituting the closed forms and rearranging yields Wallis's product:
$$
\frac{\pi}{2}
=\lim_{m\to\infty}
\frac{2}{1}\frac{2}{3}\frac{4}{3}\frac{4}{5}
\cdots\frac{2m}{2m-1}\frac{2m}{2m+1}.
$$
This is a convergent infinite product, not an assertion that any finite partial product equals $\pi/2$.

:::warn title="Double factorials skip every other factor"
For example, $6!!=6\cdot4\cdot2$ and $5!!=5\cdot3\cdot1$. They do not mean repeated factorial operations. Always retain the base factor $\pi/2$ for even powers and omit it for odd powers.
:::
