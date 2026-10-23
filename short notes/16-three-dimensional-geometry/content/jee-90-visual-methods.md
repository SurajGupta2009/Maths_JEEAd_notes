---
id: jee-90-visual-methods
part: jee
title: "Visual 3D Geometry Lab"
---

## A displacement becomes a direction after normalization

For $A=(1,2,3)$ and $B=(4,6,9)$, the edge vector is $\mathbf{d}=(3,4,6)$ and $|\mathbf{d}|=\sqrt{61}$. Its direction cosines are therefore $(3,4,6)/\sqrt{61}$.

:::diagram
{
  "type": "vector3d",
  "title": "The component path and the direct displacement have the same endpoints",
  "xrange": [0, 5], "yrange": [0, 7], "zrange": [0, 10],
  "elev": 22, "azim": -57,
  "elements": [
    {"kind": "arrow", "a": [1, 2, 3], "b": [4, 6, 9], "label": "d = (3,4,6)", "label_at": [2.5, 4, 6], "offset": [0.5, 0, 0.4], "color": "#0F766E"},
    {"kind": "segment", "a": [1, 2, 3], "b": [4, 2, 3], "label": "3", "label_at": [2.5, 2, 3], "offset": [0, -0.3, 0], "color": "#5B6B84"},
    {"kind": "segment", "a": [4, 2, 3], "b": [4, 6, 3], "label": "4", "label_at": [4, 4, 3], "offset": [0.25, 0, 0], "color": "#B8860B"},
    {"kind": "segment", "a": [4, 6, 3], "b": [4, 6, 9], "label": "6", "label_at": [4, 6, 6], "offset": [0.3, 0, 0], "color": "#B91C1C"},
    {"kind": "point", "at": [1, 2, 3], "label": "A", "offset": [-0.3, 0, -0.25]},
    {"kind": "point", "at": [4, 6, 9], "label": "B", "offset": [0.3, 0, 0.2]}
  ],
  "caption": "The three component steps have squared lengths 9,16,36. The direct displacement has squared length 61 and unit direction (3,4,6)/sqrt(61)."
}
:::

**Visual check:** $(3^2+4^2+6^2)/61=1$, so the normalized components are genuine direction cosines.

:::key title="Second read: projection is another normalized dot product"
Using the same displacement and the direction $\mathbf{b}=(2,-1,2)$, whose length is $3$, the signed projection is $(6-4+12)/3=14/3$. The raw dot product is $14$; division by the direction length turns it into a length.
:::

<!-- pagebreak -->
## Two planes reveal their intersection direction

For $x+y+z=1$ and $2x-3y+4z=5$, the normals are $\mathbf{n}_1=(1,1,1)$ and $\mathbf{n}_2=(2,-3,4)$. Their cross product is $\mathbf{d}=(7,-2,-5)$, and $P=(8/5,-3/5,0)$ lies on both planes.

:::diagram
{
  "type": "vector3d",
  "title": "The intersection line is perpendicular to both plane normals",
  "xrange": [-2, 4], "yrange": [-3, 3], "zrange": [-3, 3],
  "elev": 28, "azim": -45, "zoom": 1.25,
  "elements": [
    {"kind": "plane", "centre": [1.6, -0.6, 0], "u": [1.2, -1.2, 0], "v": [0.9, 0, -0.9], "fill": "#DCEFED", "alpha": 0.16, "color": "#0F766E", "label": "P1", "label_at": [-0.5, 0.6, 0.9], "offset": [-0.2, 0, 0.2]},
    {"kind": "plane", "centre": [1.6, -0.6, 0], "u": [1.2, 0, -0.6], "v": [0, 1.2, 0.9], "fill": "#FFF3B0", "alpha": 0.14, "color": "#B8860B", "label": "P2", "label_at": [2.8, 0.6, 0.3], "offset": [0.2, 0, 0.2]},
    {"kind": "segment", "a": [-0.15, -0.1, 1.25], "b": [3.35, -1.1, -1.25], "label": "d", "label_at": [2.6, -0.9, -0.6], "offset": [0.3, 0, -0.2], "color": "#B91C1C", "lw": 3},
    {"kind": "point", "at": [1.6, -0.6, 0], "label": "P", "offset": [-0.6, 0, 0.4], "color": "#B91C1C"}
  ],
  "caption": "The line is P+t(7,-2,-5). Every direction along it has zero dot product with both normals, so it stays in both planes."
}
:::

