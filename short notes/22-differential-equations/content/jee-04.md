---
id: jee-04
part: jee
title: "Homogeneous First-Order Equations"
---

## Use the ratio, not the word homogeneous alone

Here homogeneous means $y'=F(y/x)$ on an interval not containing $x=0$. Put
$$
y=vx,\qquad y'=v+xv'.
$$
The $v$ terms often cancel, leaving a separable equation in $v$ and $x$. Return to $y=vx$ only after solving for $v$.

:::diagram
{
  "type": "flow",
  "title": "The substitution y = vx exposes the hidden separation",
  "steps": [
    {"title": "Recognize", "detail": "Confirm that the right-hand side depends only on y/x."},
    {"title": "Substitute", "detail": "Replace y by vx and y-prime by v plus x times v-prime."},
    {"title": "Solve", "detail": "Separate v and x; audit any equilibrium v before dividing."},
    {"title": "Restore", "detail": "Set v = y/x and impose the initial condition and interval."}
  ],
  "caption": "This meaning of homogeneous is different from a linear equation with zero right-hand side."
}
:::

:::example title="S5 and Q9: immediate cancellation"
For $y'=(x+y)/x=1+y/x$,
$$
v+xv'=1+v
\quad\Longrightarrow\quad xv'=1.
$$
Thus $v=\ln|x|+C$. With $y(1)=0$, $v(1)=0$ and $C=0$; on $x>0$,
$$
{y=x\ln x},\qquad {y(e)=e}.
$$
The maximal IVP interval is $(0,\infty)$ because the original equation contains $1/x$.
:::

:::example title="P5 and Q10: a finite blow-up boundary"
For $y'=y/x+(y/x)^2$,
$$
xv'=v^2
\quad\Longrightarrow\quad
-\frac{1}{v}=\ln|x|+C
$$
on a nonzero-$v$ branch. The condition $y(1)=1$ gives $v(1)=1$ and $C=-1$. Therefore
$$
{y=\frac{x}{1-\ln x}},\qquad
{y(2)=\frac{2}{1-\ln2}}.
$$
Starting at $x=1$, the maximal interval is $(0,e)$: the denominator vanishes at $x=e$, while $x=0$ is forbidden.
:::

:::example title="Q11: the radicand determines the lower endpoint"
For $y'=(x^2+y^2)/(xy)=x/y+y/x$,
$$
v+xv'=v+\frac{1}{v}
\quad\Longrightarrow\quad v\,dv=\frac{dx}{x}.
$$
Hence $v^2=2\ln|x|+C$. Since $v(1)=1$, $C=1$, and the positive branch on $x>0$ is
$$
{y=x\sqrt{2\ln x+1}},\qquad {y(e)=e\sqrt{3}}.
$$
The IVP interval is $(e^{-1/2},\infty)$; at its lower endpoint both the radicand and $y$ reach zero, so the original denominator $xy$ fails.
:::

:::warn title="Never discard v = 0 without checking it"
If separation divides by $v$, the constant ratio $v=0$ may give $y=0$ as an additional solution of the general equation. It does not affect the three nonzero IVPs above, but it matters when listing all branches.
:::
