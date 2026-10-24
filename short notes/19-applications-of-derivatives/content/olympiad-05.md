---
id: olympiad-05
part: olympiad
title: "Extension V — Symmetric Optimisation and Its Frontier"
---

## Symmetry suggests equal variables; monotonicity in the product proves it

For positive $x,y$ with fixed sum $t$, put $s=xy$. Then
$$
0<s\leq\frac{t^2}{4},
$$
with equality at $x=y=t/2$. A symmetric expression rewritten in terms of $t$ and $s$ is optimised by checking whether it increases or decreases in $s$.

:::example title="Two minima with x+y=10"
Since $s=xy\leq25$,
$$
\frac{1}{x}+\frac{1}{y}=\frac{10}{s}\geq\frac{10}{25}=\frac{2}{5},
$$
and
$$
x^2+y^2=100-2s\geq100-50=50.
$$
Both minima occur at $x=y=5$.
:::

For positive $x,y,z$ with $x+y+z=1$, AM–GM gives
$$
xyz\leq\left(\frac{x+y+z}{3}\right)^3=\frac{1}{27},
$$
with equality at $x=y=z=1/3$. A one-variable alternative fixes $x$ and uses $yz\leq(1-x)^2/4$, then maximises $x(1-x)^2/4$ by differentiation.

## The symmetric cubic is a counterexample to blind equalising

For positive $x,y$ with $x+y=6$,
$$
x^3+y^3=216-18xy
=18(x-3)^2+54.
$$
Since $xy\leq9$, the attained minimum is $54$ at $x=y=3$. But as $x\to0^+$ and $y\to6$, the value approaches $216$ from below. Therefore the **supremum is $216$ and no maximum is attained** on the positive domain.

:::diagram
{
  "type": "graph",
  "title": "The symmetric cubic has an interior minimum but no attained maximum",
  "xrange": [0, 6], "yrange": [0, 230],
  "xticks": [0, 1, 2, 3, 4, 5, 6], "yticks": [0, 50, 100, 150, 200],
  "curves": [{"expr": "x**3+(6-x)**3", "from": 0.001, "to": 5.999}],
  "points": [
    {"x": 0, "y": 216, "label": "not attained", "dx": 0.2, "dy": -18, "face": "#FFFFFF", "color": "#B91C1C"},
    {"x": 3, "y": 54, "label": "minimum 54", "dx": 0.25, "dy": 10},
    {"x": 6, "y": 216, "label": "not attained", "dx": -1.4, "dy": -18, "face": "#FFFFFF", "color": "#B91C1C"}
  ],
  "caption": "The graph shows x^3+y^3 after substituting y=6-x. Hollow red endpoints mark limits outside the positive domain; the interior point (3,54) is the attained minimum."
}
:::

As a numerical check, at $(x,y)=(0.1,5.9)$ the value is $0.001+205.379=205.38$, close to but below $216$. This corrects the companion solution's printed check value $205.8$.

## Equal variables minimise a sum of squares under a plane constraint

For positive $x,y,z$ with $x+y+z=1$,
$$
\left(x-\frac{1}{3}\right)^2+
\left(y-\frac{1}{3}\right)^2+
\left(z-\frac{1}{3}\right)^2
=x^2+y^2+z^2-\frac{1}{3}.
$$
Hence
$$
x^2+y^2+z^2\geq\frac{1}{3},
$$
with equality exactly when $x=y=z=1/3$. The same completed-square argument proves the Lagrange example in Extension IV.

:::warn title="Always identify whether the objective increases or decreases in s"
Equal variables maximise $xy$ and minimise $x^2+y^2$ for a fixed positive sum, but they minimise rather than maximise $x^3+y^3$. Symmetry alone does not choose the type of extremum.
:::
