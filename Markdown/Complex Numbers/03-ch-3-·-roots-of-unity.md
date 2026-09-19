# Chapter 3 — Ch 3 · Roots of Unity

*5 sections · 8 questions*

*Chapter 3 of 6*

# Roots of Unity

The most special numbers in the whole subject: the solutions of $z^n = 1$. One definition buys you a whole family of identities — sums that vanish, products that collapse to $n$, trigonometric products with clean answers, and the "roots-of-unity filter," a JEE-Advanced/Olympiad workhorse for binomial sums with $k \equiv r \pmod n$. Master this chapter and a whole class of "magical" answers stops being magical.

### 3.1 The cube roots of unity — one number, five identities

The equation $z^3 = 1$ has exactly three solutions (Ch 2, §2.4): 
$$ 1,\qquad \omega = e^{2\pi i/3} = -\frac12 + i\frac{\sqrt3}{2},\qquad
    \omega^2 = e^{4\pi i/3} = -\frac12 - i\frac{\sqrt3}{2}. $$
 By universal convention, **$\omega$ denotes a non-real cube root of unity**, so $\omega^3 = 1$ and $\omega \ne 1$. Everything below is either a one-line computation from that, or a direct read-off from the plane. Learn the five identities; they appear in JEE questions at least once a year.

> **📦 The five $\omega$-identities (with proofs — no memorizing without reasons)**
>
> **(i) $1 + \omega + \omega^2 = 0$.** Since $\omega \ne 1$ is a root of $x^3 - 1 = (x-1)(x^2 + x + 1)$, we have $\omega^2 + \omega + 1 = 0$. (Equivalent view: geometric series $\frac{1-\omega^3}{1-\omega} = 0$, valid because $\omega \ne 1$.) **(ii) $\bar\omega = \omega^2$.** Conjugation reflects in the real axis: $\bar\omega = e^{-2\pi i/3} = e^{4\pi i/3} = \omega^2$. Geometrically, $\omega$ and $\omega^2$ are mirror images — both sit at $\pm 120^\circ$. **(iii) $(1-\omega)(1-\omega^2) = 3$.** Expand: $1 - \omega - \omega^2 + \omega\omega^2 = 1 - (\omega + \omega^2) + \omega^3 = 1 - (-1) + 1 = 3$, using (i) and $\omega^3 = 1$. **(iv) $1 + \omega = e^{i\pi/3}$.** Algebra: $1 + \omega = 1 - \frac12 + i\frac{\sqrt3}{2}
>       = \frac12 + i\frac{\sqrt3}{2} = \cos\frac{\pi}{3} + i\sin\frac{\pi}{3}$. So $1+\omega$ has modulus $1$ and argument $60^\circ$. (Useful consequence: $1+\omega = -\omega^2$, from (i).) **(v) $1 - \omega = \sqrt3\, e^{-i\pi/6}$.** $1 - \omega = \frac32 - i\frac{\sqrt3}{2}
>       = \sqrt3\left(\frac{\sqrt3}{2} - \frac{i}{2}\right) = \sqrt3\left(\cos\frac{-\pi}{6} + i\sin\frac{-\pi}{6}\right)$. So $|1-\omega| = \sqrt3$ — the side length of the equilateral triangle $\{1, \omega, \omega^2\}$ — and its argument is $-30^\circ$.

Why does this triangle matter? $1, \omega, \omega^2$ are equally spaced ($120^\circ$ apart) on the unit circle, so they form an *equilateral triangle*. Every identity above is either "plug in the geometry" or "expand and use $1+\omega+\omega^2=0$". When a JEE question says "let $\omega$ be a cube root of unity," your first move is always: rewrite everything in terms of $\omega + \omega^2 = -1$ and $\omega^3 = 1$.

**Worked — evaluate $(1+\omega)(1+\omega^2)$ two ways.** Algebra: expand and use $1+\omega+\omega^2 = 0$, $\omega^3 = 1$: 
$$ (1+\omega)(1+\omega^2) = 1 + (\omega+\omega^2) + \omega\omega^2 = 1 + (-1) + 1 = 1. $$
 Polar: use identities (iv)–(v), $1+\omega = e^{i\pi/3}$, $1+\omega^2 = \overline{1+\omega} = e^{-i\pi/3}$: 
$$ (1+\omega)(1+\omega^2) = e^{i\pi/3} \cdot e^{-i\pi/3} = 1. $$
 The two methods agree — and they should, which is a useful habit: when one method feels shaky, run the other one. Here the polar version is also a preview of a general principle: $1+\omega$ and $1+\omega^2$ are conjugates, so their product is $|1+\omega|^2 = 1$, real and positive, in one step.

