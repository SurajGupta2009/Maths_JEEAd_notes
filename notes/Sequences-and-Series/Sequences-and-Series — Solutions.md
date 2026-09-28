---
title: "Sequences & Series — Solutions"
aliases: ["Sequences and Series Solutions"]
module: "Sequences-and-Series"
module_title: "Sequences & Series"
type: solutions
tags: [sequences-and-series, solutions, olympiad, algebra, progressions]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Sequences-and-Series — Paper|Paper]] · 📖 [[Sequences-and-Series|Complete Notes]]

# Sequences & Series — Solutions

> Full solutions to all 34 questions, same Q-ids as the
> [[Sequences-and-Series — Paper|paper]]. Every solution: **method first →
> derivation → a check.** Every numeric answer was verified in pure Python
> (stdlib only) before this file was written.

---

## A · Arithmetic progressions

#### **Q1**
**Method: $a_n=a+(n-1)d$.** With $a=2$, $d=3$, $n=20$: $2+19\cdot3=59$.
**Answer:** $59$.

#### **Q2**
**Method: $S_n=\frac n2\big(2a+(n-1)d\big)$.** $\frac{20}{2}(4+57)=10\cdot61=610$.
**Answer:** $610$. (Check by pairing: mean of first and last $=\frac{2+59}{2}=30.5$, and $20\cdot30.5=610$ ✓.)

#### **Q3**
**Method: $d=a_2-a_1$.** $5-2=3$.
**Answer:** $d=3$.

#### **Q4**
**Method: $d=\frac{b-a}{k+1}$ with $k=3$.** $\frac{14-2}{4}=3$, so the means are $2+3,2+6,2+9$.
**Answer:** $5,8,11$. (Check: $2,5,8,11,14$ is an AP with $d=3$ ✓.)

#### **Q5**
**Method: AP with $a=2$, $d=2$, $n=20$.** $S_{20}=\frac{20}{2}(4+38)=10\cdot42=420$.
**Answer:** $420$. (Equivalently $2\cdot\frac{20\cdot21}{2}=420$ ✓.)

---

## B · Geometric progressions

#### **Q6**
**Method: $a_n=ar^{n-1}$.** $3\cdot2^9=3\cdot512$.
**Answer:** $1536$.

#### **Q7**
**Method: $S_n=\frac{a(r^n-1)}{r-1}$.** $\frac{3(2^{10}-1)}1=3\cdot1023$.
**Answer:** $3069$. (Check on the first four terms: $3+6+12+24=45$ and $\frac{3(16-1)}1=45$ ✓.)

#### **Q8**
**Method: $S_\infty=\frac a{1-r}$ since $\lvert r\rvert=\frac12<1$.** $\frac1{1-\frac12}=2$.
**Answer:** $2$. (Partial sums: after $10$ terms, $1.9980$ ✓.)

#### **Q9**
**Method: $r=\left(\frac ba\right)^{1/(k+1)}$ with $k=3$.** $81^{1/4}=3$, so the means are $3,9,27$.
**Answer:** $3,9,27$.

#### **Q10**
**Method: geometric mean of three terms is $(abc)^{1/3}$.** $(2\cdot8\cdot32)^{1/3}=512^{1/3}$.
**Answer:** $8$. (It is the middle term of the GP $2,8,32$ ✓.)

---

## C · Special series

#### **Q11**
**Method: $\frac{n(n+1)}2$.** $\frac{20\cdot21}{2}$.
**Answer:** $210$.

#### **Q12**
**Method: $\frac{n(n+1)(2n+1)}6$.** $\frac{10\cdot11\cdot21}{6}$.
**Answer:** $385$.

#### **Q13**
**Method: the cube formula is the square of the linear one.** $\left(\frac{10\cdot11}{2}\right)^2=55^2$.
**Answer:** $3025$.

#### **Q14**
**Method: AP with $a=2$, $d=2$, and $50$ terms** (since $\frac{100-2}{2}+1=50$). $S_{50}=\frac{50}{2}(4+98)=25\cdot102$.
**Answer:** $2550$.

#### **Q15**
**Method: the first $n$ odd numbers are $2k-1$, whose sum is $n^2$.** $10^2=100$, so the mean is $\frac{100}{10}=10$.
**Answer:** sum $100$, AM $10$. (Check: $1+3+5+\cdots+19=100$ ✓.)

---

## D · Arithmetico-geometric progressions

#### **Q16**
**Method: infinite AGP formula $\frac a{1-r}+\frac{dr}{(1-r)^2}$ with $a=1,d=1,r=\frac12$.**
$$\frac1{1-\frac12}+\frac{\frac12}{(1-\frac12)^2}=2+\frac{1/2}{1/4}=2+2=4.$$
**Answer:** $4$. (Partial sums: after $10$ terms, $3.9805$ ✓.)

