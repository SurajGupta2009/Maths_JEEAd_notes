---
id: jee-06
part: jee
title: Descriptive Statistics I — Centre & Deviation
---

## Data and frequency notation

Observations $x_i$ with frequencies $f_i$; total $N=\sum f_i$. For ungrouped data, frequencies may all equal 1. Arithmetic mean:
$$\bar x=\frac{\sum_i f_ix_i}{N}.$$
It is the balance point and minimizes the sum of squared deviations, not the sum of absolute deviations.

## Median and mode

Sort the $N$ observations. For odd $N$, median is position $(N+1)/2$; for even $N$, average of positions $N/2$ and $N/2+1$. Mode is the most frequent value; multiple modes are possible.

:::example title="Five observations"
Data $2,3,3,7,10$: mean $=25/5=5$, median $=3$, mode $=3$. Outlier 10 pulls the mean more than the median.
:::

For a discrete frequency table, locate the middle cumulative-frequency positions. For continuous grouped classes of common width $h$, let $l$ be the lower boundary of the median class, $c_f$ cumulative frequency before it, and $f$ its frequency. Linear interpolation gives $\mathrm{Median}=l+\frac{N/2-c_f}{f}h$. This estimates a grouped distribution, not the unknowable exact raw median.

## Mean deviation

Mean deviation about a reference $a$ is the average absolute distance:
$$MD_a=\frac{\sum_i f_i|x_i-a|}{N}.$$
Often asked about the mean or median; specify the centre. Absolute values prevent positive/negative deviations cancelling.

:::warn title="Use absolute values"
$\sum f_i(x_i-\bar x)=0$ by construction, so the signed mean deviation is not a spread measure. Use $|x_i-a|$.
:::

:::key title="Grouped continuous classes"
Use class marks $x_i=(\text{lower boundary}+\text{upper boundary})/2$ as representative observations for mean/variance estimates. Results are estimates because original within-class positions are unknown.
:::
