---
title: "Diagrams — SVG + Mermaid Catalog"
aliases: ["Diagrams", "Figures"]
module: "docs"
type: catalog
tags: [diagrams, svg, mermaid]
created: 2026-09-27
---

# Diagrams — SVG + Mermaid Catalog

> Every diagram lives as an SVG in the module's `notes/<Module>/assets/fig-XX.svg`
> and is augmented with a Mermaid flowchart for native GitHub/Obsidian rendering.

## PnC — Permutations & Combinations

### 1. Product Rule — Decision Tree

**SVG**: `notes/PnC/assets/fig-02.svg` — Tree with 3 colors × 2 styles = 6 leaves

**Mermaid**:
```mermaid
flowchart TD
    Start([Start]) --> Red[Red]
    Start --> Blue[Blue]
    Start --> Black[Black]
    Red --> RB["red·bold"]
    Red --> RI["red·ital"]
    Blue --> BB["blue·bold"]
    Blue --> BI["blue·ital"]
    Black --> KB["blk·bold"]
    Black --> KI["blk·ital"]
```

**Theory**: Product rule works iff every branch at level $i$ has same $n_i$ children. Leaves = $n_1 n_2 \cdots n_k$.

### 2. Circular Permutations — Rotation Equivalence

**SVG**: `notes/PnC/assets/fig-03.svg` — Linear vs circular arrangements

**Mermaid**:
```mermaid
flowchart LR
    subgraph Linear [Linear: n!]
        A[ABC]
        B[BCA]
        C[CAB]
    end
    subgraph Circular [Circular: (n-1)!]
        D[(ABC) same as BCA]
    end
    A -- rotate --> B
    B -- rotate --> C
    C -- rotate --> A
    A -.-> D
```

**Theory**: $n$ rotations give same necklace → divide by $n$. If flip allowed (bracelet), divide by $2n$ → $(n-1)!/2$.

### 3. Pascal's Triangle & Hockey-Stick

**SVG**: `notes/PnC/assets/fig-05.svg` (approx) — Triangle with $\binom{n}{k} = \binom{n-1}{k-1}+\binom{n-1}{k}$

**Mermaid**:
```mermaid
flowchart TD
    R0["Row 0: 1"]
    R1["Row 1: 1 1"]
    R2["Row 2: 1 2 1"]
    R3["Row 3: 1 3 3 1"]
    R4["Row 4: 1 4 6 4 1"]
    R0 --> R1
    R1 --> R2
    R2 --> R3
    R3 --> R4
    R4 --> HS["Hockey-stick: C(r,r)+C(r+1,r)+...+C(n,r)=C(n+1,r+1)"]
```

**Identity**: $\sum_{i=r}^n \binom{i}{r} = \binom{n+1}{r+1}$ — telescope via Pascal.

### 4. Stars and Bars — Distribution

**SVG**: `notes/PnC/assets/fig-06.svg` — Stars and bars visualization

**Mermaid**:
```mermaid
flowchart LR
    A["Distribution: 10 identical balls into 3 distinct boxes"] --> B["***|*|****** = (3,1,6)"]
    B --> C["n stars, k-1 bars"]
    C --> D["Choose positions of bars: C(n+k-1,k-1)"]
    D --> E["Positive: C(n-1,k-1)"]
```

**Formulas**:
- Non-negative: $\binom{n+k-1}{k-1}$
- Positive: $\binom{n-1}{k-1}$
- Compositions of $n$: $2^{n-1}$

### 5. Lattice Paths & Reflection Principle

**SVG**: `notes/PnC/assets/fig-08.svg` — Grid paths from $(0,0)$ to $(a,b)$

**Mermaid**:
```mermaid
flowchart TD
    O["(0,0)"] --> Paths["Total monotone paths: C(a+b,b)"]
    Paths --> Good["Good: never above diagonal y=x"]
    Paths --> Bad["Bad: crosses y=x+1"]
    Bad --> Reflect["Reflect up to first crossing<br>Start becomes (-1,1)"]
    Reflect --> BadCount["Bad = C(2n,n-1)"]
    Good --> Catalan["Catalan C_n = C(2n,n) - C(2n,n-1) = C(2n,n)/(n+1)"]
```

**Ballot**: $\frac{p-q}{p+q}\binom{p+q}{q}$ — $p$ votes for A, $q$ for B, $p>q$, probability A always ahead.

### 6. Young Diagram — Partition Conjugation

**SVG**: `notes/PnC/assets/fig-09.svg` — Young diagram transpose

