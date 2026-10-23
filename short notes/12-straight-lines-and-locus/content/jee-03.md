---
id: jee-03
part: jee
title: "Angles, Parallelism, Perpendicularity, Distance"
---

## Compare directions without trusting a sketch

For nonvertical slopes $m_1,m_2$, the acute angle $\theta$ between the lines satisfies
$$\tan\theta=\left|\frac{m_1-m_2}{1+m_1m_2}\right|.$$
Hence parallel lines have equal slopes and perpendicular lines have $m_1m_2=-1$. The slope test needs care for vertical lines; the coefficient test below does not.

For $L_i:a_ix+b_iy+c_i=0$, use normals $n_i=(a_i,b_i)$. The acute angle obeys
$$\cos\theta=\frac{|a_1a_2+b_1b_2|}{\sqrt{a_1^2+b_1^2}\sqrt{a_2^2+b_2^2}},\qquad
\sin\theta=\frac{|a_1b_2-a_2b_1|}{\sqrt{a_1^2+b_1^2}\sqrt{a_2^2+b_2^2}}.$$
Parallel iff $a_1b_2-a_2b_1=0$; perpendicular iff $a_1a_2+b_1b_2=0$.

:::example title="A vertical–horizontal pair"
$x=2$ has normal $(1,0)$ and $y=-3$ has normal $(0,1)$. Their dot product is $0$, so the lines are perpendicular even though one slope is undefined.
:::

:::diagram
{"type":"graph","xrange":[-4,4],"yrange":[-4,4],"curves":[{"expr":"0.5*x+1","from":-4,"to":4,"label":"m = 1/2","color":"#0F766E"},{"expr":"-2*x+1","from":-1.5,"to":2.5,"label":"m = -2","color":"#16295C"}],"points":[{"x":0,"y":1,"label":"P"}],"title":"Perpendicular lines: slope product = -1"}
:::

## Perpendicular distance is a projection

For $L:ax+by+c=0$ and point $P=(x_0,y_0)$,
$$d(P,L)=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}.$$
The signed distance is the same expression without absolute values, once the normal orientation is fixed.

:::derive title="Foot of the perpendicular"
Let $H=P-t(a,b)$. Requiring $H$ on $L$ gives $t=(ax_0+by_0+c)/(a^2+b^2)$. Thus
$$H=P-\frac{ax_0+by_0+c}{a^2+b^2}(a,b).$$
The removed vector is parallel to the normal, so $PH\perp L$; its length is the point–line distance.
:::

:::example title="Distance and foot for the same line"
From $P=(1,2)$ to $x+y=0$, signed distance is $3/\sqrt{2}$ and $H=(1,2)-(3/2)(1,1)=(-1/2,1/2)$. Check $H$ satisfies $x+y=0$ and $PH$ has direction $(1,1)$, normal to the line.
:::

:::warn title="Distance formula is scale-invariant"
Multiplying $a,b,c$ by a nonzero number does not change the line or its distance: numerator and denominator scale by the same absolute factor. Do not omit $\sqrt{a^2+b^2}$.
:::
