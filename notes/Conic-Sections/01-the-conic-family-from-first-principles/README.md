# Chapter 1 — The Conic Family from First Principles

*5 sections · 10 questions*

*Chapter 1 of 6*

# The Conic Family from First Principles

Every curve in this module is born twice: once as a slice of a double cone, and once as a locus built from a point, a line and a single number $e$. The slice picture explains *why* the three curves belong to one family; the locus definition is what you will actually compute with for the next five chapters. This chapter derives all three standard forms from scratch, so that no formula later ever has to be memorised.

### 1.0 What you will be able to do

This chapter is the load-bearing wall of the module. Everything later — focal chords, polars, confocals — is the definition below wearing a different hat.

- Explain how one plane cutting one double cone produces the circle, ellipse, parabola and hyperbola — and the three degenerate cases.
- Derive $y^2 = 4ax$, $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ and $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ from their distance definitions, and read off foci, directrices, eccentricity and latus rectum from any of them.
- Convert fluently between "locus story" and "equation": given a focus, a directrix and $e$, write the conic; given the conic, recover all four ingredients.
- Use eccentricity as the classification number: $e = 0$ circle, $0 \lt e \lt 1$ ellipse, $e = 1$ parabola, $e \gt 1$ hyperbola — and say what each boundary case means.


### 1.1 Slicing the double cone

Take two identical right circular cones placed tip to tip along a vertical axis. Slice this double cone with a plane and watch the tilt angle $\beta$ between the plane and the axis, compared with the semi-vertical angle $\alpha$ of the cone:

- $\beta = 90^\circ$: the slice is a **circle**.
- $\alpha \lt \beta \lt 90^\circ$: a closed oval — an **ellipse**.
- $\beta = \alpha$: the plane is parallel to one generator line — a **parabola**.
- $0 \le \beta \lt \alpha$: the plane cuts *both* halves — a **hyperbola**.
- Degenerate tilts: through the apex only — a point ($\beta \gt \alpha$), one line ($\beta = \alpha$), or a pair of lines ($\beta \lt \alpha$).

> **⛁ First Principles — Dandelin's spheres: why the foci are hiding in the cone**
>
> For the ellipse, slide one sphere into each half of the cone so that each sphere touches the cutting plane (at points $F_1, F_2$) and rests tangent to the cone along a circle. Any straight generator line of the cone crosses both tangent circles, and the slant distance between those two circles *along the generator is the same for every generator*. Each segment of the generator is also a tangent segment from the slice point $P$ to one of the spheres, and tangent segments from $P$ to a sphere are equal — one pair ends at $F_1$, the other at $F_2$. So $|PF_1| + |PF_2|$ equals that constant slant length: the ellipse is born with its foci and its constant sum built in. The same argument with one sphere (or with the generators of the second half) produces the parabola and hyperbola versions. Nothing here is a coordinate computation — the distance definitions are *native* to the cone.

The vocabulary this fixes for the whole module: the curves are called **conic sections**, or simply **conics**; the special points and lines revealed by Dandelin's spheres are the **foci** and **directrices**; and the tilt of the slice is measured by one number — the eccentricity of §1.2.

> **📌 Note — the three degenerate conics are real exam objects**
>
> A "conic" equation can collapse: a point, a single line, or a pair of lines. JEE Advanced loves asking whether a given second-degree equation represents a degenerate conic, and the answer is always decided by attempting a factorisation or by checking a discriminant. We will meet genuine examples in P8 and Q5 of the paper.


### 1.2 The focus-directrix definition and eccentricity

Fix a point $F$ (the **focus**), a line $\ell$ not through $F$ (the **directrix**), and a positive number $e$ (the **eccentricity**). The locus

$$ |PF| \;=\; e\,|P\ell| $$

is a parabola when $e = 1$, an ellipse when $0 \lt e \lt 1$, and a hyperbola when $e \gt 1$. One moving distance compared to another, with one dial to turn — that is the whole family.

