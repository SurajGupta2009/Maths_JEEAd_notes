# Chapter 6 — Ch 6 · The Olympiad Frontier — Reflection, Confocals and Triangles

*6 sections · 10 questions*

*Chapter 6 of 6*

# The Olympiad Frontier — Reflection, Confocals and Triangles

Olympiad conic problems are rarely "find the equation" problems. They are geometry problems in which a conic appears as a *machine for an angle or a distance*: a mirror that sends one focus to the other, a pair of confocal curves that must meet at right angles, a rectangular hyperbola that smuggles an orthocentre into the picture. This chapter builds those machines, proves the big theorems, and works them numerically until they are yours.

### 6.0 What you will be able to do

- Prove and deploy all three reflection properties (parabola, ellipse, hyperbola) — the backbone of billiard and optics problems.
- Prove confocal orthogonality with one gradient computation, and build confocal pairs on demand.
- Use the theorem *rectangular hyperbola through a triangle passes through the orthocentre*, find hyperbola centres, and connect them to the nine-point circle.
- Handle Simson lines, Steiner lines and Lambert's inscribed-parabola theorem.
- Quote Pascal and Brianchon and use their degenerate forms on tangents.


### 6.1 The three reflection properties, proved

> **⛁ First Principles — ellipse: minimality gives the angles**
>
> Let the tangent at $P$ meet the conic only at $P$, and reflect the far focus $F_2$ across the tangent to $F_2'$. For *any* point $Q$ of the tangent line:
>
>
>
> $$ |QF_1| + |QF_2| \;=\; |QF_1| + |QF_2'| \;\ge\; |F_1F_2'|, $$
>
>
>
> with equality exactly when $Q$ lies on segment $F_1F_2'$. But on the ellipse itself the sum is constantly $2a$, and $P$ achieves $|PF_1| + |PF_2'| = |PF_1| + |PF_2| = 2a$: so $P$ lies on $F_1F_2'$ and the tangent line touches the ellipse only there. Collinearity of $F_1, P, F_2'$ means the tangent makes equal angles with $PF_1$ and $PF_2$ — and the law of reflection does the rest. Every ingredient is Chapter 1's definition plus the triangle inequality.

> **★ Olympiad Extension — the same proof, flipped signs**
>
> **Hyperbola:** with the difference $\big||PF_1| - |PF_2|\big| = 2a$, reflecting $F_2$ gives $|PF_1| - |PF_2'| = \pm 2a$, so $F_1, P, F_2'$ are again collinear, while for other $Q$ on the tangent the reverse triangle inequality makes $\big||QF_1| - |QF_2|\big| \lt |F_1F_2'|$. Same conclusion: the tangent bisects the angle between the focal radii — a ray aimed at one focus reflects as if from the other. **Parabola:** the far focus "at infinity" makes the incident rays parallel: Chapter 2's $SP = SN$ is the same proof collapsed to one focus. Billiards inside an elliptical table: any shot through one focus returns through the other, forever — the seed of Poncelet's closure theorem.

#### **P41**[JEE Main][practice][whispering gallery]A whispering gallery has ceiling profile [formula] (units: metres). Two people…

A whispering gallery has ceiling profile $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$ (units: metres). Two people stand at the foci. How far apart are they, and how far is each from the nearest wall (vertex)?

<details>
<summary>Answer + Reasoning</summary>

**Method: reflection property says the foci are the "hot spots".** $c = \sqrt{25 - 9} = 4$: foci $(\pm 4, 0)$, distance apart $8$ m; nearest vertex $(\pm 5, 0)$, so $1$ m away.


Answer: **8 m apart; each 1 m from the nearest vertex**. (Whispers at one focus converge at the other — an application of §6.1 ✓.)

</details>

#### **P42**[Olympiad][practice][hyperbola bisector]Verify numerically that at [formula] on [formula] , the tangent bisects the an…

Verify numerically that at $P = (4\sqrt2, 3)$ on $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, the tangent bisects the angle between the focal segments.

<details>
<summary>Answer + Reasoning</summary>

**Method: three slopes, two angles.** $P$ is on the curve: $\tfrac{32}{16} - 1 = 1$ ✓. Tangent slope: $\dfrac{b^2x}{a^2y} = \dfrac{9\cdot4\sqrt2}{16\cdot3} = \dfrac{3\sqrt2}{4}$, direction angle $\approx 46.70^\circ$. Focal rays: to $F_2(5,0)$: $\approx -102.37^\circ$; to $F_1(-5,0)$: $\approx -164.26^\circ$. Halfway between the rays: $\approx -133.32^\circ$, which is exactly the tangent direction modulo $180^\circ$ ($46.70^\circ - 180^\circ = -133.30^\circ$, equal up to rounding).


