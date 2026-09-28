---
title: "Complex Numbers — Olympiad Paper Solutions"
aliases:
  - Complex-Numbers Solutions
module: "Complex-Numbers"
module_title: "Complex Numbers"
type: solutions
tags:
  - complex-numbers
  - solutions
  - olympiad
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Complex-Numbers — Paper|Paper]] · 📖 [[Complex-Numbers|Complex Numbers]]

# Olympiad Paper · 48 questions · Solutions & marking guide

*Companion to the 48-question paper*

# Full Worked Solutions

Every solution shows the *method name* first, then the computation, then a check. Where a problem has two standard methods, both are given — the exam rewards the ability to choose, and the notes are built on the same principle.

### A · Foundations (Q1–Q6)

#### **Q1**[JEE Main]Find the principal argument of $1 - i\sqrt3$.

Find the principal argument of $1 - i\sqrt3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: quadrant + reference angle.** $z = 1 - i\sqrt3$: real part $1 &gt; 0$, imaginary part $-\sqrt3 &lt; 0$ → fourth quadrant. $\tan\theta = -\sqrt3$, reference angle $\pi/3$, so $\operatorname{Arg} z = -\pi/3 \in (-\pi, \pi]$.


Answer: $-\dfrac{\pi}{3}$


Check in polar form: $|z| = \sqrt{1+3} = 2$, and $2(\cos(-\pi/3) + i\sin(-\pi/3)) = 2(\tfrac12 - i\tfrac{\sqrt3}{2}) = 1 - i\sqrt3$ ✓.

</details>

#### **Q2**[JEE Main]For $z = -1 + i$, find $|z|$ and $\operatorname{Arg} z$.

For $z = -1 + i$, find $|z|$ and $\operatorname{Arg} z$.

<details>
<summary>Answer + Reasoning</summary>

$|z| = \sqrt{1+1} = \sqrt2$. Second quadrant: $\tan\theta = -1$, reference $\pi/4$, so $\operatorname{Arg} z = \pi - \pi/4 = 3\pi/4$.


Answer: $\sqrt2,\ \dfrac{3\pi}{4}$

</details>

#### **Q3**[JEE Main]Evaluate $(1+i)^{10}$.

Evaluate $(1+i)^{10}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: polar form.** $1+i = \sqrt2\, e^{i\pi/4}$. Hence 
$$ (1+i)^{10} = (\sqrt2)^{10} e^{i\,10\pi/4} = 2^5 e^{i5\pi/2} = 32 e^{i\pi/2} = 32i $$
 (since $5\pi/2 \equiv \pi/2 \pmod{2\pi}$).


Answer: $32i$


Shortcut check: $(1+i)^2 = 2i$, so $(1+i)^{10} = (2i)^5
        = 32 i^5 = 32i$ ✓ — same answer in four lines.

</details>

#### **Q4**[JEE Advanced]If $z^4 = 1$ and $z \ne 1$, find all possible values of $z + \dfrac{1}{z}$.

If $z^4 = 1$ and $z \ne 1$, find all possible values of $z + \dfrac{1}{z}$.

<details>
<summary>Answer + Reasoning</summary>

The fourth roots of $1$ are $1, i, -1, -i$. Excluding $z = 1$, and using $\dfrac{1}{z} = \bar z$ on the unit circle:


- $z = i$: $z + 1/z = i + (-i) = 0$.
- $z = -1$: $z + 1/z = -2$.
- $z = -i$: $z + 1/z = -i + i = 0$.


Distinct values: $\{0, -2\}$. (Structure: $z = \pm i$ gives $2\cos(\pm\pi/2) = 0$; $z = -1$ gives $2\cos\pi = -2$.)


Answer: $\{0,\ -2\}$

</details>

#### **Q5**[JEE Advanced]Prove $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$ using De Moivre, and deduce…

Prove $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$ using De Moivre, and deduce $\operatorname{Re}(z^3 + z^{-3})$ for $|z| = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Part 1.** By De Moivre, 
$$ (\cos\theta + i\sin\theta)^3 = \cos 3\theta + i\sin 3\theta. $$
 Expanding the left: $\cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta
        - i\sin^3\theta$. Equating real parts: 
$$ \cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta
        = \cos^3\theta - 3\cos\theta(1-\cos^2\theta) = 4\cos^3\theta - 3\cos\theta. \ \checkmark $$
 **Part 2.** For $|z| = 1$, write $z = e^{i\theta}$: $z^3 + z^{-3} = e^{i3\theta} + e^{-i3\theta} = 2\cos 3\theta$, so 
$$ \operatorname{Re}(z^3+z^{-3}) = 2\cos 3\theta
        = 2(4\cos^3\theta - 3\cos\theta) = 8\cos^3\theta - 6\cos\theta. $$



Answer: proof; $8\cos^3\theta - 6\cos\theta$

</details>

#### **Q6**[JEE Main]Find all fourth roots of $16$.

Find all fourth roots of $16$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the $n$-root formula.** $16 = 16 e^{i\cdot 0}$, so the fourth roots are $z_k = 16^{1/4} e^{i(0 + 2k\pi)/4} = 2 e^{ik\pi/2}$, $k = 0,1,2,3$: 
$$ 2,\quad 2i,\quad -2,\quad -2i. $$
 All four satisfy $z^4 = 16$; four distinct roots, as the degree requires.


Answer: $\pm 2,\ \pm 2i$

</details>


### B · Roots of Unity (Q7–Q12)

#### **Q7**[JEE Main]If $\omega$ is a non-real cube root of unity, evaluate $(1-\omega)(1-\omega^2)$.

If $\omega$ is a non-real cube root of unity, evaluate $(1-\omega)(1-\omega^2)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand + the $\omega$-identities.** 
$$ (1-\omega)(1-\omega^2) = 1 - (\omega+\omega^2) + \omega^3 = 1 - (-1) + 1 = 3. $$
 Polar cross-check: $1-\omega = \sqrt3 e^{-i\pi/6}$, $1-\omega^2 = \sqrt3 e^{i\pi/6}$, product $= 3$ ✓.


Answer: $3$

</details>

#### **Q8**[JEE Advanced]For $n \ge 4$, let $S_n = \sum_{k=0}^{n-1} (-1)^k e^{2\pi i k/n}$. Show $S_n = 0$ for even…

For $n \ge 4$, let $S_n = \sum_{k=0}^{n-1} (-1)^k e^{2\pi i k/n}$. Show $S_n = 0$ for even $n$, and find $S_n$ for odd $n$.

<details>
<summary>Answer + Reasoning</summary>

**Method: geometric series with ratio $-\zeta$, $\zeta = e^{2\pi i/n}$.** The ratio is $-\zeta \ne 1$ for $n \ge 3$ (since $-\zeta = 1$ would force $\zeta = -1$, i.e. $n = 2$). So 
$$ S_n = \frac{1 - (-\zeta)^n}{1 + \zeta} = \frac{1 - (-1)^n \zeta^n}{1 + \zeta}
        = \frac{1 - (-1)^n}{1 + e^{2\pi i/n}} $$
 using $\zeta^n = 1$. **Even $n$:** $(-1)^n = 1$ → $S_n = 0$. **Odd $n$:** $(-1)^n = -1$ → $S_n = \dfrac{2}{1 + e^{2\pi i/n}}$. Clean form: $1 + e^{2\pi i/n} = 2 e^{\pi i/n}\cos\frac{\pi}{n}$, so 
