---
id: jee-09
part: jee
title: "Pencils, Bisector Planes and Mixed Strategy"
---

## A pencil keeps the common line automatically

Suppose $P_1=0$ and $P_2=0$ are independent plane equations. Every plane of the form
$$
P_1+\lambda P_2=0
$$
contains their line of intersection, because both residuals vanish there. This one-parameter form covers every plane through that line **except $P_2=0$ itself**. To include every member at once, use the homogeneous pencil
$$
\alpha P_1+\beta P_2=0,\qquad (\alpha,\beta)\ne(0,0).
$$
Impose one additional point or normal condition to find the required member.

:::example title="A plane through an intersection line and the origin"
For
$$
P_1=x+y+z-1,\qquad P_2=2x-3y+4z-5,
$$
use $P_1+\lambda P_2=0$. At the origin, $-1-5\lambda=0$, so $\lambda=-1/5$. Multiplying by $5$ gives
$$
3x+8y+z=0.
$$
This contains the origin and every point satisfying both original plane equations.
:::

:::example title="A second point determines a second pencil member"
Through the intersection of $x+2y+3z=4$ and $2x+y-z=5$, and through $(1,1,1)$, substitution into the pencil gives $\lambda=2/3$. Clearing denominators,
$$
7x+8y+7z=22.
$$
The required point and the common line satisfy this equation.
:::

## Bisector planes are equal-distance loci

For planes $P_1=0$ and $P_2=0$ with normals $\mathbf{n}_1,\mathbf{n}_2$, equal distances to the two planes require
$$
\frac{|P_1|}{|\mathbf{n}_1|}=\frac{|P_2|}{|\mathbf{n}_2|}.
$$
Removing absolute values gives the two bisector planes:
$$
\frac{P_1}{|\mathbf{n}_1|}=\pm\frac{P_2}{|\mathbf{n}_2|}.
$$
The two signs select the two angle bisectors; normalization is essential when the normal lengths differ.

:::example title="Two perpendicular bisector planes"
For $x+y+z=0$ and $x-y+z=0$, both normal lengths are $\sqrt{3}$. Hence
$$
x+y+z=\pm(x-y+z).
$$
The two planes are
$$
y=0\qquad\text{and}\qquad x+z=0.
$$
Their normals $(0,1,0)$ and $(1,0,1)$ have dot product zero, so the bisector planes are perpendicular.
:::

:::diagram
{
  "type": "flow",
  "title": "Choose the smallest sufficient 3D computation",
  "steps": [
    {"title": "Line from points or planes?", "detail": "Use head minus tail for a direction, or cross two plane normals. Find one point and verify every original equation."},
    {"title": "Classify two lines", "detail": "Parallel directions need a coincidence test. Nonparallel lines need the coplanarity triple product before intersection or skew distance."},
    {"title": "Angle or distance?", "detail": "Line-plane angle uses sine. Point-plane distance uses an absolute normalized residual; skew distance uses volume divided by base area."},
    {"title": "Foot, image or family?", "detail": "Project to get a foot and double for an image. Use a pencil for a common line and normalized residuals for bisector planes."}
  ],
  "caption": "Name the geometric object first. Then select a formula whose hypotheses match it and finish with direct substitution or perpendicularity."
}
:::

:::warn title="Do not normalize only part of a formula"
Direction ratios must be normalized for direction cosines, plane residuals for equal-distance loci, and parallel-plane equations before subtracting constants. Keep exact coefficients until the correct normalization is clear.
:::

:::key title="Final 3D self-check"
Does the point satisfy every required equation? Is every direction or normal nonzero? Does the line direction dot each relevant normal to zero? Are the common-perpendicular connector and the two line directions mutually perpendicular? Does the requested angle use cosine or sine appropriately? These checks are faster than repeating the same algebra.
:::
