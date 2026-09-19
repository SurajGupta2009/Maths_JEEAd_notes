# Chapter 6 — Synthesis

*5 sections · 5 questions*

*Chapter 6 of 6*

# Synthesis & Stretch

The problems where the whole module has to work at once. Four themes: *configurations on the unit circle* (where the condition $|z| = 1$ plus a symmetric relation forces a specific shape), *product identities* from the factorization $z^n - 1$, the two-vertex transformation $w = z + 1/z$ (circles becoming line segments), and distance theorems (British Flag) that are one-line computations once you know $\lvert z-a\rvert^2 = (z-a)(\bar z - \bar a)$. After this chapter: the 38-question paper.

### 6.1 Unit-circle configurations — four unit numbers summing to zero

#### **P47**[Olympiad][unit-circle config]Let [formula] be complex numbers with [formula] for all [formula] and [formula…

Let $z_1, z_2, z_3, z_4$ be complex numbers with $|z_k| = 1$ for all $k$ and $z_1 + z_2 + z_3 + z_4 = 0$. Prove that they are the vertices of a rectangle (in some order). When is it a square?

<details>
<summary>Answer + Reasoning</summary>

**Step 1 — split into a conjugate pair or an antipodal pair.** From the sum, $z_1 + z_2 = -(z_3 + z_4)$. Conjugate the equation and use $\bar z_k = 1/z_k$ (valid since $|z_k| = 1$): 
$$ \frac{1}{z_1} + \frac{1}{z_2} = -\left(\frac{1}{z_3} + \frac{1}{z_4}\right)
        \iff \frac{z_1 + z_2}{z_1 z_2} = \frac{z_1 + z_2}{z_3 z_4}, $$
 where the right-hand side used $z_3+z_4 = -(z_1+z_2)$. Hence 
$$ (z_1 + z_2)\left(\frac{1}{z_1 z_2} - \frac{1}{z_3 z_4}\right) = 0. $$
 So either **(i)** $z_1 + z_2 = 0$ (an antipodal pair), or **(ii)** $z_1 z_2 = z_3 z_4$.


**Case (i).** $z_2 = -z_1$; the sum then forces $z_4 = -z_3$. The four points are $\{\pm a, \pm b\}$ on the unit circle — read in the cyclic order around the circle they form a parallelogram inscribed in the circle, hence a rectangle (a parallelogram has equal opposite angles; a cyclic quadrilateral has supplementary opposite angles; both together force $90^\circ$).


**Case (ii).** Let $s = z_1 + z_2$, so $z_3 + z_4 = -s$, and let $p = z_1 z_2 = z_3 z_4$. Then $z_1, z_2$ are the roots of $t^2 - s t + p = 0$ and $z_3, z_4$ the roots of $t^2 + s t + p = 0$, whose roots are *precisely the negatives* of the first pair's roots. So $\{z_3, z_4\} = \{-z_1, -z_2\}$ — the same shape as Case (i): a rectangle. ∎


**Square, exactly when:** in the cyclic ordering the adjacent vertices are $90^\circ$ apart, i.e. $z_2 = \pm i\, z_1$. (Equivalently, the two antipodal pairs differ by a quarter-turn: $b = i a$ after naming.)


The whole proof hinged on one move — conjugating a unit-modulus relation to replace $\bar z$ by $1/z$. That move converts "on the circle" into "algebraic," and it is the standard entry point for every unit-circle configuration problem.

</details>


### 6.2 Product identities from $z^n - 1 = \prod (z - \zeta_k)$

> **📦 $\displaystyle\prod_{k=0}^{n-1} \lvert z - e^{2\pi i k/n}\rvert = \lvert z^n - 1\rvert$**
>
> **Proof.** Factor $z^n - 1$ over its roots $\zeta_k = e^{2\pi i k/n}$: $z^n - 1 = \prod_{k=0}^{n-1}(z - \zeta_k)$. Take moduli. One line. This is the distance version of Ch 3's product formula — there we pinned $z = 1$ (getting $n$), here $z$ is free.

#### **P48**[JEE Advanced][product identity]Let [formula] be the vertices of a regular pentagon on the unit circle. Find t…

Let $v_0, \dots, v_4$ be the vertices of a regular pentagon on the unit circle. Find the product of the distances from the point $2$ (on the real axis) to the five vertices.

<details>
<summary>Answer + Reasoning</summary>

