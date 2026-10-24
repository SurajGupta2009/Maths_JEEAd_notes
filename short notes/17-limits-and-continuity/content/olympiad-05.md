---
id: olympiad-05
part: olympiad
title: "Extension V — Functional Equations and IVT"
---

## Build a function whose endpoint signs are forced to oppose

Suppose $f$ is continuous on $[0,1]$ and $f(0)=f(1)$. Define
$$
g(x)=f(x)-f\!\left(x+\frac{1}{2}\right),\qquad 0\leq x\leq\frac{1}{2}.
$$
Then
$$
g\left(\frac{1}{2}\right)=f\left(\frac{1}{2}\right)-f(1)
=f\left(\frac{1}{2}\right)-f(0)=-g(0).
$$
If $g(0)=0$, take $c=0$. Otherwise IVT gives $c\in(0,1/2)$ with $g(c)=0$. Hence
$$
f(c)=f\!\left(c+\frac{1}{2}\right).
$$

:::example title="An exact half-shift check"
For $f(x)=(x-1/2)^2$, we have $f(0)=f(1)=1/4$ and
$$
g(x)=\left(x-\frac{1}{2}\right)^2-x^2=\frac{1}{4}-x.
$$
Thus $c=1/4$, and indeed $f(1/4)=f(3/4)=1/16$. The same antipodal-difference idea applied to continuous temperature $T$ on a circle gives at least one pair of antipodal points with equal temperature.
:::

## Continuity extends rational information to all reals

An additive function satisfies $f(x+y)=f(x)+f(y)$. Induction and scaling give
$$
f(qx)=qf(x)\qquad(q\in\mathbb{Q}).
$$
If $f$ is continuous and $a=f(1)$, then for any real $x$, choose rationals $q_k\to x$. Continuity gives
$$
f(x)=\lim_{k\to\infty}f(q_k)=\lim_{k\to\infty}aq_k=ax.
$$
Without continuity, additivity alone permits pathological solutions.

For the Jensen midpoint relation
$$
f\!\left(\frac{x+y}{2}\right)=\frac{f(x)+f(y)}{2},
$$
subtract $b=f(0)$. The function $g=f-b$ has the same midpoint property and $g(0)=0$. It follows that $g$ is additive, so continuity at one point gives $g(x)=ax$ and therefore $f(x)=ax+b$.

:::example title="The continuous exponential functional equation"
Suppose $f$ is continuous, $f(x+y)=f(x)f(y)$, and $f(1)=a>0$. First, $f(0)=1$: the alternative $f(0)=0$ would force $f\equiv0$, contradicting $f(1)>0$. Also $f(x)=f(x/2)^2\geq0$, and a zero value anywhere would force $f(1)=0$, so $f$ is strictly positive.

The functional equation gives $f(q)=a^q$ for every rational $q$. Rational density and continuity then extend this to
$$
f(x)=a^x\qquad(x\in\mathbb{R}).
$$
:::

:::diagram
{
  "type": "flow",
  "title": "Continuity turns local or discrete information into a global conclusion",
  "steps": [
    {"title": "Build the auxiliary object", "detail": "Use a difference for IVT; subtract f(0) to normalize."},
    {"title": "Extract signs or rational values", "detail": "Find opposite signs or values on the rationals."},
    {"title": "Apply the continuity hypothesis", "detail": "Use IVT on an interval or continuity through rationals."},
    {"title": "Verify the final form", "detail": "Substitute back; check sign, domain and endpoints."}
  ],
  "caption": "The algebra produces candidates; continuity is what makes the limiting or density argument legitimate."
}
:::

:::key title="Do not overstate antipodal conclusions"
The argument guarantees **at least one** antipodal pair with equal values, not that every attained value occurs at antipodal pairs. Likewise, IVT guarantees a point with a required value, while a separate argument is needed for uniqueness or a formula for that point.
:::