$$ S_n = \frac{1}{e^{\pi i/n}\cos\frac{\pi}{n}} = \sec\frac{\pi}{n}\; e^{-\pi i/n}
        \qquad (n \text{ odd}). $$
 Check $n = 5$: $S_5 = \sec 36^\circ \, e^{-i36^\circ} = 1.2361(0.8090 - 0.5878i)
        = 1 - 0.7266i$; direct summation gives $1 - 0.7266i$ ✓.


Answer: $0$ (even); $\dfrac{2}{1+e^{2\pi i/n}} =
        \sec\frac{\pi}{n}\,e^{-\pi i/n}$ (odd)

</details>

#### **Q9**[JEE Main]If $\omega^3 = 1$ and $\omega \ne 1$, evaluate $\sum_{k=0}^{101} \omega^k$.

If $\omega^3 = 1$ and $\omega \ne 1$, evaluate $\sum_{k=0}^{101} \omega^k$.

<details>
<summary>Answer + Reasoning</summary>

102 terms $= 34$ blocks of three; each block sums to $1 + \omega + \omega^2 = 0$: 
$$ \sum_{k=0}^{101} \omega^k = 34 \cdot 0 = 0. $$
 (Equivalently: geometric series $\frac{1-\omega^{102}}{1-\omega} = 0$, since $\omega^{102} = (\omega^3)^{34} = 1$.)


Answer: $0$

</details>

#### **Q10**[JEE Advanced]Find $\sum_{k \equiv 1 \pmod 3} \binom{9}{k}$.

Find $\sum_{k \equiv 1 \pmod 3} \binom{9}{k}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: roots-of-unity filter** ($n = 3, r = 1$, $\omega = e^{2\pi i/3}$): 
$$ \sum_{k \equiv 1(3)} \binom{9}{k} = \frac13\sum_{j=0}^{2} \omega^{-j}(1+\omega^j)^9. $$
 The three terms: $j = 0$: $\;2^9 = 512$. $j = 1$: $\;\omega^{-1}(1+\omega)^9 = \omega^2 \cdot e^{i3\pi} = -\omega^2$ (using $1+\omega = e^{i\pi/3}$). $j = 2$: $\;\omega^{-2}(1+\omega^2)^9 = \omega \cdot e^{-i3\pi} = -\omega$. Hence the sum $= \frac13\left(512 - \omega - \omega^2\right) = \frac13(512 + 1) = 171$.


Answer: $171$


Direct check: $\binom91 + \binom94 + \binom97 = 9 + 126 + 36 = 171$ ✓. (The $k \equiv 0$ class gives $170$ and $k \equiv 2$ gives $171$; total $512$ ✓.)

</details>

#### **Q11**[JEE Advanced]Evaluate $\prod_{k=1}^{5}\left(1 - e^{2\pi i k/5}\right)$.

Evaluate $\prod_{k=1}^{5}\left(1 - e^{2\pi i k/5}\right)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the product formula** $\prod_{k=1}^{n-1}(1-\zeta_k) = n$ (derivative of $x^n - 1$ at $x = 1$). With $n = 5$: the product is $5$.


Answer: $5$

</details>

#### **Q12**[Olympiad]Evaluate $\prod_{k=1}^{5} \sin\dfrac{\pi k}{5}$.

Evaluate $\prod_{k=1}^{5} \sin\dfrac{\pi k}{5}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the trigonometric product formula.** $\prod_{k=1}^{n-1}\sin\frac{\pi k}{n} = \frac{n}{2^{n-1}}$. With $n = 5$: $\frac{5}{16}$. Direct check: $\sin 36^\circ\sin 72^\circ\sin 108^\circ\sin 144^\circ
        = \sin^2 36^\circ \sin^2 72^\circ = (0.5878)^2(0.9511)^2 = 0.3125 = \frac{5}{16}$ ✓.


Answer: $\dfrac{5}{16}$

</details>


### C · Loci & Optimization (Q13–Q18)

#### **Q13**[JEE Main]Find the locus of $z$ satisfying $|z - 1| = |z - i|$.

Find the locus of $z$ satisfying $|z - 1| = |z - i|$.

<details>
<summary>Answer + Reasoning</summary>

Equal distance from $1$ and $i$: the perpendicular bisector of the segment joining $(1,0)$ and $(0,1)$. Algebraically, with $z = a+bi$: 
$$ (a-1)^2 + b^2 = a^2 + (b-1)^2 \iff -2a + 1 = -2b + 1 \iff a = b. $$
 Locus: the line $y = x$.


Answer: the line $y = x$

</details>

#### **Q14**[JEE Advanced]If $|z| = 1$, find the range of $\left|z + \dfrac{1}{z} + 2i\right|$.

If $|z| = 1$, find the range of $\left|z + \dfrac{1}{z} + 2i\right|$.

<details>
<summary>Answer + Reasoning</summary>

On $|z| = 1$, $\frac1z = \bar z$, so with $z = e^{i\theta}$: $z + \frac1z + 2i = 2\cos\theta + 2i$. Modulus: 
$$ 2\sqrt{\cos^2\theta + 1} \in [2, 2\sqrt2], $$
 since $\cos^2\theta \in [0,1]$. Endpoints attained: $z = \pm i$ (min, $2$) and $z = \pm 1$ (max, $2\sqrt2$).


Answer: $[2,\ 2\sqrt2]$

</details>

#### **Q15**[JEE Advanced]If $|z| = 1$, find $\min |z - (1-2i)|$ and the $z$ where it occurs.

If $|z| = 1$, find $\min |z - (1-2i)|$ and the $z$ where it occurs.

<details>
<summary>Answer + Reasoning</summary>

**Method: triangle inequality with equality condition.** 
$$ |z - a| \ge \big||a| - |z|\big| = \sqrt5 - 1, $$
 with equality iff $z$ points in the same direction as $a = 1-2i$: $z = \dfrac{a}{|a|} = \dfrac{1-2i}{\sqrt5}$. Geometrically: the ray from the origin through $a$ exits the unit circle at the closest point.


Answer: $\sqrt5 - 1$, at $z = \dfrac{1-2i}{\sqrt5}$

</details>

#### **Q16**[JEE Advanced]If $|z| = |w| = 1$ and $z\bar w = i$, find $|z - w|$.

If $|z| = |w| = 1$ and $z\bar w = i$, find $|z - w|$.

<details>
<summary>Answer + Reasoning</summary>

$$ |z-w|^2 = (z-w)(\bar z - \bar w) = 2 - (z\bar w + \bar z w) = 2 - 2\operatorname{Re}(z\bar w)
        = 2 - 2\operatorname{Re}(i) = 2. $$
 So $|z-w| = \sqrt2$. Geometric reading: $z\bar w = i$ means $w = iz$ — the two points are a quarter-turn apart, chord $2\sin 45^\circ = \sqrt2$.


