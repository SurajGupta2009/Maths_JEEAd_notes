# Chapter 2 — Ch 2 · Polar Form & De Moivre

*7 sections · 12 questions*

*Chapter 2 · Polar Form & De Moivre*

# Stretch × Rotate

Every complex number is a *length times a direction*. Once the direction becomes a variable, multiplication becomes angle-addition, powers become angle-multiplication, and "find the n-th roots" becomes "draw a regular n-gon". De Moivre's theorem is the engine; everything in this chapter is its consequence.

`argument` `polar form` `De Moivre` `n-th roots` `square roots of complex numbers` `Euler's form`

### 2.1 The argument — the missing half of the story

Chapter 1 gave the *length* of $z = a + bi$: the modulus $|z| = \sqrt{a^2+b^2}$. The *direction* is equally intrinsic, and it is what multiplication actually does. Look at the point $z$ on the complex plane: it has a distance from $O$ and an angle from the positive real axis. That angle is the **argument**.

> **⛁ First Principles — definition, and why it is multi-valued**
>
> For $z \ne 0$, an **argument** of $z$ is any real number $\theta$ with 
> $$ a = |z|\cos\theta, \qquad b = |z|\sin\theta. $$
>  Such a $\theta$ is determined only up to adding multiples of $2\pi$: if $\theta$ works, so does $\theta + 2k\pi$, $k \in \mathbb Z$. So "the argument" is really a *set*: $\arg z = \{\theta_0 + 2k\pi : k \in \mathbb Z\}$. We write $\arg z$ for the set and **principal argument** $\operatorname{Arg} z \in (-\pi, \pi]$ for the canonical representative.
>
>
> Why the set matters: angles *add*, and addition of angles is only defined mod $2\pi$. Keeping "mod $2\pi$" visible (instead of silently picking one representative) is what keeps De Moivre honest for negative and rational powers.

