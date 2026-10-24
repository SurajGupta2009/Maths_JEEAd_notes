---
id: jee-10
part: jee
title: "Cauchy–Euler Equations — Trial Powers"
---

## Variable coefficients can still produce an algebraic root equation

On $x>0$, a second-order Cauchy–Euler equation has the form
$$
ax^2y''+bxy'+cy=0.
$$
Try $y=x^m$. Since $xy'=mx^m$ and $x^2y''=m(m-1)x^m$,
$$
am(m-1)+bm+c=0.
$$
Distinct roots $m_1,m_2$ give $y=Ax^{m_1}+Bx^{m_2}$. A repeated root $m$ gives $y=x^m(A+B\ln x)$ on $x>0$.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "Constant-coefficient and Euler trials are related but not identical",
  "columns": ["Equation", "Trial", "Root equation or caution"],
  "col_widths": [0.28, 0.30, 0.42],
  "rows": [
    ["Constant coefficient", "exp(rx)", "a r^2 + b r + c"],
    ["Euler", "x^m", "a m(m-1) + b m + c"],
    ["Repeated Euler m", "x^m, x^m ln x", "Log gives independence"],
    ["Initial x0 > 0", "Stay on x > 0", "Do not cross 0"]
  ],
  "caption": "The Euler coefficient b multiplies m, while the coefficient a multiplies m(m-1)."
}
:::

:::example title="S13 and Q24: roots 1 and -1"
For $x^2y''+xy'-y=0$,
$$
m(m-1)+m-1=m^2-1=0.
$$
Thus $y=Ax+B/x$. The conditions at $x=1$ give
$$
A+B=0,\qquad A-B=1,
$$
so $A=1/2$, $B=-1/2$. Therefore
$$
y=\frac{1}{2}\left(x-\frac{1}{x}\right),
\qquad y(2)=\frac{3}{4},
$$
on the maximal interval $(0,\infty)$.
:::

:::example title="P12 and Q25: the initial data select a single power"
For $x^2y''-2xy'+2y=0$,
$$
m(m-1)-2m+2=m^2-3m+2=(m-1)(m-2).
$$
Hence $y=Ax+Bx^2$. At $x=1$,
$$
A+B=1,\qquad A+2B=2,
$$
so $B=1$, $A=0$. The IVP solution is $y=x^2$ and $y(3)=9$. Extension I independently obtains the same general solution by reduction of order.
:::

## Why the logarithm appears for repeated roots

The substitution $t=\ln x$ transforms an Euler equation on $x>0$ into a constant-coefficient equation in $t$. A repeated root then produces $te^{mt}$, and returning to $x$ turns $t$ into $\ln x$. This explains the template rather than memorizing it separately.

:::warn title="The standard form has singular coefficients at x = 0"
After dividing by $x^2$, the coefficients contain $1/x$ and $1/x^2$. Solutions from an initial point with $x>0$ stay on $x>0$ unless a separate continuation analysis is supplied.
:::