Answer: **both angles $\approx 30.96^\circ$** — the tangent is the internal bisector, mirror-image of the ellipse's external bisector ✓.

</details>

#### **P47**[JEE Adv][practice][billiard]On the elliptical billiard table [formula] , a ball is shot from the focus [fo…

On the elliptical billiard table $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, a ball is shot from the focus $(4, 0)$ to the point $(0, 3)$. Show that after one cushion contact it passes through the other focus.

<details>
<summary>Answer + Reasoning</summary>

**Method: reflect the direction in the tangent.** At $(0,3)$ (top of the ellipse) the tangent is horizontal: $y = 3$. The ball travels from $(4,0)$ to $(0,3)$ along direction $(-4, 3)$; reflecting in the horizontal cushion gives $(-4, -3)$. From $(0,3)$ with direction $(-4,-3)$: at parameter $t=1$ we reach $(-4, 0)$ — the other focus.


Answer: **yes — it passes through $(-4, 0)$**, exactly as §6.1 predicts ✓.

</details>


### 6.2 Confocal conics meet at right angles

Fix the foci $(\pm c, 0)$. The ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ with $a^2 - b^2 = c^2$ and the hyperbola $\dfrac{x^2}{A^2} - \dfrac{y^2}{B^2} = 1$ with $A^2 + B^2 = c^2$ are called a **confocal pair**. Through every point off the axes passes exactly one confocal ellipse and one confocal hyperbola — and:

> **⛁ First Principles — orthogonality from two unit vectors**
>
> The ellipse is a level set of $u = d_1 + d_2$ (sum of distances to the foci); the confocal hyperbola through the same point is a level set of $v = d_1 - d_2$. The gradient of $u$ is $\mathbf{u}_1 + \mathbf{u}_2$, where $\mathbf{u}_i$ are the unit vectors pointing from the two foci to $P$; the gradient of $v$ is $\mathbf{u}_1 - \mathbf{u}_2$. Their dot product:
>
>
>
> $$ (\mathbf{u}_1 + \mathbf{u}_2)\cdot(\mathbf{u}_1 - \mathbf{u}_2)
>          \;=\; |\mathbf{u}_1|^2 - |\mathbf{u}_2|^2 \;=\; 1 - 1 \;=\; 0. $$
>
>
>
> Gradients are normals; perpendicular normals mean **perpendicular tangents**. The entire theorem is the algebra of a rhombus. This is why elliptical coordinates $(d_1 + d_2, d_1 - d_2)$ form an orthogonal grid — the parameterisation behind separation of variables in Laplace's equation.

#### **S15**[Olympiad][solved][confocal pair]Find the confocal hyperbola through [formula] for the ellipse [formula] , and …

Find the confocal hyperbola through $\left(\tfrac32, \sqrt3\right)$ for the ellipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$, and verify the tangents are perpendicular there.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** $c^2 = 9 - 4 = 5$. Distances from $\left(\tfrac32, \sqrt3\right)$ to $(\pm\sqrt5, 0)$: $d_1^2 = \left(\tfrac32 - \sqrt5\right)^2 + 3 = \tfrac{41}{4} - 3\sqrt5$ and $d_2^2 = \left(\tfrac32 + \sqrt5\right)^2 + 3 = \tfrac{41}{4} + 3\sqrt5$; since $d_1 + d_2 = 2a = 6$ (P is on the ellipse), $(d_2 - d_1)(d_2 + d_1) = d_2^2 - d_1^2 = 6\sqrt5$, giving $d_2 - d_1 = \sqrt5$.


Hyperbola: $2A = \sqrt5$, so $A^2 = \tfrac54$, $B^2 = c^2 - A^2 = 5 - \tfrac54 = \tfrac{15}{4}$: $\dfrac{x^2}{5/4} - \dfrac{y^2}{15/4} = 1$. Check the point: $\dfrac{9/4}{5/4} - \dfrac{3}{15/4} = \dfrac95 - \dfrac45 = 1$ ✓.


Slopes: ellipse $-\dfrac{b^2x}{a^2y} = -\dfrac{4\cdot 3/2}{9\sqrt3} = -\dfrac{2}{3\sqrt3}$; hyperbola $\dfrac{B^2x}{A^2y} = \dfrac{(15/4)(3/2)}{(5/4)\sqrt3} = \dfrac{3\sqrt3}{2}$. Product: $-\dfrac{2}{3\sqrt3}\cdot\dfrac{3\sqrt3}{2} = -1$ ✓.


