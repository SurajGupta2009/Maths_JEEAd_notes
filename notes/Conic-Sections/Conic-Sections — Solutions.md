---
title: "Conic Sections — Olympiad Paper Solutions"
aliases:
  - Conic-Sections Solutions
module: "Conic-Sections"
module_title: "Conic Sections"
type: solutions
tags:
  - conic-sections
  - solutions
  - olympiad
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Conic-Sections — Paper|Paper]] · 📖 [[Conic-Sections|Conic Sections]]

# Olympiad Paper · Solutions & marking guide

*Companion to the 38-question paper*

# Full Worked Solutions

Every solution shows the *method name* first, then the computation, then a check. Where a problem has two standard methods, both are given — the exam rewards the ability to choose, and the notes are built on the same principle. All numeric answers below were re-verified by an independent pure-Python computation (exact rational arithmetic where possible) before this key was written.

### A · First Principles & Eccentricity (Q1–Q5)

#### **Q1**[JEE Main]Find the equation of the parabola with focus [formula] and directrix [formula]…

Find the equation of the parabola with focus $(0, -3)$ and directrix $y = 3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: write the locus, square once.** $\sqrt{x^2 + (y+3)^2} = |y - 3|$. Squaring: $x^2 + y^2 + 6y + 9 = y^2 - 6y + 9 \Rightarrow x^2 = -12y$.


Answer: $x^2 = -12y$


Check: $(4, -\tfrac43)$ is on it ($16 = -12\cdot(-\tfrac43)$); distance to focus $= \sqrt{16 + (5/3)^2} = \tfrac{13}{3}$, to the line $= 3 + \tfrac43 = \tfrac{13}{3}$ ✓. (The parabola opens downward — the focus sits below the directrix.)

</details>

#### **Q2**[JEE Main]A point moves so that its distance from [formula] is half its distance from th…

A point moves so that its distance from $(3, 0)$ is half its distance from the line $x = 12$.

<details>
<summary>Answer + Reasoning</summary>

**Method 1: read the data through the focus-directrix form.** $e = \tfrac12$, $\dfrac{a}{e} = 12 \Rightarrow a = 6$, $b^2 = a^2(1 - e^2) = 36\cdot\tfrac34 = 27$: ellipse $\dfrac{x^2}{36} + \dfrac{y^2}{27} = 1$.


**Method 2: square directly.** $\sqrt{(x-3)^2 + y^2} = \tfrac{12 - x}{2}$. Squaring: $4(x-3)^2 + 4y^2 = (12-x)^2 \Rightarrow 4x^2 - 24x + 36 + 4y^2 = 144 - 24x + x^2$, i.e. $3x^2 + 4y^2 = 108$ — the same ellipse after dividing by 108.


Answer: ellipse $\dfrac{x^2}{36} + \dfrac{y^2}{27} = 1$, $e = \tfrac12$


Check: $(6, 0)$: distance to $(3,0)$ is $3$; to the line is $6 = 2\cdot3$ ✓.

</details>

#### **Q3**[JEE Main]Find the eccentricity and the foci of [formula] .

Find the eccentricity and the foci of $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $e^2 = 1 - \tfrac{b^2}{a^2}$.** $e = \sqrt{1 - \tfrac{9}{25}} = \tfrac45$; $c = ae = 5\cdot\tfrac45 = 4$: foci $(\pm 4, 0)$.


Answer: $e = \tfrac45$; foci $(\pm 4, 0)$


Check: $c^2 = a^2 - b^2 = 16$ ✓ (the hyperbola formula $c^2 = a^2 + b^2$ would give $\sqrt{34}$ — the minus sign is the classification).

</details>

#### **Q4**[JEE Adv]For [formula] , find [formula] , the foci and the directrices.

For $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, find $e$, the foci and the directrices.

<details>
<summary>Answer + Reasoning</summary>

**Method: $e^2 = 1 + \tfrac{b^2}{a^2}$.** $e = \sqrt{1 + \tfrac{9}{16}} = \tfrac54$; $c = ae = 5$: foci $(\pm 5, 0)$; directrices $x = \pm\tfrac{a}{e} = \pm\tfrac{16}{5}$.


Answer: $e = \tfrac54$; foci $(\pm 5, 0)$; $x = \pm\tfrac{16}{5}$


Check: $\tfrac{16}{5} \lt 4$: the directrices sit between centre and vertices, as they must for a hyperbola ✓.

</details>

#### **Q5**[Olympiad]The focus-directrix definition with focus [formula] , directrix [formula] , [f…

The focus-directrix definition with focus $(0,0)$, directrix $x = 0$, $e = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: square and watch the locus collapse.** $\sqrt{x^2 + y^2} = |x| \Rightarrow x^2 + y^2 = x^2 \Rightarrow y = 0$. Every point of the $x$-axis satisfies the definition — but as a locus equation $y = 0$ is a *doubled* line: the parabola degenerated because the directrix passes through the focus, removing the "thickness" that generates a genuine curve.


