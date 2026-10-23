---
id: jee-02
part: jee
title: "The Straight Line — Slope and Equations"
---

## Slope measures rise per run

For distinct points $A(x_1,y_1),B(x_2,y_2)$ with $x_2\ne x_1$,
$$m=\frac{y_2-y_1}{x_2-x_1}.$$
A vertical line has no finite slope; a horizontal line has slope $0$. Slope is unchanged by translation or by choosing a different pair of points on the same line.

:::example title="Build one line in several forms"
Through $(2,-1)$ with slope $3$: $y+1=3(x-2)$, hence $3x-y-7=0$. Its slope-intercept form is $y=3x-7$.
:::

## A line has several useful forms

| Form | Equation / use |
|---|---|
| Point–slope | $y-y_1=m(x-x_1)$; requires nonvertical line |
| Two-point | $(y-y_1)(x_2-x_1)=(y_2-y_1)(x-x_1)$; works when points differ |
| Slope–intercept | $y=mx+c$; misses vertical lines |
| Intercept | $x/a+y/b=1$; requires both intercepts nonzero |
| General | $ax+by+c=0$, $(a,b)\ne(0,0)$ |
| Normal | $x\cos\alpha+y\sin\alpha=p$; signed perpendicular distance $p$ from the origin |

In $ax+by+c=0$, $(a,b)$ is a normal vector and a direction vector is $(-b,a)$. If $b\ne0$, slope is $-a/b$; if $b=0$, the line is vertical.

:::derive title="Normal form from a perpendicular projection"
A point $X=(x,y)$ lies on a line at signed distance $p$ from the origin with unit normal $n=(\cos\alpha,\sin\alpha)$ exactly when its projection onto $n$ is $p$: $X\cdot n=p$. Thus $x\cos\alpha+y\sin\alpha=p$. Keeping $p$ signed avoids changing the line when the normal is reversed.
:::

:::example title="Vertical lines are not exceptional in general form"
The vertical line through $(4,-2)$ is $x=4$, or $x-4=0$. It has no slope-intercept form, but it is fully represented by $ax+by+c=0$.
:::

:::warn title="Intercept-form trap"
$x/a+y/b=1$ presumes $a,b\ne0$. A line through the origin has zero intercepts and should be written in point-slope or general form instead.
:::
