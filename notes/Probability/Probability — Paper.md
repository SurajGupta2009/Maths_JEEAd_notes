---
title: "Probability — Olympiad Paper"
aliases: ["Probability Paper", "Probability-Olympiad-Paper"]
module: "Probability"
module_title: "Probability"
type: paper
tags: [probability, paper, olympiad, statistics, bayes, binomial]
created: 2026-09-28
---

> [!info] Navigation
> ⬅ [[Probability|Chapter 6]] · 📖 [[Probability|Complete Notes]] · ✅ [[Probability — Solutions|Solutions]] ➡

# Probability — Olympiad Paper

> **38 questions · Sections A–G · difficulty ramps JEE Main → JEE Advanced → Olympiad.** → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Probability — Solutions|solutions]].
> Every numeric answer was verified in pure Python (exact fractions and simulation)
> before this file was written.

---

## A · Classical probability and sample spaces (Q1–Q5)

#### **Q1**[JEE Main][sample space]Two fair dice are thrown. Find the probability that the sum is $7$.

**Answer:** $\dfrac16$

#### **Q2**[JEE Main][sample space]A bag contains $5$ red, $3$ blue and $2$ green balls. One ball is drawn at random. Find the probability that it is red.

**Answer:** $\dfrac12$

#### **Q3**[JEE Main][sample space]Three fair coins are tossed. Find the probability of getting at least one head.

**Answer:** $\dfrac78$

#### **Q4**[JEE Main][cards]A card is drawn from a standard $52$-card deck. Find the probability that it is a heart or a king.

**Answer:** $\dfrac4{13}$

#### **Q5**[JEE Main][dice]A die is rolled twice. Find the probability that the product of the two outcomes is even.

**Answer:** $\dfrac34$

---

## B · Addition rule and "at least" (Q6–Q10)

#### **Q6**[JEE Main][addition]Given $P(A)=0.3$, $P(B)=0.4$ and $P(A\cup B)=0.6$, find $P(A\cap B)$.

**Answer:** $0.1$

#### **Q7**[JEE Main][dice]Two fair dice are thrown. Find the probability that the sum is at least $10$.

**Answer:** $\dfrac16$

#### **Q8**[JEE Main][addition]Given $P(A)=0.4$, $P(B)=0.5$ and $P(A\cap B)=0.2$, find $P(A\cup B)$.

**Answer:** $0.7$

#### **Q9**[JEE Adv][counting]A committee of $3$ is chosen from $5$ men and $4$ women. Find the probability that it contains at least one woman.

**Answer:** $\dfrac{37}{42}$

#### **Q10**[JEE Main][binomial]Five fair coins are tossed. Find the probability of getting exactly three heads.

**Answer:** $\dfrac5{16}$

---

## C · Conditional probability and independence (Q11–Q15)

#### **Q11**[JEE Main][conditional]A fair die is thrown. Given that the outcome is even, find the probability that it is $6$.

**Answer:** $\dfrac13$

#### **Q12**[JEE Main][without replacement]Two cards are drawn at random without replacement from a $52$-card deck. Find the probability that both are aces.

**Answer:** $\dfrac1{221}$

#### **Q13**[JEE Main][independence]Given $P(A)=0.6$, $P(B)=0.3$ and $P(A\cap B)=0.18$, determine whether $A$ and $B$ are independent.

**Answer:** Yes — $0.6\times0.3=0.18=P(A\cap B)$

#### **Q14**[JEE Adv][conditional]A family has two children. Given that at least one of them is a boy, find the probability that both are boys.

**Answer:** $\dfrac13$

#### **Q15**[JEE Main][without replacement]A bag contains $4$ white and $6$ black balls. Two balls are drawn without replacement. Find the probability that the second ball is black, given that the first is white.

**Answer:** $\dfrac23$

---

## D · Total probability and Bayes' theorem (Q16–Q20)

#### **Q16**[JEE Main][total probability]Three machines $A,B,C$ produce $50\%$, $30\%$ and $20\%$ of a factory's output, with defect rates $1\%$, $2\%$ and $3\%$ respectively. An item is chosen at random. Find the probability that it is defective.

**Answer:** $\dfrac{17}{1000}$

#### **Q17**[JEE Adv][bayes]For the factory in Q16, given that the chosen item is defective, find the probability that it was produced by machine $A$.

**Answer:** $\dfrac5{17}$

#### **Q18**[JEE Main][total probability]Two urns: $U_1$ holds $3$ red and $7$ blue balls, $U_2$ holds $8$ red and $2$ blue. An urn is chosen at random and one ball drawn from it. Find the probability that the ball is red.

**Answer:** $\dfrac{11}{20}$

#### **Q19**[JEE Adv][bayes]For the urns in Q18, given that the drawn ball is red, find the probability that it came from $U_2$.

**Answer:** $\dfrac8{11}$

