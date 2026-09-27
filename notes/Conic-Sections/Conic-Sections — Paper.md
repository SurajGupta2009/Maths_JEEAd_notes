---
title: "Conic Sections — Olympiad Paper"
aliases:
  - Conic-Sections Paper
module: "Conic-Sections"
module_title: "Conic Sections"
type: paper
tags:
  - conic-sections
  - paper
  - olympiad
  - assessment
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[06-the-olympiad-frontier-reflection-confocals-and-triangles|Chapter 6]] · 📖 [[Conic-Sections|Conic Sections]] · ✅ [[Conic-Sections — Solutions|Solutions]] ➡

# Olympiad Paper · 38 questions

*Final assessment · whole module*

# Olympiad & JEE Advanced Paper — Conic Sections

38 questions in eight sections (A–H), JEE Main → JEE Advanced → Olympiad. Each section maps onto a chapter's signature move: A · first principles, B · parabola machinery, C · ellipse, D · hyperbola, E · tangents and polars, F · normals and parameters, G · reflection/confocals/triangles, H · synthesis. **Do it cold, on paper.** Suggested time: 3 h 30 m. Short-form answers are given; full worked solutions are in [the companion file](#solutions). Every numeric answer below was verified by an independent pure-Python computation before publication.

### Supplementary notes

**Instructions.** Each question is tagged with difficulty. "Prove" questions earn marks only for a complete argument — a claim without proof earns none. Numeric answers are expected fully reduced unless stated otherwise.


### A · First Principles & Eccentricity (Q1–Q5)

#### **Q1**[JEE Main]Find the equation of the parabola with focus [formula] and directrix [formula]…

Find the equation of the parabola with focus $(0, -3)$ and directrix $y = 3$.


Answer: $x^2 = -12y$

#### **Q2**[JEE Main]A point moves so that its distance from [formula] is half its distance from th…

A point moves so that its distance from $(3, 0)$ is half its distance from the line $x = 12$. Identify the conic and give its equation and eccentricity.


Answer: ellipse $\dfrac{x^2}{36} + \dfrac{y^2}{27} = 1$, $e = \tfrac12$

#### **Q3**[JEE Main]Find the eccentricity and the foci of [formula] .

Find the eccentricity and the foci of $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.


Answer: $e = \tfrac45$; foci $(\pm 4, 0)$

#### **Q4**[JEE Adv]For [formula] , find the eccentricity, the foci and the directrices.

For $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, find the eccentricity, the foci and the directrices.


Answer: $e = \tfrac54$; foci $(\pm 5, 0)$; directrices $x = \pm\tfrac{16}{5}$

#### **Q5**[Olympiad]Show that the focus-directrix definition with focus [formula] , directrix [for…

Show that the focus-directrix definition with focus $(0,0)$, directrix $x = 0$ and $e = 1$ produces a degenerate locus, and identify it.


Answer: the doubled line $y = 0$ (the axis itself)


### B · Parabola Machinery (Q6–Q11)

#### **Q6**[JEE Main]Find the focal distance of the point [formula] on the parabola [formula] .

Find the focal distance of the point $(4, 4)$ on the parabola $y^2 = 4x$.


Answer: $x + a = 4 + 1 = 5$

#### **Q7**[JEE Adv]One end of a focal chord of [formula] has parameter [formula] . Find the other…

One end of a focal chord of $y^2 = 8x$ has parameter $t = 3$. Find the other end and the length of the chord.


Answer: $\left(\tfrac29, -\tfrac43\right)$; length $\tfrac{200}{9}$

#### **Q8**[JEE Adv]Find the equation of the chord of [formula] bisected at [formula] .

Find the equation of the chord of $y^2 = 4x$ bisected at $\left(\tfrac{13}{4}, 3\right)$.


Answer: $4x - 6y + 5 = 0$

#### **Q9**[JEE Adv]How many normals can be drawn from [formula] to [formula] ? Find their slopes …

