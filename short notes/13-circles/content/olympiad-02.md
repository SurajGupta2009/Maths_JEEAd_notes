---
id: olympiad-02
part: olympiad
title: "Inversion and Distance-Ratio Circles"
---

## Inversion in a circle

Inversion of radius $\rho$ about centre $O$ sends $P\ne O$ to $P'$ on ray $OP$ so that $OP\cdot OP'=\rho^2$. With $O$ at the origin,
$$P'=\frac{\rho^2P}{|P|^2}.$$
It is involutive and reverses orientation while preserving angles in magnitude. The centre has no finite image.

:::derive title="A line not through the inversion centre becomes a circle"
For unit inversion, write $x=X/(X^2+Y^2)$ and $y=Y/(X^2+Y^2)$. The line $x=a\ne0$ becomes $X=a(X^2+Y^2)$, or $(X-1/(2a))^2+Y^2=1/(4a^2)$: a circle through the origin. A line through the origin stays a line; conversely, a circle through the origin maps to a line not through it.
:::

## Distance ratio is a circle, with a line as the limiting case

For distinct $A,B$, the locus $PA/PB=k$ is the perpendicular bisector when $k=1$ and a circle when $k\ne1$. The centre lies on $AB$ and the circle degenerates to $A$ at $k=0$. This is the Apollonius locus; a derivation and coordinate-safe formula are in Chapter 12.

:::warn title="Check for the exceptional ratio"
Do not divide by $1-k^2$ before splitting off $k=1$. For equal distances the locus is a line, not a circle of “infinite radius” in an ordinary coordinate calculation.
:::
