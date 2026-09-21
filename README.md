# Maths_JEEAd_notes

Hand-crafted, well-ordered math study notes — authored in **Markdown** — that
walk a student from board-level basics to **JEE Advanced and Olympiad
mathematics**: every formula *derived from reasoning*, every answer
numerically verified.

Each module is one folder under `notes/` with **one chapter folder per
chapter** (all of a chapter's content inside), an Olympiad paper with full
solutions, diagrams, and a one-page well-ordered theory reference. The four
existing modules additionally ship a frozen standalone HTML mindmap in
`published/` (the legacy one-file distribution).

[![verify](https://img.shields.io/github/actions/workflow/status/SurajGupta2009/Maths_JEEAd_notes/verify.yml?branch=main&style=flat-square&label=verify)](https://github.com/SurajGupta2009/Maths_JEEAd_notes/actions/workflows/verify.yml)

## Modules

| Module | Status | Chapters | Practice Qs | Paper Qs | Notes | One-file HTML |
|---|---|---|---|---|---|---|
| **PnC** · Permutations & Combinations | ✅ complete | 6 | 47 (P1–P8 per chapter) | 40 (A–G + stretch) | [notes](notes/PnC/README.md) | [open map](published/PnC/pnc-mindmap.html) |
| **Complex Numbers** | ✅ complete | 6 | 50 (P1–P51, continuous) | 38 (A–H) | [notes](notes/Complex-Numbers/README.md) | [open map](published/Complex-Numbers/complex-numbers-mindmap.html) |
| **Binomial Theorem** | ✅ complete | 6 | 47 (P1–P47, continuous) | 38 (A–H) | [notes](notes/Binomial-Theorem/README.md) | [open map](published/Binomial-Theorem/binomial-theorem-mindmap.html) |
| **Conic Sections** | ✅ complete | 6 | 48 (P1–P48, continuous) | 38 (A–H) | [notes](notes/Conic-Sections/README.md) | [open map](published/Conic-Sections/conic-sections-mindmap.html) |

## Repo structure

```
Maths_JEEAd_notes/
├── notes/                     # ★ canonical Markdown notes — one folder per module
│   ├── README.md              # index of all modules
│   └── <Module-Slug>/
│       ├── README.md                  # module index / course map
│       ├── 00-WELL-ORDERED-THEORY.md  # one-page theory reference (hand-written)
│       ├── 01-<chapter-slug>/         # one folder per chapter —
│       │   └── README.md              #   ALL of the chapter's content lives here
│       ├── … 02-… 03-… 04-… 05-… 06-…
│       ├── olympiad-paper.md          # 30+ Q, sections A–H, answer lines
│       ├── olympiad-paper-solutions.md
│       ├── <slug>-complete.md         # GENERATED single-file snapshot (never edit)
│       └── assets/fig-XX.svg          # the module's diagrams
├── published/                 # legacy standalone HTML mindmaps (frozen)
│   └── <Module-Slug>/
│       ├── <slug>-mindmap.html        # one standalone expandable course file
│       └── assets/notes.css
├── docs/                      # course reference docs
│   ├── ROADMAP.md                            # basics → JEE Main → JEE Adv → Olympiad
│   ├── JEE-ADVANCED-OLYMPIAD-COVERAGE.md     # per-topic coverage checklist
│   ├── FORMATTING-GUIDE.md                   # formatting & pipeline conventions
│   └── DIAGRAMS.md                           # SVG + Mermaid diagram catalog
├── templates/
│   ├── CHECKLIST.md               # the 10-step new-module procedure
│   ├── markdown/                  # skeletons for module index, chapter, paper, …
│   └── html/                      # legacy HTML skeletons (reference only)
├── tools/
│   ├── verify-md.py               # Markdown quality gate (math, blocks, image links)
│   ├── build-complete.py          # notes/ → <slug>-complete.md snapshots
│   ├── convert_to_md.py           # legacy re-export: published/ → notes/
│   ├── build-mindmap.py           # legacy: source HTML → published/ mindmaps
│   ├── verify-math.py             # HTML tag + MathJax delimiter quality gate
│   ├── verify-mindmap.py          # published-map integrity checks
│   └── mindmap-overrides.json     # per-module label pins & CLI aliases
└── README.md · CONTRIBUTING.md (the notes standard) · AGENTS.md · .gitignore
```

## Quick start

- **Read a module (Markdown, canonical):** open
  `notes/<Module>/README.md` — the chapter folders, paper and solutions are
  linked from there. Everything renders natively on GitHub (MathJax + Mermaid).
- **One-file offline mode (legacy HTML):** open a map from `published/` in a
  browser — e.g. `published/PnC/pnc-mindmap.html`. Internet is required for
  the MathJax CDN (everything else works offline).
- To check tooling: Python 3, stdlib only.

## The notes standard (how notes are written)

The rules for writing and maintaining JEE Advanced + Olympiad notes are
defined in [CONTRIBUTING.md](CONTRIBUTING.md) — in short:

- **Scope ladder** — every module is well-ordered
  *board basics → JEE Main → JEE Advanced → Olympiad frontier* in the same
  six-chapter arc (foundations → machinery → core → applications → frontier
  → synthesis).
- **First principles** — every formula is derived, never memorized; every
  counting claim carries a small-case check ($n=3,4$); both languages are
  given where a topic has two (algebra ↔ geometry).
- **Fixed vocabularies** — callout taxonomy (⛁ First Principles · 💡 Key Idea
  · ⚠ Common Trap · ★ Olympiad Extension · …), question formats
  (`S#`/`P#`/`Q#` with difficulty tags), continuous per-module numbering.
- **Correctness** — real TeX math only (`$…$`, `$$…$$`); every paper answer
  numerically verified in pure Python before solutions are written; balanced
  delimiters and resolving image links (gated by CI).

## Reference docs

- [docs/ROADMAP.md](docs/ROADMAP.md) — the full theory roadmap per module,
  with Mermaid diagrams
- [docs/JEE-ADVANCED-OLYMPIAD-COVERAGE.md](docs/JEE-ADVANCED-OLYMPIAD-COVERAGE.md) —
  detailed checklist proving coverage for every chapter
- [docs/FORMATTING-GUIDE.md](docs/FORMATTING-GUIDE.md) — formatting and
  pipeline conventions
- [docs/DIAGRAMS.md](docs/DIAGRAMS.md) — diagram catalog (decision tree,
  circular, Pascal, stars & bars, reflection, Young, Burnside, complex plane,
  conic reflection, …)

## Tooling

```bash
# Markdown notes — the daily gates:
python3 tools/verify-md.py                  # every notes/**/*.md must PASS
python3 tools/build-complete.py all         # regenerate <slug>-complete.md snapshots
git diff --exit-code -- 'notes/*-complete.md'

# legacy published maps — must never drift:
python3 tools/verify-math.py                # every *.html — all PASS
python3 tools/verify-mindmap.py all         # published-map integrity
python3 tools/build-mindmap.py all          # source-less maps are safe no-ops
```

`<slug>-complete.md` is the single-file snapshot of a module (course map →
chapters → paper → solutions); CI regenerates it and fails if it is stale.
The standalone maps in `published/` are frozen: CSS embedded, SVG IDs
namespaced, every node expandable, no links to deleted source pages.

## Planned modules (roadmap)

Ordered draft — **curation of the final list and order is on hold for review**.
Proposed folder slugs follow the naming rule in the notes standard
(kebab-case under `notes/`).

| # | Module | Proposed folder |
|---|---|---|
| 1 | Quadratic Equations | `notes/Quadratic-Equations/` |
| 2 | Inequalities | `notes/Inequalities/` |
| 3 | Trigonometry | `notes/Trigonometry/` |
| 4 | Sequences & Series | `notes/Sequences-and-Series/` |
| 5 | Limits & Continuity | `notes/Limits-and-Continuity/` |
| 6 | Differentiation | `notes/Differentiation/` |
| 7 | Applications of Derivatives | `notes/Applications-of-Derivatives/` |
| 8 | Integration | `notes/Integration/` |
| 9 | Differential Equations | `notes/Differential-Equations/` |
| 10 | Coordinate Geometry — Lines & Circles | `notes/Coordinate-Geometry-Lines-and-Circles/` |
| 11 | Conic Sections | `notes/Conic-Sections/` |
| 12 | 3D Geometry | `notes/3D-Geometry/` |
| 13 | Vectors | `notes/Vectors/` |
| 14 | Matrices & Determinants | `notes/Matrices-and-Determinants/` |
| 15 | Probability | `notes/Probability/` |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) (the notes standard) — module anatomy,
the scope ladder, callout/question/numbering rules, correctness and verify
commands. AI agents: read [AGENTS.md](AGENTS.md). When adding a module, follow
[templates/CHECKLIST.md](templates/CHECKLIST.md) end to end and open a PR —
do not push to `main`.