**Visual check:** $(7,-2,-5)\cdot(1,1,1)=0$ and $(7,-2,-5)\cdot(2,-3,4)=14+6-20=0$.

:::key title="Second read: verify the whole parametrization"
At $P+t\mathbf{d}$, both plane residuals equal their values at $P$ plus $t$ times a zero directional dot product. Thus one verified point and two verified perpendicularities prove that the entire parametrized line is the intersection.
:::

<!-- pagebreak -->
## A perpendicular foot creates a reflection

Let $L:(0,0,1)+t(1,0,0)$ and $P=(1,2,3)$. Projection gives $F=(1,0,1)$ and reflection gives $I=2F-P=(1,-2,-1)$.

:::diagram
{
  "type": "vector3d",
  "title": "F is the midpoint of P and its image I",
  "xrange": [-2, 3], "yrange": [-3, 3], "zrange": [-2, 4],
  "elev": 22, "azim": -55,
  "elements": [
    {"kind": "segment", "a": [-2, 0, 1], "b": [3, 0, 1], "label": "L", "label_at": [2.4, 0, 1], "offset": [0, 0, 0.3], "color": "#5B6B84"},
    {"kind": "segment", "a": [1, 2, 3], "b": [1, 0, 1], "ls": "--", "color": "#B91C1C"},
    {"kind": "segment", "a": [1, 0, 1], "b": [1, -2, -1], "ls": "--", "color": "#B8860B"},
    {"kind": "point", "at": [1, 2, 3], "label": "P(1,2,3)", "offset": [0.65, 0, 0.2]},
    {"kind": "point", "at": [1, 0, 1], "label": "F(1,0,1)", "offset": [-0.75, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [1, -2, -1], "label": "I(1,-2,-1)", "offset": [0.7, 0, -0.2]}
  ],
  "caption": "PF=(0,-2,-2) is perpendicular to the x-direction. The same displacement continued past F reaches I, so PF=FI=2 sqrt(2)."
}
:::

**Visual check:** $P+I=(2,0,2)=2F$, and $(P-F)\cdot(1,0,0)=0$.

:::key title="Second read: cross-product height finds the distance without F"
With $A=(0,0,1)$ and $\mathbf{b}=(1,0,0)$, $(P-A)\times\mathbf{b}=(0,2,-2)$. Dividing its length $2\sqrt{2}$ by $|\mathbf{b}|=1$ gives the same distance $2\sqrt{2}$.
:::

<!-- pagebreak -->
## Skew distance is the gap along a common normal

For $L_1:\mathbf{r}=t(1,0,0)$ and $L_2:\mathbf{r}=(0,1,0)+s(0,0,1)$, the directions cross to $(0,-1,0)$. The connector from $F_1=(0,0,0)$ to $F_2=(0,1,0)$ is perpendicular to both lines.

:::diagram
{
  "type": "vector3d",
  "title": "The shortest connector is perpendicular to both skew lines",
  "xrange": [-2, 3], "yrange": [-1, 2.5], "zrange": [-2, 3],
  "elev": 23, "azim": -55,
  "elements": [
    {"kind": "segment", "a": [-2, 0, 0], "b": [3, 0, 0], "label": "L1", "label_at": [2.3, 0, 0], "offset": [0, 0, 0.3], "color": "#0F766E"},
    {"kind": "segment", "a": [0, 1, -2], "b": [0, 1, 3], "label": "L2", "label_at": [0, 1, 2.3], "offset": [0.4, 0, 0], "color": "#B8860B"},
    {"kind": "segment", "a": [0, 0, 0], "b": [0, 1, 0], "color": "#B91C1C", "lw": 3},
    {"kind": "point", "at": [0, 0, 0], "label": "F1", "offset": [-0.35, 0, -0.25], "color": "#B91C1C"},
    {"kind": "point", "at": [0, 1, 0], "label": "F2", "offset": [0.35, 0, 0.2], "color": "#B91C1C"}
  ],
  "caption": "The red connector has length 1. It is antiparallel to b1 × b2=(0,-1,0), and its dot product with each line direction is zero."
}
:::

**Visual check:** the signed triple product is $(0,1,0)\cdot(0,-1,0)=-1$, and $d=|-1|/|(0,-1,0)|=1$.

:::key title="Second read: volume divided by base area"
The connector and the two unit directions form a unit parallelepiped of volume $1$. The base spanned by the line directions has area $1$, so its height is $1$. A zero volume would instead put the two lines in one plane.
:::

<!-- pagebreak -->
## A plane reflection follows its normal

For the plane $x+y+z=0$ and $P=(1,1,1)$, the foot is $F=(0,0,0)$ and the image is $I=(-1,-1,-1)$. The displacement $P-F=(1,1,1)$ is the plane's normal direction.

:::diagram
{
  "type": "vector3d",
  "title": "P and I are symmetric about the plane through F",
  "xrange": [-3, 3], "yrange": [-3, 3], "zrange": [-3, 3],
  "elev": 23, "azim": -55,
  "elements": [
    {"kind": "plane", "centre": [0, 0, 0], "u": [1.5, -1.5, 0], "v": [1.1, 0, -1.1], "fill": "#DCEFED", "alpha": 0.20, "color": "#5B6B84", "label": "x+y+z=0", "offset": [-1, 1, 0]},
    {"kind": "segment", "a": [1, 1, 1], "b": [0, 0, 0], "ls": "--", "color": "#B91C1C"},
    {"kind": "segment", "a": [0, 0, 0], "b": [-1, -1, -1], "ls": "--", "color": "#B8860B"},
    {"kind": "point", "at": [1, 1, 1], "label": "P", "offset": [0.3, 0, 0.2]},
    {"kind": "point", "at": [0, 0, 0], "label": "F", "offset": [-0.3, 0, 0.2], "color": "#B91C1C"},
    {"kind": "point", "at": [-1, -1, -1], "label": "I", "offset": [-0.3, 0, -0.2]}
  ],
  "caption": "The residual is 3 and the normal squared length is 3, so F=P-(1,1,1)=0 and I=P-2(1,1,1)=(-1,-1,-1)."
}
:::

**Visual check:** $P+I=2F$ and the point-plane distance is $|3|/\sqrt{3}=\sqrt{3}=|P-F|$.

:::key title="Second read: a parallel-plane distance uses the same normal"
The plane $x+y+z=3$ contains $P$ and is parallel to the original plane. Their separation is $|3-0|/\sqrt{3}=\sqrt{3}$. The foot $F$ is therefore the nearest point of the original plane to the entire parallel plane through $P$.
:::

<!-- pagebreak -->
## Let the geometry choose the formula

:::diagram
{
  "type": "flow",
  "title": "A visual decision sequence for 3D problems",
  "steps": [
    {"title": "Points or displacement?", "detail": "Use coordinates and head minus tail. Normalize only after a nonzero direction is known."},
    {"title": "One line or two planes?", "detail": "A line needs a point and direction. Two independent plane normals cross to give their intersection direction."},
    {"title": "Nearest point or separation?", "detail": "Projection gives a foot; a cross or triple product gives distance as area/base or volume/base-area."},
    {"title": "Reflection or family?", "detail": "Double the foot displacement for an image. Use pencils and normalized equal-distance equations for plane families."}
  ],
  "caption": "The picture identifies the object and the shortest reliable computation. Exact substitution then certifies the result."
}
:::

:::diagram
{
  "type": "table",
  "title": "Match each 3D question to its controlling quantity",
  "columns": ["Question", "Computation", "Essential check"],
  "rows": [
    ["Line direction", "B-A or n1×n2", "nonzero; perpendicular to normals"],
    ["Two lines coplanar?", "(a2-a1)·(b1×b2)", "zero test after parallel test"],
    ["Line and plane angle", "|b·n|/(|b||n|)=sin(theta)", "complement of line-normal angle"],
    ["Point and plane distance", "|p·n-d|/|n|", "absolute normalized residual"],
    ["Skew-line distance", "|triple|/|b1×b2|", "common perpendicular direction"]
  ],
  "col_widths": [0.29, 0.38, 0.33],
  "caption": "Every formula has a hypothesis. Parallel directions make b1×b2 zero, so that case needs the point-to-line distance method instead."
}
:::