#### **Q20**[JEE Adv][bayes]A person tells the truth $90\%$ of the time. He throws a die and reports that it shows a $6$. Find the probability that it really is a $6$, assuming that whenever he lies he names one of the other five faces at random.

**Answer:** $\dfrac9{10}$

---

## E · Binomial distribution (Q21–Q25)

#### **Q21**[JEE Main][binomial]Let $X\sim\mathrm{Bin}(10,0.2)$. Find $P(X=3)$.

**Answer:** $0.201326592$

#### **Q22**[JEE Main][binomial]Let $X\sim\mathrm{Bin}\big(6,\tfrac13\big)$. Find $P(X=2)$.

**Answer:** $\dfrac{80}{243}$

#### **Q23**[JEE Adv][binomial]For $X\sim\mathrm{Bin}(n,p)$ the mean is $6$ and the variance is $4.8$. Find $n$ and $p$.

**Answer:** $n=30$, $p=\dfrac15$

#### **Q24**[JEE Adv][binomial]A fair die is rolled $8$ times. Find the probability of obtaining three or more sixes.

**Answer:** $\dfrac{75497}{559872}\approx0.1348$

#### **Q25**[JEE Adv][moments]Let $X\sim\mathrm{Bin}\big(5,\tfrac12\big)$. Find $E[X^2]$.

**Answer:** $\dfrac{15}{2}$

---

## F · Expectation, variance and games (Q26–Q29)

#### **Q26**[JEE Main][expectation]A discrete random variable takes the values $1,2,3$ with probabilities $0.2,0.3,0.5$. Find $E[X]$ and $\operatorname{Var}(X)$.

**Answer:** $E[X]=\dfrac{23}{10}$, $\operatorname{Var}(X)=\dfrac{61}{100}$

#### **Q27**[JEE Main][expectation]A fair die is rolled once. Find the expected value of the outcome.

**Answer:** $\dfrac72$

#### **Q28**[JEE Main][expectation]Two fair dice are rolled. Find the expected value of their sum.

**Answer:** $7$

#### **Q29**[JEE Main][geometric]A fair coin is tossed until the first head appears. Find the expected number of tosses.

**Answer:** $2$

---

## G · Olympiad frontier (Q30–Q38)

#### **Q30**[Olympiad][expectation]A bag contains $3$ red and $5$ blue balls. Balls are drawn one at a time without replacement until a red ball appears. Find the expected number of draws.

**Answer:** $\dfrac94$

#### **Q31**[Olympiad][geometric]A stick of unit length is broken at two points chosen independently and uniformly at random. Find the probability that the three resulting pieces can form a triangle.

**Answer:** $\dfrac14$

#### **Q32**[Olympiad][memoryless]Let $X$ be a geometric random variable with $p=\tfrac12$. Compute $P(X>20\mid X>10)$.

**Answer:** $\dfrac1{1024}$

#### **Q33**[Olympiad][coupon collector]A fair die is rolled repeatedly. How many rolls are needed on average before all six faces have appeared at least once?

**Answer:** $\dfrac{147}{10}$ rolls

#### **Q34**[Olympiad][game]Two players alternately toss a fair coin; the first to throw a head wins. Find the probability that the first player to toss wins.

**Answer:** $\dfrac23$

#### **Q35**[Olympiad][ballot]In an election candidate $A$ receives $a$ votes and $B$ receives $b$ votes with $a>b$, counted in a uniformly random order. Prove Bertrand's ballot theorem: the probability that $A$ is strictly ahead after every vote is $\dfrac{a-b}{a+b}$. Verify it for $(a,b)=(3,2)$.

**Answer:** $\dfrac{a-b}{a+b}$; for $(3,2)$ it is $\dfrac15$

#### **Q36**[Olympiad][gambler ruin]A fair coin game starts at $3$ units and stops at $0$ or $10$ units. Find the probability of reaching $10$ before ruin.

**Answer:** $\dfrac3{10}$

#### **Q37**[Olympiad][runs]Find the expected number of tosses of a fair coin needed to see three heads in a row.

**Answer:** $14$ tosses

#### **Q38**[Olympiad][derangements]Five letters are placed at random into five addressed envelopes. Find the probability that no letter is in its correct envelope.

**Answer:** $\dfrac{11}{30}\approx0.3667$

---

> [!note] Exam technique notes
> - **State the sample space first**, and make sure its outcomes are equally likely
>   before using $\frac{\lvert E\rvert}{\lvert S\rvert}$.
> - **For "at least one", use the complement** — it is almost always smaller.
> - **Never confuse $P(A\mid B)$ with $P(B\mid A)$.** Bayes' theorem is the only
>   legitimate bridge between them, and it needs the priors.
> - **Linearity of expectation needs no independence** — use it before attempting a
>   full distribution.
> - **For a process with a reset, write a recursion on the state** rather than
>   enumerating outcomes.
> - **A fair gamble is a martingale:** $E[\text{final}]=E[\text{start}]$ gives
>   gambler's ruin instantly.
