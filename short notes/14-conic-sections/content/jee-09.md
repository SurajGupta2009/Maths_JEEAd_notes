---
id: jee-09
part: jee
title: "Pole, Polar and Mixed Conic Strategy"
---

## Polarity turns points into lines

For a point $P=(x_1,y_1)$, the line $T=0$ is its **polar**, and $P$ is the **pole** of that line. If $P$ is external, the polar is the chord of contact. If $P$ lies on the conic, the polar is the tangent at $P$. The definition remains meaningful for interior points too.

:::derive title="La Hire's theorem is symmetry"
Polar equations use a symmetric bilinear expression. Therefore
$$
Q\text{ lies on the polar of }P
\quad\Longleftrightarrow\quad
P\text{ lies on the polar of }Q.
$$
This incidence reciprocity is La Hire's theorem. It often replaces a fresh equation-solving step with one substitution.
:::

Two special cases are worth immediate recognition:

- The polar of a focus is its corresponding directrix. For the ellipse, the polar of $(ae,0)$ is $aex/a^2=1$, hence $x=a/e$.
- The pole of a tangent is its contact point. Conversely, the pole of a chord is the intersection of the tangents at its endpoints.

:::example title="Find a pole by matching coefficients"
For $y^2=4x$, the polar of $(x_1,y_1)$ is $yy_1=2(x+x_1)$. To obtain the vertical line $x=8$, we need $y_1=0$ and $2(x+x_1)$ proportional to $x-8$. Thus $x_1=-8$. The pole is $(-8,0)$; indeed its polar is $0=2(x-8)$.
:::

## The three director loci are not interchangeable

The locus of intersections of perpendicular tangents is
$$
\text{ellipse: }x^2+y^2=a^2+b^2,
$$
$$
\text{hyperbola: }x^2+y^2=a^2-b^2,
$$
while for a parabola it is the directrix $x=-a$. For the hyperbola, reality requires $a>b$; the rectangular case has no real perpendicular tangent pair.

:::example title="One ellipse, several coordinated answers"
For $x^2/25+y^2/9=1$ and $P$ with eccentric angle $60^\circ$:
$$
P=\left(\frac{5}{2},\frac{3\sqrt{3}}{2}\right),\qquad e=\frac{4}{5}.
$$
Its focal distances are $a-ex=3$ and $a+ex=7$. The tangent at $P$ is
$$
\frac{x\cos60^\circ}{5}+\frac{y\sin60^\circ}{3}=1
\quad\Longleftrightarrow\quad3x+5\sqrt{3}y=30.
$$
The director circle is $x^2+y^2=34$. Each result comes from a different named tool; none requires expanding two distance radicals.
:::

:::diagram
{
  "type": "flow",
  "title": "A reliable mixed-conic workflow",
  "steps": [
    {"title": "Name the curve and orientation", "detail": "Read denominators and signs; identify axes, a, b, c and e before substituting data."},
    {"title": "Choose coordinates or parameters", "detail": "Use t for parabola chords, eccentric angle for ellipse, sec/tan for hyperbola, and ct,c/t for xy=c^2."},
    {"title": "Match the requested object", "detail": "Use focal-distance laws, tangent forms, T = 0, T = S1, or polarity rather than expanding by default."},
    {"title": "Close with an independent check", "detail": "Verify membership, incidence, slope product, discriminant, root sum, or a focal-distance sum/difference."}
  ],
  "caption": "Most conic errors are convention errors rather than difficult algebra. A ten-second final check catches a wrong directrix, sign, branch, or parameter immediately."
}
:::

:::warn title="A formula cannot rescue impossible data"
Check that the point lies on the claimed curve, the slope lies in the allowed tangent range, and a requested chord has real endpoints. If the geometry is impossible, the correct response is to report that fact—not to continue until an algebraic expression appears.
:::
