---
id: jee-06
part: jee
title: "Hyperbola — Branches, Asymptotes and Conjugate"
---

## A constant absolute difference gives two branches

For foci $(\pm c,0)$ and $c>a$, the condition $|PF_1-PF_2|=2a$ gives
$$
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1,
\qquad b^2=c^2-a^2.
$$
The vertices are $(\pm a,0)$, foci $(\pm ae,0)$, $e=c/a>1$, directrices $x=\pm a/e$, and latus rectum length $2b^2/a$. On the right branch, the near/right and far/left focal distances are $ex-a$ and $ex+a$; mirror the signs on the left branch.

:::warn title="The absolute value matters"
A fixed signed difference selects only one branch. The full hyperbola uses the absolute difference. Also $b^2=c^2-a^2$, not $a^2-c^2$: now $c>a$, so the foci lie outside the vertices.
:::

## Asymptotes are the straight skeleton

Dividing the equation far from the centre shows that the curve approaches
$$
y=\pm\frac{b}{a}x.
$$
These lines are not tangents at finite points. If $2\alpha$ is the asymptote angle around the transverse axis, then $\tan\alpha=b/a$ and
$$
\cos(2\alpha)=\frac{2}{e^2}-1.
$$
A rectangular hyperbola has perpendicular asymptotes, equivalently $a=b$ and $e=\sqrt{2}$ in horizontal standard form.

:::diagram
{
  "type": "geometry",
  "label_fontsize": 10,
  "title": "The 3-4-5 hyperbola and its asymptotes",
  "xrange": [-7.5, 7.5], "yrange": [-7, 7], "grid": true,
  "elements": [
    {"kind": "hyperbola", "a": 3, "b": 4, "umax": 0.95, "color": "#0F766E"},
    {"kind": "line", "a": [-5.25, -7], "b": [5.25, 7], "color": "#5B6B84"},
    {"kind": "line", "a": [-5.25, 7], "b": [5.25, -7], "color": "#5B6B84"},
    {"kind": "point", "at": [3, 0], "label": "(3,0)", "dx": 0.15, "dy": 0.25},
    {"kind": "point", "at": [-3, 0], "label": "(-3,0)", "dx": -1.5, "dy": 0.25},
    {"kind": "point", "at": [5, 0], "label": "F(5,0)", "dx": 0.15, "dy": -0.55, "color": "#B8860B"},
    {"kind": "point", "at": [-5, 0], "label": "F(-5,0)", "dx": -1.25, "dy": -0.55, "color": "#B8860B"},
    {"kind": "text", "at": [-2.8, -5.8], "text": "asymptotes: y = +/- 4x/3", "color": "#5B6B84"}
  ],
  "caption": "The latus rectum is 2b^2/a = 32/3. The directrices lie between the centre and vertices, while the foci lie outside them."
}
:::

:::example title="From a distance difference to the full anatomy"
Suppose the absolute difference of distances from $(\pm5,0)$ is $6$. Then $2a=6$, so $a=3$, and $c=5$. Hence $b^2=25-9=16$ and
$$
\frac{x^2}{9}-\frac{y^2}{16}=1,
\qquad e=\frac{5}{3},
\qquad x=\pm\frac{9}{5}
$$
are the hyperbola, eccentricity and directrices. Its asymptotes are $y=\pm4x/3$.
:::

## The conjugate shares asymptotes but swaps axes

The conjugate of $x^2/a^2-y^2/b^2=1$ is
$$
\frac{y^2}{b^2}-\frac{x^2}{a^2}=1.
$$
Both have the same asymptotes and $c^2=a^2+b^2$. If their eccentricities are $e=c/a$ and $e'=c/b$, then
$$
\frac{1}{e^2}+\frac{1}{(e')^2}=1.
$$
For $a=3,b=4$, this reads $e=5/3$, $e'=5/4$, and $9/25+16/25=1$.

## Hyperbola focal chords need branch care

For a **same-branch** focal chord with the focus between its endpoints, the unsigned lengths $u,v$ satisfy
$$
\frac{1}{u}+\frac{1}{v}=\frac{2a}{b^2}.
$$
For the right focus, write $\ell=b^2/a$. If the two focal radii make opposite angles with the axis, then $u=\ell/(1-e\cos\theta)$ and $v=\ell/(1+e\cos\theta)$ in the same-branch case, giving the result. This is not a licence to use the formula for a chord joining opposite branches.

:::example title="A same-branch check and an opposite-branch warning"
For $x^2/9-y^2/16=1$, the right focus is $(5,0)$. The vertical same-branch focal chord has endpoints $(5,\pm16/3)$, so $u=v=16/3$ and
$$
\frac{1}{u}+\frac{1}{v}=\frac{3}{8}=\frac{2a}{b^2}.
$$
In contrast, the transverse-axis chord joins $(-3,0)$ and $(3,0)$. Its focal segments are $8$ and $2$, whose reciprocal sum is $5/8=2c/b^2$, not $3/8$. Branch inspection changes the formula.
:::

:::key title="Use position signs with geometric interpretation"
For $S=x^2/a^2-y^2/b^2-1$, $S_1>0$ marks the regions containing the two branches, while $S_1<0$ marks the region between them. Unlike an ellipse, the plane is not simply described as one inside and one outside region.
:::