Answer: the doubled line $y = 0$


Check: for $e = 1$ with focus *not* on the directrix (P6 of Chapter 1) the same algebra yields a true parabola — only the through-the-focus placement degenerates ✓.

</details>


### B · Parabola Machinery (Q6–Q11)

#### **Q6**[JEE Main]Focal distance of [formula] on [formula] .

Focal distance of $(4, 4)$ on $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: focal distance $= x + a$.** $4 + 1 = 5$.


Answer: $5$


Check (both methods): direct distance $\sqrt{(4-1)^2 + 16} = \sqrt{25} = 5$ ✓.

</details>

#### **Q7**[JEE Adv]Focal chord of [formula] with one end [formula] : other end and length.

Focal chord of $y^2 = 8x$ with one end $t = 3$: other end and length.

<details>
<summary>Answer + Reasoning</summary>

**Method: $t_1t_2 = -1$, length $a(t + \tfrac1t)^2$.** $a = 2$. Other end $t = -\tfrac13$: $\left(2\cdot\tfrac19, 4\cdot(-\tfrac13)\right) = \left(\tfrac29, -\tfrac43\right)$. Length $= 2\left(3 + \tfrac13\right)^2 = 2\cdot\tfrac{100}{9} = \tfrac{200}{9}$.


**Method 2: parts.** $|SP(3)| = a(1+t^2) = 20$, $|SP(-\tfrac13)| = 2(1+\tfrac19) = \tfrac{20}{9}$; total $\tfrac{200}{9}$ ✓.


Answer: $\left(\tfrac29, -\tfrac43\right)$; length $\tfrac{200}{9}$


Check: harmonic mean of the parts $= \tfrac{2}{\tfrac{1}{20} + \tfrac{9}{20}} = 4 = 2a$ ✓; the chord passes $(2, 0)$ ✓.

</details>

#### **Q8**[JEE Adv]Chord of [formula] bisected at [formula] .

Chord of $y^2 = 4x$ bisected at $\left(\tfrac{13}{4}, 3\right)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = S_1$.** $S_1 = 9 - 13 = -4$. $T = S_1$: $3y - 2\left(x + \tfrac{13}{4}\right) = -4$, i.e. $3y - 2x - \tfrac{13}{2} = -4$: multiply by 2: $6y - 4x - 13 = -8$, so



$$ 4x - 6y + 5 = 0. $$



Answer: $4x - 6y + 5 = 0$


Check (Vieta): substituting $y = \tfrac{4x+5}{6}$ into $y^2 = 4x$: $16x^2 - 104x + 25 = 0$; sum of roots $= \tfrac{104}{16} = \tfrac{13}{2}$: midpoint $x = \tfrac{13}{4}$ ✓, endpoints $\left(\tfrac14, 1\right)$ and $\left(\tfrac{25}{4}, 5\right)$ ✓.

</details>

#### **Q9**[JEE Adv]Normals from [formula] to [formula] .

Normals from $(9, 6)$ to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the normal cubic.** $am^3 + (2a - h)m + k = 0$ with $a=1$: $m^3 - 7m + 6 = 0$. Rational root $m = 1$: factor $(m-1)(m-2)(m+3) = 0$: slopes $1, 2, -3$ — three normals, sum $0$ as the cubic's vanished $m^2$-coefficient guarantees.


Feet $(m^2, -2m)$: $(1, -2)$, $(4, -4)$, $(9, 6)$. The last foot is the point itself — $(9,6)$ lies on the parabola ($36 = 4\cdot9$), so one "normal from the point" is the normal at the point.


Answer: three; slopes $1, 2, -3$; feet $(1,-2), (4,-4), (9,6)$


Check: the normal of slope $m$ is $y = -tx + 2t + t^3$ with $t = -m$: for $m=1$ ($t=-1$): $y = x - 3$, passes $(9,6)$: $9 - 3 = 6$ ✓; similarly $m=2$: $y = 2x - 12$: $18 - 12 = 6$ ✓; $m=-3$ ($t=3$): $y = -3x + 33$: $-27 + 33 = 6$ ✓.

</details>

#### **Q10**[JEE Adv]Normal at [formula] on [formula] meets the axis at [formula] .

Normal at $t = 2$ on $y^2 = 4x$ meets the axis at $N$.

<details>
<summary>Answer + Reasoning</summary>

**Method: normal $y = -tx + 2at + at^3$, then the isosceles reading.** $y = -2x + 4 + 8 = -2x + 12$: $N = (6, 0)$. $|SP| = a(1+t^2) = 5$ (or directly: $P = (4,4)$, $S = (1,0)$: $\sqrt{9+16} = 5$). $|SN| = 6 - 1 = 5$.


Answer: $N = (6, 0)$; $|SP| = |SN| = 5$ — triangle $SPN$ is isosceles


