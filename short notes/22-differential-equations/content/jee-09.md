---
id: jee-09
part: jee
title: "Constant-Coefficient Second-Order Equations"
---

## The characteristic equation controls the solution shape

For $ay''+by'+cy=0$, try $y=e^{rx}$. Since each derivative multiplies by another $r$,
$$
ar^2+br+c=0.
$$
Two independent real solutions form the general solution. Initial values determine their constants; they do not change the characteristic roots.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "Three root patterns, three independent-solution templates",
  "columns": ["Roots", "Real general solution", "Key point"],
  "col_widths": [0.22, 0.48, 0.30],
  "rows": [
    ["r1, r2 real", "A e^(r1 x)+B e^(r2 x)", "Two rates"],
    ["Repeated r", "(A+Bx) e^(rx)", "x gives independence"],
    ["u +/- iv", "e^(ux)(A cos vx+B sin vx)", "Envelope + oscillation"]
  ],
  "caption": "For complex roots u+/-iv, v is nonzero. A repeated root without the x companion would supply only one independent solution."
}
:::

:::example title="P9 and Q21: pure oscillation"
For $y''+y=0$, $r^2+1=0$, so $r=\pm i$ and
$$
y=A\cos x+B\sin x.
$$
The conditions $y(0)=0$ and $y'(0)=1$ give $A=0$, $B=1$. Hence $y=\sin x$ on $(-\infty,\infty)$. Here there is no exponential envelope, so this solution is genuinely periodic with period $2\pi$.
:::

:::example title="S11 and Q22: two distinct real roots"
For $y''-3y'+2y=0$,
$$
r^2-3r+2=(r-1)(r-2),
\qquad y=Ae^x+Be^{2x}.
$$
The initial conditions give $A+B=0$ and $A+2B=1$, hence $A=-1$, $B=1$. Therefore
$$
y=e^{2x}-e^x,
\qquad y(1)=e^2-e.
$$
Differentiate once to verify $y'(0)=2-1=1$.
:::

:::example title="S12 and Q23: repeated root"
For $y''+4y'+4y=0$, $r=-2$ is repeated, so
$$
y=(A+Bx)e^{-2x}.
$$
Now $y(0)=A=1$ and $y'=(B-2A-2Bx)e^{-2x}$, so $y'(0)=B-2=0$ gives $B=2$. Thus
$$
y=(1+2x)e^{-2x},
\qquad y(1)=3e^{-2}.
$$
:::

:::warn title="Do not write two copies of the same exponential for a repeated root"
The functions $e^{rx}$ and $xe^{rx}$ are independent; $e^{rx}$ and another $e^{rx}$ are not. Their Wronskian is tested in Extension I.
:::
