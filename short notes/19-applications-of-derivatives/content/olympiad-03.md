---
id: olympiad-03
part: olympiad
title: "Extension III — Envelopes and the Parabola Directrix"
---

## Differentiate the family with respect to its parameter

For $a>0$ and $m\ne0$, consider
$$
F(x,y,m)=y-mx-\frac{a}{m}=0.
$$
An envelope point satisfies both $F=0$ and $\partial F/\partial m=0$:
$$
-x+\frac{a}{m^2}=0
\quad\Longrightarrow\quad x=\frac{a}{m^2}.
$$
Substitution into the line gives $y=2a/m$. Therefore the contact point is
$$
\left(\frac{a}{m^2},\frac{2a}{m}\right),
$$
and eliminating $m$ yields $y^2=4ax$. Thus every line $y=mx+a/m$ touches this parabola at the stated point.

:::diagram
{
  "type": "graph",
  "title": "A family of lines envelops the parabola y^2=4x",
  "xrange": [-1.4, 4.2], "yrange": [-4.5, 5.5],
  "curves": [
    {"expr": "2*sqrt(x)", "from": 0, "to": 4},
    {"expr": "-2*sqrt(x)", "from": 0, "to": 4},
    {"expr": "0.5*x+2", "from": 0, "to": 4, "color": "#B7791F"},
    {"expr": "x+1", "from": 0, "to": 4, "color": "#B91C1C"},
    {"expr": "2*x+0.5", "from": 0, "to": 2.4, "color": "#5B6B84"}
  ],
  "vlines": [{"x": -1, "label": "directrix", "dx": 0.55}],
  "points": [
    {"x": 4, "y": 4, "label": ""},
    {"x": 1, "y": 2, "label": ""},
    {"x": 0.25, "y": 1, "label": ""}
  ],
  "annotations": [
    {"text": "m=1/2", "x": 4, "y": 4, "tx": 2.9, "ty": 5.1, "color": "#B7791F"},
    {"text": "m=1", "x": 1, "y": 2, "tx": 0.15, "ty": 3.6, "color": "#B91C1C"},
    {"text": "m=2", "x": 0.25, "y": 1, "tx": 1.0, "ty": 0.3, "color": "#5B6B84"}
  ],
  "caption": "For a=1, the gold, red and slate lines have m=1/2,1,2 and touch at the marked points. The red dashed line x=-1 is the directrix used in the perpendicular-tangent theorem."
}
:::

## Perpendicular tangents meet on the directrix

A tangent perpendicular to $y=mx+a/m$ has slope $-1/m$. Replacing $m$ by $-1/m$ in the family gives
$$
y=-\frac{x}{m}-am.
$$
At the intersection of the two tangents,
$$
mx+\frac{a}{m}=-\frac{x}{m}-am,
$$
so
$$
\left(m+\frac{1}{m}\right)(x+a)=0.
$$
Since $m+1/m\ne0$ for real $m$, the intersection has $x=-a$, the directrix of $y^2=4ax$.

:::warn title="Envelope differentiation uses the parameter, not x or y"
The equation $\partial F/\partial m=0$ is taken while $x$ and $y$ are held fixed. It supplies the second equation needed to locate the envelope and its contact point.
:::