Check: this is exactly the reflection property of Chapter 2 — the normal makes equal angles with $SP$ and the axis ✓.

</details>

#### **Q11**[Olympiad]Foot of the perpendicular from the focus to any tangent of [formula] .

Foot of the perpendicular from the focus to any tangent of $y^2 = 4ax$.

<details>
<summary>Answer + Reasoning</summary>

**Method: foot-of-perpendicular formula.** Tangent at $t$: $x - ty + at^2 = 0$; focus $S(a, 0)$. With $A = 1, B = -t, C = at^2$ the foot is $\left(a - \tfrac{A\cdot(Aa + C)}{A^2+B^2},\; \tfrac{-B(Aa+C)}{A^2+B^2}\right)$ and $Aa + C = a(1 + t^2)$:



$$ \left(a - \frac{a(1+t^2)}{1+t^2},\; \frac{t\,a(1+t^2)}{1+t^2}\right) = (0,\ at). $$



The $x$-coordinate is $0$ for all $t$: the foot always lies on $x = 0$, the tangent at the vertex.


Answer: foot $= (0, at)$; for $a = 1, t = 2$: $(0, 2)$


Check $(a=1, t=2)$: tangent $2y = x + 4$; the perpendicular from $(1,0)$ has slope $-2$: $y = -2(x-1)$; intersection: $2(-2x+2) = x + 4 \Rightarrow x = 0, y = 2$ ✓.

</details>


### C · The Ellipse (Q12–Q17)

#### **Q12**[JEE Main]Eccentricity and latus rectum of [formula] .

Eccentricity and latus rectum of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: plug into the two formulas.** $e = \sqrt{1 - \tfrac{9}{16}} = \tfrac{\sqrt7}{4}$; LR $= \dfrac{2b^2}{a} = \dfrac{18}{4} = \dfrac92$.


Answer: $e = \tfrac{\sqrt7}{4}$; LR $= \tfrac92$


Check: $c = ae = \sqrt7$, $c^2 = 7 = 16 - 9$ ✓.

</details>

#### **Q13**[JEE Main]Tangents of slope [formula] to [formula] .

Tangents of slope $1$ to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method 1: slope form.** $y = x \pm \sqrt{a^2m^2 + b^2} = x \pm \sqrt{25} = x \pm 5$.


**Method 2: discriminant.** Substituting $y = x + c$ into the ellipse and multiplying by 144: $25x^2 + 32cx + 16c^2 - 144 = 0$. Tangency: $(32c)^2 = 4\cdot25(16c^2 - 144) \Rightarrow 14400 = 576c^2 \Rightarrow c = \pm 5$ ✓.


Answer: $y = x \pm 5$; for $c = 5$: $25x^2 + 160x + 256 = (5x+16)^2$


Check: the double root $x = -\tfrac{16}{5}$ gives the contact point $\left(-\tfrac{16}{5}, \tfrac95\right)$, which is on the ellipse: $\tfrac{256/25}{16} + \tfrac{81/25}{9} = \tfrac{16}{25} + \tfrac{9}{25} = 1$ ✓.

</details>

#### **Q14**[JEE Adv][formula] , foci [formula] .

$|PF_1| + |PF_2| = 10$, foci $(\mp 4, 0)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: constant sum is $2a$.** $a = 5$, $c = 4$, $b^2 = 25 - 16 = 9$: ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.


Latus rectum: $\dfrac{2b^2}{a} = \dfrac{18}{5}$; ends $\left(\pm 4, \pm\tfrac95\right)$; the one through $(4, 0)$ has ends $\left(4, \pm\tfrac95\right)$.


Answer: $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$; LR $= \tfrac{18}{5}$; ends $\left(4, \pm\tfrac95\right)$


Check: $\tfrac{16}{25} + \tfrac{81}{225} = \tfrac{16 + 9}{25} = 1$ ✓; the semi-latus rectum $\tfrac95 = \tfrac{b^2}{a}$ ✓.

</details>

#### **Q15**[JEE Adv]Director circle of [formula] .

Director circle of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $x^2 + y^2 = a^2 + b^2$.** $x^2 + y^2 = 25$; axis intercepts $(\pm 5, 0)$, $(0, \pm 5)$.


**Method 2 (spot verification):** the tangents $y = x + 5$ and $y = -x - 5$ are perpendicular and meet at $(-5, 0)$; likewise for the other sign pairs — all four intersections lie on the circle (S8 of Chapter 3).


Answer: $x^2 + y^2 = 25$; $(\pm 5, 0)$, $(0, \pm 5)$


Check: $5 = \sqrt{16 + 9}$ ✓.

</details>

#### **Q16**[JEE Adv]Chord of contact from [formula] to [formula] .

Chord of contact from $(5, 3)$ to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = 0$.** $\dfrac{5x}{16} + \dfrac{3y}{9} = 1$, i.e. $15x + 16y = 48$. (The point is outside: $\tfrac{25}{16} + 1 - 1 = \tfrac{25}{16} \gt 0$.)