> **⛁ First Principles — deriving $y^2 = 4ax$ in three lines**
>
> Place the focus at $F(a, 0)$ and the directrix as $x = -a$ (so the origin sits midway, at what will be the vertex). Squaring $|PF| = |P\ell|$ for a point $P(x,y)$:
>
>
>
> $$ (x-a)^2 + y^2 = (x+a)^2 \;\Longrightarrow\; x^2 - 2ax + a^2 + y^2 = x^2 + 2ax + a^2
>       \;\Longrightarrow\; y^2 = 4ax. $$
>
>
>
> The origin is the **vertex**, the $x$-axis is the **axis** of symmetry, and the double ordinate through the focus — the **latus rectum** — has length $4a$ (put $x = a$: $y = \pm 2a$). Note what the placement bought us: the vertex sits exactly halfway between focus and directrix, so the two "distances" in the definition meet at a point where both are $a$.

> **⛁ First Principles — the ellipse from a constant sum**
>
> Take foci $F_1(-c,0), F_2(c,0)$ and impose $|PF_1| + |PF_2| = 2a$ with $a \gt c$. Squaring $|PF_1| = 2a - |PF_2|$ twice and simplifying (expand, cancel, square again) gives
>
>
>
> $$ \frac{x^2}{a^2} + \frac{y^2}{a^2 - c^2} = 1. $$
>
>
>
> Write $b^2 = a^2 - c^2$: the ellipse is $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ with $a \gt b$. The eccentricity is $e = \dfrac{c}{a}$, so $b^2 = a^2(1-e^2)$ — the ellipse's minus sign. The directrices reappear at $x = \pm \dfrac{a}{e}$: the focus-directrix form and the two-focus form are the same curve, and plugging $|PF_2| = e \cdot$ (distance to $x = a/e$) into the locus reproduces everything. The **focal distances** of a point on the ellipse are $a - ex$ and $a + ex$, summing to $2a$ on the nose.

> **⛁ First Principles — the hyperbola from a constant difference**
>
> Same foci, but impose $\big||PF_1| - |PF_2|\big| = 2a$ with $c \gt a$. The same two squarings now produce
>
>
>
> $$ \frac{x^2}{a^2} - \frac{y^2}{c^2 - a^2} = 1, $$
>
>
>
> and writing $b^2 = c^2 - a^2$ gives $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ with eccentricity $e = \dfrac{c}{a} \gt 1$ and $b^2 = a^2(e^2 - 1)$ — the hyperbola's minus sign. Directrices again at $x = \pm a/e$; focal distances $|ex \mp a|$; latus rectum $2b^2/a$, exactly as in the ellipse. The single sign in front of $y^2$ is the entire difference between the two curves.

$$ \begin{array}{c|c|c|c|c}
      \text{curve} &amp; \text{equation} &amp; e &amp; \text{foci} &amp; \text{directrices} \\ \hline
      \text{parabola} &amp; y^2 = 4ax &amp; 1 &amp; (a,0) &amp; x = -a \\
      \text{ellipse} &amp; \dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1,\ a \gt b &amp; \sqrt{1-\dfrac{b^2}{a^2}} &amp; (\pm ae, 0) &amp; x = \pm \dfrac{a}{e} \\
      \text{hyperbola} &amp; \dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1 &amp; \sqrt{1+\dfrac{b^2}{a^2}} &amp; (\pm ae, 0) &amp; x = \pm \dfrac{a}{e}
      \end{array} $$

> **⚠ Common Trap — the minus sign is the classification**
>
> In the ellipse $b^2 = a^2 - c^2$; in the hyperbola $b^2 = c^2 - a^2$. Students who reuse the ellipse relation for the hyperbola get imaginary $b$ and then "fix" it by swapping $a$ and $b$ — corrupting the latus rectum, the directrices and the asymptotes in one stroke. Decide the curve *first*, then use its relation. Also: for both central conics $c = ae$, but the ellipse has $c \lt a$ while the hyperbola has $c \gt a$ — the focus is inside the ellipse but outside the hyperbola's vertex.

#### **P1**[JEE Main][practice][parabola locus]Find the equation of the parabola with focus [formula] and directrix [formula]…

Find the equation of the parabola with focus $(2, 0)$ and directrix $x = -2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: write the locus, square once.** $\sqrt{(x-2)^2 + y^2} = x + 2$ (for $x \ge -2$); squaring: $(x-2)^2 + y^2 = (x+2)^2 \Rightarrow y^2 = 8x$.