How many normals can be drawn from $(9, 6)$ to $y^2 = 4x$? Find their slopes and their feet, and verify the sum of the slopes.


Answer: three; slopes $1, 2, -3$ (sum $0$); feet $(1,-2), (4,-4), (9,6)$

#### **Q10**[JEE Adv]The normal at the point with [formula] on [formula] meets the axis at [formula…

The normal at the point with $t = 2$ on $y^2 = 4x$ meets the axis at $N$. Compute $N$, $|SP|$ and $|SN|$, and name the property these lengths exhibit.


Answer: $N = (6, 0)$; $|SP| = |SN| = 5$ — the isosceles triangle $SPN$

#### **Q11**[Olympiad]Prove that the foot of the perpendicular from the focus of [formula] to any ta…

Prove that the foot of the perpendicular from the focus of $y^2 = 4ax$ to any tangent lies on the tangent at the vertex, and compute that foot for the tangent at $t = 2$ when $a = 1$.


Answer: foot $= (0, at) = (0, 2)$ — always on $x = 0$


### C · The Ellipse (Q12–Q17)

#### **Q12**[JEE Main]Find the eccentricity and the latus rectum of [formula] .

Find the eccentricity and the latus rectum of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$.


Answer: $e = \tfrac{\sqrt7}{4}$; LR $= \tfrac92$

#### **Q13**[JEE Main]Write all tangent lines of slope [formula] to [formula] , and verify one of th…

Write all tangent lines of slope $1$ to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$, and verify one of them is genuinely tangent by the discriminant test.


Answer: $y = x \pm 5$; $25x^2 + 160x + 256 = (5x+16)^2$, a double root

#### **Q14**[JEE Adv]A point moves with [formula] , [formula] . Find the ellipse, the length of its…

A point moves with $|PF_1| + |PF_2| = 10$, $F_{1,2} = (\mp 4, 0)$. Find the ellipse, the length of its latus rectum, and the ends of the latus rectum through $(4, 0)$.


Answer: $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$; LR $= \tfrac{18}{5}$; ends $\left(4, \pm\tfrac95\right)$

#### **Q15**[JEE Adv]Find the director circle of [formula] and its four axis intercepts.

Find the director circle of $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ and its four axis intercepts.


Answer: $x^2 + y^2 = 25$; $(\pm 5, 0)$, $(0, \pm 5)$

#### **Q16**[JEE Adv]Find the chord of contact from [formula] to [formula] , and show it meets the …

Find the chord of contact from $(5, 3)$ to $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$, and show it meets the ellipse in two real points.


Answer: $15x + 16y = 48$; contacts $(0, 3)$ and $\left(\tfrac{160}{41}, -\tfrac{27}{41}\right)$

#### **Q17**[Olympiad]At the latus-rectum end [formula] of [formula] , compute the angles the tangen…

At the latus-rectum end $P = \left(4, \tfrac95\right)$ of $\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$, compute the angles the tangent makes with the two focal segments and confirm the reflection property.


Answer: both angles $\approx 51.34^\circ$ — equal, so a ray from one focus reflects to the other


### D · Hyperbola & Rectangular Hyperbola (Q18–Q23)

#### **Q18**[JEE Main]For [formula] , find [formula] , the foci and the latus rectum.

For $9x^2 - 16y^2 = 144$, find $e$, the foci and the latus rectum.


Answer: $e = \tfrac54$; foci $(\pm 5, 0)$; LR $= \tfrac92$

#### **Q19**[JEE Main]Find the asymptotes of [formula] and the angle between them (around the transv…

Find the asymptotes of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ and the angle between them (around the transverse axis).


Answer: $y = \pm\tfrac32 x$; $2\arctan\tfrac32 \approx 112.62^\circ$

#### **Q20**[JEE Adv]The asymptotes of a hyperbola make [formula] around the transverse axis. Find …

The asymptotes of a hyperbola make $60^\circ$ around the transverse axis. Find the eccentricity.


Answer: $e = \dfrac{2}{\sqrt3}$

