---
id: jee-01
part: jee
title: "Vector Language — Components, Magnitude and Direction"
---

## A vector is a displacement, not a location

A **scalar** has size only. A **vector** has size and direction. Two arrows represent the same free vector when they have the same length and direction, even if their starting points differ. This freedom to translate an arrow is why vectors simplify geometry.

A **position vector** is different in use: after an origin $O$ is chosen, $\mathbf{a}=\overrightarrow{OA}$ names the point $A$. A displacement between two points is always
$$
\overrightarrow{AB}=\mathbf{b}-\mathbf{a}.
$$
Subtract in the order **head minus tail**. Reversing the order reverses the vector.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "A free vector can be translated without changing it",
  "xrange": [-1, 7], "yrange": [-1, 4.5], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [3, 2], "label": "a = (3,2)", "dx": -0.55, "dy": 0.35, "color": "#0F766E"},
    {"kind": "arrow", "a": [3, 0], "b": [6, 2], "label": "same a", "dx": -0.35, "dy": 0.35, "color": "#B8860B"},
    {"kind": "point", "at": [0, 0], "label": "tail", "dx": -0.4, "dy": -0.55},
    {"kind": "point", "at": [3, 2], "label": "head", "dx": 0.15, "dy": 0.15}
  ],
  "caption": "Both arrows have horizontal component 3 and vertical component 2. Their starting points do not change the vector."
}
:::

## Components turn geometry into arithmetic

In three dimensions,
$$
\mathbf{a}=a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}=(a_1,a_2,a_3),
\qquad
|\mathbf{a}|=\sqrt{a_1^2+a_2^2+a_3^2}.
$$
For a nonzero vector, its unit vector is $\widehat{\mathbf{a}}=\mathbf{a}/|\mathbf{a}|$. The components of this unit vector are its **direction cosines**, so their squares sum to $1$.

The ordinary components are direction ratios: they fix direction but need not have length $1$. Normalize before calling them direction cosines.

:::example title="Magnitude, unit vector and direction cosines"
For $\mathbf{a}=(2,-1,2)$,
$$
|\mathbf{a}|=\sqrt{4+1+4}=3,
\qquad
\widehat{\mathbf{a}}=\left(\frac{2}{3},-\frac{1}{3},\frac{2}{3}\right).
$$
Thus the direction cosines are $2/3,-1/3,2/3$, and
$$
\left(\frac{2}{3}\right)^2+\left(-\frac{1}{3}\right)^2+\left(\frac{2}{3}\right)^2=1.
$$
The direction ratios $2,-1,2$ are not themselves direction cosines.
:::

:::example title="A displacement is head minus tail"
If $A=(1,-2,3)$ and $B=(4,2,-1)$, then
$$
\overrightarrow{AB}=(4-1,2-(-2),-1-3)=(3,4,-4),
\qquad AB=\sqrt{9+16+16}=\sqrt{41}.
$$
Also $\overrightarrow{BA}=(-3,-4,4)=-\overrightarrow{AB}$.
:::

## Equality, parallelism and the zero vector

Vectors are equal exactly when all corresponding components agree. Two nonzero vectors are parallel when one is a scalar multiple of the other; the scalar's sign tells whether they have the same or opposite direction. Equivalently, their component ratios agree wherever the ratios are defined, but scalar multiplication avoids division-by-zero problems.

The zero vector $\mathbf{0}=(0,0,0)$ has length $0$ and no direction. Do not divide by $|\mathbf{a}|$ until $\mathbf{a}\ne\mathbf{0}$ is known, and do not assign a unit vector to $\mathbf{0}$.

:::key title="Choose the object before choosing the formula"
Use a **position vector** to locate a point, a **displacement** to compare two points, and a **free vector** to represent a direction or physical quantity. Once the object is clear, component arithmetic is routine.
:::
