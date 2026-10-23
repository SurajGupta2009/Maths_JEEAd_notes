---
id: jee-90-visual-methods
part: jee
title: "Visual Vector Lab"
---

## Translate the origin to expose symmetry

For a parallelogram with vertices $0,\mathbf{a},\mathbf{a}+\mathbf{b},\mathbf{b}$, both diagonals have midpoint $(\mathbf{a}+\mathbf{b})/2$. Placing one vertex at the origin turns a synthetic bisection statement into one average.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Both diagonals have the same midpoint",
  "xrange": [-1, 6], "yrange": [-1, 4.5], "grid": true,
  "elements": [
    {"kind": "polygon", "points": [[0, 0], [4, 0], [5, 3], [1, 3]], "fill": "#DCEFED", "alpha": 0.35, "color": "#0F766E"},
    {"kind": "segment", "a": [0, 0], "b": [5, 3], "color": "#B91C1C"},
    {"kind": "segment", "a": [4, 0], "b": [1, 3], "color": "#B8860B"},
    {"kind": "point", "at": [0, 0], "label": "O", "dx": -0.35, "dy": -0.4},
    {"kind": "point", "at": [4, 0], "label": "a", "dx": 0.15, "dy": -0.45},
    {"kind": "point", "at": [1, 3], "label": "b", "dx": -0.55, "dy": 0.2},
    {"kind": "point", "at": [5, 3], "label": "a+b", "dx": 0.15, "dy": 0.15},
    {"kind": "point", "at": [2.5, 1.5], "label": "M=(a+b)/2", "dx": 0.25, "dy": 0.25, "color": "#B91C1C"}
  ],
  "caption": "For a=(4,0), b=(1,3), M=(5/2,3/2). It is the midpoint of both 0 to a+b and a to b."
}
:::

**Visual check:** $\overrightarrow{OM}=(5/2,3/2)$, while the other diagonal has endpoints $(4,0)$ and $(1,3)$, whose average is identical. No length formula is needed.

:::key title="Second read: the two diagonals also obey the parallelogram law"
Here $\mathbf{a}+\mathbf{b}=(5,3)$ and $\mathbf{a}-\mathbf{b}=(3,-3)$, so the squared diagonal lengths are $34$ and $18$. Their sum is $52=2(16+10)$, exactly twice the sum of the squared side lengths.
:::

<!-- pagebreak -->
## Projection and rejection make a right triangle

For $\mathbf{a}=(4,2)$ and $\mathbf{b}=(1,2)$, we have $\mathbf{a}\cdot\mathbf{b}=8$ and $|\mathbf{b}|^2=5$. Therefore
$$
\operatorname{proj}_{\mathbf{b}}\mathbf{a}=\frac{8}{5}(1,2),
\qquad
\mathbf{a}_{\perp}=\left(\frac{12}{5},-\frac{6}{5}\right).
$$

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "The rejection is perpendicular to the projection",
  "xrange": [-1, 5], "yrange": [-2, 3.5], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [4, 2], "label": "a=(4,2)", "dx": -0.2, "dy": 0.3, "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0], "b": [1.6, 3.2], "label": "projection 8b/5", "dx": -1.8, "dy": 0, "color": "#B8860B"},
    {"kind": "arrow", "a": [1.6, 3.2], "b": [4, 2], "label": "rejection", "dx": 0.15, "dy": 0.1, "color": "#B91C1C"},
    {"kind": "arrow", "a": [0, 0], "b": [2, 4], "label": "2b", "dx": 0.15, "dy": -0.3, "color": "#5B6B84", "lw": 1.4},
    {"kind": "point", "at": [1.6, 3.2], "label": "(8/5,16/5)", "dx": -1.65, "dy": 0.25}
  ],
  "caption": "Projection plus rejection is (8/5+12/5,16/5-6/5)=(4,2). The rejection dots (1,2) to zero."
}
:::

**Visual check:** $(12/5,-6/5)\cdot(1,2)=12/5-12/5=0$, and the scalar projection is $8/\sqrt{5}$.

