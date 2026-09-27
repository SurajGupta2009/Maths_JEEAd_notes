---
title: "Chapter 4 — JEE Advanced Core"
aliases:
  - JEE Advanced Core
  - Ch 4 — JEE Advanced Core
module: "Complex-Numbers"
module_title: "Complex Numbers"
chapter: 4
level: applications
tags:
  - complex-numbers
  - chapter
  - applications
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Complex-Numbers|Complex Numbers]] · ⬅ [[03-roots-of-unity|Chapter 3]] · [[05-geometry-via-complex-numbers|Chapter 5]] ➡ · 📝 [[Complex-Numbers — Paper|Olympiad Paper]] · ✅ [[Complex-Numbers — Solutions|Solutions]]

# Chapter 4 — JEE Advanced Core

*7 sections · 11 questions*

*Chapter 4 of 6*

# JEE Advanced Core — Loci & Optimization

Where the toolkit of Chapters 1–3 meets the JEE Advanced question sheet. Two families dominate this chapter: *loci* — the set of all $z$ satisfying a modulus or argument condition (circles and arcs, always) — and *optimization* — the range of $|z - a|$ under a constraint on $z$. Every method below reduces, in the end, to one of three moves: separate real and imaginary parts, use the triangle inequality with an equality condition, or rotate the picture.

### 4.1 Solving equations that mix $z$ and $\bar z$

Chapters 1–3 assumed the equation was "pure" in $z$ (like $z^2 = -4$). JEE questions instead mix $z$ and its conjugate: $2z + i\bar z = 5 + 2i$. Two systematic methods exist; you should be able to do both, and use the second as a check on the first.

> [!tip] Method 1 — real and imaginary parts (always works)
>
> Write $z = a + bi$, so $\bar z = a - bi$, expand, and equate real and imaginary parts. Two real linear equations in $a, b$. Mechanical, bulletproof, and the method to reach for under exam pressure.

> [!tip] Method 2 — the conjugate trick (fast, for linear equations)
>
> If the equation is *linear* in $z$ and $\bar z$, say $\alpha z + \beta \bar z = c$, then conjugating the whole equation gives $\bar\alpha \bar z + \bar\beta z = \bar c$ — a *second* linear equation in the same two unknowns $z, \bar z$. Solve the 2×2 system for $z$. No expansion into $a, b$ needed.

#### **P29**[JEE Advanced][z & z̄ equations]Solve [formula] .

Solve $2z + i\bar z = 5 + 2i$.

<details>
<summary>Answer + Reasoning</summary>

**Method 1.** $z = a + bi$: $2(a+bi) + i(a-bi) = 2a + 2bi + ia + b
        = (2a + b) + i(2b + a) = 5 + 2i$. So 
$$ 2a + b = 5, \qquad a + 2b = 2. $$
 Eliminate: $2a + b = 5$ minus $2(a + 2b = 2)$, i.e. $(2a+b) - 2(a+2b) = 5 - 4$ gives $-3b = 1$, so $b = -\tfrac13$, and then $2a = 5 - b = 5 + \tfrac13 = \tfrac{16}{3}$, $a = \tfrac83$.


**Method 2.** Conjugate the equation — remembering $\bar i = -i$: 
$$ \overline{2z + i\bar z} = 2\bar z - iz = 5 - 2i. $$
 Multiply this by $i$ so the coefficients of $z$ and $\bar z$ line up with the original equation: $i\cdot 2\bar z = 2i\bar z$, $i\cdot(-iz) = z$, $i(5-2i) = 2 + 5i$, giving 
$$ z + 2i\bar z = 2 + 5i. $$
 Subtract from $2z + i\bar z = 5 + 2i$: 
$$ z - i\bar z = (5+2i) - (2+5i) = 3 - 3i. $$
 Add to $2z + i\bar z = 5 + 2i$: the $\bar z$ terms cancel, $3z = 8 - i$, so $z = \tfrac83 - \tfrac13 i$ — same as Method 1 ✓.


Answer: $z = \dfrac{8}{3} - \dfrac{1}{3}\, i$


Lesson baked in: Method 2 is faster but has a sign trap in the conjugation step; Method 1 is slower and cannot be argued with. Know both, verify one with the other.

</details>


### 4.2 Quadratic equations and complex-conjugate roots

