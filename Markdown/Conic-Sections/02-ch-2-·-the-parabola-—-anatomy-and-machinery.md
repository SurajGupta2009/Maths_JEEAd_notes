# Chapter 2 — Ch 2 · The Parabola — Anatomy and Machinery

*5 sections · 11 questions*

*Chapter 2 of 6*

# The Parabola — Anatomy and Machinery

The parabola $y^2 = 4ax$ is the simplest conic — one focus, one directrix, no centre — and the proving ground for every technique the other conics will reuse. The single most profitable habit of this chapter is the *parametric point* $(at^2, 2at)$: focal chords, tangents, normals and reflection all collapse to one-line computations in $t$. Master it here and Chapters 3–5 become pattern-matching.

### 2.0 What you will be able to do

By the end of this chapter, a question like "the normal at one end of a focal chord…" should trigger a parameter reflex, not an algebraic brawl.

- Read the full anatomy of $y^2 = 4ax$ and its three reflected/rotated siblings, and of shifted parabolas $(y-k)^2 = 4a(x-h)$.
- Work entirely in the parameter $t$: chords, focal chords, tangents, normals, intersections.
- Prove and use the focal-chord package: $t_1 t_2 = -1$, length $a\left(t + \tfrac1t\right)^2$, semi-latus rectum as harmonic mean, tangents meeting on the directrix.
- Handle the normal cubic $am^3 + (2a - h)m + k = 0$ — how many normals, sum of slopes — and prove the reflection property from the isosceles triangle $SPN$.


### 2.1 Anatomy of $y^2 = 4ax$

All names in one place, for $a \gt 0$:

- **Vertex** $(0,0)$; **axis**: the $x$-axis.
- **Focus** $S(a, 0)$; **directrix** $x = -a$.
- **Latus rectum**: chord through the focus perpendicular to the axis, ends $(a, \pm 2a)$, length $4a$.
- **Focal distance** of a point $P(x,y)$ on the parabola: $|SP| = x + a$ — by the definition, it equals distance to the directrix, which is $x - (-a)$. No square roots ever.

$$ y^2 = 4ax \ \text{(opens right, focus } (a,0)\text{)} \qquad
         y^2 = -4ax \ \text{(opens left)} $$
 
$$ x^2 = 4ay \ \text{(opens up)} \qquad
         x^2 = -4ay \ \text{(opens down)} $$

A parabola with vertex $(h, k)$ and the first orientation is $(y-k)^2 = 4a(x-h)$: shift the origin, everything translates. Parabolas with vertical axis of the ordinary function type $y = Ax^2 + Bx + C$ are exactly the $x^2 = 4ay$ family after completing the square — worth remembering when a "parabola through three points" question appears: three points determine $A, B, C$ linearly.

> **💡 Key Idea — the focal distance is a coordinate, not a computation**
>
> Because the directrix is vertical, "distance to directrix" is literally $x + a$. Every focal-length question on a parabola is therefore a coordinate read-off. This fails for no reason except forgetting which way the parabola opens — check the sign of the $x^2$ or $y^2$ term first.

#### **P9**[JEE Main][practice][focal distance]Find the points on [formula] whose focal distance is [formula] .

Find the points on $y^2 = 16x$ whose focal distance is $9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: focal distance $= x + a$.** Here $a = 4$, so $x + 4 = 9
        \Rightarrow x = 5$; then $y^2 = 80$, $y = \pm 4\sqrt5$.


Answer: **$\left(5, \pm 4\sqrt5\right)$**. (Check: $80 = 16 \cdot 5$ ✓.)

</details>

#### **P10**[JEE Main][practice][latus rectum]Write the ends and the length of the latus rectum of [formula] .

Write the ends and the length of the latus rectum of $y^2 = 8x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $4y^2 = 4ax$ pattern-match.** $a = 2$: ends $(a, \pm 2a) = (2, \pm 4)$, length $4a = 8$.