Examples that build the reflex: 
$$ \begin{array}{c|c|c}
    z & |z| & \operatorname{Arg} z \\ \hline
    1 & 1 & 0 \\
    i & 1 & \frac{\pi}{2} \\
    -1 & 1 & \pi \ \ (\text{not } -\pi) \\
    -i & 1 & -\frac{\pi}{2} \\
    1+i & \sqrt2 & \frac{\pi}{4} \\
    1-i\sqrt3 & 2 & -\frac{\pi}{3} \\
    -1+i & \sqrt2 & \frac{3\pi}{4}
    \end{array} $$
 The quadrant check is the whole skill: the quadrant of $(a,b)$ fixes which reference angle to use; $\operatorname{Arg}(-1+i) = \pi - \pi/4 = 3\pi/4$, *not* $-\pi/4$ (that's the fourth quadrant).

> **💡 Key Idea — arguments turn multiplication into addition**
>
> For $z_1, z_2 \ne 0$: 
> $$ \arg(z_1 z_2) = \arg z_1 + \arg z_2 \pmod{2\pi}, \qquad
>       \arg\frac{z_1}{z_2} = \arg z_1 - \arg z_2 \pmod{2\pi}, $$
>  and $\arg \bar z = -\arg z$, $\arg(z^n) = n\arg z$. Proof preview: these all follow in one line from the polar form (next section). Consequence you can already use: the angle of the product is the *sum of the angles* — "rotate by $\theta_1$, then by $\theta_2$, is a rotation by $\theta_1+\theta_2$".

#### **P9**[warm-up][practice][argument]Find the modulus and principal argument of [formula] . Hence express it in the…

Find the modulus and principal argument of $-1 + i$. Hence express it in the form $r(\cos\theta + i\sin\theta)$ with $r &gt; 0$.

<details>
<summary>Answer + Reasoning</summary>

$|-1+i| = \sqrt{1+1} = \sqrt2$. Point $(-1, 1)$ is in quadrant II; reference angle $\pi/4$: $\operatorname{Arg}(-1+i) = \pi - \pi/4 = 3\pi/4$.



$$ -1 + i = \sqrt2\left(\cos\frac{3\pi}{4} + i\sin\frac{3\pi}{4}\right). $$
 Check: $\cos 3\pi/4 = -\frac{\sqrt2}{2}$, $\sin 3\pi/4 = \frac{\sqrt2}{2}$ → $\sqrt2 \cdot (-\frac{\sqrt2}{2} + i\frac{\sqrt2}{2}) = -1 + i$ ✓

</details>

#### **P10**[JEE Main][practice][argument]Express [formula] in polar form with principal argument.

Express $1 - i\sqrt3$ in polar form with principal argument.

<details>
<summary>Answer + Reasoning</summary>

$|1 - i\sqrt3| = \sqrt{1+3} = 2$. Point $(1, -\sqrt3)$ is quadrant IV with reference angle $\tan^{-1}(\sqrt3) = \pi/3$, so the principal argument is $-\pi/3$.



$$ 1 - i\sqrt3 = 2\left(\cos\frac{-\pi}{3} + i\sin\frac{-\pi}{3}\right). $$
 (Equivalently $2(\cos \frac{5\pi}{3} + i\sin\frac{5\pi}{3})$ — same direction, non-principal representative.)

</details>


### 2.2 Polar (trigonometric) form

**Definition.** Every $z \ne 0$ can be written uniquely as 
$$ z = r(\cos\theta + i\sin\theta), \qquad r = |z| &gt; 0,\ \theta \in \arg z. $$
 The **polar form** separates the two pieces of data a complex number carries: the stretch $r$ and the direction $\theta$. Derivation (not a convention): draw the right triangle with hypotenuse $|z|$ and angle $\theta$ — the legs are exactly $|z|\cos\theta$ and $|z|\sin\theta$, i.e. $a$ and $b$.

The inverse conversion (polar → Cartesian) is just expansion: 
$$ r(\cos\theta + i\sin\theta) = r\cos\theta + i\, r\sin\theta. $$


> **⛁ First Principles — why the polar form multiplies the way it does**
>
> Let $z_1 = r_1(\cos\theta_1 + i\sin\theta_1)$ and $z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$. Expanding the product: 
> $$ z_1z_2 = r_1 r_2\big[(\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2)
>       + i(\cos\theta_1\sin\theta_2 + \sin\theta_1\cos\theta_2)\big]. $$
>  The two brackets are exactly the cosine- and sine-addition formulas, so 
> $$ z_1 z_2 = r_1 r_2 \big(\cos(\theta_1+\theta_2) + i\sin(\theta_1+\theta_2)\big). $$
>  **Read that result:** multiplying stretches by $r_1 r_2$ and rotates by $\theta_1 + \theta_2$. This one calculation is the seed of De Moivre's theorem (set $z_1 = z_2$, then induct) and the reason arguments add. Everything else in this chapter is bookkeeping for it.

**Worked — a full round trip.** Convert $-\sqrt3 + i$ to polar, then back.

- $r = \sqrt{3+1} = 2$. Point $(-\sqrt3, 1)$: quadrant II, reference angle $\tan^{-1}(1/\sqrt3) = \pi/6$, so $\theta = \pi - \pi/6 = 5\pi/6$.
- Polar: $-\sqrt3 + i = 2(\cos 5\pi/6 + i\sin 5\pi/6)$.
- Back: $2\cos 5\pi/6 = 2(-\sqrt3/2) = -\sqrt3$, $2\sin 5\pi/6 = 2(1/2) = 1$ ✓.

#### **P11**[JEE Main][practice][polar form]Find the polar form of [formula] , and of [formula] .

Find the polar form of $-i$, and of $\dfrac{1}{1+i}$.

<details>
<summary>Answer + Reasoning</summary>

$-i$: $r = 1$, direction straight down: $\operatorname{Arg} = -\pi/2$. Polar: $\cos(-\pi/2) + i\sin(-\pi/2)$.


$\frac{1}{1+i} = \frac{1-i}{(1+i)(1-i)} = \frac{1-i}{2} = \frac12 - \frac12 i$. So $r = \sqrt{\tfrac14 + \tfrac14} = \frac{1}{\sqrt2}$, quadrant IV, reference $\pi/4$: $\operatorname{Arg} = -\pi/4$.



$$ \frac{1}{1+i} = \frac{1}{\sqrt2}\left(\cos\frac{-\pi}{4} + i\sin\frac{-\pi}{4}\right). $$
 Sanity check via arguments: $\arg(1/(1+i)) = -\arg(1+i) = -\pi/4$ ✓, $|1/(1+i)| = 1/|1+i| = 1/\sqrt2$ ✓ — the two-language method works in either direction.

</details>


### 2.3 De Moivre's theorem — the engine

> **⛁ First Principles — statement and proof by induction**
>
> **Theorem (De Moivre).** For $z = \cos\theta + i\sin\theta$ (i.e. $|z| = 1$) and every integer $n \ge 1$: 
> $$ (\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta. $$
>  More generally, for $z = r(\cos\theta + i\sin\theta)$: 
> $$ z^n = r^n(\cos n\theta + i\sin n\theta). $$
>  **Proof.** The general case follows from the $|z|=1$ case since $z^n = r^n(\cos\theta+i\sin\theta)^n$. For $|z|=1$: $n=1$ is the identity. Assume it holds for $n$. Then by the angle-addition calculation of §2.2, 
> $$ (\cos\theta+i\sin\theta)^{n+1}
>       = (\cos n\theta + i\sin n\theta)(\cos\theta + i\sin\theta)
>       = \cos(n+1)\theta + i\sin(n+1)\theta. \qquad \square $$
>  **Negative exponents.** $(\cos\theta+i\sin\theta)^{-1} =
>       \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta)$ (conjugation flips the sign of the angle, §2.1), so the theorem extends to all $n \in \mathbb Z$ by writing $z^n = (z^{-1})^{-n}$.

**Worked — powering without expanding.** Compute $(\sqrt3 + i)^4$ two ways.

- *De Moivre:* $\sqrt3+i = 2(\cos\pi/6 + i\sin\pi/6)$, so $(\sqrt3+i)^4 = 2^4(\cos 2\pi/3 + i\sin 2\pi/3)
      = 16(-\tfrac12 + i\tfrac{\sqrt3}{2}) = -8 + 8\sqrt3\, i$.
- *Brute force (sanity):* $(\sqrt3+i)^2 = 2 + 2\sqrt3\, i
      = 4(\cos\pi/3 + i\sin\pi/3)$; squaring: $16(\cos 2\pi/3 + i\sin 2\pi/3)$ — same answer, and the squaring route shows why De Moivre halves the work each step.

**Corollary — the triple-angle formulas.** Set $n = 3$: 
$$ \cos 3\theta + i\sin 3\theta = (\cos\theta + i\sin\theta)^3
    = \cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta. $$
 Equate real and imaginary parts (justified because two complex numbers are equal iff both parts are — Chapter 1, §1.1): 
$$ \boxed{\ \cos 3\theta = 4\cos^3\theta - 3\cos\theta,\qquad
    \sin 3\theta = 3\sin\theta - 4\sin^3\theta\ } $$
 (using $\sin^2\theta = 1 - \cos^2\theta$ and $\cos^2\theta = 1 - \sin^2\theta$). These are the kind of "trig identity" a JEE problem expects you to *derive in ten seconds* from De Moivre instead of remembering.

> **🏛 Exam flavor — $(1+i)^n$ and the $45^\circ$-direction trick**
>
> $1+i = \sqrt2\, e^{i\pi/4}$, so $(1+i)^n = 2^{n/2}(\cos n\pi/4 + i\sin n\pi/4)$: the angle steps by $45^\circ$ each power. In particular $(1+i)^2 = 2i$, $(1+i)^4 = -4$, $(1+i)^8 = 16$, and the cycle of directions has period 8. Any $(1+i)^n$ with $n \le 40$ is a 5-second computation: halve the exponent's parity, multiply by $2^{n/2}$, read the angle from the table of $n\pi/4 \bmod 2\pi$.

#### **P12**[JEE Main][practice][De Moivre]Compute [formula] .

Compute $(1+i)^8$.

<details>
<summary>Answer + Reasoning</summary>

$(1+i)^8 = \big((1+i)^2\big)^4 = (2i)^4 = 16\, i^4 = \mathbf{16}$.


De Moivre check: $(\sqrt2\, e^{i\pi/4})^8 = 2^4 e^{i2\pi} = 16$ ✓.

</details>

#### **P13**[JEE Adv][practice][De Moivre · trig]If [formula] , express [formula] as a function of [formula] .

If $z = \cos\theta + i\sin\theta$, express $\operatorname{Re}(z^3 + z^{-3})$ as a function of $\cos\theta$.

<details>
<summary>Answer + Reasoning</summary>

By De Moivre: $z^3 = \cos 3\theta + i\sin 3\theta$. Also $z^{-1} = \bar z = \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta)$, so $z^{-3} = \cos 3\theta - i\sin 3\theta$.



