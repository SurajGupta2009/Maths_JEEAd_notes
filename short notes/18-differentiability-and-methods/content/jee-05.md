---
id: jee-05
part: jee
title: "Inverse Functions and Inverse Trigonometric Derivatives"
---

## The inverse-function rule is a reciprocal on the correct branch

If $y=f(x)$ has a local differentiable inverse and $f'(x)\ne0$, differentiating $f(f^{-1}(y))=y$ gives
$$
(f^{-1})'(y)=\frac{1}{f'(f^{-1}(y))}.
$$
The nonzero derivative ensures a nonvertical tangent for the inverse relation. Applying this to the principal trigonometric branches gives
$$
(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}\quad(|x|<1),
$$
$$
(\arccos x)'=-\frac{1}{\sqrt{1-x^2}}\quad(|x|<1),
\qquad
(\arctan x)'=\frac{1}{1+x^2}.
$$
Thus $(\arctan x)'|_{x=1}=1/2$, and for $|x|<1/2$,
$$
\frac{d}{dx}\arcsin(2x)=\frac{2}{\sqrt{1-4x^2}}.
$$

## Simplify first, but keep the principal branch visible

Where $1+\cos x\ne0$,
$$
\frac{\sin x}{1+\cos x}=\tan\frac{x}{2}.
$$
However, $\arctan(\tan u)=u$ only when $u\in(-\pi/2,\pi/2)$. Therefore
$$
\arctan\!\left(\frac{\sin x}{1+\cos x}\right)=\frac{x}{2}
\quad\text{only for }-\pi<x<\pi.
$$
On each interval $((2k-1)\pi,(2k+1)\pi)$, the simplified value is $x/2-k\pi$; the derivative is $1/2$ on every such interval.

:::diagram
{
  "type": "graph",
  "title": "arctan(tan(x/2)) repeats the principal branch",
  "xrange": [-9.5, 9.5], "yrange": [-2, 2],
  "xticks": [-9.42477796, -3.14159265, 0, 3.14159265, 9.42477796],
  "xticklabels": ["-3pi", "-pi", "0", "pi", "3pi"],
  "yticks": [-1.57079633, 0, 1.57079633], "yticklabels": ["-pi/2", "0", "pi/2"],
  "curves": [
    {"expr": "atan(tan(x/2))", "from": -9.20, "to": -3.25, "label": "x/2+pi", "labpos": 0.45, "label_dy": 0.18},
    {"expr": "atan(tan(x/2))", "from": -3.04, "to": 3.04, "label": "x/2", "labpos": 0.65, "label_dy": 0.18},
    {"expr": "atan(tan(x/2))", "from": 3.25, "to": 9.20, "label": "x/2-pi", "labpos": 0.45, "label_dy": 0.18}
  ],
  "vlines": [{"x": -3.14159265, "dx": -0.5}, {"x": 3.14159265, "dx": 0.5}],
  "points": [
    {"x": -3.14159265, "y": 1.57079633, "face": "white", "color": "#B91C1C"},
    {"x": -3.14159265, "y": -1.57079633, "face": "white", "color": "#B91C1C"},
    {"x": 3.14159265, "y": 1.57079633, "face": "white", "color": "#B91C1C"},
    {"x": 3.14159265, "y": -1.57079633, "face": "white", "color": "#B91C1C"}
  ],
  "caption": "Each branch has slope 1/2, but the intercept changes by pi. At odd multiples of pi the original denominator 1+cos(x) is zero, so no value or derivative is claimed there."
}
:::

:::warn title="A trigonometric identity does not erase inverse-branch jumps"
Replacing $\arctan(\tan(x/2))$ by $x/2$ everywhere would invent values at odd multiples of $\pi$ and remove the jumps between principal branches. State the interval before differentiating a simplified inverse-trigonometric expression.
:::
