---
id: jee-10
part: jee
title: "Feasible Optimisation — Standard Models"
---

## Reduce to one variable, but retain the feasible interval

An optimisation model has an objective, a constraint and a domain. Differentiate the reduced objective, then check every feasible candidate. A stationary point outside the physical domain is irrelevant.

:::example title="Fencing with a wall: the optimum is interior"
Let $x$ be each side perpendicular to the wall and $y$ the parallel side. With 40 m of fence,
$$
2x+y=40,\qquad A=x(40-2x),\qquad 0\leq x\leq20.
$$
Since $A'(x)=40-4x$, the only interior stationary point is $x=10$. The endpoint areas are zero, while $A(10)=200$. Thus the maximum area is $200$ m$^2$, with dimensions $10$ m by $20$ m.
:::

:::diagram
{
  "type": "graph",
  "title": "The feasible fencing area is a downward parabola",
  "xrange": [0, 20], "yrange": [0, 220],
  "xticks": [0, 5, 10, 15, 20], "yticks": [0, 50, 100, 150, 200],
  "xlabel": "x (m)", "ylabel": "area A",
  "curves": [{"expr": "40*x-2*x**2", "from": 0, "to": 20}],
  "points": [
    {"x": 0, "y": 0, "label": "endpoint", "dx": 0.5, "dy": 8},
    {"x": 10, "y": 200, "label": "maximum 200", "dx": 1.0, "dy": 8},
    {"x": 20, "y": 0, "label": "endpoint", "dx": -3.2, "dy": 22}
  ],
  "caption": "Here x is the side perpendicular to the wall. The vertex x=10 is feasible and gives y=20; both zero-area endpoints remain in the candidate comparison."
}
:::

:::example title="An open box: the second derivative and endpoints agree"
From a $12$ cm by $12$ cm sheet, cut squares of side $x$ from the corners. Then
$$
V(x)=x(12-2x)^2,\qquad 0\leq x\leq6.
$$
Differentiate and factor:
$$
V'(x)=(12-2x)(12-6x)=12(6-x)(2-x).
$$
The feasible interior stationary point is $x=2$, where $V=128$ cm$^3$ and $V''(2)=-48<0$. Since $V(0)=V(6)=0$, this is the absolute maximum.
:::

:::example title="Product with fixed sum; area with fixed perimeter"
For positive $x,y$ with $x+y=20$,
$$
P=x(20-x)=100-(x-10)^2,
$$
so the maximum product is $100$ at $x=y=10$. The same calculation with sum $10$ gives maximum $25$ at $x=y=5$.

For a rectangle of fixed perimeter $p$, write $l+b=p/2$ and
$$
A=l\left(\frac{p}{2}-l\right)=\frac{p^2}{16}-\left(l-\frac{p}{4}\right)^2.
$$
The greatest area is $p^2/16$, attained by the square with $l=b=p/4$. In both models the completed square proves the global conclusion.
:::

:::example title="Three positive factors with sum 1"
For $x+y+z=1$, fix $x$. Since $y+z=1-x$, the product $yz$ is at most $(1-x)^2/4$. Hence
$$
xyz\leq B(x)=\frac{x(1-x)^2}{4},\qquad 0<x<1.
$$
Now $4B'(x)=(1-x)(1-3x)$, so $B$ increases up to $x=1/3$ and decreases afterwards. Equality in the first step requires $y=z$. Thus the maximum is $1/27$ at $x=y=z=1/3$.
:::

:::warn title="Do not drop the constraints after eliminating a variable"
The expression $x(12-2x)^2$ makes algebraic sense for $x>6$, but those values produce a negative base length and are not box models. The feasible interval is part of the answer.
:::