Real-coefficient quadratics with negative discriminant have complex-conjugate roots — and JEE loves to ask about *quantities built from* the roots (moduli of differences, sums of moduli, etc.) without ever naming them. The standard move: Vieta + conjugation.

#### **P30**[JEE Advanced][quadratics]Let [formula] be the roots of [formula] . Find [formula] and [formula] .

Let $z_1, z_2$ be the roots of $x^2 - 4x + 13 = 0$. Find $|z_1 - \bar z_1|$ and $|z_1 - z_2|$.

<details>
<summary>Answer + Reasoning</summary>

Discriminant: $16 - 52 = -36$, so $z_{1,2} = \frac{4 \pm 6i}{2} = 2 \pm 3i$. Take $z_1 = 2 + 3i$: $z_1 - \bar z_1 = (2+3i) - (2-3i) = 6i$, so $|z_1 - \bar z_1| = 6$. And $z_1 - z_2 = 6i$, so $|z_1 - z_2| = 6$ too. (For conjugate roots the two distances coincide: $|z_1 - z_2| = |z_1 - \bar z_1|$ because $z_2 = \bar z_1$.)


Answer: $6$ and $6$

</details>

The general fact worth naming: for $x^2 + bx + c = 0$ with $\Delta = b^2 - 4c < 0$, the roots are $\tfrac{-b}{2} \pm i\tfrac{\sqrt{4c-b^2}}{2}$, so $|z_1 - z_2| = \sqrt{4c - b^2}$ and $|z_1 - \bar z_1| = \sqrt{4c-b^2}$ — one formula, no root-finding needed. (Here: $\sqrt{52-16} = 6$ ✓.)


### 4.3 Loci from modulus conditions — circles

The condition $|z - a| = r$ *is* the circle centered at $a$ with radius $r$; the JEE skill is recognizing circle-conditions that are *disguised*.

#### **P38**[JEE Advanced][locus → circle]Find the locus of [formula] satisfying [formula] . Show it is a circle and fin…

Find the locus of $z$ satisfying $|z|^2 = z + \bar z$. Show it is a circle and find the maximum of $|z|$ on it.

<details>
<summary>Answer + Reasoning</summary>

Write $z = a + bi$. Then $|z|^2 = a^2 + b^2$ and $z + \bar z = 2a$, so the condition is $a^2 + b^2 = 2a$, i.e. 
$$ a^2 - 2a + b^2 = 0 \iff (a-1)^2 + b^2 = 1. $$
 Circle, center $1$ (i.e. $(1,0)$), radius $1$. It passes through the origin — and that is the key: the farthest point from $0$ on the circle is the point on the line from $0$ through the center $(1,0)$, at distance $1 + 1 = 2$.


Answer: circle, center $(1,0)$, radius $1$; $\max|z| = 2$

</details>

#### **P39**[JEE Advanced][pure imaginary]Find the locus of [formula] for which [formula] is purely imaginary.

Find the locus of $z$ for which $\dfrac{z+1}{z-1}$ is purely imaginary.

<details>
<summary>Answer + Reasoning</summary>

A number is purely imaginary iff its sum with its conjugate is $0$: 
$$ \frac{z+1}{z-1} + \overline{\left(\frac{z+1}{z-1}\right)} = 0
        \iff \frac{z+1}{z-1} + \frac{\bar z+1}{\bar z-1} = 0. $$
 Combine: $\dfrac{(z+1)(\bar z-1) + (\bar z+1)(z-1)}{(z-1)(\bar z-1)} = 0$. The numerator is $(|z|^2 - z + \bar z - 1) + (|z|^2 + z - \bar z - 1) = 2|z|^2 - 2$. So the condition is $|z|^2 = 1$, with $z \ne 1$ (the fraction is undefined) — and $z = -1$ gives $\frac{0}{-2} = 0$, purely imaginary, so $z = -1$ stays.


Answer: the unit circle, $z \ne 1$


Geometric reading (the deeper reason): $\arg\frac{z+1}{z-1}$ is the angle $\angle(z+1, z-1)$ at the point $z$ — "purely imaginary" means that angle is $90^\circ$, and the locus of points from which the segment $[-1, 1]$ is seen at a right angle is the circle on that segment as diameter (Thales). The circle on diameter $[-1,1]$ is exactly the unit circle. Algebra and geometry give the same answer — that agreement is the check.

</details>


### 4.4 Loci from argument conditions — arcs of circles