#### **Q21**[JEE Adv]Write the conjugate hyperbola of [formula] , compute both eccentricities, and …

Write the conjugate hyperbola of $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, compute both eccentricities, and verify $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$.


Answer: $\dfrac{y^2}{9} - \dfrac{x^2}{16} = 1$; $e = \tfrac54$, $e' = \tfrac53$; $\tfrac{16}{25} + \tfrac{9}{25} = 1$

#### **Q22**[JEE Adv]For the rectangular hyperbola [formula] , find the tangent and normal at [form…

For the rectangular hyperbola $xy = 9$, find the tangent and normal at $t = 3$, and verify perpendicularity via slopes.


Answer: tangent $x + 9y = 18$ (slope $-\tfrac19$); normal $y = 9x - 80$ (slope $9$)

#### **Q23**[Olympiad]Show that no two real perpendicular tangents can be drawn to the rectangular h…

Show that no two real perpendicular tangents can be drawn to the rectangular hyperbola $x^2 - y^2 = a^2$, by analysing the slope form, and identify its director "circle".


Answer: perpendicular slopes force $|m| = 1$, $c = 0$ — the asymptotes; director circle degenerates to $x^2 + y^2 = 0$


### E · Tangents, Chords & Polars (Q24–Q28)

#### **Q24**[JEE Main]Find the tangent of slope [formula] to [formula] and its contact point.

Find the tangent of slope $2$ to $y^2 = 4x$ and its contact point.


Answer: $y = 2x + \tfrac12$; contact $\left(\tfrac14, 1\right)$

#### **Q25**[JEE Adv]Find the joint equation of the pair of tangents from [formula] to [formula] , …

Find the joint equation of the pair of tangents from $(1, 3)$ to $y^2 = 4x$, and the two tangent slopes.


Answer: $x^2 + y^2 - 3xy + 7x - 3y + 1 = 0$; slopes $\tfrac{3 \pm \sqrt5}{2}$

#### **Q26**[JEE Adv]Find the chord of contact from [formula] to [formula] and show its two contact…

Find the chord of contact from $(1, 3)$ to $y^2 = 4x$ and show its two contact points are real.


Answer: $2x - 3y + 2 = 0$; contact $x$-coordinates $\tfrac{7 \pm 3\sqrt5}{2}$, real

#### **Q27**[JEE Adv]Find the pole of the line [formula] with respect to [formula] , and verify by …

Find the pole of the line $3x - 4y + 7 = 0$ with respect to $y^2 = 4x$, and verify by recomputing its polar.


Answer: pole $= \left(\tfrac73, \tfrac83\right)$; polar $8y = 6x + 14 \propto 3x - 4y + 7 = 0$

#### **Q28**[Olympiad]Prove that the polar of a focus of an ellipse is the corresponding directrix, …

Prove that the polar of a focus of an ellipse is the corresponding directrix, for $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.


Answer: polar of $(4, 0)$ is $x = \tfrac{25}{4} = \tfrac{a}{e}$ — the directrix


### F · Normals & Parametric Geometry (Q29–Q32)

#### **Q29**[JEE Main]Find the point on [formula] with eccentric angle [formula] , and verify it lie…

Find the point on $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ with eccentric angle $60^\circ$, and verify it lies on the curve.


Answer: $\left(2, \tfrac{3\sqrt3}{2}\right)$; $\tfrac{4}{16} + \tfrac{27/4}{9} = 1$

#### **Q30**[JEE Adv]Find the tangent and the normal at the point of Q29, and verify they are perpe…

Find the tangent and the normal at the point of Q29, and verify they are perpendicular.


Answer: tangent $3x + 4\sqrt3\,y = 24$; normal $8\sqrt3\,x - 6y = 7\sqrt3$; slopes $-\tfrac{3}{4\sqrt3}$ and $\tfrac{4\sqrt3}{3}$

#### **Q31**[JEE Adv]Find the points on [formula] at which the normal has slope [formula] .

