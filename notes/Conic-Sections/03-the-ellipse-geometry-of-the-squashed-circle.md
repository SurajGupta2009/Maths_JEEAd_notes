---
title: "Chapter 3 — The Ellipse — Geometry of the Squashed Circle"
aliases:
  - The Ellipse — Geometry of the Squashed Circle
  - Ch 3 — The Ellipse — Geometry of the Squashed Circle
module: "Conic-Sections"
module_title: "Conic Sections"
chapter: 3
level: core
tags:
  - conic-sections
  - chapter
  - core
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Conic-Sections|Conic Sections]] · ⬅ [[02-the-parabola-anatomy-and-machinery|Chapter 2]] · [[04-the-hyperbola-and-its-asymptotes|Chapter 4]] ➡ · 📝 [[Conic-Sections — Paper|Olympiad Paper]] · ✅ [[Conic-Sections — Solutions|Solutions]]

# Chapter 3 — The Ellipse — Geometry of the Squashed Circle

*7 sections · 11 questions*

*Chapter 3 of 6*

# The Ellipse — Geometry of the Squashed Circle

The ellipse is the image of a circle under a vertical squash — and almost all of its geometry becomes transparent if you keep the unsquashed *auxiliary circle* in view. The eccentric angle $\theta$ is the circle's angle smuggled onto the ellipse; tangents, normals, focal distances and even the reflection property are circle facts wearing the squash. This chapter builds that dictionary and harvests it.

### 3.0 What you will be able to do

- Read the full anatomy of $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$: foci, directrices, eccentricity, latus rectum, focal distances $a \mp ex$ — and reconstruct it from partial data.
- Move fluently between the point $(a\cos\theta, b\sin\theta)$, the auxiliary circle, and tangent/normal lines in point, parameter and slope form.
- Use the director circle $x^2 + y^2 = a^2 + b^2$ and the position test $S_1 \lt 0$.
- Prove the reflection property (whispering gallery) and apply it to real geometries.


### 3.1 Anatomy of the ellipse

For $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ with $a \gt b \gt 0$: vertices $(\pm a, 0)$; foci $(\pm ae, 0)$ with $c = ae = \sqrt{a^2 - b^2}$; eccentricity $e = \sqrt{1 - \dfrac{b^2}{a^2}} \in (0,1)$; directrices $x = \pm \dfrac{a}{e}$; latus rectum through either focus, ends $\left(\pm ae, \pm \dfrac{b^2}{a}\right)$, length $\dfrac{2b^2}{a}$.

> [!abstract] First Principles — why the focal distances are $a - ex$ and $a + ex$
>
> For $P(x, y)$ on the ellipse, $|PF_{\text{right}}| = e \times$ (distance to the right directrix $x = a/e$) $= e\left(\dfrac{a}{e} - x\right) = a - ex$. One line — no square roots — because the focus-directrix definition is literally built this way. The left focus gives $a + ex$ by symmetry, and the sum is $2a$ on the nose. Sanity at the vertex: $x = a$ gives $a - ea = a - c$ ✓.

#### **S6**[JEE Main][solved][applied ellipse]An arch is a semi-ellipse with a [formula] m span and maximum height [formula]…

An arch is a semi-ellipse with a $20$ m span and maximum height $5$ m. A truck $4$ m wide, centred on the axis, is $4.8$ m tall. Does it clear the arch at a point $2$ m from the centre?

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: model, substitute, compare.** The full ellipse has $2a = 20$, $b = 5$: $\dfrac{x^2}{100} + \dfrac{y^2}{25} = 1$. At $x = 2$: $y = 5\sqrt{1 - \tfrac{4}{100}} = 5\sqrt{0.96} \approx 4.899$ m.


Since $4.899 \gt 4.8$, the truck clears by about $10$ cm.


Total: **Answer: clears (height available $\approx 4.899$ m)**


**Check:** at $x = 0$ the height is $5$ m and the ellipse decreases away from the centre — $4.899 \lt 5$ is consistent ✓. Note the margin is thin: an off-centre load flips the answer, which is exactly how these questions are graded.

