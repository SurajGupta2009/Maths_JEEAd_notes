---
id: oly-04
part: olympiad
title: "Specialised Toolkit — Triangle Formulae & Derived Special Values"
---

## Status of this sheet

**Important classification note.** The current JEE Advanced syllabus sentence for trigonometry is "Trigonometric functions. General solution of trigonometric equations. Identities." — it does **not** list properties of triangles or heights & distances. The formulae below are the **standard triangle toolkit** used across JEE Main-level papers, olympiads (RMO/INMO geometry-algebra), and later chapters (conics, 3D, vectors). They are *added theory* (not derivable from the identities alone — they encode triangle *geometry*), but every model built here only uses Part I identities plus the sine/cosine rules as stated. Do not assume they "can never appear"; assume they are simply outside the quoted syllabus sentence and learn them as toolkit.

## The four triangle formulae

For a triangle with sides $a, b, c$ opposite angles $A, B, C$, circumradius $R$, inradius $r$, semiperimeter $s = \frac{a + b + c}{2}$, area $\Delta$:

$$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} = 2R, \qquad a^{2} = b^{2} + c^{2} - 2bc \cos A$$

$$\Delta = \dfrac{1}{2} bc \sin A = \sqrt{s(s-a)(s-b)(s-c)}, \qquad r = \dfrac{\Delta}{s}$$

$$\tan\dfrac{A}{2} = \dfrac{r}{s - a}$$

:::derive title="Cosine rule and $\Delta = rs$ — one line each"
Cosine rule: drop a height $h = c \sin B$ from $C$; project: $a = b \cos C + c \cos B$-style coordinate computation gives $a^{2} = b^{2} + c^{2} - 2bc \cos A$ (or expand $| \vec{B} - \vec{C} |^{2}$ in the vectors chapter). $\Delta = rs$: split the triangle into three $(r, s)$-shaped pieces — $\Delta = \frac{1}{2} r a + \frac{1}{2} r b + \frac{1}{2} r c = r s$ ✓. $\tan\frac{A}{2} = \frac{r}{s - a}$: the incircle tangent lengths are $s - a, s - b, s - c$ and half-angle right triangles give the ratio.
:::

## Derived special values (pure identities, pentagon angles)

$$\sin 18^{\circ} = \dfrac{\sqrt{5} - 1}{4} \approx 0.30902$$

$$\cos 36^{\circ} = \dfrac{\sqrt{5} + 1}{4} \approx 0.80902$$

:::derive title="Derivation — double-angle, then quadratic"
Let $x = 18^{\circ}$, so $5x = 90^{\circ}$ and $2x = 90^{\circ} - 3x$, hence $\sin 2x = \cos 3x$. Expand: $2 \sin x \cos x = 4 \cos^{3} x - 3 \cos x$; with $\cos x \ne 0$: $2 \sin x = 4 \cos^{2} x - 3 = 4(1 - \sin^{2} x) - 3 = 1 - 4 \sin^{2} x$. So $4 \sin^{2} x + 2 \sin x - 1 = 0 \Rightarrow \sin x = \frac{-2 + \sqrt{4 + 16}}{8} = \frac{\sqrt{5} - 1}{4}$ (positive root; $\sin 18^{\circ} > 0$) ✓. Then $\cos 36^{\circ} = 1 - 2 \sin^{2} 18^{\circ} = \frac{\sqrt{5} + 1}{4}$ ✓ (check numerically: $0.809017$).
:::

:::example title="Worked. Triangle with $A = 60^{\circ}$, $b = 5$, $c = 8$: find $a$ and $\Delta$"
Cosine rule: $a^{2} = 25 + 64 - 2 \cdot 5 \cdot 8 \cdot \frac{1}{2} = 49 \Rightarrow a = 7$. $\Delta = \frac{1}{2} \cdot 5 \cdot 8 \cdot \frac{\sqrt{3}}{2} = 10\sqrt{3} \approx 17.32$. Cross-check with Heron: $s = \frac{7 + 5 + 8}{2} = 10$, $\sqrt{10 \cdot 3 \cdot 5 \cdot 2} = \sqrt{300} = 10\sqrt{3}$ ✓.
:::

:::example title="Worked. $R$ and $r$ for the same triangle"
$2R = \frac{a}{\sin A} = \frac{7}{\sqrt{3}/2} = \frac{14}{\sqrt{3}} \Rightarrow R = \frac{7}{\sqrt{3}} \approx 4.041$. $r = \frac{\Delta}{s} = \frac{10\sqrt{3}}{10} = \sqrt{3} \approx 1.732$. Check $\tan\frac{A}{2} = \tan 30^{\circ} = \frac{1}{\sqrt{3}}$ vs $\frac{r}{s - a} = \frac{\sqrt{3}}{3} = \frac{1}{\sqrt{3}}$ ✓.
:::

:::warn title="Traps — triangle toolkit"
- The sine rule gives an **ambiguous case** (SSA): $a = b \frac{\sin A}{\sin B}$ with $\sin B = \frac{b \sin A}{a}$ may admit two triangles ($B$ and $180^{\circ} - B$).
- $\Delta = \frac{1}{2} (\text{base})(\text{height})$ needs the height; $\frac{1}{2} bc \sin A$ needs the angle **between** the two sides.
- Heron's formula: $s$ is semiperimeter; writing $s = a + b + c$ is the classic slip.
- $\tan\frac{A}{2} = \frac{r}{s - a}$ requires the usual triangle convention ($s > a$); for degenerate/failing configurations state the inequality.
- $18^{\circ}$-family values ($\sin 18^{\circ}, \cos 36^{\circ}, \sin 54^{\circ} = \cos 36^{\circ}$ etc.): derive from the quadratic each time if memory fails — and pick the sign from the quadrant ($18^{\circ}$ is QI).
:::

## Assumptions & conventions

Triangle = non-degenerate (positive angles summing to $\pi$, positive sides satisfying triangle inequalities); $R$ circumradius, $r$ inradius, $s$ semiperimeter, $\Delta$ area; special values derived from double-angle identities as shown; toolkit status per the note at the top of this sheet.
