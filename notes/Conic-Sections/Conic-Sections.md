---
title: "Conic Sections — Complete Notes"
aliases:
  - Conic Sections
  - Conic-Sections
module: "Conic-Sections"
type: notes
tags:
  - conic-sections
  - module
  - complete
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 📝 [[Conic-Sections — Paper|Olympiad Paper]] · ✅ [[Conic-Sections — Solutions|Solutions]]

*JEE Advanced → Olympiad Ladder*

# Conic Sections

From slicing a double cone to confocal families and the nine-point circle — one locus idea, six layers deep. Every tangent you will ever draw, every focal chord you will ever measure, derived from the focus-directrix definition rather than memorised. The parabola, the ellipse and the hyperbola are one object wearing three eccentricities.

`6 chapters · basics → JEE Advanced → Olympiad` `15 worked examples (S1–S15)` `48 practice questions (P1–P48, verified answers)` `38-question Olympiad paper + full solutions`

### ★ How to use these notes

**Read in order — do not skip the "why" boxes.** Each chapter is built in layers: *concept → first-principles reasoning → JEE theory → Olympiad extension*.

- **Colored boxes** — First Principles = the actual reasoning; Key Idea = the takeaway technique; Common Trap = the classic mistake; Olympiad Extension = the frontier version.
- **Questions are placed in context** — a solved example right after the technique that solves it, plus practice sets with difficulty tags: [JEE Main] [JEE Adv] [Olympiad]
- **The Olympiad paper at the end** (38 questions) is the exam: attempt it after Chapter 6, without solutions. The [[Conic-Sections — Solutions|solution key]] is separate and complete.

### ▣ The roadmap

The logical skeleton of the module. First principles build the three standard curves; each curve gets its own machinery chapter; the toolkit chapter unifies tangents and polars across all three; the frontier chapter harvests the Olympiad theorems.

**Diagram**

![Diagram](assets/fig-01.svg)

### ∑ Exam paper

[[Conic-Sections — Paper| The Capstone Olympiad-Level Paper — 38 Questions Eight sections (A–H) ramping JEE Main → Advanced → Olympiad: eccentricity vaults, focal-chord machinery, polars, normals, and the reflection/confocal frontier. ]] [[Conic-Sections — Solutions| Attempt first, then open Full Solutions Key Complete step-by-step solutions for all 38 questions — method name first, then the derivation, then a check. Every numeric answer verified by pure-Python computation. ]] 

### ! One-page mindset

> [!abstract] First Principles — the only rule of the game
>
> **A conic is a locus, never a picture to recall.** The parabola is "distance to a point equals distance to a line"; the ellipse is "a sum of two distances held constant"; the hyperbola is "a difference held constant" — and the focus-directrix form $|PF| = e\,|P\ell|$ generates all three with one number $e$. Every tangent, normal, chord and polar property in this module is a two-line consequence of substituting a line into that locus. When stuck, return to the definition: name the distances, write the equation, and the formula you were about to look up will fall out.

> [!warning] Common Trap — the mistakes this module punishes
>
> Five recurring own goals: (i) in the ellipse $b^2 = a^2 - c^2$ but in the hyperbola $b^2 = c^2 - a^2$ — the minus sign is the classification; (ii) the latus rectum is $2b^2/a$, the *semi*-latus rectum is $b^2/a$ — the harmonic-mean property uses the semi one; (iii) the tangent slope form $y = mx \pm \sqrt{a^2m^2 - b^2}$ for the hyperbola needs $|m| \gt b/a$, or the square root is imaginary; (iv) $S_1$ in $T = S_1$ carries its own $-1$ — dropping it moves the whole line; (v) "distance between directrices" is $2a/e$, not $a/e$. Each trap costs full marks on its question; none costs more than one habit to fix.

## Roadmap

- **Chapter 1**: Ch 1 · The Conic Family from First Principles — 5 sections · 10 questions
- **Chapter 2**: Ch 2 · The Parabola — Anatomy and Machinery — 5 sections · 11 questions
- **Chapter 3**: Ch 3 · The Ellipse — Geometry of the Squashed Circle — 7 sections · 11 questions
- **Chapter 4**: Ch 4 · The Hyperbola and Its Asymptotes — 6 sections · 11 questions
- **Chapter 5**: Ch 5 · Tangents, Normals, Chords and Polars — 6 sections · 10 questions
- **Chapter 6**: Ch 6 · The Olympiad Frontier — Reflection, Confocals and Triangles — 6 sections · 10 questions
- **Olympiad Paper**: Olympiad Paper · 38 questions — 
- **Solutions**: Olympiad Paper · Solutions & marking guide

---

## Contents

1. Chapter 1 — The Conic Family from First Principles
2. Chapter 2 — The Parabola — Anatomy and Machinery
3. Chapter 3 — The Ellipse — Geometry of the Squashed Circle
4. Chapter 4 — The Hyperbola and Its Asymptotes
5. Chapter 5 — Tangents, Normals, Chords and Polars
6. Chapter 6 — The Olympiad Frontier — Reflection, Confocals and Triangles

---

# Chapter 1 — The Conic Family from First Principles

*5 sections · 10 questions*

*Chapter 1 of 6*

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

> [!abstract] First Principles — Dandelin's spheres: why the foci are hiding in the cone
>
> For the ellipse, slide one sphere into each half of the cone so that each sphere touches the cutting plane (at points $F_1, F_2$) and rests tangent to the cone along a circle. Any straight generator line of the cone crosses both tangent circles, and the slant distance between those two circles *along the generator is the same for every generator*. Each segment of the generator is also a tangent segment from the slice point $P$ to one of the spheres, and tangent segments from $P$ to a sphere are equal — one pair ends at $F_1$, the other at $F_2$. So $|PF_1| + |PF_2|$ equals that constant slant length: the ellipse is born with its foci and its constant sum built in. The same argument with one sphere (or with the generators of the second half) produces the parabola and hyperbola versions. Nothing here is a coordinate computation — the distance definitions are *native* to the cone.

The vocabulary this fixes for the whole module: the curves are called **conic sections**, or simply **conics**; the special points and lines revealed by Dandelin's spheres are the **foci** and **directrices**; and the tilt of the slice is measured by one number — the eccentricity of §1.2.

> [!note] Note — the three degenerate conics are real exam objects
>
> A "conic" equation can collapse: a point, a single line, or a pair of lines. JEE Advanced loves asking whether a given second-degree equation represents a degenerate conic, and the answer is always decided by attempting a factorisation or by checking a discriminant. We will meet genuine examples in P8 and Q5 of the paper.

### 1.2 The focus-directrix definition and eccentricity

Fix a point $F$ (the **focus**), a line $\ell$ not through $F$ (the **directrix**), and a positive number $e$ (the **eccentricity**). The locus

$$ |PF| \;=\; e\,|P\ell| $$

is a parabola when $e = 1$, an ellipse when $0 \lt e \lt 1$, and a hyperbola when $e \gt 1$. One moving distance compared to another, with one dial to turn — that is the whole family.

> [!abstract] First Principles — deriving $y^2 = 4ax$ in three lines
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

> [!abstract] First Principles — the ellipse from a constant sum
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

> [!abstract] First Principles — the hyperbola from a constant difference
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

> [!warning] Common Trap — the minus sign is the classification
>
> In the ellipse $b^2 = a^2 - c^2$; in the hyperbola $b^2 = c^2 - a^2$. Students who reuse the ellipse relation for the hyperbola get imaginary $b$ and then "fix" it by swapping $a$ and $b$ — corrupting the latus rectum, the directrices and the asymptotes in one stroke. Decide the curve *first*, then use its relation. Also: for both central conics $c = ae$, but the ellipse has $c \lt a$ while the hyperbola has $c \gt a$ — the focus is inside the ellipse but outside the hyperbola's vertex.

#### **P1**[JEE Main][practice][parabola locus]Find the equation of the parabola with focus $(2, 0)$ and directrix $x = -2$.

Find the equation of the parabola with focus $(2, 0)$ and directrix $x = -2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: write the locus, square once.** $\sqrt{(x-2)^2 + y^2} = x + 2$ (for $x \ge -2$); squaring: $(x-2)^2 + y^2 = (x+2)^2 \Rightarrow y^2 = 8x$.

Answer: **$y^2 = 8x$**. (Check: $(2, 4)$ satisfies $y^2 = 8x$ and is equidistant from $(2,0)$ and $x=-2$: both distances $=4$ ✓.)

</details>

#### **P2**[JEE Main][practice][ellipse locus]A point moves so that its distance from $(4,0)$ is one third of its distance from the line…

A point moves so that its distance from $(4,0)$ is one third of its distance from the line $x = 36$. Identify the conic and find its equation and eccentricity.

<details>
<summary>Answer + Reasoning</summary>

**Method: read the focus-directrix data, then square.** Here $e = \tfrac13$, focus $(4,0)$, directrix $x = 36$. Since $\dfrac{a}{e} = 36$, we get $a = 12$ and $b^2 = a^2(1-e^2) = 144 \cdot \tfrac{8}{9} = 128$.

Answer: **ellipse $\dfrac{x^2}{144} + \dfrac{y^2}{128} = 1$, $e = \tfrac13$**. (Check $(12, 0)$: distance to focus $= 8$, to line $= 24 = 3 \times 8$ ✓.)

</details>

### 1.3 Worked examples — from words to equations and back

#### **S1**[JEE Adv][solved][focus-directrix to equation]A point moves so that its distance from $(2,0)$ is two thirds of its distance from the line…

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

