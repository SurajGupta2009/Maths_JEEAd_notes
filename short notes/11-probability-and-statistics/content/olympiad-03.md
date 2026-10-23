---
id: olympiad-03
part: olympiad
title: Gambler's Ruin, Derangements, Averaging
---

## Gambler's ruin

Fortune starts at $i$ units, absorbing barriers $0,N$, and each unit bet wins with probability $p$, loses with $q=1-p$. Success probability solves $u_i=pu_{i+1}+qu_{i-1}$, $u_0=0,u_N=1$:
$$u_i=\frac{1-(q/p)^i}{1-(q/p)^N}\quad(p\ne q),\qquad u_i=i/N\quad(p=q=1/2).$$

:::intuition title="Fair fortune is a martingale"
Expected final fortune equals initial fortune $i$; final fortune is $N$ with probability $u_i$ and zero otherwise, so $Nu_i=i$.
:::

## Derangements by inclusion–exclusion

For $n$ objects assigned uniformly to $n$ positions, probability none fixed is
$$\sum_{k=0}^{n}\frac{(-1)^k}{k!},$$
so $D_n=n!\sum_{k=0}^{n}(-1)^k/k!$ and it tends to $1/e$. At $n=5$, $D_5=44$ and probability $11/30$.

:::example title="Biased walk, exact value"
Take $p=3/5$, $q/p=2/3$, barriers 0 and 10, start $i=5$. Then $u_5=[1-(2/3)^5]/[1-(2/3)^{10}]\approx0.88364$. The edge makes success more likely than 1/2; the boundary conditions still matter.
:::

:::warn title="Do not overgeneralize optional stopping"
The elementary fair-ruin argument is safe for finite barriers and the process stopped at absorption. General martingale stopping claims require hypotheses; do not invoke an unrestricted optional-stopping theorem.
:::

## Derangement proof and a small check

Let $A_i$ be the event that object $i$ is fixed. Inclusion–exclusion gives $D_n=\sum_{j=0}^n(-1)^j\binom{n}{j}(n-j)!=n!\sum_{j=0}^n\frac{(-1)^j}{j!}$.  For $n=3$, this is $6-9+2=2$; probability $1/3$. For $n=5$, $D_5=44$, probability $11/30$. The limit $1/e$ is approached with alternating partial-sum error bounded by the next reciprocal factorial.

## Why averaging helps

For a random variable $X$, $E[X]=\sum_iE[I_i]$ when $X=\sum_i I_i$, regardless of dependence. This linearity powers coupon-collector stage sums and indicator proofs of expected collision counts. Variance does not share this unrestricted additivity.


## What these extensions teach

The same ideas recur: complement for rare collisions, inclusion–exclusion for forbidden fixed points, state recursions for sequential games, and expectation decomposed into stages. These models add methods; they are not explicit JEE syllabus promises.
