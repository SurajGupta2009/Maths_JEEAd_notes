---
id: jee-01
part: jee
title: "The Meaning of a Limit — Approach and ε–δ"
---

## A limit describes approach, not attendance

Write $\lim_{x\to a}f(x)=L$ when $f(x)$ stays arbitrarily close to $L$ whenever $x$ is sufficiently close to $a$, **with $x\ne a$**. The value $f(a)$ may be different, or may not exist at all.

For example,
$$
\frac{x^2-1}{x-1}=x+1\qquad(x\ne1),
$$
so its limit as $x\to1$ is $2$, even though the original expression is undefined at $1$. Cancellation changes the formula only at the excluded point, which the limit already ignores.

## The ε–δ definition makes “arbitrarily close” precise

The statement $\lim_{x\to a}f(x)=L$ means:
$$
\forall\varepsilon>0\ \exists\delta>0:\quad
0<|x-a|<\delta\ \Longrightarrow\ |f(x)-L|<\varepsilon.
$$
You choose an output tolerance $\varepsilon$; a working $\delta$ must keep every punctured input in that band inside the output tolerance. One successful $\delta$ can always be replaced by a smaller positive one.

:::example title="A complete ε–δ proof for a linear function"
To prove $\lim_{x\to2}(3x+1)=7$, observe
$$
|(3x+1)-7|=3|x-2|.
$$
Given $\varepsilon>0$, choose $\delta=\varepsilon/3$. Then
$$
0<|x-2|<\delta\quad\Longrightarrow\quad |(3x+1)-7|<3\delta=\varepsilon.
$$
For the illustrated choice $\varepsilon=3/2$, the corresponding $\delta=1/2$ works exactly.
:::

:::diagram
{
  "type": "graph",
  "title": "A delta-band on x controls the epsilon-band on y",
  "xrange": [0.5, 3.5], "yrange": [3.5, 10],
  "xticks": [1, 1.5, 2, 2.5, 3], "yticks": [4, 5.5, 7, 8.5, 10],
  "curves": [{"expr": "3*x+1", "label": "y = 3x + 1", "labpos": 0.80, "label_dx": -0.65, "label_dy": 0.25}],
  "hlines": [{"y": 5.5, "label": "L-eps = 5.5"}, {"y": 7, "label": "L = 7"}, {"y": 8.5, "label": "L+eps = 8.5"}],
  "bands": [{"a": 1.5, "b": 2.5, "label": "a-delta to a+delta, delta = 1/2"}],
  "points": [{"x": 2, "y": 7, "label": "(2,7)", "dx": 0.15, "dy": -0.55}],
  "caption": "For 1.5 < x < 2.5, the graph stays between 5.5 and 8.5. The puncture x != 2 matters in the definition, even though this line is defined there."
}
:::

## Two one-sided limits must agree

The two-sided limit exists and equals $L$ exactly when
$$
\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L.
$$
A finite one-sided limit can exist on just one side when the domain lies only on that side, as with $\sqrt{x}$ at $0$.

:::example title="The greatest-integer function jumps at an integer"
At $x=2$,
$$
\lim_{x\to2^-}\lfloor x\rfloor=1,
\qquad
\lim_{x\to2^+}\lfloor x\rfloor=2.
$$
Therefore the two-sided limit does not exist. At a noninteger, the function is locally constant and its two-sided limit does exist.
:::

:::warn title="Defined, finite and convergent are different claims"
A function can be defined at $a$ and still have no limit there. It can have a limit without being defined there. And writing $f(x)\to\infty$ describes unbounded divergence, not a finite limit. State which claim you are making before calculating.
:::