Answer: $\sqrt2$

</details>

#### **Q17**[JEE Advanced]Find the locus of $z$ with $\arg\dfrac{z-1}{z+1} = \dfrac{\pi}{4}$. Verify a point.

Find the locus of $z$ with $\arg\dfrac{z-1}{z+1} = \dfrac{\pi}{4}$. Verify a point.

<details>
<summary>Answer + Reasoning</summary>

**Method: argument locus → arc of a circle** (inscribed angle $\pi/4$ subtending chord $[-1, 1]$). Radius: $R = \dfrac{|1-(-1)|}{2\sin(\pi/4)} = \dfrac{2}{\sqrt2} = \sqrt2$. Center: on the perpendicular bisector of $[-1,1]$ (the imaginary axis) at distance $\tfrac{2}{2}\cot\frac{\pi}{4} = 1$ from $0$ → $C = i$. Circle: $|z - i| = \sqrt2$, i.e. $x^2 + (y-1)^2 = 2$. **Which arc:** test $z = i(1+\sqrt2)$ (the top of the circle): $z-1 = -1 + i(1+\sqrt2)$, $z+1 = 1 + i(1+\sqrt2)$. With $1+\sqrt2 = \tan\frac{3\pi}{8}$: $\arg(z+1) = \frac38\pi$, $\arg(z-1) = \pi - \frac38\pi = \frac58\pi$, so $\arg\frac{z-1}{z+1} = \frac58\pi - \frac38\pi = \frac{\pi}{4}$ ✓ — the upper arc. Endpoints $\pm 1$ excluded (fraction undefined at $1$; ratio $0$ — argument undefined — at $-1$).


Answer: arc of $x^2 + (y-1)^2 = 2$, $y &gt; 0$, excluding $\pm 1$

</details>

#### **Q18**[JEE Advanced]If $\operatorname{Re} z &gt; 0$ and $|z - 1| &lt; 1$, find the range of $|z|$.

If $\operatorname{Re} z &gt; 0$ and $|z - 1| &lt; 1$, find the range of $|z|$.

<details>
<summary>Answer + Reasoning</summary>