$$ z^3 + z^{-3} = 2\cos 3\theta \quad (\text{purely real}) $$
 and with the triple-angle formula, 
$$ \operatorname{Re}(z^3+z^{-3}) = 2\cos 3\theta = \mathbf{8\cos^3\theta - 6\cos\theta}. $$
 The general pattern — $z^n + z^{-n}$ is a polynomial in $2\cos\theta$ of degree $n$ — is how roots-of-unity sums get evaluated in Chapter 3.

</details>

#### **P14**[Olympiad][practice][De Moivre · identity]Prove that for all [formula] : [formula] (Here [formula] — the notation of §2.…

Prove that for all $\theta$: 
$$ e^{i\theta} + e^{i(\theta + 2\pi/3)} + e^{i(\theta + 4\pi/3)} = 0. $$
 (Here $e^{i\theta} := \cos\theta + i\sin\theta$ — the notation of §2.6.)

<details>
<summary>Answer + Reasoning</summary>

Factor out $e^{i\theta}$: 
$$ e^{i\theta}\big(1 + e^{2\pi i/3} + e^{4\pi i/3}\big). $$
 The bracket is $1 + \omega + \omega^2$ with $\omega = e^{2\pi i/3}$ — the sum of all three cube roots of 1. Since $t^3 - 1 = (t-1)(t^2+t+1)$, every root of $t^2+t+1 = 0$ (i.e. $\omega, \omega^2$) satisfies $1 + \omega + \omega^2 = 0$. Hence the whole expression is $0$. $\square$


