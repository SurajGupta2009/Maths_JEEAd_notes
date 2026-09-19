# JEE Advanced + Olympiad Coverage — Detailed Checklist

> This document proves that theory **up to JEE Advanced and Olympiad** is covered and well-ordered in the Markdown notes.

> File paths below are relative to `notes/<Module>/` (e.g.
> `01-counting-basics/` = the folder `notes/PnC/01-counting-basics/`).

## How Theory Is Organized

Each module follows **First Principles → JEE Main → JEE Advanced → Olympiad**:

1. **First Principles Box** (⛁) — derivation from definition, not memorization
2. **JEE Main** — single-step application, formula direct
3. **JEE Advanced** — multi-step, casework, hidden structure, optimization
4. **Olympiad** (★) — bijection, double counting, generating functions, invariance

Every formula has a **proof** and a **small-case verification** ($n=3,4$ explicit listing).

---

## PnC — Permutations & Combinations

### Chapter 1: Counting Basics — 7 Sections

| Topic | Level | Coverage | Markdown Location |
|-------|-------|----------|-------------------|
| What does "to count" mean? Finite sets | Board | Definition, examples | `01-counting-basics/` §1.1 |
| Product rule | JEE Main | Statement, proof by induction on $k$, decision tree | §1.2 + Mermaid + `fig-02.svg` |
| Sum rule | JEE Main | Disjoint union, exhaustive check | §1.3 |
| Complement principle | JEE Main | $|\bar A| = |U|-|A|$, at least one | §1.4 |
| Bijections & involutions | JEE Adv | Half subsets even size via toggle, even/odd permutations equal | §1.5 + worked proofs |
| Double counting | Olympiad | $\sum k\binom{n}{k}=n2^{n-1}$ committee+chair, sum of integers | §1.6 |
| Mistake checklist | All | Labeled vs unlabeled, order, independence, exhaustive/disjoint, small-case | §1.7 |

**JEE Adv Questions**: S1–S4 (solved), P1–P7 (practice) — product+cases, complement+product, bijection, committee

**Olympiad Extension**: Involutions, double counting as proof machine

### Chapter 2: Permutations — 6 Sections

| Topic | Level | Coverage |
|-------|-------|----------|
| $^nP_r = n!/(n-r)!$, $0!=1$ empty bijection | Main | Definition, proof, $n=3$ verification |
| Identical objects $\frac{n!}{n_1!n_2!\cdots}$ | Adv | Overcounting argument, $n=4$ example |
| Circular $(n-1)!$, necklace $(n-1)!/2$ | Adv | Rotation equivalence, divide by $n$, Mermaid diagram, `fig-03.svg` |
| Bundle method (together) | Main | Treat as block, $n=3$ listing |
| Gap method (no two adjacent) | Adv | $_{n+1}P_r$, stars and bars connection |
| Derangements $D_n$, rencontres | Olympiad | IE proof, recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$, nearest integer to $n!/e$, $\binom{n}{k}D_{n-k}$ |

### Chapter 3: Combinations — 6 Sections

| Topic | Level | Coverage |
|-------|-------|----------|
| $\binom{n}{r}$, symmetry, Pascal | Main | Complement bijection, conditioning on element |
| Restricted selections | Adv | Must include/exclude, gap method |
| Hockey-stick $\sum \binom{i}{r} = \binom{n+1}{r+1}$ | Adv | Pascal telescope, Mermaid, `fig-05.svg` |
| Stars and bars $\binom{n+k-1}{k-1}$ | Adv | Non-negative, positive, compositions $2^{n-1}$, Mermaid + `fig-06.svg` |
| Multinomial $\frac{n!}{n_1!\cdots n_k!}$ | Adv | Distribution, distinct terms $\binom{n+2}{2}$ |
| Partitions $p(n)$ | Olympiad | No closed form, GF $\prod \frac{1}{1-x^k}$, Euler distinct=odd, Young diagram conjugation `fig-09.svg` |

### Chapter 4: Binomial Coefficients & Identities — 5 Sections

