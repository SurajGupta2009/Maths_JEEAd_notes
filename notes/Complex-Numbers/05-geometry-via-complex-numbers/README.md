# Chapter 5 — Geometry via Complex Numbers

*6 sections · 6 questions*

*Chapter 5 of 6*

# Geometry via Complex Numbers

Chapters 1–4 worked with one $z$. This chapter works with *several* complex numbers as vertices of a polygon, and turns classical geometry — equilateral triangles, Ptolemy, Van Aubel, Napoleon — into a few lines of algebra in $\mathbb{C}$. The engine is one idea: **rotation is multiplication by $e^{i\theta}$** (Ch 1, §1.4). Once you can write "rotate $X$ by $\theta$ about $A$" as $A + e^{i\theta}(X - A)$, the theorems almost prove themselves.

### 5.1 The engine: rotation, and the equilateral-triangle condition

> **📦 Rotation by $\theta$ about $A$**
>
> The point $X$ rotated through angle $\theta$ (counterclockwise) about the point $A$ is 
> $$ X' = A + e^{i\theta}(X - A). $$
>  Proof is one line: $X - A$ is the vector from $A$ to $X$; multiplying by $e^{i\theta}$ keeps its length and adds $\theta$ to its direction; adding $A$ re-anchors it. For $\theta = \pi/3$, $e^{i\pi/3} = 1 + \omega$ (Ch 3, identity iv), and for $\theta = -\pi/3$, $e^{-i\pi/3} = -\omega$ (and also $e^{-i\pi/3} =
>       \overline{e^{i\pi/3}}$).

#### **P41**[JEE Advanced][equilateral]Let [formula] be complex numbers and [formula] a non-real cube root of unity. …

Let $a, b, c$ be complex numbers and $\omega$ a non-real cube root of unity. Prove: the triangle $(a,b,c)$ is equilateral (with vertices in counterclockwise order) $\iff a + \omega b + \omega^2 c = 0$.

<details>
<summary>Answer + Reasoning</summary>

**($\Rightarrow$)** Equilateral, CCW: the side $c - a$ is the side $b - a$ rotated by $+60^\circ$ about $a$: 
$$ c - a = e^{i\pi/3}(b - a) = (1+\omega)(b-a) = (1+\omega)b - (1+\omega)a. $$
 Then $c = a - (1+\omega)a + (1+\omega)b = -\omega a + (1+\omega)b$. Now compute: 
$$ a + \omega b + \omega^2 c = a + \omega b + \omega^2\big(-\omega a + (1+\omega)b\big)
        = a + \omega b - \omega^3 a + (\omega^2 + \omega^3) b. $$
 With $\omega^3 = 1$ and $\omega^2 + 1 = -\omega$: $= a + \omega b - a - \omega b = 0$ ✓.


**($\Leftarrow$)** Suppose $a + \omega b + \omega^2 c = 0$. Then $c = -\omega^{-2}(a + \omega b) = -\omega(a + \omega b) = -\omega a - \omega^2 b$ (using $\omega^{-2} = \omega$). So 
$$ c - a = -\omega a - \omega^2 b - a = -(1+\omega)a - \omega^2 b. $$
 We claim $c - a = (1+\omega)(b - a)$: expand the RHS: $(1+\omega)b - (1+\omega)a
        = (1+\omega)b - a - \omega a$. Compare with $c - a = -a - \omega a - \omega^2 b$: equal iff $(1+\omega)b = -\omega^2 b$, i.e. $1 + \omega + \omega^2 = 0$ ✓. Hence $c - a = (1+\omega)(b-a) = e^{i\pi/3}(b-a)$: $|c-a| = |b-a|$ and the rotation is exactly $60^\circ$, so the triangle is equilateral with the CCW ordering. ∎


Check on the standard example: $a = 0, b = 1, c = e^{i\pi/3}$ (equilateral, CCW): $a + \omega b + \omega^2 c = \omega + \omega^2 e^{i\pi/3}
        = \omega + \omega^2(-\omega^2) = \omega - \omega^4 = \omega - \omega = 0$ ✓.

</details>

