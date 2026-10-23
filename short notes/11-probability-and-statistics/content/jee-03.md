---
id: jee-03
part: jee
title: Independence, Total Probability, Bayes
---

## Independence is factorisation

Events $A,B$ are independent iff $P(A\cap B)=P(A)P(B)$; equivalently, if $P(B)>0$, $P(A\mid B)=P(A)$. Pairwise independence of three events does not guarantee mutual independence.

:::warn title="Exclusive is not independent"
If $A,B$ are disjoint and both have positive probability, $P(A\cap B)=0$ but $P(A)P(B)>0$, so they are dependent.
:::

## Partition into causes

If $B_1,\ldots,B_n$ are disjoint and cover $S$, then
$$P(A)=\sum_i P(A\mid B_i)P(B_i).$$
The partition must be exhaustive and its branches disjoint.

## Bayes reverses the tree

$$P(B_i\mid A)=\frac{P(A\mid B_i)P(B_i)}{\sum_jP(A\mid B_j)P(B_j)}.$$
Numerator = prior × likelihood; denominator = total probability of observed evidence.

:::example title="Factory defect"
Machines A,B,C make 50%,30%,20%, with defect rates 1%,2%,3%. Overall defect chance is $0.5(0.01)+0.3(0.02)+0.2(0.03)=0.017$. Given defective, source A probability is $0.005/0.017=5/17$.
:::

:::warn title="Base-rate trap"
Sensitivity $P(+\mid D)$ is not the posterior $P(D\mid +)$. The latter depends on prevalence and false-positive rate through Bayes' denominator.
:::
