---
id: jee-12
part: jee
title: "Damping — Under, Critical and Over"
---

## The discriminant determines the regime

For $\omega>0$ and $\zeta\geq0$, write
$$
y''+2\zeta\omega y'+\omega^2y=0.
$$
The roots are $-\zeta\omega\pm\omega\sqrt{\zeta^2-1}$. Negative real parts produce decay, but only complex roots produce oscillation.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "Damping classification from zeta and the characteristic roots",
  "columns": ["Regime", "Roots", "Behaviour"],
  "col_widths": [0.27, 0.33, 0.40],
  "rows": [
    ["Under: zeta < 1", "Complex, Re < 0", "Decaying oscillation"],
    ["Critical: zeta = 1", "Repeated negative", "Repeated-root template"],
    ["Over: zeta > 1", "Two negative real", "No sustained oscillation"],
    ["Undamped: zeta = 0", "Purely imaginary", "Periodic, no decay"]
  ],
  "caption": "A damped sinusoid is not periodic: shifting by its oscillation interval also multiplies the envelope by a nontrivial exponential."
}
:::

:::example title="S21 and Q29: under-damped, not periodic"
For $y''+2y'+5y=0$, $r=-1\pm2i$ and
$$
y=e^{-x}(A\cos2x+B\sin2x).
$$
The initial conditions give $A=0$ and $2B=2$, so
$$
y=e^{-x}\sin2x,
\qquad y(1)=e^{-1}\sin2\approx0.3345118292.
$$
Here $\omega=\sqrt{5}$, $\zeta=1/\sqrt{5}<1$. Zeros occur at $x=n\pi/2$, so consecutive zeros are $\pi/2$ apart. Corresponding phases of $\sin2x$ recur after $\pi$, the oscillation or quasi-period, but
$$
y(x+\pi)=e^{-\pi}y(x)\neq y(x)
$$
unless $y(x)=0$. Thus the source's word “period” is corrected: the damped solution is not periodic.
:::

:::example title="P16 and Q30: over-damped with one initial rise"
For $y''+3y'+2y=0$, the roots are $-1$ and $-2$, so the regime is over-damped. Write $y=Ae^{-x}+Be^{-2x}$. The initial data give $A+B=0$ and $-A-2B=1$, hence
$$
y=e^{-x}-e^{-2x}=e^{-2x}(e^x-1).
$$
Therefore $y>0$ for every $x>0$ and $y\to0$; there is no positive zero crossing. Also $y(1)=e^{-1}-e^{-2}\approx0.2325441579$. The maximum occurs at $x=\ln2$, where $y=1/4$.
:::

## Envelope versus actual graph

For Q29, the curves $e^{-x}$ and $-e^{-x}$ bound the solution but are not the solution. The actual graph touches an envelope only where $|\sin2x|=1$ and crosses zero between touches. Visual Lab 4 displays all three curves with exact tick spacing.

:::warn title="Decay alone does not imply over-damping"
Under-damped and critically damped solutions can also tend to zero. Classify by the roots or by $\zeta$, not merely by the long-term limit.
:::
