---
id: jee-02
part: jee
title: "The Fundamental Theorem of Calculus"
---

## Accumulated area differentiates back to the height

For continuous $f$, define
$$
A(x)=\int_a^x f(t)\,dt.
$$
Then
$$
A(x+h)-A(x)=\int_x^{x+h}f(t)\,dt.
$$
For small $h$, the continuous height is close to $f(x)$, so the difference quotient tends to $f(x)$:
$$
A'(x)=f(x).
$$
This is FTC Part 1. If $F'=f$, FTC Part 2 gives
$$
\int_a^b f(x)\,dx=F(b)-F(a).
$$

:::diagram
{
  "type": "flow",
  "title": "The Fundamental Theorem joins the two directions of calculus",
  "steps": [
    {"title": "Accumulate", "detail": "Define A(x) as the signed integral from a fixed start to x."},
    {"title": "Differentiate", "detail": "The accumulation rate A'(x) is the current height f(x)."},
    {"title": "Find an antiderivative", "detail": "Use Chapter 20 to obtain any F with F'=f."},
    {"title": "Subtract endpoint values", "detail": "The definite value is F(b)-F(a); the constant cancels."}
  ],
  "caption": "The dummy variable t prevents confusion with the moving upper limit x. An antiderivative's arbitrary constant does not affect a definite difference."
}
:::

:::example title="S9 and Q23: subtract antiderivative values"
$$
\int_0^1x^2dx=\left[\frac{x^3}{3}\right]_0^1=\frac{1}{3},
\qquad
\int_0^1x^3dx=\left[\frac{x^4}{4}\right]_0^1=\frac{1}{4}.
$$
The first result agrees with a right-sum limit on $[0,1]$; the second also equals the total area because $x^3\geq0$ on this interval.
:::

:::example title="S10 and Q22: differentiate an accumulation function"
If $A(x)=\int_0^x t^2dt$, then $A'(x)=x^2$. Indeed $A(x)=x^3/3$. Similarly,
$$
\frac{d}{dx}\int_0^x t^3dt=x^3,
$$
because the explicit accumulation function is $x^4/4$.
:::

## Variable upper and lower limits use the chain rule

For differentiable $u,v$ and continuous $f$,
$$
\frac{d}{dx}\int_{u(x)}^{v(x)}f(t)dt
=f(v(x))v'(x)-f(u(x))u'(x).
$$
For example,
$$
\frac{d}{dx}\int_{x^2}^{\sin x}e^{t^2}dt
=e^{\sin^2x}\cos x-2xe^{x^4}.
$$
No elementary antiderivative of $e^{t^2}$ is needed.

:::warn title="Do not differentiate the integrand with respect to x"
In $\int_0^x f(t)dt$, the integrand uses the dummy variable $t$. FTC substitutes the upper limit into $f$; it does not produce $\int_0^x f'(t)dt$ or $f'(x)$.
:::