| Topic | Level | Coverage |
|-------|-------|----------|
| Binomial theorem via counting | Main | $(x+y)^n$, pick-lists, $2^n$, even/odd split |
| Double counting toolkit | Adv | Committee+chair, Vandermonde $\sum \binom{r}{k}\binom{s}{n-k}=\binom{r+s}{n}$, $\sum \binom{n}{k}^2=\binom{2n}{n}$ |
| Negative binomial $(1-x)^{-k}$ | Adv | Stars and bars GF, $\binom{n+k-1}{k-1}$ |
| Bounded coefficient extraction | Adv | IE with upper bounds, inclusion-exclusion for $\le$ constraints |
| Generating function proofs | Olympiad | Formal power series, convolution = independent stages |

### Chapter 5: Advanced Methods — 5 Sections

| Topic | Level | Coverage |
|-------|-------|----------|
| Inclusion-Exclusion | Adv | $|\cup A_i|$, rook polynomials, derangements |
| Pigeonhole (Dirichlet) | Adv | $\lceil n/k \rceil$, van der Waerden $W(2,3)=9$, $R(3,3)=6$, Erdős–Szekeres |
| Recurrence counting | Adv | Tilings Fibonacci in Pascal, $a_n = a_{n-1}+a_{n-2}$ |
| Rook polynomials | Adv | Board, inclusion-exclusion for forbidden positions |
| Probabilistic method intro | Olympiad | $\mathbb{E}<1 \Rightarrow \exists$, Erdős |

### Chapter 6: Olympiad Theory — 8 Sections

| Topic | Level | Coverage | Diagram |
|-------|-------|----------|---------|
| Generating functions OGF $A(x)=\sum a_n x^n$ | Olympiad | Operations, catalog, Fibonacci GF, sequence $\frac{1}{1-B(x)}$ | - |
| Lattice paths $\binom{a+b}{b}$ | Olympiad | Monotone, reflection principle, ballot $\frac{p-q}{p+q}\binom{p+q}{q}$ | `fig-08.svg` + Mermaid |
| Catalan $C_n=\frac{1}{n+1}\binom{2n}{n}$ | Olympiad | 5 definitions, Dyck paths, triangulations, $\binom{2n}{n}-\binom{2n}{n+1}$ | Reflection Mermaid |
| Burnside $\frac{1}{|G|}\sum |\text{Fix}(g)|$ | Olympiad | Necklaces $N(n,k)=\frac{1}{n}\sum_{d|n}\varphi(d)k^{n/d}$, bracelet, cube 24 rotations = 23 colorings | Mermaid |
| Pólya enumeration | Olympiad | Cycle index, weighted counting | - |
| Partitions & Euler | Olympiad | GF $\prod \frac{1}{1-x^k}$, pentagonal theorem, recurrence $p(n)=p(n-1)+p(n-2)-p(n-5)-\cdots$, conjugation Young | `fig-09.svg` + Mermaid |
| Stirling $S(n,k)$, Bell $B_n$ | Olympiad | Recurrence $kS(n-1,k)+S(n-1,k-1)$, IE closed form, onto $k!S(n,k)$, $B_n=\sum S(n,k)$ | - |
| Sperner, Erdős–Szekeres, Cycle lemma | Olympiad | LYM random chain, $(r-1)(s-1)+1$, Dvoretzky–Motzkin | - |

**Paper**: 40 questions A–G + stretch, 4–5 hours, full solutions

---

## Complex Numbers — 6 Chapters

### Coverage

