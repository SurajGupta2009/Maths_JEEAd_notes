---
id: jee-11
part: jee
title: "The Half-Angle Substitution"
---

## Convert sine and cosine into rational functions of one variable

For a rational expression in $\sin x$ and $\cos x$, the universal substitution is
$$
t=\tan\frac{x}{2},\qquad
\sin x=\frac{2t}{1+t^2},\qquad
\cos x=\frac{1-t^2}{1+t^2},\qquad
dx=\frac{2\,dt}{1+t^2}.
$$
It is powerful but algebra-heavy, so first check for a simpler identity, symmetry or direct substitution.

:::diagram
{
  "type": "flow",
  "title": "The half-angle substitution is a complete change of variable",
  "steps": [
    {"title": "Set t=tan(x/2)", "detail": "Choose an interval on which the substitution is defined and monotone."},
    {"title": "Replace all four pieces", "detail": "Convert sin x, cos x, dx and every remaining trigonometric factor."},
    {"title": "Integrate rationally", "detail": "Simplify, then use division or partial fractions in t."},
    {"title": "Return and retain branch", "detail": "Replace t by tan(x/2) and state the x-interval of validity."}
  ],
  "caption": "The factor dx=2dt/(1+t^2) is essential. Omitting it can coincidentally produce a familiar expression but cannot produce the correct antiderivative."
}
:::

:::example title="The antiderivative behind S13 and Q35"
For
$$
I=\int\frac{dx}{2+\cos x},
$$
the denominator becomes
$$
2+\cos x=2+\frac{1-t^2}{1+t^2}=\frac{3+t^2}{1+t^2}.
$$
Including $dx=2dt/(1+t^2)$ gives
$$
I=\int\frac{2}{3+t^2}dt
=\frac{2}{\sqrt{3}}\tan^{-1}\frac{t}{\sqrt{3}}+C.
$$
Thus, on $-\pi<x<\pi$,
$$
I=\frac{2}{\sqrt{3}}\tan^{-1}\left(\frac{\tan(x/2)}{\sqrt{3}}\right)+C.
$$
The definite value on $[0,\pi/2]$ is completed in Chapter 21.
:::

## Another route can give an equivalent-looking answer

For $\int dx/(1+\sin x)$, the same substitution gives
$$
\int\frac{2\,dt}{(1+t)^2}=-\frac{2}{1+t}+C
=-\frac{2}{1+\tan(x/2)}+C.
$$
On an allowed branch this differs from $\tan x-\sec x$ only by a constant, and both differentiate to $1/(1+\sin x)$.

:::warn title="The substitution has branches"
$t=\tan(x/2)$ is undefined at $x=(2k+1)\pi$. The displayed arctangent antiderivative is not automatically one continuous antiderivative across those points. Use it on a single branch; definite problems also require an interval free of the original integrand's singularities.
:::
