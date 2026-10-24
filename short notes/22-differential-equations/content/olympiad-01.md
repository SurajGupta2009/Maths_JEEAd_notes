---
id: olympiad-01
part: olympiad
title: "Extension I — Reduction of Order and Wronskians"
---

## One known solution generates a second

Normalize a linear equation as $y''+P(x)y'+Q(x)y=0$ and suppose $y_1$ is a known nonzero solution on an interval. Put $y=vy_1$. After using $y_1''+Py_1'+Qy_1=0$,
$$
y_1v''+(2y_1'+Py_1)v'=0.
$$
This is first order in $w=v'$. Integrating once more gives the standard formula
$$
y_2=y_1\int\frac{e^{-\int P(x)dx}}{y_1^2}\,dx.
$$
The integral is computed locally where $y_1\neq0$; a resulting formula can sometimes be extended by direct verification.

:::diagram
{
  "type": "flow",
  "title": "Reduction of order converts a second-order equation into a first-order one",
  "steps": [
    {"title": "Normalize", "detail": "Make the coefficient of y'' equal to one on the chosen interval."},
    {"title": "Set y = v y1", "detail": "Use the known solution to eliminate the undifferentiated v terms."},
    {"title": "Solve for v-prime", "detail": "Integrate the remaining first-order equation, then integrate again."},
    {"title": "Test independence", "detail": "Check a nonzero Wronskian or show the ratio y2/y1 is nonconstant."}
  ],
  "caption": "The Wronskian convention used here is W=y1 y2-prime minus y1-prime y2."
}
:::

:::example title="S17 and Q34: a corrected Wronskian sign"
For $y''+y=0$, $P=0$ and $y_1=\sin x$. On an interval where $\sin x\neq0$,
$$
y_2=\sin x\int\csc^2x\,dx
=\sin x(-\cot x)=-\cos x.
$$
Direct substitution extends $-\cos x$ to a solution on $(-\infty,\infty)$. The general solution is $C_1\sin x+C_2\cos x$. With $y_2=-\cos x$,
$$
W=y_1y_2'-y_1'y_2
=\sin^2x+\cos^2x=+1.
$$
The source's $-1$ is a sign error under this convention; choosing $y_2=\cos x$ instead would reverse the Wronskian but not the independence conclusion.
:::

:::example title="P13 and Q35: reduce the Euler equation"
Given $y_1=x$ for $x^2y''-2xy'+2y=0$, put $y=xv$. Then
$$
y'=v+xv',\qquad y''=2v'+xv''.
$$
Substitution leaves $x^3v''=0$, so on $x>0$ or $x<0$, $v''=0$ and $v=Ax+B$. Hence
$$
y=Ax^2+Bx.
$$
For $y_1=x$, $y_2=x^2$, the Wronskian is $W=x(2x)-1(x^2)=x^2$, nonzero away from the singular point $x=0$.
:::

:::warn title="A Wronskian sign depends on ordering and representative choice"
Independence requires a nonzero Wronskian, not a particular sign. Always state the ordering and the actual second function before reporting W.
:::
