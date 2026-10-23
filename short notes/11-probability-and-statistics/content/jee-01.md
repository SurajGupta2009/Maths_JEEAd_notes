---
id: jee-01
part: jee
title: Probability Foundations — Spaces, Events, Complements
---

## Sample space first

An experiment has sample space $S$ of possible outcomes; an event is a subset of $S$. Classical $P(E)=|E|/|S|$ is valid only if the chosen outcomes are equally likely. Two fair dice use 36 equally likely ordered pairs, not 21 equally likely unordered pairs.

:::intuition title="Probability is a normalized count"
For equally likely finite outcomes, probability is a fraction of the whole sample space. For unequal outcomes, weight them by their probabilities instead of counting them uniformly.
:::

Axioms: $P(S)=1$, $P(E)\geq0$, and disjoint events add. Hence $P(\varnothing)=0$, $0\leq P(E)\leq1$, and if $E\subseteq F$, then $P(E)\leq P(F)$.

## Complement principle

$$P(E^c)=1-P(E).$$
For “at least one”, the complement “none” often has fewer cases. For $n$ independent trials, success chance $p$:
$$P(\text{at least one success})=1-(1-p)^n.$$

:::example title="Two dice"
Sum 7 has six ordered outcomes among 36: probability $1/6$. Writing the ordered space avoids weighting errors: unordered pair {1,6} has twice the probability of {1,1}.
:::

## Equally likely versus independent

Equally likely is a property of outcomes in a model; independence is a relation between events. Independent events satisfy $P(A\cap B)=P(A)P(B)$. Neither notion implies the other.

:::warn title="Sample-space checklist"
State what is selected, whether order matters, replacement rules, and why outcomes have equal weight. “Favourable over total” without those assumptions is not a probability argument.
:::