Geometrically: three unit vectors spaced $120^\circ$ apart sum to zero — an equilateral triangle closed. This single fact powers a third of Chapter 3.

</details>


### 2.4 The n-th roots of a complex number

**Problem.** Solve $z^n = w$ for $z \in \mathbb C$, $w \ne 0$. Write $w = R(\cos\phi + i\sin\phi)$ and $z = r(\cos\theta + i\sin\theta)$. De Moivre turns the equation into two real conditions: 
$$ r^n = R, \qquad n\theta \equiv \phi \pmod{2\pi}. $$
 First: $r = R^{1/n} &gt; 0$ — *unique*. Second: $\theta = \frac{\phi + 2k\pi}{n}$, $k \in \mathbb Z$ — but $\theta$ is only defined mod $2\pi$, so distinct $k$ give distinct roots only while $k$ runs over $n$ consecutive values. Hence:

> **⛁ First Principles — exactly n roots, equally spaced**
>
> **Theorem.** $w \ne 0$ has exactly $n$ n-th roots: 
> $$ z_k = R^{1/n}\left(\cos\frac{\phi + 2k\pi}{n} + i\sin\frac{\phi + 2k\pi}{n}\right),
>       \qquad k = 0, 1, \dots, n-1. $$
>  They lie on the circle $|z| = R^{1/n}$, and consecutive ones differ in angle by exactly $2\pi/n$: **they are the vertices of a regular $n$-gon** circumscribed on that circle. (Existence and count: the $n$ values of $k$ are distinct mod $2\pi$; no other $\theta$ is possible since $n\theta \equiv \phi$ has exactly $n$ solutions mod $2\pi$.)

**Diagram**

![Diagram](assets/fig-06.svg)