Answer: **ends $(2, 4)$ and $(2, -4)$, length $8$**. (Check: both ends satisfy $y^2 = 8x$: $16 = 16$ ✓.)

</details>


### 2.2 The parametric point and focal chords

Every point of $y^2 = 4ax$ can be written as

$$ P(t) = (at^2,\ 2at), \qquad t \in \mathbb{R} $$

— verified instantly: $(2at)^2 = 4a \cdot at^2$. The parameter has meaning: the chord from the vertex to $P(t)$ has slope $\dfrac{2at}{at^2} = \dfrac{2}{t}$, and the focal distance is $|SP| = a(1 + t^2)$ — a fact used constantly below.

#### Chords and the focal condition

The chord joining $P(t_1)$ and $P(t_2)$ has slope $\dfrac{2at_1 - 2at_2}{at_1^2 - at_2^2}
    = \dfrac{2}{t_1 + t_2}$, and forcing it through $P(t_1)$ gives its equation:

$$ (t_1 + t_2)\, y \;=\; 2x + 2a\,t_1 t_2 $$

> **⛁ First Principles — why focal chords are exactly $t_1 t_2 = -1$**
>
> A chord passes through the focus $S(a, 0)$ iff $(t_1+t_2)\cdot 0 = 2a + 2at_1t_2$, i.e. iff $t_1 t_2 = -1$. So a focal chord with one end $P(t)$ has its other end at $P(-1/t)$. The two parts of the chord are $|SP(t)| = a(1+t^2)$ and $|SP(-1/t)| = a\left(1 + \tfrac{1}{t^2}\right)$, so the total length is 
> $$ a\left(2 + t^2 + \frac{1}{t^2}\right) = a\left(t + \frac{1}{t}\right)^2, $$
>  minimised at $t = \pm 1$ — the latus rectum, length $4a$, exactly as promised.

> **ƒ Named Property — the semi-latus rectum is the harmonic mean**
>
> $\dfrac{1}{|SP(t)|} + \dfrac{1}{|SP(-1/t)|} = \dfrac{1}{a(1+t^2)} + \dfrac{t^2}{a(1+t^2)}
>       = \dfrac1a = \dfrac{2}{2a}$. So for *every* focal chord, the reciprocal sum of its two parts is constant: the semi-latus rectum $l = 2a$ is the harmonic mean of the two parts. This survives verbatim for the ellipse and hyperbola (with $l = b^2/a$) — a favourite Olympiad fact.

#### **S3**[JEE Adv][solved][focal chord]One end of a focal chord of [formula] is the point with parameter [formula] . …

One end of a focal chord of $y^2 = 8x$ is the point with parameter $t = 2$. Find the other end, the chord's length, and verify the harmonic-mean property.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** other end $= P(-1/t) = P(-\tfrac12)$.


Here $a = 2$. Points: $P(2) = (8, 8)$; $P(-\tfrac12) = (2\cdot\tfrac14,\ 4\cdot(-\tfrac12)) = (\tfrac12, -2)$.


Length: $a\left(t + \tfrac1t\right)^2 = 2\left(2 + \tfrac12\right)^2 = 2 \cdot \tfrac{25}{4} = \dfrac{25}{2}$.


Harmonic mean of the parts: $|SP(2)| = 2(1+4) = 10$, $|SP(-\tfrac12)| = 2(1+\tfrac14) = \tfrac52$; $\dfrac{2}{\tfrac{1}{10} + \tfrac{2}{5}} = \dfrac{2}{\tfrac12} = 4 = 2a$ — the semi-latus rectum ✓.


Total: **Answer: other end $\left(\tfrac12, -2\right)$, length $\tfrac{25}{2}$**


**Check:** the chord through $(8,8)$ and $(\tfrac12,-2)$ has slope $\tfrac{10}{7.5} = \tfrac43$ and passes $(2, 0)$: $8 + \tfrac43(2-8) = 0$ ✓.

</details>

#### **P11**[JEE Adv][practice][focal chord]One end of a focal chord of [formula] is [formula] . Find the other end and th…

