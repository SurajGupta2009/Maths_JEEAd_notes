# Maths_JEEAd_notes

Hand-crafted, self-contained HTML study notes that walk a JEE aspirant from
board-level basics to JEE Advanced and Olympiad mathematics — every formula
*derived from reasoning*, every answer numerically verified. Each published
module is delivered as one standalone, expandable mindmap HTML containing its
complete theory, worked examples, practice questions, paper, solutions and
diagrams.

[![verify](https://img.shields.io/github/actions/workflow/status/SurajGupta2009/Maths_JEEAd_notes/verify.yml?branch=main&style=flat-square&label=verify)](https://github.com/SurajGupta2009/Maths_JEEAd_notes/actions/workflows/verify.yml)

## Modules

| Module | Status | Chapters | Practice Qs | Paper Qs | Standalone mindmap |
|---|---|---|---|---|---|
| **PnC** · Permutations & Combinations | ✅ complete | 6 | 47 (P1–P8 per chapter) | 40 (A–G + stretch) | [open map](PnC/pnc-mindmap.html) |
| **Complex Numbers** | ✅ complete | 6 | 50 (P1–P51, continuous) | 38 (A–H) | [open map](Complex%20Numbers/cn-mindmap.html) |
| **Binomial Theorem** | ✅ complete | 6 | 47 (P1–P47, continuous) | 38 (A–H) | [open map](Binomial-Theorem/binomial-theorem-mindmap.html) |
| **Conic Sections** | ✅ complete | 6 | 48 (P1–P48, continuous) | 38 (A–H) | [open map](Conic-Sections/conic-sections-mindmap.html) |

Each module’s published folder now contains only its final `*-mindmap.html`
deliverable (plus the local stylesheet kept for the generator’s source-backed
workflow). The map is lossless for course content: chapter introductions,
sections, subtopics, theory, diagrams, worked examples, every practice/paper
question, answer pills and full solutions are embedded as expandable nodes.
The reusable HTML templates remain in `templates/` for future modules; they are
not part of the published course folders.

## Planned modules (roadmap)

Ordered draft — **curation of the final list and order is on hold for review**.
Proposed folder slugs follow the naming rule (see [CONTRIBUTING.md](CONTRIBUTING.md)).

| # | Module | Proposed folder |
|---|---|---|
| 1 | Quadratic Equations | `Quadratic-Equations/` |
| 2 | Inequalities | `Inequalities/` |
| 3 | Trigonometry | `Trigonometry/` |
| 4 | Sequences & Series | `Sequences-and-Series/` |
| 5 | Limits & Continuity | `Limits-and-Continuity/` |
| 6 | Differentiation | `Differentiation/` |
| 7 | Applications of Derivatives | `Applications-of-Derivatives/` |
| 8 | Integration | `Integration/` |
| 9 | Differential Equations | `Differential-Equations/` |
| 10 | Coordinate Geometry — Lines & Circles | `Coordinate-Geometry-Lines-and-Circles/` |
| 11 | Conic Sections | `Conic-Sections/` |
| 12 | 3D Geometry | `3D-Geometry/` |
| 13 | Vectors | `Vectors/` |
| 14 | Matrices & Determinants | `Matrices-and-Determinants/` |
| 15 | Probability | `Probability/` |

## Quick start

No build step, no dependencies — open a final mindmap directly in a browser:

- `PnC/pnc-mindmap.html`
- `Complex Numbers/cn-mindmap.html`
- `Binomial-Theorem/binomial-theorem-mindmap.html`
- `Conic-Sections/conic-sections-mindmap.html`

Internet **is** required for the MathJax CDN (formulas render via jsdelivr;
everything else works offline). To check tooling: Python 3, stdlib only.

## Markdown notes (JEE Advanced + Olympiad, well-ordered)

All HTML mindmaps are also converted to **well-ordered Markdown** with proper formatting and diagrams:

```bash
python3 tools/convert_to_md.py all
```

Output in `Markdown/`:

- `Markdown/README.md` — index with coverage matrix
- `Markdown/ROADMAP.md` — basics → JEE Main → JEE Advanced → Olympiad roadmap with Mermaid diagrams
- `Markdown/FORMATTING-GUIDE.md` — conversion pipeline, math handling, diagram handling (SVG + Mermaid)
- `Markdown/DIAGRAMS.md` — 20+ diagrams catalog (decision tree, circular, Pascal, stars & bars, reflection, Young, Burnside, complex plane, conic reflection, etc.)
- `Markdown/JEE-ADVANCED-OLYMPIAD-COVERAGE.md` — detailed checklist proving coverage for every chapter
- `Markdown/<Module>/01-ch-1-...md` … `06-ch-6-...md` — 6 chapters per module, properly ordered
- `Markdown/<Module>/assets/fig-XX.svg` — preserved SVG diagrams
- `Markdown/<Module>/olympiad-paper.md` + `olympiad-paper-solutions.md` — 40 Q paper
- `Markdown/<Module>/*-complete.md` — single-file complete notes

Each markdown file uses:
- **Math**: `$...$` inline, `$$...$$` display (GitHub native MathJax)
- **Diagrams**: SVG `![](assets/fig-XX.svg)` + Mermaid ````mermaid` flowcharts
- **Callouts**: `> **⛁ First Principles**`, `> **💡 Key Idea**`, `> **⚠ Common Trap**`, `> **★ Olympiad Extension**`
- **Questions**: `#### **S1**[JEE Main][solved]` with collapsible `<details><summary>Answer + Reasoning</summary>`
- **Ordering**: Foundations → tools → applications → frontier, with dependencies respected, small-case verification, two-language translation (algebra ↔ geometry)

## Repo structure

```
Maths_JEEAd_notes/
├── .github/workflows/verify.yml    CI: MathJax/HTML + standalone mindmap checks
├── PnC/                            final Permutations & Combinations deliverable
│   ├── pnc-mindmap.html            one standalone expandable course file
│   └── assets/notes.css            local stylesheet retained for source-backed builds
├── Complex Numbers/                final Complex Numbers deliverable
│   ├── cn-mindmap.html             one standalone expandable course file
│   └── assets/notes.css
├── Binomial-Theorem/               final Binomial Theorem deliverable
│   ├── binomial-theorem-mindmap.html
│   └── assets/notes.css
├── Conic-Sections/                 final Conic Sections deliverable
│   ├── conic-sections-mindmap.html
│   └── assets/notes.css
├── templates/                      reusable skeletons for future source-backed modules
├── tools/
│   ├── build-mindmap.py            builder + safe no-op for published source-less maps
│   ├── verify-mindmap.py           completeness/source-less standalone-map checks
│   ├── verify-math.py              HTML tag + MathJax delimiter quality gate
│   └── mindmap-overrides.json      per-module label pins & CLI aliases
└── README.md · CONTRIBUTING.md · AGENTS.md · .gitignore
```

## Tooling

```bash
# source-backed builds (or safe no-op after publishing the final maps):
python3 tools/build-mindmap.py PnC
python3 tools/build-mindmap.py cn          # alias for 'Complex Numbers'
python3 tools/build-mindmap.py all

# quality gate — HTML tag balance + MathJax delimiter balance, every file must PASS:
python3 tools/verify-math.py

# source-backed completeness, or standalone-map integrity after source removal:
python3 tools/verify-mindmap.py all
```

Mind maps are generated from the source pages before publication and are then
self-contained: CSS is embedded, SVG IDs are namespaced, page links become
in-map anchors, all chapter/page headers are preserved, and the final folder
has no links to deleted source pages. The builder refuses to overwrite a
source-less final map, so `build-mindmap.py all` remains idempotent.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) (humans) or [AGENTS.md](AGENTS.md)
(AI agents) — both state the file-layout rules, the exact MathJax head, the
question/box markup, the numbering rules, and the verify commands. Follow
[templates/CHECKLIST.md](templates/CHECKLIST.md) when adding a module.