> **⚠️ Watch out — the classic sign slip**
>
> $(1+\omega)(1+\omega^2) = 1$, and **not** 2. The slip is treating $\omega + \omega^2$ as $+1$. Drill: $\omega + \omega^2 = -1$, $\omega\omega^2 = 1$, $\omega^3 = 1$. If you ever write "2" here, one of those three is wrong in your head.


### 3.2 The $n$-th roots of unity and the vanishing sum

Generalize to $z^n = 1$. By Ch 2, the exactly-$n$ solutions are

*primitive*

> **📦 The vanishing-sum identity**
>
> For any integer $m$: 
> $$ \sum_{k=0}^{n-1} \zeta^{mk} = \begin{cases} n, & n \mid m,\\ 0, & n \nmid m. \end{cases} $$
>  **Proof.** This is a geometric series with ratio $\zeta^m$. If $n \mid m$, then $\zeta^m = 1$ and all $n$ terms are $1$. Otherwise $\zeta^m \ne 1$ and 
> $$ \sum_{k=0}^{n-1} (\zeta^m)^k = \frac{(\zeta^m)^n - 1}{\zeta^m - 1} = \frac{(\zeta^n)^m - 1}{\zeta^m - 1} = 0. $$
>  Two lines. This is the engine behind every "sum of roots" problem you will meet.