The condition $\arg\dfrac{z-a}{z-b} = \theta$ (fixed $\theta$, $0 < |\theta| < \pi$) is the statement "the angle $\angle azb$, measured at $z$, equals $|\theta|$". By the inscribed-angle theorem, the locus is an *arc of a circle* through $a$ and $b$: the chord $ab$ subtends angle $|\theta|$ at the arc. Two arcs qualify (one on each side of the chord); the sign of $\theta$ selects which one (orientation).

> [!abstract] First Principles — the construction, from scratch
>
> Given $a, b$ and $\theta$: the radius of the circle is $R = \dfrac{|a-b|}{2\sin|\theta|}$ (sine rule in the triangle with chord $ab$ and inscribed angle $|\theta|$), and its center $C$ lies on the perpendicular bisector of $ab$, at distance $\dfrac{|a-b|}{2}\cot|\theta|$ from the midpoint, on the side that makes the inscribed angle $|\theta|$. The actual locus is the arc of that circle from $a$ to $b$ *opposite* the center (major arc if $|\theta| < \pi/2$), excluding $a$ and $b$ themselves (the fraction is $0$ or undefined there).

#### **P34**[JEE Advanced][argument locus]Find the locus of [formula] satisfying [formula] . Verify a point on it.

Find the locus of $z$ satisfying $\arg\dfrac{z-1}{z+1} = \dfrac{\pi}{4}$. Verify a point on it.

<details>
<summary>Answer + Reasoning</summary>

Here $a = 1$, $b = -1$, $|\theta| = \pi/4$. Chord length $|a-b| = 2$, so 
$$ R = \frac{2}{2\sin\pi/4} = \frac{1}{\sin\pi/4} = \sqrt2, $$
 and the center is on the perpendicular bisector of $[-1,1]$ (the imaginary axis) at distance $\tfrac{2}{2}\cot\frac{\pi}{4} = 1$ from the midpoint $0$ — i.e. $C = i$. The circle is $|z - i| = \sqrt2$, i.e. $x^2 + (y-1)^2 = 2$. Which arc? The angle at $z$ is $+45^\circ$ (counterclockwise from the ray $zb$ to the ray $za$… orientation: $\arg\frac{z-1}{z+1}$ is the angle from $z+1$ to $z-1$), and a test point settles the side. Take $z = i(1+\sqrt2)$ (the top of the circle): $z - 1 = -1 + i(1+\sqrt2)$, $z + 1 = 1 + i(1+\sqrt2)$. With $1+\sqrt2 = \tan\frac{3\pi}{8}$: $\arg(z+1) = \frac{3\pi}{8}$, $\arg(z-1) = \pi - \frac{3\pi}{8} = \frac{5\pi}{8}$, so $\arg\frac{z-1}{z+1} = \frac{5\pi}{8} - \frac{3\pi}{8} = \frac{\pi}{4}$ ✓ — the top of the circle works, so the locus is the **upper arc** ($y &gt; 0$), with the endpoints $\pm 1$ excluded.


Answer: arc of $x^2 + (y-1)^2 = 2$, $y &gt; 0$, excluding $\pm 1$


Note the $\tan\frac{3\pi}{8} = \sqrt2 + 1$ — a standard value worth knowing (it is $\cot\frac{\pi}{8}$, from the half-angle formulas for $45^\circ$).

</details>

C = i −1 1 z = i(1+√2) O $\arg\frac{z-1}{z+1} = \frac{\pi}{4}$: the upper arc of the circle $|z-i| = \sqrt2$ (dashed: the rest of the circle), endpoints $\pm 1$ excluded. The marked point $z = i(1+\sqrt2)$ verifies the angle.


### 4.5 Optimization — the range of $|z - a|$ under constraints

The workhorse of this chapter. Three results, in increasing power:

> [!info] (A) Triangle inequality, with the equality condition
>
> $|z - a| \ge \big||z| - |a|\big|$ — and equality iff $z$ and $a$ point in the *same direction* (one is a positive real multiple of the other). This is the only tool you need for "minimum of $|z-a|$ given $|z| = 1$" and its cousins.

> [!info] (B) Minimum on the unit circle
>
> If $|z| = 1$ and $a \ne 0$: 
> $$ \min |z - a| = \big||a| - 1\big|, \qquad \text{attained at } z = \frac{a}{|a|}
>       \ (\text{the unit vector pointing at } a). $$
>  Proof: $|z - a| \ge ||a| - |z|| = ||a|-1|$, with equality at $z = a/|a|$ (same direction as $a$, modulus 1). Similarly $\max |z-a| = |a| + 1$ at $z = -a/|a|$.