Total: **Answer: $\dfrac{x^2}{5/4} - \dfrac{y^2}{15/4} = 1$; perpendicular tangents**

</details>

#### **P45**[Olympiad][practice][confocal pair]For the ellipse [formula] , find the confocal hyperbola through [formula] and …

For the ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, find the confocal hyperbola through $P = \left(\tfrac52, \tfrac{3\sqrt3}{2}\right)$ and verify orthogonality there.

<details>
<summary>Answer + Reasoning</summary>

**Method: $c = 4$; use the focal distances.** From P21: $d_1 = 3, d_2 = 7$, so $2A = |d_2 - d_1| = 4$: $A = 2$, $B^2 = 16 - 4 = 12$.


Answer: **$\dfrac{x^2}{4} - \dfrac{y^2}{12} = 1$**. Slopes: ellipse $-\dfrac{9\cdot 5/2}{25\cdot 3\sqrt3/2} = -\dfrac{\sqrt3}{5}$; hyperbola $\dfrac{12\cdot 5/2}{4\cdot 3\sqrt3/2} = \dfrac{5}{\sqrt3}$; product $-1$ ✓.

</details>


### 6.3 Rectangular hyperbolas through a triangle

A rectangular hyperbola with asymptotes parallel to the coordinate axes has equation $xy + Dx + Ey + F = 0$ — three parameters after scaling, so **exactly one** such hyperbola passes through three given points. Where does it go next?

> **⛁ First Principles — the orthocentre theorem, via parameters**
>
> Put the hyperbola in the pure form $xy = c^2$ (shifting the centre only relabels points) and write the three vertices as $P(t_i) = \left(ct_i, \tfrac{c}{t_i}\right)$. The chord $t_2t_3$ has slope $\dfrac{c/t_2 - c/t_3}{ct_2 - ct_3} = -\dfrac{1}{t_2t_3}$, so the altitude from $t_1$ has slope $t_2t_3$: $y = t_2t_3x - ct_1t_2t_3 + \tfrac{c}{t_1}$. Intersecting two altitudes gives the orthocentre
>
>
>
> $$ H \;=\; \left(-\frac{c}{t_1t_2t_3},\; -c\,t_1t_2t_3\right) \;=\; P\!\left(-\frac{1}{t_1t_2t_3}\right), $$
>
>
>
> which is a point of the hyperbola. **The orthocentre of any triangle inscribed in a rectangular hyperbola lies on the hyperbola.** The parameter bookkeeping even names the point: its parameter is $-\tfrac{1}{t_1t_2t_3}$.

> **★ Olympiad Extension — centres ride the nine-point circle**
>
> The **centre** of $xy + Dx + Ey + F = 0$ is the intersection of its asymptotes $x = -E$, $y = -D$. Theorem: as the rectangular hyperbola through three fixed points varies, its centre traces the **nine-point circle** of the triangle (the circle through the side midpoints). One consequence: the unique rectangular hyperbola through three points *and* their orthocentre is the one whose centre is a specified nine-point point — and the triangle's circumcircle leader to Feuerbach territory. Numerically verified below in P44.

#### **S14**[Olympiad][solved][orthocentre theorem]Find the rectangular hyperbola (asymptotes parallel to the axes) through [form…

Find the rectangular hyperbola (asymptotes parallel to the axes) through $(1,1)$, $(2,5)$, $(5,3)$; find the triangle's orthocentre; and verify it lies on the hyperbola.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: solve for $D, E, F$ in $xy + Dx + Ey + F = 0$.** The three conditions: $1 + D + E + F = 0$; $10 + 2D + 5E + F = 0$; $15 + 5D + 3E + F = 0$. Subtracting pairs: $9 + D + 4E = 0$ and $14 + 4D + 2E = 0$, i.e. $7 + 2D + E = 0$. Solving: $E = -\tfrac{11}{7}$, $D = -\tfrac{19}{7}$, $F = \tfrac{23}{7}$ — multiply by 7:



$$ 7xy - 19x - 11y + 23 = 0. $$



**Orthocentre:** slope of the side from $(2,5)$ to $(5,3)$ is $-\tfrac23$: altitude from $(1,1)$ has slope $\tfrac32$. Slope from $(1,1)$ to $(5,3)$ is $\tfrac12$: altitude from $(2,5)$ has slope $-2$. Solving $y - 1 = \tfrac32(x-1)$ with $y - 5 = -2(x - 2)$: $x = \tfrac{19}{7}$, $y = \tfrac{25}{7}$.