**Worked — cube roots of 8.** $R = 2$, $\phi = 0$: 
$$ z_k = 2\left(\cos\frac{2k\pi}{3} + i\sin\frac{2k\pi}{3}\right),\ k = 0,1,2:
    \qquad z_0 = 2,\quad z_1 = -1 + i\sqrt3,\quad z_2 = -1 - i\sqrt3. $$
 Check each: $2^3 = 8$; and $(-1+i\sqrt3)^2 = 1 - 2i\sqrt3 - 3 = -2 - 2i\sqrt3$, so 
$$ (-1+i\sqrt3)^3 = (-1+i\sqrt3)(-2-2i\sqrt3) = 2 + 2i\sqrt3 - 2i\sqrt3 + \underbrace{(-2)(i\sqrt3)(i\sqrt3)}_{+6} = 8 \ \checkmark $$
 (The shortcut is the polar form: $-1+i\sqrt3 = 2e^{2\pi i/3}$, so its cube is $8e^{2\pi i} = 8$.)

**Worked — square roots of $-8$.** $R = 8$, $\phi = \pi$: 
$$ z_k = \sqrt8\left(\cos\frac{\pi + 2k\pi}{2} + i\sin\frac{\pi+2k\pi}{2}\right),\ k = 0,1:
    \quad z_0 = 2\sqrt2\, e^{i\pi/2} = 2\sqrt2\, i, \quad z_1 = 2\sqrt2\, e^{i3\pi/2} = -2\sqrt2\, i. $$
 Check: $(2\sqrt2\, i)^2 = 8i^2 = -8$ ✓. Notice the pattern: the two square roots are always opposite points on the circle (a regular 2-gon = a diameter).

> **📌 Note — "the" root vs "a" root**
>
> When a problem writes $\sqrt{w}$ for complex $w$, the convention is the **principal square root** (the one with argument in $(-\pi/2, \pi/2]$, i.e. non-negative real part — and for purely negative imaginary results, the one with non-negative imaginary part). But "find the n-th roots" always means *all n*. The ambiguity is a classic trap: $\sqrt{(-1)^2} = 1$, while $(\sqrt{-1})^2 = -1$ — never distribute a root over a product for complex numbers.

#### **P15**[JEE Main][practice][n-th roots]Find all fourth roots of [formula] .

Find all fourth roots of $16$.

<details>
<summary>Answer + Reasoning</summary>

$R = 16$, $\phi = 0$: $r = 2$, angles $\frac{2k\pi}{4} = \frac{k\pi}{2}$, $k = 0,1,2,3$.



$$ z_k = 2\left(\cos\frac{k\pi}{2} + i\sin\frac{k\pi}{2}\right)
        \in \{\ 2,\ 2i,\ -2,\ -2i\ \}. $$
 Each checks: $(2i)^4 = 16i^4 = 16$ ✓. Geometrically: the square inscribed in $|z| = 2$ — exactly as the diagram shows.

</details>

#### **P16**[JEE Adv][practice][n-th roots · geometry]Let [formula] be the three cube roots of [formula] . Find [formula] and [formu…

Let $z_1, z_2, z_3$ be the three cube roots of $-27$. Find $z_1 z_2 + z_2 z_3 + z_3 z_1$ and $z_1 + z_2 + z_3$.

<details>
<summary>Answer + Reasoning</summary>

The roots of $t^3 + 27 = 0$, i.e. of $t^3 = -27$, are the roots of $t^3 + 27$. Vieta gives it directly: for $t^3 + 0\cdot t^2 + 0\cdot t + 27$, 
$$ z_1 + z_2 + z_3 = -\frac{0}{1} = \mathbf{0}, \qquad
        z_1z_2 + z_2z_3 + z_3z_1 = \frac{0}{1} = \mathbf{0}. $$
 **But the geometry explains *why* Vieta says so:** the roots are $-3, \tfrac32 \pm i\tfrac{3\sqrt3}{2}$ — an equilateral triangle centered at the origin, and any regular $n$-gon centered at $0$ has vertex-sum $0$ (§3, roots of unity) and, for $n = 3$, the pairwise-product sum $0$ as well.


