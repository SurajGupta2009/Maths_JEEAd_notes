# Contributing — the Notes Standard

This repo is a single, well-ordered course of hand-crafted math notes that
takes a student from board-level basics to **JEE Advanced and Olympiad
mathematics** — every formula *derived from reasoning*, every answer
numerically verified.

**The notes are Markdown.** You author them directly in
`notes/<Module>/<chapter-folder>/`. The standalone HTML mindmaps in
`published/` are the *legacy distribution format* of the four existing
modules — frozen, verified, but no longer the medium future notes are
written in.

Everything in this file is a rule. New content that violates any of it does
not get merged. AI agents: read [AGENTS.md](AGENTS.md), which restates the
machine-checkable invariants.

---

## 1. Repo layout (canonical)

```
Maths_JEEAd_notes/
├── notes/                         # ★ the canonical, hand-authored Markdown notes
│   ├── README.md                  # index of all modules (chapter-folder links)
│   └── <Module-Slug>/
│       ├── README.md                      # module index / course map (hand-written)
│       ├── 00-WELL-ORDERED-THEORY.md      # hand-written one-page theory reference
│       ├── 01-<chapter-slug>/
│       │   └── README.md                  # ALL of chapter 1's content lives here
│       ├── 02-<chapter-slug>/
│       │   └── README.md
│       ├── …                          (exactly six chapter folders)
│       ├── olympiad-paper.md                  # 30+ Q, sections A–H, answer lines
│       ├── olympiad-paper-solutions.md        # same Q-ids, full solutions
│       ├── <slug>-complete.md                 # GENERATED single-file snapshot — never edit
│       └── assets/fig-XX.svg                  # module's diagrams
├── published/                     # legacy standalone HTML mindmaps (frozen)
│   └── <Module-Slug>/
│       ├── <slug>-mindmap.html    # one standalone expandable course file
│       └── assets/notes.css       # per-module stylesheet copy
├── docs/                          # hand-written course reference docs
│   ├── ROADMAP.md                        # basics → JEE Main → JEE Adv → Olympiad
│   ├── JEE-ADVANCED-OLYMPIAD-COVERAGE.md # coverage proof per topic
│   ├── FORMATTING-GUIDE.md               # formatting & pipeline conventions
│   └── DIAGRAMS.md                       # SVG + Mermaid diagram catalog
├── templates/
│   ├── CHECKLIST.md               # the 10-step new-module procedure
│   ├── markdown/                  # skeletons: module index, chapter, paper,
│   │                              #   solutions, 00-WELL-ORDERED-THEORY
│   └── html/                      # legacy HTML skeletons (reference only)
├── tools/
│   ├── verify-md.py               # Markdown quality gate (math, blocks, image links)
│   ├── build-complete.py          # notes/ → <slug>-complete.md snapshots
│   ├── convert_to_md.py           # legacy re-export: published/ HTML maps → notes/
│   ├── build-mindmap.py           # legacy: source HTML → published/ mindmaps
│   ├── verify-math.py             # HTML tag + MathJax delimiter gate (published/, templates/)
│   ├── verify-mindmap.py          # published-map integrity checks
│   └── mindmap-overrides.json     # per-module label pins & CLI aliases (legacy)
└── README.md · CONTRIBUTING.md · AGENTS.md
```

Layout rules:

- **One module = exactly one folder under `notes/`.** Kebab-case slug
  (`Quadratic-Equations/`). No module files at the repo root, no module files
  outside `notes/` and `published/`.