</details>

#### **P17**[JEE Main][practice][anatomy]For [formula] , find [formula] , the foci, and the latus rectum.

For $\dfrac{x^2}{36} + \dfrac{y^2}{16} = 1$, find $e$, the foci, and the latus rectum.

<details>
<summary>Answer + Reasoning</summary>

**Method: $e^2 = 1 - b^2/a^2$.** $e = \sqrt{1 - \tfrac{16}{36}} = \dfrac{\sqrt5}{3}$; $c = ae = 6\cdot\tfrac{\sqrt5}{3} = 2\sqrt5$; LR $= \dfrac{2b^2}{a} = \dfrac{32}{6} = \dfrac{16}{3}$.


Answer: **$e = \tfrac{\sqrt5}{3}$, foci $(\pm 2\sqrt5, 0)$, LR $\tfrac{16}{3}$**. (Check: $c^2 = a^2 - b^2 = 20$ ✓.)

</details>

#### **P18**[JEE Main][practice][reconstruct]Find the ellipse centred at the origin with foci [formula] that passes through…

Find the ellipse centred at the origin with foci $(\pm 2, 0)$ that passes through $(2, 3)$, and give its eccentricity.

<details>
<summary>Answer + Reasoning</summary>

**Method: constant sum from the two foci.** At $(2,3)$: distances $3$ and $\sqrt{16 + 9} = 5$, so $2a = 8$, $a = 4$, $b^2 = a^2 - c^2 = 16 - 4 = 12$.


Answer: **$\dfrac{x^2}{16} + \dfrac{y^2}{12} = 1$, $e = \tfrac{c}{a} = \tfrac12$**. (Check: $\tfrac{4}{16} + \tfrac{9}{12} = \tfrac14 + \tfrac34 = 1$ ✓.)

</details>


### 3.2 The auxiliary circle and the eccentric angle

Draw the circle $x^2 + y^2 = a^2$ on the major axis. The vertical line through an ellipse point $P$ meets this circle at $Q$; writing $Q = (a\cos\theta, a\sin\theta)$ makes

$$ P = (a\cos\theta,\ b\sin\theta) $$

$\theta$ is the **eccentric angle** of $P$ — not a geometric angle at $P$ or at the centre-to-$P$ line, but the angle of the *circle point above it*. This distinction is a standing JEE Advanced trap: "the point with eccentric angle $\theta$" means $(a\cos\theta, b\sin\theta)$, full stop.