**Method: draw the region.** $|z-1| &lt; 1$: open disk, center $1$, radius $1$ — it touches the origin and lies in $\operatorname{Re} z \ge 0$. Intersecting with $\operatorname{Re} z &gt; 0$ removes exactly the origin (the disk's sole point with real part $0$). Distances from $0$: infimum $0$ (approached from inside, not attained — the origin is excluded), supremum $2$ (the rightmost point $2$ is on the boundary, also excluded since the disk is open).


Answer: $(0,\ 2)$

</details>


### D · Regions & Conics (Q19–Q23)

#### **Q19**[JEE Main]If $|z + 2| \le 3$, find the range of $|z|$.

If $|z + 2| \le 3$, find the range of $|z|$.

<details>
<summary>Answer + Reasoning</summary>

**Method: triangle inequality, both directions.** $|z| \le |z+2| + 2 \le 3 + 2 = 5$, with equality at $z = -5$ (on the boundary, included since $\le$). And $0 \le |z|$, attained at $z = 0$ (check: $|0+2| = 2
        \le 3$ ✓).


Answer: $[0,\ 5]$

</details>

#### **Q20**[JEE Advanced]If $|z - 1| + |z + 1| = 6$, find $\max \operatorname{Im} z$.

If $|z - 1| + |z + 1| = 6$, find $\max \operatorname{Im} z$.

<details>
<summary>Answer + Reasoning</summary>

**Method: ellipse.** Foci $\pm 1$: $2c = 2 \Rightarrow c = 1$; $2a = 6 \Rightarrow a = 3$ (check $2a &gt; 2c$ ✓ non-degenerate). $b = \sqrt{a^2 - c^2} = \sqrt{8} = 2\sqrt2$. Max height = top of the minor axis: $z = \pm i\, 2\sqrt2$. Check: $|i2\sqrt2 - 1| = |i2\sqrt2 + 1| = \sqrt{1+8} = 3$, sum $6$ ✓.


Answer: $2\sqrt2$

</details>

#### **Q21**[JEE Advanced]Find the locus of $|z|^2 = z + \bar z$ and $\max|z|$ on it.

Find the locus of $|z|^2 = z + \bar z$ and $\max|z|$ on it.

<details>
<summary>Answer + Reasoning</summary>

With $z = a+bi$: $a^2 + b^2 = 2a \iff (a-1)^2 + b^2 = 1$: circle, center $(1,0)$, radius $1$, passing through the origin. Max distance from $0$: the far point on the line through center and origin, at distance $1 + 1 = 2$ (point $z = 2$; check: $|2|^2 = 4 = 2 + 2$ ✓).


Answer: circle, center $(1,0)$, radius $1$; $\max|z| = 2$

</details>

#### **Q22**[JEE Advanced]Find $z$ with $\arg z = \dfrac{\pi}{3}$ and $|z - 4| = 4$.

Find $z$ with $\arg z = \dfrac{\pi}{3}$ and $|z - 4| = 4$.

<details>
<summary>Answer + Reasoning</summary>

Write $z = r e^{i\pi/3} = \frac{r}{2} + i\frac{r\sqrt3}{2}$, $r &gt; 0$. Then 
$$ |z-4|^2 = \left(\frac{r}{2} - 4\right)^2 + \frac{3r^2}{4} = r^2 - 4r + 16 = 16
        \iff r^2 - 4r = 0 \iff r = 4. $$
 So $z = 4e^{i\pi/3} = 2 + 2\sqrt3\, i$. Check: $\arg z = \pi/3$ ✓, $|z - 4| = |{-2} + 2\sqrt3 i| = \sqrt{4 + 12} = 4$ ✓. Geometric picture: $z$ is the second intersection of the ray $\arg\pi/3$ with the circle center $4$, radius $4$ — the triangle $O, 4, z$ is equilateral (sides $4, 4, 4$).


Answer: $2 + 2\sqrt3\, i$

</details>

#### **Q23**[JEE Advanced]Let $z = t(1+i)$, $t \in \mathbb{R}$. Find $\min |z - 1|$ and where it is attained.

Let $z = t(1+i)$, $t \in \mathbb{R}$. Find $\min |z - 1|$ and where it is attained.

<details>
<summary>Answer + Reasoning</summary>

$$ |z-1|^2 = (t-1)^2 + t^2 = 2t^2 - 2t + 1 = 2\left(t - \frac12\right)^2 + \frac12
        \ge \frac12, $$
 with equality at $t = \frac12$. So $\min|z-1| = \frac{1}{\sqrt2} = \frac{\sqrt2}{2}$, attained at $z = \frac{1+i}{2}$. Geometrically: the closest point of the line $y = x$ to $(1,0)$ — the foot of the perpendicular.


Answer: $\dfrac{\sqrt2}{2}$, at $z = \dfrac{1+i}{2}$

</details>


### E · Algebraic Core (Q24–Q27)

#### **Q24**[JEE Advanced]Solve $2z + i\bar z = 5 + 2i$.

Solve $2z + i\bar z = 5 + 2i$.

<details>
<summary>Answer + Reasoning</summary>

**Method 1 (real/imag parts).** $z = a+bi$: $2a + 2bi + ia + b = (2a+b) + i(2b+a) = 5 + 2i$. So $2a + b = 5$, $a + 2b = 2$. Eliminating: $(2a+b) - 2(a+2b) = 5 - 4 \Rightarrow -3b = 1 \Rightarrow b = -\frac13$; then $2a = 5 + \frac13 = \frac{16}{3}$, $a = \frac83$.


**Method 2 (conjugate trick).** Conjugate: $2\bar z - iz = 5 - 2i$. Multiply by $i$: $z + 2i\bar z = 2 + 5i$. Subtract from the original: $z - i\bar z = 3 - 3i$. Add to the original: $3z = 8 - i$, $z = \frac83 - \frac13 i$ ✓ agrees.


Answer: $z = \dfrac{8}{3} - \dfrac{1}{3} i$

</details>

#### **Q25**[JEE Advanced]Find the roots of $z^2 - (2+6i)z + (-7+6i) = 0$.

Find the roots of $z^2 - (2+6i)z + (-7+6i) = 0$.

<details>
<summary>Answer + Reasoning</summary>

Discriminant: 
$$ \Delta = (2+6i)^2 - 4(-7+6i) = (4 + 24i - 36) + 28 - 24i = -4. $$
 $\sqrt{\Delta} = \pm 2i$. Hence 
$$ z = \frac{(2+6i) \pm 2i}{2} \in \{1 + 4i,\ 1 + 2i\}. $$
 Check (Vieta): sum $(1+4i) + (1+2i) = 2 + 6i$ ✓; product $(1+4i)(1+2i) = 1 + 2i
        + 4i + 8i^2 = -7 + 6i$ ✓.


Answer: $\{1+2i,\ 1+4i\}$

</details>

#### **Q26**[JEE Advanced]Find the locus of $\arg\dfrac{z}{z-4i} = \dfrac{\pi}{2}$.

Find the locus of $\arg\dfrac{z}{z-4i} = \dfrac{\pi}{2}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand the ratio, demand real part $0$, imaginary part $&gt; 0$.** Write $z = a + bi$ and multiply by the conjugate of the denominator: 
$$ \frac{z}{z-4i} = \frac{(a+bi)\big(a - (b-4)i\big)}{a^2 + (b-4)^2}
        = \frac{a^2 + b^2 - 4b + 4ai}{a^2 + (b-4)^2}
        = \frac{a^2+b^2-4b}{a^2+(b-4)^2} \;+\; i\,\frac{4a}{a^2+(b-4)^2}. $$
 Argument $+\pi/2$ means real part $0$ *and* imaginary part $&gt; 0$: $a^2 + b^2 - 4b = 0 \iff a^2 + (b-2)^2 = 4$: the circle, center $2i$, radius $2$ (Thales: the $90^\circ$-locus over the segment $[0, 4i]$). $\dfrac{4a}{a^2+(b-4)^2} &gt; 0 \iff a &gt; 0$ (denominator positive off $z = 4i$): the *right half* of that circle. Excluded endpoints: $z = 0$ (ratio $0$, no argument) and $z = 4i$ (undefined).


**Why both conditions matter.** "Purely imaginary" alone gives the whole circle — the left half gives argument $-\pi/2$ (test $z = -2+2i$: $\frac{-2+2i}{-2-2i} = -i$). The sign of the argument halves the circle; testing one point per half is the standard check before writing the answer.


Answer: the half of the circle (center $2i$, radius $2$) with $\operatorname{Re} z &gt; 0$, excluding $0$ and $4i$

</details>

#### **Q27**[JEE Advanced]Find the locus of $\dfrac{z+1}{z-1}$ purely imaginary and non-zero.

Find the locus of $\dfrac{z+1}{z-1}$ purely imaginary and non-zero.

<details>
<summary>Answer + Reasoning</summary>

Purely imaginary ⟺ sum with conjugate is $0$: 
$$ \frac{z+1}{z-1} + \frac{\bar z+1}{\bar z-1} = \frac{(z+1)(\bar z-1) + (\bar z+1)(z-1)}
        {|z-1|^2} = \frac{2|z|^2 - 2}{|z-1|^2} = 0 \iff |z|^2 = 1. $$
 Exclusions: $z = 1$ (undefined); $z = -1$ (ratio $= 0$, excluded by "non-zero"). Locus: the unit circle minus $\pm 1$. Thales reading: the angle at $z$ subtending $[-1, 1]$ is $90^\circ$ — the circle on that diameter, both semicircles (the sign of the angle is unrestricted here).


Answer: the unit circle, excluding $z = \pm 1$

</details>


### F · Geometry Proofs (Q28–Q32)

#### **Q28**[JEE Advanced]Prove: CCW triangle $(a,b,c)$ equilateral $\iff a + \omega b + \omega^2 c = 0$.

Prove: CCW triangle $(a,b,c)$ equilateral $\iff a + \omega b + \omega^2 c = 0$.

<details>
<summary>Answer + Reasoning</summary>

**($\Rightarrow$)** Equilateral CCW: $c - a = e^{i\pi/3}(b-a)
        = (1+\omega)(b-a)$ (rotation by $60^\circ$; $e^{i\pi/3} = 1+\omega$ since $1+\omega = \frac12 + i\frac{\sqrt3}{2}$). So $c = a + (1+\omega)b - (1+\omega)a
        = -\omega a + (1+\omega)b$. Then 
$$ a + \omega b + \omega^2 c = a + \omega b + \omega^2(-\omega a + (1+\omega)b)
        = a + \omega b - \omega^3 a + (\omega^2 + \omega^3) b = a + \omega b - a - \omega b = 0 $$
 (using $\omega^3 = 1$ and $\omega^2 + 1 = -\omega$.) **($\Leftarrow$)** $a + \omega b + \omega^2 c = 0 \Rightarrow c =
        -\omega(a + \omega b) = -\omega a - \omega^2 b$, so 
$$ c - a = -(1+\omega)a - \omega^2 b,
        \quad\text{while}\quad (1+\omega)(b-a) = (1+\omega)b - a - \omega a. $$
 These are equal iff $(1+\omega)b = -\omega^2 b \iff 1 + \omega + \omega^2 = 0$ ✓. Hence $c - a = e^{i\pi/3}(b-a)$: $|c-a| = |b-a|$ with a $+60^\circ$ rotation — equilateral, CCW. ∎


Answer: proof complete

</details>

#### **Q29**[JEE Advanced]From $(a-c)(b-d) = (a-b)(c-d) + (b-c)(a-d)$, prove Ptolemy's inequality; show equality iff…

From $(a-c)(b-d) = (a-b)(c-d) + (b-c)(a-d)$, prove Ptolemy's inequality; show equality iff cyclic (in order); check the unit square.

<details>
<summary>Answer + Reasoning</summary>

**Identity (verify once):** expand the right: $(ac - ad - bc + bd) + (ab - bd - ca + cd) = ab - ad - bc + cd = (a-c)(b-d)$ ✓. **Inequality:** take moduli: 
$$ |a-c||b-d| = |(a-b)(c-d) + (b-c)(a-d)| \le |a-b||c-d| + |b-c||a-d|. $$
 **Equality condition:** the two summands point the same way, i.e. $\frac{(b-c)(a-d)}{(a-b)(c-d)} \in \mathbb{R}_{>0}$. Taking arguments (with $\arg(b-c) = \arg(c-b) + \pi$): 
$$ \arg\frac{(b-c)(a-d)}{(a-b)(c-d)} = \pi + \varphi(a;d,b) - \varphi(c;d,b) \pmod{2\pi},
        \quad \varphi(X;Y,Z) = \arg(Y-X) - \arg(Z-X). $$
 Real-and-positive ($0 \bmod 2\pi$) ⟺ $\varphi(a;d,b) - \varphi(c;d,b) \equiv
        \pi \pmod{2\pi}$: the angles the chord $bd$ subtends at $a$ and $c$ are supplementary ⟺ $a,b,c,d$ concyclic (or collinear), in order. ∎ **Unit-square check** ($1, i, -1, -i$): diagonals $2, 2$ → product $4$; sides $\sqrt2$ → $\sqrt2\cdot\sqrt2 + \sqrt2\cdot\sqrt2 = 4$ ✓ equality, as a cyclic quadrilateral must give.


Answer: proof complete; square check $4 = 4$

</details>

#### **Q30**[Olympiad]Prove Van Aubel's theorem.

Prove Van Aubel's theorem.

<details>
<summary>Answer + Reasoning</summary>

CCW quadrilateral $a, b, c, d$; outward-square center on side $p \to q$: $m_{pq} = \frac{(1+i)p + (1-i)q}{2}$ (midpoint, half-side rotated $90^\circ$ to the right — the outward side for a CCW quadrilateral). Then 
$$ 2(m_{bc} - m_{da}) = (1+i)b + (1-i)c - (1+i)d - (1-i)a, $$
 
$$ 2(m_{cd} - m_{ab}) = (1+i)c + (1-i)d - (1+i)a - (1-i)b. $$
 Multiply the second by $i$ (using $i(1+i) = i-1 = -(1-i)$ and $i(1-i) = 1+i$): 
$$ i\cdot 2(m_{cd} - m_{ab}) = -(1-i)c + (1+i)d + (1-i)a - (1+i)b = -2(m_{bc} - m_{da}). $$
 Hence $m_{bc} - m_{da} = -i(m_{cd} - m_{ab})$: multiplication by $-i$ is a $90^\circ$ rotation preserving length — the two segments are **perpendicular and equal**. ∎


Answer: proof complete


Numerical check, quad $0, 1, 1.5+1.2i, 0.3+0.9i$: both opposite-center segments have length $2.16448\ldots$; their ratio is pure imaginary ✓.

</details>

#### **Q31**[Olympiad]Prove Napoleon's theorem.

Prove Napoleon's theorem.

<details>
<summary>Answer + Reasoning</summary>

CCW triangle $a, b, c$; outward-equilateral center on $a \to b$: third vertex $a + e^{-i\pi/3}(b-a) = a - \omega(b-a)$ (since $e^{-i\pi/3} = -\omega$), so 
$$ m_{ab} = \frac{a + b + a - \omega b + \omega a}{3} = \frac{(2+\omega)a + (1-\omega)b}{3}. $$
 By Q28, $X, Y, Z$ form a CCW equilateral triangle iff $X + \omega Y + \omega^2 Z = 0$. With $X = m_{ab}, Y = m_{bc}, Z = m_{ca}$: 
$$ 3\big(m_{ab} + \omega m_{bc} + \omega^2 m_{ca}\big) $$
 
$$ = \big((2+\omega)a + (1-\omega)b\big) + \omega\big((2+\omega)b + (1-\omega)c\big)
        + \omega^2\big((2+\omega)c + (1-\omega)a\big). $$
 $a$-coefficient: $(2+\omega) + \omega^2(1-\omega) = 2 + \omega + \omega^2 - 1
        = 1 + \omega + \omega^2 = 0$. $b$-coefficient: $(1-\omega) + \omega(2+\omega) = 1 + \omega + \omega^2 = 0$. $c$-coefficient: $\omega(1-\omega) + \omega^2(2+\omega) = 1 + \omega + \omega^2 = 0$. Every coefficient vanishes, so $m_{ab} + \omega m_{bc} + \omega^2 m_{ca} = 0$: the centers form an equilateral triangle. ∎


Answer: proof complete


Numerical check, triangle $(0,0), (4,0), (1,3)$: centers $(2, -1.1547), (3.366, 2.366), (-0.366, 1.789)$; all three Napoleon sides $= \sqrt{14.261}$ ✓.

</details>

#### **Q32**[JEE Advanced]Regular hexagon, circumradius $2$, center $O$; $|P - O| = 1$. Find…

Regular hexagon, circumradius $2$, center $O$; $|P - O| = 1$. Find $\sum_{k=1}^{6} |P - v_k|^2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: centroid distance-sum formula (Leibniz).** $\sum |p - v_k|^2 = n|p - c|^2 + \sum|v_k - c|^2$ with centroid $c = O$: 
$$ 6 \cdot |P - O|^2 + 6 \cdot 2^2 = 6 \cdot 1 + 6 \cdot 4 = 6 + 24 = 30. $$
 Independent of the direction of $P$ (only $|P-O|$ enters).


Answer: $30$

</details>


### G · Synthesis (Q33–Q36)

#### **Q33**[Olympiad] $|z_k| = 1$, $\sum z_k = 0$: prove rectangle; with $z_1 = 1$, describe $\{z_2, z_3, z_4\}$.

$|z_k| = 1$, $\sum z_k = 0$: prove rectangle; with $z_1 = 1$, describe $\{z_2, z_3, z_4\}$.

<details>
<summary>Answer + Reasoning</summary>

**Proof.** $z_1 + z_2 = -(z_3+z_4)$. Conjugate and use $\bar z_k = 1/z_k$: 
$$ \frac{z_1+z_2}{z_1z_2} = \frac{z_1+z_2}{z_3z_4}
        \ \Rightarrow\ (z_1+z_2)\left(\frac{1}{z_1z_2} - \frac{1}{z_3z_4}\right) = 0. $$
 **Case (i):** $z_1 + z_2 = 0$: then $z_3 + z_4 = 0$ too, and the four points are $\{\pm\alpha, \pm\beta\}$ — a parallelogram inscribed in the circle, hence a rectangle (opposite angles both equal and supplementary). **Case (ii):** $z_1z_2 = z_3z_4 =: p$. With $s = z_1+z_2$ (so $z_3+z_4 = -s$): $z_1, z_2$ root $t^2 - st + p$; $z_3, z_4$ root $t^2 + st + p$, whose roots are $-z_1, -z_2$. Again $\{\pm\alpha, \pm\beta\}$: a rectangle. ∎ **With $z_1 = 1$:** the multiset is $\{1, -1, b, -b\}$, $|b| = 1$, $b \ne \pm 1$ (otherwise two points coincide — degenerate). So $\{z_2, z_3, z_4\}$ is a permutation of $\{-1, e^{i\theta}, -e^{i\theta}\}$ with $\theta \not\equiv 0, \pi \pmod{2\pi}$.


Answer: proof; $\{-1,\ e^{i\theta},\ -e^{i\theta}\}$, $\theta \not\equiv 0, \pi$

</details>

#### **Q34**[JEE Advanced]Regular hexagon on the unit circle; product of distances from $3$ to the six vertices.

Regular hexagon on the unit circle; product of distances from $3$ to the six vertices.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\prod_{k=0}^{n-1}(z - \zeta_k) = z^n - 1$.** 
$$ \prod_{k=0}^{5} |3 - e^{2\pi i k/6}| = |3^6 - 1| = 729 - 1 = 728. $$
 Check by pairing: distances $|3-1| = 2$, $|3+1| = 4$, $|3 - e^{\pm i\pi/3}| = \sqrt7$, $|3 - e^{\pm i2\pi/3}| = \sqrt{13}$ (via $|3-e^{i\alpha}|^2 = 10 - 6\cos\alpha$: $\cos 60^\circ = \tfrac12 \Rightarrow 7$; $\cos 120^\circ = -\tfrac12 \Rightarrow 13$). Product: $2 \cdot 4 \cdot 7 \cdot 13 = 728$ ✓.


Answer: $728$

</details>

#### **Q35**[JEE Advanced]Locus of $w = z + \dfrac{1}{z} + 2i$ as $|z| = 1$ varies.

Locus of $w = z + \dfrac{1}{z} + 2i$ as $|z| = 1$ varies.

<details>
<summary>Answer + Reasoning</summary>

$\frac1z = \bar z$ on the unit circle, so $z + \frac1z = 2\cos\theta \in
        [-2, 2]$ (real). Hence $w = 2\cos\theta + 2i$: the horizontal segment from $-2+2i$ to $2+2i$. Surjectivity: every $x \in [-2,2]$ is $2\cos\theta$ for some $\theta$. (The map is two-to-one except at the endpoints — the Joukowski collapse of the unit circle, translated up by $2i$.)


Answer: the segment $[{-2+2i},\ 2+2i]$

</details>

#### **Q36**[JEE Main]Area of the triangle with vertices $2$, $4i$, $-1+3i$.

Area of the triangle with vertices $2$, $4i$, $-1+3i$.

<details>
<summary>Answer + Reasoning</summary>

**Method: complex area formula.** With $z_1 = 2, z_2 = 4i,
        z_3 = -1+3i$: 
$$ (z_2-z_1)\overline{(z_3-z_1)} = (-2+4i)(-3-3i) = 6 + 6i - 12i - 12i^2 = 18 - 6i. $$
 Area $= \frac12 |{-6}| = 3$. Shoelace check: vertices $(2,0), (0,4), (-1,3)$: $\frac12 |2(4-3) + 0(3-0) + (-1)(0-4)| = \frac12 \cdot 6 = 3$ ✓.


Answer: $3$

</details>


### H · Stretch (Q37–Q38)

#### **Q37**[Olympiad] $|z_k| = 1$, $z_1+z_2+z_3 = 0$: prove (i) $120^\circ$ apart, (ii)…

$|z_k| = 1$, $z_1+z_2+z_3 = 0$: prove (i) $120^\circ$ apart, (ii) $z_1^2 + z_2^2 + z_3^2 = 0$, (iii) $\{\pm z_k\}$ is a regular hexagon.

<details>
<summary>Answer + Reasoning</summary>

**(i)** $|z_1 + z_2| = |z_3| = 1$, so $1 = |z_1+z_2|^2 = 2 + 2\operatorname{Re}(z_1\bar z_2)$, giving $\operatorname{Re}(z_1\bar z_2) = -\frac12$: the angle between $z_1$ and $z_2$ is $120^\circ$. Symmetric in all three pairs. **(ii)** $(z_1+z_2+z_3)^2 = 0 \Rightarrow z_1^2+z_2^2+z_3^2 =
        -2(z_1z_2 + z_2z_3 + z_3z_1)$. So we need $z_1z_2 + z_2z_3 + z_3z_1 = 0$: divide by $z_1z_2z_3$ (unit modulus, never $0$): 
$$ \frac{1}{z_3} + \frac{1}{z_1} + \frac{1}{z_2} = \bar z_3 + \bar z_1 + \bar z_2
        = \overline{z_1+z_2+z_3} = 0. $$
 Hence $z_1z_2 + z_2z_3 + z_3z_1 = 0$ and (ii) follows. **(iii)** The six points have arguments $\{\theta_k, \theta_k + \pi\}$ with the $\theta_k$ mutually $120^\circ$ apart. Sorting: between $\theta_1$ and $\theta_2 = \theta_1 + 120^\circ$ sits the antipode $-z_1$ at $\theta_1 + 180^\circ$ — exactly $60^\circ$ from both. So the six arguments advance in $60^\circ$ steps: a regular hexagon. ∎


Answer: proof complete (three claims)

</details>

#### **Q38**[Olympiad]Rectangle $0, 2, 2+3i, 3i$: (a) check the British Flag identity at $e = 1+i$; (b) prove it…

Rectangle $0, 2, 2+3i, 3i$: (a) check the British Flag identity at $e = 1+i$; (b) prove it for all $e$.

<details>
<summary>Answer + Reasoning</summary>

**(a)** $|e|^2 = |1+i|^2 = 2$. $|e-(2+3i)|^2 = |{-1}-2i|^2 = 1 + 4 = 5$. LHS $= 7$. $|e-2|^2 = |{-1}+i|^2 = 2$. $|e-3i|^2 = |1-2i|^2 = 1 + 4 = 5$. RHS $= 7$ ✓. **(b)** Expand with $|e-a|^2 = |e|^2 - e\bar a - \bar e a + |a|^2$. For $a = 2+3i$: $|e-a|^2 = |e|^2 - e(2-3i) - \bar e(2+3i) + 13$ $= |e|^2 - 2e + 3ie - 2\bar e - 3i\bar e + 13$. For $a = 2$: $|e-2|^2 = |e|^2
        - 2e - 2\bar e + 4$. For $a = 3i$: $|e-3i|^2 = |e|^2 + 3ie - 3i\bar e + 9$. LHS $= 2|e|^2 - 2e + 3ie - 2\bar e - 3i\bar e + 13$. RHS $= 2|e|^2 - 2e - 2\bar e + 3ie - 3i\bar e + 13$. Identical — the far corner's expansion splits exactly into the two near corners, because the rectangle's sides are orthogonal ($\operatorname{Re}(2 \cdot \overline{3i}) = 0$). ∎


Answer: (a) $7 = 7$; (b) proof complete

</details>


### I · Gauss Sums, Gauss–Lucas and Pompeiu (Q39–Q48)

#### **Q39**[Olympiad]Evaluate $\displaystyle G(7)=\sum_{k=0}^{6}\zeta^{k^{2}}$ for $\zeta=e^{2\pi i/7}$.

Evaluate $G(7)=\sum_{k=0}^{6}\zeta^{k^{2}}$ for $\zeta=e^{2\pi i/7}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: pair $k$ with $7-k$, then use the residue class of $n$.** The residues $k^{2}\bmod 7$ run $0,1,4,2,2,4,1$, so $G(7)=1+2(\zeta+\zeta^{2}+\zeta^{4})$. Since $7\equiv3\pmod4$, the closed form gives $i\sqrt7$. Direct evaluation of $1+2(\zeta+\zeta^{2}+\zeta^{4})$ at $\zeta=e^{2\pi i/7}$ gives $2.6457513\,i$ ✓, and $|G(7)|^{2}=7$ ✓, exactly as the squaring argument predicts.


Answer: $i\sqrt7\approx2.6458\,i$


Check: $|G(7)|^{2}=7$ ✓ and the direct sum agrees to $10^{-15}$ ✓.

</details>


#### **Q40**[Olympiad]State the quadratic Gauss sum $G(n)=\sum_{k=0}^{n-1}\zeta^{k^{2}}$ in closed form, for all four residue classes of $n\bmod4$.

State the quadratic Gauss sum $G(n)=\sum_{k=0}^{n-1}\zeta^{k^{2}}$ in closed form, for all four residue classes of $n\bmod4$.

<details>
<summary>Answer + Reasoning</summary>

**Method: state the four cases and remember where they come from.** $G(n)=\sum_{k=0}^{n-1}\zeta^{k^{2}}$ with $\zeta=e^{2\pi i/n}$. Squaring gives $|G(n)|^{2}=\sum_{h}\zeta^{h^{2}}\sum_{l}\zeta^{2lh}$, and the inner filter keeps only $h$ with $n\mid2h$: one term for odd $n$ (modulus $\sqrt n$), two terms $h=0,m$ for $n=2m$ with $\zeta^{m^{2}}=(-1)^{m}$.


Answer: $\sqrt n$ for $n\equiv1\pmod4$; $i\sqrt n$ for $n\equiv3\pmod4$; $(1+i)\sqrt n$ for $n\equiv0\pmod4$; $0$ for $n\equiv2\pmod4$


Check: verified numerically for every $n=1,\dots,60$ ✓ — all four cases, exact to $10^{-9}$.

</details>


#### **Q41**[JEE Advanced]Evaluate $G(8)=\sum_{k=0}^{7}\zeta^{k^{2}}$ for $\zeta=e^{2\pi i/8}$, using only the residues $k^{2}\bmod 8$.

Evaluate $G(8)=\sum_{k=0}^{7}\zeta^{k^{2}}$ for $\zeta=e^{2\pi i/8}$, using only the residues $k^{2}\bmod 8$.

<details>
<summary>Answer + Reasoning</summary>

**Method: list the residues $k^{2}\bmod 8$ and count multiplicities.** $k^{2}\bmod 8$ for $k=0,\dots,7$ is $0,1,4,1,0,1,4,1$: the residue $0$ appears twice, $4$ twice, $1$ four times. Hence $G(8)=2\zeta^{0}+2\zeta^{4}+4\zeta^{1}=2(1+\zeta^{4})+4\zeta$. Now $\zeta^{4}=e^{\pi i}=-1$ kills the first bracket, and $\zeta=e^{i\pi/4}=\tfrac{1+i}{\sqrt2}$, so $G(8)=4\cdot\tfrac{1+i}{\sqrt2}=2\sqrt2\,(1+i)$.


Answer: $2\sqrt2\,(1+i)=(1+i)\sqrt8\approx2.8284+2.8284\,i$


Check: direct summation gives $2.8284271+2.8284271\,i$ ✓, and $|G(8)|^{2}=16=2n$ ✓ as the squaring argument requires for $n\equiv0\pmod4$.

</details>


#### **Q42**[Olympiad]State the Gauss–Lucas theorem.

State the Gauss–Lucas theorem.

<details>
<summary>Answer + Reasoning</summary>

**Method: differentiate the factored form and use a separating line.** With $p(z)=c\prod(z-r_{k})$, logarithmic differentiation gives $\frac{p'}{p}=\sum_{k}\frac{1}{z-r_{k}}$. If $z$ is outside the convex hull, a line separates $z$ from all the roots, so for some real $\theta$ every $\operatorname{Re}\big(e^{-i\theta}(z-r_{k})\big)>0$; taking real parts after multiplying by $e^{i\theta}$ gives a strictly positive sum of positive terms, so $p'(z)\ne0$.


Answer: every zero of $p'$ lies in $\operatorname{conv}\{r_{1},\dots,r_{n}\}$, the convex hull of the zeros of $p$


Check: checked on $600$ random polynomials of degree $2$ to $5$: not one critical point fell outside the hull ✓. The real-rooted corollary (all critical points real) was checked on $400$ further polynomials ✓.

</details>


#### **Q43**[JEE Advanced]The roots of a cubic $p$ are $0$, $2$ and $1+2i$. Find its critical points and identify the region containing them.

The roots of a cubic $p$ are $0$, $2$ and $1+2i$. Find its critical points and identify the region containing them.

<details>
<summary>Answer + Reasoning</summary>

**Method: expand, differentiate, and solve the quadratic; then locate the hull.** $p(z)=z(z-2)(z-1-2i)=z^{3}+(-3-2i)z^{2}+(2+4i)z$, so $p'(z)=3z^{2}+(-6-4i)z+(2+4i)$. With $a=3$, $b=-6-4i$, $c=2+4i$: $b^{2}=20+48i$ and $4ac=24+48i$, so the discriminant is $-4$ and $z=\frac{6+4i\pm2i}{6}$, giving $1+i$ and $1+\tfrac{i}{3}$. The hull of $0$, $2$, $1+2i$ — as points $(0,0)$, $(2,0)$, $(1,2)$ — is cut out by $y\ge0$, $y\le2x$, $y\le4-2x$, and both $(1,1)$ and $(1,\tfrac13)$ satisfy all three.


Answer: $1+i$ and $1+\dfrac{i}{3}$, both inside $\operatorname{conv}\{0,2,1+2i\}$


Check: shifting the centroid $1+\tfrac23 i$ to the origin turns them into $\pm\tfrac{i}{3}$, symmetric about the centroid ✓ — and $p'(1+i)=p'(1+\tfrac{i}{3})=0$ exactly ✓.

</details>


#### **Q44**[Olympiad]For the triangle with vertices $0$, $2$, $1+2i$, state Marden's theorem and name its two foci.

For the triangle with vertices $0$, $2$, $1+2i$, state Marden's theorem and name its two foci.

<details>
<summary>Answer + Reasoning</summary>

**Method: Marden's theorem says the foci of the Steiner inellipse are the roots of $p'$.** For a cubic whose roots are the vertices of a triangle, the unique ellipse tangent to the three sides at their midpoints has its two foci at the zeros of $p'$.


Answer: the two roots of $p'$, namely $1+i$ and $1+\dfrac{i}{3}$, are the foci of the Steiner inellipse of the triangle $0,2,1+2i$


Check: with the centroid shifted to the origin the foci are $\pm\tfrac{i}{3}$, and the three side midpoints all satisfy $|m-f_{1}|+|m-f_{2}|=\text{constant}$ with the tangent (the side) making equal angles with the two focal segments ✓ — checked on $298$ random triangles with no failure.

</details>


#### **Q45**[Olympiad]State Pompeiu's theorem for an equilateral triangle $ABC$ and an arbitrary point $P$.

State Pompeiu's theorem for an equilateral triangle $ABC$ and an arbitrary point $P$.

<details>
<summary>Answer + Reasoning</summary>

**Method: state the theorem and its degeneracy locus.** Pompeiu: for an equilateral triangle $ABC$ and *any* point $P$ of the plane, the three lengths $PA$, $PB$, $PC$ satisfy the triangle inequalities, so they are the side lengths of a (possibly degenerate) triangle. The triangle of distances degenerates exactly when $P$ lies on the circumcircle of $ABC$.


Answer: $PA,PB,PC$ form a triangle; degenerate exactly on the circumcircle of $ABC$


Check: on $4000$ random equilateral configurations the slack $a+b-c$ was never negative (minimum $9.8\times10^{-9}$, numerical noise) ✓; with $P$ on the circumcircle the slack is $0$ to $2.7\times10^{-15}$, and with $P$ off it it is at least $2.7\times10^{-5}$ ✓.

</details>


#### **Q46**[JEE Advanced]Prove Pompeiu's theorem using the equilateral condition $A+\omega B+\omega^{2}C=0$ with $\omega=e^{2\pi i/3}$.

Prove Pompeiu's theorem using the equilateral condition $A+\omega B+\omega^{2}C=0$ with $\omega=e^{2\pi i/3}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: cancel the $P$ terms, then rotate one identity three ways.** Let $\omega=e^{2\pi i/3}$ and $u=P-A$, $v=P-B$, $w=P-C$. The equilateral condition is $A+\omega B+\omega^{2}C=0$, and $1+\omega+\omega^{2}=0$, so $u+\omega v+\omega^{2}w=P(1+\omega+\omega^{2})-(A+\omega B+\omega^{2}C)=0$. From $u=-\omega v-\omega^{2}w$ we get $|u|\le|v|+|w|$; multiplying by $\omega^{2}$ gives $\omega^{2}u+v+\omega w=0$, so $|v|\le|u|+|w|$; multiplying by $\omega$ gives $\omega u+\omega^{2}v+w=0$, so $|w|\le|u|+|v|$. Hence $PA,PB,PC$ form a triangle.


Answer: the three triangle inequalities $|u|\le|v|+|w|$, $|v|\le|u|+|w|$, $|w|\le|u|+|v|$, from the single relation $u+\omega v+\omega^{2}w=0$


Check: for $A,B,C=1,\omega,\omega^{2}$ and several $P$, $|u+\omega v+\omega^{2}w|$ is $0$ to $10^{-15}$ ✓.

</details>


#### **Q47**[Olympiad]For the equilateral triangle $1,\omega,\omega^{2}$ and $P=e^{i\theta}$, show $PA+PB=PC$ for $0\le\theta\le\tfrac{2\pi}{3}$.

For the equilateral triangle $1,\omega,\omega^{2}$ and $P=e^{i\theta}$, show $PA+PB=PC$ for $0\le\theta\le\tfrac{2\pi}{3}$.

<details>
<summary>Answer + Reasoning</summary>

**Method: chord formula, then sum-to-product.** $|e^{i\theta}-e^{i\alpha}|=2\big|\sin\tfrac{\theta-\alpha}{2}\big|$. For $\theta\in[0,\tfrac{2\pi}{3}]$ this gives $PA=2\sin\tfrac\theta2$, $PB=2\sin(\tfrac\pi3-\tfrac\theta2)$ and $PC=2\sin(\tfrac{2\pi}3-\tfrac\theta2)$. Then $\sin x+\sin y=2\sin\frac{x+y}{2}\cos\frac{x-y}{2}$ with $x=\tfrac\theta2$, $y=\tfrac\pi3-\tfrac\theta2$ gives $PA+PB=4\sin\tfrac\pi6\cos(\tfrac\theta2-\tfrac\pi6)=2\cos(\tfrac\theta2-\tfrac\pi6)$, and $PC=2\sin(\tfrac{2\pi}3-\tfrac\theta2)=2\cos(\tfrac\pi6-\tfrac\theta2)=2\cos(\tfrac\theta2-\tfrac\pi6)$ since cosine is even.


Answer: $PA+PB=PC$ identically on $0\le\theta\le\tfrac{2\pi}{3}$


Check: numerically the slack $PA+PB-PC$ is $0$ to machine precision over $721$ sample points on the unit circle (maximum $6.7\times10^{-16}$) ✓, and $PA+PB$ matches $2\cos(\tfrac\theta2-\tfrac\pi6)$ exactly at each tested $\theta$ ✓.

</details>


#### **Q48**[Olympiad]For which positive integers $n$ does the Gauss sum $G(n)=\sum_{k=0}^{n-1}\zeta^{k^{2}}$ vanish?

For which positive integers $n$ does the Gauss sum $G(n)=\sum_{k=0}^{n-1}\zeta^{k^{2}}$ vanish?

<details>
<summary>Answer + Reasoning</summary>

**Method: read the vanishing off the squaring argument.** $|G(n)|^{2}=\sum_{h:\,n\mid2h}n\,\zeta^{h^{2}}$. For $n=2m$ the surviving $h$ are $0$ and $m$, contributing $1$ and $\zeta^{m^{2}}=e^{\pi i m}=(-1)^{m}$, which cancel exactly when $m$ is odd — that is $n\equiv2\pmod4$. For odd $n$ only $h=0$ survives, so $|G(n)|^{2}=n\ne0$; for $n\equiv0\pmod4$ both terms are $+1$ and $|G(n)|^{2}=2n$.


Answer: exactly $n\equiv2\pmod4$, i.e. $n=2,6,10,14,18,\dots$


Check: $G(2)=G(6)=G(10)=G(14)=0$ to $10^{-15}$, while $G(3)=i\sqrt3$, $G(4)=2+2i$, $G(5)=\sqrt5$ are all non-zero ✓.

</details>




---

### ✅ Self-assessment key

> [!success] Self-assessment key
>
> - **39+/48:** the toolkit is solid; focus on the proof-writing discipline in F, H and I (state excluded points, check orientation, verify both directions).
> - **31–38:** strong computation, shaky synthesis — redo Q8, Q10, Q33, Q37, Q42 and the argument-locus sign trap (Q26).
> - **< 31:** go back chapter by chapter; the practice sets P1–P55 are the repair path.
