---
id: jee-08
part: jee
title: Probability and Statistics — Mixed Strategy, Assumptions
---

## A workflow that prevents most errors

1. Define outcomes / variable / data convention.
2. State equally-likely, independence, replacement, or class-mark assumptions.
3. Choose count, conditional probability, Bayes, distribution, or descriptive statistic.
4. Compute exactly when possible; check range, units, and limiting cases.

:::example title="Two cards without replacement"
Probability both are aces: $(4/52)(3/51)=1/221$. The second conditional probability is $3/51$, not $4/52$; equivalently $\binom{4}{2}/\binom{52}{2}$.
:::

## Useful identities

For independent $X_i$: $E[\sum X_i]=\sum E[X_i]$ always; $\operatorname{Var}(\sum X_i)=\sum\operatorname{Var}(X_i)$ under independence. For Bernoulli indicators, $X=\sum I_i$ yields binomial mean and variance immediately.

:::key title="Range and sanity checks"
Probability lies in $[0,1]$; variance is nonnegative; SD has original units; mean lies between min and max. A grouped estimate cannot recover exact within-class data.
:::

## Official coverage and source gap

JEE Advanced includes probability plus descriptive statistics (mean, median, mode, mean deviation, variance and standard deviation for grouped/ungrouped data, and mean/variance of a random variable). The repository's Probability module covers probability deeply but does not provide a dedicated descriptive-statistics treatment; these statistics sheets are authored to the syllabus and standard definitions, with the class-mark approximation stated.

:::warn title="Not a sampling-statistics chapter"
The variance formula here uses divisor $N$ for a complete data set / probability distribution. The unbiased sample estimator with divisor $N-1$, confidence intervals, and hypothesis testing are outside this syllabus-oriented set.
:::