**Mermaid**:
```mermaid
flowchart LR
    subgraph P ["5+3+2+1"]
        A1["XXXXX"]
        A2["XXX"]
        A3["XX"]
        A4["X"]
    end
    P -- transpose rows↔cols --> C
    subgraph C ["4+3+2+1+1"]
        B1["XXXX"]
        B2["XXX"]
        B3["XX"]
        B4["X"]
        B5["X"]
    end
```

**Bijection**: Conjugation is involution → number of partitions of $n$ equals number with largest part = number of parts, etc. Euler distinct = odd via generating functions.

### 7. Burnside — Necklace Counting

**Mermaid**:
```mermaid
flowchart TD
    G["Group G acts on colorings"]
    G --> Fix["Fix(g) = colorings fixed by g"]
    Fix --> Burnside["Orbits = (1/|G|) Σ |Fix(g)|"]
    Burnside --> Necklace["Necklaces: (1/n) Σ_{d|n} φ(d) k^{n/d}"]
    Burnside --> Bracelet["Bracelets: include reflections"]
    Burnside --> Cube["Cube: 24 rotations -> 23 colorings with 2 colors"]
```

### 8. Inclusion-Exclusion — Sieve

**Mermaid**:
```mermaid
flowchart TD
    A["|A ∪ B| = |A|+|B|-|A∩B|"]
    A --> B["|A∪B∪C| = Σ|A_i| - Σ|A_i∩A_j| + |A∩B∩C|"]
    B --> C["General: Σ (-1)^{k+1} Σ |intersection of k sets|"]
    C --> D["Derangements: D_n = n! Σ (-1)^k/k!"]
    C --> E["Onto: k!S(n,k) = Σ (-1)^j C(k,j)(k-j)^n"]
```

---

## Complex Numbers

### 9. Complex Plane — Loci

**SVG**: `notes/Complex-Numbers/assets/fig-02.svg` — Plane with points, circles

**Mermaid**:
```mermaid
flowchart TD
    A["z = a+bi ↔ (a,b)"]
    A --> B["|z| = √(a²+b²) = distance from origin"]
    B --> C["|z-w| = distance between points"]
    C --> D["|z-z0|=r → circle center z0 radius r"]
    C --> E["|z-a|=|z-b| → perp bisector of ab"]
    C --> F["Re z = c → vertical line x=c"]
    C --> G["|z-a|+|z-b|=2k → ellipse foci a,b"]
    C --> H["|z-a|=k|z-b| → Apollonius circle"]
```

### 10. Multiplication = Rotation

**SVG**: `notes/Complex-Numbers/assets/fig-03.svg` — Rotation by $i$

**Mermaid**:
```mermaid
flowchart LR
    A["z = a+bi"] -- "× i = -b+ai" --> B["90° CCW, |iz|=|z|"]
    B -- "× i" --> C["180°: -a-bi"]
    C -- "× i" --> D["270°: b-ai"]
    D -- "× i" --> A
    A -- "× re^{iθ} = stretch r, rotate θ" --> E["General multiplication"]
```

**Theorem**: $|zw|=|z||w|$, $\arg(zw)=\arg z + \arg w$.

### 11. Roots of Unity — Regular Polygon

**Mermaid**:
```mermaid
flowchart TD
    A["ω = e^{2πi/n}, ω^n=1"] --> B["n roots = regular n-gon on unit circle"]
    B --> C["1+ω+...+ω^{n-1}=0"]
    C --> D["Factorization: x^n-1 = ∏(x-ω^k)"]
    D --> E["Filter: (1/n)Σ ζ^{-rk} picks every r-th term"]
    E --> F["Binomial sums: Σ_{k≡r mod n} C(n,k)"]
```

---

## Binomial Theorem

### 12. Decision Tree — What $(a+b)^n$ Counts

**Mermaid**:
```mermaid
flowchart TD
    A["(a+b)^3 = (a+b)(a+b)(a+b)"] --> B["Pick one letter per bracket"]
    B --> C["2×2×2=8 pick-lists: aaa, aab, aba, baa, abb, bab, bba, bbb"]
    C --> D["Group by #b's: C(3,0)=1, C(3,1)=3, C(3,2)=3, C(3,3)=1"]
    D --> E["Coefficient = #pick-lists = binomial coefficient"]
```

### 13. Substitution Engines

