---
id: olympiad-01
part: olympiad
title: "Extension I — Supporting Lines, Jensen and a Cosine Bound"
---

## One tangent can prove a global inequality

If $f$ is differentiable and convex, then for every $a$ and $x$ in its interval,
$$
f(x)\geq f(a)+f'(a)(x-a).
$$
For $f(x)=x^2$ at $a=3$, the supporting line is
$$
y=9+6(x-3)=6x-9.
$$
Thus $x^2\geq6x-9$, with equality only at $x=3$. Independently, the difference is $(x-3)^2\geq0$.

:::diagram
{
  "type": "graph",
  "title": "A convex parabola lies above its supporting line",
  "xrange": [-1, 5], "yrange": [-10, 25],
  "xticks": [-1, 0, 1, 2, 3, 4, 5], "yticks": [-10, 0, 10, 20],
  "curves": [
    {"expr": "x**2", "from": -1, "to": 5},
    {"expr": "6*x-9", "from": 1.2, "to": 5, "color": "#B91C1C"}
  ],
  "points": [{"x": 3, "y": 9, "label": ""}],
  "annotations": [
    {"text": "contact (3,9)", "x": 3, "y": 9, "tx": 0.3, "ty": 14}
  ],
  "caption": "The red supporting line y=6x-9 touches the teal graph y=x^2 at x=3 and stays below it everywhere. Their difference is (x-3)^2."
}
:::

## Jensen follows by averaging supporting lines

Let $\lambda_i\geq0$ and $\sum_{i=1}^n\lambda_i=1$, and put $\bar x=\sum_{i=1}^n\lambda_i x_i$. Apply the supporting-line inequality at $\bar x$ to each $x_i$, multiply by $\lambda_i$, and add. The first-order terms cancel because $\sum\lambda_i(x_i-\bar x)=0$. Hence
$$
f(\bar x)\leq\sum_{i=1}^n\lambda_i f(x_i).
$$
For strictly convex $f$, equality requires all the $x_i$ with positive weights to coincide.

:::example title="Jensen for the exponential"
Since $D^2(e^x)=e^x>0$, for positive $a,b,c$,
$$
\frac{e^a+e^b+e^c}{3}\geq e^{(a+b+c)/3},
$$
with equality exactly when $a=b=c$. At $(1,2,3)$, the left side is approximately $10.0643$ and the right side is $e^2\approx7.3891$, so the inequality is strict.
:::

## Convexity of a difference can locate its global minimum

:::example title="Prove cos x >= 1-x^2/2 for every real x"
Let
$$
g(x)=\cos x-1+\frac{x^2}{2}.
$$
Then $g'(x)=x-\sin x$ and $g''(x)=1-\cos x\geq0$. Thus $g'$ is increasing. Since $g'(0)=0$, we have $g'<0$ for $x<0$ and $g'>0$ for $x>0$. Therefore $g$ decreases up to $0$ and increases afterwards, so
$$
g(x)\geq g(0)=0.
$$
Equality holds only at $x=0$. The argument uses monotonicity of $g'$, not an unsupported claim that $g''\geq0$ alone makes $g$ nonnegative.
:::