By the identity with $n = 5, z = 2$: 
$$ \prod_{k=0}^{4} |2 - e^{2\pi i k/5}| = |2^5 - 1| = 31. $$
 No trigonometry, no law of cosines, no pairing of symmetric factors — the factorization does all the work. (Numerical sense-check, via $|2 - e^{2\pi i k/5}|^2 = 5 - 4\cos\frac{2\pi k}{5}$: the distances are $1,\ \sqrt{3.764},\ \sqrt{8.236},\ \sqrt{8.236},\ \sqrt{3.764}$ — product $1 \cdot 3.764 \cdot 8.236 = 31$ ✓.)


Answer: $31$

</details>

**Corollary worth memorizing.** Put $z = e^{i\theta}$ (also on the unit circle): $\prod_{k=0}^{n-1}\lvert e^{i\theta} - e^{2\pi i k/n}\rvert
    = \lvert e^{in\theta} - 1\rvert = 2\left|\sin\frac{n\theta}{2}\right|$ — a clean product of $n$ chords. At $\theta = 0$ it degenerates to Ch 3's $\prod_{k=1}^{n-1}
    2\sin\frac{\pi k}{n} = n$. The same identity, two specializations.


### 6.3 The map $w = z + \dfrac{1}{z}$ — circles become line segments

On the unit circle, $\frac{1}{z} = \bar z$, so $w = z + \bar z = 2\operatorname{Re} z
    = 2\cos\theta$ is *real*, running over $[-2, 2]$ as $\theta$ runs over $[0, 2\pi)$. The map $z \mapsto z + 1/z$ (the *Joukowski map* — the name matters less than the behavior) **collapses the unit circle onto the real segment $[-2, 2]$**, two-to-one except at $\pm 1$. Any affine image of the circle behaves the same, up to translation and rotation in the $w$-plane.

#### **P49**[JEE Advanced][w = z + 1/z]As [formula] varies, find the locus of [formula] .

As $|z| = 1$ varies, find the locus of $w = z + \dfrac{1}{z} + i$.

<details>
<summary>Answer + Reasoning</summary>

$z + 1/z = 2\cos\theta \in [-2, 2]$ (real), so $w = 2\cos\theta + i$: the horizontal line segment from $-2 + i$ to $2 + i$, traced twice as $\theta$ goes around (except at the endpoints, each hit once). Conversely every point of the segment is hit (take $\cos\theta = (x)/2$).


Answer: the segment $[{-2+i},\ 2+i]$

</details>


### 6.4 Three unit numbers summing to zero — the $120^\circ$ configuration

The three-point analogue of 6.1. If $|z_k| = 1$ and $z_1 + z_2 + z_3 = 0$, then $|z_1 + z_2| = |z_3| = 1$, so 
$$ 1 = |z_1 + z_2|^2 = 2 + 2\operatorname{Re}(z_1 \bar z_2)
    \iff \operatorname{Re}(z_1 \bar z_2) = -\frac12
    \iff \angle(z_1, z_2) = 120^\circ. $$
 By symmetry all three pairwise angles are $120^\circ$: the points are the vertices of an equilateral triangle centered at the origin — and $\{\pm z_1, \pm z_2, \pm z_3\}$ is a **regular hexagon** (antipodal points fill in the missing $60^\circ$ steps).

#### **P50**[Olympiad][$120^\circ$ config]Let [formula] satisfy [formula] and [formula] . Show that [formula] are [formu…

Let $z_1, z_2, z_3$ satisfy $|z_k| = 1$ and $z_1 + z_2 + z_3 = 0$. Show that $z_1, z_2, z_3$ are $120^\circ$ apart, and that $\{\pm z_1, \pm z_2, \pm z_3\}$ are the vertices of a regular hexagon.

<details>
<summary>Answer + Reasoning</summary>

The computation is the paragraph above. For the hexagon: the six points have arguments $\{\theta_k, \theta_k + \pi\}$, and the $\theta_k$ are mutually $120^\circ$ apart, so the sorted arguments are $\alpha, \alpha + 60^\circ, \alpha + 120^\circ, \alpha + 180^\circ, \alpha + 240^\circ,
        \alpha + 300^\circ$ — exactly $60^\circ$ steps on the unit circle: a regular hexagon. ∎ (Check the $60^\circ$: between $\theta_1$ and $\theta_2 = \theta_1
        + 120^\circ$ lies the antipode $-z_1$ at $\theta_1 + 180^\circ$… and $\theta_1 + 180^\circ = \theta_2 - 60^\circ$ ✓ — each antipode lands exactly halfway, at $60^\circ$ from its neighbors.)


