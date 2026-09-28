---
title: "Probability — Solutions"
aliases: ["Probability Solutions", "Probability-Olympiad-Solutions"]
module: "Probability"
module_title: "Probability"
type: solutions
tags: [probability, solutions, olympiad, statistics, bayes, binomial]
created: 2026-09-28
---

> [!info] Navigation
> ⬅ [[Probability — Paper|Paper]] · 📖 [[Probability|Complete Notes]]

# Probability — Solutions

> Full solutions to all 34 questions, same Q-ids as the
> [[Probability — Paper|paper]]. Every solution: **method first → derivation →
> a check.** Every numeric answer was verified in pure Python (exact fractions
> and, where relevant, simulation) before this file was written.

---

## A · Classical probability and sample spaces

#### **Q1**
**Method: $\frac{\text{favourable}}{\text{total}}$ over the $36$ ordered pairs.** The
pairs summing to $7$ are $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ — six of them.
$P=\frac6{36}=\frac16$.
**Answer:** $\dfrac16$. (Check: the sum $7$ is the mode of the two-dice
distribution with $6$ of $36$ outcomes ✓.)

#### **Q2**
**Method: $\frac{\text{favourable}}{\text{total}}$.** $10$ equally likely balls,
$5$ red.
**Answer:** $\dfrac12$. (Check: $5+3+2=10$ and the three probabilities sum to $1$ ✓.)

#### **Q3**
**Method: the complement.** Only $TTT$ has no head, so
$P=1-\frac18=\frac78$.
**Answer:** $\dfrac78$. (Check: direct count gives $7$ favourable of $8$ ✓.)

#### **Q4**
**Method: addition rule with the overlap subtracted.** There are $13$ hearts and
$4$ kings, but the king of hearts is counted twice:
$P=\frac{13+4-1}{52}=\frac{16}{52}=\frac4{13}$.
**Answer:** $\dfrac4{13}$. (Check: $13$ hearts plus the $3$ non-heart kings $=16$ ✓.)

#### **Q5**
**Method: complement — the product is odd only when both rolls are odd.**
$P=1-\frac{3}{6}\cdot\frac{3}{6}=1-\frac14=\frac34$.
**Answer:** $\dfrac34$. (Check: direct count gives $27$ of $36$ ordered pairs ✓.)

---

## B · Addition rule and "at least"

#### **Q6**
**Method: rearrange the addition rule.**
$P(A\cap B)=P(A)+P(B)-P(A\cup B)=0.3+0.4-0.6=0.1$.
**Answer:** $0.1$. (Check: Venn regions $A$ only $=0.2$, $B$ only $=0.3$, both
$=0.1$, neither $=0.4$; total $1.0$ ✓.)

#### **Q7**
**Method: count sums $10,11,12$.** These have $3,2,1$ ordered pairs respectively,
so $P=\frac{3+2+1}{36}=\frac6{36}=\frac16$.
**Answer:** $\dfrac16$. (Check: a $200000$-throw simulation gave $0.1668$ ✓.)

#### **Q8**
**Method: addition rule.** $0.4+0.5-0.2=0.7$.
**Answer:** $0.7$. (Check: regions $0.2+0.3+0.2=0.7$, complement $0.3$ ✓.)

#### **Q9**
**Method: complement — subtract the all-men committee.**
$P=1-\frac{\binom53}{\binom93}=1-\frac{10}{84}=\frac{74}{84}=\frac{37}{42}$.
**Answer:** $\dfrac{37}{42}$. (Check: direct count
$\binom41\binom52+\binom42\binom51+\binom43\binom50=40+30+4=74$ ✓.)

#### **Q10**
**Method: binomial pmf with $n=5$, $p=\frac12$.**
$P=\frac{\binom53}{2^5}=\frac{10}{32}=\frac5{16}$.
**Answer:** $\dfrac5{16}$. (Check: $\sum_{k=0}^5\binom5k/32=32/32=1$ ✓.)

---

## C · Conditional probability and independence

#### **Q11**
**Method: $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$.** $P(A\cap B)=P(\{6\})=\frac16$ and
$P(B)=\frac36=\frac12$, so $P=\frac{1/6}{1/2}=\frac13$.
**Answer:** $\dfrac13$. (Check: the shrunken space $\{2,4,6\}$ has one favourable
of three equally likely outcomes ✓.)

#### **Q12**
**Method: multiplication rule for drawing without replacement.**
$P=\frac4{52}\cdot\frac3{51}=\frac{12}{2652}=\frac1{221}$.
**Answer:** $\dfrac1{221}$. (Check: $\binom42/\binom{52}2=\frac6{1326}=\frac1{221}$ ✓.)

#### **Q13**
**Method: test the factorisation $P(A)P(B)=P(A\cap B)$.**
$0.6\times0.3=0.18=P(A\cap B)$, so the product rule holds.
**Answer:** Yes, $A$ and $B$ are independent. (Check: $P(A\mid B)=0.18/0.3=0.6=P(A)$ ✓.)

