---
id: jee-11
part: jee
title: "Growth, Cooling and Reduction for Autonomous Equations"
---

## Model the rate statement before integrating

Exponential models arise when a relative rate is constant: $P'/P=k$ gives $P=P_0e^{kx}$. Newton cooling instead says that the temperature excess above the environment decays exponentially. An autonomous second-order equation has no explicit $x$; the substitution $p=y'$, $y''=p\,dp/dy$ lowers its order.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "Translate each verbal or structural clue into a differential equation",
  "columns": ["Clue", "Model", "Consequence"],
  "col_widths": [0.30, 0.34, 0.36],
  "rows": [
    ["Relative rate k", "P' = kP", "P = P0 e^(kx)"],
    ["Cooling to Ta", "T' = -k(T-Ta)", "Excess decays"],
    ["No explicit x", "p = y'", "y'' = p dp/dy"],
    ["Divide by p or y", "Nonzero branch", "Test equilibria separately"]
  ],
  "caption": "A yearly percentage described as discrete compounding is not the same convention as a continuous relative growth rate."
}
:::

:::example title="S14 and Q26: cooling differences can be squared"
Let $T$ be temperature and $k>0$. Newton's law gives
$$
T-20=80e^{-kx}.
$$
After $10$ minutes, $60-20=80e^{-10k}$, so $e^{-10k}=1/2$. After another $10$ minutes,
$$
T(20)=20+80(e^{-10k})^2
=20+80\cdot\frac{1}{4}=40^\circ\mathrm{C}.
$$
The temperature excess halves every $10$ minutes; the absolute temperature does not.
:::

:::example title="P10 and Q27: state the continuous-growth convention"
If “$10\%$ per year” means the continuous relative rate $P'/P=0.1$, then
$$
P(t)=1000e^{0.1t},
\qquad P(10)=1000e\approx2718.2818.
$$
This is the source's intended answer. If instead growth occurs by annual discrete compounding, the model is $P(t)=1000(1.1)^t$ and $P(10)=1000(1.1)^{10}\approx2593.7425$. The modelling convention changes the answer.
:::

:::example title="S16 and Q31: reduce yy'' = (y')^2"
Put $p=y'$. On a branch with $y\neq0$ and $p\neq0$,
$$
yp\frac{dp}{dy}=p^2
\quad\Longrightarrow\quad
\frac{dp}{p}=\frac{dy}{y}.
$$
Thus $p=Cy$, so $y'=Cy$ and $y=Ae^{Cx}$ on a nonzero branch. The initial data $y(0)=1$, $y'(0)=1$ give $A=C=1$, hence
$$
y=e^x.
$$
The separation also excludes constant solutions from the derivation; direct substitution shows that every constant $y=A$ solves the original equation, including $y=0$. None changes this IVP.
:::

:::warn title="y'' is not dp/dx after choosing p(y)"
When $p=y'$ is regarded as a function of $y$, the chain rule gives $y''=dp/dx=(dp/dy)(dy/dx)=p\,dp/dy$.
:::
