---
title: "Complex Numbers — Course Notes"
aliases:
  - Complex Numbers
  - Complex-Numbers
module: "Complex-Numbers"
type: index
tags:
  - complex-numbers
  - module
  - index
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 🧪 [[Complex-Numbers — Paper|Olympiad Paper]] · ✅ [[Complex-Numbers — Solutions|Solutions]] · 📘 [[Complex-Numbers — Theory|Theory Reference]]

# Complex-Numbers — Complete Course Notes


*Module · Complex Numbers*

# Complex Numbers

From the equation that has no answer — $x^2 = -1$ — to a geometric language where multiplication is rotation and Olympiad geometry collapses into algebra. Every formula is *derived from reasoning*, never memorized.

`6 chapters · complete` `50 in-context questions (P1–P51)` `38-question paper + solutions` `SVG diagrams` `JEE Advanced → Olympiad`

### ★ How to use these notes

**Read in order — do not skip the "why" boxes.** Each chapter is built in layers: *concept → first-principles reasoning → JEE theory → Olympiad extension*. The single most important habit this module trains: **switching languages** — algebraic ($a+bi$, conjugates, modulus) when you need to compute, geometric (the plane, distances, rotations) when you need insight. Nearly every JEE Advanced and Olympiad problem in this subject is solved by doing exactly that.

> [!tip] Key Idea — the two languages
>
> Algebraic: $z = a + bi$, conjugate $\bar z$, modulus $|z|$, division via $\bar z$. Geometric: $z$ is a point/vector in the plane; $|z-w|$ is a distance; $|zw| = |z||w|$ says multiplication stretches; $\times i$ is a quarter-turn. **One object, two faces — problems are solved at the interface.**


### ▣ The roadmap

**Diagram**

![Diagram](assets/fig-01.svg)

| Chapter | Core idea | Signature results |
| --- | --- | --- |
| 1 · Foundations | $\mathbb{C}$ as pairs with one rule: $i^2 = -1$ | conjugate, modulus, distance, triangle inequality, parallelogram law, $\times i$ = rotation |
| 2 · Polar & De Moivre | stretch $\times$ rotate | $z = r(\cos\theta + i\sin\theta)$, $(\cos\theta+i\sin\theta)^n$, n-th roots |
| 3 · Roots of unity | the $n$-th roots form a regular polygon | $1+\omega+\cdots+\omega^{n-1}=0$, factorizations, $\binom$-sums via filters |
| 4 · JEE Advanced | the interface language | $\|z-a\|=r$, arg conditions, $\|z\|$-inequalities, solving $z$ equations, loci |
| 5 · Olympiad geometry | geometry collapses to algebra | Ptolemy as $\|z_1z_3+w_1w_3\|=\|z_1z_2\|\|w_2w_3\|$-style identities, van Aubel, regular $n$-gons |
| 6 · Synthesis | the whole toolkit | 38-question paper + full solutions |


### 1 Chapters

[[01-foundations-algebra-and-the-plane| Chapter 1 · Foundations Why $i$ must exist, the algebra of $a+bi$, conjugate and division, the complex plane, modulus as distance, triangle inequality, parallelogram law, and the first taste of rotation. 6 sections · 8 in-context questions · 2 SVG diagrams · **ready →** ]] [[02-polar-form-and-de-moivre| Chapter 2 · Polar form & De Moivre Argument, polar (trigonometric) form, De Moivre's theorem with a real proof, powers, and the n-th roots of a complex number. 7 sections · 12 questions (P9–P20) · 1 SVG · **ready →** ]] [[03-roots-of-unity| Chapter 3 · Roots of unity $\omega$, the regular-polygon structure, sums like $1+\omega+\omega^2=0$, product formulas, and the roots-of-unity filter for binomial sums. 5 sections · 8 questions (P21–P28) · 1 SVG · **ready →** ]] [[04-jee-advanced-core| Chapter 4 · JEE Advanced core Equations mixing $z$ and $\bar z$, circles from modulus, arcs from argument, minimizing $|z-a|$, ellipses, and ranges over regions. 7 sections · 11 questions (P29–P39) · 2 SVG · **ready →** ]] [[05-geometry-via-complex-numbers| Chapter 5 · Geometry via complex numbers Rotation as the engine: the equilateral condition, Ptolemy from a one-line identity, Van Aubel, Napoleon, centroid distance-sums, area and circumcenter. 6 sections · 6 questions (P41–P46) · 1 SVG · **ready →** ]] [[06-synthesis| Chapter 6 · Synthesis & stretch Unit-circle configurations (rectangle, hexagon), product identities from $z^n-1$, the Joukowski map $z+1/z$, and the British Flag theorem. 5 sections · 5 questions (P47–P51) · 1 SVG · **ready →** ]] [[Complex-Numbers — Paper| 📝 Olympiad & JEE Advanced paper 38 questions in eight sections (A–H), JEE Main → Olympiad, covering every chapter's signature move — with short-form answers. 38 questions · 8 sections · **take it →** ]] [[Complex-Numbers — Solutions| 🔑 Full worked solutions Every question solved: method name first, then the computation, then a check — both methods where two exist. 38 solutions · **open →** ]] 


### ! One-page mindset

Three habits separate people who "know complex numbers" from people who can solve olympiad problems with them:

- **Distance, not coordinates.** The moment you see $|z-a|$, stop computing: it is the distance from $a$. Loci problems are geometry problems wearing algebra clothes.
- **Conjugate = reflection.** $\bar z$ mirrors across the real axis; $\frac{z_1}{z_2}$ is the "shape" (rotation + scale) that takes $z_2$ to $z_1$. Perpendicularity, collinearity and similarity all become one-line statements.
- **Verify small cases first.** Before trusting an identity in $n$ roots of unity, test $n=2,3,4$ by hand — the arithmetic either clicks or it doesn't.



## Roadmap

- **Chapter 1**: Ch 1 · Foundations — Algebra & the Plane — 5 sections · 8 questions
- **Chapter 2**: Ch 2 · Polar Form & De Moivre — 7 sections · 12 questions
- **Chapter 3**: Ch 3 · Roots of Unity — 5 sections · 8 questions
- **Chapter 4**: Ch 4 · JEE Advanced Core — 7 sections · 11 questions
- **Chapter 5**: Ch 5 · Geometry via Complex Numbers — 6 sections · 6 questions
- **Chapter 6**: Ch 6 · Synthesis — 5 sections · 5 questions
- **Olympiad Paper**: Olympiad Paper · 38 questions — 
- **Solutions**: Olympiad Paper · Solutions & marking guide


## Chapters

```dataview
TABLE chapter AS "Ch", level AS "Level"
FROM "notes/Complex-Numbers"
WHERE chapter
SORT chapter ASC
```
