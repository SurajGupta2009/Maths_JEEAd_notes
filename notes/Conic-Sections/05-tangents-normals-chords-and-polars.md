---
title: "Chapter 5 — Tangents, Normals, Chords and Polars"
aliases:
  - Tangents, Normals, Chords and Polars
  - Ch 5 — Tangents, Normals, Chords and Polars
module: "Conic-Sections"
module_title: "Conic Sections"
chapter: 5
level: frontier
tags:
  - conic-sections
  - chapter
  - frontier
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Conic-Sections|Conic Sections]] · ⬅ [[04-the-hyperbola-and-its-asymptotes|Chapter 4]] · [[06-the-olympiad-frontier-reflection-confocals-and-triangles|Chapter 6]] ➡ · 📝 [[Conic-Sections — Paper|Olympiad Paper]] · ✅ [[Conic-Sections — Solutions|Solutions]]

# Chapter 5 — Tangents, Normals, Chords and Polars

*6 sections · 10 questions*

*Chapter 5 of 6*

# Tangents, Normals, Chords and Polars

Everything the last three chapters did separately, this chapter does once. The trick is the two-letter shorthand: for any conic $S = 0$ and point $(x_1, y_1)$, define $S_1$ (substitute) and $T$ (halve the cross terms). Then *chord of contact is $T = 0$*, *chord with given midpoint is $T = S_1$*, and *pair of tangents is $SS_1 = T^2$* — for the parabola, ellipse and hyperbola alike. Polarity is the same machine read backwards.

### 5.0 What you will be able to do

- Write, from memory, the tangent to any standard conic in point, parameter and slope form — and know each slope form's validity range.
- Produce chord of contact, midpoint chord and pair of tangents from $T$ and $S_1$ in one line each.
- Define pole and polar, prove and use La Hire's theorem, and find the polar of a focus and the pole of a tangent.
- State how many normals can be drawn from a point to each conic and why.


### 5.1 The tangent dictionary

One card to carry into the exam. $m$ = slope; $\theta$ = parameter of the curve.

$$ \begin{array}{c|c|c|c}
      \text{curve} &amp; \text{at } (x_1,y_1) &amp; \text{parametric} &amp; \text{slope form} \\ \hline
      y^2 = 4ax &amp; yy_1 = 2a(x + x_1) &amp; ty = x + at^2 &amp; y = mx + \dfrac{a}{m} \\
      \dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1 &amp; \dfrac{xx_1}{a^2}+\dfrac{yy_1}{b^2}=1 &amp;
      \dfrac{x\cos\theta}{a}+\dfrac{y\sin\theta}{b}=1 &amp; y = mx \pm \sqrt{a^2m^2+b^2} \\
      \dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1 &amp; \dfrac{xx_1}{a^2}-\dfrac{yy_1}{b^2}=1 &amp;
      \dfrac{x\sec\theta}{a}-\dfrac{y\tan\theta}{b}=1 &amp; y = mx \pm \sqrt{a^2m^2-b^2},\ |m| \gt \tfrac ba \\
      xy = c^2 &amp; xy_1 + x_1y = 2c^2 &amp; \dfrac{x}{t} + ty = 2c &amp; \text{slopes } m \lt 0
      \end{array} $$

All of these come from the same engine: write a line with the right slope through the right point, substitute into the conic, and set the resulting quadratic's discriminant to zero. That derivation is worth re-running once by hand — it is the proof that the dictionary is *complete*.

> [!warning] Common Trap — slope forms with restricted $m$
>
> For the hyperbola, $y = mx + c$ is tangent iff $c^2 = a^2m^2 - b^2$: real only for $|m| \gt \tfrac ba$. Flatter lines miss the curve entirely or cut it twice. For the parabola the restriction is different in kind: $y = mx + \tfrac{a}{m}$ needs $m \ne 0$ — the axis direction is never tangent.