**Mermaid**:
```mermaid
flowchart LR
    A["f(x)=(1+x)^n=Σ C(n,k)x^k"] --> B["f(1)=2^n = sum all coeffs"]
    A --> C["f(-1)=0 = even-odd"]
    A --> D["(f(1)+f(-1))/2 = sum even positions"]
    A --> E["(f(1)-f(-1))/2 = sum odd positions"]
    A --> F["f'(1)=n2^{n-1}=Σ kC(n,k)"]
```

### 14. Negative Binomial — Stars and Bars GF

**Mermaid**:
```mermaid
flowchart TD
    A["(1-x)^{-k} = Σ C(n+k-1,k-1)x^n"] --> B["Stars and bars GF"]
    B --> C["(1+x)^n = Σ C(n,k)x^k"]
    C --> D["(1-x)^{-1}=1+x+x^2+..."]
    D --> E["Coefficient extraction with bounds via IE"]
```

---

## Conic Sections

### 15. Conic Family — Eccentricity

**Mermaid**:
```mermaid
flowchart TD
    A["Focus-directrix: e = dist to focus / dist to directrix"] --> B["e<1: ellipse"]
    A --> C["e=1: parabola"]
    A --> D["e>1: hyperbola"]
    B --> E["Second-degree: ax²+2hxy+by²+...=0"]
    E --> F["h²-ab <0 ellipse, =0 parabola, >0 hyperbola"]
```

### 16. Parabola — Tangent & Reflection

**Mermaid**:
```mermaid
flowchart LR
    A["y²=4ax, focus (a,0), directrix x=-a"] --> B["Parametric: at²,2at"]
    B --> C["Tangent: ty = x+at²"]
    C --> D["Normal: y = -tx+2at+at³"]
    D --> E["Reflection: parallel rays -> focus"]
    E --> F["Applications: satellite dish, headlight"]
```

### 17. Ellipse — Squashed Circle

**Mermaid**:
```mermaid
flowchart TD
    A["x²/a²+y²/b²=1, b²=a²(1-e²)"] --> B["Parametric: a cosθ, b sinθ"]
    B --> C["Tangent: x cosθ/a + y sinθ/b =1"]
    C --> D["Director circle: x²+y²=a²+b² (perp tangents)"]
    D --> E["Reflection: focus -> other focus"]
    E --> F["Sum distances =2a constant"]
```

### 18. Hyperbola — Asymptotes

**Mermaid**:
```mermaid
flowchart TD
    A["x²/a²-y²/b²=1, b²=a²(e²-1)"] --> B["Asymptotes: y=±(b/a)x (limiting tangents)"]
    B --> C["Rectangular: xy=c², asymptotes axes"]
    C --> D["Parametric: a secθ, b tanθ"]
    D --> E["Director: x²+y²=a²-b²"]
    E --> F["Reflection: focus -> away from other focus"]
```

### 19. Unified Machinery — T=0, S1, Polar

**Mermaid**:
```mermaid
flowchart TD
    A["S=0 conic"] --> B["T=0 tangent at (x1,y1)"]
    A --> C["S1=0 chord with midpoint (x1,y1): T=S1"]
    A --> D["Pair of tangents: SS1=T²"]
    D --> E["Chord of contact: T=0 from external point"]
    E --> F["Polar: locus of chord of contact, pole-polar duality"]
    F --> G["Director circle: locus of perp tangents"]
```

### 20. Confocal & Reflection Proofs

**Mermaid**:
```mermaid
flowchart TD
    A["Confocal family: same foci"] --> B["Ellipses and hyperbolas intersect orthogonally"]
    B --> C["Elliptic coordinates"]
    C --> D["Reflection proofs via angle bisector of tangent"]
    D --> E["Parabola: tangent makes equal angles with line to focus and axis"]
    E --> F["Ellipse: tangent makes equal angles with lines to foci"]
    F --> G["Hyperbola: tangent bisects external angle"]
```

---

## How Diagrams Are Used in Markdown

1. **SVG** — Exact figure from HTML, preserved for offline use:
   ```md
   ![Fig 1.1 — Product rule tree](assets/fig-02.svg)
   ```

2. **Mermaid** — Added for GitHub native rendering, same concept but interactive:
   ````md
   ```mermaid
   flowchart TD
       Start --> Red
   ```
   ````

3. **Both** — Every major concept has SVG + Mermaid, so notes work offline (SVG) and online (Mermaid) — dual redundancy.

---

*All figures are stored as `notes/<Module>/assets/fig-XX.svg`; see [FORMATTING-GUIDE.md](FORMATTING-GUIDE.md) for how they are referenced.*
