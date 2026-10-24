---
id: olympiad-06
part: olympiad
title: "Extension VI — Nonhomogeneous Second-Order Linear Equations"
---

## Add one particular solution to the homogeneous general solution

For $L[y]=ay''+by'+cy=g(x)$, linearity gives
$$
y=y_h+y_p,
$$
where $L[y_h]=0$ and $L[y_p]=g$. Two arbitrary constants belong to $y_h$. Undetermined coefficients is efficient for exponential, polynomial and trigonometric forcing; variation of parameters is more general.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "Choose a particular-solution method from the forcing term",
  "columns": ["Forcing", "Trial or start", "Adjustment"],
  "col_widths": [0.32, 0.34, 0.34],
  "rows": [
    ["exp(kx), nonresonant", "A exp(kx)", "Find A by substitution"],
    ["Already homogeneous", "Multiply trial by x", "Repeat if needed"],
    ["Polynomial/sine/cosine", "Full same-type trial", "Keep all related terms"],
    ["General continuous g", "Variation of parameters", "Use independent y1, y2"]
  ],
  "caption": "This extension is additional enrichment beyond the 41 canonical paper questions; its formulas are verified independently in the mathematical suite."
}
:::

:::example title="Undetermined coefficients: nonresonant and resonant forcing"
For $y''-y=e^{2x}$, try $y_p=Ae^{2x}$. Then $(4-1)A=1$, so
$$
y=C_1e^x+C_2e^{-x}+\frac{1}{3}e^{2x}.
$$
For $y''-y=e^x$, the plain trial $Ae^x$ is homogeneous and gives zero. Instead,
$$
L[xe^x]=(x+2)e^x-xe^x=2e^x,
$$
so $y_p=xe^x/2$ and
$$
y=C_1e^x+C_2e^{-x}+\frac{1}{2}xe^x.
$$
:::

## Variation of parameters with the same Wronskian convention

For normalized $y''+P y'+Q y=g$, let $y_1,y_2$ be independent homogeneous solutions and $W=y_1y_2'-y_1'y_2$. Then
$$
u_1'=-\frac{y_2g}{W},\qquad u_2'=\frac{y_1g}{W},
\qquad y_p=u_1y_1+u_2y_2.
$$
The formula follows by imposing $u_1'y_1+u_2'y_2=0$ and matching the first-derivative equation.

:::example title="A trigonometric interval where cosine is positive"
For $y''+y=1/\cos x$ on $(-\pi/2,\pi/2)$, choose $y_1=\cos x$, $y_2=\sin x$, so $W=1$. Then
$$
u_1'=-\tan x,\qquad u_2'=1.
$$
Hence $u_1=\ln(\cos x)$, $u_2=x$, and a particular solution is
$$
y_p=\cos x\,\ln(\cos x)+x\sin x.
$$
The interval matters: both $1/\cos x$ and $\ln(\cos x)$ require $\cos x>0$.
:::

:::warn title="Do not force a resonant trial to work by changing only its amplitude"
If the trial solves the homogeneous equation, every amplitude still produces zero on the left. Multiplication by x changes the functional form and supplies the missing forcing term.
:::