#### **S2**[JEE Adv][solved][difference locus]A point moves so that the (absolute) difference of its distances from $(5,0)$ and $(-5,0)$…

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

> [!example] Olympiad Extension — the boundaries of the definition
>
> What happens at the edges of $|PF| = e|P\ell|$? If $\ell$ passes through $F$ and $e = 1$, squaring gives $x^2 + y^2 = x^2$: the locus is the line through $F$ parallel to $\ell$ — a *doubled* line (a degenerate parabola). If $e = 0$ with a finite directrix, $|PF| = 0$ forces the single point $F$ (a degenerate ellipse); the honest circle is the *limit* $e \to 0$ with the directrix retreating to infinity. And $e \to \infty$ with $\ell$ approaching $F$ degenerates towards a pair of lines. The non-degenerate conics are exactly the interior of this boundary — a one-parameter family in good standing.

#### **P3**[JEE Main][practice][hyperbola data]A hyperbola has foci $(\pm 10, 0)$ and eccentricity $\tfrac54$. Find its equation and the…

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

#### **P6**[JEE Adv][practice][tilted parabola]Show that the locus of points equidistant from $F(1,2)$ and the line $x + y = 6$ is a…

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

#### **P8**[Olympiad][practice][degenerate locus]Show that the focus-directrix definition with $e = 0$ and directrix $x = 5$ produces a…

Show that the focus-directrix definition with $e = 0$ and directrix $x = 5$ produces a single point, and explain in one sentence why the circle is nevertheless said to have eccentricity $0$.

<details>
<summary>Answer + Reasoning</summary>

**Method: write the locus and squeeze it.** $|PF| = 0$ forces $P = F$: the locus is the single point $(0,0)$ (taking $F$ at the origin) — the degenerate ellipse. Meanwhile the family of ellipses with fixed $a$ and directrix $x = a/e$ converges, as $e \to 0$, to the circle $x^2 + y^2 = a^2$ — the directrix has run off to infinity, and a line receding to infinity stops constraining the locus.

Answer: **locus $= \{F\}$; the circle is the limit as the directrix escapes to infinity**. (Check: an ellipse with $a = 1, e = 0.001$ has $b = 0.99999\ldots$, visibly circular ✓.)

</details>

---

---

# Chapter 2 — The Parabola — Anatomy and Machinery

*5 sections · 11 questions*

*Chapter 2 of 6*

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

> [!tip] Key Idea — the focal distance is a coordinate, not a computation
>
> Because the directrix is vertical, "distance to directrix" is literally $x + a$. Every focal-length question on a parabola is therefore a coordinate read-off. This fails for no reason except forgetting which way the parabola opens — check the sign of the $x^2$ or $y^2$ term first.

#### **P9**[JEE Main][practice][focal distance]Find the points on $y^2 = 16x$ whose focal distance is $9$.

Find the points on $y^2 = 16x$ whose focal distance is $9$.

<details>
<summary>Answer + Reasoning</summary>

**Method: focal distance $= x + a$.** Here $a = 4$, so $x + 4 = 9
        \Rightarrow x = 5$; then $y^2 = 80$, $y = \pm 4\sqrt5$.

Answer: **$\left(5, \pm 4\sqrt5\right)$**. (Check: $80 = 16 \cdot 5$ ✓.)

</details>

#### **P10**[JEE Main][practice][latus rectum]Write the ends and the length of the latus rectum of $y^2 = 8x$.

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

> [!abstract] First Principles — why focal chords are exactly $t_1 t_2 = -1$
>
> A chord passes through the focus $S(a, 0)$ iff $(t_1+t_2)\cdot 0 = 2a + 2at_1t_2$, i.e. iff $t_1 t_2 = -1$. So a focal chord with one end $P(t)$ has its other end at $P(-1/t)$. The two parts of the chord are $|SP(t)| = a(1+t^2)$ and $|SP(-1/t)| = a\left(1 + \tfrac{1}{t^2}\right)$, so the total length is 
> $$ a\left(2 + t^2 + \frac{1}{t^2}\right) = a\left(t + \frac{1}{t}\right)^2, $$
>  minimised at $t = \pm 1$ — the latus rectum, length $4a$, exactly as promised.

> [!quote] Named Property — the semi-latus rectum is the harmonic mean
>
> $\dfrac{1}{|SP(t)|} + \dfrac{1}{|SP(-1/t)|} = \dfrac{1}{a(1+t^2)} + \dfrac{t^2}{a(1+t^2)}
>       = \dfrac1a = \dfrac{2}{2a}$. So for *every* focal chord, the reciprocal sum of its two parts is constant: the semi-latus rectum $l = 2a$ is the harmonic mean of the two parts. This survives verbatim for the ellipse and hyperbola (with $l = b^2/a$) — a favourite Olympiad fact.

#### **S3**[JEE Adv][solved][focal chord]One end of a focal chord of $y^2 = 8x$ is the point with parameter $t = 2$. Find the other…

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

#### **P11**[JEE Adv][practice][focal chord]One end of a focal chord of $y^2 = 4x$ is $P(-3)$. Find the other end and the length of the…

One end of a focal chord of $y^2 = 4x$ is $P(-3)$. Find the other end and the length of the chord.

<details>
<summary>Answer + Reasoning</summary>

**Method: $t_1t_2 = -1$.** Other end $= P(\tfrac13) = \left(\tfrac19, \tfrac23\right)$. Length $= a\left(t + \tfrac1t\right)^2 = \left(-3 - \tfrac13\right)^2 = \left(-\tfrac{10}{3}\right)^2 = \tfrac{100}{9}$.

Answer: **$\left(\tfrac19, \tfrac23\right)$, length $\tfrac{100}{9}$**. (Check: chord slope $= \tfrac{2/3 + 6}{1/9 - 9} = -\tfrac34$, and it passes $(1,0)$: $-6 + \tfrac34 \cdot 8 = 0$ ✓.)

</details>

#### **P12**[JEE Adv][practice][tangent intersection]The tangents at $(4, 4)$ and $(4, -4)$ on $y^2 = 4x$ meet at $T$. Show that $T$ lies on the…

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

> [!abstract] First Principles — normals from a point: a cubic, hence three
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

#### **S4**[JEE Adv][solved][normal cubic]Find all the normals drawn from $(6, 0)$ to the parabola $y^2 = 4x$, with their feet.

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

#### **P13**[JEE Adv][practice][midpoint chord]The chord-with-midpoint formula $T = S_1$ (Chapter 5) applied to $y^2 = 4x$ with "midpoint"…

The chord-with-midpoint formula $T = S_1$ (Chapter 5) applied to $y^2 = 4x$ with "midpoint" $\left(\tfrac94, 3\right)$ produces a single line. Show that this line is the tangent at that point, and explain why.

<details>
<summary>Answer + Reasoning</summary>

**Method: notice the midpoint lies on the curve.** $\left(\tfrac94\right)\cdot 4 = 9 = 3^2$ — the point is on the parabola (it is $P(\tfrac32)$). A "chord" bisected at a point of the curve must have both ends coalescing there: the chord degenerates to the tangent.

Compute: $T = S_1$ reads $yy_1 - 2(x + x_1) = y_1^2 - 4x_1$, i.e. $3y - 2x - \tfrac92 = 9 - 9 = 0$, so $3y = 2x + \tfrac92$. Compare the tangent at $t = \tfrac32$: $ty = x + at^2 \Rightarrow \tfrac32 y = x + \tfrac94$, i.e. $3y = 2x + \tfrac92$ — identical.

Answer: **the formula returns the tangent $3y = 2x + \tfrac92$**, because a chord bisected on the curve is a doubled point ✓.

</details>

#### **P14**[JEE Main][practice][subnormal]For $y^2 = 8x$, write the normal at the point with $t = 1$, find where it meets the axis…

For $y^2 = 8x$, write the normal at the point with $t = 1$, find where it meets the axis, and verify that the subnormal equals $2a$.

<details>
<summary>Answer + Reasoning</summary>

**Method: plug into $y = -tx + 2at + at^3$.** With $a = 2, t = 1$: $y = -x + 4 + 2 = -x + 6$. It meets the axis at $N(6, 0)$.

The foot of $P(2, 4)$ on the axis is $M(2, 0)$; the subnormal is $|NG| = 6 - 2 = 4 = 2a$ ✓.

Answer: **normal $y = -x + 6$, meets axis at $(6,0)$, subnormal $4 = 2a$**.

</details>

### 2.4 Reflection — the parabola as a focusing machine

Headlights and satellite dishes are parabolic for one reason: rays parallel to the axis reflect through the focus. The proof is a picture with two equal lengths.

> [!example] Olympiad Extension — reflection from the isosceles triangle $SPN$
>
> Let the normal at $P(t)$ meet the axis at $N$ and let $S$ be the focus. From §2.3, $N = (at^2 + 2a, 0)$, so $|SN| = |at^2 + 2a - a| = a(1 + t^2)$. But the focal distance is $|SP| = a(1 + t^2)$ too. Hence $SP = SN$: triangle $SPN$ is **isosceles**, so the normal makes equal angles with $SP$ and with the axis. A ray travelling along the axis direction hits the tangent at $P$; the normal is the angle bisector between the reflected ray and the axis direction — the reflected ray must be the mirror image, i.e. it passes through $S$. Conversely (optics is reversible) rays emitted from $S$ leave parallel to the axis: the headlight principle.

#### **S5**[Olympiad][solved][reflection verified]A laser travelling parallel to the $x$-axis (in the $-x$ direction) strikes $y^2 = 4x$ at…

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

#### **P15**[Olympiad][practice][foot on vertex tangent]Prove that the foot of the perpendicular from the focus of $y^2 = 4ax$ to any tangent lies…