> [!info] (C) Chord distances between two unit complex numbers
>
> If $|z| = |w| = 1$, then 
> $$ |z - w|^2 = (z-w)(\bar z - \bar w) = 2 - z\bar w - \bar z w = 2 - 2\operatorname{Re}(z\bar w), $$
>  so $|z-w|$ depends only on the angle between $z$ and $w$: $|z - w| = 2\left|\sin\frac{\varphi}{2}\right|$ where $\varphi = \arg(w/z)$. In particular, $|z - w| = \sqrt2$ iff $\varphi = \pm \pi/2$, i.e. iff $z\bar w = \pm i$.

#### **P32**[JEE Advanced][min on |z|=1]If [formula] , find [formula] and the [formula] where it occurs.

If $|z| = 1$, find $\min |z - (1-2i)|$ and the $z$ where it occurs.

<details>
<summary>Answer + Reasoning</summary>

By (B) with $a = 1-2i$: $|a| = \sqrt5 &gt; 1$, so $\min |z-a| = \sqrt5 - 1$, attained at $z = \dfrac{a}{|a|} = \dfrac{1-2i}{\sqrt5}$. Geometric picture: the closest point on the unit circle to an exterior point $a$ is where the ray $O \to a$ exits the circle.


Answer: $\sqrt5 - 1$, at $z = \dfrac{1-2i}{\sqrt5}$

</details>

O z = (1−2i)/√5 a = 1−2i √5 − 1 1 Closest point of the unit circle to $a = 1-2i$: the ray $O \to a$ meets the circle at $z = a/|a|$, and the gap is $|a| - 1 = \sqrt5 - 1$ (bold segment).

#### **P33**[JEE Advanced][chord distance]If [formula] and [formula] , find [formula] .

If $|z| = |w| = 1$ and $z\bar w = i$, find $|z - w|$.

<details>
<summary>Answer + Reasoning</summary>

By (C): $|z-w|^2 = 2 - 2\operatorname{Re}(z\bar w) = 2 - 2\operatorname{Re}(i) = 2 - 0 = 2$, so $|z-w| = \sqrt2$. Geometrically: $z\bar w = i$ means $w/z = i$, i.e. the two points are $90^\circ$ apart on the unit circle — a chord of the "quarter" arc, length $2\sin 45^\circ = \sqrt2$.


Answer: $\sqrt2$

</details>

#### **P31**[JEE Advanced][range on |z|=1]If [formula] , find the range of [formula] .

If $|z| = 1$, find the range of $\left|z + \dfrac{1}{z} + 2i\right|$.

<details>
<summary>Answer + Reasoning</summary>

On $|z|=1$, $\dfrac{1}{z} = \bar z$. Write $z = \cos\theta + i\sin\theta$: $z + \bar z = 2\cos\theta$, so 
$$ z + \frac{1}{z} + 2i = 2\cos\theta + 2i, $$
 a purely horizontal point on the line $\operatorname{Im} = 2$. Its modulus is 
$$ 2\sqrt{\cos^2\theta + 1}, $$
 which ranges over $[2, 2\sqrt2]$ as $\cos^2\theta$ ranges over $[0,1]$. Minimum $2$ at $\theta = \pm\pi/2$ (i.e. $z = \pm i$); maximum $2\sqrt2$ at $z = \pm 1$.


Answer: $[2,\ 2\sqrt2]$

</details>


### 4.6 Ellipses — $|z-A| + |z-B| =$ constant

The sum of distances to two fixed points equals a constant $2a$ (with $2a &gt; |A-B| = 2c$): by the conic definition, an **ellipse** with foci $A, B$, major axis $a$, and minor axis $b = \sqrt{a^2 - c^2}$. The maximum height of an ellipse $|z - c| + |z + c| = 2a$ is $b$ (at the top of the minor axis) — this is a favorite "find the maximum of $\operatorname{Im} z$" setup.

#### **P37**[JEE Advanced][ellipse]If [formula] , find the maximum of [formula] .

If $|z - 1| + |z + 1| = 6$, find the maximum of $\operatorname{Im} z$.

<details>
<summary>Answer + Reasoning</summary>

