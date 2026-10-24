---
id: olympiad-02
part: olympiad
title: "Extension II — Reduction Formulae and Recurrence"
---

## Lower the difficulty one exponent at a time

A reduction formula expresses an integral with exponent $n$ in terms of a smaller exponent. It is a recurrence of antiderivatives, with a constant fixed only at the end.

For $I_n=\int x^ne^xdx$, integration by parts gives
$$
I_n=x^ne^x-nI_{n-1},\qquad I_0=e^x+C.
$$
Thus $I_1=e^x(x-1)$ and $I_2=e^x(x^2-2x+2)$, followed by
$$
I_3=e^x(x^3-3x^2+6x-6)+C.
$$

:::diagram
{
  "type": "flow",
  "title": "A reduction recurrence terminates at a known base case",
  "steps": [
    {"title": "Define I_n", "detail": "Keep the exponent symbolic and choose parts to reduce it by one or two."},
    {"title": "Derive the recurrence", "detail": "Record signs, coefficients and the lower index exactly."},
    {"title": "Iterate to a base", "detail": "Stop at I_0 or I_1, or at another independently known integral."},
    {"title": "Differentiate the closed form", "detail": "Check the final polynomial-trigonometric coefficients and restore +C."}
  ],
  "caption": "A recurrence is not just a computational shortcut: it also proves the antiderivative's structural form by induction on the exponent."
}
:::

## Logarithmic powers follow the same pattern

For $x>0$, let $J_n=\int(\ln x)^n dx$. With $u=(\ln x)^n$ and $dv=dx$,
$$
J_n=x(\ln x)^n-nJ_{n-1},\qquad J_0=x+C.
$$
The first three closed forms are
$$
J_1=x\ln x-x,\qquad
J_2=x(\ln x)^2-2x\ln x+2x,
$$
$$
J_3=x(\ln x)^3-3x(\ln x)^2+6x\ln x-6x,
$$
all up to the same final additive constant.

## Trigonometric powers step down by two

For $n\geq2$, let $S_n=\int\sin^n x\,dx$. By parts,
$$
S_n=-\frac{1}{n}\sin^{n-1}x\cos x+\frac{n-1}{n}S_{n-2},
$$
with $S_0=x+C$ and $S_1=-\cos x+C$. In particular,
$$
S_6=-\frac{1}{6}\sin^5x\cos x-\frac{5}{24}\sin^3x\cos x
-\frac{5}{16}\sin x\cos x+\frac{5}{16}x+C.
$$
Differentiating this expression returns $\sin^6x$. The source's Wallis questions S15, S19, Q30 and Q43 apply limits to this same recurrence in Chapter 21.

:::warn title="The recurrence's constant belongs to the completed answer"
The displayed recurrence is an equality of chosen antiderivatives. When iterating, keep a consistent choice and add the arbitrary constant at the end. Do not allow unrelated constants at each stage to masquerade as extra terms.
:::
