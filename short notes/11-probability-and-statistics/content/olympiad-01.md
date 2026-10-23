---
id: olympiad-01
part: olympiad
title: Geometric Probability, Ballot, Birthday
---

## Continuous sample spaces

Uniformly chosen points in a region: probability is favourable area / total area, provided the joint distribution is uniform in the stated coordinates. Coordinate choice and sampling procedure matter.

:::example title="Broken stick"
Two independent uniform break points on a unit stick make three pieces. Triangle condition is that no piece is at least $1/2$. The region of valid break-point pairs has one quarter the total area, so probability $1/4$.
:::

## Bertrand ballot theorem

If $a>b$ votes are randomly ordered, the probability A is strictly ahead after every vote is $(a-b)/(a+b)$. Reflection of paths at their first diagonal contact counts the bad orderings. Strictly ahead excludes ties after the first vote.

## Birthday collision

With $d$ equally likely birthdays, independent and ignoring leap day, probability of no match among $n\leq d$ people is $\prod_{j=0}^{n-1}(d-j)/d$; collision probability is one minus this. For $d=365,n=23$, about $0.5073$.

:::warn title="Model assumptions matter"
Uniform birthdays, independence, and a 365-day year are approximations. The answer is conditional on this idealised model, not a statement about real populations.
:::
