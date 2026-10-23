---
id: jee-01
part: jee
title: "The Conic Family — Focus, Directrix and Eccentricity"
---

## One distance ratio creates three curves

Fix a focus $F$, a directrix $\ell$ not passing through $F$, and $e>0$. A point $P$ lies on the corresponding conic when
$$
PF=e\,\operatorname{dist}(P,\ell).
$$
The ratio is the **eccentricity**: $0<e<1$ gives an ellipse, $e=1$ a parabola, and $e>1$ a hyperbola. A circle is the limiting ellipse with $e=0$ and its directrix at infinity; putting $e=0$ into the finite-line equation instead collapses the locus to the focus itself.

:::key title="Classify before calculating"
The value of $e$ names the curve. Do not apply an ellipse relation such as $b^2=a^2-c^2$ to a hyperbola, where $b^2=c^2-a^2$. First decide the curve, then choose its formula family.
:::

## The parabola is one squaring away

For $F=(a,0)$ and directrix $x=-a$, the vertex is midway between them. At $P=(x,y)$,
$$
(x-a)^2+y^2=(x+a)^2\quad\Longrightarrow\quad y^2=4ax.
$$
Here $a>0$, the focus is $(a,0)$, the axis is $y=0$, and the latus rectum has endpoints $(a,\pm2a)$ and length $4a$. On the curve, $PF=x+a$: a focal distance becomes a coordinate, not a square root.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "On y^2 = 4x, both distances at P(4,4) equal 5",
  "xrange": [-2.2, 6.5], "yrange": [-5.5, 5.5], "grid": true,
  "elements": [
    {"kind": "parabola", "a": 1, "trange": [-2.25, 2.25], "color": "#0F766E"},
    {"kind": "line", "a": [-1, -5], "b": [-1, 5], "color": "#B91C1C"},
    {"kind": "segment", "a": [1, 0], "b": [4, 4], "label": "PF = 5", "label_pos": 0.55, "dx": 0.5, "dy": -0.4, "color": "#B8860B"},
    {"kind": "segment", "a": [-1, 4], "b": [4, 4], "label": "distance = 5", "label_pos": 0.3, "dy": 0.3},
    {"kind": "point", "at": [1, 0], "label": "F(1,0)", "dy": -0.55, "color": "#B8860B"},
    {"kind": "point", "at": [4, 4], "label": "P(4,4)", "dx": 0.4, "dy": 0.7},
    {"kind": "point", "at": [-1, 4], "label": "foot", "dx": -0.55, "dy": 0.2, "size": 6},
    {"kind": "text", "at": [0.3, -4.5], "text": "directrix x = -1", "color": "#B91C1C"}
  ],
  "caption": "The curve is y^2 = 4x, so a = 1. PF = sqrt(3^2 + 4^2) = 5 and the distance to x = -1 is also 5."
}
:::

## Central conics use two foci

For an ellipse with foci $(\pm c,0)$ and $a>c$,
$$
PF_1+PF_2=2a,\qquad b^2=a^2-c^2,\qquad \frac{x^2}{a^2}+\frac{y^2}{b^2}=1.
$$
Its eccentricity is $e=c/a<1$, its directrices are $x=\pm a/e$, and its focal distances are $a\pm ex$. For a hyperbola with $c>a$,
$$
|PF_1-PF_2|=2a,\qquad b^2=c^2-a^2,\qquad \frac{x^2}{a^2}-\frac{y^2}{b^2}=1.
$$
Now $e=c/a>1$, the directrices remain $x=\pm a/e$, and the absolute difference selects both branches.

:::diagram
{
  "type": "table",
  "title": "The anatomy dictionary",
  "columns": ["Curve", "Distance law", "Parameter relation", "Latus rectum"],
  "rows": [
    ["Parabola", "PF = line distance", "a = focal length", "4a"],
    ["Ellipse", "sum = 2a", "c^2 = a^2 - b^2", "2b^2/a"],
    ["Hyperbola", "|difference| = 2a", "c^2 = a^2 + b^2", "2b^2/a"]
  ],
  "col_widths": [0.19, 0.29, 0.31, 0.21],
  "caption": "For both central conics c = ae and the directrices are x = +/- a/e. The parameter relation carries the crucial sign."
}
:::

:::example title="Recover an ellipse from focus–directrix data"
A point moves so that its distance from $(2,0)$ is $2/3$ of its distance from $x=9/2$. Thus $e=2/3<1$. Squaring gives
$$
(x-2)^2+y^2=\frac{4}{9}\left(x-\frac{9}{2}\right)^2
\quad\Longrightarrow\quad5x^2+9y^2=45.
$$
Hence the locus is $x^2/9+y^2/5=1$. As a check, $a=3$, $ae=2$, and $a/e=9/2$, exactly the supplied focus and directrix.
:::

:::warn title="Degeneracy is a separate question"
A second-degree equation can represent a point, a line, two lines, or no real points. The simple $e$-classification assumes a genuine nondegenerate conic with the focus off the directrix. Always check degenerate data explicitly rather than forcing it into a standard formula.
:::
