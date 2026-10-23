---
id: jee-02
part: jee
title: "Parabola — Anatomy, Parameters and Focal Chords"
---

## Read the anatomy before starting algebra

For $y^2=4ax$ with $a>0$: vertex $(0,0)$, focus $S(a,0)$, directrix $x=-a$, axis $y=0$, and latus rectum endpoints $(a,\pm2a)$. At $P(x,y)$ on the curve, $SP=x+a$. The reflected forms are $y^2=-4ax$, $x^2=4ay$, and $x^2=-4ay$; a vertex shift $(h,k)$ gives $(y-k)^2=4a(x-h)$ and its analogues.

:::warn title="Match $4a$, not $a$"
For $y^2=16x$, $4a=16$, so $a=4$. The focus is not $(16,0)$. Also reverse the focal-distance sign when the parabola opens left: always derive it from the corresponding directrix rather than memorizing blindly.
:::

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "Anatomy of y^2 = 8x: a = 2",
  "xrange": [-3.5, 10], "yrange": [-9, 9],
  "elements": [
    {"kind": "parabola", "a": 2, "trange": [-2.15, 2.15], "color": "#0F766E"},
    {"kind": "line", "a": [-2, -8], "b": [-2, 8], "label": "directrix x = -2", "label_pos": 0.1, "dx": 0.2, "color": "#B91C1C"},
    {"kind": "segment", "a": [2, -4], "b": [2, 4], "label": "latus rectum = 8", "label_pos": 0.72, "dx": 0.4, "dy": 0.0, "color": "#B8860B"},
    {"kind": "point", "at": [0, 0], "label": "V", "dx": -0.35, "dy": 0.25},
    {"kind": "point", "at": [2, 0], "label": "S(2,0)", "dx": 0.25, "dy": -0.65, "color": "#B8860B"},
    {"kind": "point", "at": [2, 4], "label": "(2,4)", "dx": 0.5},
    {"kind": "point", "at": [2, -4], "label": "(2,-4)", "dx": 0.5, "dy": -0.5},
    {"kind": "point", "at": [8, 8], "label": "P(2) = (8,8)", "dx": -1.7, "dy": 0.65}
  ],
  "caption": "At P(t) = (at^2, 2at), t = 2 gives (8,8). Its focal distance is x + a = 10 = a(1 + t^2)."
}
:::

## The parameter turns coordinates into one variable
Every point of $y^2=4ax$ is
$$
P(t)=(at^2,2at),\qquad t\in\mathbb{R}.
$$
Immediately $SP=a(1+t^2)$. The chord through $P(t_1)$ and $P(t_2)$ is
$$
(t_1+t_2)y=2x+2at_1t_2.
$$
Its slope is $2/(t_1+t_2)$ when $t_1+t_2\ne0$. Substituting the focus $(a,0)$ into the chord equation proves the essential focal-chord test
$$
t_1t_2=-1.
$$
Thus one end $P(t)$ determines the other $P(-1/t)$. Their focal distances are $a(1+t^2)$ and $a(1+1/t^2)$, so the full chord length is
$$
a\left(2+t^2+\frac{1}{t^2}\right)=a\left(t+\frac{1}{t}\right)^2.
$$
The minimum is $4a$ at $t=\pm1$, the latus rectum.

:::derive title="The semi-latus rectum is a harmonic mean"
If a focal chord is divided by the focus into lengths $u$ and $v$, then
$$
\frac{1}{u}+\frac{1}{v}=\frac{1}{a}=\frac{2}{2a}.
$$
Therefore the harmonic mean $2/(1/u+1/v)$ is $2a$, the semi-latus rectum. For an ellipse the corresponding constant is $b^2/a$. Hyperbola focal chords require branch-aware signs, so this unsigned formula must not be transferred automatically.
:::

:::example title="A focal chord with exact endpoints"
For $y^2=8x$, $a=2$. Take $t=2$, so one endpoint is $P(2)=(8,8)$. The other parameter is $-1/2$, giving
$$
P\left(-\frac{1}{2}\right)=\left(\frac{1}{2},-2\right).
$$
The two focal parts are $10$ and $5/2$, so the chord length is $25/2$. Also $1/10+2/5=1/2=1/a$, confirming the harmonic-mean relation.
:::

:::key title="When to choose parameters"
Use $t$ for chords through named points, focal chords, tangent intersections, and normals. Use direct $(x,y)$ substitution for a single focal distance or a quick membership check. The parameter is not an angle.
:::