#### **P33**[JEE Main][practice][slope form]Find the tangent of slope [formula] to [formula] .

Find the tangent of slope $-1$ to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y = mx + \tfrac{a}{m}$.** $y = -x - 1$. (Contact point $\left(\tfrac{a}{m^2}, \tfrac{2a}{m}\right) = (1, -2)$.)


Answer: **$y = -x - 1$**. (Check: $(x+1)^2 = 4x \Rightarrow (x-1)^2 = 0$: double root at $(1, -2)$ ✓.)

</details>


### 5.2 Chord of contact and the pair of tangents

Fix a point $P_1 = (x_1, y_1)$ outside a conic $S = 0$. Two tangents touch at $Q$ and $R$.

> [!abstract] First Principles — why the chord of contact is $T = 0$
>
> The tangent to the ellipse at $(x_2, y_2)$ is $\dfrac{xx_2}{a^2} + \dfrac{yy_2}{b^2} = 1$. It passes through $P_1$ exactly when $\dfrac{x_1x_2}{a^2} + \dfrac{y_1y_2}{b^2} = 1$ — which says that *$(x_2, y_2)$ lies on the line $\dfrac{xx_1}{a^2} + \dfrac{yy_1}{b^2} = 1$*. So both contact points $Q, R$ lie on that line, and it is the chord of contact $QR = T = 0$. The identical argument works for every conic in the dictionary — the line $T = 0$ is the *only* new object needed.

> [!quote] Named Formula — pair of tangents: $S S_1 = T^2$
>
> The pair of tangent lines from $P_1$ is the degenerate quadratic 
> $$ S \cdot S_1 = T^2. $$
>  It vanishes exactly on the two tangents (each tangent point satisfies both $S = 0$ and $T = 0$), it passes through $P_1$ (both sides vanish there), and it factors into two lines. Interpretation: it is the limit of the secant pair as the two intersection points merge. For the unit circle it reads $(x^2+y^2-1)(x_1^2+y_1^2-1) = (xx_1 + yy_1 - 1)^2$ — expand and admire the cancellation.

#### **P34**[JEE Adv][practice][pair of tangents]Find the joint equation of the pair of tangents from [formula] to [formula] , …

Find the joint equation of the pair of tangents from $(-2, 5)$ to $y^2 = 4x$, and check that each member really is tangent.

<details>
<summary>Answer + Reasoning</summary>

**Method: $SS_1 = T^2$.** $S = y^2 - 4x$, $S_1 = 25 + 8 = 33$, $T = 5y - 2(x - 2) = 5y - 2x + 4$. So $33(y^2 - 4x) = (5y - 2x + 4)^2$, which expands and simplifies to



$$ x^2 - 5xy - 2y^2 + 29x + 10y + 4 = 0. $$



Tangency check: the lines through $(-2,5)$ of slope $m$ are tangent to $y^2=4x$ iff $m^2 - 3m + 1 = 0$ (from the discriminant of $my^2 - 4y + 12 - 4m$), i.e. $m = \tfrac{3 \pm \sqrt5}{2}$ — two real slopes, matching the two factors.


Answer: **$x^2 - 5xy - 2y^2 + 29x + 10y + 4 = 0$**. (Check: vanishes at $(-2,5)$: $4 + 50 - 50 - 58 + 50 + 4 = 0$ ✓; discriminant identity verified at $m = \tfrac{3+\sqrt5}{2}$: $16 - 4m(12 - 4m) = 0$ ✓.)

</details>

#### **P35**[JEE Adv][practice][chord of contact]Find the chord of contact from [formula] to [formula] , its contact points, an…

Find the chord of contact from $(4, 2)$ to $\dfrac{x^2}{16} + \dfrac{y^2}{4} = 1$, its contact points, and verify the tangents there pass through $(4, 2)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = 0$.** $\dfrac{4x}{16} + \dfrac{2y}{4} = 1$, i.e. $x + 2y = 4$. Intersecting with the ellipse: $y = 0$ forces $x = 4$ and $x = 0$ forces $y = 2$: the contact points are $(4, 0)$ and $(0, 2)$.