Explicit check (for the anxious): the arguments are $\pi, \pi/3, 5\pi/3$, so the pairwise products are $9e^{i4\pi/3},\ 9e^{i2\pi/3},\ 9e^{i2\pi} = 9$, and 
$$ z_1z_2 + z_2z_3 + z_3z_1 = 9\left(e^{i4\pi/3} + e^{i2\pi/3} + 1\right)
        = 9\left(-\tfrac12 - i\tfrac{\sqrt3}{2} - \tfrac12 + i\tfrac{\sqrt3}{2} + 1\right) = 0 \ \checkmark $$
 Vieta is the method; this is the verification.

</details>


### 2.5 Every complex number has a square root

Chapter 1, §1.2 promised: "every complex number has a square root — the statement that needs proof". Here it is, in the algebraic language (the polar proof is the $n = 2$ case of §2.4; both are below, because each trains a different reflex).

> **⛁ First Principles — the formula, derived from scratch**
>
> Seek $\sqrt{a+bi} = x + iy$ with $x, y \in \mathbb R$. Squaring and matching parts (Ch 1, §1.1 — equality is componentwise): 
> $$ (x+iy)^2 = x^2 - y^2 + 2xyi = a + bi
>       \iff \begin{cases} x^2 - y^2 = a,\\ 2xy = b. \end{cases} $$
>  One more identity closes the system: $|x+iy|^2 = x^2 + y^2$ must equal $|\sqrt{a+bi}|^2 = |a+bi| = r := \sqrt{a^2+b^2}$. Adding and subtracting: 
> $$ \boxed{\ x^2 = \frac{r + a}{2}, \qquad y^2 = \frac{r - a}{2}\ } $$
>  (both non-negative since $|a| \le r$), and the sign of $y$ is the sign of $b$ (with $x$ taken positive — $x = 0$ only when $a = -r$, handled by the same formula). So the two square roots of $a+bi$ are 
> $$ \pm\left(\sqrt{\frac{r+a}{2}} + i\,\operatorname{sgn}(b)\sqrt{\frac{r-a}{2}}\right)
>       \quad (b \ne 0), $$
>  with the obvious limit when $b = 0$. $\square$

**Worked — $\sqrt{3+4i}$.** $r = \sqrt{9+16} = 5$: $x^2 = \frac{5+3}{2} = 4$, $y^2 = \frac{5-3}{2} = 1$, and $b = 4 &gt; 0$ forces $x, y$ same sign. So $\sqrt{3+4i} = 2 + i$ (and the other root $-2 - i$). Check: $(2+i)^2 = 4 + 4i + i^2 = 3 + 4i$ ✓.

**Worked — $\sqrt{-3+4i}$.** $r = 5$: $x^2 = \frac{5-3}{2} = 1$, $y^2 = \frac{5+3}{2} = 4$, $b = 4 &gt; 0$: roots $1 + 2i$ and $-1 - 2i$. Check: $(1+2i)^2 = 1 + 4i - 4 = -3 + 4i$ ✓.

**Worked — $\sqrt{1+i}$ (the "ugly" case, for the record).** $r = \sqrt2$: $x^2 = \frac{\sqrt2+1}{2}$, $y^2 = \frac{\sqrt2-1}{2}$, $b &gt; 0$: 
$$ \sqrt{1+i} = \sqrt{\frac{1+\sqrt2}{2}} \;+\; i\,\sqrt{\frac{\sqrt2-1}{2}}. $$
 Clean verification: $x^2 - y^2 = \frac{(1+\sqrt2) - (\sqrt2-1)}{2} = 1 = a$ ✓, and $2xy = 2\sqrt{\frac{(1+\sqrt2)(\sqrt2-1)}{4}} = 2\sqrt{\frac{2-1}{4}} = 1 = b$ ✓. (Equivalently, $\sqrt{1+i} = 2^{1/4}\, e^{i\pi/8}$ — the polar form makes the "half-angle" structure visible.)

> **💡 Key Idea — the payoff for Chapter 1**
>
> Now the quadratic formula *always* works: $x^2 + bx + c = 0$ has the two roots $\frac{-b \pm \sqrt{b^2-4c}}{2}$, with $\sqrt{\ \cdot\ }$ defined on all of $\mathbb C$. Combined with the fundamental theorem of algebra (every polynomial splits over $\mathbb C$), the complex numbers are the algebraically closed home of polynomial equations — the reason the subject exists at all in olympiad mathematics.

