# Chapter 4 — The Hyperbola and Its Asymptotes

*6 sections · 11 questions*

*Chapter 4 of 6*

# The Hyperbola and Its Asymptotes

The hyperbola is the ellipse with one sign flipped — and that flip changes everything: the foci move outside the curve, a second conjugate curve appears, and the curve grows two straight *asymptotes* that every JEE question eventually touches. The rotated member of the family, $xy = c^2$, is the quiet star of Olympiad geometry: Chapter 6 will ride it through the orthocentre of a triangle.

### 4.0 What you will be able to do

- Read the anatomy of $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ — including why $b^2 = c^2 - a^2$ and why the foci are *outside* the vertices.
- Handle the conjugate hyperbola and the identity $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$.
- Derive the asymptotes, connect their angle to $e$, and detect "line parallel to an asymptote" pathologies.
- Work the rotated rectangular hyperbola $xy = c^2$: parametric point, tangent, normal.


### 4.1 Anatomy of the hyperbola

For $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$: vertices $(\pm a, 0)$; foci $(\pm ae, 0)$ with $c = ae = \sqrt{a^2 + b^2}$; eccentricity $e = \sqrt{1 + \dfrac{b^2}{a^2}} \gt 1$; directrices $x = \pm \dfrac{a}{e}$ (now *between* the centre and the vertices, since $a/e \lt a$); latus rectum ends $\left(\pm ae, \pm \dfrac{b^2}{a}\right)$, length $\dfrac{2b^2}{a}$.

> **⛁ First Principles — focal distances on the right branch**
>
> For $P(x, y)$ on the right branch ($x \ge a$), the focus-directrix definition with directrix $x = a/e$ gives $|PF_{\text{right}}| = e\left(x - \dfrac{a}{e}\right) = ex - a$, and by the difference definition $|PF_{\text{left}}| = ex + a$ — difference $2a$ exactly. Sanity at the vertex $x = a$: distances $a(1-e)$·… concretely $ea - a = c - a$ to the near focus and $c + a$ to the far one, and $(c+a) - (c-a) = 2a$ ✓. On the left branch the signs mirror. The absolute-value rule $\big||PF_1| - |PF_2|\big| = 2a$ is what "difference of distances" means — a fixed sign would trace one branch only.

#### **S9**[JEE Main][solved][full anatomy]Read off everything for [formula] : eccentricity, foci, latus rectum, asymptot…

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

#### **P25**[JEE Main][practice][standardise]For [formula] , find the eccentricity, the foci and the latus rectum.

For $4x^2 - 9y^2 = 36$, find the eccentricity, the foci and the latus rectum.

<details>
<summary>Answer + Reasoning</summary>

**Method: divide by 36 first.** $\dfrac{x^2}{9} - \dfrac{y^2}{4} = 1$: $a = 3, b = 2$, $c = \sqrt{13}$.


Answer: **$e = \tfrac{\sqrt{13}}{3}$, foci $(\pm\sqrt{13}, 0)$, LR $\tfrac{2\cdot4}{3} = \tfrac83$**. (Check: $e^2 = 1 + \tfrac49 = \tfrac{13}{9}$ ✓.)

</details>


### 4.2 The conjugate hyperbola