The condition $a + \omega b + \omega^2 c = 0$ is *orientation-sensitive*: for the same triangle read clockwise it reads $a + \omega^2 b + \omega c = 0$. JEE questions usually ask you to *use* the condition (given the triangle is equilateral, prove some relation) rather than verify orientation — but if a problem states "equilateral" without ordering, the two conditions differ only by conjugating $\omega \leftrightarrow
    \omega^2$, and most real-valued conclusions are unaffected.


### 5.2 Ptolemy's theorem — a one-line identity plus the triangle inequality

**Ptolemy (geometry statement).** *Inequality:* for any four points $a, b, c, d$ (in that order), the product of the diagonals is bounded by the sum of the products of opposite sides: $|a-c|\,|b-d| \le |a-b|\,|c-d| + |b-c|\,|a-d|$. *Theorem:* if the four points lie on one circle in cyclic order $a, b, c, d$, then **equality** holds — the familiar product-of-diagonals formula. The secret: the engine underneath is *pure algebra in $\mathbb{C}$, valid for every four points, no circle anywhere*.

> **📦 The Ptolemy identity (verify it yourself — it is 30 seconds)**
>
> For all complex $a, b, c, d$: 
> $$ (a-c)(b-d) = (a-b)(c-d) + (b-c)(a-d). $$
>  Expand the right: $(ac - ad - bc + bd) + (ab - bd - ca + cd) = ab - ad - bc + cd$, which is exactly $(a-c)(b-d)$. Done. No geometry used at all.

**Now the geometry, in one move.** Take moduli in the identity: 
$$ |a-c|\,|b-d| = \big|(a-b)(c-d) + (b-c)(a-d)\big|
    \le |a-b|\,|c-d| + |b-c|\,|a-d|, $$
 by the triangle inequality — that is Ptolemy's *inequality*, for any four points. Equality in the triangle inequality holds iff the two complex numbers $(a-b)(c-d)$ and $(b-c)(a-d)$ point in the *same direction* — one is a *positive real* multiple of the other, i.e. their ratio lies in $\mathbb{R}_{>0}$: 
$$ \frac{(b-c)(a-d)}{(a-b)(c-d)} \in \mathbb{R}_{>0}. $$
 Take arguments in the ratio. Writing $\varphi(X; Y, Z) = \arg(Y-X) - \arg(Z-X)$ (the signed angle at vertex $X$ between the rays to $Y$ and $Z$), and using $\arg(b-c) = \arg(c-b) + \pi$: 
$$ \arg\frac{(b-c)(a-d)}{(a-b)(c-d)} = \pi + \big[\varphi(a; d, b) - \varphi(c; d, b)\big] \pmod{2\pi}. $$
 The ratio is *real and positive* (argument $0 \bmod 2\pi$) exactly when $\varphi(a; d, b) - \varphi(c; d, b) \equiv \pi \pmod{2\pi}$: the angles that the chord $bd$ subtends at $a$ and at $c$ are **supplementary** (the signed version: $a$ and $c$ sit on opposite arcs, difference $\pi$). Opposite angles supplementary $\iff$ the four points lie on one circle (or line), in the order $a, b, c, d$ — the inscribed-angle theorem of Ch 4, §4.4, in complex clothing. Hence equality in Ptolemy holds precisely for cyclic quadrilaterals: **Ptolemy's theorem**. (Square check: the ratio was exactly $1$ — real and positive — as it must be.)

#### **P42**[JEE Advanced][Ptolemy]Prove Ptolemy's theorem for a cyclic quadrilateral using the identity above. C…

Prove Ptolemy's theorem for a cyclic quadrilateral using the identity above. Check the formula on the unit square.

<details>
<summary>Answer + Reasoning</summary>

The proof is the two paragraphs above: identity → moduli → triangle inequality for the inequality; equality condition (same direction) ⟺ cyclic + cyclic order, for the theorem. **Unit-square check** ($a=1, b=i, c=-1, d=-i$, cyclic): diagonals $|a-c| = 2$, $|b-d| = 2$, product $4$; sides all $|1 - i|
        = \sqrt2$, so $|a-b||c-d| + |b-c||a-d| = \sqrt2\cdot\sqrt2 + \sqrt2\cdot\sqrt2 = 2 + 2
        = 4$ ✓. Equality, as it must be for a cyclic quadrilateral.