#### **Q17**
**Method: $\sum kx^k=\frac x{(1-x)^2}$ with $x=\frac12$.**
$$\frac{1/2}{(1/2)^2}=\frac{1/2}{1/4}=2.$$
**Answer:** $2$.

#### **Q18**
**Method: evaluate directly, or use the finite formula $\frac{1-(n+1)x^n+nx^{n+1}}{(1-x)^2}$.**
$$1+2\cdot\frac12+3\cdot\frac14+4\cdot\frac18+5\cdot\frac1{16}=1+1+\frac34+\frac12+\frac5{16}=\frac{16+16+12+8+5}{16}=\frac{57}{16}.$$
**Answer:** $\dfrac{57}{16}=3.5625$. (The infinite limit is $\frac1{(1-\frac12)^2}=4$ ✓.)

#### **Q19**
**Method: split into $2\sum\frac{k}{2^k}-\sum\frac1{2^k}$.** The first is $2\cdot2=4$ (from Q17) and the second is $\frac{1/2}{1-1/2}=1$.
**Answer:** $4-1=3$. (Partial sums: after $20$ terms, $2.99992$ ✓.)

---

## E · Telescoping and the method of differences

#### **Q20**
**Method: $\frac1{k(k+1)}=\frac1k-\frac1{k+1}$; the sum telescopes.**
$$1-\frac1{11}=\frac{10}{11}.$$
**Answer:** $\dfrac{10}{11}\approx0.9091$.

#### **Q21**
**Method: $\frac1{k(k+2)}=\frac12\left(\frac1k-\frac1{k+2}\right)$; the interior cancels, leaving the first two and last two terms.**
$$\frac12\left(1+\frac12-\frac16-\frac17\right)=\frac12\left(\frac32-\frac{13}{42}\right)=\frac12\cdot\frac{50}{42}=\frac{25}{42}.$$
**Answer:** $\dfrac{25}{42}\approx0.5952$. (Direct check: $\frac13+\frac18+\frac1{15}+\frac1{24}+\frac1{35}\approx0.5952$ ✓.)

#### **Q22**
**Method: telescope.** $1-\frac1{n+1}$.
**Answer:** $\dfrac n{n+1}$.

#### **Q23**
**Method: telescope.** $\left(1-\frac12\right)+\left(\frac12-\frac13\right)+\left(\frac13-\frac14\right)=1-\frac14$.
**Answer:** $\dfrac34$.

---

## F · Harmonic progressions and means

#### **Q24**
**Method: $H=\frac{2ab}{a+b}$.** $\frac{2\cdot2\cdot4}{2+4}=\frac{16}{6}$.
**Answer:** $\dfrac83$.

#### **Q25**
**Method: $H=\frac{n}{\sum\frac1{a_i}}$.** $\frac3{1+\frac12+\frac14}=\frac3{7/4}=\frac{12}{7}$.
**Answer:** $\dfrac{12}{7}\approx1.7143$.

#### **Q26**
**Method: compare $A$, $G$ and $H$ for $4$ and $9$.** $A=\frac{4+9}{2}=6.5$,
$G=\sqrt{36}=6$ and $H=\frac{2\cdot4\cdot9}{4+9}=\frac{72}{13}\approx5.5385$.
**Answer:** $6.5\ge6\ge\dfrac{72}{13}$. (Check: $A^2=42.25\ge36=G^2$ ✓, and
$G^2=36\ge\frac{5184}{169}\approx30.67=H^2$ ✓.)

#### **Q27**
**Method: the reciprocals form an AP.** The reciprocals are $1,2,3,\ldots$ with
common difference $1$, so the $4^{\rm th}$ reciprocal is $4$.
**Answer:** $\dfrac14$. (Check: the HP is $\frac11,\frac12,\frac13,\frac14$ ✓.)

#### **Q28**
**Method: split as a difference of two-factor terms.**
$\frac1{k(k+1)(k+2)}=\frac12\left[\frac1{k(k+1)}-\frac1{(k+1)(k+2)}\right]$, so
$$\sum_{k=1}^n\frac1{k(k+1)(k+2)}=\frac12\left[\frac12-\frac1{(n+1)(n+2)}\right]=\frac{n(n+3)}{4(n+1)(n+2)}.$$
**Answer:** $\dfrac{n(n+3)}{4(n+1)(n+2)}$. (Check for $n=5$: direct sum
$\frac16+\frac1{24}+\frac1{60}+\frac1{120}+\frac1{210}=\frac{200}{840}=\frac5{21}$, and the
formula gives $\frac{40}{168}=\frac5{21}$ ✓. For $n=10$: $\frac{65}{264}$ ✓.)