| Chapter | JEE Main | JEE Advanced | Olympiad |
|---------|----------|--------------|----------|
| 1 Foundations | $i^2=-1$, $a+bi$, $\bar z$, $|z|$, division $\frac{z\bar w}{|w|^2}$, $0!$-like $0=0+0i$, no zero divisors → field, triangle inequality, parallelogram law, loci $|z-z_0|=r$, $|z-a|=|z-b|$, $\text{Re}z=c$ | $|z|=1$ min $|z-3-4i|$ via triangle, reverse triangle, midpoint $\frac{z_1+z_2}{2}$ | - |
| 2 Polar & De Moivre | $z=r(\cos\theta+i\sin\theta)$, $|zw|=|z||w|$, $\times i$ = $90^\circ$ CCW | $\arg(zw)=\arg z+\arg w$, $n$-th roots regular $n$-gon, powers | - |
| 3 Roots of Unity | $\omega=e^{2\pi i/n}$, $\omega^n=1$ | $1+\omega+\cdots+\omega^{n-1}=0$, $x^n-1$ factorization | Filter $\frac{1}{n}\sum \zeta^{-rk}$, regular polygons algebraic, cyclotomic |
| 4 JEE Adv Core | Equations in $z$, $\bar z$, $|z|$ | Apollonius $|z-a|=k|z-b|$ circle, $\arg\frac{z-a}{z-b}=\theta$ arc, optimization via triangle inequality, $iz=\bar z$ line $y=-x$ | - |
| 5 Geometry via Complex | - | Section formula, rotation $e^{i\theta}$, collinearity, concyclicity | Ptolemy, van Aubel, complex bash, $z\bar z=|z|^2$ |
| 6 Synthesis Paper | 38 Q A–H, $i$ cycle to geometry, with solutions | - | - |

**Diagrams**: Complex plane `fig-02.svg` + Mermaid loci, multiplication=rotation `fig-03.svg` + Mermaid, roots of unity regular polygon Mermaid

---

## Binomial Theorem — 6 Chapters

| Chapter | JEE Main | JEE Advanced | Olympiad |
|---------|----------|--------------|----------|
| 1 What $(a+b)^n$ counts | $(a+b)^n=\sum \binom{n}{k}a^{n-k}b^k$ via pick-lists, Pascal as census, $2^n$, even/odd split, general term, symmetry, Pascal rule via conditioning | Substitution $f(1),f(0),f(-1)$, half-sum $(f(1)\pm f(-1))/2$ | Bijection subset counting, committee+chair, double counting as technique |
| 2 Coefficient machinery | $T_{k+1}=\binom{n}{k}a^{n-k}b^k$, middle term, numerically greatest term | Coeff of $x^m$ in $(1+x+x^2)^n$, $(1+x)^n(1+1/x)^n$, greatest coefficient | - |
| 3 Three identity engines | Substitution, bijection $k\binom{n}{k}=n\binom{n-1}{k-1}$, $\sum k\binom{n}{k}=n2^{n-1}$ | Double counting Vandermonde, $\sum \binom{n}{k}^2=\binom{2n}{n}$ | Generating function proofs |
| 4 Beyond non-negative integer | - | Negative binomial $(1+x)^{-n}=\sum (-1)^k\binom{n+k-1}{k}x^k$, $(1-x)^{-k}$, infinite series $|x|<1$, multinomial $(a+b+c)^n$, $\frac{n!}{i!j!k!}$, $\binom{n+2}{2}$ distinct terms | - |
| 5 Size, growth, extremes | Middle largest, unimodal | Greatest term, greatest coefficient, $\binom{2n}{n}\sim\frac{4^n}{\sqrt{\pi n}}$, inequalities $\binom{n}{k}\le\frac{n^k}{k!}$, bounding sums | - |
| 6 Divisibility, parity, primes | - | $\binom{p}{k}\equiv0\pmod p$ prime $p$ | Lucas, Kummer, $v_p(n!)$, $\binom{2n}{n}$ divisibility, parity via binary |

**Diagrams**: Decision tree Mermaid, substitution engines Mermaid, negative binomial stars-bars GF Mermaid

---

## Conic Sections — 6 Chapters

