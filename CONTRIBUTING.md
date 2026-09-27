# Contributing — the Notes Standard (Obsidian vault)

This repo is a single, well-ordered course of hand-crafted maths notes, authored
**directly in Markdown inside an [Obsidian](https://obsidian.md) vault**. It
takes a student from board-level basics to **JEE Advanced and Olympiad
mathematics** — every formula *derived from reasoning*, every answer
*numerically verified*.

Everything in this file is a rule. New content that violates it does not get
merged. AI agents: read [AGENTS.md](AGENTS.md), which restates the
machine-checkable invariants and the exact commands.

---

## 1. Vault layout (canonical)

```
Maths_JEEAd_notes/
├── Home.md                      # vault entry point (Dataview dashboards)
├── .obsidian/                   # vault config + enabled plugins (share it)
├── notes/                       # ★ the canonical, hand-authored notes
│   └── <Module>/                # one folder per module, kebab-case slug
│       ├── <Module>.md                  # module index / course map
│       ├── 01-<chapter-slug>.md         # ONE note = ONE chapter …
│       ├── … 02-… 03-… 04-… 05-… 06-…   #   exactly six chapter notes
│       ├── <Module> — Theory.md         # one-page theory reference
│       ├── <Module> — Paper.md          # Olympiad paper (sections A–H)
│       ├── <Module> — Solutions.md      # full worked solutions
│       └── assets/fig-XX.svg            # the module's diagrams
├── docs/                        # ROADMAP · coverage · formatting · diagrams
├── templates/markdown/          # skeletons for a new module
├── tools/                       # verify-md.py · verify-structure.py · …
└── README.md · CONTRIBUTING.md · AGENTS.md
```

Layout rules:

- **One module = exactly one folder under `notes/`.** Kebab-case slug
  (`Quadratic-Equations/`). No module files at the repo root, none outside
  `notes/`.
- **One chapter = one note** named `NN-<chapter-slug>.md`, and **all of that
  chapter's content lives in the note**. Never split a chapter across files.
- Chapter note name = `NN-` + the chapter title lowercased, non-alphanumerics
  collapsed to single hyphens, `&` → `and`
  (`Ch 4 · Binomial Coefficients & Identities` →
  `04-binomial-coefficients-and-identities.md`).
- **Note names are globally unique** across the vault, so `[[Wikilinks]]`
  resolve without ambiguity. Chapter slugs are naturally unique; the module
  notes are prefixed with the module name (`PnC — Paper.md`, `Complex-Numbers —
  Theory.md`, …).
- Diagrams live in the module's `assets/` — `fig-XX.svg`, numbered in order of
  first appearance. From any module note reference `assets/fig-XX.svg`. Every
  image link must resolve (enforced by `tools/verify-md.py`).

## 2. Note anatomy (frontmatter + callouts)

Every note starts with YAML frontmatter:

```yaml
---
title: "Chapter 1 — Counting Basics"
aliases: ["Counting Basics", "Ch 1 — Counting Basics"]
module: "PnC"
module_title: "PnC"
chapter: 1
level: foundations            # foundations | machinery | core | applications | frontier | synthesis
tags: [pnc, chapter, foundations]
created: 2026-09-27
---
```

The six-chapter arc is always **foundations → machinery → core → applications →
frontier → synthesis** (chapter 6 holds the Olympiad frontier).

### The scope ladder (what every module must cover)

> **board-level basics → JEE Main → JEE Advanced → Olympiad frontier**

- **JEE Main** — direct single-step application of a rule.
- **JEE Advanced** — multi-step, casework, hidden structure, optimization.
- **Olympiad** — bijections, involutions, double counting, invariants,
  generating functions.

### First-principles rule

- Every formula is **derived from reasoning** inside a First Principles callout
  — never "memorize this".
- Every counting claim carries a **small-case check** (explicit listing at
  $n=3,4$).
- Where a topic has two languages (algebra ↔ geometry), both are given.

### Callout taxonomy (fixed — Obsidian callout types)

| Callout | Obsidian form |
|---|---|
| First principles | `> [!abstract] First Principles — <why it is true>` |
| Key idea | `> [!tip] Key Idea — <takeaway technique>` |
| Common trap | `> [!warning] Common Trap — <the classic mistake>` |
| Olympiad extension | `> [!example] Olympiad Extension — <frontier version>` |
| Note | `> [!note] <…>` |
| Formula / box | `> [!info] <…>` |
| Named identity / result | `> [!quote] <name>` |
| Checklist | `> [!success] <…>` |
| Bridge to next chapter | `> [!info] Bridge — <…>` |

Body lines of a callout are `>`-prefixed lines under the title. The vault ships
a CSS snippet (`.obsidian/snippets/maths-vault.css`) that tints these types.

### Question formats (fixed)

- **Worked example `S#`** — `#### **S1**[JEE Main][solved][<technique>]preview`
  then the statement, then `<details><summary>Answer + Reasoning</summary> … </details>`.
- **Practice `P#`** — `#### **P1**[JEE Adv][practice][<concept>]preview` with the
  same `<details>` block.
- **Paper `Q#`** — `#### **Q1**[JEE Main][<concept>]preview` with the statement
  and a short `**Answer:**` line (no details block; answers live in the paper).
- Every solution: **method name first (bold) → full derivation → a check**. Give
  **both** standard methods wherever two exist.

### Numbering (fixed)

- **Practice `P1…Pn`** and **worked examples `S1…Sn`** — continuous *per module*
  and unique across the six chapter notes, woven **between** theory sections.
  (PnC is the one legacy exception: it numbers `P1–P8` within each chapter.)
- **Paper `Q1…Qn`** — continuous across lettered sections **A–H**, difficulty
  ramping Main → Advanced → Olympiad; minimum 30, aim 38–40. The Solutions note
  reuses the Q-ids verbatim and answers every one.

## 3. Authoring rules (Markdown in Obsidian)

- **Math**: inline `$…$`, display `$$…$$`. Real math only — never fake prose
  math with Unicode glyphs (`x²`, `√`, `≤`). SVG diagram labels may use literal
  readable text.
- **Links**: use `[[Wikilinks]]` for internal navigation (module home, prev/next
  chapter, paper, solutions). Every note carries a `> [!info] Navigation` callout.
- **Collapsible answers**: `<details><summary>Answer + Reasoning</summary>` blocks;
  keep them balanced.
- **Diagrams**: SVG files in `assets/` + `![caption](assets/fig-XX.svg)`; Mermaid
  flowcharts for key ideas where they add clarity.
- **Tables**: GitHub Flavored Markdown. **Language**: English.

## 4. Correctness (non-negotiable)

1. **Every paper answer is verified numerically in pure Python** (stdlib only —
   no numpy, no sympy) **before** the Solutions note is written. Unverified
   answer ⇒ reject your own work. Keep the throwaway script out of the repo;
   paste its verdict into the PR description.
2. Math delimiters must balance in every file (the gate enforces it).
3. Before merging, manually review every chapter note for complete expandable
   theory, every question/answer, correct rendering and every figure.

## 5. New-module procedure

Follow [templates/CHECKLIST.md](templates/CHECKLIST.md) (10 steps). In one line
each:

1. `notes/<Module-Slug>/` + `assets/`.
2. Module index `<Module>.md` from `templates/markdown/module-index.md`.
3. Six chapter notes `01-…/README.md`→`01-….md` from
   `templates/markdown/chapter.md` (frontmatter + callouts + navigation).
4. Number P/S continuously per module.
5. `<Module> — Paper.md` — ≥30 Q, A–H, answer lines — **verify all answers in
   pure Python first**.
6. `<Module> — Solutions.md` — method first → derivation → check.
7. `<Module> — Theory.md` — the one-page reference.
8. Diagrams in `assets/`, Mermaid where it helps.
9. Run the gates (below); fix anything that fails.
10. Update [[Home]] + [README.md](README.md) + [docs/ROADMAP.md](docs/ROADMAP.md),
    open a PR — do not push to `main`.

## 6. Verify before you commit (CI enforces this)

```bash
python3 tools/verify-md.py          # notes/**.md — frontmatter, math, blocks, images
python3 tools/verify-structure.py   # 6 chapters/module, unique names, P/S numbering
```

Non-PASS output ⇒ fix the file. Do not commit, do not loosen the verifier to make
content pass.

## 7. Hard rules (NEVER)

- Never split a chapter's main text across multiple files, or store a chapter's
  content outside its note.
- Never add dependencies, build systems, frameworks, caches or binary image
  files (SVG only) — pure stdlib Python, no new tooling (maintainer opted out).
- Never create two notes with the same basename (ambiguous Wikilinks).
- Never commit paper answers that were not numerically verified.
- Never push to `main` or force-push — work on a branch and open a PR.
