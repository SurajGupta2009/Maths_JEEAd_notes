---
title: "PnC — Course Notes"
aliases:
  - PnC
module: "PnC"
type: index
tags:
  - pnc
  - module
  - index
created: 2026-09-27
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 🧪 [[PnC — Paper|Olympiad Paper]] · ✅ [[PnC — Solutions|Solutions]] · 📘 [[PnC — Theory|Theory Reference]]

# PnC — Complete Course Notes


*JEE Advanced → Olympiad Ladder*

# Permutations & Combinations

A complete conceptual build-up: from the two primitive rules of counting, through every JEE Advanced weapon, to the Olympiad frontier — Burnside, Catalan, partitions and generating functions. Every formula is *derived from reasoning*, never memorized.

`6 chapters` `~90 worked & practice questions` `SVG diagrams` `40-question Olympiad paper + full solutions`



### ★ How to use these notes

**Read in order — do not skip the "why" boxes.** Each chapter is built in layers: *concept → first-principles reasoning → JEE theory → Olympiad extension*. If you can only remember the formula and not the argument behind it, you will lose the moment a problem twists the situation — which is exactly what JEE Advanced and Olympiads do.

- **Colored boxes** — First Principles = the actual reasoning a mathematician uses; Key Idea = the takeaway technique; Common Trap = the classic mistake; Olympiad Extension = the frontier version.
- **Questions are placed in context** — a solved example right after the technique that solves it, plus practice sets with difficulty tags: [JEE Main] [JEE Adv] [Olympiad]
- **The Olympiad paper at the end** (38 questions) is the exam: attempt it after Chapter 6, without solutions. The [[PnC — Solutions|solution key]] is separate and complete.
- **Small-case habit** — the single most repeated advice: whenever you get a counting answer, *list all cases for a tiny instance* and check. It catches 90% of errors.


### ▣ The roadmap

Here is the logical skeleton of the entire chapter. Notice that everything — even the hardest Olympiad theorem — is an application of **one of three moves**: *construct* (product rule), *split* (sum rule / cases), or *match up* (bijection / double counting).

**Diagram**

![Diagram](assets/fig-01.svg)


### 1–6 Chapters

[[01-counting-basics| Chapter 1 · Foundations Counting Basics What "counting" really means: the product rule, the sum rule, complements, bijections as the ultimate weapon, and the mistake checklist. ]] [[02-permutations| Chapter 2 · Order matters Permutations $nPr$, repeated letters, circular permutations, adjacency & gap methods, fixed relative order, and derangements — with the $n!/e$ surprise. ]] [[03-combinations| Chapter 3 · Order irrelevant Combinations Why divide by $r!$, Pascal's triangle, restricted selections, stars & bars, compositions, multinomial coefficients, first look at partitions. ]] [[04-binomial-coefficients-and-identities| Chapter 4 · Coefficients count Binomial Theorem & Double Counting The theorem proved by counting, the double-counting method as a proof machine, the full identity toolkit, coefficient extraction with bounds. ]] [[05-advanced-methods| Chapter 5 · JEE Advanced weapons Inclusion–Exclusion, Pigeonhole & Recurrences IE from a Venn diagram to rook polynomials; pigeonhole principles and their classic proofs; counting by recurrence (tilings, strings, Fibonacci in Pascal). ]] [[06-olympiad-theory| Chapter 6 · The frontier Olympiad Theory Generating functions as a real tool, lattice paths & the reflection principle, Catalan numbers, Burnside–Pólya, integer partitions & Euler, Stirling numbers, and a gallery of Olympiad lemmas. ]]


### ∑ Exam paper

[[PnC — Paper| The Capstone Olympiad-Level Paper — 40 Questions Eight sections covering every concept of the chapter: arrangements, stars & bars, identities, inclusion–exclusion, pigeonhole, lattice paths & Catalan, Burnside & partitions, and synthesis (Erdős–Szekeres, IMO classics). Difficulty-tagged. ]] [[PnC — Solutions| Attempt first, then open Full Solutions Key Complete step-by-step solutions for all 38 questions, with the reasoning that motivates each step — not just algebra. ]]


### ! One-page mindset

> [!abstract] First Principles — the only rule of the game
>
> To count a set of objects **never reach for a formula first**. Ask: *Can I put these objects in one-to-one correspondence with something whose size I already know?* Or: *Can I build each object by a sequence of independent choices?* If the answer to either is yes, the count falls out. Every tool in this course — $nC_r$, stars & bars, inclusion–exclusion, Burnside's lemma — is just a packaged version of one of these two moves, discovered to be useful over and over.

> [!warning] Common Trap — the three sins of counting
>
> **1. Overcounting** — the same final object produced by two different choice paths. **2. Undercounting** — cases that are not exhaustive, or objects that "look impossible" but exist. **3. Broken independence** — assuming "3 choices, then 3 choices" when the second count depends on the first in a way you didn't track. The cure for all three: *verify a small case by brute force*.



## Roadmap

- **Chapter 1**: Ch 1 · Counting Basics — 7 sections · 11 questions
- **Chapter 2**: Ch 2 · Permutations — 6 sections · 13 questions
- **Chapter 3**: Ch 3 · Combinations — 7 sections · 14 questions
- **Chapter 4**: Ch 4 · Binomial Coefficients & Identities — 6 sections · 13 questions
- **Chapter 5**: Ch 5 · Advanced Methods — 4 sections · 15 questions
- **Chapter 6**: Ch 6 · Olympiad Theory — 7 sections · 13 questions
- **Olympiad Paper**: Olympiad Paper · 40 questions — 
- **Solutions**: Olympiad Paper · Solutions & marking guide


## Chapters

```dataview
TABLE chapter AS "Ch", level AS "Level"
FROM "notes/PnC"
WHERE chapter
SORT chapter ASC
```