One end of a focal chord of $y^2 = 4x$ is $P(-3)$. Find the other end and the length of the chord.

<details>
<summary>Answer + Reasoning</summary>

**Method: $t_1t_2 = -1$.** Other end $= P(\tfrac13) = \left(\tfrac19, \tfrac23\right)$. Length $= a\left(t + \tfrac1t\right)^2 = \left(-3 - \tfrac13\right)^2 = \left(-\tfrac{10}{3}\right)^2 = \tfrac{100}{9}$.


Answer: **$\left(\tfrac19, \tfrac23\right)$, length $\tfrac{100}{9}$**. (Check: chord slope $= \tfrac{2/3 + 6}{1/9 - 9} = -\tfrac34$, and it passes $(1,0)$: $-6 + \tfrac34 \cdot 8 = 0$ ✓.)

</details>

#### **P12**[JEE Adv][practice][tangent intersection]The tangents at [formula] and [formula] on [formula] meet at [formula] . Show …

The tangents at $(4, 4)$ and $(4, -4)$ on $y^2 = 4x$ meet at $T$. Show that $T$ lies on the directrix, and write the chord of contact.

<details>
<summary>Answer + Reasoning</summary>

**Method: tangents at $t_1, t_2$ meet at $\left(at_1t_2,\ a(t_1+t_2)\right)$.** Here $t_1 = 2, t_2 = -2$: $T = (-4, 0)$ — exactly on the directrix $x = -4$.


The chord of contact of $T$ is the line through $(4, \pm4)$: the vertical line $x = 4$ (from the $T = 0$ form: $0 \cdot y = 2(x - 4)$).


