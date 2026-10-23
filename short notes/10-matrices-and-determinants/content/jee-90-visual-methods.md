---
id: jee-90
part: jee
title: "Visual Matrix Lab — Transformations, Determinants and Linear Systems"
---

## Columns are images of the basis vectors

For $A=\begin{pmatrix}2&1\\0&1\end{pmatrix}$, the first column is $Ae_1=(2,0)^T$ and the second is $Ae_2=(1,1)^T$. The whole unit square maps to the parallelogram spanned by those two columns.

:::diagram
{
  "type": "geometry",
  "title": "A unit square becomes a parallelogram of area 2",
  "xrange": [-0.5, 3], "yrange": [-0.5, 2], "grid": true,
  "elements": [
    {"kind": "polygon", "points": [[0, 0], [2, 0], [3, 1], [1, 1]], "fill": "#E6F4F3", "alpha": 0.55, "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0], "b": [2, 0], "label": "A(e1) = (2,0)", "dy": -0.35},
    {"kind": "arrow", "a": [0, 0], "b": [1, 1], "label": "A(e2) = (1,1)", "dx": 0.15, "color": "#B8860B"},
    {"kind": "point", "at": [3, 1], "label": "A(1,1) = (3,1)", "dx": -1.6, "dy": 0.2}
  ],
  "caption": "The determinant is 2*1 - 1*0 = 2. The parallelogram has base 2 and height 1, so its area is also 2: the determinant is the signed area scale."
}
:::

If the determinant is zero, the two columns are dependent and the parallelogram collapses to a segment or point. The matrix then cannot be inverted because distinct inputs can share an output.

<!-- pagebreak -->
## Determinant sign records orientation

Swapping coordinates is reflection in $y=x$. Areas stay the same but orientation reverses, so the determinant is $-1$. More generally, $|\det A|$ is the area or volume scale, while the sign tells whether orientation is preserved or reversed.

:::diagram
{
  "type": "geometry",
  "title": "Swapping coordinates reverses orientation",
  "xrange": [-0.5, 2.5], "yrange": [-0.5, 2.5], "grid": true,
  "elements": [
    {"kind": "line", "a": [-0.4, -0.4], "b": [2.3, 2.3], "label": "y = x", "label_pos": 0.55, "dx": 0.15, "color": "#5B6B84", "ls": "--"},
    {"kind": "polygon", "points": [[0, 0], [2, 0], [0, 1]], "fill": "#E6F4F3", "alpha": 0.45},
    {"kind": "polygon", "points": [[0, 0], [0, 2], [1, 0]], "fill": "#FFF3B0", "alpha": 0.35, "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0], "b": [2, 0], "label": "(2,0)", "dy": -0.4},
    {"kind": "arrow", "a": [0, 0], "b": [0, 2], "label": "(0,2)", "dx": 0.15, "color": "#B8860B"}
  ],
  "caption": "The matrix [[0,1],[1,0]] reflects in y = x. Areas stay the same but orientation reverses, so its determinant is -1."
}
:::

For a $3\times3$ matrix, the same interpretation uses signed volume. The identities $\det(AB)=\det A\det B$ and $\det(A^T)=\det A$ become plausible respectively as successive volume scaling and preservation of the parallelepiped's volume. The scalar rule for an $n\times n$ matrix is $\det(\lambda A)=\lambda^n\det A$.

<!-- pagebreak -->
## A two-variable system is an intersection problem

The system $x+y=3$ and $x-y=1$ represents two lines. Their intersection is $(2,1)$, so the unique solution is $x=2,y=1$. A parallel distinct second line would give no solution; the same line repeated would give infinitely many.

:::diagram
{
  "type": "graph",
  "title": "The solution is the common point of two lines",
  "xrange": [-1, 4], "yrange": [-2, 4],
  "curves": [{"expr": "3-x", "label": "x + y = 3", "labpos": 0.75}, {"expr": "x-1", "label": "x - y = 1", "labpos": 0.78, "color": "#B8860B"}],
  "points": [{"x": 2, "y": 1, "label": "unique solution (2,1)", "dx": 0.25, "dy": 0.55}],
  "caption": "The determinant of the coefficient matrix is 1*(-1) - 1*1 = -2, which is nonzero. This algebraic condition matches the geometric fact that the lines have one intersection."
}
:::

Cramer's rule and the inverse method require the appropriate nonzero determinant. Row operations can still solve singular systems, but the answer may be inconsistency or a family rather than a unique point.

<!-- pagebreak -->
## Matrix strategy: structure before arithmetic

:::diagram
{
  "type": "flow",
  "title": "A reusable matrix workflow",
  "steps": [
    {"title": "Check shapes and entry domains", "detail": "Confirm that multiplication is defined and identify whether the matrix is square, symmetric, orthogonal or singular."},
    {"title": "Choose geometry or algebra", "detail": "Use columns and determinant for transformations; use cofactors, row operations or block structure for computation."},
    {"title": "Apply the operation with its hypothesis", "detail": "Inverse and Cramer require nonzero determinant; eigenvalue shortcuts require the correct matrix type."},
    {"title": "Verify with a product or substituted point", "detail": "For an inverse check A A^-1 = I; for a system substitute the solution into every original equation."}
  ],
  "caption": "Matrix calculations become shorter when the structure is recognised first. Verification should use the original matrix or system, not an intermediate row-reduced form alone."
}
:::

:::example title="Verify an inverse instead of trusting one"
For $A=\begin{pmatrix}2&1\\0&1\end{pmatrix}$, $\det A=2$ and $A^{-1}=\begin{pmatrix}1/2&-1/2\\0&1\end{pmatrix}$. Multiplication in either order gives $I$. This check catches both cofactor transposition errors and a missing determinant factor.
:::
