---
id: jee-90
part: jee
title: "Visual Exponential and Logarithm Lab — Shape, Inverse and Domain"
---

## The base changes the direction of growth

For $a>0$ and $a\ne1$, $f(x)=a^x$ has domain $\mathbb{R}$, range $(0,\infty)$, and passes through $(0,1)$. If $a>1$, it increases; if $0<a<1$, it decreases. In both cases the $x$-axis is a horizontal asymptote, but the axis is never reached at a finite $x$.

:::diagram
{
  "type": "graph",
  "title": "Growing and decaying exponentials are mirror images",
  "xrange": [-3, 3], "yrange": [-1, 8],
  "curves": [{"expr": "2**x", "label": "y = 2^x", "labpos": 0.82}, {"expr": "0.5**x", "label": "y = (1/2)^x", "labpos": 0.18, "color": "#B8860B"}],
  "hlines": [{"y": 1, "label": "common height 1"}],
  "points": [{"x": 0, "y": 1, "label": "(0, 1)", "dx": 0.15}],
  "caption": "Since 0.5^x = 2^(-x), the decay graph is obtained by reflecting the growth graph in the y-axis. Neither curve crosses the x-axis."
}
:::

The reflection identity $a^{-x}=(1/a)^x$ explains the whole picture. It also gives a quick comparison tool: for $a>1$, $a^u>a^v$ exactly when $u>v$; for $0<a<1$, the inequality reverses. When an exponential inequality has a variable base, first split into these base cases instead of applying a memorised rule blindly.

### A logarithm undoes the exponential

The equation $y=\log_a x$ means $a^y=x$. Consequently the logarithm has domain $(0,\infty)$ and range $\mathbb{R}$. Its graph passes through $(1,0)$ because $a^0=1$, and through $(a,1)$ because $a^1=a$. The vertical line $x=0$ is an asymptote.

<!-- pagebreak -->
## Logarithmic shape carries the laws

:::diagram
{
  "type": "graph",
  "title": "Logarithmic shape for bases greater and less than one",
  "xrange": [-0.5, 8], "yrange": [-4, 4], "xticks": [0, 1, 2, 4, 6, 8], "yticks": [-4, -2, 0, 2, 4],
  "curves": [{"expr": "log(x)/log(2)", "from": 0.05, "to": 8, "label": "log base 2", "labpos": 0.82}, {"expr": "log(x)/log(0.5)", "from": 0.05, "to": 8, "label": "log base 1/2", "labpos": 0.62, "color": "#B8860B"}],
  "points": [{"x": 1, "y": 0, "label": "(1, 0)", "dy": 0.35}, {"x": 2, "y": 1, "label": "(2, 1)", "dy": 0.2}, {"x": 2, "y": -1, "label": "(2, -1)", "dy": -0.55, "color": "#B8860B"}],
  "caption": "Every logarithm graph lies to the right of x = 0. Changing a base a > 1 to its reciprocal reflects the graph in the x-axis."
}
:::

The laws are therefore not arbitrary algebraic rules. Since $a^u a^v=a^{u+v}$, multiplication of inputs becomes addition of their logarithms. The hypothesis $M,N>0$ is essential: $\log_a(MN)$ can exist when both $M,N$ are negative, while $\log_a M$ and $\log_a N$ are not real. Expand only after writing the domain.

### A graph cannot replace the domain filter

Solve $\log_2(x-1)+\log_2(x-3)=3$. Before combining logs, require $x-1>0$ and $x-3>0$, hence $x>3$. On that domain,
$$
\log_2((x-1)(x-3))=3 \quad\Longrightarrow\quad (x-1)(x-3)=8.
$$
Thus $x^2-4x-5=0$, so $x=5$ or $x=-1$. Only $5$ survives the original domain.

<!-- pagebreak -->
## Candidate roots are not yet solutions