**Reality of the contacts:** substitute $y = \tfrac{48 - 15x}{16}$ into the ellipse; multiplying by 2304: $144x^2 + (48 - 15x)^2 = 2304 \Rightarrow 369x^2 - 1440x = 0$. Two real roots: $x = 0$ and $x = \tfrac{160}{41}$ — contacts $(0, 3)$ and $\left(\tfrac{160}{41}, -\tfrac{27}{41}\right)$.


Answer: $15x + 16y = 48$; contacts $(0, 3)$, $\left(\tfrac{160}{41}, -\tfrac{27}{41}\right)$


Check: $\tfrac{(160/41)^2}{16} + \tfrac{(27/41)^2}{9} = \tfrac{1600 + 81}{1681} = 1$ ✓; the tangent at $(0,3)$ is $y = 3$, which passes $(5,3)$ ✓.

</details>

#### **Q17**[Olympiad]Reflection angles at [formula] of [formula] .

Reflection angles at $P = \left(4, \tfrac95\right)$ of $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: three directions, two angles.** Tangent slope at $P$: $-\dfrac{b^2x}{a^2y} = -\dfrac{9\cdot4}{25\cdot 9/5} = -\dfrac45$: direction angle $\arctan(-\tfrac45) \approx -38.66^\circ$. Ray to the near focus $F_2(4,0)$: vertical ($90^\circ$). Ray to $F_1(-4, 0)$: slope $\dfrac{9/5}{8} = \dfrac{9}{40}$: angle $\arctan\tfrac{9}{40} \approx 12.68^\circ$.


Angle with the vertical ray: $|90 - (-38.66)| \to 90 - 38.66 = 51.34^\circ$. Angle with the far ray: $|12.68 - (-38.66)| = 51.34^\circ$. Equal — the reflection property in numbers.


Answer: both $\approx 51.34^\circ$; a ray from $F_1$ reflects to $F_2$


Check: $38.66 + 51.34 = 90$: the two acute angles the tangent makes with the axes are complementary, consistent with slopes $-\tfrac45$ and $\tfrac54$ being negative reciprocals ✓.

</details>


### D · Hyperbola & Rectangular Hyperbola (Q18–Q23)

#### **Q18**[JEE Main][formula] : anatomy.

$9x^2 - 16y^2 = 144$: anatomy.

<details>
<summary>Answer + Reasoning</summary>

**Method: standardise, then read.** $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$: $a = 4, b = 3$, $c = 5$. $e = \tfrac54$; foci $(\pm 5, 0)$; LR $\tfrac{2\cdot9}{4} = \tfrac92$.


Answer: $e = \tfrac54$; foci $(\pm 5, 0)$; LR $= \tfrac92$


