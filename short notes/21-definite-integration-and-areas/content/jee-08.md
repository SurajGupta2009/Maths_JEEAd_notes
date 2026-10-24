---
id: jee-08
part: jee
title: "Improper Integrals II — Singular Endpoints and Logarithms"
---

## Approach a singular endpoint from inside the interval

If $f$ is continuous on $(0,1]$ but unbounded near $0$, define
$$
\int_0^1f(x)dx=\lim_{\varepsilon\to0^+}\int_\varepsilon^1f(x)dx
$$
when the limit is finite. For $p<1$,
$$
\int_0^1x^{-p}dx=\frac{1}{1-p}.
$$
The complete finite-interval $p$-test says that $\int_0^1x^{-p}dx$ converges exactly when $p<1$; at $p=1$ it gives $-\ln\varepsilon\to\infty$.

:::example title="P13: the logarithm is unbounded but integrable"
Using $\int\ln x\,dx=x\ln x-x$,
$$
\int_\varepsilon^1\ln x\,dx=-1-(\varepsilon\ln\varepsilon-\varepsilon).
$$
Since $\varepsilon\ln\varepsilon\to0$ and $\varepsilon\to0$,
$$
\int_0^1\ln x\,dx=-1.
$$
:::

:::example title="S14/Q28 and P14/Q29: logarithmic powers still have finite area"
For $x\ln x$,
$$
\int_0^1x\ln x\,dx
=\lim_{\varepsilon\to0^+}\left[\frac{x^2}{2}\ln x-\frac{x^2}{4}\right]_\varepsilon^1
=-\frac{1}{4}.
$$
For $(\ln x)^2$,
$$
\int_0^1(\ln x)^2dx
=\lim_{\varepsilon\to0^+}\left[x((\ln x)^2-2\ln x+2)\right]_\varepsilon^1=2.
$$
Both use $x(\ln x)^k\to0$ as $x\to0^+$ for fixed positive $k$.
:::

:::diagram
{
  "type": "table",
  "title": "Endpoint limits used by the logarithmic integrals",
  "columns": ["Limit as x->0+", "Value", "Why it matters"],
  "rows": [
    ["x ln x", "0", "removes the lower endpoint term"],
    ["x (ln x)^2", "0", "permits the squared-log integral"],
    ["x^2 ln x", "0", "permits the x ln x integral"],
    ["x^p integral, p<1", "finite", "finite-interval p-test"],
    ["ln x itself", "-infinity", "unbounded does not mean nonintegrable"]
  ],
  "col_widths": [0.31, 0.18, 0.51],
  "caption": "The integrand may diverge while its signed or absolute area remains finite. Each endpoint term is evaluated as a limit, never by substituting x=0 into ln x."
}
:::

:::warn title="Distinguish an improper integral from a continuous removable expression"
If an expression has a finite continuous extension, it can be assigned that value at the endpoint. If it remains unbounded, as $\ln x$ does, the integral must be defined through $\varepsilon\to0^+$. In either case, the original domain and the limiting interpretation must be stated.
:::
