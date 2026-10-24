---
id: jee-04
part: jee
title: "Algebra and Trigonometric Preparation"
---

## Simplify before choosing a technique

Many integrals become elementary after division, expansion or a trigonometric identity. Preparation is part of the calculation, not an optional cosmetic step:
$$
\int\frac{x+1}{\sqrt{x}}dx
=\int\left(x^{1/2}+x^{-1/2}\right)dx
=\frac{2}{3}x^{3/2}+2x^{1/2}+C\qquad(x>0).
$$

:::example title="A direct power substitution"
For $\int\sin^3x\cos x\,dx$, put $u=\sin x$, $du=\cos x\,dx$:
$$
\int\sin^3x\cos x\,dx=\int u^3du
=\frac{\sin^4x}{4}+C.
$$
:::

## Odd and even trigonometric powers need different preparation

For an odd power of sine, reserve one sine factor for $du=-\sin x\,dx$ and convert the remaining even power with $\sin^2x=1-\cos^2x$:
$$
\int\sin^3x\,dx
=\int(1-\cos^2x)\sin x\,dx
=-\cos x+\frac{\cos^3x}{3}+C.
$$
For even powers, halve the angle:
$$
\sin^2x=\frac{1-\cos2x}{2},
\qquad
\cos^2x=\frac{1+\cos2x}{2}.
$$
Consequently,
$$
\int\sin^2x\,dx=\frac{x}{2}-\frac{\sin2x}{4}+C,
\qquad
\int\cos^2x\,dx=\frac{x}{2}+\frac{\sin2x}{4}+C.
$$
These antiderivatives also underpin the source's definite questions P10, Q24 and Q36; evaluation over limits is deferred to Chapter 21.

:::diagram
{
  "type": "table",
  "title": "Choose a trigonometric preparation from the powers",
  "columns": ["Pattern", "Preparation", "Likely next step"],
  "rows": [
    ["sin^n x cos x", "u = sin x", "power rule"],
    ["cos^n x sin x", "u = cos x", "power rule"],
    ["odd sine power", "save sin x dx", "u = cos x"],
    ["odd cosine power", "save cos x dx", "u = sin x"],
    ["even powers", "half-angle identities", "linear trigonometric terms"],
    ["product sin x cos x", "u = sin x or double angle", "equivalent answers"]
  ],
  "col_widths": [0.28, 0.38, 0.34],
  "caption": "The aim is to create either a complete du or a sum of standard forms. Do not mix the odd-power and even-power strategies midway."
}
:::

:::example title="Different-looking answers can all be correct"
Three routes to $I=\int\sin x\cos x\,dx$ give
$$
I=\frac{1}{2}\sin^2x+C,
\qquad
I=-\frac{1}{2}\cos^2x+C,
\qquad
I=-\frac{1}{4}\cos2x+C.
$$
Their derivatives are all $\sin x\cos x$. Moreover,
$$
-\frac{1}{2}\cos^2x=\frac{1}{2}\sin^2x-\frac{1}{2},
\qquad
-\frac{1}{4}\cos2x=\frac{1}{2}\sin^2x-\frac{1}{4}.
$$
The apparent discrepancies are constants, not errors.
:::

:::warn title="Keep the original domain after cancellation"
Algebraic simplification may expose a removable factor, but it does not restore points where the original integrand was undefined. State the simplified antiderivative only on intervals of the original domain.
:::