Tangents: at $(4,0)$: $\dfrac{4x}{16} = 1 \Rightarrow x = 4$ — contains $(4,2)$ ✓. At $(0,2)$: $\dfrac{2y}{4} = 1 \Rightarrow y = 2$ — contains $(4,2)$ ✓.


Answer: **chord of contact $x + 2y = 4$; contacts $(4,0)$ and $(0,2)$**.

</details>


### 5.3 The chord with a given midpoint

> [!abstract] First Principles — the $T = S_1$ derivation, once for all conics
>
> Let a chord of the ellipse through $(x_1, y_1)$ have direction $(\ell, m)$: points $(x_1 + t\ell, y_1 + tm)$. Substituting into the ellipse gives a quadratic in $t$ whose roots are the two ends. The midpoint is $(x_1,y_1)$ itself exactly when the roots sum to zero — i.e. when the linear coefficient vanishes:
>
>
>
> $$ \frac{x_1\ell}{a^2} + \frac{y_1 m}{b^2} = 0
>       \quad\Longrightarrow\quad \text{slope} = -\frac{b^2 x_1}{a^2 y_1}. $$
>
>
>
> Writing that line through $(x_1, y_1)$ and tidying: $\dfrac{xx_1}{a^2} + \dfrac{yy_1}{b^2} = \dfrac{x_1^2}{a^2} + \dfrac{y_1^2}{b^2}$, which is exactly $\boxed{T = S_1}$. For the hyperbola the mixed term flips sign and the slope becomes $+\tfrac{b^2x_1}{a^2y_1}$ — but the tidy form is again $T = S_1$. For the parabola: $yy_1 - 2a(x + x_1) = y_1^2 - 4ax_1$, also $T = S_1$. One formula, three curves — and P13 showed the boundary case where the "chord" is a tangent.

#### **S12**[JEE Adv][solved][midpoint chord]Find the chord of [formula] bisected at [formula] , and verify the midpoint by…

Find the chord of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ bisected at $(5, 3)$, and verify the midpoint by Vieta.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** $T = S_1$, remembering $S_1$ carries its own $-1$: $S_1 = \tfrac{25}{4} - \tfrac{9}{9} - 1 = \tfrac{17}{4}$.


$T = S_1$: $\dfrac{5x}{4} - \dfrac{y}{3} - 1 = \tfrac{17}{4}$, so $\dfrac{5x}{4} - \dfrac{y}{3} = \tfrac{21}{4}$, i.e.



$$ 15x - 4y = 63. $$



Slope sanity: $\tfrac{15}{4} = +\tfrac{b^2x_1}{a^2y_1} = \tfrac{9\cdot5}{4\cdot3}$ ✓ (positive, unlike the ellipse).


**Vieta check:** substituting $y = \tfrac{15x - 63}{4}$ into $9x^2 - 4y^2 = 36$: $36x^2 - (15x - 63)^2 = 144$, i.e. $-189x^2 + 1890x - 4113 = 0$. Sum of roots $= \tfrac{1890}{189} = 10$: midpoint $x = 5$ ✓ (and the $y$-midpoint is $3$ by the line equation).


Total: **Answer: $15x - 4y = 63$**

</details>


### 5.4 Poles and polars — La Hire's theorem

For a point $P_1$ (inside or outside), the line $T = 0$ is called the **polar** of $P_1$. When $P_1$ is outside, the polar is the chord of contact — the definition extends the idea to every point. Reversing roles, a line's **pole** is the point whose polar it is.

