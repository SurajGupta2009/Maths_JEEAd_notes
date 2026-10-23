---
id: jee-05
part: jee
title: Binomial and Geometric Models
---

## Binomial: fixed independent trials

$n$ independent Bernoulli trials, each success chance $p$, $q=1-p$. Number of successes $X$ has
$$P(X=k)=\binom{n}{k}p^kq^{n-k},\quad k=0,1,\ldots,n$$

$$E[X]=np,\qquad \operatorname{Var}(X)=npq.$$
The choose factor selects which $k$ trials succeed; each such pattern has probability $p^kq^{n-k}$.

:::example title="Exactly three successes"
For 10 independent trials with $p=0.2$, $P(X=3)=\binom{10}{3}(0.2)^3(0.8)^7\approx0.201327$. “At least” can be summed or complemented.
:::

:::warn title="Model conditions"
Fixed number of trials, two outcomes per trial, constant success probability, and independence. Without-replacement sampling is generally hypergeometric, not binomial.
:::

## Geometric waiting time

Let $X$ count trials up to and including first success, $0<p\leq1$. Then $P(X=k)=q^{k-1}p$ for $k\geq1$, $E[X]=1/p$, $\operatorname{Var}(X)=q/p^2$. If instead counting failures before success, support begins at 0: state the convention.

:::intuition title="Why the mean is reciprocal"
The tail probabilities are $P(X\geq k)=q^{k-1}$. Their sum is $E[X]=1+q+q^2+\cdots=1/(1-q)=1/p$.
:::

A geometric waiting time is memoryless: $P(X>m+n\mid X>m)=P(X>n)$ for nonnegative integers $m,n$.
