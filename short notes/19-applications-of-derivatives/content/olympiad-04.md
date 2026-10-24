---
id: olympiad-04
part: olympiad
title: "Extension IV — Director Circles and Lagrange Multipliers"
---

## Perpendicular ellipse tangents determine a concentric circle

For the ellipse $x^2/a^2+y^2/b^2=1$, a nonvertical tangent of slope $m$ can be written
$$
y=mx\pm\sqrt{a^2m^2+b^2}.
$$
If it passes through $P=(x,y)$, rearranging and squaring gives
$$
(x^2-a^2)m^2-2xym+(y^2-b^2)=0.
$$
The two tangent slopes from $P$ are perpendicular exactly when their product is $-1$. By the product of roots,
$$
\frac{y^2-b^2}{x^2-a^2}=-1
\quad\Longrightarrow\quad
x^2+y^2=a^2+b^2.
$$
This is the **director circle**. Vertical or horizontal tangent cases satisfy the same locus directly.

:::example title="The 5-3 ellipse and the circle special case"
For $x^2/25+y^2/9=1$, perpendicular tangents meet at $P$ with
$$
|OP|^2=25+9=34,
\qquad |OP|=\sqrt{34}\approx5.831.
$$
When $a=b=R$, the ellipse is a circle and the director circle has radius $\sqrt{2}R$. Thus perpendicular tangents to $x^2+y^2=R^2$ meet at distance $\sqrt{2}R$ from the centre.
:::

:::diagram
{
  "type": "graph",
  "title": "Perpendicular tangents to the ellipse meet on its director circle",
  "ratio": 0.85,
  "xrange": [-7, 7], "yrange": [-6, 6],
  "xticks": [-6, -4, -2, 0, 2, 4, 6], "yticks": [-6, -3, 0, 3, 6],
  "curves": [
    {"expr": "3*sqrt(1-x**2/25)", "from": -5, "to": 5},
    {"expr": "-3*sqrt(1-x**2/25)", "from": -5, "to": 5},
    {"expr": "sqrt(34-x**2)", "from": -5.830951895, "to": 5.830951895, "color": "#B7791F"},
    {"expr": "-sqrt(34-x**2)", "from": -5.830951895, "to": 5.830951895, "color": "#B7791F"}
  ],
  "vlines": [{"x": 5, "label": "x=5", "dx": -0.7}],
  "hlines": [{"y": 3, "label": "y=3"}],
  "points": [{"x": 5, "y": 3, "label": "P(5,3)", "dx": 0.25, "dy": 0.25}],
  "caption": "The teal ellipse has perpendicular tangents x=5 and y=3 at (5,0) and (0,3). They meet at P=(5,3), which lies on the gold director circle x^2+y^2=34."
}
:::

## Lagrange multipliers encode a constrained stationary point

To extremise $f$ subject to $g=0$, a regular interior extremum satisfies $\nabla f=\lambda\nabla g$. For
$$
f=x^2+y^2+z^2,\qquad g=x+y+z-3=0,
$$
this gives $2x=2y=2z=\lambda$. Hence $x=y=z$, and the constraint gives $x=y=z=1$. The candidate value is $3$.

A global proof is immediate:
$$
x^2+y^2+z^2-3=(x-1)^2+(y-1)^2+(z-1)^2\geq0
$$
when $x+y+z=3$. Thus the minimum is $3$ at $(1,1,1)$, not merely a stationary candidate.

:::warn title="Multipliers find candidates; a separate argument establishes global extrema"
Check regularity, boundaries and attainment. Here the completed squares supply the missing global comparison in one line.
:::