- **One chapter = one folder, named after the chapter**
  (`01-counting-basics/`), and **all of that chapter's content is inside the
  folder** (its `README.md` is the chapter's full text). Never split a
  chapter's main text across multiple files, and never store a chapter's
  content outside its folder.
- Chapter folder name = `NN-` + the chapter title lowercased, non-alphanumerics
  collapsed to single hyphens, `&` → `and`
  (`Ch 4 · Binomial Coefficients & Identities` →
  `04-binomial-coefficients-and-identities/`).
- Diagrams live in the module's `assets/` — `fig-XX.svg`, numbered in order of
  first appearance. From module-level files reference `assets/fig-XX.svg`;
  from inside a chapter folder reference `../assets/fig-XX.svg`.
- `notes/<Module>/<slug>-complete.md` is **generated** by
  `tools/build-complete.py` (whole course in one file) — never hand-edit it;
  edit the chapter folders and rebuild.
- `published/` is frozen: its maps and stylesheets are not modified by new
  content work. `notes/<Module>/00-WELL-ORDERED-THEORY.md` and all chapter
  folders are hand-authored.

## 2. Module anatomy

Each module under `notes/` contains exactly:

| Path | Role |
|---|---|
| `README.md` | module index / course map: pitch, how-to-use, box legend, roadmap table |
| `00-WELL-ORDERED-THEORY.md` | one-page revision reference: statement → proof idea → small-case check |
| `01-…/README.md` … `06-…/README.md` | six chapters — **one folder per chapter, all content inside** |
| `olympiad-paper.md` | 30+ questions (aim 38–40), sections A–H, short `**Answer:**` lines |
| `olympiad-paper-solutions.md` | full solutions, same Q-ids verbatim, marking notes |
| `<slug>-complete.md` | generated single-file snapshot (do not edit) |
| `assets/fig-XX.svg` | the module's diagrams |

The six-chapter arc is always:
**foundations → machinery → core → applications → frontier → synthesis**.

### The scope ladder (what every module must cover)

Content is well-ordered along one axis:

> **board-level basics → JEE Main → JEE Advanced → Olympiad frontier**

- **JEE Main** — direct single-step application of a rule.
- **JEE Advanced** — multi-step, casework, hidden structure, optimization.
- **Olympiad** — bijections, involutions, double counting, invariants,
  generating functions.

Every topic is presented at each level it reaches; chapter 6 collects the
module's Olympiad frontier.

### First-principles rule

- Every formula is **derived from reasoning** inside a First Principles
  callout — never stated as "memorize this".
- Every counting claim carries a **small-case check** (explicit listing at
  $n=3,4$).
- Where a topic has two languages (algebra ↔ geometry), both are given —
  e.g. complex numbers ↔ the plane, conics ↔ reflection/optics.
- Dependencies are respected: nothing is used before it is established.

### Callout taxonomy (fixed — use these blockquote forms, nothing else)

| Callout | Form |
|---|---|
| First principles | `> **⛁ First Principles — <why it is true>**` |
| Key idea | `> **💡 Key Idea — <takeaway technique>**` |
| Common trap | `> **⚠ Common Trap — <the classic mistake>**` |
| Olympiad extension | `> **★ Olympiad Extension — <frontier version>**` |
| Note | `> **📌 Note — <…>**` |
| Verification habit | `> **✔ Check — <…>**` |
| Bridge to next chapter | `> **➡ Bridge — <…>**` |
| Named identity | `> **🧮 Identity: <name>**` |

Body lines of a callout are `>`-prefixed lines under the title.

### Question formats (fixed)

- **Worked example `S#`** — `#### **S1**[JEE Main][solved][<technique>]<one-line preview>`
  followed by the full statement, then
  `<details><summary>Answer + Reasoning</summary> … </details>`.
- **Practice `P#`** — `#### **P1**[JEE Adv][practice][<concept>]<one-line preview>`
  with the same details block.
- **Paper `Q#`** — `#### **Q1**[JEE Main][<concept>]<one-line preview>` with the
  statement and a short `**Answer:** <answer>` line (no details block).
- Every solution: **method name first (bold) → full derivation → a check**.
  Where two standard methods exist, give both.

### Numbering (fixed)

- **Practice `P1…Pn`** — continuous *per module*, unique across all six
  chapter folders, woven **between** theory sections (not dumped at chapter
  ends).
- **Worked examples `S1…Sn`** — continuous per module, like P.
- **Paper `Q1…Qn`** — continuous across lettered sections **A–H**, difficulty
  ramping Main → Advanced → Olympiad; minimum 30, aim 38–40. The solutions
  file reuses the Q-ids verbatim and answers every one.
- **Difficulty tags**: `[JEE Main]` · `[JEE Adv]` · `[Olympiad]`, plus role
  tags `[solved]`, `[practice]`, and topic tags.

## 3. Authoring rules (Markdown)

- **Math**: inline `$…$`, display `$$…$$` (GitHub/MathJax native). Real math
  only — **never** fake prose math with Unicode glyphs (`x²`, `√`, `≤`, `≈`).
  Diagrams may use literal readable text inside SVG.
- **Diagrams**: SVG files in `assets/` + `![caption](…)`; Mermaid flowcharts
  for key ideas where they add clarity. Every image link must resolve
  (enforced by `tools/verify-md.py`).
- **Collapsible answers**: `<details><summary>Answer + Reasoning</summary>`
  blocks; keep them balanced.
- **Tables**: GitHub Flavored Markdown.
- **Language**: English; notation consistent with the published modules.

## 4. Correctness (non-negotiable)

1. **Every paper answer is verified numerically in pure Python** (stdlib only
   — no numpy, no sympy) **before** the solutions file is written. Unverified
   answer ⇒ reject your own work. Keep the throwaway script out of the repo;
   paste its verdict into the PR description.
2. Math delimiters must balance in every file (`$$` pairs, inline `$` pairs) —
   the gate enforces it.
3. Before merging, manually review every chapter folder for complete
   expandable theory, every question/answer, correct rendering and every
   figure.

## 5. New-module procedure

Follow [templates/CHECKLIST.md](templates/CHECKLIST.md) (10 steps) top to
bottom. In one line each:

1. `notes/<Module-Slug>/` + `assets/`.
2. Module index `README.md` from `templates/markdown/module-index.md`.
3. Six chapter folders `01-…/README.md` from `templates/markdown/chapter.md`.
4. Number P/S continuously per module (gate checks duplicates).
5. `olympiad-paper.md` — ≥30 Q, A–H, answer lines — **verify all answers in
   pure Python first**.
6. `olympiad-paper-solutions.md` — method first → derivation → check.
7. `00-WELL-ORDERED-THEORY.md` — the one-page reference.
8. Diagrams in `assets/`, Mermaid where it helps.
9. `python3 tools/build-complete.py <Module>` → run `tools/verify-md.py` and
   the published-gates → snapshot must be stable.
10. Update [README.md](README.md) + `notes/README.md`, open a PR — do not
    push to `main`. Paste verifier outputs in the PR description.

## 6. Verify before you commit (CI enforces all of this)

```bash
python3 tools/verify-md.py                     # notes/**.md — math balance, blocks, image links
python3 tools/build-complete.py all            # regenerate <slug>-complete.md snapshots
git diff --exit-code -- 'notes/*-complete.md'  # snapshots must be stable

# legacy gates (published HTML must never drift):
python3 tools/verify-math.py                   # every *.html — all PASS
python3 tools/verify-mindmap.py all            # published-map integrity
python3 tools/build-mindmap.py all             # source-less maps are safe no-ops
```

Non-PASS output ⇒ fix the file. Do not commit, do not loosen the verifier to
make content pass.

## 7. Hard rules (NEVER)

- Never hand-edit a generated `<slug>-complete.md` file.
- Never split a chapter's main text across multiple files, or store a
  chapter's content outside its folder.
- Never add dependencies, build systems, frameworks, caches or binary image
  files (SVG only) — pure stdlib Python, no new tooling (maintainer opted
  out).
- Never rename a published module folder or its map files in `published/`,
  and never place module files at the repo root.
- Never commit paper answers that were not numerically verified.
- Never push to `main` or force-push — work on a branch and open a PR.
- Never casually alter curated content: requested corrections must pass
  `tools/verify-md.py` and a fresh snapshot rebuild before merging.
