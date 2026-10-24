---
id: jee-04
part: jee
title: "Exponential, Logarithmic and Power Limits"
---

## The two first-order standards

Near $x=0$,
$$
\lim_{x\to0}\frac{e^x-1}{x}=1,
\qquad
\lim_{x\to0}\frac{\ln(1+x)}{x}=1.
$$
They describe the first-order behaviour of the exponential and logarithm. Substitution rescales them: for fixed $k$,
$$
\frac{e^{kx}-1}{x}=k\cdot\frac{e^{kx}-1}{kx}\longrightarrow k.
$$
For $a>0$, writing $a^x=e^{x\ln a}$ gives
$$
\lim_{x\to0}\frac{a^x-1}{x}=\ln a.
$$
Thus $(2^x-1)/x\to\ln2$ and $(e^{3x}-1)/x\to3$.

## The number e is a continuous exponential limit

For $x>-1$ and $x\ne0$, set
$$
y=(1+x)^{1/x}.
$$
Taking logarithms and using continuity of $\ln$ and $\exp$,
$$
\ln y=\frac{\ln(1+x)}{x}\longrightarrow1
\quad\Longrightarrow\quad y\longrightarrow e.
$$
Replacing $x$ by $1/x$ also gives $(1+1/x)^x\to e$ as $x\to\infty$. More generally, $(1+3/x)^x\to e^3$. By the quotient law, $(1+1/n)^n/n\to0$; this needs no Stolz–Cesàro argument.

:::diagram
{
  "type": "graph",
  "title": "The removable gap at x=0 has height e",
  "xrange": [-0.75, 2], "yrange": [1, 6],
  "xticks": [-0.5, 0, 0.5, 1, 1.5, 2], "yticks": [1, 2, 2.71828, 4, 6],
  "yticklabels": ["1", "2", "e", "4", "6"],
  "curves": [
    {"expr": "exp(log(1+x)/x)", "from": -0.70, "to": -0.02, "clip": 6, "color": "#0F766E"},
    {"expr": "exp(log(1+x)/x)", "from": 0.02, "to": 2, "label": "(1+x)^(1/x)", "labpos": 0.70, "label_dy": 0.30}
  ],
  "hlines": [{"y": 2.718281828, "label": "y = e"}],
  "points": [{"x": 0, "y": 2.718281828, "label": "open target (0,e)", "face": "white", "color": "#B91C1C", "dx": 0.12, "dy": 0.20}],
  "caption": "The formula is undefined at 0, but the logarithm of the expression tends to 1 from both sides. Continuity of exp therefore forces the limit e."
}
:::

## Convert a 1^∞ form into a product before taking the limit

If $f(x)\to0$, $1+f(x)>0$ near the approach, and $f(x)g(x)\to L$, then
$$
(1+f(x))^{g(x)}
=\exp\!\left(g(x)\ln(1+f(x))\right)\longrightarrow e^L,
$$
because, interpreting the last quotient by its removable value $1$ if $f(x)=0$,
$$
g(x)\ln(1+f(x))=[f(x)g(x)]\frac{\ln(1+f(x))}{f(x)}\longrightarrow L.
$$

:::example title="Extract the exponent coefficient exactly"
As $x\to0$,
$$
(1+2x)^{3/x}\longrightarrow e^6,
$$
since $f(x)=2x$, $g(x)=3/x$, and $f(x)g(x)=6$. The base tends to $1$, but the exponent grows rapidly enough to preserve a finite non-$1$ limit.
:::

:::warn title="Do not substitute 1^∞ = 1"
The forms $1^\infty$, $0^0$ and $\infty^0$ are indeterminate because base and exponent compete. Take a logarithm first, and check that the logarithm's limit exists before exponentiating. Also record the domain condition $1+f(x)>0$ for a real variable exponent.
:::
