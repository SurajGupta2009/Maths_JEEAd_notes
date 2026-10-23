---
id: olympiad-03
part: olympiad
title: "Simson Line and Ptolemy"
---

## Simson line: an exact hypothesis

Let $ABC$ be a nondegenerate triangle and $P$ any point. The feet of perpendiculars from $P$ to the three **lines** $BC,CA,AB$ are collinear if and only if $P$ lies on the circumcircle of $ABC$. The word “lines” matters: a foot may fall on an extension of a side.

:::derive title="The cyclic quadrilaterals behind Simson"
Call the feet $D\in BC$, $E\in CA$, $F\in AB$. The right angles show $P,D,C,E$ and $P,D,B,F$ are cyclic. Directed angles modulo $180^\circ$ give
$$\angle EDF=\angle EDP+\angle PDF.$$
The two right-angle circles give $\angle EDP=\angle ECP$ and $\angle PDF=\angle PBF$. Since $E,C,A$ and $F,B,A$ lie on the same side-lines,
$$\angle ECP=\angle ACP,\qquad \angle PBF=\angle PBA.$$
If $A,B,C,P$ are concyclic, $\angle ACP=\angle ABP$, while $\angle PBA=-\angle ABP$ as directed angles, so $\angle EDF=0$ and the feet are collinear. Reversing the same equalities proves the converse in the nondegenerate case. Numerical collinearity alone is evidence, not a proof.
:::

## Ptolemy: order the vertices around the circle

For a convex cyclic quadrilateral $A,B,C,D$ in circular order,
$$AC\cdot BD=AB\cdot CD+BC\cdot DA.$$

:::derive title="A similarity proof"
Choose $E$ on diagonal $AC$ so that $\angle ABE=\angle CBD$. Since $A,B,C,D$ are cyclic and $E$ lies on $AC$, triangles $ABE$ and $CBD$ are similar, giving $AE\cdot BD=AB\cdot CD$. The remaining triangles $BCE$ and $BDA$ are similar, giving $CE\cdot BD=BC\cdot DA$. Add and use $AE+CE=AC$ to obtain Ptolemy.
:::

:::example title="Pythagoras is the rectangle case"
For a rectangle with adjacent sides $a,b$ and both diagonals $c$, Ptolemy gives $c^2=a^2+b^2$. The rectangle condition matters: a general cyclic quadrilateral with one diagonal a diameter does not by itself make Ptolemy reduce directly to that equation.
:::

:::warn title="Source-paper consistency correction"
A cyclic quadrilateral with successive sides $3,4,5,6$ and a diagonal of length $7$ cannot exist: that diagonal and the adjacent sides $3,4$ would form a degenerate triangle ($3+4=7$). Ptolemy's numerical equation alone is not an existence proof for arbitrary proposed side/diagonal data.
:::