**Worked — $\sum_{k=0}^{5} e^{i\pi k/3}$.** The terms are $e^{0}, e^{i\pi/3}, e^{i2\pi/3}, e^{i\pi}, e^{i4\pi/3}, e^{i5\pi/3}$ — precisely the six sixth-roots of unity $\eta, \eta^2, \dots$ with $\eta = e^{i\pi/3}$. By the identity with $n = 6, m = 1$: **sum $= 0$**. (Read geometrically: the six vectors are the six sides' worth of a closed regular hexagon — they cancel.)

1 ζ ζ² −1 ζ⁴ ζ⁵ O The six sixth-roots of unity, $\zeta^k = e^{2\pi i k/6}$, form a regular hexagon. Their sum is $0$ — the vectors close the hexagon.

#### **P25**[JEE Main][roots of unity]Evaluate [formula] .

Evaluate $\displaystyle\sum_{k=0}^{5} e^{i\pi k/3}$.

<details>
<summary>Answer + Reasoning</summary>

The six terms are the sixth-roots of unity (in order). Either invoke $\sum_{k=0}^{5}\eta^k = \frac{1-\eta^6}{1-\eta} = 0$ with $\eta = e^{i\pi/3}$, or read the hexagon: opposite vertices cancel in pairs $(1 + (-1)) = 0$, $(e^{i\pi/3} + e^{i4\pi/3}) = 0$, $(e^{i2\pi/3} + e^{i5\pi/3}) = 0$.


Answer: $0$

</details>


### 3.3 Two product formulas — where the number $n$ hides

Sums of roots vanish; *products* of distances from $1$ to the roots produce exactly $n$. This is one of the most beautiful one-line applications of $z^n - 1$ in all of algebra.

> **📦 Product formula — $\displaystyle\prod_{k=1}^{n-1}(1-\zeta_k) = n$**
>
> **Proof.** Factor completely over $\mathbb{C}$: 
> $$ x^n - 1 = \prod_{k=0}^{n-1}(x - \zeta_k) = (x-1)\prod_{k=1}^{n-1}(x-\zeta_k). $$
>  Divide by $x-1$ and take the limit $x \to 1$ (equivalently, compare derivatives at $x=1$): 
> $$ \prod_{k=1}^{n-1}(1-\zeta_k) = \lim_{x\to 1}\frac{x^n-1}{x-1} = \left.\frac{d}{dx}x^n\right|_{x=1} = n. $$
>  The limit is just the definition of the derivative of $x^n$ at $x = 1$. Two-line proof, olympiad-grade content.

> **📦 Trigonometric cousin — $\displaystyle\prod_{k=1}^{n-1}\sin\frac{\pi k}{n} = \frac{n}{2^{n-1}}$**
>
> **Derivation.** Compute $|1-\zeta_k|$ directly: 
> $$ |1-e^{2\pi i k/n}| = \left|e^{\pi i k/n}(e^{-\pi i k/n} - e^{\pi i k/n})\right|
>       = |{-2i\sin(\pi k/n)}| = 2\sin\frac{\pi k}{n} $$
>  (positive for $1 \le k \le n-1$, since $0 < \pi k/n < \pi$). Taking moduli in the product formula: 
> $$ n = \prod_{k=1}^{n-1}|1-\zeta_k| = \prod_{k=1}^{n-1} 2\sin\frac{\pi k}{n}
>       = 2^{n-1}\prod_{k=1}^{n-1}\sin\frac{\pi k}{n}. $$
>  **Check, $n = 6$:** $\sin\frac{\pi}{6}\sin\frac{\pi}{3}\sin\frac{\pi}{2}\sin\frac{2\pi}{3}\sin\frac{5\pi}{6}
>       = \frac12\cdot\frac{\sqrt3}{2}\cdot1\cdot\frac{\sqrt3}{2}\cdot\frac12 = \frac{3}{16}$, and the formula gives $\frac{6}{2^5} = \frac{3}{16}$ ✓.

#### **P23**[JEE Advanced][product formula]Evaluate [formula] .

Evaluate $\displaystyle\prod_{k=1}^{5}\left(1 - e^{2\pi i k/5}\right)$.

<details>
<summary>Answer + Reasoning</summary>

Immediate from the product formula with $n = 5$: the product is $5$. (You could also note the factors come in conjugate pairs, so the product is real and positive — the formula gives its value for free.)


Answer: $5$

</details>

#### **P24**[Olympiad][trig product]Evaluate [formula] .

Evaluate $\displaystyle\sin\frac{\pi}{5}\sin\frac{2\pi}{5}\sin\frac{3\pi}{5}\sin\frac{4\pi}{5}$.

<details>
<summary>Answer + Reasoning</summary>

By the trigonometric product formula with $n = 5$: $\prod_{k=1}^{4}\sin\frac{\pi k}{5} = \frac{5}{2^4} = \frac{5}{16}$. (Sanity: each sine is between $0$ and $1$, product $\approx 0.31$ — plausible.)


Answer: $\dfrac{5}{16}$

</details>


### 3.4 The roots-of-unity filter — binomial sums with $k \equiv r \pmod n$

**The problem type.** "Find $\sum_{k \equiv 0 \pmod 3} \binom{9}{k}$" — i.e., add only the binomial coefficients whose index lands in one residue class. Direct counting is ugly; the *roots-of-unity filter* makes it a two-line computation.

> **⛁ First Principles — where the filter comes from**
>
> We want a function that is $1$ when $k \equiv r \pmod n$ and $0$ otherwise. Consider $\zeta = e^{2\pi i/n}$. The average 
> $$ \frac1n\sum_{j=0}^{n-1} \zeta^{j(k-r)} = \begin{cases}1, & n \mid (k-r),\\ 0, & \text{otherwise},\end{cases} $$
>  is exactly that indicator — it is the vanishing-sum identity applied to $m = k - r$! So for $P(x) = \sum_k c_k x^k$: 
> $$ \sum_{k \equiv r \pmod n} c_k = \frac1n\sum_{j=0}^{n-1} \zeta^{-rj}\, P(\zeta^j). $$
>  For $P(x) = (1+x)^N$ this gives the binomial version: 
> $$ \boxed{\ \sum_{k \equiv r \pmod n} \binom{N}{k} = \frac1n\sum_{j=0}^{n-1} e^{-2\pi i r j/n}
>       \left(1 + e^{2\pi i j/n}\right)^{N}\ } $$
>  One sum to evaluate — and for $n = 3$, $1 + e^{2\pi i j/3}$ has a clean polar form for each $j$, so the whole thing is trigonometry plus De Moivre.

**Worked — $\sum_{k \equiv 0 \pmod 3} \binom{9}{k}$ (JEE Advanced pattern).** Let $\omega = e^{2\pi i/3}$. The filter with $n = 3, r = 0$: 
$$ \sum_{k \equiv 0(3)} \binom{9}{k} = \frac13\left[(1+1)^9 + (1+\omega)^9 + (1+\omega^2)^9\right]. $$
 Now $(1+\omega)^9 = \left(e^{i\pi/3}\right)^9 = e^{i3\pi} = -1$, and $(1+\omega^2)^9 = \left(e^{-i\pi/3}\right)^9 = e^{-i3\pi} = -1$. Hence 
$$ \frac13\left(512 - 1 - 1\right) = \frac{510}{3} = 170. $$
 Direct verification: $\binom{9}{0} + \binom{9}{3} + \binom{9}{6} + \binom{9}{9}
    = 1 + 84 + 84 + 1 = 170$ ✓.

**The sibling classes.** For $r = 1$: $\frac13\left[2^9 + \omega^{-1}(1+\omega)^9 + \omega^{-2}(1+\omega^2)^9\right]
    = \frac13\left[512 + \omega^2(-1) + \omega(-1)\right] = \frac13\left[512 - (\omega + \omega^2)\right]
    = \frac13(512 + 1) = 171$. And $r = 2$ gives $171$ by the conjugate symmetry. Check: $170 + 171 + 171 = 512 = 2^9$ ✓ — the three residue classes partition the $2^9$ subsets of a 9-set.

#### **P26**[JEE Advanced][filter]Find [formula] .

Find $\displaystyle\sum_{k \equiv 0 \pmod 3} \binom{9}{k}$.

<details>
<summary>Answer + Reasoning</summary>

Filter: $\frac13\left[2^9 + (1+\omega)^9 + (1+\omega^2)^9\right] = \frac13(512 - 1 - 1) = 170$. Direct: $1 + 84 + 84 + 1 = 170$.


Answer: $170$


Bonus (same method): the $r = 1$ and $r = 2$ classes each sum to $171$.

</details>


### 3.5 Practice set — $\omega$ under pressure

#### **P21**[JEE Main][$\omega$ identities]If [formula] is a non-real cube root of unity, find [formula] .

If $\omega$ is a non-real cube root of unity, find $(1+\omega)(1+\omega^2)$.

<details>
<summary>Answer + Reasoning</summary>

$(1+\omega)(1+\omega^2) = 1 + (\omega+\omega^2) + \omega^3 = 1 - 1 + 1 = 1$. Polar shortcut: $(e^{i\pi/3})(e^{-i\pi/3}) = 1$.


Answer: $1$

</details>

#### **P22**[JEE Main][periodic sums]Evaluate [formula] .

Evaluate $\displaystyle\sum_{k=0}^{2023} \omega^k$.

<details>
<summary>Answer + Reasoning</summary>

The sum is $3\cdot 674 + 2$ terms. Each block of three sums to $1+\omega+\omega^2 = 0$, so only the last two terms survive: $\omega^{2022} + \omega^{2023} = \omega^0 + \omega^1 = 1 + \omega = -\omega^2$.


Answer: $-\omega^2$

</details>

#### **P27**[JEE Main][$\omega$ identities]If [formula] and [formula] , find [formula] .

If $\omega^3 = 1$ and $\omega \ne 1$, find $(\omega + \omega^2)^3 + 3(\omega + \omega^2) + 1$.

<details>
<summary>Answer + Reasoning</summary>

$\omega + \omega^2 = -1$, so the expression is $(-1)^3 + 3(-1) + 1 = -1 - 3 + 1 = -3$.


Answer: $-3$

</details>

#### **P28**[JEE Advanced][$\omega$ + polar]If [formula] is a non-real cube root of unity, evaluate [formula] and [formula…

If $\omega$ is a non-real cube root of unity, evaluate $|1-\omega|^2$ and $\arg(1-\omega)$.

<details>
<summary>Answer + Reasoning</summary>

From identity (v): $1-\omega = \sqrt3\, e^{-i\pi/6}$. So $|1-\omega|^2 = 3$ (the squared side of the equilateral triangle on the unit circle) and $\arg(1-\omega) = -\pi/6$. Pure-algebra check: $|1-\omega|^2 = (1-\omega)(1-\omega^2) = 3$ (identity iii).


Answer: $3$, $-\dfrac{\pi}{6}$

</details>

> **✅ Chapter checklist**
>
> - Five $\omega$-identities, each with its one-line proof — and the sign-slip warning.
> - Vanishing sum: $\sum_{k=0}^{n-1}\zeta^{mk} = 0$ unless $n \mid m$.
> - Product formula: $\prod_{k=1}^{n-1}(1-\zeta_k) = n$ (derivative of $x^n - 1$ at $1$).
> - Trig cousin: $\prod_{k=1}^{n-1}\sin\frac{\pi k}{n} = \frac{n}{2^{n-1}}$.
> - Roots-of-unity filter for $\sum_{k \equiv r \pmod n} \binom{N}{k}$, worked for $N = 9, n = 3$.

> **🌉 Bridge to Ch 4 — JEE Advanced core: loci & optimization**
>
> Chapters 1–3 are the toolkit: algebra (Ch 1), polar/De Moivre (Ch 2), roots of unity (Ch 3). Chapter 4 is where JEE Advanced becomes JEE Advanced — equations mixing $z$ and $\bar z$, loci defined by modulus/argument conditions, and minimizing $|z - a|$ subject to constraints. Every tool in this chapter gets used there at least once.



---