Swap the roles of the axes: $\dfrac{y^2}{b^2} - \dfrac{x^2}{a^2} = 1$ is the **conjugate hyperbola** — same $a, b$, but transverse axis now vertical, foci on the $y$-axis at $(0, \pm e'b)$ where $e' = \sqrt{1 + \dfrac{a^2}{b^2}}$ (the focal distance $c$ is shared: $c^2 = a^2 + b^2$).

> **ƒ Named Identity — $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$**
>
> $\dfrac{1}{e^2} = \dfrac{a^2}{a^2+b^2}$ and $\dfrac{1}{e'^2} = \dfrac{b^2}{a^2+b^2}$; the sum is $1$. Two hyperbolas sharing asymptote directions can never both be eccentricity $\sqrt2$ — the rectangularity budget is shared. JEE asks this identity almost verbatim.

#### **S11**[JEE Adv][solved][conjugate + identity]For the hyperbola with [formula] , compute [formula] and the conjugate's [form…

For the hyperbola with $a = 3, b = 4$, compute $e$ and the conjugate's $e'$, and verify $\dfrac{1}{e^2} + \dfrac{1}{e'^2} = 1$.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Method: same $c$, two denominators.** $c = 5$: $e = \tfrac53$ (transverse $a = 3$), $e' = \tfrac{c}{b} = \tfrac54$ (transverse $b = 4$).


$\dfrac{1}{e^2} + \dfrac{1}{e'^2} = \dfrac{9}{25} + \dfrac{16}{25} = 1$ ✓.


Total: **Answer: $e = \tfrac53$, $e' = \tfrac54$, identity holds**


**Check:** $e, e' \gt 1$ both, and neither equals $\sqrt2$: a hyperbola and its conjugate cannot both be rectangular ✓.

</details>

#### **P29**[JEE Main][practice][position test]Classify [formula] , [formula] , [formula] with respect to [formula] .

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

> **⚠ Common Trap — points on an asymptote determine nothing**
>
> Asking for the hyperbola $x^2/a^2 - y^2/b^2 = 1$ with given $e$ that "passes through" a point on $y = \pm\frac{b}{a}x$ is a trick: the answer is *no such hyperbola*. The curve and its asymptote never meet; a point on the asymptote is a witness of impossibility. Always test the point against $y = \frac{b}{a}x$ before solving.

#### **P26**[JEE Main][practice][asymptotes]What are the asymptotes of [formula] ? And find the angle between the asymptot…

What are the asymptotes of $xy = 6$? And find the angle between the asymptotes of $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: read the axes; then $\tan\alpha = b/a$.** $xy = 6$ never touches $x = 0$ or $y = 0$ and approaches both: its asymptotes are the coordinate axes. For the second: $\tan\alpha = \tfrac34$, angle $2\alpha = 2\arctan(0.75) \approx 73.74^\circ$.


Answer: **axes; $73.74^\circ$** around the transverse axis. (Check via the identity: $e^2 = 1 + \tfrac{9}{16} = \tfrac{25}{16}$, $\cos 2\alpha = \tfrac{2}{25/16} - 1 = \tfrac{32}{25} - 1 = \tfrac{7}{25}$, and $2\arctan(3/4)$ has cosine $\tfrac{1 - 9/16}{1 + 9/16} = \tfrac{7}{25}$ ✓.)

</details>

#### **P27**[JEE Adv][practice][reconstruct + trap](i) Explain why no hyperbola [formula] with [formula] passes through [formula]…

(i) Explain why no hyperbola $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ with $e = \tfrac54$ passes through $(4, 3)$. (ii) Find the one passing through $\left(4, \tfrac32\right)$.

<details>
<summary>Answer + Reasoning</summary>

**Method: check the asymptote first.** (i) With $e = \tfrac54$: $b^2 = a^2(e^2 - 1) = \tfrac{9}{16}a^2$, so the asymptote is $y = \tfrac34 x$ — and $(4,3)$ lies exactly on it. The curve never meets its asymptote: no solution exists.


(ii) Plug $\left(4, \tfrac32\right)$: $\dfrac{16}{a^2} - \dfrac{9/4}{9a^2/16} =
        \dfrac{16}{a^2} - \dfrac{4}{a^2} = \dfrac{12}{a^2} = 1$, so $a^2 = 12$, $b^2 = \tfrac{27}{4}$.


Answer: **(i) impossible — $(4,3)$ is on the asymptote $y = \tfrac34x$; (ii) $\dfrac{x^2}{12} - \dfrac{4y^2}{27} = 1$**. (Check: $\tfrac{16}{12} - \tfrac{(9/4)\cdot 4}{27} = \tfrac43 - \tfrac13 = 1$ ✓.)

</details>

#### **P28**[JEE Adv][practice][midpoint chord]Find the chord of [formula] bisected at [formula] , and verify the midpoint by…

Find the chord of $\dfrac{x^2}{4} - \dfrac{y^2}{9} = 1$ bisected at $(3, -2)$, and verify the midpoint by Vieta. (The formula $T = S_1$, previewed in P13 of Chapter 2, is proved in general in Chapter 5.)

<details>
<summary>Answer + Reasoning</summary>

**Method: $T = S_1$, with $S_1$ carrying its $-1$.** $S_1 = \tfrac94 - \tfrac49 - 1 = -\tfrac{31}{36}$. $T = S_1$ reads $\dfrac{3x}{4} - \dfrac{(-2)y}{9} - 1 = -\tfrac{31}{36}$, so $\dfrac{3x}{4} + \dfrac{2y}{9} = 1 - \tfrac{31}{36} = \dfrac{5}{36}$, i.e.



$$ 27x + 8y = 65. $$



Slope sanity: $-\tfrac{27}{8} = +\tfrac{b^2x_1}{a^2y_1} = \tfrac{9\cdot3}{4\cdot(-2)}$ ✓ (hyperbola sign, Chapter 5).


**Vieta:** substituting $y = \tfrac{65 - 27x}{8}$ into the hyperbola gives $-585x^2 + 3510x - 4801 = 0$; sum of roots $= \tfrac{3510}{585} = 6$, midpoint $x = 3$ ✓ (midpoint $y = -2$ follows from the line).


Answer: **$27x + 8y = 65$**.

</details>

#### **P31**[JEE Adv][practice][parallel to asymptote]Show that the line [formula] meets [formula] in exactly one finite point, and …

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

> **ƒ Named Result — the director circle can vanish**
>
> The same perpendicular-tangents computation as the ellipse (Chapter 3) now yields $x^2 + y^2 = a^2 - b^2$. If $a \gt b$ this is a real circle; if $a = b$ (rectangular hyperbola) it collapses to the single point $(0,0)$ — and since no real tangent pair passes through the origin except the asymptotes themselves, **a rectangular hyperbola has no pair of real perpendicular tangents**. Verified end-to-end in Q23 of the paper.

#### **P32**[JEE Adv][practice][director circle]Find the locus of intersection of perpendicular tangents to [formula] , and st…

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

#### **S10**[JEE Adv][solved][tangent + normal]For [formula] , find the tangent and normal at [formula] , and verify perpendi…

For $xy = 4$, find the tangent and normal at $t = 2$, and verify perpendicularity.

<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning


**Name the move first:** point $(ct, c/t) = (4, 1)$ with $c = 2$; then the two formulas.


Tangent: $\dfrac{x}{2} + 2y = 4$, i.e. $x + 4y = 8$ (slope $-\tfrac14$). Normal: $y = 4x - 16 + 1 = 4x - 15$ (slope $4$). Product of slopes: $-1$ ✓.


Total: **Answer: tangent $x + 4y = 8$; normal $y = 4x - 15$**


**Check:** both pass $(4,1)$: $4 + 4 = 8$ ✓; $16 - 15 = 1$ ✓; and implicit differentiation of $y = \tfrac4x$: $y'(4) = -\tfrac{4}{16} = -\tfrac14$ ✓.

</details>

#### **P30**[JEE Main][practice][tangent + normal]Find the tangent and normal to [formula] at [formula] .

Find the tangent and normal to $xy = 9$ at $t = 1$.

<details>
<summary>Answer + Reasoning</summary>

**Method: same recipe.** Point $(3, 3)$. Tangent: $x + y = 6$; normal: $y = t^2x - ct^3 + \tfrac{c}{t} = x - 3 + 3 = x$.


Answer: **tangent $x + y = 6$ (slope $-1$); normal $y = x$ (slope $1$)**. (Check: $3 + 3 = 6$ ✓; $y=x$ passes $(3,3)$ and is perpendicular to the tangent ✓.)

</details>



---

