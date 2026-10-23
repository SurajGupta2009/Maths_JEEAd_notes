---
id: jee-04
part: jee
title: Random Variables — Mean and Variance
---

## A random variable turns outcomes into numbers

Discrete $X$ has pmf $p(x)=P(X=x)$, with $p(x)\geq0$ and $\sum_xp(x)=1$. For finite support:
$$E[X]=\sum_x xp(x),\qquad E[X^2]=\sum_xx^2p(x)$$

$$\operatorname{Var}(X)=E[X^2]-(E[X])^2.$$
Standard deviation $\sigma=\sqrt{\operatorname{Var}(X)}$ has the original units; variance has squared units.

:::derive title="Variance as spread about the mean"
Expand $E[(X-\mu)^2]$ with $\mu=E[X]$: $E[X^2]-2\mu E[X]+\mu^2=E[X^2]-\mu^2$. Variance is nonnegative and is zero exactly when $X$ is constant with probability 1.
:::

## Linear changes and indicators

$E[aX+b]=aE[X]+b$; $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$. For indicator $I_A$, $E[I_A]=P(A)$ and $\operatorname{Var}(I_A)=p(1-p)$.

:::example title="Three-point distribution"
If $X=1,2,3$ with probabilities $0.2,0.3,0.5$, then $E[X]=2.3$, $E[X^2]=5.9$, variance $=5.9-2.3^2=0.61$, SD $\approx0.781$.
:::

:::warn title="Variance of a sum"
In general $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y)$. The two-variance shortcut needs zero covariance (independence suffices); expectation linearity needs no independence.
:::