Prove that the foot of the perpendicular from the focus of $y^2 = 4ax$ to any tangent lies on the tangent at the vertex, and compute that foot for the tangent at $t = 3$ when $a = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: foot-of-perpendicular formula.** Tangent at $t$: $x - ty + at^2 = 0$. The foot from $S(a, 0)$:

$$ \left(a - \frac{a + at^2}{1 + t^2},\ 0 + \frac{t(a+at^2)}{1+t^2}\right) = (0,\ at). $$

Its $x$-coordinate is $0$ for every $t$ — the foot rides up and down the line $x = 0$, the tangent at the vertex.

Answer: **foot $= (0, at)$; for $a = 1, t = 3$: $(0, 3)$**. (Check: $(0,3)$ on $x = 0$ and $3y = x + 9$ passes it: $9 = 9$ ✓.)

</details>

#### **P16**[Olympiad][practice][perpendicular tangents]Show that the tangents at $t = 1$ and $t = -1$ on $y^2 = 4x$ are perpendicular, and that…

Show that the tangents at $t = 1$ and $t = -1$ on $y^2 = 4x$ are perpendicular, and that they meet on the directrix. Which general facts are these instances of?

<details>
<summary>Answer + Reasoning</summary>

**Method: compute both lines.** $t = 1$: $y = x + 1$ (slope $1$); $t = -1$: $-y = x + 1$, i.e. $y = -x - 1$ (slope $-1$). Product of slopes $-1$: perpendicular. Intersection: $x + 1 = -x - 1 \Rightarrow x = -1, y = 0$: the point $(-1, 0)$ lies on the directrix $x = -1$.

Answer: **perpendicular, meeting at $(-1, 0)$**. General facts: tangents at $t_1, t_2$ are perpendicular exactly when $t_1t_2 = -1$, and their intersection $\left(at_1t_2,\ a(t_1+t_2)\right)$ then sits at $(-a, 0)$ — on the directrix. The locus of intersection of perpendicular tangents to a parabola is its directrix (the "director circle" degenerates to a line), and the tangents at the ends of any focal chord ($t_1t_2 = -1$) are exactly such a pair ✓.

</details>

---

---

# Chapter 3 — The Ellipse — Geometry of the Squashed Circle

*7 sections · 11 questions*

*Chapter 3 of 6*

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

#### **S6**[JEE Main][solved][applied ellipse]An arch is a semi-ellipse with a $20$ m span and maximum height $5$ m. A truck $4$ m wide…

An arch is a semi-ellipse with a $20$ m span and maximum height $5$ m. A truck $4$ m wide, centred on the axis, is $4.8$ m tall. Does it clear the arch at a point $2$ m from the centre?

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Method: model, substitute, compare.** The full ellipse has $2a = 20$, $b = 5$: $\dfrac{x^2}{100} + \dfrac{y^2}{25} = 1$. At $x = 2$: $y = 5\sqrt{1 - \tfrac{4}{100}} = 5\sqrt{0.96} \approx 4.899$ m.

Since $4.899 \gt 4.8$, the truck clears by about $10$ cm.

Total: **Answer: clears (height available $\approx 4.899$ m)**

**Check:** at $x = 0$ the height is $5$ m and the ellipse decreases away from the centre — $4.899 \lt 5$ is consistent ✓. Note the margin is thin: an off-centre load flips the answer, which is exactly how these questions are graded.

</details>

#### **P17**[JEE Main][practice][anatomy]For $\dfrac{x^2}{36} + \dfrac{y^2}{16} = 1$, find $e$, the foci, and the latus rectum.

For $\dfrac{x^2}{36} + \dfrac{y^2}{16} = 1$, find $e$, the foci, and the latus rectum.

<details>
<summary>Answer + Reasoning</summary>

**Method: $e^2 = 1 - b^2/a^2$.** $e = \sqrt{1 - \tfrac{16}{36}} = \dfrac{\sqrt5}{3}$; $c = ae = 6\cdot\tfrac{\sqrt5}{3} = 2\sqrt5$; LR $= \dfrac{2b^2}{a} = \dfrac{32}{6} = \dfrac{16}{3}$.

Answer: **$e = \tfrac{\sqrt5}{3}$, foci $(\pm 2\sqrt5, 0)$, LR $\tfrac{16}{3}$**. (Check: $c^2 = a^2 - b^2 = 20$ ✓.)

</details>

#### **P18**[JEE Main][practice][reconstruct]Find the ellipse centred at the origin with foci $(\pm 2, 0)$ that passes through $(2, 3)$…

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

#### **P23**[JEE Main][practice][eccentric angle]Find the eccentric angle of the point $\left(2\sqrt2, \tfrac{3}{\sqrt2}\right)$ on…

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

#### **S7**[JEE Adv][solved][tangent + normal]Find the tangent and normal to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ at the point with…

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

#### **P19**[JEE Adv][practice][slope form]Find the tangents of slope $2$ to $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$.

Find the tangents of slope $2$ to $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $y = mx \pm \sqrt{a^2m^2 + b^2}$.** $y = 2x \pm \sqrt{9\cdot4 + 4} = 2x \pm \sqrt{40} = 2x \pm 2\sqrt{10}$.

Answer: **$y = 2x \pm 2\sqrt{10}$**. (Check: substituting $y = 2x + 2\sqrt{10}$ into the ellipse gives $40x^2 + 72\sqrt{10}\,x + 324 = 0$ scaled — discriminant $(72\sqrt{10})^2 - 4\cdot40\cdot324 = 0$ ✓.)

</details>

#### **P20**[JEE Adv][practice][normal by slope]Find the points on $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ at which the normal has slope $2$.

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

#### **P21**[JEE Adv][practice][focal distances + chord]For $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$ and the point $P$ with eccentric angle…

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

#### **S8**[JEE Adv][solved][director circle]Verify the director circle of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ using the tangents of…

Verify the director circle of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ using the tangents of slopes $1$ and $-1$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Method: write the four tangents, intersect, check the circle.** Slope $1$: $y = x \pm \sqrt{25} = x \pm 5$. Slope $-1$: $y = -x \pm 5$. Each line is genuinely tangent: substituting $y = x + 5$ into the ellipse gives $25x^2 + 160x + 256 = 0 = (5x+16)^2$ — a double root ✓ (and similarly for the others).

The four pairwise intersections are $(0, 5), (0, -5), (5, 0), (-5, 0)$, and all satisfy $x^2 + y^2 = 25 = a^2 + b^2$.

Total: **Answer: director circle $x^2 + y^2 = 25$ verified**

**Check:** $(\pm 5, 0)$ and $(0, \pm 5)$ all at distance $5 = \sqrt{16 + 9}$ from the origin ✓.

</details>

#### **P22**[JEE Main][practice][position test]Classify the points $(1, 1)$, $(1, 2)$, $(3, 1)$ with respect to…

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

#### **P24**[Olympiad][practice][angle equality]For $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$…

For $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, $P = \left(\tfrac52, \tfrac{3\sqrt3}{2}\right)$: compute the angles the tangent at $P$ makes with $PF_1$ and $PF_2$ and confirm they are equal.

<details>
<summary>Answer + Reasoning</summary>

**Method: three slopes, two angles.** Tangent slope at $P$: $-\dfrac{b^2x}{a^2y} = -\dfrac{9\cdot 5/2}{25\cdot 3\sqrt3/2} = -\dfrac{45}{75\sqrt3} = -\dfrac{\sqrt3}{5}$, angle $\approx -19.11^\circ$. Ray directions: to $F_2(4,0)$: $-60.00^\circ$; to $F_1(-4,0)$: $-158.21^\circ$.

Angles with the tangent: $\left|-60 + 19.11\right| = 40.89^\circ$ and $\left|-158.21 + 19.11\right| = 139.10^\circ$, whose supplement is $40.90^\circ$ — equal within rounding.

Answer: **both angles $\approx 40.89^\circ$** — the tangent is the external bisector, and a ray from $F_1$ through $P$ reflects to $F_2$ ✓.

</details>

---

---

# Chapter 4 — The Hyperbola and Its Asymptotes

*6 sections · 11 questions*

*Chapter 4 of 6*

The hyperbola is the ellipse with one sign flipped — and that flip changes everything: the foci move outside the curve, a second conjugate curve appears, and the curve grows two straight *asymptotes* that every JEE question eventually touches. The rotated member of the family, $xy = c^2$, is the quiet star of Olympiad geometry: Chapter 6 will ride it through the orthocentre of a triangle.

### 4.0 What you will be able to do

- Read the anatomy of $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ — including why $b^2 = c^2 - a^2$ and why the foci are *outside* the vertices.
- Handle the conjugate hyperbola and the identity $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$.
- Derive the asymptotes, connect their angle to $e$, and detect "line parallel to an asymptote" pathologies.
- Work the rotated rectangular hyperbola $xy = c^2$: parametric point, tangent, normal.

### 4.1 Anatomy of the hyperbola

For $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$: vertices $(\pm a, 0)$; foci $(\pm ae, 0)$ with $c = ae = \sqrt{a^2 + b^2}$; eccentricity $e = \sqrt{1 + \dfrac{b^2}{a^2}} \gt 1$; directrices $x = \pm \dfrac{a}{e}$ (now *between* the centre and the vertices, since $a/e \lt a$); latus rectum ends $\left(\pm ae, \pm \dfrac{b^2}{a}\right)$, length $\dfrac{2b^2}{a}$.