:::key title="Second read: Pythagoras checks the decomposition"
The squared projection length is $(64/25)|(1,2)|^2=64/5$, and the squared rejection length is $(144+36)/25=36/5$. They sum to $100/5=20=|(4,2)|^2$, while the rejection's length is $6/\sqrt{5}$.
:::

<!-- pagebreak -->
## One parallelogram checks dot, cross and angle

Take $\mathbf{a}=(3,1)$ and $\mathbf{b}=(1,2)$. Then $\mathbf{a}\cdot\mathbf{b}=5$ and the $z$-component of $\mathbf{a}\times\mathbf{b}$ is $3\cdot2-1\cdot1=5$.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Area 5 and angle 45 degrees in one construction",
  "xrange": [-1, 5], "yrange": [-1, 4], "grid": true,
  "elements": [
    {"kind": "polygon", "points": [[0, 0], [3, 1], [4, 3], [1, 2]], "fill": "#DCEFED", "alpha": 0.4, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0], "b": [3, 1], "label": "a", "dx": 0, "dy": -0.45, "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0], "b": [1, 2], "label": "b", "dx": -0.55, "dy": 0.1, "color": "#B8860B"},
    {"kind": "arrow", "a": [3, 1], "b": [4, 3], "color": "#B8860B"},
    {"kind": "arrow", "a": [1, 2], "b": [4, 3], "color": "#0F766E"},
    {"kind": "text", "at": [1.3, 1.1], "text": "area = 5", "color": "#B91C1C"},
    {"kind": "text", "at": [0.1, 3.4], "text": "25 + 25 = 10·5", "color": "#16295C"}
  ],
  "caption": "Cross magnitude squared 25 plus dot squared 25 equals |a|^2|b|^2=50. Also cos(theta)=1/sqrt(2)."
}
:::

**Visual check:** the parallelogram area is $5$, the triangle on the same edges is $5/2$, and Lagrange's identity reads $25+25=50$.

:::key title="Second read: the diagonals span twice the area"
The diagonals are $\mathbf{a}+\mathbf{b}=(4,3)$ and $\mathbf{a}-\mathbf{b}=(2,-1)$. Their planar cross determinant is $4(-1)-3(2)=-10$, whose absolute value is twice the original area $5$, as the diagonal identity predicts.
:::

<!-- pagebreak -->
## A triple product splits into base and height

For $\mathbf{u}=(1,1,0)$, $\mathbf{v}=(1,0,1)$ and $\mathbf{w}=(0,1,1)$,
$$
\mathbf{v}\times\mathbf{w}=(-1,-1,1),
\qquad [\mathbf{u}\ \mathbf{v}\ \mathbf{w}]=-2.
$$

:::diagram
{
  "type": "vector3d",
  "label_fontsize": 10,
  "title": "Signed triple product -2 means volume 2",
  "xrange": [-0.5, 2.8], "yrange": [-0.5, 2.8], "zrange": [-0.5, 2.5],
  "elev": 23, "azim": -54,
  "elements": [
    {"kind": "parallelepiped", "origin": [0, 0, 0], "u": [1, 1, 0], "v": [1, 0, 1], "w": [0, 1, 1], "fill": "#DCEFED", "alpha": 0.15, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 1, 0], "label": "u", "label_at": [0.5, 0.5, 0], "offset": [0, 0.25, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 0, 1], "label": "v", "label_at": [0.5, 0, 0.5], "offset": [0.25, -0.2, 0], "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [0, 1, 1], "label": "w", "label_at": [0, 0.5, 0.5], "offset": [-0.35, 0.15, 0], "color": "#B91C1C"}
  ],
  "caption": "The base spanned by v,w has area sqrt(3), so the height is 2/sqrt(3). The corresponding tetrahedron has volume 1/3."
}
:::

**Visual check:** $|[\mathbf{u}\ \mathbf{v}\ \mathbf{w}]|=2$; swapping any two edges changes the sign but not the volume.

:::key title="Second read: the tetrahedron uses the same three edges"
The tetrahedron with vertices $\mathbf{0},\mathbf{u},\mathbf{v},\mathbf{w}$ has volume $2/6=1/3$. Its centroid is $(\mathbf{u}+\mathbf{v}+\mathbf{w})/4=(1/2,1/2,1/2)$, so volume and centroid need no new edge computation.
:::

