---
id: jee-01
part: jee
title: "Definite Integrals as Limits of Riemann Sums"
---

## Accumulation begins with a partition

For a bounded function $f$ on $[a,b]$, divide the interval into $n$ equal pieces of width
$$
\Delta x=\frac{b-a}{n},\qquad x_i=a+i\Delta x.
$$
The right-endpoint Riemann sum is
$$
R_n=\sum_{i=1}^{n}f(x_i)\Delta x.
$$
For continuous $f$, these sums approach the definite integral:
$$
\int_a^b f(x)\,dx=\lim_{n\to\infty}\frac{b-a}{n}
\sum_{i=1}^{n}f\left(a+i\frac{b-a}{n}\right).
$$
The integral is a **signed** accumulator: heights below the $x$-axis contribute negatively.

:::diagram
{
  "type": "flow",
  "title": "A Riemann sum becomes an integral only in the limit",
  "steps": [
    {"title": "Partition", "detail": "Choose the interval, sample points and a small width Delta x."},
    {"title": "Approximate", "detail": "Add signed rectangle heights times their widths."},
    {"title": "Refine", "detail": "Let the largest subinterval width tend to zero."},
    {"title": "Identify", "detail": "Match the limit to the definite integral when convergence is known."}
  ],
  "caption": "A finite rectangle sum is an approximation or a discrete identity. The limiting process is what defines the continuous accumulation."
}
:::

:::example title="Evaluate the source's x-squared area directly as a limit"
For $f(x)=x^2$ on $[0,2]$, $\Delta x=2/n$ and $x_i=2i/n$. Therefore
$$
R_n=\frac{2}{n}\sum_{i=1}^{n}\left(\frac{2i}{n}\right)^2
=\frac{8}{n^3}\sum_{i=1}^{n}i^2.
$$
Using $\sum_{i=1}^{n}i^2=n(n+1)(2n+1)/6$,
$$
R_n=\frac{4(n+1)(2n+1)}{3n^2}\longrightarrow\frac{8}{3}.
$$
Thus $\int_0^2x^2dx=8/3$. The editable visual lab recreates the source's right-endpoint rectangles.
:::

## A Riemann sum can also be the unknown in a limit

If a limit has the form
$$
\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}f\left(\frac{i}{n}\right),
$$
then it equals $\int_0^1f(x)dx$, provided $f$ is integrable. For example,
$$
\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}\frac{i}{n}
=\int_0^1x\,dx=\frac{1}{2}.
$$

:::warn title="Do not call signed area by the shorter word area alone"
On $[-1,1]$, $\int_{-1}^{1}x^3dx=0$, but the geometric area between the cubic and the axis is $1/2$. Total area requires $\int_a^b|f(x)|dx$ and a split at zeros.
:::