> [!abstract] First Principles — focal distances on the right branch
>
> For $P(x, y)$ on the right branch ($x \ge a$), the focus-directrix definition with directrix $x = a/e$ gives $|PF_{\text{right}}| = e\left(x - \dfrac{a}{e}\right) = ex - a$, and by the difference definition $|PF_{\text{left}}| = ex + a$ — difference $2a$ exactly. Sanity at the vertex $x = a$: distances $a(1-e)$·… concretely $ea - a = c - a$ to the near focus and $c + a$ to the far one, and $(c+a) - (c-a) = 2a$ ✓. On the left branch the signs mirror. The absolute-value rule $\big||PF_1| - |PF_2|\big| = 2a$ is what "difference of distances" means — a fixed sign would trace one branch only.

#### **S9**[JEE Main][solved][full anatomy]Read off everything for $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$: eccentricity, foci, latus…

Read off everything for $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$: eccentricity, foci, latus rectum, asymptotes, directrices.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Name the move first:** the $3\text{-}4\text{-}5$ hyperbola. Here $a = 3, b = 4$, so $c = \sqrt{9 + 16} = 5$.

- $e = c/a = \tfrac53$; foci $(\pm 5, 0)$.
- LR $= \dfrac{2b^2}{a} = \dfrac{32}{3}$, ends $\left(\pm 5, \pm \tfrac{16}{3}\right)$.
- Asymptotes $y = \pm \dfrac{b}{a}x = \pm \dfrac{4x}{3}$.
- Directrices $x = \pm \dfrac{a}{e} = \pm \dfrac{9}{5}$ — inside the vertices, as promised ($9/5 \lt 3$).

Total: **Answer: $e = \tfrac53$, foci $(\pm5,0)$, LR $\tfrac{32}{3}$, asymptotes $y=\pm\tfrac43x$, $x=\pm\tfrac95$**

**Check:** $b^2 = c^2 - a^2 = 25 - 9 = 16$ ✓; the point $(5, \tfrac{16}{3})$ satisfies $\tfrac{25}{9} - \tfrac{256/9}{16} = \tfrac{25 - 16}{9} = 1$ ✓.

</details>

#### **P25**[JEE Main][practice][standardise]For $4x^2 - 9y^2 = 36$, find the eccentricity, the foci and the latus rectum.

For $4x^2 - 9y^2 = 36$, find the eccentricity, the foci and the latus rectum.

<details>
<summary>Answer + Reasoning</summary>

**Method: divide by 36 first.** $\dfrac{x^2}{9} - \dfrac{y^2}{4} = 1$: $a = 3, b = 2$, $c = \sqrt{13}$.

Answer: **$e = \tfrac{\sqrt{13}}{3}$, foci $(\pm\sqrt{13}, 0)$, LR $\tfrac{2\cdot4}{3} = \tfrac83$**. (Check: $e^2 = 1 + \tfrac49 = \tfrac{13}{9}$ ✓.)

</details>

### 4.2 The conjugate hyperbola

