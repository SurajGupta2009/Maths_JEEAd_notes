---
id: jee-08
part: jee
title: "Orthogonal Trajectories — Replace Slope Correctly"
---

## Eliminate the family parameter, then rotate the tangent

If a family satisfies $y'=p(x,y)$, an intersecting curve with finite nonzero perpendicular slope satisfies
$$
y'=-\frac{1}{p(x,y)}.
$$
Solve that new differential equation. Horizontal and vertical tangents need geometric handling because a finite-slope formula alone cannot express every perpendicular direction.

:::diagram
{
  "type": "flow",
  "title": "Orthogonality acts on the differential equation, not on the original y-formula",
  "steps": [
    {"title": "Form", "detail": "Differentiate the given family and eliminate its arbitrary parameter."},
    {"title": "Rotate", "detail": "Replace a finite nonzero slope p by its negative reciprocal -1/p."},
    {"title": "Solve", "detail": "Integrate the new equation and add the trajectory constant."},
    {"title": "Restore directions", "detail": "Check vertical or horizontal lines missed by the finite-slope calculation."}
  ],
  "caption": "The negative reciprocal is applied after eliminating the family parameter, not to the parameter itself."
}
:::

:::example title="S10 and Q19: parabolas become ellipses"
For $y=cx^2$ on $x\neq0$, $c=y/x^2$ and $y'=2cx$, so the family equation is
$$
y'=\frac{2y}{x}.
$$
On a branch with finite nonzero slope, an orthogonal trajectory therefore satisfies
$$
\frac{dy}{dx}=-\frac{x}{2y}
\quad\Longrightarrow\quad 2y\,dy+x\,dx=0.
$$
Integration gives
$$
x^2+2y^2=C.
$$
For $C>0$, these are ellipses centred at the origin. The calculation is local away from the origin and from points where the required slope divisions fail.
:::

:::example title="P8 and Q20: the vertical radial line must be included"
For $x^2+y^2=c$, differentiation gives $x+yy'=0$. Away from coordinate-axis slope degeneracies, the orthogonal equation is
$$
\frac{dy}{dx}=\frac{y}{x}
\quad\Longrightarrow\quad
\frac{dy}{y}=\frac{dx}{x}.
$$
Thus $y=Cx$ on half-plane intervals. Geometrically, every radial line is orthogonal to every concentric circle it meets. Consequently the complete nondegenerate family is
$$
y=Cx,\qquad x=0.
$$
The vertical line is omitted if one reports only finite slopes; the source answer is corrected here.
:::

## A fast geometric check

Circles centred at the origin have radial normals. Their orthogonal trajectories must therefore be radial curves, namely straight lines through the same centre. For the parabolas $y=cx^2$, check an ellipse implicitly: $x+2yy'=0$, so its slope is $-x/(2y)$, whose product with $2y/x$ is $-1$ away from degenerate directions.

:::warn title="An arbitrary constant is not automatically a complete geometric family"
The formula $y=Cx$ excludes vertical lines. Whenever a derivation assumes a finite slope or divides by x or y, compare the result with the original geometry before calling it complete.
:::