:::diagram
{
  "type": "numberline",
  "title": "The original domain selects the admissible root",
  "range": [-2.5, 6.5], "ticks": [-2, -1, 0, 1, 2, 3, 4, 5, 6], "xlabel": "x",
  "items": [
    {"kind": "interval", "a": 3, "b": 6.2, "closed_a": false, "closed_b": false, "label": "original domain: x > 3", "label_x": 4.5},
    {"kind": "points", "xs": [-1], "label": "algebraic candidate: reject", "label_x": -1, "label_y": 0.95, "color": "#B91C1C"},
    {"kind": "points", "xs": [5], "label": "admissible solution", "label_x": 5, "label_y": -1.05, "color": "#B8860B"}
  ],
  "caption": "The quadratic supplies candidates; the logarithm conditions decide which candidate is allowed. Substitution at x = 5 gives log2(4) + log2(2) = 3."
}
:::

:::warn title="Never repair an invalid input by simplifying harder"
At $x=-1$, the combined product $(x-1)(x-3)=8$ is positive, so the combined logarithm exists. The original two logarithms nevertheless do not exist over $\mathbb{R}$. This is why the domain must be copied from the original equation before any law is used.
:::

### Choose the method from the structure

A substitution $t=a^x$ is useful only with $t>0$. A common-base step is useful only when the base is valid and both sides are defined. Taking a logarithm of both sides requires positive sides. Each method has an admission ticket.

<!-- pagebreak -->
## Exponential and logarithmic equations: a reliable order

:::diagram
{
  "type": "flow",
  "title": "Domain first, algebra second, verification last",
  "steps": [
    {"title": "Record reality conditions", "detail": "Positive logarithm inputs, valid base, nonnegative even-root inputs, nonzero denominators."},
    {"title": "Make the two sides comparable", "detail": "Use one base, one logarithm, a substitution, or take a logarithm of two positive sides."},
    {"title": "Solve the simpler equation", "detail": "Keep every candidate until the end; do not silently divide by a factor that might be zero."},
    {"title": "Filter and verify", "detail": "Intersect with the original domain and substitute into the original, not the simplified, equation."}
  ],
  "caption": "Most wrong answers in this chapter come from skipping the first or last step, not from the algebra in the middle."
}
:::

:::example title="A substitution with two branches"
For $4^x-5\cdot2^x+4=0$, put $t=2^x$, so $t>0$ and $4^x=t^2$. Then $t^2-5t+4=0$, giving $t=1$ or $t=4$. Both are positive, so $2^x=1$ gives $x=0$ and $2^x=4$ gives $x=2$. Direct substitution gives $1-5+4=0$ and $16-20+4=0$. The condition $t>0$ is part of the substitution, not an afterthought.
:::

:::key title="What the pictures should leave behind"
An exponential never returns a nonpositive output; a logarithm never accepts a nonpositive input. Growth reverses when the base is replaced by its reciprocal. Graphs reveal sign, monotonicity and asymptotes, while the original domain remains the final authority for solutions.
:::


<!-- pagebreak -->
## Worked synthesis: growth models become logarithm models

An exponential model carries both a starting value and a time unit. For $N(t)=80\cdot3^{t/5}$, the initial value is $N(0)=80$ and the multiplication by $3$ occurs every $5$ time units. To find when $N(t)=720$, divide before taking a logarithm:
$$
3^{t/5}=9=3^2\quad\Longrightarrow\quad t=10.
$$
The equivalent logarithmic calculation is $t=5\log_3 9=10$. Substitution gives $80\cdot3^2=720$, verifying both the value and the time unit.

:::example title="Decay uses the same equation, not a new trick"
For $Q(t)=64(1/2)^{t/3}$, solve $Q(t)=4$. Then $(1/2)^{t/3}=1/16=(1/2)^4$, so $t=12$. A negative exponential rate would produce the same conclusion after logarithms; the essential hypotheses are a positive base different from $1$ and a positive target-to-initial ratio.
:::

:::warn title="Do not take a logarithm before isolating the exponential"
In an equation such as $a b^{kt}+c=d$, first obtain $b^{kt}=(d-c)/a$ and check that the right side is positive. Only then is the real logarithm step available.
:::

:::key title="Interpret the answer"
Report what the computed $t$ measures, check whether the model asks for elapsed time or calendar time, and substitute into the original model. A numerically correct exponent with the wrong unit is not a correct model solution.
:::
