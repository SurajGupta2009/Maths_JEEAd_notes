---
id: olympiad-02
part: olympiad
title: "Extension II — Barycentric Coordinates, Ceva and Routh"
---

## Barycentric coordinates are vector weights and area ratios

For a nondegenerate triangle $ABC$, normalized barycentric coordinates write
$$
P=\alpha A+\beta B+\gamma C,
\qquad \alpha+\beta+\gamma=1.
$$
For a point inside the triangle,
$$
\alpha=\frac{[PBC]}{[ABC]},\qquad
\beta=\frac{[PCA]}{[ABC]},\qquad
\gamma=\frac{[PAB]}{[ABC]}.
$$
Outside the triangle, use signed areas and signed weights. Unnormalized coordinates $(\lambda_1:\lambda_2:\lambda_3)$ become normalized after division by their nonzero sum.

:::example title="Coordinates from areas and back again"
For $A=(0,0)$, $B=(4,0)$, $C=(0,3)$ and $P=(1,1)$,
$$
P=\frac{5}{12}A+\frac{1}{4}B+\frac{1}{3}C.
$$
Thus the unnormalized coordinates are $(5:3:4)$. Also $[ABC]=6$ and $[PBC]=5/2$, so $[PBC]/[ABC]=5/12$, matching the coefficient of $A$. The three subtriangle area ratios are $5/12,1/4,1/3$, whose sum is $1$.
:::

## Ceva is a product of directed ratios

Put
$$
x=\frac{BX}{XC},\qquad y=\frac{CY}{YA},\qquad z=\frac{AZ}{ZB},
$$
where $X\in BC$, $Y\in CA$ and $Z\in AB$. The cevians $AX,BY,CZ$ are concurrent exactly when
$$
xyz=1,
$$
with directed ratios used for external points. In barycentrics, $X=(0:1:x)$, $Y=(y:0:1)$ and $Z=(1:z:0)$; eliminating the cevian equations gives the same product condition.

:::example title="A concurrent Ceva configuration"
If $BX:XC=2:1$, $CY:YA=3:1$ and $AZ:ZB=1:6$, then
$$
x=2,\qquad y=3,\qquad z=\frac{1}{6},
\qquad xyz=1.
$$
Therefore $AX,BY,CZ$ are concurrent. No coordinates of the intersection are required for the conclusion.
:::

## Routh measures the triangle bounded by three cevians

With the same ratio convention and $xyz\ne1$, the cevians bound a triangle $PQR$ satisfying
$$
\frac{[PQR]}{[ABC]}
=\frac{(xyz-1)^2}{(xy+x+1)(yz+y+1)(zx+z+1)}.
$$
When $xyz=1$, the cevians concur and the numerator correctly becomes zero.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 9,
  "title": "The three cevians bound the central triangle PQR",
  "xrange": [-0.7, 5.7], "yrange": [-0.7, 4.7], "grid": true,
  "elements": [
    {"kind": "polygon", "points": [[0, 0], [5, 0], [1, 4]], "fill": "#F4F8FC", "alpha": 0.25, "color": "#5B6B84"},
    {"kind": "segment", "a": [0, 0], "b": [2.3333, 2.6667], "color": "#0F766E"},
    {"kind": "segment", "a": [5, 0], "b": [0.6667, 2.6667], "color": "#B8860B"},
    {"kind": "segment", "a": [1, 4], "b": [3.75, 0], "color": "#B91C1C"},
    {"kind": "polygon", "points": [[1.75, 2], [2.8333, 1.3333], [2.1, 2.4]], "fill": "#FFF3B0", "alpha": 0.75, "color": "#16295C"},
    {"kind": "point", "at": [0, 0], "label": "A", "dx": -0.3, "dy": -0.4},
    {"kind": "point", "at": [5, 0], "label": "B", "dx": 0.15, "dy": -0.4},
    {"kind": "point", "at": [1, 4], "label": "C", "dx": -0.25, "dy": 0.15},
    {"kind": "point", "at": [1.75, 2], "label": "P", "dx": -0.35, "dy": -0.25, "size": 5},
    {"kind": "point", "at": [2.8333, 1.3333], "label": "Q", "dx": 0.15, "dy": -0.3, "size": 5},
    {"kind": "point", "at": [2.1, 2.4], "label": "R", "dx": -0.1, "dy": 0.2, "size": 5}
  ],
  "caption": "A=(0,0), B=(5,0), C=(1,4), x=2, y=1/2, z=3. Direct cevian intersections give P=(7/4,2), Q=(17/6,4/3), R=(21/10,12/5)."
}
:::

:::example title="An exact Routh calculation, checked by intersections"
For $x=2$, $y=1/2$ and $z=3$, we have $xyz=3$ and
$$
xy+x+1=4,\qquad yz+y+1=3,\qquad zx+z+1=10.
$$
Therefore
$$
\frac{[PQR]}{[ABC]}=\frac{(3-1)^2}{4\cdot3\cdot10}
=\frac{1}{30}.
$$
The displayed coordinates independently give the same ratio. Since $[ABC]=10$, the central triangle has area $1/3$. Keep the cyclic factors in order: here $yz+y+1=3/2+1/2+1=3$, not $2$; using $2$ would give the incorrect result $1/20$.
:::