#### **P17**[JEE Main][practice][square roots]Find the square roots of [formula] .

Find the square roots of $3+4i$.

<details>
<summary>Answer + Reasoning</summary>

$r = 5$: $x^2 = \frac{5+3}{2} = 4$, $y^2 = \frac{5-3}{2} = 1$, $b &gt; 0$ → same sign. **Roots: $\pm(2+i)$.** Check $(2+i)^2 = 3+4i$ ✓.


Shortcut for perfect cases: guess $(m+ni)^2 = m^2-n^2 + 2mni =
        a+bi$ with small integers — here $m^2+n^2 = 5$ immediately suggests $1,2$.

</details>

#### **P18**[JEE Adv][practice][square roots · algebra]Solve [formula] . Verify both roots directly.

Solve $z^2 = 4i$. Verify both roots directly.

<details>
<summary>Answer + Reasoning</summary>

$a = 0$, $b = 4$, $r = 4$: $x^2 = \frac{4+0}{2} = 2$, $y^2 = \frac{4-0}{2} = 2$, $b &gt; 0$ → same sign. Roots: $\pm(1+i)\sqrt{2} = \pm(\sqrt2 + i\sqrt2)$.


Check directly: $(\sqrt2 + i\sqrt2)^2 = 2(1+i)^2 = 2(2i) = 4i$ ✓.


Polar cross-check: $4i = 4e^{i\pi/2}$; square roots $2e^{i\pi/4}, 2e^{i5\pi/4} = \pm\sqrt2(1+i)$ ✓ — both languages agree.

</details>


### 2.6 Euler's form — $e^{i\theta}$, and the formula that unifies everything

Writing $\cos\theta + i\sin\theta$ over and over is noise. Euler's notation defines, for real $\theta$, 
$$ e^{i\theta} := \cos\theta + i\sin\theta, $$
 so the polar form becomes $z = r\,e^{i\theta}$, powers are $z^n = r^n e^{in\theta}$, and roots are $z_k = R^{1/n} e^{i(\phi+2k\pi)/n}$. The notation is not decorative — it is *exactly correct*: expanding the exponential series $e^w = \sum w^n/n!$ at $w = i\theta$ and grouping even/odd terms gives $\sum (-1)^k\theta^{2k}/(2k)! + i\sum (-1)^k\theta^{2k+1}/(2k+1)!$, which is $\cos\theta + i\sin\theta$ term for term. (Series convergence of $e^w$ for complex $w$ is a standard analysis fact; we use the identity as a proven theorem.)

> **🏛 The identity that made Euler famous**
>
> Set $\theta = \pi$: 
> $$ e^{i\pi} + 1 = 0. $$
>  Five fundamental constants — $0, 1, e, i, \pi$ — in one line. It is the "checkpoint" that every proof of the exponential's complex behavior must pass: it says the point reached after a half-turn of unit speed around the unit circle is $-1$.

**What you can now do mechanically.**

| Task | Euler-form move |
| --- | --- |
| Powers | $(re^{i\theta})^n = r^n e^{in\theta}$ — multiply the angle |
| Roots | $n$-th roots of $Re^{i\phi}$: $R^{1/n}e^{i(\phi+2k\pi)/n}$, $k = 0,\dots,n-1$ |
| Products/quotients | multiply/divide moduli, add/subtract arguments |
| $z + \bar z$, $z - \bar z$ | $re^{i\theta} + re^{-i\theta} = 2r\cos\theta$; $re^{i\theta} - re^{-i\theta} = 2ir\sin\theta$ |

That last row is the workhorse of the next two chapters: *a complex number plus its conjugate is twice its real part*, and for $|z| = 1$, $\bar z = 1/z$, so $z + 1/z = 2\cos\theta$ whenever $z = e^{i\theta}$. Chapter 3 is essentially the art of using $e^{i\theta}$-form to turn polynomial and binomial questions into geometry on the unit circle.

#### **P19**[JEE Main][practice][Euler form]Using [formula] notation, show that [formula] .

