---
id: jee-06
part: jee
title: "Bernoulli Equations and Trigonometric Forcing"
---

## Bernoulli becomes linear after a power substitution

For $n\neq0,1$, the equation
$$
y'+P(x)y=Q(x)y^n
$$
has the substitution $u=y^{1-n}$. On a nonzero solution branch,
$$
u'+(1-n)P(x)u=(1-n)Q(x).
$$
Solve this linear equation and return to $y$. If $y=0$ is defined in the original equation, check it separately before dividing by $y^n$.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "Recognize the method from the right-hand side",
  "columns": ["Feature", "Try", "Audit"],
  "col_widths": [0.28, 0.34, 0.38],
  "rows": [
    ["y^n forcing", "u = y^(1-n)", "Test y = 0 first"],
    ["sin x forcing", "A sin x + B cos x", "Match both coefficients"],
    ["exp(kx) forcing", "IF or A exp(kx)", "Check resonance"],
    ["Pole in answer", "Restrict x-interval", "Never cross the pole"]
  ],
  "caption": "A substitution changes the algebra, not the obligation to verify the final function in the original equation."
}
:::

:::example title="S8 and Q15: Bernoulli with n = 2"
For $y'+y=xy^2$, $y(0)=1$, the zero equilibrium fails the IVP. Put $u=1/y$. Dividing by $y^2$ gives
$$
-u'+u=x
\quad\Longrightarrow\quad u'-u=-x.
$$
With integrating factor $e^{-x}$,
$$
(ue^{-x})'=-xe^{-x}
\quad\Longrightarrow\quad u=x+1+Ce^x.
$$
The initial condition gives $u(0)=1$, hence $C=0$. Therefore
$$
y=\frac{1}{x+1},\qquad y(1)=\frac{1}{2}.
$$
Starting at $x=0$, the maximal interval is $(-1,\infty)$, not all real numbers.
:::

## A sine forcing term needs both sine and cosine

For constant-coefficient linear equations, a trial $A\sin x+B\cos x$ accounts for the derivative interchanging sine and cosine.

:::example title="Q28: solve y-prime + y = sin x"
Substitute $y_p=A\sin x+B\cos x$ into $y'+y=\sin x$:
$$
(A-B)\sin x+(A+B)\cos x=\sin x.
$$
Thus $A-B=1$ and $A+B=0$, so $A=1/2$, $B=-1/2$. The general solution is
$$
y=\frac{1}{2}(\sin x-\cos x)+Ce^{-x}.
$$
Since $y(0)=0$, $C=1/2$, and
$$
y=\frac{1}{2}(\sin x-\cos x+e^{-x}),
\qquad
y\!\left(\frac{\pi}{2}\right)=\frac{1+e^{-\pi/2}}{2}.
$$
:::

:::warn title="A one-term sine trial is usually incomplete"
The derivative of sine is cosine. Omitting the cosine trial forces an inconsistent coefficient comparison unless the equation has special structure.
:::