Answer: **$y^2 = 8x$**. (Check: $(2, 4)$ satisfies $y^2 = 8x$ and is equidistant from $(2,0)$ and $x=-2$: both distances $=4$ ✓.)

</details>

#### **P2**[JEE Main][practice][ellipse locus]A point moves so that its distance from [formula] is one third of its distance…

A point moves so that its distance from $(4,0)$ is one third of its distance from the line $x = 36$. Identify the conic and find its equation and eccentricity.

<details>
<summary>Answer + Reasoning</summary>

**Method: read the focus-directrix data, then square.** Here $e = \tfrac13$, focus $(4,0)$, directrix $x = 36$. Since $\dfrac{a}{e} = 36$, we get $a = 12$ and $b^2 = a^2(1-e^2) = 144 \cdot \tfrac{8}{9} = 128$.


Answer: **ellipse $\dfrac{x^2}{144} + \dfrac{y^2}{128} = 1$, $e = \tfrac13$**. (Check $(12, 0)$: distance to focus $= 8$, to line $= 24 = 3 \times 8$ ✓.)

</details>


### 1.3 Worked examples — from words to equations and back

#### **S1**[JEE Adv][solved][focus-directrix to equation]A point moves so that its distance from [formula] is two thirds of its distanc…

A point moves so that its distance from $(2,0)$ is two thirds of its distance from the line $x = \tfrac92$. Find the locus and name the curve.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** this is the focus-directrix form with $e = \tfrac23$, so an ellipse, with focus $(2,0)$ and directrix $x = \tfrac92$.


Square the definition directly: $(x-2)^2 + y^2 = \tfrac49\left(x - \tfrac92\right)^2$. Multiply by 9: $9(x-2)^2 + 9y^2 = 4\left(x-\tfrac92\right)^2 = 4x^2 - 36x + 81$. Expanding the left side: $9x^2 - 36x + 36 + 9y^2$. Cancel $-36x$ from both sides:



$$ 5x^2 + 9y^2 = 45 \quad\Longleftrightarrow\quad \frac{x^2}{9} + \frac{y^2}{5} = 1. $$



Consistency check with the theory: $a/e = 3/(2/3) = 9/2$ — exactly the given directrix, and $ae = 2$ — exactly the given focus. Total: **Answer: $\dfrac{x^2}{9}+\dfrac{y^2}{5}=1$**


**Check:** $(3,0)$ is on the ellipse; distance to $(2,0)$ is $1$, distance to $x = 9/2$ is $3/2$, and $1 = \tfrac23 \cdot \tfrac32$ ✓.

</details>

#### **S2**[JEE Adv][solved][difference locus]A point moves so that the (absolute) difference of its distances from [formula…

A point moves so that the (absolute) difference of its distances from $(5,0)$ and $(-5,0)$ is $6$. Find the locus, its eccentricity and its directrices.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: match against the difference definition.** Constant difference $2a = 6 \Rightarrow a = 3$; foci at $(\pm 5, 0)$ give $c = 5$. Then $b^2 = c^2 - a^2 = 25 - 9 = 16$.


Locus: $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$, with $e = c/a = \tfrac53$ and directrices $x = \pm \dfrac{a}{e} = \pm \dfrac{9}{5}$.


Total: **Answer: $\dfrac{x^2}{9}-\dfrac{y^2}{16}=1,\ e=\tfrac53,\ x=\pm\tfrac95$**


**Check:** $\left(\tfrac{15}{4}, 3\right)$ is on the curve: distances $\sqrt{(15/4-5)^2+9} = \tfrac92$ and $\sqrt{(15/4+5)^2+9} = \tfrac{21}{2}$; difference $= 6$ ✓.

</details>


### 1.4 Eccentricity as the dial — boundary cases