Using $e^{i\theta}$ notation, show that $(1+i)^{10} = 32i$.

<details>
<summary>Answer + Reasoning</summary>

$1+i = \sqrt2\, e^{i\pi/4}$, so 
$$ (1+i)^{10} = (\sqrt2)^{10} e^{i10\pi/4} = 2^5 e^{i5\pi/2} = 32 e^{i(\pi/2 + 2\pi)}
        = 32 e^{i\pi/2} = \mathbf{32i}. $$
 The reduction $5\pi/2 \equiv \pi/2 \pmod{2\pi}$ is the only real work — De Moivre did the rest.

</details>

#### **P20**[Olympiad][practice][Euler form · geometry]Let [formula] be four quarter-turn- adjacent points [formula] (a square on the…

Let $z_0, z_1, z_2, z_3$ be four quarter-turn-*adjacent* points $e^{i\alpha}, e^{i(\alpha+\pi/2)}, e^{i(\alpha+\pi)}, e^{i(\alpha+3\pi/2)}$ (a square on the unit circle). Show that 
$$ z_0 + z_1 + z_2 + z_3 = 0 $$
 and deduce: *any* regular $n$-gon centered at the origin has vertex-sum $0$.

<details>
<summary>Answer + Reasoning</summary>

Factor $e^{i\alpha}$: 
$$ e^{i\alpha}(1 + i + (-1) + (-i)) = e^{i\alpha}\cdot 0 = 0. $$
 The bracket is $1 + e^{i\pi/2} + e^{i\pi} + e^{i3\pi/2}$ — the sum of all fourth roots of 1, which is $0$ because $t^4 - 1 = (t-1)(t^3+t^2+t+1)$ and the other three roots satisfy $t^3+t^2+t+1 = 0$.


**General $n$:** the vertices are $re^{i\alpha}e^{2\pi ik/n}$, $k = 0,\dots,n-1$; factor $re^{i\alpha}$ and sum the geometric series with ratio $\omega = e^{2\pi i/n} \ne 1$: 
$$ \sum_{k=0}^{n-1}\omega^k = \frac{\omega^n - 1}{\omega - 1} = 0. \qquad \square $$
 This "vertex-sum zero" fact — proved once here — is used as a black box in Chapters 3, 5 and 6 (loci, Ptolemy, Napoleon).

</details>


### 2.7 Mistake checklist & the bridge to Chapter 3

> **⚠ Mistake checklist (this chapter)**
>
> - **Principal argument is in $(-\pi, \pi]$** — $\operatorname{Arg}(-1) = \pi$, never $-\pi$; quadrant IV gives *negative* arguments, e.g. $\operatorname{Arg}(1-i\sqrt3) = -\pi/3$.
> - **Angles are mod $2\pi$** — "$=$" on arguments silently means "$= \cdots \bmod 2\pi$"; write the modulus sign when it matters.
> - **$z^n$ has n roots, not one** — "the cube root of 8" as a JEE answer is always the set $\{2, -1\pm i\sqrt3\}$ unless "principal" is specified.
> - **Never cancel roots across products:** $\sqrt{z}\sqrt{w} \ne
>         \sqrt{zw}$ for complex $z, w$ in general (the principal-root branch cuts bite); for *algebraic* root-finding, always solve $z^n = w$ from scratch as in §2.4.
> - **$e^{i\theta}$ has modulus 1** — $e^{i\theta} \ne 1$ in general; $e^{i\theta} = 1 \iff \theta \equiv 0 \bmod 2\pi$.

**Where this is going.** The $n$-th roots of $1$ themselves — $1, \omega, \omega^2, \dots$ with $\omega = e^{2\pi i/n}$ — are the next chapter's heroes. Two facts from this chapter carry straight across: (i) they form a regular $n$-gon (vertex-sum zero, §2.6), and (ii) $1 + \omega + \cdots + \omega^{n-1} = 0$ (geometric-series ratio $\omega \ne 1$). Chapter 3 turns these into a computation toolkit: sums of powers, filter formulas for "every r-th term" binomial sums, and the product $\prod_{k=1}^{n-1}(1 - \omega^k) = n$.



---

