# AGENTS.md — non-negotiable repo rules (Obsidian vault)

You are editing a repo of hand-crafted **JEE Advanced + Olympiad maths notes**,
authored in **Markdown inside an [Obsidian](https://obsidian.md) vault**. The
content standard lives in [CONTRIBUTING.md](CONTRIBUTING.md); this file restates
the machine-checkable invariants and the exact commands. When they disagree,
CONTRIBUTING.md wins for content and this file wins for commands.

## Structure (MUST)

```
notes/<Module-Slug>/        ★ canonical hand-authored Markdown — one folder per module
.obsidian/                  vault config + enabled plugins (share; don't commit workspace/cache)
docs/                       ROADMAP, coverage, formatting guide, diagrams
templates/markdown/         note skeletons (module index, chapter, paper, solutions, theory)
tools/                      verify-md.py, verify-structure.py, migrate-to-obsidian.py (legacy)
```

- **One module = one folder under `notes/`** (kebab-case slug). No module files
  at the repo root; no module files outside `notes/`.
- **One chapter = one note** `NN-<chapter-slug>.md`, containing ALL of the
  chapter's content. Exactly six chapter notes per module, numbered `01`…`06`
  (`foundations → machinery → core → applications → frontier → synthesis`).
- Chapter note name = `NN-` + chapter title lowercased, non-alphanumerics → single
  hyphens, `&` → `and`.
- **Note basenames are globally unique** across the vault (clean `[[Wikilinks]]`).
  Module notes are module-prefixed: `<Module>.md`, `<Module> — Paper.md`,
  `<Module> — Solutions.md`, `<Module> — Theory.md`.
- Diagrams: `assets/fig-XX.svg` per module, referenced as `assets/fig-XX.svg`.
  Every image link must resolve.
- Every note starts with YAML frontmatter defining `title` and `module`/`type`.

## Math & content (MUST)

- Markdown math: inline `$…$`, display `$$…$$`. NEVER fake prose math with
  Unicode glyphs (`x² √ ≤ ≈ ℝ`); SVG labels may use literal readable text.
- Callouts use Obsidian types only: `[!abstract]` First Principles · `[!tip]` Key
  Idea · `[!warning]` Common Trap · `[!example]` Olympiad Extension · `[!note]` ·
  `[!info]` formula box · `[!quote]` named result · `[!success]` checklist.
- Questions: `#### **S1**[JEE Main][solved][technique]preview` (worked) ·
  `#### **P1**[JEE Adv][practice][concept]preview` (practice) ·
  `#### **Q1**[JEE Main][concept]preview` (paper, short `**Answer:**` line).
  Answers in `<details><summary>Answer + Reasoning</summary>` blocks (not in the
  paper). Solution = **method name first**, derivation, then a check.
- Numbering: `P1…Pn`/`S1…Sn` continuous per module, unique across chapter notes,
  interleaved between theory sections (PnC is the legacy per-chapter exception);
  paper `Q1…Qn` continuous across A–H, ≥30 (aim 38–40); solutions repeat Q-ids
  verbatim.

## Correctness (MUST)

- Every paper answer is verified **numerically in pure Python (stdlib only — no
  numpy, no sympy)** BEFORE the Solutions note is written. Unverified answer ⇒
  reject your own work.
- Math delimiters must balance in every file (the gate enforces it).
- Before finishing, manually review every chapter note for complete theory,
  every question/answer, rendering and every figure.

## Verify (MUST, before finishing)

```bash
python3 tools/verify-md.py          # every notes/**.md — frontmatter, math, blocks, images
python3 tools/verify-structure.py   # 6 chapters/module, unique names, P/S numbering
```

Non-PASS output ⇒ fix the file; do not commit, do not loosen the verifier to make
content pass.

## Forbidden (NEVER)

- Never hand-edit `.obsidian/workspace*`, `.obsidian/cache`, or `.trash/` (they
  are git-ignored per-machine state).
- Never split a chapter's main text across multiple files, or store a chapter's
  content outside its note.
- Never create two notes with the same basename.
- Never add dependencies, build systems, frameworks, caches or binary image files
  (SVG only) (maintainer opted out).
- Never rename module folders or their notes inconsistently; never place module
  files at the repo root.
- Never push to `main` or force-push; work on a branch and open a PR.
- Never commit answers that were not numerically verified.

## New module procedure

Follow `templates/CHECKLIST.md` (10 steps): `notes/<Module-Slug>/` + `assets/` →
`<Module>.md` from `templates/markdown/module-index.md` → six chapter notes from
`templates/markdown/chapter.md` → continuous P/S numbering → `<Module> — Paper.md`
(≥30 Q, A–H; **pure-Python verification first**) → `<Module> — Solutions.md` →
`<Module> — Theory.md` → diagrams in `assets/` → run both gates → update [[Home]],
[README.md](README.md) and [docs/ROADMAP.md](docs/ROADMAP.md) → PR.