Swap the roles of the axes: $\dfrac{y^2}{b^2} - \dfrac{x^2}{a^2} = 1$ is the **conjugate hyperbola** — same $a, b$, but transverse axis now vertical, foci on the $y$-axis at $(0, \pm e'b)$ where $e' = \sqrt{1 + \dfrac{a^2}{b^2}}$ (the focal distance $c$ is shared: $c^2 = a^2 + b^2$).

> [!quote] Named Identity — $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$
>
> $\dfrac{1}{e^2} = \dfrac{a^2}{a^2+b^2}$ and $\dfrac{1}{e'^2} = \dfrac{b^2}{a^2+b^2}$; the sum is $1$. Two hyperbolas sharing asymptote directions can never both be eccentricity $\sqrt2$ — the rectangularity budget is shared. JEE asks this identity almost verbatim.

#### **S11**[JEE Adv][solved][conjugate + identity]For the hyperbola with $a = 3, b = 4$, compute $e$ and the conjugate's $e'$, and verify…

For the hyperbola with $a = 3, b = 4$, compute $e$ and the conjugate's $e'$, and verify $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Method: same $c$, two denominators.** $c = 5$: $e = \tfrac53$ (transverse $a = 3$), $e' = \tfrac{c}{b} = \tfrac54$ (transverse $b = 4$).

$\dfrac{1}{e^2} + \dfrac{1}{e'^2} = \dfrac{9}{25} + \dfrac{16}{25} = 1$ ✓.

Total: **Answer: $e = \tfrac53$, $e' = \tfrac54$, identity holds**

**Check:** $e, e' \gt 1$ both, and neither equals $\sqrt2$: a hyperbola and its conjugate cannot both be rectangular ✓.

</details>

#### **P29**[JEE Main][practice][position test]Classify $(6, 4)$, $(-6, 4)$, $(1, 0)$ with respect to…

Classify $(6, 4)$, $(-6, 4)$, $(1, 0)$ with respect to $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: evaluate $S_1$, then interpret the sign.** $(6,4)$: $\tfrac{36}{4} - \tfrac{16}{9} - 1 = 9 - \tfrac{25}{9} = \tfrac{56}{9} \gt 0$: in the "right branch" region (same sign as $(a, 0)$). $(-6,4)$: same value $\gt 0$, but left of the $y$-axis: left-branch region. $(1,0)$: $\tfrac14 - 1 \lt 0$: between the branches (the region containing the conjugate hyperbola).

Answer: **$(6,4)$ right-branch side, $(-6,4)$ left-branch side, $(1,0)$ between the branches**. (Unlike the ellipse, "outside" is not one region — the sign of $S_1$ says which wedge you inhabit, and the $x$-coordinate says which wedge ✓.)

</details>

### 4.3 Asymptotes — the straight skeleton

Factor the defining equation: $\left(\dfrac{x}{a} - \dfrac{y}{b}\right)\left(\dfrac{x}{a} +
    \dfrac{y}{b}\right) = 1$. Far from the origin the right side becomes negligible compared to the growing factors, so the curve hugs the lines where one factor vanishes:

$$ y = \frac{b}{a}x \qquad \text{and} \qquad y = -\frac{b}{a}x $$

Three consequences worth their weight:

- The **angle** $2\alpha$ between the asymptotes (measured around the transverse axis) has $\tan\alpha = \dfrac ba$, and combining with $e^2 = \dfrac{a^2+b^2}{a^2}$ gives the identity $\cos 2\alpha = \dfrac{2}{e^2} - 1$. Rectangular hyperbola ($2\alpha = 90^\circ$) $\Leftrightarrow a = b \Leftrightarrow e = \sqrt2$.
- Conjugate hyperbola: same asymptotes. The pair of asymptotes $y^2 = \dfrac{b^2}{a^2}x^2$ is itself a degenerate conic — the hyperbola "squared".
- A line **parallel to an asymptote** meets the hyperbola in exactly one finite point (the second intersection has escaped to infinity). Exam questions hide this as "show the line meets the curve in exactly one point".

> [!warning] Common Trap — points on an asymptote determine nothing
>
> Asking for the hyperbola $x^2/a^2 - y^2/b^2 = 1$ with given $e$ that "passes through" a point on $y = \pm\frac{b}{a}x$ is a trick: the answer is *no such hyperbola*. The curve and its asymptote never meet; a point on the asymptote is a witness of impossibility. Always test the point against $y = \frac{b}{a}x$ before solving.

#### **P26**[JEE Main][practice][asymptotes]What are the asymptotes of $xy = 6$? And find the angle between the asymptotes of…

What are the asymptotes of $xy = 6$? And find the angle between the asymptotes of $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: read the axes; then $\tan\alpha = b/a$.** $xy = 6$ never touches $x = 0$ or $y = 0$ and approaches both: its asymptotes are the coordinate axes. For the second: $\tan\alpha = \tfrac34$, angle $2\alpha = 2\arctan(0.75) \approx 73.74^\circ$.

Answer: **axes; $73.74^\circ$** around the transverse axis. (Check via the identity: $e^2 = 1 + \tfrac{9}{16} = \tfrac{25}{16}$, $\cos 2\alpha = \tfrac{2}{25/16} - 1 = \tfrac{32}{25} - 1 = \tfrac{7}{25}$, and $2\arctan(3/4)$ has cosine $\tfrac{1 - 9/16}{1 + 9/16} = \tfrac{7}{25}$ ✓.)

</details>

#### **P27**[JEE Adv][practice][reconstruct + trap](i) Explain why no hyperbola $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ with $e = \tfrac54$…

(i) Explain why no hyperbola $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ with $e = \tfrac54$ passes through $(4, 3)$. (ii) Find the one passing through $\left(4, \tfrac32\right)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: check the asymptote first.** (i) With $e = \tfrac54$: $b^2 = a^2(e^2 - 1) = \tfrac{9}{16}a^2$, so the asymptote is $y = \tfrac34 x$ — and $(4,3)$ lies exactly on it. The curve never meets its asymptote: no solution exists.

(ii) Plug $\left(4, \tfrac32\right)$: $\dfrac{16}{a^2} - \dfrac{9/4}{9a^2/16} =
        \dfrac{16}{a^2} - \dfrac{4}{a^2} = \dfrac{12}{a^2} = 1$, so $a^2 = 12$, $b^2 = \tfrac{27}{4}$.

Answer: **(i) impossible — $(4,3)$ is on the asymptote $y = \tfrac34x$; (ii) $\dfrac{x^2}{12} - \dfrac{4y^2}{27} = 1$**. (Check: $\tfrac{16}{12} - \tfrac{(9/4)\cdot 4}{27} = \tfrac43 - \tfrac13 = 1$ ✓.)

</details>

#### **P28**[JEE Adv][practice][midpoint chord]Find the chord of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ bisected at $(3, -2)$, and verify…

Find the chord of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ bisected at $(3, -2)$, and verify the midpoint by Vieta. (The formula $T = S_1$, previewed in P13 of Chapter 2, is proved in general in Chapter 5.)

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = S_1$, with $S_1$ carrying its $-1$.** $S_1 = \tfrac94 - \tfrac49 - 1 = -\tfrac{31}{36}$. $T = S_1$ reads $\dfrac{3x}{4} - \dfrac{(-2)y}{9} - 1 = -\tfrac{31}{36}$, so $\dfrac{3x}{4} + \dfrac{2y}{9} = 1 - \tfrac{31}{36} = \dfrac{5}{36}$, i.e.

$$ 27x + 8y = 65. $$

Slope sanity: $-\tfrac{27}{8} = +\tfrac{b^2x_1}{a^2y_1} = \tfrac{9\cdot3}{4\cdot(-2)}$ ✓ (hyperbola sign, Chapter 5).

**Vieta:** substituting $y = \tfrac{65 - 27x}{8}$ into the hyperbola gives $-585x^2 + 3510x - 4801 = 0$; sum of roots $= \tfrac{3510}{585} = 6$, midpoint $x = 3$ ✓ (midpoint $y = -2$ follows from the line).

Answer: **$27x + 8y = 65$**.

</details>

#### **P31**[JEE Adv][practice][parallel to asymptote]Show that the line $y = \tfrac32 x + 1$ meets $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ in…

Show that the line $y = \tfrac32 x + 1$ meets $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ in exactly one finite point, and find it.

<details>
<summary>Answer + Reasoning</summary>

**Method: substitute; watch the quadratic collapse.** The line is parallel to the asymptote $y = \tfrac32 x$. Substituting: $\dfrac{x^2}{4} - \dfrac{(3x/2 + 1)^2}{9} = 1 \Rightarrow \dfrac{x^2}{4} - \dfrac{x^2}{4} - \dfrac{x}{3} - \dfrac19 = 1
        \Rightarrow -\dfrac{x}{3} = \dfrac{10}{9}$: linear! One root: $x = -\tfrac{10}{3}$, $y = \tfrac32(-\tfrac{10}{3}) + 1 = -4$.

Answer: **exactly one point $\left(-\tfrac{10}{3}, -4\right)$**; the second intersection is at infinity along the asymptote direction. (Check: $\tfrac{100/9}{4} - \tfrac{16}{9} = \tfrac{25}{9} - \tfrac{16}{9} = 1$ ✓.)

</details>

### 4.4 Tangent, normal, director circle

$$ \frac{xx_1}{a^2} - \frac{yy_1}{b^2} = 1 \qquad
         \frac{x\sec\theta}{a} - \frac{y\tan\theta}{b} = 1 \qquad
         y = mx \pm \sqrt{a^2m^2 - b^2},\ \ |m| \gt \frac ba $$

$$ ax\sin\theta + by = (a^2 + b^2)\tan\theta \qquad
         y = mx - \frac{(a^2+b^2)\,m}{\sqrt{a^2 - b^2m^2}},\ \ |m| \lt \frac ab $$

Notice the mirror-image restrictions: tangent slopes must be *steeper* than the asymptote ($|m| \gt b/a$), normal slopes *shallower* than the reciprocal asymptote ($|m| \lt a/b$). A line of slope $m$ with $|m| \le b/a$ can never be tangent.

> [!quote] Named Result — the director circle can vanish
>
> The same perpendicular-tangents computation as the ellipse (Chapter 3) now yields $x^2 + y^2 = a^2 - b^2$. If $a \gt b$ this is a real circle; if $a = b$ (rectangular hyperbola) it collapses to the single point $(0,0)$ — and since no real tangent pair passes through the origin except the asymptotes themselves, **a rectangular hyperbola has no pair of real perpendicular tangents**. Verified end-to-end in Q23 of the paper.

#### **P32**[JEE Adv][practice][director circle]Find the locus of intersection of perpendicular tangents to…

Find the locus of intersection of perpendicular tangents to $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, and state what happens for the rectangular hyperbola $x^2 - y^2 = a^2$.

<details>
<summary>Answer + Reasoning</summary>

**Method: $x^2 + y^2 = a^2 - b^2$.** Here $a^2 - b^2 = 7$: the circle $x^2 + y^2 = 7$. For $a = b$: $x^2 + y^2 = 0$ — a point-circle; tangents of slopes $m$ and $-\tfrac1m$ would both need $c^2 = a^2m^2 - a^2 \ge 0$ (so $|m| \ge 1$) and $|1/m| \ge 1$ (so $|m| \le 1$): forced $|m| = 1$, $c = 0$, i.e. the lines $y = \pm x$ — the asymptotes, which are not tangents.

Answer: **$x^2 + y^2 = 7$; for the rectangular hyperbola no real perpendicular tangent pair exists** ✓.

</details>

### 4.5 The rectangular hyperbola $xy = c^2$

Rotate $x^2 - y^2 = 2c^2$ by $45^\circ$ (swap to $x = \tfrac{X - Y}{\sqrt2}$, $y = \tfrac{X + Y}{\sqrt2}$) and the equation becomes $xy = c^2$: asymptotes are the coordinate axes, centre the origin, $e = \sqrt2$. Its parametric point mirrors Chapter 2's beautifully:

$$ P(t) = \left(ct, \frac{c}{t}\right), \qquad
         \text{tangent: } \frac{x}{t} + ty = 2c, \qquad
         \text{normal: } y = t^2x - ct^3 + \frac{c}{t} $$

The tangent's slope is $-\tfrac{1}{t^2}$ — always negative — and the tangent at $t$ meets the tangent at $-t$ on the $y$-axis: small facts that unlock big problems.

#### **S10**[JEE Adv][solved][tangent + normal]For $xy = 4$, find the tangent and normal at $t = 2$, and verify perpendicularity.

For $xy = 4$, find the tangent and normal at $t = 2$, and verify perpendicularity.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Name the move first:** point $(ct, c/t) = (4, 1)$ with $c = 2$; then the two formulas.

Tangent: $\dfrac{x}{2} + 2y = 4$, i.e. $x + 4y = 8$ (slope $-\tfrac14$). Normal: $y = 4x - 16 + 1 = 4x - 15$ (slope $4$). Product of slopes: $-1$ ✓.

Total: **Answer: tangent $x + 4y = 8$; normal $y = 4x - 15$**

**Check:** both pass $(4,1)$: $4 + 4 = 8$ ✓; $16 - 15 = 1$ ✓; and implicit differentiation of $y = \tfrac4x$: $y'(4) = -\tfrac{4}{16} = -\tfrac14$ ✓.

</details>

#### **P30**[JEE Main][practice][tangent + normal]Find the tangent and normal to $xy = 9$ at $t = 1$.

Find the tangent and normal to $xy = 9$ at $t = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: same recipe.** Point $(3, 3)$. Tangent: $x + y = 6$; normal: $y = t^2x - ct^3 + \tfrac{c}{t} = x - 3 + 3 = x$.

Answer: **tangent $x + y = 6$ (slope $-1$); normal $y = x$ (slope $1$)**. (Check: $3 + 3 = 6$ ✓; $y=x$ passes $(3,3)$ and is perpendicular to the tangent ✓.)

</details>

---

---

# Chapter 5 — Tangents, Normals, Chords and Polars

*6 sections · 10 questions*

*Chapter 5 of 6*

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

#### **P33**[JEE Main][practice][slope form]Find the tangent of slope $-1$ to $y^2 = 4x$.

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

#### **P34**[JEE Adv][practice][pair of tangents]Find the joint equation of the pair of tangents from $(-2, 5)$ to $y^2 = 4x$, and check…

Find the joint equation of the pair of tangents from $(-2, 5)$ to $y^2 = 4x$, and check that each member really is tangent.

<details>
<summary>Answer + Reasoning</summary>

**Method: $SS_1 = T^2$.** $S = y^2 - 4x$, $S_1 = 25 + 8 = 33$, $T = 5y - 2(x - 2) = 5y - 2x + 4$. So $33(y^2 - 4x) = (5y - 2x + 4)^2$, which expands and simplifies to

$$ x^2 - 5xy - 2y^2 + 29x + 10y + 4 = 0. $$

Tangency check: the lines through $(-2,5)$ of slope $m$ are tangent to $y^2=4x$ iff $m^2 - 3m + 1 = 0$ (from the discriminant of $my^2 - 4y + 12 - 4m$), i.e. $m = \tfrac{3 \pm \sqrt5}{2}$ — two real slopes, matching the two factors.

Answer: **$x^2 - 5xy - 2y^2 + 29x + 10y + 4 = 0$**. (Check: vanishes at $(-2,5)$: $4 + 50 - 50 - 58 + 50 + 4 = 0$ ✓; discriminant identity verified at $m = \tfrac{3+\sqrt5}{2}$: $16 - 4m(12 - 4m) = 0$ ✓.)

</details>

#### **P35**[JEE Adv][practice][chord of contact]Find the chord of contact from $(4, 2)$ to $\dfrac{x^2}{16} + \dfrac{y^2}{4} = 1$, its…

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

#### **S12**[JEE Adv][solved][midpoint chord]Find the chord of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ bisected at $(5, 3)$, and verify…

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

#### **S13**[Olympiad][solved][La Hire in action]Show that the polar of $(4, 3)$ w.r.t. $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ is…

Show that the polar of $(4, 3)$ w.r.t. $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ is $\dfrac{x}{4} + \dfrac{y}{3} = 1$, and verify La Hire's theorem along it.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Name the move first:** $T = 0$ with $(x_1, y_1) = (4, 3)$: $\dfrac{4x}{16} + \dfrac{3y}{9} = 1$, i.e. $\dfrac{x}{4} + \dfrac{y}{3} = 1$.

**La Hire along the line:** take any $(u, v)$ on the polar, e.g. $(4, 0)$, $(0, 3)$, $\left(2, \tfrac32\right)$. The polar of $(u, v)$ is $\dfrac{ux}{16} + \dfrac{vy}{9} = 1$; evaluate at $(4, 3)$: $\dfrac{4u}{16} + \dfrac{3v}{9} = \dfrac{u}{4} + \dfrac{v}{3} = 1$ — true because $(u,v)$ is on the polar of $(4,3)$. So every polar of every point of the line passes through $(4, 3)$: the whole pencil of lines through $(4,3)$ is the mirror image of the line's points.

Total: **Answer: polar $\tfrac{x}{4} + \tfrac{y}{3} = 1$; La Hire verified**

**Check:** $S_1 = \tfrac{16}{16} + \tfrac{9}{9} - 1 = 1 \gt 0$: $(4,3)$ is outside the ellipse, so its polar is a genuine chord of contact ✓.

</details>

#### **P36**[JEE Adv][practice][pole of a line]Find the pole of the line $x = 8$ with respect to $y^2 = 4x$.

Find the pole of the line $x = 8$ with respect to $y^2 = 4x$.

<details>
<summary>Answer + Reasoning</summary>

**Method: match $T = 0$ to the line.** Polar of $(x_1, y_1)$: $yy_1 = 2(x + x_1)$. To be the vertical line $x = 8$ we need $y_1 = 0$ and $2(x + x_1) \propto x - 8$: $2x + 2x_1 = k(x - 8)$ gives $k = 2$, $x_1 = -8$.

Answer: **pole $= (-8, 0)$**. (Check: its polar is $0\cdot y = 2(x - 8)$, i.e. $x = 8$ ✓.)

</details>

#### **P37**[JEE Adv][practice][polar + La Hire]Find the polar of $(2, 3)$ with respect to $\dfrac{x^2}{9} - \dfrac{y^2}{4} = 1$, and…

Find the polar of $(2, 3)$ with respect to $\dfrac{x^2}{9} - \dfrac{y^2}{4} = 1$, and verify La Hire's theorem for three points on it.

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = 0$, sign convention honoured.** $\dfrac{2x}{9} - \dfrac{3y}{4} = 1$, i.e. $8x - 27y = 36$.

La Hire: points on it include $\left(\tfrac92, 0\right)$, $\left(0, -\tfrac43\right)$, $\left(\tfrac94, -\tfrac23\right)$. The polar of $(u,v)$ is $\dfrac{ux}{9} - \dfrac{vy}{4} = 1$; at $(2,3)$ it gives $\dfrac{2u}{9} - \dfrac{3v}{4} = 1$ — true for all three points, i.e. all their polars pass through $(2,3)$ ✓.

Answer: **$8x - 27y = 36$**, with the reciprocity checked ✓.

</details>

#### **P40**[Olympiad][practice][pole of tangent]Find the pole of $x + 4y = 8$ with respect to $xy = 4$, and interpret the answer.

Find the pole of $x + 4y = 8$ with respect to $xy = 4$, and interpret the answer.

<details>
<summary>Answer + Reasoning</summary>

**Method: match the polar form.** Polar of $(x_1, y_1)$ w.r.t. $xy = c^2$: $\dfrac{xy_1 + x_1y}{2} = c^2$, i.e. $xy_1 + x_1y = 8$. Matching $y_1 : x_1 = 1 : 4$ and the constant: $x_1 = 4k, y_1 = k$, $8k = 8$, $k = 1$: pole $= (4, 1)$.

Interpretation: $x + 4y = 8$ is the tangent at $t = 2$ (contact $(4,1)$, Chapter 4's S10) — and the pole of a tangent is its contact point.

Answer: **pole $= (4, 1)$, the point of contact**. (Check: polar of $(4,1)$: $x + 4y = 8$ ✓.)

</details>

### 5.5 How many normals? And the three director loci

**Normals from a point.** For the parabola, the normal cubic (Chapter 2) gives at most three. For the ellipse, eliminating the parameter produces a quartic in general position — **four normals** can be drawn from a general point (a theorem of Apollonius; the four feet lie on a rectangular hyperbola through the centre and the two foci, a lovely fact we will not prove here). The hyperbola similarly admits four. What the exam tests is the *mechanism*: substitute the normal's equation into the point and count real roots.

#### **P39**[JEE Adv][practice][normal through centre]Show that a normal to $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ passes through the centre iff…

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

#### **P38**[JEE Main][practice][director circle]Find the director circle of $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ and verify it with the…

Find the director circle of $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ and verify it with the horizontal/vertical tangent pair.

<details>
<summary>Answer + Reasoning</summary>

**Method: $x^2 + y^2 = a^2 + b^2$.** $x^2 + y^2 = 41$. The tangents $y = \pm 4$ and $x = \pm 5$ are perpendicular pairs meeting at $(\pm 5, \pm 4)$, and $25 + 16 = 41$ ✓.

Answer: **$x^2 + y^2 = 41$**.

</details>

---

---

# Chapter 6 — The Olympiad Frontier — Reflection, Confocals and Triangles

*6 sections · 10 questions*

*Chapter 6 of 6*

Olympiad conic problems are rarely "find the equation" problems. They are geometry problems in which a conic appears as a *machine for an angle or a distance*: a mirror that sends one focus to the other, a pair of confocal curves that must meet at right angles, a rectangular hyperbola that smuggles an orthocentre into the picture. This chapter builds those machines, proves the big theorems, and works them numerically until they are yours.

### 6.0 What you will be able to do

- Prove and deploy all three reflection properties (parabola, ellipse, hyperbola) — the backbone of billiard and optics problems.
- Prove confocal orthogonality with one gradient computation, and build confocal pairs on demand.
- Use the theorem *rectangular hyperbola through a triangle passes through the orthocentre*, find hyperbola centres, and connect them to the nine-point circle.
- Handle Simson lines, Steiner lines and Lambert's inscribed-parabola theorem.
- Quote Pascal and Brianchon and use their degenerate forms on tangents.

### 6.1 The three reflection properties, proved

> [!abstract] First Principles — ellipse: minimality gives the angles
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

> [!example] Olympiad Extension — the same proof, flipped signs
>
> **Hyperbola:** with the difference $\big||PF_1| - |PF_2|\big| = 2a$, reflecting $F_2$ gives $|PF_1| - |PF_2'| = \pm 2a$, so $F_1, P, F_2'$ are again collinear, while for other $Q$ on the tangent the reverse triangle inequality makes $\big||QF_1| - |QF_2|\big| \lt |F_1F_2'|$. Same conclusion: the tangent bisects the angle between the focal radii — a ray aimed at one focus reflects as if from the other. **Parabola:** the far focus "at infinity" makes the incident rays parallel: Chapter 2's $SP = SN$ is the same proof collapsed to one focus. Billiards inside an elliptical table: any shot through one focus returns through the other, forever — the seed of Poncelet's closure theorem.

#### **P41**[JEE Main][practice][whispering gallery]A whispering gallery has ceiling profile $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$ (units…

A whispering gallery has ceiling profile $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$ (units: metres). Two people stand at the foci. How far apart are they, and how far is each from the nearest wall (vertex)?

<details>
<summary>Answer + Reasoning</summary>

**Method: reflection property says the foci are the "hot spots".** $c = \sqrt{25 - 9} = 4$: foci $(\pm 4, 0)$, distance apart $8$ m; nearest vertex $(\pm 5, 0)$, so $1$ m away.

Answer: **8 m apart; each 1 m from the nearest vertex**. (Whispers at one focus converge at the other — an application of §6.1 ✓.)

</details>

#### **P42**[Olympiad][practice][hyperbola bisector]Verify numerically that at $P = (4\sqrt2, 3)$ on $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$…

Verify numerically that at $P = (4\sqrt2, 3)$ on $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, the tangent bisects the angle between the focal segments.

<details>
<summary>Answer + Reasoning</summary>

**Method: three slopes, two angles.** $P$ is on the curve: $\tfrac{32}{16} - 1 = 1$ ✓. Tangent slope: $\dfrac{b^2x}{a^2y} = \dfrac{9\cdot4\sqrt2}{16\cdot3} = \dfrac{3\sqrt2}{4}$, direction angle $\approx 46.70^\circ$. Focal rays: to $F_2(5,0)$: $\approx -102.37^\circ$; to $F_1(-5,0)$: $\approx -164.26^\circ$. Halfway between the rays: $\approx -133.32^\circ$, which is exactly the tangent direction modulo $180^\circ$ ($46.70^\circ - 180^\circ = -133.30^\circ$, equal up to rounding).

Answer: **both angles $\approx 30.96^\circ$** — the tangent is the internal bisector, mirror-image of the ellipse's external bisector ✓.

</details>

#### **P47**[JEE Adv][practice][billiard]On the elliptical billiard table $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, a ball is shot…

On the elliptical billiard table $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, a ball is shot from the focus $(4, 0)$ to the point $(0, 3)$. Show that after one cushion contact it passes through the other focus.

<details>
<summary>Answer + Reasoning</summary>

**Method: reflect the direction in the tangent.** At $(0,3)$ (top of the ellipse) the tangent is horizontal: $y = 3$. The ball travels from $(4,0)$ to $(0,3)$ along direction $(-4, 3)$; reflecting in the horizontal cushion gives $(-4, -3)$. From $(0,3)$ with direction $(-4,-3)$: at parameter $t=1$ we reach $(-4, 0)$ — the other focus.

Answer: **yes — it passes through $(-4, 0)$**, exactly as §6.1 predicts ✓.

</details>

### 6.2 Confocal conics meet at right angles

Fix the foci $(\pm c, 0)$. The ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ with $a^2 - b^2 = c^2$ and the hyperbola $\dfrac{x^2}{A^2} - \dfrac{y^2}{B^2} = 1$ with $A^2 + B^2 = c^2$ are called a **confocal pair**. Through every point off the axes passes exactly one confocal ellipse and one confocal hyperbola — and:

> [!abstract] First Principles — orthogonality from two unit vectors
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

#### **S15**[Olympiad][solved][confocal pair]Find the confocal hyperbola through $\left(\tfrac32, \sqrt3\right)$ for the ellipse…

Find the confocal hyperbola through $\left(\tfrac32, \sqrt3\right)$ for the ellipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$, and verify the tangents are perpendicular there.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning

**Name the move first:** $c^2 = 9 - 4 = 5$. Distances from $\left(\tfrac32, \sqrt3\right)$ to $(\pm\sqrt5, 0)$: $d_1^2 = \left(\tfrac32 - \sqrt5\right)^2 + 3 = \tfrac{41}{4} - 3\sqrt5$ and $d_2^2 = \left(\tfrac32 + \sqrt5\right)^2 + 3 = \tfrac{41}{4} + 3\sqrt5$; since $d_1 + d_2 = 2a = 6$ (P is on the ellipse), $(d_2 - d_1)(d_2 + d_1) = d_2^2 - d_1^2 = 6\sqrt5$, giving $d_2 - d_1 = \sqrt5$.

Hyperbola: $2A = \sqrt5$, so $A^2 = \tfrac54$, $B^2 = c^2 - A^2 = 5 - \tfrac54 = \tfrac{15}{4}$: $\dfrac{x^2}{5/4} - \dfrac{y^2}{15/4} = 1$. Check the point: $\dfrac{9/4}{5/4} - \dfrac{3}{15/4} = \dfrac95 - \dfrac45 = 1$ ✓.

Slopes: ellipse $-\dfrac{b^2x}{a^2y} = -\dfrac{4\cdot 3/2}{9\sqrt3} = -\dfrac{2}{3\sqrt3}$; hyperbola $\dfrac{B^2x}{A^2y} = \dfrac{(15/4)(3/2)}{(5/4)\sqrt3} = \dfrac{3\sqrt3}{2}$. Product: $-\dfrac{2}{3\sqrt3}\cdot\dfrac{3\sqrt3}{2} = -1$ ✓.

Total: **Answer: $\dfrac{x^2}{5/4} - \dfrac{y^2}{15/4} = 1$; perpendicular tangents**

</details>

#### **P45**[Olympiad][practice][confocal pair]For the ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, find the confocal hyperbola through…

For the ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$, find the confocal hyperbola through $P = \left(\tfrac52, \tfrac{3\sqrt3}{2}\right)$ and verify orthogonality there.

<details>
<summary>Answer + Reasoning</summary>

**Method: $c = 4$; use the focal distances.** From P21: $d_1 = 3, d_2 = 7$, so $2A = |d_2 - d_1| = 4$: $A = 2$, $B^2 = 16 - 4 = 12$.

Answer: **$\dfrac{x^2}{4} - \dfrac{y^2}{12} = 1$**. Slopes: ellipse $-\dfrac{9\cdot 5/2}{25\cdot 3\sqrt3/2} = -\dfrac{\sqrt3}{5}$; hyperbola $\dfrac{12\cdot 5/2}{4\cdot 3\sqrt3/2} = \dfrac{5}{\sqrt3}$; product $-1$ ✓.

</details>

### 6.3 Rectangular hyperbolas through a triangle

A rectangular hyperbola with asymptotes parallel to the coordinate axes has equation $xy + Dx + Ey + F = 0$ — three parameters after scaling, so **exactly one** such hyperbola passes through three given points. Where does it go next?

> [!abstract] First Principles — the orthocentre theorem, via parameters
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

> [!example] Olympiad Extension — centres ride the nine-point circle
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

#### **P43**[Olympiad][practice][orthocentre theorem]Repeat S14 for the triangle $(1, 2)$, $(3, 6)$, $(7, 0)$: find the hyperbola, the…

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

> [!example] Olympiad Extension — Lambert's theorem
>
> A parabola *inscribed* in a triangle (tangent to all three sides) has its focus on the circumcircle — and its **directrix is the Steiner line of that focus**. Why: the parabola with focus $F$ and directrix $\ell$ is tangent to a line $m$ exactly when the reflection of $F$ across $m$ lies on $\ell$ (the equal-angle definition of tangency). For the parabola to hug all three sides, $\ell$ must pass through all three reflections of $F$ — which is precisely the Steiner line, and exists precisely when $F$ is on the circumcircle. This links Chapter 2's curve to the triangle's circle in one stroke, and it is a standing ISL/Olympiad construction: *given a triangle, construct a parabola tangent to its sides*.

#### **P46**[Olympiad][practice][Simson + Steiner]For the right triangle $(0,0)$, $(4,0)$, $(0,3)$ and the point $P = (2,4)$: verify $P$ is…

For the right triangle $(0,0)$, $(4,0)$, $(0,3)$ and the point $P = (2,4)$: verify $P$ is on the circumcircle, find the Simson line and the Steiner line, and deduce the directrix of the inscribed parabola with focus $P$.

<details>
<summary>Answer + Reasoning</summary>

**Method: compute everything.** Circumcircle of the $3\text{-}4\text{-}5$ triangle: $x^2 + y^2 - 4x - 3y = 0$; $P = (2,4)$: $4 + 16 - 8 - 12 = 0$ ✓.

Feet: to $y = 0$: $(2, 0)$; to $x = 0$: $(0, 4)$; to $3x + 4y = 12$: $\left(\tfrac45, \tfrac{12}{5}\right)$. All three satisfy $y = -2x + 4$: **Simson line $y = -2x + 4$**.

Reflections: across $y=0$: $(2, -4)$; across $x=0$: $(-2, 4)$; across the hypotenuse: $\left(-\tfrac25, \tfrac45\right)$. All on $y = -2x$: **Steiner line $y = -2x$** — parallel to the Simson line ✓.

Answer: **Simson $y = -2x + 4$; Steiner $y = -2x$; the inscribed parabola with focus $(2,4)$ has directrix $y = -2x$** (Lambert ✓).

</details>

### 6.5 Pascal, Brianchon, and a construction worth knowing

> [!example] Olympiad Extension — the two hexagon theorems
>
> **Pascal's theorem.** For six points on a conic, the three intersections of opposite sides of the hexagon are collinear. **Brianchon's theorem.** For six tangents to a conic, the three "main diagonals" of the circumscribed hexagon are concurrent. The two are polar duals of each other — polarity (Chapter 5) maps one to the other. The olympiad workhorse is the *degenerate* version: let two adjacent vertices coincide, and the "side" between them becomes the tangent there. With *two* pairs coinciding you get the theorem that the intersections of two pairs of tangents and one pair of chords line up — instantly producing collinearity/concurrency conclusions that coordinate bashing would take a page to reach. (Poncelet's porism — infinitely many triangles inscribed in one conic and circumscribed about another — is the deep cousin of the billiard observation in §6.1.)

#### **P48**[Olympiad][practice][auxiliary circle]For $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ at eccentric angle $45^\circ$, show that the…

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

---

# Appendix — Well-Ordered Theory Reference

> **Philosophy**: One definition $e$ = focus-directrix ratio, everything else (second-degree equation, parametric, $T=0$, reflection) derived.

---

## 1. Conic Family from First Principles

### 1.1 Focus-Directrix Definition

Locus of point $P$ such that $\frac{\text{dist to focus }F}{\text{dist to directrix }l}=e$ constant eccentricity.

- $e<1$ ellipse, $e=1$ parabola, $e>1$ hyperbola.
- $e=0$ circle (focus = center, directrix at infinity).

**Why $e$ determines shape**: Fix $F$ and $l$, vary $e$ → cross-section of cone by plane at different angles.

### 1.2 Second-Degree General Equation

$ax^2+2hxy+by^2+2gx+2fy+c=0$, $S=0$.

Discriminant $h^2-ab$: $<0$ ellipse, $=0$ parabola, $>0$ hyperbola (provided non-degenerate, $\Delta\neq0$).

Rotation removing $xy$ term: rotate axes by $\theta$ where $\tan2\theta=\frac{2h}{a-b}$ → eigenvalues of $\begin{pmatrix}a&h\\h&b\end{pmatrix}$ give $a',b'$.

```mermaid
flowchart TD
    A["Focus-directrix e"] --> B["e<1 ellipse"]
    A --> C["e=1 parabola"]
    A --> D["e>1 hyperbola"]
    B --> E["Second-degree S=0"]
    E --> F["h²-ab <0 ellipse, =0 parabola, >0 hyperbola"]
```

---

## 2. Parabola — Anatomy and Machinery

### 2.1 Standard $y^2=4ax$

Focus $(a,0)$, directrix $x=-a$, vertex $(0,0)$, axis $y=0$, latus rectum $4a$ (focal chord $\perp$ axis).

**Parametric**: $P(t)=(at^2,2at)$, $t$ is not angle but parameter, slope of tangent? Actually $t$ relates to point.

**Derivation**: Distance to focus $\sqrt{(x-a)^2+y^2}$ = distance to directrix $|x+a|$ → square → $y^2=4ax$.

### 2.2 Chords, Tangents, Normals

- **Chord joining $t_1,t_2$**: $(t_1+t_2)y = 2x + 2at_1t_2$ — the limit $t_1,t_2 \to t$ recovers the tangent $ty = x+at^2$.

- **Tangent at $t$**: $ty = x+at^2$.
- **Normal at $t$**: $y = -tx +2at+at^3$.
- **Chord of contact from $(x_1,y_1)$**: $T=0$ → $yy_1 =2a(x+x_1)$? Wait for parabola $y^2=4ax$, $T$: $yy_1=2a(x+x_1)$.
- **Director circle**: Locus of perpendicular tangents — for parabola, directrix $x=-a$ itself.

```mermaid
flowchart LR
    A["y²=4ax"] --> B["Param at²,2at"]
    B --> C["Tangent ty=x+at²"]
    C --> D["Normal y=-tx+2at+at³"]
    D --> E["Reflection parallel→focus"]
```

### 2.3 Reflection Property

Parabola reflects rays parallel to axis to focus.

**Proof via angle bisector**: Tangent at $P$ makes equal angles with line $PF$ and line through $P$ parallel to axis. Show via $\frac{d}{dx}$ or vector.

**Applications**: Satellite dish, headlight, solar cooker.

---

## 3. Ellipse — Geometry of Squashed Circle

### 3.1 Standard $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$, $a\ge b$

Foci $(\pm ae,0)$, $b^2=a^2(1-e^2)$, $e=\sqrt{1-b^2/a^2}$, major axis $2a$ along $x$, minor $2b$, latus rectum $2b^2/a$, center $(0,0)$.

**Parametric**: $a\cos\theta,b\sin\theta$, $\theta$ eccentric angle (not polar angle, auxiliary circle).

**Definition sum distances**: $PF_1+PF_2=2a$ constant — Gardener's string.

### 3.2 Tangents, Director, Auxiliary

- **Tangent at $\theta$**: $\frac{x\cos\theta}{a}+\frac{y\sin\theta}{b}=1$.
- **Director circle**: Locus of perpendicular tangents $x^2+y^2=a^2+b^2$ — proof via $m_1m_2=-1$ for $y=mx\pm\sqrt{a^2m^2+b^2}$.
- **Auxiliary circle**: $x^2+y^2=a^2$, foot of perpendicular from focus to tangent lies on auxiliary? Actually for ellipse...
- **Chord with midpoint $(x_1,y_1)$**: $T=S_1$ → $\frac{xx_1}{a^2}+\frac{yy_1}{b^2}=\frac{x_1^2}{a^2}+\frac{y_1^2}{b^2}$.

```mermaid
flowchart TD
    A["x²/a²+y²/b²=1"] --> B["Param a cosθ, b sinθ"]
    B --> C["Tangent x cosθ/a + y sinθ/b=1"]
    C --> D["Director x²+y²=a²+b²"]
    D --> E["Reflection focus→other focus"]
    E --> F["Sum distances 2a constant"]
```

### 3.3 Reflection Property

Ellipse reflects ray from one focus to other focus.

**Proof**: Tangent bisects external angle between $F_1P$ and $F_2P$, i.e., makes equal angles with lines to foci.

**Applications**: Whispering gallery, lithotripter.

---

## 4. Hyperbola and Its Asymptotes

### 4.1 Standard $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$

Foci $(\pm ae,0)$, $b^2=a^2(e^2-1)$, $e=\sqrt{1+b^2/a^2}>1$, transverse axis $2a$, conjugate $2b$, latus rectum $2b^2/a$.

Asymptotes $y=\pm\frac{b}{a}x$ — limiting tangents as $P\to\infty$, diagonals of rectangle.

Rectangular hyperbola $xy=c^2$, asymptotes coordinate axes, $e=\sqrt2$.

**Parametric**: $a\sec\theta,b\tan\theta$ or $a\cosh t,b\sinh t$.

### 4.2 Tangents, Director, Conjugate

- **Tangent at $\theta$**: $\frac{x\sec\theta}{a}-\frac{y\tan\theta}{b}=1$.
- **Director**: $x^2+y^2=a^2-b^2$ (real only if $a>b$, i.e., $e<\sqrt2$).
- **Conjugate hyperbola**: $\frac{y^2}{b^2}-\frac{x^2}{a^2}=1$, same asymptotes, roles swapped.

```mermaid
flowchart TD
    A["x²/a²-y²/b²=1"] --> B["Asymptotes y=±(b/a)x limiting tangents"]
    B --> C["Rectangular xy=c² asymptotes axes"]
    C --> D["Param a secθ, b tanθ"]
    D --> E["Director x²+y²=a²-b²"]
    E --> F["Reflection focus→away from other"]
```

### 4.3 Reflection Property

Hyperbola reflects ray from one focus away from other focus (tangent bisects internal angle? Actually external).

---

## 5. Tangents, Normals, Chords and Polars — Unified Machinery

### 5.1 $T=0$, $S_1$, $T=S_1$, $SS_1=T^2$

For $S=0$ conic:

- **Tangent at $(x_1,y_1)$ on curve**: $T=0$ where $T$ is obtained by replacing $x^2\to xx_1$, $y^2\to yy_1$, $xy\to\frac{xy_1+x_1y}{2}$, $x\to\frac{x+x_1}{2}$, $y\to\frac{y+y_1}{2}$.
- **Chord with midpoint $(x_1,y_1)$**: $T=S_1$ where $S_1=S(x_1,y_1)$.
- **Pair of tangents from $(x_1,y_1)$**: $SS_1=T^2$ — homogeneous second-degree pair of lines.
- **Chord of contact from $(x_1,y_1)$**: $T=0$ (same as tangent formula but $(x_1,y_1)$ outside).
- **Polar of $(x_1,y_1)$**: $T=0$ locus of chord of contact as point moves? Actually polar is $T=0$, pole is $(x_1,y_1)$.
- **Director circle**: Locus of point from which two perpendicular tangents can be drawn.

```mermaid
flowchart TD
    A["S=0 conic"] --> B["T=0 tangent at (x1,y1) on curve"]
    A --> C["S1=0 value at (x1,y1)"]
    C --> D["T=S1 chord with midpoint (x1,y1)"]
    A --> E["SS1=T² pair of tangents from (x1,y1)"]
    E --> F["T=0 chord of contact from external (x1,y1)"]
    F --> G["Polar T=0, pole (x1,y1) duality"]
    G --> H["Director circle locus perp tangents"]
```

**JEE Adv**: $y=mx+c$ tangent to $y^2=4ax$ iff $c=a/m$, to $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ iff $c^2=a^2m^2+b^2$, to $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ iff $c^2=a^2m^2-b^2$.

### 5.2 Pole-Polar Duality

If $P$ lies on polar of $Q$, then $Q$ lies on polar of $P$ — duality.

Harmonic bundles: $(A,B;C,D)=-1$ etc.

---

## 6. Olympiad Frontier — Reflection, Confocal, Synthesis

### 6.1 Reflection Proofs via Angle Bisector

- **Parabola**: Tangent makes equal angles with $PF$ and line parallel to axis → prove via $y^2=4ax$, tangent $ty=x+at^2$, vector.
- **Ellipse**: Tangent makes equal angles with $F_1P$, $F_2P$ → sum distances minimal property.
- **Hyperbola**: Tangent bisects angle between $F_1P$ and $F_2P$ external.

```mermaid
flowchart TD
    P["Parabola"] --> R1["Parallel→focus"]
    E["Ellipse"] --> R2["Focus→other focus"]
    H["Hyperbola"] --> R3["Focus→away from other"]
    R1 --> Proof["Proof via tangent angle bisector"]
    R2 --> Proof
    R3 --> Proof
```

### 6.2 Confocal Family

Conics with same foci: $\frac{x^2}{a^2-\lambda}+\frac{y^2}{b^2-\lambda}=1$ (confocal ellipses/hyperbolas).

Property: Confocal ellipse and hyperbola intersect orthogonally — elliptic coordinates orthogonal system.

**Elliptic coordinates**: $(\lambda,\mu)$ where $\lambda$ = confocal ellipse parameter, $\mu$ = hyperbola.

### 6.3 Second-Degree Homogeneous & Classification

$ax^2+2hxy+by^2=0$ pair of lines through origin, $h^2-ab$ determines real/coincident/imaginary.

General $S=0$ classification via eigenvalues of $\begin{pmatrix}a&h&g\\h&b&f\\g&f&c\end{pmatrix}$ and top-left $2×2$.

Rotation removing $xy$: $\tan2\theta=2h/(a-b)$.

### 6.4 Synthesis

- $S=0$ as locus: e.g., $S_1+\lambda S_2=0$ family through intersection.
- Coaxal system, radical axis.

---

## Paper — 38 Questions A–H + Stretch

Attempt after Chapter 6, 4–5 hours, full solutions in `olympiad-paper-solutions.md`.

Covers focus-directrix, parametric, $T=0$, $S_1$, pair of tangents, director, asymptotes, reflection, confocal orthogonal.

---

*Well-ordered: $e$ definition → second-degree $h^2-ab$ → parabola $y^2=4ax$ $at^2,2at$ $ty=x+at^2$ → ellipse $x^2/a^2+y^2/b^2=1$ $a\cos\theta,b\sin\theta$ → hyperbola $x^2/a^2-y^2/b^2=1$ asymptotes → unified $T=0,S_1,T=S_1,SS_1=T^2$ → pole-polar → reflection proofs → confocal orthogonal → classification.*