#### **Q29**
**Method: telescope.** $k\,k!=(k+1-1)k!=(k+1)!-k!$, so
$$\sum_{k=1}^n k\,k!=\sum_{k=1}^n\big[(k+1)!-k!\big]=(n+1)!-1.$$
**Answer:** $(n+1)!-1$. (Check for $n=5$: $1+4+18+96+600=719$ and $6!-1=719$ ✓.
For $n=7$: $40319=8!-1$ ✓.)

#### **Q30**
**Method: the tangent difference formula.** With $\tan\alpha=\frac1k$ and
$\tan\beta=\frac1{k+1}$,
$\tan(\alpha-\beta)=\frac{1/(k(k+1))}{1+1/(k(k+1))}=\frac1{k^2+k+1}$, so each term
is $\arctan\frac1k-\arctan\frac1{k+1}$ and the sum telescopes:
$$\sum_{k=1}^n\arctan\frac1{k^2+k+1}=\arctan1-\arctan\frac1{n+1}=\frac\pi4-\arctan\frac1{n+1}.$$
**Answer:** $\dfrac\pi4-\arctan\dfrac1{n+1}$. (Check numerically for $n=5$: the
sum equals $\frac\pi4-\arctan\frac16$ to $10^{-9}$ ✓. As $n\to\infty$ the sum tends
to $\frac\pi4\approx0.7854$ ✓.)

#### **Q31**
**Method: solve for $F(x)$, then partial fractions.** Let
$F(x)=\sum_{n\ge0}F_nx^n$ with $F_0=0$, $F_1=1$. Since
$F_n=F_{n-1}+F_{n-2}$ for $n\ge2$,
$$F(x)=xF(x)+x^2F(x)+x\quad\Longrightarrow\quad F(x)=\frac{x}{1-x-x^2}.$$
Factor $1-x-x^2=(1-\varphi x)(1-\psi x)$ with $\varphi=\frac{1+\sqrt5}{2}$,
$\psi=\frac{1-\sqrt5}{2}$, and write
$\frac{x}{(1-\varphi x)(1-\psi x)}=\frac{A}{1-\varphi x}+\frac{B}{1-\psi x}$ with
$A=\frac1{\sqrt5}$, $B=-\frac1{\sqrt5}$. Expanding each fraction as a geometric
series gives $F_n=A\varphi^n+B\psi^n$.
**Answer:** $F_n=\dfrac{\varphi^n-\psi^n}{\sqrt5}$. (Check: $F_1=\frac{1.618034+0.618034}{2.236068}=1$ ✓,
$F_7=13$ ✓, $F_{10}=55$ ✓, and $(1-x-x^2)\sum_{n=0}^{13}F_nx^n=x$ exactly ✓.)

#### **Q32**
**Method: difference of squares, then cancel.**
$1-\frac1{k^2}=\frac{k-1}{k}\cdot\frac{k+1}{k}$, so
$$\prod_{k=2}^n\left(1-\frac1{k^2}\right)=\prod_{k=2}^n\frac{k-1}{k}\cdot\prod_{k=2}^n\frac{k+1}{k}=\frac1n\cdot\frac{n+1}{2}=\frac{n+1}{2n}.$$
**Answer:** $\dfrac{n+1}{2n}$, tending to $\dfrac12$. (Check for $n=4$:
$\frac34\cdot\frac89\cdot\frac{15}{16}=\frac{360}{576}=\frac58=\frac{4+1}{2\cdot4}$ ✓.
For $n=7$: $\frac47$ ✓.)

#### **Q33**
**Method: shift and subtract.** Writing $S=\sum_{k=1}^n k2^{k-1}$ and
$2S=\sum_{k=1}^n k2^k$, subtraction gives
$S=2S-S=\sum_{k=1}^n k2^k-\sum_{k=1}^n k2^{k-1}$; re-indexing the first sum and
cancelling leaves $S=(n-1)2^n+1$.
**Answer:** $1+(n-1)2^n$. (Check for $n=5$: $1+4+12+32+80=129$ and
$1+4\cdot32=129$ ✓.)

#### **Q34**
**Method: shift by the fixed point.** $L=\frac1{1-2}=-1$, so
$a_n+1=2^{n-1}(a_1+1)=2^n$, giving $a_n=2^n-1$.
**Answer:** $a_n=2^n-1$. (Check: $a_1=1$, $a_2=3$, $a_3=7$, $a_4=15$ — each is
$2^n-1$ ✓, and $2a_{n-1}+1=2(2^{n-1}-1)+1=2^n-1=a_n$ ✓.)
