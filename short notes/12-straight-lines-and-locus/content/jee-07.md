---
id: jee-07
part: jee
title: "Pairs of Lines and a Coordinate Toolkit"
---

## A homogeneous quadratic may be two lines

The equation $ax^2+2hxy+by^2=0$ passes through the origin and is homogeneous. Put $y=mx$ to obtain $bm^2+2hm+a=0$; its real roots are the slopes of the line factors. If $b=0$, factor in the other direction so a vertical factor is not lost.

:::derive title="Angle and perpendicularity from the roots"
For two distinct real slopes $m_1,m_2$, their angle obeys $\tan\theta=|(m_1-m_2)/(1+m_1m_2)|$. The product of roots is $a/b$ when $b\ne0$, so perpendicular factors require $a/b=-1$, equivalently $a+b=0$. The discriminant $4(h^2-ab)$ determines whether the factors are real and distinct, repeated, or complex.
:::

:::example title="Factor first, then identify the geometry"
$2x^2+3xy-2y^2=(2x-y)(x+2y)$, so the lines are $y=2x$ and $y=-x/2$. Their slopes multiply to $-1$: they are perpendicular.
:::

:::warn title="Scope and degeneracy"
This homogeneous-pair criterion is a useful derived tool, not a separately listed line-form bullet in the official syllabus. A real pair requires $h^2-ab\geq0$; if equality holds the line is repeated. The slope-root method must account for a vertical factor.
:::

## Five checks before a coordinate answer is final

1. **Domain of the formula:** is a denominator zero, or is a slope vertical?
2. **Geometry:** do distances stay nonnegative and are lines distinct where assumed?
3. **Scale:** is a point–line formula invariant if the equation is rescaled?
4. **Locus:** does the equation imply the original condition as well as follow from it?
5. **Triangle centre:** does the proposed point satisfy its defining equal-distance or perpendicularity property?

:::example title="Quick independent check"
For $A=(0,0),B=(4,0)$, the point $P=(2,3)$ is equidistant from both: $PA^2=2^2+3^2=13=PB^2$. It lies on $x=2$, the derived locus. The converse also holds for every point on that line.
:::