<!-- pagebreak -->
## Zero volume is visible dependence

Keep the base edges $\mathbf{u}=(1,0,0)$ and $\mathbf{v}=(0,1,0)$ fixed. For $D=(1,1,0)$, the edge $\mathbf{w}=(1,1,0)$ lies in the base plane. For $D'=(1,1,1)$, the edge $\mathbf{w}'=(1,1,1)$ lifts out of it.

:::diagram
{
  "type": "vector3d",
  "label_fontsize": 10,
  "title": "Coplanar edges collapse the volume to zero",
  "xrange": [-0.5, 1.8], "yrange": [-0.5, 1.8], "zrange": [-0.5, 1.8],
  "elev": 24, "azim": -55,
  "elements": [
    {"kind": "polygon", "points": [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]], "fill": "#DCEFED", "alpha": 0.35, "color": "#5B6B84"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 0, 0], "label": "u", "label_at": [0.5, 0, 0], "offset": [0, -0.25, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [0, 1, 0], "label": "v", "label_at": [0, 0.5, 0], "offset": [-0.25, 0, 0], "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 1, 0], "label": "w: triple = 0", "label_at": [0.5, 0.5, 0], "offset": [0.5, 0.2, 0], "color": "#0F766E"},
    {"kind": "arrow", "a": [0, 0, 0], "b": [1, 1, 1], "label": "w': triple = 1", "label_at": [0.5, 0.5, 0.5], "offset": [-0.75, 0, 0.2], "color": "#B91C1C"}
  ],
  "caption": "With u=i and v=j, the triple product is the z-component of w. It is 0 for w=(1,1,0) and 1 for w'=(1,1,1)."
}
:::

**Visual check:** the zero case does not imply that every edge is zero; it implies that the three edges fail to span a three-dimensional volume.

:::key title="Second read: height is the remaining coordinate"
For a general third edge $\mathbf{w}=(s,t,h)$ with $\mathbf{u}=\mathbf{i}$ and $\mathbf{v}=\mathbf{j}$, the triple product is simply $h$. Every $h=0$ point lies in the base plane; for $h\ne0$, the parallelepiped volume is $|h|$ because the base is a unit square.
:::

<!-- pagebreak -->
## Let the picture choose the product

:::diagram
{
  "type": "flow",
  "title": "Read the geometry before doing component arithmetic",
  "steps": [
    {"title": "A sum, section or centroid?", "detail": "Use displacement and linear combination. Place a convenient vertex at the origin."},
    {"title": "An angle, projection or perpendicular?", "detail": "Use a dot product and check that direction vectors are nonzero."},
    {"title": "A normal, parallel test or area?", "detail": "Use a cross product in the requested order, then verify both perpendicularities."},
    {"title": "A volume or coplanarity test?", "detail": "Use three edges from one point in a scalar triple product; take absolute value and 1/6 only when required."}
  ],
  "caption": "A sketch identifies the right operation and supplies an independent geometric estimate; exact components supply the proof."
}
:::

:::diagram
{
  "type": "table",
  "title": "The three products answer different questions",
  "columns": ["Operation", "Output", "Zero condition", "Geometric meaning"],
  "rows": [
    ["a·b", "scalar", "perpendicular nonzero vectors", "angle and projection"],
    ["a×b", "vector", "parallel or zero input", "normal and area"],
    ["a·(b×c)", "scalar", "dependent/coplanar edges", "signed volume"]
  ],
  "col_widths": [0.18, 0.14, 0.34, 0.34],
  "caption": "Do not interchange the zero tests: dot zero is perpendicularity, whereas cross zero is parallelism or a zero vector."
}
:::

:::key title="The final visual habit"
After computing, return to the sketch. Is every displacement head minus tail? Are direction vectors nonzero? Does the projection point the right way and the normal lie on the expected side? Is area positive, and did a tetrahedron include $1/6$? These visual and structural checks catch errors that repeated algebra in the same mistaken setup cannot.
:::