Answer: proven; square check $4 = 4$ ✓

</details>


### 5.3 Van Aubel — squares on the sides of a quadrilateral

**Van Aubel (geometry statement).** On the four sides of any quadrilateral, construct squares outward. The segments joining the centers of *opposite* squares are **equal in length and perpendicular**.

> **📦 Outward-square center formula**
>
> For a **counterclockwise** quadrilateral, the interior lies to the *left* of each directed side $p \to q$, so the outward square on side $pq$ has center 
> $$ m_{pq} = \frac{p+q}{2} - \frac{i}{2}(q-p) = \frac{(1+i)p + (1-i)q}{2}. $$
>  (The center of *any* square on base $pq$ is $\tfrac{p+q}{2} \pm \tfrac{i}{2}(q-p)$: midpoint plus the half-side rotated by $\pm 90^\circ$; the sign picks the side.)

#### **P43**[Olympiad][Van Aubel]Prove Van Aubel's theorem using the center formula.

Prove Van Aubel's theorem using the center formula.

<details>
<summary>Answer + Reasoning</summary>

Let the CCW quadrilateral be $a, b, c, d$, and $m_{pq}$ the outward-square center on side $pq$. Compare the two opposite-center segments: 
$$ 2(m_{bc} - m_{da}) = \big((1+i)b + (1-i)c\big) - \big((1+i)d + (1-i)a\big), $$
 
$$ 2(m_{cd} - m_{ab}) = \big((1+i)c + (1-i)d\big) - \big((1+i)a + (1-i)b\big). $$
 Now multiply the second expression by $i$ and collect: 
$$ i\cdot 2(m_{cd} - m_{ab}) = i(1+i)c + i(1-i)d - i(1+i)a - i(1-i)b $$
 
$$ = (i-1)c + (1+i)d - (i+1)a + (1+i)b = -(1-i)c + (1+i)d + (1-i)a - (1+i)b. $$
 That is precisely the *negative* of $2(m_{bc} - m_{da})$. Therefore 
$$ m_{bc} - m_{da} = -\,i\,(m_{cd} - m_{ab}). $$
 One complex equation, two geometric facts: multiplication by $-i$ rotates by $90^\circ$ and preserves length — so the segments are **perpendicular and equal**. ∎ (Numerical check, quad $0, 1, 1.5+1.2i, 0.3+0.9i$: both segments have length $2.16448\ldots$ and the ratio of one to the other is pure imaginary ✓.)


Answer: $m_{bc} - m_{da} = -i(m_{cd} - m_{ab})$ — equal + perpendicular ∎

</details>


### 5.4 Napoleon — equilateral triangles on the sides of a triangle

**Napoleon's theorem (geometry statement).** On the three sides of any triangle, construct equilateral triangles outward. The centers of those three triangles themselves form an **equilateral triangle** (the "outer Napoleon triangle").

> **📦 Outward-equilateral center formula**
>
> For a CCW triangle $a, b, c$, the outward equilateral triangle on side $a \to b$ has third vertex $a + e^{-i\pi/3}(b-a) = a - \omega(b-a)$ (rotate the side by $-60^\circ$, the right-hand side), so its center is 
> $$ m_{ab} = \frac{a + b + \big(a - \omega(b-a)\big)}{3}
>       = \frac{(2+\omega)a + (1-\omega)b}{3}. $$
>  (Use $e^{-i\pi/3} = -\omega$, and check $1 - \omega^2 = 2 + \omega$ — they are the same number, since $1+\omega+\omega^2 = 0$.)

#### **P44**[Olympiad][Napoleon]Prove Napoleon's theorem using the equilateral condition from P41.

Prove Napoleon's theorem using the equilateral condition from P41.

<details>
<summary>Answer + Reasoning</summary>