Find the points on $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$ at which the normal has slope $1$.


Answer: $\pm\left(\tfrac{16}{5}, \tfrac95\right)$

#### **Q32**[Olympiad]Prove that the normals at the ends of any focal chord of [formula] are perpend…

Prove that the normals at the ends of any focal chord of $y^2 = 4ax$ are perpendicular, and verify for $a = 1$, $t = 2$.


Answer: slopes $-t$ and $\tfrac1t$, product $-1$; normals $y = -2x + 12$ and $y = \tfrac{x}{2} - \tfrac98$


### G · Reflection, Confocals & Triangles (Q33–Q36)

#### **Q33**[JEE Adv]A whispering gallery has ceiling profile [formula] (meters). How far apart are…

A whispering gallery has ceiling profile $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$ (meters). How far apart are the foci — the two "whisper spots"?


Answer: $2c = 2\sqrt{100 - 36} = 16$ m

#### **Q34**[Olympiad]Verify numerically that at [formula] on [formula] , the tangent bisects the an…

Verify numerically that at $P = \left(5, \tfrac94\right)$ on $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, the tangent bisects the angle between the two focal segments.


Answer: both angles $\approx 38.66^\circ$ — tangent is the internal bisector

#### **Q35**[Olympiad]Find the orthocentre of the triangle [formula] , [formula] , [formula] ; show …

Find the orthocentre of the triangle $(0, 4)$, $(6, 4)$, $(2, 0)$; show that the rectangular hyperbola $xy - 4x - 2y + 8 = 0$ passes through all three vertices and the orthocentre.


Answer: $H = (2, 2)$; $H$ and all vertices satisfy the hyperbola

#### **Q36**[Olympiad]Find the hyperbola confocal with [formula] that passes through [formula] , and…

Find the hyperbola confocal with $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ that passes through $\left(4, \tfrac{12}{5}\right)$, and verify the two curves meet at right angles there.


Answer: $\dfrac{25x^2}{144} - \dfrac{25y^2}{81} = 1$; slopes $-\tfrac{16}{15}$ and $\tfrac{15}{16}$, product $-1$


### H · Synthesis & Stretch (Q37–Q38)

#### **Q37**[Olympiad]Show that the midpoints of all focal chords of [formula] lie on a parabola; fi…

Show that the midpoints of all focal chords of $y^2 = 4ax$ lie on a parabola; find it and its latus rectum, and check with the chord whose ends are $t = 2$ and $t = -\tfrac12$ for $a = 1$.


Answer: locus $y^2 = 2a(x - a)$; LR $= 2a$; midpoint $\left(\tfrac{17}{8}, \tfrac32\right)$ satisfies it

#### **Q38**[Olympiad]Prove that for any tangent to [formula] , the product of the perpendicular dis…

Prove that for any tangent to $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$, the product of the perpendicular distances of the two foci from the tangent equals $b^2$, and verify at the tangent with eccentric angle $60^\circ$ for $a = 4$, $b = 3$.


Answer: product $= \dfrac{|c^2\cos^2\theta/a^2 - 1|}{\cos^2\theta/a^2 + \sin^2\theta/b^2} = b^2$; numerically $= 9$


### 📝 Exam technique notes

> **📝 Exam technique notes**
>
> (i) **Name the conic before the algebra**: the sign of the squared terms picks the chapter, and each chapter has its own $b^2$ relation. (ii) **Prefer parameters to coordinates** on the parabola ($t$) and both central conics ($\theta$); most tangent/normal questions collapse to one line. (iii) **Discriminant zero is the tangency certificate** — when asked to "show tangency", substitute and factor, don't argue by picture. (iv) **Midpoint chords and polars are $T = S_1$ and $T = 0$** — write $S_1$ with its $-1$ before anything else. (v) **Reflection questions** want the named property plus one verified angle or distance; quote the theorem, then do the arithmetic. (vi) Budget: sections A–C should cost you under 75 minutes to leave time for the G/H proofs.
