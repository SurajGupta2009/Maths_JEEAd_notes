---
id: jee-03
part: jee
title: "Points, Section Formula and Centroids"
---

## Section formula is a weighted average

Let $P$ divide $AB$ internally in the ratio $AP:PB=m:n$. Because $P$ is $m/(m+n)$ of the way from $A$ to $B$,
$$
\mathbf{p}=\mathbf{a}+\frac{m}{m+n}(\mathbf{b}-\mathbf{a})
=\frac{n\mathbf{a}+m\mathbf{b}}{m+n}.
$$
The weights are **opposite** the segments: the weight on $A$ is $n$, and the weight on $B$ is $m$. The midpoint is the $m=n$ case.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "ratio": 0.55,
  "title": "AP:PB = 2:1 means P is two-thirds of the way",
  "xrange": [-1, 7], "yrange": [-1, 4.5], "grid": true,
  "elements": [
    {"kind": "segment", "a": [0, 0], "b": [6, 3], "color": "#5B6B84"},
    {"kind": "point", "at": [0, 0], "label": "A", "dx": -0.4, "dy": -0.4},
    {"kind": "point", "at": [6, 3], "label": "B", "dx": 0.2, "dy": 0.15},
    {"kind": "point", "at": [4, 2], "label": "P = (A+2B)/3", "dx": -1.6, "dy": 0.45, "color": "#B91C1C"},
    {"kind": "segment", "a": [0, 0], "b": [4, 2], "label": "2 parts", "label_pos": 0.45, "dx": -0.2, "dy": -0.55, "color": "#0F766E"},
    {"kind": "segment", "a": [4, 2], "b": [6, 3], "label": "1 part", "label_pos": 0.5, "dx": 0.15, "dy": 0.2, "color": "#B8860B"}
  ],
  "caption": "For AP:PB=2:1, P=(A+2B)/3. The coefficient of B is the AP numerator, not the PB numerator."
}
:::

:::example title="An internal division in 3D"
Divide the join of $A=(1,0,0)$ and $B=(4,5,6)$ in the ratio $2:3$. Then
$$
\mathbf{p}=\frac{3(1,0,0)+2(4,5,6)}{5}
=\left(\frac{11}{5},2,\frac{12}{5}\right).
$$
As a check, $\mathbf{p}-\mathbf{a}=(6/5,2,12/5)$ and $\mathbf{b}-\mathbf{p}=(9/5,3,18/5)$, whose component ratio is $2:3$.
:::

## External division needs a signed denominator

If $P$ lies beyond $B$ and $AP:PB=m:n$ with $m>n$, then
$$
\mathbf{p}=\frac{m\mathbf{b}-n\mathbf{a}}{m-n}.
$$
For $m<n$, the external point lies beyond $A$. Rather than memorizing two pictures, use directed ratios or derive from $\mathbf{p}=\mathbf{a}+t(\mathbf{b}-\mathbf{a})$ and locate $t$.

:::example title="Check an external point with displacements"
For $A=(1,-1,2)$ and $B=(3,3,-2)$, external division in the ratio $2:1$ beyond $B$ gives
$$
P=2B-A=(5,7,-6).
$$
Indeed $\overrightarrow{AP}=(4,8,-8)$ and $\overrightarrow{PB}=(-2,-4,4)$ have lengths in the ratio $2:1$, with $B$ between $A$ and $P$.
:::

## Centroids are equal-weight section formulas

For a triangle,
$$
\mathbf{g}=\frac{\mathbf{a}+\mathbf{b}+\mathbf{c}}{3}.
$$
For a tetrahedron with a fourth vertex $\mathbf{d}$, the centroid is $(\mathbf{a}+\mathbf{b}+\mathbf{c}+\mathbf{d})/4$. These are averages of position vectors, not averages of side lengths. To see the median concurrency, put $A$ at the origin and let $D=(\mathbf{b}+\mathbf{c})/2$ be the midpoint of $BC$. Then $(2/3)D=(\mathbf{a}+\mathbf{b}+\mathbf{c})/3$ lies two-thirds along the median; symmetry gives the same point on all three medians.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "ratio": 0.55,
  "title": "The centroid lies two-thirds along every median",
  "xrange": [-1, 7], "yrange": [-1, 5], "grid": true,
  "elements": [
    {"kind": "polygon", "points": [[0, 0], [6, 0], [2, 4]], "fill": "#DCEFED", "alpha": 0.35, "color": "#0F766E"},
    {"kind": "segment", "a": [0, 0], "b": [4, 2], "color": "#5B6B84", "ls": "--"},
    {"kind": "segment", "a": [6, 0], "b": [1, 2], "color": "#5B6B84", "ls": "--"},
    {"kind": "segment", "a": [2, 4], "b": [3, 0], "color": "#5B6B84", "ls": "--"},
    {"kind": "point", "at": [0, 0], "label": "A", "dx": -0.4, "dy": -0.4},
    {"kind": "point", "at": [6, 0], "label": "B", "dx": 0.2, "dy": -0.4},
    {"kind": "point", "at": [2, 4], "label": "C", "dx": 0.15, "dy": 0.15},
    {"kind": "point", "at": [2.6667, 1.3333], "label": "G", "dx": 0.25, "dy": 0.2, "color": "#B91C1C"}
  ],
  "caption": "For A=(0,0), B=(6,0), C=(2,4), G=(8/3,4/3). On the median from A to (4,2), AG:GD=2:1."
}
:::