> [!abstract] First Principles — La Hire: the relation is symmetric
>
> All polar equations are of the form $B\big((x,y), (x_1,y_1)\big) = 1$ where $B$ is a *symmetric bilinear* expression (the symmetrised conic: $\tfrac{xx_1}{a^2} +
>       \tfrac{yy_1}{b^2}$, etc.). "Point $Q$ lies on the polar of $P$" is the statement $B(P, Q) = 1$; by symmetry $B(Q, P) = 1$ is the *same* equation — so $P$ lies on the polar of $Q$. That one line is **La Hire's theorem**: pole-of and polar-of are reciprocal relations, and polarity is a dictionary between points and lines that preserves incidence.

> [!example] Olympiad Extension — two polar facts worth their weight in gold
>
> **The polar of a focus is the directrix.** For the ellipse, the polar of $(ae, 0)$ is $\dfrac{ae\,x}{a^2} = 1$, i.e. $x = \dfrac{a}{e}$ — exactly the directrix (Q28). **The pole of a tangent is its contact point.** A tangent's "chord of contact" is the doubled point of contact, so $T = 0$ with $S_1 = 0$ — the polar of the contact point (P40). Between these two sits the classical pole of a chord: the pole of any chord is the intersection of the tangents at its ends.

#### **S13**[Olympiad][solved][La Hire in action]Show that the polar of [formula] w.r.t. [formula] is [formula] , and verify La…

Show that the polar of $(4, 3)$ w.r.t. $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ is $\dfrac{x}{4} + \dfrac{y}{3} = 1$, and verify La Hire's theorem along it.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** $T = 0$ with $(x_1, y_1) = (4, 3)$: $\dfrac{4x}{16} + \dfrac{3y}{9} = 1$, i.e. $\dfrac{x}{4} + \dfrac{y}{3} = 1$.


**La Hire along the line:** take any $(u, v)$ on the polar, e.g. $(4, 0)$, $(0, 3)$, $\left(2, \tfrac32\right)$. The polar of $(u, v)$ is $\dfrac{ux}{16} + \dfrac{vy}{9} = 1$; evaluate at $(4, 3)$: $\dfrac{4u}{16} + \dfrac{3v}{9} = \dfrac{u}{4} + \dfrac{v}{3} = 1$ — true because $(u,v)$ is on the polar of $(4,3)$. So every polar of every point of the line passes through $(4, 3)$: the whole pencil of lines through $(4,3)$ is the mirror image of the line's points.


Total: **Answer: polar $\tfrac{x}{4} + \tfrac{y}{3} = 1$; La Hire verified**


**Check:** $S_1 = \tfrac{16}{16} + \tfrac{9}{9} - 1 = 1 \gt 0$: $(4,3)$ is outside the ellipse, so its polar is a genuine chord of contact ✓.

</details>

#### **P36**[JEE Adv][practice][pole of a line]Find the pole of the line [formula] with respect to [formula] .

Find the pole of the line $x = 8$ with respect to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: match $T = 0$ to the line.** Polar of $(x_1, y_1)$: $yy_1 = 2(x + x_1)$. To be the vertical line $x = 8$ we need $y_1 = 0$ and $2(x + x_1) \propto x - 8$: $2x + 2x_1 = k(x - 8)$ gives $k = 2$, $x_1 = -8$.


Answer: **pole $= (-8, 0)$**. (Check: its polar is $0\cdot y = 2(x - 8)$, i.e. $x = 8$ ✓.)

</details>

#### **P37**[JEE Adv][practice][polar + La Hire]Find the polar of [formula] with respect to [formula] , and verify La Hire's t…

Find the polar of $(2, 3)$ with respect to $\dfrac{x^2}{9} - \dfrac{y^2}{4} = 1$, and verify La Hire's theorem for three points on it.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = 0$, sign convention honoured.** $\dfrac{2x}{9} - \dfrac{3y}{4} = 1$, i.e. $8x - 27y = 36$.


