---
id: jee-08
part: jee
title: "Conditional Identities — When $A + B + C = \pi$"
---

## The model: one constraint, many identities

If $A + B + C = \pi$ (angles of a triangle, or any three reals summing to $\pi$), then $C = \pi - (A + B)$, so $\sin C = \sin(A + B)$, $\cos C = -\cos(A + B)$, $\tan C = -\tan(A + B)$. Substituting the compound formulae collapses symmetric expressions. **This is derived from Part I machinery — no new theory, just the constraint exploited.**

| Identity (given $A + B + C = \pi$) | Form |
|---|---|
| Tangents | $\tan A + \tan B + \tan C = \tan A \tan B \tan C$ |
| Sine double angles | $\sin 2A + \sin 2B + \sin 2C = 4 \sin A \sin B \sin C$ |
| Cosines squared | $\cos^{2} A + \cos^{2} B + \cos^{2} C + 2 \cos A \cos B \cos C = 1$ |
| Sines | $\sin A + \sin B + \sin C = 4 \cos\dfrac{A}{2} \cos\dfrac{B}{2} \cos\dfrac{C}{2}$ |
| Half-angle tangents | $\tan\dfrac{A}{2} \tan\dfrac{B}{2} + \tan\dfrac{B}{2} \tan\dfrac{C}{2} + \tan\dfrac{C}{2} \tan\dfrac{A}{2} = 1$ |

:::derive title="Derive the tangent identity (the exam workhorse)"
$\tan(A + B) = \tan(\pi - C) = -\tan C$, and $\tan(A+B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$. So $\tan A + \tan B = -\tan C \,(1 - \tan A \tan B)$, i.e. $\tan A + \tan B + \tan C = \tan A \tan B \tan C$ ✓. (Fails exactly when some $\cos$ vanishes — a $90^{\circ}$ angle — then read the identity in the limit or in the cotangent form.)
:::

:::derive title="Derive $\sin 2A + \sin 2B + \sin 2C = 4 \sin A \sin B \sin C$ (model derivation)"
$\sin 2A + \sin 2B = 2 \sin(A+B) \cos(A-B)$ and $\sin 2C = \sin(2\pi - 2(A+B)) = -\sin 2(A+B) = -2 \sin(A+B)\cos(A+B)$. Sum: $2 \sin(A+B)[\cos(A-B) - \cos(A+B)] = 2 \sin(A+B) \cdot 2 \sin A \sin B = 4 \sin A \sin B \sin C$ (using $\sin(A+B) = \sin C$ and the sum-to-product identity from sheet 5) ✓. Numeric check $(60^{\circ}, 60^{\circ}, 60^{\circ})$: LHS $= 3 \sin 120^{\circ} = 2.598$ = RHS $= 4 (\frac{\sqrt{3}}{2})^{3} = 2.598$ ✓; $(30^{\circ}, 60^{\circ}, 90^{\circ})$: both $1.732$ ✓.
:::

## Applications

**Symmetric tangent expressions.** If $A, B, C$ are angles of a triangle and $\tan A = 1$, $\tan B = 2$, then $\tan C = -\tan(A+B) = -\frac{1 + 2}{1 - 2} = 3$; check the identity: $1 + 2 + 3 = 6 = 1 \cdot 2 \cdot 3$ ✓.

:::example title="Worked (classic). Evaluate $\tan 20^{\circ} \tan 40^{\circ} \tan 80^{\circ}$"
Use $\tan 3\theta = \frac{3t - t^{3}}{1 - 3t^{2}}$ at $\theta = 20^{\circ}$ where $\tan 60^{\circ} = \sqrt{3}$: $t = \tan 20^{\circ}$ satisfies $t^{3} - 3\sqrt{3}\, t^{2} - 3t + \sqrt{3} = 0$. The roots are $\tan 20^{\circ}, \tan 80^{\circ}, \tan 140^{\circ} = -\tan 40^{\circ}$ (adding $60^{\circ}, 120^{\circ}$ preserves $\tan 3\theta$). Product of roots $= -\sqrt{3}$, so $\tan 20^{\circ} \tan 80^{\circ} (-\tan 40^{\circ}) = -\sqrt{3} \Rightarrow \tan 20^{\circ} \tan 40^{\circ} \tan 80^{\circ} = \sqrt{3} \approx 1.7321$ ✓ (direct: $0.36397 \times 0.83910 \times 5.67128 = 1.7321$).
:::

:::key
**When to use conditional identities.** Spot the hidden constraint: "angles of a triangle", $A + B + C = \pi$ (or $= 180^{\circ}$, $= 2\pi - $ something), or complementary/linked angles like $A + B = \frac{\pi}{2}$. Then substitute the constraint into one angle and let the identity do the algebra. For products like $\tan 20 \tan 40 \tan 80$ the **triple-angle polynomial** (roots-of-Vieta) is the standard second tool — Part II generalises it to roots-of-unity products.
:::

:::warn title="Traps — conditional identities"
- The identity $\tan A + \tan B + \tan C = \tan A \tan B \tan C$ needs all tangents defined; a right angle breaks it (one side undefined).
- Degrees vs radians inside one identity — convert before substituting ($180^{\circ} = \pi$).
- The constraint must actually hold: "$A, B, C$ are three angles" without "of a triangle" does **not** give $A + B + C = \pi$.
- Vieta on the triple-angle cubic gives $\sum$ of roots $= 3\sqrt{3}$ and product $= -\sqrt{3}$; track the sign flip from $\tan 140^{\circ} = -\tan 40^{\circ}$ carefully — it is where errors creep in.
:::