Watch what the dial $e$ does to the standard ellipse $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$: $b^2 = a^2(1-e^2)$, so $e \to 0$ fattens the ellipse into the circle $x^2 + y^2 = a^2$ (foci collapse onto the centre), while $e \to 1^-$ flattens it towards a segment. For the hyperbola $b^2 = a^2(e^2-1)$, so $e \to 1^+$ pinches the hyperbola onto its transverse axis, and $e \to \infty$ opens the asymptote angle towards $180^\circ$. The parabola sits exactly on the boundary $e = 1$: the one conic with a single focus, no centre, and no bounded branch.

#### Two ready-to-use eccentricity gadgets

**Latus-rectum comparisons.** The latus rectum of both central conics is $\dfrac{2b^2}{a}$ — concretely $2a(1-e^2)$ for the ellipse and $2a(e^2-1)$ for the hyperbola. Any exam condition "LR equals/doubles something" is one equation in $e$.

**Asymptote angle (preview of Ch 4).** The asymptotes of the hyperbola make angle $2\alpha$ around the transverse axis with $\tan\alpha = b/a$, and one line of algebra ($\cos 2\alpha = \frac{1-\tan^2\alpha}{1+\tan^2\alpha}$ with $e^2 = \frac{a^2+b^2}{a^2}$) gives $\cos 2\alpha = \dfrac{2}{e^2} - 1$. Rectangular hyperbola ($2\alpha = 90^\circ$): $e = \sqrt2$.

> **★ Olympiad Extension — the boundaries of the definition**
>
> What happens at the edges of $|PF| = e|P\ell|$? If $\ell$ passes through $F$ and $e = 1$, squaring gives $x^2 + y^2 = x^2$: the locus is the line through $F$ parallel to $\ell$ — a *doubled* line (a degenerate parabola). If $e = 0$ with a finite directrix, $|PF| = 0$ forces the single point $F$ (a degenerate ellipse); the honest circle is the *limit* $e \to 0$ with the directrix retreating to infinity. And $e \to \infty$ with $\ell$ approaching $F$ degenerates towards a pair of lines. The non-degenerate conics are exactly the interior of this boundary — a one-parameter family in good standing.

#### **P3**[JEE Main][practice][hyperbola data]A hyperbola has foci [formula] and eccentricity [formula] . Find its equation …

A hyperbola has foci $(\pm 10, 0)$ and eccentricity $\tfrac54$. Find its equation and the length of its latus rectum.

<details>
<summary>Answer + Reasoning</summary>

**Method: $c = ae$, then $b^2 = c^2 - a^2$.** $a = c/e = 10/(5/4) = 8$, so $b^2 = 64\left(\tfrac{25}{16}-1\right) = 36$.


Answer: **$\dfrac{x^2}{64} - \dfrac{y^2}{36} = 1$; LR $= \dfrac{2b^2}{a} = 9$**. (Check $(10, \tfrac92)$: $\tfrac{100}{64} - \tfrac{81}{144}\cdot 4 = 1.5625 - 0.5625 = 1$ ✓.)

</details>

#### **P4**[JEE Main][practice][latus rectum condition]The latus rectum of an ellipse equals its semi-minor axis. Find its eccentrici…

The latus rectum of an ellipse equals its semi-minor axis. Find its eccentricity.

<details>
<summary>Answer + Reasoning</summary>

**Method: translate the condition.** LR $= \dfrac{2b^2}{a} = b$ gives $a = 2b$. Then $e^2 = 1 - \dfrac{b^2}{a^2} = 1 - \dfrac14 = \dfrac34$.


Answer: **$e = \dfrac{\sqrt3}{2}$**. (Check: $a = 2, b = 1$ is a witness ellipse: LR $= 2/2 = 1 = b$ ✓.)

</details>

#### **P5**[JEE Adv][practice][golden ellipse]The distance between the foci of an ellipse equals the length of its latus rec…

The distance between the foci of an ellipse equals the length of its latus rectum. Show that $e$ satisfies $e^2 + e - 1 = 0$ and compute it.

<details>
<summary>Answer + Reasoning</summary>

**Method: one condition, one equation in $e$.** $2c = \dfrac{2b^2}{a} \Rightarrow ca = a^2 - c^2$. Divide by $a^2$: the left side is $e$, the right side is $1 - e^2$. So $e^2 + e - 1 = 0$, giving the positive root