| Chapter | JEE Main | JEE Advanced | Olympiad |
|---------|----------|--------------|----------|
| 1 Conic family | Focus-directrix $e$, $e<1$ ellipse, $e=1$ parabola, $e>1$ hyperbola, general second-degree $ax^2+2hxy+by^2+...=0$, $h^2-ab$ | Why $e$ determines shape, rotation removing $xy$ | Classification via eigenvalues |
| 2 Parabola | $y^2=4ax$, focus $(a,0)$, directrix $x=-a$, latus rectum $4a$, parametric $at^2,2at$ | Chord $ty=x+at^2$, tangent $ty=x+at^2$, normal $y=-tx+2at+at^3$, chord of contact, director circle | Reflection parallel→focus, proof via tangent angle bisector |
| 3 Ellipse | $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$, foci $(\pm ae,0)$, $b^2=a^2(1-e^2)$, latus rectum $2b^2/a$, parametric $a\cos\theta,b\sin\theta$ | Tangent $\frac{x\cos\theta}{a}+\frac{y\sin\theta}{b}=1$, director $x^2+y^2=a^2+b^2$, auxiliary circle, chord, normal | Reflection focus→focus, sum distances $2a$ constant |
| 4 Hyperbola | $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$, $b^2=a^2(e^2-1)$, asymptotes $y=\pm\frac{b}{a}x$, rectangular $xy=c^2$, parametric $a\sec\theta,b\tan\theta$ | Asymptotes limiting tangents, director $x^2+y^2=a^2-b^2$, conjugate hyperbola | Reflection focus→away |
| 5 Tangents, normals, chords, polars | $T=0$ tangent, $S_1=0$ chord with midpoint $T=S_1$ | Pair tangents $SS_1=T^2$, chord of contact, polar, pole, director locus perp tangents, family coaxal | Pole-polar duality, harmonic bundles, confocal orthogonal |
| 6 Olympiad frontier | - | Second-degree homogeneous, rotation, $S=0$ locus | Confocal same foci orthogonal, elliptic coordinates, reflection proofs, classification |

**Diagrams**: Conic family eccentricity Mermaid, parabola tangent+reflection Mermaid, ellipse squashed circle + director Mermaid, hyperbola asymptotes Mermaid, unified $T=0,S_1$, polar Mermaid, confocal orthogonal Mermaid, plus 11 SVG figures from HTML

---

## Verification

### Math Delimiters — PASS

```bash
python3 tools/verify-math.py
# PnC: balance OK | math D40/bad0 I2337/bad0 $$17/bad0 -> PASS
# Complex-Numbers: D146/bad0 I2102/bad0 $$2/bad0 -> PASS
# Binomial-Theorem: D28/bad0 I1753/bad0 $$0/bad0 -> PASS
# Conic-Sections: D42/bad0 I2187/bad0 $$0/bad0 -> PASS
```

### Mindmap Completeness — PASS

```bash
python3 tools/verify-mindmap.py all
# All modules PASS: top nodes 9, heroes 9, q nodes 139/159 etc., visuals, audit counts, no source cards, box summaries, links, SVG ids, tag balance, math delimiters
```

### Markdown Generation

```bash
python3 tools/convert_to_md.py all
# Generated 6 chapters + paper + solutions per module
# PnC: 6 ch + 10 figs
# Complex-Numbers: 6 ch + 7 figs
# Binomial-Theorem: 6 ch + 1 fig
# Conic-Sections: 6 ch + 1 fig
# Combined *-complete.md per module
```

---

## Well-Ordered Guarantee

1. **Dependencies respected**: Product rule before permutations, permutations before combinations, combinations before binomial coefficients, binomial before advanced methods, advanced before Olympiad (generating functions need binomial, Burnside needs group action, partitions need GF)
2. **Spiral**: Each chapter revisits earlier tools (e.g., Chapter 4 binomial uses Chapter 1 product rule + Chapter 3 combinations + Chapter 2 permutations for identical objects)
3. **Small-case habit**: Every counting claim has $n=3,4$ explicit verification in markdown
4. **Two languages**: Algebra ↔ Geometry translation explicit (complex numbers: $a+bi$ ↔ $(a,b)$; conics: focus-directrix ↔ second-degree)
5. **Mistake checklist**: Before every problem set, common traps listed (labeled vs unlabeled, order, independence, exhaustive/disjoint, sign flip $-2i^2=+2$, modulus vs equality, $T=0$ vs $S_1$)

---

*This checklist is generated from the HTML mindmaps and the Markdown conversion — see `docs/ROADMAP.md` for the visual roadmap and `docs/DIAGRAMS.md` for all diagrams.*
