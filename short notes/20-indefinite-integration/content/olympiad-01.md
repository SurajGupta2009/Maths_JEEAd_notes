---
id: olympiad-01
part: olympiad
title: "Extension I — Euler Substitution for Radicals"
---

## Turn a radical into a rational variable

For $s=\sqrt{x^2+a^2}$, introduce
$$
t=x+s>0.
$$
Then $s=t-x$ and $s^2=x^2+a^2$, so
$$
x=\frac{t^2-a^2}{2t},\qquad
s=\frac{t^2+a^2}{2t},\qquad
\frac{dx}{s}=\frac{dt}{t}.
$$
This is an Euler substitution. It proves the standard form rather than merely quoting it:
$$
\int\frac{dx}{\sqrt{x^2+a^2}}
=\ln t+C
=\ln\left(x+\sqrt{x^2+a^2}\right)+C.
$$
The absolute value is unnecessary here because $x+\sqrt{x^2+a^2}>0$ for every real $x$.

:::diagram
{
  "type": "table",
  "title": "Euler's substitution removes the radical and preserves dx/s",
  "columns": ["Quantity", "Rational form in t", "Consequence"],
  "rows": [
    ["t", "x+sqrt(x^2+a^2)", "t is positive"],
    ["x", "(t^2-a^2)/(2t)", "x is rational in t"],
    ["s", "(t^2+a^2)/(2t)", "radical is rationalised"],
    ["dx/s", "dt/t", "integral becomes logarithmic"]
  ],
  "col_widths": [0.18, 0.48, 0.34],
  "caption": "The identity dx/s=dt/t is the key simplification. It follows by differentiating x(t) and comparing with s(t), not by treating dx as a separate number."
}
:::

## The same idea works on a branch of a difference of squares

For $x>a>0$, put $t=x+\sqrt{x^2-a^2}>0$. Now
$$
x=\frac{t^2+a^2}{2t},\qquad
\sqrt{x^2-a^2}=\frac{t^2-a^2}{2t},
$$
and again $dx/s=dt/t$. Thus
$$
\int\frac{dx}{\sqrt{x^2-a^2}}=\ln t+C.
$$
On $x<-a$, the compact answer uses $\ln|x+\sqrt{x^2-a^2}|$ and is checked separately on that interval.

:::example title="An initial value fixes the logarithmic constant"
If $F'(x)=1/\sqrt{x^2+4}$ and $F(0)=0$, then
$$
F(x)=\ln\left(x+\sqrt{x^2+4}\right)+C.
$$
Since the value at zero is $\ln2+C$, we need $C=-\ln2$:
$$
F(x)=\ln\left(\frac{x+\sqrt{x^2+4}}{2}\right).
$$
:::

:::diagram
{
  "type": "graph",
  "title": "Euler's logarithm has derivative 1/sqrt(x^2+1)",
  "xrange": [-3, 3], "yrange": [-2, 2],
  "xticks": [-3, -2, -1, 0, 1, 2, 3], "yticks": [-2, -1, 0, 1, 2],
  "curves": [
    {"expr": "1/sqrt(x**2+1)", "from": -3, "to": 3, "color": "#B91C1C"},
    {"expr": "log(x+sqrt(x**2+1))", "from": -3, "to": 3}
  ],
  "points": [
    {"x": 0, "y": 0, "label": "F(0)=0", "dx": 0.15, "dy": 0.18},
    {"x": 1, "y": 0.881373587, "label": "F(1)=ln(1+sqrt(2))", "dx": -1.75, "dy": 0.30}
  ],
  "caption": "Red is f=1/sqrt(x^2+1), and teal is F=ln(x+sqrt(x^2+1)). F is odd, passes through zero and has positive slope f everywhere."
}
:::
