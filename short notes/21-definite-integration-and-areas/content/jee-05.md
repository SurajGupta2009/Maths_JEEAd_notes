---
id: jee-05
part: jee
title: "Definite-Integral Properties and Symmetry"
---

## Interval and symmetry properties can shorten the work

For integrable functions and constants $\alpha,\beta$,
$$
\int_a^c f=\int_a^b f+\int_b^c f,
\qquad
\int_a^b f=-\int_b^a f,
\qquad
\int_a^a f=0,
$$
$$
\int_a^b(\alpha f+\beta g)
=\alpha\int_a^b f+\beta\int_a^b g.
$$
Additivity uses signed orientation, so $b$ need not lie between $a$ and $c$ when the convention $\int_u^v=-\int_v^u$ is retained.

:::diagram
{
  "type": "table",
  "title": "Use symmetry only with its required interval or period",
  "columns": ["Hypothesis", "Definite-integral consequence", "Essential check"],
  "rows": [
    ["f is odd", "integral on [-a,a] is zero", "symmetric interval"],
    ["f is even", "integral on [-a,a] is twice 0 to a", "symmetric interval"],
    ["f has period T", "any interval of length T gives same integral", "full period length"],
    ["reverse endpoints", "integral changes sign", "orientation"],
    ["additivity", "split at a convenient point", "integrability on pieces"]
  ],
  "col_widths": [0.25, 0.48, 0.27],
  "caption": "Odd/even symmetry concerns function values. Periodicity concerns translation of the whole interval. Neither is a substitute for checking convergence in an improper setting."
}
:::

## Odd powers cancel on symmetric intervals

For S11 and Q25, $x^3$ is odd, so
$$
\int_{-1}^1x^3dx=0.
$$
Directly, $[x^4/4]_{-1}^1=0$. For P11, $\sin^5x$ is odd and the interval $[-\pi/2,\pi/2]$ is symmetric, hence its integral is also zero.

For the even function $x^2$ on the same type of interval,
$$
\int_{-1}^1x^2dx=2\int_0^1x^2dx=\frac{2}{3}.
$$

## Periodic intervals can be translated

If $f(x+T)=f(x)$ for every $x$, then for any $a$,
$$
\int_a^{a+T}f(x)dx=\int_0^Tf(x)dx.
$$
For example, $|\sin x|$ has period $\pi$, so every interval of length $\pi$ has the same total area $2$.

:::warn title="Cancellation is not positive area"
The odd-function result gives signed cancellation. The total area of $y=x^3$ on $[-1,1]$ is $2\int_0^1x^3dx=1/2$, not zero. Use absolute values when the question asks for geometric area.
:::