Foci at $\pm 1$: $2c = 2$, so $c = 1$. Constant $2a = 6$, so $a = 3$. Then $b = \sqrt{a^2 - c^2} = \sqrt{9 - 1} = \sqrt8 = 2\sqrt2$. The maximum of $\operatorname{Im} z$ is the top of the minor axis: **$2\sqrt2$** (at $z = \pm i\cdot 2\sqrt2$; check: $|i2\sqrt2 - 1| = \sqrt{1 + 8} = 3$, $|i2\sqrt2 + 1| = 3$, sum $6$ ✓).


Answer: $2\sqrt2$

</details>

> [!warning] Check the constant first
>
> If the constant $\le |A-B|$, the "ellipse" degenerates: equal to the focal distance gives the segment $AB$ itself; smaller than it gives the empty set. In the JEE setup $|z-1|+|z+1| = 2$ would be the segment $[-1,1]$, not an ellipse. One inequality check saves a whole wrong solution.


### 4.7 Ranges of $|z|$ over regions

Given a *region* $R$ (intersection of a disk and a half-plane, say), find the range of $|z|$ for $z \in R$. The method is geometric, not algebraic: $|z|$ is the distance from the origin, so its minimum and maximum over $R$ are the closest and farthest points of $R$ from $0$ — which live on the boundary (or at a boundary vertex) of $R$. Draw the region; the answer is a distance you can read off.

#### **P35**[JEE Advanced][region range]If [formula] and [formula] , find the range of [formula] .

If $\operatorname{Re} z &gt; 0$ and $|z - 1| &lt; 1$, find the range of $|z|$.

<details>
<summary>Answer + Reasoning</summary>

$|z-1| &lt; 1$ is the open disk centered at $1$ with radius $1$ — it touches the origin and lies entirely in $\operatorname{Re} z \ge 0$ (its leftmost point is $0$, excluded). Intersecting with $\operatorname{Re} z &gt; 0$ removes only the origin itself (the disk's only point with $\operatorname{Re} z = 0$). Distances from $0$ inside the disk range over $(0, 2)$: closest is arbitrarily near $0$, farthest is the rightmost point $2$ (excluded, since the disk is open).


Answer: $(0,\ 2)$

</details>

#### **P36**[JEE Main][region range]If [formula] , find the range of [formula] .

If $|z + 2| \le 3$, find the range of $|z|$.

<details>
<summary>Answer + Reasoning</summary>

Disk centered at $-2$ (on the real axis) with radius $3$, closed. It contains the origin ($|0+2| = 2 \le 3$), so the minimum of $|z|$ is $0$, at $z = 0$. The farthest point from $0$ is the one on the line from $0$ through the center, extended by the radius: $-2 - 3 = -5$, so $\max|z| = 5$. (Triangle inequality: $|z| \le |z+2| + 2 \le 5$, equality at $z = -5$; $|z| \ge 0$ is trivial.)


Answer: $[0,\ 5]$

</details>

> [!success] Chapter checklist
>
> - Solving $\alpha z + \beta\bar z = c$: real/imag parts, and the conjugate trick (with its sign trap).
> - Complex-conjugate quadratic roots: $|z_1 - z_2| = \sqrt{4c - b^2}$ directly.
> - Modulus loci → circles, including disguised ones ($|z|^2 = z+\bar z$, "purely imaginary" → Thales circle).
> - Argument loci → arcs: $R = \frac{|a-b|}{2\sin|\theta|}$, center on the perpendicular bisector, sign picks the arc.
> - Optimization on $|z| = 1$: $\min |z-a| = ||a|-1|$ at $z = a/|a|$; chord formula $|z-w| = 2|\sin(\varphi/2)|$.
> - Ellipses from $|z-A|+|z-B| = 2a$: $b = \sqrt{a^2-c^2}$, max height $= b$; degenerate cases checked first.
> - Range of $|z|$ over a region: draw it; extrema live on the boundary.

> [!info] Bridge to Ch 5 — geometry via complex numbers
>
> Everything in this chapter was *one object* — a $z$, a locus, a distance. Chapter 5 works with *several* complex numbers as vertices of a polygon, and proves geometric theorems (equilateral triangles, Ptolemy, Van Aubel, Napoleon) as algebra in $\mathbb{C}$. The unit-circle parametrization of §4.5 and the argument geometry of §4.4 become the standard setup there.



---
