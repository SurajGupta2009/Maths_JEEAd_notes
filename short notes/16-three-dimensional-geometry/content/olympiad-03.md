---
id: olympiad-03
part: olympiad
title: "Extension III — Radical Planes, Polars and Orthogonality"
---

## Subtracting sphere equations leaves a radical plane

The power of $P$ with respect to a sphere with centre $C$ and radius $R$ is $|P-C|^2-R^2$. For two spheres, subtracting their equations cancels all quadratic terms and gives the **radical plane**: the locus of points having equal power with respect to both. It is perpendicular to the line of centres. If the spheres intersect, their intersection circle lies in this plane.

:::example title="A radical plane with a power check"
For
$$
x^2+y^2+z^2=25,
\qquad (x-3)^2+y^2+z^2=16,
$$
write the second as $x^2+y^2+z^2-6x-7=0$. Subtracting gives
$$
6x-18=0\quad\Longrightarrow\quad x=3.
$$
At $(3,1,2)$, both powers are $-11$. The intersection circle is $y^2+z^2=16$ in the plane $x=3$.
:::

## Orthogonal spheres have perpendicular radii at intersection

Two intersecting spheres are orthogonal when their radii to a common point are perpendicular. If their centres are distance $d$ apart, the triangle formed by the centres and that point gives
$$
d^2=r_1^2+r_2^2.
$$
In general-form coefficients this is equivalently
$$
2(u_1u_2+v_1v_2+w_1w_2)=d_1+d_2.
$$

:::example title="Orthogonality checked two ways"
For $x^2+y^2+z^2-6x=0$ and $x^2+y^2+z^2-6y=0$, the centres are $(3,0,0)$ and $(0,3,0)$, and both radii are $3$. Hence
$$
d^2=18=9+9=r_1^2+r_2^2.
$$
The coefficient form gives $0=0$ as well. In contrast, radii $5,4$ with centre distance $5$ do not satisfy orthogonality because $25\ne25+16$.
:::

## Tangents from an external point form a cone

For $P$ outside a sphere, let $D=PC>R$. Every tangent segment has length $\sqrt{D^2-R^2}$. The semi-vertical angle $\alpha$ of the tangent cone satisfies
$$
\sin\alpha=\frac{R}{D}.
$$
The contact points form a circle in the polar plane, at distance $R^2/D$ from $C$ along $CP$, with circle radius
$$
\rho=R\sqrt{1-\frac{R^2}{D^2}}.
$$

:::example title="The 5–12–13 tangent cone"
For $P=(13,0,0)$ and $x^2+y^2+z^2=25$,
$$
D=13,\qquad \sin\alpha=\frac{5}{13},\qquad \alpha\approx22.62^\circ.
$$
The tangent length is $12$. The contact circle lies in
$$
x=\frac{25}{13},
\qquad y^2+z^2=\left(\frac{60}{13}\right)^2,
$$
so its radius is $60/13$. Its plane is the polar plane $13x=25$ of $P$.
:::

:::diagram
{
  "type": "vector3d",
  "title": "The contact circle lies in the external point's polar plane",
  "xrange": [-6, 15], "yrange": [-7, 7], "zrange": [-7, 7],
  "elev": 20, "azim": -60, "zoom": 1.05,
  "elements": [
    {"kind": "sphere", "centre": [0, 0, 0], "r": 5, "fill": "#DCEFED", "color": "#5B6B84", "alpha": 0.08, "wire_alpha": 0.23},
    {"kind": "circle3d", "centre": [1.9231, 0, 0], "r": 4.6154, "normal": [1, 0, 0], "color": "#B91C1C", "lw": 3},
    {"kind": "segment", "a": [13, 0, 0], "b": [1.9231, 0, 4.6154], "color": "#0F766E", "lw": 2.5},
    {"kind": "segment", "a": [13, 0, 0], "b": [1.9231, 4.6154, 0], "color": "#0F766E", "lw": 2.5},
    {"kind": "segment", "a": [0, 0, 0], "b": [1.9231, 0, 4.6154], "ls": "--", "color": "#B8860B"},
    {"kind": "point", "at": [13, 0, 0], "label": "P(13,0,0)", "offset": [0.2, 0, 1.2]},
    {"kind": "point", "at": [0, 0, 0], "label": "C", "offset": [-0.4, 0, -0.3]},
    {"kind": "point", "at": [1.9231, 0, 4.6154], "label": "T", "offset": [-0.35, 0, 0.3], "color": "#B91C1C"},
    {"kind": "point", "at": [1.9231, 4.6154, 0], "label": "T'", "offset": [0, 0.4, 0], "color": "#B91C1C"}
  ],
  "caption": "CT=5 is perpendicular to PT=12, while CP=13. Every contact point lies on x=25/13 and has y^2+z^2=(60/13)^2."
}
:::

## Polar and radical constructions extend naturally

For $x^2+y^2+z^2=R^2$, the polar plane of $P=(x_1,y_1,z_1)$ is
$$
xx_1+yy_1+zz_1=R^2.
$$
For $P=(1,2,3)$ and $R=5$, it is $x+2y+3z=25$. Since $P$ is inside the sphere, no real tangent cone exists, but the polar plane remains defined. If the polar of $P$ contains $Q$, the polar of $Q$ contains $P$.

:::example title="Reciprocity checked on a contact point"
For $P=(13,0,0)$ and $R=5$, take the contact point $T=(25/13,0,60/13)$. The polar of $P$ is $13x=25$, which contains $T$. Conversely, the polar of $T$ is
$$
\frac{25}{13}x+\frac{60}{13}z=25,
$$
and substituting $P$ gives $25=25$. This verifies the reciprocal polar relation using the tangent construction.
:::

Three spheres generally have three radical planes sharing a **radical axis**. For the source spheres $x^2+y^2+z^2=14$, $(x-5)^2+y^2+z^2=29$ and $x^2+(y-5)^2+z^2=19$, those planes give $x=1$, $y=2$ and $y=x+1$. Thus the radical axis is $(1,2,t)$, and every point on it has common power $t^2-9$.

:::key title="A useful coaxal extension"
A sphere orthogonal to two given spheres is orthogonal to every member of their coaxal pencil, and its centre lies on their radical plane. This follows by linearity of the general-form orthogonality condition.
:::
