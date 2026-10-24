---
id: olympiad-03
part: olympiad
title: "Extension III — Limits of Sums and Products"
---

## Recognize a right-endpoint Riemann sum

For continuous $f$ on $[0,1]$,
$$
\frac{1}{n}\sum_{k=1}^n f\!\left(\frac{k}{n}\right)
\longrightarrow\int_0^1 f(x)\,dx.
$$
The factor $1/n$ is the mesh and $k/n$ are right endpoints. This extension previews the definite-integral theory developed fully in Chapter 21; here it is used as a sequence-limit technique.

:::example title="Expose the sample point before integrating"
$$
\sum_{k=1}^n\frac{n}{n^2+k^2}
=\frac{1}{n}\sum_{k=1}^n\frac{1}{1+(k/n)^2}
\longrightarrow\int_0^1\frac{dx}{1+x^2}=\frac{\pi}{4}.
$$
Similarly,
$$
\frac{1}{n}\sum_{k=1}^n\frac{1}{1+k/n}
\longrightarrow\int_0^1\frac{dx}{1+x}=\ln2.
$$
:::

For $p>0$, factoring $n^p$ gives
$$
\frac{1^p+2^p+\cdots+n^p}{n^{p+1}}
=\frac{1}{n}\sum_{k=1}^n\left(\frac{k}{n}\right)^p
\longrightarrow\frac{1}{p+1}.
$$
The values $p=1/2,1,2,3$ give $2/3,1/2,1/3,1/4$ respectively.

:::key title="Keep the mesh, sample point and error order visible"
A sum is not a Riemann sum until the factor $1/n$ and the sampled function are explicit. A product is not evaluated by replacing every factor by $1$: infinitely many small contributions can add to a nonzero logarithm.
:::

:::diagram
{
  "type": "graph",
  "title": "Eight right endpoints approximate the area under y=x^2",
  "xrange": [0, 1.05], "yrange": [0, 1.1],
  "xticks": [0, 0.25, 0.5, 0.75, 1], "yticks": [0, 0.5, 1],
  "curves": [{"expr": "x**2", "from": 0, "to": 1, "label": "y=x^2", "labpos": 0.72, "label_dy": 0.10}],
  "rays": [
    {"x": [0.125, 0.125], "y": [0, 0.015625]}, {"x": [0.25, 0.25], "y": [0, 0.0625]},
    {"x": [0.375, 0.375], "y": [0, 0.140625]}, {"x": [0.5, 0.5], "y": [0, 0.25]},
    {"x": [0.625, 0.625], "y": [0, 0.390625]}, {"x": [0.75, 0.75], "y": [0, 0.5625]},
    {"x": [0.875, 0.875], "y": [0, 0.765625]}, {"x": [1, 1], "y": [0, 1]}
  ],
  "points": [
    {"x": 0.125, "y": 0.015625}, {"x": 0.25, "y": 0.0625}, {"x": 0.375, "y": 0.140625}, {"x": 0.5, "y": 0.25},
    {"x": 0.625, "y": 0.390625}, {"x": 0.75, "y": 0.5625}, {"x": 0.875, "y": 0.765625}, {"x": 1, "y": 1}
  ],
  "caption": "For n=8 the right-endpoint sum is 51/128 = 0.3984375, above the limit 1/3. Increasing n refines the mesh; the samples are not an unweighted average."
}
:::

## Products become sums after logarithms

Let
$$
P_n=\prod_{k=1}^n\left(1+\frac{k}{n^2}\right).
$$
Then $\ln P_n=\sum_{k=1}^n\ln(1+k/n^2)$. For $x\geq0$,
$$
x-\frac{x^2}{2}\leq\ln(1+x)\leq x.
$$
Summing the upper bound gives
$$
\sum_{k=1}^n\frac{k}{n^2}=\frac{n+1}{2n}\longrightarrow\frac{1}{2}.
$$
The subtracted error is bounded by
$$
\frac{1}{2}\sum_{k=1}^n\frac{k^2}{n^4}
=\frac{n(n+1)(2n+1)}{12n^4}\longrightarrow0.
$$
Hence $\ln P_n\to1/2$, and continuity of the exponential gives $P_n\to\sqrt{e}$.