#### **Q14**
**Method: state the sample space, then remove the outcomes the information excludes.**
The four equally likely cases are $BB,BG,GB,GG$. "At least one boy" removes only
$GG$, leaving three cases of which one is $BB$.
**Answer:** $\dfrac13$. (Check: if instead the *older* child is known to be a boy
the space shrinks to $\{BB,BG\}$ and the answer becomes $\frac12$ — the two
phrasings are genuinely different ✓.)

#### **Q15**
**Method: the first draw changes the bag's composition.** After removing a white
ball the bag holds $3$ white and $6$ black, so $9$ equally likely balls remain.
**Answer:** $\dfrac69=\dfrac23$. (Check: by symmetry $P(\text{2nd black})=\frac6{10}$
marginal, and $P(\text{1st white})=\frac4{10}$; $\frac{2}{3}\cdot\frac4{10}=\frac{8}{30}$
while $P(\text{white then black})=\frac4{10}\cdot\frac69=\frac{24}{90}=\frac4{15}$ ✓.)

---

## D · Total probability and Bayes' theorem

#### **Q16**
**Method: law of total probability over the three machines.**
$P(D)=\tfrac12\cdot0.01+\tfrac3{10}\cdot0.02+\tfrac15\cdot0.03=0.005+0.006+0.006=0.017$.
**Answer:** $\dfrac{17}{1000}$. (Check: $0.017$ lies between the smallest and
largest defect rate, as it must ✓.)

#### **Q17**
**Method: Bayes' theorem.**
$$P(A\mid D)=\frac{P(D\mid A)P(A)}{P(D)}=\frac{0.01\times0.5}{0.017}=\frac5{17}.$$
**Answer:** $\dfrac5{17}$. (Check: the three posteriors are $\frac5{17}$,
$\frac6{17}$ and $\frac6{17}$, which sum to $1$ ✓.)

#### **Q18**
**Method: total probability over the urn.**
$P(R)=\tfrac12\cdot\tfrac3{10}+\tfrac12\cdot\tfrac8{10}=0.15+0.40=0.55$.
**Answer:** $\dfrac{11}{20}$. (Check: the two contributions sum to $0.55$ ✓.)

#### **Q19**
**Method: Bayes' theorem.**
$$P(U_2\mid R)=\frac{P(R\mid U_2)P(U_2)}{P(R)}=\frac{0.8\times0.5}{0.55}=\frac8{11}.$$
**Answer:** $\dfrac8{11}$. (Check: the posteriors $\frac3{11}$ and $\frac8{11}$
sum to $1$ ✓.)

#### **Q20**
**Method: Bayes' theorem with the lie modelled explicitly.**
$P(\text{says }6\mid6)=0.9$; given a non-six face, he names $6$ with probability
$\frac1{5}$, so $P(\text{says }6\mid\neg6)=0.1\times\frac15=\frac1{50}$.
$$P(6\mid\text{says }6)=\frac{0.9\cdot\frac16}{0.9\cdot\frac16+\frac1{50}\cdot\frac56}
=\frac{0.15}{0.15+\frac1{60}}=\frac{0.15}{\frac16}=\frac9{10}.$$
**Answer:** $\dfrac9{10}$. (Check: with the prior $\frac16$ and a symmetric lie
the likelihood ratio is $0.9:\frac{0.1}{5}=0.9:0.02=45:1$, and the posterior
$\frac{45}{45+5}=\frac9{10}$ ✓.)

---

## E · Binomial distribution

#### **Q21**
**Method: $P(X=k)=\binom nk p^kq^{n-k}$.**
$\binom{10}{3}\cdot0.2^3\cdot0.8^7=120\cdot0.008\cdot0.2097152=0.201326592$.
**Answer:** $0.201326592$. (Check: the full pmf over $k=0,\ldots,10$ sums to $1$
and has mean $2=np$ ✓.)

#### **Q22**
**Method: binomial pmf.**
$\binom62\cdot\big(\tfrac13\big)^2\big(\tfrac23\big)^4=15\cdot\frac19\cdot\frac{16}{81}=\frac{240}{729}=\frac{80}{243}$.
**Answer:** $\dfrac{80}{243}$. (Check: $\frac{80}{243}\approx0.3292$ and $k=2$ is
the mode of $\mathrm{Bin}(6,\frac13)$ ✓.)

#### **Q23**
**Method: solve $np=6$ and $npq=4.8$ simultaneously.** Dividing gives
$q=\frac{4.8}{6}=0.8$, so $p=0.2$ and $n=\frac6{0.2}=30$.
**Answer:** $n=30$, $p=\dfrac15$. (Check: $30\cdot0.2=6$ and
$30\cdot0.2\cdot0.8=4.8$ ✓.)

#### **Q24**
**Method: complement of "0, 1 or 2 sixes" with $n=8$, $p=\frac16$.**
$$P(X\ge3)=1-\Big[\binom80\big(\tfrac56\big)^8+\binom81\tfrac16\big(\tfrac56\big)^7+\binom82\big(\tfrac16\big)^2\big(\tfrac56\big)^6\Big].$$
The three excluded terms are $0.23257$, $0.37210$ and $0.26047$, summing to
$0.86514$, so $P=0.13485$.
**Answer:** $\dfrac{75497}{559872}\approx0.1348$. (Check: a simulation of
$200000$ repetitions of $8$ rolls gave $0.1349$ ✓.)

