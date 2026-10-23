---
id: jee-90
part: jee
title: "Visual Complex-Number Lab — Argand Plane, Roots and Transformations"
---

## A complex number is a point and a vector

The number $z=x+iy$ corresponds to the point $(x,y)$. Its modulus $|z|=\sqrt{x^2+y^2}$ is the distance from the origin, and its argument is a directed angle, defined only modulo $2\pi$ unless a principal branch is requested. The conjugate $\bar z=x-iy$ is reflection in the real axis.

:::diagram
{
  "type": "geometry",
  "title": "Conjugation reflects; modulus measures distance",
  "xrange": [-1, 4.5], "yrange": [-3, 3], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [3, 2], "label": "z = 3 + 2i", "dx": 0.15},
    {"kind": "arrow", "a": [0, 0], "b": [3, -2], "label": "z bar = 3 - 2i", "dx": 0.15, "color": "#B8860B"},
    {"kind": "segment", "a": [3, -2], "b": [3, 2], "label": "imaginary parts reverse", "label_pos": 0.55, "dx": 0.15, "color": "#5B6B84"},
    {"kind": "point", "at": [3, 2], "label": "(3, 2)", "dx": 0.15},
    {"kind": "point", "at": [3, -2], "label": "(3, -2)", "dx": 0.15, "color": "#B8860B"}
  ],
  "caption": "Both vectors have modulus sqrt(13). Their real parts agree and their imaginary parts are negatives, so their product z z bar = 13 is real and nonnegative."
}
:::

Algebraically, $z\bar z=(x+iy)(x-iy)=x^2+y^2=|z|^2$. Also $z+\bar z=2x$ and $z-\bar z=2iy$. These identities turn many modulus or real-part questions into coordinate geometry.

<!-- pagebreak -->
## Roots of unity are equally spaced

Solutions of $z^n=1$ lie on the unit circle at angles $2k\pi/n$. They are vertices of a regular $n$-gon, not an unordered list to memorise. For $n=5$, write $\omega=e^{2\pi i/5}$; the roots are $1,\omega,\omega^2,\omega^3,\omega^4$.

:::diagram
{
  "type": "geometry",
  "title": "The five fifth roots of unity",
  "xrange": [-1.6, 1.6], "yrange": [-1.5, 1.5], "axes": false,
  "elements": [
    {"kind": "circle", "centre": [0, 0], "r": 1, "color": "#5B6B84", "ls": "--"},
    {"kind": "polygon", "points": [[1, 0], [0.309, 0.951], [-0.809, 0.588], [-0.809, -0.588], [0.309, -0.951]], "color": "#0F766E", "fill": "#E6F4F3", "alpha": 0.4},
    {"kind": "point", "at": [1, 0], "label": "1", "dx": 0.12},
    {"kind": "point", "at": [0.309, 0.951], "label": "w", "dx": 0.12},
    {"kind": "point", "at": [-0.809, 0.588], "label": "w^2", "dx": -0.45},
    {"kind": "point", "at": [-0.809, -0.588], "label": "w^3", "dx": -0.45, "dy": -0.3},
    {"kind": "point", "at": [0.309, -0.951], "label": "w^4", "dx": 0.12, "dy": -0.3}
  ],
  "caption": "Rotation by 2pi/5 permutes the roots. Their vector sum is zero, matching the coefficient of z^4 in z^5 - 1."
}
:::

Since $z^5-1=(z-1)(z^4+z^3+z^2+z+1)$, a nonreal fifth root satisfies $1+\omega+\omega^2+\omega^3+\omega^4=0$. The same symmetry gives $\omega^5=1$ and $\bar\omega=\omega^{-1}=\omega^4$.

<!-- pagebreak -->
## Multiplication rotates and scales

Write $z_1=r_1e^{i\theta_1}$ and $z_2=r_2e^{i\theta_2}$. Then $z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)}$: **moduli multiply and arguments add**. Division instead divides moduli and subtracts arguments, provided $z_2\ne0$.

:::diagram
{
  "type": "geometry",
  "title": "A product constructed from lengths and directions",
  "xrange": [-2, 3.5], "yrange": [-1, 4], "grid": true,
  "elements": [
    {"kind": "arrow", "a": [0, 0], "b": [1, 1], "label": "z1 = 1 + i", "dx": 0.15},
    {"kind": "arrow", "a": [0, 0], "b": [1, 2], "label": "z2 = 1 + 2i", "dx": 0.15, "color": "#B8860B"},
    {"kind": "arrow", "a": [0, 0], "b": [-1, 3], "label": "z1 z2 = -1 + 3i", "dx": 0.15, "color": "#B91C1C"},
    {"kind": "point", "at": [-1, 3], "label": "product", "dx": 0.15, "color": "#B91C1C"}
  ],
  "caption": "Direct multiplication gives (1 + i)(1 + 2i) = -1 + 3i. Its modulus is sqrt(10) = sqrt(2) sqrt(5), and its argument is the sum of the two input arguments."
}
:::

:::example title="Use geometry to check algebra"
For $(1+i)(1+2i)$, expansion gives $1+2i+i+2i^2=-1+3i$. Independently, $|1+i|=\sqrt{2}$, $|1+2i|=\sqrt{5}$, and $|-1+3i|=\sqrt{10}$. The modulus check does not prove every sign, but it quickly detects many expansion errors.
:::

<!-- pagebreak -->
## Transformations and equations: a reliable order

:::diagram
{
  "type": "flow",
  "title": "Translate between algebra and the Argand plane",
  "steps": [
    {"title": "Choose the representation", "detail": "Use x + iy for real and imaginary parts; use modulus-argument form for products, powers and rotations."},
    {"title": "Translate the condition geometrically", "detail": "Modulus gives distance, argument gives direction, conjugation reflects, and multiplication scales and rotates."},
    {"title": "Solve with the appropriate branch", "detail": "For roots include every angle modulo 2pi; for principal arguments use the specified interval."},
    {"title": "Verify modulus, argument and root count", "detail": "Substitute numerically and confirm that a degree-n polynomial has not lost or gained candidates."}
  ],
  "caption": "The picture supplies a model and a check, while exact algebra supplies the final values. Use both rather than treating them as separate chapters."
}
:::

:::key title="Three identities worth reconstructing"
For $z\ne0$, $z^{-1}=\bar z/|z|^2$. On the unit circle this becomes $z^{-1}=\bar z$. For any $z$, $|z|^2=z\bar z$. For roots of unity, equally spaced points make sums and products visible before any trigonometric evaluation.
:::