By P41, three points $X, Y, Z$ form a CCW equilateral triangle iff $X + \omega Y + \omega^2 Z = 0$. Set $X = m_{ab}$, $Y = m_{bc}$, $Z = m_{ca}$ and compute $3\big(m_{ab} + \omega m_{bc} + \omega^2 m_{ca}\big)$: 
$$ \big((2+\omega)a + (1-\omega)b\big) + \omega\big((2+\omega)b + (1-\omega)c\big)
        + \omega^2\big((2+\omega)c + (1-\omega)a\big). $$
 Collect the $a$-coefficient: $(2+\omega) + \omega^2(1-\omega) = 2 + \omega + \omega^2 - \omega^3
        = 1 + \omega + \omega^2 = 0$ (using $\omega^3 = 1$). The $b$-coefficient: $(1-\omega) + \omega(2+\omega) = 1 - \omega + 2\omega + \omega^2 = 1 + \omega + \omega^2 = 0$. The $c$-coefficient: $\omega(1-\omega) + \omega^2(2+\omega) = \omega - \omega^2 + 2\omega^2 + \omega^3
        = 1 + \omega + \omega^2 = 0$. Every coefficient is $1 + \omega + \omega^2$: 
$$ m_{ab} + \omega m_{bc} + \omega^2 m_{ca} = 0 \ \Longrightarrow \ \text{the centers form an equilateral triangle. ∎} $$
 **Numerical check**, triangle $(0,0), (4,0), (1,3)$: the outward centers are $(2, -1.1547)$, $(3.366, 2.366)$, $(-0.366, 1.789)$, and the Napoleon triangle's sides are $\sqrt{14.261}$ each — equal, as required. (Note the proof is one computation; the heavy lifting was done twice — once in P41, once here — which is why the theorems are taught in this order.)


Answer: $m_{ab} + \omega m_{bc} + \omega^2 m_{ca} = 0$ — centers equilateral ∎

</details>

a b c m_ab m_bc m_ca Napoleon on the scalene triangle $(0,0), (4,0), (1,3)$: three outward equilateral triangles (teal), and their centers (orange) form the Napoleon triangle — visibly equilateral (sides $\sqrt{14.261}$ each, verified numerically).


### 5.5 Distance sums — the centroid formula (Leibniz)

> **📦 For points $v_1, \dots, v_n$ with centroid $c = \frac1n\sum v_k$, and any point $p$: $\displaystyle\sum_{k=1}^n |p - v_k|^2 = n\,|p - c|^2 + \sum_{k=1}^n |v_k - c|^2$**
>
> **Proof.** Write $p - v_k = (p - c) - (v_k - c)$ and expand: 
> $$ \sum |p-v_k|^2 = \sum \big|(p-c) - (v_k-c)\big|^2
>       = n|p-c|^2 + \sum |v_k-c|^2 - 2\operatorname{Re}\Big((p-c)\overline{\sum(v_k - c)}\Big). $$
>  The cross term vanishes because $\sum(v_k - c) = \sum v_k - n c = 0$. Two lines. The second term is fixed (the "inertia" of the configuration); the first is minimized at $p = c$ — which is why the centroid is the point of minimum total squared distance. That sentence is the theorem's real content.

#### **P45**[JEE Advanced][distance sum]Let [formula] be the vertices of a regular hexagon of circumradius [formula] c…

Let $v_1, \dots, v_6$ be the vertices of a regular hexagon of circumradius $2$ centered at $O$. If $P$ is a point with $|P - O| = 1$, find $\sum_{k=1}^{6} |P - v_k|^2$.

<details>
<summary>Answer + Reasoning</summary>

Centroid $c = O$ (symmetry), $\sum|v_k - O|^2 = 6 \cdot 2^2 = 24$, and $n|p - c|^2 = 6 \cdot 1^2 = 6$. Hence the sum $= 6 + 24 = 30$ — *independent of where* $P$ sits on the circle of radius $1$. (The formula even gives the same value for $P = O$: $0 + 24$… no — for $P = O$: $6\cdot 0 + 24 = 24$; the $30$ uses $|P-O| = 1$. The independence is in the *direction* of $P$, not its distance from $O$.)


Answer: $30$

</details>


### 5.6 Area, circumcenter — the remaining classics

