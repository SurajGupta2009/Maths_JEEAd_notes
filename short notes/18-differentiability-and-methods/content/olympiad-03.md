---
id: olympiad-03
part: olympiad
title: "Extension III — Functional Equations by Differentiation"
---

## First exclude degenerate solutions, then differentiate

Suppose a differentiable $f:\mathbb{R}\to\mathbb{R}$ satisfies
$$
f(x+y)=f(x)f(y)
$$
and $f$ is not identically zero. Since $f(0)=f(0)^2$, $f(0)$ is $0$ or $1$. If $f(0)=0$, then $f(x)=f(x)f(0)=0$ for every $x$, which is excluded. Hence $f(0)=1$.

Also $f(x)=f(x/2)^2\geq0$. If $f(a)=0$ for some $a$, then $f(x)=f(a)f(x-a)=0$ for every $x$, again impossible. Thus $f>0$ everywhere.

Differentiate the functional equation with respect to $y$ and set $y=0$:
$$
f'(x+y)=f(x)f'(y)
\quad\Longrightarrow\quad
f'(x)=cf(x),\qquad c=f'(0).
$$
Now $g(x)=e^{-cx}f(x)$ has derivative $e^{-cx}(f'-cf)=0$. The zero-derivative theorem, justified in Extension V, gives $g(x)=g(0)=1$. Therefore
$$
f(x)=e^{cx},
$$
and direct substitution verifies every such function.

## A product argument produces logarithms

Suppose instead that $f:(0,\infty)\to\mathbb{R}$ is differentiable and
$$
f(xy)=f(x)+f(y).
$$
Putting $x=y=1$ gives $f(1)=0$. Differentiate with respect to $y$:
$$
x f'(xy)=f'(y).
$$
Set $y=1$ and $a=f'(1)$ to obtain $xf'(x)=a$, hence $f'(x)=a/x$. Since $f(x)-a\ln x$ has zero derivative and vanishes at $1$,
$$
f(x)=a\ln x\qquad(x>0).
$$
Again, substitution verifies the whole family.

## An additive equation has constant derivative

If a differentiable $f:\mathbb{R}\to\mathbb{R}$ satisfies
$$
f(x+y)=f(x)+f(y),
$$
then $f(0)=2f(0)$, so $f(0)=0$. Differentiate with respect to $y$ and set $y=0$:
$$
f'(x+y)=f'(y)
\quad\Longrightarrow\quad
f'(x)=f'(0)=a.
$$
Thus $f(x)-ax$ has zero derivative and vanishes at $0$, giving $f(x)=ax$. For the source value $a=f'(0)=3$, the answer is $f(x)=3x$. Differentiability is what rules out nonregular additive solutions.

:::diagram
{
  "type": "flow",
  "title": "Differentiation converts functional equations into rate equations",
  "steps": [
    {"title": "Normalize and exclude degeneracy", "detail": "Find f(0) or f(1); remove the identically zero case."},
    {"title": "Differentiate in one variable", "detail": "Hold the other variable fixed and apply the chain rule."},
    {"title": "Specialize the free variable", "detail": "Set y=0 or y=1 to expose a constant rate."},
    {"title": "Solve and substitute back", "detail": "Use zero derivative or a limiting argument, then verify globally."}
  ],
  "caption": "The exponential case excludes zero before solving; the product-argument case is defined only on positive reals. Additive equations need no logarithm."
}
:::

:::warn title="Differentiability is an essential hypothesis"
Without regularity, additive and related functional equations can admit pathological solutions. Differentiation cannot be applied merely because an algebraic relation looks familiar.
:::
