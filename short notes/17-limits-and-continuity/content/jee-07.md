---
id: jee-07
part: jee
title: "Continuity — When the Limit Equals the Value"
---

## Three conditions must all hold

A function $f$ is continuous at $a$ when
$$
f(a)\text{ is defined},\qquad \lim_{x\to a}f(x)\text{ exists},\qquad \lim_{x\to a}f(x)=f(a).
$$
On an interval, continuity means this condition at every point, using one-sided limits at included endpoints. On a domain with isolated points or excluded points, always interpret the statement relative to that domain.

A limit can exist without continuity: if $f(x)=x^2$ for $x\ne1$ but $f(1)=3$, then the limit at $1$ is $1$ while the value is $3$. The discontinuity is removable by redefining $f(1)=1$.

## Name the failure precisely

- **Removable:** a finite two-sided limit exists, but the value is missing or different.
- **Jump:** both one-sided limits are finite but unequal.
- **Infinite:** at least one side is unbounded.
- **Oscillatory:** nearby values fail to settle, as for $\sin(1/x)$ at $0$.

:::diagram
{
  "type": "graph",
  "title": "A greatest-integer step has unequal one-sided limits",
  "xrange": [-0.2, 3.2], "yrange": [-0.5, 2.7],
  "xticks": [0, 1, 2, 3], "yticks": [0, 1, 2],
  "curves": [
    {"expr": "0*x", "from": 0, "to": 0.98},
    {"expr": "1+0*x", "from": 1, "to": 1.98, "label": "floor(x)", "labpos": 0.50, "label_dy": 0.18},
    {"expr": "2+0*x", "from": 2, "to": 3}
  ],
  "points": [
    {"x": 0, "y": 0}, {"x": 1, "y": 0, "face": "white", "color": "#B91C1C"}, {"x": 1, "y": 1},
    {"x": 2, "y": 1, "label": "left limit 1", "face": "white", "color": "#B91C1C", "dx": -1.15, "dy": -0.30},
    {"x": 2, "y": 2, "label": "value and right limit 2", "dx": 0.15, "dy": 0.12}, {"x": 3, "y": 2, "face": "white", "color": "#B91C1C"}
  ],
  "caption": "At x=2 the left limit is 1, while the value and right limit are 2. This is a jump, not a removable hole."
}
:::

## Algebra and composition preserve continuity on their domains

Sums, differences, products and constant multiples of continuous functions remain continuous. A quotient is continuous where its denominator is nonzero, and a composition is continuous when the inner output belongs to the outer function's domain. Consequently polynomials, exponentials, sine and cosine are continuous everywhere; logarithms and roots are continuous on their domains.

The function $|x|$ is continuous at $0$ because both sides approach $|0|=0$. Its corner concerns differentiability, which is a separate condition studied in the next chapter.

:::example title="Match the value and the two one-sided limits"
For $x\leq2$, let $f(x)=kx+1$; for $x>2$, let $f(x)=3x-1$. At $2$,
$$
f(2)=2k+1,\qquad \lim_{x\to2^-}f(x)=2k+1,\qquad \lim_{x\to2^+}f(x)=5.
$$
Continuity therefore requires $2k+1=5$, so $k=2$. With this value, all three quantities equal $5$.
:::

:::warn title="A formula being defined is not enough"
The floor function has a value at every integer but is discontinuous there. Conversely, $1/x$ is continuous at every point of its domain $(-\infty,0)\cup(0,\infty)$, even though it has an infinite discontinuity at the excluded point $0$. Always distinguish “continuous on its domain” from “continuous everywhere on $\mathbb{R}$.”
:::