> **📦 Area of triangle $(z_1, z_2, z_3)$**
>
> $$ \text{Area} = \frac12 \left|\operatorname{Im}\Big((z_2 - z_1)\,\overline{(z_3 - z_1)}\Big)\right|. $$
>  Reason: $(z_2-z_1)\overline{(z_3-z_1)}$ is the product of two vectors sharing the vertex $z_1$; its modulus is $|z_2-z_1|\,|z_3-z_1|$ and its argument is the (signed) angle between them, so its imaginary part is $|z_2-z_1|\,|z_3-z_1|\sin(\text{signed angle})$ — the cross product of the two sides. Half of its absolute value is the area. (This is the shoelace formula in complex clothing.)

> **📦 Circumcenter as a 2×2 solve**
>
> The circumcenter $u$ satisfies $|u-a|^2 = |u-b|^2 = |u-c|^2$. Expanding one: 
> $$ u\bar u - u\bar a - \bar u a = u\bar u - u\bar b - \bar u b
>       \iff u(\bar b - \bar a) + \bar u (b - a) = \bar b\, b - \bar a\, a. $$
>  Two such equations (one for each of $b, c$) are linear in the two unknowns $u, \bar u$ — solve the 2×2. No coordinate geometry, no perpendicular bisectors drawn.

#### **P46**[JEE Main][area + circumcenter](a) Find the area of the triangle with vertices [formula] , [formula] , [formu…

(a) Find the area of the triangle with vertices $1$, $3i$, $-2+2i$. (b) Find the circumcenter of the triangle with vertices $1, i, -1$.

<details>
<summary>Answer + Reasoning</summary>

(a) $z_2 - z_1 = -1 + 3i$, $z_3 - z_1 = -3 + 2i$, $(z_2-z_1)\overline{(z_3-z_1)} = (-1+3i)(-3-2i) = 3 + 2i - 9i - 6i^2 = 9 - 7i$. Area $= \tfrac12 |{-7}| = \tfrac72$. (Shoelace check: $\tfrac12|1(3-2) + 0(2-0)
        + (-2)(0-3)| = \tfrac12 \cdot 7$ ✓.)


(b) The points $1, i, -1$ all lie on the unit circle — the circumcenter is $0$. The linear method confirms it: with $a = 1, b = i, c = -1$, the first equation $u(\bar b - \bar a) + \bar u(b - a) = |b|^2 - |a|^2 = 0$ becomes $u(-i - 1) + \bar u(i - 1) = 0$, which $u = 0$ satisfies (and uniqueness of the circumcenter of a non-degenerate triangle makes $0$ the answer).


Answer: (a) $\dfrac72$; (b) $0$

</details>

> **✅ Chapter checklist**
>
> - Rotation formula $X' = A + e^{i\theta}(X-A)$ — the engine of the whole chapter.
> - Equilateral condition: CCW $(a,b,c)$ equilateral $\iff a + \omega b + \omega^2 c = 0$ (both directions proven).
> - Ptolemy: algebraic identity → triangle inequality → equality condition = cyclic order.
> - Van Aubel: outward-square center $\frac{(1+i)p+(1-i)q}{2}$ (CCW quad); $m_{bc} - m_{da} = -i(m_{cd}-m_{ab})$.
> - Napoleon: outward-equilateral center $\frac{(2+\omega)a+(1-\omega)b}{3}$; centers satisfy the equilateral condition.
> - Centroid distance-sum formula (Leibniz) with the "minimum at the centroid" corollary.
> - Area $=\tfrac12|\operatorname{Im}((z_2-z_1)\overline{(z_3-z_1)})|$; circumcenter as a linear solve in $u, \bar u$.

> **🌉 Bridge to Ch 6 — synthesis & the stretch problems**
>
> Everything is now in place: algebra, polar, roots of unity, loci, and polygon geometry. Chapter 6 assembles them into the problems that separate "knows the formulas" from "sees the structure" — unit-circle configurations that force rectangles, product identities for regular polygons, and the two-vertex transformations $w = z + 1/z$ that turn circles into line segments. Then: the 38-question paper, where the whole module is tested at once.



---