**Verify:** $7\cdot\tfrac{19}{7}\cdot\tfrac{25}{7} - 19\cdot\tfrac{19}{7} - 11\cdot\tfrac{25}{7} + 23
        = \tfrac{475 - 361 - 275 + 161}{7} = 0$ ✓.


Total: **Answer: $7xy - 19x - 11y + 23 = 0$; $H = \left(\tfrac{19}{7}, \tfrac{25}{7}\right)$ on it**

</details>

#### **P43**[Olympiad][practice][orthocentre theorem]Repeat S14 for the triangle [formula] , [formula] , [formula] : find the hyper…

Repeat S14 for the triangle $(1, 2)$, $(3, 6)$, $(7, 0)$: find the hyperbola, the orthocentre, and verify.

<details>
<summary>Answer + Reasoning</summary>

**Method: same three-condition solve.** Conditions: $2 + D + 2E + F = 0$; $18 + 3D + 6E + F = 0$; $7D + F = 0$. From the last, $F = -7D$; substituting: $D = -\tfrac67$, $E = -\tfrac{25}{7}$, $F = 6$. Hyperbola: $7xy - 6x - 25y + 42 = 0$.


**Orthocentre:** side $(3,6)$-$(7,0)$ has slope $-\tfrac32$: altitude from $(1,2)$ has slope $\tfrac23$. Side $(1,2)$-$(7,0)$ has slope $-\tfrac13$: altitude from $(3,6)$ has slope $3$. Solving: $H = \left(\tfrac{13}{7}, \tfrac{18}{7}\right)$.


Answer: **$7xy - 6x - 25y + 42 = 0$; $H = \left(\tfrac{13}{7}, \tfrac{18}{7}\right)$**. (Check: $7\cdot\tfrac{13}{7}\cdot\tfrac{18}{7} - \tfrac{78}{7} - \tfrac{450}{7} + 42 =
        \tfrac{234 - 78 - 450 + 294}{7} = 0$ ✓.)

</details>

#### **P44**[Olympiad][practice][nine-point circle]Show that the centre of P43's hyperbola lies on the nine-point circle of its t…

Show that the centre of P43's hyperbola lies on the nine-point circle of its triangle.

<details>
<summary>Answer + Reasoning</summary>

**Method: two circles, one distance.** Centre: asymptotes $x = -E = \tfrac{25}{7}$, $y = -D = \tfrac67$: centre $C = \left(\tfrac{25}{7}, \tfrac67\right)$. Side midpoints: $(2, 4)$, $(5, 3)$, $(4, 1)$; the circle through them has centre $N = \left(\tfrac{45}{14}, \tfrac{37}{14}\right)$ and radius squared $\tfrac{650}{196}$. Then



$$ |CN|^2 = \left(\tfrac{25}{7} - \tfrac{45}{14}\right)^2 + \left(\tfrac67 - \tfrac{37}{14}\right)^2
        = \left(\tfrac{5}{14}\right)^2 + \left(-\tfrac{25}{14}\right)^2 = \tfrac{650}{196}. $$



Answer: **$|CN|^2 = \tfrac{650}{196} = R^2$: the centre lies on the nine-point circle** ✓.

</details>


### 6.4 Simson lines, Steiner lines, and Lambert's parabola

**Simson line.** For a point $P$ on the circumcircle of a triangle, the feet of the perpendiculars from $P$ to the three sides are **collinear** (proof: two angle chases with cyclic quadrilaterals — each pair of feet subtends a right angle with a side, so both lie on the circle with diameter $P$ + vertex, and the angles add to a straight line).

**Steiner line.** Reflect $P$ across the three sides: the three reflections are also collinear — the **Steiner line**, parallel to the Simson line, which is its image under the homothety centred at $P$ with ratio $\tfrac12$.

> **★ Olympiad Extension — Lambert's theorem**
>
> A parabola *inscribed* in a triangle (tangent to all three sides) has its focus on the circumcircle — and its **directrix is the Steiner line of that focus**. Why: the parabola with focus $F$ and directrix $\ell$ is tangent to a line $m$ exactly when the reflection of $F$ across $m$ lies on $\ell$ (the equal-angle definition of tangency). For the parabola to hug all three sides, $\ell$ must pass through all three reflections of $F$ — which is precisely the Steiner line, and exists precisely when $F$ is on the circumcircle. This links Chapter 2's curve to the triangle's circle in one stroke, and it is a standing ISL/Olympiad construction: *given a triangle, construct a parabola tangent to its sides*.