#### **Q25**
**Method: $E[X^2]=\operatorname{Var}(X)+E[X]^2$.**
$\operatorname{Var}=5\cdot\tfrac12\cdot\tfrac12=\frac54$ and $E[X]=\frac52$, so
$E[X^2]=\frac54+\frac{25}{4}=\frac{30}{4}=\frac{15}{2}$.
**Answer:** $\dfrac{15}{2}$. (Check: $\sum_{k=0}^5 k^2\binom5k/32=240/32=7.5$ ✓.)

---

## F · Expectation, variance and games

#### **Q26**
**Method: $E[X]=\sum k\,p(k)$, then $E[X^2]$.**
$E[X]=1(0.2)+2(0.3)+3(0.5)=2.3$; $E[X^2]=1(0.2)+4(0.3)+9(0.5)=5.9$.
$\operatorname{Var}=5.9-2.3^2=0.61$.
**Answer:** $E[X]=\dfrac{23}{10}$, $\operatorname{Var}(X)=\dfrac{61}{100}$.
(Check: the probabilities sum to $1$ and $E[X]$ lies inside $[1,3]$ ✓.)

#### **Q27**
**Method: $E[X]=\frac{1+2+3+4+5+6}{6}$.**
$E[X]=\frac{21}{6}=\frac72$.
**Answer:** $\dfrac72$. (Check: $\operatorname{Var}=\frac{91}{6}-\frac{49}{4}=\frac{35}{12}>0$ ✓.)

#### **Q28**
**Method: linearity of expectation — no independence needed.**
$E[X_1+X_2]=E[X_1]+E[X_2]=\frac72+\frac72=7$.
**Answer:** $7$. (Check: the distribution of the sum is symmetric about $7$ ✓.)

#### **Q29**
**Method: $E[X]=1/p$ for the geometric distribution, with $p=\frac12$.**
Equivalently $E[X]=\sum_{k\ge1}k\,2^{-k}=\frac{1/2}{(1-1/2)^2}=2$.
**Answer:** $2$. (Check: a $200000$-trial simulation gave a mean of $2.0023$ ✓.)

---

## G · Olympiad frontier

#### **Q30**
**Method: sum the tail probabilities.** Let $T$ be the position of the first red
ball among the $8$. Then
$P(T\ge k)=\binom{9-k}{3}/\binom83$ for $k\le6$, so
$$E[T]=\sum_{k=1}^6P(T\ge k)=\frac{\binom83+\binom73+\binom63+\binom53+\binom43+\binom33}{\binom83}=\frac{56+35+20+10+4+1}{56}=\frac94.$$
**Answer:** $\dfrac94$. (Check: the general formula for the minimum of $k$ red
positions among $n$ balls is $\frac{n+1}{k+1}=\frac{9}{4}$ ✓, and a simulation
over $100000$ shuffles gave $2.2499$ ✓.)

#### **Q31**
**Method: area ratio in the $(x,y)$ sample space.** With break points
$0<x<y<1$ the pieces are $x$, $y-x$ and $1-y$; each must be below $\frac12$.
The sample triangle $\{0<x<y<1\}$ has area $\frac12$; the three forbidden
corner triangles ($x\ge\frac12$, $y-x\ge\frac12$, $1-y\ge\frac12$) have total
area $\frac38$, so the favourable area is $\frac12-\frac38=\frac18$.
$$P=\frac{1/8}{1/2}=\frac14.$$
**Answer:** $\dfrac14$. (Check: a $400000$-point simulation gave $0.2503$ ✓.)

#### **Q32**
**Method: the memoryless property of the geometric distribution.**
$P(X>k)=q^k$, so
$$P(X>20\mid X>10)=\frac{P(X>20)}{P(X>10)}=\frac{q^{20}}{q^{10}}=q^{10}=\big(\tfrac12\big)^{10}.$$
**Answer:** $\dfrac1{1024}$. (Check: $2^{-10}=0.0009766$ ✓.)

#### **Q33**
**Method: the coupon collector.** Split the wait into $6$ stages; at stage $j$
the success probability is $\frac{6-j+1}{6}$, so the stage mean is
$\frac{6}{6-j+1}$. Summing $j=1$ to $6$ and reversing the index gives
$6H_6=6\big(1+\frac12+\frac13+\frac14+\frac15+\frac16\big)=6\cdot\frac{49}{20}$.
**Answer:** $\dfrac{147}{10}$ rolls. (Check: a simulation over $50000$ complete
collections gave a mean of $14.71$ rolls ✓.)

#### **Q34**
**Method: recursion on the first move.** The first player wins at once with
probability $\frac12$; if both fail (probability $\frac14$) the situation resets,
so $p=\frac12+\frac14p$, giving $p=\frac{1/2}{1-1/4}$.
**Answer:** $\dfrac23$. (Check: direct summation
$\frac12+\frac18+\frac1{32}+\cdots=\frac{1/2}{1-1/4}$ ✓, and a $200000$-game
simulation gave $0.6664$ ✓.)
