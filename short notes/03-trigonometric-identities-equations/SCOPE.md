# SCOPE — Chapter 3: Trigonometric Identities & Equations

## Syllabus reading (official JEE Advanced 2026 Mathematics)

- **Trigonometry** reads exactly: *"Trigonometric functions. General solution of trigonometric equations. Identities."* — and (same unit) inverse trigonometric functions with principal values, which belong to **chapter 4** and are only forward-referenced here.
- The official list does **not** include properties of triangles or heights & distances. Triangle formulae (sine rule, cosine rule, area, in/exradii) therefore live in **Part II with an explicit classification note** — they are added theory (they encode triangle geometry), not derivable from the identities alone. Nothing here claims they "can never appear in JEE"; the sheets say plainly they sit outside the quoted syllabus sentence while remaining standard toolkit elsewhere.
- **Radian conventions** are the default throughout; degree equivalents are given for standard values.

## Classification rule used

- **Part I (JEE)** — everything under the syllabus sentence: ratios/functions and their identities (including allied angles and standard values), compound/multiple/submultiple identities and transformations (these *are* the identities), general solutions and the standard equation methods, plus **conditional identities** ($A+B+C=\pi$) which are direct derivations of the supplied identities under a stated constraint.
- **Part II (extensions)** — Weierstrass substitution, roots-of-unity products, $\sum\cot^{2}/\csc^{2}$, telescoping trig series (classic RMO/INMO algebra; every step derivable from Part I + elementary complex moduli, which is stated), and the triangle toolkit + $\sin 18^{\circ}$-family special values (added geometry theory; special values themselves are re-derived from pure identities on the sheet).

## Sheet → concept map

### Part I — `JEE/` (10 sheets)

| Sheet | Concepts |
|---|---|
| 01 | Six ratios (right-triangle + unit-circle definitions); radian/degree convention; $\sin^{2}+\cos^{2}=1$ as the unit-circle equation; reciprocal & quotient identities; the other two Pythagorean forms by division (derived); domains/undefined points; ranges |
| 02 | Quadrant signs (ASTC); allied angles with the quarter-turn rotation derivation ("odd multiples of $\frac{\pi}{2}$ swap, even multiples sign-only"); standard values table extended by symmetry; periods ($2\pi$ vs $\pi$) |
| 03 | $\sin(A\pm B)$, $\cos(A\pm B)$, $\tan(A\pm B)$ with the chord-distance derivation of $\cos(A-B)$; sign-flip trap; evaluations ($\sin 75^{\circ}$, $\tan 105^{\circ}$, $63/65$ model); $\lvert a\sin x + b\cos x\rvert \leq \sqrt{a^{2}+b^{2}}$ (first pass) |
| 04 | Double angles (3 forms of $\cos 2A$); triple angles with re-derivation; half-angle radicals with $\pm$ resolved from the quadrant of $\frac{A}{2}$; rational $\tan\frac{A}{2}$ forms; power reduction $\sin^{2}, \cos^{2}$ |
| 05 | Product→sum (4) and sum→product (4, with the one minus sign) derived from the compound pair; evaluations; factoring $\sin x + \sin 3x + \sin 5x$; purposes (solve, telescope, values) |
| 06 | Principal vs general solutions; the three master forms with the $(-1)^{n}$ derivation from the unit circle; wave diagram with marked solutions; degrees/radians consistency; counting solutions in intervals |
| 07 | Methods: factorise (never divide — worked $\sin 2x = \cos x$); harmonic form $R\sin(x+\varphi)$ with compatibility test (worked $\sqrt{3}\sin x + \cos x = 1$); polynomial-in-ratio with range clipping; squaring + ghost filtering; method chooser |
| 08 | Conditional identities $A+B+C=\pi$: tangent identity and $\sin 2A + \sin 2B + \sin 2C = 4\sin A\sin B\sin C$ derived; symmetric applications; classic $\tan 20^{\circ}\tan 40^{\circ}\tan 80^{\circ} = \sqrt{3}$ via the $\tan 3\theta$ cubic + Vieta |
| 09–10 | Chapter recap; five questions; assumptions; where the toolkit reappears; final trap sweep (incl. $\sin 2x = \sin 2y$ double-family warning) |

### Part II — `Olympiad/` (6 sheets, extensions)

| Sheet | Concepts | Status |
|---|---|---|
| 01 | Weierstrass $t = \tan\frac{A}{2}$: formulas, derivation, worked $\sin x + \cos x = 1$, the $A = \pi$ blind spot (checked), when to use vs cheaper tools | RMO/INMO-standard; derived from Part I |
| 02 | $\prod_{k=1}^{n-1}\sin\frac{k\pi}{n} = \frac{n}{2^{n-1}}$, $\prod_{k=1}^{n}\cos\frac{k\pi}{2n+1} = \frac{1}{2^{n}}$ via $z^{n}-1$ at $z = \pm 1$ and $\lvert 1 - e^{i\theta}\rvert = 2\lvert\sin\frac{\theta}{2}\rvert$; Vieta pattern for tangent products | olympiad algebra; needs elementary complex moduli (stated) |
| 03 | Telescoping $\sum \sin k\theta$, $\sum \cos k\theta$ via the $2\sin\frac{\theta}{2}$ multiplier; $\sum\cot^{2} = \frac{(n-1)(n-2)}{3}$, $\sum\csc^{2} = \frac{n^{2}-1}{3}$ via polynomial roots + Vieta | olympiad algebra; derived from transformations |
| 04–05 | Triangle toolkit: sine rule, cosine rule, $\Delta = \frac{1}{2}bc\sin A$ and Heron, $r = \frac{\Delta}{s}$, $\tan\frac{A}{2} = \frac{r}{s-a}$; derived special values $\sin 18^{\circ}, \cos 36^{\circ}$; worked triangle with $R$, $r$ cross-checks | **outside the current Advanced syllabus sentence** (labelled on-sheet); standard toolkit elsewhere |

## Prerequisites assumed

Chapter 1 (functions, domains) and chapter 2 (exponents/logarithms where magnitudes are compared); elementary right-triangle trig from school; complex numbers appear **only** on Part II sheet 02 in the minimal form $e^{i\theta} = \cos\theta + i\sin\theta$, $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$ (stated as assumptions there).

## Out of scope here

Inverse trigonometric functions (chapter 4 — principal values are NOT mixed into these sheets); properties of triangles in full depth (kept as a compact toolkit only, per classification above); heights & distances; calculus-based curve analysis of trig functions (chapters 17–19).
