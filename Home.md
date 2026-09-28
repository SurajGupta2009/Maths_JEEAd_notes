---
title: "Home — JEE Advanced + Olympiad Maths"
aliases:
  - "Vault Home"
  - "Start Here"
type: home
tags:
  - home
  - index
created: 2026-09-27
---

# 🧮 JEE Advanced + Olympiad Maths — Obsidian Vault

Hand-crafted, first-principles maths notes that climb one ladder:
**board basics → JEE Main → JEE Advanced → Olympiad frontier.** Every formula
is *derived*, never memorised; every paper answer is *numerically verified*.

> [!tip] How to use this vault
> - **One note per module.** Each `<Module>.md` is the complete note for that
>   module — six chapters (`# Chapter 1`…`# Chapter 6`, foundations → machinery →
>   core → applications → frontier → synthesis) plus a theory appendix. The
>   paper and its solutions are two separate notes.
> - **Navigate with Wikilinks** — every note has a `Navigation` callout at the
>   top (module home · paper · solutions). Use the **Graph view** (left ribbon)
>   to see the whole course.
> - **Callouts** carry the pedagogy: `[!abstract]` = First Principles,
>   `[!tip]` = Key Idea, `[!warning]` = Common Trap, `[!example]` = Olympiad
>   Extension, `[!note]`/`[!info]`/`[!quote]` = formulas & named results.
> - **Math is real LaTeX** — `$…$` inline, `$$…$$` display (renders via
>   Obsidian's built-in MathJax).
> - **Dataview** powers the dashboard below (install the *Dataview* community
>   plugin if the table is empty — see [[README]]).

## 📚 Modules — all 18 complete

108 chapters · 756 paper questions · 122 Olympiad Extension callouts.

| Module | Folder | Chapters | Paper Qs | Start |
|---|---|---|---|---|
| **PnC** — Permutations & Combinations | `notes/PnC` | 6 | 50 | [[PnC]] |
| **Complex Numbers** | `notes/Complex-Numbers` | 6 | 48 | [[Complex-Numbers]] |
| **Binomial Theorem** | `notes/Binomial-Theorem` | 6 | 48 | [[Binomial-Theorem]] |
| **Conic Sections** | `notes/Conic-Sections` | 6 | 48 | [[Conic-Sections]] |
| **Limits & Continuity** | `notes/Limits-and-Continuity` | 6 | 39 | [[Limits-and-Continuity]] |
| **Differentiation & Methods** | `notes/Differentiation-and-Methods` | 6 | 38 | [[Differentiation-and-Methods]] |
| **Applications of Derivatives** | `notes/Applications-of-Derivatives` | 6 | 46 | [[Applications-of-Derivatives]] |
| **Integration** | `notes/Integration` | 6 | 46 | [[Integration]] |
| **Differential Equations** | `notes/Differential-Equations` | 6 | 41 | [[Differential-Equations]] |
| **Coordinate Geometry — Lines & Circles** | `notes/Coordinate-Geometry-Lines-and-Circles` | 6 | 46 | [[Coordinate-Geometry-Lines-and-Circles]] |
| **3D Geometry** | `notes/3D-Geometry` | 6 | 46 | [[3D-Geometry]] |
| **Vectors** | `notes/Vectors` | 6 | 46 | [[Vectors]] |
| **Matrices & Determinants** | `notes/Matrices-and-Determinants` | 6 | 36 | [[Matrices-and-Determinants]] |
| **Quadratic Equations** | `notes/Quadratic-Equations` | 6 | 34 | [[Quadratic-Equations]] |
| **Inequalities** | `notes/Inequalities` | 6 | 36 | [[Inequalities]] |
| **Sequences & Series** | `notes/Sequences-and-Series` | 6 | 34 | [[Sequences-and-Series]] |
| **Trigonometry** | `notes/Trigonometry` | 6 | 36 | [[Trigonometry]] |
| **Probability** | `notes/Probability` | 6 | 38 | [[Probability]] |

Each module is one complete-notes note (six chapters + theory appendix), plus its
Olympiad paper and its full solutions.

## 📖 Modules in this vault (Dataview)

```dataview
TABLE module AS "Module", rows.file.link AS "Notes"
FROM "notes"
WHERE type = "notes"
SORT file.name ASC
```

## 🎯 Status

**Complete.** Every module is written from basics to the Olympiad frontier, with
a paper and full solutions. See [[ROADMAP]] for the syllabus coverage and
[[CONTRIBUTING]] for the authoring standard.
