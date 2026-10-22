# SOURCE-AUDIT — Chapter 3: Trigonometric Identities & Equations

## Sources reviewed

- **`notes/Trigonometry/Trigonometry.md` (790 lines) — read in full** before authoring, including the six-chapter structure, all S/P worked examples, and the Appendix theory reference (sections A–I).
- `notes/Trigonometry/Trigonometry — Paper.md` and `— Solutions.md` (36-question olympiad paper) were surveyed as problem-style context; the main note is the prose source of record.
- Official JEE Advanced 2026 Mathematics syllabus (fetched earlier): Trigonometry = "Trigonometric functions. General solution of trigonometric equations. Identities." (+ inverse trig, handled in chapter 4).

## Source accuracy: overall

The source is mathematically strong and its identities, general solutions, worked examples and olympiad results were re-derived/re-computed independently (194/194 numeric checks PASS against the claims reused here). The items below are the complete list of corrections, presentation fixes and classification decisions.

## Corrections & presentation fixes

1. **Misprint not reproduced:** source S16 writes `$A+B+C=180^\unicode{00b0}$` (a `unicode` artifact instead of `^\circ`). Rendered here as $180^{\circ}$ / $\pi$ in the usual way.
2. **Internal structure inconsistency (noted, not carried over):** the source roadmap labels its Chapter 6 "Properties of triangles & the Olympiad frontier", but the chapter itself is titled "The Olympiad Identities" and triangle properties appear only in Appendix F. Our sheets are organised by concept (identities → equations → conditional identities → extensions) instead.
3. **Formula hygiene kept from the source and re-verified:** $\cos(A-B) = \cos A\cos B + \sin A\sin B$ sign convention; half-angle $\pm$ resolved from the quadrant of $\frac{A}{2}$ (source's $A = 420^{\circ}$ trap kept as motivation); "never divide by a trig factor" (source S14 $\sin 2x = \cos x$ reused with its four-solution check); the $(-1)^{n}$ general solution of sine (derived on-sheet from the two-families view).

## Classification decisions (judgments, logged as required)

1. **Triangle properties** (sine/cosine rules, $\Delta$, $R$, $r$, $\tan\frac{A}{2} = \frac{r}{s-a}$): the source treats them as core module content (Ch-6 roadmap item / Appendix F); the **official Advanced syllabus sentence does not list them**. They are placed in **Part II with an explicit "outside the current syllabus sentence" banner** (sheets OLY-04/05), together with the statement that the models remain derivable from Part I identities plus the stated rules. We do **not** claim they can never appear.
2. **$A+B+C=\pi$ identities**: the source files these under "The Olympiad Identities"; the tangent identity and $\sin 2A + \sin 2B + \sin 2C$ identity are **direct derivations of Part I compound-angle identities under one constraint**, and such conditional identities are classic Advanced-level manipulation, so they sit in Part I (sheet JEE-08) with derivations shown. The roots-of-unity products and $\sum\cot^{2}/\csc^{2}$ remain Part II.
3. **$\sin 18^{\circ}, \cos 36^{\circ}$** appear in the source appendix under Triangles; they are **pure identities** (double-angle quadratic, derived on OLY-05) and are presented as such.
4. **Series sums $\sum \sin k\theta$** (source tags OLY): kept in Part II as extensions, with the derivation shown as transformation-formula telescoping (derivable from Part I, flagged).

## Independent verification record

- `scripts/math_checks.py` — **194/194 PASS**: all six-ratio identities at random angles; allied-angle table; compound formulae and the $63/65$ and $\sin 75^{\circ}/\tan 105^{\circ}$ values; double/triple/half-angle identities and power reduction at random angles; all eight transformation formulae; general-solution families at $n = -3\ldots3$; equation worked examples ($\sin 2x = \cos x$ four roots; $\sqrt{3}\sin x + \cos x = 1$; $2\cos^{2} x + 3\sin x = 0$; squaring-filter case); conditional identities on three triangles ($\tan$ product-sum, $\sin 2A$ family, $\cos^{2}$ family, $\sin$ sum, half-angle product); $\tan 20^{\circ}\tan 40^{\circ}\tan 80^{\circ} = \sqrt{3}$ and the cubic root relations; Weierstrass conversions; $\prod \sin$ for $n = 5, 6, 7$; cosine product $= \frac{1}{8}$; $\sin 36^{\circ}\sin 72^{\circ} = \frac{\sqrt{5}}{4}$; series closed forms at $n = 3$; $\sum\cot^{2}, \sum\csc^{2}$ for $n = 3\ldots7$; $\sin 18^{\circ}, \cos 36^{\circ}$; triangle example ($a = 7$, $\Delta = 10\sqrt{3}$, $R = \frac{7}{\sqrt{3}}$, $r = \sqrt{3}$, Heron and $\tan\frac{A}{2}$ cross-checks).
- `scripts/check.py` — deliverable/render checks PASS (formula parsing, fonts, margins, ZIP/PDF integrity, gallery links).
- Visual: all 16 sheets reviewed at contact resolution; every diagram (unit circles ×2, sine/cosine comparison wave, general-solution wave with marked roots, solution number line) inspected at full resolution; label collisions found during review were fixed and re-rendered.

## Unresolved assumptions (logged)

- **Degrees vs radians:** radians are the default; degree values appear only for standard angles and the classic $18^{\circ}/20^{\circ}/36^{\circ}/40^{\circ}/80^{\circ}$ models, always converted at the boundary (stated in ASSUMPTIONS boxes).
- **Complex moduli** used only on Part II sheet 02: $e^{i\theta} = \cos\theta + i\sin\theta$, $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$, $\lvert 1 - e^{i\theta}\rvert = 2\lvert\sin\frac{\theta}{2}\rvert$ (the last proved on-sheet). Readers without chapter 5 (complex numbers) can take these as stated inputs — flagged on the sheet.
- **Weierstrass domain:** $A \ne \pi + 2k\pi$ under $t = \tan\frac{A}{2}$; the blind-spot case must be checked separately (demonstrated in the worked example).
- **Triangle toolkit status** — see classification decision 1; sheets say "outside the quoted syllabus sentence", not "never in JEE".
- **Conditional-identity degenerate cases** ($90^{\circ}$ angle breaking the tangent identity) noted on-sheet as the standard exclusion.
