---
id: jee-03
part: jee
title: "Parabola — Tangents, Normals and Reflection"
---

## Two lines at $P(t)$ do most of the work

At $P(t)=(at^2,2at)$ on $y^2=4ax$,
$$
\text{tangent: }ty=x+at^2,\qquad
\text{normal: }y=-tx+2at+at^3.
$$
For a finite tangent slope $m=1/t\ne0$,
$$
y=mx+\frac{a}{m},\qquad \text{contact }\left(\frac{a}{m^2},\frac{2a}{m}\right).
$$
For a normal of slope $m=-t$, $y=mx-2am-am^3$. Tangents at $t_1,t_2$ meet at
$$
T=\left(at_1t_2,a(t_1+t_2)\right).
$$
Consequently they are perpendicular exactly when their slopes multiply to $-1$, namely $t_1t_2=-1$; their intersection then lies on $x=-a$, the directrix.

:::example title="The focal-chord and directrix facts agree"
Use the focal chord of $y^2=8x$ with parameters $2$ and $-1/2$. Here $a=2$ and $t_1t_2=-1$. The tangents meet at
$$
T=\left(2\cdot(-1),2\left(2-\frac{1}{2}\right)\right)=(-2,3),
$$
which really is on the directrix $x=-2$. Their slopes $1/2$ and $-2$ multiply to $-1$. Notice that the parameters, not merely the endpoint coordinates, are needed for this conclusion.
:::

## Axis intercepts give quick geometric quantities

The tangent at $P(t)$ meets the axis at $(-at^2,0)$. For $t\ne0$, the normal meets it at $N=(at^2+2a,0)$, and the subnormal is constantly $2a$; at $t=0$, the normal is the axis itself. At the focus $S(a,0)$,
$$
SN=a(1+t^2)=SP.
$$
So triangle $SPN$ is isosceles. The normal bisects the angle between the focal ray and the axis direction; this proves the reflection property: rays parallel to the axis reflect through the focus, and rays from the focus emerge parallel to the axis.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "At P(1,2) on y^2 = 4x, SP = SN = 2",
  "xrange": [-2.5, 4.5], "yrange": [-3.5, 4.5],
  "elements": [
    {"kind": "parabola", "a": 1, "trange": [-1.8, 1.8], "color": "#0F766E"},
    {"kind": "line", "a": [-1, 0], "b": [3, 4], "color": "#B8860B"},
    {"kind": "line", "a": [0, 3], "b": [4, -1], "color": "#B91C1C"},
    {"kind": "segment", "a": [1, 0], "b": [1, 2], "color": "#B8860B"},
    {"kind": "segment", "a": [1, 0], "b": [3, 0]},
    {"kind": "point", "at": [1, 2], "label": "P(1,2)", "dx": 0.15},
    {"kind": "point", "at": [1, 0], "label": "S", "dx": -0.3, "dy": -0.45, "color": "#B8860B"},
    {"kind": "point", "at": [3, 0], "label": "N(3,0)", "dx": 0.15, "dy": 0.2, "color": "#B91C1C"},
    {"kind": "text", "at": [1.45, 3.25], "text": "tangent: y = x + 1", "color": "#B8860B"},
    {"kind": "text", "at": [-2.25, 3.25], "text": "normal: y = -x + 3", "color": "#B91C1C"},
    {"kind": "text", "at": [1.25, 0.55], "text": "SP = 2", "color": "#B8860B"},
    {"kind": "text", "at": [1.35, -0.75], "text": "SN = 2", "color": "#0F766E"}
  ],
  "caption": "Here a = 1 and t = 1. The tangent and normal are perpendicular, while equal lengths SP and SN explain the equal-angle reflection property."
}
:::

## Normals from an external point form a cubic

A normal of slope $m$ passes through $(h,k)$ precisely when
$$
am^3+(2a-h)m+k=0.
$$
There are at most three real normals. Vieta also gives $m_1+m_2+m_3=0$ for the cubic roots; in particular, when three real normals exist, their slopes sum to zero. A cubic root count must still be checked—having three algebraic roots does not say all are real and distinct.

:::example title="All normals from $(6,0)$ to $y^2=4x$"
With $a=1$, the cubic becomes
$$
m^3-4m=m(m-2)(m+2)=0.
$$
The slopes are $0,2,-2$. Since the contact parameter is $t=-m$, the feet are $(0,0),(4,-4),(4,4)$, respectively. The three normal lines are $y=0$, $y=2x-12$, and $y=-2x+12$; all pass through $(6,0)$.
:::

## Tangency is a repeated-root condition

Substituting $y=mx+c$ into $y^2=4ax$ gives
$$
m^2x^2+(2mc-4a)x+c^2=0.
$$
A tangent has a repeated root, so its discriminant is zero and $c=a/m$ for $m\ne0$. This is the derivation behind the slope form, and it also supplies a quick independent check: substitution at the stated contact must produce a perfect square.

:::example title="Two tangents from a point on the directrix"
For $y^2=8x$, take the external point $(-2,0)$ on the directrix. A tangent $y=mx+2/m$ passes through it when
$$
0=-2m+\frac{2}{m}\quad\Longrightarrow\quad m^2=1.
$$
The tangents are $y=x+2$ and $y=-x-2$, with contacts $(2,4)$ and $(2,-4)$. Their slopes are perpendicular, and the contact chord is the latus rectum $x=2$.
:::

:::warn title="Do not invent a directrix"
The intersection formula gives $x=at_1t_2$. Only when $t_1t_2=-1$ does this become $x=-a$. Two arbitrary tangents need not be perpendicular and need not meet on the directrix. Verify the parameter product before quoting the focal-chord theorem.
:::
