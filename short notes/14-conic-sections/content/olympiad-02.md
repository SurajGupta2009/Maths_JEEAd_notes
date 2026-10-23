---
id: olympiad-02
part: olympiad
title: "Extension II — Rectangular Hyperbola and Triangle Geometry"
---

## Four concyclic-style incidences on $xy=c^2$

Take three noncollinear points on a rectangular hyperbola, with distinct nonzero parameters:
$$
A=\left(ct_1,\frac{c}{t_1}\right),\quad
B=\left(ct_2,\frac{c}{t_2}\right),\quad
C=\left(ct_3,\frac{c}{t_3}\right).
$$
The slope of $AB$ is $-1/(t_1t_2)$, so an altitude perpendicular to it has slope $t_1t_2$. Imposing the two altitude conditions gives the orthocentre
$$
H=\left(-\frac{c}{t_1t_2t_3},-ct_1t_2t_3\right).
$$
This point also lies on $xy=c^2$, because its coordinates have product $c^2$. Thus, for a nondegenerate triangle inscribed in a rectangular hyperbola, **the orthocentre lies on the same hyperbola**.

:::derive title="Why the formula works"
The altitude through $A$ is perpendicular to $BC$, whose slope is $-1/(t_2t_3)$; its slope is therefore $t_2t_3$. The line through $H$ and $A$ has exactly that slope after the parameter formula is substituted. Cyclic permutation verifies the other two altitudes, so all three concur at $H$.
:::

:::example title="A small exact configuration"
On $xy=1$, take parameters $1,2,-1$:
$$
A=(1,1),\qquad B=\left(2,\frac{1}{2}\right),\qquad C=(-1,-1).
$$
Their product is $-2$, so the formula gives $H=(1/2,2)$. Indeed $BC$ has slope $1/2$, and $AH$ has slope $-2$; $AC$ has slope $1$, and $BH$ has slope $-1$. All four points lie on $xy=1$.
:::

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "A, B, C and their orthocentre H all lie on xy = 1",
  "xrange": [-3, 3.5], "yrange": [-3, 3.5],
  "elements": [
    {"kind": "rectangular", "c": 1, "trange": [0.3, 3.4], "color": "#0F766E"},
    {"kind": "segment", "a": [1, 1], "b": [2, 0.5], "color": "#16295C"},
    {"kind": "segment", "a": [2, 0.5], "b": [-1, -1], "color": "#16295C"},
    {"kind": "segment", "a": [-1, -1], "b": [1, 1], "color": "#16295C"},
    {"kind": "segment", "a": [1, 1], "b": [0.5, 2], "ls": "--", "color": "#B8860B"},
    {"kind": "segment", "a": [2, 0.5], "b": [0.5, 2], "ls": "--", "color": "#B8860B"},
    {"kind": "segment", "a": [-1, -1], "b": [0.5, 2], "ls": "--", "color": "#B8860B"},
    {"kind": "point", "at": [1, 1], "label": "A", "dx": 0.15},
    {"kind": "point", "at": [2, 0.5], "label": "B", "dx": 0.15},
    {"kind": "point", "at": [-1, -1], "label": "C", "dx": -0.35, "dy": -0.35},
    {"kind": "point", "at": [0.5, 2], "label": "H(1/2,2)", "dx": 0.15, "color": "#B91C1C"}
  ],
  "caption": "The dashed segments lie along the three altitudes. The slope checks AH perpendicular BC and BH perpendicular AC are exact; the third altitude follows by concurrence."
}
:::

## Connect the configuration to the Euler line

For any triangle with circumcentre $O$, orthocentre $H$, and nine-point centre $N$,
$$
N=\frac{O+H}{2},\qquad R_{\text{nine-point}}=\frac{R_{\text{circum}}}{2}.
$$
These are general triangle facts, not special hypotheses about the hyperbola. The rectangular-hyperbola theorem adds the powerful incidence $H\in xy=c^2$; combining it with Euler-line geometry often exposes a midpoint, circle, or reflection that coordinates alone would hide.

:::key title="A productive proof pattern"
Parameterize three points by $t_1,t_2,t_3$, compute a slope as $-1/(t_it_j)$, and use the orthocentre formula when perpendicularity appears. If the problem involves a fourth point on the same rectangular hyperbola, test whether it is the orthocentre of the other three before introducing more variables.
:::
