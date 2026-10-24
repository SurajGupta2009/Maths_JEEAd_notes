---
id: olympiad-02
part: olympiad
title: "Extension II — Advanced Closed Forms and Identities"
---

## Powers and reciprocals have compact nth derivatives

For a real exponent $r$ and a domain on which $ax+b>0$,
$$
D^n(ax+b)^r=a^n r(r-1)\cdots(r-n+1)(ax+b)^{r-n}.
$$
If $m$ is a nonnegative integer and $0\leq n\leq m$, this becomes
$$
D^n(ax+b)^m=\frac{m!}{(m-n)!}a^n(ax+b)^{m-n},
$$
and derivatives of order greater than $m$ vanish. For $a\ne0$ and $ax+b\ne0$,
$$
D^n\frac{1}{ax+b}=\frac{(-1)^n n!a^n}{(ax+b)^{n+1}}.
$$
Thus the fourth derivative of $(2x+1)^3$ is $0$, while the second derivative of $1/x$ is $2/x^3$ on either side of its domain. In particular,
$$
D^n\frac{1}{1-x}=\frac{n!}{(1-x)^{n+1}}\qquad(x\ne1).
$$

## Split a logarithm's derivative without inventing real logarithms

For $y=\ln(x^2-1)$, the real domain is $|x|>1$. On either component,
$$
y'=\frac{2x}{x^2-1}=\frac{1}{x-1}+\frac{1}{x+1}.
$$
Therefore, for $n\geq1$,
$$
y^{(n)}=(-1)^{n-1}(n-1)!\left[(x-1)^{-n}+(x+1)^{-n}\right].
$$
The decomposition is applied to the **derivative** as a rational identity. On $x<-1$, the original logarithm is real, but $\ln(x-1)$ and $\ln(x+1)$ are not separately real.

## Exponential-trigonometric derivatives rotate by a fixed phase

For $(a,b)\ne(0,0)$, let $r=\sqrt{a^2+b^2}>0$ and choose $\phi$ with $\cos\phi=a/r$, $\sin\phi=b/r$. Then
$$
D(e^{ax}\cos bx)=r e^{ax}\cos(bx+\phi).
$$
Iterating gives
$$
D^n(e^{ax}\cos bx)=r^n e^{ax}\cos(bx+n\phi).
$$
For $a=b=1$, this is
$$
D^n(e^x\cos x)=2^{n/2}e^x\cos\left(x+\frac{n\pi}{4}\right).
$$

:::example title="A differential identity can replace repeated messy expansion"
For $y=\sqrt{1-x^2}$ on $|x|<1$,
$$
y'=-\frac{x}{y},\qquad y''=-\frac{1}{y^3}.
$$
Consequently
$$
(1-x^2)y''-xy'=-\frac{1-x^2}{y^3}+\frac{x^2}{y}
=-\frac{1}{y}+\frac{x^2}{y}=\frac{x^2-1}{y}=-y.
$$
This exact identity is a useful independent check of both derivatives.
:::

:::diagram
{
  "type": "table",
  "title": "Choose a closed form from the expression's structure",
  "columns": ["Structure", "Closed-form cue", "Caution"],
  "rows": [
    ["Polynomial power", "Falling factorial", "degree and order"],
    ["Real power", "Falling factorial", "positive base"],
    ["Reciprocal", "Sign and n!", "exclude pole"],
    ["Log of quadratic", "Split its derivative", "|x| above 1"],
    ["Exp. times sine", "Amplitude; phase", "choose phi"],
    ["Implicit radical", "Use exact relation", "check domain"]
  ],
  "col_widths": [0.28, 0.39, 0.33],
  "caption": "Closed forms shorten iteration, but a low-order direct derivative remains the fastest way to detect a missing factor."
}
:::