Check: $b^2 = c^2 - a^2 = 25 - 16 = 9$ ✓ (the $3\text{-}4\text{-}5$ hyperbola, conjugate orientation of Q4's).

</details>

#### **Q19**[JEE Main]Asymptotes of [formula] and the angle between them.

Asymptotes of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ and the angle between them.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y = \pm\tfrac ba x$; angle via $\tan\alpha = \tfrac ba$.** Asymptotes $y = \pm\tfrac32 x$; $\alpha = \arctan\tfrac32 \approx 56.31^\circ$, so the angle around the transverse axis is $2\alpha \approx 112.62^\circ$.


**Cross-check by the eccentricity identity:** $e^2 = 1 + \tfrac94 = \tfrac{13}{4}$, $\cos 2\alpha = \tfrac{2}{e^2} - 1 = \tfrac{8}{13} - 1 = -\tfrac{5}{13}$, and indeed $\cos(112.62^\circ) = -\tfrac{5}{13}$ ✓ (from the $2\text{-}3\text{-}\sqrt{13}$ triangle: $\cos 2\alpha = \tfrac{4-9}{13}$).


Answer: $y = \pm\tfrac32x$; $2\arctan\tfrac32 \approx 112.62^\circ$

</details>

#### **Q20**[JEE Adv]Asymptote angle [formula] around the transverse axis: find [formula] .

Asymptote angle $60^\circ$ around the transverse axis: find $e$.

<details>
<summary>Answer + Reasoning</summary>

**Method 1: $\tan\alpha = b/a$.** $\alpha = 30^\circ$: $\tfrac ba = \tfrac{1}{\sqrt3}$, so $e = \sqrt{1 + \tfrac13} = \tfrac{2}{\sqrt3}$.


**Method 2: $\cos 2\alpha = \tfrac{2}{e^2} - 1$.** $\tfrac12 = \tfrac{2}{e^2} - 1 \Rightarrow e^2 = \tfrac43 \Rightarrow e = \tfrac{2}{\sqrt3}$ ✓.


Answer: $e = \dfrac{2}{\sqrt3}$


Check: $e = 1.1547 \gt 1$, and between the rectangular value $\sqrt2$ and the degenerate $e \to 1$ — right, since $60^\circ$ is narrower than $90^\circ$ ✓.

</details>

#### **Q21**[JEE Adv]Conjugate hyperbola of [formula] and the eccentricity identity.

Conjugate hyperbola of $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$ and the eccentricity identity.

<details>
<summary>Answer + Reasoning</summary>

**Method: swap the axes; same $c$.** Conjugate: $\dfrac{y^2}{9} - \dfrac{x^2}{16} = 1$, $c = 5$. Original: $e = \tfrac{c}{a} = \tfrac54$; conjugate: $e' = \tfrac{c}{b} = \tfrac53$.


Identity: $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = \dfrac{16}{25} + \dfrac{9}{25} = 1$ ✓.


Answer: $\dfrac{y^2}{9} - \dfrac{x^2}{16} = 1$; $e = \tfrac54$, $e' = \tfrac53$


Check: neither is $\sqrt2$ — a hyperbola and its conjugate share the rectangularity budget ✓.

</details>

#### **Q22**[JEE Adv][formula] : tangent and normal at [formula] .

$xy = 9$: tangent and normal at $t = 3$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the $xy = c^2$ dictionary.** $c = 3$: point $(ct, \tfrac{c}{t}) = (9, 1)$. Tangent $\dfrac{x}{t} + ty = 2c$: $\dfrac{x}{3} + 3y = 6$, i.e. $x + 9y = 18$ (slope $-\tfrac19$). Normal $y = t^2x - ct^3 + \tfrac{c}{t} = 9x - 81 + 1 = 9x - 80$ (slope $9$).


Answer: tangent $x + 9y = 18$; normal $y = 9x - 80$; $-\tfrac19 \cdot 9 = -1$


Check: both pass $(9, 1)$: $9 + 9 = 18$ ✓; $81 - 80 = 1$ ✓; implicit differentiation $y' = -\tfrac{9}{x^2}$ gives $y'(9) = -\tfrac19$ ✓.

</details>

#### **Q23**[Olympiad]No real perpendicular tangents to [formula] .

No real perpendicular tangents to $x^2 - y^2 = a^2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: the slope form's validity range.** Tangent of slope $m$: $y = mx \pm\sqrt{a^2m^2 - a^2}$, real iff $|m| \ge 1$. A perpendicular partner has slope $-\tfrac1m$, also needing $\left|\tfrac1m\right| \ge 1$, i.e. $|m| \le 1$. Together: $|m| = 1$, forcing $c = 0$ — the "tangents" $y = \pm x$ are exactly the asymptotes, which meet the curve nowhere (substituting $y = x$: $x^2 - x^2 = 0 \ne a^2$). Hence no real perpendicular pair exists.


Answer: impossible; director "circle" is $x^2 + y^2 = a^2 - a^2 = 0$


Check: this is the director circle $x^2 + y^2 = a^2 - b^2$ with $a = b$ — degenerated to a point ✓.

</details>


### E · Tangents, Chords & Polars (Q24–Q28)

#### **Q24**[JEE Main]Tangent of slope [formula] to [formula] .

Tangent of slope $2$ to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y = mx + \tfrac{a}{m}$.** $y = 2x + \tfrac12$; contact $\left(\tfrac{a}{m^2}, \tfrac{2a}{m}\right) = \left(\tfrac14, 1\right)$.


Answer: $y = 2x + \tfrac12$; contact $\left(\tfrac14, 1\right)$


Check: $\left(2x + \tfrac12\right)^2 = 4x \Rightarrow 4x^2 - 2x + \tfrac14 = 0
        \Rightarrow \left(2x - \tfrac12\right)^2 = 0$: double root $x = \tfrac14$ ✓.

</details>

#### **Q25**[JEE Adv]Pair of tangents from [formula] to [formula] .

Pair of tangents from $(1, 3)$ to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $SS_1 = T^2$.** $S_1 = 9 - 4 = 5$; $T = 3y - 2(x+1) = 3y - 2x - 2$. So $(3y - 2x - 2)^2 = 5(y^2 - 4x)$; expanding and collecting:



$$ 4x^2 + 4y^2 - 12xy + 28x - 12y + 4 = 0, $$
 i.e. $x^2 + y^2 - 3xy + 7x - 3y + 1 = 0$.


**Tangent slopes:** lines $y = m(x-1) + 3$ tangent to $y^2 = 4x$ need the discriminant of $my^2 - 4y + 12 - 4m = 0$ to vanish: $16 - 4m(12 - 4m) = 16(m^2 - 3m + 1) = 0$: $m = \tfrac{3 \pm \sqrt5}{2}$ — two real slopes, matching the two factors of the joint equation.


Answer: $x^2 + y^2 - 3xy + 7x - 3y + 1 = 0$; slopes $\tfrac{3\pm\sqrt5}{2}$


Check: the joint equation vanishes at $(1,3)$: $1 + 9 - 9 + 7 - 9 + 1 = 0$ ✓.

</details>

#### **Q26**[JEE Adv]Chord of contact from [formula] to [formula] .

Chord of contact from $(1, 3)$ to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = 0$ is $yy_1 = 2(x + x_1)$.** $3y = 2x + 2$, i.e. $2x - 3y + 2 = 0$.


**Reality:** substituting $y = \tfrac{2x+2}{3}$ into $y^2 = 4x$: $4x^2 - 28x + 4 = 0$, discriminant $784 - 64 = 720 \gt 0$: two real contact points with $x = \tfrac{7 \pm 3\sqrt5}{2}$.


Answer: $2x - 3y + 2 = 0$; contact $x$-coordinates $\tfrac{7 \pm 3\sqrt5}{2}$


Check: real contacts are guaranteed anyway because $(1,3)$ is outside ($S_1 = 5 \gt 0$) ✓.

</details>

#### **Q27**[JEE Adv]Pole of [formula] w.r.t. [formula] .

Pole of $3x - 4y + 7 = 0$ w.r.t. $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: match the polar form to the line.** Polar of $(x_1, y_1)$: $yy_1 = 2x + 2x_1$, i.e. $y = \tfrac{2}{y_1}x + \tfrac{2x_1}{y_1}$. The line is $y = \tfrac34 x + \tfrac74$. Matching: $\tfrac{2}{y_1} = \tfrac34 \Rightarrow y_1 = \tfrac83$; $\tfrac{2x_1}{y_1} = \tfrac74 \Rightarrow x_1 = \tfrac{7y_1}{8} = \tfrac73$.


Answer: pole $= \left(\tfrac73, \tfrac83\right)$


Check: the polar of $\left(\tfrac73, \tfrac83\right)$ is $\tfrac83 y = 2x + \tfrac{14}{3}$, i.e. $8y = 6x + 14$, i.e. $3x - 4y + 7 = 0$ after dividing by $-2$ ✓.

</details>

#### **Q28**[Olympiad]Polar of a focus is the directrix.

Polar of a focus is the directrix.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = 0$ at the focus.** For $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, the right focus is $(4, 0)$. Its polar: $\dfrac{4x}{25} + 0 = 1$, i.e. $x = \tfrac{25}{4}$. But $a/e = 5/(4/5) = \tfrac{25}{4}$: this is exactly the directrix.


**Why it is general:** the polar of $(ae, 0)$ reads $\dfrac{ae\,x}{a^2} = 1$, i.e. $x = \tfrac{a}{e}$ — no special numbers were used. The same computation works for the hyperbola and (with the vertical-line polar form) for the parabola, whose polar of the focus is $x = -a$.


Answer: $x = \tfrac{25}{4} = \tfrac{a}{e}$ — the directrix, in general


Check: by La Hire, the pole of the directrix is the focus — the dictionary runs both ways ✓.

</details>


### F · Normals & Parametric Geometry (Q29–Q32)

#### **Q29**[JEE Main]Point with eccentric angle [formula] on [formula] .

Point with eccentric angle $60^\circ$ on $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $(a\cos\theta, b\sin\theta)$.** $\left(4\cdot\tfrac12,\ 3\cdot\tfrac{\sqrt3}{2}\right) = \left(2, \tfrac{3\sqrt3}{2}\right)$.


Answer: $\left(2, \tfrac{3\sqrt3}{2}\right)$


Check: $\tfrac{4}{16} + \tfrac{27/4}{9} = \tfrac14 + \tfrac34 = 1$ ✓.

</details>

#### **Q30**[JEE Adv]Tangent and normal at the point of Q29.

Tangent and normal at the point of Q29.

<details>
<summary>Answer + Reasoning</summary>

**Method: the parametric forms.** Tangent $\dfrac{x\cos\theta}{a} + \dfrac{y\sin\theta}{b} = 1$: $\dfrac{x}{8} + \dfrac{\sqrt3 y}{6} = 1$, i.e. $3x + 4\sqrt3\,y = 24$. Normal $ax\sin\theta - by\cos\theta = (a^2-b^2)\sin\theta\cos\theta$: $2\sqrt3 x - \tfrac32 y = \tfrac{7\sqrt3}{4}$, i.e. $8\sqrt3 x - 6y = 7\sqrt3$.


Slopes: $-\dfrac{3}{4\sqrt3}$ and $\dfrac{4\sqrt3}{3}$; product $-1$ ✓.


Answer: tangent $3x + 4\sqrt3 y = 24$; normal $8\sqrt3 x - 6y = 7\sqrt3$


Check: both pass $\left(2, \tfrac{3\sqrt3}{2}\right)$: $6 + 18 = 24$ ✓; $16\sqrt3 - 9\sqrt3 = 7\sqrt3$ ✓.

</details>

#### **Q31**[JEE Adv]Points where the normal to [formula] has slope [formula] .

Points where the normal to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ has slope $1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: normal slope $= \tfrac{a}{b}\tan\theta$.** $\tfrac43\tan\theta = 1 \Rightarrow \tan\theta = \tfrac34$: take $\cos\theta = \tfrac45, \sin\theta = \tfrac35$ and the antipodal pair. Points: $\left(\tfrac{16}{5}, \tfrac95\right)$ and $\left(-\tfrac{16}{5}, -\tfrac95\right)$.


Answer: $\pm\left(\tfrac{16}{5}, \tfrac95\right)$


Check: on the curve: $\tfrac{256/25}{16} + \tfrac{81/25}{9} = \tfrac{16}{25} + \tfrac{9}{25} = 1$ ✓; tangent slope there $-\tfrac{b^2x}{a^2y} = -\tfrac{9\cdot16/5}{16\cdot9/5} = -1$, so the normal slope is $1$ ✓.

</details>

#### **Q32**[Olympiad]Normals at the ends of a focal chord of [formula] are perpendicular.

Normals at the ends of a focal chord of $y^2 = 4ax$ are perpendicular.

<details>
<summary>Answer + Reasoning</summary>

**Method: parameters.** Focal chord ends: $t$ and $-\tfrac1t$. Normal slope at $t$ is $-t$ (from $y = -tx + 2at + at^3$); at $-\tfrac1t$ it is $\tfrac1t$. Product: $-t\cdot\tfrac1t = -1$: perpendicular — always, for every focal chord.


Verification for $a = 1, t = 2$: ends $(4, 4)$ and $(\tfrac14, -1)$. Normals: $y = -2x + 12$ (slope $-2$) and $y = \tfrac{x}{2} - \tfrac98$ (slope $\tfrac12$).


Answer: slopes $-t$ and $\tfrac1t$, product $-1$; $y = -2x+12$ and $y = \tfrac{x}{2} - \tfrac98$


Check: $(4,4)$ on $y = -2x+12$: $4 = 4$ ✓; $(\tfrac14, -1)$ on $y = \tfrac{x}{2} - \tfrac98$: $\tfrac18 - \tfrac98 = -1$ ✓.

</details>


### G · Reflection, Confocals & Triangles (Q33–Q36)

#### **Q33**[JEE Adv]Whispering gallery [formula] .

Whispering gallery $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: foci at $(\pm c, 0)$, $c = \sqrt{a^2 - b^2}$.** $c = \sqrt{64} = 8$: foci $16$ m apart. By the reflection property, a whisper at one focuses at the other.


Answer: $16$ m


Check: $c^2 = 100 - 36 = 64$ ✓.

</details>

#### **Q34**[Olympiad]Tangent bisects the focal angle at [formula] on [formula] .

Tangent bisects the focal angle at $\left(5, \tfrac94\right)$ on $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: three directions, two angles.** $P$ is on the curve: $\tfrac{25}{16} - \tfrac{81/16}{9} = \tfrac{25 - 9}{16} = 1$ ✓. Tangent slope: $\dfrac{b^2x}{a^2y} = \dfrac{45}{36} = \tfrac54$: direction $51.34^\circ$. Rays: to the near focus $(5, 0)$: vertical ($90^\circ$); to $(-5, 0)$: slope $\dfrac{9/4}{10} = \dfrac{9}{40}$: $12.68^\circ$.


Angles with the tangent: $90 - 51.34 = 38.66^\circ$ and $51.34 - 12.68 = 38.66^\circ$ — equal, so the tangent is the internal bisector (the hyperbola's version of the ellipse's external one).


Answer: both angles $\approx 38.66^\circ$


Check: the two ray directions $90^\circ$ and $12.68^\circ$ have exact bisector $51.34^\circ$ — precisely the tangent's angle ✓.

</details>

#### **Q35**[Olympiad]Orthocentre of [formula] and the hyperbola [formula] .

Orthocentre of $(0,4), (6,4), (2,0)$ and the hyperbola $xy - 4x - 2y + 8 = 0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: altitudes.** Side $(0,4)$-$(6,4)$ is horizontal: the altitude from $(2,0)$ is $x = 2$. Side $(0,4)$-$(2,0)$ has slope $-2$: the altitude from $(6,4)$ has slope $\tfrac12$: $y = 4 + \tfrac{x-6}{2}$. At $x = 2$: $y = 4 - 2 = 2$. So $H = (2, 2)$.


**Hyperbola check:** $(0,4)$: $0 - 0 - 8 + 8 = 0$ ✓; $(6,4)$: $24 - 24 - 8 + 8 = 0$ ✓; $(2,0)$: $0 - 8 - 0 + 8 = 0$ ✓; $H$: $4 - 8 - 4 + 8 = 0$ ✓.


Answer: $H = (2, 2)$; all four points lie on $xy - 4x - 2y + 8 = 0$


Check: this is the orthocentre theorem of Chapter 6 — a rectangular hyperbola through a triangle automatically swallows the orthocentre ✓.

</details>

#### **Q36**[Olympiad]Confocal hyperbola through [formula] for [formula] .

Confocal hyperbola through $\left(4, \tfrac{12}{5}\right)$ for $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: focal distances give $A$.** $c^2 = 9$. Distances from $P$ to $(\pm 3, 0)$: $\sqrt{1 + \tfrac{144}{25}} = \tfrac{13}{5}$ and $\sqrt{49 + \tfrac{144}{25}} = \tfrac{37}{5}$. Difference: $\tfrac{24}{5} = 2A$: $A^2 = \tfrac{144}{25}$, $B^2 = 9 - \tfrac{144}{25} = \tfrac{81}{25}$.


Hyperbola: $\dfrac{x^2}{144/25} - \dfrac{y^2}{81/25} = 1$. Slopes at $P$: ellipse $-\dfrac{16\cdot4}{25\cdot12/5} = -\dfrac{16}{15}$; hyperbola $\dfrac{(81/25)\cdot4}{(144/25)\cdot(12/5)} = \dfrac{15}{16}$. Product: $-1$ ✓ — the confocal orthogonality theorem in numbers.


Answer: $\dfrac{25x^2}{144} - \dfrac{25y^2}{81} = 1$; slopes $-\tfrac{16}{15}$, $\tfrac{15}{16}$


Check: $P$ on the hyperbola: $\tfrac{25\cdot16}{144} - \tfrac{25\cdot(144/25)}{81} = \tfrac{25}{9} - \tfrac{16}{9} = 1$ ✓.

</details>


### H · Synthesis & Stretch (Q37–Q38)

#### **Q37**[Olympiad]Midpoints of focal chords of [formula] .

Midpoints of focal chords of $y^2 = 4ax$.

<details>
<summary>Answer + Reasoning</summary>

**Method: a focal chord is a line through the focus.** Write it as $y = m(x - a)$. Intersecting with $y^2 = 4ax$: $m^2x^2 - (2am^2 + 4a)x + a^2m^2 = 0$; by Vieta the midpoint's $x = \dfrac{2am^2 + 4a}{2m^2} = a + \dfrac{2a}{m^2}$, and from the line, $y = \dfrac{2a}{m}$. Eliminating $m$: $y^2 = \dfrac{4a^2}{m^2} = 2a\left(x - a\right)$.


Locus: the parabola $y^2 = 2a(x - a)$ — vertex $(a, 0)$ (the focus of the original!), latus rectum $2a$.


Answer: $y^2 = 2a(x - a)$; LR $= 2a$


Check ($a=1$, ends $t = 2, -\tfrac12$): midpoint $\left(\tfrac{17}{8}, \tfrac32\right)$; $\left(\tfrac32\right)^2 = \tfrac94$ and $2\left(\tfrac{17}{8} - 1\right) = \tfrac{9}{4}$ ✓.

</details>

#### **Q38**[Olympiad]Product of the focal perpendiculars to a tangent of the ellipse.

Product of the focal perpendiculars to a tangent of the ellipse.

<details>
<summary>Answer + Reasoning</summary>

**Method: distance formula, then cancel.** Tangent at $\theta$: $\dfrac{x\cos\theta}{a} + \dfrac{y\sin\theta}{b} = 1$. Denote $D = \sqrt{\dfrac{\cos^2\theta}{a^2} + \dfrac{\sin^2\theta}{b^2}}$, $c = ae$. The two distances are $\dfrac{\left|1 - \tfrac{c\cos\theta}{a}\right|}{D}$ and $\dfrac{\left|1 + \tfrac{c\cos\theta}{a}\right|}{D}$; since $c \lt a$, both inner terms are positive and the product is



$$ \frac{1 - \dfrac{c^2\cos^2\theta}{a^2}}{D^2}
         = \frac{1 - \dfrac{(a^2-b^2)\cos^2\theta}{a^2}}{D^2}
         = \frac{\sin^2\theta + \dfrac{b^2}{a^2}\cos^2\theta}{D^2}
         = \frac{b^2\left(\dfrac{\sin^2\theta}{b^2} + \dfrac{\cos^2\theta}{a^2}\right)}{D^2} = b^2. $$



Answer: product $= b^2$, exactly, for every tangent


Check ($a=4, b=3, \theta = 60^\circ$): $D^2 = \tfrac{1}{64} + \tfrac{1}{12}
        = \tfrac{19}{192}$; $\tfrac{c^2\cos^2\theta}{a^2} = \tfrac{7}{64}$, so the numerator is $1 - \tfrac{7}{64} = \tfrac{57}{64}$; product $= \tfrac{57/64}{19/192} = \tfrac{57\cdot192}{64\cdot19} = 9 = b^2$ ✓ — the same value the direct numerical computation of both distances gives.

</details>
