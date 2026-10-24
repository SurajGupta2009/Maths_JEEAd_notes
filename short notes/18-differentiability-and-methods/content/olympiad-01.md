---
id: olympiad-01
part: olympiad
title: "Extension I — Higher Derivatives and Leibniz's Rule"
---

## Differentiate a product n times without expanding every case

Leibniz's rule generalizes the product rule. For sufficiently differentiable $u,v$,
$$
(uv)^{(n)}=\sum_{k=0}^{n}\binom{n}{k}u^{(k)}v^{(n-k)}.
$$
Here $u^{(0)}=u$. The formula is especially short when one factor is a polynomial, because sufficiently high derivatives of that factor vanish.

:::example title="Only three Leibniz terms survive for x^2e^x"
Take $u=x^2$ and $v=e^x$. Since $u'''=0$ and every derivative of $v$ is $e^x$, for $n\geq2$,
$$
(x^2e^x)^{(n)}
=e^x\left[x^2+2nx+n(n-1)\right].
$$
In particular,
$$
(x^2e^x)''=e^x(x^2+4x+2),\qquad
(x^2e^x)'''=e^x(x^2+6x+6).
$$
For $n=0,1$, direct substitution gives $x^2e^x$ and $e^x(x^2+2x)$, also consistent with the displayed polynomial formula.
:::

:::example title="The same three-term pattern differentiates x^2 cos x"
For $n\geq2$, Leibniz's rule gives
$$
D^n(x^2\cos x)=x^2\cos\left(x+\frac{n\pi}{2}\right)
+2nx\cos\left(x+\frac{(n-1)\pi}{2}\right)
+n(n-1)\cos\left(x+\frac{(n-2)\pi}{2}\right).
$$
Only derivatives of $x^2$ through order $2$ survive. The cases $n=0,1$ are checked directly; the formula also reduces correctly for $n=1$.
:::

## Recognize when a polynomial terminates the sum

If $p$ has degree $m$, then $p^{(k)}=0$ for $k>m$. Hence $(pv)^{(n)}$ needs only $0\leq k\leq\min(n,m)$. This is a structural simplification, not an assumption that $v$ also has terminating derivatives.

:::diagram
{
  "type": "flow",
  "title": "A reliable higher-derivative workflow",
  "steps": [
    {"title": "Choose the splitting", "detail": "Put the polynomial or terminating factor in u."},
    {"title": "List surviving orders", "detail": "Degree m means only k=0,...,min(n,m) contribute."},
    {"title": "Apply Leibniz coefficients", "detail": "Keep binomial factors and the order n-k on v."},
    {"title": "Test low orders", "detail": "Check n=1 and n=2 directly before generalizing."}
  ],
  "caption": "Most errors come from omitted binomial coefficients or from assigning the same derivative order to both factors."
}
:::

:::warn title="Leibniz's rule does not say (uv)^(n)=u^(n)v+uv^(n)"
Those are only the two endpoint terms. Unless all intermediate terms genuinely vanish, the full binomial sum is required.
:::