Answer: **$T = (-4, 0)$ on $x = -4$; chord of contact $x = 4$**. (This is the parabola's "director circle" behaviour — perpendicular tangents meet on the directrix; see Chapter 5 ✓.)

</details>



### 2.3 Tangent, normal, and the normal cubic

Two lines do all the work. At the point $P(t) = (at^2, 2at)$:

$$ \text{tangent: } ty = x + at^2 \qquad\qquad
         \text{normal: } y = -tx + 2at + at^3 $$

In slope form (eliminate $t$, with $m = \tfrac1t$ for the tangent and $m = -t$ for the normal):

$$ \text{tangent of slope } m:\ y = mx + \frac{a}{m},\ \text{contact } \left(\frac{a}{m^2}, \frac{2a}{m}\right) $$
 
$$ \text{normal of slope } m:\ y = mx - 2am - am^3 $$

Three classical by-products, each a one-line proof from the formulas above:

- The tangent at $P(t)$ meets the axis at $T(-at^2, 0)$, so the **subtangent** (foot $M$ to $T$ along the axis) is $2 \times$ the abscissa of $P$.
- The normal meets the axis at $N(at^2 + 2a, 0)$, so the **subnormal** $|NG|$ (from the foot $M(at^2,0)$ to $N$) is $2a$ — *the same for every point*. The parabola is the only conic with a constant subnormal.
- The foot of the perpendicular from the focus to any tangent is $(0, at)$ — it always lies on the tangent at the vertex $x = 0$. (Chapter 2's own "circle of Apollonius".)

> **⛁ First Principles — normals from a point: a cubic, hence three**
>
> A normal of slope $m$ passes through a given point $(h, k)$ iff $k = mh - 2am - am^3$, i.e.
>
>
>
> $$ am^3 + (2a - h)m + k = 0. $$
>
>
>
> A cubic has at most three real roots, so **at most three normals** can be drawn from a point to a parabola — and since the cubic's $m^2$ coefficient is zero, $\boxed{m_1 + m_2 + m_3 = 0}$: the three slopes always sum to zero. Whether all three roots are real depends on $(h,k)$; points "far enough right" see three normals.

#### **S4**[JEE Adv][solved][normal cubic]Find all the normals drawn from [formula] to the parabola [formula] , with the…

Find all the normals drawn from $(6, 0)$ to the parabola $y^2 = 4x$, with their feet.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: the cubic, then the feet.** With $a = 1, h = 6, k = 0$: $m^3 - 4m = m(m-2)(m+2) = 0$, so $m \in \{0, 2, -2\}$ — three normals, slopes summing to $0$ as guaranteed.


Feet: the normal of slope $m$ touches the parabola at $(am^2, -2am)$ (i.e. $t = -m$):


- $m = 0$: foot $(0, 0)$, normal $y = 0$ — the axis itself.
- $m = 2$: foot $(4, -4)$, normal $y = 2x - 12$.
- $m = -2$: foot $(4, 4)$, normal $y = -2x + 12$.


Total: **Answer: three normals, feet $(0,0), (4, \pm 4)$**


**Check:** all three lines pass $(6,0)$: $0 = 0$, $12 - 12 = 0$, $-12 + 12 = 0$ ✓; and $(4, \pm 4)$ lie on $y^2 = 4x$ ✓.

</details>

#### **P13**[JEE Adv][practice][midpoint chord]The chord-with-midpoint formula [formula] (Chapter 5) applied to [formula] wit…

The chord-with-midpoint formula $T = S_1$ (Chapter 5) applied to $y^2 = 4x$ with "midpoint" $\left(\tfrac94, 3\right)$ produces a single line. Show that this line is the tangent at that point, and explain why.

<details>
<summary>Answer + Reasoning</summary>

**Method: notice the midpoint lies on the curve.** $\left(\tfrac94\right)\cdot 4 = 9 = 3^2$ — the point is on the parabola (it is $P(\tfrac32)$). A "chord" bisected at a point of the curve must have both ends coalescing there: the chord degenerates to the tangent.


Compute: $T = S_1$ reads $yy_1 - 2(x + x_1) = y_1^2 - 4x_1$, i.e. $3y - 2x - \tfrac92 = 9 - 9 = 0$, so $3y = 2x + \tfrac92$. Compare the tangent at $t = \tfrac32$: $ty = x + at^2 \Rightarrow \tfrac32 y = x + \tfrac94$, i.e. $3y = 2x + \tfrac92$ — identical.


Answer: **the formula returns the tangent $3y = 2x + \tfrac92$**, because a chord bisected on the curve is a doubled point ✓.

</details>

#### **P14**[JEE Main][practice][subnormal]For [formula] , write the normal at the point with [formula] , find where it m…

For $y^2 = 8x$, write the normal at the point with $t = 1$, find where it meets the axis, and verify that the subnormal equals $2a$.

<details>
<summary>Answer + Reasoning</summary>

**Method: plug into $y = -tx + 2at + at^3$.** With $a = 2, t = 1$: $y = -x + 4 + 2 = -x + 6$. It meets the axis at $N(6, 0)$.


The foot of $P(2, 4)$ on the axis is $M(2, 0)$; the subnormal is $|NG| = 6 - 2 = 4 = 2a$ ✓.


Answer: **normal $y = -x + 6$, meets axis at $(6,0)$, subnormal $4 = 2a$**.

</details>


### 2.4 Reflection — the parabola as a focusing machine

Headlights and satellite dishes are parabolic for one reason: rays parallel to the axis reflect through the focus. The proof is a picture with two equal lengths.

> **★ Olympiad Extension — reflection from the isosceles triangle $SPN$**
>
> Let the normal at $P(t)$ meet the axis at $N$ and let $S$ be the focus. From §2.3, $N = (at^2 + 2a, 0)$, so $|SN| = |at^2 + 2a - a| = a(1 + t^2)$. But the focal distance is $|SP| = a(1 + t^2)$ too. Hence $SP = SN$: triangle $SPN$ is **isosceles**, so the normal makes equal angles with $SP$ and with the axis. A ray travelling along the axis direction hits the tangent at $P$; the normal is the angle bisector between the reflected ray and the axis direction — the reflected ray must be the mirror image, i.e. it passes through $S$. Conversely (optics is reversible) rays emitted from $S$ leave parallel to the axis: the headlight principle.

#### **S5**[Olympiad][solved][reflection verified]A laser travelling parallel to the [formula] -axis (in the [formula] direction…

A laser travelling parallel to the $x$-axis (in the $-x$ direction) strikes $y^2 = 4x$ at $(9, 6)$. Where does the reflected ray cross the axis?

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** reflect the incident direction in the tangent line; by §2.4 the result must pass through the focus. Let us confirm numerically.


$(9,6)$ is $P(3)$. Tangent: $3y = x + 9$, i.e. $x - 3y + 9 = 0$ with unit normal $n = \tfrac{1}{\sqrt{10}}(1, -3)$. Incident direction $d = (-1, 0)$. Reflection in the line: $d' = d - 2(d \cdot n)n = (-1, 0) - 2\left(-\tfrac{1}{\sqrt{10}}\right)\tfrac{1}{\sqrt{10}}(1,-3)
        = (-1, 0) + \tfrac15(1, -3) = \left(-\tfrac45, -\tfrac35\right)$.


From $(9,6)$ in direction $\left(-\tfrac45, -\tfrac35\right)$: reaching $x = 1$ takes $t = 10$ time units, giving $y = 6 - \tfrac35 \cdot 10 = 0$. The ray crosses the axis exactly at $(1, 0)$.


Total: **Answer: through the focus $S(1, 0)$**


**Check:** the reflected slope $\tfrac{-3/5}{-4/5} = \tfrac34$ and the reflected angle with the tangent equals the incident angle $71.57^\circ$ ✓ (mirror across the $18.43^\circ$ tangent line).

</details>

#### **P15**[Olympiad][practice][foot on vertex tangent]Prove that the foot of the perpendicular from the focus of [formula] to any ta…

Prove that the foot of the perpendicular from the focus of $y^2 = 4ax$ to any tangent lies on the tangent at the vertex, and compute that foot for the tangent at $t = 3$ when $a = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: foot-of-perpendicular formula.** Tangent at $t$: $x - ty + at^2 = 0$. The foot from $S(a, 0)$:



$$ \left(a - \frac{a + at^2}{1 + t^2},\ 0 + \frac{t(a+at^2)}{1+t^2}\right) = (0,\ at). $$



Its $x$-coordinate is $0$ for every $t$ — the foot rides up and down the line $x = 0$, the tangent at the vertex.


Answer: **foot $= (0, at)$; for $a = 1, t = 3$: $(0, 3)$**. (Check: $(0,3)$ on $x = 0$ and $3y = x + 9$ passes it: $9 = 9$ ✓.)

</details>

#### **P16**[Olympiad][practice][perpendicular tangents]Show that the tangents at [formula] and [formula] on [formula] are perpendicul…

Show that the tangents at $t = 1$ and $t = -1$ on $y^2 = 4x$ are perpendicular, and that they meet on the directrix. Which general facts are these instances of?

<details>
<summary>Answer + Reasoning</summary>

**Method: compute both lines.** $t = 1$: $y = x + 1$ (slope $1$); $t = -1$: $-y = x + 1$, i.e. $y = -x - 1$ (slope $-1$). Product of slopes $-1$: perpendicular. Intersection: $x + 1 = -x - 1 \Rightarrow x = -1, y = 0$: the point $(-1, 0)$ lies on the directrix $x = -1$.


Answer: **perpendicular, meeting at $(-1, 0)$**. General facts: tangents at $t_1, t_2$ are perpendicular exactly when $t_1t_2 = -1$, and their intersection $\left(at_1t_2,\ a(t_1+t_2)\right)$ then sits at $(-a, 0)$ — on the directrix. The locus of intersection of perpendicular tangents to a parabola is its directrix (the "director circle" degenerates to a line), and the tangents at the ends of any focal chord ($t_1t_2 = -1$) are exactly such a pair ✓.

</details>



---