La Hire: points on it include $\left(\tfrac92, 0\right)$, $\left(0, -\tfrac43\right)$, $\left(\tfrac94, -\tfrac23\right)$. The polar of $(u,v)$ is $\dfrac{ux}{9} - \dfrac{vy}{4} = 1$; at $(2,3)$ it gives $\dfrac{2u}{9} - \dfrac{3v}{4} = 1$ — true for all three points, i.e. all their polars pass through $(2,3)$ ✓.


Answer: **$8x - 27y = 36$**, with the reciprocity checked ✓.

</details>

#### **P40**[Olympiad][practice][pole of tangent]Find the pole of [formula] with respect to [formula] , and interpret the answe…

Find the pole of $x + 4y = 8$ with respect to $xy = 4$, and interpret the answer.

<details>
<summary>Answer + Reasoning</summary>

**Method: match the polar form.** Polar of $(x_1, y_1)$ w.r.t. $xy = c^2$: $\dfrac{xy_1 + x_1y}{2} = c^2$, i.e. $xy_1 + x_1y = 8$. Matching $y_1 : x_1 = 1 : 4$ and the constant: $x_1 = 4k, y_1 = k$, $8k = 8$, $k = 1$: pole $= (4, 1)$.


Interpretation: $x + 4y = 8$ is the tangent at $t = 2$ (contact $(4,1)$, Chapter 4's S10) — and the pole of a tangent is its contact point.


Answer: **pole $= (4, 1)$, the point of contact**. (Check: polar of $(4,1)$: $x + 4y = 8$ ✓.)

</details>


### 5.5 How many normals? And the three director loci

**Normals from a point.** For the parabola, the normal cubic (Chapter 2) gives at most three. For the ellipse, eliminating the parameter produces a quartic in general position — **four normals** can be drawn from a general point (a theorem of Apollonius; the four feet lie on a rectangular hyperbola through the centre and the two foci, a lovely fact we will not prove here). The hyperbola similarly admits four. What the exam tests is the *mechanism*: substitute the normal's equation into the point and count real roots.

#### **P39**[JEE Adv][practice][normal through centre]Show that a normal to [formula] passes through the centre iff it is drawn at o…

Show that a normal to $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ passes through the centre iff it is drawn at one of the four vertices.

<details>
<summary>Answer + Reasoning</summary>

**Method: feed $(0,0)$ into the normal equation.** $ax\sin\theta - by\cos\theta = (a^2-b^2)\sin\theta\cos\theta$ at $(0,0)$: the left side is $0$, so $(a^2 - b^2)\sin\theta\cos\theta = 0$. Since $a \ne b$: $\sin\theta = 0$ or $\cos\theta = 0$ — the points $(\pm 3, 0)$ and $(0, \pm 2)$.


Answer: **only at the four vertices** (the axis normals are the coordinate axes themselves ✓).

</details>

> [!quote] Named Result — the three director loci, side by side
>
> Locus of intersection of perpendicular tangents:
>
>
>
> $$ \text{ellipse: } x^2 + y^2 = a^2 + b^2 \qquad
>          \text{hyperbola: } x^2 + y^2 = a^2 - b^2 \qquad
>          \text{parabola: the directrix.} $$
>
>
>
> The ellipse's is always real; the hyperbola's needs $a \gt b$ and degenerates for the rectangular case; the parabola's is a line. One computation, three answers — the signature of the unified Chapter 5 viewpoint (P38, P32, P16).

#### **P38**[JEE Main][practice][director circle]Find the director circle of [formula] and verify it with the horizontal/vertic…

Find the director circle of $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ and verify it with the horizontal/vertical tangent pair.

<details>
<summary>Answer + Reasoning</summary>

**Method: $x^2 + y^2 = a^2 + b^2$.** $x^2 + y^2 = 41$. The tangents $y = \pm 4$ and $x = \pm 5$ are perpendicular pairs meeting at $(\pm 5, \pm 4)$, and $25 + 16 = 41$ ✓.


Answer: **$x^2 + y^2 = 41$**.

</details>



---