Answer: **$e = \dfrac{\sqrt5 - 1}{2} \approx 0.618$** — the golden ratio. (Check: $e^2 = 1 - e$, so $b^2/a^2 = 1 - e^2 = e = c/a$, i.e. $b^2 = ca = c^2/e$… cleaner: for $a=1, c = 0.618$: $2c = 1.236$ and $2b^2/a = 2(1-c^2) = 2(1-0.382) = 1.236$ ✓.)

</details>

#### **P6**[JEE Adv][practice][tilted parabola]Show that the locus of points equidistant from [formula] and the line [formula…

Show that the locus of points equidistant from $F(1,2)$ and the line $x + y = 6$ is a parabola; find its vertex and the distance from $F$ to the directrix.

<details>
<summary>Answer + Reasoning</summary>

**Method: foot of the perpendicular first.** Equality of a point-distance and a line-distance with $e = 1$ *is* the parabola definition (the focus is not on the line since $1 + 2 \ne 6$). The axis of the parabola is the perpendicular from $F$ to $\ell$: along direction $(1,1)$. Foot: $(1,2) + \tfrac{6-3}{2}(1,1) = \left(\tfrac52, \tfrac72\right)$.


The vertex is halfway between focus and directrix along the axis: $V = \tfrac12\left[(1,2) + \left(\tfrac52, \tfrac72\right)\right] = \left(\tfrac74, \tfrac{11}{4}\right)$. The focus-directrix distance is $\dfrac{|1+2-6|}{\sqrt2} = \dfrac{3}{\sqrt2}$ (this equals $2a$ in the vertex form, so the focal length is $\tfrac{3}{2\sqrt2}$).


Answer: **parabola; vertex $\left(\tfrac74, \tfrac{11}{4}\right)$; focus-directrix distance $\tfrac{3}{\sqrt2}$**. (Check: $V$ is equidistant from $F$ and $\ell$: both distances $= \tfrac{3}{2\sqrt2}$ ✓.)

</details>

#### **P7**[JEE Adv][practice][asymptote angle]Find the eccentricity of a hyperbola whose asymptotes make (i) a right angle, …

Find the eccentricity of a hyperbola whose asymptotes make (i) a right angle, (ii) an angle of $120^\circ$ around the transverse axis.

<details>
<summary>Answer + Reasoning</summary>

**Method: $\tan\alpha = b/a$ (or $\cos 2\alpha = 2/e^2 - 1$).** (i) $2\alpha = 90^\circ$: $b/a = \tan 45^\circ = 1$, so $e = \sqrt{1 + b^2/a^2} = \sqrt2$ — the rectangular hyperbola. (ii) $2\alpha = 120^\circ$: $\alpha = 60^\circ$, so $b/a = \tan 60^\circ = \sqrt3$ and $e = \sqrt{1 + 3} = 2$. Cross-check with the cosine identity: $\cos 120^\circ = -\tfrac12 = \tfrac{2}{e^2} - 1 \Rightarrow e^2 = 4$ — same answer.


Answer: (i) **$\sqrt2$**; (ii) **$2$**. Note $b \gt a$ here: a "wide-opening" hyperbola. Had the $120^\circ$ been quoted around the *conjugate* axis instead, $\alpha$ and $b/a$ invert — always ask which axis the angle opens around.

</details>

#### **P8**[Olympiad][practice][degenerate locus]Show that the focus-directrix definition with [formula] and directrix [formula…

Show that the focus-directrix definition with $e = 0$ and directrix $x = 5$ produces a single point, and explain in one sentence why the circle is nevertheless said to have eccentricity $0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: write the locus and squeeze it.** $|PF| = 0$ forces $P = F$: the locus is the single point $(0,0)$ (taking $F$ at the origin) — the degenerate ellipse. Meanwhile the family of ellipses with fixed $a$ and directrix $x = a/e$ converges, as $e \to 0$, to the circle $x^2 + y^2 = a^2$ — the directrix has run off to infinity, and a line receding to infinity stops constraining the locus.


Answer: **locus $= \{F\}$; the circle is the limit as the directrix escapes to infinity**. (Check: an ellipse with $a = 1, e = 0.001$ has $b = 0.99999\ldots$, visibly circular ✓.)

</details>




---

