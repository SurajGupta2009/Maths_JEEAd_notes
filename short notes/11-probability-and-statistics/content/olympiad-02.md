---
id: olympiad-02
part: olympiad
title: Recursions, Memorylessness, Coupon Collector
---

## Build state equations

For a process with finite memory, let $p_s$ be the desired probability from state $s$. Condition on the next move: $p_s=\sum_t P(s\to t)p_t$, using boundary values for winning/losing states. For expectations, add one unit of cost per step: $E_s=1+\sum_tP(s\to t)E_t$.

:::example title="Alternating first-head game"
Fair coin; players alternate, first head wins. Let $p$ be first player's win chance. She wins now with $1/2$ or both tosses fail with $1/4$ and state resets: $p=1/2+p/4$, hence $p=2/3$.
:::

## Coupon collector

For $n$ equally likely types, when $j$ distinct types are collected the next-new-type chance is $(n-j)/n$. Summing geometric stage means gives
$$E[T]=n\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)=nH_n.$$

## Memorylessness and runs

Geometric waiting time: $P(X>m+n\mid X>m)=P(X>n)$. There is no “due” effect. Expected tosses to obtain $r$ consecutive heads obey a run-state recurrence; for a fair coin it is $2^{r+1}-2$.