> [!tip] Key Idea — squashing maps circle facts to ellipse facts
>
> The map $(x, y) \mapsto \left(x, \tfrac{b}{a}y\right)$ squashes the auxiliary circle onto the ellipse. Areas scale by $\tfrac ba$ (so the ellipse's area is $\pi ab$); vertical lines stay vertical; the circle's tangent at $Q$ and the ellipse's tangent at $P$ meet on the $x$-axis at the same point $(a\sec\theta, 0)$. When an ellipse computation stalls, unsquash, think circle, squash back.

#### **P23**[JEE Main][practice][eccentric angle]Find the eccentric angle of the point [formula] on [formula] , and the corresp…

Find the eccentric angle of the point $\left(2\sqrt2, \tfrac{3}{\sqrt2}\right)$ on $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$, and the corresponding point on the auxiliary circle.

<details>
<summary>Answer + Reasoning</summary>

**Method: invert the parametrisation.** $\cos\theta = \dfrac{2\sqrt2}{4} = \dfrac{1}{\sqrt2}$, $\sin\theta = \dfrac{3/\sqrt2}{3} = \dfrac{1}{\sqrt2}$: $\theta = 45^\circ$. The auxiliary-circle point is $(a\cos\theta, a\sin\theta) = (2\sqrt2, 2\sqrt2)$.


Answer: **$\theta = 45^\circ$; circle point $(2\sqrt2, 2\sqrt2)$**. (Check: $\tfrac{8}{16} + \tfrac{9/2}{9} = \tfrac12 + \tfrac12 = 1$ ✓.)

</details>


### 3.3 Tangent and normal in three forms

$$ \frac{xx_1}{a^2} + \frac{yy_1}{b^2} = 1 \qquad
         \frac{x\cos\theta}{a} + \frac{y\sin\theta}{b} = 1 \qquad
         y = mx \pm \sqrt{a^2m^2 + b^2} $$

$$ ax\sin\theta - by\cos\theta = (a^2 - b^2)\sin\theta\cos\theta $$
 
$$ y = mx - \frac{(a^2-b^2)\,m}{\sqrt{a^2 + b^2m^2}} \qquad
         \frac{a^2 x}{x_1} - \frac{b^2 y}{y_1} = a^2 - b^2 $$

The slope-form tangent is valid for every $m$ (no restriction — the ellipse slopes gently everywhere); the slope-form normal always exists too. Note the sign structure: the tangent's root has $+\,b^2$, the normal's correction subtracts along the direction of the slope — getting these two mixed is a standard error.

#### **S7**[JEE Adv][solved][tangent + normal]Find the tangent and normal to [formula] at the point with eccentric angle [fo…

Find the tangent and normal to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ at the point with eccentric angle $45^\circ$, and verify they are perpendicular.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** point first, then the two forms.


Point: $P = \left(4\cos 45^\circ,\ 3\sin 45^\circ\right) = \left(2\sqrt2, \tfrac{3}{\sqrt2}\right)$.


Tangent: $\dfrac{x\cos 45^\circ}{4} + \dfrac{y\sin 45^\circ}{3} = 1$. Multiply by $\dfrac{24}{\sqrt2}$: $\;3x + 4y = 12\sqrt2$.


Normal: $ax\sin\theta - by\cos\theta = (a^2-b^2)\sin\theta\cos\theta$ gives $4x\cdot\tfrac{1}{\sqrt2} - 3y\cdot\tfrac{1}{\sqrt2} = 7 \cdot \tfrac12$, i.e. $\;4x - 3y = \dfrac{7}{\sqrt2} = \dfrac{7\sqrt2}{2}$.


Slopes: tangent $-\tfrac34$, normal $\tfrac43$; product $-1$ — perpendicular, as a tangent and its normal must be.


Total: **Answer: tangent $3x + 4y = 12\sqrt2$; normal $4x - 3y = \tfrac{7\sqrt2}{2}$**


**Check:** both pass $P$: $3(2\sqrt2) + 4\cdot\tfrac{3}{\sqrt2} = 6\sqrt2 + 6\sqrt2 = 12\sqrt2$ ✓; $4(2\sqrt2) - 3\cdot\tfrac{3}{\sqrt2} = 8\sqrt2 - \tfrac{9\sqrt2}{2} = \tfrac{7\sqrt2}{2}$ ✓.

</details>

#### **P19**[JEE Adv][practice][slope form]Find the tangents of slope [formula] to [formula] .

Find the tangents of slope $2$ to $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y = mx \pm \sqrt{a^2m^2 + b^2}$.** $y = 2x \pm \sqrt{9\cdot4 + 4} = 2x \pm \sqrt{40} = 2x \pm 2\sqrt{10}$.


Answer: **$y = 2x \pm 2\sqrt{10}$**. (Check: substituting $y = 2x + 2\sqrt{10}$ into the ellipse gives $40x^2 + 72\sqrt{10}\,x + 324 = 0$ scaled — discriminant $(72\sqrt{10})^2 - 4\cdot40\cdot324 = 0$ ✓.)

</details>

#### **P20**[JEE Adv][practice][normal by slope]Find the points on [formula] at which the normal has slope [formula] .

Find the points on $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ at which the normal has slope $2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: normal slope $= \dfrac{a\sin\theta}{b\cos\theta} = \dfrac{a}{b}\tan\theta$.** $\dfrac{3}{2}\tan\theta = 2 \Rightarrow \tan\theta = \tfrac43$: take $\cos\theta = \tfrac35, \sin\theta = \tfrac45$ (and the antipodal point). Points: $\left(3\cdot\tfrac35,\ 2\cdot\tfrac45\right) = \left(\tfrac95, \tfrac85\right)$ and its negative.


Answer: **$\pm\left(\tfrac95, \tfrac85\right)$**. (Check: on curve $\tfrac{81}{225} + \tfrac{64}{100} = 0.36 + 0.64 = 1$; tangent slope there $-\tfrac{b^2x}{a^2y} = -\tfrac{4\cdot 9/5}{9\cdot 8/5} = -\tfrac12$, so the normal slope is $2$ ✓.)

</details>


### 3.4 Focal chords and the latus rectum

A **focal chord** is any chord through a focus. Its two parts inherit the harmonic-mean property from Chapter 2, with the semi-latus rectum playing the constant role.

> [!quote] Named Property — $l = b^2/a$ is the harmonic mean of the two parts
>
> For a focal chord cut into segments of lengths $u$ and $v$ by the focus: $\dfrac{1}{u} + \dfrac{1}{v} = \dfrac{2a}{b^2} = \dfrac{2}{l}$, where $l = \dfrac{b^2}{a}$ is the semi-latus rectum. Proof without coordinates: for $P$ on the ellipse, $|SP_{\text{near}}| = a - ex$ and the chord's other end $P'$ has parameter reflected through the focus, giving $|SP'| = a + ex'$ with the reciprocal sum collapsing to $\tfrac{2a}{b^2}$; the latus-rectum case $u = v = l$ alone already forces the constant. (Numerically verified in P21.)

#### **P21**[JEE Adv][practice][focal distances + chord]For [formula] and the point [formula] with eccentric angle [formula] : find bo…

For $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$ and the point $P$ with eccentric angle $60^\circ$: find both focal distances, and the harmonic mean of the two parts of the focal chord through $P$ (right focus).

<details>
<summary>Answer + Reasoning</summary>

**Method: $a \mp ex$, then intersect the line $PF$ with the curve again.** $P = \left(\tfrac52, \tfrac{3\sqrt3}{2}\right)$, $e = \tfrac45$: $a - ex = 5 - \tfrac45\cdot\tfrac52 = 3$ and $a + ex = 7$. Sum $= 10 = 2a$ ✓.


The line $P(4, 0)$ meets the ellipse again at $Q \approx (8.5, -2.598)$; numerically $|PF| = 3$, $|QF| = 4.5$, and $\dfrac{2}{\tfrac13 + \tfrac{1}{4.5}} = \dfrac{9}{5} = \dfrac{b^2}{a}$.


Answer: **$3$ and $7$; harmonic mean $= \tfrac95$ — the semi-latus rectum** ✓.

</details>


### 3.5 Position of a point; the director circle

For $S = \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - 1$ evaluated at a probe point $(x_1, y_1)$: $S_1 \lt 0$ means inside, $S_1 = 0$ on, $S_1 \gt 0$ outside. No factorisations, just arithmetic.

> [!abstract] First Principles — the director circle $x^2 + y^2 = a^2 + b^2$
>
> The locus of intersection of **perpendicular tangents** is a circle, and the fastest derivation anticipates Chapter 5's joint equation. From an external point $(h, k)$ the pair of tangents to the ellipse is the degenerate quadratic $S S_1 = T^2$, whose $x^2$ and $y^2$ coefficients are $S_1/a^2 - h^2/a^4$ and $S_1/b^2 - k^2/b^4$. A pair of lines $Ax^2 + 2Hxy + By^2 = 0$ is perpendicular exactly when $A + B = 0$. Imposing that and multiplying by $a^4b^4$:
>
>
>
> $$ (h^2b^2 + k^2a^2 - a^2b^2)(a^2 + b^2) = h^2b^4 + k^2a^4 \;\Longrightarrow\;
>       a^2b^2(h^2 + k^2) = a^2b^2(a^2 + b^2), $$
>
>
>
> so $h^2 + k^2 = a^2 + b^2$ — the **director circle**. It is always real (unlike the hyperbola's, Chapter 4). The same computation for the parabola degenerates to its directrix, as P12 and P16 witnessed.

#### **S8**[JEE Adv][solved][director circle]Verify the director circle of [formula] using the tangents of slopes [formula]…

Verify the director circle of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ using the tangents of slopes $1$ and $-1$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: write the four tangents, intersect, check the circle.** Slope $1$: $y = x \pm \sqrt{25} = x \pm 5$. Slope $-1$: $y = -x \pm 5$. Each line is genuinely tangent: substituting $y = x + 5$ into the ellipse gives $25x^2 + 160x + 256 = 0 = (5x+16)^2$ — a double root ✓ (and similarly for the others).


The four pairwise intersections are $(0, 5), (0, -5), (5, 0), (-5, 0)$, and all satisfy $x^2 + y^2 = 25 = a^2 + b^2$.


Total: **Answer: director circle $x^2 + y^2 = 25$ verified**


**Check:** $(\pm 5, 0)$ and $(0, \pm 5)$ all at distance $5 = \sqrt{16 + 9}$ from the origin ✓.

</details>

#### **P22**[JEE Main][practice][position test]Classify the points [formula] , [formula] , [formula] with respect to [formula…

Classify the points $(1, 1)$, $(1, 2)$, $(3, 1)$ with respect to $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: evaluate $S_1$.** $(1,1)$: $\tfrac19 + \tfrac14 - 1 = -\tfrac{23}{36} \lt 0$: inside. $(1,2)$: $\tfrac19 + 1 - 1 = \tfrac19 \gt 0$: outside. $(3,1)$: $1 + \tfrac14 - 1 = \tfrac14 \gt 0$: outside.


Answer: **$(1,1)$ inside; $(1,2)$ and $(3,1)$ outside**. (Note $(3,1)$: $x = 3$ is inside the $x$-range but the $y$-coordinate pushes it out — both coordinates matter ✓.)

</details>


### 3.6 Reflection — the whispering gallery

> [!example] Olympiad Extension — the tangent is the external bisector
>
> At a point $P$ of the ellipse the tangent makes *equal angles* with the two focal segments $PF_1$, $PF_2$ (equivalently: the *normal* bisects the angle $\angle F_1PF_2$ internally). Consequently a ray emitted from one focus reflects off the ellipse straight into the other — the whispering-gallery effect, used from cathedral domes to lithotripsy machines. The cleanest proof compares the distances travelled via any nearby point $P'$ of the ellipse: since $|PF_1| + |PF_2| = |P'F_1| + |P'F_2| = 2a$, the path $F_1 \to P \to F_2$ is a stationary path; Fermat's principle then says the angles with the tangent are equal. Chapter 6 proves it with pure angle-chasing.

#### **P24**[Olympiad][practice][angle equality]For [formula] , [formula] : compute the angles the tangent at [formula] makes …

For $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, $P = \left(\tfrac52, \tfrac{3\sqrt3}{2}\right)$: compute the angles the tangent at $P$ makes with $PF_1$ and $PF_2$ and confirm they are equal.

<details>
<summary>Answer + Reasoning</summary>

**Method: three slopes, two angles.** Tangent slope at $P$: $-\dfrac{b^2x}{a^2y} = -\dfrac{9\cdot 5/2}{25\cdot 3\sqrt3/2} = -\dfrac{45}{75\sqrt3} = -\dfrac{\sqrt3}{5}$, angle $\approx -19.11^\circ$. Ray directions: to $F_2(4,0)$: $-60.00^\circ$; to $F_1(-4,0)$: $-158.21^\circ$.


Angles with the tangent: $\left|-60 + 19.11\right| = 40.89^\circ$ and $\left|-158.21 + 19.11\right| = 139.10^\circ$, whose supplement is $40.90^\circ$ — equal within rounding.


Answer: **both angles $\approx 40.89^\circ$** — the tangent is the external bisector, and a ray from $F_1$ through $P$ reflects to $F_2$ ✓.

</details>



---
