---
id: olympiad-02
part: olympiad
title: "Extension II — Stolz–Cesàro and Recursive Sequences"
---

## Stolz–Cesàro is a discrete quotient rule

If $b_n$ is strictly increasing and unbounded, and
$$
\frac{a_{n+1}-a_n}{b_{n+1}-b_n}\longrightarrow L,
$$
then $a_n/b_n\longrightarrow L$. The denominator increments are eventually positive, so the difference quotient controls successive weighted averages. Check the monotonicity and unboundedness before using the rule.

:::example title="Arithmetic sums and harmonic growth"
For $a_n=1+2+\cdots+n$ and $b_n=n^2$,
$$
\frac{a_{n+1}-a_n}{b_{n+1}-b_n}
=\frac{n+1}{2n+1}\longrightarrow\frac{1}{2},
$$
so $(1+\cdots+n)/n^2\to1/2$.

For $H_n=1+1/2+\cdots+1/n$ and $b_n=\ln n$,
$$
\frac{H_{n+1}-H_n}{\ln(n+1)-\ln n}
=\frac{1/(n+1)}{\ln(1+1/n)}\longrightarrow1.
$$
Thus $H_n/\ln n\to1$.
:::

## A recursive sequence needs convergence before algebra

If $a_{n+1}=f(a_n)$ with continuous $f$ and $a_n\to L$, then passing to the limit gives $L=f(L)$. That equation is the **last** step, not a proof that the sequence converges. A common positive proof is monotone + bounded.

:::example title="A nested-square-root recurrence"
Let $a_1=1$ and $a_{n+1}=\sqrt{2+a_n}$. If $1\leq a_n<2$, then
$$
a_{n+1}=\sqrt{2+a_n}<2.
$$
Also $a_{n+1}\geq a_n$ because $2+a_n\geq a_n^2$ is equivalent to $(2-a_n)(a_n+1)\geq0$. The base case $a_1=1$ starts the induction, so the sequence is increasing and bounded above by $2$.

Therefore $L$ exists and
$$
L=\sqrt{2+L}\quad\Longrightarrow\quad L^2-L-2=0.
$$
The roots are $2$ and $-1$; positivity selects $L=2$.
:::

:::diagram
{
  "type": "graph",
  "title": "The recurrence increases toward its fixed point 2",
  "xrange": [0.5, 6.5], "yrange": [0.5, 2.2],
  "xticks": [1, 2, 3, 4, 5, 6], "yticks": [1, 1.5, 2],
  "curves": [{"expr": "2+0*x", "from": 0.5, "to": 6.5, "label": "candidate fixed point 2", "labpos": 0.68, "label_dy": 0.08, "color": "#5B6B84", "ls": "--"}],
  "rays": [{"x": [1, 2, 3, 4, 5, 6], "y": [1, 1.732050808, 1.931851653, 1.982889723, 1.995717846, 1.998929175]}],
  "points": [
    {"x": 1, "y": 1, "label": "a1=1", "dx": 0.1, "dy": -0.15},
    {"x": 2, "y": 1.732050808}, {"x": 3, "y": 1.931851653}, {"x": 4, "y": 1.982889723},
    {"x": 5, "y": 1.995717846}, {"x": 6, "y": 1.998929175, "label": "a6 ~1.998929", "dx": -1.15, "dy": -0.18}
  ],
  "caption": "The dots are sequence terms, not a continuous function. Monotone increase and the upper bound prove convergence before the fixed-point equation is used."
}
:::

:::example title="Heron's iteration converges downward to sqrt(2)"
Let $a_1=2$ and $a_{n+1}=(a_n+2/a_n)/2$. AM–GM gives $a_{n+1}\geq\sqrt{2}$. When $a_n\geq\sqrt{2}$, we also have $2/a_n\leq a_n$, so $a_{n+1}\leq a_n$. Thus the sequence is decreasing and bounded below.

Its limit satisfies $L=(L+2/L)/2$, so $L^2=2$. Positivity gives $L=\sqrt{2}$, not the algebraic alternative $-\sqrt{2}$.
:::

:::example title="An exponent-tracking recurrence"
For $a_1=\sqrt{2}$ and $a_{n+1}=\sqrt{2a_n}$, induction gives
$$
a_n=2^{1-2^{-n}}\longrightarrow2.
$$
Here an explicit exponent formula replaces the monotone-and-bounded argument.
:::

:::warn title="A fixed-point equation can have extraneous candidates"
Writing $L=f(L)$ before proving convergence may produce numbers that the sequence never approaches. Establish monotonicity and a bound, or another convergence argument, then use continuity and discard candidates using sign and range information.
:::
