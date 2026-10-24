---
id: olympiad-04
part: olympiad
title: "Extension IV — Stirling, Harmonic Limits and Rates"
---

## Asymptotic equivalence preserves ratios, not differences

Write $u_n\sim v_n$ when $u_n/v_n\to1$. Stirling's formula states
$$
n!\sim\sqrt{2\pi n}\left(\frac{n}{e}\right)^n.
$$
One proof compares $\ln(n!)=\sum_{k=1}^n\ln k$ with an integral and then tracks the correction terms. The formula is especially useful when factorial powers cancel in a ratio.

:::example title="Central-binomial decay"
Applying Stirling to numerator and denominator,
$$
(2n)!\sim\sqrt{4\pi n}\left(\frac{2n}{e}\right)^{2n},
\qquad
(n!)^2\sim2\pi n\left(\frac{n}{e}\right)^{2n}.
$$
Therefore
$$
\frac{(2n)!}{4^n(n!)^2}\sim\frac{1}{\sqrt{\pi n}}.
$$
In particular the ratio tends to $0$, while $n$ times its square tends to $1/\pi$. Merely writing every factorial as “large” would lose this exact decay rate.
:::

## Harmonic sums separate a logarithm from a constant

The Euler–Mascheroni constant is defined by
$$
H_n-\ln n\longrightarrow\gamma\approx0.5772156649.
$$
Consequently $H_n/\ln n\to1$, but the difference $H_n-\ln n$ does **not** tend to $0$. This illustrates why asymptotic equivalence cannot automatically be subtracted.

:::example title="Cancel gamma without assuming it is zero"
Since $\ln(2n)=\ln2+\ln n$,
$$
H_{2n}-H_n
=(H_{2n}-\ln(2n))-(H_n-\ln n)+\ln2
\longrightarrow\gamma-\gamma+\ln2=\ln2.
$$
Thus $H_{2n}-H_n-\ln2\to0$, while $H_{2n}-H_n$ itself tends to $\ln2$.
:::

## A second-order term determines the convergence rate

The notation $R_n=O(n^{-2})$ means $|R_n|\leq Cn^{-2}$ for some constant $C$ and all large $n$. Starting with
$$
\ln(1+x)=x-\frac{x^2}{2}+O(x^3)\qquad(x\to0),
$$
put $x=1/n$ and multiply by $n$:
$$
n\ln\!\left(1+\frac{1}{n}\right)=1-\frac{1}{2n}+O(n^{-2}).
$$
Exponentiating and expanding $e^u=1+u+O(u^2)$ gives
$$
\left(1+\frac{1}{n}\right)^n
=e\left(1-\frac{1}{2n}+O(n^{-2})\right).
$$
Therefore
$$
n\left[\left(1+\frac{1}{n}\right)^n-e\right]\longrightarrow-\frac{e}{2}.
$$

:::diagram
{
  "type": "graph",
  "title": "Multiplying the error by n exposes the constant -e/2",
  "xrange": [0, 100], "yrange": [-2.5, -1.2],
  "xticks": [0, 25, 50, 75, 100], "yticks": [-2.5, -2, -1.359140914, -1.2],
  "yticklabels": ["-2.5", "-2", "-e/2", "-1.2"],
  "curves": [{"expr": "x*(exp(x*log(1+1/x))-e)", "from": 1, "to": 100, "label": "n[(1+1/n)^n-e]", "labpos": 0.68, "label_dy": -0.45}],
  "hlines": [{"y": -1.359140914, "label": "y = -e/2"}],
  "caption": "The unscaled error tends to 0, but the scaled error tends to -e/2. A graph of the original sequence alone would hide this first-order rate."
}
:::

:::warn title="The leading limit and the rate answer different questions"
The statements $(1+1/n)^n\to e$ and $n[(1+1/n)^n-e]\to-e/2$ are compatible. The second contains more information. To obtain it, expand one order beyond the first constant term and keep the Big-O remainder under control.
:::