#### **P46**[Olympiad][practice][Simson + Steiner]For the right triangle [formula] , [formula] , [formula] and the point [formul…

For the right triangle $(0,0)$, $(4,0)$, $(0,3)$ and the point $P = (2,4)$: verify $P$ is on the circumcircle, find the Simson line and the Steiner line, and deduce the directrix of the inscribed parabola with focus $P$.

<details>
<summary>Answer + Reasoning</summary>

**Method: compute everything.** Circumcircle of the $3\text{-}4\text{-}5$ triangle: $x^2 + y^2 - 4x - 3y = 0$; $P = (2,4)$: $4 + 16 - 8 - 12 = 0$ ✓.


Feet: to $y = 0$: $(2, 0)$; to $x = 0$: $(0, 4)$; to $3x + 4y = 12$: $\left(\tfrac45, \tfrac{12}{5}\right)$. All three satisfy $y = -2x + 4$: **Simson line $y = -2x + 4$**.


Reflections: across $y=0$: $(2, -4)$; across $x=0$: $(-2, 4)$; across the hypotenuse: $\left(-\tfrac25, \tfrac45\right)$. All on $y = -2x$: **Steiner line $y = -2x$** — parallel to the Simson line ✓.


Answer: **Simson $y = -2x + 4$; Steiner $y = -2x$; the inscribed parabola with focus $(2,4)$ has directrix $y = -2x$** (Lambert ✓).

</details>


### 6.5 Pascal, Brianchon, and a construction worth knowing

> **★ Olympiad Extension — the two hexagon theorems**
>
> **Pascal's theorem.** For six points on a conic, the three intersections of opposite sides of the hexagon are collinear. **Brianchon's theorem.** For six tangents to a conic, the three "main diagonals" of the circumscribed hexagon are concurrent. The two are polar duals of each other — polarity (Chapter 5) maps one to the other. The olympiad workhorse is the *degenerate* version: let two adjacent vertices coincide, and the "side" between them becomes the tangent there. With *two* pairs coinciding you get the theorem that the intersections of two pairs of tangents and one pair of chords line up — instantly producing collinearity/concurrency conclusions that coordinate bashing would take a page to reach. (Poncelet's porism — infinitely many triangles inscribed in one conic and circumscribed about another — is the deep cousin of the billiard observation in §6.1.)

#### **P48**[Olympiad][practice][auxiliary circle]For [formula] at eccentric angle [formula] , show that the ellipse tangent and…

For $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ at eccentric angle $45^\circ$, show that the ellipse tangent and the auxiliary-circle tangent (at the corresponding circle point) meet the $x$-axis at the same point $(a\sec\theta, 0)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: two tangent lines, two axis intercepts.** Ellipse tangent (S7): $3x + 4y = 12\sqrt2$: meets $y = 0$ at $x = 4\sqrt2$. Circle point $(2\sqrt2, 2\sqrt2)$ on $x^2 + y^2 = 16$: tangent $2\sqrt2x + 2\sqrt2y = 16$, i.e. $x + y = 4\sqrt2$: meets $y = 0$ at $x = 4\sqrt2$. Same point — and $a\sec\theta = 4/\cos 45^\circ = 4\sqrt2$ ✓.


Answer: **both meet the $x$-axis at $(4\sqrt2, 0)$** — the squash map sends circle tangents to ellipse tangents through a common axis point, the fact that makes the eccentric-angle parametrisation coherent ✓.

</details>

#### The formula vault — everything at a glance

$$ \begin{array}{ll}
      \text{reflection} &amp; \text{ellipse: tangent = external bisector; hyperbola: internal; parabola: axis rays focus} \\
      \text{confocal} &amp; a^2 - b^2 = A^2 + B^2 = c^2;\ \text{orthogonal at every common point} \\
      \text{rect. hyp.} &amp; xy + Dx + Ey + F = 0 \text{ through } A, B, C \Rightarrow H \text{ on it; centre on 9-pt circle} \\
      \text{Simson/Steiner} &amp; \text{feet collinear; reflections collinear; Steiner } \parallel \text{ Simson} \\
      \text{Lambert} &amp; \text{inscribed parabola} \Leftrightarrow \text{focus on circumcircle; directrix = Steiner line} \\
      \text{Pascal/Brianchon} &amp; \text{opposite-side intersections collinear / diagonals concurrent}
      \end{array} $$




---

