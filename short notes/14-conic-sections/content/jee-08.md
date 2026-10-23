---
id: jee-08
part: jee
title: "The Unified Toolkit — Tangents, Contacts and Midpoint Chords"
---

## Define $S$, $S_1$ and $T$ once

Write a conic as $S(x,y)=0$. Let $S_1=S(x_1,y_1)$. Obtain $T$ by the symmetric replacements
$$
x^2\mapsto xx_1,\quad y^2\mapsto yy_1,\quad
2xy\mapsto xy_1+x_1y,
$$
$$
2x\mapsto x+x_1,\quad 2y\mapsto y+y_1,\quad \text{constants unchanged}.
$$
For example, the ellipse has $S=x^2/a^2+y^2/b^2-1$ and $T=xx_1/a^2+yy_1/b^2-1$. For $y^2=4ax$, use $S=y^2-4ax$ and $T=yy_1-2a(x+x_1)$.

:::key title="Four meanings of the same notation"
- At an on-conic point, the tangent is $T=0$.
- From an external point, the chord of contact is $T=0$.
- The chord with midpoint $(x_1,y_1)$ is $T=S_1$, provided the resulting chord is real.
- The joint equation of the pair of tangents from $(x_1,y_1)$ is $SS_1=T^2$.

These formulas use consistent conventions. Mixing a conic normalized with $-1$ against a $T$ expression without that $-1$ destroys the result.
:::

## Chord of contact: two tangents, one line

If tangents from $(x_1,y_1)$ touch at $Q$ and $R$, each contact point satisfies the condition for its tangent to pass through $(x_1,y_1)$. That condition is precisely $T=0$, so both contacts lie on this one line.

:::example title="Contacts from $(4,2)$ to $x^2/16+y^2/4=1$"
The chord of contact is
$$
\frac{4x}{16}+\frac{2y}{4}=1
\quad\Longleftrightarrow\quad x+2y=4.
$$
Intersecting it with the ellipse gives $Q=(4,0)$ and $R=(0,2)$. The tangents are respectively $x=4$ and $y=2$, and both contain $(4,2)$. This verifies both the contact points and the chord equation.
:::

## A midpoint condition is a Vieta condition

For a chord through $(x_1,y_1)$ in direction $(u,v)$, substituting $(x_1+tu,y_1+tv)$ gives a quadratic in $t$. The midpoint is exactly the supplied point when the two roots are opposite, so their sum is zero. Removing that linear coefficient yields $T=S_1$.

:::example title="An ellipse chord bisected at $(2,1)$"
For $x^2/16+y^2/9=1$,
$$
S_1=\frac{4}{16}+\frac{1}{9}-1=-\frac{23}{36}.
$$
Thus $T=S_1$ becomes
$$
\frac{2x}{16}+\frac{y}{9}=\frac{4}{16}+\frac{1}{9}
\quad\Longleftrightarrow\quad9x+8y=26.
$$
Substitution into the ellipse gives a quadratic whose two $x$-roots sum to $4$ and whose discriminant is positive; the corresponding $y$-roots sum to $2$. Hence this is a genuine chord, not merely a formal line.
:::

:::diagram
{
  "type": "flow",
  "title": "Choose the unified conic tool by the wording of the question",
  "steps": [
    {"title": "Point lies on the conic", "detail": "Use T = 0 for the tangent; verify membership first."},
    {"title": "Tangents from an external point", "detail": "Use T = 0 for the chord of contact, or S*S1 = T^2 for the pair of tangents."},
    {"title": "Midpoint of a chord is supplied", "detail": "Use T = S1, then check that real intersection points exist."},
    {"title": "Verify the geometry", "detail": "Check incidence, tangency by a repeated root, and midpoint by root sums."}
  ],
  "caption": "The formula is only the start. A final incidence or reality check prevents a formally correct line from describing an impossible configuration."
}
:::

:::warn title="A midpoint on the conic is a boundary case"
If $(x_1,y_1)$ lies on the conic, the two chord endpoints must coalesce there for it to be their midpoint. The formula $T=S_1$ then reduces to the tangent $T=0$ because $S_1=0$. Do not expect two distinct endpoints in this case.
:::
