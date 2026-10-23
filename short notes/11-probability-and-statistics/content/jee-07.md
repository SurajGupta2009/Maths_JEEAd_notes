---
id: jee-07
part: jee
title: Descriptive Statistics II — Spread & Grouping
---

## Population variance and standard deviation

For data $x_i$ with frequencies $f_i$, mean $\bar x$ and $N=\sum f_i$:
$$\sigma^2=\frac{\sum_i f_i(x_i-\bar x)^2}{N}=\frac{\sum_i f_ix_i^2}{N}-\bar x^2,\qquad \sigma=\sqrt{\sigma^2}.$$
This syllabus convention treats the listed data as the full distribution. Sample variance using divisor $N-1$ is a different inferential estimator; do not silently substitute it.

:::derive title="Computational identity"
Expand $\sum f_i(x_i-\bar x)^2=\sum f_ix_i^2-2\bar x\sum f_ix_i+N\bar x^2=\sum f_ix_i^2-N\bar x^2$.
:::

## Shift and coding shortcuts

Adding constant $c$ shifts mean and median by $c$, leaves variance/SD unchanged. Multiplying by $a$ scales mean by $a$, variance by $a^2$, SD by $|a|$. For equal class width $h$, coded values $u_i=(x_i-A)/h$ give $\sigma_x=h\sigma_u$.

:::example title="Frequency table"
Values $1,2,3$ with frequencies $1,2,1$: $N=4$, mean 2, mean square $= (1+8+9)/4=4.5$, variance $=0.5$, SD $=\sqrt{0.5}$.
:::

## Grouped continuous data

For classes $[a_i,b_i)$ with frequency $f_i$, class mark $m_i=(a_i+b_i)/2$ approximates every value in the class. Use $m_i$ in the frequency formulas for mean and variance. Median class is first cumulative frequency at least $N/2$; estimated median is $l+\frac{N/2-c_f}{f_m}h$. For a unique modal class in equal-width classes of width $h$, lower boundary $l$, modal-class frequency $f_1$ and adjacent frequencies $f_0,f_2$, the standard interpolation estimate is $\mathrm{Mode}=l+\frac{f_1-f_0}{2f_1-f_0-f_2}h$. These interpolations assume a reasonably smooth distribution within/around the relevant classes.

:::example title="Grouped table estimate"
Classes $[0,10),[10,20),[20,30)$ have frequencies $4,8,4$ ($N=16$). Midpoints $5,15,25$ give mean $15$, variance $50$, SD $\sqrt{50}$. The middle class has $l=10,c_f=4,f_m=8$, so grouped median estimate is $10+(8-4)10/8=15$. Its mode estimate is also 15 by symmetry ($f_0=f_2=4$). Mean deviation about 15 is $(4\cdot10+8\cdot0+4\cdot10)/16=5$. All are class-based estimates, not exact raw-data statistics.
:::

:::warn title="Unequal class widths"
For a histogram with unequal class widths, bar height is frequency density $f_i/\text{width}_i$, not raw frequency. The modal class is determined by density when comparing unequal-width histogram bars.
:::