Answer: $120^\circ$ apart; $\{\pm z_k\}$ is a regular hexagon ∎

</details>

z₁ z₂ z₃ −z₁ −z₂ −z₃ O $z_1, z_2, z_3$ (teal) summing to zero on the unit circle are $120^\circ$ apart; their antipodes (orange) complete the regular hexagon.


### 6.5 British Flag — distance theorems as one-line algebra

**British Flag theorem (geometry).** For any point $e$ in the plane of a rectangle with vertices $A, B, C, D$: $|e-A|^2 + |e-C|^2 = |e-B|^2 + |e-D|^2$ (diagonal pairs of vertices). For a square $0, 1, 1+i, i$ and any $e$ — *anywhere in the plane, no restriction* — it reads $|e|^2 + |e-(1+i)|^2 = |e-1|^2 + |e-i|^2$. The complex proof is one expansion:

#### **P51**[Olympiad][British Flag]Prove the British Flag theorem for the square [formula] using [formula] .

Prove the British Flag theorem for the square $0, 1, 1+i, i$ using $\lvert z-a\rvert^2 = (z-a)(\bar z - \bar a)$.

<details>
<summary>Answer + Reasoning</summary>

Expand both sides with $\lvert z-a\rvert^2 = |z|^2 - z\bar a - \bar z a + |a|^2$. For $a = 1+i$: $|e-(1+i)|^2 = |e|^2 - e(1-i) - \bar e(1+i) + 2 = |e|^2 - e + ie
        - \bar e - i\bar e + 2$. For $a = 1$: $|e-1|^2 = |e|^2 - e - \bar e + 1$. For $a = i$: $|e-i|^2 = |e|^2 + ie - i\bar e + 1$. Hence 
$$ \text{LHS} = |e|^2 + |e-(1+i)|^2 = 2|e|^2 - e + ie - \bar e - i\bar e + 2, $$
 
$$ \text{RHS} = |e-1|^2 + |e-i|^2 = 2|e|^2 - e + ie - \bar e - i\bar e + 2. $$
 Identical term for term — the cross terms $-e + ie - \bar e - i\bar e$ from the far corner $(1+i)$ are exactly reproduced by the sum of the two near corners $1$ and $i$. Done, for *every* $e$ in the plane. ∎


The pattern: $\lvert z-a\rvert^2$ is *quadratic in $z, \bar z$ with no $z\bar z$ issue* — always expand it as $(z-a)(\bar z-\bar a)$, and distance theorems about rectangles and squares become "collect like terms." (The rectangle generalization: vertices $0, w, w + i\ell\ldots$ — same expansion, same cancellation, because the four vertex constants pair up: $0 + (w+v) = w + v$.)

</details>

> **✅ Chapter checklist — the whole module, compressed**
>
> - **Algebra (Ch 1):** $\mathbb{C}$ as a field, conjugation, division, $|zw| = |z||w|$, rotation by $i$.
> - **Polar (Ch 2):** argument is multi-valued; products add angles; De Moivre; $n$ roots form a regular $n$-gon; square-root formula; Euler.
> - **Roots of unity (Ch 3):** the five $\omega$-identities; vanishing sums; $\prod(1-\zeta_k) = n$; the sine product; the residue-class filter.
> - **Loc & optimization (Ch 4):** $z, \bar z$ systems; circles from modulus, arcs from argument; $\min|z-a| = ||a|-1|$ on $|z| = 1$; ellipses; region ranges.
> - **Geometry (Ch 5):** rotation $= A + e^{i\theta}(X-A)$; equilateral $a + \omega b + \omega^2 c = 0$; Ptolemy from an identity; Van Aubel; Napoleon; centroid sums; area; circumcenter as linear algebra.
> - **Synthesis (Ch 6):** unit-circle configurations (rectangle, hexagon) via $\bar z = 1/z$; $\prod|z-\zeta_k| = |z^n - 1|$; the Joukowski collapse $z + 1/z \to [-2,2]$; distance theorems by expansion.

> **🎯 Next — the 38-question Olympiad paper**
>
> Everything above, tested at once: eight sections, JEE Main → JEE Advanced → Olympiad, covering every chapter's signature move. Full worked solutions follow in the companion file. Do it cold, on paper, before opening the solutions — the paper is built so that each section's questions get harder within the section, and the stretch questions (37–38) require chaining three or four techniques.



---

